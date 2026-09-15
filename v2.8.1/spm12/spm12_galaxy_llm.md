# ARCHITECTURAL_BRIEF: spm12
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spm/spm12` |
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
| Total Artifacts | 5154 |
| Analyzed Artifacts (Scanned) | 4230 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 924 |
| Total LOC | 397971 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 82.1% |
| Dominant Lang | MATLAB |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7876 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2609 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.099 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MATLAB | 4029 | 359762 | 95.2% |
| C | 137 | 37055 | 3.2% |
| MARKDOWN | 22 | 0 | 0.5% |
| PLAINTEXT | 20 | 0 | 0.5% |
| MAKEFILE | 9 | 445 | 0.2% |
| CPP | 4 | 225 | 0.1% |
| OBJECTIVE-C | 3 | 234 | 0.1% |
| SHELL | 2 | 97 | 0.0% |
| HTML | 2 | 86 | 0.0% |
| JAVA | 1 | 33 | 0.0% |
| CSS | 1 | 34 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +2.48; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 42%, Compute Cores Files 20%, Data / Markup / Trivial 12%, Defensive Guards Files 8%, I/O & Config Routines Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4188 | 99.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 42 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 924*

**Composition by Extension & Reason:**
- `.png`: 230x Excluded (Explicitly Denied Extension: '.png')
- `.m`: 68x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 77 exceeds 500 chars), 4x Packed Payload Guard (Impossible Density: 4.60 hits/line)
- `.mexa64`: 80x Excluded (Unsupported Extension: '.mexa64')
- `.mexw64`: 80x Excluded (Unsupported Extension: '.mexw64')
- `.mexmaci64`: 79x Excluded (Unsupported Extension: '.mexmaci64')
- `.mexw32`: 75x Excluded (Unsupported Extension: '.mexw32')
- `.mat`: 42x Excluded (Unsupported Extension: '.mat')
- `.tex`: 39x Excluded (Unsupported Extension: '.tex'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nii`: 37x Excluded (Unsupported Extension: '.nii')
- `.p`: 26x Excluded (Unsupported Extension: '.p')
- `.pdf`: 19x Excluded (Explicitly Denied Extension: '.pdf')
- `.lut`: 13x Excluded (Unsupported Extension: '.lut')
- `.sfp`: 13x Excluded (Unsupported Extension: '.sfp')
- `.fig`: 11x Excluded (Explicitly Denied Extension: '.fig')
- `.gii`: 6x Excluded (Unsupported Extension: '.gii')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 51.6 | 61.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 84.8 | 96.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 47.2 | 62.2 | 62.2 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.0 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 92.9 | 3.7 | 3.4 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 88.0 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.3 | 10.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 94.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 85.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19909 | 2136 | 7 | `@gifti/private/miniz.c` |
| cleanup | 2045 | 745 | 1 | `external/fieldtrip/fileio/private/read_besa_besa.m` |
| guards | 24998 | 2593 | 15 | `@nifti/private/nifti_stats.c` |
| danger | 4128 | 1196 | 3 | `src/spm_diffeo.c` |
| concurrency | 145 | 58 | 0 | `toolbox/DAiSS/bf_group_batch.m` |
| connectivity | 7452 | 3999 | 3 | `@gifti/private/miniz.c` |
| io | 4198 | 710 | 2 | `external/fieldtrip/fileio/private/read_4d_hdr.m` |
| crypto | 0 | 0 | 0 | - |
| ipc | 132 | 67 | 0 | `external/fieldtrip/src/rfbevent.c` |
| time | 382 | 146 | 0 | `tests/test_spm_openmp.m` |
| serialization | 926 | 411 | 0 | `config/spm_run_dcm_bms.m` |
| regex | 455 | 121 | 0 | `matlabbatch/cfg_ui_util.m` |
| events | 4 | 3 | 0 | `help/index.html` |
| tests | 277 | 50 | 0 | `tests/test_spm_jsonread.m` |
| docs | 861 | 132 | 0 | `@nifti/private/nifti_stats.c` |
| debt | 5883 | 1329 | 4 | `external/ctf/setCTFDataBalance.m` |
| mutation | 300613 | 4096 | 167 | `@nifti/private/nifti_stats.c` |
| dead_code | 8973 | 3990 | 4 | `spm_orthviews.m` |
| credential | 355 | 5 | 0 | `man/batch/face_single_subject.m` |
| threat | 1936 | 441 | 1 | `@nifti/private/nifti_stats.c` |
| ml_ai | 10270 | 1594 | 7 | `@nifti/private/nifti_stats.c` |
| ui | 3997 | 660 | 3 | `toolbox/FieldMap/FieldMap.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `external/fieldtrip/fileio/private/read_4d_hdr.m` (Hits: 158)
- `external/fieldtrip/fileio/private/read_besa_besa.m` (Hits: 130)
- `spm_ecat2nifti.m` (Hits: 123)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **spm_mapping.h** (`src/spm_mapping.h`) — 10 inbound connections
2. **spm_mex.h** (`src/spm_mex.h`) — 9 inbound connections
3. **Makefile.var** (`src/Makefile.var`) — 8 inbound connections
4. **shoot_boundary.h** (`src/shoot_boundary.h`) — 8 inbound connections
5. **geometry.h** (`external/fieldtrip/src/geometry.h`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rfbevent.c** (`external/fieldtrip/src/rfbevent.c`) — 18 outbound dependencies
2. **file2mat.c** (`@file_array/private/file2mat.c`) — 14 outbound dependencies
3. **spm_diffeo.c** (`src/spm_diffeo.c`) — 11 outbound dependencies
4. **spm_mapping.c** (`src/spm_mapping.c`) — 11 outbound dependencies
5. **mat2file.c** (`@file_array/private/mat2file.c`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addcolouredblobs` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **807.9** | LOC: 1659
  * *Intent:* %========================================================================== % function addcolouredblobs(handle, xyz, t, mat, colour, name) %==========...
