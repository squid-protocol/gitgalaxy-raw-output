# ARCHITECTURAL_BRIEF: keystone
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/keystone-engine/keystone.git` |
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
| Total Artifacts | 1095 |
| Analyzed Artifacts (Scanned) | 579 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 516 |
| Total LOC | 65689 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 52.9% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5346 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2977 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7081 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 44 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 260 | 54852 | 44.9% |
| C | 79 | 3738 | 13.6% |
| PYTHON | 70 | 2713 | 12.1% |
| PLAINTEXT | 42 | 0 | 7.3% |
| MAKEFILE | 29 | 1716 | 5.0% |
| JAVA | 22 | 718 | 3.8% |
| MARKDOWN | 19 | 0 | 3.3% |
| SHELL | 12 | 285 | 2.1% |
| BATCH | 6 | 58 | 1.0% |
| RUBY | 6 | 66 | 1.0% |
| CSHARP | 5 | 311 | 0.9% |
| RUST | 5 | 344 | 0.9% |
| GO | 4 | 169 | 0.7% |
| HASKELL | 4 | 140 | 0.7% |
| M4 | 3 | 65 | 0.5% |
| XML | 3 | 0 | 0.5% |
| JAVASCRIPT | 3 | 105 | 0.5% |
| ASSEMBLY | 2 | 271 | 0.3% |
| POWERSHELL | 2 | 94 | 0.3% |
| PHP | 2 | 5 | 0.3% |
| APEX | 1 | 39 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z +0.89; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 23%, Data / Markup / Trivial 17%, Declarative / Non-Code 16%, Large Core Modules 12%, Defensive Guards Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 518 | 89.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 61 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 516*

**Composition by Extension & Reason:**
- `.cpp`: 86x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 60 LOC), 1x Excluded (Machine-Generated Source Code Signature: 358 LOC)
- `.txt`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 25x Unsupported Format (.undeterminable), 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.inc`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Zero-Density Threshold (LOC: 106, Signals: 0)
- `.cmake`: 22x Excluded (Unsupported Extension: '.cmake')
- `.py`: 10x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (Machine-Generated Source Code Signature: 437 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)
- `.go`: 10x Excluded (Machine-Generated Source Code Signature: 10 LOC), 1x Excluded (Machine-Generated Source Code Signature: 112 LOC)
- `.js`: 10x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)
- `.rb`: 10x Excluded (Machine-Generated Source Code Signature: 7 LOC), 1x Excluded (Machine-Generated Source Code Signature: 97 LOC)
- `.cs`: 8x Excluded (Machine-Generated Source Code Signature: 10 LOC), 1x Excluded (Machine-Generated Source Code Signature: 107 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)
- `.chs`: 10x Unsupported Format (.chs)
- `.rc`: 8x Excluded (Unsupported Extension: '.Rc'), 2x Excluded (Unsupported Extension: '.rc')
- `.ml`: 9x Excluded (Unsupported Extension: '.ml')
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.3 | 16.9 | 6.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 48.6 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 37.7 | 24.5 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.3 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.6 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.1 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 57.9 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 82.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 60.2 | 89.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 11988 | 307 | 49 | `llvm/lib/Support/regcomp.c` |
| cleanup | 169 | 84 | 1 | `bindings/python/Makefile` |
| guards | 8748 | 352 | 43 | `llvm/include/llvm/ADT/APInt.h` |
| danger | 590 | 162 | 4 | `llvm/include/llvm/Support/ARMTargetParser.def` |
| concurrency | 37 | 9 | 0 | `llvm/utils/llvm-build/llvmbuild/componentinfo.py` |
| connectivity | 2133 | 335 | 10 | `llvm/include/llvm/MC/MCAsmInfo.h` |
| io | 265 | 55 | 0 | `bindings/python/setup.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 8 | 3 | 0 | `bindings/python/setup.py` |
| time | 2 | 1 | 0 | `llvm/include/llvm/Support/FileSystem.h` |
| serialization | 0 | 0 | 0 | - |
| regex | 49 | 4 | 0 | `suite/fuzz/gentargets.sh` |
| events | 34 | 15 | 0 | `llvm/include/llvm/ADT/STLExtras.h` |
| tests | 80 | 11 | 0 | `bindings/java/src/test/java/keystone/KeystoneTest.java` |
| docs | 9749 | 216 | 39 | `llvm/include/llvm/ADT/APInt.h` |
| debt | 878 | 203 | 6 | `kstool/kstool.cpp` |
| mutation | 14914 | 420 | 51 | `llvm/lib/MC/MCParser/AsmParser.cpp` |
| dead_code | 1696 | 299 | 5 | `llvm/lib/MC/MCParser/AsmParser.cpp` |
| credential | 0 | 0 | 0 | - |
| threat | 487 | 112 | 1 | `suite/fuzz/gentargets.sh` |
| ml_ai | 172 | 16 | 0 | `llvm/include/llvm/ADT/DenseSet.h` |
| ui | 4 | 1 | 0 | `suite/regress/c-crashers/run-all-overview.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bindings/python/setup.py` (Hits: 57)
- `suite/fuzz/gentargets.sh` (Hits: 46)
- `llvm/utils/llvm-build/llvmbuild/main.py` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **keystone.h** (`include/keystone/keystone.h`) — 76 inbound connections
2. **regress.py** (`suite/regress/regress.py`) — 54 inbound connections
3. **StringRef.h** (`llvm/include/llvm/ADT/StringRef.h`) — 40 inbound connections
4. **raw_ostream.h** (`llvm/include/llvm/Support/raw_ostream.h`) — 34 inbound connections
5. **Compiler.h** (`llvm/include/llvm/Support/Compiler.h`) — 34 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AsmParser.cpp** (`llvm/lib/MC/MCParser/AsmParser.cpp`) — 33 outbound dependencies
2. **MCContext.cpp** (`llvm/lib/MC/MCContext.cpp`) — 24 outbound dependencies
3. **MCELFStreamer.cpp** (`llvm/lib/MC/MCELFStreamer.cpp`) — 24 outbound dependencies
4. **ELFObjectWriter.cpp** (`llvm/lib/MC/ELFObjectWriter.cpp`) — 23 outbound dependencies
5. **MCAssembler.cpp** (`llvm/lib/MC/MCAssembler.cpp`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `AsmParser::parseStatement` **(Many-Argument Workhorses)** (@ `llvm/lib/MC/MCParser/AsmParser.cpp`) -> Impact: **436.2** | LOC: 525
  * *Intent:* /// ParseStatement: /// ::= EndOfStatement /// ::= Label* Directive ...Operands... EndOfStatement /// ::= Label* Identifier OperandList* EndOfStatemen...
- `backref` **(Many-Argument Workhorses)** (@ `llvm/lib/Support/regengine.inc`) -> Impact: **298.3** | LOC: 196
  * *Intent:* */
- `AsmParser::parseMSInlineAsm` **(Many-Argument Workhorses)** (@ `llvm/lib/MC/MCParser/AsmParser.cpp`) -> Impact: **279.3** | LOC: 213
- `MCExpr::evaluateAsRelocatableImpl` **(Many-Argument Workhorses)** (@ `llvm/lib/MC/MCExpr.cpp`) -> Impact: **234.5** | LOC: 165
- `ks_open` **(Many-Argument Workhorses)** (@ `llvm/keystone/ks.cpp`) -> Impact: **203.3** | LOC: 267
- `MCSymbolRefExpr::getVariantKindName` **(Compute Cores)** (@ `llvm/lib/MC/MCExpr.cpp`) -> Impact: **189.1** | LOC: 133
- `dissect` **(Many-Argument Workhorses)** (@ `llvm/lib/Support/regengine.inc`) -> Impact: **170.9** | LOC: 184
  * *Intent:* */
- `identify_magic` **(Compute Cores)** (@ `llvm/lib/Support/Path.cpp`) -> Impact: **162.1** | LOC: 160
  * *Intent:* /// @brief Identify the magic in magic.
- `step` **(Many-Argument Workhorses)** (@ `llvm/lib/Support/regengine.inc`) -> Impact: **161.7** | LOC: 112
  * *Intent:* */
- `AsmParser::expandMacro` **(Many-Argument Workhorses)** (@ `llvm/lib/MC/MCParser/AsmParser.cpp`) -> Impact: **156.9** | LOC: 121

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `llvm/lib/Support` | 39 | 15336.94 | 43.7% | 65.22% |
| `llvm/lib/MC/MCParser` | 11 | 6466.1 | 17.5% | 73.03% |
| `llvm/lib/MC` | 35 | 6000.1 | 36.26% | 91.04% |
| `llvm/include/llvm/ADT` | 36 | 4221.66 | 11.87% | 29.1% |
| `llvm/include/llvm/Support` | 56 | 3053.37 | 7.04% | 17.66% |
| `llvm/include/llvm/MC` | 48 | 2575.4 | 4.36% | 20.47% |
| `suite/fuzz` | 30 | 1070.68 | 57.34% | 58.1% |
| `llvm/utils/llvm-build/llvmbuild` | 5 | 1018.36 | 26.64% | 24.15% |
| `llvm/lib/Support/Windows` | 4 | 1016.14 | 38.02% | 49.71% |
| `llvm/keystone` | 7 | 654.16 | 11.17% | 15.37% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bindings/csharp/Keystone.Net/NativeInterop.cs` -> **100.0%** Exposure
- `bindings/vb6/vbKeystone.cpp` -> **100.0%** Exposure
- `llvm/lib/MC/MCObjectStreamer.cpp` -> **100.0%** Exposure
- `llvm/lib/MC/MCStreamer.cpp` -> **100.0%** Exposure
- `llvm/lib/Support/TargetParser.cpp` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `llvm/lib/Support/regcomp.c` -> **100.0%** Exposure
- `bindings/nodejs/index.js` -> **100.0%** Exposure
- `bindings/powershell/Keystone/Keystone.psm1` -> **100.0%** Exposure
- `bindings/python/keystone/keystone.py` -> **100.0%** Exposure
- `bindings/python/setup.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `llvm/lib/MC/MCParser/AsmParser.cpp` -> **133** Orphaned Functions | **0** Duplicates
- `llvm/lib/MC/MCStreamer.cpp` -> **110** Orphaned Functions | **0** Duplicates
- `llvm/lib/Support/APFloat.cpp` -> **94** Orphaned Functions | **0** Duplicates
- `llvm/lib/Support/APInt.cpp` -> **91** Orphaned Functions | **0** Duplicates
- `llvm/lib/MC/MCObjectStreamer.cpp` -> **44** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `44` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1749` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `llvm/utils/llvm-build/llvmbuild/componentinfo.py` (PYTHON) -> Cumulative Risk: **680.84**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.45)
- **Magnitude:** 316.86 | **LOC:** 476 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9981%), Safety Score (92.6979%)
- **Heaviest Functions:** `_read_components_from_parser` (Many-Argument Workhorses, Impact: 11.8), `get_optional_bool` (Type Conversions, Impact: 8.4), `get_optional_string` (Compute Cores, Impact: 7.3)

