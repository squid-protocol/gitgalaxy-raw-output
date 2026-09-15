# ARCHITECTURAL_BRIEF: wrf-fortran
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wrf-model/WRF.git` |
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
| Total Artifacts | 4912 |
| Analyzed Artifacts (Scanned) | 3708 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1204 |
| Total LOC | 1181896 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 75.5% |
| Dominant Lang | FORTRAN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6843 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1689 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0928 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 81 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| FORTRAN | 2928 | 1084570 | 79.0% |
| C | 338 | 68737 | 9.1% |
| MAKEFILE | 165 | 8001 | 4.4% |
| PLAINTEXT | 117 | 7 | 3.2% |
| SHELL | 85 | 14030 | 2.3% |
| MARKDOWN | 27 | 0 | 0.7% |
| PYTHON | 13 | 2243 | 0.4% |
| M4 | 9 | 738 | 0.2% |
| MATLAB | 8 | 160 | 0.2% |
| YACC | 6 | 2058 | 0.2% |
| BINARY_THREAT | 5 | 5 | 0.1% |
| PERL | 4 | 1321 | 0.1% |
| OBJECTIVE-C | 2 | 18 | 0.1% |
| CSV | 1 | 8 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +2.49; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 32%, Declarative / Non-Code 31%, Data / Markup / Trivial 15%, Defensive Guards Files 7%, I/O & Config Routines Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3558 | 96.0% |
| Unknown | 12 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 138 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1204*

**Composition by Extension & Reason:**
- `.f90`: 372x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 127 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1083 LOC)
- `no_extension`: 46x Unresolved Ambiguity (No Retainable Structure), 38x Unsupported Format (.undeterminable), 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.f`: 3x Excluded (Embedded Array/Matrix Payload: 9753 commas in 2194 LOC), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (Machine-Generated Source Code Signature: 57 LOC)
- `.eqn`: 48x Excluded (Unsupported Extension: '.eqn')
- `.kpp`: 47x Excluded (Unsupported Extension: '.kpp')
- `.spc`: 47x Excluded (Unsupported Extension: '.spc')
- `.info`: 42x Excluded (Unsupported Extension: '.info')
- `.equiv`: 30x Excluded (Unsupported Extension: '.equiv')
- `.code`: 28x Excluded (Unsupported Extension: '.code')
- `.tbl`: 17x Excluded (Unsupported Extension: '.TBL'), 7x Excluded (Unsupported Extension: '.tbl')
- `.ncl`: 19x Excluded (Unsupported Extension: '.ncl')
- `.input`: 17x Excluded (Unsupported Extension: '.input')
- `.cmake`: 16x Excluded (Unsupported Extension: '.cmake')
- `.mk`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.setup`: 9x Excluded (Unsupported Extension: '.setup')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 39.7 | 45.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 63.4 | 82.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.0 | 3.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 66.7 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 58.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 55.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 47827 | 1308 | 20 | `phys/module_ra_cam.F` |
| cleanup | 4979 | 657 | 2 | `wrftladj/module_adtl_grid_utilities.F` |
| guards | 100642 | 1604 | 52 | `phys/module_ra_rrtmg_swf.F` |
| danger | 20886 | 1443 | 8 | `tools/regtest_hwrf.csh` |
| concurrency | 7660 | 233 | 0 | `phys/module_mp_wdm7.F` |
| connectivity | 14776 | 2554 | 9 | `arch/md_calls.inc` |
| io | 26813 | 1193 | 13 | `tools/regtest.csh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 461 | 39 | 0 | `hydro/MPP/mpp_land.F90` |
| time | 181 | 39 | 0 | `tools/regtest.csh` |
| serialization | 1445 | 188 | 0 | `hydro/OrchestratorLayer/config.F90` |
| regex | 837 | 39 | 0 | `arch/Config.pl` |
| events | 272 | 53 | 0 | `var/da/da_statistics/da_analysis_stats.inc` |
| tests | 34 | 16 | 0 | `configure` |
| docs | 2612 | 232 | 0 | `frame/module_io.F` |
| debt | 13780 | 716 | 5 | `chem/chemics_init.F` |
| mutation | 631512 | 3042 | 327 | `chem/module_isofwd.F` |
| dead_code | 11870 | 1694 | 6 | `wrftladj/module_em_ad.F` |
| credential | 2 | 2 | 0 | `external/RSL_LITE/gen_comms.c` |
| threat | 1480 | 239 | 0 | `external/io_grib1/WGRIB/gds.h` |
| ml_ai | 26364 | 1170 | 17 | `phys/module_ra_rrtmg_lw.F` |
| ui | 6 | 3 | 0 | `chem/KPP/kpp/kpp-2.1/util/sparsity_plots.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/regtest.csh` (Hits: 1423)
- `tools/regtest_hwrf.csh` (Hits: 1221)
- `tools/regtest_nmmnest.csh` (Hits: 1165)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **module_configure.F** (`frame/module_configure.F`) — 201 inbound connections
2. **module_model_constants.F** (`share/module_model_constants.F`) — 159 inbound connections
3. **module_domain.F** (`frame/module_domain.F`) — 129 inbound connections
4. **module_wrf_error.F** (`frame/module_wrf_error.F`) — 92 inbound connections
5. **module_dm.F** (`external/RSL_LITE/module_dm.F`) — 90 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **module_physics_init.F** (`phys/module_physics_init.F`) — 117 outbound dependencies
2. **da_read_obs_ascii.inc** (`var/da/da_obs_io/da_read_obs_ascii.inc`) — 103 outbound dependencies
3. **chem_driver.F** (`chem/chem_driver.F`) — 43 outbound dependencies
4. **module_microphysics_driver.F** (`phys/module_microphysics_driver.F`) — 41 outbound dependencies
5. **solve_em_ad.F** (`wrftladj/solve_em_ad.F`) — 41 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `surface_driver` **(Many-Argument Workhorses)** (@ `phys/module_surface_driver.F`) -> Impact: **22820.7** | LOC: 4497
- `nssl_2mom_gs` **(Many-Argument Workhorses)** (@ `phys/module_mp_nssl_2mom.F`) -> Impact: **17591.0** | LOC: 12531
- `chem_init` **(Many-Argument Workhorses)** (@ `chem/chemics_init.F`) -> Impact: **11599.5** | LOC: 2090
- `radiation_driver` **(Many-Argument Workhorses)** (@ `phys/module_radiation_driver.F`) -> Impact: **11596.8** | LOC: 3272
- `microphysics_driver` **(Many-Argument Workhorses)** (@ `phys/module_microphysics_driver.F`) -> Impact: **10346.7** | LOC: 2925
- `lsm_mosaic` **(Many-Argument Workhorses)** (@ `phys/module_sf_noahdrv.F`) -> Impact: **6059.1** | LOC: 2592
- `pbl_driver` **(Many-Argument Workhorses)** (@ `phys/module_pbl_driver.F`) -> Impact: **5441.1** | LOC: 2274
- `bio_emissions_megan2` **(Many-Argument Workhorses)** (@ `chem/module_bioemi_megan2.F`) -> Impact: **5429.6** | LOC: 1821
- `phy_init` **(Many-Argument Workhorses)** (@ `phys/module_physics_init.F`) -> Impact: **5032.9** | LOC: 1712
- `deng_shcu` **(Many-Argument Workhorses)** (@ `phys/module_shcu_deng.F`) -> Impact: **4821.8** | LOC: 3143

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `phys` | 230 | 811458.82 | 62.87% | 5.27% |
| `chem` | 190 | 315558.18 | 48.64% | 6.12% |
| `dyn_em` | 38 | 108400.4 | 57.03% | 12.49% |
| `share` | 55 | 63074.4 | 47.59% | 16.84% |
| `wrftladj` | 29 | 46784.86 | 50.61% | 16.69% |
| `run` | 17 | 37626.94 | 0.0% | 0.0% |
| `hydro/Routing` | 18 | 34050.16 | 60.17% | 10.13% |
| `frame` | 59 | 18649.04 | 25.94% | 11.72% |
| `var/obsproc/src` | 39 | 16879.34 | 53.5% | 7.34% |
| `var/da/da_radiance` | 109 | 16460.42 | 53.63% | 6.31% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `share/bobrand.c` -> **100.0%** Exposure
- `frame/clog.c` -> **99.9999%** Exposure
- `frame/hires_timer.c` -> **99.9999%** Exposure
- `var/external/bufr/cread.c` -> **99.9999%** Exposure
- `external/esmf_time_f90/ESMF_Clock.F90` -> **99.9998%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `arch/Config.pl` -> **100.0%** Exposure
- `tools/subinfo` -> **100.0%** Exposure
- `arch/configure_reader.py` -> **100.0%** Exposure
- `tools/manage_externals/manic/externals_description.py` -> **100.0%** Exposure
- `tools/manage_externals/manic/externals_status.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `hydro/MPP/mpp_land.F90` -> **72** Orphaned Functions | **0** Duplicates
- `wrftladj/adStack.c` -> **45** Orphaned Functions | **0** Duplicates
- `wrftladj/adBuffer.F` -> **42** Orphaned Functions | **0** Duplicates
- `frame/libmassv.F` -> **40** Orphaned Functions | **0** Duplicates
- `chem/KPP/kpp/kpp-2.1/src/scanner.c` -> **37** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `98` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5478` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `share/wrf_timeseries.F` (FORTRAN) -> Cumulative Risk: **798.15**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.07)
- **Magnitude:** 1382.18 | **LOC:** 1200 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Churn (100.0%)
- **Heaviest Functions:** `calc_ts_locations` (Compute Cores, Impact: 87.8), `write_ts` (Compute Cores, Impact: 87.7), `calc_p8w` (Many-Argument Workhorses, Impact: 13.1)