- `addtruecolourimage` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **786.6** | LOC: 1604
  * *Intent:* %========================================================================== % function addtruecolourimage(handle,fname,colourmap,prop,mx,mn) %========...
- `addblobs` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **768.6** | LOC: 1704
  * *Intent:* %========================================================================== % function addblobs(handle, xyz, t, mat, name) %==========================...
- `writeCTFds` **(Many-Argument Workhorses)** (@ `external/ctf/writeCTFds.m`) -> Impact: **722.8** | LOC: 1711
  * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % % % This program creates datasets that can be analyzed by CTF sof...
- `ConvertSpectroscopy` **(Many-Argument Workhorses)** (@ `spm_dicom_convert.m`) -> Impact: **713.0** | LOC: 1228
  * *Intent:* %========================================================================== % function fnames = ConvertSpectroscopy(Headers, RootDirectory, format, Ou...
- `specify_image` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **650.4** | LOC: 1749
  * *Intent:* %========================================================================== % function H = specify_image(img, h) %====================================...
- `spm_sp` **(Compute Cores)** (@ `spm_sp.m`) -> Impact: **637.8** | LOC: 1415
  * *Intent:* % Orthogonal (design) matrix space setting & manipulation % FORMAT varargout = spm_spc(action,varargin) % % This function computes the different proje...
- `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (@ `spm_eeg_review_callbacks.m`) -> Impact: **626.4** | LOC: 1527
- `addcolouredimage` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **623.5** | LOC: 1629
  * *Intent:* %========================================================================== % function addcolouredimage(handle, fname,colour) %=======================...
- `addCTFtrial` **(Many-Argument Workhorses)** (@ `external/ctf/addCTFtrial.m`) -> Impact: **608.7** | LOC: 1273
  * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % % % This program creates datasets that can be analyzed by CTF sof...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 743 | 167433.0 | 57.62% | 45.59% |
| `toolbox/DEM` | 264 | 32753.9 | 42.81% | 40.8% |
| `src` | 72 | 30834.26 | 49.23% | 21.45% |
| `config` | 117 | 25627.44 | 35.83% | 43.09% |
| `toolbox/dcm_meeg` | 107 | 17112.16 | 53.08% | 50.64% |
| `@nifti/private` | 21 | 11904.68 | 53.03% | 45.85% |
| `@gifti/private` | 18 | 10798.14 | 66.71% | 47.61% |
| `toolbox/DAiSS` | 74 | 10532.7 | 50.59% | 32.67% |
| `matlabbatch` | 23 | 10331.48 | 59.55% | 46.03% |
| `toolbox/FieldMap` | 37 | 9316.2 | 52.5% | 39.22% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `external/fieldtrip/fileio/private/fetch_url.m` -> **100.0%** Exposure
- `external/fieldtrip/fileio/private/netmeg2grad.m` -> **100.0%** Exposure
- `external/fieldtrip/fileio/private/dimlength.m` -> **99.9991%** Exposure
- `external/fieldtrip/private/dimlength.m` -> **99.9991%** Exposure
- `external/fieldtrip/utilities/private/dimlength.m` -> **99.9991%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `@file_array/cat.m` -> **100.0%** Exposure
- `@file_array/isnan.m` -> **100.0%** Exposure
- `@file_array/private/datatypes.m` -> **100.0%** Exposure
- `@file_array/private/dtype.m` -> **100.0%** Exposure
- `@file_array/size.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `spm_eeg_inv_imag_api.m` -> **25** Orphaned Functions | **0** Duplicates
- `spm_eeg_inv_visu3D_api.m` -> **25** Orphaned Functions | **0** Duplicates
- `toolbox/dcm_meeg/spm_api_erp.m` -> **20** Orphaned Functions | **0** Duplicates
- `src/shoot_diffeo3d.c` -> **18** Orphaned Functions | **0** Duplicates
- `tests/test_spm_openmp.m` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `external/fieldtrip/utilities/ft_trackusage.m` -> **99.9999%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `370` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `475` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `external/fieldtrip/utilities/private/fixsource.m` (MATLAB) -> Cumulative Risk: **762.7**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.37)
- **Magnitude:** 0.3 | **LOC:** 422 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9792%)
- **Heaviest Functions:** `fixsource` (Compute Cores, Impact: 105.4), `__global_context__` (I/O & Config Routines, Impact: 2.5), `Anonymous_Block` (Defensive Guards, Impact: 2.2)

### 2. `external/fieldtrip/fileio/private/dimlength.m` (MATLAB) -> Cumulative Risk: **693.69**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.67)
- **Magnitude:** 0.31 | **LOC:** 232 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9991%)
- **Heaviest Functions:** `dimlength` (Many-Argument Workhorses, Impact: 80.6), `__global_context__` (I/O & Config Routines, Impact: 35.5), `Anonymous_Block` (Defensive Guards, Impact: 4.3)

