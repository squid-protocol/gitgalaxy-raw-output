# ARCHITECTURAL_BRIEF: livecode
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/livecode/livecode.git` |
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
- **Scope:** 1202 analyzed artifact(s), 211323 LOC.
- **Load-bearing artifact:** `tests/_testlib.livecodescript` -- 185 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `libgraphics/src/context.cpp` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ide-support/revliburl.livecodescript` at magnitude 5996.72 (structural weight, not risk).
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
| Total Artifacts | 7644 |
| Analyzed Artifacts (Scanned) | 1202 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6442 |
| Total LOC | 211323 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 15.7% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2695 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8717 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 60 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| LIVECODE | 415 | 68424 | 34.5% |
| CPP | 324 | 102403 | 27.0% |
| MARKDOWN | 198 | 0 | 16.5% |
| PYTHON | 85 | 14297 | 7.1% |
| XML | 38 | 0 | 3.2% |
| PLAINTEXT | 30 | 0 | 2.5% |
| OBJECTIVE-C | 28 | 13344 | 2.3% |
| PERL | 26 | 1059 | 2.2% |
| C | 23 | 9057 | 1.9% |
| SHELL | 21 | 850 | 1.7% |
| MAKEFILE | 4 | 353 | 0.3% |
| BATCH | 4 | 119 | 0.3% |
| HTML | 3 | 1000 | 0.2% |
| JAVA | 2 | 325 | 0.2% |
| YAML | 1 | 92 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1030 |
| utf-8 | bom | 172 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 27%, Declarative / Non-Code 17%, Large Core Modules (3) 16%, Large Core Modules 11%, Interface Declarations Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 974 | 81.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 228 | 19.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6442*

