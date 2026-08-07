# ARCHITECTURAL_BRIEF: wrf-fortran
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/wrf-fortran` |
| **Timestamp** | `2026-08-07T05:41:45.910779+00:00` |
| **Scan Duration** | `30.78s` |
| **Git Branch** | `master` |
| **Git Commit** | `f15568ccc1447780e3bd664b9f0196edd784bf33` |
| **Git Remote** | `https://github.com/wrf-model/WRF.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3410 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Total Artifacts | 4915 |
| Analyzed Artifacts (Scanned) | 3547 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1368 |
| Total LOC | 1137651 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 72.2% |
| Dominant Lang | FORTRAN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6646 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1791 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8373 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 75 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| FORTRAN | 2803 | 1048165 | 79.0% |
| C | 329 | 60120 | 9.3% |
| MAKEFILE | 155 | 7550 | 4.4% |
| PLAINTEXT | 107 | 7 | 3.0% |
| SHELL | 84 | 13984 | 2.4% |
| MARKDOWN | 25 | 0 | 0.7% |
| PYTHON | 13 | 2243 | 0.4% |
| MATLAB | 8 | 160 | 0.2% |
| M4 | 8 | 3190 | 0.2% |
| BINARY_THREAT | 5 | 5 | 0.1% |
| PERL | 4 | 1321 | 0.1% |
| YACC | 3 | 880 | 0.1% |
| OBJECTIVE-C | 2 | 18 | 0.1% |
| CSV | 1 | 8 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.233`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2581 | 72.8% |
| file_cluster_13 | 447 | 12.6% |
| file_cluster_11 | 122 | 3.4% |
| file_cluster_17 | 114 | 3.2% |
| file_cluster_4 | 77 | 2.2% |
| file_cluster_9 | 39 | 1.1% |
| file_cluster_12 | 18 | 0.5% |
| Unknown | 12 | 0.3% |
| file_cluster_0 | 7 | 0.2% |
| file_cluster_6 | 3 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 127 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1368*

**Composition by Extension & Reason:**
- `.f90`: 372x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 127 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1083 LOC)
- `no_extension`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 42x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus), 18x Unsupported Format (.undeterminable)
- `.f`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Embedded Array/Matrix Payload: 9753 commas in 2194 LOC), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.inc`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 52 LOC), 1x Excluded (Machine-Generated Source Code Signature: 29 LOC)
- `.eqn`: 39x Excluded (Unsupported Extension: '.eqn'), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kpp`: 46x Excluded (Unsupported Extension: '.kpp'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.spc`: 38x Excluded (Unsupported Extension: '.spc'), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.info`: 42x Excluded (Unsupported Extension: '.info')
- `.equiv`: 30x Excluded (Unsupported Extension: '.equiv')
- `.code`: 28x Excluded (Unsupported Extension: '.code')
- `.tbl`: 13x Excluded (Unsupported Extension: '.TBL'), 6x Excluded (Unsupported Extension: '.tbl'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ncl`: 18x Excluded (Unsupported Extension: '.ncl'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.input`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 16x Excluded (Unsupported Extension: '.cmake')
- `.c`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2406 LOC), 1x Excluded (Embedded Array/Matrix Payload: 7541 commas in 1703 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 56.1 | 69.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 77.8 | 97.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.1 | 6.1 | 5.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 80.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 88.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 51.3 | 38.5 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/regtest.csh` (Hits: 1423)
- `tools/regtest_hwrf.csh` (Hits: 1221)
- `tools/regtest_nmmnest.csh` (Hits: 1165)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **module_configure.F** (`frame/module_configure.F`) — 194 inbound connections
2. **module_model_constants.F** (`share/module_model_constants.F`) — 150 inbound connections
3. **module_domain.F** (`frame/module_domain.F`) — 129 inbound connections
4. **module_wrf_error.F** (`frame/module_wrf_error.F`) — 91 inbound connections
5. **module_dm.F** (`external/RSL_LITE/module_dm.F`) — 88 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **module_physics_init.F** (`phys/module_physics_init.F`) — 117 outbound dependencies
2. **chem_driver.F** (`chem/chem_driver.F`) — 43 outbound dependencies
3. **module_microphysics_driver.F** (`phys/module_microphysics_driver.F`) — 41 outbound dependencies
4. **solve_em_ad.F** (`wrftladj/solve_em_ad.F`) — 41 outbound dependencies
5. **module_ra_rrtmg_sw.F** (`phys/module_ra_rrtmg_sw.F`) — 40 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `bio_emissions_megan2` (@ `chem/module_bioemi_megan2.F`) -> Impact: **6547.4** | LOC: 1755
- `lsm_mosaic` (@ `phys/module_sf_noahdrv.F`) -> Impact: **6518.3** | LOC: 2205
- `init_domain_rk` (@ `dyn_em/module_initialize_real.F`) -> Impact: **5887.3** | LOC: 4586
- `MORR_TWO_MOMENT_MICRO` (@ `phys/module_mp_morr_two_moment_aero.F`) -> Impact: **5668.7** | LOC: 3063
- `microphysics_driver` (@ `phys/module_microphysics_driver.F`) -> Impact: **5582.3** | LOC: 2581
- `SBM` (@ `phys/module_mp_full_sbm.F`) -> Impact: **4869.0** | LOC: 1562
- `nssl_2mom_gs` (@ `phys/module_mp_nssl_2mom.F`) -> Impact: **4817.9** | LOC: 9963
- `nssl_2mom_driver` (@ `phys/module_mp_nssl_2mom.F`) -> Impact: **4657.7** | LOC: 1118
- `deng_shcu` (@ `phys/module_shcu_deng.F`) -> Impact: **4635.0** | LOC: 2189
- `MORR_TWO_MOMENT_MICRO` (@ `phys/module_mp_morr_two_moment.F`) -> Impact: **4568.6** | LOC: 2495

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `phys` | 229 | 779049.68 | 67.92% | 8.94% |
| `chem` | 184 | 333519.78 | 55.13% | 6.6% |
| `dyn_em` | 38 | 130876.6 | 65.08% | 11.57% |
| `var/da/da_radiance` | 109 | 86190.44 | 73.08% | 0.56% |
| `frame` | 59 | 77705.76 | 47.15% | 22.05% |
| `share` | 55 | 73934.19 | 57.06% | 20.17% |
| `wrftladj` | 29 | 60953.5 | 60.14% | 13.38% |
| `var/da/da_obs_io` | 40 | 57544.14 | 74.95% | 1.56% |
| `var/da/da_setup_structures` | 44 | 38468.38 | 76.23% | 0.18% |
| `run` | 17 | 37626.94 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `chem/KPP/configure_kpp` -> **100.0%** Exposure
- `chem/KPP/kpp/kpp-2.1/kpp_compile` -> **100.0%** Exposure
- `chem/KPP/util/wkc/linker.csh` -> **100.0%** Exposure
- `chem/KPP/util/write_decomp/write_decom.csh` -> **100.0%** Exposure
- `compile_new` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `arch/Config.pl` -> **100.0%** Exposure
- `hydro/wrf_hydro_config` -> **100.0%** Exposure
- `tools/check_for_bad_includes.pl` -> **100.0%** Exposure
- `tools/subinfo` -> **100.0%** Exposure
- `tools/manage_externals/manic/externals_status.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `frame/xxx_template_ioapi.F` -> **1** Orphaned Functions | **126** Duplicates
- `share/dfi.F` -> **1** Orphaned Functions | **92** Duplicates
- `frame/module_dm_stubs.F` -> **0** Orphaned Functions | **84** Duplicates
- `external/RSL_LITE/module_dm.F` -> **0** Orphaned Functions | **58** Duplicates
- `external/io_int/io_int.F90` -> **0** Orphaned Functions | **54** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`chem/KPP/kpp/kpp-2.1/src/scan.y`** -> AI Confidence: **99.48%**
2. **`chem/KPP/util/wkc/compare_kpp_to_species.c`** -> AI Confidence: **99.48%**
3. **`chem/KPP/util/wkc/gen_kpp.c`** -> AI Confidence: **99.48%**
4. **`chem/KPP/util/wkc/get_kpp_chem_specs.c`** -> AI Confidence: **99.48%**
5. **`chem/KPP/util/wkc/get_wrf_chem_specs.c`** -> AI Confidence: **99.48%**
6. **`chem/KPP/util/wkc/registry_kpp.c`** -> AI Confidence: **99.48%**
7. **`external/RSL_LITE/c_code.c`** -> AI Confidence: **99.48%**
8. **`external/RSL_LITE/rsl_malloc.c`** -> AI Confidence: **99.48%**
9. **`external/io_grib1/MEL_grib1/FTP_getfile.c`** -> AI Confidence: **99.48%**
10. **`external/io_grib1/MEL_grib1/grib_enc.c`** -> AI Confidence: **99.48%**
11. **`external/io_grib1/MEL_grib1/gribputpds.c`** -> AI Confidence: **99.48%**
12. **`external/io_grib1/MEL_grib1/ld_enc_lookup.c`** -> AI Confidence: **99.48%**
13. **`external/io_grib1/MEL_grib1/ld_grib_origctrs.c`** -> AI Confidence: **99.48%**
14. **`external/io_grib1/MEL_grib1/pack_spatial.c`** -> AI Confidence: **99.48%**
15. **`external/io_grib1/MEL_grib1/prt_inp_struct.c`** -> AI Confidence: **99.48%**
16. **`external/io_grib1/WGRIB/BDSunpk.c`** -> AI Confidence: **99.48%**
17. **`external/io_grib1/WGRIB/ensemble.c`** -> AI Confidence: **99.48%**
18. **`external/io_grib1/WGRIB/wgrib_main.c`** -> AI Confidence: **99.48%**
19. **`external/io_grib1/grib1_util/read_grib.c`** -> AI Confidence: **99.48%**
20. **`tools/data.c`** -> AI Confidence: **99.48%**
21. **`tools/gen_allocs.c`** -> AI Confidence: **99.48%**
22. **`tools/gen_args.c`** -> AI Confidence: **99.48%**
23. **`tools/gen_config.c`** -> AI Confidence: **99.48%**
24. **`tools/gen_defs.c`** -> AI Confidence: **99.48%**
25. **`tools/gen_interp.c`** -> AI Confidence: **99.48%**
26. **`tools/gen_irr_diag.c`** -> AI Confidence: **99.48%**
27. **`tools/gen_model_data_ord.c`** -> AI Confidence: **99.48%**
28. **`tools/gen_scalar_indices.c`** -> AI Confidence: **99.48%**
29. **`tools/gen_wrf_io.c`** -> AI Confidence: **99.48%**
30. **`tools/misc.c`** -> AI Confidence: **99.48%**
31. **`tools/reg_parse.c`** -> AI Confidence: **99.48%**
32. **`tools/registry.c`** -> AI Confidence: **99.48%**
33. **`tools/set_dim_strs.c`** -> AI Confidence: **99.48%**
34. **`tools/type.c`** -> AI Confidence: **99.48%**
35. **`var/da/makedepf90-2.8.8/main.c`** -> AI Confidence: **99.48%**
36. **`chem/chemics_init.F`** -> AI Confidence: **99.48%**
37. **`chem/convert_emiss.F`** -> AI Confidence: **99.48%**
38. **`dyn_em/couple_or_uncouple_em.F`** -> AI Confidence: **99.48%**
39. **`dyn_em/module_initialize_heldsuarez.F`** -> AI Confidence: **99.48%**
40. **`dyn_em/solve_em.F`** -> AI Confidence: **99.48%**
41. **`dyn_em/start_em.F`** -> AI Confidence: **99.48%**
42. **`hydro/Routing/module_RT.F90`** -> AI Confidence: **99.48%**
43. **`share/input_wrf.F`** -> AI Confidence: **99.48%**
44. **`var/obsproc/src/module_qc.F90`** -> AI Confidence: **99.48%**
45. **`var/obsproc/src/module_recoverh.F90`** -> AI Confidence: **99.48%**
46. **`wrftladj/solve_em_ad.F`** -> AI Confidence: **99.48%**
47. **`wrftladj/solve_em_tl.F`** -> AI Confidence: **99.48%**
48. **`var/da/da_main/da_solve_init.inc`** -> AI Confidence: **99.48%**
49. **`chem/module_mosaic_driver.F`** -> AI Confidence: **99.44%**
50. **`dyn_em/module_initialize_real.F`** -> AI Confidence: **99.44%**
51. **`var/obsproc/src/module_decoded.F90`** -> AI Confidence: **99.44%**
52. **`chem/module_dep_simple.F`** -> AI Confidence: **99.43%**
53. **`dyn_em/module_initialize_ideal.F`** -> AI Confidence: **99.43%**
54. **`arch/configure_reader.py`** -> AI Confidence: **99.39%**
55. **`external/io_grib1/MEL_grib1/map_lvl.c`** -> AI Confidence: **99.39%**
56. **`external/io_grib1/grib1_routines.c`** -> AI Confidence: **99.39%**
57. **`external/io_grib2/bacio-1.3/bacio.v1.3.c`** -> AI Confidence: **99.39%**
58. **`share/landread.c`** -> AI Confidence: **99.39%**
59. **`tools/gen_scalar_derefs.c`** -> AI Confidence: **99.39%**
60. **`tools/gen_streams.c`** -> AI Confidence: **99.39%**
61. **`var/da/makedepf90-2.8.8/utils.c`** -> AI Confidence: **99.39%**
62. **`chem/chem_driver.F`** -> AI Confidence: **99.39%**
63. **`chem/module_cam_mam_aerchem_driver.F`** -> AI Confidence: **99.39%**
64. **`chem/module_cam_mam_calcsize.F`** -> AI Confidence: **99.39%**
65. **`chem/module_cam_mam_initaerodata.F`** -> AI Confidence: **99.39%**
66. **`chem/module_cam_mam_setsox.F`** -> AI Confidence: **99.39%**
67. **`chem/module_sorgam_cloudchem.F`** -> AI Confidence: **99.39%**
68. **`chem/module_sorgam_vbs_cloudchem.F`** -> AI Confidence: **99.39%**
69. **`dyn_em/module_initialize_fire.F`** -> AI Confidence: **99.39%**
70. **`dyn_em/module_initialize_tropical_cyclone.F`** -> AI Confidence: **99.39%**
71. **`main/real_em.F`** -> AI Confidence: **99.39%**
72. **`share/output_wrf.F`** -> AI Confidence: **99.39%**
73. **`share/track_driver.F`** -> AI Confidence: **99.39%**
74. **`var/obsproc/src/module_err_afwa.F90`** -> AI Confidence: **99.39%**
75. **`var/obsproc/src/module_write.F90`** -> AI Confidence: **99.39%**
76. **`wrftladj/start_em_ad.F`** -> AI Confidence: **99.39%**
77. **`wrftladj/start_em_tl.F`** -> AI Confidence: **99.39%**
78. **`main/ideal_nmm.F`** -> AI Confidence: **99.35%**
79. **`chem/KPP/kpp/kpp-2.1/src.org/scan.y`** -> AI Confidence: **99.34%**
80. **`chem/KPP/kpp/kpp-2.1/src/code_matlab.c`** -> AI Confidence: **99.34%**
81. **`chem/KPP/kpp/kpp-2.1/src/gen.c`** -> AI Confidence: **99.34%**
82. **`chem/KPP/util/wkc/change_chem_Makefile.c`** -> AI Confidence: **99.34%**
83. **`chem/KPP/util/wkc/gen_kpp_interface.c`** -> AI Confidence: **99.34%**
84. **`external/RSL_LITE/gen_comms.c`** -> AI Confidence: **99.34%**
85. **`external/RSL_LITE/swap.c`** -> AI Confidence: **99.34%**
86. **`external/io_grib1/MEL_grib1/gbyte.c`** -> AI Confidence: **99.34%**
87. **`external/io_grib1/MEL_grib1/grib_dec.c`** -> AI Confidence: **99.34%**
88. **`external/io_grib1/MEL_grib1/grib_seek.c`** -> AI Confidence: **99.34%**
89. **`external/io_grib1/MEL_grib1/gribgetbds.c`** -> AI Confidence: **99.34%**
90. **`external/io_grib1/MEL_grib1/gribgetbms.c`** -> AI Confidence: **99.34%**
91. **`external/io_grib1/MEL_grib1/gribhdr2file.c`** -> AI Confidence: **99.34%**
92. **`external/io_grib1/MEL_grib1/ld_dec_lookup.c`** -> AI Confidence: **99.34%**
93. **`external/io_grib1/MEL_grib1/ld_enc_input.c`** -> AI Confidence: **99.34%**
94. **`external/io_grib1/MEL_grib1/make_grib_log.c`** -> AI Confidence: **99.34%**
95. **`external/io_grib1/WGRIB/PDStimes.c`** -> AI Confidence: **99.34%**
96. **`external/io_grib1/WGRIB/ec_ext.c`** -> AI Confidence: **99.34%**
97. **`external/io_grib1/WGRIB/gds_grid.c`** -> AI Confidence: **99.34%**
98. **`external/io_grib1/WGRIB/gribtable.c`** -> AI Confidence: **99.34%**
99. **`external/io_grib_share/get_region_center.c`** -> AI Confidence: **99.34%**
100. **`tools/CodeBase/callgraph.c`** -> AI Confidence: **99.34%**
101. **`tools/CodeBase/wrfvar.c`** -> AI Confidence: **99.34%**
102. **`tools/gen_mod_state_descr.c`** -> AI Confidence: **99.34%**
103. **`var/da/makedepf90-2.8.8/errormesg.c`** -> AI Confidence: **99.34%**
104. **`var/da/makedepf90-2.8.8/modfile_name.c`** -> AI Confidence: **99.34%**
105. **`var/external/wavelet/TestFilter.c`** -> AI Confidence: **99.34%**
106. **`chem/module_cam_mam_init.F`** -> AI Confidence: **99.34%**
107. **`chem/module_input_chem_data.F`** -> AI Confidence: **99.34%**
108. **`chem/module_mosaic_initmixrats.F`** -> AI Confidence: **99.34%**
109. **`hydro/HYDRO_drv/module_HYDRO_drv.F90`** -> AI Confidence: **99.34%**
110. **`main/module_wrf_top.F`** -> AI Confidence: **99.34%**
111. **`phys/module_microphysics_driver.F`** -> AI Confidence: **99.34%**
112. **`phys/module_radiation_driver.F`** -> AI Confidence: **99.34%**
113. **`var/obsproc/src/module_gpspw_gst.F90`** -> AI Confidence: **99.34%**
114. **`var/obsproc/src/module_thin_ob.F90`** -> AI Confidence: **99.34%**
115. **`var/da/da_vtox_transforms/da_transform_xtoxa.inc`** -> AI Confidence: **99.34%**
116. **`chem/module_mosaic_therm.F`** -> AI Confidence: **99.33%**
117. **`dyn_em/module_polarfft.F`** -> AI Confidence: **99.33%**
118. **`phys/module_diag_afwa.F`** -> AI Confidence: **99.33%**
119. **`chem/KPP/kpp/kpp-2.1/src.org/code_c.c`** -> AI Confidence: **99.32%**
120. **`chem/KPP/kpp/kpp-2.1/src.org/code_matlab.c`** -> AI Confidence: **99.32%**
121. **`chem/KPP/kpp/kpp-2.1/src.org/gdef.h`** -> AI Confidence: **99.32%**
122. **`chem/KPP/kpp/kpp-2.1/src.org/gen_org.c`** -> AI Confidence: **99.32%**
123. **`chem/KPP/kpp/kpp-2.1/src/gen_org.c`** -> AI Confidence: **99.32%**
124. **`chem/KPP/util/write_decomp/integr_edit.c`** -> AI Confidence: **99.32%**
125. **`external/io_grib1/MEL_grib1/grib_uthin.c`** -> AI Confidence: **99.32%**
126. **`external/io_grib1/test_write_grib.c`** -> AI Confidence: **99.32%**
127. **`external/io_grib1/trim.c`** -> AI Confidence: **99.32%**
128. **`tools/CodeBase/subinfo_calls.c`** -> AI Confidence: **99.32%**
129. **`tools/standard.c`** -> AI Confidence: **99.32%**
130. **`var/external/wavelet/dwtai_w.c`** -> AI Confidence: **99.32%**
131. **`var/external/wavelet/idwtai_w.c`** -> AI Confidence: **99.32%**
132. **`chem/KPP/kpp/kpp-2.1/int/kpp_odessa_ddm.f`** -> AI Confidence: **99.32%**
133. **`chem/KPP/kpp/kpp-2.1/int/kpp_sdirk.f`** -> AI Confidence: **99.32%**
134. **`chem/KPP/kpp/kpp-2.1/int/kpp_seulex.f`** -> AI Confidence: **99.32%**
135. **`chem/KPP/kpp/kpp-2.1/int/sdirk.f`** -> AI Confidence: **99.32%**
136. **`frame/module_clear_halos.F`** -> AI Confidence: **99.32%**
137. **`var/obsproc/src/qc_reduction.F90`** -> AI Confidence: **99.32%**
138. **`wrftladj/module_bc_ad.F`** -> AI Confidence: **99.32%**
139. **`var/da/da_transfer_model/da_transfer_wrftoxb.inc`** -> AI Confidence: **99.32%**
140. **`var/da/da_transfer_model/da_transfer_xatowrftl_lbc.inc`** -> AI Confidence: **99.32%**
141. **`tools/manage_externals/manic/externals_description.py`** -> AI Confidence: **99.31%**
142. **`tools/manage_externals/manic/repository_git.py`** -> AI Confidence: **99.31%**
143. **`tools/manage_externals/manic/sourcetree.py`** -> AI Confidence: **99.31%**
144. **`tools/manage_externals/manic/utils.py`** -> AI Confidence: **99.31%**
145. **`chem/KPP/kpp/kpp-2.1/src.org/scanutil.c`** -> AI Confidence: **99.31%**
146. **`chem/KPP/kpp/kpp-2.1/src/scanutil.c`** -> AI Confidence: **99.31%**
147. **`chem/KPP/util/wkc/get_wrf_radicals.c`** -> AI Confidence: **99.31%**
148. **`chem/KPP/util/wkc/kpp_data.c`** -> AI Confidence: **99.31%**
149. **`chem/KPP/util/wkc/tuv_kpp.c`** -> AI Confidence: **99.31%**
150. **`external/io_grib1/MEL_grib1/gribputgds.c`** -> AI Confidence: **99.31%**
151. **`external/io_grib_share/open_file.c`** -> AI Confidence: **99.31%**
152. **`external/io_int/io_int_idx.c`** -> AI Confidence: **99.31%**
153. **`frame/collect_on_comm.c`** -> AI Confidence: **99.31%**
154. **`chem/aerosol_driver.F`** -> AI Confidence: **99.31%**
155. **`chem/emissions_driver.F`** -> AI Confidence: **99.31%**
156. **`chem/isocom.F`** -> AI Confidence: **99.31%**
157. **`chem/module_cam_mam_coag.F`** -> AI Confidence: **99.31%**
158. **`chem/module_cam_mam_gasaerexch.F`** -> AI Confidence: **99.31%**
159. **`chem/module_cam_mam_mo_sethet.F`** -> AI Confidence: **99.31%**
160. **`chem/module_cam_mam_rename.F`** -> AI Confidence: **99.31%**
161. **`chem/module_cbmz.F`** -> AI Confidence: **99.31%**
162. **`chem/module_chem_cup.F`** -> AI Confidence: **99.31%**
163. **`chem/module_optical_averaging.F`** -> AI Confidence: **99.31%**
164. **`chem/module_wetscav_driver.F`** -> AI Confidence: **99.31%**
165. **`dyn_em/module_initialize_scm_xy.F`** -> AI Confidence: **99.31%**
166. **`dyn_em/nest_init_utils.F`** -> AI Confidence: **99.31%**
167. **`external/RSL_LITE/interp_domain_em_small.F`** -> AI Confidence: **99.31%**
168. **`frame/module_io_quilt_old.F`** -> AI Confidence: **99.31%**
169. **`hydro/CPL/WRF_cpl/module_wrf_HYDRO.F90`** -> AI Confidence: **99.31%**
170. **`hydro/CPL/WRF_cpl/module_wrf_HYDRO_downscale.F90`** -> AI Confidence: **99.31%**
171. **`main/ideal_em.F`** -> AI Confidence: **99.31%**
172. **`main/ndown_em.F`** -> AI Confidence: **99.31%**
173. **`main/real_nmm.F`** -> AI Confidence: **99.31%**
174. **`main/tc_em.F`** -> AI Confidence: **99.31%**
175. **`main/wrf_SST_ESMF.F`** -> AI Confidence: **99.31%**
176. **`phys/module_cam_mp_cldwat2m_micro.F`** -> AI Confidence: **99.31%**
177. **`phys/module_mp_p3.F`** -> AI Confidence: **99.31%**
178. **`share/dfi.F`** -> AI Confidence: **99.31%**
179. **`share/interp_fcn.F`** -> AI Confidence: **99.31%**
180. **`share/mediation_nest_move.F`** -> AI Confidence: **99.31%**
181. **`var/obsproc/src/module_diagnostics.F90`** -> AI Confidence: **99.31%**
182. **`var/obsproc/src/obsproc.F90`** -> AI Confidence: **99.31%**
183. **`wrftladj/module_first_rk_step_part2_tl.F`** -> AI Confidence: **99.31%**
184. **`hydro/Makefile`** -> AI Confidence: **99.29%**
185. **`hydro/Routing/Makefile`** -> AI Confidence: **99.29%**
186. **`chem/KPP/util/create_inc_files.csh`** -> AI Confidence: **99.29%**
187. **`cleanCMake.sh`** -> AI Confidence: **99.29%**
188. **`configure`** -> AI Confidence: **99.29%**
189. **`configure_new`** -> AI Confidence: **99.29%**
190. **`external/esmf_time_f90/testall.csh`** -> AI Confidence: **99.29%**
191. **`hydro/configure`** -> AI Confidence: **99.29%**
192. **`var/external/bufr/preproc.sh`** -> AI Confidence: **99.29%**
193. **`chem/KPP/kpp/kpp-2.1/drv/exact.c`** -> AI Confidence: **99.29%**
194. **`chem/KPP/kpp/kpp-2.1/int/oldies/exqssa.c`** -> AI Confidence: **99.29%**
195. **`chem/KPP/kpp/kpp-2.1/int/oldies/rodas3.c`** -> AI Confidence: **99.29%**
196. **`chem/KPP/kpp/kpp-2.1/int/oldies/ros2.c`** -> AI Confidence: **99.29%**
197. **`chem/KPP/kpp/kpp-2.1/int/oldies/ros3.c`** -> AI Confidence: **99.29%**
198. **`chem/KPP/kpp/kpp-2.1/src.org/code_f77.c`** -> AI Confidence: **99.29%**
199. **`chem/KPP/kpp/kpp-2.1/src.org/code_f90.c`** -> AI Confidence: **99.29%**
200. **`chem/KPP/kpp/kpp-2.1/src.org/debug.c`** -> AI Confidence: **99.29%**
201. **`chem/KPP/kpp/kpp-2.1/src/code_c.c`** -> AI Confidence: **99.29%**
202. **`chem/KPP/kpp/kpp-2.1/src/code_f77.c`** -> AI Confidence: **99.29%**
203. **`chem/KPP/kpp/kpp-2.1/src/code_f90.c`** -> AI Confidence: **99.29%**
204. **`chem/KPP/kpp/kpp-2.1/src/debug.c`** -> AI Confidence: **99.29%**
205. **`chem/KPP/kpp/kpp-2.1/util/Mex_Fun.c`** -> AI Confidence: **99.29%**
206. **`chem/KPP/kpp/kpp-2.1/util/Mex_Hessian.c`** -> AI Confidence: **99.29%**
207. **`chem/KPP/kpp/kpp-2.1/util/Mex_Jac_SP.c`** -> AI Confidence: **99.29%**
208. **`chem/KPP/kpp/kpp-2.1/util/UpdateSun.c`** -> AI Confidence: **99.29%**
209. **`chem/KPP/kpp/kpp-2.1/util/mex.c`** -> AI Confidence: **99.29%**
210. **`external/RSL_LITE/buf_for_proc.c`** -> AI Confidence: **99.29%**
211. **`external/RSL_LITE/cycle.c`** -> AI Confidence: **99.29%**
212. **`external/RSL_LITE/period.c`** -> AI Confidence: **99.29%**
213. **`external/RSL_LITE/task_for_point.c`** -> AI Confidence: **99.29%**
214. **`external/io_grib1/MEL_grib1/display_gribhdr.c`** -> AI Confidence: **99.29%**
215. **`external/io_grib1/MEL_grib1/gribgetgds.c`** -> AI Confidence: **99.29%**
216. **`external/io_grib1/MEL_grib1/gribgetpds.c`** -> AI Confidence: **99.29%**
217. **`external/io_grib1/MEL_grib1/prt_badmsg.c`** -> AI Confidence: **99.29%**
218. **`external/io_grib1/WGRIB/ectable_128.c`** -> AI Confidence: **99.29%**
219. **`external/io_grib1/WGRIB/ectable_140.c`** -> AI Confidence: **99.29%**
220. **`external/io_grib1/WGRIB/levels.c`** -> AI Confidence: **99.29%**
221. **`external/io_grib1/WGRIB/nceptab_129.c`** -> AI Confidence: **99.29%**
222. **`external/io_grib1/WGRIB/nceptable_opn.c`** -> AI Confidence: **99.29%**
223. **`external/io_grib_share/get_region_center.h`** -> AI Confidence: **99.29%**
224. **`external/io_grib_share/gridnav.c`** -> AI Confidence: **99.29%**
225. **`frame/loop_based_x_shift_code.h`** -> AI Confidence: **99.29%**
226. **`frame/loop_based_y_shift_code.h`** -> AI Confidence: **99.29%**
227. **`tools/CodeBase/deftab.c`** -> AI Confidence: **99.29%**
228. **`tools/CodeBase/nocontf90.c`** -> AI Confidence: **99.29%**
229. **`tools/CodeBase/util.c`** -> AI Confidence: **99.29%**
230. **`tools/mpi2_test.c`** -> AI Confidence: **99.29%**
231. **`tools/my_strtok.c`** -> AI Confidence: **99.29%**
232. **`tools/nc4_test.c`** -> AI Confidence: **99.29%**
233. **`var/convertor/decode_l2_airs/geth_newdate.c`** -> AI Confidence: **99.29%**
234. **`var/external/bufr/rbytes.c`** -> AI Confidence: **99.29%**
235. **`var/external/bufr/restd.c`** -> AI Confidence: **99.29%**
236. **`var/external/bufr/stseq.c`** -> AI Confidence: **99.29%**
237. **`var/external/wavelet/PrintFilter.c`** -> AI Confidence: **99.29%**
238. **`var/external/wavelet/realt.h`** -> AI Confidence: **99.29%**
239. **`var/mri4dvar/task_for_point.c`** -> AI Confidence: **99.29%**
240. **`dyn_em/namelist_remappings_em.h`** -> AI Confidence: **99.29%**
241. **`external/io_grib2/bacio-1.3/baciof.h`** -> AI Confidence: **99.29%**
242. **`external/ioapi_share/wrf_io_flags.h`** -> AI Confidence: **99.29%**
243. **`inc/bench_solve_em_def.h`** -> AI Confidence: **99.29%**
244. **`inc/streams.h`** -> AI Confidence: **99.29%**
245. **`phys/fr_fire_params_decl.h`** -> AI Confidence: **99.29%**
246. **`phys/mic-wsm5-3-5-callsite.h`** -> AI Confidence: **99.29%**
247. **`phys/mic-wsm5-3-5-code.h`** -> AI Confidence: **99.29%**
248. **`phys/rrtmg_lw_cpu_defs.h`** -> AI Confidence: **99.29%**
249. **`phys/taug_cpu_defs.h`** -> AI Confidence: **99.29%**
250. **`chem/KPP/kpp/kpp-2.1/drv/general_ddm_ic.f`** -> AI Confidence: **99.29%**
251. **`chem/KPP/kpp/kpp-2.1/int/atm_odessa_ddm.f`** -> AI Confidence: **99.29%**
252. **`chem/KPP/kpp/kpp-2.1/int/atm_radau5.f`** -> AI Confidence: **99.29%**
253. **`chem/KPP/kpp/kpp-2.1/int/oldies/exqssa.f`** -> AI Confidence: **99.29%**
254. **`chem/KPP/kpp/kpp-2.1/int/oldies/qssa.f`** -> AI Confidence: **99.29%**
255. **`chem/KPP/kpp/kpp-2.1/int/oldies/qssa1.f`** -> AI Confidence: **99.29%**
256. **`chem/KPP/kpp/kpp-2.1/int/oldies/ros2_cts_adj.f`** -> AI Confidence: **99.29%**
257. **`chem/KPP/kpp/kpp-2.1/util/mex.f`** -> AI Confidence: **99.29%**
258. **`chem/module_bioemi_megan2.F`** -> AI Confidence: **99.29%**
259. **`chem/module_ghg_fluxes.F`** -> AI Confidence: **99.29%**
260. **`chem/module_isofwd.F`** -> AI Confidence: **99.29%**
261. **`chem/module_isorev.F`** -> AI Confidence: **99.29%**
262. **`external/esmf_time_f90/ESMF_Macros.inc`** -> AI Confidence: **99.29%**
263. **`external/esmf_time_f90/ESMF_TimeMgr.inc`** -> AI Confidence: **99.29%**
264. **`external/fftpack/fftpack5/xerfft.F`** -> AI Confidence: **99.29%**
265. **`hydro/Routing/Reservoirs/Level_Pool/module_levelpool_tests.F90`** -> AI Confidence: **99.29%**
266. **`hydro/Routing/Reservoirs/Persistence_Level_Pool_Hybrid/module_persistence_levelpool_hybrid_tests.F90`** -> AI Confidence: **99.29%**
267. **`hydro/Routing/module_date_utilities_rt.F90`** -> AI Confidence: **99.29%**
268. **`var/convertor/average_be/module_readwrf.F`** -> AI Confidence: **99.29%**
269. **`var/convertor/kmabufr/read_bufr.F`** -> AI Confidence: **99.29%**
270. **`var/external/bufr/adn30.f`** -> AI Confidence: **99.29%**
271. **`var/external/bufr/bfrini.f`** -> AI Confidence: **99.29%**
272. **`var/external/bufr/blocks.f`** -> AI Confidence: **99.29%**
273. **`var/external/bufr/capit.f`** -> AI Confidence: **99.29%**
274. **`var/external/bufr/chekstab.f`** -> AI Confidence: **99.29%**
275. **`var/external/bufr/cktaba.f`** -> AI Confidence: **99.29%**
276. **`var/external/bufr/closbf.f`** -> AI Confidence: **99.29%**
277. **`var/external/bufr/closmg.f`** -> AI Confidence: **99.29%**
278. **`var/external/bufr/cmsgini.f`** -> AI Confidence: **99.29%**
279. **`var/external/bufr/copybf.f`** -> AI Confidence: **99.29%**
280. **`var/external/bufr/copymg.f`** -> AI Confidence: **99.29%**
281. **`var/external/bufr/copysb.f`** -> AI Confidence: **99.29%**
282. **`var/external/bufr/cpdxmm.f`** -> AI Confidence: **99.29%**
283. **`var/external/bufr/cpymem.f`** -> AI Confidence: **99.29%**
284. **`var/external/bufr/datebf.f`** -> AI Confidence: **99.29%**
285. **`var/external/bufr/drstpl.f`** -> AI Confidence: **99.29%**
286. **`var/external/bufr/dumpbf.f`** -> AI Confidence: **99.29%**
287. **`var/external/bufr/dxdump.f`** -> AI Confidence: **99.29%**
288. **`var/external/bufr/dxinit.f`** -> AI Confidence: **99.29%**
289. **`var/external/bufr/dxmini.f`** -> AI Confidence: **99.29%**
290. **`var/external/bufr/elemdx.f`** -> AI Confidence: **99.29%**
291. **`var/external/bufr/getntbe.f`** -> AI Confidence: **99.29%**
292. **`var/external/bufr/gets1loc.f`** -> AI Confidence: **99.29%**
293. **`var/external/bufr/gettbh.f`** -> AI Confidence: **99.29%**
294. **`var/external/bufr/getwin.f`** -> AI Confidence: **99.29%**
295. **`var/external/bufr/i4dy.f`** -> AI Confidence: **99.29%**
296. **`var/external/bufr/idxmsg.f`** -> AI Confidence: **99.29%**
297. **`var/external/bufr/ifbget.f`** -> AI Confidence: **99.29%**
298. **`var/external/bufr/igetntbi.f`** -> AI Confidence: **99.29%**
299. **`var/external/bufr/igettdi.f`** -> AI Confidence: **99.29%**
300. **`var/external/bufr/invcon.f`** -> AI Confidence: **99.29%**
301. **`var/external/bufr/invmrg.f`** -> AI Confidence: **99.29%**
302. **`var/external/bufr/ishrdx.f`** -> AI Confidence: **99.29%**
303. **`var/external/bufr/istdesc.f`** -> AI Confidence: **99.29%**
304. **`var/external/bufr/iupbs3.f`** -> AI Confidence: **99.29%**
305. **`var/external/bufr/iupvs01.f`** -> AI Confidence: **99.29%**
306. **`var/external/bufr/jstchr.f`** -> AI Confidence: **99.29%**
307. **`var/external/bufr/lstjpb.f`** -> AI Confidence: **99.29%**
308. **`var/external/bufr/makestab.f`** -> AI Confidence: **99.29%**
309. **`var/external/bufr/mesgbc.f`** -> AI Confidence: **99.29%**
310. **`var/external/bufr/mesgbf.f`** -> AI Confidence: **99.29%**
311. **`var/external/bufr/minimg.f`** -> AI Confidence: **99.29%**
312. **`var/external/bufr/msgini.f`** -> AI Confidence: **99.29%**
313. **`var/external/bufr/msgwrt.f`** -> AI Confidence: **99.29%**
314. **`var/external/bufr/mvb.f`** -> AI Confidence: **99.29%**
315. **`var/external/bufr/nemtab.f`** -> AI Confidence: **99.29%**
316. **`var/external/bufr/nemtbax.f`** -> AI Confidence: **99.29%**
317. **`var/external/bufr/nemtbb.f`** -> AI Confidence: **99.29%**
318. **`var/external/bufr/nemtbd.f`** -> AI Confidence: **99.29%**
319. **`var/external/bufr/nenubd.f`** -> AI Confidence: **99.29%**
320. **`var/external/bufr/nevn.f`** -> AI Confidence: **99.29%**
321. **`var/external/bufr/nmsub.f`** -> AI Confidence: **99.29%**
322. **`var/external/bufr/numtab.f`** -> AI Confidence: **99.29%**
323. **`var/external/bufr/numtbd.f`** -> AI Confidence: **99.29%**
324. **`var/external/bufr/nvnwin.f`** -> AI Confidence: **99.29%**
325. **`var/external/bufr/openbf.f`** -> AI Confidence: **99.29%**
326. **`var/external/bufr/openmg.f`** -> AI Confidence: **99.29%**
327. **`var/external/bufr/pad.f`** -> AI Confidence: **99.29%**
328. **`var/external/bufr/parusr.f`** -> AI Confidence: **99.29%**
329. **`var/external/bufr/parutg.f`** -> AI Confidence: **99.29%**
330. **`var/external/bufr/pkbs1.f`** -> AI Confidence: **99.29%**
331. **`var/external/bufr/pkc.f`** -> AI Confidence: **99.29%**
332. **`var/external/bufr/rcstpl.f`** -> AI Confidence: **99.29%**
333. **`var/external/bufr/rdbfdx.f`** -> AI Confidence: **99.29%**
334. **`var/external/bufr/rdcmps.f`** -> AI Confidence: **99.29%**
335. **`var/external/bufr/rdmemm.f`** -> AI Confidence: **99.29%**
336. **`var/external/bufr/rdmems.f`** -> AI Confidence: **99.29%**
337. **`var/external/bufr/rdmgsb.f`** -> AI Confidence: **99.29%**
338. **`var/external/bufr/rdmtbb.f`** -> AI Confidence: **99.29%**
339. **`var/external/bufr/rdmtbd.f`** -> AI Confidence: **99.29%**
340. **`var/external/bufr/rdtree.f`** -> AI Confidence: **99.29%**
341. **`var/external/bufr/rdusdx.f`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `101` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5216` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `external/esmf_time_f90/ESMF_Stubs.F90` (FORTRAN) -> Cumulative Risk: **734.06**
- **Archetype:** `file_cluster_4` (Distance: 13.693 IQR)
- **Magnitude:** 0.12 | **LOC:** 133 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9987%), Tech Debt (99.0842%)
- **Heaviest Functions:** `ESMF_Finalize` (Impact: 27.9), `ESMF_Initialize` (Impact: 15.2), `ESMF_LogWrite` (Impact: 3.3)

