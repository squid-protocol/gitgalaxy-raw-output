# ARCHITECTURAL_BRIEF: serenity
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/SerenityOS/serenity.git` |
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
- **Scope:** 13270 analyzed artifact(s), 1084525 LOC.
- **Load-bearing artifact:** `Userland/Libraries/LibGfx/ImageFormats/WebPSharedLossless.h` -- 1648 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Ports/AvailablePorts.md` -- pulls in 358 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Userland/Libraries/LibWeb/CSS/Parser/Parser.cpp` at magnitude 5648.18 (structural weight, not risk).
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
| Total Artifacts | 18572 |
| Analyzed Artifacts (Scanned) | 13270 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5302 |
| Total LOC | 1084525 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5551 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1016 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 206 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 7398 | 933402 | 55.7% |
| HTML | 1795 | 46463 | 13.5% |
| PLAINTEXT | 1560 | 16 | 11.8% |
| JAVASCRIPT | 1115 | 58149 | 8.4% |
| MARKDOWN | 604 | 0 | 4.6% |
| SHELL | 431 | 11811 | 3.2% |
| JSON | 168 | 20397 | 1.3% |
| OBJECTIVE-C | 45 | 6061 | 0.3% |
| XML | 37 | 0 | 0.3% |
| PYTHON | 34 | 3960 | 0.3% |
| ASSEMBLY | 21 | 1762 | 0.2% |
| YAML | 19 | 1044 | 0.1% |
| CSS | 19 | 1109 | 0.1% |
| GLSL | 10 | 46 | 0.1% |
| SQLITE | 6 | 110 | 0.0% |
| NIX | 3 | 105 | 0.0% |
| DOCKERFILE | 2 | 50 | 0.0% |
| LUA | 2 | 28 | 0.0% |
| MAKEFILE | 1 | 12 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 13265 |
| cp1252 | cp1252-fallback | 1 |
| latin-1 | latin-1-fallback | 1 |
| unknown | unknown | 1 |
| utf-16-be | utf-16-heuristic | 1 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Declarative / Non-Code 17%, Large Core Modules (3) 12%, Interface Declarations Files 8%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 11105 | 83.7% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2160 | 16.3% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5302*

**Composition by Extension & Reason:**
- `.png`: 3035x Excluded (Explicitly Denied Extension: '.png')
- `.patch`: 472x Excluded (Unsupported Extension: '.patch'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.idl`: 429x Excluded (Unsupported Extension: '.idl')
- `.txt`: 159x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2092 LOC)
- `.gn`: 138x Excluded (Unsupported Extension: '.gn'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gml`: 133x Excluded (Unsupported Extension: '.gml')
- `.jbig2`: 107x Excluded (Unsupported Extension: '.jbig2')
- `.af`: 71x Excluded (Unsupported Extension: '.af')
- `.ini`: 55x Excluded (Unsupported Extension: '.ini'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.font`: 51x Excluded (Unsupported Extension: '.font')
- `no_extension`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded (Binary Format Detected), 8x Unsupported Format (.undeterminable)
- `.jp2`: 45x Excluded (Unsupported Extension: '.jp2')
- `.tiff`: 44x Excluded (Explicitly Denied Extension: '.tiff')
- `.ipc`: 36x Excluded (Unsupported Extension: '.ipc')
- `.pdf`: 32x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.9 | 3.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.4 | 28.9 | 42.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 26.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 38.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 93.5 | 0.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 63.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 24586 | 3332 | 4 | `Userland/Libraries/LibJS/Parser.cpp` |
| cleanup | 1285 | 590 | 0 | `Userland/Libraries/LibGUI/VimEditingEngine.cpp` |
| guards | 97516 | 6530 | 18 | `Userland/Libraries/LibJS/AST.h` |
| danger | 5282 | 1372 | 1 | `Kernel/Arch/aarch64/Registers.h` |
| concurrency | 2907 | 627 | 0 | `Userland/Libraries/LibJS/Tests/syntax/async-await.js` |
| connectivity | 16864 | 3768 | 3 | `Userland/Libraries/LibWeb/CSS/ComputedValues.h` |
| io | 4703 | 1362 | 1 | `Base/res/html/misc/welcome.html` |
| crypto | 1 | 1 | 0 | `Meta/download_file.py` |
| ipc | 710 | 215 | 0 | `Kernel/Bus/USB/xHCI/xHCIController.cpp` |
| time | 320 | 92 | 0 | `Base/res/html/misc/set-timeout-and-interval.html` |
| serialization | 180 | 67 | 0 | `Base/usr/share/Spreadsheet/runtime.js` |
| regex | 319 | 83 | 0 | `Userland/Libraries/LibJS/Tests/builtins/String/String.prototype.replace.js` |
| events | 2820 | 745 | 0 | `Userland/Libraries/LibJS/Bytecode/ASTCodegen.cpp` |
| tests | 33769 | 2009 | 2 | `Userland/Libraries/LibJS/Tests/builtins/Intl/NumberFormat/NumberFormat.prototype.format.js` |
| docs | 709 | 255 | 0 | `Userland/Libraries/LibGfx/ImageFormats/JPEGXLLoader.cpp` |
| debt | 9101 | 1986 | 1 | `Userland/Libraries/LibJS/Bytecode/Op.h` |
| mutation | 213016 | 8479 | 36 | `Userland/Libraries/LibWeb/CSS/Parser/Parser.cpp` |
| dead_code | 30896 | 3860 | 6 | `Userland/Libraries/LibShell/AST.cpp` |
| credential | 375 | 343 | 0 | `Ports/xash3d-fwgs/package.sh` |
| threat | 625 | 52 | 0 | `Userland/Libraries/LibJS/Tests/builtins/Intl/NumberFormat/NumberFormat.prototype.format.js` |
| ml_ai | 873 | 174 | 0 | `Tests/LibWeb/Screenshot/svg-stroke-styles.html` |
| ui | 2017 | 629 | 0 | `Base/res/html/misc/display-grid.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Base/res/html/misc/welcome.html` (Hits: 306)
- `Tests/LibCompress/brotli-test-files/happy3rd.html` (Hits: 208)
- `Kernel/Net/NetworkTask.cpp` (Hits: 141)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **WebPSharedLossless.h** (`Userland/Libraries/LibGfx/ImageFormats/WebPSharedLossless.h`) — 1648 inbound connections
2. **Format.h** (`AK/Format.h`) — 877 inbound connections
3. **ByteString.h** (`AK/ByteString.h`) — 746 inbound connections
4. **include.js** (`Tests/LibWeb/Text/input/include.js`) — 685 inbound connections
5. **String.h** (`AK/String.h`) — 680 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AvailablePorts.md** (`Ports/AvailablePorts.md`) — 358 outbound dependencies
2. **Document.cpp** (`Userland/Libraries/LibWeb/DOM/Document.cpp`) — 130 outbound dependencies
3. **Intrinsics.cpp** (`Userland/Libraries/LibJS/Runtime/Intrinsics.cpp`) — 126 outbound dependencies
4. **ElementFactory.cpp** (`Userland/Libraries/LibWeb/DOM/ElementFactory.cpp`) — 109 outbound dependencies
5. **GlobalObject.cpp** (`Userland/Libraries/LibJS/Runtime/GlobalObject.cpp`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `BytecodeInterpreter::interpret_instruction` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibWasm/AbstractMachine/BytecodeInterpreter.cpp`) -> Impact: **1036.5** | LOC: 1250
- `Parser::basic_parse` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibURL/Parser.cpp`) -> Impact: **885.2** | LOC: 950
  * *Intent:* // https://url.spec.whatwg.org/#concept-basic-url-parser
- `generate_to_cpp` **(Many-Argument Workhorses)** (@ `Meta/Lagom/Tools/CodeGenerators/LibWeb/BindingsGenerator/IDLGenerators.cpp`) -> Impact: **856.7** | LOC: 1053
- `Instruction::to_byte_string_internal` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibDisassembly/x86/Instruction.cpp`) -> Impact: **727.7** | LOC: 870
- `Instruction::parse` **(Compute Cores)** (@ `Userland/Libraries/LibWasm/Parser/Parser.cpp`) -> Impact: **666.4** | LOC: 629
- `Parser::parse_css_value` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibWeb/CSS/Parser/Parser.cpp`) -> Impact: **456.0** | LOC: 360
- `build_in_table` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibDisassembly/x86/Instruction.cpp`) -> Impact: **421.7** | LOC: 179
- `Lexer::lex_impl` **(Compute Cores)** (@ `Userland/Libraries/LibCpp/Lexer.cpp`) -> Impact: **407.9** | LOC: 578
- `Lexer::lex_impl` **(Compute Cores)** (@ `Userland/Libraries/LibGLSL/Lexer.cpp`) -> Impact: **395.2** | LOC: 551
- `Type1FontProgram::parse_glyph` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibPDF/Fonts/Type1FontProgram.cpp`) -> Impact: **390.1** | LOC: 600

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Userland/Libraries/LibGUI` | 256 | 23359.98 | 20.21% | 41.64% |
| `AK` | 231 | 23283.06 | 25.13% | 24.78% |
| `Userland/Libraries/LibGfx/ImageFormats` | 99 | 22399.34 | 30.67% | 32.19% |
| `Userland/Utilities` | 224 | 22322.3 | 29.85% | 33.77% |
| `Userland/Libraries/LibJS/Runtime` | 325 | 18760.46 | 13.41% | 41.25% |
| `Userland/Libraries/LibWeb/HTML` | 403 | 17542.68 | 8.18% | 47.59% |
| `Userland/Libraries/LibWeb/Layout` | 95 | 11422.56 | 15.1% | 41.68% |
| `Userland/Libraries/LibC` | 131 | 11386.42 | 19.91% | 34.24% |
| `Userland/Libraries/LibShell` | 26 | 11273.38 | 24.09% | 39.3% |
| `Userland/Libraries/LibWeb/CSS` | 150 | 11059.74 | 11.45% | 41.87% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `AK/BitStream.h` -> **100.0%** Exposure
- `AK/JsonObject.cpp` -> **100.0%** Exposure
- `AK/MemoryStream.cpp` -> **100.0%** Exposure
- `AK/NumericLimits.h` -> **100.0%** Exposure
- `AK/Result.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `AK/BigIntBase.h` -> **100.0%** Exposure
- `AK/BitmapView.h` -> **100.0%** Exposure
- `AK/MemMem.h` -> **100.0%** Exposure
- `AK/OptionParser.cpp` -> **100.0%** Exposure
- `AK/RedBlackTree.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Userland/Libraries/LibShell/AST.cpp` -> **296** Orphaned Functions | **0** Duplicates
- `Userland/Libraries/LibWeb/CSS/StyleValues/CSSMathValue.cpp` -> **277** Orphaned Functions | **0** Duplicates
- `Userland/Libraries/LibWeb/DOM/Document.cpp` -> **266** Orphaned Functions | **0** Duplicates
- `Userland/Libraries/LibJS/Bytecode/Op.h` -> **0** Orphaned Functions | **229** Duplicates
- `Userland/Libraries/LibJS/Bytecode/Interpreter.cpp` -> **206** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `Tests/LibCrypto/TestRSA.cpp` -> **99.9998%** Exposure
- `Userland/Libraries/LibCrypto/ASN1/PEM.cpp` -> **99.9925%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `369` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `41666` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Userland/Libraries/LibWeb/CSS/Parser/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.717)
- **Top Global Matches:** file_cluster_6: 8.717, file_cluster_8: 10.033, file_cluster_4: 16.196
- **Magnitude:** 5648.18 | **LOC:** 9504 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **78**; blast radius 0.056; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.6%), Mutation Surface (formerly State Flux) (93.2%), Guard Balance (formerly Safety Score) (56.5%), Complexity Load (formerly Cognitive Load) (39.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parser::parse_css_value` **(Many-Argument Workhorses)** (Impact: 456.0)
  * `Parser::parse_css_value_for_properties` **(Compute Cores)** (Impact: 223.0)
  * `Parser::substitute_attr_function` **(Many-Argument Workhorses)** (Impact: 170.8)
    * *Intent:* // https://drafts.csswg.org/css-values-5/#attr-substitution
  * `Parser::convert_to_font_face_rule` **(Compute Cores)** (Impact: 151.9)
  * `Parser::parse_position_value` **(Many-Argument Workhorses)** (Impact: 126.9)
    * *Intent:* // https://www.w3.org/TR/css-values-4/#position
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 981
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2381`, `structural_boundaries: 2475`, `args: 773`, `func_start: 208`, `class_start: 10`
* *Risk/State:* `state_mutation: 335`, `planned_debt: 14`, `fragile_debt: 55`, `unreferenced_by_name: 177`
* *Architecture:* `api: 2`, `import: 78`
* *Defense:* `safety: 18`, `immutability_locks: 161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 120):` CharacterTypes.h, Debug.h, GenericLexer.h, QuickSort.h, SourceLocation.h, TemporaryChange.h, CSSFontFaceRule.h, CSSImportRule.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `Base/etc/shadow` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibJS/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.008)
- **Top Global Matches:** file_cluster_6: 8.008, file_cluster_8: 11.204, file_cluster_4: 14.967
- **Magnitude:** 3501.78 | **LOC:** 5193 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 0.048; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Debt Markers (formerly Tech Debt) (85.2%), Complexity Load (formerly Cognitive Load) (74.8%), Guard Balance (formerly Safety Score) (59.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parser::parse_class_expression` **(Compute Cores)** (Impact: 191.0)
  * `Parser::parse_secondary_expression` **(Many-Argument Workhorses)** (Impact: 156.7)
  * `Parser::parse_binding_pattern` **(Many-Argument Workhorses)** (Impact: 153.8)
  * `Parser::parse_export_statement` **(Compute Cores)** (Impact: 116.9)
  * `~ScopePusher` **(Compute Cores)** (Impact: 84.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 246 instances
* *State Mutation (weighted view):* 792
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1559`, `structural_boundaries: 905`, `args: 557`, `func_start: 147`, `class_start: 10`
* *Risk/State:* `state_mutation: 300`, `dead_code: 1`, `fragile_debt: 9`, `unreferenced_by_name: 106`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 9`, `immutability_locks: 276`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.048
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 26):` Array.h, CharacterTypes.h, HashTable.h, ScopeGuard.h, StdLibExtras.h, TemporaryChange.h, RegExpObject.h, Regex.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibGfx/ImageFormats/JPEGXLLoader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.391)
- **Top Global Matches:** file_cluster_4: 5.391, file_cluster_15: 10.139, file_cluster_6: 11.224
- **Magnitude:** 2456.34 | **LOC:** 3882 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 90.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.0%), Complexity Load (formerly Cognitive Load) (51.0%)
- **Documentation Coverage:** 91.9118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_hf_coefficients` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* // I.4 - Decoding of quantized HF coefficients
  * `get_properties` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `read_frame_header` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `read_modular_bitstream` **(Compute Cores)** (Impact: 67.0)
  * `dct_select_to_dct_size` **(Compute Cores)** (Impact: 45.1)
    * *Intent:* // NOTE: In the spec, DCT matrices use "matrices order" so DCT16x8 is actually // 16 rows and 8 colu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 1000
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 586`, `structural_boundaries: 658`, `args: 258`, `func_start: 129`, `class_start: 61`
* *Risk/State:* `state_mutation: 386`, `dead_code: 1`, `planned_debt: 20`, `fragile_debt: 14`, `unreferenced_by_name: 14`
* *Architecture:* `api: 6`, `import: 19`
* *Defense:* `safety: 6`, `doc: 61`, `immutability_locks: 218`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 35):` BitStream.h, ConstrainedStream.h, Debug.h, Endian.h, Enumerate.h, FixedArray.h, String.h, Brotli.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibWeb/DOM/Document.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.833)
- **Top Global Matches:** file_cluster_15: 7.833, file_cluster_4: 8.886, file_cluster_11: 9.196
- **Magnitude:** 2419.84 | **LOC:** 5651 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **130**; blast radius 0.038; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (94.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Document::shared_declarative_refresh_steps` **(Many-Argument Workhorses)** (Impact: 70.1)
    * *Intent:* // https://html.spec.whatwg.org/multipage/semantics.html#shared-declarative-refresh-steps
  * `Document::create_event` **(Compute Cores)** (Impact: 60.2)
    * *Intent:* // https://dom.spec.whatwg.org/#dom-document-createevent
  * `Document::dispatch_events_for_animation_if_necessary` **(Compute Cores)** (Impact: 51.9)
    * *Intent:* // https://www.w3.org/TR/css-animations-2/#event-dispatch
  * `is_valid_name_start_character` **(Compute Cores)** (Impact: 43.4)
    * *Intent:* // https://www.w3.org/TR/xml/#NT-NameStartChar
  * `Document::update_for_history_step_application` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* // https://html.spec.whatwg.org/multipage/browsing-the-web.html#update-document-for-history-step-app...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 554
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 829`, `structural_boundaries: 968`, `args: 320`, `func_start: 308`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 234`, `planned_debt: 4`, `fragile_debt: 130`, `unreferenced_by_name: 266`
* *Architecture:* `import: 130`
* *Defense:* `immutability_locks: 200`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 181):` CharacterTypes.h, Debug.h, GenericLexer.h, InsertionSort.h, StringBuilder.h, Utf8View.h, Timer.h, Array.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibGfx/ImageFormats/JBIG2Loader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.549)
- **Top Global Matches:** file_cluster_6: 5.549, file_cluster_4: 11.938, file_cluster_8: 12.8
- **Magnitude:** 2319.88 | **LOC:** 3761 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 0.042; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `symbol_dictionary_decoding_procedure` **(Many-Argument Workhorses)** (Impact: 141.0)
    * *Intent:* // 6.5 Symbol Dictionary Decoding Procedure
  * `text_region_decoding_procedure` **(Many-Argument Workhorses)** (Impact: 109.0)
    * *Intent:* // 6.4 Text Region Decoding Procedure
  * `decode_text_region` **(Many-Argument Workhorses)** (Impact: 86.8)
  * `decode_data` **(Compute Cores)** (Impact: 76.4)
  * `generic_refinement_region_decoding_procedure` **(Many-Argument Workhorses)** (Impact: 76.2)
    * *Intent:* // 6.3 Generic Refinement Region Decoding Procedure
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 223 instances
* *State Mutation (weighted view):* 912
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 641`, `structural_boundaries: 498`, `args: 237`, `func_start: 74`, `class_start: 15`
* *Risk/State:* `state_mutation: 466`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 14`
* *Architecture:* `import: 12`
* *Defense:* `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 21):` BitStream.h, Debug.h, Enumerate.h, GenericShorthands.h, IntegralMath.h, Utf16View.h, BilevelImage.h, CCITTDecoder.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibGfx/Painter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.942)
- **Top Global Matches:** file_cluster_4: 5.942, file_cluster_15: 10.461, file_cluster_6: 11.445
- **Magnitude:** 2296.38 | **LOC:** 2546 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **25**; blast radius 0.193; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.2%), Complexity Load (formerly Cognitive Load) (91.1%), Guard Balance (formerly Safety Score) (66.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Painter::draw_line` **(Many-Argument Workhorses)** (Impact: 155.6)
  * `Painter::split_text_into_directional_runs` **(Many-Argument Workhorses)** (Impact: 98.9)
  * `do_draw_scaled_bitmap` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `draw_text_line` **(Many-Argument Workhorses)** (Impact: 69.3)
  * `Painter::draw_triangle` **(Many-Argument Workhorses)** (Impact: 56.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 233 instances
* *State Mutation (weighted view):* 733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 475`, `args: 162`, `func_start: 114`, `class_start: 5`
* *Risk/State:* `state_mutation: 267`, `planned_debt: 2`, `fragile_debt: 28`, `unreferenced_by_name: 47`
* *Architecture:* `api: 1`, `import: 25`
* *Defense:* `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 30):` Assertions.h, Debug.h, Function.h, Math.h, Memory.h, Queue.h, QuickSort.h, Stack.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibShell/AST.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.614)
- **Top Global Matches:** file_cluster_15: 7.614, file_cluster_4: 8.085, file_cluster_16: 9.499
- **Magnitude:** 2288.52 | **LOC:** 3973 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.046; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.6%), Guard Balance (formerly Safety Score) (55.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Execute::for_each_entry` **(Many-Argument Workhorses)** (Impact: 86.8)
  * `AK::Formatter::format` **(Compute Cores)** (Impact: 70.0)
    * *Intent:* #include "Shell.h" #include <AK/Find.h> #include <AK/MemoryStream.h> #include <AK/ScopeGuard.h> #inc...
  * `MatchExpr::run` **(Compute Cores)** (Impact: 59.0)
  * `Node::complete_for_editor` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `ForLoop::run` **(Compute Cores)** (Impact: 48.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 739`, `structural_boundaries: 837`, `args: 464`, `func_start: 305`
* *Risk/State:* `state_mutation: 134`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 296`
* *Architecture:* `io: 1`, `import: 15`
* *Defense:* `immutability_locks: 138`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 24):` Find.h, MemoryStream.h, ScopeGuard.h, ScopedValueRollback.h, String.h, StringBuilder.h, AST.h, Highlight.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibWeb/HTML/Parser/HTMLParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.899)
- **Top Global Matches:** file_cluster_8: 8.899, file_cluster_6: 9.853, file_cluster_4: 17.685
- **Magnitude:** 2211.56 | **LOC:** 4972 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **38**; blast radius 0.063; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.8%), Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HTMLParser::handle_in_body` **(Compute Cores)** (Impact: 362.1)
    * *Intent:* // https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inbody
  * `HTMLParser::process_using_the_rules_for` **(Compute Cores)** (Impact: 88.7)
  * `HTMLParser::handle_in_head` **(Compute Cores)** (Impact: 79.6)
  * `HTMLParser::serialize_html_fragment` **(Many-Argument Workhorses)** (Impact: 78.7)
    * *Intent:* // https://html.spec.whatwg.org/multipage/parsing.html#html-fragment-serialisation-algorithm
  * `HTMLParser::handle_in_select` **(Compute Cores)** (Impact: 66.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 919`, `structural_boundaries: 695`, `args: 336`, `func_start: 81`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 175`, `planned_debt: 4`, `fragile_debt: 41`, `unreferenced_by_name: 69`
* *Architecture:* `import: 38`
* *Defense:* `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 51):` Debug.h, SourceLocation.h, Utf32View.h, Decoder.h, ExceptionOrUtils.h, MainThreadVM.h, LengthStyleValue.h, PercentageStyleValue.h...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `Userland/Utilities/jbig2-from-json.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.111)
- **Top Global Matches:** file_cluster_6: 8.111, file_cluster_8: 9.264, file_cluster_4: 16.033
- **Magnitude:** 2182.94 | **LOC:** 2962 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jbig2_pattern_dictionary_from_json` **(Many-Argument Workhorses)** (Impact: 150.1)
  * `jbig2_text_region_flags_from_json` **(Compute Cores)** (Impact: 76.8)
  * `jbig2_segment_from_json` **(Compute Cores)** (Impact: 75.6)
  * `jbig2_symbol_dictionary_from_json` **(Many-Argument Workhorses)** (Impact: 61.6)
  * `jbig2_halftone_region_from_json` **(Many-Argument Workhorses)** (Impact: 56.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 245 instances
* *State Mutation (weighted view):* 756
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 684`, `structural_boundaries: 803`, `args: 146`, `func_start: 65`, `class_start: 4`
* *Risk/State:* `state_mutation: 266`, `fragile_debt: 15`, `unreferenced_by_name: 1`
* *Architecture:* `import: 15`
* *Defense:* `immutability_locks: 182`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 28):` Enumerate.h, IntegralMath.h, JsonObject.h, JsonValue.h, LexicalPath.h, MemoryStream.h, ArgsParser.h, File.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibWeb/CSS/StyleComputer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.59)
- **Top Global Matches:** file_cluster_6: 6.59, file_cluster_4: 12.137, file_cluster_8: 13.673
- **Magnitude:** 2102.64 | **LOC:** 2886 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **75**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.5%), Mutation Surface (formerly State Flux) (90.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `StyleComputer::compute_font_for_style_values` **(Many-Argument Workhorses)** (Impact: 270.2)
  * `StyleComputer::for_each_property_expanding_shorthands` **(Many-Argument Workhorses)** (Impact: 194.9)
  * `StyleComputer::collect_matching_rules` **(Many-Argument Workhorses)** (Impact: 122.6)
  * `StyleComputer::make_rule_cache_for_cascade_origin` **(Compute Cores)** (Impact: 84.2)
  * `StyleComputer::compute_cascaded_values` **(Many-Argument Workhorses)** (Impact: 81.7)
    * *Intent:* // https://www.w3.org/TR/css-cascade/#cascading // https://drafts.csswg.org/css-cascade-5/#layering
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 378
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 680`, `structural_boundaries: 599`, `args: 262`, `func_start: 70`, `class_start: 6`
* *Risk/State:* `state_mutation: 146`, `planned_debt: 8`, `fragile_debt: 29`, `unreferenced_by_name: 52`
* *Architecture:* `import: 75`
* *Defense:* `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 100):` BinarySearch.h, Debug.h, Error.h, Find.h, Function.h, HashMap.h, Math.h, QuickSort.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibWeb/Layout/GridFormattingContext.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.571)
- **Top Global Matches:** file_cluster_8: 8.571, file_cluster_6: 9.146, file_cluster_4: 17.173
- **Magnitude:** 2022.48 | **LOC:** 2510 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GridFormattingContext::layout_absolutely_positioned_element` **(Compute Cores)** (Impact: 72.8)
  * `GridFormattingContext::resolve_grid_position` **(Compute Cores)** (Impact: 66.1)
  * `GridFormattingContext::distribute_extra_space_across_spanned_tracks_base_size` **(Many-Argument Workhorses)** (Impact: 63.3)
  * `GridFormattingContext::resolve_track_spacing` **(Compute Cores)** (Impact: 61.3)
  * `GridFormattingContext::increase_sizes_to_accommodate_spanning_items_crossing_content_sized_tracks` **(Compute Cores)** (Impact: 59.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 255 instances
* *State Mutation (weighted view):* 795
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 635`, `structural_boundaries: 501`, `args: 138`, `func_start: 70`, `class_start: 3`
* *Risk/State:* `state_mutation: 285`, `planned_debt: 1`, `fragile_debt: 17`, `unreferenced_by_name: 68`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 188`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 13):` Node.h, Box.h, GridFormattingContext.h, ReplacedBox.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibLine/Editor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.009)
- **Top Global Matches:** file_cluster_6: 6.009, file_cluster_4: 9.581, file_cluster_8: 15.808
- **Magnitude:** 1908.64 | **LOC:** 2401 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **27**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Debt Markers (formerly Tech Debt) (86.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Editor::handle_read_event` **(I/O & Config Routines)** (Impact: 170.8)
  * `actual_rendered_string_length_step` **(Many-Argument Workhorses)** (Impact: 112.9)
  * `Editor::refresh_display` **(I/O & Config Routines)** (Impact: 67.5)
  * `merge` **(Many-Argument Workhorses)** (Impact: 60.3)
  * `Editor::vt_dsr` **(I/O & Config Routines)** (Impact: 58.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 247 instances
* *State Mutation (weighted view):* 796
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 597`, `structural_boundaries: 359`, `args: 113`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `state_mutation: 302`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 47`
* *Architecture:* `io: 1`, `import: 27`
* *Defense:* `safety: 1`, `immutability_locks: 45`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 37):` CharacterTypes.h, Debug.h, GenericLexer.h, JsonObject.h, MemoryStream.h, RedBlackTree.h, ScopeGuard.h, ScopedValueRollback.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibRegex/RegexParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.345)
- **Top Global Matches:** file_cluster_6: 7.345, file_cluster_8: 9.844, file_cluster_4: 15.143
- **Magnitude:** 1890.52 | **LOC:** 2795 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ECMA262Parser::parse_nonempty_class_ranges` **(Compute Cores)** (Impact: 136.9)
  * `PosixExtendedParser::parse_sub_expression` **(Many-Argument Workhorses)** (Impact: 136.6)
  * `AbstractPosixParser::parse_bracket_expression` **(Compute Cores)** (Impact: 117.7)
    * *Intent:* // ============================= // Abstract Posix Parser // =============================
  * `ECMA262Parser::parse_character_escape` **(Many-Argument Workhorses)** (Impact: 58.5)
  * `ECMA262Parser::read_capture_group_specifier` **(Compute Cores)** (Impact: 57.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 682`, `structural_boundaries: 481`, `args: 349`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `state_mutation: 180`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 56`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 19`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 19):` AnyOf.h, ByteString.h, CharacterTypes.h, Debug.h, GenericLexer.h, ScopeGuard.h, StringBuilder.h, StringUtils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibJS/Bytecode/Interpreter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.858)
