# ARCHITECTURAL_BRIEF: root
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/root-project/root.git` |
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
- **Scope:** 14084 analyzed artifact(s), 1959834 LOC.
- **Load-bearing artifact:** `core/base/inc/TString.h` -- 899 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `roottest/root/io/prefetching/atlasFlushed/atlasFlushedProjectHeaders.h` -- pulls in 255 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `builtins/glew/src/glew.c` at magnitude 30822.26 (structural weight, not risk).
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
| Total Artifacts | 31167 |
| Analyzed Artifacts (Scanned) | 14084 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17083 |
| Total LOC | 1959834 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 45.2% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6439 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0815 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 640 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 8114 | 1527552 | 57.6% |
| C | 2710 | 307408 | 19.2% |
| XML | 911 | 0 | 6.5% |
| PLAINTEXT | 792 | 0 | 5.6% |
| PYTHON | 677 | 50588 | 4.8% |
| MARKDOWN | 276 | 0 | 2.0% |
| HTML | 150 | 12660 | 1.1% |
| BINARY_THREAT | 122 | 122 | 0.9% |
| SHELL | 71 | 2915 | 0.5% |
| MAKEFILE | 59 | 9235 | 0.4% |
| JAVASCRIPT | 54 | 15463 | 0.4% |
| YAML | 40 | 2249 | 0.3% |
| OBJECTIVE-C | 38 | 13909 | 0.3% |
| M4 | 23 | 2641 | 0.2% |
| JSON | 20 | 977 | 0.1% |
| CSV | 9 | 150 | 0.1% |
| CSS | 8 | 1100 | 0.1% |
| BATCH | 4 | 275 | 0.0% |
| FORTRAN | 4 | 12570 | 0.0% |
| POWERSHELL | 1 | 6 | 0.0% |
| SQLITE | 1 | 14 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 4 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 13958 |
| unknown | unknown | 122 |
| cp1252 | cp1252-fallback | 4 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Declarative / Non-Code 15%, Large Core Modules (3) 13%, Large Core Modules 11%, Interface Declarations Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12894 | 91.6% |
| Unknown | 122 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1068 | 7.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17083*

**Composition by Extension & Reason:**
- `.h`: 4579x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2619 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 23687 LOC)
- `.cpp`: 4415x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 1350x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.rst')
- `.ref`: 1046x Excluded (Unsupported Extension: '.ref')
- `.png`: 892x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 673x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3357 LOC)
- `.td`: 668x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 394x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 401 LOC), 1x Excluded (Machine-Generated Source Code Signature: 342 LOC)
- `.xpm`: 383x Excluded (Unsupported Extension: '.xpm'), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.root`: 323x Excluded (Unsupported Extension: '.root')
- `.py`: 263x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 115 LOC)
- `.jpg`: 191x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 139x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Unsupported Format (.undeterminable), 2x Unresolved Ambiguity (No Retainable Structure)
- `.def`: 146x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 351, Signals: 0), 1x Zero-Density Threshold (LOC: 72, Signals: 0)
- `.mjs`: 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.8 | 2.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 35.4 | 49.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.9 | 1.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 17.0 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 91.5 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.3 | 23.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 45891 | 3764 | 6 | `roottest/root/io/prefetching/atlasFlushed/atlasFlushedProjectSource.cxx` |
| cleanup | 2275 | 665 | 0 | `roofit/roofitcore/src/BidirMMapPipe.cxx` |
| guards | 192427 | 7960 | 33 | `builtins/glew/src/glew.c` |
| danger | 17827 | 2538 | 2 | `misc/minicern/src/zebra.f` |
| concurrency | 1852 | 298 | 0 | `gui/webdisplay/src/RWebWindow.cxx` |
| connectivity | 40088 | 6839 | 8 | `roottest/cling/template/typedef/cmspb_orig.C` |
| io | 4986 | 766 | 0 | `roottest/scripts/run_roottest.sh` |
| crypto | 3 | 3 | 0 | `.github/workflows/root-ci-config/build_utils.py` |
| ipc | 490 | 118 | 0 | `roofit/roofitcore/src/BidirMMapPipe.cxx` |
| time | 222 | 77 | 0 | `math/mathcore/test/fit/testLogLExecPolicy.cxx` |
| serialization | 362 | 80 | 0 | `misc/minicern/src/zebra.f` |
| regex | 461 | 107 | 0 | `gui/webdisplay/src/RWebDisplayHandle.cxx` |
| events | 2346 | 346 | 0 | `tree/dataframe/inc/ROOT/RDF/ActionHelpers.hxx` |
| tests | 19001 | 605 | 0 | `tree/ntuple/test/ntuple_types.cxx` |
| docs | 197610 | 7397 | 30 | `tree/tree/src/TTree.cxx` |
| debt | 21437 | 2867 | 3 | `test/stressLinear.cxx` |
| mutation | 647423 | 9421 | 88 | `tutorials/legacy/g3d/na49.C` |
| dead_code | 54107 | 5967 | 10 | `roofit/xroofit/src/xRooNode.cxx` |
| credential | 138 | 44 | 0 | `roottest/cling/template/typedef/cmspb_orig.C` |
| threat | 21 | 7 | 0 | `tree/ntuple/test/ntuple_endian.cxx` |
| ml_ai | 2843 | 471 | 0 | `roottest/cling/dict/runalgebra.C` |
| ui | 706 | 99 | 0 | `graf2d/cocoa/src/X11Events.mm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `roottest/scripts/run_roottest.sh` (Hits: 191)
- `documentation/doxygen/makeinput.sh` (Hits: 128)
- `roottest/scripts/Rules.mk` (Hits: 122)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TString.h** (`core/base/inc/TString.h`) — 899 inbound connections
2. **TROOT.h** (`core/base/inc/TROOT.h`) — 827 inbound connections
3. **TMath.h** (`math/mathcore/inc/TMath.h`) — 773 inbound connections
4. **TFile.h** (`io/io/inc/TFile.h`) — 767 inbound connections
5. **TString.cxx** (`core/base/src/TString.cxx`) — 756 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **atlasFlushedProjectHeaders.h** (`roottest/root/io/prefetching/atlasFlushed/atlasFlushedProjectHeaders.h`) — 255 outbound dependencies
2. **converters.h** (`graf2d/win32gdk/gdk/src/iconv/converters.h`) — 146 outbound dependencies
3. **TCling.cxx** (`core/metacling/src/TCling.cxx`) — 134 outbound dependencies
4. **TestCustomModelsFromONNX.cxx** (`tmva/sofie/test/TestCustomModelsFromONNX.cxx`) — 99 outbound dependencies
5. **Spectrum.md** (`documentation/spectrum/Spectrum.md`) — 88 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `TSpectrum2Painter::Paint` **(Many-Argument Workhorses)** (@ `hist/spectrumpainter/src/TSpectrum2Painter.cxx`) -> Impact: **2464.7** | LOC: 5481
  * *Intent:* /// ~~~ /// root > .x VisA.C /// ~~~ /// ~~~ {.cpp} /// #include "TSpectrum2Painter.h" /// /// void VisA() { /// TFile *f = new TFile("TSpectrum2.root...
- `TGaxis::PaintAxis` **(Many-Argument Workhorses)** (@ `graf2d/graf/src/TGaxis.cxx`) -> Impact: **2093.9** | LOC: 1481
  * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Control function to draw an axis. /// Original authors: O.Couet C...
- `TFormula::Analyze` **(Many-Argument Workhorses)** (@ `hist/hist/src/TFormula_v5.cxx`) -> Impact: **1802.8** | LOC: 1457
  * *Intent:* /// /// and write your own constructor /// /// ~~~ {.cpp} /// MyClass::MyClass(const char *name,const char *expression) : TFormula() /// ~~~ /// /// w...
- `glewIsSupported` **(Many-Argument Workhorses)** (@ `builtins/glew/src/glew.c`) -> Impact: **1477.4** | LOC: 5732
  * *Intent:* #endif
- `TTreeFormula::ParseWithLeaf` **(Many-Argument Workhorses)** (@ `tree/treeplayer/src/TTreeFormula.cxx`) -> Impact: **1469.2** | LOC: 1440
  * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Decompose 'expression' as pointing to something inside the leaf /...
- `TSpectrum3::SearchHighRes` **(Many-Argument Workhorses)** (@ `hist/spectrum/src/TSpectrum3.cxx`) -> Impact: **1439.0** | LOC: 1205
  * *Intent:* /// } /// } /// Double_t *PosX = new Double_t[nfound]; /// Double_t *PosY = new Double_t[nfound]; /// Double_t *PosZ = new Double_t[nfound]; /// PosX ...
- `RpdCheckHostsEquiv` **(Many-Argument Workhorses)** (@ `net/rpdutils/src/rpdutils.cxx`) -> Impact: **1319.0** | LOC: 2588
  * *Intent:* /// /// remote.host.dom auser /// /// (allowing user named 'auser' from host 'remote.host.dom' to /// login to any non-root local account without spec...
- `TLatex::Analyse` **(Many-Argument Workhorses)** (@ `graf2d/graf/src/TLatex.cxx`) -> Impact: **1304.2** | LOC: 1393
  * *Intent:* /// /// ~~~ {.cpp} /// width = max(width_arg1, width_arg2) /// up = up_arg1 + down_arg1 /// down = up_arg2 + down_arg2 /// ~~~ /// /// so, when the us...
- `TStreamerInfo::ReadBuffer` **(Many-Argument Workhorses)** (@ `io/io/src/TStreamerInfoReadBuffer.cxx`) -> Impact: **1291.2** | LOC: 983
  * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Deserialize information from buffer b into object at pointer /// ...
- `TSpectrum3::SearchFast` **(Many-Argument Workhorses)** (@ `hist/spectrum/src/TSpectrum3.cxx`) -> Impact: **1221.9** | LOC: 1164
  * *Intent:* /// - source-pointer to the matrix of source spectrum /// - ssizex-x length of source spectrum /// - ssizey-y length of source spectrum /// - ssizez-z...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `hist/hist/src` | 73 | 74741.64 | 37.44% | 65.39% |
| `tmva/sofie/test/input_models` | 122 | 61000.0 | 0.0% | 0.0% |
| `geom/geom/src` | 53 | 55690.38 | 34.79% | 83.07% |
| `gui/gui/src` | 92 | 54751.94 | 32.08% | 83.0% |
| `tmva/tmva/src` | 159 | 48830.72 | 27.2% | 74.69% |
| `roofit/roofitcore/src` | 223 | 44539.48 | 19.13% | 66.8% |
| `hist/spectrum/src` | 7 | 42482.18 | 46.21% | 16.84% |
| `io/io/src` | 37 | 36526.0 | 39.91% | 73.56% |
| `graf2d/asimage/src/libAfterImage` | 53 | 34899.34 | 25.57% | 16.95% |
| `builtins/glew/src` | 3 | 34069.54 | 63.81% | 23.63% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ui5/browser/model/BrowserListBinding.js` -> **100.0%** Exposure
- `ui5/eve7/lib/GlViewer.js` -> **100.0%** Exposure
- `ui5/panel/Controller.js` -> **100.0%** Exposure
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_roofit/_roodecays.py` -> **100.0%** Exposure
- `geom/gdml/writer.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `etc/html/ROOT.js` -> **100.0%** Exposure
- `tutorials/http/httptextlog.mjs` -> **100.0%** Exposure
- `tutorials/visualisation/webcanv/triangle.mjs` -> **100.0%** Exposure
- `ui5/browser/model/BrowserModel.js` -> **100.0%** Exposure
- `ui5/canv/controller/Ged.controller.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/metacling/src/TCling.cxx` -> **312** Orphaned Functions | **0** Duplicates
- `gui/ged/src/TStyleManager.cxx` -> **277** Orphaned Functions | **0** Duplicates
- `roottest/root/io/prefetching/atlasFlushed/atlasFlushedProjectSource.cxx` -> **270** Orphaned Functions | **0** Duplicates
- `roottest/cling/template/typedef/cmspb_orig.C` -> **56** Orphaned Functions | **187** Duplicates
- `graf2d/win32gdk/src/TGWin32.cxx` -> **216** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `122` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `54252` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `builtins/glew/src/glew.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.333)
- **Top Global Matches:** file_cluster_4: 10.333, file_cluster_6: 13.404, file_cluster_16: 14.135
- **Magnitude:** 30822.26 | **LOC:** 28582 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 0.031; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.1%), Guard Balance (formerly Safety Score) (85.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `glewIsSupported` **(Many-Argument Workhorses)** (Impact: 1477.4)
    * *Intent:* #endif
  * `glewContextInit` **(Compute Cores)** (Impact: 837.0)
  * `eglewIsSupported` **(Many-Argument Workhorses)** (Impact: 254.5)
    * *Intent:* #elif defined(GLEW_EGL)
  * `_glewInit_GL_EXT_direct_state_access` **(Compute Cores)** (Impact: 226.1)
    * *Intent:* #endif /* GL_EXT_depth_bounds_test */ #ifdef GL_EXT_direct_state_access
  * `eglewInit` **(Many-Argument Workhorses)** (Impact: 182.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 7629 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 23103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5266`, `structural_boundaries: 1620`, `args: 95`, `func_start: 496`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7845`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 12`