### 2. `llvm/lib/Support/SourceMgr.cpp` (CPP) -> Cumulative Risk: **677.62**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.04)
- **Magnitude:** 441.12 | **LOC:** 477 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.7376%)
- **Heaviest Functions:** `SMDiagnostic::print` (Many-Argument Workhorses, Impact: 108.1), `SourceMgr::GetMessage` (Many-Argument Workhorses, Impact: 44.7), `buildFixItLine` (Many-Argument Workhorses, Impact: 34.5)

### 3. `llvm/lib/Support/TargetParser.cpp` (CPP) -> Cumulative Risk: **663.29**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.78)
- **Magnitude:** 457.86 | **LOC:** 610 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), State Flux (99.9954%)
- **Heaviest Functions:** `llvm_ks::ARM::getFPUFeatures` (Compute Cores, Impact: 56.0), `llvm_ks::ARM::parseArchVersion` (Compute Cores, Impact: 44.5), `llvm_ks::ARM::getCanonicalArchName` (Compute Cores, Impact: 30.7)

### 4. `llvm/lib/MC/StringTableBuilder.cpp` (CPP) -> Cumulative Risk: **662.03**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.52)
- **Magnitude:** 167.36 | **LOC:** 184 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (95.4526%)
- **Heaviest Functions:** `StringTableBuilder::finalizeStringTable` (Compute Cores, Impact: 49.1), `multikey_qsort` (Many-Argument Workhorses, Impact: 17.5), `StringTableBuilder::StringTableBuilder` (Compute Cores, Impact: 13.5)

