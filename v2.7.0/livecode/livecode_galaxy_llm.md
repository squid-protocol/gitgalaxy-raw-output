# ARCHITECTURAL_BRIEF: livecode
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/livecode/livecode.git` |
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
| Total Artifacts | 7643 |
| Analyzed Artifacts (Scanned) | 2256 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5387 |
| Total LOC | 635362 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 29.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3441 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0428 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.1081 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 85 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1040 | 432686 | 46.1% |
| LIVECODE | 434 | 71542 | 19.2% |
| MARKDOWN | 203 | 0 | 9.0% |
| PYTHON | 136 | 33101 | 6.0% |
| OBJECTIVE-C | 103 | 47951 | 4.6% |
| JAVA | 79 | 16832 | 3.5% |
| C | 50 | 24564 | 2.2% |
| PLAINTEXT | 48 | 0 | 2.1% |
| JSON | 42 | 66 | 1.9% |
| XML | 38 | 0 | 1.7% |
| PERL | 29 | 1106 | 1.3% |
| SHELL | 27 | 1377 | 1.2% |
| JAVASCRIPT | 11 | 1987 | 0.5% |
| HTML | 6 | 3178 | 0.3% |
| MAKEFILE | 5 | 849 | 0.2% |
| BATCH | 5 | 123 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2002 | 88.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 251 | 11.1% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5387*

**Composition by Extension & Reason:**
- `.lcdoc`: 2630x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1668x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 67 LOC)
- `.test`: 322x Excluded (Unsupported Extension: '.test')
- `.json`: 295x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.png`: 127x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 25x Unsupported Format (.undeterminable), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Unsupported Extension: '.compilertest')
- `.diff`: 20x Excluded (Unsupported Extension: '.diff')
- `.strings`: 18x Excluded (Unsupported Extension: '.strings')
- `.b`: 18x Unsupported Format (.b)
- `.livecode`: 13x Excluded (Binary Format Detected), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.lcb`: 2x Excluded (Saturation: Line 47 exceeds 500 chars), 2x Excluded (Saturation: Line 49 exceeds 500 chars), 1x Excluded (Saturation: Line 58 exceeds 500 chars)
- `.parsertest`: 12x Excluded (Unsupported Extension: '.parsertest')
- `.g`: 12x Unsupported Format (.g)
- `.rev`: 11x Excluded (Binary Format Detected)
- `.ios`: 11x Excluded (Unsupported Extension: '.ios')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 29.3 | 16.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 60.6 | 75.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 41.1 | 17.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 29.5 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.1 | 29.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.5 | 2.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 81.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 67.4 | 93.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 106801 | 1223 | 139 | `libfoundation/src/foundation-string.cpp` |
| cleanup | 1501 | 365 | 1 | `engine/src/dskmac.cpp` |
| guards | 18177 | 1238 | 20 | `extensions/libraries/timezone/tz/zic.c` |
| danger | 9129 | 847 | 10 | `engine/src/java/com/runrev/android/Engine.java` |
| concurrency | 928 | 246 | 1 | `engine/src/dskmac.cpp` |
| connectivity | 10016 | 894 | 11 | `engine/src/funcs.h` |
| io | 2394 | 245 | 1 | `extensions/libraries/timezone/tz/tz-link.html` |
| crypto | 3 | 3 | 0 | `gyp/pylib/gyp/MSVSNew.py` |
| ipc | 493 | 100 | 0 | `tests/lcs/core/network/network.livecodescript` |
| time | 323 | 52 | 0 | `extensions/libraries/timezone/tz/localtime.c` |
| serialization | 25 | 10 | 0 | `extensions/libraries/json/json.lcb` |
| regex | 277 | 78 | 0 | `ide-support/revdocsparser.livecodescript` |
| events | 2724 | 517 | 3 | `engine/src/java/com/runrev/android/Engine.java` |
| tests | 453 | 48 | 0 | `libfoundation/test/test_typeconvert.cpp` |
| docs | 7688 | 838 | 9 | `engine/src/canvas.lcb` |
| debt | 6437 | 809 | 7 | `toolchain/lc-compile/src/syntax-gen.c` |
| mutation | 167805 | 1439 | 208 | `toolchain/gentle/gentle/yytab.c` |
| dead_code | 19511 | 1281 | 23 | `engine/src/exec-interface2.cpp` |
| credential | 92 | 14 | 0 | `prebuilt/libcef.gyp` |
| threat | 4587 | 623 | 2 | `engine/src/sysdefs.h` |
| ml_ai | 743 | 138 | 0 | `tests/lcs/core/math/math.livecodescript` |
| ui | 3931 | 282 | 2 | `tests/lcs/core/interface/interface.livecodescript` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extensions/libraries/timezone/tz/tz-link.html` (Hits: 536)
- `extensions/libraries/timezone/tz/tzselect.ksh` (Hits: 104)
- `extensions/libraries/timezone/tz/tz-art.html` (Hits: 96)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **prefix.h** (`engine/src/prefix.h`) — 440 inbound connections
2. **parsedef.h** (`engine/src/parsedef.h`) — 423 inbound connections
3. **globdefs.h** (`engine/src/globdefs.h`) — 416 inbound connections
4. **filedefs.h** (`engine/src/filedefs.h`) — 410 inbound connections
5. **objdefs.h** (`engine/src/objdefs.h`) — 402 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **globals.cpp** (`engine/src/globals.cpp`) — 58 outbound dependencies
2. **opensslsocket.cpp** (`engine/src/opensslsocket.cpp`) — 54 outbound dependencies
3. **object.cpp** (`engine/src/object.cpp`) — 52 outbound dependencies
4. **mode_development.cpp** (`engine/src/mode_development.cpp`) — 49 outbound dependencies
5. **Engine.java** (`engine/src/java/com/runrev/android/Engine.java`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MCWindowProc` (@ `engine/src/w32dcw32.cpp`) -> Impact: **839.3** | LOC: 1044
  * *Intent:* #endif #include <crtdbg.h>
- `MCButton::draw` (@ `engine/src/buttondraw.cpp`) -> Impact: **777.3** | LOC: 609
  * *Intent:* #include "button.h" #include "field.h" #include "stacklst.h" #include "undolst.h" #include "mcerror.h" #include "param.h" #include "globals.h" #includ...
- `MCProperty::parse` (@ `engine/src/property.cpp`) -> Impact: **759.0** | LOC: 665
- `revSaveAsMobileStandaloneMain` (@ `ide-support/revsaveasandroidstandalone.livecodescript`) -> Impact: **715.2** | LOC: 1021
- `LCValueArrayFromObjcDictionary` (@ `lcidlc/src/Support.mm`) -> Impact: **665.9** | LOC: 2059
- `MCExecFetchProperty` (@ `engine/src/exec.cpp`) -> Impact: **569.4** | LOC: 878
- `MCChunk::getoptionalobj` (@ `engine/src/chunk.cpp`) -> Impact: **484.7** | LOC: 574
- `REVVideoGrabber` (@ `revvideograbber/src/revvideograbber.cpp`) -> Impact: **483.3** | LOC: 564
- `MCStack::openrect` (@ `engine/src/stack2.cpp`) -> Impact: **475.8** | LOC: 599
- `MCScreenDC::handle` (@ `engine/src/lnxdclnx.cpp`) -> Impact: **454.6** | LOC: 729

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `engine/src` | 816 | 323950.52 | 35.61% | 59.89% |
| `libfoundation/src` | 59 | 24210.18 | 37.25% | 66.04% |
| `ide-support` | 11 | 22412.3 | 85.3% | 66.81% |
| `gyp/pylib/gyp` | 25 | 12288.4 | 35.31% | 39.5% |
| `gyp/pylib/gyp/generator` | 12 | 10191.64 | 35.08% | 50.2% |
| `libgraphics/src` | 21 | 9570.92 | 44.5% | 65.86% |
| `extensions/libraries/timezone/tz` | 34 | 9357.48 | 21.3% | 6.77% |
| `lcidlc/src` | 24 | 8972.26 | 26.08% | 38.8% |
| `libscript/src` | 72 | 8799.3 | 13.91% | 50.71% |
| `toolchain/gentle/gentle` | 10 | 8364.98 | 47.45% | 14.31% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `gyp/pylib/gyp/common_test.py` -> **100.0%** Exposure
- `engine/src/mac-internal.h` -> **100.0%** Exposure
- `engine/src/mbliphoneapp.h` -> **100.0%** Exposure
- `engine/src/mbliphoneview.h` -> **100.0%** Exposure
- `revmobile/src/CoreSimulator.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `config.py` -> **100.0%** Exposure
- `fetch.py` -> **100.0%** Exposure
- `gyp/PRESUBMIT.py` -> **100.0%** Exposure
- `gyp/gyptest.py` -> **100.0%** Exposure
- `gyp/pylib/gyp/MSVSNew.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `engine/src/exec-interface2.cpp` -> **286** Orphaned Functions | **0** Duplicates
- `engine/src/exec-interface-object.cpp` -> **257** Orphaned Functions | **0** Duplicates
- `engine/src/module-canvas.cpp` -> **241** Orphaned Functions | **0** Duplicates
- `engine/src/exec-interface.cpp` -> **194** Orphaned Functions | **0** Duplicates
- `engine/src/exec-interface-stack.cpp` -> **191** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11306` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ide-support/revdeploylibraryios.livecodescript` (LIVECODE) -> Cumulative Risk: **777.44**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 699.92 | **LOC:** 724 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.3694%)
- **Heaviest Functions:** `deployDo` (Impact: 160.3), `deployAutoconfigureSDKs` (Impact: 25.4), `deployGetIphoneOSes` (Impact: 21.8)

### 2. `engine/src/em-liburl.js` (JAVASCRIPT) -> Cumulative Risk: **777.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 178.8 | **LOC:** 277 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%)
- **Heaviest Functions:** `requestSend` (Impact: 13.2), `requestCallbackLoad` (Impact: 10.1), `requestCreate` (Impact: 7.9)

### 3. `benchmarks/_benchmarkrunner.livecodescript` (LIVECODE) -> Cumulative Risk: **747.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 272.02 | **LOC:** 356 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.0105%)
- **Heaviest Functions:** `runGetBenchmarkFileNames_Recursive` (Impact: 31.1), `runSingleCommand` (Impact: 18.1), `runGetBenchmarkCommandNames` (Impact: 17.1)

### 4. `builder/builder_utilities.livecodescript` (LIVECODE) -> Cumulative Risk: **743.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 646.72 | **LOC:** 894 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9163%), Tech Debt (99.5989%)
- **Heaviest Functions:** `builderFetchEngine` (Impact: 55.1), `dietAndStrip` (Impact: 46.6), `builderBuild` (Impact: 43.2)

### 5. `revmobile/src/reviphoneproxy.mm` (OBJECTIVE-C) -> Cumulative Risk: **742.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 223.94 | **LOC:** 357 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9566%), Safety Score (99.237%)
- **Heaviest Functions:** `main` (Impact: 46.5), `getSimDeviceSet` (Impact: 12.8), `isValid` (Impact: 5.5)

### 6. `engine/src/java/com/runrev/android/URLLoader.java` (JAVA) -> Cumulative Risk: **724.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 214.32 | **LOC:** 337 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%)
- **Heaviest Functions:** `run` (Impact: 22.1), `setHeaders` (Impact: 10.8), `URLLoader` (Impact: 8.3)

### 7. `builder/installer/installeruiupdatedownloadcardbehavior.livecodescript` (LIVECODE) -> Cumulative Risk: **721.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 184.8 | **LOC:** 195 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.996%)
- **Heaviest Functions:** `downloadNewVersion` (Impact: 32.5), `launchDownloadedInstaller` (Impact: 29.6), `downloadLatestRevisionComplete` (Impact: 11.1)

### 8. `extensions/script-libraries/oauth2/oauth2.livecodescript` (LIVECODE) -> Cumulative Risk: **721.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 242.78 | **LOC:** 429 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.2971%)
- **Heaviest Functions:** `OAuth2` (Impact: 68.8), `__HandleRequest` (Impact: 19.8), `__RemoveDialog` (Impact: 9.2)

### 9. `engine/src/java/com/runrev/android/billing/samsung/SamsungBillingProvider.java` (JAVA) -> Cumulative Risk: **720.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 405.88 | **LOC:** 609 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.981%), Tech Debt (99.9083%), Documentation (98.4615%)
- **Heaviest Functions:** `handleRequestPayment` (Impact: 22.6), `mapResponseCode` (Impact: 18.3), `OnSucceedGetInboxList` (Impact: 13.4)

### 10. `builder/installer/installeruiwaitcardbehavior.livecodescript` (LIVECODE) -> Cumulative Risk: **707.51**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 75.98 | **LOC:** 118 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9053%), Concurrency (98.2883%)
- **Heaviest Functions:** `fetchConflictingMac` (Impact: 14.0), `fetchConflictingApps` (Impact: 5.8), `fetchConflictingLinux` (Impact: 4.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `toolchain/gentle/gentle/yytab.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7013.84 | **LOC:** 6509 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.612%), Tech Debt (7.9512%)
**Top Internal Functions/Classes:**
  * `yyparse` (Impact: 370.6)
  * `yysymprint` (Impact: 13.5)
    * *Intent:* `--------------------------------*/
  * `yystpcpy` (Impact: 9.5)
    * *Intent:* # endif # endif # ifndef yystpcpy # if defined (__GLIBC__) && defined (_STRING_H) && defined (_GNU_S...
  * `yydestruct` (Impact: 7.9)
    * *Intent:* `-----------------------------------------------*/
  * `yystrlen` (Impact: 7.8)
    * *Intent:* #ifndef YYMAXDEPTH # define YYMAXDEPTH 10000 #endif #if YYERROR_VERBOSE # ifndef yystrlen # if defin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1987 instances
