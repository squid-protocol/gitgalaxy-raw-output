# ARCHITECTURAL_BRIEF: cobrix
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AbsaOSS/cobrix.git` |
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
- **Scope:** 629 analyzed artifact(s), 43540 LOC.
- **Load-bearing artifact:** `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/base/SparkTestBase.scala` -- 85 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` -- pulls in 33 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` at magnitude 872.76 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 629 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 76 |
| Total LOC | 43540 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 89.2% |
| Dominant Lang | SCALA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5894 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2799 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8138 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 32 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SCALA | 445 | 36647 | 70.7% |
| PLAINTEXT | 77 | 276 | 12.2% |
| JSON | 39 | 5922 | 6.2% |
| COBOL | 31 | 442 | 4.9% |
| XML | 18 | 0 | 2.9% |
| MARKDOWN | 8 | 0 | 1.3% |
| YAML | 4 | 167 | 0.6% |
| CSV | 4 | 41 | 0.6% |
| GROOVY | 1 | 26 | 0.2% |
| SHELL | 1 | 4 | 0.2% |
| REXX | 1 | 15 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 629 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 31%, Declarative / Non-Code 28%, State Mutators Files 8%, Large Core Modules 7%, Generic / Templated Code Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 535 | 85.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 79 | 12.6% |
| Static: Minified & Vendor Opaque Mass | 15 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 76*

**Composition by Extension & Reason:**
- `.dat`: 28x Excluded (Unsupported Extension: '.dat')
- `.java`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 20472 hex tokens in 1352 LOC), 1x Excluded (Embedded Hex Payload: 15144 hex tokens in 985 LOC)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.scala`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 723 hex tokens in 567 LOC)
- `.bin`: 6x Excluded (Unsupported Extension: '.bin')
- `.g4`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.plot`: 3x Excluded (Unsupported Extension: '.plot')
- `.cob`: 3x Zero-Density Threshold (LOC: 200, Signals: 0)
- `.json`: 2x Excluded (Static Asset Blob without Intent: 2350 LOC)
- `.gz`: 2x Excluded (Explicitly Denied Extension: '.gz')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bz2`: 1x Excluded (Explicitly Denied Extension: '.bz2')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.4 | 7.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.2 | 23.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 43.1 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 44.8 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.9 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 73.4 | 5.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 32.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3738 | 162 | 6 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` |
| cleanup | 96 | 51 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/IndexBuilder.scala` |
| guards | 3302 | 247 | 13 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` |
| danger | 1645 | 214 | 6 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` |
| concurrency | 13 | 4 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/LRUCache.scala` |
| connectivity | 903 | 270 | 4 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` |
| io | 308 | 107 | 1 | `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test5MultisegmentSpec.scala` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 2 | 0 | `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/streaming/FileStreamerSpec.scala` |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` |
| events | 90 | 32 | 0 | `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/IndexBuilder.scala` |
| tests | 3038 | 155 | 12 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` |
| docs | 536 | 203 | 2 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Statement.scala` |
| debt | 59 | 24 | 0 | `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/writer/FixedLengthEbcdicWriterSuite.scala` |
| mutation | 9976 | 400 | 39 | `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen6TypeVariety.scala` |
| dead_code | 246 | 131 | 1 | `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryNumberDecoders.scala` |
| credential | 8 | 1 | 0 | `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecodersSpec.scala` |
| threat | 13 | 5 | 0 | `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/model/CommonLists.scala` |
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
2. **CopybookParser.scala** (`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala`) — 69 inbound connections
3. **BinaryFileFixture.scala** (`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/fixtures/BinaryFileFixture.scala`) — 57 inbound connections
4. **Group.scala** (`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Group.scala`) — 41 inbound connections
5. **SparkUtils.scala** (`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala`) — 36 inbound connections

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
- `validateSparkCobolOptions` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala`) -> Impact: **197.8** | LOC: 235
  * *Intent:* /** * Validates if all options passed to 'spark-cobol' are recognized. * */
- `sparseIndexGenerator` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala`) -> Impact: **126.7** | LOC: 110
- `decodeEbcdicNumber` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala`) -> Impact: **118.2** | LOC: 62
  * *Intent:* * A decoder for any EBCDIC uncompressed numbers supporting * <ul> * <li> Separate leading and trailing sign</li> * <li> Sign punched into the number</...
