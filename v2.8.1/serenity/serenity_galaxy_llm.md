# ARCHITECTURAL_BRIEF: serenity
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/SerenityOS/serenity.git` |
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
| Total Artifacts | 18572 |
| Analyzed Artifacts (Scanned) | 13192 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5380 |
| Total LOC | 1065223 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.0% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6152 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1702 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4273 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 374 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 7374 | 915832 | 55.9% |
| HTML | 1794 | 46453 | 13.6% |
| PLAINTEXT | 1515 | 16 | 11.5% |
| JAVASCRIPT | 1112 | 57349 | 8.4% |
| MARKDOWN | 605 | 0 | 4.6% |
| SHELL | 439 | 11888 | 3.3% |
| JSON | 168 | 20397 | 1.3% |
| OBJECTIVE-C | 45 | 6061 | 0.3% |
| XML | 37 | 0 | 0.3% |
| PYTHON | 34 | 3960 | 0.3% |
| ASSEMBLY | 21 | 1762 | 0.2% |
| CSS | 20 | 1114 | 0.2% |
| GLSL | 10 | 46 | 0.1% |
| SQLITE | 6 | 110 | 0.0% |
| YAML | 3 | 39 | 0.0% |
| NIX | 3 | 105 | 0.0% |
| DOCKERFILE | 2 | 50 | 0.0% |
| LUA | 2 | 28 | 0.0% |
| MAKEFILE | 1 | 12 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.13; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 34%, Declarative / Non-Code 19%, Interface Declarations Files 14%, Large Core Modules 13%, Compute Cores Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 11070 | 83.9% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2116 | 16.0% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5380*

**Composition by Extension & Reason:**
- `.png`: 3035x Excluded (Explicitly Denied Extension: '.png')
- `.patch`: 477x Excluded (Unsupported Extension: '.patch')
- `.idl`: 429x Excluded (Unsupported Extension: '.idl')
- `.txt`: 159x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2092 LOC)
- `.gn`: 138x Excluded (Unsupported Extension: '.gn'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gml`: 133x Excluded (Unsupported Extension: '.gml')
- `.jbig2`: 107x Excluded (Unsupported Extension: '.jbig2')
- `.af`: 71x Excluded (Unsupported Extension: '.af')
- `.ini`: 55x Excluded (Unsupported Extension: '.ini'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.font`: 51x Excluded (Unsupported Extension: '.font')
- `no_extension`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded (Binary Format Detected), 9x Unsupported Format (.undeterminable)
- `.jp2`: 45x Excluded (Unsupported Extension: '.jp2')
- `.cmake`: 44x Excluded (Unsupported Extension: '.cmake')
- `.tiff`: 44x Excluded (Explicitly Denied Extension: '.tiff')
- `.ipc`: 36x Excluded (Unsupported Extension: '.ipc')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.4 | 4.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 34.1 | 34.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 28.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 38.6 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 63.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 121402 | 5059 | 22 | `Userland/Libraries/LibDisassembly/x86/Instruction.cpp` |
| cleanup | 1279 | 587 | 0 | `Userland/Libraries/LibGUI/VimEditingEngine.cpp` |
| guards | 96748 | 6504 | 18 | `Userland/Libraries/LibJS/AST.h` |
| danger | 5271 | 1369 | 1 | `Kernel/Arch/aarch64/Registers.h` |
| concurrency | 2904 | 624 | 0 | `Userland/Libraries/LibJS/Tests/syntax/async-await.js` |
| connectivity | 16713 | 3745 | 3 | `Userland/Libraries/LibWeb/CSS/ComputedValues.h` |
| io | 4675 | 1361 | 1 | `Base/res/html/misc/welcome.html` |
| crypto | 1 | 1 | 0 | `Meta/download_file.py` |
| ipc | 708 | 213 | 0 | `Kernel/Bus/USB/xHCI/xHCIController.cpp` |
| time | 320 | 92 | 0 | `Base/res/html/misc/set-timeout-and-interval.html` |
| serialization | 180 | 67 | 0 | `Base/usr/share/Spreadsheet/runtime.js` |
| regex | 318 | 82 | 0 | `Userland/Libraries/LibJS/Tests/builtins/String/String.prototype.replace.js` |
| events | 2811 | 739 | 0 | `Userland/Libraries/LibJS/Bytecode/ASTCodegen.cpp` |
| tests | 33384 | 2005 | 2 | `Userland/Libraries/LibJS/Tests/builtins/Intl/NumberFormat/NumberFormat.prototype.format.js` |
| docs | 659 | 240 | 0 | `Userland/Libraries/LibGfx/ImageFormats/JPEGXLLoader.cpp` |
| debt | 8989 | 1972 | 1 | `Userland/Libraries/LibJS/Bytecode/Op.h` |
| mutation | 211149 | 8453 | 36 | `Userland/Libraries/LibWeb/CSS/Parser/Parser.cpp` |
| dead_code | 30608 | 3895 | 6 | `Userland/Libraries/LibShell/AST.cpp` |
| credential | 384 | 352 | 0 | `Ports/xash3d-fwgs/package.sh` |
| threat | 8845 | 1737 | 1 | `Userland/Libraries/LibGL/GL/gl.h` |
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

1. **include.js** (`Tests/LibWeb/Text/input/include.js`) — 685 inbound connections
2. **Types.h** (`AK/Types.h`) — 641 inbound connections
3. **Vector.h** (`AK/Vector.h`) — 549 inbound connections
4. **ByteString.h** (`AK/ByteString.h`) — 430 inbound connections
5. **StringView.h** (`AK/StringView.h`) — 417 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AvailablePorts.md** (`Ports/AvailablePorts.md`) — 358 outbound dependencies
2. **Document.cpp** (`Userland/Libraries/LibWeb/DOM/Document.cpp`) — 130 outbound dependencies
3. **Intrinsics.cpp** (`Userland/Libraries/LibJS/Runtime/Intrinsics.cpp`) — 126 outbound dependencies
4. **ElementFactory.cpp** (`Userland/Libraries/LibWeb/DOM/ElementFactory.cpp`) — 109 outbound dependencies
5. **GlobalObject.cpp** (`Userland/Libraries/LibJS/Runtime/GlobalObject.cpp`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Parser::basic_parse` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibURL/Parser.cpp`) -> Impact: **909.7** | LOC: 950
  * *Intent:* // https://url.spec.whatwg.org/#concept-basic-url-parser
- `Instruction::to_byte_string_internal` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibDisassembly/x86/Instruction.cpp`) -> Impact: **727.7** | LOC: 870
- `Instruction::parse` **(Compute Cores)** (@ `Userland/Libraries/LibWasm/Parser/Parser.cpp`) -> Impact: **666.4** | LOC: 629
- `BytecodeInterpreter::interpret_instruction` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibWasm/AbstractMachine/BytecodeInterpreter.cpp`) -> Impact: **647.5** | LOC: 869
- `Parser::parse_css_value` **(Compute Cores)** (@ `Userland/Libraries/LibWeb/CSS/Parser/Parser.cpp`) -> Impact: **456.0** | LOC: 360
- `build_in_table` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibDisassembly/x86/Instruction.cpp`) -> Impact: **421.7** | LOC: 179
- `Lexer::lex_impl` **(Compute Cores)** (@ `Userland/Libraries/LibCpp/Lexer.cpp`) -> Impact: **410.7** | LOC: 578
- `Type1FontProgram::parse_glyph` **(Many-Argument Workhorses)** (@ `Userland/Libraries/LibPDF/Fonts/Type1FontProgram.cpp`) -> Impact: **399.9** | LOC: 600
- `Lexer::lex_impl` **(Compute Cores)** (@ `Userland/Libraries/LibGLSL/Lexer.cpp`) -> Impact: **398.1** | LOC: 551
- `cpu_feature_to_description` **(Compute Cores)** (@ `Kernel/Arch/aarch64/CPUID.cpp`) -> Impact: **397.5** | LOC: 482
  * *Intent:* // https://developer.arm.com/downloads/-/exploration-tools/feature-names-for-a-profile

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Userland/Utilities` | 224 | 24557.7 | 30.9% | 47.04% |
| `Userland/Libraries/LibGUI` | 255 | 23464.8 | 20.32% | 42.87% |
| `AK` | 230 | 23018.42 | 27.0% | 28.44% |
| `Userland/Libraries/LibGfx/ImageFormats` | 98 | 21933.1 | 31.18% | 35.15% |
| `Userland/Libraries/LibJS/Runtime` | 324 | 18165.28 | 13.22% | 43.37% |
| `Userland/Libraries/LibWeb/HTML` | 401 | 17708.54 | 8.41% | 49.02% |
| `Userland/Libraries/LibWeb/Layout` | 95 | 11452.66 | 15.16% | 44.5% |
| `Userland/Libraries/LibShell` | 26 | 11377.78 | 24.43% | 39.84% |
| `Userland/Libraries/LibWeb/CSS` | 150 | 11143.94 | 11.47% | 44.04% |
| `Userland/Libraries/LibC` | 130 | 11127.9 | 22.02% | 36.74% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `AK/BitStream.h` -> **100.0%** Exposure
- `AK/Coroutine.h` -> **100.0%** Exposure
- `AK/JsonObject.cpp` -> **100.0%** Exposure
- `AK/MemoryStream.cpp` -> **100.0%** Exposure
- `AK/NumericLimits.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `AK/BigIntBase.h` -> **100.0%** Exposure
- `AK/BitmapView.h` -> **100.0%** Exposure
- `AK/MemMem.h` -> **100.0%** Exposure
- `AK/OptionParser.cpp` -> **100.0%** Exposure
- `AK/RedBlackTree.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Userland/Libraries/LibShell/AST.cpp` -> **295** Orphaned Functions | **0** Duplicates
- `Userland/Libraries/LibWeb/CSS/StyleValues/CSSMathValue.cpp` -> **277** Orphaned Functions | **0** Duplicates
- `Userland/Libraries/LibWeb/DOM/Document.cpp` -> **267** Orphaned Functions | **0** Duplicates
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
- **Binary Anomalies (X-Ray):** `396` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `41512` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Userland/Libraries/LibCrypto/ASN1/PEM.cpp` (CPP) -> Cumulative Risk: **751.55**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -1.54)
- **Magnitude:** 129.4 | **LOC:** 133 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Secrets Risk (99.9925%)
- **Heaviest Functions:** `decode_pem` (Compute Cores, Impact: 23.5), `decode_pems` (Compute Cores, Impact: 17.4), `encode_pem` (Compute Cores, Impact: 17.3)

### 2. `Userland/Libraries/LibHTTP/Job.cpp` (CPP) -> Cumulative Risk: **742.93**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.22)
- **Magnitude:** 401.06 | **LOC:** 577 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.862%), Concurrency (99.664%)
- **Heaviest Functions:** `Job::parse_body` (Compute Cores, Impact: 72.3), `Job::parse_headers` (Compute Cores, Impact: 48.9), `handle_content_encoding` (Compute Cores, Impact: 24.2)

### 3. `Userland/Libraries/LibGfx/ImageFormats/JPEG2000ProgressionIterators.cpp` (CPP) -> Cumulative Risk: **742.04**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.30)
- **Magnitude:** 163.62 | **LOC:** 335 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9995%), State Flux (99.8702%)
- **Heaviest Functions:** `ResolutionLevelPositionComponentLayerProgressionIterator::generator` (I/O & Config Routines, Impact: 16.4), `PositionComponentResolutionLevelLayerProgressionIterator::generator` (I/O & Config Routines, Impact: 16.4), `ComponentPositionResolutionLevelLayerProgressionIterator::generator` (I/O & Config Routines, Impact: 16.4)

### 4. `Userland/Libraries/LibTLS/Socket.cpp` (CPP) -> Cumulative Risk: **721.33**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.23)
- **Magnitude:** 242.44 | **LOC:** 363 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.999%), Safety Score (89.1944%)
- **Heaviest Functions:** `TLSv12::check_connection_state` (Compute Cores, Impact: 34.3), `TLSv12::read_from_socket` (I/O & Config Routines, Impact: 15.3), `TLSv12::flush` (Compute Cores, Impact: 15.1)

### 5. `Kernel/Arch/x86_64/Processor.cpp` (CPP) -> Cumulative Risk: **704.81**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.24)
- **Magnitude:** 1289.54 | **LOC:** 1557 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.7502%)
- **Heaviest Functions:** `Processor::cpu_detect` (Compute Cores, Impact: 215.2), `Processor::smp_process_pending_messages` (Compute Cores, Impact: 20.6), `Processor::cpu_setup` (I/O & Config Routines, Impact: 18.2)

### 6. `Base/usr/share/Shell/completion/builtin.sh` (SHELL) -> Cumulative Risk: **703.69**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.30)
- **Magnitude:** 111.72 | **LOC:** 97 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.9392%)
- **Heaviest Functions:** `__complete_job_spec` (Compute Cores, Impact: 9.6), `_complete_cd` (State Mutators, Impact: 6.4), `_complete_unalias` (Compute Cores, Impact: 5.1)

### 7. `Kernel/Bus/USB/xHCI/xHCIController.cpp` (CPP) -> Cumulative Risk: **703.17**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.84)
- **Magnitude:** 1202.7 | **LOC:** 1458 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.2091%)
- **Heaviest Functions:** `xHCIController::initialize_device` (Compute Cores, Impact: 92.4), `xHCIController::initialize_endpoint_if_needed` (Compute Cores, Impact: 77.5), `xHCIController::clear_port_feature` (Many-Argument Workhorses, Impact: 52.9)

### 8. `Userland/Libraries/LibGfx/ICC/TagTypes.h` (CPP) -> Cumulative Risk: **698.47**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.14)
- **Magnitude:** 784.14 | **LOC:** 1641 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.978%), State Flux (99.4809%)
- **Heaviest Functions:** `LutBToATagData::evaluate` (Many-Argument Workhorses, Impact: 33.6), `Lut16TagData::evaluate_from_pcs` (Many-Argument Workhorses, Impact: 26.9), `Lut8TagData::evaluate_from_pcs` (Many-Argument Workhorses, Impact: 26.8)

### 9. `Userland/Libraries/LibGfx/ImageFormats/JBIG2Loader.cpp` (CPP) -> Cumulative Risk: **695.9**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.26)
- **Magnitude:** 2363.88 | **LOC:** 3761 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 92.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9991%), Churn (93.52%)
- **Heaviest Functions:** `symbol_dictionary_decoding_procedure` (Many-Argument Workhorses, Impact: 141.0), `text_region_decoding_procedure` (Many-Argument Workhorses, Impact: 109.0), `decode_text_region` (Many-Argument Workhorses, Impact: 86.8)

### 10. `Toolchain/BuildJakt.sh` (SHELL) -> Cumulative Risk: **694.78**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.46)
- **Magnitude:** 173.68 | **LOC:** 273 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.8373%), Documentation (93.82%)
- **Heaviest Functions:** `already_available` (Compute Cores, Impact: 14.0), `build_for` (Compute Cores, Impact: 12.4), `__global_context__` (I/O & Config Routines, Impact: 7.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Userland/Libraries/LibWeb/CSS/Parser/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5670.68 | **LOC:** 9504 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.1587%), Tech Debt (95.6172%)
**Top Internal Functions/Classes:**
  * `Parser::parse_css_value` **(Compute Cores)** (Impact: 456.0)
  * `Parser::parse_css_value_for_properties` **(Compute Cores)** (Impact: 223.0)
  * `Parser::substitute_attr_function` **(Many-Argument Workhorses)** (Impact: 173.1)
    * *Intent:* // https://drafts.csswg.org/css-values-5/#attr-substitution
  * `Parser::convert_to_font_face_rule` **(Compute Cores)** (Impact: 153.3)
  * `Parser::parse_position_value` **(Compute Cores)** (Impact: 126.9)
    * *Intent:* // https://www.w3.org/TR/css-values-4/#position
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 981
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2396`, `structural_boundaries: 2475`, `args: 773`, `func_start: 208`, `class_start: 10`
* *Risk/State:* `state_mutation: 335`, `dead_code: 9`, `planned_debt: 14`, `fragile_debt: 55`, `unreferenced_by_name: 177`
* *Architecture:* `api: 2`, `import: 78`
* *Defense:* `safety: 18`, `immutability_locks: 161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 77):` CharacterTypes.h, Debug.h, GenericLexer.h, QuickSort.h, SourceLocation.h, TemporaryChange.h, CSSFontFaceRule.h, CSSImportRule.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Base/etc/shadow` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Utilities/jbig2-from-json.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3915.44 | **LOC:** 2962 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 98.5%
- **Risk Profile:** Cognitive Load (70.2146%), Tech Debt (25.438%)
**Top Internal Functions/Classes:**
  * `jbig2_pattern_dictionary_from_json` **(Many-Argument Workhorses)** (Impact: 186.1)
  * `TRY` **(Compute Cores)** (Impact: 113.1)
  * `TRY` **(Compute Cores)** (Impact: 109.4)
  * `jbig2_text_region_flags_from_json` **(Compute Cores)** (Impact: 93.7)
  * `jbig2_segment_from_json` **(Compute Cores)** (Impact: 91.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 252 instances
* *State Mutation (weighted view):* 770
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 897`, `structural_boundaries: 803`, `args: 146`, `func_start: 102`, `class_start: 4`
* *Risk/State:* `state_mutation: 266`, `fragile_debt: 15`, `unreferenced_by_name: 1`
* *Architecture:* `import: 15`
* *Defense:* `immutability_locks: 182`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Enumerate.h, IntegralMath.h, JsonObject.h, JsonValue.h, LexicalPath.h, MemoryStream.h, ArgsParser.h, File.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibJS/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3538.68 | **LOC:** 5193 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9578%), Tech Debt (85.4011%)
**Top Internal Functions/Classes:**
  * `Parser::parse_class_expression` **(Compute Cores)** (Impact: 192.4)
  * `Parser::parse_secondary_expression` **(Many-Argument Workhorses)** (Impact: 156.7)
  * `Parser::parse_binding_pattern` **(Compute Cores)** (Impact: 155.5)
  * `Parser::parse_export_statement` **(Compute Cores)** (Impact: 118.3)
  * `~ScopePusher` **(Compute Cores)** (Impact: 84.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 248 instances
* *State Mutation (weighted view):* 796
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1600`, `structural_boundaries: 905`, `args: 557`, `func_start: 148`, `class_start: 10`
* *Risk/State:* `state_mutation: 300`, `dead_code: 2`, `fragile_debt: 9`, `unreferenced_by_name: 106`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 9`, `immutability_locks: 276`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Array.h, CharacterTypes.h, HashTable.h, ScopeGuard.h, StdLibExtras.h, TemporaryChange.h, RegExpObject.h, Regex.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibGfx/ImageFormats/JPEGXLLoader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2468.44 | **LOC:** 3882 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 97.9%
- **Risk Profile:** Cognitive Load (51.1307%), Tech Debt (46.0019%)
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
* *Structure:* `branch: 593`, `structural_boundaries: 658`, `args: 258`, `func_start: 129`, `class_start: 61`
* *Risk/State:* `state_mutation: 386`, `dead_code: 1`, `planned_debt: 20`, `fragile_debt: 14`, `unreferenced_by_name: 14`
* *Architecture:* `api: 6`, `import: 19`
* *Defense:* `safety: 6`, `doc: 61`, `immutability_locks: 218`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` BitStream.h, ConstrainedStream.h, Debug.h, Endian.h, Enumerate.h, FixedArray.h, String.h, Brotli.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibWeb/DOM/Document.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2432.44 | **LOC:** 5651 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.8759%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Document::shared_declarative_refresh_steps` **(Compute Cores)** (Impact: 70.1)
    * *Intent:* // https://html.spec.whatwg.org/multipage/semantics.html#shared-declarative-refresh-steps
  * `Document::create_event` **(Compute Cores)** (Impact: 61.6)
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
* *Structure:* `branch: 831`, `structural_boundaries: 968`, `args: 320`, `func_start: 309`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 234`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 130`, `unreferenced_by_name: 267`
* *Architecture:* `import: 130`
* *Defense:* `immutability_locks: 200`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 128):` CharacterTypes.h, Debug.h, GenericLexer.h, InsertionSort.h, StringBuilder.h, Utf8View.h, Timer.h, Array.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibGfx/ImageFormats/JBIG2Loader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2363.88 | **LOC:** 3761 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 92.2%
- **Risk Profile:** Cognitive Load (92.6522%), Tech Debt (30.8902%)
**Top Internal Functions/Classes:**
  * `symbol_dictionary_decoding_procedure` **(Many-Argument Workhorses)** (Impact: 141.0)
    * *Intent:* // 6.5 Symbol Dictionary Decoding Procedure
  * `text_region_decoding_procedure` **(Many-Argument Workhorses)** (Impact: 109.0)
    * *Intent:* // 6.4 Text Region Decoding Procedure
  * `decode_text_region` **(Many-Argument Workhorses)** (Impact: 86.8)
  * `decode_symbol_dictionary` **(Compute Cores)** (Impact: 83.7)
  * `decode_data` **(Compute Cores)** (Impact: 76.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 914
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 653`, `structural_boundaries: 498`, `args: 237`, `func_start: 76`, `class_start: 15`
* *Risk/State:* `state_mutation: 466`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 14`
* *Architecture:* `import: 12`
* *Defense:* `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` BitStream.h, Debug.h, Enumerate.h, GenericShorthands.h, IntegralMath.h, Utf16View.h, BilevelImage.h, CCITTDecoder.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibGfx/Painter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2301.08 | **LOC:** 2546 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.1474%), Tech Debt (98.347%)
**Top Internal Functions/Classes:**
  * `Painter::draw_line` **(Many-Argument Workhorses)** (Impact: 155.6)
  * `Painter::split_text_into_directional_runs` **(Compute Cores)** (Impact: 98.9)
  * `do_draw_scaled_bitmap` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `draw_text_line` **(Many-Argument Workhorses)** (Impact: 69.3)
  * `Painter::draw_triangle` **(Many-Argument Workhorses)** (Impact: 56.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 233 instances
* *State Mutation (weighted view):* 733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 511`, `structural_boundaries: 475`, `args: 162`, `func_start: 115`, `class_start: 5`
* *Risk/State:* `state_mutation: 267`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 28`, `unreferenced_by_name: 48`
* *Architecture:* `api: 1`, `import: 25`
* *Defense:* `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` Assertions.h, Debug.h, Function.h, Math.h, Memory.h, Queue.h, QuickSort.h, Stack.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibShell/AST.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2224.42 | **LOC:** 3973 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3027%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `Execute::for_each_entry` **(Compute Cores)** (Impact: 86.8)
  * `MatchExpr::run` **(Compute Cores)** (Impact: 59.0)
  * `Node::complete_for_editor` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `ForLoop::run` **(Compute Cores)** (Impact: 49.8)
  * `IfCond::IfCond` **(Many-Argument Workhorses)** (Impact: 35.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 745`, `structural_boundaries: 837`, `args: 464`, `func_start: 304`