### 2. `hydro/MPP/mpp_land.F90` (FORTRAN) -> Cumulative Risk: **790.32**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.76)
- **Magnitude:** 4528.48 | **LOC:** 2838 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `MPP_CHANNEL_COM_REAL` (Many-Argument Workhorses, Impact: 87.8), `MPP_CHANNEL_COM_REAL8` (Many-Argument Workhorses, Impact: 87.8), `MPP_CHANNEL_COM_INT` (Many-Argument Workhorses, Impact: 87.8)

### 3. `external/RSL_LITE/module_dm.F` (FORTRAN) -> Cumulative Risk: **789.53**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.55)
- **Magnitude:** 7.42 | **LOC:** 4275 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `patch_domain_rsl_lite` (Many-Argument Workhorses, Impact: 789.6), `compute_memory_dims_rsl_lite` (Many-Argument Workhorses, Impact: 430.4), `rsl_comm_iter` (Many-Argument Workhorses, Impact: 372.8)

### 4. `hydro/MPP/module_mpp_ReachLS.F90` (FORTRAN) -> Cumulative Risk: **749.96**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.84)
- **Magnitude:** 2108.6 | **LOC:** 1500 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `TONODE2RSL8` (Many-Argument Workhorses, Impact: 54.2), `TONODE2RSL` (Many-Argument Workhorses, Impact: 54.0), `pack_decomp_int` (Many-Argument Workhorses, Impact: 39.8)

