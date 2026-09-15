# ARCHITECTURAL_BRIEF: cobrix
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AbsaOSS/cobrix.git` |
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
| Total Artifacts | 705 |
| Analyzed Artifacts (Scanned) | 645 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 60 |
| Total LOC | 49272 |
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
| BATCH | 1 | 3 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.16; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Declarative / Non-Code 27%, I/O & Config Routines Files 9%, State Mutators Files 7%, Callbacks & Closures Files 7%
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
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 80.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.0 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 84.1 | 5.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 32.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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
  * *Intent:* * @param variableLengthOccurs If true, OCCURS DEPENDING ON data size will depend on the number of elements. * @param generateRecordId If true, a recor...
- `extractHierarchicalRecord` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> Impact: **221.8** | LOC: 195
  * *Intent:* * @param segmentsData The data bits containing the record * @param segmentRedefines A list of segment redefine GROUPs * @param segmentIdRedefineMap A ...
- `validateSparkCobolOptions` **(Many-Argument Workhorses)** (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala`) -> Impact: **201.8** | LOC: 235
  * *Intent:* /** * Validates if all options passed to 'spark-cobol' are recognized. * * @param params Parameters provided by spark.read.option(...) */
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

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` (SCALA) -> Cumulative Risk: **624.92**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.82)
- **Magnitude:** 872.76 | **LOC:** 555 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Safety Score (97.108%), Verification (80.0%)
- **Heaviest Functions:** `extractRecord` (Many-Argument Workhorses, Impact: 228.9), `extractHierarchicalRecord` (Many-Argument Workhorses, Impact: 221.8), `applyRecordPostProcessing` (Many-Argument Workhorses, Impact: 53.0)

### 2. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/BinaryEncoders.scala` (SCALA) -> Cumulative Risk: **609.25**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.22)
- **Magnitude:** 78.94 | **LOC:** 72 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Cognitive Load (88.2402%)
- **Heaviest Functions:** `encodeBinaryNumber` (Many-Argument Workhorses, Impact: 59.0)

### 3. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/streaming/BufferedFSDataInputStream.scala` (SCALA) -> Cumulative Risk: **588.37**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.06)
- **Magnitude:** 120.22 | **LOC:** 150 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (93.806%), Verification (80.0%)
- **Heaviest Functions:** `readFully` (Many-Argument Workhorses, Impact: 36.3), `readFullyHelper` (Many-Argument Workhorses, Impact: 14.8), `openStream` (I/O & Config Routines, Impact: 9.3)

### 4. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/NumExprBuilderImpl.scala` (SCALA) -> Cumulative Risk: **582.39**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.03)
- **Magnitude:** 106.96 | **LOC:** 142 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9982%), Safety Score (85.5851%)
- **Heaviest Functions:** `eval` (Callbacks & Closures, Impact: 11.5), `closeParen` (Compute Cores, Impact: 7.7), `getResult` (I/O & Config Routines, Impact: 6.6)

### 5. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` (SCALA) -> Cumulative Risk: **581.26**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.27)
- **Magnitude:** 130.72 | **LOC:** 125 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.5823%)
- **Heaviest Functions:** `parse` (Callbacks & Closures, Impact: 70.7)

### 6. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` (SCALA) -> Cumulative Risk: **580.6**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.67)
- **Magnitude:** 587.52 | **LOC:** 599 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Api Exposure (91.2806%), Safety Score (82.8897%)
- **Heaviest Functions:** `copyMetadata` (Many-Argument Workhorses, Impact: 67.1), `flattenSchema` (Callbacks & Closures, Impact: 56.2), `splitFieldPath` (Compute Cores, Impact: 24.8)

### 7. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA) -> Cumulative Risk: **571.87**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.36)
- **Magnitude:** 2277.46 | **LOC:** 3481 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8764%), Verification (80.0%)
- **Heaviest Functions:** `pic` (Compute Cores, Impact: 119.2), `group` (Compute Cores, Impact: 53.1), `identifier` (I/O & Config Routines, Impact: 38.1)

### 8. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` (JAVA) -> Cumulative Risk: **565.76**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.46)
- **Magnitude:** 331.92 | **LOC:** 516 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (93.1542%), Verification (80.0%)
- **Heaviest Functions:** `value` (I/O & Config Routines, Impact: 21.9), `obj` (I/O & Config Routines, Impact: 9.8), `arr` (I/O & Config Routines, Impact: 9.8)

### 9. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextFullRecordExtractor.scala` (SCALA) -> Cumulative Risk: **556.78**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.08)
- **Magnitude:** 119.12 | **LOC:** 197 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.4062%)
- **Heaviest Functions:** `findNextLineBreak` (Compute Cores, Impact: 16.9), `findNextNonEmptyRecord` (I/O & Config Routines, Impact: 8.9), `findNextRecord` (I/O & Config Routines, Impact: 7.3)