### 5. `llvm/lib/MC/MCAssembler.cpp` (CPP) -> Cumulative Risk: **646.37**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.62)
- **Magnitude:** 728.5 | **LOC:** 937 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9953%), Tech Debt (99.8689%), Documentation (96.1538%)
- **Heaviest Functions:** `writeFragment` (Many-Argument Workhorses, Impact: 98.6), `MCAssembler::evaluateFixup` (Many-Argument Workhorses, Impact: 82.6), `MCAssembler::computeFragmentSize` (Many-Argument Workhorses, Impact: 52.1)

### 6. `llvm/lib/Support/APFloat.cpp` (CPP) -> Cumulative Risk: **642.83**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.03)
- **Magnitude:** 3515.8 | **LOC:** 3999 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.9729%), Tech Debt (96.8874%)
- **Heaviest Functions:** `APFloat::toString` (Many-Argument Workhorses, Impact: 112.1), `APFloat::convert` (Many-Argument Workhorses, Impact: 68.8), `APFloat::convertToSignExtendedInteger` (Many-Argument Workhorses, Impact: 66.3)

### 7. `llvm/lib/Support/SmallPtrSet.cpp` (CPP) -> Cumulative Risk: **640.65**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.21)
- **Magnitude:** 278.38 | **LOC:** 299 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9066%), Tech Debt (99.8565%)
- **Heaviest Functions:** `SmallPtrSetImplBase::CopyFrom` (Defensive Guards, Impact: 21.2), `SmallPtrSetImplBase::swap` (Compute Cores, Impact: 15.2), `SmallPtrSetImplBase::Grow` (Type Conversions, Impact: 14.5)

### 8. `llvm/lib/Support/regcomp.c` (C) -> Cumulative Risk: **638.75**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.49)
- **Magnitude:** 1311.88 | **LOC:** 1575 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.8944%)
- **Heaviest Functions:** `p_ere_exp` (Compute Cores, Impact: 86.3), `p_simp_re` (Compute Cores, Impact: 76.6), `findmust` (Compute Cores, Impact: 45.3)

### 9. `llvm/lib/Support/Path.cpp` (CPP) -> Cumulative Risk: **633.67**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.15)
- **Magnitude:** 868.22 | **LOC:** 1161 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7158%), Documentation (98.5507%), Tech Debt (85.7286%)
- **Heaviest Functions:** `identify_magic` (Compute Cores, Impact: 162.1), `createUniqueEntity` (Many-Argument Workhorses, Impact: 43.0), `append` (Many-Argument Workhorses, Impact: 33.7)

