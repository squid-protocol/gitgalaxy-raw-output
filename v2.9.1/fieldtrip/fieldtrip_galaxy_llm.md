# ARCHITECTURAL_BRIEF: fieldtrip
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/fieldtrip/fieldtrip` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 3449 analyzed artifact(s), 290236 LOC.
- **Load-bearing artifact:** `realtime/src/buffer/src/buffer.h` -- 69 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `realtime/src/buffer/src/platform_includes.h` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ft_electrodeplacement.m` at magnitude 6424.62 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 3449 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4569 |
| Total LOC | 290236 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 43.0% |
| Dominant Lang | MATLAB |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7346 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2909 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3962 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 46 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MATLAB | 2955 | 244719 | 85.7% |
| C | 207 | 24533 | 6.0% |
| CPP | 76 | 10134 | 2.2% |
| PLAINTEXT | 65 | 0 | 1.9% |
| MARKDOWN | 64 | 0 | 1.9% |
| JAVA | 37 | 5150 | 1.1% |
| MAKEFILE | 28 | 2093 | 0.8% |
| SHELL | 6 | 2660 | 0.2% |
| PYTHON | 5 | 597 | 0.1% |
| XML | 2 | 0 | 0.1% |
| OBJECTIVE-C | 2 | 317 | 0.1% |
| BATCH | 2 | 33 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `2.828`
> **Composition Archetype:** `Flat Modular Platform` (z +2.83; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 33%, Many-Argument Workhorses Files 30%, Data / Markup / Trivial 11%, Compute Cores Files 8%, Large Core Modules (2) 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3320 | 96.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 129 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4569*

**Composition by Extension & Reason:**
- `.m`: 2299x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Saturation: Line 10 exceeds 500 chars), 7x Excluded (Saturation: Line 12 exceeds 500 chars)
- `no_extension`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 97x Excluded (Binary Format Detected), 4x Unsupported Format (.undeterminable)
- `.mexa64`: 90x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 73x Excluded (Unsupported Extension: '.mexa64'), 35x Excluded (Binary Format Detected)
- `.mexmaci64`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 65x Excluded (Unsupported Extension: '.mexmaci64'), 31x Excluded (Binary Format Detected)
- `.mexw64`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 56x Excluded (Unsupported Extension: '.mexw64'), 30x Excluded (Binary Format Detected)
- `.mexw32`: 64x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 60x Excluded (Unsupported Extension: '.mexw32'), 30x Excluded (Binary Format Detected)
- `.mat`: 124x Excluded (Unsupported Extension: '.mat'), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.mexmaca64`: 75x Excluded (Unsupported Extension: '.mexmaca64'), 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 30x Excluded (Binary Format Detected)
- `.mexglx`: 55x Excluded (Unsupported Extension: '.mexglx'), 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 25x Excluded (Binary Format Detected)
- `.mexmaci`: 55x Excluded (Unsupported Extension: '.mexmaci'), 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 28x Excluded (Binary Format Detected)
- `.txt`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.p`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.p')
- `.c`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 62x Excluded (Explicitly Denied Extension: '.exe')
- `.mexmac`: 31x Excluded (Unsupported Extension: '.mexmac'), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 41.7 | 41.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 83.5 | 94.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.9 | 24.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.8 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.5 | 3.4 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 57.6 | 99.9 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 10.8 | 6.6 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 92.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 14846 | 1508 | 8 | `realtime/src/buffer/src/dmarequest.c` |
| cleanup | 1895 | 696 | 2 | `fileio/private/read_besa_besa.m` |
| guards | 20201 | 2005 | 16 | `fileio/ft_read_event.m` |
| danger | 3115 | 774 | 2 | `test/test_ft_timelockanalysis_new.m` |
| concurrency | 475 | 107 | 0 | `realtime/src/buffer/src/dmarequest.c` |
| connectivity | 6473 | 3201 | 3 | `realtime/src/acquisition/neuromag/include/fiff.h` |
| io | 3314 | 656 | 1 | `fileio/private/read_4d_hdr.m` |
| crypto | 0 | 0 | 0 | - |
| ipc | 401 | 145 | 0 | `realtime/src/buffer/src/socketserver.c` |
| time | 571 | 173 | 0 | `test/invalid/failed_old_specest_vs_oldimplementation.m` |
| serialization | 673 | 383 | 1 | `test/test_ft_freqanalysis.m` |
| regex | 443 | 142 | 0 | `utilities/ft_channelselection.m` |
| events | 127 | 46 | 0 | `realtime/src/acquisition/neuralynx/nlx2ft.cc` |
| tests | 27 | 13 | 0 | `contrib/MOxUnit_fieldtrip/tests/test_moxunit_fieldtrip_test_suite_filtering.m` |
| docs | 1359 | 203 | 0 | `realtime/src/acquisition/siemens/include/nifti1.h` |
| debt | 5691 | 1115 | 4 | `realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java` |
| mutation | 217654 | 3220 | 147 | `bin/synchronize-private.sh` |
| dead_code | 7996 | 3178 | 4 | `realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java` |
| credential | 14 | 9 | 0 | `test/test_bug2096.m` |
| threat | 1321 | 408 | 1 | `realtime/src/acquisition/tmsi/Sadio.h` |
| ml_ai | 5606 | 912 | 4 | `connectivity/ft_connectivity_granger.m` |
| ui | 2956 | 445 | 2 | `test/test_ft_plot_sens.m` |

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