**Composition by Extension & Reason:**
- `.lcdoc`: 2630x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1669x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 468x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 337x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 322x Excluded (Unsupported Extension: '.test')
- `.h`: 270x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 127x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 68x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 8x Excluded (Unsupported Extension: '.compilertest')
- `.java`: 77x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mm`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lcb`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 47 exceeds 500 chars), 2x Excluded (Saturation: Line 49 exceeds 500 chars)
- `.diff`: 20x Excluded (Unsupported Extension: '.diff')
- `.strings`: 18x Excluded (Unsupported Extension: '.strings')
- `.b`: 18x Unsupported Format (.b)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.0 | 23.7 | 9.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 44.1 | 55.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 84.3 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 68.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4161 | 267 | 5 | `revmobile/src/CoreSimulator.h` |
| cleanup | 612 | 137 | 1 | `lcidlc/src/Support.mm` |
| guards | 8193 | 514 | 16 | `extensions/script-libraries/drawing/drawing.livecodescript` |
| danger | 3707 | 351 | 7 | `revmobile/src/CoreSimulator.h` |
| concurrency | 393 | 105 | 0 | `ide-support/revsaveasstandalone.livecodescript` |
| connectivity | 4553 | 449 | 9 | `revmobile/src/CoreSimulator.h` |
| io | 632 | 129 | 1 | `lcidlc/lclink.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 344 | 73 | 0 | `tests/lcs/core/network/network.livecodescript` |
| time | 67 | 27 | 0 | `ide-support/revliburl.livecodescript` |
| serialization | 21 | 9 | 0 | `extensions/libraries/json/json.lcb` |
| regex | 193 | 52 | 0 | `ide-support/revdocsparser.livecodescript` |
| events | 1738 | 324 | 4 | `ide-support/revliburl.livecodescript` |
| tests | 379 | 35 | 0 | `libfoundation/test/test_typeconvert.cpp` |
| docs | 2706 | 280 | 7 | `revdb/src/revdb.cpp` |
| debt | 1751 | 289 | 3 | `toolchain/lc-compile/src/syntax-gen.c` |
| mutation | 48331 | 665 | 109 | `libfoundation/src/foundation-string.cpp` |
| dead_code | 5731 | 612 | 13 | `lcidlc/src/Support.mm` |
| credential | 82 | 10 | 0 | `prebuilt/libcef.gyp` |
| threat | 2 | 1 | 0 | `libfoundation/test/test_hash.cpp` |
| ml_ai | 511 | 84 | 0 | `tests/lcs/core/math/math.livecodescript` |
| ui | 3336 | 224 | 5 | `tests/lcs/core/interface/interface.livecodescript` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lcidlc/lclink.sh` (Hits: 42)
- `config.py` (Hits: 38)
- `tests/lcs/core/network/network.livecodescript` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_testlib.livecodescript** (`tests/_testlib.livecodescript`) — 185 inbound connections
2. **foundation.h** (`libfoundation/include/foundation.h`) — 101 inbound connections
3. **foundation-auto.h** (`libfoundation/include/foundation-auto.h`) — 82 inbound connections
4. **foundation-string.cpp** (`libfoundation/src/foundation-string.cpp`) — 80 inbound connections
5. **test_new.cpp** (`engine/test/test_new.cpp`) — 61 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **context.cpp** (`libgraphics/src/context.cpp`) — 18 outbound dependencies
2. **revzip.cpp** (`revzip/src/revzip.cpp`) — 15 outbound dependencies
3. **emit.cpp** (`toolchain/lc-compile/src/emit.cpp`) — 15 outbound dependencies
4. **harfbuzztext.cpp** (`libgraphics/src/harfbuzztext.cpp`) — 14 outbound dependencies
5. **revandroid.cpp** (`revmobile/src/revandroid.cpp`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `revSaveAsMobileStandaloneMain` **(Many-Argument Workhorses)** (@ `ide-support/revsaveasandroidstandalone.livecodescript`) -> Impact: **715.2** | LOC: 1021
- `LCValueArrayFromObjcDictionary` **(Many-Argument Workhorses)** (@ `lcidlc/src/Support.mm`) -> Impact: **650.3** | LOC: 2059
- `REVVideoGrabber` **(Many-Argument Workhorses)** (@ `revvideograbber/src/revvideograbber.cpp`) -> Impact: **472.7** | LOC: 564
- `JsonImport` **(Many-Argument Workhorses)** (@ `extensions/libraries/json/json.lcb`) -> Impact: **449.1** | LOC: 484
  * *Intent:* */
- `revSaveAsMobileStandaloneMain` **(Many-Argument Workhorses)** (@ `ide-support/revsaveasiosstandalone.livecodescript`) -> Impact: **415.1** | LOC: 745
- `compilerParse` **(Many-Argument Workhorses)** (@ `builder/package_compiler.livecodescript`) -> Impact: **322.6** | LOC: 425
  * *Intent:* ################################################################################ -- Parsing builds a tree of components, and flattens compound command...
- `MCGDrawingContext::Execute` **(Many-Argument Workhorses)** (@ `libgraphics/src/drawing.cpp`) -> Impact: **237.7** | LOC: 394
  * *Intent:* /* The (template based) implementation of the Execute method. */
- `revDocsExtractDocBlocks` **(Many-Argument Workhorses)** (@ `ide-support/revdocsparser.livecodescript`) -> Impact: **236.4** | LOC: 301
  * *Intent:* */
- `hexfour` **(Many-Argument Workhorses)** (@ `util/perfect/perfect.c`) -> Impact: **228.0** | LOC: 541
  * *Intent:* /* * Find a perfect hash when there are only four keys. Max 10 instructions. * Note that a perfect hash for 4 keys will automatically be minimal. */
- `MCStringFormatV` **(Many-Argument Workhorses)** (@ `libfoundation/src/foundation-string.cpp`) -> Impact: **227.2** | LOC: 384
  * *Intent:* ////////////////////////////////////////////////////////////////////////////////

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `libfoundation/src` | 60 | 24670.02 | 37.14% | 62.43% |
| `ide-support` | 11 | 22412.3 | 85.3% | 64.17% |
| `libgraphics/src` | 21 | 9580.22 | 44.31% | 65.49% |
| `lcidlc/src` | 24 | 8847.26 | 25.66% | 35.86% |
| `libscript/src` | 72 | 8710.6 | 13.57% | 49.04% |
| `libbrowser/src` | 27 | 8033.11 | 23.65% | 42.7% |
| `builder` | 16 | 7592.44 | 54.68% | 33.38% |
| `revdb/src` | 36 | 7257.58 | 36.75% | 39.26% |
| `revbrowser/src` | 18 | 6340.94 | 27.15% | 44.06% |
| `revvideograbber/src` | 17 | 6298.6 | 37.13% | 32.49% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `revmobile/src/CoreSimulator.h` -> **100.0%** Exposure
- `revmobile/src/DVTiPhoneSimulatorRemoteClient.h` -> **100.0%** Exposure
- `revmobile/src/iPhoneSimulatorRemoteClient.h` -> **100.0%** Exposure
- `Makefile` -> **100.0%** Exposure
- `builder/installer/uninstalleruistackbehavior.livecodescript` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `config.py` -> **100.0%** Exposure
- `fetch.py` -> **100.0%** Exposure
- `prebuilt/archive.py` -> **100.0%** Exposure
- `prebuilt/build.py` -> **100.0%** Exposure
- `prebuilt/package.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lcidlc/src/Support.mm` -> **115** Orphaned Functions | **0** Duplicates
- `revbrowser/src/w32browser.cpp` -> **102** Orphaned Functions | **0** Duplicates
- `revbrowser/src/cefbrowser.cpp` -> **93** Orphaned Functions | **0** Duplicates
- `libfoundation/src/foundation-string.cpp` -> **88** Orphaned Functions | **0** Duplicates
- `libgraphics/src/context.cpp` -> **83** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `23` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1713` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ide-support/revliburl.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.565)
- **Top Global Matches:** file_cluster_6: 5.565, file_cluster_4: 9.879, file_cluster_8: 15.232
- **Magnitude:** 5996.72 | **LOC:** 5369 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); blast radius 3.617; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `high_risk_execution: 30`, `state_mutation: 1152`, `dead_code: 7`, `fragile_debt: 17`, `unreferenced_by_name: 55`
* *Architecture:* `io: 33`, `api: 137`, `concurrency: 17`
* *Defense:* `safety: 27`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.617
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.005166
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `libfoundation/src/foundation-string.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.778)
- **Top Global Matches:** file_cluster_4: 6.778, file_cluster_15: 10.546, file_cluster_16: 11.397
- **Magnitude:** 5461.86 | **LOC:** 7360 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **80** in-repo importer(s); it depends on **12**; blast radius 15.511; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 85.8407% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCStringFormatV` **(Many-Argument Workhorses)** (Impact: 227.2)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringCreateWithBytes` **(Many-Argument Workhorses)** (Impact: 89.4)
    * *Intent:* // Create an immutable string from the given bytes, interpreting them using // the specified encodin...
  * `MCStringSplit` **(Many-Argument Workhorses)** (Impact: 84.7)
  * `MCStringConvertToBytes` **(Many-Argument Workhorses)** (Impact: 80.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringDelimitedOffset` **(Many-Argument Workhorses)** (Impact: 71.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 674 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1160`, `structural_boundaries: 651`, `args: 285`, `func_start: 226`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 755`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 34`, `unreferenced_by_name: 88`
* *Architecture:* `import: 12`
* *Defense:* `doc: 35`, `immutability_locks: 118`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.511
  * `Choke Point (Betweenness):` 0.00165 | `Ripple Effect (Closeness):` 0.072722
  * `Imports (Out-Degree: 17):` Windows.h, errno.h, foundation-auto.h, foundation-bidi.h, foundation-chunk.h, foundation-private.h, foundation-string-native.cpp.h, foundation-unicode.h...
  * `Imported By (In-Degree: 80):` (Excluded from Brief to save tokens)

### `lcidlc/src/Support.mm` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.32)
- **Top Global Matches:** file_cluster_4: 10.32, file_cluster_12: 10.495, file_cluster_15: 12.246
- **Magnitude:** 4229.36 | **LOC:** 4484 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.824; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.4%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 89.9038% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LCValueArrayFromObjcDictionary` **(Many-Argument Workhorses)** (Impact: 650.3)
  * `LCValueFetch` **(Many-Argument Workhorses)** (Impact: 136.7)
  * `LCValueStore` **(Many-Argument Workhorses)** (Impact: 87.0)
  * `LCArrayLookupKeyOnPath` **(Many-Argument Workhorses)** (Impact: 73.9)
  * `LCArrayListKeysOnPath` **(Many-Argument Workhorses)** (Impact: 70.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 559 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 1725
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 422`, `args: 215`, `func_start: 215`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 607`, `planned_debt: 1`, `fragile_debt: 23`, `unreferenced_by_name: 115`
* *Architecture:* `io: 9`, `api: 3`, `import: 12`
* *Defense:* `doc: 36`, `immutability_locks: 122`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.824
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.001658
  * `Imports (Out-Degree: 2):` Foundation.h, LiveCode.h, UIKit.h, log.h, jni.h, pthread.h, stdarg.h, stdint.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ide-support/revdocsparser.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.836)
- **Top Global Matches:** file_cluster_4: 5.836, file_cluster_6: 8.376, file_cluster_16: 12.99
- **Magnitude:** 3500.1 | **LOC:** 2938 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.634; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.3%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `state_mutation: 697`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 71`
* *Defense:* `safety: 2`, `doc: 9`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.634
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000829
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `revxml/src/revxml.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.322)
- **Top Global Matches:** file_cluster_6: 6.322, file_cluster_4: 8.949, file_cluster_9: 16.465
- **Magnitude:** 3282.94 | **LOC:** 3136 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 1.605; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.9%), Complexity Load (formerly Cognitive Load) (70.7%), Debt Markers (formerly Tech Debt) (59.5%)
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
* *Structure:* `branch: 591`, `structural_boundaries: 124`, `args: 98`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `state_mutation: 545`, `planned_debt: 9`, `fragile_debt: 17`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`, `api: 1`, `import: 12`
* *Defense:* `safety: 3`, `doc: 12`, `immutability_locks: 18`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.605
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.001658
  * `Imports (Out-Degree: 7):` cmath, cstdio, cstdlib, ctime, cxml.h, xpath.h, transform.h, xsltutils.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ide-support/revsblibrary.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.157)
