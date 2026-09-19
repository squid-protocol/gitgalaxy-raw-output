# ARCHITECTURAL_BRIEF: cobrix
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AbsaOSS/cobrix.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 645 analyzed artifact(s), 49284 LOC.
- **Load-bearing artifact:** `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/base/SparkTestBase.scala` -- 85 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` -- pulls in 33 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` at magnitude 2277.46 (structural weight, not risk).
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
| Total Artifacts | 705 |
| Analyzed Artifacts (Scanned) | 645 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 60 |
| Total LOC | 49284 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 91.5% |
| Dominant Lang | SCALA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.578 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2967 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3926 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SCALA | 449 | 36831 | 69.6% |
| PLAINTEXT | 77 | 276 | 11.9% |
| JSON | 39 | 5922 | 6.0% |
| COBOL | 35 | 1215 | 5.4% |
| XML | 18 | 0 | 2.8% |
| JAVA | 8 | 4939 | 1.2% |
| BINARY_THREAT | 6 | 6 | 0.9% |
| MARKDOWN | 5 | 0 | 0.8% |
| CSV | 4 | 41 | 0.6% |
| SHELL | 2 | 13 | 0.3% |
| GROOVY | 1 | 26 | 0.2% |
| REXX | 1 | 15 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `3.76`
> **Composition Archetype:** `Hub-Coupled App` (z +3.76; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Declarative / Non-Code 28%, State Mutators Files 9%, Large Core Modules 7%, Generic / Templated Code Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 548 | 85.0% |
| Unknown | 6 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 76 | 11.8% |
| Static: Minified & Vendor Opaque Mass | 15 | 2.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 60*

**Composition by Extension & Reason:**
- `.dat`: 28x Excluded (Unsupported Extension: '.dat')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.g4`: 3x Unsupported Format (.g4)
- `.java`: 1x Excluded (Embedded Hex Payload: 20472 hex tokens in 1352 LOC), 1x Excluded (Embedded Hex Payload: 15144 hex tokens in 985 LOC), 1x Excluded (Embedded Hex Payload: 29256 hex tokens in 999 LOC)
- `.plot`: 3x Excluded (Unsupported Extension: '.plot')
- `.scala`: 1x Excluded (Embedded Hex Payload: 2080 hex tokens in 912 LOC), 1x Excluded (Embedded Hex Payload: 723 hex tokens in 567 LOC)
- `.json`: 2x Excluded (Static Asset Blob without Intent: 2350 LOC)
- `.gz`: 2x Excluded (Explicitly Denied Extension: '.gz')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bz2`: 1x Excluded (Explicitly Denied Extension: '.bz2')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.4 | 8.4 | 4.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 26.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 43.1 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 44.8 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.0 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 84.1 | 5.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 32.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3667 | 164 | 5 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` |
| cleanup | 96 | 51 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/IndexBuilder.scala` |
| guards | 3399 | 250 | 13 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` |
| danger | 1940 | 221 | 7 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` |
| concurrency | 12 | 3 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/LRUCache.scala` |
| connectivity | 1664 | 279 | 4 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` |
| io | 314 | 109 | 1 | `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test5MultisegmentSpec.scala` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 2 | 0 | `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/streaming/FileStreamerSpec.scala` |
| serialization | 4 | 4 | 0 | `data/test24_copybook.cob` |
| regex | 4 | 2 | 0 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` |
| events | 91 | 33 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/IndexBuilder.scala` |
| tests | 2819 | 155 | 12 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` |
| docs | 684 | 211 | 2 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` |
| debt | 179 | 26 | 0 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` |
| mutation | 10320 | 412 | 40 | `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen6TypeVariety.scala` |
| dead_code | 416 | 142 | 1 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` |
| credential | 0 | 0 | 0 | - |
| threat | 203 | 99 | 1 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/utils/UsingUtilsSuite.scala` |
| ml_ai | 24 | 15 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/IndexBuilder.scala` |
| ui | 2 | 2 | 0 | `build.sbt` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test5MultisegmentSpec.scala` (Hits: 23)
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test24DebugModeSpec.scala` (Hits: 14)
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test6TypeVarietySpec.scala` (Hits: 14)

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

- `extractRecord` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> Impact: **228.9** | LOC: 165
  * *Intent:* * All other segment redefines will be skipped. */
- `extractHierarchicalRecord` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> Impact: **221.8** | LOC: 195
  * *Intent:* */
- `validateSparkCobolOptions` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala`) -> Impact: **201.8** | LOC: 235
  * *Intent:* /** * Validates if all options passed to 'spark-cobol' are recognized. * */