### 2. `external/RSL_LITE/module_dm.F` (FORTRAN) -> Cumulative Risk: **726.18**
- **Archetype:** `file_cluster_4` (Distance: 15.241 IQR)
- **Magnitude:** 8.94 | **LOC:** 4275 | **CtrlFlow:** 49.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.0993%)
- **Heaviest Functions:** `patch_domain_rsl_lite` (Impact: 1051.9), `compute_memory_dims_rsl_lite` (Impact: 656.1), `rsl_comm_iter` (Impact: 458.2)

### 3. `share/mediation_wrfmain.F` (FORTRAN) -> Cumulative Risk: **722.89**
- **Archetype:** `file_cluster_4` (Distance: 13.54 IQR)
- **Magnitude:** 197.44 | **LOC:** 267 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.981%), Concurrency (99.9508%)
- **Heaviest Functions:** `start_domain` (Impact: 36.0), `med_shutdown_io_recurse` (Impact: 13.8), `med_shutdown_io_recurse` (Impact: 3.8)

### 4. `hydro/MPP/mpp_land.F90` (FORTRAN) -> Cumulative Risk: **706.93**
- **Archetype:** `file_cluster_4` (Distance: 14.94 IQR)
- **Magnitude:** 4601.94 | **LOC:** 2838 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9889%)
- **Heaviest Functions:** `write_chanel_real` (Impact: 55.1), `write_chanel_int` (Impact: 55.0), `write_chanel_int8` (Impact: 55.0)