- **Top Global Matches:** file_cluster_4: 5.157, file_cluster_16: 10.56, file_cluster_6: 10.929
- **Magnitude:** 3255.42 | **LOC:** 3194 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); blast radius 7.791; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.4%), Guard Balance (formerly Safety Score) (72.5%)
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
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 478`, `fragile_debt: 14`
* *Architecture:* `io: 17`, `api: 88`, `concurrency: 4`
* *Defense:* `safety: 37`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 31`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.791
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014109
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `util/perfect/perfect.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.223)
- **Top Global Matches:** file_cluster_8: 10.223, file_cluster_6: 15.315, file_cluster_4: 23.285
- **Magnitude:** 3067.36 | **LOC:** 3119 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.445; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%)
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
* *Amplified Cascading Flux:* 497 instances
* *High Risk Execution (weighted view):* 11
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1577
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 194`, `args: 7`, `func_start: 38`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 144`, `high_risk_execution: 18`, `state_mutation: 583`, `dead_code: 29`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 36`, `import: 5`
* *Defense:* `safety: 15`, `doc: 11`, `immutability_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stddef.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revsaveasstandalone.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.931)
- **Top Global Matches:** file_cluster_6: 6.931, file_cluster_8: 10.63, file_cluster_4: 14.597
- **Magnitude:** 2799.62 | **LOC:** 2675 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 1.592; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.5%), Complexity Load (formerly Cognitive Load) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revSaveAsWindowsStandalone` **(Many-Argument Workhorses)** (Impact: 145.6)
  * `revCopyExternals` **(Many-Argument Workhorses)** (Impact: 112.5)
  * `revDoSaveAsStandalone` **(Many-Argument Workhorses)** (Impact: 102.2)
  * `revCopyResources` **(Many-Argument Workhorses)** (Impact: 100.8)
    * *Intent:* ##################################################################### # Copies general resources to ...
  * `revCopyDatabaseDrivers` **(Many-Argument Workhorses)** (Impact: 89.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 364 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 1186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 886`, `args: 57`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 8`, `state_mutation: 458`, `dead_code: 5`, `fragile_debt: 42`, `unreferenced_by_name: 6`
* *Architecture:* `io: 6`, `api: 14`, `concurrency: 7`, `import: 1`
* *Defense:* `safety: 61`, `sync_locks: 20`, `immutability_locks: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.592
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005839
  * `Imports (Out-Degree: 1):` pStack
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `extensions/script-libraries/drawing/drawing.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.575)
- **Top Global Matches:** file_cluster_4: 5.575, file_cluster_16: 9.555, file_cluster_6: 11.137
- **Magnitude:** 2745.58 | **LOC:** 3358 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_svgParseFeatureValue` **(Many-Argument Workhorses)** (Impact: 125.1)
    * *Intent:* /******************************************************************************* * * SVG VALUE PARSI...
  * `_svgCompilePaintServer` **(Many-Argument Workhorses)** (Impact: 81.4)
  * `svgSpecLoad` **(I/O & Config Routines)** (Impact: 80.0)
    * *Intent:* /* svgSpecLoad loads and parses a description of attributes, and the node types * they apply to. */
  * `_svgEncode` **(Many-Argument Workhorses)** (Impact: 71.8)
  * `_svgEncodePath` **(Many-Argument Workhorses)** (Impact: 56.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 365 instances
* *State Mutation (weighted view):* 1200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 671`, `structural_boundaries: 929`, `args: 133`, `func_start: 139`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 470`, `planned_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 4`
* *Defense:* `safety: 32`, `doc: 3`, `sync_locks: 2`, `immutability_locks: 56`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revsaveasandroidstandalone.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.89)
- **Top Global Matches:** file_cluster_4: 5.89, file_cluster_16: 10.258, file_cluster_15: 11.382
- **Magnitude:** 2365.58 | **LOC:** 2184 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 97.0149% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revSaveAsMobileStandaloneMain` **(Many-Argument Workhorses)** (Impact: 715.2)
  * `ConvertArrayDimensionToXML` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `addAssetsToArchive` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `mapFilePath` **(Compute Cores)** (Impact: 46.6)
    * *Intent:* ################################################################################ -- MW-2013-06-13: [...
  * `ConvertXMLNodeToArray` **(Many-Argument Workhorses)** (Impact: 35.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 288 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 941
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 558`, `structural_boundaries: 814`, `args: 51`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 365`, `dead_code: 15`, `fragile_debt: 13`, `unreferenced_by_name: 4`
* *Architecture:* `io: 17`, `api: 10`, `concurrency: 16`
* *Defense:* `safety: 45`, `doc: 2`, `sync_locks: 1`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `revdb/src/revdb.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.749)
- **Top Global Matches:** file_cluster_4: 6.749, file_cluster_9: 8.881, file_cluster_15: 9.647
- **Magnitude:** 2310.92 | **LOC:** 2355 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Complexity Load (formerly Cognitive Load) (34.5%), Debt Markers (formerly Tech Debt) (19.0%)
- **Documentation Coverage:** 73.0159% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `REVDB_Connect` **(Many-Argument Workhorses)** (Impact: 67.7)
    * *Intent:* /// @param username The username to log into the database with. /// @param password The password to ...
  * `BindVariables` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* //extract arguments from variable list or array
  * `REVDB_QueryList` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `REVDB_ColumnNames` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* /// @brief Lists the number of columns in a table or recordset /// @param pCursorOrConnectionId This...
  * `GetColumnByNumber` **(Many-Argument Workhorses)** (Impact: 34.2)
    * *Intent:* //utility function to get column data by number
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 439 instances
* *Memory Alloc (weighted view):* 48
* *State Mutation (weighted view):* 1342
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 135`, `args: 100`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 464`, `fragile_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 13`
* *Defense:* `doc: 129`, `immutability_locks: 19`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` dbdriver.h, dbdrivercommon.h, iossupport.h, large_buffer.h, math.h, osxsupport.h, external.h, support.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ide-support/revsaveasiosstandalone.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.724)
- **Top Global Matches:** file_cluster_8: 8.724, file_cluster_6: 8.982, file_cluster_4: 17.112
- **Magnitude:** 2207.8 | **LOC:** 2136 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Debt Markers (formerly Tech Debt) (90.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revSaveAsMobileStandaloneMain` **(Many-Argument Workhorses)** (Impact: 415.1)
  * `revCreateMobilePlist` **(Many-Argument Workhorses)** (Impact: 218.0)
  * `revCopyMobileFiles` **(Many-Argument Workhorses)** (Impact: 167.9)
    * *Intent:* -- The files list from the standalone builder contains relative and absolute references. -- -- Relat...
  * `revDecorateImageAssets` **(Many-Argument Workhorses)** (Impact: 85.0)
    * *Intent:* ################################################################################
  * `mapFilePath` **(Compute Cores)** (Impact: 49.8)
    * *Intent:* ################################################################################ -- MW-2013-06-13: [...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 280 instances
* *High Risk Execution (weighted view):* 17
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 957
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 456`, `structural_boundaries: 790`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 22`, `state_mutation: 397`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 29`, `unreferenced_by_name: 3`
* *Architecture:* `io: 18`, `api: 4`, `concurrency: 2`
* *Defense:* `safety: 31`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `builder/package_compiler.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.69)
- **Top Global Matches:** file_cluster_4: 5.69, file_cluster_16: 10.468, file_cluster_6: 10.937
- **Magnitude:** 2174.56 | **LOC:** 1836 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.634; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.7%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compilerParse` **(Many-Argument Workhorses)** (Impact: 322.6)
    * *Intent:* ################################################################################ -- Parsing builds a...
  * `compilerExecuteCopy` **(Many-Argument Workhorses)** (Impact: 137.8)
  * `packageCompilerBuild` **(Many-Argument Workhorses)** (Impact: 85.5)
    * *Intent:* -- Build the given installer component
  * `compilerExecute` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `createManifest` **(Stateful Encapsulated Methods)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 315 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1016
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 697`, `args: 62`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 386`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `io: 5`, `api: 11`, `concurrency: 2`
* *Defense:* `safety: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.634
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000829
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `revvideograbber/src/dsvideograbber.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.969)
- **Top Global Matches:** file_cluster_4: 6.969, file_cluster_12: 10.432, file_cluster_6: 11.609
- **Magnitude:** 1996.86 | **LOC:** 3085 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.628; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CDirectXVideoGrabber::GetStreamConfigbyColorSpaceSet` **(Many-Argument Workhorses)** (Impact: 98.3)
    * *Intent:* //! GetStreamConfigbyColorSpaceSet: use the user set color space to make a stream config to be used ...
  * `CDirectXVideoGrabber::InitCaptureGraph` **(Compute Cores)** (Impact: 67.3)
    * *Intent:* //! InitCaptureGraph: Initial a filter graph For AVI capture use
  * `CDirectXVideoGrabber::InitStillGraph` **(I/O & Config Routines)** (Impact: 51.0)
    * *Intent:* //!InitStillGraph, Initial a filter graph for Snapshot and video preview
  * `CDirectXVideoGrabber::GetFormatInfo` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `CDirectXVideoGrabber::GetCurrentCodecFilter` **(Compute Cores)** (Impact: 44.7)
    * *Intent:* //! GetCurrentCodecFilter: get current select codec filter
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 339 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 235`, `args: 217`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 432`, `dead_code: 10`, `fragile_debt: 1`, `unreferenced_by_name: 59`
* *Architecture:* `import: 6`
* *Defense:* `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.628
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.002709
  * `Imports (Out-Degree: 7):` ficommon.h, fiint.h, Vfw.h, core.h, dsvideograbber.h, external.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `revzip/src/revzip.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.936)
- **Top Global Matches:** file_cluster_6: 5.936, file_cluster_8: 12.21, file_cluster_4: 12.895
- **Magnitude:** 1855.44 | **LOC:** 1544 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Complexity Load (formerly Cognitive Load) (70.9%), Debt Markers (formerly Tech Debt) (38.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revZipDescribeItem` **(Many-Argument Workhorses)** (Impact: 91.0)
  * `revZipExtractItemToVariable` **(Many-Argument Workhorses)** (Impact: 78.4)
  * `revZipExtractItemToFile` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `revZipEnumerateItems` **(Many-Argument Workhorses)** (Impact: 54.2)
  * `revZipAddItemWithDataAndCompression` **(Many-Argument Workhorses)** (Impact: 43.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 351 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1055
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 67`, `args: 29`, `func_start: 26`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 353`, `dead_code: 5`, `fragile_debt: 11`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `import: 16`
* *Defense:* `immutability_locks: 5`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` CoreServices.h, cstdlib, cstring, errno.h, fcntl.h, iostream, list, map...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `revbrowser/src/revbrowser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.637)
- **Top Global Matches:** file_cluster_15: 6.637, file_cluster_4: 7.398, file_cluster_16: 8.321
- **Magnitude:** 1705.06 | **LOC:** 1970 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **7**; blast radius 1.236; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.1%), Complexity Load (formerly Cognitive Load) (86.1%), Guard Balance (formerly Safety Score) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revBrowserGetProp` **(Many-Argument Workhorses)** (Impact: 150.6)
    * *Intent:* // Description: // - "busy" : Returns true if the browser is in the middle of an operation // - "rec...
  * `revBrowserSetProp` **(Many-Argument Workhorses)** (Impact: 128.3)
  * `revBrowserCreateCallbackScript` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `BrowserInstances::Callback` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `XBrowserGetProp` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* // Returns the version of the browser external. // // Property: // XBrowser_Get("htmltext", [ pInsta...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 253 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 133`, `args: 99`, `func_start: 70`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 285`, `fragile_debt: 8`, `unreferenced_by_name: 27`
* *Architecture:* `io: 4`, `api: 3`, `import: 7`
* *Defense:* `doc: 7`, `immutability_locks: 37`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.236
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.008952
  * `Imports (Out-Degree: 5):` cmath, core.h, cstdio, cstdlib, cstring, revbrowser.h, external.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `libfoundation/src/foundation-unicode.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.513)