* *State Mutation (weighted view):* 6434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 472`, `structural_boundaries: 203`, `args: 59`, `func_start: 1`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2460`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 40`, `import: 3`
* *Defense:* `safety: 4`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stddef.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revliburl.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5996.72 | **LOC:** 5369 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.5449%), Tech Debt (62.5295%)
**Top Internal Functions/Classes:**
  * `ulGetFormat` (Impact: 119.9)
    * *Intent:* ####################breaks down the url into components####################
  * `ulFtpGet` (Impact: 107.9)
    * *Intent:* #####################FTP GET##################
  * `ulDoProcess` (Impact: 83.4)
    * *Intent:* -------------------------------------------
  * `ulBuildHttpRequest` (Impact: 83.0)
  * `ulFtpSend` (Impact: 79.7)
    * *Intent:* ##############FTP PUT #########################
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 5 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 1030 instances
* *High Risk Execution (weighted view):* 27
* *Concurrency (weighted view):* 87
* *Sec Tainted Injection (weighted view):* 5
* *State Mutation (weighted view):* 3212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1280`, `structural_boundaries: 2095`, `args: 129`, `func_start: 159`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 30`, `state_mutation: 1152`, `dead_code: 42`, `fragile_debt: 17`, `unreferenced_by_name: 56`
* *Architecture:* `io: 33`, `api: 137`, `concurrency: 17`
* *Defense:* `safety: 27`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libfoundation/src/foundation-string.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5500.06 | **LOC:** 7360 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.1585%), Tech Debt (81.6117%)
**Top Internal Functions/Classes:**
  * `MCStringFormatV` (Impact: 233.2)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringCreateWithBytes` (Impact: 96.8)
    * *Intent:* // Create an immutable string from the given bytes, interpreting them using // the specified encodin...
  * `MCStringConvertToBytes` (Impact: 88.2)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringSplit` (Impact: 84.7)
  * `MCStringDelimitedOffset` (Impact: 71.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 679 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1177`, `structural_boundaries: 651`, `args: 285`, `func_start: 226`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 755`, `dead_code: 9`, `planned_debt: 5`, `fragile_debt: 34`, `unreferenced_by_name: 88`
* *Architecture:* `import: 12`
* *Defense:* `doc: 35`, `immutability_locks: 118`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Windows.h, errno.h, foundation-auto.h, foundation-bidi.h, foundation-chunk.h, foundation-private.h, foundation-string-native.cpp.h, foundation-unicode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/object.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5266.66 | **LOC:** 5885 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.2121%), Tech Debt (99.7563%)
**Top Internal Functions/Classes:**
  * `MCObject::getforecolor` (Impact: 281.8)
  * `MCObject::save` (Impact: 235.6)
  * `MCObject::kdown` (Impact: 216.5)
  * `MCObject::load` (Impact: 163.2)
    * *Intent:* /////////////////////////////////////////////////////////////////////////////// // // SAVING AND LOA...
  * `MCObject::message` (Impact: 91.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 695 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 2217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1217`, `structural_boundaries: 496`, `args: 329`, `func_start: 228`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 827`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 44`, `unreferenced_by_name: 183`