- `sparseIndexGenerator` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala`) -> Impact: **130.2** | LOC: 110
- `pic` **(Compute Cores)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> Impact: **119.2** | LOC: 184
- `decodeEbcdicNumber` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala`) -> Impact: **118.2** | LOC: 62
  * *Intent:* * A decoder for any EBCDIC uncompressed numbers supporting * <ul> * <li> Separate leading and trailing sign</li> * <li> Sign punched into the number</...
- `getIntegralDecoder` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala`) -> Impact: **88.1** | LOC: 62
  * *Intent:* /** Gets a decoder function for an integral data type. A direct conversion from array of bytes to the target type is used where possible. */
- `getBytesCount` **(Compute Cores)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryUtils.scala`) -> Impact: **82.3** | LOC: 29
- `encodeBCDNumber` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/BCDNumberEncoders.scala`) -> Impact: **77.5** | LOC: 69
  * *Intent:* * * Output length (bytes): * - With mandatory sign nibble (signed or unsigned): ceil((precision + 1) / 2) * - Unsigned without sign nibble: ceil(preci...
- `putEncodedNumStrToArray` **(Many-Argument Workhorses)** (@ `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala`) -> Impact: **71.5** | LOC: 59
  * *Intent:* /** * Puts an arbitrary number represented as a string into a byte array according to provided encoding. * The resulting bytes are inserted into an ar...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr` | 15 | 3774.28 | 11.59% | 52.38% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders` | 9 | 1409.18 | 24.28% | 41.52% |
| `data/test2_data` | 2 | 1000.0 | 0.0% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record` | 3 | 914.36 | 25.81% | 3.77% |
| `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils` | 8 | 776.58 | 6.93% | 1.11% |
| `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration` | 45 | 774.66 | 6.65% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters` | 9 | 738.2 | 7.07% | 0.0% |
| `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators` | 15 | 716.84 | 30.55% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform` | 10 | 711.68 | 24.04% | 53.11% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw` | 11 | 602.64 | 29.08% | 13.64% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserVisitor.java` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonBaseVisitor.java` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonVisitor.java` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryNumberDecoders.scala` -> **99.9997%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextFullRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/stream/SimpleMemoryStream.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/AutoCloseableSpy.scala` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` -> **6** Orphaned Functions | **120** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` -> **55** Orphaned Functions | **0** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserVisitor.java` -> **55** Orphaned Functions | **0** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryNumberDecoders.scala` -> **19** Orphaned Functions | **0** Duplicates
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` -> **13** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2284` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2277.46 | **LOC:** 3481 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.069; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.4%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pic` **(Compute Cores)** (Impact: 119.2)
  * `group` **(Compute Cores)** (Impact: 53.1)
  * `identifier` **(I/O & Config Routines)** (Impact: 38.1)
  * `specialValues` **(I/O & Config Routines)** (Impact: 38.0)
  * `precision9` **(I/O & Config Routines)** (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 617`, `structural_boundaries: 955`, `args: 447`, `func_start: 447`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 126`, `duplicate_logic: 120`, `unreferenced_by_name: 6`
* *Architecture:* `api: 512`, `import: 4`
* *Defense:* `safety: 178`, `doc: 1`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001553
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Iterator, java.util.List, org.antlr.v4.runtime.*, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.dfa.DFA, org.antlr.v4.runtime.misc.*, org.antlr.v4.runtime.tree.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 872.76 | **LOC:** 555 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **15**; blast radius 2.718; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 63.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extractRecord` **(Many-Argument Workhorses)** (Impact: 228.9)
    * *Intent:* * All other segment redefines will be skipped. */
  * `extractHierarchicalRecord` **(Many-Argument Workhorses)** (Impact: 221.8)
    * *Intent:* */
  * `applyRecordPostProcessing` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* */
  * `extractArray` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `extractArray` **(Compute Cores)** (Impact: 37.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 27`, `args: 43`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 52`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `import: 11`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.718
  * `Choke Point (Betweenness):` 0.000265 | `Ripple Effect (Closeness):` 0.01457
  * `Imports (Out-Degree: 7):` COMP4, ListBuffer, Primitive, Statement, scala.collection.mutable, scala.collection.mutable.ArrayBuffer, scala.reflect.ClassTag, za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 646.3 | **LOC:** 880 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 1.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.0%), Connectivity (formerly Api Exposure) (63.3%), Complexity Load (formerly Cognitive Load) (21.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromNumericZPicRegexDecimalScaled` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `checkBounds` **(Compute Cores)** (Impact: 52.0)
  * `visitPrimitive` **(Defensive Guards)** (Impact: 45.0)
  * `replaceUsage` **(Compute Cores)** (Impact: 43.2)
  * `fromNumericSPicRegexDecimalScaled` **(Many-Argument Workhorses)** (Impact: 42.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 78`, `args: 121`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 7`
* *Architecture:* `io: 1`, `api: 46`, `import: 18`
* *Defense:* `safety: 9`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.069
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.001553
  * `Imports (Out-Degree: 11):` Position, Primitive, Right, RuleContext, java.nio.charset.Charset, org.antlr.v4.runtime.ParserRuleContext, scala.collection.JavaConverters._, scala.collection.mutable...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 605.32 | **LOC:** 1069 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 92.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **15**; blast radius 2.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.9%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateSparkCobolOptions` **(Many-Argument Workhorses)** (Impact: 201.8)
    * *Intent:* /** * Validates if all options passed to 'spark-cobol' are recognized. * */
  * `parseVariableLengthParameters` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `getIsEbcdic` **(Compute Cores)** (Impact: 25.4)
  * `parse` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `parseBdw` **(Stateful Encapsulated Methods)** (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 111`, `args: 57`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 37`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.147
  * `Choke Point (Betweenness):` 0.00043 | `Ripple Effect (Closeness):` 0.020649
  * `Imports (Out-Degree: 8):` scala.collection.mutable, scala.collection.mutable.ListBuffer, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.CopybookParser, za.co.absa.cobrix.cobol.parser.antlr.ParserJson, za.co.absa.cobrix.cobol.parser.decoders.FloatingPointFormat, za.co.absa.cobrix.cobol.parser.decoders.FloatingPointFormat.FloatingPointFormat...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 587.52 | **LOC:** 599 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **18**; blast radius 9.18; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.3%), Guard Balance (formerly Safety Score) (82.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.7692% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyMetadata` **(Many-Argument Workhorses)** (Impact: 67.1)
    * *Intent:* /** * Copies metadata from one schema to another as long as names and data types are the same. * */
  * `flattenSchema` **(Callbacks & Closures)** (Impact: 56.2)
    * *Intent:* /** * Given an instance of DataFrame returns a dataframe with flattened schema. * All nested structu...
  * `splitFieldPath` **(Stateful Encapsulated Methods)** (Impact: 24.8)
  * `getField` **(Callbacks & Closures)** (Impact: 24.1)
    * *Intent:* /** * Get a Spark field from a text path and a given schema * (originally implemented here: https://...
  * `processArray` **(Generic / Templated Code)** (Impact: 22.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 26`, `args: 108`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 24`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 32`, `import: 14`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.18
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.057065
  * `Imports (Out-Degree: 1):` DataFrame, Path, Row, SparkSession, com.fasterxml.jackson.databind.ObjectMapper, org.apache.hadoop.fs.FileSystem, org.apache.spark.SparkContext, org.apache.spark.sql.Column...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 510.54 | **LOC:** 480 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.985; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.8%), Complexity Load (formerly Cognitive Load) (40.7%), Connectivity (formerly Api Exposure) (10.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `putEncodedNumStrToArray` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* /** * Puts an arbitrary number represented as a string into a byte array according to provided encod...
  * `encodeUncompressed` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* /** * Encodes a number according to the rules of uncompressed (DISPLAY) COBOL EBCDIC format. Returns...
  * `encodeBcd` **(Type Conversions)** (Impact: 20.5)
    * *Intent:* /** * Encodes an arbitrary number in BCD format. * Returns the corresponding array of bytes. */
  * `putDecimalToArray` **(Many-Argument Workhorses)** (Impact: 15.7)
    * *Intent:* /** * Puts a 64 bit little-endian decimal number defined by integral and fracture parts to a byte ar...
  * `strToBigArray` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* /** * Encodes an arbitrary big integer in a big-endian binary (COMP) format. * Returns the correspon...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 9`, `args: 35`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `unreferenced_by_name: 13`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 8`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` scala.util.Random, scodec.Attempt.Successful, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.decoders.BinaryUtils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test15_data/a/example.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test15_data/b/example.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test1_data/example.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test2_data/example.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test2_data/example2.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/example_data/raw_data/file1.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 424.12 | **LOC:** 429 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 1.089; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.9%), Connectivity (formerly Api Exposure) (49.6%), Complexity Load (formerly Cognitive Load) (46.7%)
- **Documentation Coverage:** 7.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeEbcdicNumber` **(Many-Argument Workhorses)** (Impact: 118.2)
    * *Intent:* * A decoder for any EBCDIC uncompressed numbers supporting * <ul> * <li> Separate leading and traili...
  * `decodeAsciiNumber` **(Many-Argument Workhorses)** (Impact: 71.4)
    * *Intent:* /** * A decoder for any ASCII uncompressed numbers supporting leading and trailing sign * */
  * `decodeAsciiString` **(Compute Cores)** (Impact: 33.2)
    * *Intent:* /** * A decoder for any ASCII string fields (alphabetical or any char) * */
  * `decodeUtf16String` **(Many-Argument Workhorses)** (Impact: 27.8)
    * *Intent:* /** * A decoder for any UTF-16 string field * */
  * `decodeEbcdicString` **(Compute Cores)** (Impact: 25.4)
    * *Intent:* /** * A decoder for any EBCDIC string fields (alphabetical or any char) * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 35`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 27`
* *Architecture:* `io: 1`, `api: 13`, `import: 6`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.089
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.001553
  * `Imports (Out-Degree: 2):` Constants._, StringTools._, java.nio.charset.StandardCharsets, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.encoding.codepage.CodePage
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 347.9 | **LOC:** 480 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **10**; blast radius 7.688; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.8%)
- **Documentation Coverage:** 38.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFieldByName` **(Generic / Templated Code)** (Impact: 42.2)
    * *Intent:* /** * Get the AST object of a field by name. * * Nested field names can contain '.' to identify the ...
  * `setPrimitiveField` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* /** * Set value of a field of the copybook record by the AST object of the field * * Nested field na...
  * `merge` **(Callbacks & Closures)** (Impact: 34.3)
  * `generateGroupLayoutPositions` **(Compute Cores)** (Impact: 26.2)
  * `dropFillers` **(Compute Cores)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 60`, `args: 58`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 4`, `dead_code: 1`
* *Architecture:* `api: 29`, `import: 8`
* *Defense:* `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.688
  * `Choke Point (Betweenness):` 0.00164 | `Ripple Effect (Closeness):` 0.066336
  * `Imports (Out-Degree: 5):` Copybook._, Primitive, Statement, java.util.concurrent.ConcurrentHashMap, scala.collection.mutable, scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 341.24 | **LOC:** 354 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **15**; blast radius 2.498; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.3%), Complexity Load (formerly Cognitive Load) (21.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getIntegralDecoder` **(Many-Argument Workhorses)** (Impact: 88.1)
    * *Intent:* /** Gets a decoder function for an integral data type. A direct conversion from array of bytes to th...
  * `getBinaryEncodedIntegralDecoder` **(Stateful Encapsulated Methods)** (Impact: 65.5)
    * *Intent:* /** Gets a decoder function for a binary encoded integral data type. A direct conversion from array ...
  * `getDecimalDecoder` **(Many-Argument Workhorses)** (Impact: 56.4)
    * *Intent:* /** Gets a decoder function for a decimal data type. The input array of bytes is always converted to...
  * `getDecoder` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* * <li> Integral types are represented as boxed integers and longs. Larger integral numbers are repre...
  * `getStringDecoder` **(Stateful Encapsulated Methods)** (Impact: 25.0)
    * *Intent:* /** Gets a decoder function for a string data type. Decoder is chosed depending on whether input enc...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 34`, `args: 92`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`
* *Architecture:* `io: 1`, `api: 1`, `import: 13`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.498
  * `Choke Point (Betweenness):` 0.000575 | `Ripple Effect (Closeness):` 0.066943
  * `Imports (Out-Degree: 6):` CodePageCommon, FloatingPointFormat._, StandardCharsets, java.nio.charset.Charset, maxLongPrecision, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.parser.ast.datatype._, za.co.absa.cobrix.cobol.parser.common.Constants...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 331.92 | **LOC:** 516 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.985; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (71.0%), Guard Balance (formerly Safety Score) (67.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `value` **(I/O & Config Routines)** (Impact: 21.9)
  * `obj` **(I/O & Config Routines)** (Impact: 9.8)
  * `arr` **(I/O & Config Routines)** (Impact: 9.8)
  * `accept` **(Generic / Templated Code)** (Impact: 7.3)
  * `accept` **(Generic / Templated Code)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 157`, `args: 56`, `func_start: 56`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 27`, `duplicate_logic: 4`, `unreferenced_by_name: 6`
* *Architecture:* `api: 75`, `import: 4`
* *Defense:* `safety: 26`, `doc: 1`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.Iterator, java.util.List, org.antlr.v4.runtime.*, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.dfa.DFA, org.antlr.v4.runtime.misc.*, org.antlr.v4.runtime.tree.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/writer/NestedRecordCombiner.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 268.38 | **LOC:** 476 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.985; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeToBytes` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* * * For array fields (both primitive and group-of-primitives) each element is written * using the `f...
  * `buildGroupNode` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* /** * Builds a [[WriterAst]] node for a group copybook field. For groups with OCCURS the getter * ex...
  * `buildPrimitiveNode` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* /** * Builds a [[WriterAst]] node for a primitive copybook field, using the field's index in the * s...
  * `combine` **(Many-Argument Workhorses)** (Impact: 25.6)
    * *Intent:* /** * Converts Spark DataFrame to the RDD with data in mainframe format as arrays of bytes, each arr...
  * `processRDD` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* * For variable-length records with OCCURS DEPENDING ON, the output may be trimmed to the actual byte...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 42`, `args: 46`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Integral, NestedRecordCombiner._, Primitive, Row, StructType, org.apache.spark.rdd.RDD, org.apache.spark.sql.DataFrame, org.apache.spark.sql.types.ArrayType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/DisplayEncoders.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 252.46 | **LOC:** 213 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.985; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (65.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encodeDisplayNumberSignSeparate` **(Many-Argument Workhorses)** (Impact: 67.9)
  * `encodeDisplayNumberSignOverpunched` **(Many-Argument Workhorses)** (Impact: 62.1)
  * `setPaddedEbcdicNumberWithSignSeparate` **(Many-Argument Workhorses)** (Impact: 50.7)
  * `setPaddedEbcdicNumberWithSignOverpunched` **(Many-Argument Workhorses)** (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.math.RoundingMode, za.co.absa.cobrix.cobol.parser.position.Position
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryUtils.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 225.24 | **LOC:** 249 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 2.845; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.0%), Mutation Surface (formerly State Flux) (54.2%), Connectivity (formerly Api Exposure) (34.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBytesCount` **(Compute Cores)** (Impact: 82.3)
  * `decodeBinaryNumber` **(Many-Argument Workhorses)** (Impact: 57.9)
    * *Intent:* /** A generic decoder for 2s compliment binary numbers aka COMP * */
  * `addDecimalPoint` **(Many-Argument Workhorses)** (Impact: 44.2)
    * *Intent:* /** Transforms a string representation of an integer to a string representation of decimal * by addi...
  * `decodeString` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* /** A decoder for any string fields (alphabetical or any char) * */
  * `ebcdicToAscii` **(State Mutators)** (Impact: 1.5)
    * *Intent:* /** Convert an EBCDIC character to ASCII */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 14`, `args: 39`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.845
  * `Choke Point (Betweenness):` 0.000125 | `Ripple Effect (Closeness):` 0.067805
  * `Imports (Out-Degree: 2):` Constants._, Encoding, za.co.absa.cobrix.cobol.parser.ast.datatype._, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.encoding.EBCDIC
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen6TypeVariety.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 217.86 | **LOC:** 575 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.985; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.7%), Complexity Load (formerly Cognitive Load) (53.7%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 7.7)
  * `getVeryBigNumber` **(State Mutators)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 197`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 3`
* *Defense:* `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FileOutputStream, com.example.spark.cobol.examples.parser.generators.utils.GeneratorTools._, java.io.BufferedOutputStream, scala.util.Random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/schema/CobolSchema.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 217.04 | **LOC:** 444 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **27**; blast radius 3.973; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.4%), Connectivity (formerly Api Exposure) (28.5%), Mutation Surface (formerly State Flux) (25.8%)
- **Documentation Coverage:** 88.0952% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parsePrimitive` **(Compute Cores)** (Impact: 54.8)
  * `createSparkSchema` **(I/O & Config Routines)** (Impact: 24.4)
  * `parseGroup` **(Stateful Encapsulated Methods)** (Impact: 22.5)
  * `builder` **(Stateful Encapsulated Methods)** (Impact: 11.6)
  * `addExtendedPrimitiveMetadata` **(Stateful Encapsulated Methods)** (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 34`, `args: 56`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`
* *Architecture:* `api: 16`, `import: 16`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.973
  * `Choke Point (Betweenness):` 0.000742 | `Ripple Effect (Closeness):` 0.017469
  * `Imports (Out-Degree: 11):` COMP1, COMP2, COMP4, COMP5, COMP9, CorruptFieldsPolicy, Decimal, Integral...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 189.46 | **LOC:** 171 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 1.332; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sparseIndexGenerator` **(Many-Argument Workhorses)** (Impact: 130.2)
  * `getSplitCondition` **(Stateful Encapsulated Methods)** (Impact: 5.9)
    * *Intent:* /** Returns a predicate that returns true when current index entry has reached the required size */
  * `getSegmentId` **(Encapsulated Accessors)** (Impact: 5.4)
  * `isSegmentGoodForSplit` **(Encapsulated Accessors)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 15`, `args: 9`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 7.7e-05 | `Ripple Effect (Closeness):` 0.007226
  * `Imports (Out-Degree: 8):` scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.Copybook, za.co.absa.cobrix.cobol.parser.ast.Primitive, za.co.absa.cobrix.cobol.parser.headerparsers.RecordHeaderParser, za.co.absa.cobrix.cobol.reader.common.Constants, za.co.absa.cobrix.cobol.reader.extractors.raw.RawRecordExtractor, za.co.absa.cobrix.cobol.reader.index.entry.SparseIndexEntry...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 166.5 | **LOC:** 292 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 1.297; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.3%), Connectivity (formerly Api Exposure) (19.3%), Complexity Load (formerly Cognitive Load) (17.5%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `recordExtractor` **(Compute Cores)** (Impact: 57.8)
  * `generateIndex` **(Many-Argument Workhorses)** (Impact: 43.3)
    * *Intent:* /** * Traverses the data sequentially as fast as possible to generate record index. * This index wil...
  * `getRecordIterator` **(Many-Argument Workhorses)** (Impact: 11.4)
  * `getRootSegmentId` **(Stateful Encapsulated Methods)** (Impact: 10.5)
  * `getRecordHeaderParser` **(Stateful Encapsulated Methods)** (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 37`, `args: 25`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`
* *Architecture:* `api: 7`, `import: 15`
* *Defense:* `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.297
  * `Choke Point (Betweenness):` 0.000396 | `Ripple Effect (Closeness):` 0.005072
  * `Imports (Out-Degree: 13):` FixedLength, RecordHeaderParserFactory, VarLenNestedIterator, VariableBlock, VariableLength, scala.collection.mutable.ArrayBuffer, scala.reflect.ClassTag, za.co.absa.cobrix.cobol.internal.Logging...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/stream/SimpleMemoryStream.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 161.36 | **LOC:** 191 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.403; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (41.4%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `searchOutOfLookbackBuffer` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* /** Searches the sequence of bytes outsize of the lookback buffer. Returns the index of the beginnin...
  * `search` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* /** Searches the stream for the specified sequence of bytes. Returns the index of the beginning of t...
  * `getBytes` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* /* Gets the specific number of bytes starting from specific index. Returns the number of bytes read ...
  * `AddBytesToLookbackBuffer` **(Stateful Encapsulated Methods)** (Impact: 14.0)
    * *Intent:* /** Adds bytes to the lookback buffer */
  * `extractOutOfLoobackBufferBytes` **(Stateful Encapsulated Methods)** (Impact: 12.1)
    * *Intent:* /** Extracts the values ahead of the lookback buffer and shifts the lookback buffer accordingly */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 3`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001553
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/EncoderSelector.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 157.84 | **LOC:** 150 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 2.363; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (92.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (32.8%), Complexity Load (formerly Cognitive Load) (25.3%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getEncoder` **(Generic / Templated Code)** (Impact: 51.5)
  * `getBdcEncoder` **(Callbacks & Closures)** (Impact: 30.4)
  * `getDisplayEncoder` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `getBinaryEncoder` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `getStringEncoder` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* /** Gets an encoder function for a string data type. The encoder is chosen depending on whether the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 26`, `args: 46`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`
* *Architecture:* `io: 1`, `api: 4`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.363
  * `Choke Point (Betweenness):` 0.000186 | `Ripple Effect (Closeness):` 0.066427
  * `Imports (Out-Degree: 9):` COMP3, COMP3U, COMP4, COMP9, CobolType, CodePageCommon, Decimal, Integral...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` -> Churn: **60.06%** | Cog Load: 71.81% | Debt: 11.3016%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 646.3
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` -> **Ruslan Iushchenko** (92.3% isolated ownership) | Magnitude: 605.32
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 587.52
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 424.12
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 347.9

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` -> **Severity: 0.074** (Bridge: 0.0033 * Flux: 22.6604%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` -> **Severity: 0.053** (Bridge: 0.003 * Flux: 17.886%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/RawRecordContext.scala` -> **Severity: 0.053** (Bridge: 0.0009 * Flux: 57.5103%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **Severity: 0.048** (Bridge: 0.0016 * Flux: 29.3968%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` -> **Severity: 0.04** (Bridge: 0.0004 * Flux: 93.457%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 10.053** (Embedded: 0.1404 * Error Risk: 71.6205%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` -> **Severity: 6.673** (Embedded: 0.0971 * Error Risk: 68.7243%)
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/FileUtils.scala` -> **Severity: 6.396** (Embedded: 0.0895 * Error Risk: 71.4415%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/EncoderSelector.scala` -> **Severity: 6.132** (Embedded: 0.0664 * Error Risk: 92.3049%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Group.scala` -> **Severity: 5.829** (Embedded: 0.1037 * Error Risk: 56.2017%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 2890.5** (Blast Radius: 38.54 * Doc Risk: 75.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/datatype/Usage.scala` -> **Severity: 1380.9** (Blast Radius: 13.809 * Doc Risk: 100.0%)
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/FileUtils.scala` -> **Severity: 1051.885** (Blast Radius: 24.544 * Doc Risk: 42.8571%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/stream/SimpleStream.scala` -> **Severity: 997.8** (Blast Radius: 9.978 * Doc Risk: 100.0%)
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/fixtures/BinaryFileFixture.scala` -> **Severity: 928.44** (Blast Radius: 15.474 * Doc Risk: 60.0%)

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
