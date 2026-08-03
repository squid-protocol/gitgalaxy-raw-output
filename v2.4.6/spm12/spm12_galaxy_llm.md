# ARCHITECTURAL_BRIEF: spm12
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/spm12` |
| **Timestamp** | `2026-08-03T21:37:00.155580+00:00` |
| **Scan Duration** | `12.14s` |
| **Git Branch** | `main` |
| **Git Commit** | `03ac9473cad402407b6472228377c0167fdc54b8` |
| **Git Remote** | `https://github.com/spm/spm12` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4173 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 5154 |
| Analyzed Artifacts (Scanned) | 4218 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 936 |
| Total LOC | 385633 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.8% |
| Dominant Lang | MATLAB |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7627 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2053 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6848 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MATLAB | 4017 | 357833 | 95.2% |
| C | 137 | 26684 | 3.2% |
| MARKDOWN | 22 | 0 | 0.5% |
| PLAINTEXT | 20 | 0 | 0.5% |
| MAKEFILE | 9 | 437 | 0.2% |
| CPP | 4 | 225 | 0.1% |
| OBJECTIVE-C | 3 | 204 | 0.1% |
| SHELL | 2 | 97 | 0.0% |
| HTML | 2 | 86 | 0.0% |
| JAVA | 1 | 33 | 0.0% |
| CSS | 1 | 34 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.038`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2396 | 56.8% |
| file_cluster_17 | 1425 | 33.8% |
| file_cluster_9 | 156 | 3.7% |
| file_cluster_13 | 61 | 1.4% |
| file_cluster_11 | 58 | 1.4% |
| file_cluster_2 | 37 | 0.9% |
| file_cluster_6 | 22 | 0.5% |
| file_cluster_4 | 10 | 0.2% |
| file_cluster_0 | 4 | 0.1% |
| file_cluster_10 | 4 | 0.1% |
| file_cluster_12 | 3 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 42 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 936*

**Composition by Extension & Reason:**
- `.png`: 230x Excluded (Explicitly Denied Extension: '.png')
- `.m`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 77 exceeds 500 chars), 2x Excluded (Machine-Generated Source Code Signature: 36 LOC)
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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 61.0 | 75.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 78.3 | 88.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.1 | 0.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 94.9 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 99.3 | 10.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 88.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.8 | 14.5 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `external/fieldtrip/fileio/private/read_besa_besa.m` (Hits: 190)
- `external/fieldtrip/fileio/private/read_4d_hdr.m` (Hits: 161)
- `spm_ecat2nifti.m` (Hits: 126)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **spm_mapping.h** (`src/spm_mapping.h`) — 10 inbound connections
2. **spm_mex.h** (`src/spm_mex.h`) — 9 inbound connections
3. **shoot_boundary.h** (`src/shoot_boundary.h`) — 8 inbound connections
4. **geometry.h** (`external/fieldtrip/src/geometry.h`) — 7 inbound connections
5. **compiler.h** (`external/fieldtrip/src/compiler.h`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rfbevent.c** (`external/fieldtrip/src/rfbevent.c`) — 18 outbound dependencies
2. **file2mat.c** (`@file_array/private/file2mat.c`) — 14 outbound dependencies
3. **spm_diffeo.c** (`src/spm_diffeo.c`) — 11 outbound dependencies
4. **spm_mapping.c** (`src/spm_mapping.c`) — 11 outbound dependencies
5. **mat2file.c** (`@file_array/private/mat2file.c`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `serialize_jsonld` (@ `spm_provenance.m`) -> Impact: **1312.5** | LOC: 579
- `mrqcof` (@ `src/spm_brainwarp.c`) -> Impact: **1164.6** | LOC: 316
- `E0000` (@ `@nifti/private/nifti_stats.c`) -> Impact: **929.0** | LOC: 172
- `mexFunction` (@ `external/fieldtrip/src/nanstd.c`) -> Impact: **613.4** | LOC: 327
  * *Intent:* #if defined (COMPILER_MSVC) #include <math.h> #define isnan _isnan #define INFINITY (HUGE_VAL+HUGE_VAL) #define NAN (INFINITY - INFINITY) #elif define...
- `mexFunction` (@ `external/fieldtrip/src/nanvar.c`) -> Impact: **613.4** | LOC: 327
  * *Intent:* #if defined (COMPILER_MSVC) #include <math.h> #define isnan _isnan #define INFINITY (HUGE_VAL+HUGE_VAL) #define NAN (INFINITY - INFINITY) #elif define...
- `cdfbin` (@ `@nifti/private/nifti_stats.c`) -> Impact: **534.4** | LOC: 253
- `cdfbet` (@ `@nifti/private/nifti_stats.c`) -> Impact: **510.6** | LOC: 250
- `cdfnbn` (@ `@nifti/private/nifti_stats.c`) -> Impact: **510.4** | LOC: 246
- `cdfgam` (@ `@nifti/private/nifti_stats.c`) -> Impact: **459.0** | LOC: 180
  * *Intent:* */
- `convxyz` (@ `src/spm_conv_vol.c`) -> Impact: **457.4** | LOC: 239

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `spm_fMRI_design_show` (@ `compat/spm_fMRI_design_show.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % Interactive review of fMRI design matrix % FORMAT spm_fMRI_design_show(SPM,s,i) % % Sess(s).U(i) - see spm_fMRI_design for session s, trial i. % %__...
- `get_maxima` (@ `src/spm_get_lm.c`) -> **O(2^N) [Recursive]**
- `part` (@ `config/spm_make_manual.m`) -> **O(2^N) [Recursive]**
  * *Intent:* %========================================================================== % this is always false, and each cfg_item has a tag %if isstruct(c) && isf...
