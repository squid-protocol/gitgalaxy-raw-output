# ARCHITECTURAL_BRIEF: livecode
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/livecode/livecode.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2256 analyzed artifact(s), 635362 LOC.
- **Load-bearing artifact:** `engine/src/prefix.h` -- 440 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `engine/src/globals.cpp` -- pulls in 58 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `toolchain/gentle/gentle/yytab.c` at magnitude 7013.84 (structural weight, not risk).
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
| Avg Path Length | 2.5651 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 85 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1035 | 431164 | 45.9% |
| LIVECODE | 434 | 71542 | 19.2% |
| MARKDOWN | 203 | 0 | 9.0% |
| PYTHON | 136 | 33101 | 6.0% |
| OBJECTIVE-C | 108 | 49473 | 4.8% |
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
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `4.002`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +4.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 25%, Data / Markup / Trivial 20%, Declarative / Non-Code 16%, Parameter Forwarders Files 9%, Interface Declarations Files 8%
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
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 41.3 | 17.5 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 29.4 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.1 | 29.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.5 | 2.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.4 | 93.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 106743 | 1224 | 139 | `libfoundation/src/foundation-string.cpp` |
| cleanup | 1501 | 365 | 1 | `engine/src/dskmac.cpp` |
| guards | 18098 | 1238 | 20 | `extensions/libraries/timezone/tz/zic.c` |
| danger | 9129 | 847 | 10 | `engine/src/java/com/runrev/android/Engine.java` |
| concurrency | 919 | 245 | 1 | `engine/src/dskmac.cpp` |
| connectivity | 9822 | 886 | 10 | `engine/src/funcs.h` |
| io | 2394 | 245 | 1 | `extensions/libraries/timezone/tz/tz-link.html` |
| crypto | 3 | 3 | 0 | `gyp/pylib/gyp/MSVSNew.py` |
| ipc | 493 | 100 | 0 | `tests/lcs/core/network/network.livecodescript` |
| time | 323 | 52 | 0 | `extensions/libraries/timezone/tz/localtime.c` |
| serialization | 25 | 10 | 0 | `extensions/libraries/json/json.lcb` |
| regex | 277 | 78 | 0 | `ide-support/revdocsparser.livecodescript` |
| events | 2724 | 517 | 3 | `engine/src/java/com/runrev/android/Engine.java` |
| tests | 453 | 48 | 0 | `libfoundation/test/test_typeconvert.cpp` |
| docs | 7688 | 838 | 9 | `engine/src/canvas.lcb` |
| debt | 6419 | 809 | 7 | `toolchain/lc-compile/src/syntax-gen.c` |
| mutation | 167803 | 1439 | 208 | `toolchain/gentle/gentle/yytab.c` |
| dead_code | 19665 | 1290 | 23 | `engine/src/exec-interface2.cpp` |
| credential | 92 | 14 | 0 | `prebuilt/libcef.gyp` |
| threat | 4578 | 618 | 2 | `engine/src/sysdefs.h` |
| ml_ai | 744 | 139 | 0 | `tests/lcs/core/math/math.livecodescript` |
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

- `MCWindowProc` **(Many-Argument Workhorses)** (@ `engine/src/w32dcw32.cpp`) -> Impact: **839.3** | LOC: 1044
  * *Intent:* #endif #include <crtdbg.h>
- `MCButton::draw` **(Many-Argument Workhorses)** (@ `engine/src/buttondraw.cpp`) -> Impact: **777.3** | LOC: 609
  * *Intent:* #include "button.h" #include "field.h" #include "stacklst.h" #include "undolst.h" #include "mcerror.h" #include "param.h" #include "globals.h" #includ...