- `getIntegralDecoder` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala`) -> Impact: **83.6** | LOC: 62
  * *Intent:* /** Gets a decoder function for an integral data type. A direct conversion from array of bytes to the target type is used where possible. */
- `getBytesCount` **(Compute Cores)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryUtils.scala`) -> Impact: **82.3** | LOC: 29
- `encodeBCDNumber` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/BCDNumberEncoders.scala`) -> Impact: **77.5** | LOC: 69
  * *Intent:* * * Output length (bytes): * - With mandatory sign nibble (signed or unsigned): ceil((precision + 1) / 2) * - Unsigned without sign nibble: ceil(preci...
- `putEncodedNumStrToArray` **(Many-Argument Workhorses)** (@ `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala`) -> Impact: **71.5** | LOC: 59
  * *Intent:* /** * Puts an arbitrary number represented as a string into a byte array according to provided encoding. * The resulting bytes are inserted into an ar...
- `writeToBytes` **(Many-Argument Workhorses)** (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/writer/NestedRecordCombiner.scala`) -> Impact: **71.5** | LOC: 108
  * *Intent:* * * For array fields (both primitive and group-of-primitives) each element is written * using the `fieldStartOffsetOverride` parameter so the exact by...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders` | 9 | 1399.08 | 24.7% | 39.4% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record` | 3 | 914.36 | 25.81% | 3.56% |
| `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils` | 8 | 769.68 | 6.83% | 1.06% |
| `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators` | 15 | 716.84 | 30.55% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters` | 9 | 710.9 | 6.9% | 0.0% |
| `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration` | 45 | 707.66 | 3.68% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform` | 10 | 697.48 | 23.7% | 47.42% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw` | 11 | 600.24 | 28.97% | 10.3% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding` | 5 | 589.16 | 46.32% | 18.38% |
| `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils` | 1 | 510.54 | 40.73% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryNumberDecoders.scala` -> **99.9996%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala` -> **99.9925%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringTools.scala` -> **99.593%** Exposure
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/builder/SparkCobolOptionsBuilder.scala` -> **99.0462%** Exposure
- `.github/workflows/jacoco_check.yml` -> **98.4733%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextFullRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/stream/SimpleMemoryStream.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/AutoCloseableSpy.scala` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryNumberDecoders.scala` -> **19** Orphaned Functions | **0** Duplicates
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` -> **13** Orphaned Functions | **0** Duplicates
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` -> **7** Orphaned Functions | **0** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/FloatingPointDecoders.scala` -> **6** Orphaned Functions | **0** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala` -> **6** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `2219` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 14.878)
- **Top Global Matches:** file_cluster_3: 14.878, file_cluster_8: 20.254, file_cluster_6: 31.446
- **Magnitude:** 872.76 | **LOC:** 555 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **15**; blast radius 2.587; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (71.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.587
  * `Choke Point (Betweenness):` 0.000765 | `Ripple Effect (Closeness):` 0.020435
  * `Imports (Out-Degree: 11):` scala.collection.mutable, scala.collection.mutable.ArrayBuffer, scala.collection.mutable.ListBuffer, scala.reflect.ClassTag, za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST, za.co.absa.cobrix.cobol.parser.ast.Group, za.co.absa.cobrix.cobol.parser.ast.Primitive, za.co.absa.cobrix.cobol.parser.ast.Statement...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.006)
- **Top Global Matches:** file_cluster_4: 12.006, file_cluster_5: 13.529, file_cluster_6: 14.06
- **Magnitude:** 584.02 | **LOC:** 599 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **18**; blast radius 8.79; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%)
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
* *Structure:* `branch: 140`, `structural_boundaries: 26`, `args: 108`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 24`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 32`, `import: 14`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.79
  * `Choke Point (Betweenness):` 0.000326 | `Ripple Effect (Closeness):` 0.057365
  * `Imports (Out-Degree: 4):` com.fasterxml.jackson.databind.ObjectMapper, org.apache.hadoop.fs.FileSystem, org.apache.hadoop.fs.Path, org.apache.spark.SparkContext, org.apache.spark.sql.Column, org.apache.spark.sql.DataFrame, org.apache.spark.sql.Row, org.apache.spark.sql.SparkSession...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.901)