* *Risk/State:* `state_mutation: 134`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 295`
* *Architecture:* `io: 1`, `import: 15`
* *Defense:* `immutability_locks: 138`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Find.h, MemoryStream.h, ScopeGuard.h, ScopedValueRollback.h, String.h, StringBuilder.h, AST.h, Highlight.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibWeb/HTML/Parser/HTMLParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2214.86 | **LOC:** 4972 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.2253%), Tech Debt (97.8904%)
**Top Internal Functions/Classes:**
  * `HTMLParser::handle_in_body` **(Compute Cores)** (Impact: 362.1)
    * *Intent:* // https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inbody
  * `HTMLParser::process_using_the_rules_for` **(Compute Cores)** (Impact: 88.7)
  * `HTMLParser::serialize_html_fragment` **(Many-Argument Workhorses)** (Impact: 81.0)
    * *Intent:* // https://html.spec.whatwg.org/multipage/parsing.html#html-fragment-serialisation-algorithm
  * `HTMLParser::handle_in_head` **(Compute Cores)** (Impact: 79.6)
  * `HTMLParser::handle_in_select` **(Compute Cores)** (Impact: 66.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 921`, `structural_boundaries: 695`, `args: 336`, `func_start: 81`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 175`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 41`, `unreferenced_by_name: 69`