* *Architecture:* `io: 5`, `import: 52`
* *Defense:* `safety: 1`, `doc: 13`, `immutability_locks: 41`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 51):` MCBlock.h, aclip.h, bitmapeffect.h, button.h, card.h, cdata.h, chunk.h, context.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/module-canvas.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4673.06 | **LOC:** 7185 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.4015%), Tech Debt (98.9486%)
**Top Internal Functions/Classes:**
  * `MCCanvasPathSVGParseCallback` (Impact: 94.6)
  * `MCSVGParseParams` (Impact: 89.7)
  * `MCCanvasEffectMakeWithPropertyArray` (Impact: 82.7)
  * `MCGPathToSVGDataCallback` (Impact: 47.5)
  * `MCCanvasFillTextAligned` (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 565 instances
* *State Mutation (weighted view):* 2025
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 698`, `structural_boundaries: 837`, `args: 692`, `func_start: 519`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 895`, `dead_code: 3`, `planned_debt: 29`, `fragile_debt: 1`, `unreferenced_by_name: 241`
* *Architecture:* `import: 7`
* *Defense:* `doc: 55`, `sync_locks: 2`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` image.h, module-canvas-internal.h, module-canvas.h, module-engine.h, prefix.h, stack.h, widget.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/dskmac.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4556.76 | **LOC:** 6008 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.2305%), Tech Debt (96.3871%)
**Top Internal Functions/Classes:**
  * `SetResource` (Impact: 122.5)
  * `MCS_startprocess_unix` (Impact: 101.3)
  * `RequestAE` (Impact: 85.8)
    * *Intent:* // MW-2006-08-05: Vetted for Endian issues
  * `getAEAttributes` (Impact: 82.5)
    * *Intent:* // MW-2006-08-05: Vetted for Endian issues
  * `getAEParams` (Impact: 82.5)
    * *Intent:* // MW-2006-08-05: Vetted for Endian issues
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 617 instances
* *Memory Alloc (weighted view):* 29
* *State Mutation (weighted view):* 1964
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1068`, `structural_boundaries: 525`, `args: 302`, `func_start: 157`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 730`, `dead_code: 10`, `planned_debt: 8`, `fragile_debt: 56`, `unreferenced_by_name: 94`
* *Architecture:* `io: 15`, `api: 2`, `import: 41`
* *Defense:* `doc: 39`, `sync_locks: 42`, `immutability_locks: 34`, `cleanup: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` CoreFoundation.h, IOBSD.h, IOKitLib.h, IOSerialKeys.h, Authorization.h, AuthorizationTags.h, button.h, card.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lcidlc/src/Support.mm` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4254.86 | **LOC:** 4484 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.3499%), Tech Debt (98.4532%)
**Top Internal Functions/Classes:**
  * `LCValueArrayFromObjcDictionary` (Impact: 665.9)
  * `LCValueFetch` (Impact: 136.7)
  * `LCValueStore` (Impact: 87.0)
  * `LCArrayLookupKeyOnPath` (Impact: 73.9)
  * `LCArrayListKeysOnPath` (Impact: 70.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 560 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 1727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 422`, `args: 215`, `func_start: 215`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 607`, `planned_debt: 1`, `fragile_debt: 23`, `unreferenced_by_name: 115`
* *Architecture:* `io: 9`, `api: 3`, `import: 12`
* *Defense:* `doc: 36`, `immutability_locks: 122`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Foundation.h, LiveCode.h, UIKit.h, log.h, jni.h, pthread.h, stdarg.h, stdint.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/paragraf.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4077.88 | **LOC:** 4022 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.5592%), Tech Debt (99.9901%)
**Top Internal Functions/Classes:**
  * `MCParagraph::setfocus` (Impact: 310.7)
  * `MCParagraph::draw` (Impact: 295.4)
    * *Intent:* //draw text of paragraph
  * `MCParagraph::fillselect` (Impact: 195.2)
    * *Intent:* // MW-2008-04-02: [[ Bug 6259 ]] Make sure front and back hilites are only // drawn if appropriate....
  * `MCParagraph::fmovefocus` (Impact: 121.7)
  * `MCParagraph::load` (Impact: 114.0)
    * *Intent:* // **** mutate blocks
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 594 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 1836
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 818`, `structural_boundaries: 169`, `args: 111`, `func_start: 92`
* *Risk/State:* `state_mutation: 648`, `dead_code: 6`, `planned_debt: 6`, `fragile_debt: 90`, `unreferenced_by_name: 88`
* *Architecture:* `import: 20`
* *Defense:* `safety: 3`, `immutability_locks: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` MCBlock.h, context.h, exec-interface.h, field.h, filedefs.h, globals.h, globdefs.h, line.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/libraries/timezone/tz/zic.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3734.7 | **LOC:** 3261 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.8425%), Tech Debt (11.5873%)
**Top Internal Functions/Classes:**
  * `writezone` (Impact: 212.9)
  * `outzone` (Impact: 160.4)
  * `rulesub` (Impact: 120.6)
  * `main` (Impact: 97.8)
  * `is_alpha` (Impact: 78.6)
    * *Intent:* /* Is A an alphabetic character in the C locale? */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Rce:* 7 instances