### 5. `dyn_em/module_wps_io_arw.F` (FORTRAN) -> Cumulative Risk: **739.0**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.27)
- **Magnitude:** 2733.3 | **LOC:** 1976 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `read_wps` (Many-Argument Workhorses, Impact: 409.2), `inventory_wrf_binary_file` (Many-Argument Workhorses, Impact: 166.5), `count_recs_wrf_binary_file` (Many-Argument Workhorses, Impact: 72.8)

### 6. `external/RSL_LITE/interp_domain_em_small.F` (FORTRAN) -> Cumulative Risk: **736.27**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -1.03)
- **Magnitude:** 0.33 | **LOC:** 412 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9823%)
- **Heaviest Functions:** `interp_domain_em_small_part1` (Many-Argument Workhorses, Impact: 45.4), `interp_domain_em_small_part2` (Many-Argument Workhorses, Impact: 33.8), `feedback_nest_prep` (Many-Argument Workhorses, Impact: 5.9)

### 7. `external/atm_ocn/cmpcomm.F` (FORTRAN) -> Cumulative Risk: **721.69**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.28)
- **Magnitude:** 0.82 | **LOC:** 986 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9479%)
- **Heaviest Functions:** `CMP_INIT` (Many-Argument Workhorses, Impact: 25.5), `CMP_gnr_RECV` (Many-Argument Workhorses, Impact: 24.1), `CMP_RECV` (Many-Argument Workhorses, Impact: 21.3)

### 8. `hydro/Routing/module_gw_gw2d.F90` (FORTRAN) -> Cumulative Risk: **717.32**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -1.42)
- **Magnitude:** 2774.44 | **LOC:** 2131 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `gwstep` (Many-Argument Workhorses, Impact: 364.7), `sub_n_form` (Many-Argument Workhorses, Impact: 187.1), `parxsolv1` (Many-Argument Workhorses, Impact: 98.1)

### 9. `var/da/da_par_util/da_proc_stats_combine.inc` (FORTRAN) -> Cumulative Risk: **715.73**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.75)
- **Magnitude:** 228.7 | **LOC:** 108 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `da_proc_stats_combine` (Many-Argument Workhorses, Impact: 53.2)