- **Top Global Matches:** file_cluster_4: 9.901, file_cluster_6: 11.49, file_cluster_12: 14.088
- **Magnitude:** 578.02 | **LOC:** 1069 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 91.7%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **15**; blast radius 4.382; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.6%), Guard Balance (formerly Safety Score) (60.2%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateSparkCobolOptions` **(Many-Argument Workhorses)** (Impact: 197.8)
    * *Intent:* /** * Validates if all options passed to 'spark-cobol' are recognized. * */
  * `parseVariableLengthParameters` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `parse` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `getIsEbcdic` **(Compute Cores)** (Impact: 22.0)
  * `parseBdw` **(Stateful Encapsulated Methods)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 111`, `args: 57`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 37`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.382
  * `Choke Point (Betweenness):` 0.001444 | `Ripple Effect (Closeness):` 0.030464
  * `Imports (Out-Degree: 14):` scala.collection.mutable, scala.collection.mutable.ListBuffer, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.CopybookParser, za.co.absa.cobrix.cobol.parser.antlr.ParserJson, za.co.absa.cobrix.cobol.parser.decoders.FloatingPointFormat, za.co.absa.cobrix.cobol.parser.decoders.FloatingPointFormat.FloatingPointFormat...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.775)
- **Top Global Matches:** file_cluster_4: 8.775, file_cluster_6: 11.634, file_cluster_9: 12.648
- **Magnitude:** 510.54 | **LOC:** 480 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **4**; blast radius 5.749; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (40.7%), Connectivity (formerly Api Exposure) (10.2%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.749
  * `Choke Point (Betweenness):` 0.000113 | `Ripple Effect (Closeness):` 0.023734
  * `Imports (Out-Degree: 2):` scala.util.Random, scodec.Attempt.Successful, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.decoders.BinaryUtils
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.549)
- **Top Global Matches:** file_cluster_6: 12.549, file_cluster_8: 16.24, file_cluster_4: 17.309
- **Magnitude:** 424.12 | **LOC:** 429 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 2.861; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.7%), Connectivity (formerly Api Exposure) (49.6%), Complexity Load (formerly Cognitive Load) (46.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.861
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.057465
  * `Imports (Out-Degree: 4):` Constants._, StringTools._, java.nio.charset.StandardCharsets, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.encoding.codepage.CodePage
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.997)
- **Top Global Matches:** file_cluster_4: 11.997, file_cluster_5: 12.727, file_cluster_6: 13.742
- **Magnitude:** 340.5 | **LOC:** 480 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **10**; blast radius 8.123; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.5%)
- **Documentation Coverage:** 38.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFieldByName` **(Generic / Templated Code)** (Impact: 42.2)
    * *Intent:* /** * Get the AST object of a field by name. * * Nested field names can contain '.' to identify the ...
  * `merge` **(Callbacks & Closures)** (Impact: 34.3)
  * `setPrimitiveField` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* /** * Set value of a field of the copybook record by the AST object of the field * * Nested field na...
  * `generateGroupLayoutPositions` **(Compute Cores)** (Impact: 26.2)
  * `dropFillers` **(Compute Cores)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 60`, `args: 58`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 4`
* *Architecture:* `api: 29`, `import: 8`
* *Defense:* `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.123
  * `Choke Point (Betweenness):` 0.002953 | `Ripple Effect (Closeness):` 0.108004
  * `Imports (Out-Degree: 6):` Copybook._, java.util.concurrent.ConcurrentHashMap, scala.collection.mutable, scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST, za.co.absa.cobrix.cobol.parser.ast.Group, za.co.absa.cobrix.cobol.parser.ast.Primitive...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.377)
- **Top Global Matches:** file_cluster_8: 12.377, file_cluster_6: 15.944, file_cluster_4: 23.31
- **Magnitude:** 336.74 | **LOC:** 354 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 1.94; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.3%), Complexity Load (formerly Cognitive Load) (21.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getIntegralDecoder` **(Many-Argument Workhorses)** (Impact: 83.6)
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
* *Structure:* `branch: 133`, `structural_boundaries: 34`, `args: 92`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`
* *Architecture:* `io: 1`, `api: 1`, `import: 13`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.94
  * `Choke Point (Betweenness):` 0.002323 | `Ripple Effect (Closeness):` 0.071902
  * `Imports (Out-Degree: 12):` FloatingPointFormat._, java.nio.charset.Charset, java.nio.charset.StandardCharsets, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.parser.ast.datatype._, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.common.Constants.maxIntegerPrecision, za.co.absa.cobrix.cobol.parser.common.Constants.maxLongPrecision...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/writer/NestedRecordCombiner.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.373)
- **Top Global Matches:** file_cluster_4: 11.373, file_cluster_6: 12.928, file_cluster_5: 13.426
- **Magnitude:** 259.98 | **LOC:** 476 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.968; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeToBytes` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* * * For array fields (both primitive and group-of-primitives) each element is written * using the `f...
  * `buildPrimitiveNode` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* /** * Builds a [[WriterAst]] node for a primitive copybook field, using the field's index in the * s...
  * `buildGroupNode` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /** * Builds a [[WriterAst]] node for a group copybook field. For groups with OCCURS the getter * ex...
  * `combine` **(Many-Argument Workhorses)** (Impact: 25.6)
    * *Intent:* /** * Converts Spark DataFrame to the RDD with data in mainframe format as arrays of bytes, each arr...
  * `processRDD` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* * For variable-length records with OCCURS DEPENDING ON, the output may be trimmed to the actual byte...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 42`, `args: 46`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.968
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` NestedRecordCombiner._, org.apache.spark.rdd.RDD, org.apache.spark.sql.DataFrame, org.apache.spark.sql.Row, org.apache.spark.sql.types.ArrayType, org.apache.spark.sql.types.StructType, org.slf4j.LoggerFactory, scala.collection.mutable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/DisplayEncoders.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.022)
- **Top Global Matches:** file_cluster_1: 6.022, file_cluster_3: 48.256, file_cluster_8: 70.072
- **Magnitude:** 252.46 | **LOC:** 213 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.068; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.8%), Guard Balance (formerly Safety Score) (59.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055143
  * `Imports (Out-Degree: 1):` java.math.RoundingMode, za.co.absa.cobrix.cobol.parser.position.Position
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryUtils.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.679)
- **Top Global Matches:** file_cluster_3: 9.679, file_cluster_8: 21.792, file_cluster_6: 34.244
- **Magnitude:** 225.24 | **LOC:** 249 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 5.423; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (54.2%), Guard Balance (formerly Safety Score) (52.6%), Connectivity (formerly Api Exposure) (34.5%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.423
  * `Choke Point (Betweenness):` 0.00017 | `Ripple Effect (Closeness):` 0.088262
  * `Imports (Out-Degree: 2):` Constants._, za.co.absa.cobrix.cobol.parser.ast.datatype._, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.encoding.EBCDIC, za.co.absa.cobrix.cobol.parser.encoding.Encoding
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen6TypeVariety.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.103)
- **Top Global Matches:** file_cluster_2: 6.103, file_cluster_15: 7.19, file_cluster_10: 7.271
- **Magnitude:** 217.86 | **LOC:** 575 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.968; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.5%), Complexity Load (formerly Cognitive Load) (53.7%), Connectivity (formerly Api Exposure) (3.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.968
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.example.spark.cobol.examples.parser.generators.utils.GeneratorTools._, java.io.BufferedOutputStream, java.io.FileOutputStream, scala.util.Random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/schema/CobolSchema.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.846)
- **Top Global Matches:** file_cluster_4: 7.846, file_cluster_12: 11.253, file_cluster_16: 11.342
- **Magnitude:** 217.04 | **LOC:** 444 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **27**; blast radius 3.453; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.4%), Guard Balance (formerly Safety Score) (52.6%), Connectivity (formerly Api Exposure) (28.5%), Mutation Surface (formerly State Flux) (25.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.453
  * `Choke Point (Betweenness):` 0.001102 | `Ripple Effect (Closeness):` 0.019018
  * `Imports (Out-Degree: 15):` org.apache.spark.sql.types._, scala.collection.mutable, scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.Copybook, za.co.absa.cobrix.cobol.parser.ast._, za.co.absa.cobrix.cobol.parser.ast.datatype.AlphaNumeric, za.co.absa.cobrix.cobol.parser.ast.datatype.COMP1...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.673)
- **Top Global Matches:** file_cluster_8: 12.673, file_cluster_6: 13.508, file_cluster_4: 20.259
- **Magnitude:** 185.96 | **LOC:** 171 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 1.284; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (67.3%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sparseIndexGenerator` **(Many-Argument Workhorses)** (Impact: 126.7)
  * `getSplitCondition` **(Stateful Encapsulated Methods)** (Impact: 5.9)
    * *Intent:* /** Returns a predicate that returns true when current index entry has reached the required size */
  * `getSegmentId` **(Encapsulated Accessors)** (Impact: 5.4)
  * `isSegmentGoodForSplit` **(Encapsulated Accessors)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 15`, `args: 9`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.284
  * `Choke Point (Betweenness):` 0.000141 | `Ripple Effect (Closeness):` 0.011424
  * `Imports (Out-Degree: 8):` scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.Copybook, za.co.absa.cobrix.cobol.parser.ast.Primitive, za.co.absa.cobrix.cobol.parser.headerparsers.RecordHeaderParser, za.co.absa.cobrix.cobol.reader.common.Constants, za.co.absa.cobrix.cobol.reader.extractors.raw.RawRecordExtractor, za.co.absa.cobrix.cobol.reader.index.entry.SparseIndexEntry...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.644)
- **Top Global Matches:** file_cluster_6: 10.644, file_cluster_4: 12.956, file_cluster_5: 17.56
- **Magnitude:** 166.5 | **LOC:** 292 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **20**; blast radius 1.479; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.8%), Connectivity (formerly Api Exposure) (19.9%), Complexity Load (formerly Cognitive Load) (17.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.479
  * `Choke Point (Betweenness):` 0.001337 | `Ripple Effect (Closeness):` 0.011484
  * `Imports (Out-Degree: 17):` scala.collection.mutable.ArrayBuffer, scala.reflect.ClassTag, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.headerparsers.RecordHeaderParser, za.co.absa.cobrix.cobol.parser.headerparsers.RecordHeaderParserFactory, za.co.absa.cobrix.cobol.parser.recordformats.RecordFormat.FixedBlock, za.co.absa.cobrix.cobol.parser.recordformats.RecordFormat.FixedLength...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/stream/SimpleMemoryStream.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.789)
- **Top Global Matches:** file_cluster_9: 7.789, file_cluster_16: 9.498, file_cluster_0: 9.896
- **Magnitude:** 161.36 | **LOC:** 191 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.379; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (41.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.379
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001582
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/EncoderSelector.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 18.085)
- **Top Global Matches:** file_cluster_6: 18.085, file_cluster_8: 20.387, file_cluster_4: 22.207
- **Magnitude:** 155.44 | **LOC:** 150 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 1.894; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (32.8%), Complexity Load (formerly Cognitive Load) (24.6%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getEncoder` **(Generic / Templated Code)** (Impact: 51.5)
  * `getDisplayEncoder` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `getBdcEncoder` **(Callbacks & Closures)** (Impact: 28.0)
  * `getBinaryEncoder` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `getStringEncoder` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* /** Gets an encoder function for a string data type. The encoder is chosen depending on whether the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 26`, `args: 46`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`
* *Architecture:* `io: 1`, `api: 4`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.894
  * `Choke Point (Betweenness):` 0.001184 | `Ripple Effect (Closeness):` 0.071743
  * `Imports (Out-Degree: 12):` java.nio.charset.Charset, java.nio.charset.StandardCharsets, java.util, za.co.absa.cobrix.cobol.parser.ast.datatype.AlphaNumeric, za.co.absa.cobrix.cobol.parser.ast.datatype.COMP3, za.co.absa.cobrix.cobol.parser.ast.datatype.COMP3U, za.co.absa.cobrix.cobol.parser.ast.datatype.COMP4, za.co.absa.cobrix.cobol.parser.ast.datatype.COMP9...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.456)
- **Top Global Matches:** file_cluster_0: 7.456, file_cluster_5: 9.377, file_cluster_10: 9.77
- **Magnitude:** 151.5 | **LOC:** 491 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **69** in-repo importer(s); it depends on **26**; blast radius 17.482; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.4%), Guard Balance (formerly Safety Score) (51.9%), Mutation Surface (formerly State Flux) (22.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseTree` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* * resolving segment redefines. */
  * `parseSimple` **(Many-Argument Workhorses)** (Impact: 14.2)
    * *Intent:* * (the name of this parameter is retained for compatibility, fields won't be actually removed from *...
  * `getParentToChildrenMap` **(Callbacks & Closures)** (Impact: 11.3)
    * *Intent:* /** * Given an AST of a copybook returns a map from segment redefines to their children * */
  * `findCycleHelper` **(Generic / Templated Code)** (Impact: 11.1)
  * `findCycleInAMap` **(Generic / Templated Code)** (Impact: 11.0)
    * *Intent:* /** * Finds a cycle in a parent-child relation map. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 31`, `args: 31`, `func_start: 16`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 14`, `import: 17`
* *Defense:* `doc: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.482
  * `Choke Point (Betweenness):` 0.005723 | `Ripple Effect (Closeness):` 0.119161
  * `Imports (Out-Degree: 14):` java.nio.charset.Charset, java.nio.charset.StandardCharsets, scala.annotation.tailrec, scala.collection.immutable.HashMap, scala.collection.mutable, scala.collection.mutable.ArrayBuffer, scala.collection.mutable.ListBuffer, za.co.absa.cobrix.cobol.internal.Logging...
  * `Imported By (In-Degree: 69):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/VarOccursRecordExtractor.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.498)
- **Top Global Matches:** file_cluster_4: 9.498, file_cluster_6: 10.736, file_cluster_12: 14.391
- **Magnitude:** 145.76 | **LOC:** 157 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%), Complexity Load (formerly Cognitive Load) (56.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extractVarOccursRecordBytes` **(Callbacks & Closures)** (Impact: 35.3)
  * `extractArray` **(Compute Cores)** (Impact: 25.6)
  * `extractValue` **(Callbacks & Closures)** (Impact: 20.1)
  * `extractGroup` **(Compute Cores)** (Impact: 13.3)
  * `ensureBytesRead` **(Stateful Encapsulated Methods)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 8`, `args: 19`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 11`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.173
  * `Choke Point (Betweenness):` 5.5e-05 | `Ripple Effect (Closeness):` 0.003165
  * `Imports (Out-Degree: 3):` java.util, za.co.absa.cobrix.cobol.parser.ast.Group, za.co.absa.cobrix.cobol.parser.ast.Primitive, za.co.absa.cobrix.cobol.parser.ast.Statement
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.625)
- **Top Global Matches:** file_cluster_4: 8.625, file_cluster_12: 11.027, file_cluster_5: 11.811
- **Magnitude:** 142.2 | **LOC:** 324 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 1.007; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.4%), Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (40.4%), Mutation Surface (formerly State Flux) (38.1%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveHeaderTrailerOffsets` **(Many-Argument Workhorses)** (Impact: 48.6)
    * *Intent:* /** * Resolves record_header_name / record_trailer_name options into file_start_offset / file_end_of...
  * `createRelation` **(Many-Argument Workhorses)** (Impact: 25.2)
    * *Intent:* /** Writer relation */
  * `buildEitherReader` **(Compute Cores)** (Impact: 16.8)
    * *Intent:* /** * Builds one of two Readers, depending on the parameters. * * This method will probably be remov...
  * `createRelation` **(Many-Argument Workhorses)** (Impact: 5.1)
    * *Intent:* /** Reader relation */
  * `schema` **(Generic / Templated Code)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 51`, `args: 28`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 5`, `planned_debt: 1`
* *Architecture:* `api: 12`, `import: 19`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.007
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.001582
  * `Imports (Out-Degree: 17):` DefaultSource._, org.apache.hadoop.fs.Path, org.apache.hadoop.io.BytesWritable, org.apache.hadoop.io.NullWritable, org.apache.hadoop.mapred.FileInputFormat, org.apache.spark.sql.DataFrame, org.apache.spark.sql.SQLContext, org.apache.spark.sql.SaveMode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BCDNumberDecoders.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 18.402)
- **Top Global Matches:** file_cluster_3: 18.402, file_cluster_1: 35.244, file_cluster_8: 38.039
- **Magnitude:** 141.46 | **LOC:** 175 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.078; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.3%), Complexity Load (formerly Cognitive Load) (55.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeBigBCDNumber` **(Many-Argument Workhorses)** (Impact: 66.6)
    * *Intent:* /** * Decode a binary encoded decimal (BCD) aka COMP-3 format to a String * */
  * `decodeBCDIntegralNumber` **(Compute Cores)** (Impact: 31.7)
    * *Intent:* /** * Decode an integral binary encoded decimal (BCD) aka COMP-3 format to a String * */
  * `decodeBigBCDDecimal` **(Generic / Templated Code)** (Impact: 4.8)
    * *Intent:* /** Malformed data does not cause exceptions in Spark. Null values are returned instead */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 15`, `args: 6`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 11`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055236
  * `Imports (Out-Degree: 0):` scala.util.control.NonFatal
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/IndexBuilder.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.765)
- **Top Global Matches:** file_cluster_5: 8.765, file_cluster_12: 9.716, file_cluster_0: 10.222
- **Magnitude:** 134.98 | **LOC:** 398 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 1.278; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.6%), Mutation Surface (formerly State Flux) (20.1%), Complexity Load (formerly Cognitive Load) (8.4%)
- **Documentation Coverage:** 64.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildIndexForVarLenReader` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /** * Builds records indexes. Does not take locality into account. Used for file systems that * do n...
  * `buildIndex` **(Generic / Templated Code)** (Impact: 18.8)
  * `selfCheckForIndexCompatibility` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `getStreams` **(Stateful Encapsulated Methods)** (Impact: 17.1)
  * `buildIndexForVarLenReaderWithFullLocality` **(Stateful Encapsulated Methods)** (Impact: 13.2)
    * *Intent:* /** * Builds the indexes by querying HDFS about the records locations and then asking Spark to assig...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 42`, `args: 36`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `doc: 6`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.278
  * `Choke Point (Betweenness):` 0.00048 | `Ripple Effect (Closeness):` 0.005651
  * `Imports (Out-Degree: 17):` org.apache.hadoop.conf.Configuration, org.apache.hadoop.fs._, org.apache.hadoop.hdfs.DistributedFileSystem, org.apache.spark.SparkContext, org.apache.spark.rdd.RDD, org.apache.spark.sql.SQLContext, scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.internal.Logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.477)
- **Top Global Matches:** file_cluster_0: 8.477, file_cluster_5: 9.056, file_cluster_12: 9.39
- **Magnitude:** 132.64 | **LOC:** 292 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.968; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.7%), Guard Balance (formerly Safety Score) (52.3%), Concurrency Surface (formerly Concurrency) (43.1%)
- **Documentation Coverage:** 69.5652% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process` **(Stateful Encapsulated Methods)** (Impact: 37.9)
    * *Intent:* /** * Runs raw record processing and returns the record count processed. * */
  * `getRecordRdd` **(Stateful Encapsulated Methods)** (Impact: 24.3)
  * `load` **(Generic / Templated Code)** (Impact: 6.4)
  * `processListOfFiles` **(Many-Argument Workhorses)** (Impact: 4.8)
  * `save` **(Stateful Encapsulated Methods)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 58`, `args: 26`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 5`, `import: 24`
* *Defense:* `safety: 1`, `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.968
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` java.io.BufferedOutputStream, java.util.concurrent.ExecutorService, java.util.concurrent.Executors, org.apache.hadoop.fs.Path, org.apache.spark.rdd.RDD, org.apache.spark.sql.SparkSession, org.slf4j.LoggerFactory, scala.collection.mutable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.339)
- **Top Global Matches:** file_cluster_1: 8.339, file_cluster_3: 48.548, file_cluster_8: 70.264
- **Magnitude:** 130.72 | **LOC:** 125 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.616; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Compute Cores)** (Impact: 70.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 19`, `args: 23`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.616
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.011125
  * `Imports (Out-Degree: 2):` scala.collection.mutable.ListBuffer, za.co.absa.cobrix.cobol.parser.expression.exception.ExprSyntaxError, za.co.absa.cobrix.cobol.parser.expression.lexer.Token, za.co.absa.cobrix.cobol.parser.expression.lexer.Token._
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/utils/UsingUtilsSuite.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.874)
- **Top Global Matches:** file_cluster_7: 5.874, file_cluster_12: 8.563, file_cluster_5: 9.408
- **Magnitude:** 124.5 | **LOC:** 513 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.968; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (53.5%), Guard Balance (formerly Safety Score) (38.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 88`, `args: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 39`
* *Architecture:* `import: 2`
* *Defense:* `safety: 102`, `test: 102`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.968
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` UsingUtils.Implicits._, org.scalatest.wordspec.AnyWordSpec
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/FixedWithRecordLengthExprRawRecordExtractor.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 13.263)
- **Top Global Matches:** file_cluster_4: 13.263, file_cluster_6: 14.018, file_cluster_5: 14.441
- **Magnitude:** 122.1 | **LOC:** 208 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.036; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.2%), Complexity Load (formerly Cognitive Load) (42.7%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getRecordLengthFromField` **(Stateful Encapsulated Methods)** (Impact: 30.5)
  * `fetchRecordUsingRecordLengthFieldExpression` **(Stateful Encapsulated Methods)** (Impact: 17.6)
  * `fetchNext` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `fetchRecordUsingRecordLengthField` **(Stateful Encapsulated Methods)** (Impact: 9.5)
  * `getRecordLengthFromMapping` **(Encapsulated Accessors)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 40`, `args: 37`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 9`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.036
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.001582
  * `Imports (Out-Degree: 6):` org.slf4j.LoggerFactory, scala.util.Try, za.co.absa.cobrix.cobol.parser.Copybook, za.co.absa.cobrix.cobol.parser.ast.Primitive, za.co.absa.cobrix.cobol.reader.iterator.RecordLengthExpression, za.co.absa.cobrix.cobol.reader.parameters.ReaderParameters, za.co.absa.cobrix.cobol.reader.validator.ReaderParametersValidator, za.co.absa.cobrix.cobol.utils.StringUtils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/utils/Test10CustomRDWParser.scala` (SCALA) | Magnitude: 25.16 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 10, core_var_decl: 10, design_camel_case: 6
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePageCommonExt.scala` (SCALA) | Magnitude: 5.32 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 61, core_var_decl: 37, design_snake_case: 36, structural_boundaries: 5
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/regression/Test04VarcharFields.scala` (SCALA) | Magnitude: 16.98 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 91, bitwise_ops: 63, explicit_casts: 55, core_var_decl: 12
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/regression/Test16BinaryLittleEndian.scala` (SCALA) | Magnitude: 16.06 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, bitwise_ops: 11, structural_boundaries: 10, core_var_decl: 8
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/extract/OccursExtractorSpec.scala` (SCALA) | Magnitude: 15.94 | Delta: **0.178** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, import: 13, bitwise_ops: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/utils/FileUtilsSpec.scala` (SCALA) | Magnitude: 21.36 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 47, core_var_decl: 44, test: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/utils/HDFSUtilsSpec.scala` (SCALA) | Magnitude: 6.82 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 20, core_var_decl: 11, test: 8
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/AsciiStringDecoderWrapperSpec.scala` (SCALA) | Magnitude: 16.3 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 23, core_var_decl: 20, design_snake_case: 20
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/copybooks/ParseDebugRedefinedSpec.scala` (SCALA) | Magnitude: 17.18 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 50, bitwise_ops: 23, structural_boundaries: 9, core_var_decl: 7
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReaderSpec.scala` (SCALA) | Magnitude: 25.98 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 185, core_var_decl: 50, safety: 47, test: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test38StrictBinaryTypeSpec.scala` (SCALA) | Magnitude: 17.1 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 99, bitwise_ops: 45, core_var_decl: 14, design_camel_case: 10
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/Test01DisplayPicAsStrings.scala` (SCALA) | Magnitude: 17.3 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 106, bitwise_ops: 48, core_var_decl: 16, structural_boundaries: 11
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/ResourceUtils.scala` (SCALA) | Magnitude: 2.62 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, args: 1, func_start: 1
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/base/SimpleComparisonBase.scala` (SCALA) | Magnitude: 7.7 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/extract/BinaryExtractorSpec.scala` (SCALA) | Magnitude: 13.36 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 148, explicit_casts: 140, core_var_decl: 53, design_pascal_case: 42
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/CobolRelation.scala` (SCALA) | Magnitude: 31.46 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 38, import: 16, args: 15
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/streaming/FileStreamer.scala` (SCALA) | Magnitude: 68.44 | Delta: **0.202** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 77, core_var_decl: 29, branch: 24, structural_boundaries: 20
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/parse/JsonSpec.scala` (SCALA) | Magnitude: 3.98 | Delta: **0.215** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 23, test: 17, safety: 13, generics: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/copybooks/CopybookCharsSpec.scala` (SCALA) | Magnitude: 15.92 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 40, core_var_decl: 16, design_snake_case: 14, test: 12
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/encoding/BinaryEncodersSuite.scala` (SCALA) | Magnitude: 16.18 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 54, core_var_decl: 21, design_snake_case: 19, structural_boundaries: 15
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test25OccursMappings.scala` (SCALA) | Magnitude: 20.42 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 108, core_var_decl: 29, design_camel_case: 19, structural_boundaries: 18
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtilsSuite.scala` (SCALA) | Magnitude: 22.16 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 716, bitwise_ops: 554, core_var_decl: 170, test: 123
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/BuildProperties.scala` (SCALA) | Magnitude: 7.18 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, core_var_decl: 10, structural_boundaries: 7, design_pascal_case: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` -> Churn: **64.5%** | Cog Load: 71.81% | Debt: 10.687%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 584.02
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` -> **Ruslan Iushchenko** (91.7% isolated ownership) | Magnitude: 578.02
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 424.12
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 340.5
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 336.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` -> **Severity: 0.135** (Bridge: 0.0014 * Flux: 93.457%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` -> **Severity: 0.13** (Bridge: 0.0057 * Flux: 22.6604%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` -> **Severity: 0.109** (Bridge: 0.0061 * Flux: 17.886%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **Severity: 0.087** (Bridge: 0.003 * Flux: 29.3968%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/RawRecordContext.scala` -> **Severity: 0.086** (Bridge: 0.0015 * Flux: 57.5103%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 7.452** (Embedded: 0.1325 * Error Risk: 56.2528%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **Severity: 6.27** (Embedded: 0.108 * Error Risk: 58.0488%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` -> **Severity: 6.189** (Embedded: 0.1192 * Error Risk: 51.9345%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` -> **Severity: 5.753** (Embedded: 0.1029 * Error Risk: 55.896%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/EncoderSelector.scala` -> **Severity: 5.739** (Embedded: 0.0717 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/datatype/Usage.scala` -> **Severity: 1552.5** (Blast Radius: 15.525 * Doc Risk: 100.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/SingleByteCodePage.scala` -> **Severity: 1296.734** (Blast Radius: 19.451 * Doc Risk: 66.6667%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 956.925** (Blast Radius: 12.759 * Doc Risk: 75.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/stream/SimpleStream.scala` -> **Severity: 956.8** (Blast Radius: 9.568 * Doc Risk: 100.0%)
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/fixtures/BinaryFileFixture.scala` -> **Severity: 890.22** (Blast Radius: 14.837 * Doc Risk: 60.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `31` files carry mainframe facts -- `0` call sites, `0` dataset bindings, `400` record items.

### `data/test17_hierarchical.cob` (COBOL)
- **Record layouts (32 items):** `ENTITY (32)`

### `data/test18 special_char.cob` (COBOL)
- **Record layouts (32 items):** `ENTITY (32)`

### `data/test7_fillers.cob` (COBOL)
- **Record layouts (20 items):** `RECORD (20)`

### `data/test15_copybook.cob` (COBOL)
- **Record layouts (15 items):** `RECORD (15)`

### `data/test19_display_num.cob` (COBOL)
- **Record layouts (15 items):** `WS-INPUT-RECORD (15)`

### `data/test1_copybook.cob` (COBOL)
- **Record layouts (15 items):** `RECORD (15)`

### `data/test2_copybook.cob` (COBOL)
- **Record layouts (15 items):** `RECORD (15)`

### `data/test5d_copybook.cob` (COBOL)
- **Record layouts (15 items):** `COMPANY-DETAILS (15)`

### `examples/example_data/raw_file.cob` (COBOL)
- **Record layouts (15 items):** `RECORD (15)`

### `data/test16_fix_len_segments.cob` (COBOL)
- **Record layouts (14 items):** `ENTITY (14)`

### `data/test1a_copybook.cob` (COBOL)
- **Record layouts (14 items):** `RECORD (14)`

### `data/test11_copybook.cob` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

### `data/test12_copybook.cob` (COBOL)
- **Record layouts (13 items):** `RECORD-A (10)`, `RECORD-B (3)`

### `data/test13b_vrl_file_headers.cob` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

### `data/test14_copybook.cob` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

### `data/test4_copybook.cob` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

### `data/test5_copybook.cob` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

### `examples/example_data/companies_copybook.cpy` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

### `examples/example_data/copybook_codec.cob` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

### `examples/example_data/multisegment.cob` (COBOL)
- **Record layouts (13 items):** `COMPANY-DETAILS (13)`

*(+11 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 315 literal sites + 13 sites through wrappers = 328

- `reportInvalidHeaderZeros` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala`
- `reportInvalidValue` (function, panics_and_aborts, primitive): 2 call sites in 2 files -- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala`
- `getDestinationDirectory` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/replication/CobolBinaryFilesReplicator.scala`
- `getFilesSourceDirectory` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/replication/CobolBinaryFilesReplicator.scala`
- `getInitialDestinationFileId` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/replication/CobolBinaryFilesReplicator.scala`
- `getMaxAllowedSpaceBytes` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/replication/CobolBinaryFilesReplicator.scala`
- `getMaxParallelReplicators` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/replication/CobolBinaryFilesReplicator.scala`
- `reportInvalidHeaderLength` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala`
- `reportMinimumLength` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala`
- `reportTooLargeBlockLength` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala`
- `reportZeroLength` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderCommon.scala`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3228 call pairs -- scoped 28.0%, unique 0.7%, ambiguous 16.8%, external 54.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| scala | 3227 | 28.0% | 0.7% | 16.8% | 54.5% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