- `MCProperty::parse` **(Many-Argument Workhorses)** (@ `engine/src/property.cpp`) -> Impact: **759.0** | LOC: 665
- `revSaveAsMobileStandaloneMain` **(Many-Argument Workhorses)** (@ `ide-support/revsaveasandroidstandalone.livecodescript`) -> Impact: **715.2** | LOC: 1021
- `LCValueArrayFromObjcDictionary` **(Many-Argument Workhorses)** (@ `lcidlc/src/Support.mm`) -> Impact: **665.9** | LOC: 2059
- `MCExecFetchProperty` **(Many-Argument Workhorses)** (@ `engine/src/exec.cpp`) -> Impact: **569.4** | LOC: 878
- `MCChunk::getoptionalobj` **(Many-Argument Workhorses)** (@ `engine/src/chunk.cpp`) -> Impact: **484.7** | LOC: 574
- `REVVideoGrabber` **(Many-Argument Workhorses)** (@ `revvideograbber/src/revvideograbber.cpp`) -> Impact: **483.3** | LOC: 564
- `MCStack::openrect` **(Many-Argument Workhorses)** (@ `engine/src/stack2.cpp`) -> Impact: **475.8** | LOC: 599
- `MCScreenDC::handle` **(Many-Argument Workhorses)** (@ `engine/src/lnxdclnx.cpp`) -> Impact: **454.6** | LOC: 729

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `engine/src` | 816 | 323850.52 | 35.61% | 60.28% |
| `libfoundation/src` | 59 | 24210.18 | 37.25% | 66.04% |
| `ide-support` | 11 | 22412.3 | 85.3% | 66.81% |
| `gyp/pylib/gyp` | 25 | 12288.4 | 35.31% | 39.5% |
| `gyp/pylib/gyp/generator` | 12 | 10191.64 | 35.08% | 50.2% |
| `libgraphics/src` | 21 | 9570.92 | 44.5% | 65.86% |
| `extensions/libraries/timezone/tz` | 34 | 9357.48 | 21.3% | 6.77% |
| `lcidlc/src` | 24 | 8972.26 | 26.08% | 38.8% |
| `libscript/src` | 72 | 8808.3 | 13.91% | 50.39% |
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

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `toolchain/gentle/gentle/yytab.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7013.84 | **LOC:** 6509 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.239; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (86.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `yyparse` **(I/O & Config Routines)** (Impact: 370.6)
  * `yysymprint` **(Stateful Encapsulated Methods)** (Impact: 13.5)
    * *Intent:* `--------------------------------*/
  * `yystpcpy` **(Stateful Encapsulated Methods)** (Impact: 9.5)
    * *Intent:* # endif # endif # ifndef yystpcpy # if defined (__GLIBC__) && defined (_STRING_H) && defined (_GNU_S...
  * `yydestruct` **(Stateful Encapsulated Methods)** (Impact: 7.9)
    * *Intent:* `-----------------------------------------------*/
  * `yystrlen` **(Stateful Encapsulated Methods)** (Impact: 7.8)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5996.72 | **LOC:** 5369 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ulGetFormat` **(Many-Argument Workhorses)** (Impact: 119.9)
    * *Intent:* ####################breaks down the url into components####################
  * `ulFtpGet` **(Compute Cores)** (Impact: 107.9)
    * *Intent:* #####################FTP GET##################
  * `ulDoProcess` **(Compute Cores)** (Impact: 83.4)
    * *Intent:* -------------------------------------------
  * `ulBuildHttpRequest` **(Compute Cores)** (Impact: 83.0)
  * `ulFtpSend` **(Compute Cores)** (Impact: 79.7)
    * *Intent:* ##############FTP PUT #########################
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 1030 instances
* *High Risk Execution (weighted view):* 27
* *Concurrency (weighted view):* 87
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5500.06 | **LOC:** 7360 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.9%), Debt Markers (formerly Tech Debt) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.8407% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCStringFormatV` **(Many-Argument Workhorses)** (Impact: 233.2)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringCreateWithBytes` **(Many-Argument Workhorses)** (Impact: 96.8)
    * *Intent:* // Create an immutable string from the given bytes, interpreting them using // the specified encodin...
  * `MCStringConvertToBytes` **(Many-Argument Workhorses)** (Impact: 88.2)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringSplit` **(Many-Argument Workhorses)** (Impact: 84.7)
  * `MCStringDelimitedOffset` **(Many-Argument Workhorses)** (Impact: 71.2)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5266.66 | **LOC:** 5885 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **52**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (95.3%), Complexity Load (formerly Cognitive Load) (91.2%)
- **Documentation Coverage:** 96.5066% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCObject::getforecolor` **(Many-Argument Workhorses)** (Impact: 281.8)
  * `MCObject::save` **(Many-Argument Workhorses)** (Impact: 235.6)
  * `MCObject::kdown` **(Compute Cores)** (Impact: 216.5)
  * `MCObject::load` **(Many-Argument Workhorses)** (Impact: 163.2)
    * *Intent:* /////////////////////////////////////////////////////////////////////////////// // // SAVING AND LOA...
  * `MCObject::message` **(Many-Argument Workhorses)** (Impact: 91.2)
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
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 4673.06 | **LOC:** 7185 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.9%), Guard Balance (formerly Safety Score) (90.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.2366% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCCanvasPathSVGParseCallback` **(Many-Argument Workhorses)** (Impact: 94.6)
  * `MCSVGParseParams` **(Many-Argument Workhorses)** (Impact: 89.7)
  * `MCCanvasEffectMakeWithPropertyArray` **(Many-Argument Workhorses)** (Impact: 82.7)
  * `MCGPathToSVGDataCallback` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `MCCanvasFillTextAligned` **(Many-Argument Workhorses)** (Impact: 44.1)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4556.76 | **LOC:** 6008 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.4%), Guard Balance (formerly Safety Score) (92.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 89.8089% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetResource` **(Many-Argument Workhorses)** (Impact: 122.5)
  * `MCS_startprocess_unix` **(Many-Argument Workhorses)** (Impact: 101.3)
  * `RequestAE` **(Many-Argument Workhorses)** (Impact: 85.8)
    * *Intent:* // MW-2006-08-05: Vetted for Endian issues
  * `getAEAttributes` **(Many-Argument Workhorses)** (Impact: 82.5)
    * *Intent:* // MW-2006-08-05: Vetted for Endian issues
  * `getAEParams` **(Many-Argument Workhorses)** (Impact: 82.5)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4254.86 | **LOC:** 4484 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.5%), Guard Balance (formerly Safety Score) (97.1%), Complexity Load (formerly Cognitive Load) (81.3%)