1. **buffer.h** (`realtime/src/buffer/src/buffer.h`) — 69 inbound connections
2. **stdint.h** (`realtime/src/buffer/src/win32/stdint.h`) — 17 inbound connections
3. **platform_includes.h** (`realtime/src/buffer/src/platform_includes.h`) — 16 inbound connections
4. **socketserver.h** (`realtime/src/buffer/src/socketserver.h`) — 11 inbound connections
5. **FtBuffer.h** (`realtime/src/buffer/cpp/FtBuffer.h`) — 11 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **platform_includes.h** (`realtime/src/buffer/src/platform_includes.h`) — 22 outbound dependencies
2. **rfbevent.c** (`src/rfbevent.c`) — 18 outbound dependencies
3. **opengl_client.cc** (`realtime/src/acquisition/siemens/src/opengl_client.cc`) — 18 outbound dependencies
4. **neuromag2ft.c** (`realtime/src/acquisition/neuromag/neuromag2ft.c`) — 16 outbound dependencies
5. **viewer.cc** (`realtime/src/utilities/viewer/viewer.cc`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__global_context__` **(I/O & Config Routines)** (@ `fileio/ft_filetype.m`) -> Impact: **681.4** | LOC: 1268
  * *Intent:* % FT_FILETYPE determines the filetype of many EEG/MEG/MRI data files by % looking at the name, extension and optionally (part of) its contents. % It t...
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
- `ft_read_header` **(Many-Argument Workhorses)** (@ `fileio/ft_read_header.m`) -> Impact: **423.7** | LOC: 1199
  * *Intent:* % FT_READ_HEADER reads header information from a variety of EEG, MEG and other time % series data files and represents the header information in a com...
- `cb_redraw` **(Many-Argument Workhorses)** (@ `ft_electrodeplacement.m`) -> Impact: **422.7** | LOC: 1180
  * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 161 | 82120.66 | 69.62% | 39.31% |
| `fileio/private` | 359 | 58956.6 | 62.18% | 52.86% |
| `private` | 320 | 42103.12 | 54.12% | 56.87% |
| `fileio` | 34 | 26378.22 | 58.06% | 44.22% |
| `utilities` | 93 | 19593.14 | 59.65% | 51.33% |
| `plotting/private` | 90 | 11787.98 | 53.61% | 55.4% |
| `forward/private` | 95 | 11530.14 | 53.52% | 58.36% |
| `utilities/private` | 119 | 11136.98 | 54.96% | 52.89% |
| `plotting` | 32 | 9272.58 | 68.56% | 37.29% |
| `src` | 72 | 7769.46 | 46.38% | 49.03% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `contrib/spike/ft_spike_rate_orituning.m` -> **100.0%** Exposure
- `contrib/spike/private/getdimsiz.m` -> **100.0%** Exposure
- `fileio/private/fetch_url.m` -> **100.0%** Exposure
- `fileio/private/netmeg2grad.m` -> **100.0%** Exposure
- `utilities/ft_affinecoordinates.m` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/scripts/suggest_tests.py` -> **100.0%** Exposure
- `realtime/src/acquisition/siemens/python/fakeScanner.py` -> **100.0%** Exposure
- `realtime/src/buffer/python/FieldTrip.py` -> **100.0%** Exposure
- `realtime/src/buffer/python/addNoise.py` -> **100.0%** Exposure
- `besa2fieldtrip.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `realtime/src/acquisition/openbci/java/src/OpenBCI_ADS1299.java` -> **38** Orphaned Functions | **0** Duplicates
- `test/invalid/failed_ft_sourceanalysis.m` -> **23** Orphaned Functions | **0** Duplicates
- `realtime/src/acquisition/amp/AmpServerClient.cpp` -> **21** Orphaned Functions | **0** Duplicates
- `realtime/src/acquisition/tmsi/Feature.cpp` -> **20** Orphaned Functions | **0** Duplicates
- `realtime/src/acquisition/siemens/src/PixelDataGrabber.cc` -> **17** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `utilities/ft_trackusage.m` -> **99.9999%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `732` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1331` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ft_electrodeplacement.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 6424.62 | **LOC:** 2086 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_help` **(Many-Argument Workhorses)** (Impact: 453.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 422.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_volume` **(Many-Argument Workhorses)** (Impact: 421.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_scatter` **(Many-Argument Workhorses)** (Impact: 375.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_headshape` **(Many-Argument Workhorses)** (Impact: 332.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 341 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 1281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 149`, `args: 33`, `func_start: 34`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 599`, `dead_code: 11`, `fragile_debt: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 34`
* *Defense:* `safety: 42`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_filetype.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 4330.96 | **LOC:** 1873 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Complexity Load (formerly Cognitive Load) (89.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(I/O & Config Routines)** (Impact: 681.4)
    * *Intent:* % FT_FILETYPE determines the filetype of many EEG/MEG/MRI data files by % looking at the name, exten...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 121.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % start determining t...
  * `filetype_true` **(I/O & Config Routines)** (Impact: 45.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that al...
  * `filetype_check_ced_spike6mat` **(I/O & Config Routines)** (Impact: 45.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that ch...
  * `filetype_check_openvibe_mat` **(I/O & Config Routines)** (Impact: 36.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION that ch...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1021 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 3070
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 776`, `structural_boundaries: 66`, `args: 13`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1028`, `dead_code: 4`, `fragile_debt: 10`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 13`
* *Defense:* `safety: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_header.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4143.4 | **LOC:** 3097 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (93.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_read_header` **(Many-Argument Workhorses)** (Impact: 423.7)
    * *Intent:* % FT_READ_HEADER reads header information from a variety of EEG, MEG and other time % series data fi...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 162.7)
    * *Intent:* % FT_READ_HEADER reads header information from a variety of EEG, MEG and other time % series data fi...
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 25.8)
    * *Intent:* % the BIDS sidecar files extend/overrule the information that is present in the file header itself t...
  * `filesize` **(Defensive Guards)** (Impact: 25.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION to dete...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 952 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 3059
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 564`, `structural_boundaries: 338`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1155`, `dead_code: 25`, `planned_debt: 6`, `fragile_debt: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 6`
* *Defense:* `safety: 188`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_geometryplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 4058.76 | **LOC:** 1005 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_geometryplot` **(Many-Argument Workhorses)** (Impact: 228.4)
    * *Intent:* % FT_GEOMETRYPLOT plots objects in 3D, such as sensors, headmodels, sourcemodels, % headshapes, mesh...
  * `cb_creategui` **(Many-Argument Workhorses)** (Impact: 221.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 191.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_toggle` **(Many-Argument Workhorses)** (Impact: 187.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_camlight` **(Many-Argument Workhorses)** (Impact: 186.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 155 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 576
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 74`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 266`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 28`
* *Defense:* `safety: 54`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/read_besa_besa.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3997.88 | **LOC:** 2073 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.265; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.9%)
- **Documentation Coverage:** 76.1905% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_BEVT` **(Many-Argument Workhorses)** (Impact: 344.2)
    * *Intent:* %% EVENT BLOCK FUNCTIONS %% Read event block % BEVT_offset [scalar] - offset of current event block ...
  * `thirdscheme_lookup` **(Many-Argument Workhorses)** (Impact: 274.9)
    * *Intent:* % Lookup table for third scheme % Use persistent variable so lookup table does not need to be recomp...
  * `read_event_tag_base` **(Many-Argument Workhorses)** (Impact: 172.4)
    * *Intent:* % Read data in the COMM event tag block % Loop through all tags in data section while ~feof(fid) && ...
  * `read_event_tag_comm` **(Many-Argument Workhorses)** (Impact: 169.7)
    * *Intent:* % Read data in the COMM event tag block % Loop through all tags in data section while ~feof(fid) && ...
  * `read_event_tag_mark` **(Many-Argument Workhorses)** (Impact: 159.7)
    * *Intent:* % Read data in the MARK event tag block % Loop through all tags in data section while ~feof(fid) && ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 410 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1385
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 256`, `args: 28`, `func_start: 28`
* *Risk/State:* `state_mutation: 565`, `dead_code: 2`, `planned_debt: 10`, `unreferenced_by_name: 2`
* *Architecture:* `io: 130`, `api: 28`, `import: 1`
* *Defense:* `safety: 39`, `doc: 15`, `cleanup: 70`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.mathworks.mlwidgets.io.InterruptibleStreamCopier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_event.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 3511.22 | **LOC:** 2690 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (80.0%), Debt Markers (formerly Tech Debt) (17.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(I/O & Config Routines)** (Impact: 150.5)
    * *Intent:* % FT_READ_EVENT reads all events from an EEG, MEG or other time series dataset and % returns them in...
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 36.5)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 32.1)
    * *Intent:* % check whether there's an event definition in the fif file
  * `ft_read_event` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* % FT_READ_EVENT reads all events from an EEG, MEG or other time series dataset and % returns them in...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 29.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 795 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 2517
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 604`, `structural_boundaries: 611`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 927`, `dead_code: 29`, `fragile_debt: 12`
* *Architecture:* `io: 5`, `api: 1`
* *Defense:* `safety: 223`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_volumerealign.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3304.56 | **LOC:** 2147 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assignweights` **(Many-Argument Workhorses)** (Impact: 400.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `ft_volumerealign` **(Many-Argument Workhorses)** (Impact: 325.2)
    * *Intent:* % FT_VOLUMEREALIGN spatially aligns an anatomical MRI with head coordinates based on % external fidu...
  * `cb_help` **(Many-Argument Workhorses)** (Impact: 183.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 179.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw_ortho` **(Many-Argument Workhorses)** (Impact: 178.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 434 instances
* *High Risk Execution (weighted view):* 10
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1504
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 150`, `args: 18`, `func_start: 17`
* *Risk/State:* `high_risk_execution: 18`, `state_mutation: 636`, `dead_code: 16`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 17`
* *Defense:* `safety: 62`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/ft_checkdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3237.56 | **LOC:** 1911 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 110.3)
  * `freq2raw` **(Compute Cores)** (Impact: 105.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 99.2)
    * *Intent:* % from one bivariate representation to another % nothing to do elseif (strcmp(current, 'full') && st...
  * `timelock2raw` **(Compute Cores)** (Impact: 90.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `fixcsd` **(Defensive Guards)** (Impact: 86.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % represent the cros...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 636 instances
* *Memory Alloc (weighted view):* 39
* *State Mutation (weighted view):* 1978
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 265`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 706`, `dead_code: 34`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* `api: 19`
* *Defense:* `safety: 122`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utilities/ft_checkdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3237.56 | **LOC:** 1911 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 110.3)
  * `freq2raw` **(Compute Cores)** (Impact: 105.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 99.2)
    * *Intent:* % from one bivariate representation to another % nothing to do elseif (strcmp(current, 'full') && st...
  * `timelock2raw` **(Compute Cores)** (Impact: 90.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between dat...
  * `fixcsd` **(Defensive Guards)** (Impact: 86.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % represent the cros...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 636 instances
* *Memory Alloc (weighted view):* 39
* *State Mutation (weighted view):* 1978
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 265`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 706`, `dead_code: 34`, `planned_debt: 1`, `fragile_debt: 9`
* *Architecture:* `api: 19`
* *Defense:* `safety: 122`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_prepare_layout.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2985.48 | **LOC:** 1843 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sens2lay` **(Many-Argument Workhorses)** (Impact: 349.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % conve...
  * `opto2lay` **(Many-Argument Workhorses)** (Impact: 200.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % conve...
  * `readlay` **(Many-Argument Workhorses)** (Impact: 182.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % read ...
  * `ft_prepare_layout` **(Many-Argument Workhorses)** (Impact: 148.4)
    * *Intent:* % FT_PREPARE_LAYOUT loads or creates a 2-D layout of the channel locations. This % layout is require...
  * `shiftxy` **(Many-Argument Workhorses)** (Impact: 109.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION % shift...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 442 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 229`, `args: 12`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 605`, `dead_code: 9`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 11`
* *Defense:* `safety: 135`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_sourceplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2662.58 | **LOC:** 2164 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 173.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_help` **(Many-Argument Workhorses)** (Impact: 160.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `ft_sourceplot` **(Many-Argument Workhorses)** (Impact: 132.2)
    * *Intent:* % FT_SOURCEPLOT plots functional source reconstruction data on slices or on a surface, % optionally ...
  * `cb_keyboard` **(Many-Argument Workhorses)** (Impact: 62.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 39.5)
    * *Intent:* % FT_SOURCEPLOT plots functional source reconstruction data on slices or on a surface, % optionally ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 496 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 1635
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 523`, `structural_boundaries: 252`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 643`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `api: 10`
* *Defense:* `safety: 102`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_databrowser.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2556.84 | **LOC:** 2391 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (91.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_databrowser` **(Many-Argument Workhorses)** (Impact: 253.7)
    * *Intent:* % FT_DATABROWSER can be used for visual inspection of data. Artifacts that were % detected by artifa...
  * `select_range_cb` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 41.2)
    * *Intent:* % FT_DATABROWSER can be used for visual inspection of data. Artifacts that were % detected by artifa...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 35.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % add the component to...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 534 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1797
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 236`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 729`, `dead_code: 39`, `fragile_debt: 21`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 14`
* *Defense:* `safety: 88`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `private/prepare_mesh_manual.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2369.02 | **LOC:** 939 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_btn_dwn2` **(Many-Argument Workhorses)** (Impact: 173.1)
  * `prepare_mesh_manual` **(Many-Argument Workhorses)** (Impact: 156.7)
    * *Intent:* % PREPARE_MESH_MANUAL is called by PREPARE_MESH and opens a GUI to manually % select points/polygons...
  * `cb_btn_dwn` **(Many-Argument Workhorses)** (Impact: 137.2)
  * `erase_points2d` **(Compute Cores)** (Impact: 128.8)
  * `assign_points3d` **(Many-Argument Workhorses)** (Impact: 106.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 160 instances
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 110`, `args: 29`, `func_start: 33`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 215`, `dead_code: 3`, `fragile_debt: 7`, `unreferenced_by_name: 7`
* *Architecture:* `api: 33`
* *Defense:* `safety: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_data.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 2271.58 | **LOC:** 1775 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_read_data` **(Many-Argument Workhorses)** (Impact: 288.8)
    * *Intent:* % FT_READ_DATA reads data from a variety of EEG, MEG and other time series data files % and represen...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 103.5)
    * *Intent:* % FT_READ_DATA reads data from a variety of EEG, MEG and other time series data files % and represen...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 17.1)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 12.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert the channel...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 11.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % convert between 3-D...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 506 instances
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 1571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 189`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 559`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `api: 1`
* *Defense:* `safety: 56`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/ft_read_headshape.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2167.96 | **LOC:** 1720 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (74.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_read_headshape` **(Many-Argument Workhorses)** (Impact: 260.4)
    * *Intent:* % FT_READ_HEADSHAPE reads the fiducials and/or the measured headshape and/or meshes % that describe ...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 64.5)
    * *Intent:* % FT_READ_HEADSHAPE reads the fiducials and/or the measured headshape and/or meshes % that describe ...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 13.2)
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 12.6)
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* % there are multiple types of meshes % this also allows for specifications like 'tri+tet' if hastri ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 484 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1503
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 202`, `args: 1`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 535`, `dead_code: 11`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 2`
* *Defense:* `safety: 140`, `doc: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_meshrealign.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 2011.56 | **LOC:** 951 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_meshrealign` **(Many-Argument Workhorses)** (Impact: 418.2)
    * *Intent:* % FT_MESHREALIGN rotates, translates and optionally scales a surface description of % the head or of...
  * `cb_redraw_surface` **(Many-Argument Workhorses)** (Impact: 234.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_keyboard_surface` **(Many-Argument Workhorses)** (Impact: 225.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 218.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cb_keyboard` **(Many-Argument Workhorses)** (Impact: 68.7)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 187 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 77`, `args: 11`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 229`, `dead_code: 13`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 11`
* *Defense:* `safety: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/synchronize-private.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1982.48 | **LOC:** 4226 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.1%), Complexity Load (formerly Cognitive Load) (50.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sync` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* #!/usr/bin/env bash ################################################################################...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 1927
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1919`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compat/obsolete/ft_selectdata_new.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1809.22 | **LOC:** 1360 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (96.6%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `state_mutation: 369`, `dead_code: 32`, `planned_debt: 1`, `fragile_debt: 18`, `unreferenced_by_name: 2`
* *Architecture:* `api: 21`
* *Defense:* `safety: 67`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utilities/ft_selectdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1805.7 | **LOC:** 1399 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (97.1%), Test Surface (formerly Verification) (80.0%)
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
  * `__global_context__` **(I/O & Config Routines)** (Impact: 31.1)
    * *Intent:* % FT_SELECTDATA makes a selection in the input data along specific data % dimensions, such as channe...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 318 instances
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 1003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 244`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 367`, `dead_code: 38`, `fragile_debt: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 15`
* *Defense:* `safety: 86`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_connectivityanalysis.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1715.62 | **LOC:** 1372 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (83.7%), Debt Markers (formerly Tech Debt) (83.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_connectivityanalysis` **(Many-Argument Workhorses)** (Impact: 277.4)
    * *Intent:* % FT_CONNECTIVITYANALYSIS computes various measures of connectivity between % MEG/EEG channels or be...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 127.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 36.5)
    * *Intent:* % FT_CONNECTIVITYANALYSIS computes various measures of connectivity between % MEG/EEG channels or be...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 16.8)
    * *Intent:* % check if jackknife is required % do nothing elseif hasrpt && dojack && ~ismember(cfg.method, {'wpl...
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 13.7)
    * *Intent:* % based on powindx switch dtype case {'freq' 'freqmvar'} if isfield(data, 'labelcmb') && ~isstruct(p...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 357 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 1110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 185`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 396`, `dead_code: 10`, `fragile_debt: 16`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`
* *Defense:* `safety: 124`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_interactiverealign.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1677.28 | **LOC:** 866 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Complexity Load (formerly Cognitive Load) (70.6%), Debt Markers (formerly Tech Debt) (28.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cb_creategui` **(Many-Argument Workhorses)** (Impact: 188.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_redraw` **(Many-Argument Workhorses)** (Impact: 122.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_camlight` **(Many-Argument Workhorses)** (Impact: 101.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_material` **(Many-Argument Workhorses)** (Impact: 100.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
  * `cb_cutplane` **(Many-Argument Workhorses)** (Impact: 99.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % SUBFUNCTION %%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 104 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 195`, `dead_code: 2`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 18`
* *Defense:* `safety: 60`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_sourceanalysis.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 1620.76 | **LOC:** 1344 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_sourceanalysis` **(Many-Argument Workhorses)** (Impact: 580.5)
    * *Intent:* % FT_SOURCEANALYSIS performs beamformer dipole analysis on EEG or MEG data % after preprocessing and...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 18.1)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* % the fields in the dip structure might be more recent than those in the sourcemodel structure sourc...
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* % remember the trialinfo
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* % remove the precomputed leadfields from the output source (if present) source = removefields(source...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 305 instances
* *State Mutation (weighted view):* 989
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 110`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 379`, `dead_code: 15`, `fragile_debt: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 61`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ft_artifact_zvalue.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1512.68 | **LOC:** 1185 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ft_artifact_zvalue` **(Many-Argument Workhorses)** (Impact: 352.3)
    * *Intent:* % FT_ARTIFACT_ZVALUE scans data segments of interest for artifacts, by means of % thresholding the z...
  * `artval_cb` **(Many-Argument Workhorses)** (Impact: 156.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `keyboard_cb` **(Many-Argument Workhorses)** (Impact: 77.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `redraw_cb` **(Many-Argument Workhorses)** (Impact: 45.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
  * `cleanup_cb` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 260 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 844
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 102`, `args: 6`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 324`, `dead_code: 9`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`
* *Defense:* `safety: 38`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fileio/private/read_nervus_header.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1447.88 | **LOC:** 1000 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.3%)
- **Documentation Coverage:** 68.4211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_nervus_header_dynamicpackets` **(Many-Argument Workhorses)** (Impact: 118.8)
  * `read_nervus_header_staticpackets` **(Compute Cores)** (Impact: 77.6)
    * *Intent:* % Get StaticPackets structure and Channel IDS fseek(h, 172,'bof'); NrStaticPackets = fread(h,1, 'uin...
  * `compareTsInfoPackets` **(Compute Cores)** (Impact: 40.6)
  * `read_nervus_header_events` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* %% Get events - Andrei Barborica, Dec 2015 % Find sequence of events, that are stored in the section...
  * `read_nervus_header` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* % read_nervus_header Returns header information from Nicolet file. % % FILENAME is the file name of ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 262 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 91`, `args: 19`, `func_start: 19`
* *Risk/State:* `state_mutation: 466`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 92`, `api: 19`
* *Defense:* `safety: 4`, `doc: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `realtime/src/acquisition/openbci/openbci2ft.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1447.24 | **LOC:** 1097 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.265; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (82.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 372.4)
  * `iniHandler` **(Many-Argument Workhorses)** (Impact: 311.6)
  * `interpret24bitAsInt32` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* ; #endif
  * `interpret16bitAsInt32` **(Compute Cores)** (Impact: 4.8)
  * `serialWriteSlow` **(Parameter Forwarders)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 205 instances
* *State Mutation (weighted view):* 723
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 21`, `args: 10`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 6`, `state_mutation: 313`, `dead_code: 7`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` buffer.h, ini.h, math.h, platform.h, serial.h, signal.h, socketserver.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `qsub/qsubget.m` -> Churn: **100.0%** | Cog Load: 78.4202% | Debt: 17.7664%
- `ft_statistics_mvpa.m` -> Churn: **81.91%** | Cog Load: 82.6854% | Debt: 22.0331%
- `bin/synchronize-private.sh` -> Churn: **69.1%** | Cog Load: 50.1256% | Debt: 0.0%
- `plotting/ft_plot_mesh.m` -> Churn: **66.67%** | Cog Load: 85.8326% | Debt: 10.5571%
- `ft_electrodeplacement.m` -> Churn: **60.3%** | Cog Load: 68.6344% | Debt: 17.0919%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ft_electrodeplacement.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 6424.62
- `fileio/ft_read_event.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 3511.22
- `ft_volumerealign.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 3304.56
- `ft_meshrealign.m` -> **Robert Oostenveld** (100.0% isolated ownership) | Magnitude: 2011.56
- `utilities/ft_selectdata.m` -> **Jan-Mathijs Schoffelen** (100.0% isolated ownership) | Magnitude: 1805.7

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `realtime/src/buffer/src/buffer.h` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 21.2639%)
- `realtime/src/buffer/cpp/FtBuffer.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `realtime/src/buffer/cpp/OnlineDataManager.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `realtime/src/buffer/src/buffer.h` -> **Severity: 1.502** (Embedded: 0.0195 * Error Risk: 76.8525%)
- `realtime/src/buffer/src/win32/stdint.h` -> **Severity: 0.968** (Embedded: 0.0163 * Error Risk: 59.3131%)
- `realtime/src/buffer/src/message.h` -> **Severity: 0.653** (Embedded: 0.0125 * Error Risk: 52.1748%)
- `realtime/src/buffer/cpp/FtBuffer.h` -> **Severity: 0.433** (Embedded: 0.0044 * Error Risk: 98.812%)
- `realtime/src/buffer/cpp/SimpleStorage.h` -> **Severity: 0.28** (Embedded: 0.0031 * Error Risk: 90.7207%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `realtime/src/buffer/cpp/FtBuffer.h` -> **Severity: 143.1** (Blast Radius: 1.431 * Doc Risk: 100.0%)
- `realtime/src/buffer/cpp/StringServer.h` -> **Severity: 106.7** (Blast Radius: 1.067 * Doc Risk: 100.0%)
- `realtime/src/acquisition/tmsi/RTDevice.h` -> **Severity: 105.3** (Blast Radius: 1.053 * Doc Risk: 100.0%)
- `realtime/src/acquisition/gtec/Device.hpp` -> **Severity: 97.4** (Blast Radius: 0.974 * Doc Risk: 100.0%)
- `realtime/src/buffer/cpp/TemplateVectorMath.h` -> **Severity: 88.7** (Blast Radius: 0.887 * Doc Risk: 100.0%)

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