### 10. `dyn_em/module_initialize_ideal.F` (FORTRAN) -> Cumulative Risk: **714.66**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.19)
- **Magnitude:** 2947.18 | **LOC:** 2253 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.9578%)
- **Heaviest Functions:** `init_domain_rk` (Compute Cores, Impact: 494.9), `get_sounding_b_wave` (Many-Argument Workhorses, Impact: 65.4), `calc_jet_sounding` (Many-Argument Workhorses, Impact: 62.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `phys/module_mp_nssl_2mom.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 50203.82 | **LOC:** 25164 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.1527%), Tech Debt (8.7587%)
**Top Internal Functions/Classes:**
  * `nssl_2mom_gs` **(Many-Argument Workhorses)** (Impact: 17591.0)
  * `nssl_2mom_driver` **(Many-Argument Workhorses)** (Impact: 4581.7)
  * `NUCOND` **(Many-Argument Workhorses)** (Impact: 2434.8)
  * `setvtz` **(Many-Argument Workhorses)** (Impact: 2155.8)
  * `ziegfall1d` **(Many-Argument Workhorses)** (Impact: 1680.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Rce:* 9 instances
* *Amplified Cascading Flux:* 5177 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 4
* *Sec Tainted Injection (weighted view):* 9
* *State Mutation (weighted view):* 16525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4566`, `structural_boundaries: 2183`, `args: 196`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 6171`, `dead_code: 354`, `fragile_debt: 16`
* *Architecture:* `io: 416`, `api: 26`, `concurrency: 3`
* *Defense:* `safety: 550`, `doc: 92`, `immutability_locks: 290`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000832
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dyn_em/module_advect_em.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 29612.84 | **LOC:** 13047 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.9469%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `advect_v` **(Many-Argument Workhorses)** (Impact: 2629.8)
  * `advect_scalar_pd` **(Many-Argument Workhorses)** (Impact: 2552.0)
    * *Intent:* #endif
  * `advect_u` **(Many-Argument Workhorses)** (Impact: 2535.3)
  * `advect_w` **(Many-Argument Workhorses)** (Impact: 2441.6)
  * `advect_scalar` **(Many-Argument Workhorses)** (Impact: 2211.6)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 3531 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 11316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2699`, `structural_boundaries: 397`, `args: 137`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4254`, `dead_code: 57`
* *Architecture:* `io: 17`, `api: 16`, `import: 4`
* *Defense:* `safety: 158`, `immutability_locks: 121`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000871
  * `Imports (Out-Degree: 3):` advection_kernel, module_bc, module_model_constants, module_wrf_error
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_surface_driver.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 26766.72 | **LOC:** 7289 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.2157%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `surface_driver` **(Many-Argument Workhorses)** (Impact: 22820.7)
  * `sfclayrev_seaice_wrapper` **(Many-Argument Workhorses)** (Impact: 248.2)
  * `sfclay_seaice_wrapper` **(Many-Argument Workhorses)** (Impact: 239.1)
  * `mynn_seaice_wrapper` **(Many-Argument Workhorses)** (Impact: 178.2)
  * `myjsfc_seaice_wrapper` **(Many-Argument Workhorses)** (Impact: 171.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 619 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 2368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 843`, `structural_boundaries: 1070`, `args: 1224`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 1130`, `dead_code: 25`
* *Architecture:* `io: 4`, `api: 13`, `import: 43`
* *Defense:* `safety: 964`, `doc: 2`, `immutability_locks: 315`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.222
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.000479
  * `Imports (Out-Degree: 29):` module_cpl, module_irrigation, module_model_constants, module_ra_gfdleta, module_sf_clm, module_sf_ctsm, module_sf_fogdes, module_sf_gfs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_mp_full_sbm.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 18988.78 | **LOC:** 13487 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.626%), Tech Debt (7.768%)
**Top Internal Functions/Classes:**
  * `SBM` **(Many-Argument Workhorses)** (Impact: 3179.0)
  * `ONECOND3` **(Many-Argument Workhorses)** (Impact: 745.9)
  * `ONECOND2` **(Many-Argument Workhorses)** (Impact: 369.4)
  * `ONECOND1` **(Many-Argument Workhorses)** (Impact: 299.1)
  * `COAL_BOTT_NEW` **(Many-Argument Workhorses)** (Impact: 288.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 32 instances
* *Amplified Cascading Flux:* 3098 instances
* *High Risk Execution (weighted view):* 80
* *Concurrency (weighted view):* 249
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 10494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1731`, `structural_boundaries: 778`, `args: 188`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 86`, `state_mutation: 4298`, `dead_code: 128`, `fragile_debt: 1`
* *Architecture:* `io: 118`, `api: 78`, `concurrency: 89`, `import: 1`
* *Defense:* `safety: 150`, `sync_locks: 3`, `immutability_locks: 86`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000832
  * `Imports (Out-Degree: 1):` module_mp_radar
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_radiation_driver.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 17751.66 | **LOC:** 5711 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.7587%), Tech Debt (7.9669%)
**Top Internal Functions/Classes:**
  * `radiation_driver` **(Many-Argument Workhorses)** (Impact: 11596.8)
  * `toposhad` **(Many-Argument Workhorses)** (Impact: 461.7)
  * `cal_cldfra1` **(Many-Argument Workhorses)** (Impact: 244.5)
  * `toposhad_init` **(Many-Argument Workhorses)** (Impact: 225.8)
  * `find_cloudLayers` **(Many-Argument Workhorses)** (Impact: 218.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1048 instances
* *Concurrency (weighted view):* 28
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 3575
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 993`, `structural_boundaries: 476`, `args: 372`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 1479`, `dead_code: 45`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `api: 22`, `concurrency: 8`, `import: 35`
* *Defense:* `safety: 376`, `doc: 4`, `immutability_locks: 181`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.376
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.002212
  * `Imports (Out-Degree: 23):` module_bc, module_comm_dm, module_dm, module_domain, module_model_constants, module_mp_thompson, module_ra_aerosol, module_ra_cam...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `chem/module_isofwd.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 17294.44 | **LOC:** 18724 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.763%), Tech Debt (7.9127%)