- **Documentation Coverage:** 89.9038% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LCValueArrayFromObjcDictionary` **(Many-Argument Workhorses)** (Impact: 665.9)
  * `LCValueFetch` **(Many-Argument Workhorses)** (Impact: 136.7)
  * `LCValueStore` **(Many-Argument Workhorses)** (Impact: 87.0)
  * `LCArrayLookupKeyOnPath` **(Many-Argument Workhorses)** (Impact: 73.9)
  * `LCArrayListKeysOnPath` **(Many-Argument Workhorses)** (Impact: 70.3)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4077.88 | **LOC:** 4022 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCParagraph::setfocus` **(Many-Argument Workhorses)** (Impact: 310.7)
  * `MCParagraph::draw` **(Many-Argument Workhorses)** (Impact: 295.4)
    * *Intent:* //draw text of paragraph
  * `MCParagraph::fillselect` **(Many-Argument Workhorses)** (Impact: 195.2)
    * *Intent:* // drawn if appropriate.
  * `MCParagraph::fmovefocus` **(Compute Cores)** (Impact: 121.7)
  * `MCParagraph::load` **(Many-Argument Workhorses)** (Impact: 114.0)
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
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3734.7 | **LOC:** 3261 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writezone` **(Many-Argument Workhorses)** (Impact: 212.9)
  * `outzone` **(Many-Argument Workhorses)** (Impact: 160.4)
  * `rulesub` **(Many-Argument Workhorses)** (Impact: 120.6)
  * `main` **(Compute Cores)** (Impact: 97.8)
  * `is_alpha` **(Compute Cores)** (Impact: 78.6)
    * *Intent:* /* Is A an alphabetic character in the C locale? */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 647 instances
* *Memory Alloc (weighted view):* 3
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3623.48 | **LOC:** 2975 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 92.4051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xpm_read_v1_header` **(Many-Argument Workhorses)** (Impact: 148.3)
  * `bmp_read_dib_header` **(Many-Argument Workhorses)** (Impact: 87.6)
  * `bmp_read_rle4_image` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `MCXBMImageLoader::LoadHeader` **(Many-Argument Workhorses)** (Impact: 81.4)
  * `MCBitmapConvertRow` **(Many-Argument Workhorses)** (Impact: 77.3)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3577.6 | **LOC:** 3966 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.6%), Guard Balance (formerly Safety Score) (93.8%), Complexity Load (formerly Cognitive Load) (93.1%)
