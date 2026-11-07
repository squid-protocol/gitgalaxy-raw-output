# ARCHITECTURAL_BRIEF: spm12
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spm/spm12` |
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
- **Scope:** 2601 analyzed artifact(s), 238302 LOC.
- **Load-bearing artifact:** `@meeg/isempty.m` -- 768 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `@file_array/private/file2mat.c` -- pulls in 14 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `spm_orthviews.m` at magnitude 18930.74 (structural weight, not risk).
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
| Total Artifacts | 5154 |
| Analyzed Artifacts (Scanned) | 2601 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2553 |
| Total LOC | 238302 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.5% |
| Dominant Lang | MATLAB |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4518 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1714 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.9558 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 136 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MATLAB | 2492 | 205824 | 95.8% |
| C | 84 | 31157 | 3.2% |
| PLAINTEXT | 9 | 0 | 0.3% |
| MAKEFILE | 7 | 413 | 0.3% |
| MARKDOWN | 2 | 0 | 0.1% |
| SHELL | 2 | 97 | 0.1% |
| HTML | 2 | 86 | 0.1% |
| CPP | 2 | 691 | 0.1% |
| CSS | 1 | 34 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 2601 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 40%, Data / Markup / Trivial 14%, Compute Cores Files 13%, Large Core Modules (2) 11%, Large Core Modules 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2590 | 99.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2553*

**Composition by Extension & Reason:**
- `.m`: 1649x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2126 LOC), 1x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `.png`: 230x Excluded (Explicitly Denied Extension: '.png')
- `.mexa64`: 40x Excluded (Unsupported Extension: '.mexa64'), 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mexw64`: 40x Excluded (Unsupported Extension: '.mexw64'), 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mexmaci64`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 39x Excluded (Unsupported Extension: '.mexmaci64')
- `.mexw32`: 40x Excluded (Unsupported Extension: '.mexw32'), 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mat`: 41x Excluded (Unsupported Extension: '.mat'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tex`: 40x Excluded (Unsupported Extension: '.tex')
- `.nii`: 37x Excluded (Unsupported Extension: '.nii')
- `no_extension`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.p`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pdf`: 19x Excluded (Explicitly Denied Extension: '.pdf')
- `.lut`: 13x Excluded (Unsupported Extension: '.lut')
- `.sfp`: 13x Excluded (Unsupported Extension: '.sfp')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 47.0 | 56.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.4 | 67.3 | 72.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.4 | 36.8 | 37.8 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.3 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 92.9 | 3.8 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 84.9 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 88.5 | 3.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 77.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6140 | 1216 | 6 | `spm_preproc8.m` |
| cleanup | 816 | 331 | 1 | `toolbox/Longitudinal/spm_groupwise_ls.m` |
| guards | 13016 | 1441 | 12 | `@nifti/private/nifti_stats.c` |
| danger | 2663 | 761 | 3 | `src/spm_diffeo.c` |
| concurrency | 121 | 42 | 0 | `toolbox/DAiSS/bf_group_batch.m` |
| connectivity | 4754 | 2413 | 3 | `@gifti/private/miniz.c` |
| io | 1475 | 444 | 1 | `spm_ecat2nifti.m` |
| crypto | 0 | 0 | 0 | - |
| ipc | 34 | 20 | 0 | `@xmltree/convert.m` |
| time | 232 | 75 | 0 | `tests/test_spm_openmp.m` |
| serialization | 865 | 373 | 1 | `config/spm_run_dcm_bms.m` |
| regex | 168 | 42 | 0 | `matlabbatch/cfg_ui_util.m` |
| events | 3 | 2 | 0 | `help/index.html` |
| tests | 274 | 47 | 0 | `tests/test_spm_jsonread.m` |
| docs | 586 | 88 | 0 | `@nifti/private/nifti_stats.c` |
| debt | 2794 | 755 | 3 | `spm_check_installation.m` |
| mutation | 180216 | 2517 | 162 | `@nifti/private/nifti_stats.c` |
| dead_code | 3541 | 2364 | 2 | `spm_eeg_prep_ui.m` |
| credential | 354 | 4 | 0 | `man/batch/face_single_subject.m` |
| threat | 4 | 2 | 0 | `toolbox/MEEGtools/spm_eeg_headplot.m` |
| ml_ai | 6395 | 1043 | 5 | `@nifti/private/nifti_stats.c` |
| ui | 3279 | 574 | 4 | `toolbox/FieldMap/FieldMap.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.75**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spm_ecat2nifti.m` (Hits: 123)
- `spm_dicom_header.m` (Hits: 72)
- `compat/spm_read_hdr.m` (Hits: 53)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **isempty.m** (`@meeg/isempty.m`) — 768 inbound connections
2. **numel.m** (`@file_array/numel.m`) — 765 inbound connections
3. **find.m** (`@xmltree/find.m`) — 460 inbound connections
4. **spm_figure.m** (`spm_figure.m`) — 351 inbound connections
5. **plot.m** (`@gifti/plot.m`) — 349 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **file2mat.c** (`@file_array/private/file2mat.c`) — 14 outbound dependencies
2. **spm_diffeo.c** (`src/spm_diffeo.c`) — 11 outbound dependencies
3. **spm_mapping.c** (`src/spm_mapping.c`) — 11 outbound dependencies
4. **mat2file.c** (`@file_array/private/mat2file.c`) — 9 outbound dependencies
5. **miniz.c** (`@gifti/private/miniz.c`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addcolouredblobs` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **911.1** | LOC: 1659
  * *Intent:* %========================================================================== % function addcolouredblobs(handle, xyz, t, mat, colour, name) %==========...
- `addtruecolourimage` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **881.9** | LOC: 1604
  * *Intent:* %========================================================================== % function addtruecolourimage(handle,fname,colourmap,prop,mx,mn) %========...
- `addblobs` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **866.6** | LOC: 1704
  * *Intent:* %========================================================================== % function addblobs(handle, xyz, t, mat, name) %==========================...
- `ConvertSpectroscopy` **(Many-Argument Workhorses)** (@ `spm_dicom_convert.m`) -> Impact: **713.0** | LOC: 1228
  * *Intent:* %========================================================================== % function fnames = ConvertSpectroscopy(Headers, RootDirectory, format, Ou...
- `WriteSpectroscopyVolume` **(Many-Argument Workhorses)** (@ `spm_dicom_convert.m`) -> Impact: **710.0** | LOC: 1218
  * *Intent:* %========================================================================== % function fname = WriteSpectroscopyVolume(Headers, RootDirectory, format,...
- `addcolouredimage` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **697.5** | LOC: 1629
  * *Intent:* %========================================================================== % function addcolouredimage(handle, fname,colour) %=======================...
- `specify_image` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **650.4** | LOC: 1749
  * *Intent:* %========================================================================== % function H = specify_image(img, h) %====================================...
- `spm_sp` **(Many-Argument Workhorses)** (@ `spm_sp.m`) -> Impact: **637.8** | LOC: 1415
  * *Intent:* % Orthogonal (design) matrix space setting & manipulation % FORMAT varargout = spm_spc(action,varargin) % % This function computes the different proje...
- `addimage` **(Many-Argument Workhorses)** (@ `spm_orthviews.m`) -> Impact: **631.3** | LOC: 1679
  * *Intent:* %========================================================================== % function addimage(handle, fname) %======================================...
- `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (@ `spm_eeg_review_callbacks.m`) -> Impact: **626.4** | LOC: 1527

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 750 | 173126.32 | 57.53% | 29.31% |
| `toolbox/DEM` | 272 | 33739.54 | 43.16% | 25.9% |
| `src` | 72 | 30831.26 | 48.42% | 17.0% |
| `config` | 119 | 27588.7 | 36.06% | 22.61% |
| `toolbox/dcm_meeg` | 108 | 17224.16 | 53.3% | 33.19% |
| `@nifti/private` | 21 | 11890.58 | 52.9% | 28.41% |
| `@gifti/private` | 18 | 10738.24 | 66.67% | 30.77% |
| `matlabbatch` | 24 | 10546.26 | 59.69% | 30.89% |
| `toolbox/DAiSS` | 74 | 10536.2 | 50.59% | 20.69% |
| `toolbox/FieldMap` | 38 | 9614.34 | 51.57% | 27.18% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `spm_eeg_read_bsa.m` -> **99.9925%** Exposure
- `src/spm_getdata.c` -> **99.9925%** Exposure
- `matlabbatch/cfg_job.m` -> **99.8629%** Exposure
- `@nifti/Contents.m` -> **99.8499%** Exposure
- `spm_eeg_inv_imag_api.m` -> **99.6922%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `@file_array/cat.m` -> **100.0%** Exposure
- `@file_array/isnan.m` -> **100.0%** Exposure
- `@file_array/private/datatypes.m` -> **100.0%** Exposure
- `@file_array/private/dtype.m` -> **100.0%** Exposure
- `@file_array/size.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `spm_eeg_inv_imag_api.m` -> **26** Orphaned Functions | **0** Duplicates
- `spm_eeg_inv_visu3D_api.m` -> **24** Orphaned Functions | **0** Duplicates
- `toolbox/dcm_meeg/spm_api_erp.m` -> **20** Orphaned Functions | **0** Duplicates
- `src/shoot_diffeo3d.c` -> **18** Orphaned Functions | **0** Duplicates
- `tests/test_spm_openmp.m` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `198` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `296` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `spm_orthviews.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 14.278)
- **Top Global Matches:** file_cluster_1: 14.278, file_cluster_3: 34.577, file_cluster_8: 56.376
- **Magnitude:** 18930.74 | **LOC:** 2292 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **48** in-repo importer(s); blast radius 1.024; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addcolouredblobs` **(Many-Argument Workhorses)** (Impact: 911.1)
    * *Intent:* %========================================================================== % function addcolouredbl...
  * `addtruecolourimage` **(Many-Argument Workhorses)** (Impact: 881.9)
    * *Intent:* %========================================================================== % function addtruecolour...
  * `addblobs` **(Many-Argument Workhorses)** (Impact: 866.6)
    * *Intent:* %========================================================================== % function addblobs(hand...
  * `addcolouredimage` **(Many-Argument Workhorses)** (Impact: 697.5)
    * *Intent:* %========================================================================== % function addcolouredim...
  * `specify_image` **(Many-Argument Workhorses)** (Impact: 650.4)
    * *Intent:* %========================================================================== % function H = specify_i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 469 instances
* *State Mutation (weighted view):* 1576
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 317`, `args: 37`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 638`, `dead_code: 42`
* *Architecture:* `io: 1`, `api: 44`
* *Defense:* `safety: 94`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.006187 | `Ripple Effect (Closeness):` 0.138194
  * `Imports (Out-Degree: 32):` None
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `@nifti/private/nifti_stats.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.682)
- **Top Global Matches:** file_cluster_6: 6.682, file_cluster_4: 10.677, file_cluster_8: 15.517
- **Magnitude:** 10587.92 | **LOC:** 11278 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.143; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%)
- **Documentation Coverage:** 6.1361% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gaminv` **(Many-Argument Workhorses)** (Impact: 198.0)
    * *Intent:* } /* END */ /***=====================================================================***/
  * `cdfbin` **(Many-Argument Workhorses)** (Impact: 189.2)
    * *Intent:* #undef tol #undef atol #undef zero #undef inf #undef one } /* END */ /***===========================...
  * `cdfbet` **(Many-Argument Workhorses)** (Impact: 180.0)
    * *Intent:* } /* END */ /***=====================================================================***/
  * `cdfnbn` **(Many-Argument Workhorses)** (Impact: 179.8)
    * *Intent:* #undef tol #undef atol #undef zero #undef inf } /* END */ /***======================================...
  * `E0000` **(Many-Argument Workhorses)** (Impact: 167.4)
    * *Intent:* #undef maxit #undef eps #undef r2pi #undef nhalf #undef dennor } /* END */ /***=====================...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2158 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 6726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1162`, `structural_boundaries: 557`, `args: 214`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 2410`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 10`, `import: 6`
* *Defense:* `doc: 149`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000385
  * `Imports (Out-Degree: 1):` ctype.h, math.h, nifti1.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spm_dicom_convert.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 13.749)
- **Top Global Matches:** file_cluster_1: 13.749, file_cluster_3: 35.332, file_cluster_8: 57.114
- **Magnitude:** 8803.9 | **LOC:** 1982 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConvertSpectroscopy` **(Many-Argument Workhorses)** (Impact: 713.0)
    * *Intent:* %========================================================================== % function fnames = Conv...
  * `WriteSpectroscopyVolume` **(Many-Argument Workhorses)** (Impact: 710.0)
    * *Intent:* %========================================================================== % function fname = Write...
  * `SelectLastGuff` **(Many-Argument Workhorses)** (Impact: 400.8)
    * *Intent:* %========================================================================== % function [standard, gu...
  * `CheckFields` **(Many-Argument Workhorses)** (Impact: 400.3)
    * *Intent:* %========================================================================== % function ok = CheckFie...
  * `SelectTomographicImages` **(Many-Argument Workhorses)** (Impact: 400.0)
    * *Intent:* %========================================================================== % function [images,guff]...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 427 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 1365
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 283`, `args: 32`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 511`, `dead_code: 32`, `unreferenced_by_name: 1`
* *Architecture:* `io: 17`, `api: 31`
* *Defense:* `safety: 129`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.000385
  * `Imports (Out-Degree: 22):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `@gifti/private/miniz.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.868)
- **Top Global Matches:** file_cluster_6: 5.868, file_cluster_4: 8.791, file_cluster_8: 16.514
- **Magnitude:** 8341.62 | **LOC:** 8891 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.186; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tinfl_decompress` **(Many-Argument Workhorses)** (Impact: 345.7)
  * `mz_zip_writer_add_mem_ex_v2` **(Many-Argument Workhorses)** (Impact: 331.8)
  * `mz_zip_writer_add_cfile` **(Many-Argument Workhorses)** (Impact: 278.2)
    * *Intent:* #ifndef MINIZ_NO_STDIO
  * `mz_zip_writer_add_from_zip_reader` **(Many-Argument Workhorses)** (Impact: 142.1)
    * *Intent:* /* TODO: This func is now pretty freakin complex due to zip64, split it up? */
  * `mz_zip_reader_extract_to_callback` **(Many-Argument Workhorses)** (Impact: 134.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 1175 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 3940
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1441`, `structural_boundaries: 974`, `args: 332`, `func_start: 177`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 1590`, `dead_code: 7`, `planned_debt: 13`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 290`, `import: 13`
* *Defense:* `safety: 207`, `doc: 4`, `immutability_locks: 311`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000385
  * `Imports (Out-Degree: 0):` assert.h, stddef.h, stdio.h, stdlib.h, string.h, stat.h, utime.h, time.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `toolbox/dcm_meeg/spm_api_erp.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 15.475)
- **Top Global Matches:** file_cluster_1: 15.475, file_cluster_3: 33.442, file_cluster_8: 55.209
- **Magnitude:** 5805.38 | **LOC:** 1554 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.11; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.7%), Guard Balance (formerly Safety Score) (66.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_Callback` **(Many-Argument Workhorses)** (Impact: 513.0)
    * *Intent:* %-DCM files and directories: Load and save %========================================================...
  * `save_Callback` **(Many-Argument Workhorses)** (Impact: 367.9)
    * *Intent:* % --- Executes on button press in save. % ----------------------------------------------------------...
  * `spm_api_erp` **(Many-Argument Workhorses)** (Impact: 364.7)
    * *Intent:* % SPM_API_ERP Application M-file for spm_api_erp.fig % FIG = SPM_API_ERP launch spm_api_erp GUI. % S...
  * `reset_Callback` **(Many-Argument Workhorses)** (Impact: 364.4)
    * *Intent:* % store selections in DCM % ------------------------------------------------------------------------...
  * `Datafile_Callback` **(Many-Argument Workhorses)** (Impact: 353.4)
    * *Intent:* % Data selection and design %=======================================================================...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 169 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 176`, `args: 27`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 241`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 6`, `api: 27`
* *Defense:* `safety: 104`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 5.5e-05 | `Ripple Effect (Closeness):` 0.000513
  * `Imports (Out-Degree: 36):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spm_mesh_render.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.272)
- **Top Global Matches:** file_cluster_1: 5.272, file_cluster_3: 48.144, file_cluster_8: 69.988
- **Magnitude:** 4556.26 | **LOC:** 871 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); blast radius 0.135; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.3%), Guard Balance (formerly Safety Score) (72.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `myMenuCallback` **(Many-Argument Workhorses)** (Impact: 261.8)
    * *Intent:* %==========================================================================
  * `myPostCallback` **(Many-Argument Workhorses)** (Impact: 240.2)
    * *Intent:* %==========================================================================
  * `myInflate` **(Many-Argument Workhorses)** (Impact: 224.1)
    * *Intent:* %==========================================================================
  * `myCCLabel` **(Many-Argument Workhorses)** (Impact: 223.8)
    * *Intent:* %==========================================================================
  * `myView` **(Many-Argument Workhorses)** (Impact: 212.1)
    * *Intent:* %==========================================================================
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 144 instances
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 126`, `args: 25`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 162`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 24`
* *Defense:* `safety: 63`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.001041 | `Ripple Effect (Closeness):` 0.054304
  * `Imports (Out-Degree: 26):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `matlabbatch/cfg_getfile.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.483)