### 3. `external/fieldtrip/private/dimlength.m` (MATLAB) -> Cumulative Risk: **693.69**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.67)
- **Magnitude:** 0.31 | **LOC:** 232 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9991%)
- **Heaviest Functions:** `dimlength` (Many-Argument Workhorses, Impact: 80.6), `__global_context__` (I/O & Config Routines, Impact: 35.5), `Anonymous_Block` (Defensive Guards, Impact: 4.3)

### 4. `external/fieldtrip/utilities/private/dimlength.m` (MATLAB) -> Cumulative Risk: **693.69**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.67)
- **Magnitude:** 0.31 | **LOC:** 232 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9991%)
- **Heaviest Functions:** `dimlength` (Many-Argument Workhorses, Impact: 80.6), `__global_context__` (I/O & Config Routines, Impact: 35.5), `Anonymous_Block` (Defensive Guards, Impact: 4.3)

### 5. `external/fieldtrip/connectivity/private/sfactorization_wilson.m` (MATLAB) -> Cumulative Risk: **692.88**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.47)
- **Magnitude:** 0.24 | **LOC:** 252 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.8445%)
- **Heaviest Functions:** `sfactorization_wilson` (Many-Argument Workhorses, Impact: 36.7), `Anonymous_Block` (I/O & Config Routines, Impact: 8.0), `Anonymous_Block` (I/O & Config Routines, Impact: 7.1)

### 6. `external/fieldtrip/utilities/ft_selectdata.m` (MATLAB) -> Cumulative Risk: **689.63**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.02)
- **Magnitude:** 1.74 | **LOC:** 1334 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.4754%)
- **Heaviest Functions:** `ft_selectdata` (Many-Argument Workhorses, Impact: 192.1), `makeselection` (Many-Argument Workhorses, Impact: 136.6), `cellmatselect` (Many-Argument Workhorses, Impact: 77.2)

### 7. `matlabbatch/@cfg_repeat/harvest.m` (MATLAB) -> Cumulative Risk: **689.12**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.55)
- **Magnitude:** 152.5 | **LOC:** 103 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.4641%)
- **Heaviest Functions:** `harvest` (Many-Argument Workhorses, Impact: 72.2)

### 8. `spm_jobman.m` (MATLAB) -> Cumulative Risk: **684.85**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.23)
- **Magnitude:** 637.64 | **LOC:** 551 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.9857%), Cognitive Load (87.4873%)
- **Heaviest Functions:** `spm_jobman` (Compute Cores, Impact: 78.8), `load_jobs` (Defensive Guards, Impact: 64.1), `fill_run_job` (Many-Argument Workhorses, Impact: 44.5)

### 9. `external/fieldtrip/src/ft_getopt.c` (C) -> Cumulative Risk: **684.11**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.91)
- **Magnitude:** 0.13 | **LOC:** 127 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.3081%)
- **Heaviest Functions:** `mexFunction` (Many-Argument Workhorses, Impact: 73.8)

### 10. `external/fieldtrip/ft_databrowser.m` (MATLAB) -> Cumulative Risk: **677.37**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.21)
- **Magnitude:** 2.2 | **LOC:** 2165 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6886%)
- **Heaviest Functions:** `ft_databrowser` (Many-Argument Workhorses, Impact: 239.9), `__global_context__` (I/O & Config Routines, Impact: 45.2), `select_range_cb` (Many-Argument Workhorses, Impact: 38.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `spm_orthviews.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 16980.34 | **LOC:** 2292 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5876%), Tech Debt (8.7245%)
**Top Internal Functions/Classes:**
  * `addcolouredblobs` **(Many-Argument Workhorses)** (Impact: 807.9)
    * *Intent:* %========================================================================== % function addcolouredbl...
  * `addtruecolourimage` **(Many-Argument Workhorses)** (Impact: 786.6)
    * *Intent:* %========================================================================== % function addtruecolour...
  * `addblobs` **(Many-Argument Workhorses)** (Impact: 768.6)
    * *Intent:* %========================================================================== % function addblobs(hand...
  * `specify_image` **(Many-Argument Workhorses)** (Impact: 650.4)
    * *Intent:* %========================================================================== % function H = specify_i...
  * `addcolouredimage` **(Many-Argument Workhorses)** (Impact: 623.5)
    * *Intent:* %========================================================================== % function addcolouredim...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 467 instances
* *State Mutation (weighted view):* 1572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 317`, `args: 37`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 638`, `dead_code: 44`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 44`
* *Defense:* `safety: 94`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `@nifti/private/nifti_stats.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 10600.72 | **LOC:** 11278 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2827%), Tech Debt (7.8696%)
**Top Internal Functions/Classes:**
  * `gaminv` **(Many-Argument Workhorses)** (Impact: 198.0)
    * *Intent:* } /* END */ /***=====================================================================***/
  * `cdfbin` **(Many-Argument Workhorses)** (Impact: 189.2)
    * *Intent:* #undef tol #undef atol #undef zero #undef inf #undef one } /* END */ /***===========================...
  * `cdfbet` **(Many-Argument Workhorses)** (Impact: 180.0)
    * *Intent:* } /* END */ /***=====================================================================***/
  * `cdfnbn` **(Many-Argument Workhorses)** (Impact: 179.8)
    * *Intent:* #undef tol #undef atol #undef zero #undef inf } /* END */ /***======================================...
  * `E0000` **(Many-Argument Workhorses)** (Impact: 171.1)
    * *Intent:* #undef maxit #undef eps #undef r2pi #undef nhalf #undef dennor } /* END */ /***=====================...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2158 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 6726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1170`, `structural_boundaries: 557`, `args: 214`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 2410`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 10`, `import: 6`
* *Defense:* `doc: 149`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ctype.h, math.h, nifti1.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `@gifti/private/miniz.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 8482.92 | **LOC:** 8891 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.5174%), Tech Debt (8.5076%)
**Top Internal Functions/Classes:**
  * `tinfl_decompress` **(Many-Argument Workhorses)** (Impact: 357.1)
  * `mz_zip_writer_add_mem_ex_v2` **(Many-Argument Workhorses)** (Impact: 331.8)
  * `mz_zip_writer_add_cfile` **(Many-Argument Workhorses)** (Impact: 278.2)
    * *Intent:* #ifndef MINIZ_NO_STDIO
  * `mz_zip_writer_add_from_zip_reader` **(Many-Argument Workhorses)** (Impact: 142.1)
    * *Intent:* /* TODO: This func is now pretty freakin complex due to zip64, split it up? */
  * `mz_zip_reader_extract_to_callback` **(Many-Argument Workhorses)** (Impact: 134.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 1220 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 4030
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1580`, `structural_boundaries: 974`, `args: 332`, `func_start: 177`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 1590`, `dead_code: 9`, `planned_debt: 13`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 290`, `import: 13`
* *Defense:* `safety: 207`, `doc: 4`, `immutability_locks: 311`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.431
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000236
  * `Imports (Out-Degree: 0):` assert.h, stddef.h, stdio.h, stdlib.h, string.h, stat.h, utime.h, time.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spm_dicom_convert.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 8325.1 | **LOC:** 1982 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.4689%), Tech Debt (11.0883%)