- `readCTFhdm` (@ `external/ctf/readCTFhdm.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % Version 1.1 19 April 2007 - Test date. % 21 March 2007. Modified to read v6.0 .hdm files that have additional % fields in MultiSphere_Data % Reads a...
- `cat` (@ `matlabbatch/@cfg_item/cat.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % function varargout = cat(varargin) % Prevent cat for cfg_item objects. % % This code is part of a batch job configuration system for MATLAB. See % h...
- `basym` (@ `@nifti/private/nifti_stats.c`) -> **O(2^N) [Recursive]**
- `array` (@ `src/spm_jsonread.c`) -> **O(2^N) [Recursive]**
- `sensors` (@ `@meeg/sensors.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % Sets and gets sensor fields for EEG and MEG % returns empty matrix if no sensors are defined. % FORMAT res = sensors(this, type, newsens) % type - '...
- `harvest` (@ `matlabbatch/@cfg_exbranch/harvest.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % function [tag, val, typ, dep, chk, cj] = harvest(item, cj, dflag, rflag) % harvest function for cfg_exbranch % item - cfg_exbranch to harvest % dfla...
- `spm_voice_likelihood` (@ `toolbox/DEM/spm_voice_likelihood.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % Return the lexical likelihood % FORMAT [L,M,N] = spm_voice_likelihood(xY,w) % % xY - word structure array % w - indices of words in VOX.LEX to consi...

### Highest Data Gravity (Database Complexity)
- `serialize_jsonld` (@ `spm_provenance.m`) -> DB Complexity: **209**
- `mrqcof` (@ `src/spm_brainwarp.c`) -> DB Complexity: **204**
- `kernel` (@ `src/shoot_regularisers.c`) -> DB Complexity: **181**
- `load_curry_data_file` (@ `external/fieldtrip/fileio/private/load_curry_data_file.m`) -> DB Complexity: **171**
- `smalldef_objfun_mn` (@ `src/shoot_dartel.c`) -> DB Complexity: **155**
- `relax_all` (@ `src/shoot_regularisers.c`) -> DB Complexity: **154**
- `initialise_objfun_mn` (@ `src/shoot_dartel.c`) -> DB Complexity: **153**
- `pushc_grads` (@ `src/shoot_diffeo3d.c`) -> DB Complexity: **152**
- `composition_stuff` (@ `src/shoot_diffeo3d.c`) -> DB Complexity: **150**
  * *Intent:* /* Compute Lie bracket */
- `Cii_linear` (@ `external/bemcp/bem_Cii_lin.c`) -> DB Complexity: **145**
  * *Intent:* */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 741 | 161133.5 | 66.99% | 26.66% |
| `src` | 72 | 42582.82 | 54.77% | 22.44% |
| `toolbox/DEM` | 264 | 35322.23 | 53.08% | 31.17% |
| `config` | 117 | 21007.94 | 45.66% | 52.47% |
| `toolbox/dcm_meeg` | 107 | 15129.55 | 60.77% | 51.22% |
| `@nifti/private` | 21 | 14790.03 | 66.06% | 33.93% |
| `toolbox/FieldMap` | 37 | 12900.5 | 61.9% | 21.51% |
| `toolbox/MEEGtools` | 30 | 9505.42 | 74.03% | 35.56% |
| `toolbox/DAiSS` | 74 | 8960.54 | 56.94% | 46.49% |
| `toolbox/mci/inference` | 43 | 7908.41 | 63.06% | 15.12% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `@file_array/fieldnames.m` -> **100.0%** Exposure
- `@file_array/full.m` -> **100.0%** Exposure
- `@file_array/horzcat.m` -> **100.0%** Exposure
- `@file_array/private/mystruct.m` -> **100.0%** Exposure
- `@file_array/vertcat.m` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `@file_array/cat.m` -> **100.0%** Exposure
- `@file_array/double.m` -> **100.0%** Exposure
- `@file_array/end.m` -> **100.0%** Exposure
- `@file_array/file_array.m` -> **100.0%** Exposure
- `@file_array/horzcat.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/shoot_diffeo3d.c` -> **18** Orphaned Functions | **0** Duplicates
- `@nifti/private/nifti_stats.c` -> **13** Orphaned Functions | **0** Duplicates
- `bin/spm12-matlab` -> **2** Orphaned Functions | **5** Duplicates
- `toolbox/dcm_meeg/spm_api_erp.m` -> **6** Orphaned Functions | **0** Duplicates
- `src/spm_getdata.c` -> **6** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`external/fieldtrip/src/rfbevent.c`** -> AI Confidence: **99.48%**
2. **`src/shoot_dartel.c`** -> AI Confidence: **99.48%**
3. **`src/spm_diffeo.c`** -> AI Confidence: **99.48%**
4. **`src/spm_mapping.c`** -> AI Confidence: **99.48%**
5. **`@file_array/private/init.c`** -> AI Confidence: **99.39%**
6. **`@file_array/private/file2mat.c`** -> AI Confidence: **99.35%**
7. **`@nifti/private/nifti_stats.c`** -> AI Confidence: **99.34%**
8. **`@nifti/private/nifti_stats_mex.c`** -> AI Confidence: **99.34%**
9. **`external/eeprobe/read_eep_cnt.c`** -> AI Confidence: **99.34%**
10. **`external/eeprobe/write_eep_avr.c`** -> AI Confidence: **99.34%**
11. **`external/eeprobe/write_eep_cnt.c`** -> AI Confidence: **99.34%**
12. **`external/fieldtrip/src/nanmean.c`** -> AI Confidence: **99.34%**
13. **`external/fieldtrip/src/nanstd.c`** -> AI Confidence: **99.34%**
14. **`external/fieldtrip/src/nansum.c`** -> AI Confidence: **99.34%**
15. **`external/fieldtrip/src/nanvar.c`** -> AI Confidence: **99.34%**
16. **`src/shoot_diffeo3d.c`** -> AI Confidence: **99.34%**
17. **`src/shoot_optim3d.c`** -> AI Confidence: **99.34%**
18. **`src/spm_field.c`** -> AI Confidence: **99.34%**
19. **`src/spm_jsonread.c`** -> AI Confidence: **99.34%**
20. **`toolbox/FieldMap/pm_create_connectogram_dtj.c`** -> AI Confidence: **99.34%**
21. **`toolbox/FieldMap/pm_estimate_ramp.c`** -> AI Confidence: **99.34%**
22. **`toolbox/FieldMap/pm_merge_regions.c`** -> AI Confidence: **99.34%**
23. **`toolbox/FieldMap/pm_restore_ramp.c`** -> AI Confidence: **99.34%**
24. **`external/fieldtrip/src/inv3x3.c`** -> AI Confidence: **99.32%**
25. **`external/fieldtrip/src/lmoutr.c`** -> AI Confidence: **99.32%**
26. **`external/fieldtrip/src/ltrisect.c`** -> AI Confidence: **99.32%**
27. **`external/fieldtrip/src/meg_leadfield1.c`** -> AI Confidence: **99.32%**
28. **`external/fieldtrip/src/plinproj.c`** -> AI Confidence: **99.32%**
29. **`external/fieldtrip/src/ptriproj.c`** -> AI Confidence: **99.32%**
30. **`external/fieldtrip/src/routlm.c`** -> AI Confidence: **99.32%**
31. **`external/fieldtrip/src/solid_angle.c`** -> AI Confidence: **99.32%**
32. **`src/shoot_bsplines.c`** -> AI Confidence: **99.32%**
33. **`src/shoot_regularisers.c`** -> AI Confidence: **99.32%**
34. **`src/spm_add.c`** -> AI Confidence: **99.32%**
35. **`src/spm_brainwarp.c`** -> AI Confidence: **99.32%**
36. **`src/spm_bsplins.c`** -> AI Confidence: **99.32%**
37. **`src/spm_hist2.c`** -> AI Confidence: **99.32%**
38. **`src/spm_krutil.c`** -> AI Confidence: **99.32%**
39. **`src/spm_project.c`** -> AI Confidence: **99.32%**
40. **`src/spm_render_vol.c`** -> AI Confidence: **99.32%**
41. **`src/spm_resels_vol.c`** -> AI Confidence: **99.32%**
42. **`src/spm_unlink.c`** -> AI Confidence: **99.32%**
43. **`src/spm_unvec.c`** -> AI Confidence: **99.32%**
44. **`src/spm_vec.c`** -> AI Confidence: **99.32%**
45. **`src/spm_voronoi.c`** -> AI Confidence: **99.32%**
46. **`external/fieldtrip/src/combineClusters.cpp`** -> AI Confidence: **99.32%**
47. **`@file_array/private/mat2file.c`** -> AI Confidence: **99.31%**
48. **`@gifti/private/miniz.c`** -> AI Confidence: **99.31%**
49. **`src/Simplify.h`** -> AI Confidence: **99.31%**
50. **`@file_array/initialise.m`** -> AI Confidence: **99.29%**
51. **`@file_array/private/dim.m`** -> AI Confidence: **99.29%**
52. **`@file_array/private/offset.m`** -> AI Confidence: **99.29%**
53. **`@gifti/fieldnames.m`** -> AI Confidence: **99.29%**
54. **`@gifti/saveas.m`** -> AI Confidence: **99.29%**
55. **`@nifti/private/decode_qform0.m`** -> AI Confidence: **99.29%**
56. **`@nifti/private/encode_qform0.m`** -> AI Confidence: **99.29%**
57. **`@nifti/private/niftistruc.m`** -> AI Confidence: **99.29%**
58. **`bin/spm12-octave`** -> AI Confidence: **99.29%**
59. **`compat/spm_eeval.m`** -> AI Confidence: **99.29%**
60. **`compat/spm_matlab_version_chk.m`** -> AI Confidence: **99.29%**
61. **`config/spm_cfg_bbox.m`** -> AI Confidence: **99.29%**
62. **`config/spm_cfg_bms_map.m`** -> AI Confidence: **99.29%**
63. **`config/spm_cfg_cat.m`** -> AI Confidence: **99.29%**
64. **`config/spm_cfg_checkreg.m`** -> AI Confidence: **99.29%**
65. **`config/spm_cfg_coreg.m`** -> AI Confidence: **99.29%**
66. **`config/spm_cfg_dcm_bms.m`** -> AI Confidence: **99.29%**
67. **`config/spm_cfg_dicom.m`** -> AI Confidence: **99.29%**
68. **`config/spm_cfg_eeg_average.m`** -> AI Confidence: **99.29%**
69. **`config/spm_cfg_eeg_contrast.m`** -> AI Confidence: **99.29%**
70. **`config/spm_cfg_eeg_convert2images.m`** -> AI Confidence: **99.29%**
71. **`config/spm_cfg_eeg_firstlevel.m`** -> AI Confidence: **99.29%**
72. **`config/spm_cfg_eeg_merge.m`** -> AI Confidence: **99.29%**
73. **`config/spm_cfg_eeg_montage.m`** -> AI Confidence: **99.29%**
74. **`config/spm_cfg_fmri_data.m`** -> AI Confidence: **99.29%**
75. **`config/spm_cfg_fmri_design.m`** -> AI Confidence: **99.29%**
76. **`config/spm_cfg_fmri_est.m`** -> AI Confidence: **99.29%**
77. **`config/spm_cfg_opm_create.m`** -> AI Confidence: **99.29%**
78. **`config/spm_cfg_opm_synth_gradiometer.m`** -> AI Confidence: **99.29%**
79. **`config/spm_cfg_ppi.m`** -> AI Confidence: **99.29%**
80. **`config/spm_cfg_realignunwarp.m`** -> AI Confidence: **99.29%**
81. **`config/spm_cfg_reorient.m`** -> AI Confidence: **99.29%**
82. **`config/spm_cfg_smooth.m`** -> AI Confidence: **99.29%**
83. **`config/spm_cfg_split.m`** -> AI Confidence: **99.29%**
84. **`config/spm_cfg_st.m`** -> AI Confidence: **99.29%**
85. **`config/spm_cfg_tissue_volumes.m`** -> AI Confidence: **99.29%**
86. **`config/spm_cfg_voi.m`** -> AI Confidence: **99.29%**
87. **`external/fieldtrip/connectivity/private/det2x2.m`** -> AI Confidence: **99.29%**
88. **`external/fieldtrip/connectivity/private/inv2x2.m`** -> AI Confidence: **99.29%**
89. **`external/fieldtrip/connectivity/private/standardise.m`** -> AI Confidence: **99.29%**
90. **`external/fieldtrip/fileio/ft_chanunit.m`** -> AI Confidence: **99.29%**
91. **`external/fieldtrip/fileio/ft_filetype.m`** -> AI Confidence: **99.29%**
92. **`external/fieldtrip/fileio/ft_filter_event.m`** -> AI Confidence: **99.29%**
93. **`external/fieldtrip/fileio/ft_read_headmodel.m`** -> AI Confidence: **99.29%**
94. **`external/fieldtrip/fileio/private/ft_datatype.m`** -> AI Confidence: **99.29%**
95. **`external/fieldtrip/fileio/private/ft_determine_units.m`** -> AI Confidence: **99.29%**
96. **`external/fieldtrip/fileio/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
97. **`external/fieldtrip/fileio/private/ft_senstype.m`** -> AI Confidence: **99.29%**
98. **`external/fieldtrip/fileio/private/ft_warp_apply.m`** -> AI Confidence: **99.29%**
99. **`external/fieldtrip/fileio/private/in_fread_manscan.m`** -> AI Confidence: **99.29%**
100. **`external/fieldtrip/fileio/private/ndgrid.m`** -> AI Confidence: **99.29%**
101. **`external/fieldtrip/fileio/private/yokogawa2headmodel.m`** -> AI Confidence: **99.29%**
102. **`external/fieldtrip/forward/ft_determine_units.m`** -> AI Confidence: **99.29%**
103. **`external/fieldtrip/forward/ft_headmodel_infinite.m`** -> AI Confidence: **99.29%**
104. **`external/fieldtrip/forward/ft_senstype.m`** -> AI Confidence: **99.29%**
105. **`external/fieldtrip/forward/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
106. **`external/fieldtrip/forward/private/ft_warp_apply.m`** -> AI Confidence: **99.29%**
107. **`external/fieldtrip/ft_artifact_tms.m`** -> AI Confidence: **99.29%**
108. **`external/fieldtrip/ft_statistics_analytic.m`** -> AI Confidence: **99.29%**
109. **`external/fieldtrip/inverse/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
110. **`external/fieldtrip/inverse/private/ft_senstype.m`** -> AI Confidence: **99.29%**
111. **`external/fieldtrip/plotting/private/coordsys2label.m`** -> AI Confidence: **99.29%**
112. **`external/fieldtrip/plotting/private/ft_determine_units.m`** -> AI Confidence: **99.29%**
113. **`external/fieldtrip/plotting/private/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
114. **`external/fieldtrip/plotting/private/ft_senstype.m`** -> AI Confidence: **99.29%**
115. **`external/fieldtrip/plotting/private/ft_warp_apply.m`** -> AI Confidence: **99.29%**
116. **`external/fieldtrip/plotting/private/intersect_plane.m`** -> AI Confidence: **99.29%**
117. **`external/fieldtrip/plotting/private/ndgrid.m`** -> AI Confidence: **99.29%**
118. **`external/fieldtrip/preproc/ft_preproc_hilbert.m`** -> AI Confidence: **99.29%**
119. **`external/fieldtrip/private/char2rgb.m`** -> AI Confidence: **99.29%**
120. **`external/fieldtrip/private/coordsys2label.m`** -> AI Confidence: **99.29%**
121. **`external/fieldtrip/private/dimnum.m`** -> AI Confidence: **99.29%**
122. **`external/fieldtrip/private/fixcoordsys.m`** -> AI Confidence: **99.29%**
123. **`external/fieldtrip/private/ft_fetch_sens.m`** -> AI Confidence: **99.29%**
124. **`external/fieldtrip/private/ft_getuserfun.m`** -> AI Confidence: **99.29%**
125. **`external/fieldtrip/private/grid2transform.m`** -> AI Confidence: **99.29%**
126. **`external/fieldtrip/private/ignorefields.m`** -> AI Confidence: **99.29%**
127. **`external/fieldtrip/private/ismatch.m`** -> AI Confidence: **99.29%**
128. **`external/fieldtrip/private/isrealmat.m`** -> AI Confidence: **99.29%**
129. **`external/fieldtrip/private/isrealvec.m`** -> AI Confidence: **99.29%**
130. **`external/fieldtrip/private/ndgrid.m`** -> AI Confidence: **99.29%**
131. **`external/fieldtrip/private/print_tim.m`** -> AI Confidence: **99.29%**
132. **`external/fieldtrip/private/read_besa_src.m`** -> AI Confidence: **99.29%**
133. **`external/fieldtrip/private/setviewpoint.m`** -> AI Confidence: **99.29%**
134. **`external/fieldtrip/private/smartinput.m`** -> AI Confidence: **99.29%**
135. **`external/fieldtrip/private/standardise.m`** -> AI Confidence: **99.29%**
136. **`external/fieldtrip/private/swapmemfile.m`** -> AI Confidence: **99.29%**
137. **`external/fieldtrip/private/transform2grid.m`** -> AI Confidence: **99.29%**
138. **`external/fieldtrip/src/det2x2.m`** -> AI Confidence: **99.29%**
139. **`external/fieldtrip/src/inv2x2.m`** -> AI Confidence: **99.29%**
140. **`external/fieldtrip/trialfun/private/ismatch.m`** -> AI Confidence: **99.29%**
141. **`external/fieldtrip/utilities/ft_datatype.m`** -> AI Confidence: **99.29%**
142. **`external/fieldtrip/utilities/ft_hastoolbox.m`** -> AI Confidence: **99.29%**
143. **`external/fieldtrip/utilities/ft_warp_apply.m`** -> AI Confidence: **99.29%**
144. **`external/fieldtrip/utilities/private/coordsys2label.m`** -> AI Confidence: **99.29%**
145. **`external/fieldtrip/utilities/private/ignorefields.m`** -> AI Confidence: **99.29%**
146. **`external/fieldtrip/utilities/private/smartinput.m`** -> AI Confidence: **99.29%**
147. **`matlabbatch/@cfg_choice/subsasgn_check.m`** -> AI Confidence: **99.29%**
148. **`matlabbatch/@cfg_item/all_set.m`** -> AI Confidence: **99.29%**
149. **`matlabbatch/@cfg_mchoice/subsasgn_check.m`** -> AI Confidence: **99.29%**
150. **`matlabbatch/@cfg_repeat/all_set_item.m`** -> AI Confidence: **99.29%**
151. **`matlabbatch/@cfg_repeat/subsasgn_check.m`** -> AI Confidence: **99.29%**
152. **`matlabbatch/cfg_basicio/cfg_basicio_rewrite.m`** -> AI Confidence: **99.29%**
153. **`matlabbatch/cfg_basicio/cfg_cfg_basicio.m`** -> AI Confidence: **99.29%**
154. **`matlabbatch/cfg_basicio/cfg_check_assignin.m`** -> AI Confidence: **99.29%**
155. **`matlabbatch/cfg_basicio/cfg_run_file_fplist.m`** -> AI Confidence: **99.29%**
156. **`matlabbatch/cfg_basicio/cfg_vout_save_vars.m`** -> AI Confidence: **99.29%**
157. **`matlabbatch/cfg_basicio/src/01_file_dir_ops/01_dir_ops/batch_basicio_03_mkdir.m`** -> AI Confidence: **99.29%**
158. **`matlabbatch/cfg_basicio/src/01_file_dir_ops/01_dir_ops/batch_basicio_04_named_dir.m`** -> AI Confidence: **99.29%**
159. **`matlabbatch/cfg_basicio/src/01_file_dir_ops/02_file_ops/batch_basicio_01_file_move.m`** -> AI Confidence: **99.29%**
160. **`matlabbatch/cfg_basicio/src/01_file_dir_ops/02_file_ops/batch_basicio_05_named_file.m`** -> AI Confidence: **99.29%**
161. **`matlabbatch/cfg_basicio/src/01_file_dir_ops/02_file_ops/batch_basicio_07_file_filter.m`** -> AI Confidence: **99.29%**
162. **`matlabbatch/cfg_basicio/src/01_file_dir_ops/02_file_ops/batch_basicio_09_file_split.m`** -> AI Confidence: **99.29%**
163. **`matlabbatch/cfg_basicio/src/02_var_ops/batch_basicio_10_named_input.m`** -> AI Confidence: **99.29%**
164. **`matlabbatch/cfg_basicio/src/02_var_ops/batch_basicio_12_save_vars.m`** -> AI Confidence: **99.29%**
165. **`matlabbatch/cfg_basicio/src/02_var_ops/batch_basicio_14_assignin.m`** -> AI Confidence: **99.29%**
166. **`matlabbatch/cfg_basicio/src/03_run_ops/batch_basicio_15_runjobs.m`** -> AI Confidence: **99.29%**
167. **`matlabbatch/cfg_dbstop.m`** -> AI Confidence: **99.29%**
168. **`matlabbatch/private/cfg_run_cm.m`** -> AI Confidence: **99.29%**
169. **`matlabbatch/subsasgn_check_num.m`** -> AI Confidence: **99.29%**
170. **`spm_ECdensity.m`** -> AI Confidence: **99.29%**
171. **`spm_Ncdf_jdw.m`** -> AI Confidence: **99.29%**
172. **`spm_P.m`** -> AI Confidence: **99.29%**
173. **`spm_P_RF.m`** -> AI Confidence: **99.29%**
174. **`spm_SpUtil.m`** -> AI Confidence: **99.29%**
175. **`spm_XYZreg_Ex2.m`** -> AI Confidence: **99.29%**
176. **`spm_affine_priors.m`** -> AI Confidence: **99.29%**
177. **`spm_clusters.m`** -> AI Confidence: **99.29%**
178. **`spm_dcm_fmri_mar.m`** -> AI Confidence: **99.29%**
179. **`spm_dcm_fmri_nmm.m`** -> AI Confidence: **99.29%**
180. **`spm_eeg_project3D.m`** -> AI Confidence: **99.29%**
181. **`spm_gx_fmri_linear.m`** -> AI Confidence: **99.29%**
182. **`spm_help.m`** -> AI Confidence: **99.29%**
183. **`spm_log_evidence_reduce.m`** -> AI Confidence: **99.29%**
184. **`spm_mesh_adjacency.m`** -> AI Confidence: **99.29%**
185. **`spm_mesh_geodesic.m`** -> AI Confidence: **99.29%**
186. **`spm_mesh_isoline.m`** -> AI Confidence: **99.29%**
187. **`spm_mesh_polyhedron.m`** -> AI Confidence: **99.29%**
188. **`spm_mesh_sphere.m`** -> AI Confidence: **99.29%**
189. **`spm_mip.m`** -> AI Confidence: **99.29%**
190. **`spm_mvNpdf.m`** -> AI Confidence: **99.29%**
191. **`spm_progress_bar.m`** -> AI Confidence: **99.29%**
192. **`spm_resels.m`** -> AI Confidence: **99.29%**
193. **`spm_smoothkern.m`** -> AI Confidence: **99.29%**
194. **`spm_softmax.m`** -> AI Confidence: **99.29%**
195. **`spm_speye.m`** -> AI Confidence: **99.29%**
196. **`spm_spy.m`** -> AI Confidence: **99.29%**
197. **`spm_u.m`** -> AI Confidence: **99.29%**
198. **`spm_uw_show.m`** -> AI Confidence: **99.29%**
199. **`spm_vb_spatial_precision.m`** -> AI Confidence: **99.29%**
200. **`spm_vol_nifti.m`** -> AI Confidence: **99.29%**
201. **`spm_z2p.m`** -> AI Confidence: **99.29%**
202. **`toolbox/DEM/ADEM_occlusion.m`** -> AI Confidence: **99.29%**
203. **`toolbox/DEM/ADEM_writing.m`** -> AI Confidence: **99.29%**
204. **`toolbox/DEM/DEM_demo_Bayesian_Model_Reduction.m`** -> AI Confidence: **99.29%**
205. **`toolbox/DEM/spm_voice_Q.m`** -> AI Confidence: **99.29%**
206. **`toolbox/DEM/spm_voice_filter.m`** -> AI Confidence: **99.29%**
207. **`toolbox/DEM/spm_voice_iQ.m`** -> AI Confidence: **99.29%**
208. **`toolbox/FieldMap/tbx_cfg_fieldmap.m`** -> AI Confidence: **99.29%**
209. **`toolbox/MEEGtools/spm_create_labels.m`** -> AI Confidence: **99.29%**
210. **`toolbox/NVC/spm_dcm_nvc.m`** -> AI Confidence: **99.29%**
211. **`toolbox/NVC/spm_dcm_nvc_priors.m`** -> AI Confidence: **99.29%**
212. **`toolbox/Neural_Models/NMDA_NMM_MFM/spm_dcm_x_neural_NMDA.m`** -> AI Confidence: **99.29%**
213. **`toolbox/Neural_Models/spm_demo_proceed.m`** -> AI Confidence: **99.29%**
214. **`toolbox/OldNorm/spm_cfg_normalise.m`** -> AI Confidence: **99.29%**
215. **`toolbox/Shoot/tbx_cfg_shoot.m`** -> AI Confidence: **99.29%**
216. **`toolbox/TSSS/tsss_config.m`** -> AI Confidence: **99.29%**
217. **`toolbox/dcm_meeg/spm_dcm_nfm.m`** -> AI Confidence: **99.29%**
218. **`toolbox/dcm_meeg/spm_dcm_tfm.m`** -> AI Confidence: **99.29%**
219. **`toolbox/dcm_meeg/spm_dcm_x_neural.m`** -> AI Confidence: **99.29%**
220. **`toolbox/dcm_meeg/spm_ssr_priors.m`** -> AI Confidence: **99.29%**
221. **`toolbox/mci/demo-thermodynamic/mci_demo_ramsay_surface.m`** -> AI Confidence: **99.29%**
222. **`toolbox/mci/inference/spm_mci_like_ind.m`** -> AI Confidence: **99.29%**
223. **`toolbox/mci/models/discount/mci_discount_struct.m`** -> AI Confidence: **99.29%**
224. **`toolbox/mci/models/logistic/mci_logistic_struct.m`** -> AI Confidence: **99.29%**
225. **`toolbox/spectral/spm_ccf2gew.m`** -> AI Confidence: **99.29%**
226. **`toolbox/spectral/spm_rar_demo.m`** -> AI Confidence: **99.29%**
227. **`external/fieldtrip/fileio/private/read_ah5_markers.m`** -> AI Confidence: **99.29%**
228. **`toolbox/mci/demo-models/mci_demo_growth.m`** -> AI Confidence: **99.29%**
229. **`@gifti/private/Makefile`** -> AI Confidence: **99.29%**
230. **`@gifti/private/zstream.c`** -> AI Confidence: **99.29%**
231. **`@xmltree/private/xml_findstr.c`** -> AI Confidence: **99.29%**
232. **`external/bemcp/bem_Cii_cog.c`** -> AI Confidence: **99.29%**
233. **`external/bemcp/bem_Cii_cst.c`** -> AI Confidence: **99.29%**
234. **`external/bemcp/bem_Cii_lin.c`** -> AI Confidence: **99.29%**
235. **`external/bemcp/bem_Cij_cog.c`** -> AI Confidence: **99.29%**
236. **`external/bemcp/bem_Cij_cst.c`** -> AI Confidence: **99.29%**
237. **`external/bemcp/bem_Cij_lin.c`** -> AI Confidence: **99.29%**
238. **`external/bemcp/bem_Gi_cog.c`** -> AI Confidence: **99.29%**
239. **`external/bemcp/bem_Gi_vert.c`** -> AI Confidence: **99.29%**
240. **`external/eeprobe/read_eep_avr.c`** -> AI Confidence: **99.29%**
241. **`external/fieldtrip/src/ft_getopt.c`** -> AI Confidence: **99.29%**
242. **`external/fieldtrip/src/ft_spike_sub_crossx.c`** -> AI Confidence: **99.29%**
243. **`external/fieldtrip/src/mtimes3x3.c`** -> AI Confidence: **99.29%**
244. **`external/fieldtrip/src/nanaccum.c`** -> AI Confidence: **99.29%**
245. **`external/fieldtrip/src/sandwich2x2.c`** -> AI Confidence: **99.29%**
246. **`external/fieldtrip/src/sandwich3x3.c`** -> AI Confidence: **99.29%**
247. **`external/fieldtrip/src/splint_gh.c`** -> AI Confidence: **99.29%**
248. **`src/hist2.c`** -> AI Confidence: **99.29%**
249. **`src/shoot_invdef.c`** -> AI Confidence: **99.29%**
250. **`src/shoot_optimN.c`** -> AI Confidence: **99.29%**
251. **`src/spm_bsplinc.c`** -> AI Confidence: **99.29%**
252. **`src/spm_bwlabel.c`** -> AI Confidence: **99.29%**
253. **`src/spm_conv_vol.c`** -> AI Confidence: **99.29%**
254. **`src/spm_dilate_erode.c`** -> AI Confidence: **99.29%**
255. **`src/spm_gamrnd.c`** -> AI Confidence: **99.29%**
256. **`src/spm_global.c`** -> AI Confidence: **99.29%**
257. **`src/spm_make_lookup.c`** -> AI Confidence: **99.29%**
258. **`src/spm_matfuns.c`** -> AI Confidence: **99.29%**
259. **`src/spm_mesh_utils.c`** -> AI Confidence: **99.29%**
260. **`src/spm_mrf.c`** -> AI Confidence: **99.29%**
261. **`src/spm_sample_vol.c`** -> AI Confidence: **99.29%**
262. **`src/spm_slice_vol.c`** -> AI Confidence: **99.29%**
263. **`src/spm_vol_utils.c`** -> AI Confidence: **99.29%**
264. **`toolbox/FieldMap/pm_ff_unwrap.c`** -> AI Confidence: **99.29%**
265. **`toolbox/FieldMap/pm_invert_phasemap_dtj.c`** -> AI Confidence: **99.29%**
266. **`toolbox/FieldMap/pm_pad.c`** -> AI Confidence: **99.29%**
267. **`external/fieldtrip/src/platform.h`** -> AI Confidence: **99.29%**
268. **`src/spm_mesh_reduce.cpp`** -> AI Confidence: **99.29%**
269. **`external/fieldtrip/src/read_24bit.c`** -> AI Confidence: **99.23%**
270. **`src/spm_mex.h`** -> AI Confidence: **99.23%**
271. **`external/fieldtrip/src/compiler.h`** -> AI Confidence: **99.23%**
272. **`src/shoot_multiscale.c`** -> AI Confidence: **99.2%**
273. **`src/spm_cat.c`** -> AI Confidence: **99.2%**
274. **`@file_array/file_array.m`** -> AI Confidence: **99.17%**
275. **`@file_array/private/fname.m`** -> AI Confidence: **99.17%**
276. **`@file_array/private/permission.m`** -> AI Confidence: **99.17%**
277. **`@file_array/private/scl_inter.m`** -> AI Confidence: **99.17%**
278. **`@file_array/private/scl_slope.m`** -> AI Confidence: **99.17%**
279. **`@file_array/reshape.m`** -> AI Confidence: **99.17%**
280. **`@gifti/gifti.m`** -> AI Confidence: **99.17%**
281. **`@gifti/private/read_freesurfer_file.m`** -> AI Confidence: **99.17%**
282. **`@gifti/private/zstream.m`** -> AI Confidence: **99.17%**
283. **`@meeg/fiducials.m`** -> AI Confidence: **99.17%**
284. **`@meeg/meeg.m`** -> AI Confidence: **99.17%**
285. **`@meeg/montage.m`** -> AI Confidence: **99.17%**
286. **`@meeg/save.m`** -> AI Confidence: **99.17%**
287. **`@meeg/transformtype.m`** -> AI Confidence: **99.17%**
288. **`@meeg/type.m`** -> AI Confidence: **99.17%**
289. **`@nifti/private/M2Q.m`** -> AI Confidence: **99.17%**
290. **`@slover/private/mars_struct.m`** -> AI Confidence: **99.17%**
291. **`@xmltree/private/xml_findstr.m`** -> AI Confidence: **99.17%**
292. **`@xmltree/save.m`** -> AI Confidence: **99.17%**
293. **`@xmltree/xmltree.m`** -> AI Confidence: **99.17%**
294. **`compat/spm_resss.m`** -> AI Confidence: **99.17%**
295. **`config/spm_cfg_dcm_est.m`** -> AI Confidence: **99.17%**
296. **`config/spm_cfg_eeg_channel_selector.m`** -> AI Confidence: **99.17%**
297. **`config/spm_cfg_eeg_dipfit.m`** -> AI Confidence: **99.17%**
298. **`config/spm_cfg_eeg_inv_headmodelhelmet.m`** -> AI Confidence: **99.17%**
299. **`config/spm_cfg_eeg_inv_post.m`** -> AI Confidence: **99.17%**
300. **`config/spm_cfg_eeg_momentfit.m`** -> AI Confidence: **99.17%**
301. **`config/spm_cfg_eeg_spatial_confounds.m`** -> AI Confidence: **99.17%**
302. **`config/spm_cfg_eeg_tf_rescale.m`** -> AI Confidence: **99.17%**
303. **`config/spm_cfg_imcalc.m`** -> AI Confidence: **99.17%**
304. **`config/spm_cfg_minc.m`** -> AI Confidence: **99.17%**
305. **`config/spm_run_results.m`** -> AI Confidence: **99.17%**
306. **`external/fieldtrip/besa2fieldtrip.m`** -> AI Confidence: **99.17%**
307. **`external/fieldtrip/connectivity/ft_connectivity_mim.m`** -> AI Confidence: **99.17%**
308. **`external/fieldtrip/connectivity/private/ft_platform_supports.m`** -> AI Confidence: **99.17%**
309. **`external/fieldtrip/connectivity/private/ft_warning.m`** -> AI Confidence: **99.17%**
310. **`external/fieldtrip/connectivity/private/istrue.m`** -> AI Confidence: **99.17%**
311. **`external/fieldtrip/external/images/rgb2hsv.m`** -> AI Confidence: **99.17%**
312. **`external/fieldtrip/external/signal/butter.m`** -> AI Confidence: **99.17%**
313. **`external/fieldtrip/external/signal/private/bilinear.m`** -> AI Confidence: **99.17%**
314. **`external/fieldtrip/external/signal/triang.m`** -> AI Confidence: **99.17%**
315. **`external/fieldtrip/external/stats/betapdf.m`** -> AI Confidence: **99.17%**
316. **`external/fieldtrip/fileio/ft_chantype.m`** -> AI Confidence: **99.17%**
317. **`external/fieldtrip/fileio/ft_flush_data.m`** -> AI Confidence: **99.17%**
318. **`external/fieldtrip/fileio/ft_flush_event.m`** -> AI Confidence: **99.17%**
319. **`external/fieldtrip/fileio/ft_flush_header.m`** -> AI Confidence: **99.17%**
320. **`external/fieldtrip/fileio/ft_write_mri.m`** -> AI Confidence: **99.17%**
321. **`external/fieldtrip/fileio/ft_write_sens.m`** -> AI Confidence: **99.17%**
322. **`external/fieldtrip/fileio/private/bounding_mesh.m`** -> AI Confidence: **99.17%**
323. **`external/fieldtrip/fileio/private/cstructdecode.m`** -> AI Confidence: **99.17%**
324. **`external/fieldtrip/fileio/private/db_select.m`** -> AI Confidence: **99.17%**
325. **`external/fieldtrip/fileio/private/decode_nifti1.m`** -> AI Confidence: **99.17%**
326. **`external/fieldtrip/fileio/private/fixdimord.m`** -> AI Confidence: **99.17%**
327. **`external/fieldtrip/fileio/private/ft_convert_units.m`** -> AI Confidence: **99.17%**
328. **`external/fieldtrip/fileio/private/ft_datatype_headmodel.m`** -> AI Confidence: **99.17%**
329. **`external/fieldtrip/fileio/private/ft_datatype_sens.m`** -> AI Confidence: **99.17%**
330. **`external/fieldtrip/fileio/private/ft_estimate_units.m`** -> AI Confidence: **99.17%**
331. **`external/fieldtrip/fileio/private/ft_headcoordinates.m`** -> AI Confidence: **99.17%**
332. **`external/fieldtrip/fileio/private/ft_headmodeltype.m`** -> AI Confidence: **99.17%**
333. **`external/fieldtrip/fileio/private/ft_platform_supports.m`** -> AI Confidence: **99.17%**
334. **`external/fieldtrip/fileio/private/ft_warning.m`** -> AI Confidence: **99.17%**
335. **`external/fieldtrip/fileio/private/getdimord.m`** -> AI Confidence: **99.17%**
336. **`external/fieldtrip/fileio/private/hasyokogawa.m`** -> AI Confidence: **99.17%**
337. **`external/fieldtrip/fileio/private/istrue.m`** -> AI Confidence: **99.17%**
338. **`external/fieldtrip/fileio/private/loadvar.m`** -> AI Confidence: **99.17%**
339. **`external/fieldtrip/fileio/private/neuralynx_timestamp.m`** -> AI Confidence: **99.17%**
340. **`external/fieldtrip/fileio/private/normals.m`** -> AI Confidence: **99.17%**
341. **`external/fieldtrip/fileio/private/np_readdata.m`** -> AI Confidence: **99.17%**
342. **`external/fieldtrip/fileio/private/read_asa_bnd.m`** -> AI Confidence: **99.17%**
343. **`external/fieldtrip/fileio/private/read_asa_elc.m`** -> AI Confidence: **99.17%**
344. **`external/fieldtrip/fileio/private/read_asa_mri.m`** -> AI Confidence: **99.17%**
345. **`external/fieldtrip/fileio/private/read_asa_msr.m`** -> AI Confidence: **99.17%**
346. **`external/fieldtrip/fileio/private/read_biff.m`** -> AI Confidence: **99.17%**
347. **`external/fieldtrip/fileio/private/read_eyelink_asc.m`** -> AI Confidence: **99.17%**
348. **`external/fieldtrip/fileio/private/read_micromed_event.m`** -> AI Confidence: **99.17%**
349. **`external/fieldtrip/fileio/private/read_micromed_trc.m`** -> AI Confidence: **99.17%**
350. **`external/fieldtrip/fileio/private/read_neuralynx_nts.m`** -> AI Confidence: **99.17%**
351. **`external/fieldtrip/fileio/private/read_neuromag_hc.m`** -> AI Confidence: **99.17%**
352. **`external/fieldtrip/fileio/private/read_neuroshare.m`** -> AI Confidence: **99.17%**
353. **`external/fieldtrip/fileio/private/read_nifti2_hdr.m`** -> AI Confidence: **99.17%**
354. **`external/fieldtrip/fileio/private/read_tdt_sev.m`** -> AI Confidence: **99.17%**
355. **`external/fieldtrip/fileio/private/read_tdt_tev.m`** -> AI Confidence: **99.17%**
356. **`external/fieldtrip/fileio/private/timestamp_neuralynx.m`** -> AI Confidence: **99.17%**
357. **`external/fieldtrip/fileio/private/write_gdf.m`** -> AI Confidence: **99.17%**
358. **`external/fieldtrip/fileio/private/write_ply.m`** -> AI Confidence: **99.17%**
359. **`external/fieldtrip/fileio/private/write_vtk.m`** -> AI Confidence: **99.17%**
360. **`external/fieldtrip/forward/ft_convert_units.m`** -> AI Confidence: **99.17%**
361. **`external/fieldtrip/forward/ft_estimate_units.m`** -> AI Confidence: **99.17%**
362. **`external/fieldtrip/forward/ft_headmodel_openmeeg.m`** -> AI Confidence: **99.17%**
363. **`external/fieldtrip/forward/ft_headmodel_singleshell.m`** -> AI Confidence: **99.17%**
364. **`external/fieldtrip/forward/ft_headmodeltype.m`** -> AI Confidence: **99.17%**
365. **`external/fieldtrip/forward/private/bounding_mesh.m`** -> AI Confidence: **99.17%**
366. **`external/fieldtrip/forward/private/eeg_leadfield4.m`** -> AI Confidence: **99.17%**
367. **`external/fieldtrip/forward/private/ft_datatype_headmodel.m`** -> AI Confidence: **99.17%**
368. **`external/fieldtrip/forward/private/ft_datatype_sens.m`** -> AI Confidence: **99.17%**
369. **`external/fieldtrip/forward/private/ft_headcoordinates.m`** -> AI Confidence: **99.17%**
370. **`external/fieldtrip/forward/private/ft_platform_supports.m`** -> AI Confidence: **99.17%**
371. **`external/fieldtrip/forward/private/ft_warning.m`** -> AI Confidence: **99.17%**
372. **`external/fieldtrip/forward/private/getdimord.m`** -> AI Confidence: **99.17%**
373. **`external/fieldtrip/forward/private/hasyokogawa.m`** -> AI Confidence: **99.17%**
374. **`external/fieldtrip/forward/private/headsurface.m`** -> AI Confidence: **99.17%**
375. **`external/fieldtrip/forward/private/istrue.m`** -> AI Confidence: **99.17%**
376. **`external/fieldtrip/forward/private/mesh2edge.m`** -> AI Confidence: **99.17%**
377. **`external/fieldtrip/forward/private/normals.m`** -> AI Confidence: **99.17%**
378. **`external/fieldtrip/forward/private/surfaceorientation.m`** -> AI Confidence: **99.17%**
379. **`external/fieldtrip/ft_appendfreq.m`** -> AI Confidence: **99.17%**
380. **`external/fieldtrip/ft_connectivityanalysis.m`** -> AI Confidence: **99.17%**
381. **`external/fieldtrip/ft_denoise_dssp.m`** -> AI Confidence: **99.17%**
382. **`external/fieldtrip/ft_freqsimulation.m`** -> AI Confidence: **99.17%**
383. **`external/fieldtrip/ft_meshrealign.m`** -> AI Confidence: **99.17%**
384. **`external/fieldtrip/ft_prepare_mesh.m`** -> AI Confidence: **99.17%**
385. **`external/fieldtrip/ft_singleplotTFR.m`** -> AI Confidence: **99.17%**
386. **`external/fieldtrip/ft_sourceanalysis.m`** -> AI Confidence: **99.17%**
387. **`external/fieldtrip/ft_sourcedescriptives.m`** -> AI Confidence: **99.17%**
388. **`external/fieldtrip/ft_sourceplot.m`** -> AI Confidence: **99.17%**
389. **`external/fieldtrip/ft_statistics_montecarlo.m`** -> AI Confidence: **99.17%**
390. **`external/fieldtrip/ft_statistics_stats.m`** -> AI Confidence: **99.17%**
391. **`external/fieldtrip/ft_volumerealign.m`** -> AI Confidence: **99.17%**
392. **`external/fieldtrip/ft_volumewrite.m`** -> AI Confidence: **99.17%**
393. **`external/fieldtrip/inverse/private/SAM_costfun.m`** -> AI Confidence: **99.17%**
394. **`external/fieldtrip/inverse/private/bounding_mesh.m`** -> AI Confidence: **99.17%**
395. **`external/fieldtrip/inverse/private/calctangent.m`** -> AI Confidence: **99.17%**
396. **`external/fieldtrip/inverse/private/fixdipole.m`** -> AI Confidence: **99.17%**
397. **`external/fieldtrip/inverse/private/ft_headmodeltype.m`** -> AI Confidence: **99.17%**
398. **`external/fieldtrip/inverse/private/ft_inv.m`** -> AI Confidence: **99.17%**
399. **`external/fieldtrip/inverse/private/ft_platform_supports.m`** -> AI Confidence: **99.17%**
400. **`external/fieldtrip/inverse/private/ft_warning.m`** -> AI Confidence: **99.17%**
401. **`external/fieldtrip/inverse/private/hasyokogawa.m`** -> AI Confidence: **99.17%**
402. **`external/fieldtrip/inverse/private/headsurface.m`** -> AI Confidence: **99.17%**
403. **`external/fieldtrip/plotting/ft_plot_axes.m`** -> AI Confidence: **99.17%**
404. **`external/fieldtrip/plotting/ft_plot_crosshair.m`** -> AI Confidence: **99.17%**
405. **`external/fieldtrip/plotting/ft_plot_mesh.m`** -> AI Confidence: **99.17%**
406. **`external/fieldtrip/plotting/ft_plot_montage.m`** -> AI Confidence: **99.17%**
407. **`external/fieldtrip/plotting/private/ft_convert_units.m`** -> AI Confidence: **99.17%**
408. **`external/fieldtrip/plotting/private/ft_datatype_sens.m`** -> AI Confidence: **99.17%**
409. **`external/fieldtrip/plotting/private/ft_estimate_units.m`** -> AI Confidence: **99.17%**
410. **`external/fieldtrip/plotting/private/ft_headmodeltype.m`** -> AI Confidence: **99.17%**
411. **`external/fieldtrip/plotting/private/ft_platform_supports.m`** -> AI Confidence: **99.17%**
412. **`external/fieldtrip/plotting/private/ft_warning.m`** -> AI Confidence: **99.17%**
413. **`external/fieldtrip/plotting/private/headsurface.m`** -> AI Confidence: **99.17%**
414. **`external/fieldtrip/plotting/private/istrue.m`** -> AI Confidence: **99.17%**
415. **`external/fieldtrip/plotting/private/mesh2edge.m`** -> AI Confidence: **99.17%**
416. **`external/fieldtrip/plotting/private/normals.m`** -> AI Confidence: **99.17%**
417. **`external/fieldtrip/plotting/private/surfaceorientation.m`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `@file_array/subsasgn.m` -> **100.0%** Exposure
- `@gifti/private/mvtk_write.m` -> **100.0%** Exposure
- `@gifti/subsasgn.m` -> **100.0%** Exposure
- `@meeg/clone.m` -> **100.0%** Exposure
- `@meeg/sensors.m` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `external/fieldtrip/fileio/ft_write_event.m` -> **100.0%** Exposure
- `external/fieldtrip/forward/ft_headmodel_dipoli.m` -> **100.0%** Exposure
- `external/fieldtrip/forward/ft_headmodel_fns.m` -> **100.0%** Exposure
- `external/fieldtrip/ft_volumewrite.m` -> **100.0%** Exposure
- `external/fieldtrip/utilities/ft_standalone.m` -> **100.0%** Exposure
### Raw Memory Manipulation
- `@nifti/private/nifti_stats.c` -> **10.0%** Exposure
- `@gifti/private/miniz.c` -> **5.0862%** Exposure
- `src/shoot_regularisers.c` -> **0.0304%** Exposure
- `external/fieldtrip/src/geometry.c` -> **0.0057%** Exposure
- `src/bsplines.c` -> **0.0002%** Exposure
### Hardcoded Payload Artifacts
- `external/fieldtrip/utilities/ft_trackusage.m` -> **99.9999%** Exposure
### Algorithmic DoS Exposure
- `@meeg/clone.m` -> **100.0%** Exposure
- `compat/loadxml.m` -> **100.0%** Exposure
- `compat/spm_fMRI_design_show.m` -> **100.0%** Exposure
- `config/spm_make_manual.m` -> **100.0%** Exposure
- `config/spm_run_realignunwarp.m` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `374` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `475` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `matlabbatch/private/cfg_disp_error.m` (MATLAB) -> Cumulative Risk: **873.29**
- **Archetype:** `file_cluster_17` (Distance: 17.844 IQR)
- **Magnitude:** 118.18 | **LOC:** 49 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `cfg_disp_error` (Impact: 80.5)

### 2. `@xmltree/private/xml_findstr.c` (C) -> Cumulative Risk: **792.77**
- **Archetype:** `file_cluster_8` (Distance: 13.732 IQR)
- **Magnitude:** 311.86 | **LOC:** 111 | **CtrlFlow:** 96.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9725%)
- **Heaviest Functions:** `mexFunction` (Impact: 205.5)

### 3. `matlabbatch/private/cfg_onscreen.m` (MATLAB) -> Cumulative Risk: **785.28**
- **Archetype:** `file_cluster_17` (Distance: 16.15 IQR)
- **Magnitude:** 77.08 | **LOC:** 41 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (99.8968%)
- **Heaviest Functions:** `cfg_onscreen` (Impact: 46.6)

### 4. `@xmltree/find.m` (MATLAB) -> Cumulative Risk: **783.42**
- **Archetype:** `file_cluster_17` (Distance: 17.906 IQR)
- **Magnitude:** 197.52 | **LOC:** 175 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.7061%)
- **Heaviest Functions:** `sub_pathfinder` (Impact: 58.1), `find` (Impact: 10.9), `sub_comp_element` (Impact: 10.4)

### 5. `external/fieldtrip/fileio/private/read_ahdf5_hdr.m` (MATLAB) -> Cumulative Risk: **777.67**
- **Archetype:** `file_cluster_8` (Distance: 13.001 IQR)
- **Magnitude:** 0.14 | **LOC:** 67 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9978%)
- **Heaviest Functions:** `read_ahdf5_hdr` (Impact: 65.8)

### 6. `toolbox/spectral/spm_mar2ccf.m` (MATLAB) -> Cumulative Risk: **775.21**
- **Archetype:** `file_cluster_8` (Distance: 13.861 IQR)
- **Magnitude:** 129.64 | **LOC:** 87 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.996%)
- **Heaviest Functions:** `spm_mar2ccf` (Impact: 59.7)

### 7. `external/fieldtrip/src/ft_getopt.c` (C) -> Cumulative Risk: **771.33**
- **Archetype:** `file_cluster_13` (Distance: 14.655 IQR)
- **Magnitude:** 0.22 | **LOC:** 127 | **CtrlFlow:** 94.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (96.5913%)
- **Heaviest Functions:** `mexFunction` (Impact: 147.5)

### 8. `compat/loadxml.m` (MATLAB) -> Cumulative Risk: **767.52**
- **Archetype:** `file_cluster_11` (Distance: 14.038 IQR)
- **Magnitude:** 234.56 | **LOC:** 150 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `loadxml` (Impact: 65.8), `xml_create_var` (Impact: 58.6)

### 9. `spm_dcm_delay.m` (MATLAB) -> Cumulative Risk: **766.36**
- **Archetype:** `file_cluster_8` (Distance: 14.081 IQR)
- **Magnitude:** 196.54 | **LOC:** 177 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9992%)
- **Heaviest Functions:** `spm_dcm_delay` (Impact: 78.0)

### 10. `src/spm_unlink.c` (C) -> Cumulative Risk: **753.87**
- **Archetype:** `file_cluster_13` (Distance: 12.525 IQR)
- **Magnitude:** 97.58 | **LOC:** 44 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9946%)
- **Heaviest Functions:** `mexFunction` (Impact: 62.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `@nifti/private/nifti_stats.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_12` (Drift: 15.514 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.461 IQR)
- **Top Global Matches:** file_cluster_12: 15.514, file_cluster_8: 15.655, file_cluster_11: 15.758
- **Magnitude:** 12930.36 | **LOC:** 11278 | **CtrlFlow:** 80.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (79.3691%), Tech Debt (10.4452%)
**Top Internal Functions/Classes:**
  * `E0000` (Impact: 929.0 | O(2^N) | DB: 73)
  * `cdfbin` (Impact: 534.4 | O(N^2) | DB: 87)
  * `cdfbet` (Impact: 510.6 | O(N^2) | DB: 88)
  * `cdfnbn` (Impact: 510.4 | O(N^2) | DB: 86)
  * `cdfgam` (Impact: 459.0 | O(N^3) | DB: 59)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1369`, `structural_boundaries: 327`, `args: 142`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `state_mutation: 4933`, `dead_code: 2`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 439`, `import: 6`
* *Defense:* `doc: 93`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, math.h, stdlib.h, ctype.h, nifti1.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_DisplayTimeSeries.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.307 IQR)
- **Top Global Matches:** file_cluster_8: 14.307, file_cluster_17: 14.358, file_cluster_11: 14.565
- **Magnitude:** 4462.84 | **LOC:** 545 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.0997%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 61`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 435`, `dead_code: 1`
* *Architecture:* None
* *Defense:* `safety: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/FieldMap/pm_segment.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.103 IQR)
- **Top Global Matches:** file_cluster_8: 14.103, file_cluster_17: 14.47, file_cluster_11: 14.511
- **Magnitude:** 4342.31 | **LOC:** 705 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (67.0941%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 69`, `args: 19`, `func_start: 19`
* *Risk/State:* `state_mutation: 567`
* *Architecture:* None
* *Defense:* `safety: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spm_diffeo.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.004 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_8: 14.004, file_cluster_13: 14.172, file_cluster_7: 14.33
- **Magnitude:** 3299.42 | **LOC:** 1180 | **CtrlFlow:** 93.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (86.5705%), Tech Debt (8.6936%)
**Top Internal Functions/Classes:**
  * `mexFunction` (Impact: 338.9 | O(N^3) | DB: 2)
  * `comp_mexFunction` (Impact: 239.6 | O(N^4) | DB: 39)
  * `pushc_grads_mexFunction` (Impact: 211.2 | O(N^4) | DB: 33)
  * `fmg3_mexFunction` (Impact: 165.7 | O(N^3) | DB: 37)
  * `push_mexFunction` (Impact: 135.6 | O(N^3) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 33`, `args: 30`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 908`, `orphaned_logic: 1`
* *Architecture:* `api: 120`, `import: 11`
* *Defense:* `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` mex.h, spm_openmp.h, shoot_diffeo3d.h, shoot_optim3d.h, string.h, math.h, shoot_bsplines.h, shoot_dartel.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_dartel.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.569 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.673 IQR)
- **Top Global Matches:** file_cluster_8: 14.569, file_cluster_13: 14.816, file_cluster_7: 14.889
- **Magnitude:** 2839.5 | **LOC:** 1565 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 155
- **Risk Profile:** Cognitive Load (64.6703%), Tech Debt (9.0367%)
**Top Internal Functions/Classes:**
  * `dartel_mexFunction` (Impact: 134.7 | O(N^3) | DB: 35)
  * `exp_mexFunction` (Impact: 68.5 | O(N^3) | DB: 23)
  * `unwrap` (Impact: 66.6 | O(N^5) | DB: 39)
  * `smalldef_objfun_mn` (Impact: 56.5 | O(N^6) | DB: 155)
  * `initialise_objfun_mn` (Impact: 44.5 | O(N^6) | DB: 153)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 29`, `args: 7`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 2038`, `orphaned_logic: 2`
* *Architecture:* `api: 157`, `import: 7`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` mex.h, shoot_diffeo3d.h, shoot_optim3d.h, math.h, shoot_regularisers.h, shoot_boundary.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compat/spm_eeval.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.779 IQR)
- **Top Global Matches:** file_cluster_8: 13.779, file_cluster_17: 14.066, file_cluster_0: 14.16
- **Magnitude:** 2819.4 | **LOC:** 257 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.2541%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 159`
* *Architecture:* None
* *Defense:* `safety: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `@meeg/private/checkmeeg.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.141 IQR)
- **Top Global Matches:** file_cluster_8: 14.141, file_cluster_17: 14.148, file_cluster_0: 14.492
- **Magnitude:** 2420.58 | **LOC:** 448 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (85.6243%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 87`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 267`
* *Architecture:* None
* *Defense:* `safety: 67`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_regularisers.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.636 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.084 IQR)
- **Top Global Matches:** file_cluster_8: 14.636, file_cluster_7: 14.789, file_cluster_13: 14.935
- **Magnitude:** 2317.68 | **LOC:** 1659 | **CtrlFlow:** 91.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 181
- **Risk Profile:** Cognitive Load (29.8997%), Tech Debt (10.5297%)
**Top Internal Functions/Classes:**
  * `relax_all` (Impact: 92.5 | O(N^6) | DB: 154)
  * `relax_be` (Impact: 91.2 | O(N^6) | DB: 111)
  * `sumsq` (Impact: 68.5 | O(N^6) | DB: 129)
  * `relax_le` (Impact: 67.3 | O(N^6) | DB: 104)
  * `relax_me` (Impact: 66.5 | O(N^6) | DB: 79)
    * *Intent:* /************************************************************************************************/ /...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 12`, `args: 1`, `func_start: 11`
* *Risk/State:* `state_mutation: 1702`, `orphaned_logic: 4`
* *Architecture:* `api: 109`, `import: 3`
* *Defense:* `doc: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` shoot_boundary.h, math.h, spm_mex.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_provenance.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.22 IQR)
- **Top Global Matches:** file_cluster_17: 16.22, file_cluster_11: 16.293, file_cluster_0: 16.324
- **Magnitude:** 2315.24 | **LOC:** 1114 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 209
- **Risk Profile:** Cognitive Load (94.5315%), Tech Debt (13.088%)
**Top Internal Functions/Classes:**
  * `serialize_jsonld` (Impact: 1312.5 | O(N^6) | DB: 209)
  * `serialize_json` (Impact: 53.2 | O(N^5) | DB: 11)
  * `get_namespace` (Impact: 6.2 | O(N^2) | DB: 1)
  * `add_namespace` (Impact: 3.1 | O(N^2) | DB: 1)
  * `remove_namespace` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 267`, `args: 57`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 916`, `dead_code: 25`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 74`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spm_brainwarp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.544 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.443 IQR)
- **Top Global Matches:** file_cluster_8: 14.544, file_cluster_13: 14.743, file_cluster_7: 14.841
- **Magnitude:** 2261.22 | **LOC:** 688 | **CtrlFlow:** 95.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 204
- **Risk Profile:** Cognitive Load (74.4142%), Tech Debt (62.0895%)
**Top Internal Functions/Classes:**
  * `mrqcof` (Impact: 1164.6 | O(N^6) | DB: 204)
  * `mexFunction` (Impact: 273.0 | O(N^4) | DB: 52)
  * `matmul` (Impact: 27.1 | O(N^4) | DB: 9)
  * `scale` (Impact: 6.3 | O(N^2) | DB: 3)
  * `transform_grads` (Impact: 2.2 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 6`, `args: 16`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 737`, `fragile_debt: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 42`, `import: 3`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, mex.h, spm_mapping.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_diffeo3d.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.608 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.261 IQR)
- **Top Global Matches:** file_cluster_8: 14.608, file_cluster_13: 14.873, file_cluster_7: 14.951
- **Magnitude:** 2153.22 | **LOC:** 1268 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 152
- **Risk Profile:** Cognitive Load (63.8054%), Tech Debt (33.6455%)
**Top Internal Functions/Classes:**
  * `grad1` (Impact: 96.8 | O(N^6) | DB: 37)
    * *Intent:* #define LOG(x) (((x)>0) ? log(x+0.001): -6.9078)
  * `pushc_grads` (Impact: 95.1 | O(N^6) | DB: 152)
  * `pushpull` (Impact: 87.5 | O(N^6) | DB: 76)
  * `composition_stuff` (Impact: 64.5 | O(N^6) | DB: 150)
    * *Intent:* /* Compute Lie bracket */
  * `def2jac_neuman` (Impact: 55.4 | O(N^5) | DB: 47)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 23`, `args: 2`, `func_start: 23`
* *Risk/State:* `state_mutation: 1458`, `orphaned_logic: 18`
* *Architecture:* `api: 143`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` shoot_optim3d.h, math.h, shoot_boundary.h, shoot_expm3.h, stdio.h, spm_mex.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_DEM_M_set.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.913 IQR)
- **Top Global Matches:** file_cluster_17: 14.913, file_cluster_8: 15.076, file_cluster_0: 15.122
- **Magnitude:** 2097.85 | **LOC:** 454 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.4651%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 54`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 177`, `dead_code: 2`
* *Architecture:* None
* *Defense:* `safety: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_eeg_review_callbacks.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.539 IQR)
- **Top Global Matches:** file_cluster_8: 14.539, file_cluster_17: 14.588, file_cluster_11: 14.801
- **Magnitude:** 1882.86 | **LOC:** 2030 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (68.2054%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `plotScalpData` (Impact: 47.2 | O(N^3) | DB: 21)
    * *Intent:* %% plot Scalp Data
  * `switchBC` (Impact: 31.9 | O(N^2) | DB: 21)
    * *Intent:* %% Switch 'bad channel' status
  * `getUItable` (Impact: 23.3 | O(N^3) | DB: 8)
    * *Intent:* % try,str{7} = ['Time onset: ',num2str(D.timeOnset),' sec'];end %% extracting data from spm_uitable ...
  * `spm_eeg_review_callbacks` (Impact: 7.6 | O(N^1) | DB: 2)
    * *Intent:* % Callbacks of the M/EEG Review facility %__________________________________________________________...
  * `getInfo4Data` (Impact: 2.3 | O(N^1) | DB: 1)
    * *Intent:* %% Get data info
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 444`, `structural_boundaries: 249`, `args: 11`, `func_start: 8`
* *Risk/State:* `state_mutation: 1736`
* *Architecture:* `io: 2`
* *Defense:* `safety: 142`, `doc: 26`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `toolbox/MEEGtools/spm_mesh_pack_points.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.935 IQR)
- **Top Global Matches:** file_cluster_8: 13.935, file_cluster_11: 14.264, file_cluster_17: 14.296
- **Magnitude:** 1873.12 | **LOC:** 502 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (84.8368%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 40`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 415`
* *Architecture:* None
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_orthviews.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.119 IQR)
- **Top Global Matches:** file_cluster_17: 16.119, file_cluster_11: 16.159, file_cluster_0: 16.245
- **Magnitude:** 1703.94 | **LOC:** 2292 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (75.0465%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `spm_orthviews` (Impact: 25.8 | O(N^3) | DB: 1)
    * *Intent:* % Display orthogonal views of a set of images % FORMAT H = spm_orthviews('Image',filename[,area[,F]]...
  * `rmcontexts` (Impact: 8.0 | O(N^2))
    * *Intent:* %========================================================================== % function rmcontexts(ha...
  * `cm_pos` (Impact: 7.2 | O(N^1))
    * *Intent:* %========================================================================== % function cm_pos %=====...
  * `c_menu` (Impact: 3.7 | O(N^1))
    * *Intent:* %========================================================================== % function c_menu(vararg...
  * `get_cm_handles` (Impact: 3.2 | O(N^1) | DB: 1)
    * *Intent:* %========================================================================== % function cm_handles = ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 422`, `structural_boundaries: 271`, `args: 37`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1622`, `dead_code: 44`
* *Architecture:* `io: 1`
* *Defense:* `safety: 94`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_dicom_convert.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.799 IQR)
- **Top Global Matches:** file_cluster_17: 16.799, file_cluster_11: 16.865, file_cluster_0: 16.93
- **Magnitude:** 1665.4 | **LOC:** 1982 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (77.8384%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `spm_dicom_convert` (Impact: 121.9 | O(N^3) | DB: 18)
    * *Intent:* % Convert DICOM images into something that SPM can use (e.g. NIfTI) % FORMAT out = spm_dicom_convert...
  * `ReadSliceNormalVector` (Impact: 76.4 | O(N^4) | DB: 21)
    * *Intent:* %========================================================================== % function nrm = ReadSli...
  * `SelectTomographicImages` (Impact: 1.8 | O(N^1) | DB: 1)
    * *Intent:* %========================================================================== % function [images,guff]...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 233`, `args: 32`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1439`, `dead_code: 38`
* *Architecture:* `io: 20`
* *Defense:* `safety: 129`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spm_mapping.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.107 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.385 IQR)
- **Top Global Matches:** file_cluster_13: 14.107, file_cluster_8: 14.147, file_cluster_7: 14.385
- **Magnitude:** 1570.48 | **LOC:** 596 | **CtrlFlow:** 85.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (69.0467%), Tech Debt (13.876%)
**Top Internal Functions/Classes:**
  * `get_map_file` (Impact: 430.9 | O(N^5) | DB: 105)
  * `get_map_dat` (Impact: 332.3 | O(N^4) | DB: 63)
  * `get_maps_3dvol` (Impact: 62.7 | O(N^2) | DB: 38)
  * `free_maps` (Impact: 25.8 | O(N^3) | DB: 6)
    * *Intent:* #ifdef _MSC_VER #define stat _stati64 #define fstat _fstati64 #endif #define open _open #define clos...
  * `get_maps_struct` (Impact: 21.5 | O(N^4) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 32`, `args: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 588`, `orphaned_logic: 3`
