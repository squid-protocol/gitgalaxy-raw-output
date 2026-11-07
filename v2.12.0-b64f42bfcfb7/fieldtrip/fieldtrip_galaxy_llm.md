# ARCHITECTURAL_BRIEF: fieldtrip
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/fieldtrip/fieldtrip` |
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
- **Scope:** 3210 analyzed artifact(s), 266303 LOC.
- **Load-bearing artifact:** `utilities/dccnpath.m` -- 537 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/rfbevent.c` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ft_electrodeplacement.m` at magnitude 4994.82 (structural weight, not risk).
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
| Total Artifacts | 8018 |
| Analyzed Artifacts (Scanned) | 3210 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4808 |
| Total LOC | 266303 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 40.0% |
| Dominant Lang | MATLAB |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4796 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.202 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.773 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 209 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MATLAB | 2913 | 240338 | 90.7% |
| C | 90 | 11811 | 2.8% |
| CPP | 70 | 9574 | 2.2% |
| MARKDOWN | 64 | 0 | 2.0% |
| PLAINTEXT | 39 | 0 | 1.2% |
| MAKEFILE | 20 | 1644 | 0.6% |
| SHELL | 6 | 2660 | 0.2% |
| YAML | 4 | 79 | 0.1% |
| PYTHON | 2 | 112 | 0.1% |
| HTML | 1 | 54 | 0.0% |
| BATCH | 1 | 31 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 6 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3204 |
| cp1252 | cp1252-fallback | 6 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 35%, Many-Argument Workhorses Files 30%, Data / Markup / Trivial 11%, Large Core Modules (2) 8%, Compute Cores Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3107 | 96.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 103 | 3.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4808*

**Composition by Extension & Reason:**
- `.m`: 2367x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Saturation: Line 10 exceeds 500 chars), 7x Excluded (Saturation: Line 12 exceeds 500 chars)
- `no_extension`: 123x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 95x Excluded (Binary Format Detected), 2x Unsupported Format (.undeterminable)
- `.mexa64`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 73x Excluded (Unsupported Extension: '.mexa64'), 34x Excluded (Binary Format Detected)
- `.mexmaci64`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 64x Excluded (Unsupported Extension: '.mexmaci64'), 30x Excluded (Binary Format Detected)
- `.mexw64`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 55x Excluded (Unsupported Extension: '.mexw64'), 29x Excluded (Binary Format Detected)
- `.mexw32`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 59x Excluded (Unsupported Extension: '.mexw32'), 29x Excluded (Binary Format Detected)
- `.mat`: 124x Excluded (Unsupported Extension: '.mat'), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.mexmaca64`: 75x Excluded (Unsupported Extension: '.mexmaca64'), 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 30x Excluded (Binary Format Detected)
- `.c`: 137x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mexglx`: 55x Excluded (Unsupported Extension: '.mexglx'), 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 24x Excluded (Binary Format Detected)
- `.mexmaci`: 54x Excluded (Unsupported Extension: '.mexmaci'), 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 27x Excluded (Binary Format Detected)
- `.txt`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.p`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.p')
- `.exe`: 62x Excluded (Explicitly Denied Extension: '.exe')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 41.9 | 43.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.3 | 68.0 | 69.6 | 52.1 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.0 | 17.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.4 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 97.7 | 3.8 | 3.4 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 57.7 | 99.9 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 93.2 | 2.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 94.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6058 | 1280 | 5 | `fileio/private/read_besa_besa.m` |
| cleanup | 1726 | 648 | 2 | `fileio/private/read_besa_besa.m` |
| guards | 18774 | 1873 | 16 | `fileio/ft_read_event.m` |
| danger | 2333 | 656 | 2 | `test/test_ft_timelockanalysis_new.m` |
| concurrency | 183 | 69 | 0 | `realtime/src/acquisition/gtec/gdsnetworkinterfacedemo_platform_specific.hpp` |
| connectivity | 4884 | 3009 | 2 | `ft_electrodeplacement.m` |
| io | 3166 | 617 | 1 | `fileio/private/read_4d_hdr.m` |
| crypto | 0 | 0 | 0 | - |
| ipc | 281 | 113 | 0 | `src/rfbevent.c` |
| time | 478 | 149 | 0 | `test/invalid/failed_old_specest_vs_oldimplementation.m` |
| serialization | 673 | 383 | 1 | `test/test_ft_freqanalysis.m` |
| regex | 427 | 130 | 0 | `utilities/ft_channelselection.m` |
| events | 82 | 30 | 0 | `realtime/src/acquisition/neuralynx/nlx2ft.cc` |
| tests | 5 | 4 | 0 | `test/test_nanstat.m` |
| docs | 643 | 143 | 0 | `realtime/online_eeg/private/portmidi.h` |
| debt | 4637 | 1005 | 3 | `ft_volumerealign.m` |
| mutation | 206786 | 3047 | 147 | `bin/synchronize-private.sh` |
| dead_code | 4107 | 2988 | 2 | `test/invalid/failed_ft_sourceanalysis.m` |
| credential | 14 | 9 | 0 | `test/test_bug2096.m` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 8456 | 869 | 4 | `fileio/private/ft_warp_apply.m` |
| ui | 2931 | 438 | 2 | `test/test_ft_plot_sens.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `fileio/private/read_4d_hdr.m` (Hits: 158)
- `fileio/private/read_besa_besa.m` (Hits: 130)
- `fileio/private/read_itab_mhd.m` (Hits: 111)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **dccnpath.m** (`utilities/dccnpath.m`) — 537 inbound connections
2. **any.m** (`compat/matlablt2010b/@uint64/any.m`) — 472 inbound connections
3. **all.m** (`compat/matlablt2010b/@uint64/all.m`) — 387 inbound connections
4. **max.m** (`compat/matlablt2010b/@uint64/max.m`) — 354 inbound connections
5. **abs.m** (`compat/matlablt2010b/@uint64/abs.m`) — 315 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rfbevent.c** (`src/rfbevent.c`) — 18 outbound dependencies
2. **opengl_client.cc** (`realtime/src/acquisition/siemens/src/opengl_client.cc`) — 18 outbound dependencies
3. **viewer.cc** (`realtime/src/utilities/viewer/viewer.cc`) — 16 outbound dependencies
4. **gdsnetworkinterfacedemo_platform_specific.hpp** (`realtime/src/acquisition/gtec/gdsnetworkinterfacedemo_platform_specific.hpp`) — 15 outbound dependencies
5. **main.cpp** (`realtime/src/acquisition/gtec/main.cpp`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ft_sourceanalysis` **(Many-Argument Workhorses)** (@ `ft_sourceanalysis.m`) -> Impact: **580.5** | LOC: 1249
  * *Intent:* % FT_SOURCEANALYSIS performs beamformer dipole analysis on EEG or MEG data % after preprocessing and a timelocked or frequency analysis % % Use as % [...
- `cb_help` **(Many-Argument Workhorses)** (@ `ft_electrodeplacement.m`) -> Impact: **453.8** | LOC: 1213
  * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
- `ft_hastoolbox` **(Many-Argument Workhorses)** (@ `fileio/private/ft_hastoolbox.m`) -> Impact: **453.4** | LOC: 789
  * *Intent:* % FT_HASTOOLBOX tests whether an external toolbox is installed. Optionally it will % try to determine the path to the toolbox and install it automatic...
- `ft_hastoolbox` **(Many-Argument Workhorses)** (@ `forward/private/ft_hastoolbox.m`) -> Impact: **453.4** | LOC: 789
  * *Intent:* % FT_HASTOOLBOX tests whether an external toolbox is installed. Optionally it will % try to determine the path to the toolbox and install it automatic...
- `ft_hastoolbox` **(Many-Argument Workhorses)** (@ `inverse/private/ft_hastoolbox.m`) -> Impact: **453.4** | LOC: 789
  * *Intent:* % FT_HASTOOLBOX tests whether an external toolbox is installed. Optionally it will % try to determine the path to the toolbox and install it automatic...
- `ft_hastoolbox` **(Many-Argument Workhorses)** (@ `plotting/private/ft_hastoolbox.m`) -> Impact: **453.4** | LOC: 789
  * *Intent:* % FT_HASTOOLBOX tests whether an external toolbox is installed. Optionally it will % try to determine the path to the toolbox and install it automatic...
- `ft_hastoolbox` **(Many-Argument Workhorses)** (@ `utilities/ft_hastoolbox.m`) -> Impact: **453.4** | LOC: 789
  * *Intent:* % FT_HASTOOLBOX tests whether an external toolbox is installed. Optionally it will % try to determine the path to the toolbox and install it automatic...
- `cb_redraw` **(Many-Argument Workhorses)** (@ `ft_electrodeplacement.m`) -> Impact: **438.3** | LOC: 1180
  * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
- `cb_redraw_volume` **(Many-Argument Workhorses)** (@ `ft_electrodeplacement.m`) -> Impact: **430.4** | LOC: 1161
  * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
- `ft_read_header` **(Many-Argument Workhorses)** (@ `fileio/ft_read_header.m`) -> Impact: **423.7** | LOC: 1199
  * *Intent:* % FT_READ_HEADER reads header information from a variety of EEG, MEG and other time % series data files and represents the header information in a com...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 163 | 82788.24 | 69.53% | 31.21% |
| `fileio/private` | 372 | 62214.96 | 62.22% | 36.31% |
| `private` | 321 | 43069.62 | 53.96% | 38.43% |
| `fileio` | 34 | 26239.02 | 58.05% | 33.76% |
| `utilities` | 96 | 19549.92 | 59.87% | 36.32% |
| `plotting/private` | 91 | 11976.26 | 54.14% | 36.64% |
| `forward/private` | 96 | 11745.22 | 54.25% | 38.82% |
| `utilities/private` | 119 | 11158.48 | 54.96% | 36.04% |
| `plotting` | 32 | 9280.28 | 69.71% | 26.91% |
| `src` | 72 | 7617.96 | 44.41% | 33.03% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `utilities/ft_affinecoordinates.m` -> **100.0%** Exposure
- `fileio/private/fetch_url.m` -> **99.9999%** Exposure
- `fileio/private/netmeg2grad.m` -> **99.9999%** Exposure
- `fileio/private/dimlength.m` -> **99.9986%** Exposure
- `private/dimlength.m` -> **99.9986%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/scripts/suggest_tests.py` -> **100.0%** Exposure
- `realtime/src/acquisition/siemens/python/fakeScanner.py` -> **100.0%** Exposure
- `besa2fieldtrip.m` -> **100.0%** Exposure
- `compat/matlablt2010b/iscolumn.m` -> **100.0%** Exposure
- `compat/matlablt2010b/ismatrix.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/invalid/failed_ft_sourceanalysis.m` -> **23** Orphaned Functions | **0** Duplicates
- `realtime/src/acquisition/amp/AmpServerClient.cpp` -> **21** Orphaned Functions | **0** Duplicates
- `realtime/src/acquisition/tmsi/Feature.cpp` -> **20** Orphaned Functions | **0** Duplicates
- `realtime/src/acquisition/siemens/src/PixelDataGrabber.cc` -> **17** Orphaned Functions | **0** Duplicates
- `realtime/src/acquisition/gtec/Transceiver.cpp` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `utilities/ft_trackusage.m` -> **99.9999%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `715` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `738` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ft_electrodeplacement.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 13.717)
- **Top Global Matches:** file_cluster_3: 13.717, file_cluster_8: 34.984, file_cluster_1: 35.39
- **Magnitude:** 4994.82 | **LOC:** 2086 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 0.252; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_help` **(Many-Argument Workhorses)** (Impact: 453.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 438.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_volume` **(Many-Argument Workhorses)** (Impact: 430.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_scatter` **(Many-Argument Workhorses)** (Impact: 363.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_headshape` **(Many-Argument Workhorses)** (Impact: 335.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 336 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 1271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 149`, `args: 33`, `func_start: 34`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 599`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 34`
* *Defense:* `safety: 42`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.252
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.001246
  * `Imports (Out-Degree: 17):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `fileio/private/read_besa_besa.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 16.761)
- **Top Global Matches:** file_cluster_3: 16.761, file_cluster_1: 32.647, file_cluster_8: 38.003
- **Magnitude:** 4740.28 | **LOC:** 2073 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.228; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.9%)
- **Documentation Coverage:** 78.6885% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_BEVT` **(Many-Argument Workhorses)** (Impact: 344.2)
    * *Intent:* %% EVENT BLOCK FUNCTIONS %% Read event block % BEVT_offset [scalar] - offset of current event block ...
  * `read_event_tag` **(Many-Argument Workhorses)** (Impact: 281.4)
    * *Intent:* % Read an event into a structure % Create the event object event_obj.evttype = event_tag; switch eve...
  * `thirdscheme_lookup` **(Many-Argument Workhorses)** (Impact: 274.9)
    * *Intent:* % Lookup table for third scheme % Use persistent variable so lookup table does not need to be recomp...
  * `read_event_tag_base` **(Many-Argument Workhorses)** (Impact: 266.3)
    * *Intent:* % Read data in the COMM event tag block % Loop through all tags in data section while ~feof(fid) && ...
  * `read_event_tag_comm` **(Many-Argument Workhorses)** (Impact: 239.1)
    * *Intent:* % Read data in the COMM event tag block % Loop through all tags in data section while ~feof(fid) && ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 407 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1379
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 256`, `args: 28`, `func_start: 28`
* *Risk/State:* `state_mutation: 565`, `planned_debt: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 130`, `api: 28`, `import: 1`
* *Defense:* `safety: 39`, `doc: 15`, `cleanup: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074635
  * `Imports (Out-Degree: 3):` com.mathworks.mlwidgets.io.InterruptibleStreamCopier
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ft_volumerealign.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 18.2)
- **Top Global Matches:** file_cluster_1: 18.2, file_cluster_3: 30.707, file_cluster_8: 52.447
- **Magnitude:** 4538.96 | **LOC:** 2147 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); blast radius 0.534; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assignweights` **(Many-Argument Workhorses)** (Impact: 400.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_help` **(Many-Argument Workhorses)** (Impact: 399.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 390.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_ortho` **(Many-Argument Workhorses)** (Impact: 381.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `ft_volumerealign` **(Many-Argument Workhorses)** (Impact: 325.2)
    * *Intent:* % FT_VOLUMEREALIGN spatially aligns an anatomical MRI with head coordinates based on % external fidu...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 435 instances
* *High Risk Execution (weighted view):* 10
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 150`, `args: 18`, `func_start: 17`
* *Risk/State:* `high_risk_execution: 18`, `state_mutation: 636`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 17`
* *Defense:* `safety: 62`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.534
  * `Choke Point (Betweenness):` 0.00024 | `Ripple Effect (Closeness):` 0.005298
  * `Imports (Out-Degree: 25):` None
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `fileio/ft_filetype.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.312)
- **Top Global Matches:** file_cluster_6: 9.312, file_cluster_8: 9.826, file_cluster_4: 17.016
- **Magnitude:** 4219.16 | **LOC:** 1873 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); blast radius 4.649; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Complexity Load (formerly Cognitive Load) (89.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_filetype` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* % FT_FILETYPE determines the filetype of many EEG/MEG/MRI data files by % looking at the name, exten...
  * `most` **(Compute Cores)** (Impact: 30.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that he...
  * `filetype_true` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that al...
  * `filetype_check_ced_spike6mat` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that ch...
  * `filetype_check_openvibe_mat` **(Compute Cores)** (Impact: 27.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that ch...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1020 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 3068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 776`, `structural_boundaries: 66`, `args: 13`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1028`, `fragile_debt: 10`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 13`
* *Defense:* `safety: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.649
  * `Choke Point (Betweenness):` 0.000554 | `Ripple Effect (Closeness):` 0.143826
  * `Imports (Out-Degree: 7):` None
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `fileio/ft_read_header.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.772)
- **Top Global Matches:** file_cluster_6: 6.772, file_cluster_4: 11.226, file_cluster_8: 15.176
- **Magnitude:** 4156.1 | **LOC:** 3097 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **157** in-repo importer(s); blast radius 5.547; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.6%), Guard Balance (formerly Safety Score) (91.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_read_header` **(Many-Argument Workhorses)** (Impact: 423.7)
    * *Intent:* % FT_READ_HEADER reads header information from a variety of EEG, MEG and other time % series data fi...
  * `filesize` **(Defensive Guards)** (Impact: 25.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to dete...
  * `recursive_read_header` **(Defensive Guards)** (Impact: 23.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to dete...
  * `fixlabels` **(Defensive Guards)** (Impact: 8.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to fill...
  * `fixchantype` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to fill...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 952 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 3059
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 564`, `structural_boundaries: 338`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1155`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 6`
* *Defense:* `safety: 188`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.547
  * `Choke Point (Betweenness):` 0.009398 | `Ripple Effect (Closeness):` 0.101553
  * `Imports (Out-Degree: 102):` None
  * `Imported By (In-Degree: 157):` (Excluded from Brief to save tokens)

### `ft_geometryplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 18.173)
- **Top Global Matches:** file_cluster_1: 18.173, file_cluster_3: 30.396, file_cluster_8: 52.184
- **Magnitude:** 3675.06 | **LOC:** 1005 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%), Complexity Load (formerly Cognitive Load) (68.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_creategui` **(Many-Argument Workhorses)** (Impact: 257.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `ft_geometryplot` **(Many-Argument Workhorses)** (Impact: 228.4)
    * *Intent:* % FT_GEOMETRYPLOT plots objects in 3D, such as sensors, headmodels, sourcemodels, % headshapes, mesh...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 219.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_toggle` **(Many-Argument Workhorses)** (Impact: 181.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_camlight` **(Many-Argument Workhorses)** (Impact: 179.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 148 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 562
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 74`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 266`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 28`
* *Defense:* `safety: 54`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_event.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.35)
- **Top Global Matches:** file_cluster_9: 6.35, file_cluster_15: 12.477, file_cluster_16: 12.746
- **Magnitude:** 3511.22 | **LOC:** 2690 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **94** in-repo importer(s); blast radius 3.22; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Complexity Load (formerly Cognitive Load) (80.0%), Debt Markers (formerly Tech Debt) (17.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_read_event` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* % FT_READ_EVENT reads all events from an EEG, MEG or other time series dataset and % returns them in...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 795 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 2517
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 604`, `structural_boundaries: 611`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 927`, `dead_code: 5`, `fragile_debt: 12`
* *Architecture:* `io: 5`, `api: 1`
* *Defense:* `safety: 223`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.22
  * `Choke Point (Betweenness):` 0.00106 | `Ripple Effect (Closeness):` 0.033548
  * `Imports (Out-Degree: 67):` None
  * `Imported By (In-Degree: 94):` (Excluded from Brief to save tokens)

### `fileio/private/ft_checkdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.947)
- **Top Global Matches:** file_cluster_8: 6.947, file_cluster_6: 16.267, file_cluster_3: 21.56
- **Magnitude:** 3150.56 | **LOC:** 1911 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `freq2raw` **(Compute Cores)** (Impact: 105.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `timelock2raw` **(Compute Cores)** (Impact: 76.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `fixcov` **(Defensive Guards)** (Impact: 73.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % represent the covar...
  * `fixcsd` **(Many-Argument Workhorses)** (Impact: 64.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % represent the cros...
  * `chan2freq` **(Compute Cores)** (Impact: 62.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 638 instances
* *Memory Alloc (weighted view):* 39
* *State Mutation (weighted view):* 1982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 265`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 706`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* `api: 19`
* *Defense:* `safety: 122`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utilities/ft_checkdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.947)
- **Top Global Matches:** file_cluster_8: 6.947, file_cluster_6: 16.267, file_cluster_3: 21.56
- **Magnitude:** 3150.56 | **LOC:** 1911 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `freq2raw` **(Compute Cores)** (Impact: 105.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `timelock2raw` **(Compute Cores)** (Impact: 76.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `fixcov` **(Defensive Guards)** (Impact: 73.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % represent the covar...
  * `fixcsd` **(Many-Argument Workhorses)** (Impact: 64.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % represent the cros...
  * `chan2freq` **(Compute Cores)** (Impact: 62.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 638 instances
* *Memory Alloc (weighted view):* 39
* *State Mutation (weighted view):* 1982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 265`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 706`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* `api: 19`
* *Defense:* `safety: 122`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_prepare_layout.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.939)
- **Top Global Matches:** file_cluster_1: 5.939, file_cluster_3: 48.221, file_cluster_8: 70.038
- **Magnitude:** 3060.68 | **LOC:** 1843 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **59** in-repo importer(s); blast radius 1.994; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sens2lay` **(Many-Argument Workhorses)** (Impact: 329.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % conve...
  * `readlay` **(Many-Argument Workhorses)** (Impact: 182.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % read ...
  * `opto2lay` **(Many-Argument Workhorses)** (Impact: 158.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % conve...
  * `ft_prepare_layout` **(Many-Argument Workhorses)** (Impact: 148.4)
    * *Intent:* % FT_PREPARE_LAYOUT loads or creates a 2-D layout of the channel locations. This % layout is require...
  * `shiftxy` **(Many-Argument Workhorses)** (Impact: 83.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % shift...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 442 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 229`, `args: 12`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 605`, `dead_code: 4`, `fragile_debt: 3`
* *Architecture:* `io: 5`, `api: 11`
* *Defense:* `safety: 135`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.994
  * `Choke Point (Betweenness):` 0.003406 | `Ripple Effect (Closeness):` 0.039604
  * `Imports (Out-Degree: 18):` None
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `ft_sourceplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.68)
- **Top Global Matches:** file_cluster_8: 11.68, file_cluster_3: 13.612, file_cluster_6: 23.981
- **Magnitude:** 2807.08 | **LOC:** 2164 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **66** in-repo importer(s); blast radius 1.86; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 173.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_help` **(Many-Argument Workhorses)** (Impact: 160.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_keyboard` **(Many-Argument Workhorses)** (Impact: 154.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `ft_sourceplot` **(Many-Argument Workhorses)** (Impact: 132.2)
    * *Intent:* % FT_SOURCEPLOT plots functional source reconstruction data on slices or on a surface, % optionally ...
  * `cb_buttonpress` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 495 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 1633
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 523`, `structural_boundaries: 252`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 643`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `api: 10`
* *Defense:* `safety: 102`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.86
  * `Choke Point (Betweenness):` 0.001053 | `Ripple Effect (Closeness):` 0.020585
  * `Imports (Out-Degree: 26):` None
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `private/prepare_mesh_manual.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 18.576)
- **Top Global Matches:** file_cluster_1: 18.576, file_cluster_3: 30.099, file_cluster_8: 51.863
- **Magnitude:** 2634.02 | **LOC:** 939 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_mesh_manual` **(Many-Argument Workhorses)** (Impact: 156.7)
    * *Intent:* % PREPARE_MESH_MANUAL is called by PREPARE_MESH and opens a GUI to manually % select points/polygons...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 155.9)
  * `cb_btn_dwn` **(Many-Argument Workhorses)** (Impact: 137.2)
  * `cb_btn_dwn2` **(Many-Argument Workhorses)** (Impact: 137.1)
  * `erase_points2d` **(Compute Cores)** (Impact: 103.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 110`, `args: 29`, `func_start: 33`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 215`, `dead_code: 2`, `fragile_debt: 7`, `unreferenced_by_name: 5`
* *Architecture:* `api: 33`
* *Defense:* `safety: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.028304
  * `Imports (Out-Degree: 7):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ft_databrowser.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.115)
- **Top Global Matches:** file_cluster_6: 7.115, file_cluster_8: 10.658, file_cluster_4: 14.578
- **Magnitude:** 2556.84 | **LOC:** 2391 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **55** in-repo importer(s); blast radius 1.96; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.7%), Guard Balance (formerly Safety Score) (87.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_databrowser` **(Many-Argument Workhorses)** (Impact: 253.7)
    * *Intent:* % FT_DATABROWSER can be used for visual inspection of data. Artifacts that were % detected by artifa...
  * `select_range_cb` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `redraw_cb` **(Many-Argument Workhorses)** (Impact: 32.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `definetrial_cb` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `keypress_cb` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 534 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1797
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 236`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 729`, `dead_code: 14`, `fragile_debt: 21`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 14`
* *Defense:* `safety: 88`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.96
  * `Choke Point (Betweenness):` 0.001286 | `Ripple Effect (Closeness):` 0.017139
  * `Imports (Out-Degree: 38):` None
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `ft_meshrealign.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.426)
- **Top Global Matches:** file_cluster_3: 8.426, file_cluster_8: 16.214, file_cluster_6: 29.111
- **Magnitude:** 2296.56 | **LOC:** 951 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 0.232; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.5%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_meshrealign` **(Many-Argument Workhorses)** (Impact: 418.2)
    * *Intent:* % FT_MESHREALIGN rotates, translates and optionally scales a surface description of % the head or of...
  * `cb_redraw_surface` **(Many-Argument Workhorses)** (Impact: 338.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_keyboard_surface` **(Many-Argument Workhorses)** (Impact: 331.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 309.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_keyboard` **(Many-Argument Workhorses)** (Impact: 163.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 185 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 599
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 77`, `args: 11`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 229`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 11`
* *Defense:* `safety: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.001246
  * `Imports (Out-Degree: 13):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `fileio/ft_read_data.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.349)
- **Top Global Matches:** file_cluster_1: 6.349, file_cluster_3: 48.306, file_cluster_8: 70.104
- **Magnitude:** 2271.58 | **LOC:** 1775 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **95** in-repo importer(s); blast radius 3.066; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.4%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_read_data` **(Many-Argument Workhorses)** (Impact: 288.8)
    * *Intent:* % FT_READ_DATA reads data from a variety of EEG, MEG and other time series data files % and represen...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 506 instances
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 1571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 189`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 559`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `api: 1`
* *Defense:* `safety: 56`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.066
  * `Choke Point (Betweenness):` 0.004414 | `Ripple Effect (Closeness):` 0.07555
  * `Imports (Out-Degree: 81):` None
  * `Imported By (In-Degree: 95):` (Excluded from Brief to save tokens)

### `fileio/ft_read_headshape.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.995)
- **Top Global Matches:** file_cluster_3: 6.995, file_cluster_8: 20.657, file_cluster_6: 33.487
- **Magnitude:** 2167.96 | **LOC:** 1720 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **60** in-repo importer(s); blast radius 2.38; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Complexity Load (formerly Cognitive Load) (74.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_read_headshape` **(Many-Argument Workhorses)** (Impact: 260.4)
    * *Intent:* % FT_READ_HEADSHAPE reads the fiducials and/or the measured headshape and/or meshes % that describe ...
  * `simnibs_labels` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 484 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1503
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 202`, `args: 1`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 535`, `dead_code: 6`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 2`
* *Defense:* `safety: 140`, `doc: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.38
  * `Choke Point (Betweenness):` 0.006095 | `Ripple Effect (Closeness):` 0.063614
  * `Imports (Out-Degree: 39):` None
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `bin/synchronize-private.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.437)
- **Top Global Matches:** file_cluster_2: 6.437, file_cluster_15: 7.19, file_cluster_17: 8.198
- **Magnitude:** 1982.48 | **LOC:** 4226 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.1%), Complexity Load (formerly Cognitive Load) (50.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sync` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* #!/usr/bin/env bash ################################################################################...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 1927
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1919`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compat/obsolete/ft_selectdata_new.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.95)
- **Top Global Matches:** file_cluster_6: 6.95, file_cluster_4: 8.889, file_cluster_15: 16.231
- **Magnitude:** 1809.22 | **LOC:** 1360 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.6%), Guard Balance (formerly Safety Score) (86.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_selectdata_new` **(Many-Argument Workhorses)** (Impact: 311.1)
    * *Intent:* % FT_SELECTDATA_NEW is deprecated, please use FT_SELECTDATA instead. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `makeselection` **(Many-Argument Workhorses)** (Impact: 60.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTIONS %%%%%%%%%%%%...
  * `cellmatselect` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to make a ...
  * `makeselection_cumtapcnt` **(Defensive Guards)** (Impact: 31.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  * `getselection_rpt` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % this should deal with ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 331 instances
* *Memory Alloc (weighted view):* 27
* *State Mutation (weighted view):* 1031
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 230`, `args: 21`, `func_start: 21`
* *Risk/State:* `state_mutation: 369`, `dead_code: 20`, `planned_debt: 1`, `fragile_debt: 18`, `unreferenced_by_name: 2`
* *Architecture:* `api: 21`
* *Defense:* `safety: 67`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utilities/ft_selectdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.296)
- **Top Global Matches:** file_cluster_8: 7.296, file_cluster_6: 11.356, file_cluster_4: 19.656
- **Magnitude:** 1805.7 | **LOC:** 1399 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **142** in-repo importer(s); blast radius 7.633; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.1%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_selectdata` **(Many-Argument Workhorses)** (Impact: 199.9)
    * *Intent:* % FT_SELECTDATA makes a selection in the input data along specific data % dimensions, such as channe...
  * `makeselection` **(Many-Argument Workhorses)** (Impact: 142.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTIONS %%%%%%%%%...
  * `cellmatselect` **(Many-Argument Workhorses)** (Impact: 77.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to make a ...
  * `getselection_spike` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % possible specification...
  * `cellmatmean` **(Defensive Guards)** (Impact: 17.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to take an...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 318 instances
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 1003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 244`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 367`, `dead_code: 21`, `fragile_debt: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 15`
* *Defense:* `safety: 86`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.633
  * `Choke Point (Betweenness):` 0.000321 | `Ripple Effect (Closeness):` 0.109871
  * `Imports (Out-Degree: 12):` None
  * `Imported By (In-Degree: 142):` (Excluded from Brief to save tokens)

### `ft_connectivityanalysis.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.84)
- **Top Global Matches:** file_cluster_3: 6.84, file_cluster_8: 20.596, file_cluster_6: 33.442
- **Magnitude:** 1715.62 | **LOC:** 1372 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); blast radius 1.565; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.0%), Complexity Load (formerly Cognitive Load) (83.7%), Debt Markers (formerly Tech Debt) (82.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_connectivityanalysis` **(Many-Argument Workhorses)** (Impact: 277.4)
    * *Intent:* % FT_CONNECTIVITYANALYSIS computes various measures of connectivity between % MEG/EEG channels or be...
  * `catnan` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* %------------------------------------------------------------------------------- %subfunction to con...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 357 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 1110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 185`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 396`, `dead_code: 1`, `fragile_debt: 16`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`
* *Defense:* `safety: 124`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.565
  * `Choke Point (Betweenness):` 0.000607 | `Ripple Effect (Closeness):` 0.013856
  * `Imports (Out-Degree: 29):` None
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `ft_sourcemovie.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 11.181)
- **Top Global Matches:** file_cluster_1: 11.181, file_cluster_3: 38.203, file_cluster_8: 59.997
- **Magnitude:** 1670.84 | **LOC:** 742 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.164; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_slider` **(Many-Argument Workhorses)** (Impact: 160.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%%%%%%%%%%%...
  * `cb_timer` **(Many-Argument Workhorses)** (Impact: 135.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%%%%%%%%%%%...
  * `cb_playbutton` **(Many-Argument Workhorses)** (Impact: 128.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%%%%%%%%%%%...
  * `cb_quitbutton` **(Many-Argument Workhorses)** (Impact: 124.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%%%%%%%%%%%...
  * `cb_recordbutton` **(Many-Argument Workhorses)** (Impact: 123.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 64`, `args: 10`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 216`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 10`
* *Defense:* `safety: 30`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.164
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000312
  * `Imports (Out-Degree: 7):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ft_sourceanalysis.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.203)
- **Top Global Matches:** file_cluster_1: 6.203, file_cluster_3: 48.316, file_cluster_8: 70.126
- **Magnitude:** 1620.76 | **LOC:** 1344 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **57** in-repo importer(s); blast radius 1.501; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.9%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_sourceanalysis` **(Many-Argument Workhorses)** (Impact: 580.5)
    * *Intent:* % FT_SOURCEANALYSIS performs beamformer dipole analysis on EEG or MEG data % after preprocessing and...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 305 instances
* *State Mutation (weighted view):* 989
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 110`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 379`, `dead_code: 7`, `fragile_debt: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 61`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.501
  * `Choke Point (Betweenness):` 0.000559 | `Ripple Effect (Closeness):` 0.017763
  * `Imports (Out-Degree: 25):` None
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `ft_interactiverealign.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 20.985)
- **Top Global Matches:** file_cluster_3: 20.985, file_cluster_1: 28.068, file_cluster_8: 42.497
- **Magnitude:** 1588.18 | **LOC:** 866 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); blast radius 0.291; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (70.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_creategui` **(Many-Argument Workhorses)** (Impact: 188.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 184.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_camlight` **(Many-Argument Workhorses)** (Impact: 97.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_material` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_cutplane` **(Many-Argument Workhorses)** (Impact: 82.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 100 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 395
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 195`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 18`
* *Defense:* `safety: 60`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.007139
  * `Imports (Out-Degree: 13):` None
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `ft_artifact_zvalue.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.392)
- **Top Global Matches:** file_cluster_3: 15.392, file_cluster_1: 33.691, file_cluster_8: 36.727
- **Magnitude:** 1576.78 | **LOC:** 1185 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); blast radius 0.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_artifact_zvalue` **(Many-Argument Workhorses)** (Impact: 352.3)
    * *Intent:* % FT_ARTIFACT_ZVALUE scans data segments of interest for artifacts, by means of % thresholding the z...
  * `artval_cb` **(Many-Argument Workhorses)** (Impact: 187.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `redraw_cb` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `keyboard_cb` **(Many-Argument Workhorses)** (Impact: 72.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cleanup_cb` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 261 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 846
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 102`, `args: 6`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 324`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`
* *Defense:* `safety: 38`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.632
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.00369
  * `Imports (Out-Degree: 15):` None
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `realtime/online_meg/ft_realtime_headlocalizer.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.871)
- **Top Global Matches:** file_cluster_8: 6.871, file_cluster_6: 12.909, file_cluster_4: 21.482
- **Magnitude:** 1514.46 | **LOC:** 1069 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.235; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%), Complexity Load (formerly Cognitive Load) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `offset2time` **(Many-Argument Workhorses)** (Impact: 208.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that do...
  * `circumcenter` **(Compute Cores)** (Impact: 152.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION which c...
  * `draw_sub` **(Compute Cores)** (Impact: 150.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION which d...
  * `ft_realtime_headlocalizer` **(Many-Argument Workhorses)** (Impact: 148.0)
    * *Intent:* % FT_REALTIME_HEADLOCALIZER is a real-time application for online visualization of % the head positi...
  * `key_sub` **(Compute Cores)** (Impact: 52.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION which h...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 144 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 80`, `args: 18`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 226`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 18`
* *Defense:* `safety: 24`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.235
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.000623
  * `Imports (Out-Degree: 18):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/test_warning_once.m` (MATLAB) | Magnitude: 2.85 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 17, core_var_decl: 14, design_snake_case: 14
- `forward/private/meg_ini.m` (MATLAB) | Magnitude: 137.88 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: core_var_decl: 47, design_snake_case: 47, state_mutation: 35, indent_spaces: 28
- `fileio/private/write_off.m` (MATLAB) | Magnitude: 48.4 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: core_var_decl: 14, design_snake_case: 14, state_mutation: 11, indent_spaces: 11
- `test/test_bug1351.m` (MATLAB) | Magnitude: 1.47 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: debug_prints: 8, state_mutation: 7, core_var_decl: 7, design_snake_case: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/test_ft_determine_units.m` (MATLAB) | Magnitude: 2.36 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 15, core_var_decl: 13, design_snake_case: 13, indent_spaces: 7
- `fileio/private/read_ctf_pos.m` (MATLAB) | Magnitude: 77.02 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 20, core_var_decl: 15, design_snake_case: 15
- `fileio/private/sccn_xdf.m` (MATLAB) | Magnitude: 187.2 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 54, core_var_decl: 31, design_snake_case: 31
- `forward/private/pinvNx2.m` (MATLAB) | Magnitude: 46.48 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 18, scientific: 13, core_var_decl: 11, design_snake_case: 11
- `plotting/private/pinvNx2.m` (MATLAB) | Magnitude: 46.48 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 18, scientific: 13, core_var_decl: 11, design_snake_case: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `realtime/src/acquisition/siemens/src/unixtime.c` (C) | Magnitude: 10.6 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, state_mutation: 5, macros: 4, indent_tabs: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/test_ft_estimate_units.m` (MATLAB) | Magnitude: 0.75 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: safety: 9, indent_spaces: 6, core_var_decl: 4, design_snake_case: 4
- `private/isfunction.m` (MATLAB) | Magnitude: 2.96 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: core_var_decl: 2, design_snake_case: 2, design_short_vars: 2, structural_boundaries: 1
- `forward/private/leadfield_simbio.m` (MATLAB) | Magnitude: 22.88 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, core_var_decl: 6, design_snake_case: 6, state_mutation: 5
- `test/test_pull1604.m` (MATLAB) | Magnitude: 3.79 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: core_var_decl: 23, design_snake_case: 23, state_mutation: 21, time_date_logic: 10
- `test/invalid/failed_bug1988.m` (MATLAB) | Magnitude: 53.84 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 35, core_var_decl: 29, design_snake_case: 29, safety: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `realtime/online_eeg/private/midiOut.c` (C) | Magnitude: 300.86 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 205, branch: 72, state_mutation: 43, core_var_decl: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `fileio/private/read_bti_ascii.m` (MATLAB) | Magnitude: 65.38 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 12, branch: 11, structural_boundaries: 9
- `compat/matlablt2010b/@uint64/abs.c` (C) | Magnitude: 37.96 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 17, state_mutation: 8, branch: 4, core_var_decl: 4
- `realtime/src/acquisition/siemens/python/fakeScanner.py` (PYTHON) | Magnitude: 60.54 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: core_var_decl: 19, state_mutation: 18, indent_tabs: 18, design_camel_case: 13
- `src/mxDeserialize_cpp.cpp` (CPP) | Magnitude: 10.48 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 10, structural_boundaries: 8, indent_spaces: 7, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `fileio/private/read_mayo_mef30.m` (MATLAB) | Magnitude: 96.14 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: core_var_decl: 27, design_snake_case: 27, state_mutation: 25, indent_spaces: 24

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `qsub/qsubget.m` -> Churn: **100.0%** | Cog Load: 78.4202% | Debt: 13.5306%
- `ft_statistics_mvpa.m` -> Churn: **81.91%** | Cog Load: 82.6854% | Debt: 18.6976%
- `plotting/ft_plot_mesh.m` -> Churn: **66.67%** | Cog Load: 85.8326% | Debt: 9.4673%
- `bin/synchronize-private.sh` -> Churn: **61.15%** | Cog Load: 50.1256% | Debt: 0.0%
- `ft_electrodeplacement.m` -> Churn: **60.3%** | Cog Load: 68.6344% | Debt: 12.5951%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ft_electrodeplacement.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 4994.82
- `ft_volumerealign.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 4538.96
- `fileio/ft_read_header.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 4156.1
- `fileio/ft_read_event.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 3511.22
- `ft_meshrealign.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 2296.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `fileio/ft_read_header.m` -> **Severity: 0.94** (Bridge: 0.0094 * Flux: 100.0%)
- `fileio/ft_read_headshape.m` -> **Severity: 0.609** (Bridge: 0.0061 * Flux: 100.0%)
- `ft_preprocessing.m` -> **Severity: 0.483** (Bridge: 0.0048 * Flux: 100.0%)
- `fileio/ft_read_data.m` -> **Severity: 0.441** (Bridge: 0.0044 * Flux: 100.0%)
- `ft_prepare_layout.m` -> **Severity: 0.341** (Bridge: 0.0034 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `compat/matlablt2010b/@uint64/any.m` -> **Severity: 18.194** (Embedded: 0.3005 * Error Risk: 60.5532%)
- `contrib/misc/ft_nonlinearassociation.m` -> **Severity: 16.02** (Embedded: 0.1841 * Error Risk: 87.0192%)
- `compat/matlablt2010b/@uint64/all.m` -> **Severity: 14.956** (Embedded: 0.247 * Error Risk: 60.5532%)
- `compat/matlablt2010b/@uint64/max.m` -> **Severity: 14.579** (Embedded: 0.2523 * Error Risk: 57.7931%)
- `fileio/ft_filetype.m` -> **Severity: 14.132** (Embedded: 0.1438 * Error Risk: 98.2566%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `compat/matlablt2010b/@uint64/any.m` -> **Severity: 6992.4** (Blast Radius: 69.924 * Doc Risk: 100.0%)
- `compat/matlablt2010b/@uint64/all.m` -> **Severity: 2898.5** (Blast Radius: 28.985 * Doc Risk: 100.0%)
- `compat/matlablt2010b/@uint64/max.m` -> **Severity: 2647.2** (Blast Radius: 26.472 * Doc Risk: 100.0%)
- `compat/matlablt2010b/@uint64/abs.m` -> **Severity: 2179.4** (Blast Radius: 21.794 * Doc Risk: 100.0%)
- `utilities/dccnpath.m` -> **Severity: 2060.8** (Blast Radius: 20.608 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3628 literal sites + 7 sites through wrappers = 3635
- **`memory_alloc`:** 4542 literal sites + 16 sites through wrappers = 4558
- **`panics_and_aborts`:** 1264 literal sites + 5 sites through wrappers = 1269

- `FREE` (macro, memory_alloc, primitive): 16 call sites in 5 files -- `realtime/online_eeg/private/midiIn.c`
- `diep` (function, debug_prints, primitive): 5 call sites in 1 files -- `realtime/src/acquisition/jaga/jaga2ft.c`
- `diep` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `realtime/src/acquisition/jaga/jaga2ft.c`
- `issue_warning` (function, debug_prints, primitive): 1 call sites in 1 files -- `test/invalid/failed_bug2225.m`
- `myCleanupFun` (function, debug_prints, primitive): 1 call sites in 1 files -- `realtime/example/ft_realtime_sensysproxy.m`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 84429 call pairs -- scoped 3.3%, unique 13.1%, ambiguous 9.5%, external 74.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| matlab | 81319 | 3.1% | 13.5% | 9.7% | 73.8% |
| cpp | 1690 | 13.2% | 2.7% | 6.4% | 77.8% |
| c | 1343 | 8.0% | 1.8% | 1.5% | 88.8% |
| python | 30 | 3.3% | 0.0% | 0.0% | 96.7% |
| shell | 27 | 11.1% | 0.0% | 0.0% | 88.9% |
| makefile | 20 | 0.0% | 0.0% | 0.0% | 100.0% |

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