### 10. `llvm/lib/Support/Regex.cpp` (CPP) -> Cumulative Risk: **633.37**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.07)
- **Magnitude:** 200.36 | **LOC:** 194 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9938%), Safety Score (97.9028%)
- **Heaviest Functions:** `Regex::sub` (Many-Argument Workhorses, Impact: 69.8), `Regex::match` (Compute Cores, Impact: 17.5), `Regex::Regex` (State Mutators, Impact: 7.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `llvm/lib/MC/MCParser/AsmParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4588.08 | **LOC:** 6147 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.711%), Tech Debt (95.9252%)
**Top Internal Functions/Classes:**
  * `AsmParser::parseStatement` **(Many-Argument Workhorses)** (Impact: 436.2)
    * *Intent:* /// ParseStatement: /// ::= EndOfStatement /// ::= Label* Directive ...Operands... EndOfStatement //...
  * `AsmParser::parseMSInlineAsm` **(Many-Argument Workhorses)** (Impact: 279.3)
  * `AsmParser::expandMacro` **(Many-Argument Workhorses)** (Impact: 156.9)
  * `AsmParser::parsePrimaryExprAux` **(Many-Argument Workhorses)** (Impact: 118.8)
  * `AsmParser::checkForBadMacro` **(Many-Argument Workhorses)** (Impact: 87.1)
    * *Intent:* /// checkForBadMacro /// /// With the support added for named parameters there may be code out there...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 549 instances
* *State Mutation (weighted view):* 1793
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1240`, `structural_boundaries: 738`, `args: 826`, `func_start: 157`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 695`, `dead_code: 200`, `fragile_debt: 20`, `unreferenced_by_name: 133`
* *Architecture:* `api: 5`, `import: 33`
* *Defense:* `safety: 42`, `doc: 289`, `immutability_locks: 122`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` cctype, deque, keystone.h, APFloat.h, STLExtras.h, SmallString.h, StringMap.h, Twine.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/APFloat.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3515.8 | **LOC:** 3999 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2071%), Tech Debt (96.8874%)
**Top Internal Functions/Classes:**
  * `APFloat::toString` **(Many-Argument Workhorses)** (Impact: 112.1)
  * `APFloat::convert` **(Many-Argument Workhorses)** (Impact: 68.8)
    * *Intent:* /// APFloat::convert - convert a value of one floating point type to another. /// The return value c...
  * `APFloat::convertToSignExtendedInteger` **(Many-Argument Workhorses)** (Impact: 66.3)
    * *Intent:* round-to-zero to always be used. */
  * `APFloat::compare` **(Compute Cores)** (Impact: 54.5)
    * *Intent:* /* Comparison requires normalized numbers. */
  * `interpretDecimal` **(Many-Argument Workhorses)** (Impact: 53.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 564 instances
* *State Mutation (weighted view):* 1748
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 789`, `structural_boundaries: 277`, `args: 118`, `func_start: 131`, `class_start: 2`
* *Risk/State:* `state_mutation: 620`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 6`, `unreferenced_by_name: 94`
* *Architecture:* `import: 10`
* *Defense:* `safety: 97`, `doc: 33`, `immutability_locks: 146`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` cstring, limits.h, APFloat.h, APSInt.h, FoldingSet.h, Hashing.h, StringExtras.h, StringRef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/APInt.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2924.64 | **LOC:** 2875 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8416%), Tech Debt (99.1057%)
**Top Internal Functions/Classes:**
  * `APInt::divide` **(Many-Argument Workhorses)** (Impact: 149.1)
  * `APInt::toString` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `KnuthDiv` **(Many-Argument Workhorses)** (Impact: 80.0)
    * *Intent:* /// Implementation of Knuth's Algorithm D (Division of nonnegative integers) /// from "Art of Comput...
  * `APInt::fromString` **(Many-Argument Workhorses)** (Impact: 63.0)
  * `APInt::tcMultiplyPart` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* return one. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 473 instances
* *State Mutation (weighted view):* 1433
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 253`, `args: 230`, `func_start: 128`, `class_start: 2`
* *Risk/State:* `state_mutation: 487`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 91`
* *Architecture:* `import: 13`
* *Defense:* `safety: 71`, `doc: 86`, `immutability_locks: 133`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` cmath, cstdlib, cstring, limits, APInt.h, FoldingSet.h, Hashing.h, SmallString.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/regengine.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1497.18 | **LOC:** 1035 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.2833%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `backref` **(Many-Argument Workhorses)** (Impact: 298.3)
    * *Intent:* */
  * `dissect` **(Many-Argument Workhorses)** (Impact: 170.9)
    * *Intent:* */
  * `step` **(Many-Argument Workhorses)** (Impact: 161.7)
    * *Intent:* */
  * `matcher` **(Many-Argument Workhorses)** (Impact: 142.7)
    * *Intent:* */
  * `fast` **(Many-Argument Workhorses)** (Impact: 84.9)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 171 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 80`, `args: 64`, `func_start: 9`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 172`
* *Architecture:* None
* *Defense:* `safety: 55`, `immutability_locks: 55`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001721
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `llvm/lib/Support/Triple.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1396.5 | **LOC:** 1464 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.9088%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `Triple::normalize` **(Compute Cores)** (Impact: 105.4)
  * `getDefaultFormat` **(Compute Cores)** (Impact: 75.2)
  * `getArchPointerBitWidth` **(Compute Cores)** (Impact: 69.3)
  * `Triple::getArchTypeName` **(Compute Cores)** (Impact: 69.1)
  * `Triple::get64BitArchVariant` **(Compute Cores)** (Impact: 67.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 710`, `structural_boundaries: 225`, `args: 186`, `func_start: 52`
* *Risk/State:* `state_mutation: 104`, `fragile_debt: 3`, `unreferenced_by_name: 36`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `doc: 15`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` cstring, STLExtras.h, SmallString.h, StringSwitch.h, Triple.h, ErrorHandling.h, Host.h, TargetParser.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/regcomp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1311.88 | **LOC:** 1575 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.0782%), Tech Debt (73.0808%)
**Top Internal Functions/Classes:**
  * `p_ere_exp` **(Compute Cores)** (Impact: 86.3)
    * *Intent:* */
  * `p_simp_re` **(Compute Cores)** (Impact: 76.6)
    * *Intent:* */
  * `findmust` **(Compute Cores)** (Impact: 45.3)
    * *Intent:* * * This algorithm could do fancy things like analyzing the operands of | * for common subsequences....
  * `p_bracket` **(Compute Cores)** (Impact: 44.8)
    * *Intent:* * * Note a significant property of this code: if the allocset() did SETERROR, * no set operations ar...
  * `p_b_term` **(Compute Cores)** (Impact: 37.6)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 214 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 672
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 245`, `args: 178`, `func_start: 38`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 244`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 17`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 13`
* *Defense:* `safety: 64`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ctype.h, limits.h, config.h, regcclass.h, regcname.h, regex2.h, regex_impl.h, regutils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/MC/ELFObjectWriter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 889.04 | **LOC:** 1274 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8669%), Tech Debt (96.7815%)
**Top Internal Functions/Classes:**
  * `ELFObjectWriter::computeSymbolTable` **(Many-Argument Workhorses)** (Impact: 119.4)
  * `ELFObjectWriter::recordRelocation` **(Many-Argument Workhorses)** (Impact: 76.2)
  * `ELFObjectWriter::shouldRelocateWithSymbol` **(Many-Argument Workhorses)** (Impact: 71.0)
    * *Intent:* // It is always valid to create a relocation with a symbol. It is preferable // to use a relocation ...
  * `ELFObjectWriter::writeSection` **(Many-Argument Workhorses)** (Impact: 46.5)
  * `mergeTypeForSet` **(Compute Cores)** (Impact: 43.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 121`, `args: 219`, `func_start: 36`, `class_start: 6`
* *Risk/State:* `state_mutation: 84`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 27`
* *Architecture:* `api: 2`, `import: 23`
* *Defense:* `safety: 20`, `doc: 11`, `immutability_locks: 132`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` STLExtras.h, SmallPtrSet.h, SmallString.h, StringMap.h, MCAsmBackend.h, MCAsmInfo.h, MCAsmLayout.h, MCAssembler.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/Path.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 868.22 | **LOC:** 1161 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.9321%), Tech Debt (85.7286%)
**Top Internal Functions/Classes:**
  * `identify_magic` **(Compute Cores)** (Impact: 162.1)
    * *Intent:* /// @brief Identify the magic in magic.
  * `createUniqueEntity` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `append` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `make_absolute` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `copy_file` **(Compute Cores)** (Impact: 24.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 65 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 173`, `args: 133`, `func_start: 69`
* *Risk/State:* `state_mutation: 81`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 24`
* *Architecture:* `import: 13`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 54`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Path.inc, Path.inc, cctype, cstring, io.h, COFF.h, Endian.h, Errc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/MC/MCExpr.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 800.26 | **LOC:** 840 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.5327%), Tech Debt (96.6352%)
**Top Internal Functions/Classes:**
  * `MCExpr::evaluateAsRelocatableImpl` **(Many-Argument Workhorses)** (Impact: 234.5)
  * `MCSymbolRefExpr::getVariantKindName` **(Compute Cores)** (Impact: 189.1)
  * `MCExpr::print` **(Compute Cores)** (Impact: 124.4)
    * *Intent:* #define DEBUG_TYPE "mcexpr"
  * `AttemptToFoldSymbolOffsetDifference` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* /// \brief Helper method for \see EvaluateSymbolAdd().
  * `EvaluateSymbolicAdd` **(Many-Argument Workhorses)** (Impact: 52.7)
    * *Intent:* /// Result = LHS + RHS /// and /// Result = (LHS_A - LHS_B + LHS_Cst) + (RHS_A - RHS_B + RHS_Cst). /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 197`, `args: 86`, `func_start: 25`
* *Risk/State:* `state_mutation: 21`, `dead_code: 2`, `fragile_debt: 8`, `unreferenced_by_name: 13`
* *Architecture:* `import: 12`
* *Defense:* `safety: 2`, `doc: 20`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` StringSwitch.h, MCAsmInfo.h, MCAsmLayout.h, MCAssembler.h, MCContext.h, MCExpr.h, MCObjectWriter.h, MCSymbol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/MC/MCAssembler.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 728.5 | **LOC:** 937 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.717%), Tech Debt (99.8689%)
**Top Internal Functions/Classes:**
  * `writeFragment` **(Many-Argument Workhorses)** (Impact: 98.6)
    * *Intent:* /// \brief Write the fragment \p F to the output file.
  * `MCAssembler::evaluateFixup` **(Many-Argument Workhorses)** (Impact: 82.6)
  * `MCAssembler::computeFragmentSize` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `MCAssembler::writeSectionData` **(Defensive Guards)** (Impact: 40.9)
  * `MCAssembler::layout` **(Many-Argument Workhorses)** (Impact: 36.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 89`, `args: 133`, `func_start: 26`
* *Risk/State:* `state_mutation: 88`, `dead_code: 4`, `fragile_debt: 10`, `unreferenced_by_name: 25`
* *Architecture:* `import: 23`
* *Defense:* `safety: 12`, `doc: 1`, `immutability_locks: 61`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` keystone.h, StringExtras.h, Twine.h, MCAsmBackend.h, MCAsmInfo.h, MCAsmLayout.h, MCAssembler.h, MCCodeEmitter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/utils/llvm-build/llvmbuild/main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 632.32 | **LOC:** 997 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.1312%), Tech Debt (20.7287%)
**Top Internal Functions/Classes:**
  * `add_magic_target_components` **(Many-Argument Workhorses)** (Impact: 57.0)
    * *Intent:* """add_magic_target_components(project, opts) -> None Add the "magic" target based components to the...
  * `write_library_table` **(Many-Argument Workhorses)** (Impact: 33.5)
    * *Intent:* # Write out the mapping from component names to required libraries. # # We do this in topological or...
  * `validate_components` **(Compute Cores)** (Impact: 25.9)
    * *Intent:* """validate_components() -> None Validate that the project components are well-defined. Among other ...
  * `foreach_cmake_library` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `visit_component_info` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* # Topologically order the component information according to their # component references. # Check f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 64`, `args: 29`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 129`, `fragile_debt: 4`
* *Architecture:* `io: 41`, `api: 24`, `import: 8`
* *Defense:* `safety: 3`, `doc: 26`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.601
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.001721
  * `Imports (Out-Degree: 3):` __future__, filecmp, llvmbuild.componentinfo, llvmbuild.configutil, llvmbuild.util, optparse, os, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `llvm/keystone/ks.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 600.48 | **LOC:** 717 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3815%), Tech Debt (95.2615%)