* *Architecture:* `io: 12`, `api: 68`, `import: 11`
* *Defense:* `doc: 9`, `immutability_locks: 9`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fcntl.h, memory.h, windows.h, unistd.h, math.h, stat.h, mman.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_eeg_review_uis.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.633 IQR)
- **Top Global Matches:** file_cluster_8: 11.633, file_cluster_2: 11.933, file_cluster_17: 12.057
- **Magnitude:** 1533.41 | **LOC:** 600 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (64.1388%), Tech Debt (12.2706%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 46`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 261`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_eeg_render.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.475 IQR)
- **Top Global Matches:** file_cluster_8: 13.475, file_cluster_17: 13.479, file_cluster_2: 13.699
- **Magnitude:** 1524.19 | **LOC:** 375 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (66.3997%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 30`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 243`, `dead_code: 1`
* *Architecture:* None
* *Defense:* `safety: 21`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_dcm_bma_results.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.837 IQR)
- **Top Global Matches:** file_cluster_8: 12.837, file_cluster_17: 13.24, file_cluster_13: 13.327
- **Magnitude:** 1523.59 | **LOC:** 359 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (72.6097%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 49`, `args: 2`, `func_start: 5`
* *Risk/State:* `state_mutation: 270`
* *Architecture:* `io: 5`
* *Defense:* `safety: 9`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matlabbatch/cfg_util.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.429 IQR)
- **Top Global Matches:** file_cluster_17: 14.429, file_cluster_8: 14.565, file_cluster_11: 14.565
- **Magnitude:** 1478.9 | **LOC:** 1862 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (76.5571%), Tech Debt (11.4314%)
**Top Internal Functions/Classes:**
  * `cfg_util` (Impact: 30.0 | O(2^N) | DB: 1)
    * *Intent:* % This is the command line interface to the batch system. It manages the % following structures: % *...
  * `local_cd` (Impact: 20.9 | O(N^2) | DB: 3)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_addtojob` (Impact: 16.8 | O(N^3) | DB: 4)
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `local_delfromjob` (Impact: 5.6 | O(N^1))
    * *Intent:* %----------------------------------------------------------------------- %--------------------------...
  * `fprintf` (Impact: 2.5 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 193`, `args: 27`, `func_start: 18`
* *Risk/State:* `state_mutation: 1376`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 22`
* *Defense:* `safety: 82`, `doc: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spm_mnc2nifti.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.061 IQR)
- **Top Global Matches:** file_cluster_17: 15.061, file_cluster_11: 15.128, file_cluster_0: 15.169
- **Magnitude:** 1473.83 | **LOC:** 234 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.2291%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 27`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 244`, `dead_code: 3`
* *Architecture:* `io: 3`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shoot_optimN.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.173 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.664 IQR)
- **Top Global Matches:** file_cluster_8: 14.173, file_cluster_13: 14.404, file_cluster_7: 14.502
- **Magnitude:** 1467.56 | **LOC:** 768 | **CtrlFlow:** 87.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (65.4285%), Tech Debt (10.6888%)
**Top Internal Functions/Classes:**
  * `relax` (Impact: 114.0 | O(N^6) | DB: 87)
  * `LtLf` (Impact: 66.3 | O(N^6) | DB: 69)
    * *Intent:* */
  * `sumsq` (Impact: 51.0 | O(N^6) | DB: 60)
  * `fmg` (Impact: 47.1 | O(N^5) | DB: 58)
  * `solve` (Impact: 29.4 | O(N^4) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 16`, `args: 1`, `func_start: 16`
* *Risk/State:* `state_mutation: 980`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 75`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` shoot_boundary.h, math.h, shoot_multiscale.h, spm_mex.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spm_cat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.573 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.104 IQR)
- **Top Global Matches:** file_cluster_8: 14.573, file_cluster_13: 14.72, file_cluster_11: 14.781
- **Magnitude:** 1433.34 | **LOC:** 640 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (78.3224%), Tech Debt (12.0059%)
**Top Internal Functions/Classes:**
  * `mexFunction` (Impact: 153.5 | O(N^5) | DB: 29)
  * `cast2double` (Impact: 105.0 | O(N^3) | DB: 71)
  * `full2sparse` (Impact: 98.3 | O(N^6) | DB: 39)
  * `forwardPass` (Impact: 84.5 | O(N^5) | DB: 20)
  * `backwardPass` (Impact: 78.9 | O(N^6) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 43`, `args: 20`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 702`, `orphaned_logic: 2`
* *Architecture:* `api: 92`, `import: 3`
* *Defense:* `safety: 3`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string.h, math.h, mex.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spm_jsonread.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.637 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.295 IQR)
- **Top Global Matches:** file_cluster_8: 13.637, file_cluster_13: 13.713, file_cluster_0: 13.856
- **Magnitude:** 1403.84 | **LOC:** 571 | **CtrlFlow:** 83.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (80.9619%), Tech Debt (10.167%)
**Top Internal Functions/Classes:**
  * `mexFunction` (Impact: 152.0 | O(N^6) | DB: 19)
  * `valid_fieldname_hex` (Impact: 132.6 | O(N^5) | DB: 32)
  * `valid_fieldname_underscore` (Impact: 126.6 | O(N^5) | DB: 14)
  * `array` (Impact: 98.1 | O(2^N) | DB: 17)
  * `should_convert_to_array` (Impact: 81.2 | O(N^5) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 32`, `args: 10`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 447`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 64`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mex.h, string.h, jsmn.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `config/spm_cfg_eeg_artefact.m` (MATLAB) | Magnitude: 150.3 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 137, structural_boundaries: 18, indent_spaces: 8, branch: 5
- `help/index.html` (HTML) | Magnitude: 16.84 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, io: 21, structural_boundaries: 13, branch: 5
- `external/mne/mne_rt_client.m` (MATLAB) | Magnitude: 0.23 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 40, structural_boundaries: 18, branch: 7
- `matlabbatch/cfg_job.m` (MATLAB) | Magnitude: 80.22 | Delta: **0.205 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 31, structural_boundaries: 20, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `external/fieldtrip/fileio/private/ft_warp_apply.m` (MATLAB) | Magnitude: 0.12 | Delta: **0.296 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 99, indent_spaces: 71, branch: 47
- `external/fieldtrip/forward/private/ft_warp_apply.m` (MATLAB) | Magnitude: 0.12 | Delta: **0.296 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 99, indent_spaces: 71, branch: 47
- `external/fieldtrip/plotting/private/ft_warp_apply.m` (MATLAB) | Magnitude: 0.12 | Delta: **0.296 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 99, indent_spaces: 71, branch: 47
- `external/fieldtrip/utilities/ft_warp_apply.m` (MATLAB) | Magnitude: 0.12 | Delta: **0.296 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: scientific: 775, state_mutation: 99, indent_spaces: 71, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `config/spm_cfg_eeg_cfc.m` (MATLAB) | Magnitude: 109.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 107, branch: 3, dead_code: 3, structural_boundaries: 2
- `external/fieldtrip/fileio/private/read_shm_event.m` (MATLAB) | Magnitude: 0.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 97, indent_spaces: 46, structural_boundaries: 25, branch: 15
- `spm_uw_estimate.m` (MATLAB) | Magnitude: 673.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 585, indent_spaces: 222, scientific: 124, branch: 95
- `@gifti/private/mvtk_write.m` (MATLAB) | Magnitude: 397.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 348, indent_spaces: 275, branch: 122, structural_boundaries: 55
- `external/fieldtrip/connectivity/ft_connectivity_pdc.m` (MATLAB) | Magnitude: 0.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 85, indent_spaces: 31, branch: 17, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `bin/spm12-matlab` (SHELL) | Magnitude: 77.78 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 39, branch: 25, indent_spaces: 24, reflection_metaprogramming: 21
- `bin/spm12-mcr` (SHELL) | Magnitude: 38.36 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 21, branch: 17, reflection_metaprogramming: 13, state_mutation: 12
- `@nifti/private/nifti_stats.c` (C) | Magnitude: 12930.36 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 4933, indent_spaces: 2697, pointers: 1941, branch: 1369

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/jsmn.h` (C) | Magnitude: 39.78 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 17, api: 16, structural_boundaries: 8, state_mutation: 8
- `external/fieldtrip/src/meg_leadfield1.c` (C) | Magnitude: 0.15 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 76, indent_spaces: 62, branch: 13, api: 8
- `@file_array/private/file2mat.c` (C) | Magnitude: 1066.04 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 443, indent_spaces: 437, branch: 110, pointers: 109
- `@gifti/private/zstream.c` (C) | Magnitude: 119.72 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 36, branch: 20, indent_spaces: 15, api: 9
- `src/spm_mapping.c` (C) | Magnitude: 1570.48 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 588, indent_spaces: 461, branch: 186, api: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `external/fieldtrip/private/openedf.m` (MATLAB) | Magnitude: 0.67 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 177, indent_spaces: 44, branch: 29, structural_boundaries: 17
- `external/fieldtrip/utilities/ft_trackusage.m` (MATLAB) | Magnitude: 0.13 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 65, indent_spaces: 65, structural_boundaries: 30, branch: 18
- `spm_get_dataset.m` (MATLAB) | Magnitude: 194.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 117, indent_spaces: 84, branch: 40, structural_boundaries: 15
- `toolbox/Shoot/spm_shoot3di.m` (MATLAB) | Magnitude: 433.13 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 86, indent_spaces: 35, scientific: 24, branch: 17
- `external/fieldtrip/forward/private/halfspace_medium_leadfield.m` (MATLAB) | Magnitude: 0.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 53, indent_spaces: 23, scientific: 8, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `toolbox/DEM/spm_dem_reach_movie.m` (MATLAB) | Magnitude: 46.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 22, ui_framework: 5, branch: 4
- `toolbox/DEM/MDP_DEM_Oculomotion_Pharma_demo.m` (MATLAB) | Magnitude: 252.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 236, indent_spaces: 106, branch: 30, structural_boundaries: 26
- `toolbox/mci/demo-gradients/mci_compare_jacobians.m` (MATLAB) | Magnitude: 131.73 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 21, debug_prints: 7, ui_framework: 6
- `toolbox/DEM/DEM_demo_Lorenz.m` (MATLAB) | Magnitude: 36.04 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 33, indent_spaces: 28, ui_framework: 12, structural_boundaries: 2
- `toolbox/spectral/spm_gew_demo.m` (MATLAB) | Magnitude: 57.12 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 17, structural_boundaries: 7, ui_framework: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `spm_standalone.m` (MATLAB) | Magnitude: 127.08 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 132, state_mutation: 99, branch: 46, structural_boundaries: 24
- `spm_dcm_fit.m` (MATLAB) | Magnitude: 97.22 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 57, branch: 32, structural_boundaries: 13
- `spm_jobman.m` (MATLAB) | Magnitude: 365.94 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 303, state_mutation: 285, branch: 130, structural_boundaries: 75
- `man/batch/face_multi_subject_template.m` (MATLAB) | Magnitude: 28.16 | Delta: **0.336 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, io: 2, state_mutation: 2, serialization_parsing: 2
- `man/batch/face_single_subject_script.m` (MATLAB) | Magnitude: 43.24 | Delta: **0.398 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 22, concurrency: 6, indent_spaces: 4, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `matlabbatch/@cfg_item/subsasgn_check.m` (MATLAB) | Magnitude: 36.08 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 27, branch: 14, structural_boundaries: 6
- `external/fieldtrip/fileio/private/decode_res4.m` (MATLAB) | Magnitude: 0.08 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 25, indent_spaces: 22, io: 6, cleanup: 6
- `external/fieldtrip/fileio/ft_flush_event.m` (MATLAB) | Magnitude: 0.15 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 9, branch: 8, structural_boundaries: 3
- `toolbox/FieldMap/pm_defaults.m` (MATLAB) | Magnitude: 34.4 | Delta: **0.224 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 19, dead_code: 4, structural_boundaries: 1, globals: 1
- `toolbox/FieldMap/FIL/pm_defaults_Allegra.m` (MATLAB) | Magnitude: 34.4 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 19, structural_boundaries: 1, dead_code: 1, globals: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `external/fieldtrip/fileio/ft_write_headshape.m` (MATLAB) | Magnitude: 0.81 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 118, branch: 43, structural_boundaries: 19
- `toolbox/DEM/spm_mountaincar_movie.m` (MATLAB) | Magnitude: 44.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 17, scientific: 9, ui_framework: 4
- `spm_LAPF.m` (MATLAB) | Magnitude: 698.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 616, indent_spaces: 340, branch: 67, structural_boundaries: 43
- `spm_mask.m` (MATLAB) | Magnitude: 371.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 83, indent_spaces: 40, branch: 17, structural_boundaries: 15
- `external/fieldtrip/src/splint_gh.c` (C) | Magnitude: 0.25 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 153, indent_spaces: 90, api: 25, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `matlabbatch/@cfg_const/showdetail.m` (MATLAB) | Magnitude: 8.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 3, dead_code: 2, structural_boundaries: 1, args: 1
- `matlabbatch/@cfg_const/showdoc.m` (MATLAB) | Magnitude: 7.5 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 3, dead_code: 2, structural_boundaries: 1, args: 1
- `external/mne/mne_write_events.m` (MATLAB) | Magnitude: 0.05 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, structural_boundaries: 2, indent_spaces: 2, branch: 1
- `external/fieldtrip/connectivity/private/mtimes3x3.m` (MATLAB) | Magnitude: 0.03 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: scientific: 27, state_mutation: 10, args: 1, func_start: 1
- `external/fieldtrip/src/mtimes3x3.m` (MATLAB) | Magnitude: 0.03 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: scientific: 27, state_mutation: 10, args: 1, func_start: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/spm_vol_access.h` -> **Severity: 198.9** (Blast Radius: 1.989 * Doc Risk: 100.0%)
- `external/fieldtrip/src/geometry.h` -> **Severity: 130.32** (Blast Radius: 1.629 * Doc Risk: 80.0%)
- `external/fieldtrip/src/compiler.h` -> **Severity: 120.244** (Blast Radius: 1.297 * Doc Risk: 92.7096%)
- `src/spm_mapping.h` -> **Severity: 115.68** (Blast Radius: 1.928 * Doc Risk: 60.0%)
- `src/bsplines.h` -> **Severity: 73.2** (Blast Radius: 0.732 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