**Top Internal Functions/Classes:**
  * `ConvertSpectroscopy` **(Many-Argument Workhorses)** (Impact: 713.0)
    * *Intent:* %========================================================================== % function fnames = Conv...
  * `WriteSpectroscopyVolume` **(Many-Argument Workhorses)** (Impact: 604.7)
    * *Intent:* %========================================================================== % function fname = Write...
  * `SelectLastGuff` **(Many-Argument Workhorses)** (Impact: 371.4)
    * *Intent:* %========================================================================== % function [standard, gu...
  * `CheckFields` **(Many-Argument Workhorses)** (Impact: 369.1)
    * *Intent:* %========================================================================== % function ok = CheckFie...
  * `SelectTomographicImages` **(Compute Cores)** (Impact: 339.2)
    * *Intent:* %========================================================================== % function [images,guff]...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 427 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 1365
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 283`, `args: 32`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 511`, `dead_code: 38`, `unreferenced_by_name: 5`
* *Architecture:* `io: 17`, `api: 31`
* *Defense:* `safety: 129`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/dcm_meeg/spm_api_erp.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 5945.38 | **LOC:** 1554 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.6953%), Tech Debt (63.6079%)
**Top Internal Functions/Classes:**
  * `load_Callback` **(Many-Argument Workhorses)** (Impact: 488.4)
    * *Intent:* %-DCM files and directories: Load and save %========================================================...
  * `spm_api_erp` **(Compute Cores)** (Impact: 364.7)
    * *Intent:* % SPM_API_ERP Application M-file for spm_api_erp.fig % FIG = SPM_API_ERP launch spm_api_erp GUI. % S...
  * `save_Callback` **(Many-Argument Workhorses)** (Impact: 347.9)
    * *Intent:* % --- Executes on button press in save. % ----------------------------------------------------------...
  * `reset_Callback` **(Many-Argument Workhorses)** (Impact: 344.4)
    * *Intent:* % store selections in DCM % ------------------------------------------------------------------------...
  * `Datafile_Callback` **(Many-Argument Workhorses)** (Impact: 331.4)
    * *Intent:* % Data selection and design %=======================================================================...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 168 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 577
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 176`, `args: 27`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 241`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 6`, `api: 27`
* *Defense:* `safety: 104`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matlabbatch/cfg_getfile.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4866.22 | **LOC:** 1553 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.9584%), Tech Debt (14.0964%)
**Top Internal Functions/Classes:**
  * `click_dir_box` **(Many-Argument Workhorses)** (Impact: 283.8)
    * *Intent:* %======================================================================= %==========================...
  * `select_rec1` **(Many-Argument Workhorses)** (Impact: 256.4)
    * *Intent:* %======================================================================= %==========================...
  * `click_file_box` **(Many-Argument Workhorses)** (Impact: 248.3)
    * *Intent:* %======================================================================= %==========================...
  * `select` **(Many-Argument Workhorses)** (Impact: 238.7)
    * *Intent:* %======================================================================= %==========================...
  * `listfiles` **(Many-Argument Workhorses)** (Impact: 238.4)
    * *Intent:* %======================================================================= %==========================...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 240 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 176`, `args: 56`, `func_start: 39`