* *Architecture:* `import: 38`
* *Defense:* `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` Debug.h, SourceLocation.h, Utf32View.h, Decoder.h, ExceptionOrUtils.h, MainThreadVM.h, LengthStyleValue.h, PercentageStyleValue.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibWeb/CSS/StyleComputer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2158.14 | **LOC:** 2886 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.3871%), Tech Debt (98.5304%)
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
* *Structure:* `branch: 684`, `structural_boundaries: 599`, `args: 262`, `func_start: 72`, `class_start: 6`
* *Risk/State:* `state_mutation: 146`, `planned_debt: 8`, `fragile_debt: 29`, `unreferenced_by_name: 52`
* *Architecture:* `import: 75`
* *Defense:* `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 73):` BinarySearch.h, Debug.h, Error.h, Find.h, Function.h, HashMap.h, Math.h, QuickSort.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibWeb/Layout/GridFormattingContext.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2022.48 | **LOC:** 2510 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6192%), Tech Debt (99.3968%)
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
* *Risk/State:* `state_mutation: 285`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 17`, `unreferenced_by_name: 68`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 188`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Node.h, Box.h, GridFormattingContext.h, ReplacedBox.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibJS/Bytecode/Interpreter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1907.54 | **LOC:** 3676 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.2335%), Tech Debt (99.987%)
**Top Internal Functions/Classes:**
  * `put_by_property_key` **(Many-Argument Workhorses)** (Impact: 105.3)
  * `put_by_value` **(Many-Argument Workhorses)** (Impact: 86.1)
  * `Interpreter::run_bytecode` **(Compute Cores)** (Impact: 68.7)
    * *Intent:* // FIXME: GCC takes a *long* time to compile with flattening, and it will time out our CI. :| #if de...
  * `get_by_value` **(Many-Argument Workhorses)** (Impact: 67.4)
  * `format_operand` **(Compute Cores)** (Impact: 60.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 904`, `args: 462`, `func_start: 248`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 140`, `planned_debt: 3`, `fragile_debt: 12`, `unreferenced_by_name: 206`
* *Architecture:* `import: 31`
* *Defense:* `test: 2`, `immutability_locks: 414`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` Debug.h, HashTable.h, TemporaryChange.h, AST.h, BasicBlock.h, Generator.h, Instruction.h, Interpreter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibRegex/RegexParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1905.92 | **LOC:** 2795 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.9742%), Tech Debt (89.4953%)
**Top Internal Functions/Classes:**
  * `ECMA262Parser::parse_nonempty_class_ranges` **(Compute Cores)** (Impact: 136.9)
  * `PosixExtendedParser::parse_sub_expression` **(Compute Cores)** (Impact: 136.6)
  * `AbstractPosixParser::parse_bracket_expression` **(Compute Cores)** (Impact: 117.7)
    * *Intent:* // ============================= // Abstract Posix Parser // =============================
  * `ECMA262Parser::parse_character_escape` **(Many-Argument Workhorses)** (Impact: 58.5)
  * `ECMA262Parser::read_capture_group_specifier` **(Compute Cores)** (Impact: 57.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 693`, `structural_boundaries: 481`, `args: 349`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `state_mutation: 180`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 56`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 19`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` AnyOf.h, ByteString.h, CharacterTypes.h, Debug.h, GenericLexer.h, ScopeGuard.h, StringBuilder.h, StringUtils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibLine/Editor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1881.84 | **LOC:** 2401 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.2171%), Tech Debt (86.1217%)
**Top Internal Functions/Classes:**
  * `Editor::handle_read_event` **(Compute Cores)** (Impact: 170.8)
  * `actual_rendered_string_length_step` **(Many-Argument Workhorses)** (Impact: 112.9)
  * `Editor::refresh_display` **(Compute Cores)** (Impact: 67.5)
  * `merge` **(Many-Argument Workhorses)** (Impact: 60.3)
  * `Editor::vt_dsr` **(Compute Cores)** (Impact: 59.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 247 instances
* *State Mutation (weighted view):* 796
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 601`, `structural_boundaries: 359`, `args: 113`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `state_mutation: 302`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 46`
* *Architecture:* `io: 1`, `import: 27`
* *Defense:* `safety: 1`, `immutability_locks: 45`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` CharacterTypes.h, Debug.h, GenericLexer.h, JsonObject.h, MemoryStream.h, RedBlackTree.h, ScopeGuard.h, ScopedValueRollback.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibGUI/TextEditor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1835.54 | **LOC:** 2661 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.9169%), Tech Debt (99.9559%)
**Top Internal Functions/Classes:**
  * `TextEditor::paint_event` **(Compute Cores)** (Impact: 203.0)
  * `TextEditor::keydown_event` **(Compute Cores)** (Impact: 161.3)
  * `for_each_visual_line` **(Many-Argument Workhorses)** (Impact: 150.0)
  * `TextEditor::text_position_at_content_position` **(Compute Cores)** (Impact: 41.8)
  * `TextEditor::mousedown_event` **(Compute Cores)** (Impact: 40.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 162 instances
* *State Mutation (weighted view):* 521
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 438`, `args: 132`, `func_start: 147`
* *Risk/State:* `state_mutation: 197`, `fragile_debt: 8`, `unreferenced_by_name: 140`
* *Architecture:* `import: 29`
* *Defense:* `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` CharacterTypes.h, Debug.h, ScopeGuard.h, StringBuilder.h, TemporaryChange.h, Timer.h, Action.h, AutocompleteProvider.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibURL/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1808.86 | **LOC:** 1772 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.0761%), Tech Debt (14.2528%)
**Top Internal Functions/Classes:**
  * `Parser::basic_parse` **(Many-Argument Workhorses)** (Impact: 909.7)
    * *Intent:* // https://url.spec.whatwg.org/#concept-basic-url-parser
  * `parse_ipv6_address` **(Compute Cores)** (Impact: 73.6)
    * *Intent:* // https://url.spec.whatwg.org/#concept-ipv6-parser
  * `parse_ipv4_number` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* // https://url.spec.whatwg.org/#ipv4-number-parser
  * `serialize_ipv6_address` **(Compute Cores)** (Impact: 32.8)
    * *Intent:* // https://url.spec.whatwg.org/#concept-ipv6-serializer
  * `domain_to_ascii` **(Compute Cores)** (Impact: 21.3)
    * *Intent:* // https://url.spec.whatwg.org/#concept-domain-to-ascii
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 560
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 509`, `structural_boundaries: 144`, `args: 35`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 192`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` ByteString.h, CharacterTypes.h, Debug.h, IntegralMath.h, Optional.h, SourceLocation.h, StringBuilder.h, StringUtils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibDisassembly/x86/Instruction.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1795.14 | **LOC:** 2541 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.6239%), Tech Debt (93.7042%)
**Top Internal Functions/Classes:**
  * `Instruction::to_byte_string_internal` **(Many-Argument Workhorses)** (Impact: 727.7)
  * `build_in_table` **(Many-Argument Workhorses)** (Impact: 421.7)
  * `Instruction::to_byte_string` **(Compute Cores)** (Impact: 41.8)
  * `MemoryOrRegisterReference::sib_to_byte_string` **(Compute Cores)** (Impact: 36.1)
  * `MemoryOrRegisterReference::to_byte_string_a16` **(Compute Cores)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 610`, `structural_boundaries: 148`, `args: 82`, `func_start: 57`
* *Risk/State:* `state_mutation: 99`, `fragile_debt: 36`, `unreferenced_by_name: 26`
* *Architecture:* `import: 3`
* *Defense:* `test: 8`, `sync_locks: 1`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` StringBuilder.h, Instruction.h, Interpreter.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibGfx/ImageFormats/JBIG2Writer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1779.34 | **LOC:** 2759 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 98.7%
- **Risk Profile:** Cognitive Load (70.3165%), Tech Debt (45.8255%)
**Top Internal Functions/Classes:**
  * `symbol_dictionary_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 167.7)
    * *Intent:* // 6.5 Symbol Dictionary Decoding Procedure, but in reverse.
  * `text_region_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 124.2)
    * *Intent:* // 6.4 Text Region Decoding Procedure, but in reverse.
  * `encode_text_region` **(Many-Argument Workhorses)** (Impact: 90.7)
  * `generic_refinement_region_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 82.8)
    * *Intent:* // 6.3 Generic Refinement Region Decoding Procedure, but in reverse.
  * `generic_region_encoding_procedure` **(Many-Argument Workhorses)** (Impact: 73.4)
    * *Intent:* // 6.2 Generic region decoding procedure, but in reverse.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 409`, `structural_boundaries: 402`, `args: 161`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `state_mutation: 346`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 14`, `unreferenced_by_name: 7`
* *Architecture:* `import: 17`
* *Defense:* `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` BitStream.h, Enumerate.h, HashMap.h, IntegralMath.h, MemoryStream.h, NonnullOwnPtr.h, StdLibExtras.h, Stream.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibShell/Shell.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1772.42 | **LOC:** 2734 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.9391%), Tech Debt (91.9102%)
**Top Internal Functions/Classes:**
  * `Shell::run_command` **(Compute Cores)** (Impact: 131.8)
  * `Shell::complete_via_program_itself` **(Many-Argument Workhorses)** (Impact: 116.9)
  * `do_escape` **(Many-Argument Workhorses)** (Impact: 74.4)
  * `Shell::complete_path` **(Many-Argument Workhorses)** (Impact: 72.2)
  * `Shell::prompt` **(Compute Cores)** (Impact: 69.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 704`, `structural_boundaries: 537`, `args: 157`, `func_start: 110`, `class_start: 7`