### 5. `main/ideal_em.F` (FORTRAN) -> Cumulative Risk: **706.53**
- **Archetype:** `file_cluster_13` (Distance: 12.273 IQR)
- **Magnitude:** 188.02 | **LOC:** 301 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Tech Debt (97.2987%), Cognitive Load (96.684%)
- **Heaviest Functions:** `med_initialdata_output` (Impact: 60.7), `med_initialdata_output` (Impact: 9.4), `ideal` (Impact: 3.9)

### 6. `share/mediation_nest_move.F` (FORTRAN) -> Cumulative Risk: **701.69**
- **Archetype:** `file_cluster_4` (Distance: 13.582 IQR)
- **Magnitude:** 953.3 | **LOC:** 1036 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.6148%), Cognitive Load (98.2891%)
- **Heaviest Functions:** `time_for_move2` (Impact: 170.1), `time_for_move2` (Impact: 46.6), `reconcile_nest_positions_over_tasks` (Impact: 31.8)

### 7. `share/wrf_timeseries.F` (FORTRAN) -> Cumulative Risk: **700.3**
- **Archetype:** `file_cluster_4` (Distance: 13.945 IQR)
- **Magnitude:** 1099.08 | **LOC:** 1200 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Concurrency (99.9778%)
- **Heaviest Functions:** `calc_p8w` (Impact: 21.0), `calc_ts` (Impact: 15.1), `write_ts` (Impact: 12.4)