**Top Internal Functions/Classes:**
  * `ks_open` **(Many-Argument Workhorses)** (Impact: 203.3)
  * `ks_strerror` **(Compute Cores)** (Impact: 73.0)
  * `ks_asm` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* */
  * `ks_option` **(Compute Cores)** (Impact: 37.9)
  * `InitKs` **(Many-Argument Workhorses)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 101`, `args: 58`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 9`
* *Architecture:* `import: 6`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` EVMMapping.h, ks_priv.h, libkern.h, MCCodeEmitter.h, MCObjectFileInfo.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/Windows/Path.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 587.22 | **LOC:** 870 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mapped_file_region::init` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `openFileForWrite` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `getStatus` **(Compute Cores)** (Impact: 32.0)
  * `widenPath` **(Compute Cores)** (Impact: 31.9)
    * *Intent:* // Convert a UTF-8 path to UTF-16. Also, if the absolute equivalent of the // path is longer than Cr...
  * `detail::directory_iterator_construct` **(Compute Cores)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 128`, `args: 131`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 46`
* *Architecture:* `api: 23`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.947
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.001721
  * `Imports (Out-Degree: 3):` WindowsSupport.h, fcntl.h, io.h, STLExtras.h, WindowsError.h, shlobj.h, stat.h, types.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `llvm/lib/Support/StringRef.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 519.84 | **LOC:** 525 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.1088%), Tech Debt (91.6533%)
**Top Internal Functions/Classes:**
  * `StringRef::getAsInteger` **(Compute Cores)** (Impact: 47.0)
  * `llvm_ks::getAsUnsignedInteger` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* /// GetAsUnsignedInteger - Workhorse method that converts a integer character /// sequence of radix ...
  * `StringRef::compare_numeric` **(Compute Cores)** (Impact: 26.9)
    * *Intent:* /// compare_numeric - Compare strings, handle embedded numbers.
  * `StringRef::find` **(Compute Cores)** (Impact: 24.6)
    * *Intent:* //===----------------------------------------------------------------------===// // String Searching...
  * `StringRef::split` **(Many-Argument Workhorses)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 68`, `args: 66`, `func_start: 27`