### 10. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/DisplayEncoders.scala` (SCALA) -> Cumulative Risk: **554.3**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.01)
- **Magnitude:** 252.46 | **LOC:** 213 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.0611%), Verification (80.0%)
- **Heaviest Functions:** `encodeDisplayNumberSignSeparate` (Many-Argument Workhorses, Impact: 67.9), `encodeDisplayNumberSignOverpunched` (Many-Argument Workhorses, Impact: 62.1), `setPaddedEbcdicNumberWithSignSeparate` (Many-Argument Workhorses, Impact: 50.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2277.46 | **LOC:** 3481 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.3446%), Tech Debt (99.8764%)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 872.76 | **LOC:** 555 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (71.81%), Tech Debt (11.3016%)
**Top Internal Functions/Classes:**
  * `extractRecord` **(Many-Argument Workhorses)** (Impact: 228.9)
    * *Intent:* * @param variableLengthOccurs If true, OCCURS DEPENDING ON data size will depend on the number of el...
  * `extractHierarchicalRecord` **(Many-Argument Workhorses)** (Impact: 221.8)
    * *Intent:* * @param segmentsData The data bits containing the record * @param segmentRedefines A list of segmen...
  * `applyRecordPostProcessing` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* * @param ast The parsed copybook * @param records The array of [[T]] object for each Group of the co...
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 646.3 | **LOC:** 880 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.2138%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 605.32 | **LOC:** 1069 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 92.3%
- **Risk Profile:** Cognitive Load (26.5205%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateSparkCobolOptions` **(Many-Argument Workhorses)** (Impact: 201.8)
    * *Intent:* /** * Validates if all options passed to 'spark-cobol' are recognized. * * @param params Parameters ...
  * `parseVariableLengthParameters` **(Compute Cores)** (Impact: 37.8)
  * `getIsEbcdic` **(Compute Cores)** (Impact: 25.4)
  * `parse` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `parseBdw` **(Type Conversions)** (Impact: 21.9)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 587.52 | **LOC:** 599 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.708%), Tech Debt (8.8994%)
**Top Internal Functions/Classes:**
  * `copyMetadata` **(Many-Argument Workhorses)** (Impact: 67.1)
    * *Intent:* /** * Copies metadata from one schema to another as long as names and data types are the same. * * @...
  * `flattenSchema` **(Callbacks & Closures)** (Impact: 56.2)
    * *Intent:* /** * Given an instance of DataFrame returns a dataframe with flattened schema. * All nested structu...
  * `splitFieldPath` **(Compute Cores)** (Impact: 24.8)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 510.54 | **LOC:** 480 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.7259%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 424.12 | **LOC:** 429 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.7093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `decodeEbcdicNumber` **(Many-Argument Workhorses)** (Impact: 118.2)
    * *Intent:* * A decoder for any EBCDIC uncompressed numbers supporting * <ul> * <li> Separate leading and traili...
  * `decodeAsciiNumber` **(Many-Argument Workhorses)** (Impact: 71.4)
    * *Intent:* /** * A decoder for any ASCII uncompressed numbers supporting leading and trailing sign * * @param b...
  * `decodeAsciiString` **(Compute Cores)** (Impact: 33.2)
    * *Intent:* /** * A decoder for any ASCII string fields (alphabetical or any char) * * @param bytes A byte array...
  * `decodeUtf16String` **(Many-Argument Workhorses)** (Impact: 27.8)
    * *Intent:* /** * A decoder for any UTF-16 string field * * @param bytes A byte array that represents the binary...
  * `decodeEbcdicString` **(Many-Argument Workhorses)** (Impact: 25.4)
    * *Intent:* /** * A decoder for any EBCDIC string fields (alphabetical or any char) * * @param bytes A byte arra...
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 347.9 | **LOC:** 480 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.5786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFieldByName` **(Callbacks & Closures)** (Impact: 42.2)
    * *Intent:* /** * Get the AST object of a field by name. * * Nested field names can contain '.' to identify the ...
  * `setPrimitiveField` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* /** * Set value of a field of the copybook record by the AST object of the field * * Nested field na...
  * `merge` **(Callbacks & Closures)** (Impact: 34.3)
  * `generateGroupLayoutPositions` **(Compute Cores)** (Impact: 26.2)
  * `dropFillers` **(Callbacks & Closures)** (Impact: 25.6)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 341.24 | **LOC:** 354 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.6796%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getIntegralDecoder` **(Many-Argument Workhorses)** (Impact: 88.1)
    * *Intent:* /** Gets a decoder function for an integral data type. A direct conversion from array of bytes to th...
  * `getBinaryEncodedIntegralDecoder` **(Callbacks & Closures)** (Impact: 65.5)
    * *Intent:* /** Gets a decoder function for a binary encoded integral data type. A direct conversion from array ...
  * `getDecimalDecoder` **(Many-Argument Workhorses)** (Impact: 56.4)
    * *Intent:* /** Gets a decoder function for a decimal data type. The input array of bytes is always converted to...
  * `getDecoder` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* * <li> Integral types are represented as boxed integers and longs. Larger integral numbers are repre...
  * `getStringDecoder` **(Many-Argument Workhorses)** (Impact: 25.0)
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
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 331.92 | **LOC:** 516 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3994%), Tech Debt (71.0338%)
**Top Internal Functions/Classes:**
  * `value` **(I/O & Config Routines)** (Impact: 21.9)
  * `obj` **(I/O & Config Routines)** (Impact: 9.8)
  * `arr` **(I/O & Config Routines)** (Impact: 9.8)
  * `accept` **(Defensive Guards)** (Impact: 7.3)
  * `accept` **(Defensive Guards)** (Impact: 7.3)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 268.38 | **LOC:** 476 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.6574%), Tech Debt (11.2299%)
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
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 252.46 | **LOC:** 213 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.8211%), Tech Debt (26.3198%)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 225.24 | **LOC:** 249 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.02%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBytesCount` **(Compute Cores)** (Impact: 82.3)
  * `decodeBinaryNumber` **(Many-Argument Workhorses)** (Impact: 57.9)
    * *Intent:* /** A generic decoder for 2s compliment binary numbers aka COMP * * @param bytes A byte array that r...
  * `addDecimalPoint` **(Compute Cores)** (Impact: 44.2)
    * *Intent:* /** Transforms a string representation of an integer to a string representation of decimal * by addi...
  * `decodeString` **(Many-Argument Workhorses)** (Impact: 17.1)
    * *Intent:* /** A decoder for any string fields (alphabetical or any char) * * @param bytes A byte array that re...
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
- **Risk Profile:** Cognitive Load (53.7134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 7.7)
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
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 217.04 | **LOC:** 444 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (21.2292%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parsePrimitive` **(Callbacks & Closures)** (Impact: 54.8)
  * `createSparkSchema` **(I/O & Config Routines)** (Impact: 24.4)
  * `parseGroup` **(Compute Cores)** (Impact: 22.5)
  * `builder` **(Compute Cores)** (Impact: 11.6)
  * `addExtendedPrimitiveMetadata` **(Callbacks & Closures)** (Impact: 11.4)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 189.46 | **LOC:** 171 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.9573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sparseIndexGenerator` **(Many-Argument Workhorses)** (Impact: 130.2)
  * `getSplitCondition` **(Callbacks & Closures)** (Impact: 5.9)
    * *Intent:* /** Returns a predicate that returns true when current index entry has reached the required size */
  * `getSegmentId` **(Generic / Templated Code)** (Impact: 5.4)
  * `isSegmentGoodForSplit` **(Generic / Templated Code)** (Impact: 2.3)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 166.5 | **LOC:** 292 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.4903%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `recordExtractor` **(Compute Cores)** (Impact: 57.8)
  * `generateIndex` **(Many-Argument Workhorses)** (Impact: 43.3)
    * *Intent:* /** * Traverses the data sequentially as fast as possible to generate record index. * This index wil...
  * `getRecordIterator` **(Many-Argument Workhorses)** (Impact: 11.4)
  * `getRootSegmentId` **(Callbacks & Closures)** (Impact: 10.5)
  * `getRecordHeaderParser` **(Callbacks & Closures)** (Impact: 9.2)
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
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 161.36 | **LOC:** 191 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `searchOutOfLookbackBuffer` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* /** Searches the sequence of bytes outsize of the lookback buffer. Returns the index of the beginnin...
  * `search` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* /** Searches the stream for the specified sequence of bytes. Returns the index of the beginning of t...
  * `getBytes` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* /* Gets the specific number of bytes starting from specific index. Returns the number of bytes read ...
  * `AddBytesToLookbackBuffer` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* /** Adds bytes to the lookback buffer */
  * `extractOutOfLoobackBufferBytes` **(Many-Argument Workhorses)** (Impact: 12.1)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 157.84 | **LOC:** 150 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.2507%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getEncoder` **(Callbacks & Closures)** (Impact: 51.5)
  * `getBdcEncoder` **(Callbacks & Closures)** (Impact: 30.4)
  * `getDisplayEncoder` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `getBinaryEncoder` **(Callbacks & Closures)** (Impact: 24.8)
  * `getStringEncoder` **(Callbacks & Closures)** (Impact: 14.3)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
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

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