- **Top Global Matches:** file_cluster_3: 7.483, file_cluster_8: 26.96, file_cluster_6: 39.989
- **Magnitude:** 4547.02 | **LOC:** 1553 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); blast radius 0.757; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%), Complexity Load (formerly Cognitive Load) (71.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `click_dir_box` **(Many-Argument Workhorses)** (Impact: 283.8)
    * *Intent:* %======================================================================= %==========================...
  * `select_rec1` **(Many-Argument Workhorses)** (Impact: 240.4)
    * *Intent:* %======================================================================= %==========================...
  * `update` **(Compute Cores)** (Impact: 228.2)
    * *Intent:* %======================================================================= %==========================...
  * `click_file_box` **(Many-Argument Workhorses)** (Impact: 227.5)
    * *Intent:* %======================================================================= %==========================...
  * `select` **(Many-Argument Workhorses)** (Impact: 221.4)
    * *Intent:* %======================================================================= %==========================...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 236 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 176`, `args: 56`, `func_start: 39`
* *Risk/State:* `state_mutation: 314`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 39`, `concurrency: 1`
* *Defense:* `safety: 60`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.757
  * `Choke Point (Betweenness):` 0.001658 | `Ripple Effect (Closeness):` 0.126507
  * `Imports (Out-Degree: 16):` None
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `spm_eeg_review_callbacks.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 22.808)
- **Top Global Matches:** file_cluster_1: 22.808, file_cluster_3: 26.32, file_cluster_8: 47.938
- **Magnitude:** 3682.96 | **LOC:** 2030 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Complexity Load (formerly Cognitive Load) (60.9%), Connectivity (formerly Api Exposure) (5.8%)
- **Documentation Coverage:** 11.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (Impact: 626.4)
  * `updateDisp` **(Many-Argument Workhorses)** (Impact: 513.8)
    * *Intent:* %% Main update display % This function updates the display of the data and events. if ~exist('flags'...
  * `psd_defineMenuEvent` **(Many-Argument Workhorses)** (Impact: 240.0)
    * *Intent:* %% Define menu event % This funcion defines the uicontextmenu associated to the selected events. % A...
  * `switchBC` **(Defensive Guards)** (Impact: 226.1)
    * *Intent:* %% Switch 'bad channel' status
  * `getUItable` **(Defensive Guards)** (Impact: 160.0)
    * *Intent:* % try,str{7} = ['Time onset: ',num2str(D.timeOnset),' sec'];end %% extracting data from spm_uitable ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 482 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 1641
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 259`, `args: 11`, `func_start: 8`
* *Risk/State:* `state_mutation: 677`
* *Architecture:* `io: 2`, `api: 8`
* *Defense:* `safety: 142`, `doc: 26`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.001833
  * `Imports (Out-Degree: 41):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `spm_results_nidm.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 21.485)