* *Risk/State:* `state_mutation: 75`, `unreferenced_by_name: 16`
* *Architecture:* `import: 5`
* *Defense:* `safety: 1`, `doc: 36`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bitset, APInt.h, Hashing.h, StringRef.h, edit_distance.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/MC/MCParser/AsmLexer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 519.38 | **LOC:** 624 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.6111%), Tech Debt (99.6721%)
**Top Internal Functions/Classes:**
  * `AsmLexer::LexToken` **(Compute Cores)** (Impact: 78.0)
  * `AsmLexer::LexDigit` **(Compute Cores)** (Impact: 36.7)
    * *Intent:* /// LexDigit: First character is [0-9]. /// Local Label: [0-9][:] /// Forward/Backward Label: [0-9][...
  * `AsmLexer::LexHexFloatLiteral` **(Compute Cores)** (Impact: 21.8)
    * *Intent:* /// LexHexFloatLiteral matches essentially (.[0-9a-fA-F]*)?[pP][+-]?[0-9a-fA-F]+ /// while making su...
  * `doLookAhead` **(Compute Cores)** (Impact: 21.8)
    * *Intent:* // Look ahead to search for first non-hex digit, if it's [hH], then we treat the // integer as a hex...
  * `AsmLexer::LexSingleQuote` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* /// LexSingleQuote: Integer: 'b'
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 99`, `args: 114`, `func_start: 23`
* *Risk/State:* `state_mutation: 77`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 19`
* *Architecture:* `import: 8`
* *Defense:* `safety: 1`, `doc: 27`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cctype, cerrno, cstdio, cstdlib, MCAsmInfo.h, AsmLexer.h, MemoryBuffer.h, SMLoc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/ADT/APInt.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 504.16 | **LOC:** 1916 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.1596%), Tech Debt (8.7042%)
**Top Internal Functions/Classes:**
  * `getLowBitsSet` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /// \brief Get a value with low bits set /// /// Constructs an APInt value that has the bottom loBit...
  * `APInt` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* /// \name Constructors /// @{ /// \brief Create a new APInt of numBits width, initialized as val. //...
  * `getBitsSet` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* /// \brief Get a value with a block of bits set. /// /// Constructs an APInt value that has a contig...
  * `getHighBitsSet` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /// \brief Get a value with high bits set /// /// Constructs an APInt value that has the top hiBitsS...
  * `isIntN` **(Defensive Guards)** (Impact: 7.3)
    * *Intent:* /// \brief Check if this APInt has an N-bits unsigned integer value.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 255`, `args: 244`, `func_start: 143`, `class_start: 10`