* *Risk/State:* `state_mutation: 314`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 39`, `concurrency: 1`
* *Defense:* `safety: 60`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_mesh_render.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 3900.56 | **LOC:** 871 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.2905%), Tech Debt (10.0106%)
**Top Internal Functions/Classes:**
  * `myMenuCallback` **(Many-Argument Workhorses)** (Impact: 221.8)
    * *Intent:* %==========================================================================
  * `getOptions` **(Compute Cores)** (Impact: 211.6)
    * *Intent:* %==========================================================================
  * `myPostCallback` **(Many-Argument Workhorses)** (Impact: 208.2)
    * *Intent:* %==========================================================================
  * `myInflate` **(Many-Argument Workhorses)** (Impact: 196.1)
    * *Intent:* %==========================================================================
  * `myCCLabel` **(Many-Argument Workhorses)** (Impact: 189.8)
    * *Intent:* %==========================================================================
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 452
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 126`, `args: 25`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 162`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 24`
* *Defense:* `safety: 63`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_eeg_review_callbacks.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 3642.56 | **LOC:** 2030 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.8879%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (Impact: 626.4)
  * `updateDisp` **(Many-Argument Workhorses)** (Impact: 483.8)
    * *Intent:* %% Main update display % This function updates the display of the data and events. if ~exist('flags'...
  * `psd_defineMenuEvent` **(Many-Argument Workhorses)** (Impact: 227.8)
    * *Intent:* %% Define menu event % This funcion defines the uicontextmenu associated to the selected events. % A...
  * `switchBC` **(Compute Cores)** (Impact: 202.1)
    * *Intent:* %% Switch 'bad channel' status
  * `getUItable` **(Defensive Guards)** (Impact: 161.4)
    * *Intent:* % try,str{7} = ['Time onset: ',num2str(D.timeOnset),' sec'];end %% extracting data from spm_uitable ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 483 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 1643
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 259`, `args: 11`, `func_start: 8`
* *Risk/State:* `state_mutation: 677`
* *Architecture:* `io: 2`, `api: 8`
* *Defense:* `safety: 142`, `doc: 26`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_deformations.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2892.92 | **LOC:** 818 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.4868%), Tech Debt (9.4791%)
**Top Internal Functions/Classes:**
  * `spm_deformations` **(Compute Cores)** (Impact: 275.6)
    * *Intent:* % Various deformation field utilities % FORMAT out = spm_deformations(job) % job - a job created via...
  * `get_comp` **(Compute Cores)** (Impact: 253.8)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
  * `get_job` **(Compute Cores)** (Impact: 249.6)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
  * `get_sn2def` **(Compute Cores)** (Impact: 238.3)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
  * `get_def` **(Compute Cores)** (Impact: 215.3)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 252 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 834
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 92`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 330`, `dead_code: 15`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 16`
* *Defense:* `safety: 40`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_results_nidm.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 2658.74 | **LOC:** 1922 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.8947%), Tech Debt (9.8363%)
**Top Internal Functions/Classes:**
  * `spm_results_nidm` **(Many-Argument Workhorses)** (Impact: 174.3)
    * *Intent:* % Export SPM stats results using the Neuroimaging Data Model (NIDM) % FORMAT [nidmfile, prov] = spm_...
  * `xsdfloat` **(Compute Cores)** (Impact: 172.0)
    * *Intent:* %========================================================================== % function v = xsdfloat(...
  * `coordspace` **(Many-Argument Workhorses)** (Impact: 131.1)
    * *Intent:* %========================================================================== % function id = coordspa...
  * `make_ROI` **(Many-Argument Workhorses)** (Impact: 121.1)
    * *Intent:* %========================================================================== % function make_ROI(fnam...
  * `img2nii` **(Many-Argument Workhorses)** (Impact: 114.0)
    * *Intent:* %========================================================================== % function img2nii(img,n...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 292 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 955
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 155`, `args: 24`, `func_start: 19`
* *Risk/State:* `state_mutation: 371`, `dead_code: 16`, `unreferenced_by_name: 4`
* *Architecture:* `io: 8`, `api: 19`
* *Defense:* `safety: 60`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_sp.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2545.82 | **LOC:** 1416 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (26.6607%)
**Top Internal Functions/Classes:**
  * `spm_sp` **(Compute Cores)** (Impact: 637.8)
    * *Intent:* % Orthogonal (design) matrix space setting & manipulation % FORMAT varargout = spm_spc(action,vararg...
  * `sf_create` **(Compute Cores)** (Impact: 95.2)
    * *Intent:* %======================================================================= %- S U B - F U N C T I O N ...
  * `sf_set` **(Compute Cores)** (Impact: 85.9)
    * *Intent:* %======================================================================= x = sf_create; x.X = X; %--...
  * `sf_transp` **(Compute Cores)** (Impact: 79.0)
    * *Intent:* %======================================================================= % %- Tranpspose the space :...
  * `sf_tol` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* %======================================================================= x(abs(x) < t) = 0; function...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 155 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 473
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 180`, `args: 31`, `func_start: 32`
* *Risk/State:* `state_mutation: 163`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 32`
* *Defense:* `safety: 44`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_dartel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2514.74 | **LOC:** 1565 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.4579%), Tech Debt (9.0284%)
**Top Internal Functions/Classes:**
  * `dartel_mexFunction` **(Many-Argument Workhorses)** (Impact: 107.4)
  * `iteration` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `exp_mexFunction` **(Many-Argument Workhorses)** (Impact: 54.9)
  * `smalldef_objfun_mn` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `initialise_objfun_mn` **(Many-Argument Workhorses)** (Impact: 41.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 449 instances
* *State Mutation (weighted view):* 1859
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 29`, `args: 24`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 961`, `unreferenced_by_name: 2`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` math.h, mex.h, shoot_boundary.h, shoot_diffeo3d.h, shoot_optim3d.h, shoot_regularisers.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matlabbatch/cfg_util.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2340.1 | **LOC:** 1862 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1623%), Tech Debt (10.7929%)
**Top Internal Functions/Classes:**
  * `local_addtojob` **(Many-Argument Workhorses)** (Impact: 229.3)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_cd` **(Compute Cores)** (Impact: 105.6)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_delfromjob` **(Many-Argument Workhorses)** (Impact: 105.0)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_compactjob` **(Compute Cores)** (Impact: 101.8)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_gencode` **(Many-Argument Workhorses)** (Impact: 76.2)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 407 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 28
* *State Mutation (weighted view):* 1307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 318`, `structural_boundaries: 193`, `args: 27`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 493`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 15`, `api: 18`
* *Defense:* `safety: 82`, `doc: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_regularisers.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2042.48 | **LOC:** 1659 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.8227%), Tech Debt (10.5297%)
**Top Internal Functions/Classes:**
  * `relax_all` **(Many-Argument Workhorses)** (Impact: 73.9)
    * *Intent:* /************************************************************************************************/ /...
  * `relax_be` **(Many-Argument Workhorses)** (Impact: 71.6)
    * *Intent:* /************************************************************************************************/ /...
  * `sumsq` **(Many-Argument Workhorses)** (Impact: 52.8)
    * *Intent:* * \param[in] s[4] Parameter of the membrane energy (penalizes * elements of the Jacobian matrix -> 1...
  * `relax_le` **(Many-Argument Workhorses)** (Impact: 52.8)
    * *Intent:* * smoothness) * \param[in] s[5] Parameter of the bending energy (penalizes * elements of the Hessian...
  * `relax_me` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* /************************************************************************************************/ /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 383 instances
* *State Mutation (weighted view):* 1609
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 12`, `args: 12`, `func_start: 11`
* *Risk/State:* `state_mutation: 843`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `doc: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.h, shoot_boundary.h, spm_mex.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spm_diffeo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1974.02 | **LOC:** 1180 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.4782%), Tech Debt (8.6936%)
**Top Internal Functions/Classes:**
  * `mexFunction` **(Many-Argument Workhorses)** (Impact: 173.5)
    * *Intent:* #include<string.h>
  * `comp_mexFunction` **(Many-Argument Workhorses)** (Impact: 98.8)
  * `pushc_grads_mexFunction` **(Many-Argument Workhorses)** (Impact: 87.1)
  * `fmg3_mexFunction` **(Many-Argument Workhorses)** (Impact: 85.3)
  * `push_mexFunction` **(Many-Argument Workhorses)** (Impact: 69.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 238 instances
* *State Mutation (weighted view):* 794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 33`, `args: 26`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 318`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` math.h, mex.h, shoot_boundary.h, shoot_bsplines.h, shoot_dartel.h, shoot_diffeo3d.h, shoot_multiscale.h, shoot_optim3d.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_eeg_inv_imag_api.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1942.58 | **LOC:** 484 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.9526%), Tech Debt (99.6392%)
**Top Internal Functions/Classes:**
  * `CreateMeshes_Callback` **(Many-Argument Workhorses)** (Impact: 113.0)
    * *Intent:* % MAIN FUNCTIONS FOR MODEL SEPCIFICATION AND INVERSION %============================================...
  * `Reg2tem_Callback` **(Many-Argument Workhorses)** (Impact: 108.6)
    * *Intent:* % --- Executes on button press in Reg2tem. %--------------------------------------------------------...
  * `DataReg_Callback` **(Many-Argument Workhorses)** (Impact: 108.2)
    * *Intent:* % --- Executes on button press in Data Reg. %-------------------------------------------------------...
  * `Forward_Callback` **(Many-Argument Workhorses)** (Impact: 107.9)
    * *Intent:* % --- Executes on button press in Forward Model. %--------------------------------------------------...
  * `Inverse_Callback` **(Many-Argument Workhorses)** (Impact: 107.5)
    * *Intent:* % --- Executes on button press in Invert. %---------------------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 46`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 61`, `unreferenced_by_name: 25`
* *Architecture:* `io: 1`, `api: 28`
* *Defense:* `safety: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_eeg_inv_visu3D_api.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1877.74 | **LOC:** 823 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.8312%), Tech Debt (92.619%)
**Top Internal Functions/Classes:**
  * `spm_eeg_inv_visu3D_api` **(Compute Cores)** (Impact: 130.2)
    * *Intent:* % SPM_EEG_INV_VISU3D_API M-file for spm_eeg_inv_visu3D_api.fig % - FIG = SPM_EEG_INV_VISU3D_API laun...
  * `UpDate_Display_SRCS` **(Many-Argument Workhorses)** (Impact: 100.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%...
  * `UpDate_Display_SENS` **(Many-Argument Workhorses)** (Impact: 79.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % UPDATE SENSOR LEVEL DI...
  * `DataFile_Callback` **(Many-Argument Workhorses)** (Impact: 72.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % LOAD DATA FILE %%%%%%%...
  * `LoadData_Callback` **(Many-Argument Workhorses)** (Impact: 72.0)
    * *Intent:* % --- Executes on button press in LoadData.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 62`, `args: 30`, `func_start: 30`
* *Risk/State:* `state_mutation: 160`, `dead_code: 1`, `unreferenced_by_name: 25`
* *Architecture:* `api: 30`
* *Defense:* `safety: 32`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/DEM/spm_MDP_VB_XX.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1869.52 | **LOC:** 1607 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.4573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `spm_forwards` **(Many-Argument Workhorses)** (Impact: 253.7)
    * *Intent:* % auxillary functions %========================================================================== % ...
  * `spm_backwards` **(Many-Argument Workhorses)** (Impact: 161.9)
    * *Intent:* % Backwards smoothing to evaluate posterior over initial states %-----------------------------------...
  * `spm_log` **(Compute Cores)** (Impact: 88.7)
    * *Intent:* % log of numeric array plus a small constant %------------------------------------------------------...
  * `spm_norm` **(Compute Cores)** (Impact: 88.4)
    * *Intent:* % normalisation of a probability transition matrix (columns) %--------------------------------------...
  * `spm_MDP_VB_VOX` **(Many-Argument Workhorses)** (Impact: 83.3)
    * *Intent:* % FORMAT L = spm_MDP_VB_VOX(MDP,L,t) % returns likelihoods from voice recognition (and articulates r...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 258 instances
* *State Mutation (weighted view):* 822
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 230`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 306`, `dead_code: 7`
* *Architecture:* `io: 2`, `api: 11`
* *Defense:* `safety: 93`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_diffeo3d.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1866.82 | **LOC:** 1268 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.0749%), Tech Debt (33.6455%)
**Top Internal Functions/Classes:**
  * `pushpull` **(Many-Argument Workhorses)** (Impact: 76.0)
    * *Intent:* #define TINY 5e-2f
  * `pushc_grads` **(Many-Argument Workhorses)** (Impact: 74.6)
    * *Intent:* /* This should perhaps be tidied up and generalised in line with the pushpull function */
  * `grad1` **(Many-Argument Workhorses)** (Impact: 61.7)
    * *Intent:* #define LOG(x) (((x)>0) ? log(x+0.001): -6.9078)
  * `composition_stuff` **(Many-Argument Workhorses)** (Impact: 61.0)
    * *Intent:* /* * Composition operations, possibly along with Jacobian matrices. * Done using B(A) = U(A) + A, wh...
  * `def2jac_neuman` **(Many-Argument Workhorses)** (Impact: 46.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 330 instances
* *State Mutation (weighted view):* 1363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 29`, `args: 26`, `func_start: 23`
* *Risk/State:* `state_mutation: 703`, `unreferenced_by_name: 18`
* *Architecture:* `api: 21`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` math.h, shoot_boundary.h, shoot_expm3.h, shoot_optim3d.h, spm_mex.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_FcUtil.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1756.54 | **LOC:** 934 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (12.6266%)
**Top Internal Functions/Classes:**
  * `spm_FcUtil` **(Compute Cores)** (Impact: 373.3)
    * *Intent:* % Contrast utilities % FORMAT varargout = spm_FcUtil(action,varargin) %_____________________________...
  * `sf_FconFields` **(Compute Cores)** (Impact: 91.3)
    * *Intent:* %======================================================================= %==========================...
  * `sf_MinFcFields` **(Compute Cores)** (Impact: 82.0)
    * *Intent:* %======================================================================= % used internally. Minimum ...
  * `sf_IsFcon` **(Compute Cores)** (Impact: 78.6)
    * *Intent:* %======================================================================= % yes_no = spm_FcUtil('IsFc...
  * `sf_IsSet` **(Compute Cores)** (Impact: 75.0)
    * *Intent:* %======================================================================= % used internally; To be se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 143`, `args: 18`, `func_start: 20`
* *Risk/State:* `state_mutation: 109`, `dead_code: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 20`
* *Defense:* `safety: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/FieldMap/pm_segment.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1619.82 | **LOC:** 705 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.3317%), Tech Debt (14.8183%)
**Top Internal Functions/Classes:**
  * `pm_segment` **(Many-Argument Workhorses)** (Impact: 195.2)
    * *Intent:* % Segment an MR image into Gray, White & CSF. % % FORMAT VO = pm_segment(PF,PG,flags) % PF - name(s)...
  * `display_graphics` **(Many-Argument Workhorses)** (Impact: 136.0)
    * *Intent:* %======================================================================= %==========================...
  * `affine_transform` **(Many-Argument Workhorses)** (Impact: 133.5)
    * *Intent:* %======================================================================= %==========================...
  * `get_affine_mapping` **(Many-Argument Workhorses)** (Impact: 104.5)
    * *Intent:* %======================================================================= %==========================...
  * `get_bp` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* %======================================================================= %==========================...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 97`, `args: 19`, `func_start: 19`
* *Risk/State:* `state_mutation: 223`, `unreferenced_by_name: 3`
* *Architecture:* `api: 19`
* *Defense:* `safety: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/DEM/spm_MDP_VB_X.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1592.8 | **LOC:** 1675 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.1498%), Tech Debt (8.9026%)
**Top Internal Functions/Classes:**
  * `spm_MDP_VB_X` **(Many-Argument Workhorses)** (Impact: 193.3)
    * *Intent:* % active inference and learning using variational message passing % FORMAT [MDP] = spm_MDP_VB_X(MDP,...
  * `spm_log` **(Compute Cores)** (Impact: 101.1)
    * *Intent:* % auxillary functions %========================================================================== % ...
  * `spm_MDP_VB_VOX` **(Many-Argument Workhorses)** (Impact: 81.3)
    * *Intent:* % FORMAT L = spm_MDP_VB_VOX(MDP,L,t) % returns likelihoods from voice recognition (and articulates r...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 70.2)
    * *Intent:* % Variational updates (skip to t = T in HMM mode) %=================================================...
  * `spm_norm` **(Defensive Guards)** (Impact: 39.8)
    * *Intent:* % normalisation of a probability transition matrix (columns) %--------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 257`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 336`, `dead_code: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 9`
* *Defense:* `safety: 112`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/DARTEL/tbx_cfg_dartel.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1585.78 | **LOC:** 1369 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.8319%), Tech Debt (8.6565%)
**Top Internal Functions/Classes:**
  * `tbx_cfg_dartel` **(Compute Cores)** (Impact: 216.9)
    * *Intent:* % Configuration file for toolbox 'Dartel Tools' %___________________________________________________...
  * `vout_initial_import` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* %dartel.num = [0 Inf]; %_______________________________________________________________________ % %_...
  * `check_dartel_template` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* %_______________________________________________________________________ %__________________________...
  * `vout_dartel_template` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* %_______________________________________________________________________ %__________________________...
  * `vout_dartel_warp` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* %_______________________________________________________________________ %__________________________...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 254 instances
* *State Mutation (weighted view):* 1217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 33`, `args: 13`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 709`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_dicom_header.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1582.36 | **LOC:** 530 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6036%), Tech Debt (15.8081%)
**Top Internal Functions/Classes:**
  * `ReadDicom` **(Many-Argument Workhorses)** (Impact: 318.6)
    * *Intent:* %========================================================================== % function [Header, Byte...
  * `spm_dicom_header` **(Many-Argument Workhorses)** (Impact: 306.4)
    * *Intent:* % Read header information from a DICOM file % FORMAT Header = spm_dicom_header(DicomFilename, DicomD...
  * `ReadSQ` **(Many-Argument Workhorses)** (Impact: 203.4)
    * *Intent:* %========================================================================== % function [Header, Byte...
  * `ReadTag` **(Many-Argument Workhorses)** (Impact: 150.5)
    * *Intent:* %========================================================================== % function Tag = ReadTag...
  * `DecodeCSA` **(Many-Argument Workhorses)** (Impact: 54.6)
    * *Intent:* %========================================================================== % function t = DecodeCSA...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 150 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 464
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 84`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 164`, `dead_code: 6`, `unreferenced_by_name: 3`
* *Architecture:* `io: 72`, `api: 7`
* *Defense:* `safety: 26`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/OldNorm/spm_write_sn.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1519.04 | **LOC:** 559 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (19.0651%)
**Top Internal Functions/Classes:**
  * `spm_write_sn` **(Many-Argument Workhorses)** (Impact: 215.7)
    * *Intent:* % Write out warped images % FORMAT VO = spm_write_sn(V,prm,flags,msk) % V - Images to transform (fil...
  * `affine_transform` **(Many-Argument Workhorses)** (Impact: 194.4)
    * *Intent:* %========================================================================== %-function VO = affine_t...
  * `nonlin_transform` **(Many-Argument Workhorses)** (Impact: 168.2)
    * *Intent:* %========================================================================== %-function VO = nonlin_t...
  * `make_hdr_struct` **(Many-Argument Workhorses)** (Impact: 95.9)
    * *Intent:* %========================================================================== %-function VO = make_hdr...
  * `modulate` **(Many-Argument Workhorses)** (Impact: 87.2)
    * *Intent:* %========================================================================== %-function VO = modulate...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 63`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 151`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 11`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Makefile.var` -> **Severity: 0.144** (Embedded: 0.0019 * Error Risk: 75.9317%)
- `src/jsmn.h` -> **Severity: 0.027** (Embedded: 0.0005 * Error Risk: 56.3934%)
- `@gifti/private/miniz.c` -> **Severity: 0.023** (Embedded: 0.0002 * Error Risk: 96.646%)
- `src/Simplify.h` -> **Severity: 0.022** (Embedded: 0.0002 * Error Risk: 93.3559%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `@gifti/private/miniz.c` -> **Severity: 43.1** (Blast Radius: 0.431 * Doc Risk: 100.0%)
- `src/Simplify.h` -> **Severity: 43.1** (Blast Radius: 0.431 * Doc Risk: 100.0%)
- `@file_array/cat.m` -> **Severity: 23.3** (Blast Radius: 0.233 * Doc Risk: 100.0%)
- `@file_array/ctranspose.m` -> **Severity: 23.3** (Blast Radius: 0.233 * Doc Risk: 100.0%)
- `@file_array/disp.m` -> **Severity: 23.3** (Blast Radius: 0.233 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