- **Top Global Matches:** file_cluster_4: 5.513, file_cluster_12: 9.935, file_cluster_15: 9.989
- **Magnitude:** 1672.8 | **LOC:** 2463 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **13**; blast radius 3.383; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%)
- **Documentation Coverage:** 82.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCUnicodeWildcardMatch` **(Many-Argument Workhorses)** (Impact: 167.8)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCUnicodeGetProperty` **(Many-Argument Workhorses)** (Impact: 97.5)
  * `MCUnicodeCanBreakWordBetween` **(Many-Argument Workhorses)** (Impact: 94.6)
    * *Intent:* // a__b being selected as a single word.
  * `MCUnicodeGetStringProperty` **(Many-Argument Workhorses)** (Impact: 43.7)
  * `MCUnicodeFirstIndexOf` **(Many-Argument Workhorses)** (Impact: 42.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 564
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 209`, `args: 94`, `func_start: 75`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 198`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 56`
* *Architecture:* `import: 13`
* *Defense:* `doc: 15`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.383
  * `Choke Point (Betweenness):` 0.000321 | `Ripple Effect (Closeness):` 0.052427
  * `Imports (Out-Degree: 9):` foundation-auto.h, foundation-string-hash.h, foundation-text.h, foundation-unicode-private.h, foundation-unicode.h, limits, brkiter.h, coll.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `libgraphics/src/context.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.121)