- **Top Global Matches:** file_cluster_15: 6.858, file_cluster_4: 8.104, file_cluster_16: 8.858
- **Magnitude:** 1861.04 | **LOC:** 3676 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **31**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%), Mutation Surface (formerly State Flux) (39.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `put_by_property_key` **(Many-Argument Workhorses)** (Impact: 105.3)
  * `put_by_value` **(Many-Argument Workhorses)** (Impact: 83.4)
  * `get_by_value` **(Many-Argument Workhorses)** (Impact: 64.9)
  * `format_operand` **(Compute Cores)** (Impact: 60.2)
  * `get_by_id` **(Many-Argument Workhorses)** (Impact: 51.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 455`, `structural_boundaries: 904`, `args: 462`, `func_start: 248`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 140`, `planned_debt: 3`, `fragile_debt: 12`, `unreferenced_by_name: 206`
* *Architecture:* `import: 31`
* *Defense:* `test: 2`, `immutability_locks: 414`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 49):` Debug.h, HashTable.h, TemporaryChange.h, AST.h, BasicBlock.h, Generator.h, Instruction.h, Interpreter.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibJS/Bytecode/ASTCodegen.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.433)
- **Top Global Matches:** file_cluster_6: 7.433, file_cluster_4: 9.304, file_cluster_15: 16.524
- **Magnitude:** 1859.94 | **LOC:** 3561 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.4%), Mutation Surface (formerly State Flux) (84.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AssignmentExpression::generate_bytecode` **(Many-Argument Workhorses)** (Impact: 141.1)
  * `BinaryExpression::generate_bytecode` **(Compute Cores)** (Impact: 138.8)
  * `for_in_of_body_evaluation` **(Many-Argument Workhorses)** (Impact: 104.1)
    * *Intent:* // 14.7.5.7 ForIn/OfBodyEvaluation ( lhs, stmt, iteratorRecord, iterationKind, lhsKind, labelSet [ ,...
  * `generate_object_binding_pattern_bytecode` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `constant_fold_binary_expression` **(Compute Cores)** (Impact: 58.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 122 instances
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 596`, `args: 242`, `func_start: 82`, `class_start: 5`
* *Risk/State:* `state_mutation: 132`, `planned_debt: 2`, `fragile_debt: 17`, `unreferenced_by_name: 69`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 23):` Find.h, Queue.h, AST.h, Generator.h, Instruction.h, Op.h, Register.h, StringTable.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibDisassembly/x86/Instruction.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.775)
- **Top Global Matches:** file_cluster_6: 7.775, file_cluster_4: 8.606, file_cluster_15: 15.738
- **Magnitude:** 1808.14 | **LOC:** 2541 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.5%), Mutation Surface (formerly State Flux) (86.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Instruction::to_byte_string_internal` **(Many-Argument Workhorses)** (Impact: 727.7)
  * `build_in_table` **(Many-Argument Workhorses)** (Impact: 421.7)
  * `Instruction::to_byte_string` **(Compute Cores)** (Impact: 41.8)
  * `MemoryOrRegisterReference::sib_to_byte_string` **(Compute Cores)** (Impact: 36.1)
  * `MemoryOrRegisterReference::to_byte_string_a16` **(I/O & Config Routines)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 148`, `args: 82`, `func_start: 57`
* *Risk/State:* `state_mutation: 99`, `fragile_debt: 36`, `unreferenced_by_name: 26`
* *Architecture:* `import: 3`
* *Defense:* `test: 8`, `sync_locks: 1`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` StringBuilder.h, Instruction.h, Interpreter.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibURL/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.434)
- **Top Global Matches:** file_cluster_6: 5.434, file_cluster_4: 11.498, file_cluster_8: 13.373
- **Magnitude:** 1770.06 | **LOC:** 1772 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **13**; blast radius 0.066; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.0%), Guard Balance (formerly Safety Score) (73.8%), Debt Markers (formerly Tech Debt) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parser::basic_parse` **(Many-Argument Workhorses)** (Impact: 885.2)
    * *Intent:* // https://url.spec.whatwg.org/#concept-basic-url-parser
  * `parse_ipv6_address` **(Compute Cores)** (Impact: 73.6)
    * *Intent:* // https://url.spec.whatwg.org/#concept-ipv6-parser
  * `parse_ipv4_number` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* // https://url.spec.whatwg.org/#ipv4-number-parser
  * `serialize_ipv6_address` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* // https://url.spec.whatwg.org/#concept-ipv6-serializer
  * `domain_to_ascii` **(Compute Cores)** (Impact: 21.3)
    * *Intent:* // https://url.spec.whatwg.org/#concept-domain-to-ascii
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 560
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 144`, `args: 35`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 192`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 19):` ByteString.h, CharacterTypes.h, Debug.h, IntegralMath.h, Optional.h, SourceLocation.h, StringBuilder.h, StringUtils.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibGfx/ImageFormats/JBIG2Writer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.343)
- **Top Global Matches:** file_cluster_8: 7.343, file_cluster_6: 11.468, file_cluster_4: 19.794
- **Magnitude:** 1752.84 | **LOC:** 2759 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `symbol_dictionary_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 165.5)
    * *Intent:* // 6.5 Symbol Dictionary Decoding Procedure, but in reverse.
  * `text_region_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 124.2)
    * *Intent:* // 6.4 Text Region Decoding Procedure, but in reverse.
  * `encode_text_region` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `generic_refinement_region_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 82.8)
    * *Intent:* // 6.3 Generic Refinement Region Decoding Procedure, but in reverse.
  * `generic_region_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 73.4)
    * *Intent:* // 6.2 Generic region decoding procedure, but in reverse.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 397`, `structural_boundaries: 402`, `args: 161`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `state_mutation: 346`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 14`, `unreferenced_by_name: 7`
* *Architecture:* `import: 17`
* *Defense:* `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 29):` BitStream.h, Enumerate.h, HashMap.h, IntegralMath.h, MemoryStream.h, NonnullOwnPtr.h, StdLibExtras.h, Stream.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibShell/Shell.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.221)
- **Top Global Matches:** file_cluster_4: 6.221, file_cluster_6: 8.778, file_cluster_15: 12.93
- **Magnitude:** 1744.32 | **LOC:** 2734 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **42**; blast radius 0.036; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Debt Markers (formerly Tech Debt) (91.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Shell::run_command` **(Compute Cores)** (Impact: 131.8)
  * `Shell::complete_via_program_itself` **(Many-Argument Workhorses)** (Impact: 112.0)
  * `do_escape` **(Many-Argument Workhorses)** (Impact: 74.4)
  * `Shell::complete_path` **(Many-Argument Workhorses)** (Impact: 72.2)
  * `Shell::prompt` **(Compute Cores)** (Impact: 69.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 683`, `structural_boundaries: 537`, `args: 157`, `func_start: 110`, `class_start: 7`
* *Risk/State:* `state_mutation: 129`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 66`
* *Architecture:* `io: 2`, `import: 42`
* *Defense:* `safety: 24`, `immutability_locks: 97`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 59):` CharacterTypes.h, Debug.h, Function.h, GenericLexer.h, JsonParser.h, LexicalPath.h, QuickSort.h, ScopeGuard.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibMedia/Video/VP9/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.321)
- **Top Global Matches:** file_cluster_4: 5.321, file_cluster_15: 8.309, file_cluster_16: 9.767
- **Magnitude:** 1729.78 | **LOC:** 1783 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Complexity Load (formerly Cognitive Load) (81.6%), Guard Balance (formerly Safety Score) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parser::residual` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `Parser::uncompressed_header` **(Compute Cores)** (Impact: 44.8)
    * *Intent:* /* (6.2) */
  * `Parser::find_reference_motion_vectors` **(Many-Argument Workhorses)** (Impact: 35.7)
    * *Intent:* // 6.5.1 Find MV refs syntax // find_mv_refs( refFrame, block ) in the spec.
  * `Parser::decode_partition` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `Parser::inter_block_mode_info` **(Many-Argument Workhorses)** (Impact: 34.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 250 instances
* *State Mutation (weighted view):* 808
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 415`, `args: 103`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `state_mutation: 308`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 67`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 14):` MemoryStream.h, Context.h, Decoder.h, Point.h, Size.h, WorkerThread.h, Parser.h, Utilities.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibGUI/TextEditor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.089)
- **Top Global Matches:** file_cluster_15: 8.089, file_cluster_4: 8.325, file_cluster_11: 9.439
- **Magnitude:** 1687.54 | **LOC:** 2661 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **29**; blast radius 0.056; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TextEditor::paint_event` **(Compute Cores)** (Impact: 203.0)
  * `TextEditor::keydown_event` **(Compute Cores)** (Impact: 161.3)
  * `TextEditor::text_position_at_content_position` **(Compute Cores)** (Impact: 41.8)
  * `TextEditor::mousedown_event` **(Compute Cores)** (Impact: 40.9)
  * `TextEditor::recompute_visual_lines` **(Compute Cores)** (Impact: 40.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 163 instances
* *State Mutation (weighted view):* 523
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 438`, `args: 132`, `func_start: 146`
* *Risk/State:* `state_mutation: 197`, `fragile_debt: 8`, `unreferenced_by_name: 140`
* *Architecture:* `import: 29`
* *Defense:* `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 46):` CharacterTypes.h, Debug.h, ScopeGuard.h, StringBuilder.h, TemporaryChange.h, Timer.h, Action.h, AutocompleteProvider.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Kernel/Arch/aarch64/CPUID.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.198)
- **Top Global Matches:** file_cluster_3: 7.198, file_cluster_8: 21.045, file_cluster_6: 33.858
- **Magnitude:** 1685.98 | **LOC:** 1495 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.028; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cpu_feature_to_name` **(Compute Cores)** (Impact: 357.9)
    * *Intent:* // https://developer.arm.com/downloads/-/exploration-tools/feature-names-for-a-profile
  * `cpu_feature_to_description` **(Compute Cores)** (Impact: 356.4)
    * *Intent:* // https://developer.arm.com/downloads/-/exploration-tools/feature-names-for-a-profile
  * `detect_cpu_features` **(I/O & Config Routines)** (Impact: 268.8)
  * `detect_physical_address_bit_width` **(I/O & Config Routines)** (Impact: 12.2)
  * `build_cpu_feature_names` **(Compute Cores)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 642
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 733`, `structural_boundaries: 505`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 214`, `planned_debt: 5`, `fragile_debt: 5`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` CPUID.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibGfx/ImageFormats/JPEG2000Loader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.155)
- **Top Global Matches:** file_cluster_6: 6.155, file_cluster_4: 10.677, file_cluster_8: 14.837
- **Magnitude:** 1682.04 | **LOC:** 2735 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 0.04; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert_to_bitmap` **(Compute Cores)** (Impact: 125.9)
  * `read_one_packet_header` **(Many-Argument Workhorses)** (Impact: 105.0)
  * `decode_jpeg2000_header` **(Many-Argument Workhorses)** (Impact: 75.2)
  * `parse_codestream_main_header` **(Compute Cores)** (Impact: 72.5)
  * `parse_codestream_tile_header` **(Compute Cores)** (Impact: 68.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 187 instances
* *State Mutation (weighted view):* 665
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 455`, `args: 155`, `func_start: 64`, `class_start: 30`
* *Risk/State:* `state_mutation: 291`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 13`, `unreferenced_by_name: 10`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 101`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.04
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 23):` BitStream.h, Debug.h, Enumerate.h, MemoryStream.h, Profile.h, JPEG2000Boxes.h, Reader.h, JPEG2000BitplaneDecoding.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Userland/Libraries/LibVT/Terminal.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.785)
- **Top Global Matches:** file_cluster_4: 5.785, file_cluster_6: 9.882, file_cluster_15: 11.495
- **Magnitude:** 1680.72 | **LOC:** 1803 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Terminal::handle_key_press` **(Many-Argument Workhorses)** (Impact: 154.8)
  * `Terminal::SGR` **(Compute Cores)** (Impact: 126.0)
  * `Terminal::execute_csi_sequence` **(Many-Argument Workhorses)** (Impact: 123.3)
  * `Terminal::set_size` **(Many-Argument Workhorses)** (Impact: 88.8)
    * *Intent:* #ifndef KERNEL
  * `Terminal::execute_escape_sequence` **(Many-Argument Workhorses)** (Impact: 74.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 166 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 241`, `args: 102`, `func_start: 82`