* *Risk/State:* `state_mutation: 34`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 51`, `import: 7`
* *Defense:* `safety: 16`, `doc: 921`, `immutability_locks: 274`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.709
  * `Choke Point (Betweenness):` 0.00024 | `Ripple Effect (Closeness):` 0.014227
  * `Imports (Out-Degree: 3):` cassert, climits, cstring, ArrayRef.h, Compiler.h, MathExtras.h, string
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `llvm/lib/MC/MCParser/ELFAsmParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 503.2 | **LOC:** 747 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.8343%), Tech Debt (57.3614%)
**Top Internal Functions/Classes:**
  * `ELFAsmParser::ParseSectionArguments` **(Compute Cores)** (Impact: 147.8)
  * `parseSectionFlags` **(Compute Cores)** (Impact: 49.0)
  * `ELFAsmParser::ParseDirectiveType` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* /// ParseDirectiveELFType /// ::= .type identifier , STT_<TYPE_IN_UPPER_CASE> /// ::= .type identifi...
  * `ELFAsmParser::ParseSectionName` **(Compute Cores)** (Impact: 20.4)
  * `ELFAsmParser::ParseDirectiveSymbolAttribute` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /// ParseDirectiveSymbolAttribute /// ::= { ".local", ".weak", ... } [ identifier ( , identifier )* ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 95`, `args: 146`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`, `fragile_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 2`, `doc: 16`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` StringSwitch.h, Twine.h, MCAsmInfo.h, MCContext.h, MCExpr.h, MCAsmLexer.h, MCAsmParserExtension.h, MCSectionELF.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/TargetParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 457.86 | **LOC:** 610 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.7006%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `llvm_ks::ARM::getFPUFeatures` **(Compute Cores)** (Impact: 56.0)
  * `llvm_ks::ARM::parseArchVersion` **(Compute Cores)** (Impact: 44.5)
    * *Intent:* // Version number (ex. v7 = 7).
  * `llvm_ks::ARM::getCanonicalArchName` **(Compute Cores)** (Impact: 30.7)
    * *Intent:* // MArch is expected to be of the form (arm|thumb)?(eb)?(v.+)?(eb)?, but // (iwmmxt|xscale)(eb)? is ...
  * `llvm_ks::ARM::parseArchProfile` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* // Profile A/R/M
  * `llvm_ks::ARM::parseArchEndian` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* // Little/Big endian
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 99`, `args: 78`, `func_start: 37`
* *Risk/State:* `state_mutation: 57`, `fragile_debt: 7`, `duplicate_logic: 5`, `unreferenced_by_name: 27`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` cctype, StringExtras.h, StringSwitch.h, Twine.h, ARMBuildAttributes.h, ARMTargetParser.def, TargetParser.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/MC/MCELFStreamer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 446.98 | **LOC:** 685 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.4933%), Tech Debt (99.9867%)
**Top Internal Functions/Classes:**
  * `MCELFStreamer::fixSymbolsInTLSFixups` **(Compute Cores)** (Impact: 94.6)
  * `MCELFStreamer::EmitSymbolAttribute` **(Compute Cores)** (Impact: 74.4)
  * `MCELFStreamer::EmitInstToData` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `MCELFStreamer::mergeFragment` **(Compute Cores)** (Impact: 14.1)
  * `MCELFStreamer::EmitCommonSymbol` **(Many-Argument Workhorses)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 54`, `args: 110`, `func_start: 34`
* *Risk/State:* `state_mutation: 22`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 32`
* *Architecture:* `import: 24`
* *Defense:* `safety: 3`, `sync_locks: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` STLExtras.h, SmallPtrSet.h, MCAsmBackend.h, MCAsmInfo.h, MCAsmLayout.h, MCAssembler.h, MCCodeEmitter.h, MCContext.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/MC/MCParser/COFFAsmParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 445.72 | **LOC:** 803 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.9608%), Tech Debt (68.1542%)
**Top Internal Functions/Classes:**
  * `COFFAsmParser::ParseSectionFlags` **(Compute Cores)** (Impact: 72.7)
  * `COFFAsmParser::ParseDirectiveSection` **(Compute Cores)** (Impact: 29.1)
    * *Intent:* // .section name [, "flags"] [, identifier [ identifier ], identifier] // // Supported flags: // a: ...
  * `COFFAsmParser::ParseDirectiveSymbolAttribute` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* /// ParseDirectiveSymbolAttribute /// ::= { ".weak", ... } [ identifier ( , identifier )* ]
  * `COFFAsmParser::ParseSEHDirectiveHandler` **(Compute Cores)** (Impact: 13.4)
  * `COFFAsmParser::ParseSEHRegisterNumber` **(Compute Cores)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 114`, `args: 161`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`, `fragile_debt: 4`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` StringSwitch.h, Twine.h, MCAsmInfo.h, MCContext.h, MCExpr.h, MCObjectFileInfo.h, MCAsmLexer.h, MCAsmParserExtension.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/SourceMgr.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 441.12 | **LOC:** 477 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.1809%), Tech Debt (99.7376%)
**Top Internal Functions/Classes:**
  * `SMDiagnostic::print` **(Many-Argument Workhorses)** (Impact: 108.1)
  * `SourceMgr::GetMessage` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `buildFixItLine` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `SourceMgr::getLineAndColumn` **(Compute Cores)** (Impact: 19.5)
  * `printSourceLine` **(Compute Cores)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 26`, `args: 61`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 58`, `dead_code: 1`, `fragile_debt: 6`, `unreferenced_by_name: 8`
* *Architecture:* `import: 5`
* *Defense:* `safety: 5`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Twine.h, MemoryBuffer.h, Path.h, SourceMgr.h, raw_ostream.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/Support/raw_ostream.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 434.4 | **LOC:** 755 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.9661%), Tech Debt (99.9802%)
**Top Internal Functions/Classes:**
  * `raw_ostream::write_escaped` **(Compute Cores)** (Impact: 29.8)
  * `raw_fd_ostream::write_impl` **(Compute Cores)** (Impact: 26.6)
  * `raw_ostream::operator<<` **(Compute Cores)** (Impact: 23.2)
  * `raw_ostream::operator<<` **(Compute Cores)** (Impact: 22.1)
  * `raw_ostream::SetBufferAndMode` **(Defensive Guards)** (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 71`, `args: 107`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 46`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `import: 17`
* *Defense:* `safety: 12`, `doc: 8`, `immutability_locks: 21`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` WindowsSupport.h, cctype, cerrno, fcntl.h, io.h, STLExtras.h, SmallVector.h, StringExtras.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/include/llvm/ADT/DenseMap.h` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 430.58 | **LOC:** 1075 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8503%), Tech Debt (13.7938%)
**Top Internal Functions/Classes:**
  * `swap` **(Compute Cores)** (Impact: 29.0)
  * `copyFrom` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `grow` **(Compute Cores)** (Impact: 16.7)
  * `moveFromOldBuckets` **(Compute Cores)** (Impact: 11.6)
  * `InsertIntoBucketImpl` **(Many-Argument Workhorses)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 198`, `args: 176`, `func_start: 60`, `class_start: 2`