* *Risk/State:* `state_mutation: 129`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 66`
* *Architecture:* `io: 2`, `import: 42`
* *Defense:* `safety: 24`, `immutability_locks: 97`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` CharacterTypes.h, Debug.h, Function.h, GenericLexer.h, JsonParser.h, LexicalPath.h, QuickSort.h, ScopeGuard.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibMedia/Video/VP9/Parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1732.98 | **LOC:** 1783 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.7557%), Tech Debt (99.713%)
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
* *Structure:* `branch: 379`, `structural_boundaries: 415`, `args: 103`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `state_mutation: 308`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 67`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MemoryStream.h, Context.h, Decoder.h, Point.h, Size.h, WorkerThread.h, Parser.h, Utilities.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibJS/Bytecode/ASTCodegen.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1728.34 | **LOC:** 3561 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.7759%), Tech Debt (95.5022%)
**Top Internal Functions/Classes:**
  * `AssignmentExpression::generate_bytecode` **(Many-Argument Workhorses)** (Impact: 141.1)
  * `BinaryExpression::generate_bytecode` **(Compute Cores)** (Impact: 138.8)
  * `generate_object_binding_pattern_bytecode` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `constant_fold_binary_expression` **(Many-Argument Workhorses)** (Impact: 58.5)
  * `TryStatement::generate_bytecode` **(Compute Cores)** (Impact: 57.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 122 instances
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 576`, `structural_boundaries: 596`, `args: 242`, `func_start: 83`, `class_start: 5`
* *Risk/State:* `state_mutation: 132`, `planned_debt: 2`, `fragile_debt: 17`, `unreferenced_by_name: 69`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Find.h, Queue.h, AST.h, Generator.h, Instruction.h, Op.h, Register.h, StringTable.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Kernel/Arch/aarch64/CPUID.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1727.08 | **LOC:** 1495 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (14.4877%)
**Top Internal Functions/Classes:**
  * `cpu_feature_to_description` **(Compute Cores)** (Impact: 397.5)
    * *Intent:* // https://developer.arm.com/downloads/-/exploration-tools/feature-names-for-a-profile
  * `cpu_feature_to_name` **(Compute Cores)** (Impact: 357.9)
    * *Intent:* // https://developer.arm.com/downloads/-/exploration-tools/feature-names-for-a-profile
  * `detect_cpu_features` **(Compute Cores)** (Impact: 268.8)
  * `detect_physical_address_bit_width` **(I/O & Config Routines)** (Impact: 12.2)
  * `build_cpu_feature_names` **(Compute Cores)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 642
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 505`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 214`, `planned_debt: 5`, `fragile_debt: 5`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CPUID.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibGfx/ImageFormats/JPEG2000Loader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1706.34 | **LOC:** 2735 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.191%), Tech Debt (50.0978%)
**Top Internal Functions/Classes:**
  * `convert_to_bitmap` **(Compute Cores)** (Impact: 127.3)
  * `read_one_packet_header` **(Many-Argument Workhorses)** (Impact: 107.0)
  * `decode_jpeg2000_header` **(Compute Cores)** (Impact: 75.2)
  * `parse_codestream_main_header` **(Compute Cores)** (Impact: 73.9)
  * `parse_codestream_tile_header` **(Compute Cores)** (Impact: 71.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 190 instances
* *State Mutation (weighted view):* 671
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 509`, `structural_boundaries: 455`, `args: 155`, `func_start: 64`, `class_start: 30`
* *Risk/State:* `state_mutation: 291`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 13`, `unreferenced_by_name: 10`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 101`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` BitStream.h, Debug.h, Enumerate.h, MemoryStream.h, Profile.h, JPEG2000Boxes.h, Reader.h, JPEG2000BitplaneDecoding.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Userland/Libraries/LibVT/Terminal.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1687.82 | **LOC:** 1803 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.7664%), Tech Debt (99.8225%)
**Top Internal Functions/Classes:**
  * `Terminal::handle_key_press` **(Many-Argument Workhorses)** (Impact: 154.8)
  * `Terminal::SGR` **(Compute Cores)** (Impact: 126.0)
  * `Terminal::execute_csi_sequence` **(Many-Argument Workhorses)** (Impact: 125.5)
  * `Terminal::set_size` **(Compute Cores)** (Impact: 88.8)
    * *Intent:* #ifndef KERNEL
  * `Terminal::execute_escape_sequence` **(Many-Argument Workhorses)** (Impact: 74.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 166 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 560`, `structural_boundaries: 241`, `args: 102`, `func_start: 82`
* *Risk/State:* `state_mutation: 184`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 78`
* *Architecture:* `import: 7`
* *Defense:* `safety: 3`, `immutability_locks: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Debug.h, Queue.h, StringBuilder.h, StringView.h, TemporaryChange.h, VirtualConsole.h, Color.h, Terminal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Userland/Libraries/LibGfx/ImageFormats/JBIG2Writer.cpp` -> Churn: **100.0%** | Cog Load: 70.3165% | Debt: 45.8255%
- `Userland/Libraries/LibGfx/ImageFormats/JBIG2Loader.cpp` -> Churn: **93.52%** | Cog Load: 92.6522% | Debt: 30.8902%
- `Userland/Utilities/jbig2-from-json.cpp` -> Churn: **89.06%** | Cog Load: 70.2146% | Debt: 25.438%
- `Userland/Libraries/LibGfx/ImageFormats/JPEGXLLoader.cpp` -> Churn: **80.73%** | Cog Load: 51.1307% | Debt: 46.0019%
- `Userland/Services/SSHServer/SSHClient.cpp` -> Churn: **78.03%** | Cog Load: 18.9588% | Debt: 99.9997%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Userland/Utilities/jbig2-from-json.cpp` -> **Nico Weber** (98.5% isolated ownership) | Magnitude: 3915.44
- `Userland/Libraries/LibGfx/ImageFormats/JPEGXLLoader.cpp` -> **Lucas CHOLLET** (97.9% isolated ownership) | Magnitude: 2468.44
- `Userland/Libraries/LibGfx/ImageFormats/JBIG2Loader.cpp` -> **Nico Weber** (92.2% isolated ownership) | Magnitude: 2363.88
- `Userland/Libraries/LibGfx/Painter.cpp` -> **Andreas Kling** (100.0% isolated ownership) | Magnitude: 2301.08
- `Userland/Libraries/LibLine/Editor.cpp` -> **Ali Mohammad Pur** (100.0% isolated ownership) | Magnitude: 1881.84

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `AK/IntrusiveList.h` -> **Severity: 0.057** (Bridge: 0.0006 * Flux: 99.5679%)
- `AK/Vector.h` -> **Severity: 0.024** (Bridge: 0.0003 * Flux: 85.1953%)
- `AK/Memory.h` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.1589%)
- `AK/Queue.h` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.8392%)
- `AK/Function.h` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 94.7996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Userland/Libraries/LibC/string.h` -> **Severity: 14.433** (Embedded: 0.1504 * Error Risk: 95.9745%)
- `AK/StringHash.h` -> **Severity: 13.963** (Embedded: 0.146 * Error Risk: 95.63%)
- `AK/Vector.h` -> **Severity: 12.727** (Embedded: 0.1747 * Error Risk: 72.8654%)
- `AK/StdLibExtras.h` -> **Severity: 12.385** (Embedded: 0.1879 * Error Risk: 65.926%)
- `Kernel/Heap/kmalloc.h` -> **Severity: 12.249** (Embedded: 0.1245 * Error Risk: 98.3718%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `AK/Types.h` -> **Severity: 3675.5** (Blast Radius: 36.755 * Doc Risk: 100.0%)
- `AK/StdLibExtras.h` -> **Severity: 1705.4** (Blast Radius: 17.054 * Doc Risk: 100.0%)
- `Tests/LibWeb/Text/input/include.js` -> **Severity: 1642.9** (Blast Radius: 16.429 * Doc Risk: 100.0%)
- `AK/StringView.h` -> **Severity: 1135.5** (Blast Radius: 11.355 * Doc Risk: 100.0%)
- `AK/Error.h` -> **Severity: 890.7** (Blast Radius: 8.907 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