- **Documentation Coverage:** 97.9167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCButton::mup` **(Many-Argument Workhorses)** (Impact: 215.6)
  * `MCButton::mfocus` **(Many-Argument Workhorses)** (Impact: 185.3)
  * `MCButton::kdown` **(Compute Cores)** (Impact: 152.8)
  * `MCButton::save` **(Many-Argument Workhorses)** (Impact: 136.5)
  * `MCButton::load` **(Many-Argument Workhorses)** (Impact: 132.7)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3501.2 | **LOC:** 3772 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Guard Balance (formerly Safety Score) (90.1%), Complexity Load (formerly Cognitive Load) (82.9%)
- **Documentation Coverage:** 90.1961% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCExecFetchProperty` **(Many-Argument Workhorses)** (Impact: 569.4)
  * `MCExecStoreProperty` **(Many-Argument Workhorses)** (Impact: 447.5)
  * `MCExecTypeConvertToValueRefAndReleaseAlways` **(Many-Argument Workhorses)** (Impact: 94.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCExecTypeConvertNumbers` **(Many-Argument Workhorses)** (Impact: 93.5)
  * `MCExecTypeAssign` **(Many-Argument Workhorses)** (Impact: 83.3)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3500.1 | **LOC:** 2938 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (91.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.6102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revDocsExtractDocBlocks` **(Many-Argument Workhorses)** (Impact: 236.4)
    * *Intent:* */
  * `revDocsParseDocText` **(Many-Argument Workhorses)** (Impact: 146.2)
  * `revDocsFormatInlineComments` **(Compute Cores)** (Impact: 140.8)
  * `revDocsParseElements` **(Many-Argument Workhorses)** (Impact: 86.0)
  * `revDocsExtractElementsWithRegex` **(Compute Cores)** (Impact: 80.8)
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
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3466.54 | **LOC:** 4643 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 65.1639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCInterfaceExecGo` **(Many-Argument Workhorses)** (Impact: 172.0)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCInterfaceProcessToContainer` **(Many-Argument Workhorses)** (Impact: 112.5)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCInterfaceExecClone` **(Many-Argument Workhorses)** (Impact: 92.3)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCInterfaceExecResetTemplate` **(Compute Cores)** (Impact: 51.3)
  * `MCInterfaceExportBitmapToFile` **(Many-Argument Workhorses)** (Impact: 44.8)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3414.3 | **LOC:** 3379 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 0.306; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.1%)
- **Documentation Coverage:** 91.7808% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCU_strtol` **(Many-Argument Workhorses)** (Impact: 133.0)
  * `MCU_roundrect` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* // this is now used for both roundrects and ovals
  * `MCU_fix_path` **(Many-Argument Workhorses)** (Impact: 64.5)
    * *Intent:* // MW-2004-11-26: Replace strcpy with strmov - overalapping regions (VG)
  * `MCU_path_compute_split_win32` **(Many-Argument Workhorses)** (Impact: 51.8)
  * `MCU_geturl` **(Many-Argument Workhorses)** (Impact: 45.0)
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
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.000442
  * `Imports (Out-Degree: 24):` aclip.h, algorithm, card.h, dispatch.h, exec.h, field.h, filedefs.h, globals.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `revxml/src/revxml.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3282.94 | **LOC:** 3136 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Complexity Load (formerly Cognitive Load) (70.9%), Debt Markers (formerly Tech Debt) (60.3%)