* *Architecture:* `api: 23`, `import: 14`
* *Defense:* `safety: 7`, `immutability_locks: 4218`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 3):` AvailabilityMacros.h, eglew.h, glew.h, glxew.h, osmesa.h, wglew.h, dlfcn.h, dyld.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tutorials/legacy/g3d/na49.C` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.266)
- **Top Global Matches:** file_cluster_2: 6.266, file_cluster_17: 7.984, file_cluster_15: 8.151
- **Magnitude:** 14401.52 | **LOC:** 19312 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (2.3%), Connectivity (formerly Api Exposure) (1.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `na49` **(I/O & Config Routines)** (Impact: 2.0)
    * *Intent:* #ifdef __CLING__ #pragma cling optimize(0) #endif #include "TMaterial.h" #include "TMixture.h" #incl...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 14013`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 9):` TBRIK.h, TBenchmark.h, TGeometry.h, TMaterial.h, TMixture.h, TNode.h, TRotMatrix.h, TTRAP.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/spectrumpainter/src/TSpectrum2Painter.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.348)
- **Top Global Matches:** file_cluster_6: 7.348, file_cluster_8: 12.086, file_cluster_4: 13.957
- **Magnitude:** 13875.16 | **LOC:** 7820 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TSpectrum2Painter::Paint` **(Many-Argument Workhorses)** (Impact: 2464.7)
    * *Intent:* /// ~~~ /// root > .x VisA.C /// ~~~ /// ~~~ {.cpp} /// #include "TSpectrum2Painter.h" /// /// void ...
  * `TSpectrum2Painter::ColorModel` **(Many-Argument Workhorses)** (Impact: 205.9)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// This function c...
  * `TSpectrum2Painter::ColorCalculation` **(Many-Argument Workhorses)** (Impact: 190.2)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Calculates and ...
  * `TSpectrum2Painter::PaintSpectrum` **(Many-Argument Workhorses)** (Impact: 105.4)
    * *Intent:* /// - 7 = Triangle. /// /// cg(enable,color) channel grid. /// In addition to the surface drawn usin...
  * `TSpectrum2Painter::Envelope` **(Many-Argument Workhorses)** (Impact: 97.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Ensures hidden ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2955 instances
* *State Mutation (weighted view):* 10201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1959`, `structural_boundaries: 86`, `args: 43`, `func_start: 44`
* *Risk/State:* `state_mutation: 4291`, `dead_code: 1`, `unreferenced_by_name: 44`
* *Architecture:* `import: 14`
* *Defense:* `doc: 807`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 16):` TBox.h, TColor.h, TEllipse.h, TF1.h, TGaxis.h, TH2.h, THLimitsFinder.h, TLine.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/TPainter3dAlgorithms.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.904)
- **Top Global Matches:** file_cluster_3: 8.904, file_cluster_8: 15.323, file_cluster_6: 28.209
- **Magnitude:** 11032.86 | **LOC:** 5780 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TPainter3dAlgorithms::IsoSurface` **(Many-Argument Workhorses)** (Impact: 334.4)
    * *Intent:* /// /// \param[in] ns number of iso-surfaces /// \param[in] s iso-surface values /// \param[in] nx n...
  * `TPainter3dAlgorithms::ImplicitFunction` **(Many-Argument Workhorses)** (Impact: 217.7)
    * *Intent:* /// Draw implicit function FUN(X,Y,Z) = 0 in cartesian coordinates using /// hidden surface removal ...
  * `TPainter3dAlgorithms::LegoSpherical` **(Many-Argument Workhorses)** (Impact: 213.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Draw stack of l...
  * `TPainter3dAlgorithms::MarchingCube` **(Many-Argument Workhorses)** (Impact: 202.0)
    * *Intent:* /// Topological decider for "Marching Cubes" algorithm Find set of triangles /// approximating the i...
  * `TPainter3dAlgorithms::ZDepth` **(Many-Argument Workhorses)** (Impact: 183.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Z-depth algorit...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2265 instances
* *State Mutation (weighted view):* 7018
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1440`, `structural_boundaries: 386`, `args: 76`, `func_start: 67`
* *Risk/State:* `state_mutation: 2488`, `dead_code: 8`, `unreferenced_by_name: 65`
* *Architecture:* `import: 14`
* *Defense:* `doc: 446`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 20):` Hoption.h, Hparam.h, TColor.h, TF3.h, TH1.h, THLimitsFinder.h, THistPainter.h, TMath.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `math/minuit/src/TMinuit.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.933)
- **Top Global Matches:** file_cluster_8: 10.933, file_cluster_3: 13.952, file_cluster_6: 23.217
- **Magnitude:** 10905.32 | **LOC:** 7899 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (41.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TMinuit::mnexcm` **(Many-Argument Workhorses)** (Impact: 316.9)
    * *Intent:* /// IERFLG is now (94.5) defined the same as ICONDN in MNCOMD = /// - 0: command executed normally /...
  * `TMinuit::mnline` **(Many-Argument Workhorses)** (Impact: 202.3)
    * *Intent:* /// Perform a line search from position START /// /// along direction STEP, where the length of vect...
  * `TMinuit::mncros` **(Many-Argument Workhorses)** (Impact: 177.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Find point wher...
  * `TMinuit::mncont` **(Many-Argument Workhorses)** (Impact: 137.8)
    * *Intent:* /// /// FMIN (X(KE1),X(KE2)) = AMIN+UP /// /// where FMIN is the minimum of FCN with respect to all ...
  * `TMinuit::mnset` **(I/O & Config Routines)** (Impact: 137.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Interprets the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2505 instances
* *State Mutation (weighted view):* 7853
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1418`, `structural_boundaries: 645`, `args: 78`, `func_start: 78`
* *Risk/State:* `state_mutation: 2843`, `dead_code: 23`, `planned_debt: 3`, `fragile_debt: 7`, `unreferenced_by_name: 73`
* *Architecture:* `import: 10`
* *Defense:* `safety: 7`, `doc: 579`, `test: 2`, `immutability_locks: 135`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 13):` TClass.h, TError.h, TList.h, TMath.h, TMinuit.h, TPluginManager.h, TROOT.h, atomic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/histpainter/src/THistPainter.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 13.827)
- **Top Global Matches:** file_cluster_3: 13.827, file_cluster_8: 34.964, file_cluster_1: 35.52
- **Magnitude:** 10266.16 | **LOC:** 11904 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **55**; blast radius 0.023; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.2%)
- **Documentation Coverage:** 1.4085% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `THistPainter::MakeChopt` **(Compute Cores)** (Impact: 260.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Decode string `...
  * `THistPainter::ShowProjection3` **(Many-Argument Workhorses)** (Impact: 199.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Show projection...
  * `THistPainter::PaintContour` **(Compute Cores)** (Impact: 195.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Control functi...
  * `THistPainter::PaintSurface` **(Compute Cores)** (Impact: 190.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Control functi...
  * `THistPainter::PaintErrors` **(Compute Cores)** (Impact: 173.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Draw 1D histog...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1893 instances
* *State Mutation (weighted view):* 5936
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2509`, `structural_boundaries: 259`, `args: 231`, `func_start: 71`
* *Risk/State:* `state_mutation: 2150`, `dead_code: 7`, `fragile_debt: 1`, `unreferenced_by_name: 69`
* *Architecture:* `import: 55`
* *Defense:* `safety: 3`, `doc: 225`, `immutability_locks: 39`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 71):` Hoption.h, Hparam.h, TArrow.h, TCandle.h, TCanvas.h, TColor.h, TCrown.h, TCutG.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `hist/spectrum/src/TSpectrum3.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.162)
- **Top Global Matches:** file_cluster_8: 10.162, file_cluster_3: 15.2, file_cluster_6: 22.202
- **Magnitude:** 10220.46 | **LOC:** 4422 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TSpectrum3::SearchHighRes` **(Many-Argument Workhorses)** (Impact: 1439.0)
    * *Intent:* /// } /// } /// Double_t *PosX = new Double_t[nfound]; /// Double_t *PosY = new Double_t[nfound]; //...
  * `TSpectrum3::SearchFast` **(Many-Argument Workhorses)** (Impact: 1221.9)
    * *Intent:* /// - source-pointer to the matrix of source spectrum /// - ssizex-x length of source spectrum /// -...
  * `TSpectrum3::SmoothMarkov` **(Many-Argument Workhorses)** (Impact: 368.0)
    * *Intent:* /// } /// } /// s->SmoothMarkov(source,nbinsx,nbinsy,nbinsz,3); /// for (i = 0; i < nbinsx; i++){ //...
  * `TSpectrum3::Background` **(Many-Argument Workhorses)** (Impact: 325.9)
    * *Intent:* /// } /// } /// strcpy(PATH,"spectra3/back_peaks_5ds.spe"); /// out=fopen(PATH,"wb"); /// for(i=0;i<...
  * `TSpectrum3::Deconvolution` **(Many-Argument Workhorses)** (Impact: 250.4)
    * *Intent:* /// } /// } /// s->Deconvolution(source,resp,nbinsx,nbinsy,nbinsz,10,10,2); /// for (i = 0; i < nbin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2054 instances
* *State Mutation (weighted view):* 6468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1104`, `structural_boundaries: 37`, `args: 11`, `func_start: 13`
* *Risk/State:* `state_mutation: 2360`, `unreferenced_by_name: 9`
* *Architecture:* `import: 4`
* *Defense:* `doc: 645`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 7):` TH3.h, TMath.h, TSpectrum3.h, TVirtualPad.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `roofit/xroofit/src/xRooNode.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.864)
- **Top Global Matches:** file_cluster_8: 7.864, file_cluster_6: 15.961, file_cluster_3: 22.597
- **Magnitude:** 10125.26 | **LOC:** 12616 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **80**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (74.6%)
- **Documentation Coverage:** 91.5033% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xRooNode::BuildHistogram` **(Many-Argument Workhorses)** (Impact: 1149.9)
  * `xRooNode::Draw` **(Many-Argument Workhorses)** (Impact: 928.3)
  * `xRooNode::Add` **(Many-Argument Workhorses)** (Impact: 522.6)
  * `xRooNode::Multiply` **(Many-Argument Workhorses)** (Impact: 305.3)
  * `xRooNode::SetBinContent` **(Many-Argument Workhorses)** (Impact: 185.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 960 instances
* *Memory Alloc (weighted view):* 73
* *State Mutation (weighted view):* 2932
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3547`, `structural_boundaries: 1649`, `args: 589`, `func_start: 159`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1012`, `dead_code: 517`, `planned_debt: 32`, `fragile_debt: 4`, `duplicate_logic: 6`, `unreferenced_by_name: 99`
* *Architecture:* `api: 7`, `import: 96`
* *Defense:* `safety: 183`, `doc: 38`, `immutability_locks: 224`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 104):` RVersion.h, RooAbsArg.h, RooAbsData.h, RooAddPdf.h, RooAddition.h, RooBinSamplingPdf.h, RooBinning.h, RooCategory.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `misc/minicern/src/zebra.f` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 14.469)
- **Top Global Matches:** file_cluster_3: 14.469, file_cluster_8: 19.021, file_cluster_6: 30.271
- **Magnitude:** 9754.22 | **LOC:** 7291 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.041; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MZLIFT` **(Many-Argument Workhorses)** (Impact: 204.8)
    * *Intent:* *-------------------------------------------------------------------------------
  * `RZOPEN` **(Many-Argument Workhorses)** (Impact: 167.9)
    * *Intent:* *-------------------------------------------------------------------------------
  * `MZPUSH` **(Many-Argument Workhorses)** (Impact: 163.7)
    * *Intent:* *-------------------------------------------------------------------------------
  * `RZREAD` **(Many-Argument Workhorses)** (Impact: 155.3)
    * *Intent:* *-------------------------------------------------------------------------------
  * `MZIOCH` **(Many-Argument Workhorses)** (Impact: 150.9)
    * *Intent:* *-------------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2126 instances
* *State Mutation (weighted view):* 6873
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1205`, `structural_boundaries: 192`, `args: 69`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 759`, `high_risk_execution: 41`, `state_mutation: 2621`, `unreferenced_by_name: 8`
* *Architecture:* `io: 93`, `api: 66`
* *Defense:* `safety: 90`, `immutability_locks: 89`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `hist/spectrum/src/TSpectrum2Fit.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.837)
- **Top Global Matches:** file_cluster_6: 6.837, file_cluster_4: 8.132, file_cluster_15: 15.705
- **Magnitude:** 8883.0 | **LOC:** 5877 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TSpectrum2Fit::FitAwmi` **(Many-Argument Workhorses)** (Impact: 778.4)
    * *Intent:* /// FixPosX, PosY, (Bool_t *) FixPosY, PosX, (Bool_t *) FixPosX, PosY, (Bool_t *) /// FixPosY, Amp, ...
  * `TSpectrum2Fit::FitStiefel` **(Many-Argument Workhorses)** (Impact: 603.2)
    * *Intent:* /// FixPosX, PosY, (Bool_t *) FixPosY, PosX, (Bool_t *) FixPosX, PosY, (Bool_t *) /// FixPosY, Amp, ...
  * `TSpectrum2Fit::Shape2` **(Many-Argument Workhorses)** (Impact: 100.4)
    * *Intent:* /// This function calculates 2D peaks shape function (see manual) /// /// Function parameters: /// -...
  * `TSpectrum2Fit::SetPeakParameters` **(Many-Argument Workhorses)** (Impact: 85.4)
    * *Intent:* /// - fixSigmaY - logical value of sigma y parameter, which allows to fix the parameter (not to fit)...
  * `TSpectrum2Fit::SetFitParameters` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// This function s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2069 instances
* *State Mutation (weighted view):* 6523
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1068`, `structural_boundaries: 73`, `args: 139`, `func_start: 51`
* *Risk/State:* `state_mutation: 2385`, `unreferenced_by_name: 49`
* *Architecture:* `import: 2`
* *Defense:* `doc: 761`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 3):` TMath.h, TSpectrum2Fit.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graf2d/gpad/src/TPad.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.779)
- **Top Global Matches:** file_cluster_6: 6.779, file_cluster_4: 10.734, file_cluster_8: 15.45
- **Magnitude:** 8694.96 | **LOC:** 7683 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **51**; blast radius 0.315; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (63.0%)
- **Documentation Coverage:** 1.0526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TPad::ExecuteEvent` **(Many-Argument Workhorses)** (Impact: 534.0)
    * *Intent:* /// the pad is resized with the rubber rectangle. /// /// If the mouse is clicked inside the pad, th...
  * `TPad::ShowGuidelines` **(Many-Argument Workhorses)** (Impact: 300.6)
    * *Intent:* /// Shows lines to indicate if a TAttBBox2D object is aligned to /// the center or to another object...
  * `TPad::Print` **(Many-Argument Workhorses)** (Impact: 258.2)
    * *Intent:* /// similar to the following one: /// ~~~ {.cpp} /// for (int i=0; i<10; ++i) { /// // fill canvas f...
  * `TPad::ExecuteEventAxis` **(Many-Argument Workhorses)** (Impact: 256.2)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Execute action ...
  * `TPad::BuildLegend` **(Many-Argument Workhorses)** (Impact: 140.4)
    * *Intent:* /// \param[in] option The TLegend option /// /// The caller program owns the returned TLegend. /// /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1374 instances