- **Top Global Matches:** file_cluster_1: 21.485, file_cluster_3: 27.381, file_cluster_8: 49.07
- **Magnitude:** 3363.54 | **LOC:** 1922 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (64.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `coordspace` **(Many-Argument Workhorses)** (Impact: 205.2)
    * *Intent:* %========================================================================== % function id = coordspa...
  * `img2nii` **(Many-Argument Workhorses)** (Impact: 189.9)
    * *Intent:* %========================================================================== % function img2nii(img,n...
  * `make_ROI` **(Many-Argument Workhorses)** (Impact: 183.8)
    * *Intent:* %========================================================================== % function make_ROI(fnam...
  * `spm_results_nidm` **(Many-Argument Workhorses)** (Impact: 174.3)
    * *Intent:* % Export SPM stats results using the Neuroimaging Data Model (NIDM) % FORMAT [nidmfile, prov] = spm_...
  * `xsdfloat` **(Many-Argument Workhorses)** (Impact: 172.0)
    * *Intent:* %========================================================================== % function v = xsdfloat(...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 293 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 957
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 155`, `args: 24`, `func_start: 19`
* *Risk/State:* `state_mutation: 371`, `dead_code: 16`, `unreferenced_by_name: 5`
* *Architecture:* `io: 8`, `api: 19`
* *Defense:* `safety: 60`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.016427 | `Ripple Effect (Closeness):` 0.09347
  * `Imports (Out-Degree: 38):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spm_deformations.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.914)
- **Top Global Matches:** file_cluster_3: 11.914, file_cluster_8: 32.819, file_cluster_1: 37.722
- **Magnitude:** 2980.32 | **LOC:** 818 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 0.123; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spm_deformations` **(Many-Argument Workhorses)** (Impact: 275.6)
    * *Intent:* % Various deformation field utilities % FORMAT out = spm_deformations(job) % job - a job created via...
  * `get_comp` **(Many-Argument Workhorses)** (Impact: 262.2)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
  * `get_job` **(Many-Argument Workhorses)** (Impact: 258.1)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
  * `get_sn2def` **(Many-Argument Workhorses)** (Impact: 243.9)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
  * `get_def` **(Many-Argument Workhorses)** (Impact: 223.8)
    * *Intent:* %========================================================================== % function [Def,mat] = g...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 258 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 846
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 92`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 330`, `dead_code: 15`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 16`
* *Defense:* `safety: 40`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 28):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `spm_sp.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 13.731)
- **Top Global Matches:** file_cluster_1: 13.731, file_cluster_3: 35.903, file_cluster_8: 57.634
- **Magnitude:** 2833.62 | **LOC:** 1416 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); blast radius 0.299; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spm_sp` **(Many-Argument Workhorses)** (Impact: 637.8)
    * *Intent:* % Orthogonal (design) matrix space setting & manipulation % FORMAT varargout = spm_spc(action,vararg...
  * `sf_tol` **(Compute Cores)** (Impact: 80.1)
    * *Intent:* %======================================================================= x(abs(x) < t) = 0; function...
  * `sf_create` **(Compute Cores)** (Impact: 75.4)
    * *Intent:* %======================================================================= %- S U B - F U N C T I O N ...
  * `sf_set` **(Compute Cores)** (Impact: 74.6)
    * *Intent:* %======================================================================= x = sf_create; x.X = X; %--...
  * `sf_transp` **(Compute Cores)** (Impact: 70.5)
    * *Intent:* %======================================================================= % %- Tranpspose the space :...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 156 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 180`, `args: 31`, `func_start: 32`
* *Risk/State:* `state_mutation: 163`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 32`
* *Defense:* `safety: 44`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.299
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.076832
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `matlabbatch/cfg_util.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.895)
- **Top Global Matches:** file_cluster_3: 15.895, file_cluster_1: 33.557, file_cluster_8: 37.098
- **Magnitude:** 2709.9 | **LOC:** 1862 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); blast radius 0.373; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 92.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `local_addtojob` **(Many-Argument Workhorses)** (Impact: 229.3)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_delfromjob` **(Many-Argument Workhorses)** (Impact: 198.5)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_gencode` **(Many-Argument Workhorses)** (Impact: 196.2)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_cd` **(Many-Argument Workhorses)** (Impact: 184.8)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_compactjob` **(Many-Argument Workhorses)** (Impact: 176.7)
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
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 493`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 15`, `api: 18`
* *Defense:* `safety: 82`, `doc: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.373
  * `Choke Point (Betweenness):` 0.001871 | `Ripple Effect (Closeness):` 0.095406
  * `Imports (Out-Degree: 21):` None
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/shoot_dartel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.297)
- **Top Global Matches:** file_cluster_6: 6.297, file_cluster_8: 11.72, file_cluster_4: 13.593
- **Magnitude:** 2514.74 | **LOC:** 1565 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 190`, `structural_boundaries: 29`, `args: 24`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 961`, `dead_code: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000385
  * `Imports (Out-Degree: 8):` math.h, mex.h, shoot_boundary.h, shoot_diffeo3d.h, shoot_optim3d.h, shoot_regularisers.h, stdio.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/shoot_regularisers.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.715)
- **Top Global Matches:** file_cluster_3: 8.715, file_cluster_8: 15.957, file_cluster_6: 28.797
- **Magnitude:** 2020.28 | **LOC:** 1659 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.117; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (29.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `relax_all` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* /************************************************************************************************/ /...
  * `relax_be` **(Many-Argument Workhorses)** (Impact: 69.0)
    * *Intent:* /************************************************************************************************/ /...
  * `sumsq` **(Many-Argument Workhorses)** (Impact: 50.2)
    * *Intent:* * \param[in] s[4] Parameter of the membrane energy (penalizes * elements of the Jacobian matrix -> 1...
  * `relax_le` **(Many-Argument Workhorses)** (Impact: 50.1)
    * *Intent:* * smoothness) * \param[in] s[5] Parameter of the bending energy (penalizes * elements of the Hessian...
  * `relax_me` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* /************************************************************************************************/ /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 382 instances
* *State Mutation (weighted view):* 1607
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 12`, `args: 12`, `func_start: 11`
* *Risk/State:* `state_mutation: 843`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `doc: 80`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.117
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000769
  * `Imports (Out-Degree: 2):` math.h, shoot_boundary.h, spm_mex.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/spm_diffeo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 13.725)
- **Top Global Matches:** file_cluster_3: 13.725, file_cluster_8: 30.649, file_cluster_6: 43.087
- **Magnitude:** 1974.02 | **LOC:** 1180 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.101; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.0%), Complexity Load (formerly Cognitive Load) (86.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.101
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` math.h, mex.h, shoot_boundary.h, shoot_bsplines.h, shoot_dartel.h, shoot_diffeo3d.h, shoot_multiscale.h, shoot_optim3d.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/DEM/spm_MDP_VB_XX.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.35)
- **Top Global Matches:** file_cluster_3: 9.35, file_cluster_8: 16.753, file_cluster_6: 29.419
- **Magnitude:** 1869.12 | **LOC:** 1607 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Complexity Load (formerly Cognitive Load) (77.5%), Connectivity (formerly Api Exposure) (6.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spm_forwards` **(Many-Argument Workhorses)** (Impact: 253.7)
    * *Intent:* % auxillary functions %========================================================================== % ...
  * `spm_backwards` **(Many-Argument Workhorses)** (Impact: 159.3)
    * *Intent:* % Backwards smoothing to evaluate posterior over initial states %-----------------------------------...
  * `spm_log` **(Compute Cores)** (Impact: 88.7)
    * *Intent:* % log of numeric array plus a small constant %------------------------------------------------------...
  * `spm_norm` **(Compute Cores)** (Impact: 88.4)
    * *Intent:* % normalisation of a probability transition matrix (columns) %--------------------------------------...
  * `spm_MDP_VB_VOX` **(Many-Argument Workhorses)** (Impact: 83.3)
    * *Intent:* % FORMAT L = spm_MDP_VB_VOX(MDP,L,t) % returns likelihoods from voice recognition (and articulates r...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 260 instances
* *State Mutation (weighted view):* 826
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 230`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 306`
* *Architecture:* `io: 2`, `api: 11`
* *Defense:* `safety: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.000769
  * `Imports (Out-Degree: 27):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `toolbox/DARTEL/tbx_cfg_dartel.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.53)
- **Top Global Matches:** file_cluster_3: 7.53, file_cluster_8: 27.52, file_cluster_6: 40.577
- **Magnitude:** 1866.18 | **LOC:** 1369 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tbx_cfg_dartel` **(Many-Argument Workhorses)** (Impact: 216.9)
    * *Intent:* % Configuration file for toolbox 'Dartel Tools' %___________________________________________________...
  * `vout_initial_import` **(Compute Cores)** (Impact: 58.1)
    * *Intent:* %dartel.num = [0 Inf]; %_______________________________________________________________________ % %_...
  * `check_dartel_template` **(Compute Cores)** (Impact: 50.0)
    * *Intent:* %_______________________________________________________________________ %__________________________...
  * `vout_dartel_template` **(Compute Cores)** (Impact: 45.1)
    * *Intent:* %_______________________________________________________________________ %__________________________...
  * `vout_dartel_warp` **(Compute Cores)** (Impact: 38.3)
    * *Intent:* %_______________________________________________________________________ %__________________________...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 258 instances
* *State Mutation (weighted view):* 1225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 33`, `args: 13`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 709`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.101
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_diffeo3d.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.281)
- **Top Global Matches:** file_cluster_6: 7.281, file_cluster_8: 10.565, file_cluster_4: 14.682
- **Magnitude:** 1863.82 | **LOC:** 1268 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.117; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushc_grads` **(Many-Argument Workhorses)** (Impact: 74.6)
    * *Intent:* /* This should perhaps be tidied up and generalised in line with the pushpull function */
  * `pushpull` **(Many-Argument Workhorses)** (Impact: 73.0)
    * *Intent:* #define TINY 5e-2f
  * `grad1` **(Many-Argument Workhorses)** (Impact: 61.7)
    * *Intent:* #define LOG(x) (((x)>0) ? log(x+0.001): -6.9078)
  * `composition_stuff` **(Many-Argument Workhorses)** (Impact: 61.0)
    * *Intent:* /* * Composition operations, possibly along with Jacobian matrices. * Done using B(A) = U(A) + A, wh...
  * `def2jac_neuman` **(Many-Argument Workhorses)** (Impact: 46.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 330 instances
* *State Mutation (weighted view):* 1363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 29`, `args: 26`, `func_start: 23`
* *Risk/State:* `state_mutation: 703`, `dead_code: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 21`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.117
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000769
  * `Imports (Out-Degree: 6):` math.h, shoot_boundary.h, shoot_expm3.h, shoot_optim3d.h, spm_mex.h, stdio.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spm_eeg_inv_imag_api.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.058)