* *Amplified Cascading Flux:* 647 instances
* *Memory Alloc (weighted view):* 3
* *Sec Tainted Injection (weighted view):* 7
* *State Mutation (weighted view):* 1976
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 806`, `structural_boundaries: 496`, `args: 139`, `func_start: 67`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 27`, `state_mutation: 682`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 18`, `api: 11`, `import: 12`
* *Defense:* `safety: 13`, `immutability_locks: 178`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` direct.h, fcntl.h, io.h, locale.h, private.h, stdarg.h, stddef.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/ibmp.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3623.48 | **LOC:** 2975 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.402%), Tech Debt (50.2952%)
**Top Internal Functions/Classes:**
  * `xpm_read_v1_header` (Impact: 148.3)
  * `bmp_read_dib_header` (Impact: 87.6)
  * `bmp_read_rle4_image` (Impact: 84.4)
    * *Intent:* // IM-2013-08-16: [[ Bugfix 10278 ]] Add support for reading RLE compressed BMP images
  * `MCXBMImageLoader::LoadHeader` (Impact: 81.4)
  * `MCBitmapConvertRow` (Impact: 77.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 620 instances
* *State Mutation (weighted view):* 1890
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 615`, `structural_boundaries: 159`, `args: 105`, `func_start: 79`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 650`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 29`
* *Architecture:* `api: 7`, `import: 10`
* *Defense:* `doc: 11`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` filedefs.h, globals.h, image.h, imageloader.h, mcio.h, objdefs.h, parsedef.h, prefix.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/button.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3577.6 | **LOC:** 3966 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.1273%), Tech Debt (98.5671%)
**Top Internal Functions/Classes:**
  * `MCButton::mup` (Impact: 215.6)
  * `MCButton::mfocus` (Impact: 185.3)
  * `MCButton::kdown` (Impact: 152.8)
  * `MCButton::save` (Impact: 136.5)
  * `MCButton::load` (Impact: 132.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 490 instances
* *State Mutation (weighted view):* 1532
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1073`, `structural_boundaries: 248`, `args: 202`, `func_start: 96`, `class_start: 2`
* *Risk/State:* `state_mutation: 552`, `dead_code: 8`, `fragile_debt: 45`, `unreferenced_by_name: 83`
* *Architecture:* `api: 2`, `import: 35`
* *Defense:* `doc: 4`, `immutability_locks: 9`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` button.h, card.h, cdata.h, date.h, dispatch.h, exec.h, field.h, filedefs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3501.2 | **LOC:** 3772 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.9198%), Tech Debt (99.7301%)
**Top Internal Functions/Classes:**
  * `MCExecFetchProperty` (Impact: 569.4)
  * `MCExecStoreProperty` (Impact: 447.5)
  * `MCExecTypeConvertToValueRefAndReleaseAlways` (Impact: 94.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCExecTypeConvertNumbers` (Impact: 93.5)
  * `MCExecTypeAssign` (Impact: 83.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 285 instances
* *State Mutation (weighted view):* 877
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 967`, `structural_boundaries: 481`, `args: 209`, `func_start: 153`
* *Risk/State:* `safety_bypasses: 99`, `state_mutation: 307`, `planned_debt: 1`, `fragile_debt: 37`, `unreferenced_by_name: 121`
* *Architecture:* `import: 25`
* *Defense:* `safety: 1`, `doc: 16`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` debug.h, exec.h, field.h, filedefs.h, globals.h, globdefs.h, handler.h, hndlrlst.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revdocsparser.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3500.1 | **LOC:** 2938 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.3144%), Tech Debt (29.1521%)
**Top Internal Functions/Classes:**
  * `revDocsExtractDocBlocks` (Impact: 236.4)
    * *Intent:* */
  * `revDocsParseDocText` (Impact: 146.2)
  * `revDocsFormatInlineComments` (Impact: 140.8)
  * `revDocsParseElements` (Impact: 86.0)
  * `revDocsExtractElementsWithRegex` (Impact: 80.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 552 instances
* *State Mutation (weighted view):* 1801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 675`, `structural_boundaries: 1173`, `args: 89`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `state_mutation: 697`, `dead_code: 25`, `fragile_debt: 4`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 71`
* *Defense:* `safety: 2`, `doc: 9`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-interface.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3466.54 | **LOC:** 4643 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.7812%), Tech Debt (99.9828%)
**Top Internal Functions/Classes:**
  * `MCInterfaceExecGo` (Impact: 172.0)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCInterfaceProcessToContainer` (Impact: 112.5)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCInterfaceExecClone` (Impact: 92.3)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCInterfaceExecResetTemplate` (Impact: 51.3)
  * `MCInterfaceExportBitmapToFile` (Impact: 44.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 311 instances
* *State Mutation (weighted view):* 983
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 786`, `structural_boundaries: 470`, `args: 463`, `func_start: 244`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 361`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 49`, `unreferenced_by_name: 194`
* *Architecture:* `import: 43`
* *Defense:* `doc: 88`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` aclip.h, button.h, card.h, cardlst.h, chunk.h, date.h, debug.h, dispatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/util.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3414.3 | **LOC:** 3379 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.1128%), Tech Debt (17.3208%)
**Top Internal Functions/Classes:**
  * `MCU_strtol` (Impact: 133.0)
  * `MCU_roundrect` (Impact: 90.1)
    * *Intent:* // MDW-2014-07-09: [[ oval_points ]] need to factor in startAngle and arcAngle // this is now used f...
  * `MCU_fix_path` (Impact: 64.5)
    * *Intent:* // MW-2004-11-26: Replace strcpy with strmov - overalapping regions (VG)
  * `MCU_path_compute_split_win32` (Impact: 51.8)
  * `MCU_geturl` (Impact: 45.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 479 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 1502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 686`, `structural_boundaries: 277`, `args: 166`, `func_start: 138`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 544`, `dead_code: 17`, `fragile_debt: 17`
* *Architecture:* `api: 81`, `import: 27`
* *Defense:* `doc: 12`, `sync_locks: 12`, `immutability_locks: 103`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` aclip.h, algorithm, card.h, dispatch.h, exec.h, field.h, filedefs.h, globals.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `revxml/src/revxml.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3282.94 | **LOC:** 3136 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.8737%), Tech Debt (60.3165%)
**Top Internal Functions/Classes:**
  * `xpathNodeBufGetContent` (Impact: 142.4)
    * *Intent:* /** * xmlNodeBufGetContent: * @buffer: a buffer * @cur: the node being read * * Read the value of a ...
  * `XML_ListOfChildText` (Impact: 70.6)
    * *Intent:* */
  * `xpathNodeGetContent` (Impact: 62.4)
    * *Intent:* /** * xmlNodeGetContent: * @cur: the node being read * * Read the value of a node, this can be eithe...
  * `XML_SetElementContents` (Impact: 56.3)
    * *Intent:* */
  * `XML_FindElementByAttributeValue` (Impact: 47.7)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 527 instances
* *Memory Alloc (weighted view):* 42
* *State Mutation (weighted view):* 1599
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 597`, `structural_boundaries: 124`, `args: 98`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `state_mutation: 545`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 17`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`, `api: 1`, `import: 12`
* *Defense:* `safety: 3`, `doc: 12`, `immutability_locks: 18`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cmath, cstdio, cstdlib, ctime, cxml.h, xpath.h, transform.h, xsltutils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revsblibrary.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3255.42 | **LOC:** 3194 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.3764%), Tech Debt (16.4503%)
**Top Internal Functions/Classes:**
  * `__revSBCopyFile` (Impact: 151.3)
    * *Intent:* #?semantics # Copy a file and it's attributes for as much as we can. # Sends a callback with the num...
  * `revCheckObject` (Impact: 111.3)
  * `__revSBCopyFolder` (Impact: 97.6)
    * *Intent:* --- #?semantics # Copies a folder and all it's contents, under which we understand: # - (sub)folders...
  * `__UpdateSettingsFromCodeFolder` (Impact: 94.4)
  * `revSBWriteFile` (Impact: 74.4)
    * *Intent:* # This handler has not been tested..
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 381 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 1240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 785`, `structural_boundaries: 1019`, `args: 110`, `func_start: 140`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 478`, `dead_code: 8`, `fragile_debt: 14`
* *Architecture:* `io: 17`, `api: 88`, `concurrency: 4`
* *Defense:* `safety: 37`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 31`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gyp/pylib/gyp/generator/msvs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3200.04 | **LOC:** 3433 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.0012%), Tech Debt (14.8242%)
**Top Internal Functions/Classes:**
  * `_BuildCommandLineForRuleRaw` (Impact: 80.4)
  * `_AddSources2` (Impact: 53.8)
  * `_GenerateExternalRules` (Impact: 43.6)
  * `_AdjustSourcesAndConvertToFilterHierarchy` (Impact: 42.2)
  * `_ConvertSourcesToFilterHierarchy` (Impact: 39.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 542 instances
* *State Mutation (weighted view):* 1783
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 290`, `args: 117`, `func_start: 117`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 1`, `state_mutation: 699`, `dead_code: 7`, `planned_debt: 18`, `fragile_debt: 5`
* *Architecture:* `io: 57`, `api: 7`, `import: 21`
* *Defense:* `safety: 14`, `doc: 54`, `sync_locks: 21`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.61
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` collections, copy, gyp.MSVSNew, gyp.MSVSProject, gyp.MSVSSettings, gyp.MSVSToolFile, gyp.MSVSUserFile, gyp.MSVSUtil...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `engine/src/card.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3115.52 | **LOC:** 3573 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.8636%), Tech Debt (99.6665%)
**Top Internal Functions/Classes:**
  * `MCCard::getchild` (Impact: 219.8)
  * `MCCard::getchildbyid` (Impact: 99.3)
  * `MCCard::relayer` (Impact: 94.7)
  * `MCCard::mdown` (Impact: 93.1)
  * `MCCard::getchildbyordinal` (Impact: 70.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 329 instances
* *State Mutation (weighted view):* 1015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 984`, `structural_boundaries: 233`, `args: 217`, `func_start: 107`, `class_start: 2`
* *Risk/State:* `state_mutation: 357`, `dead_code: 3`, `fragile_debt: 38`, `unreferenced_by_name: 103`
* *Architecture:* `import: 45`
* *Defense:* `doc: 5`, `immutability_locks: 12`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` aclip.h, button.h, card.h, cdata.h, context.h, cpalette.h, debug.h, dispatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-interface-object.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3112.74 | **LOC:** 4865 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.8083%), Tech Debt (99.9866%)
**Top Internal Functions/Classes:**
  * `MCObject::DoGetProperties` (Impact: 94.7)
  * `MCInterfaceTextStyleFormat` (Impact: 68.3)
  * `MCInterfaceTextStyleParse` (Impact: 64.9)
    * *Intent:* //////////
  * `MCObject::GetRevAvailableVariables` (Impact: 63.5)
  * `MCObject::SetParentScript` (Impact: 56.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 415`, `args: 358`, `func_start: 279`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 401`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 29`, `unreferenced_by_name: 257`
* *Architecture:* `import: 34`
* *Defense:* `doc: 28`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` button.h, card.h, cdata.h, chunk.h, dispatch.h, exec-interface.h, exec.h, field.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `util/perfect/perfect.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3106.06 | **LOC:** 3119 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2413%), Tech Debt (9.6766%)
**Top Internal Functions/Classes:**
  * `hexfour` (Impact: 228.0)
    * *Intent:* /* * Find a perfect hash when there are only four keys. Max 10 instructions. * Note that a perfect h...
  * `initalen` (Impact: 146.0)
    * *Intent:* /* guess initial values for alen and blen */
  * `hexn` (Impact: 127.8)
    * *Intent:* * * The code will probably look like this, minus some stuff: * val += CONSTANT; * val ^= (val<<16); ...
  * `hexthree` (Impact: 103.2)
    * *Intent:* /* * Find a perfect hash when there are only three keys. Max 6 instructions. * * keys a,b,c. * There...
  * `findhash` (Impact: 76.3)
    * *Intent:* /* ** Try to find a perfect hash function. ** Return the successful initializer for the initial hash...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 19 instances
* *Amplified Cascading Flux:* 506 instances
* *High Risk Execution (weighted view):* 11
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1595
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 534`, `structural_boundaries: 194`, `args: 7`, `func_start: 38`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 144`, `high_risk_execution: 18`, `state_mutation: 583`, `dead_code: 12`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 36`, `import: 5`
* *Defense:* `safety: 15`, `doc: 11`, `immutability_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stddef.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/exec-files.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3053.58 | **LOC:** 2769 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.3429%), Tech Debt (99.6948%)
**Top Internal Functions/Classes:**
  * `MCFilesExecPerformReadFixedFor` (Impact: 411.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCFilesExecPerformReadCodeUnit` (Impact: 188.1)
    * *Intent:* // Reads from the stream a codeunit and put it back in the end of the mutable buffer x_buffer // For...
  * `MCFilesExecWriteToStream` (Impact: 165.1)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCFilesExecPerformReadBinaryUntil` (Impact: 148.2)
  * `MCFilesExecPerformReadTextUntil` (Impact: 127.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *State Mutation (weighted view):* 722
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 687`, `structural_boundaries: 221`, `args: 189`, `func_start: 118`
* *Risk/State:* `state_mutation: 254`, `dead_code: 1`, `fragile_debt: 27`, `unreferenced_by_name: 83`
* *Architecture:* `import: 14`
* *Defense:* `doc: 28`, `sync_locks: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` exec.h, filedefs.h, globals.h, globdefs.h, mcerror.h, mcio.h, mode.h, objdefs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/stack2.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2932.78 | **LOC:** 3294 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.4908%), Tech Debt (99.975%)
**Top Internal Functions/Classes:**
  * `MCStack::openrect` (Impact: 475.8)
  * `MCStack::getchild` (Impact: 149.2)
  * `MCStack::getbackground` (Impact: 120.2)
  * `MCStack::count` (Impact: 86.7)
  * `MCStack::getAV` (Impact: 83.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 338 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1086
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 848`, `structural_boundaries: 243`, `args: 190`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 410`, `dead_code: 3`, `fragile_debt: 55`, `unreferenced_by_name: 108`
* *Architecture:* `api: 1`, `import: 38`
* *Defense:* `doc: 10`, `sync_locks: 2`, `immutability_locks: 26`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` aclip.h, button.h, card.h, cardlst.h, context.h, dispatch.h, field.h, filedefs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/group.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2922.24 | **LOC:** 3139 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.9855%), Tech Debt (99.4769%)
**Top Internal Functions/Classes:**
  * `MCGroup::load` (Impact: 138.3)
  * `MCGroup::getchild` (Impact: 107.5)
  * `MCGroup::draw` (Impact: 104.7)
    * *Intent:* //----------------------------------------------------------------------------- // Redraw Management...
  * `MCGroup::mfocus_control` (Impact: 75.0)
  * `MCGroup::save` (Impact: 71.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 392 instances
* *State Mutation (weighted view):* 1199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 832`, `structural_boundaries: 252`, `args: 203`, `func_start: 94`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 415`, `dead_code: 4`, `fragile_debt: 30`, `unreferenced_by_name: 92`
* *Architecture:* `import: 35`
* *Defense:* `doc: 3`, `immutability_locks: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` button.h, card.h, cdata.h, context.h, cpalette.h, dispatch.h, eps.h, exec.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/opensslsocket.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2920.58 | **LOC:** 2528 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.2986%), Tech Debt (91.4521%)
**Top Internal Functions/Classes:**
  * `MCSocket::readsome` (Impact: 327.8)
    * *Intent:* #endif
  * `MCSocket::write` (Impact: 305.9)
    * *Intent:* // MM-2014-02-12: [[ SecureSocket ]] Updated to pass in if this write should be encrypted, rather th...
  * `MCSocket::read` (Impact: 254.4)
    * *Intent:* // MM-2014-02-12: [[ SecureSocket ]] Updated to pass in if this read is encrypted, rather than check...
  * `MCSocket::writesome` (Impact: 246.4)
  * `MCS_accept` (Impact: 104.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 257 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 792
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 603`, `structural_boundaries: 201`, `args: 123`, `func_start: 67`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 278`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 16`, `unreferenced_by_name: 41`
* *Architecture:* `io: 18`, `import: 54`
* *Defense:* `doc: 5`, `sync_locks: 1`, `immutability_locks: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` SCDynamicStore.h, SCDynamicStoreKey.h, SCSchemaDefinitions.h, inet.h, nameser.h, card.h, errno.h, exec.h...
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

- `libfoundation/include/foundation-auto.h` -> **Severity: 0.022** (Bridge: 0.0003 * Flux: 64.2653%)
- `engine/src/globals.h` -> **Severity: 0.021** (Bridge: 0.0024 * Flux: 8.6841%)
- `engine/src/parsedef.h` -> **Severity: 0.01** (Bridge: 0.0011 * Flux: 8.7715%)
- `engine/src/mcutility.h` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 73.5178%)
- `engine/src/system.h` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 99.358%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libfoundation/include/foundation-span.h` -> **Severity: 2256.7** (Blast Radius: 22.567 * Doc Risk: 100.0%)
- `libfoundation/include/foundation-auto.h` -> **Severity: 2068.127** (Blast Radius: 25.796 * Doc Risk: 80.1724%)
- `tests/lcb/compiler/iterator.lcb` -> **Severity: 1950.4** (Blast Radius: 19.504 * Doc Risk: 100.0%)
- `engine/src/object.h` -> **Severity: 1765.39** (Blast Radius: 17.858 * Doc Risk: 98.8571%)
- `engine/src/objdefs.h` -> **Severity: 1239.7** (Blast Radius: 12.397 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