- **Top Global Matches:** file_cluster_15: 6.121, file_cluster_16: 8.248, file_cluster_4: 8.774
- **Magnitude:** 1605.82 | **LOC:** 2543 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **18**; blast radius 1.208; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%)
- **Documentation Coverage:** 86.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCGContextRenderEffect` **(Many-Argument Workhorses)** (Impact: 125.1)
  * `MCGContextDrawSkBitmap` **(Many-Argument Workhorses)** (Impact: 74.2)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCGContextMeasurePlatformText` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* // The transform is used when we are measuring text with the intention of drawing it scaled. The wid...
  * `MCGContextRenderEffects` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `MCGContextBeginWithEffects` **(Many-Argument Workhorses)** (Impact: 26.0)
    * *Intent:* // The 'shape' parameter is the rectangle in user-space of the area to which the effect // is to be ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 632
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 237`, `args: 175`, `func_start: 130`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 230`, `dead_code: 14`, `planned_debt: 2`, `fragile_debt: 20`, `unreferenced_by_name: 83`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 3`, `doc: 21`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.208
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.007463
  * `Imports (Out-Degree: 10):` SkBitmap.h, SkBlurImageFilter.h, SkBlurMaskFilter.h, SkCanvas.h, SkColorFilter.h, SkColorPriv.h, SkDevice.h, SkImageFilter.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `extensions/script-libraries/extension-utils/extension-utils.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.333)