- **Top Global Matches:** file_cluster_3: 8.058, file_cluster_8: 27.607, file_cluster_6: 40.62
- **Magnitude:** 1861.38 | **LOC:** 484 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.103; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Complexity Load (formerly Cognitive Load) (68.0%), Guard Balance (formerly Safety Score) (60.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreateMeshes_Callback` **(Many-Argument Workhorses)** (Impact: 111.0)
    * *Intent:* % MAIN FUNCTIONS FOR MODEL SEPCIFICATION AND INVERSION %============================================...
  * `Reg2tem_Callback` **(Many-Argument Workhorses)** (Impact: 110.6)
    * *Intent:* % --- Executes on button press in Reg2tem. %--------------------------------------------------------...
  * `DataReg_Callback` **(Many-Argument Workhorses)** (Impact: 110.2)
    * *Intent:* % --- Executes on button press in Data Reg. %-------------------------------------------------------...
  * `Forward_Callback` **(Many-Argument Workhorses)** (Impact: 109.9)
    * *Intent:* % --- Executes on button press in Forward Model. %--------------------------------------------------...
  * `Inverse_Callback` **(Many-Argument Workhorses)** (Impact: 109.5)
    * *Intent:* % --- Executes on button press in Invert. %---------------------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 38 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 46`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 61`, `unreferenced_by_name: 26`
* *Architecture:* `io: 1`, `api: 28`
* *Defense:* `safety: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.103
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.000513
  * `Imports (Out-Degree: 26):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spm_eeg_inv_visu3D_api.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.871)
- **Top Global Matches:** file_cluster_3: 9.871, file_cluster_8: 30.368, file_cluster_1: 40.184
- **Magnitude:** 1842.24 | **LOC:** 823 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.104; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (90.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spm_eeg_inv_visu3D_api` **(Many-Argument Workhorses)** (Impact: 130.2)
    * *Intent:* % SPM_EEG_INV_VISU3D_API M-file for spm_eeg_inv_visu3D_api.fig % - FIG = SPM_EEG_INV_VISU3D_API laun...
  * `UpDate_Display_SRCS` **(Many-Argument Workhorses)** (Impact: 103.7)
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
* *Risk/State:* `state_mutation: 160`, `unreferenced_by_name: 24`
* *Architecture:* `api: 30`
* *Defense:* `safety: 32`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000577
  * `Imports (Out-Degree: 17):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `toolbox/FieldMap/pm_segment.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.218)