- **Documentation Coverage:** 84.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xpathNodeBufGetContent` **(Many-Argument Workhorses)** (Impact: 142.4)
    * *Intent:* /** * xmlNodeBufGetContent: * @buffer: a buffer * @cur: the node being read * * Read the value of a ...
  * `XML_ListOfChildText` **(Many-Argument Workhorses)** (Impact: 70.6)
    * *Intent:* */
  * `xpathNodeGetContent` **(Compute Cores)** (Impact: 62.4)
    * *Intent:* /** * xmlNodeGetContent: * @cur: the node being read * * Read the value of a node, this can be eithe...
  * `XML_SetElementContents` **(Many-Argument Workhorses)** (Impact: 56.3)
    * *Intent:* */
  * `XML_FindElementByAttributeValue` **(Many-Argument Workhorses)** (Impact: 47.7)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3255.42 | **LOC:** 3194 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__revSBCopyFile` **(Many-Argument Workhorses)** (Impact: 151.3)
    * *Intent:* #?semantics # Copy a file and it's attributes for as much as we can. # Sends a callback with the num...
  * `revCheckObject` **(Many-Argument Workhorses)** (Impact: 111.3)
  * `__revSBCopyFolder` **(Many-Argument Workhorses)** (Impact: 97.6)
    * *Intent:* --- #?semantics # Copies a folder and all it's contents, under which we understand: # - (sub)folders...
  * `__UpdateSettingsFromCodeFolder` **(Many-Argument Workhorses)** (Impact: 94.4)
  * `revSBWriteFile` **(Many-Argument Workhorses)** (Impact: 74.4)
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
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3200.04 | **LOC:** 3433 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **20**; blast radius 0.61; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.0%)
- **Documentation Coverage:** 61.7886% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_BuildCommandLineForRuleRaw` **(Many-Argument Workhorses)** (Impact: 80.4)
  * `_AddSources2` **(Many-Argument Workhorses)** (Impact: 53.8)
  * `_GenerateExternalRules` **(Many-Argument Workhorses)** (Impact: 43.6)
  * `_AdjustSourcesAndConvertToFilterHierarchy` **(Many-Argument Workhorses)** (Impact: 42.2)
  * `_ConvertSourcesToFilterHierarchy` **(Many-Argument Workhorses)** (Impact: 39.9)
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
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.002409
  * `Imports (Out-Degree: 11):` collections, copy, gyp.MSVSNew, gyp.MSVSProject, gyp.MSVSSettings, gyp.MSVSToolFile, gyp.MSVSUserFile, gyp.MSVSUtil...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `engine/src/card.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3115.52 | **LOC:** 3573 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Guard Balance (formerly Safety Score) (88.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.1963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCCard::getchild` **(Many-Argument Workhorses)** (Impact: 219.8)
  * `MCCard::getchildbyid` **(Many-Argument Workhorses)** (Impact: 99.3)
  * `MCCard::relayer` **(Many-Argument Workhorses)** (Impact: 94.7)
  * `MCCard::mdown` **(Compute Cores)** (Impact: 93.1)
  * `MCCard::getchildbyordinal` **(Many-Argument Workhorses)** (Impact: 70.7)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3112.74 | **LOC:** 4865 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 94.2652% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCObject::DoGetProperties` **(Many-Argument Workhorses)** (Impact: 94.7)
  * `MCInterfaceTextStyleFormat` **(Many-Argument Workhorses)** (Impact: 68.3)
  * `MCInterfaceTextStyleParse` **(Many-Argument Workhorses)** (Impact: 64.9)
    * *Intent:* //////////
  * `MCObject::GetRevAvailableVariables` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `MCObject::SetParentScript` **(Many-Argument Workhorses)** (Impact: 56.4)
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
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3106.06 | **LOC:** 3119 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.239; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.2%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hexfour` **(Many-Argument Workhorses)** (Impact: 228.0)
    * *Intent:* /* * Find a perfect hash when there are only four keys. Max 10 instructions. * Note that a perfect h...
  * `initalen` **(Many-Argument Workhorses)** (Impact: 146.0)
    * *Intent:* /* guess initial values for alen and blen */
  * `hexn` **(Many-Argument Workhorses)** (Impact: 127.8)
    * *Intent:* * * The code will probably look like this, minus some stuff: * val += CONSTANT; * val ^= (val<<16); ...
  * `hexthree` **(Many-Argument Workhorses)** (Impact: 103.2)
    * *Intent:* /* * Find a perfect hash when there are only three keys. Max 6 instructions. * * keys a,b,c. * There...
  * `findhash` **(Many-Argument Workhorses)** (Impact: 76.3)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3053.58 | **LOC:** 2769 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Guard Balance (formerly Safety Score) (87.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 78.8136% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCFilesExecPerformReadFixedFor` **(Many-Argument Workhorses)** (Impact: 411.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCFilesExecPerformReadCodeUnit` **(Many-Argument Workhorses)** (Impact: 188.1)
    * *Intent:* // Reads from the stream a codeunit and put it back in the end of the mutable buffer x_buffer // For...
  * `MCFilesExecWriteToStream` **(Many-Argument Workhorses)** (Impact: 165.1)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCFilesExecPerformReadBinaryUntil` **(Many-Argument Workhorses)** (Impact: 148.2)
  * `MCFilesExecPerformReadTextUntil` **(Many-Argument Workhorses)** (Impact: 127.5)
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
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2932.78 | **LOC:** 3294 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (92.2%), Complexity Load (formerly Cognitive Load) (91.5%)
- **Documentation Coverage:** 92.2414% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCStack::openrect` **(Many-Argument Workhorses)** (Impact: 475.8)
  * `MCStack::getchild` **(Many-Argument Workhorses)** (Impact: 149.2)
  * `MCStack::getbackground` **(Many-Argument Workhorses)** (Impact: 120.2)
  * `MCStack::count` **(Many-Argument Workhorses)** (Impact: 86.7)
  * `MCStack::getAV` **(Many-Argument Workhorses)** (Impact: 83.8)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2922.24 | **LOC:** 3139 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Guard Balance (formerly Safety Score) (93.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.9362% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCGroup::load` **(Many-Argument Workhorses)** (Impact: 138.3)
  * `MCGroup::getchild` **(Many-Argument Workhorses)** (Impact: 107.5)
  * `MCGroup::draw` **(Many-Argument Workhorses)** (Impact: 104.7)
    * *Intent:* //----------------------------------------------------------------------------- // Redraw Management...
  * `MCGroup::mfocus_control` **(Many-Argument Workhorses)** (Impact: 75.0)
  * `MCGroup::save` **(Many-Argument Workhorses)** (Impact: 71.8)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2920.58 | **LOC:** 2528 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **54**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.3%), Debt Markers (formerly Tech Debt) (91.5%), Guard Balance (formerly Safety Score) (91.3%)
- **Documentation Coverage:** 94.0299% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCSocket::readsome` **(I/O & Config Routines)** (Impact: 327.8)
    * *Intent:* #endif
  * `MCSocket::write` **(Many-Argument Workhorses)** (Impact: 305.9)
  * `MCSocket::read` **(Many-Argument Workhorses)** (Impact: 254.4)
  * `MCSocket::writesome` **(Compute Cores)** (Impact: 246.4)
  * `MCS_accept` **(Many-Argument Workhorses)** (Impact: 104.8)
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

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libfoundation/include/foundation-auto.h` -> **Severity: 0.022** (Bridge: 0.0003 * Flux: 74.2407%)
- `engine/src/globals.h` -> **Severity: 0.017** (Bridge: 0.002 * Flux: 8.6841%)
- `engine/src/parsedef.h` -> **Severity: 0.008** (Bridge: 0.0009 * Flux: 8.7715%)
- `gyp/pylib/gyp/generator/msvs.py` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)
- `gyp/pylib/gyp/MSVSUserFile.py` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `engine/src/globals.h` -> **Severity: 10.094** (Embedded: 0.165 * Error Risk: 61.1603%)
- `engine/src/mcutility.h` -> **Severity: 9.1** (Embedded: 0.1121 * Error Risk: 81.173%)
- `engine/src/foundation-legacy.h` -> **Severity: 8.278** (Embedded: 0.0898 * Error Risk: 92.1492%)
- `engine/src/parsedef.h` -> **Severity: 8.216** (Embedded: 0.1638 * Error Risk: 50.144%)
- `engine/src/objdefs.h` -> **Severity: 8.14** (Embedded: 0.1592 * Error Risk: 51.1448%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libfoundation/include/foundation-span.h` -> **Severity: 2256.7** (Blast Radius: 22.567 * Doc Risk: 100.0%)
- `tests/lcb/compiler/iterator.lcb` -> **Severity: 1950.4** (Blast Radius: 19.504 * Doc Risk: 100.0%)
- `libfoundation/include/foundation-auto.h` -> **Severity: 1887.968** (Blast Radius: 25.796 * Doc Risk: 73.1884%)
- `engine/src/object.h` -> **Severity: 1765.39** (Blast Radius: 17.858 * Doc Risk: 98.8571%)
- `engine/src/objdefs.h` -> **Severity: 1239.7** (Blast Radius: 12.397 * Doc Risk: 100.0%)

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