- **Top Global Matches:** file_cluster_6: 5.333, file_cluster_4: 8.756, file_cluster_8: 16.026
- **Magnitude:** 1554.66 | **LOC:** 1830 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.634; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%), Guard Balance (formerly Safety Score) (74.8%)
- **Documentation Coverage:** 92.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__extensionAddFilesToPackage` **(Compute Cores)** (Impact: 61.1)
  * `extensionValidateLCEPackage` **(Compute Cores)** (Impact: 49.1)
    * *Intent:* */
  * `extensionFetchFolderDetails` **(Defensive Guards)** (Impact: 48.8)
    * *Intent:* */
  * `extensionIsBuiltin` **(Stateful Encapsulated Methods)** (Impact: 47.1)
  * `__extensionBuildPackage` **(Many-Argument Workhorses)** (Impact: 43.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 226 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 708
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 535`, `args: 47`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 256`, `fragile_debt: 4`, `unreferenced_by_name: 7`
* *Architecture:* `io: 2`, `api: 21`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 23`, `doc: 4`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.634
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000829
  * `Imports (Out-Degree: 0):` it, pDocsParser
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `libbrowser/src/libbrowser_cef.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.881)
- **Top Global Matches:** file_cluster_4: 6.881, file_cluster_15: 7.533, file_cluster_12: 8.089
- **Magnitude:** 1514.92 | **LOC:** 2253 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.492; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 90.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCCefDictionaryToBrowserDictionary` **(Many-Argument Workhorses)** (Impact: 52.5)
  * `MCCefListToBrowserList` **(Many-Argument Workhorses)** (Impact: 44.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCCefMenuFilterItems` **(Compute Cores)** (Impact: 44.8)
  * `OnProcessMessageReceived` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `OnLoadEnd` **(Many-Argument Workhorses)** (Impact: 26.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 208 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 667
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 268`, `args: 129`, `func_start: 125`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 251`, `planned_debt: 8`, `fragile_debt: 24`, `unreferenced_by_name: 78`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `doc: 19`, `immutability_locks: 57`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.492
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000829
  * `Imports (Out-Degree: 8):` core.h, cef_app.h, cef_parser.h, cef_scoped_temp_dir.h, libbrowser_cef.h, list, set, signal_restore_posix.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `libfoundation/src/foundation-pickle.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.537)
- **Top Global Matches:** file_cluster_8: 13.537, file_cluster_3: 14.179, file_cluster_6: 25.218
- **Magnitude:** 1464.72 | **LOC:** 1009 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.475; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.5%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 82.3529% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MCPickleReadField` **(Many-Argument Workhorses)** (Impact: 175.1)
  * `MCPickleWriteField` **(Many-Argument Workhorses)** (Impact: 142.4)
  * `MCPickleReadValueRef` **(Many-Argument Workhorses)** (Impact: 137.1)
  * `MCPickleWriteValueRef` **(Many-Argument Workhorses)** (Impact: 117.3)
  * `MCPickleReadTypeInfoRefContents` **(Many-Argument Workhorses)** (Impact: 102.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 182 instances
* *State Mutation (weighted view):* 554
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 92`, `args: 20`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 190`, `planned_debt: 9`
* *Architecture:* `import: 3`
* *Defense:* `doc: 5`, `sync_locks: 1`, `immutability_locks: 7`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.475
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005209
  * `Imports (Out-Degree: 12):` foundation-auto.h, foundation-private.h, foundation.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `extensions/script-libraries/dropbox/dropbox.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.087)
- **Top Global Matches:** file_cluster_16: 5.087, file_cluster_15: 7.296, file_cluster_11: 8.38
- **Magnitude:** 1453.38 | **LOC:** 5756 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__share_folder_POST` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `__list_shared_links_POST` **(Stateful Encapsulated Methods)** (Impact: 23.4)
  * `__modify_shared_link_settings_POST` **(Stateful Encapsulated Methods)** (Impact: 21.9)
  * `__API` **(Stateful Encapsulated Methods)** (Impact: 19.7)
  * `__update_folder_policy_POST` **(Stateful Encapsulated Methods)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 136 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 606`, `args: 160`, `func_start: 221`, `class_start: 1`