- **Top Global Matches:** file_cluster_3: 8.218, file_cluster_8: 18.532, file_cluster_6: 31.281
- **Magnitude:** 1670.12 | **LOC:** 705 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.108; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pm_segment` **(Many-Argument Workhorses)** (Impact: 195.2)
    * *Intent:* % Segment an MR image into Gray, White & CSF. % % FORMAT VO = pm_segment(PF,PG,flags) % PF - name(s)...
  * `display_graphics` **(Many-Argument Workhorses)** (Impact: 148.2)
    * *Intent:* %======================================================================= %==========================...
  * `affine_transform` **(Many-Argument Workhorses)** (Impact: 138.0)
    * *Intent:* %======================================================================= %==========================...
  * `get_affine_mapping` **(Many-Argument Workhorses)** (Impact: 110.5)
    * *Intent:* %======================================================================= %==========================...
  * `get_bp` **(Many-Argument Workhorses)** (Impact: 60.4)
    * *Intent:* %======================================================================= %==========================...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 531
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 97`, `args: 19`, `func_start: 19`
* *Risk/State:* `state_mutation: 223`, `unreferenced_by_name: 3`
* *Architecture:* `api: 19`
* *Defense:* `safety: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.000992
  * `Imports (Out-Degree: 26):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spm_dicom_header.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 14.939)