* *Risk/State:* `state_mutation: 67`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* `safety: 33`, `doc: 26`, `immutability_locks: 113`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.837
  * `Choke Point (Betweenness):` 0.001235 | `Ripple Effect (Closeness):` 0.0469
  * `Imports (Out-Degree: 7):` algorithm, cassert, climits, cstddef, cstring, iterator, DenseMapInfo.h, EpochTracker.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `llvm/lib/MC/MCStreamer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 429.98 | **LOC:** 764 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.1573%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `MCStreamer::visitUsedExpr` **(Compute Cores)** (Impact: 18.2)
  * `MCStreamer::EmitIntValue` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* /// EmitIntValue - Special case of EmitValue that avoids the client having to /// pass in a MCExpr f...
  * `MCStreamer::SwitchSection` **(Defensive Guards)** (Impact: 12.8)
  * `MCStreamer::EmitWinEHHandler` **(Compute Cores)** (Impact: 12.7)
  * `MCStreamer::EmitCFIStartProc` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 116`, `args: 195`, `func_start: 110`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 63`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 110`
* *Architecture:* `import: 17`
* *Defense:* `safety: 8`, `doc: 12`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` cstdlib, SmallString.h, Twine.h, MCAsmBackend.h, MCAsmInfo.h, MCContext.h, MCExpr.h, MCInst.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `llvm/lib/MC/MCObjectFileInfo.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 424.36 | **LOC:** 765 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.0158%), Tech Debt (51.2134%)
**Top Internal Functions/Classes:**
  * `MCObjectFileInfo::initELFMCObjectFileInfo` **(Compute Cores)** (Impact: 76.9)
  * `MCObjectFileInfo::initMachOMCObjectFileInfo` **(Compute Cores)** (Impact: 33.5)
  * `MCObjectFileInfo::InitMCObjectFileInfo` **(Compute Cores)** (Impact: 24.8)
  * `MCObjectFileInfo::initCOFFMCObjectFileInfo` **(Compute Cores)** (Impact: 16.3)
  * `useCompactUnwind` **(Compute Cores)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 13`, `args: 11`, `func_start: 6`
* *Risk/State:* `state_mutation: 163`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` StringExtras.h, Triple.h, MCAsmInfo.h, MCContext.h, MCObjectFileInfo.h, MCSection.h, MCSectionCOFF.h, MCSectionELF.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `llvm/include/llvm/MC/MCSymbol.h` -> **Severity: 0.158** (Bridge: 0.0019 * Flux: 84.1478%)
- `llvm/include/llvm/ADT/SmallVector.h` -> **Severity: 0.149** (Bridge: 0.0015 * Flux: 98.9168%)
- `llvm/include/llvm/ADT/DenseMap.h` -> **Severity: 0.12** (Bridge: 0.0012 * Flux: 96.9217%)
- `llvm/include/llvm/ADT/StringMap.h` -> **Severity: 0.078** (Bridge: 0.0008 * Flux: 94.5649%)
- `llvm/include/llvm/ADT/Hashing.h` -> **Severity: 0.076** (Bridge: 0.0009 * Flux: 88.8708%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `llvm/include/llvm/ADT/SmallVector.h` -> **Severity: 8.596** (Embedded: 0.1158 * Error Risk: 74.217%)
- `suite/regress/regress.py` -> **Severity: 8.318** (Embedded: 0.0929 * Error Risk: 89.4999%)
- `llvm/include/llvm/ADT/iterator.h` -> **Severity: 6.702** (Embedded: 0.1088 * Error Risk: 61.5772%)
- `llvm/include/llvm/ADT/StringRef.h` -> **Severity: 5.323** (Embedded: 0.1319 * Error Risk: 40.3618%)
- `llvm/include/llvm/Support/SwapByteOrder.h` -> **Severity: 4.893** (Embedded: 0.0807 * Error Risk: 60.6669%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `suite/regress/regress.py` -> **Severity: 4057.8** (Blast Radius: 40.578 * Doc Risk: 100.0%)
- `llvm/include/llvm/ADT/SmallVector.h` -> **Severity: 1322.574** (Blast Radius: 20.039 * Doc Risk: 66.0%)
- `llvm/include/llvm/ADT/StringRef.h` -> **Severity: 741.408** (Blast Radius: 28.348 * Doc Risk: 26.1538%)
- `llvm/include/llvm/ADT/DenseMap.h` -> **Severity: 629.438** (Blast Radius: 6.837 * Doc Risk: 92.0635%)
- `llvm/include/llvm/ADT/StringMap.h` -> **Severity: 629.311** (Blast Radius: 8.17 * Doc Risk: 77.027%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