* *Risk/State:* `state_mutation: 210`, `unreferenced_by_name: 52`
* *Architecture:* `io: 1`, `api: 52`, `concurrency: 1`
* *Defense:* `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolchain/lc-compile/src/syntax-gen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.25)
- **Top Global Matches:** file_cluster_4: 5.25, file_cluster_16: 8.835, file_cluster_15: 9.07
- **Magnitude:** 1440.64 | **LOC:** 1932 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.1%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.2406% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GenerateSyntaxRule` **(Many-Argument Workhorses)** (Impact: 93.2)
  * `IsSyntaxNodeEqualTo` **(Many-Argument Workhorses)** (Impact: 87.0)
  * `GenerateSyntaxRuleTerm` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `PrintSyntaxNode` **(Compute Cores)** (Impact: 33.7)
  * `ListSyntaxNodeUnreservedKeywords` **(Stateful Encapsulated Methods)** (Impact: 31.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 163 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 519
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 251`, `args: 112`, `func_start: 84`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 193`, `planned_debt: 1`, `unreferenced_by_name: 45`
* *Architecture:* `api: 59`, `import: 9`
* *Defense:* `safety: 30`, `doc: 5`, `immutability_locks: 24`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` allocate.h, assert.h, literal.h, outputfile.h, position.h, report.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `revbrowser/src/w32browser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.442)
- **Top Global Matches:** file_cluster_12: 7.442, file_cluster_4: 7.879, file_cluster_15: 8.359
- **Magnitude:** 1432.22 | **LOC:** 2060 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CWebEvents::Invoke` **(Many-Argument Workhorses)** (Impact: 111.2)
  * `CWebBrowser::CallScript` **(Many-Argument Workhorses)** (Impact: 53.5)
    * *Intent:* // Calls the specified active script function, passing the supplied arguments. Returns the function'...
  * `CWebBrowser::ExecuteScript` **(Compute Cores)** (Impact: 37.5)
    * *Intent:* // Executes the specified script and returns the value of the "result" global variable, allowing use...
  * `CWebBrowser::SetSelectedText` **(Compute Cores)** (Impact: 29.9)
  * `CWebBrowser::CallWindowProcHook` **(Many-Argument Workhorses)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 704
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 207`, `args: 160`, `func_start: 111`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 282`, `fragile_debt: 2`, `unreferenced_by_name: 102`
* *Architecture:* `import: 4`
* *Defense:* `doc: 11`, `immutability_locks: 29`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` activscp.h, core.h, support.h, w32browser.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `revmobile/src/revmobile.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.227)
- **Top Global Matches:** file_cluster_4: 5.227, file_cluster_12: 10.42, file_cluster_15: 10.651
- **Magnitude:** 1431.46 | **LOC:** 1455 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (62.1%)
- **Documentation Coverage:** 76.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ForEachEmulator` **(Many-Argument Workhorses)** (Impact: 56.2)
  * `revMobileReadFileRapi` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `revMobileListDevices` **(Many-Argument Workhorses)** (Impact: 46.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// // This would be th...
  * `revMobileWriteFileRapi` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `revMobileLaunchRapi` **(Many-Argument Workhorses)** (Impact: 30.4)
    * *Intent:* //////////
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 703
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 85`, `args: 85`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 241`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `doc: 17`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` comutil.h, corecon.h, devemu.h, external.h, process.h, rapi2.h, stdio.h, windows.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `libfoundation/test/test_memory.cpp` (CPP) | Magnitude: 27.16 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 46, test: 22, explicit_casts: 11, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/lcs/core/network/network.livecodescript` (LIVECODE) | Magnitude: 163.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 47, branch: 42, ipc_rpc_bridges: 35
- `libscript/src/module-bitwise.cpp` (CPP) | Magnitude: 29.58 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 16, indent_tabs: 12, args: 10, indent_spaces: 9
- `tests/lcs/core/interface/interfaceui.livecodescript` (LIVECODE) | Magnitude: 121.44 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: ui_framework: 97, structural_boundaries: 51, branch: 37, indent_spaces: 18
- `toolchain/lc-compile-ffi-java/src/outputfile.c` (C) | Magnitude: 29.02 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, pointers: 11, immutability_locks: 9
- `tests/ide-support/standalonebuilder/java.livecodescript` (LIVECODE) | Magnitude: 32.28 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, state_mutation: 16, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `libfoundation/test/test_system-library.cpp` (CPP) | Magnitude: 49.12 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 74, pointers: 48, immutability_locks: 31, test: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `extensions/script-libraries/semver/tests/semver.livecodescript` (LIVECODE) | Magnitude: 79.64 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 16, state_mutation: 11, func_start: 10
- `tests/lcb/stdlib/bitwise.lcb` (LIVECODE) | Magnitude: 26.86 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 22, branch: 16, func_start: 6, indent_spaces: 4
- `extensions/widgets/tile/tile.lcb` (LIVECODE) | Magnitude: 104.2 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 63, state_mutation: 38, func_start: 13
- `extensions/libraries/androidaudiorecorder/androidaudiorecorder.lcb` (LIVECODE) | Magnitude: 81.72 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 58, indent_tabs: 37, structural_boundaries: 29, branch: 22
- `fetch.py` (PYTHON) | Magnitude: 115.78 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 64, branch: 25, structural_boundaries: 23, state_mutation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `extensions/script-libraries/extension-utils/resources/extension-utils.lc` (LIVECODE) | Magnitude: 37.64 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 15, state_mutation: 10, branch: 7
- `tests/ide-support/standalonebuilder/extensions.livecodescript` (LIVECODE) | Magnitude: 35.34 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 21, state_mutation: 16, func_start: 5
- `extensions/libraries/toast/toast.lcb` (LIVECODE) | Magnitude: 63.38 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 34, branch: 21, structural_boundaries: 18, func_start: 4
- `tests/lcb/vm/interop-objc.lcb` (LIVECODE) | Magnitude: 193.48 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 165, indent_tabs: 125, structural_boundaries: 83, branch: 73
- `tests/lcs/core/multimedia/multimedia.livecodescript` (LIVECODE) | Magnitude: 42.64 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: branch: 19, structural_boundaries: 14, indent_spaces: 13, indent_tabs: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `revdb/src/dbpostgresql.h` (CPP) | Magnitude: 13.92 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: macros: 74, reflection_metaprogramming: 72, indent_tabs: 27, pointers: 18
- `libbrowser/src/libbrowser_osx_webview.h` (OBJECTIVE-C) | Magnitude: 82.56 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 41, func_start: 34, args: 27, bitwise_ops: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `engine/test/test_path.cpp` (CPP) | Magnitude: 21.94 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 131, pointers: 42, test: 17, sync_locks: 10
- `tools/windows_debug_syms.pl` (PERL) | Magnitude: 0.03 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: regex_execution: 8, branch: 6, indent_tabs: 6, structural_boundaries: 5
- `engine/rsrc/emscripten-startup-template.livecodescript` (LIVECODE) | Magnitude: 20.7 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, branch: 9, structural_boundaries: 7, safety: 3
- `builder/installer/uninstalleruifinishcardbehavior.livecodescript` (LIVECODE) | Magnitude: 44.04 | Delta: **0.17** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 18, branch: 7, ui_framework: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lcidlc/src/Support.mm` (OBJECTIVE-C) | Magnitude: 4229.36 | Delta: **0.175** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 1833, indent_spaces: 770, core_var_decl: 706, branch: 609

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `extensions/script-libraries/getopt/getopt.livecodescript` (LIVECODE) | Magnitude: 250.18 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 167, structural_boundaries: 85, branch: 54, state_mutation: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `libcore/include/core.h` (CPP) | Magnitude: 204.78 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 203, args: 126, pointers: 108, indent_tabs: 106
- `libfoundation/test/test_proper-list.cpp` (CPP) | Magnitude: 18.98 | Delta: **0.181** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, pointers: 14, test: 10, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `libbrowser/src/libbrowser_nsvalue.mm` (OBJECTIVE-C) | Magnitude: 143.8 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 83, branch: 29, state_mutation: 23, core_var_decl: 21
- `tests/lcs/core/strings/delimitedchunkoffset.livecodescript` (LIVECODE) | Magnitude: 119.7 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 33, branch: 29, state_mutation: 25

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libfoundation/src/foundation-string.cpp` -> **Severity: 0.165** (Bridge: 0.0016 * Flux: 99.9998%)
- `libfoundation/src/foundation-value.cpp` -> **Severity: 0.149** (Bridge: 0.0015 * Flux: 99.9488%)
- `libfoundation/src/foundation-core.cpp` -> **Severity: 0.056** (Bridge: 0.001 * Flux: 54.3274%)
- `libfoundation/include/foundation-auto.h` -> **Severity: 0.054** (Bridge: 0.0008 * Flux: 64.2653%)
- `libbrowser/src/libbrowser_wkwebview.mm` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 99.9994%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/_testlib.livecodescript` -> **Severity: 10.669** (Embedded: 0.1536 * Error Risk: 69.4563%)
- `engine/test/test_new.cpp` -> **Severity: 6.948** (Embedded: 0.1045 * Error Risk: 66.4678%)
- `libfoundation/include/foundation.h` -> **Severity: 5.414** (Embedded: 0.0925 * Error Risk: 58.5626%)
- `libfoundation/src/foundation-string.cpp` -> **Severity: 5.023** (Embedded: 0.0727 * Error Risk: 69.0756%)
- `libfoundation/include/foundation-stdlib.h` -> **Severity: 4.836** (Embedded: 0.0604 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/_testlib.livecodescript` -> **Severity: 6810.3** (Blast Radius: 68.103 * Doc Risk: 100.0%)
- `libfoundation/include/foundation.h` -> **Severity: 3145.598** (Blast Radius: 34.55 * Doc Risk: 91.0448%)
- `engine/test/test_new.cpp` -> **Severity: 2821.5** (Blast Radius: 28.215 * Doc Risk: 100.0%)
- `libfoundation/src/foundation-value.cpp` -> **Severity: 1941.91** (Blast Radius: 22.296 * Doc Risk: 87.0968%)
- `libfoundation/src/foundation-string.cpp` -> **Severity: 1331.475** (Blast Radius: 15.511 * Doc Risk: 85.8407%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 550 literal sites + 92 sites through wrappers = 642
- **`memory_alloc`:** 831 literal sites + 192 sites through wrappers = 1023
- **`panics_and_aborts`:** 686 literal sites + 83 sites through wrappers = 769

- `new` (macro, memory_alloc, primitive): 119 call sites in 49 files -- `revdb/src/dbdriver.h`
- `Fatal_InternalInconsistency` (function, debug_prints, primitive): 20 call sites in 5 files -- `toolchain/libcompile/src/report.c`
- `Fatal_InternalInconsistency` (function, panics_and_aborts, primitive): 20 call sites in 5 files -- `toolchain/libcompile/src/report.c`
- `Fatal_OutOfMemory` (function, debug_prints, primitive): 20 call sites in 6 files -- `toolchain/libcompile/src/report.c`
- `Fatal_OutOfMemory` (function, panics_and_aborts, primitive): 20 call sites in 6 files -- `toolchain/libcompile/src/report.c`
- `error` (function, debug_prints, primitive): 12 call sites in 1 files -- `config.py`
- `error` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `config.py`
- `MCMemoryNewArray` (function, memory_alloc, via MCMemoryAllocate): 9 call sites in 1 files -- `libcore/src/core.cpp`
- `MCMemoryAllocate` (function, memory_alloc, primitive): 8 call sites in 1 files -- `libcore/src/core.cpp`
- `AnsiToWide` (function, memory_alloc, primitive): 6 call sites in 1 files -- `revmobile/src/revmobile.cpp`
- `_memory_malloc_size` (function, memory_alloc, primitive): 6 call sites in 1 files -- `libfoundation/test/test_memory.cpp`
- `PrintError` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `tests/_testrunner.lcb`
*(+59 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 32195 call pairs -- scoped 28.5%, unique 17.2%, ambiguous 6.2%, external 48.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 16964 | 34.7% | 21.6% | 10.9% | 32.8% |
| livecode | 11071 | 16.6% | 13.6% | 0.3% | 69.5% |
| objective-c | 2618 | 34.9% | 9.1% | 4.9% | 51.1% |
| c | 664 | 35.2% | 16.6% | 0.3% | 47.9% |
| python | 586 | 39.4% | 0.0% | 0.2% | 60.4% |
| shell | 146 | 11.6% | 0.0% | 0.0% | 88.4% |
| java | 82 | 37.8% | 0.0% | 3.7% | 58.5% |
| perl | 34 | 26.5% | 0.0% | 0.0% | 73.5% |
| html | 30 | 0.0% | 0.0% | 0.0% | 100.0% |

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