* *State Mutation (weighted view):* 4393
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1854`, `structural_boundaries: 389`, `args: 319`, `func_start: 190`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1645`, `dead_code: 4`, `unreferenced_by_name: 160`
* *Architecture:* `import: 51`
* *Defense:* `safety: 1`, `doc: 1207`, `immutability_locks: 106`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 67):` TAtt3D.h, TBaseClass.h, TBrowser.h, TBuffer.h, TCanvas.h, TClass.h, TClassTable.h, TColor.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `graf2d/win32gdk/src/TGWin32.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.479)
- **Top Global Matches:** file_cluster_4: 5.479, file_cluster_15: 9.975, file_cluster_16: 11.206
- **Magnitude:** 8513.82 | **LOC:** 7848 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.1%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.7782% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TGWin32::MapGCValues` **(Many-Argument Workhorses)** (Impact: 248.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Map a GCValues_...
  * `TGWin32::MapEvent` **(Many-Argument Workhorses)** (Impact: 211.9)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Map Event_t str...
  * `TGWin32::RequestString` **(Many-Argument Workhorses)** (Impact: 181.4)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Request a strin...
  * `TGWin32::RequestLocator` **(Many-Argument Workhorses)** (Impact: 105.6)
    * *Intent:* /// mode=1 sample /// /// Request locator: /// return button number 1 = left is pressed /// 2 = midd...
  * `TGWin32::UpdateMarkerStyle` **(I/O & Config Routines)** (Impact: 102.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// ///
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 1497 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 5085
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1327`, `structural_boundaries: 443`, `args: 353`, `func_start: 256`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2091`, `dead_code: 14`, `fragile_debt: 1`, `unreferenced_by_name: 216`
* *Architecture:* `io: 3`, `api: 2`, `import: 34`
* *Defense:* `doc: 786`, `sync_locks: 1`, `immutability_locks: 48`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 61):` GuiTypes.h, KeySymbols.h, RStipples.h, TApplication.h, TClassTable.h, TColor.h, TEnv.h, TError.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `hist/hist/src/TH1.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.954)
- **Top Global Matches:** file_cluster_4: 6.954, file_cluster_6: 10.287, file_cluster_15: 12.897
- **Magnitude:** 8367.64 | **LOC:** 10696 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **60** in-repo importer(s); it depends on **45**; blast radius 0.282; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (80.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%)
- **Documentation Coverage:** 0.6897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TH1::Chi2TestX` **(Many-Argument Workhorses)** (Impact: 336.1)
    * *Intent:* /// - For unweighted weighted comparison /// - igood=1'There is a bin in the 1st histogram with less...
  * `TH1::LabelsOption` **(Many-Argument Workhorses)** (Impact: 290.5)
    * *Intent:* /// - "a" sort by alphabetic order /// - ">" sort by decreasing values /// - "<" sort by increasing ...
  * `TH1::Add` **(Many-Argument Workhorses)** (Impact: 135.9)
    * *Intent:* /// you should call Sumw2 before making this operation. /// This is particularly important if you fi...
  * `TH1::KolmogorovTest` **(Many-Argument Workhorses)** (Impact: 111.3)
    * *Intent:* /// /// 1. The value of PROB should not be expected to have exactly the correct /// distribution for...
  * `TH1::Rebin` **(Many-Argument Workhorses)** (Impact: 106.7)
    * *Intent:* /// in the original histogram. If a bin edge in the new histogram is /// in the middle of a bin in t...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1372 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 4162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1770`, `structural_boundaries: 531`, `args: 347`, `func_start: 290`