**Top Internal Functions/Classes:**
  * `ISRP4F2p1` **(Many-Argument Workhorses)** (Impact: 216.3)
  * `ISRP3F2p1` **(Many-Argument Workhorses)** (Impact: 110.6)
  * `FUNCP52p1` **(Compute Cores)** (Impact: 62.9)
  * `FUNCP42p1` **(Compute Cores)** (Impact: 62.9)
  * `FUNCP32p1` **(Compute Cores)** (Impact: 62.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3616 instances
* *State Mutation (weighted view):* 13413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2049`, `structural_boundaries: 408`, `args: 164`, `func_start: 164`
* *Risk/State:* `safety_bypasses: 110`, `state_mutation: 6181`, `dead_code: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 105`, `import: 164`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` module_isrpia_inc.F
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dyn_em/module_diffusion_em.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 17273.62 | **LOC:** 8483 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.6316%), Tech Debt (8.4382%)
**Top Internal Functions/Classes:**
  * `cal_deform_and_div` **(Many-Argument Workhorses)** (Impact: 1973.4)
  * `vertical_diffusion_implicit` **(Many-Argument Workhorses)** (Impact: 1791.2)
  * `cal_helicity` **(Many-Argument Workhorses)** (Impact: 653.0)
  * `nonlocal_flux` **(Many-Argument Workhorses)** (Impact: 592.3)
  * `vertical_diffusion_2` **(Many-Argument Workhorses)** (Impact: 583.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1878 instances
* *State Mutation (weighted view):* 5830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1573`, `structural_boundaries: 619`, `args: 450`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 2074`, `dead_code: 8`, `fragile_debt: 4`
* *Architecture:* `api: 38`, `import: 4`
* *Defense:* `safety: 439`, `immutability_locks: 301`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000799
  * `Imports (Out-Degree: 3):` module_bc, module_big_step_utilities_em, module_model_constants, module_state_description
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `phys/module_ra_gfdleta.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 17068.2 | **LOC:** 10164 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.0253%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SWR93` **(Many-Argument Workhorses)** (Impact: 1885.4)
  * `FST88` **(Many-Argument Workhorses)** (Impact: 1479.2)
  * `SPA88` **(Many-Argument Workhorses)** (Impact: 1146.5)
  * `RADTN` **(Many-Argument Workhorses)** (Impact: 1054.2)
  * `LWR88` **(Many-Argument Workhorses)** (Impact: 503.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 94 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 2641 instances
* *Concurrency (weighted view):* 117
* *Memory Alloc (weighted view):* 10
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 8118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1300`, `structural_boundaries: 1030`, `args: 245`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 4`, `state_mutation: 2836`, `dead_code: 50`
* *Architecture:* `io: 61`, `api: 33`, `concurrency: 27`, `import: 3`
* *Defense:* `safety: 794`, `immutability_locks: 655`, `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002343
  * `Imports (Out-Degree: 3):` MODULE_CONFIGURE, MODULE_MODEL_CONSTANTS, MODULE_MP_ETANEW
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `chem/module_mosaic_therm.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 15618.72 | **LOC:** 17136 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0818%), Tech Debt (7.8814%)
**Top Internal Functions/Classes:**
  * `map_mosaic_species` **(Many-Argument Workhorses)** (Impact: 1416.0)
  * `equilibrium` **(Many-Argument Workhorses)** (Impact: 156.4)
  * `load_kappa_nonelectro` **(Compute Cores)** (Impact: 112.5)
  * `ASTEM_flux_mix` **(Compute Cores)** (Impact: 77.8)
  * `ASTEM_non_volatiles` **(Compute Cores)** (Impact: 68.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 2301 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 11783
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1679`, `structural_boundaries: 737`, `args: 253`, `func_start: 123`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 7181`, `dead_code: 110`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 61`, `api: 106`, `import: 32`
* *Defense:* `safety: 31`, `doc: 6`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001135
  * `Imports (Out-Degree: 6):` module_data_mosaic_asect, module_data_mosaic_other, module_data_mosaic_therm, module_mosaic_gly, module_mosaic_movesect, module_peg_util, module_state_description
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_mp_ntu.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 15567.6 | **LOC:** 6907 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.7073%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `LARGE_DT` **(Many-Argument Workhorses)** (Impact: 2816.2)
  * `NTU_MICRO` **(Many-Argument Workhorses)** (Impact: 1626.0)
  * `SMALL_DT` **(Many-Argument Workhorses)** (Impact: 1289.8)
  * `SOLVE_AFAI` **(Many-Argument Workhorses)** (Impact: 246.4)
  * `SOLVE_AFAS` **(Many-Argument Workhorses)** (Impact: 181.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2377 instances
* *State Mutation (weighted view):* 8301
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1213`, `structural_boundaries: 432`, `args: 92`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 3547`, `dead_code: 6`
* *Architecture:* `api: 32`, `import: 1`
* *Defense:* `safety: 222`, `immutability_locks: 184`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000832
  * `Imports (Out-Degree: 1):` module_wrf_error
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_mp_fast_sbm.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 14266.44 | **LOC:** 9054 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.6635%), Tech Debt (7.7216%)
**Top Internal Functions/Classes:**
  * `FAST_SBM` **(Many-Argument Workhorses)** (Impact: 2439.3)
  * `ONECOND2` **(Many-Argument Workhorses)** (Impact: 384.4)
  * `COAL_BOTT_NEW` **(Many-Argument Workhorses)** (Impact: 366.8)
  * `ONECOND3` **(Many-Argument Workhorses)** (Impact: 363.1)
  * `FAST_HUCMINIT` **(Compute Cores)** (Impact: 302.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 17 instances
* *Amplified Rce:* 28 instances
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 2188 instances
* *High Risk Execution (weighted view):* 72
* *Concurrency (weighted view):* 159
* *Memory Alloc (weighted view):* 91
* *Sec Tainted Injection (weighted view):* 28
* *State Mutation (weighted view):* 7222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1291`, `structural_boundaries: 720`, `args: 261`, `func_start: 45`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 75`, `state_mutation: 2846`, `dead_code: 38`, `planned_debt: 1`
* *Architecture:* `io: 124`, `api: 43`, `concurrency: 39`, `import: 13`
* *Defense:* `safety: 413`, `doc: 1`, `immutability_locks: 199`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000832
  * `Imports (Out-Degree: 3):` module_dm, module_domain, module_mp_SBM_Auxiliary, module_mp_SBM_BreakUp, module_mp_SBM_Collision, module_mp_SBM_Nucleation, module_mp_SBM_polar_radar, scatt_tables
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_physics_init.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 13758.6 | **LOC:** 5751 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.3958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `phy_init` **(Many-Argument Workhorses)** (Impact: 5032.9)
  * `bl_init` **(Many-Argument Workhorses)** (Impact: 4490.9)
  * `mp_init` **(Many-Argument Workhorses)** (Impact: 643.7)
  * `ra_init` **(Many-Argument Workhorses)** (Impact: 619.8)
  * `landuse_init` **(Many-Argument Workhorses)** (Impact: 369.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 455 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 100
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 758`, `structural_boundaries: 1065`, `args: 1094`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 560`, `dead_code: 31`
* *Architecture:* `io: 37`, `api: 19`, `concurrency: 25`, `import: 126`
* *Defense:* `safety: 699`, `immutability_locks: 246`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.217
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.000266
  * `Imports (Out-Degree: 99):` MODULE_CU_BMJ, constituents, microphy_p3, modal_aero_data, modal_aero_initialize_data_phys, module_bl_acm, module_bl_boulac, module_bl_camuwpbl_driver...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_lwf.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 13275.48 | **LOC:** 18237 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.8762%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RRTMG_LWRAD_FAST` **(Many-Argument Workhorses)** (Impact: 1939.1)
  * `deallocateGPUrtrnmcg` **(Compute Cores)** (Impact: 704.9)
  * `copyGPUcldprmcg` **(Many-Argument Workhorses)** (Impact: 209.6)
  * `rrtmg_lw_part` **(Many-Argument Workhorses)** (Impact: 165.2)
  * `copyGPUSetCoef` **(Compute Cores)** (Impact: 58.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 53 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2582 instances
* *High Risk Execution (weighted view):* 18
* *Concurrency (weighted view):* 76
* *Memory Alloc (weighted view):* 52
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 8612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1190`, `structural_boundaries: 2109`, `args: 607`, `func_start: 136`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 22`, `state_mutation: 3448`, `dead_code: 53`
* *Architecture:* `io: 49`, `api: 139`, `concurrency: 56`, `import: 256`
* *Defense:* `safety: 633`, `immutability_locks: 330`, `cleanup: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.274
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002009
  * `Imports (Out-Degree: 3):` MODULE_RA_CLWRF_SUPPORT, MersenneTwister_f, cudadevice, cudafor, gpu_mcica_subcol_gen_lw, gpu_rrtmg_lw_cldprmc, gpu_rrtmg_lw_rtrnmc, gpu_rrtmg_lw_setcoef...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_lw.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 13261.26 | **LOC:** 14634 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.4745%), Tech Debt (7.7278%)
**Top Internal Functions/Classes:**
  * `RRTMG_LWRAD` **(Many-Argument Workhorses)** (Impact: 2245.0)
  * `generate_stochastic_clouds` **(Many-Argument Workhorses)** (Impact: 344.3)
  * `setcoef` **(Many-Argument Workhorses)** (Impact: 256.3)
  * `rtrnmc` **(Many-Argument Workhorses)** (Impact: 190.0)
  * `inatm` **(Many-Argument Workhorses)** (Impact: 147.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2561 instances
* *High Risk Execution (weighted view):* 21
* *Concurrency (weighted view):* 76
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 8339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1086`, `structural_boundaries: 1501`, `args: 513`, `func_start: 85`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 24`, `state_mutation: 3217`, `dead_code: 44`, `planned_debt: 2`
* *Architecture:* `io: 44`, `api: 90`, `concurrency: 56`, `import: 177`
* *Defense:* `safety: 558`, `immutability_locks: 331`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.274
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002009
  * `Imports (Out-Degree: 3):` MODULE_RA_CLWRF_SUPPORT, MersenneTwister, mcica_random_numbers, mcica_subcol_gen_lw, module_model_constants, module_state_description, module_wrf_error, parkind...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `var/obsproc/MAP_plot/Dir_map/plots.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 13131.3 | **LOC:** 14120 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5448%), Tech Debt (9.4296%)
**Top Internal Functions/Classes:**
  * `mrddet` **(Many-Argument Workhorses)** (Impact: 730.4)
  * `crddet` **(Many-Argument Workhorses)** (Impact: 611.5)
  * `crdclt` **(Many-Argument Workhorses)** (Impact: 577.8)
  * `mpdrml` **(Many-Argument Workhorses)** (Impact: 446.6)
  * `crdprt` **(Many-Argument Workhorses)** (Impact: 352.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 2058 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 6420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2455`, `structural_boundaries: 619`, `args: 84`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 159`, `high_risk_execution: 1`, `state_mutation: 2304`, `dead_code: 7`, `fragile_debt: 4`, `unreferenced_by_name: 6`
* *Architecture:* `io: 164`, `api: 62`
* *Defense:* `safety: 38`, `doc: 2`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phys/module_cu_mskf.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 12912.88 | **LOC:** 8042 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.2684%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MSKF_eta_PARA` **(Many-Argument Workhorses)** (Impact: 2512.1)
  * `mskf_mphy` **(Many-Argument Workhorses)** (Impact: 1685.6)
  * `MSKF_CPS` **(Many-Argument Workhorses)** (Impact: 792.0)
  * `MSKF_CMT` **(Many-Argument Workhorses)** (Impact: 681.1)
  * `mskf_nucleati` **(Many-Argument Workhorses)** (Impact: 122.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 1936 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 6572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 858`, `structural_boundaries: 709`, `args: 140`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 2700`, `dead_code: 41`
* *Architecture:* `io: 46`, `api: 22`, `import: 5`
* *Defense:* `safety: 144`, `doc: 9`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000799
  * `Imports (Out-Degree: 1):` error_function, module_cu_mp, module_wrf_error, shr_kind_mod
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_sf_noahdrv.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 12803.28 | **LOC:** 5355 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3821%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lsm_mosaic` **(Many-Argument Workhorses)** (Impact: 6059.1)
  * `lsm` **(Many-Argument Workhorses)** (Impact: 3048.1)
  * `lsm_mosaic_init` **(Many-Argument Workhorses)** (Impact: 488.0)
  * `LSMINIT` **(Many-Argument Workhorses)** (Impact: 225.1)
    * *Intent:* #if defined(wrfmodel)
  * `SOIL_VEG_GEN_PARM` **(Many-Argument Workhorses)** (Impact: 107.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 746 instances
* *State Mutation (weighted view):* 2722
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 670`, `structural_boundaries: 688`, `args: 650`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 1230`, `dead_code: 42`
* *Architecture:* `io: 97`, `api: 5`, `concurrency: 72`, `import: 11`
* *Defense:* `safety: 412`, `doc: 1`, `immutability_locks: 159`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000799
  * `Imports (Out-Degree: 8):` module_data_gocart_dust, module_ra_gfdleta, module_sf_bep, module_sf_bep_bem, module_sf_noahlsm, module_sf_noahlsm_glacial_only, module_sf_urban, module_wrf_error...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `chem/module_isrpia.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 12792.96 | **LOC:** 14988 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4963%), Tech Debt (8.0417%)
**Top Internal Functions/Classes:**
  * `ISRP3R` **(Many-Argument Workhorses)** (Impact: 124.3)
  * `ISRP3F` **(Many-Argument Workhorses)** (Impact: 110.5)
  * `CALCR1` **(Compute Cores)** (Impact: 86.7)
  * `ISOROPIA` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `ADJUST` **(Compute Cores)** (Impact: 67.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 2677 instances
* *High Risk Execution (weighted view):* 1
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 9516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1561`, `structural_boundaries: 949`, `args: 310`, `func_start: 155`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 4162`, `dead_code: 114`, `unreferenced_by_name: 4`
* *Architecture:* `io: 36`, `api: 129`, `import: 1`
* *Defense:* `safety: 160`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` module_data_isrpia
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dyn_em/module_big_step_utilities_em.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 12747.78 | **LOC:** 6759 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.6328%), Tech Debt (8.4681%)
**Top Internal Functions/Classes:**
  * `rhs_ph` **(Many-Argument Workhorses)** (Impact: 1218.5)
  * `phy_prep_part2` **(Many-Argument Workhorses)** (Impact: 934.0)
  * `curvature` **(Many-Argument Workhorses)** (Impact: 596.8)
  * `horizontal_diffusion` **(Many-Argument Workhorses)** (Impact: 395.0)
  * `sixth_order_diffusion` **(Many-Argument Workhorses)** (Impact: 376.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1466 instances
* *State Mutation (weighted view):* 4515
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1201`, `structural_boundaries: 499`, `args: 377`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 1583`, `dead_code: 23`, `fragile_debt: 3`
* *Architecture:* `io: 7`, `api: 43`, `import: 5`
* *Defense:* `safety: 336`, `doc: 72`, `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.003214
  * `Imports (Out-Degree: 4):` module_configure, module_llxy, module_model_constants, module_state_description, module_wrf_error
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `chem/module_isorev.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 12713.52 | **LOC:** 11875 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.5642%), Tech Debt (8.0453%)
**Top Internal Functions/Classes:**
  * `ISRP4R2p1` **(Many-Argument Workhorses)** (Impact: 212.8)
  * `ISRP3R2p1` **(Many-Argument Workhorses)** (Impact: 124.2)
  * `CALCR12p1` **(Compute Cores)** (Impact: 86.7)
  * `CALCU12p1` **(Compute Cores)** (Impact: 86.7)
  * `ISRP2R2p1` **(Many-Argument Workhorses)** (Impact: 64.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2750 instances
* *State Mutation (weighted view):* 10349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1366`, `structural_boundaries: 228`, `args: 69`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 4849`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 68`, `import: 69`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` module_isrpia_inc.F
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `chem/chemics_init.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 12492.2 | **LOC:** 3538 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.0685%), Tech Debt (10.5904%)
**Top Internal Functions/Classes:**
  * `chem_init` **(Many-Argument Workhorses)** (Impact: 11599.5)
  * `print_chem_species_index` **(Compute Cores)** (Impact: 52.3)
    * *Intent:* #ifdef CHEM_DBG_I
  * `termite_initialize` **(Defensive Guards)** (Impact: 13.7)
  * `VPRM_par_initialize` **(Many-Argument Workhorses)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *State Mutation (weighted view):* 752
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1075`, `structural_boundaries: 93`, `args: 33`, `func_start: 4`
* *Risk/State:* `state_mutation: 326`, `dead_code: 20`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 4`, `import: 38`
* *Defense:* `safety: 31`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` module_HLawConst, module_aerosols_soa_vbs, module_aerosols_soa_vbs_het, module_aerosols_sorgam, module_aerosols_sorgam_vbs, module_cam_mam_init, module_cam_mam_initmixrats, module_cam_mam_wetscav...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phys/module_ra_rrtmg_swf.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 12450.78 | **LOC:** 13799 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.0326%), Tech Debt (7.9483%)
**Top Internal Functions/Classes:**
  * `RRTMG_SWRAD_FAST` **(Many-Argument Workhorses)** (Impact: 2421.2)
  * `rrtmg_sw_sub` **(Many-Argument Workhorses)** (Impact: 632.2)
  * `spcvmc_sw` **(Many-Argument Workhorses)** (Impact: 386.6)
  * `cldprmc_sw` **(Many-Argument Workhorses)** (Impact: 305.0)
  * `mcica_sw` **(Many-Argument Workhorses)** (Impact: 198.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1697 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 89
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 5758
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 978`, `structural_boundaries: 1642`, `args: 813`, `func_start: 62`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 15`, `state_mutation: 2364`, `dead_code: 53`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 60`, `api: 64`, `concurrency: 74`, `import: 163`
* *Defense:* `safety: 861`, `doc: 1`, `immutability_locks: 598`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001848
  * `Imports (Out-Degree: 4):` MODULE_RA_CLWRF_SUPPORT, cudafor, mcica_random_numbers_f, mcica_subcol_gen_sw_f, module_model_constants, module_ra_rrtmg_lwf, module_wrf_error, parrrsw_f...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_cu_sas.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 12240.38 | **LOC:** 5606 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.2395%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sascnvn` **(Many-Argument Workhorses)** (Impact: 2273.1)
  * `SASCNV` **(Many-Argument Workhorses)** (Impact: 1995.8)
  * `shalcnv` **(Many-Argument Workhorses)** (Impact: 1416.7)
  * `CU_SAS` **(Many-Argument Workhorses)** (Impact: 474.0)
  * `OLD_ARW_SHALCV` **(Many-Argument Workhorses)** (Impact: 134.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 1746 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 5653
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1182`, `structural_boundaries: 177`, `args: 49`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 2161`, `dead_code: 52`
* *Architecture:* `io: 3`, `api: 10`, `import: 18`
* *Defense:* `safety: 64`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000799
  * `Imports (Out-Degree: 3):` MODULE_GFS_FUNCPHYS, MODULE_GFS_MACHINE, MODULE_GFS_PHYSCONS, MODULE_GFS_funcphys, MODULE_GFS_machine, MODULE_GFS_physcons
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `chem/module_mosaic_driver.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 12050.62 | **LOC:** 7824 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.4869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init_data_mosaic_ptr` **(Many-Argument Workhorses)** (Impact: 3414.3)
  * `mapaer_tofrom_host` **(Many-Argument Workhorses)** (Impact: 3108.7)
  * `mosaic_aerchem_driver` **(Many-Argument Workhorses)** (Impact: 168.9)
  * `init_data_mosaic_asect` **(Many-Argument Workhorses)** (Impact: 87.1)
  * `aerchem_debug_dump` **(Many-Argument Workhorses)** (Impact: 45.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1230 instances
* *State Mutation (weighted view):* 5085
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2516`, `structural_boundaries: 119`, `args: 32`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 2625`, `dead_code: 30`
* *Architecture:* `io: 258`, `api: 5`, `import: 37`
* *Defense:* `safety: 31`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.001704
  * `Imports (Out-Degree: 12):` module_configure, module_data_mosaic_asect, module_data_mosaic_other, module_data_mosaic_therm, module_mosaic2_driver, module_mosaic_coag, module_mosaic_csuesat, module_mosaic_movesect...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `phys/module_shcu_deng.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 11736.34 | **LOC:** 5441 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.9965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deng_shcu` **(Many-Argument Workhorses)** (Impact: 4821.8)
  * `deng_shcu_driver` **(Many-Argument Workhorses)** (Impact: 666.6)
  * `TPMIXBG` **(Many-Argument Workhorses)** (Impact: 105.5)
  * `TPMIX` **(Many-Argument Workhorses)** (Impact: 91.0)
  * `deng_shcu_init` **(Many-Argument Workhorses)** (Impact: 64.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 1683 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 67
* *State Mutation (weighted view):* 5430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 713`, `structural_boundaries: 239`, `args: 135`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 2064`, `dead_code: 76`
* *Architecture:* `io: 51`, `api: 21`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 135`, `immutability_locks: 72`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000799
  * `Imports (Out-Degree: 1):` module_wrf_error
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `phys/module_diag_functions.F` -> Churn: **100.0%** | Cog Load: 89.5041% | Debt: 77.3536%
- `share/wrf_timeseries.F` -> Churn: **100.0%** | Cog Load: 99.6857% | Debt: 9.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `share/wrf_timeseries.F` -> **Massimo D'isidoro** (100.0% isolated ownership) | Magnitude: 1382.18
- `phys/module_diag_functions.F` -> **Yuxuan Xie** (100.0% isolated ownership) | Magnitude: 1023.68

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `external/RSL_LITE/module_dm.F` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `frame/module_configure.F` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9985%)
- `frame/module_domain.F` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `main/module_wrf_top.F` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `phys/module_radiation_driver.F` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `frame/module_configure.F` -> **Severity: 4.025** (Embedded: 0.0518 * Error Risk: 77.7661%)
- `frame/module_domain.F` -> **Severity: 2.867** (Embedded: 0.0324 * Error Risk: 88.35%)
- `frame/module_wrf_error.F` -> **Severity: 2.748** (Embedded: 0.0525 * Error Risk: 52.3512%)
- `external/RSL_LITE/module_dm.F` -> **Severity: 2.295** (Embedded: 0.0238 * Error Risk: 96.3431%)
- `frame/module_machine.F` -> **Severity: 2.194** (Embedded: 0.0229 * Error Risk: 95.7646%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frame/module_wrf_error.F` -> **Severity: 2264.4** (Blast Radius: 22.644 * Doc Risk: 100.0%)
- `frame/module_configure.F` -> **Severity: 1292.3** (Blast Radius: 12.923 * Doc Risk: 100.0%)
- `frame/module_driver_constants.F` -> **Severity: 1237.7** (Blast Radius: 12.377 * Doc Risk: 100.0%)
- `share/module_model_constants.F` -> **Severity: 1202.2** (Blast Radius: 12.022 * Doc Risk: 100.0%)
- `frame/module_domain.F` -> **Severity: 676.554** (Blast Radius: 6.892 * Doc Risk: 98.1651%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