- **Top Global Matches:** file_cluster_1: 14.939, file_cluster_3: 34.055, file_cluster_8: 55.834
- **Magnitude:** 1605.96 | **LOC:** 530 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReadDicom` **(Many-Argument Workhorses)** (Impact: 340.7)
    * *Intent:* %========================================================================== % function [Header, Byte...
  * `spm_dicom_header` **(Many-Argument Workhorses)** (Impact: 306.4)
    * *Intent:* % Read header information from a DICOM file % FORMAT Header = spm_dicom_header(DicomFilename, DicomD...
  * `ReadSQ` **(Many-Argument Workhorses)** (Impact: 210.8)
    * *Intent:* %========================================================================== % function [Header, Byte...
  * `ReadTag` **(Many-Argument Workhorses)** (Impact: 150.5)
    * *Intent:* %========================================================================== % function Tag = ReadTag...
  * `DecodeCSA` **(Many-Argument Workhorses)** (Impact: 51.2)
    * *Intent:* %========================================================================== % function t = DecodeCSA...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 154 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 472
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 84`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 164`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 72`, `api: 7`
* *Defense:* `safety: 26`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000513
  * `Imports (Out-Degree: 5):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spm_FcUtil.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 20.608)
- **Top Global Matches:** file_cluster_1: 20.608, file_cluster_3: 28.477, file_cluster_8: 50.147
- **Magnitude:** 1601.84 | **LOC:** 934 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); blast radius 0.235; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spm_FcUtil` **(Compute Cores)** (Impact: 373.3)
    * *Intent:* % Contrast utilities % FORMAT varargout = spm_FcUtil(action,varargin) %_____________________________...
  * `sf_FconFields` **(Compute Cores)** (Impact: 67.3)
    * *Intent:* %======================================================================= %==========================...
  * `sf_MinFcFields` **(Compute Cores)** (Impact: 66.5)
    * *Intent:* %======================================================================= % used internally. Minimum ...
  * `sf_IsFcon` **(Compute Cores)** (Impact: 65.9)
    * *Intent:* %======================================================================= % yes_no = spm_FcUtil('IsFc...
  * `sf_IsSet` **(Compute Cores)** (Impact: 62.3)
    * *Intent:* %======================================================================= % used internally; To be se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 143`, `args: 18`, `func_start: 20`
* *Risk/State:* `state_mutation: 109`, `unreferenced_by_name: 3`
* *Architecture:* `api: 20`
* *Defense:* `safety: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.235
  * `Choke Point (Betweenness):` 0.000236 | `Ripple Effect (Closeness):` 0.095745
  * `Imports (Out-Degree: 5):` None
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `toolbox/DEM/spm_MDP_VB_X.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.674)
- **Top Global Matches:** file_cluster_3: 15.674, file_cluster_1: 33.73, file_cluster_8: 36.861
- **Magnitude:** 1587.6 | **LOC:** 1675 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); blast radius 0.264; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.2%), Complexity Load (formerly Cognitive Load) (78.1%), Debt Markers (formerly Tech Debt) (8.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spm_MDP_VB_X` **(Many-Argument Workhorses)** (Impact: 193.3)
    * *Intent:* % active inference and learning using variational message passing % FORMAT [MDP] = spm_MDP_VB_X(MDP,...
  * `spm_log` **(Compute Cores)** (Impact: 101.1)
    * *Intent:* % auxillary functions %========================================================================== % ...
  * `spm_MDP_VB_VOX` **(Many-Argument Workhorses)** (Impact: 83.3)
    * *Intent:* % FORMAT L = spm_MDP_VB_VOX(MDP,L,t) % returns likelihoods from voice recognition (and articulates r...
  * `spm_norm` **(Defensive Guards)** (Impact: 39.8)
    * *Intent:* % normalisation of a probability transition matrix (columns) %--------------------------------------...
  * `spm_wnorm` **(Defensive Guards)** (Impact: 39.4)
    * *Intent:* % summation of a probability transition matrix (columns) %------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 257`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 336`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 9`
* *Defense:* `safety: 112`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 0.000236 | `Ripple Effect (Closeness):` 0.006648
  * `Imports (Out-Degree: 24):` None
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `toolbox/FieldMap/FieldMap.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.485)
- **Top Global Matches:** file_cluster_6: 8.485, file_cluster_8: 12.662, file_cluster_4: 14.888
- **Magnitude:** 1517.5 | **LOC:** 2332 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 0.182; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (66.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FieldMap` **(Many-Argument Workhorses)** (Impact: 270.9)
    * *Intent:* % FieldMap is an SPM Toolbox for creating field maps and unwarping EPI. % A full description of the ...
  * `smooth_uint8` **(Many-Argument Workhorses)** (Impact: 26.0)
    * *Intent:* %======================================================================= % % Smoothing functions req...
  * `smoothing_kernel` **(Many-Argument Workhorses)** (Impact: 25.2)
    * *Intent:* %_______________________________________________________________________ %__________________________...
  * `loaduint8` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* %======================================================================= % % Load data function requ...
  * `paccuracy` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 295 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 999
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 116`, `args: 5`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 409`, `dead_code: 3`
* *Architecture:* `api: 5`
* *Defense:* `safety: 59`, `doc: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.182
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 31):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `toolbox/DEM/DEMO_AI_NLSI.m` (MATLAB) | Magnitude: 17.32 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 12, core_var_decl: 4, design_short_vars: 3, memory_alloc: 2
- `toolbox/dcm_meeg/spm_fp_cmc_tfm.m` (MATLAB) | Magnitude: 36.12 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 17, core_var_decl: 16, design_short_vars: 15, scientific: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/ROBOT_DCM_fMRI.m` (MATLAB) | Magnitude: 77.48 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, state_mutation: 27, core_var_decl: 13, structural_boundaries: 10
- `tests/test_gifti.m` (MATLAB) | Magnitude: 92.3 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 47, core_var_decl: 35, design_snake_case: 35, design_short_vars: 23
- `toolbox/dcm_meeg/spm_dcm_tfm_multimodal.m` (MATLAB) | Magnitude: 145.94 | Delta: **0.16** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 94, core_var_decl: 37, design_short_vars: 25, safety: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `matlabbatch/@cfg_item/gencode.m` (MATLAB) | Magnitude: 24.42 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 5, core_var_decl: 5, design_snake_case: 5, branch: 2
- `spm_extrapolate_def.m` (MATLAB) | Magnitude: 45.42 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, state_mutation: 13, core_var_decl: 12, design_short_vars: 10
- `toolbox/mci/inference/spm_mci_ess.m` (MATLAB) | Magnitude: 58.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 16, state_mutation: 14, design_snake_case: 12, design_short_vars: 11
- `spm_funfun.m` (MATLAB) | Magnitude: 21.56 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 7, core_var_decl: 7, design_snake_case: 7
- `toolbox/Neural_Models/spm_lfp_mtf.m` (MATLAB) | Magnitude: 97.72 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 38, core_var_decl: 34, design_short_vars: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Makefile.var` (MAKEFILE) | Magnitude: 28.48 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 48, indent_spaces: 34, core_var_decl: 33, design_upper_case: 33
- `src/shoot_diffeo3d.h` (C) | Magnitude: 34.46 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 19, args: 19, api: 19, pointers: 17
- `src/shoot_optimN.h` (C) | Magnitude: 16.08 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 4, api: 4, pointers: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `matlabbatch/cfg_basicio/cfg_vout_dir_move.m` (MATLAB) | Magnitude: 24.6 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 6, indent_spaces: 5, core_var_decl: 4, design_snake_case: 4
- `matlabbatch/cfg_basicio/cfg_vout_file_move.m` (MATLAB) | Magnitude: 24.6 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 6, indent_spaces: 5, core_var_decl: 4, design_snake_case: 4
- `matlabbatch/cfg_basicio/cfg_vout_mkdir.m` (MATLAB) | Magnitude: 24.6 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 6, core_var_decl: 3, design_snake_case: 3, branch: 2
- `toolbox/DEM/spm_voice_iQ.m` (MATLAB) | Magnitude: 8.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: safety: 8, core_var_decl: 8, design_short_vars: 8, structural_boundaries: 4
- `spm_ADEM.m` (MATLAB) | Magnitude: 624.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 280, indent_spaces: 276, core_var_decl: 183, design_short_vars: 134

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/shoot_optimN.c` (C) | Magnitude: 1284.66 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 584, state_mutation: 359, core_var_decl: 127, design_snake_case: 127

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `toolbox/OldSeg/spm_maff.m` (MATLAB) | Magnitude: 416.2 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: core_var_decl: 124, state_mutation: 120, design_short_vars: 86, indent_spaces: 83
- `toolbox/DEM/DEM_demo_duet.m` (MATLAB) | Magnitude: 480.94 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 106, core_var_decl: 84, design_short_vars: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/test_spm_get_data.m` (MATLAB) | Magnitude: 13.76 | Delta: **0.176** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: test: 7, core_var_decl: 6, design_snake_case: 6, state_mutation: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `spm.m` -> **Severity: 2.285** (Bridge: 0.0228 * Flux: 100.0%)
- `spm_check_installation.m` -> **Severity: 1.653** (Bridge: 0.0165 * Flux: 100.0%)
- `spm_results_nidm.m` -> **Severity: 1.643** (Bridge: 0.0164 * Flux: 100.0%)
- `spm_figure.m` -> **Severity: 1.266** (Bridge: 0.0127 * Flux: 100.0%)
- `spm_list.m` -> **Severity: 0.967** (Bridge: 0.0097 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `@xmltree/find.m` -> **Severity: 22.895** (Embedded: 0.3034 * Error Risk: 75.4724%)
- `@gifti/struct.m` -> **Severity: 20.551** (Embedded: 0.3787 * Error Risk: 54.2752%)
- `@xmltree/private/xml_parser.m` -> **Severity: 17.464** (Embedded: 0.2015 * Error Risk: 86.6542%)
- `@file_array/reshape.m` -> **Severity: 17.271** (Embedded: 0.2953 * Error Risk: 58.4884%)
- `spm.m` -> **Severity: 15.225** (Embedded: 0.19 * Error Risk: 80.119%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `@gifti/struct.m` -> **Severity: 21960.7** (Blast Radius: 219.607 * Doc Risk: 100.0%)
- `@file_array/reshape.m` -> **Severity: 19314.3** (Blast Radius: 193.143 * Doc Risk: 100.0%)
- `@meeg/isempty.m` -> **Severity: 4206.0** (Blast Radius: 42.06 * Doc Risk: 100.0%)
- `@file_array/numel.m` -> **Severity: 3577.2** (Blast Radius: 35.772 * Doc Risk: 100.0%)
- `@xmltree/find.m` -> **Severity: 1609.5** (Blast Radius: 16.095 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 4718 literal sites + 25 sites through wrappers = 4743

- `MZ_FREE` (macro, memory_alloc, primitive): 14 call sites in 1 files -- `@gifti/private/miniz.c`
- `MZ_MALLOC` (macro, memory_alloc, primitive): 7 call sites in 1 files -- `@gifti/private/miniz.c`
- `MZ_REALLOC` (macro, memory_alloc, primitive): 3 call sites in 1 files -- `@gifti/private/miniz.c`
- `mz_free` (function, memory_alloc, via MZ_FREE): 1 call sites in 1 files -- `@gifti/private/miniz.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 97471 call pairs -- scoped 4.8%, unique 24.1%, ambiguous 8.6%, external 62.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| matlab | 94300 | 4.0% | 24.8% | 8.9% | 62.4% |
| c | 3023 | 28.3% | 4.0% | 0.1% | 67.6% |
| cpp | 106 | 45.3% | 0.0% | 0.0% | 54.7% |
| shell | 21 | 0.0% | 0.0% | 0.0% | 100.0% |
| makefile | 18 | 0.0% | 0.0% | 0.0% | 100.0% |
| html | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