* *Risk/State:* `state_mutation: 1418`, `dead_code: 22`, `planned_debt: 1`, `unreferenced_by_name: 152`
* *Architecture:* `io: 1`, `import: 45`
* *Defense:* `safety: 1`, `doc: 2719`, `immutability_locks: 310`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.282
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 60):` BinData.h, DataRange.h, HFitInterface.h, GoFTest.h, MinimizerOptions.h, QuantFuncMathCore.h, TBrowser.h, TBuffer.h...
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `hist/histpainter/src/TGraphPainter.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.267)
- **Top Global Matches:** file_cluster_3: 7.267, file_cluster_8: 27.352, file_cluster_6: 40.428
- **Magnitude:** 8187.6 | **LOC:** 5681 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TGraphPainter::PaintGrapHist` **(Many-Argument Workhorses)** (Impact: 650.9)
    * *Intent:* /// |"R" | Graph is drawn horizontally, parallel to X axis. (default is vertically, parallel to Y ax...
  * `TGraphPainter::PaintGraph` **(Many-Argument Workhorses)** (Impact: 414.2)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Control functi...
  * `TGraphPainter::PaintGraphMultiErrors` **(Many-Argument Workhorses)** (Impact: 291.4)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Paint this TGr...
  * `TGraphPainter::PaintGraphBentErrors` **(Many-Argument Workhorses)** (Impact: 247.7)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Paint this TGr...
  * `TGraphPainter::PaintGraphAsymmErrors` **(Many-Argument Workhorses)** (Impact: 236.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// [Paint this TGr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1523 instances
* *State Mutation (weighted view):* 4695
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1560`, `structural_boundaries: 142`, `args: 136`, `func_start: 28`
* *Risk/State:* `state_mutation: 1649`, `dead_code: 7`, `unreferenced_by_name: 28`
* *Architecture:* `import: 33`
* *Defense:* `safety: 1`, `doc: 131`, `immutability_locks: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 46):` TArrow.h, TCanvas.h, TF1.h, TFrame.h, TGaxis.h, TGraph.h, TGraph2D.h, TGraphAsymmErrors.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hist/hist/src/TFormula_v5.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.986)
- **Top Global Matches:** file_cluster_8: 8.986, file_cluster_6: 9.796, file_cluster_4: 17.641
- **Magnitude:** 7665.2 | **LOC:** 4559 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.3%)
- **Documentation Coverage:** 3.2787% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TFormula::Analyze` **(Many-Argument Workhorses)** (Impact: 1802.8)
    * *Intent:* /// /// and write your own constructor /// /// ~~~ {.cpp} /// MyClass::MyClass(const char *name,cons...
  * `TFormula::EvalParOld` **(Many-Argument Workhorses)** (Impact: 379.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Evaluate this f...
  * `TFormula::EvalParFast` **(Many-Argument Workhorses)** (Impact: 275.9)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Evaluate this f...
  * `TFormula::GetExpFormula` **(Compute Cores)** (Impact: 121.0)
    * *Intent:* /// expression originally assigned to the TFormula instance, i.e. that /// the string returned by Ge...
  * `TFormula::Optimize` **(I/O & Config Routines)** (Impact: 120.6)
    * *Intent:* /// ~~~ {.cpp} /// switch(GetActionOptimized(0)){ /// case kData : {fOptimal= (TFormulaPrimitive::TF...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1337 instances
* *State Mutation (weighted view):* 4135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1761`, `structural_boundaries: 244`, `args: 61`, `func_start: 53`
* *Risk/State:* `state_mutation: 1461`, `dead_code: 22`, `planned_debt: 1`, `unreferenced_by_name: 30`
* *Architecture:* `io: 1`, `import: 16`
* *Defense:* `doc: 506`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 27):` TBuffer.h, TClass.h, TError.h, TFunction.h, TInterpreter.h, TMath.h, TMethodCall.h, TObjString.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `graf2d/asimage/src/TASImage.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.502)
- **Top Global Matches:** file_cluster_8: 7.502, file_cluster_6: 9.682, file_cluster_4: 18.069
- **Magnitude:** 7394.56 | **LOC:** 6859 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **40**; blast radius 0.033; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (38.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TASImage::Gradient` **(Many-Argument Workhorses)** (Impact: 186.8)
    * *Intent:* /// in turn, at the intervals given by the offsets attribute. /// /// \param[in] offsets Whitespace-...
  * `TASImage::CopyArea` **(Many-Argument Workhorses)** (Impact: 179.0)
    * *Intent:* /// kGXnoop, // dst /// kGXxor, // src XOR dst /// kGXor, // src OR dst /// kGXnor, // NOT src AND N...
  * `TASImage::MapFileTypes` **(Many-Argument Workhorses)** (Impact: 150.0)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Map file type t...
  * `TASImage::DrawText` **(Many-Argument Workhorses)** (Impact: 128.9)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Draw text at th...
  * `TASImage::Paint` **(Compute Cores)** (Impact: 125.7)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Paint image. //...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1175 instances
* *Memory Alloc (weighted view):* 42
* *State Mutation (weighted view):* 3737
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1380`, `structural_boundaries: 369`, `args: 150`, `func_start: 127`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1387`, `unreferenced_by_name: 100`
* *Architecture:* `io: 8`, `import: 32`
* *Defense:* `safety: 1`, `doc: 638`, `immutability_locks: 100`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 60):` RConfigure.h, TASImage.h, TASImagePlugin.h, TASPolyUtils.c, TArrayD.h, TArrayL.h, TBuffer.h, TColor.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tree/treeplayer/src/TTreeFormula.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.993)
- **Top Global Matches:** file_cluster_8: 6.993, file_cluster_6: 16.84, file_cluster_3: 20.726
- **Magnitude:** 7287.18 | **LOC:** 5986 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **41**; blast radius 0.054; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (48.7%)
- **Documentation Coverage:** 26.5625% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TTreeFormula::ParseWithLeaf` **(Many-Argument Workhorses)** (Impact: 1469.2)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Decompose 'expr...
  * `TTreeFormula::EvalInstance` **(Many-Argument Workhorses)** (Impact: 501.8)
    * *Intent:* /// if (tfv.GetNdata() > 1) /// tfv.EvalInstance(1) /// t.GetEntry(1); /// if (tfv1.GetNdata() > 0) ...
  * `TTreeFormula::FindLeafForExpression` **(Many-Argument Workhorses)** (Impact: 447.4)
    * *Intent:* /// Look for the leaf corresponding to the start of expression. /// It returns the corresponding lea...
  * `TTreeFormula::PrintValue` **(Many-Argument Workhorses)** (Impact: 177.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Return value of...
  * `TTreeFormula::DefinedVariable` **(Many-Argument Workhorses)** (Impact: 164.3)
    * *Intent:* /// - Branch_Name.Leaf_Name[OtherLeaf_Name] /// - Branch_Name.Datamember_Name /// - '.' can be repla...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 971 instances
* *State Mutation (weighted view):* 3017
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1890`, `structural_boundaries: 360`, `args: 99`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1075`, `dead_code: 68`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 34`
* *Architecture:* `api: 1`, `import: 41`
* *Defense:* `safety: 20`, `doc: 279`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 44):` TArrayI.h, TAxis.h, TBranch.h, TBranchElement.h, TBranchObject.h, TBuffer.h, TClonesArray.h, TCutG.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `math/matrix/src/TDecompSparse.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.284)
- **Top Global Matches:** file_cluster_3: 8.284, file_cluster_8: 17.063, file_cluster_6: 29.855
- **Magnitude:** 6704.92 | **LOC:** 2730 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TDecompSparse::Factor_sub2` **(Many-Argument Workhorses)** (Impact: 581.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Help routine fo...
  * `TDecompSparse::InitPivot_sub2` **(Many-Argument Workhorses)** (Impact: 412.9)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Help routine fo...
  * `TDecompSparse::Factor` **(Many-Argument Workhorses)** (Impact: 258.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Factorization r...
  * `TDecompSparse::InitPivot_sub1` **(Many-Argument Workhorses)** (Impact: 159.2)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Help routine fo...
  * `TDecompSparse::InitPivot` **(Many-Argument Workhorses)** (Impact: 151.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Setup Pivoting ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1318 instances
* *State Mutation (weighted view):* 4095
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 52`, `args: 41`, `func_start: 28`
* *Risk/State:* `state_mutation: 1459`, `dead_code: 1`, `fragile_debt: 6`, `unreferenced_by_name: 21`
* *Architecture:* `import: 2`
* *Defense:* `doc: 62`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` TDecompSparse.h, TMath.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `graf3d/gl/src/gl2ps.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.83)
- **Top Global Matches:** file_cluster_4: 6.83, file_cluster_6: 7.319, file_cluster_15: 14.528
- **Magnitude:** 6226.0 | **LOC:** 6035 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.025; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.3%)
- **Documentation Coverage:** 94.7917% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gl2psBeginPage` **(Many-Argument Workhorses)** (Impact: 156.3)
    * *Intent:* /********************************************************************* * * Public routines * *******...
  * `gl2psParseFeedbackBuffer` **(Compute Cores)** (Impact: 110.6)
  * `gl2psPrintPostScriptPrimitive` **(Compute Cores)** (Impact: 100.2)
  * `gl2psPrintPostScriptPixmap` **(Many-Argument Workhorses)** (Impact: 92.0)
  * `gl2psPrintSVGPrimitive` **(Compute Cores)** (Impact: 78.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1110 instances
* *State Mutation (weighted view):* 3596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1169`, `structural_boundaries: 448`, `args: 386`, `func_start: 192`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 2`, `state_mutation: 1376`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 11`, `unreferenced_by_name: 18`
* *Architecture:* `io: 6`, `import: 10`
* *Defense:* `doc: 12`, `immutability_locks: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` cfloat, cmath, cstdarg, cstring, ctime, gl2ps.h, png.h, string...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `hist/spectrum/src/TSpectrum2Transform.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.878)
- **Top Global Matches:** file_cluster_3: 10.878, file_cluster_8: 13.824, file_cluster_6: 26.504
- **Magnitude:** 5930.76 | **LOC:** 2788 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (40.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TSpectrum2Transform::General2` **(Many-Argument Workhorses)** (Impact: 573.5)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// /// This functi...
  * `TSpectrum2Transform::Transform` **(Many-Argument Workhorses)** (Impact: 249.9)
    * *Intent:* /// } /// TSpectrumTransform2 *t = new TSpectrumTransform2(256,256); /// t->SetTransformType(t->kTra...
  * `TSpectrum2Transform::FilterZonal` **(Many-Argument Workhorses)** (Impact: 240.1)
    * *Intent:* /// t->SetTransformType(t->kTransformCos,0); /// t->SetRegion(0,255,128,255); /// t->FilterZonal(sou...
  * `TSpectrum2Transform::Enhance` **(Many-Argument Workhorses)** (Impact: 238.4)
    * *Intent:* /// for (i = 0; i < nbinsx; i++){ /// for (j = 0; j < nbinsy; j++){ /// source[i][j] = trans->GetBin...
  * `TSpectrum2Transform::FourCos2` **(Many-Argument Workhorses)** (Impact: 237.5)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// /// This functi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1280 instances