* *Risk/State:* `state_mutation: 184`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 78`
* *Architecture:* `import: 7`
* *Defense:* `safety: 3`, `immutability_locks: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 9):` Debug.h, Queue.h, StringBuilder.h, StringView.h, TemporaryChange.h, VirtualConsole.h, Color.h, Terminal.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `AK/MemMem.h` (CPP) | Magnitude: 150.62 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 49, branch: 39, state_mutation: 36
- `Userland/Libraries/LibWeb/DOM/NonElementParentNode.h` (CPP) | Magnitude: 8.94 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, import: 6, explicit_casts: 3
- `Userland/Libraries/LibJS/Runtime/Array.h` (CPP) | Magnitude: 11.52 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, immutability_locks: 17, structural_boundaries: 16, args: 13
- `Userland/Libraries/LibRIFF/Details.h` (CPP) | Magnitude: 12.88 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 20, immutability_locks: 9, args: 8
- `Userland/Libraries/LibTest/Randomized/Chunk.h` (CPP) | Magnitude: 4.26 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, args: 2, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `Tests/LibWeb/Text/input/HTML/get-innerHTML.html` (HTML) | Magnitude: 0.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, func_start: 5, core_var_decl: 5, design_snake_case: 5
- `Userland/Applications/CharacterMap/CharacterSearchWidget.cpp` (CPP) | Magnitude: 33.42 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 22, pointers: 18, state_mutation: 8
- `Userland/Libraries/LibJS/Tests/object-expression-numeric-property.js` (JAVASCRIPT) | Magnitude: 15.88 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 40, test: 4, core_var_decl: 4, structural_boundaries: 2
- `Userland/Libraries/LibJS/Tests/try-finally-break.js` (JAVASCRIPT) | Magnitude: 69.0 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 382, test: 135, safety: 89, structural_boundaries: 72
- `Tests/LibWeb/Text/input/HTML/relList-attribute.html` (HTML) | Magnitude: 0.0 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 30, core_var_decl: 6, func_start: 3, design_camel_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Userland/Libraries/LibMedia/Containers/Matroska/Document.h` (CPP) | Magnitude: 164.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 167, structural_boundaries: 81, func_start: 61, core_var_decl: 53
- `Kernel/Arch/aarch64/Time/PL031.cpp` (CPP) | Magnitude: 12.6 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, import: 6, pointers: 6
- `AK/AtomicRefCounted.h` (CPP) | Magnitude: 21.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 21, api: 7, immutability_locks: 7
- `Userland/Applications/Spreadsheet/SpreadsheetView.h` (CPP) | Magnitude: 47.14 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 47, args: 25, immutability_locks: 18
- `Userland/Services/ChessEngine/ChessEngine.cpp` (CPP) | Magnitude: 27.7 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 17, core_var_decl: 10, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Userland/Libraries/LibELF/DynamicLinker.cpp` (CPP) | Magnitude: 370.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 433, structural_boundaries: 154, pointers: 111, branch: 101
- `Userland/Libraries/LibDNS/PacketHeader.h` (CPP) | Magnitude: 91.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 39, func_start: 34, api: 32
- `Tests/LibWeb/Text/input/ResizeObserver/disconnect.html` (HTML) | Magnitude: 36.92 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 14, core_var_decl: 10, design_snake_case: 7
- `Userland/Libraries/LibJS/Tests/builtins/Temporal/Now/Now.plainDateISO.js` (JAVASCRIPT) | Magnitude: 3.26 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 49, test: 20, structural_boundaries: 12, args: 12
- `Tests/LibWeb/Text/input/element-scrollby-event.html` (HTML) | Magnitude: 35.0 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 26, core_var_decl: 5, design_snake_case: 5, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Tests/LibWeb/Layout/input/block-and-inline/float-should-avoid-inline-block.html` (HTML) | Magnitude: 1.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 3, decorators: 3, core_var_decl: 2
- `Userland/Applications/Piano/ProcessorParameterWidget/Dropdown.h` (CPP) | Magnitude: 12.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 8, import: 8, args: 5
- `Userland/Libraries/LibWeb/Bindings/PlatformObject.h` (CPP) | Magnitude: 5.9 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 40, immutability_locks: 29, args: 20
- `AK/ByteString.h` (CPP) | Magnitude: 160.14 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 225, immutability_locks: 107, args: 84, structural_boundaries: 81
- `Userland/Libraries/LibGUI/Model.h` (CPP) | Magnitude: 88.52 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 97, immutability_locks: 61, args: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `Toolchain/BuildClang.sh` (SHELL) | Magnitude: 150.4 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 107, branch: 38, core_var_decl: 38
- `Tests/LibWeb/Text/input/HTML/CanvasRenderingContext2D-get-image-data-correctness.html` (HTML) | Magnitude: 0.08 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 13, branch: 4, structural_boundaries: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Userland/Libraries/LibWeb/Painting/SVGGraphicsPaintable.cpp` (CPP) | Magnitude: 4.82 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 7, immutability_locks: 5, structural_boundaries: 3, func_start: 3
- `Tests/LibC/TestWchar.cpp` (CPP) | Magnitude: 180.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 369, test: 170, core_var_decl: 139, design_snake_case: 139
- `Kernel/Devices/Serial/16550/PCISerial16550.cpp` (CPP) | Magnitude: 31.4 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 18, branch: 10, core_var_decl: 10
- `Userland/Utilities/pmemdump.cpp` (CPP) | Magnitude: 52.62 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 17, core_var_decl: 16, design_snake_case: 16
- `Meta/Lagom/Fuzzers/FuzzMatroskaReader.cpp` (CPP) | Magnitude: 4.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, import: 2, explicit_casts: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Kernel/FileSystem/FATFS/Definitions.h` (CPP) | Magnitude: 17.12 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 8, core_var_decl: 7, design_pascal_case: 7
- `Userland/Applications/PixelPaint/IconBag.h` (CPP) | Magnitude: 15.84 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 2, import: 2, class_start: 1
- `AK/JsonParser.h` (CPP) | Magnitude: 3.16 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, macros: 3, import: 2
- `Userland/Libraries/LibAudio/QOALoader.h` (CPP) | Magnitude: 17.44 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 21, safety: 10, args: 8
- `AK/MemoryStream.h` (CPP) | Magnitude: 11.9 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 42, args: 16, safety: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Kernel/Arch/x86_64/SIMDState.h` (CPP) | Magnitude: 16.94 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, core_var_decl: 16, design_upper_case: 14, structural_boundaries: 4
- `Kernel/API/POSIX/errno.h` (CPP) | Magnitude: 16.82 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 85, indent_spaces: 85, macros: 4, reflection_metaprogramming: 2
- `Tests/LibWeb/Text/input/hit_testing/float-with-inline-sibling-after.html` (HTML) | Magnitude: 5.96 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 7, api: 4, func_start: 3
- `Tests/AK/TestByteString.cpp` (CPP) | Magnitude: 67.34 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 182, test: 93, core_var_decl: 43, design_snake_case: 43
- `Tests/LibWeb/Layout/input/grid/grid-placement-shorthand-single-custom-ident.html` (HTML) | Magnitude: 15.68 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 4, decorators: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Userland/Libraries/LibCompress/Gzip.cpp` (CPP) | Magnitude: 111.54 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 41, branch: 32, pointers: 28
- `Userland/DevTools/Profiler/ProfileModel.cpp` (CPP) | Magnitude: 114.9 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 113, branch: 46, structural_boundaries: 44, pointers: 33
- `AK/RedBlackTree.h` (CPP) | Magnitude: 594.08 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 479, pointers: 240, state_mutation: 120, branch: 113
- `Userland/Libraries/LibWeb/Loader/ResourceLoader.cpp` (CPP) | Magnitude: 277.84 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 351, structural_boundaries: 126, branch: 81, args: 52
- `Userland/Games/Snake/Game.cpp` (CPP) | Magnitude: 225.8 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 230, branch: 68, structural_boundaries: 48, core_var_decl: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `AK/Weakable.h` (CPP) | Magnitude: 20.74 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 41, generics: 11, func_start: 8
- `Meta/generate-libwasm-spec-test.py` (PYTHON) | Magnitude: 380.5 | Delta: **0.162** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 294, structural_boundaries: 97, branch: 94, core_var_decl: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `Userland/Libraries/LibWeb/Layout/InlineFormattingContext.cpp` (CPP) | Magnitude: 260.32 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 302, core_var_decl: 89, design_snake_case: 89, branch: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Userland/Libraries/LibJS/Tests/builtins/Object/Object.seal.js` (JAVASCRIPT) | Magnitude: 21.26 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 59, test: 27, structural_boundaries: 11, args: 10
- `Userland/Libraries/LibC/sys/mman.cpp` (CPP) | Magnitude: 55.64 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 28, args: 21, pointers: 19
- `Ports/RetroArch/package.sh` (SHELL) | Magnitude: 16.54 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: core_var_decl: 12, state_mutation: 11, design_snake_case: 11, indent_spaces: 10
- `Userland/Libraries/LibJS/Tests/builtins/Intl/ListFormat/ListFormat.prototype.resolvedOptions.js` (JAVASCRIPT) | Magnitude: 15.66 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 31, test: 11, structural_boundaries: 7, args: 7
- `Ports/fribidi/package.sh` (SHELL) | Magnitude: 13.46 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 11, core_var_decl: 8, state_mutation: 7, design_snake_case: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Userland/Libraries/LibJS/Runtime/Intl/Collator.cpp` (CPP) | Magnitude: 83.3 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 57, branch: 33, structural_boundaries: 14, state_mutation: 9
- `Userland/Utilities/pkg/AvailablePortDatabase.cpp` (CPP) | Magnitude: 76.9 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 47, core_var_decl: 33, design_snake_case: 33
- `Userland/Applications/SystemMonitor/NetworkStatisticsWidget.cpp` (CPP) | Magnitude: 32.66 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 105, pointers: 26, structural_boundaries: 17, core_var_decl: 17
- `Userland/Libraries/LibC/arpa/inet.cpp` (CPP) | Magnitude: 74.94 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 24, core_var_decl: 14, design_snake_case: 14
- `Userland/Libraries/LibWeb/Painting/ShadowPainting.cpp` (CPP) | Magnitude: 129.88 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 444, structural_boundaries: 164, core_var_decl: 153, design_snake_case: 153

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Userland/Libraries/LibGfx/ImageFormats/JBIG2Writer.cpp` -> Churn: **89.9%** | Cog Load: 69.7856% | Debt: 44.8457%
- `Userland/Services/SSHServer/SSHClient.cpp` -> Churn: **88.87%** | Cog Load: 18.485% | Debt: 99.9996%
- `Userland/Libraries/LibGfx/ImageFormats/JBIG2Loader.cpp` -> Churn: **75.23%** | Cog Load: 92.5273% | Debt: 30.2363%
- `AK/Math.h` -> Churn: **72.05%** | Cog Load: 45.0957% | Debt: 64.6232%
- `Userland/Libraries/LibSSH/Peer.cpp` -> Churn: **65.4%** | Cog Load: 16.3432% | Debt: 99.9997%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Userland/Libraries/LibGfx/ImageFormats/JPEGXLLoader.cpp` -> **Lucas CHOLLET** (90.9% isolated ownership) | Magnitude: 2456.34
- `Userland/Libraries/LibGfx/ImageFormats/JBIG2Loader.cpp` -> **Nico Weber** (100.0% isolated ownership) | Magnitude: 2319.88
- `Userland/Utilities/jbig2-from-json.cpp` -> **Nico Weber** (100.0% isolated ownership) | Magnitude: 2182.94
- `Userland/Libraries/LibLine/Editor.cpp` -> **Ali Mohammad Pur** (100.0% isolated ownership) | Magnitude: 1908.64
- `Userland/Libraries/LibGfx/ImageFormats/JBIG2Writer.cpp` -> **Nico Weber** (100.0% isolated ownership) | Magnitude: 1752.84

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `AK/Types.h` -> **Severity: 3296.5** (Blast Radius: 32.965 * Doc Risk: 100.0%)
- `AK/StdLibExtras.h` -> **Severity: 1660.6** (Blast Radius: 16.606 * Doc Risk: 100.0%)
- `Tests/LibWeb/Text/input/include.js` -> **Severity: 1548.9** (Blast Radius: 15.489 * Doc Risk: 100.0%)
- `Userland/Libraries/LibGfx/ImageFormats/WebPSharedLossless.h` -> **Severity: 1221.4** (Blast Radius: 12.214 * Doc Risk: 100.0%)
- `AK/StringView.h` -> **Severity: 1076.7** (Blast Radius: 10.767 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1245 literal sites + 154 sites through wrappers = 1399
- **`memory_alloc`:** 2383 literal sites + 119 sites through wrappers = 2502
- **`panics_and_aborts`:** 815 literal sites + 8 sites through wrappers = 823

- `printf` (function, debug_prints, primitive): 137 call sites in 30 files -- `Userland/Libraries/LibC/stdio.cpp`
- `pthread_exit` (function, memory_alloc, via pthread_exit_without_cleanup_handlers): 17 call sites in 9 files -- `Userland/Libraries/LibC/pthread.cpp`
- `strdup` (function, memory_alloc, primitive): 16 call sites in 6 files -- `Userland/Libraries/LibC/string.cpp`
- `report` (function, debug_prints, primitive): 13 call sites in 1 files -- `Meta/lint-keymaps.py`
- `emit` (function, memory_alloc, primitive): 10 call sites in 1 files -- `Userland/Libraries/LibJS/Bytecode/Generator.h`
- `dlsym` (function, memory_alloc, via store_error): 8 call sites in 2 files -- `Userland/Libraries/LibC/dlfcn.cpp`
- `fdopendir` (function, memory_alloc, primitive): 6 call sites in 3 files -- `Userland/Libraries/LibC/dirent.cpp`
- `mem_chunk` (function, memory_alloc, primitive): 5 call sites in 1 files -- `Tests/Kernel/TestMemoryDeviceMmap.cpp`
- `dlopen` (function, memory_alloc, via store_error): 4 call sites in 2 files -- `Userland/Libraries/LibC/dlfcn.cpp`
- `store_error` (function, memory_alloc, via strdup): 4 call sites in 1 files -- `Userland/Libraries/LibC/dlfcn.cpp`
- `fail` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `Userland/Utilities/printf.cpp`
- `strndup` (function, memory_alloc, primitive): 3 call sites in 3 files -- `Userland/Libraries/LibC/string.cpp`
*(+39 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 279375 call pairs -- scoped 28.8%, unique 7.6%, ambiguous 43.8%, external 19.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 272923 | 29.1% | 7.8% | 44.5% | 18.7% |
| objective-c | 1661 | 21.1% | 6.6% | 23.8% | 48.5% |
| shell | 1630 | 8.8% | 1.7% | 0.2% | 89.2% |
| javascript | 1243 | 20.8% | 0.0% | 24.2% | 55.0% |
| python | 954 | 22.9% | 0.0% | 1.3% | 75.9% |
| html | 944 | 8.2% | 0.1% | 21.6% | 70.1% |
| assembly | 10 | 10.0% | 20.0% | 10.0% | 60.0% |
| lua | 10 | 0.0% | 0.0% | 0.0% | 100.0% |

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