### 8. `frame/module_cpl_oasis3.F` (FORTRAN) -> Cumulative Risk: **699.11**
- **Archetype:** `file_cluster_4` (Distance: 13.54 IQR)
- **Magnitude:** 332.82 | **LOC:** 532 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9894%), State Flux (99.9811%), Documentation (88.1227%)
- **Heaviest Functions:** `cpl_oasis_define` (Impact: 67.5), `cpl_oasis_rcv` (Impact: 19.5), `cpl_oasis_snd` (Impact: 19.0)

### 9. `hydro/MPP/module_mpp_GWBUCKET.F90` (FORTRAN) -> Cumulative Risk: **692.93**
- **Archetype:** `file_cluster_4` (Distance: 13.805 IQR)
- **Magnitude:** 339.84 | **LOC:** 215 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9073%)
- **Heaviest Functions:** `gw_write_io_real` (Impact: 45.3), `gw_write_io_int` (Impact: 40.9), `collectSizeInd` (Impact: 20.4)

### 10. `var/scripts/gen_be/gen_be_stage4_regional.ksh` (SHELL) -> Cumulative Risk: **691.82**
- **Archetype:** `file_cluster_12` (Distance: 11.729 IQR)
- **Magnitude:** 113.42 | **LOC:** 134 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (99.9999%), State Flux (99.9991%), Safety Score (99.7843%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 49.9), `Anonymous_Block` (Impact: 4.2), `Anonymous_Block` (Impact: 3.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `frame/md_calls.m4` (M4 | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.645 IQR)
- **Top Global Matches:** file_cluster_8: 8.645, file_cluster_7: 9.659, file_cluster_1: 9.795
- **Magnitude:** 57173.32 | **LOC:** 395 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.1288%), Tech Debt (16.1297%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `args: 491`, `func_start: 3`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phys/module_mp_nssl_2mom.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_11` (Drift: 17.152 IQR)
- **Top Global Matches:** file_cluster_11: 17.152, file_cluster_17: 17.282, file_cluster_0: 17.287
- **Magnitude:** 36402.48 | **LOC:** 25164 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.1933%), Tech Debt (9.9052%)
**Top Internal Functions/Classes:**
  * `nssl_2mom_gs` (Impact: 4817.9)
  * `nssl_2mom_driver` (Impact: 4657.7)
  * `setvtz` (Impact: 2288.7)
  * `ziegfall1d` (Impact: 1858.2)
  * `nssl_2mom_init` (Impact: 1333.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4923`, `structural_boundaries: 2153`, `args: 193`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 25`, `state_mutation: 17157`, `dead_code: 354`, `fragile_debt: 16`, `duplicate_logic: 2`
* *Architecture:* `io: 417`, `api: 27`, `concurrency: 18`
* *Defense:* `safety: 546`, `doc: 92`, `immutability_locks: 287`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dyn_em/module_advect_em.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.989 IQR)
- **Top Global Matches:** file_cluster_8: 15.989, file_cluster_11: 16.062, file_cluster_0: 16.151
- **Magnitude:** 31307.92 | **LOC:** 13047 | **CtrlFlow:** 88.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.6433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `advect_v` (Impact: 2860.0)
  * `advect_u` (Impact: 2696.3)
  * `advect_w` (Impact: 2635.0)
  * `advect_scalar_pd` (Impact: 2580.7)
  * `advect_scalar` (Impact: 2405.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2899`, `structural_boundaries: 397`, `args: 137`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `state_mutation: 11855`, `dead_code: 57`
* *Architecture:* `io: 18`, `api: 15`, `import: 4`
* *Defense:* `safety: 158`, `immutability_locks: 121`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.242
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` advection_kernel, module_bc, module_model_constants, module_wrf_error
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dyn_em/module_diffusion_em.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.964 IQR)
- **Top Global Matches:** file_cluster_8: 15.964, file_cluster_11: 16.092, file_cluster_0: 16.163
- **Magnitude:** 21332.16 | **LOC:** 8483 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.684%), Tech Debt (8.5094%)
**Top Internal Functions/Classes:**
  * `cal_deform_and_div` (Impact: 3431.5)
  * `vertical_diffusion_implicit` (Impact: 2018.2)
  * `cal_helicity` (Impact: 1078.6)
  * `tke_shear` (Impact: 887.1)
  * `nonlocal_flux` (Impact: 664.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2069`, `structural_boundaries: 616`, `args: 449`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6545`, `dead_code: 8`, `fragile_debt: 4`
* *Architecture:* `api: 35`, `import: 4`
* *Defense:* `safety: 439`, `immutability_locks: 301`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` module_big_step_utilities_em, module_bc, module_model_constants, module_state_description
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `phys/module_mp_full_sbm.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_4` (Drift: 16.123 IQR)
- **Top Global Matches:** file_cluster_4: 16.123, file_cluster_11: 16.188, file_cluster_0: 16.288
- **Magnitude:** 20411.4 | **LOC:** 13487 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.2947%), Tech Debt (7.8105%)
**Top Internal Functions/Classes:**
  * `SBM` (Impact: 4869.0)
  * `COAL_BOTT_NEW` (Impact: 350.8)
  * `ONECOND3` (Impact: 225.1)
  * `FULL_HUCMINIT` (Impact: 160.0)
  * `JERSUPSAT` (Impact: 142.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2092`, `structural_boundaries: 765`, `args: 188`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 89`, `state_mutation: 10883`, `dead_code: 128`, `fragile_debt: 1`
* *Architecture:* `io: 128`, `api: 79`, `concurrency: 324`, `import: 1`
* *Defense:* `safety: 150`, `doc: 2`, `sync_locks: 3`, `immutability_locks: 86`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` module_mp_radar
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dyn_em/module_initialize_real.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.926 IQR)
- **Top Global Matches:** file_cluster_11: 15.926, file_cluster_13: 16.045, file_cluster_0: 16.09
- **Magnitude:** 18102.08 | **LOC:** 9207 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.4709%), Tech Debt (8.2781%)
**Top Internal Functions/Classes:**
  * `init_domain_rk` (Impact: 5887.3)
  * `vert_interp` (Impact: 2222.0)
  * `rh_to_mxrat1` (Impact: 331.9)
  * `fillitup` (Impact: 279.4)
  * `rh_to_mxrat2` (Impact: 275.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3165`, `structural_boundaries: 591`, `args: 216`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6920`, `dead_code: 49`, `duplicate_logic: 2`
* *Architecture:* `io: 64`, `api: 38`, `concurrency: 43`, `import: 47`
* *Defense:* `safety: 253`, `doc: 2`, `immutability_locks: 173`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` module_domain, module_dm, module_optional_input, module_comm_dm, module_polarfft, module_timing, module_bc, module_model_constants...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `chem/module_mosaic_therm.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.768 IQR)
- **Top Global Matches:** file_cluster_11: 15.768, file_cluster_8: 15.822, file_cluster_13: 15.874
- **Magnitude:** 17161.44 | **LOC:** 17136 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.669%), Tech Debt (7.9165%)
**Top Internal Functions/Classes:**
  * `map_mosaic_species` (Impact: 1847.8)
  * `load_kappa_nonelectro` (Impact: 189.3)
  * `equilibrium` (Impact: 155.2)
  * `ions_to_electrolytes` (Impact: 130.2)
  * `ASTEM_flux_mix` (Impact: 92.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1970`, `structural_boundaries: 731`, `args: 253`, `func_start: 125`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 45`, `state_mutation: 12346`, `dead_code: 110`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 61`, `api: 107`, `import: 32`
* *Defense:* `safety: 31`, `doc: 54`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.242
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` module_data_mosaic_asect, module_peg_util, module_mosaic_gly, module_mosaic_movesect, module_data_mosaic_therm, module_data_mosaic_other, module_state_description
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `chem/module_isofwd.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.258 IQR)
- **Top Global Matches:** file_cluster_8: 15.258, file_cluster_13: 15.332, file_cluster_11: 15.459
- **Magnitude:** 17122.86 | **LOC:** 18724 | **CtrlFlow:** 85.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.3021%), Tech Debt (8.0233%)
**Top Internal Functions/Classes:**
  * `ISRP4F2p1` (Impact: 210.1)
  * `ISRP3F2p1` (Impact: 107.5)
  * `FUNCP52p1` (Impact: 81.2)
  * `FUNCP42p1` (Impact: 81.2)
  * `FUNCP32p1` (Impact: 81.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2401`, `structural_boundaries: 408`, `args: 164`, `func_start: 164`
* *Risk/State:* `high_risk_execution: 352`, `state_mutation: 11661`, `dead_code: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 105`, `import: 164`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` module_isrpia_inc.F
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phys/module_mp_ntu.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.739 IQR)
- **Top Global Matches:** file_cluster_8: 15.739, file_cluster_11: 15.934, file_cluster_13: 16.022
- **Magnitude:** 16919.24 | **LOC:** 6907 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.8801%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `LARGE_DT` (Impact: 2814.7)
  * `NTU_MICRO` (Impact: 1639.1)
  * `SMALL_DT` (Impact: 1289.4)
  * `SOLVE_AFAI` (Impact: 246.2)
  * `SOLVE_AFAS` (Impact: 181.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1226`, `structural_boundaries: 430`, `args: 92`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 9643`, `dead_code: 6`
* *Architecture:* `api: 32`, `import: 1`
* *Defense:* `safety: 222`, `immutability_locks: 184`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` module_wrf_error
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_ra_gfdleta.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.635 IQR)
- **Top Global Matches:** file_cluster_11: 16.635, file_cluster_4: 16.671, file_cluster_17: 16.691
- **Magnitude:** 15921.38 | **LOC:** 10164 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `FST88` (Impact: 1473.1)
  * `SPA88` (Impact: 1130.6)
  * `RADTN` (Impact: 1062.6)
  * `SWR93` (Impact: 538.8)
  * `LWR88` (Impact: 495.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1388`, `structural_boundaries: 1009`, `args: 244`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 84`, `state_mutation: 8434`, `dead_code: 50`
* *Architecture:* `io: 65`, `api: 33`, `concurrency: 129`, `import: 3`
* *Defense:* `safety: 780`, `doc: 1`, `immutability_locks: 655`, `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MODULE_CONFIGURE, MODULE_MODEL_CONSTANTS, MODULE_MP_ETANEW
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `phys/module_mp_fast_sbm.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.252 IQR)
- **Top Global Matches:** file_cluster_11: 16.252, file_cluster_4: 16.281, file_cluster_17: 16.368
- **Magnitude:** 15675.8 | **LOC:** 9054 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8309%), Tech Debt (7.7816%)
**Top Internal Functions/Classes:**
  * `FAST_SBM` (Impact: 3556.8)
  * `COAL_BOTT_NEW` (Impact: 443.7)
  * `FAST_HUCMINIT` (Impact: 386.4)
  * `coll_xyx_lwf` (Impact: 215.3)
  * `coll_xyz_lwf` (Impact: 180.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1564`, `structural_boundaries: 700`, `args: 261`, `func_start: 46`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 44`, `state_mutation: 7892`, `dead_code: 38`, `planned_debt: 1`
* *Architecture:* `io: 138`, `api: 39`, `concurrency: 174`, `import: 13`
* *Defense:* `safety: 399`, `doc: 1`, `immutability_locks: 199`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` module_domain, module_mp_SBM_Collision, module_dm, module_mp_SBM_Nucleation, module_mp_SBM_polar_radar, module_mp_SBM_BreakUp, scatt_tables, module_mp_SBM_Auxiliary
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `chem/module_mosaic_driver.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.563 IQR)
- **Top Global Matches:** file_cluster_8: 15.563, file_cluster_11: 15.626, file_cluster_13: 15.669
- **Magnitude:** 15152.9 | **LOC:** 7824 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.7311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init_data_mosaic_ptr` (Impact: 3506.9)
  * `mapaer_tofrom_host` (Impact: 3228.7)
  * `mosaic_aerchem_driver` (Impact: 185.5)
  * `init_data_mosaic_asect` (Impact: 114.0)
  * `aerchem_debug_dump` (Impact: 78.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2629`, `structural_boundaries: 110`, `args: 32`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 7900`, `dead_code: 30`
* *Architecture:* `io: 258`, `api: 5`, `import: 37`
* *Defense:* `safety: 26`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` module_mosaic_sumpm, module_mosaic_coag, module_mosaic_wetscav, module_mosaic_csuesat, module_data_mosaic_asect, module_peg_util, module_scalar_tables, module_mosaic_movesect...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `var/obsproc/MAP_plot/Dir_map/plots.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.205 IQR)
- **Top Global Matches:** file_cluster_8: 14.205, file_cluster_11: 14.479, file_cluster_13: 14.563
- **Magnitude:** 14655.68 | **LOC:** 14120 | **CtrlFlow:** 86.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.3357%), Tech Debt (10.1195%)
**Top Internal Functions/Classes:**
  * `mrddet` (Impact: 1084.5)
  * `crddet` (Impact: 791.5)
  * `crdclt` (Impact: 774.4)
  * `mpdrml` (Impact: 638.2)
  * `crdprt` (Impact: 507.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3352`, `structural_boundaries: 533`, `args: 84`, `func_start: 62`
* *Risk/State:* `high_risk_execution: 90`, `state_mutation: 5465`, `dead_code: 7`, `fragile_debt: 4`, `orphaned_logic: 9`
* *Architecture:* `io: 165`, `api: 62`, `import: 1`
* *Defense:* `safety: 38`, `doc: 2`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `share/module_bc.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.27%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.858 IQR)
- **Top Global Matches:** file_cluster_11: 15.858, file_cluster_8: 15.863, file_cluster_17: 15.938
- **Magnitude:** 14295.84 | **LOC:** 4690 | **CtrlFlow:** 84.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.9925%), Tech Debt (14.3911%)
**Top Internal Functions/Classes:**
  * `bdy_fields_pack` (Impact: 1559.9)
  * `set_physical_bc3d` (Impact: 920.6)
  * `set_physical_bc2d` (Impact: 789.7)
  * `stuff_bdytend_ijk` (Impact: 761.5)
  * `stuff_bdytend_old` (Impact: 742.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1914`, `structural_boundaries: 360`, `args: 283`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `state_mutation: 4483`, `dead_code: 15`, `duplicate_logic: 10`
* *Architecture:* `io: 23`, `api: 30`, `import: 13`
* *Defense:* `safety: 255`, `doc: 1`, `immutability_locks: 190`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.017
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` module_wrf_error, module_bc, module_model_constants, module_configure, module_state_description
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `phys/module_cu_mskf.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.733 IQR)
- **Top Global Matches:** file_cluster_11: 15.733, file_cluster_8: 15.764, file_cluster_0: 15.827
- **Magnitude:** 14216.96 | **LOC:** 8042 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.8089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MSKF_eta_PARA` (Impact: 2861.6)
  * `mskf_mphy` (Impact: 2353.1)
  * `MSKF_CMT` (Impact: 825.5)
  * `MSKF_CPS` (Impact: 819.6)
  * `mskf_nucleati` (Impact: 146.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1052`, `structural_boundaries: 703`, `args: 140`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 5`, `state_mutation: 6659`, `dead_code: 41`
* *Architecture:* `io: 46`, `api: 23`, `import: 5`
* *Defense:* `safety: 144`, `doc: 11`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` error_function, shr_kind_mod, module_cu_mp, module_wrf_error
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_lw.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.166 IQR)
- **Top Global Matches:** file_cluster_17: 16.166, file_cluster_13: 16.235, file_cluster_4: 16.237
- **Magnitude:** 14065.06 | **LOC:** 14634 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.7372%), Tech Debt (7.7712%)
**Top Internal Functions/Classes:**
  * `RRTMG_LWRAD` (Impact: 1354.4)
  * `generate_stochastic_clouds` (Impact: 362.9)
  * `setcoef` (Impact: 267.8)
  * `rtrnmc` (Impact: 188.1)
  * `inatm` (Impact: 142.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1140`, `structural_boundaries: 1469`, `args: 513`, `func_start: 87`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 13`, `state_mutation: 9522`, `dead_code: 44`, `planned_debt: 2`
* *Architecture:* `io: 45`, `api: 90`, `concurrency: 240`, `import: 177`
* *Defense:* `safety: 558`, `doc: 9`, `immutability_locks: 331`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.305
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` rrlw_con, rrlw_cld, rrlw_vsn, rrlw_kg03, rrtmg_lw_setcoef, module_state_description, module_model_constants, rrlw_kg09...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `dyn_em/module_big_step_utilities_em.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.968 IQR)
- **Top Global Matches:** file_cluster_8: 15.968, file_cluster_11: 15.969, file_cluster_0: 16.029
- **Magnitude:** 13673.82 | **LOC:** 6759 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.5265%), Tech Debt (8.5646%)
**Top Internal Functions/Classes:**
  * `rhs_ph` (Impact: 1327.1)
  * `phy_prep_part2` (Impact: 956.7)
  * `curvature` (Impact: 593.6)
  * `sixth_order_diffusion` (Impact: 561.6)
  * `calc_p_rho_phi` (Impact: 485.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1322`, `structural_boundaries: 491`, `args: 376`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 4807`, `dead_code: 23`, `fragile_debt: 3`
* *Architecture:* `io: 7`, `api: 44`, `import: 6`
* *Defense:* `safety: 335`, `doc: 72`, `immutability_locks: 231`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.528
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` module_state_description, module_model_constants, module_llxy, module_configure, module_wrf_error
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `chem/module_isrpia.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.492 IQR)
- **Top Global Matches:** file_cluster_11: 16.492, file_cluster_17: 16.584, file_cluster_0: 16.599
- **Magnitude:** 13599.56 | **LOC:** 14988 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.9526%), Tech Debt (13.2072%)
**Top Internal Functions/Classes:**
  * `CALCR1` (Impact: 144.5)
  * `ADJUST` (Impact: 128.3)
  * `ISRP3R` (Impact: 122.6)
  * `ISRP3F` (Impact: 107.3)
  * `ISOROPIA` (Impact: 76.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1750`, `structural_boundaries: 937`, `args: 310`, `func_start: 163`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 149`, `state_mutation: 9360`, `dead_code: 114`, `duplicate_logic: 16`
* *Architecture:* `io: 36`, `api: 129`, `import: 1`
* *Defense:* `safety: 160`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` module_data_isrpia
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phys/module_sf_noahdrv.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.501 IQR)
- **Top Global Matches:** file_cluster_11: 16.501, file_cluster_17: 16.548, file_cluster_0: 16.573
- **Magnitude:** 13453.46 | **LOC:** 5355 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.9531%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lsm_mosaic` (Impact: 6518.3)
  * `lsm` (Impact: 3282.7)
    * *Intent:* #endif
  * `LSMINIT` (Impact: 257.5)
  * `lsm_mosaic_init` (Impact: 153.3)
  * `SOIL_VEG_GEN_PARM` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 723`, `structural_boundaries: 685`, `args: 648`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3116`, `dead_code: 42`
* *Architecture:* `io: 100`, `api: 5`, `concurrency: 24`, `import: 22`
* *Defense:* `safety: 410`, `doc: 1`, `immutability_locks: 159`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` module_sf_noahlsm, module_sf_bep_bem, module_ra_gfdleta, mpas_atmphys_date_time, module_sf_bep, module_sf_noahlsm_glacial_only, mpas_atmphys_utilities, module_sf_urban...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_lwf.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.368 IQR)
- **Top Global Matches:** file_cluster_17: 15.368, file_cluster_13: 15.408, file_cluster_4: 15.507
- **Magnitude:** 13281.84 | **LOC:** 18237 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.5169%), Tech Debt (7.976%)
**Top Internal Functions/Classes:**
  * `RRTMG_LWRAD_FAST` (Impact: 1135.6)
  * `deallocateGPUrtrnmcg` (Impact: 1080.7)
  * `copyGPUcldprmcg` (Impact: 233.1)
  * `copyGPUSetCoef` (Impact: 89.3)
  * `rrtmg_lw_part` (Impact: 75.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1327`, `structural_boundaries: 2055`, `args: 607`, `func_start: 139`, `class_start: 53`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 12`, `state_mutation: 8624`, `dead_code: 53`, `duplicate_logic: 2`
* *Architecture:* `io: 50`, `api: 154`, `concurrency: 240`, `import: 256`
* *Defense:* `safety: 636`, `doc: 1`, `immutability_locks: 329`, `cleanup: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.305
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` rrlw_kg03_f, rrlw_kg08_f, rrlw_kg01_f, rrlw_kg11_f, module_model_constants, rrlw_kg10_f, cudadevice, rrtmg_lw_setcoef_f...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_sw.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.987 IQR)
- **Top Global Matches:** file_cluster_17: 15.987, file_cluster_4: 16.076, file_cluster_13: 16.132
- **Magnitude:** 13167.92 | **LOC:** 12787 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.386%), Tech Debt (9.2726%)
**Top Internal Functions/Classes:**
  * `RRTMG_SWRAD` (Impact: 3842.1)
  * `generate_stochastic_clouds_sw` (Impact: 411.7)
  * `cldprmc_sw` (Impact: 406.7)
  * `inatm_sw` (Impact: 142.1)
  * `setcoef_sw` (Impact: 125.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 922`, `structural_boundaries: 1323`, `args: 534`, `func_start: 64`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 16`, `state_mutation: 6599`, `dead_code: 41`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 58`, `api: 64`, `concurrency: 298`, `import: 160`
* *Defense:* `safety: 584`, `doc: 11`, `immutability_locks: 349`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` parrrsw, rrtmg_sw_rad, rrsw_con, mcica_subcol_gen_sw, module_model_constants, rrsw_kg24, rrsw_ref, rrsw_kg25...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `chem/module_isorev.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.189 IQR)
- **Top Global Matches:** file_cluster_8: 15.189, file_cluster_13: 15.402, file_cluster_11: 15.501
- **Magnitude:** 13064.56 | **LOC:** 11875 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.4544%), Tech Debt (8.1706%)
**Top Internal Functions/Classes:**
  * `ISRP4R2p1` (Impact: 209.4)
  * `CALCR12p1` (Impact: 144.6)
  * `CALCU12p1` (Impact: 144.6)
  * `ISRP3R2p1` (Impact: 122.6)
  * `CALCW62p1` (Impact: 73.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1410`, `structural_boundaries: 228`, `args: 69`, `func_start: 69`
* *Risk/State:* `high_risk_execution: 44`, `state_mutation: 9921`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 68`, `import: 69`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.221
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` module_isrpia_inc.F
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phys/module_ra_rrtmg_swf.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.759 IQR)
- **Top Global Matches:** file_cluster_17: 15.759, file_cluster_4: 15.878, file_cluster_13: 15.924
- **Magnitude:** 12815.7 | **LOC:** 13799 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6077%), Tech Debt (9.6887%)
**Top Internal Functions/Classes:**
  * `RRTMG_SWRAD_FAST` (Impact: 2814.3)
  * `cldprmc_sw` (Impact: 301.4)
  * `mcica_sw` (Impact: 297.5)
  * `rrtmg_sw_sub` (Impact: 235.0)
  * `setcoef_sw` (Impact: 174.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1146`, `structural_boundaries: 1613`, `args: 813`, `func_start: 64`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 5927`, `dead_code: 53`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 61`, `api: 64`, `concurrency: 303`, `import: 163`
* *Defense:* `safety: 861`, `doc: 1`, `immutability_locks: 598`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rrsw_kg29_f, mcica_subcol_gen_sw_f, rrtmg_sw_spcvmc_f, module_model_constants, rrsw_tbl_f, parrrsw_f, rrsw_kg28_f, rrsw_kg22_f...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_cu_sas.F` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.121 IQR)
- **Top Global Matches:** file_cluster_11: 16.121, file_cluster_8: 16.187, file_cluster_13: 16.22
- **Magnitude:** 12477.74 | **LOC:** 5606 | **CtrlFlow:** 87.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.3786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sascnvn` (Impact: 2252.6)
  * `SASCNV` (Impact: 1974.3)
    * *Intent:* #if (NMM_CORE == 1)
  * `shalcnv` (Impact: 1405.4)
  * `CU_SAS` (Impact: 469.1)
  * `OLD_ARW_SHALCV` (Impact: 133.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1183`, `structural_boundaries: 177`, `args: 49`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5946`, `dead_code: 52`
* *Architecture:* `io: 3`, `api: 10`, `import: 18`
* *Defense:* `safety: 64`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MODULE_GFS_FUNCPHYS, MODULE_GFS_machine, MODULE_GFS_PHYSCONS, MODULE_GFS_funcphys, MODULE_GFS_physcons, MODULE_GFS_MACHINE
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `hydro/Routing/module_HYDRO_io.F90` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.782 IQR)
- **Top Global Matches:** file_cluster_17: 16.782, file_cluster_11: 17.097, file_cluster_0: 17.173
- **Magnitude:** 11828.38 | **LOC:** 11400 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.6595%), Tech Debt (9.2548%)
**Top Internal Functions/Classes:**
  * `output_chrt_bak` (Impact: 416.1)
  * `output_chrt` (Impact: 342.5)
  * `readLinkSL` (Impact: 280.6)
    * *Intent:* #endif
  * `output_chrt2` (Impact: 246.5)
  * `mpp_output_chrt2` (Impact: 240.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1662`, `structural_boundaries: 1373`, `args: 648`, `func_start: 101`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 27`, `state_mutation: 6395`, `dead_code: 172`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 241`, `api: 98`, `import: 33`