* *State Mutation (weighted view):* 3940
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 820`, `structural_boundaries: 44`, `args: 22`, `func_start: 21`
* *Risk/State:* `state_mutation: 1380`, `unreferenced_by_name: 19`
* *Architecture:* `import: 2`
* *Defense:* `doc: 338`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` TMath.h, TSpectrum2Transform.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `io/io/src/TStreamerInfo.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.618)
- **Top Global Matches:** file_cluster_8: 6.618, file_cluster_6: 12.722, file_cluster_4: 21.241
- **Magnitude:** 5929.04 | **LOC:** 6086 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **39**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%), Complexity Load (formerly Cognitive Load) (48.7%)
- **Documentation Coverage:** 31.4607% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TStreamerInfo::PrintValueAux` **(Many-Argument Workhorses)** (Impact: 433.5)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// print value of ...
  * `TStreamerInfo::BuildOld` **(I/O & Config Routines)** (Impact: 422.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// rebuild the TSt...
  * `TStreamerInfo::CompareContent` **(Many-Argument Workhorses)** (Impact: 290.5)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Return True if ...
  * `TStreamerInfo::BuildCheck` **(Many-Argument Workhorses)** (Impact: 282.4)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Check if built ...
  * `TStreamerInfo::Build` **(Compute Cores)** (Impact: 271.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Build the I/O d...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 664 instances
* *Memory Alloc (weighted view):* 57
* *State Mutation (weighted view):* 2086
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2000`, `structural_boundaries: 414`, `args: 259`, `func_start: 88`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 758`, `dead_code: 41`, `fragile_debt: 5`, `unreferenced_by_name: 48`
* *Architecture:* `io: 3`, `api: 1`, `import: 39`
* *Defense:* `safety: 15`, `doc: 262`, `immutability_locks: 157`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 52):` TArrayC.h, TArrayD.h, TArrayF.h, TArrayI.h, TArrayL.h, TArrayS.h, TBaseClass.h, TBuffer.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/stressLinear.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.679)
- **Top Global Matches:** file_cluster_8: 12.679, file_cluster_3: 12.955, file_cluster_6: 24.932
- **Magnitude:** 5871.42 | **LOC:** 4434 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (45.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.4%), Connectivity (formerly Api Exposure) (5.2%)
- **Documentation Coverage:** 61.0208% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mstress_vm_multiplications` **(I/O & Config Routines)** (Impact: 429.9)
    * *Intent:* // //------------------------------------------------------------------------ // Verify vector-matri...
  * `mstress_inversion` **(I/O & Config Routines)** (Impact: 425.1)
    * *Intent:* // //------------------------------------------------------------------------ // Verify matrix inver...
  * `spstress_mm_multiplications` **(I/O & Config Routines)** (Impact: 404.4)
    * *Intent:* // //------------------------------------------------------------------------ // Verify matrix multi...
  * `mstress_mm_multiplications` **(I/O & Config Routines)** (Impact: 373.6)
    * *Intent:* // //------------------------------------------------------------------------ // Verify matrix multi...
  * `spstress_vm_multiplications` **(I/O & Config Routines)** (Impact: 371.0)
    * *Intent:* // //------------------------------------------------------------------------ // Verify vector-matri...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 819 instances
* *State Mutation (weighted view):* 2534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 810`, `structural_boundaries: 118`, `args: 179`, `func_start: 63`, `class_start: 8`
* *Risk/State:* `state_mutation: 896`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 28`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 32):` TArrayD.h, TBenchmark.h, TDecompBK.h, TDecompChol.h, TDecompLU.h, TDecompQRH.h, TDecompSVD.h, TFile.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/pyroot/pythonizations/test/ml_dataloader.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.857)
- **Top Global Matches:** file_cluster_6: 10.857, file_cluster_8: 15.001, file_cluster_4: 16.127
- **Magnitude:** 5685.98 | **LOC:** 6444 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (83.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.6%), Complexity Load (formerly Cognitive Load) (33.9%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 99.2063% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `test` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `test` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `test06_multiple_target_columns` **(I/O & Config Routines)** (Impact: 35.7)
  * `test12_PyTorch` **(I/O & Config Routines)** (Impact: 35.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 810 instances
* *State Mutation (weighted view):* 3359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 992`, `structural_boundaries: 149`, `args: 126`, `func_start: 126`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 365`, `state_mutation: 1739`, `duplicate_logic: 25`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `api: 131`, `import: 5`
* *Defense:* `safety: 86`, `doc: 1`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` ROOT, numpy, os, random, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tree/tree/src/TTree.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.225)
- **Top Global Matches:** file_cluster_6: 5.225, file_cluster_4: 10.598, file_cluster_8: 14.245
- **Magnitude:** 5615.54 | **LOC:** 10139 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **77**; blast radius 0.187; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (87.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%)
- **Documentation Coverage:** 4.712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TTree::CheckBranchAddressType` **(Many-Argument Workhorses)** (Impact: 204.7)
    * *Intent:* /// - kMissingCompiledCollectionProxy (-3) : Missing compiled collection proxy for a compiled collec...
  * `TTree::BranchOld` **(Many-Argument Workhorses)** (Impact: 171.3)
    * *Intent:* /// ~~~ {.cpp} /// tree.Branch("B1.","MyClass",&b1,8000,1); /// tree.Branch("B2.","MyClass",&b2,8000...
  * `TTree::ReadStream` **(Many-Argument Workhorses)** (Impact: 149.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Create or simpl...
  * `TTree::CopyEntries` **(Many-Argument Workhorses)** (Impact: 139.4)
    * *Intent:* /// /// See TTree::CloneTree for a detailed explanation of the semantics of these 3 options. /// ///...
  * `TTree::BronchExec` **(Many-Argument Workhorses)** (Impact: 139.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// Helper function...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 641 instances
* *State Mutation (weighted view):* 1978
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1650`, `structural_boundaries: 640`, `args: 245`, `func_start: 190`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 696`, `dead_code: 12`, `fragile_debt: 16`, `unreferenced_by_name: 138`
* *Architecture:* `io: 2`, `import: 77`
* *Defense:* `safety: 5`, `doc: 2983`, `sync_locks: 14`, `immutability_locks: 176`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.187
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 88):` RConfig.hxx, StringConv.hxx, TIOFeatures.hxx, TThreadExecutor.hxx, TArrayC.h, TBaseClass.h, TBasket.h, TBranchClones.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `geom/gdml/src/TGDMLParse.cxx` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.332)
- **Top Global Matches:** file_cluster_3: 6.332, file_cluster_8: 19.708, file_cluster_6: 32.64
- **Magnitude:** 5573.78 | **LOC:** 4629 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 38.5965% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TGDMLParse::ParseGDML` **(Many-Argument Workhorses)** (Impact: 221.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// This function r...
  * `TGDMLParse::VolProcess` **(Many-Argument Workhorses)** (Impact: 217.3)
    * *Intent:* /// In the structure section of the GDML file, volumes can be declared. /// when the volume keyword ...
  * `TGDMLParse::MatProcess` **(Many-Argument Workhorses)** (Impact: 200.6)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// In the material...
  * `TGDMLParse::EleProcess` **(Many-Argument Workhorses)** (Impact: 129.8)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// When the elemen...
  * `TGDMLParse::BooSolid` **(Many-Argument Workhorses)** (Impact: 88.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////////// /// In the solid se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 961 instances
* *State Mutation (weighted view):* 2959
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1182`, `structural_boundaries: 82`, `args: 102`, `func_start: 57`
* *Risk/State:* `state_mutation: 1037`, `dead_code: 11`, `unreferenced_by_name: 57`
* *Architecture:* `import: 40`
* *Defense:* `doc: 209`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 40):` TGDMLMatrix.h, TGDMLParse.h, TGeant4SystemOfUnits.h, TGeoArb8.h, TGeoBBox.h, TGeoBoolNode.h, TGeoCompositeShape.h, TGeoCone.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tmva/tmva/inc/TMVA/DNN/Layer.h` (CPP) | Magnitude: 94.22 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 103, func_start: 46, immutability_locks: 45
- `math/mathcore/inc/Math/Integrator.h` (CPP) | Magnitude: 110.06 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 61, doc: 44, func_start: 34
- `test/stressMathCore.cxx` (CPP) | Magnitude: 951.76 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 847, state_mutation: 283, structural_boundaries: 276, core_var_decl: 248
- `math/smatrix/inc/Math/CholeskyDecomp.h` (CPP) | Magnitude: 764.94 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 665, structural_boundaries: 286, state_mutation: 177, immutability_locks: 138
- `math/vecops/inc/ROOT/RVec.hxx` (CPP) | Magnitude: 1410.82 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1517, structural_boundaries: 877, doc: 726, pointers: 588

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `hist/histv7/test/hist_atomic.cxx` (CPP) | Magnitude: 28.04 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 40, core_var_decl: 17, pointers: 12, args: 11
- `roottest/root/dataframe/test_readerarray.cxx` (CPP) | Magnitude: 15.58 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 9, import: 6, core_var_decl: 4
- `roottest/root/dataframe/regression_multipletriggerrun.cxx` (CPP) | Magnitude: 5.78 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, core_var_decl: 8, design_snake_case: 6
- `gui/browsable/src/TObjectDraw7Provider.cxx` (CPP) | Magnitude: 4.06 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, pointers: 8, structural_boundaries: 6, import: 4
- `tree/dataframe/test/dataframe_friends.cxx` (CPP) | Magnitude: 91.44 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 271, pointers: 88, structural_boundaries: 86, core_var_decl: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `math/experimental/genvectorx/inc/MathX/GenVectorX/PtEtaPhiM4D.h` (CPP) | Magnitude: 206.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 199, structural_boundaries: 88, func_start: 56, immutability_locks: 43
- `graf3d/g3d/inc/TMarker3DBox.h` (CPP) | Magnitude: 25.3 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 24, args: 17, pointers: 17
- `tutorials/io/ntuple/ntpl015_processor_join.C` (C) | Magnitude: 36.9 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, pointers: 20, core_var_decl: 19, structural_boundaries: 17
- `core/foundation/src/RError.cxx` (CPP) | Magnitude: 24.16 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, branch: 8, import: 6, structural_boundaries: 5
- `roottest/root/meta/evolution/execMissingCheckSum.cxx` (CPP) | Magnitude: 22.64 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, pointers: 10, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `graf3d/eve7/inc/ROOT/REveDataCollection.hxx` (CPP) | Magnitude: 60.28 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 64, args: 34, immutability_locks: 32
- `macros/Dialogs.C` (C) | Magnitude: 41.32 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 132, pointers: 75, state_mutation: 18, structural_boundaries: 15
- `io/io/inc/ROOT/RRawFileUnix.hxx` (CPP) | Magnitude: 3.6 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, safety: 7, immutability_locks: 7
- `tutorials/legacy/hist/ratioplot.C` (C) | Magnitude: 4.28 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: pointers: 76, indent_spaces: 58, doc: 11, macros: 3
- `bindings/r/src/TRCompletion.cxx` (CPP) | Magnitude: 67.52 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 57, state_mutation: 19, args: 14, core_var_decl: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `io/doc/v532/index.html` (HTML) | Magnitude: 20.44 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 39, args: 34, indent_spaces: 22, core_var_decl: 19
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_tefficiency.py` (PYTHON) | Magnitude: 8.6 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, args: 2, func_start: 2
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_tmva/_dataloader.py` (PYTHON) | Magnitude: 4.62 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, api: 2, doc: 2
- `io/doc/v530/index.html` (HTML) | Magnitude: 18.54 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 31, args: 27, core_var_decl: 11, design_snake_case: 11
- `math/mathcore/test/stress/testSVector.cxx` (CPP) | Magnitude: 9.28 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 26, core_var_decl: 15, design_snake_case: 11, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `core/meta/inc/TMethodCall.h` (CPP) | Magnitude: 36.38 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 82, indent_spaces: 79, pointers: 74, immutability_locks: 52
- `core/clingutils/src/unordered_multimapLinkdef.h` (CPP) | Magnitude: 15.42 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: macros: 19, structural_boundaries: 4, safety_bypasses: 4, import: 2
- `roottest/root/io/evolution/runReadFixedArrayNewWithOld.C` (C) | Magnitude: 3.14 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, pointers: 7, core_var_decl: 6, import: 5
- `roottest/root/io/evolution/runReadFixedArrayOldWithNew.C` (C) | Magnitude: 3.14 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, pointers: 7, core_var_decl: 6, import: 5
- `tutorials/visualisation/cocoa/parallelcoordtrans.C` (C) | Magnitude: 59.84 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 88, pointers: 81, core_var_decl: 31, design_snake_case: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `math/experimental/genvectorx/inc/MathX/GenVectorX/PtEtaPhiE4D.h` (CPP) | Magnitude: 181.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 195, structural_boundaries: 90, func_start: 53, immutability_locks: 47
- `math/minuit2/inc/Minuit2/FumiliChi2FCN.h` (CPP) | Magnitude: 22.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 16, immutability_locks: 12, structural_boundaries: 10, doc: 9
- `tree/treeplayer/test/branchobject.cxx` (CPP) | Magnitude: 11.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 40, pointers: 25, test: 15, import: 7
- `tutorials/io/ntuple/ntpl005_introspection.C` (C) | Magnitude: 20.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 55, pointers: 21, core_var_decl: 17, structural_boundaries: 15
- `tmva/tmva/src/BinarySearchTreeNode.cxx` (CPP) | Magnitude: 145.58 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 107, pointers: 34, branch: 32, doc: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `bindings/pyroot/pythonizations/test/uhi_indexing.py` (PYTHON) | Magnitude: 376.68 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 105, state_mutation: 76, core_var_decl: 69
- `roottest/root/io/customStreamer/testMemberStreamer2.C` (C) | Magnitude: 45.0 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 23, pointers: 21, branch: 9
- `misc/rmkdepend/cppsetup.c` (C) | Magnitude: 152.34 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 93, pointers: 59, structural_boundaries: 34, state_mutation: 34
- `roottest/python/pickle/PyROOT_readtests.py` (PYTHON) | Magnitude: 120.84 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 33, state_mutation: 33, core_var_decl: 33
- `tutorials/hist/histv7/hist002_RHist_weighted.C` (C) | Magnitude: 36.98 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 59, bitwise_ops: 22, core_var_decl: 17, design_snake_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `core/clingutils/inc/root_std_complex.h` (CPP) | Magnitude: 15.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 6, args: 4, safety: 4, scientific: 4
- `hist/histv7/benchmark/hist_benchmark_stats.cxx` (CPP) | Magnitude: 32.02 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 44, pointers: 16, branch: 10, structural_boundaries: 10
- `tutorials/analysis/unfold/testUnfold5b.C` (C) | Magnitude: 8.92 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 63, indent_spaces: 57, pointers: 23, structural_boundaries: 15
- `graf2d/gpadv7/inc/ROOT/RStyle.hxx` (CPP) | Magnitude: 8.4 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, immutability_locks: 14, pointers: 12, args: 8
- `graf2d/asimage/src/libAfterImage/afterbase.h` (C) | Magnitude: 15.7 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: macros: 6, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `math/genvector/test/vectorOperation.cxx` (CPP) | Magnitude: 157.54 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 53, state_mutation: 44, core_var_decl: 41
- `roottest/root/meta/genreflex/TClass/class6.h` (CPP) | Magnitude: 6.96 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 31, doc: 8, memory_alloc: 4, api: 3
- `roottest/root/tree/reader/execEnum.cxx` (CPP) | Magnitude: 15.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, import: 8, pointers: 7
- `gui/gui/src/TVirtualDragManager.cxx` (CPP) | Magnitude: 28.5 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 13, state_mutation: 12, design_camel_case: 10
- `roottest/root/ntuple/atlas-datavector/template_instantiation.py` (PYTHON) | Magnitude: 8.0 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, test: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tmva/sofie/inc/TMVA/SOFIE_common.hxx` (CPP) | Magnitude: 671.9 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 460, structural_boundaries: 175, immutability_locks: 141, pointers: 130
- `roottest/root/tree/cache/runautocache.C` (C) | Magnitude: 202.32 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 298, pointers: 118, debug_prints: 81, branch: 61
- `roofit/roofitcore/src/RooCurve.cxx` (CPP) | Magnitude: 610.14 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 432, core_var_decl: 116, branch: 107, design_snake_case: 100
- `graf3d/gl/src/TGLSAViewer.cxx` (CPP) | Magnitude: 346.46 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 510, pointers: 191, branch: 107, state_mutation: 59
- `roofit/roostats/src/ProfileLikelihoodCalculator.cxx` (CPP) | Magnitude: 129.8 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 164, pointers: 52, branch: 47, core_var_decl: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `.github/workflows/root-ci-config/build_utils.py` (PYTHON) | Magnitude: 291.7 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 75, core_var_decl: 61, design_snake_case: 61
- `graf2d/quartz/src/QuartzText.mm` (OBJECTIVE-C) | Magnitude: 164.8 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 168, immutability_locks: 39, core_var_decl: 38, pointers: 37
- `core/base/inc/TQObject.h` (CPP) | Magnitude: 81.88 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 121, pointers: 76, structural_boundaries: 59, immutability_locks: 57
- `io/io/inc/TBufferJSON.h` (CPP) | Magnitude: 22.0 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 236, immutability_locks: 225, pointers: 182, structural_boundaries: 176
- `tree/ntuple/inc/ROOT/RField.hxx` (CPP) | Magnitude: 167.06 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 293, immutability_locks: 197, structural_boundaries: 181, pointers: 146

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `hist/hist/src/TH3.cxx` (CPP) | Magnitude: 5462.42 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 2630, pointers: 973, branch: 959, state_mutation: 942
- `hist/unfold/src/TUnfoldDensity.cxx` (CPP) | Magnitude: 1102.48 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 742, doc: 479, pointers: 335, branch: 211
- `roofit/histfactory/src/HistoToWorkspaceFactoryFast.cxx` (CPP) | Magnitude: 843.44 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1083, pointers: 267, branch: 212, core_var_decl: 188
- `graf2d/win32gdk/gdk/src/gdk/testgdk.c` (C) | Magnitude: 740.04 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 574, state_mutation: 170, pointers: 138, branch: 120
- `gui/gui/src/TGSlider.cxx` (CPP) | Magnitude: 492.08 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 360, branch: 149, pointers: 129, state_mutation: 82

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `net/net/inc/TSecContext.h` (CPP) | Magnitude: 58.22 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 40, immutability_locks: 38, pointers: 27
- `tutorials/io/tree/tree501_cernstaff.C` (C) | Magnitude: 8.96 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 75, pointers: 66, structural_boundaries: 13, core_var_decl: 13
- `tmva/tmva/inc/TMVA/DNN/CNN/ContextHandles.h` (CPP) | Magnitude: 5.94 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 57, indent_spaces: 50, core_var_decl: 19, pointers: 17
- `math/mathmore/inc/Math/GSLMinimizer1D.h` (CPP) | Magnitude: 8.86 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 49, doc: 19, structural_boundaries: 17, immutability_locks: 14
- `bindings/distrdf/python/DistRDF/Backends/__init__.py` (PYTHON) | Magnitude: 17.82 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, state_mutation: 7, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `gui/guihtml/src/TGHtmlParse.cxx` (CPP) | Magnitude: 1426.8 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 891, branch: 335, state_mutation: 294, pointers: 221
- `hist/hist/src/HFitInterface.cxx` (CPP) | Magnitude: 824.82 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 520, branch: 193, core_var_decl: 169, pointers: 159

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `bindings/pyroot/pythonizations/python/ROOT/_pythonization/_tmva/_rbdt.py` (PYTHON) | Magnitude: 29.5 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, state_mutation: 6, branch: 5
- `graf2d/win32gdk/gdk/src/gdk/gdkrectangle.c` (C) | Magnitude: 94.94 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 53, pointers: 47, state_mutation: 24, core_var_decl: 14
- `math/mathcore/src/ranluxpp/mulmod.h` (CPP) | Magnitude: 115.1 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 95, core_var_decl: 52, design_snake_case: 50, state_mutation: 30
- `roofit/roofitcore/src/RooQuasiRandomGenerator.cxx` (CPP) | Magnitude: 305.96 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 142, state_mutation: 73, branch: 30, core_var_decl: 24
- `math/minuit2/src/MnPosDef.cxx` (CPP) | Magnitude: 57.04 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, core_var_decl: 16, design_snake_case: 15, branch: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tree/ntuple/src/RFieldMeta.cxx` -> Churn: **76.97%** | Cog Load: 69.1126% | Debt: 99.9849%
- `bindings/pyroot/pythonizations/python/ROOT/_facade.py` -> Churn: **70.89%** | Cog Load: 78.5192% | Debt: 8.9261%
- `main/src/RootObjTree.cxx` -> Churn: **67.86%** | Cog Load: 55.5194% | Debt: 0.0%
- `hist/hist/src/TFormula.cxx` -> Churn: **67.27%** | Cog Load: 38.6944% | Debt: 74.6754%
- `tree/ntuple/src/RField.cxx` -> Churn: **63.64%** | Cog Load: 31.4805% | Debt: 99.936%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `hist/spectrum/src/TSpectrum3.cxx` -> **ferdymercury** (100.0% isolated ownership) | Magnitude: 10220.46
- `hist/histpainter/src/TGraphPainter.cxx` -> **ferdymercury** (100.0% isolated ownership) | Magnitude: 8187.6
- `graf2d/asimage/src/TASImage.cxx` -> **Sergey Linev** (100.0% isolated ownership) | Magnitude: 7394.56
- `math/matrix/src/TDecompSparse.cxx` -> **mdessole** (100.0% isolated ownership) | Magnitude: 6704.92
- `test/stressLinear.cxx` -> **ferdymercury** (100.0% isolated ownership) | Magnitude: 5871.42

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/base/inc/Rtypes.h` -> **Severity: 3021.8** (Blast Radius: 30.218 * Doc Risk: 100.0%)
- `core/base/inc/TString.h` -> **Severity: 1970.238** (Blast Radius: 20.137 * Doc Risk: 97.8417%)
- `core/base/inc/TNamed.h` -> **Severity: 1239.7** (Blast Radius: 12.397 * Doc Risk: 100.0%)
- `core/base/inc/TObject.h` -> **Severity: 1064.895** (Blast Radius: 19.056 * Doc Risk: 55.8824%)
- `bindings/pyroot/pythonizations/python/ROOT/__init__.py` -> **Severity: 693.578** (Blast Radius: 10.789 * Doc Risk: 64.2857%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 16901 literal sites + 224 sites through wrappers = 17125
- **`memory_alloc`:** 21411 literal sites + 1188 sites through wrappers = 22599
- **`panics_and_aborts`:** 4033 literal sites + 23 sites through wrappers = 4056

- `g_free` (function, memory_alloc, primitive): 289 call sites in 59 files -- `graf2d/win32gdk/gdk/src/glib/gmem.c`
- `WIN32_GDI_FAILED` (macro, memory_alloc, via gdk_win32_gdi_failed): 125 call sites in 8 files -- `graf2d/win32gdk/gdk/src/gdk/win32/gdkprivate-win32.h`
- `safemalloc` (macro, memory_alloc, primitive): 83 call sites in 16 files -- `graf2d/asimage/src/libAfterImage/asim_afterbase.h`
- `StartTest` (function, memory_alloc, primitive): 79 call sites in 1 files -- `test/stressGraphics.cxx`
- `safecalloc` (macro, memory_alloc, primitive): 77 call sites in 14 files -- `graf2d/asimage/src/libAfterImage/asim_afterbase.h`
- `gl2psMalloc` (function, memory_alloc, primitive): 62 call sites in 1 files -- `graf3d/gl/src/gl2ps.cxx`
- `free_scanline` (function, memory_alloc, primitive): 43 call sites in 9 files -- `graf2d/asimage/src/libAfterImage/scanline.c`
- `WIN32_API_FAILED` (macro, memory_alloc, via gdk_win32_api_failed): 34 call sites in 5 files -- `graf2d/win32gdk/gdk/src/gdk/win32/gdkprivate-win32.h`
- `string2charptr` (function, memory_alloc, primitive): 25 call sites in 1 files -- `core/dictgen/src/rootcling_impl.cxx`
- `train_and_save` (function, debug_prints, primitive): 25 call sites in 1 files -- `bindings/pyroot/pythonizations/test/generate_keras_sequential.py`
- `TestOptimizeConfigParameters` (function, memory_alloc, via GetOptimiser): 24 call sites in 1 files -- `tmva/tmva/test/TestOptimizeConfigParameters.cxx`
- `create_asimage` (function, memory_alloc, via safecalloc): 21 call sites in 9 files -- `graf2d/asimage/src/libAfterImage/asimage.c`
*(+185 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 403539 call pairs -- scoped 28.8%, unique 5.3%, ambiguous 42.0%, external 23.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 326993 | 30.8% | 4.2% | 45.8% | 19.3% |
| c | 47913 | 25.2% | 14.8% | 37.4% | 22.7% |
| python | 19941 | 11.6% | 0.0% | 6.4% | 82.0% |
| javascript | 4183 | 8.7% | 0.0% | 4.8% | 86.5% |
| objective-c | 3138 | 20.0% | 12.2% | 18.9% | 48.9% |
| fortran | 536 | 42.9% | 48.9% | 0.0% | 8.2% |
| shell | 354 | 9.9% | 0.0% | 0.0% | 90.1% |
| m4 | 316 | 6.6% | 0.0% | 0.0% | 93.4% |
| html | 159 | 5.7% | 0.0% | 0.0% | 94.3% |
| makefile | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