* *Defense:* `safety: 808`, `immutability_locks: 296`, `cleanup: 178`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` module_hydro_stop, config_base, module_RT_data, netcdf, module_mpp_reachls, MODULE_mpp_GWBUCKET, module_HYDRO_utils, iso_fortran_env...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `var/scripts/gen_be/gen_be_wrapper.ksh` (SHELL) | Magnitude: 82.06 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 44, api: 43, indent_spaces: 34, branch: 22
- `chem/KPP/kpp/kpp-2.1/int/gillespie.c` (C) | Magnitude: 0.07 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 43, indent_spaces: 12, api: 9, branch: 6
- `external/io_esmf/module_esmf_extensions.F90` (FORTRAN) | Magnitude: 0.3 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 239, state_mutation: 140, args: 122, structural_boundaries: 74
- `tools/check_for_bad_includes.pl` (PERL) | Magnitude: 0.07 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 50, indent_spaces: 34, branch: 23, structural_boundaries: 15
- `chem/KPP/kpp/kpp-2.1/drv/general_stochastic.c` (C) | Magnitude: 0.07 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 48, indent_spaces: 29, api: 14, debug_prints: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `chem/module_aerosols_soa_vbs.F` (FORTRAN) | Magnitude: 4871.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 3421, state_mutation: 2939, structural_boundaries: 966, branch: 335
- `chem/module_cam_mam_aerchem_driver.F` (FORTRAN) | Magnitude: 2453.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 772, state_mutation: 645, branch: 261, structural_boundaries: 83
- `phys/module_mp_cammgmp_driver.F` (FORTRAN) | Magnitude: 2943.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1544, state_mutation: 1328, structural_boundaries: 484, branch: 329
- `var/obsproc/src/module_map.F90` (FORTRAN) | Magnitude: 433.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 322, indent_spaces: 227, branch: 45, scientific: 35
- `var/da/da_radar/da_check_max_iv_radar.inc` (FORTRAN) | Magnitude: 653.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 627, indent_spaces: 46, branch: 16, api: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/regtest_nmmnest.csh` (SHELL) | Magnitude: 1.91 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 1497, io: 1165, branch: 1164, safety_bypasses: 1038
- `tools/regtest_hwrf.csh` (SHELL) | Magnitude: 2.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 1588, branch: 1226, io: 1221, safety_bypasses: 1120
- `tools/DOMAIN_TIME_TEST/DOMAIN_TIME_TEST.csh` (SHELL) | Magnitude: 0.02 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 29, indent_spaces: 20, debug_prints: 14, branch: 11
- `configure` (SHELL) | Magnitude: 1416.84 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 751, branch: 650, state_mutation: 396, debug_prints: 240
- `chem/KPP/compile_wkc` (SHELL) | Magnitude: 55.48 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 35, indent_spaces: 33, branch: 29, reflection_metaprogramming: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `var/external/bufr/dxmini.f` (FORTRAN) | Magnitude: 0.09 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 68, indent_spaces: 37, branch: 6, high_risk_execution: 2
- `var/external/bufr/rewnbf.f` (FORTRAN) | Magnitude: 0.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 82, indent_spaces: 65, branch: 17, high_risk_execution: 6
- `chem/module_vash_settling.F` (FORTRAN) | Magnitude: 324.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 227, indent_spaces: 170, branch: 50, structural_boundaries: 26
- `external/io_esmf/io_esmf.F90` (FORTRAN) | Magnitude: 1.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1255, structural_boundaries: 620, state_mutation: 498, args: 342
- `hydro/Routing/Noah_distr_routing_subsurface.F90` (FORTRAN) | Magnitude: 931.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 436, state_mutation: 385, branch: 153, structural_boundaries: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `chem/module_cam_mam_addemiss.F` (FORTRAN) | Magnitude: 2438.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1045, indent_spaces: 420, branch: 217, indent_tabs: 212
- `chem/module_mosaic_soa_vbs.F` (FORTRAN) | Magnitude: 1779.98 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1344, indent_spaces: 1149, branch: 124, structural_boundaries: 92
- `hydro/nudging/module_stream_nudging.F90` (FORTRAN) | Magnitude: 1766.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 983, state_mutation: 892, branch: 460, structural_boundaries: 263
- `chem/module_phot_tuv.F` (FORTRAN) | Magnitude: 3316.6 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1594, state_mutation: 1249, branch: 323, structural_boundaries: 310
- `hydro/Routing/Noah_distr_routing_overland.F90` (FORTRAN) | Magnitude: 1213.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 472, state_mutation: 413, branch: 200, macros: 77

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `share/module_trajectory.F` (FORTRAN) | Magnitude: 3943.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 2421, state_mutation: 2060, branch: 816, structural_boundaries: 381
- `frame/module_cpl.F` (FORTRAN) | Magnitude: 474.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 286, state_mutation: 171, branch: 93, structural_boundaries: 91
- `phys/module_mp_sbu_ylin.F` (FORTRAN) | Magnitude: 2316.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 1435, indent_spaces: 1009, branch: 158, structural_boundaries: 130
- `var/da/da_4dvar/da_finalize_model.inc` (FORTRAN) | Magnitude: 159.22 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 140, indent_spaces: 9, api: 4, branch: 3
- `phys/module_sf_qnsesfc.F` (FORTRAN) | Magnitude: 1562.44 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 897, indent_spaces: 687, structural_boundaries: 80, branch: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `hydro/Routing/Overland/module_overland_mass_balance.F90` (FORTRAN) | Magnitude: 16.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, state_mutation: 8, args: 6
- `external/io_esmf/ext_esmf_read_field.F90` (FORTRAN) | Magnitude: 0.27 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 170, state_mutation: 96, branch: 34, structural_boundaries: 32
- `external/io_esmf/ext_esmf_write_field.F90` (FORTRAN) | Magnitude: 0.27 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 166, state_mutation: 98, branch: 34, structural_boundaries: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tools/mpi2_thread_test.c` (C) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, pointers: 3, api: 2, import: 2
- `dyn_em/module_big_step_utilities_em.F` (FORTRAN) | Magnitude: 13673.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 4807, indent_spaces: 4234, branch: 1322, structural_boundaries: 491
- `dyn_em/module_damping_em.F` (FORTRAN) | Magnitude: 120.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 51, indent_spaces: 43, structural_boundaries: 13, branch: 12
- `chem/KPP/util/write_decomp/write_decomp.F` (FORTRAN) | Magnitude: 48.54 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, state_mutation: 35, io: 30, serialization_parsing: 28
- `chem/module_cbmz_rodas3_solver.F` (FORTRAN) | Magnitude: 741.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 292, indent_spaces: 194, branch: 85, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `external/atm_ocn/mpi_more.F` (FORTRAN) | Magnitude: 0.02 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, branch: 5, structural_boundaries: 5, args: 5
- `wrftladj/module_em_ad.F` (FORTRAN) | Magnitude: 5753.0 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1464, state_mutation: 1110, dead_code: 607, branch: 556
- `var/external/wavelet/idwtai2_w.c` (C) | Magnitude: 0.04 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 21, pointers: 21, indent_spaces: 18, api: 10
- `phys/module_cam_support.F` (FORTRAN) | Magnitude: 113.86 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 79, state_mutation: 65, structural_boundaries: 59, args: 39
- `var/scripts/gen_be/gen_be_gsi.ksh` (SHELL) | Magnitude: 69.6 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 62, branch: 39, safety_bypasses: 33, reflection_metaprogramming: 32

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `phys/module_diag_functions.F` -> Churn: **100.0%** | Cog Load: 91.4732% | Debt: 10.9012%
- `share/wrf_timeseries.F` -> Churn: **100.0%** | Cog Load: 92.6689% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `phys/module_diag_functions.F` -> **Yuxuan Xie** (100.0% isolated ownership) | Magnitude: 1190.08
- `share/wrf_timeseries.F` -> **Massimo D'isidoro** (100.0% isolated ownership) | Magnitude: 1099.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `dyn_em/module_initialize_real.F` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)
- `chem/module_input_chem_data.F` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)
- `phys/module_radiation_driver.F` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)
- `external/RSL_LITE/module_dm.F` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `frame/module_domain.F` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frame/module_wrf_error.F` -> **Severity: 690.395** (Blast Radius: 23.263 * Doc Risk: 29.6778%)
- `frame/module_driver_constants.F` -> **Severity: 655.953** (Blast Radius: 12.764 * Doc Risk: 51.3909%)
- `phys/module_cam_support.F` -> **Severity: 538.771** (Blast Radius: 6.108 * Doc Risk: 88.2075%)
- `tools/registry.h` -> **Severity: 463.776** (Blast Radius: 6.355 * Doc Risk: 72.9782%)
- `frame/module_configure.F` -> **Severity: 427.698** (Blast Radius: 13.077 * Doc Risk: 32.7061%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
