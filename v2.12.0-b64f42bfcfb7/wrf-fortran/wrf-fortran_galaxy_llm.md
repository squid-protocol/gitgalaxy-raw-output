# ARCHITECTURAL_BRIEF: wrf-fortran
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wrf-model/WRF.git` |
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
- **Scope:** 3504 analyzed artifact(s), 1176603 LOC.
- **Load-bearing artifact:** `var/da/da_tracing/da_trace_exit.inc` -- 960 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `phys/module_physics_init.F` -- pulls in 117 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `phys/module_mp_nssl_2mom.F` at magnitude 50206.22 (structural weight, not risk).
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
| Total Artifacts | 4912 |
| Analyzed Artifacts (Scanned) | 3504 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1408 |
| Total LOC | 1176603 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 71.3% |
| Dominant Lang | FORTRAN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6997 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2181 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2311 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 167 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| FORTRAN | 2739 | 1078782 | 78.2% |
| C | 317 | 66857 | 9.0% |
| MAKEFILE | 159 | 7562 | 4.5% |
| PLAINTEXT | 129 | 7 | 3.7% |
| SHELL | 83 | 13989 | 2.4% |
| MARKDOWN | 26 | 0 | 0.7% |
| PYTHON | 13 | 2243 | 0.4% |
| CPP | 9 | 1993 | 0.3% |
| MATLAB | 8 | 160 | 0.2% |
| M4 | 6 | 683 | 0.2% |
| PERL | 4 | 1321 | 0.1% |
| YACC | 4 | 1589 | 0.1% |
| YAML | 2 | 186 | 0.1% |
| OBJECTIVE-C | 2 | 18 | 0.1% |
| HTML | 1 | 1134 | 0.0% |
| CSV | 1 | 8 | 0.0% |
| SCHEME | 1 | 71 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 11 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3486 |
| latin-1 | latin-1-fallback | 7 |
| unknown | unknown | 7 |
| cp1252 | cp1252-fallback | 4 |

> 2 guessed file(s) read as double-byte text that decodes strictly as shift_jis / gbk: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `var/convertor/wave2grid_kma/OUTZ.inc`, `var/convertor/wave2grid_kma/PRESUB.inc`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 50%, Data / Markup / Trivial 16%, Large Core Modules (2) 11%, Declarative / Non-Code 8%, Large Core Modules 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3245 | 92.6% |
| Unknown | 7 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 252 | 7.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1408*

**Composition by Extension & Reason:**
- `.f90`: 387x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.f`: 179x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Embedded Array/Matrix Payload: 9753 commas in 2194 LOC), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 46x Unresolved Ambiguity (No Retainable Structure), 39x Unsupported Format (.undeterminable), 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.eqn`: 48x Excluded (Unsupported Extension: '.eqn')
- `.kpp`: 47x Excluded (Unsupported Extension: '.kpp')
- `.spc`: 47x Excluded (Unsupported Extension: '.spc')
- `.info`: 42x Excluded (Unsupported Extension: '.info')
- `.equiv`: 30x Excluded (Unsupported Extension: '.equiv')
- `.code`: 28x Excluded (Unsupported Extension: '.code')
- `.tbl`: 17x Excluded (Unsupported Extension: '.TBL'), 7x Excluded (Unsupported Extension: '.tbl')
- `.ncl`: 19x Excluded (Unsupported Extension: '.ncl')
- `.input`: 17x Excluded (Unsupported Extension: '.input')
- `.h`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 428 LOC), 1x Excluded (Embedded Array/Matrix Payload: 10679 commas in 2279 LOC)
- `.c`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2406 LOC)
- `.mk`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 43.2 | 55.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.3 | 52.6 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.6 | 14.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 26.1 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.3 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 70.9 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 79.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 42271 | 1079 | 14 | `phys/module_sf_clm.F` |
| cleanup | 7837 | 757 | 3 | `phys/module_sf_clm.F` |
| guards | 110827 | 2219 | 59 | `phys/module_sf_clm.F` |
| danger | 20061 | 1329 | 8 | `tools/regtest_hwrf.csh` |
| concurrency | 9399 | 333 | 0 | `arch/md_calls.inc` |
| connectivity | 14649 | 2642 | 9 | `phys/module_sf_clm.F` |
| io | 27608 | 1266 | 15 | `tools/regtest.csh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 491 | 42 | 0 | `hydro/MPP/mpp_land.F90` |
| time | 196 | 44 | 0 | `tools/regtest.csh` |
| serialization | 1550 | 217 | 0 | `hydro/OrchestratorLayer/config.F90` |
| regex | 836 | 38 | 0 | `arch/Config.pl` |
| events | 26 | 8 | 0 | `tools/manage_externals/manic/utils.py` |
| tests | 31 | 13 | 0 | `configure` |
| docs | 2666 | 279 | 0 | `arch/md_calls.inc` |
| debt | 14754 | 733 | 5 | `chem/chemics_init.F` |
| mutation | 642798 | 2832 | 350 | `phys/module_sf_clm.F` |
| dead_code | 10041 | 2425 | 5 | `wrftladj/module_em_ad.F` |
| credential | 2 | 2 | 0 | `share/module_check_a_mundo.F` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 20803 | 1050 | 9 | `phys/module_ra_rrtmg_lw.F` |
| ui | 126 | 4 | 0 | `external/io_phdf5/INSTALL.htm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/regtest.csh` (Hits: 1423)
- `tools/regtest_hwrf.csh` (Hits: 1221)
- `tools/regtest_nmmnest.csh` (Hits: 1165)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **da_trace_exit.inc** (`var/da/da_tracing/da_trace_exit.inc`) — 960 inbound connections
2. **da_trace_entry.inc** (`var/da/da_tracing/da_trace_entry.inc`) — 959 inbound connections
3. **module_configure.F** (`frame/module_configure.F`) — 208 inbound connections
4. **da_error.inc** (`var/da/da_reporting/da_error.inc`) — 203 inbound connections
5. **module_fr_fire_util.F** (`phys/module_fr_fire_util.F`) — 163 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **module_physics_init.F** (`phys/module_physics_init.F`) — 117 outbound dependencies
2. **module_sf_clm.F** (`phys/module_sf_clm.F`) — 93 outbound dependencies
3. **chem_driver.F** (`chem/chem_driver.F`) — 43 outbound dependencies
4. **module_microphysics_driver.F** (`phys/module_microphysics_driver.F`) — 41 outbound dependencies
5. **solve_em_ad.F** (`wrftladj/solve_em_ad.F`) — 41 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `surface_driver` **(Many-Argument Workhorses)** (@ `phys/module_surface_driver.F`) -> Impact: **22820.7** | LOC: 4497
- `nssl_2mom_gs` **(Many-Argument Workhorses)** (@ `phys/module_mp_nssl_2mom.F`) -> Impact: **17591.7** | LOC: 12544
- `chem_init` **(Many-Argument Workhorses)** (@ `chem/chemics_init.F`) -> Impact: **11599.5** | LOC: 2090
- `radiation_driver` **(Many-Argument Workhorses)** (@ `phys/module_radiation_driver.F`) -> Impact: **11596.8** | LOC: 3272
- `microphysics_driver` **(Many-Argument Workhorses)** (@ `phys/module_microphysics_driver.F`) -> Impact: **10346.8** | LOC: 2927
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
| `phys` | 231 | 865261.2 | 62.88% | 4.3% |
| `chem` | 190 | 317647.88 | 48.64% | 5.05% |
| `dyn_em` | 39 | 112235.12 | 57.47% | 10.16% |
| `share` | 55 | 64477.2 | 47.69% | 13.5% |
| `wrftladj` | 29 | 47233.06 | 50.6% | 16.5% |
| `hydro/Routing` | 18 | 35343.26 | 58.98% | 9.72% |
| `run` | 12 | 35126.94 | 0.0% | 0.0% |
| `var/da/da_radiance` | 109 | 32608.08 | 63.18% | 21.17% |
| `var/da/da_obs_io` | 40 | 23641.74 | 67.22% | 15.74% |
| `frame` | 59 | 19238.64 | 25.32% | 14.52% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `frame/module_dm_stubs.F` -> **100.0%** Exposure
- `share/bobrand.c` -> **100.0%** Exposure
- `frame/clog.c` -> **99.9999%** Exposure
- `frame/hires_timer.c` -> **99.9999%** Exposure
- `var/external/bufr/cread.c` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `arch/Config.pl` -> **100.0%** Exposure
- `tools/subinfo` -> **100.0%** Exposure
- `arch/configure_reader.py` -> **100.0%** Exposure
- `tools/manage_externals/manic/externals_description.py` -> **100.0%** Exposure
- `tools/manage_externals/manic/externals_status.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `external/io_pio/wrf_io.F90` -> **83** Orphaned Functions | **0** Duplicates
- `hydro/MPP/mpp_land.F90` -> **70** Orphaned Functions | **0** Duplicates
- `external/io_grib1/io_grib1.F` -> **64** Orphaned Functions | **0** Duplicates
- `external/io_grib2/io_grib2.F` -> **64** Orphaned Functions | **0** Duplicates
- `frame/xxx_template_ioapi.F` -> **64** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `81` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5253` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `phys/module_mp_nssl_2mom.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.676)
- **Top Global Matches:** file_cluster_3: 9.676, file_cluster_8: 16.566, file_cluster_6: 29.155
- **Magnitude:** 50206.22 | **LOC:** 25164 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.136; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.2%), Guard Balance (formerly Safety Score) (87.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nssl_2mom_gs` **(Many-Argument Workhorses)** (Impact: 17591.7)
  * `nssl_2mom_driver` **(Many-Argument Workhorses)** (Impact: 4581.8)
  * `NUCOND` **(Many-Argument Workhorses)** (Impact: 2434.8)
  * `setvtz` **(Many-Argument Workhorses)** (Impact: 2155.9)
  * `ziegfall1d` **(Many-Argument Workhorses)** (Impact: 1680.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 5177 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 16525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4566`, `structural_boundaries: 2183`, `args: 196`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 6171`, `dead_code: 156`, `fragile_debt: 16`
* *Architecture:* `io: 416`, `api: 26`, `concurrency: 3`
* *Defense:* `safety: 550`, `doc: 92`, `immutability_locks: 290`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000985
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_sf_clm.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.306)
- **Top Global Matches:** file_cluster_8: 9.306, file_cluster_6: 11.224, file_cluster_4: 18.922
- **Magnitude:** 46955.38 | **LOC:** 61486 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **93**; blast radius 0.281; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clminit` **(Many-Argument Workhorses)** (Impact: 1985.9)
  * `clmdrv` **(Many-Argument Workhorses)** (Impact: 1528.1)
  * `CNiniTimeVar` **(Many-Argument Workhorses)** (Impact: 917.5)
  * `FrictionVelocity` **(Many-Argument Workhorses)** (Impact: 600.3)
  * `SNICAR_RT` **(Many-Argument Workhorses)** (Impact: 491.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1452 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 6838 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 110
* *Memory Alloc (weighted view):* 1441
* *State Mutation (weighted view):* 26228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4530`, `structural_boundaries: 10611`, `args: 1639`, `func_start: 291`, `class_start: 173`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 12552`, `dead_code: 184`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 88`, `api: 554`, `concurrency: 45`, `import: 670`
* *Defense:* `safety: 1917`, `doc: 10`, `immutability_locks: 1048`, `cleanup: 1448`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.281
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.001931
  * `Imports (Out-Degree: 7):` BalanceCheckMod, BareGroundFluxesMod, Biogeophysics1Mod, Biogeophysics2Mod, BiogeophysicsLakeMod, C13SummaryMod, CASAMod, CASAPhenologyMod...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `dyn_em/module_advect_em.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 23.625)
- **Top Global Matches:** file_cluster_3: 23.625, file_cluster_1: 25.542, file_cluster_8: 45.172
- **Magnitude:** 29612.84 | **LOC:** 13047 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.783; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4254`, `dead_code: 51`
* *Architecture:* `io: 17`, `api: 16`, `import: 4`
* *Defense:* `safety: 158`, `immutability_locks: 121`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.783
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.044527
  * `Imports (Out-Degree: 3):` advection_kernel, module_bc, module_model_constants, module_wrf_error
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_surface_driver.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.017)
- **Top Global Matches:** file_cluster_3: 8.017, file_cluster_8: 25.0, file_cluster_6: 37.835
- **Magnitude:** 26766.72 | **LOC:** 7289 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **35**; blast radius 0.138; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 1130`, `dead_code: 10`
* *Architecture:* `io: 4`, `api: 13`, `import: 43`
* *Defense:* `safety: 964`, `doc: 2`, `immutability_locks: 315`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.000563
  * `Imports (Out-Degree: 30):` module_cpl, module_irrigation, module_model_constants, module_ra_gfdleta, module_sf_clm, module_sf_ctsm, module_sf_fogdes, module_sf_gfs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_mp_full_sbm.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.124)
- **Top Global Matches:** file_cluster_8: 6.124, file_cluster_6: 15.804, file_cluster_3: 21.374
- **Magnitude:** 20352.18 | **LOC:** 13487 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **1**; blast radius 1.123; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SBM` **(Many-Argument Workhorses)** (Impact: 3179.0)
  * `MELTING` **(Many-Argument Workhorses)** (Impact: 1079.9)
  * `ONECOND3` **(Many-Argument Workhorses)** (Impact: 746.0)
  * `ONECOND2` **(Many-Argument Workhorses)** (Impact: 369.5)
  * `SHEDDING` **(Many-Argument Workhorses)** (Impact: 343.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 32 instances
* *Amplified Cascading Flux:* 3098 instances
* *High Risk Execution (weighted view):* 80
* *Concurrency (weighted view):* 249
* *State Mutation (weighted view):* 10494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1731`, `structural_boundaries: 778`, `args: 188`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 86`, `state_mutation: 4298`, `dead_code: 89`, `fragile_debt: 1`
* *Architecture:* `io: 118`, `api: 78`, `concurrency: 89`, `import: 1`
* *Defense:* `safety: 150`, `sync_locks: 3`, `immutability_locks: 86`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.123
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.003519
  * `Imports (Out-Degree: 1):` module_mp_radar
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `phys/module_radiation_driver.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.709)
- **Top Global Matches:** file_cluster_3: 9.709, file_cluster_8: 29.722, file_cluster_1: 41.148
- **Magnitude:** 17751.76 | **LOC:** 5711 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **25**; blast radius 0.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (72.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 1479`, `dead_code: 24`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `api: 22`, `concurrency: 8`, `import: 35`
* *Defense:* `safety: 376`, `doc: 4`, `immutability_locks: 181`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.236
  * `Choke Point (Betweenness):` 0.000187 | `Ripple Effect (Closeness):` 0.004883
  * `Imports (Out-Degree: 23):` module_bc, module_comm_dm, module_dm, module_domain, module_model_constants, module_mp_thompson, module_ra_aerosol, module_ra_cam...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `chem/module_isofwd.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.288)
- **Top Global Matches:** file_cluster_8: 8.288, file_cluster_6: 13.696, file_cluster_4: 21.965
- **Magnitude:** 17320.94 | **LOC:** 18724 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.187; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ISRP4F2p1` **(Many-Argument Workhorses)** (Impact: 216.4)
  * `ISRP3F2p1` **(Many-Argument Workhorses)** (Impact: 110.8)
  * `FUNCP52p1` **(I/O & Config Routines)** (Impact: 63.1)
  * `FUNCP42p1` **(I/O & Config Routines)** (Impact: 63.1)
  * `FUNCP32p1` **(I/O & Config Routines)** (Impact: 63.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3616 instances
* *State Mutation (weighted view):* 13413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2049`, `structural_boundaries: 408`, `args: 164`, `func_start: 164`
* *Risk/State:* `safety_bypasses: 110`, `state_mutation: 6181`, `unreferenced_by_name: 4`
* *Architecture:* `api: 105`, `import: 164`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000282
  * `Imports (Out-Degree: 1):` module_isrpia_inc.F
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dyn_em/module_diffusion_em.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 24.329)
- **Top Global Matches:** file_cluster_1: 24.329, file_cluster_3: 24.924, file_cluster_8: 46.473
- **Magnitude:** 17273.82 | **LOC:** 8483 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 2074`, `dead_code: 3`, `fragile_debt: 4`
* *Architecture:* `api: 38`, `import: 4`
* *Defense:* `safety: 439`, `immutability_locks: 301`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000901
  * `Imports (Out-Degree: 3):` module_bc, module_big_step_utilities_em, module_model_constants, module_state_description
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `phys/module_ra_gfdleta.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.96)
- **Top Global Matches:** file_cluster_3: 7.96, file_cluster_8: 27.208, file_cluster_6: 40.183
- **Magnitude:** 17070.7 | **LOC:** 10164 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 0.199; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SWR93` **(Many-Argument Workhorses)** (Impact: 1885.4)
  * `FST88` **(Many-Argument Workhorses)** (Impact: 1479.2)
  * `SPA88` **(Many-Argument Workhorses)** (Impact: 1146.5)
  * `RADTN` **(Many-Argument Workhorses)** (Impact: 1054.2)
  * `LWR88` **(Many-Argument Workhorses)** (Impact: 503.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 94 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 2641 instances
* *Concurrency (weighted view):* 117
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 8118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1300`, `structural_boundaries: 1030`, `args: 245`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 4`, `state_mutation: 2836`, `dead_code: 26`
* *Architecture:* `io: 61`, `api: 33`, `concurrency: 27`, `import: 3`
* *Defense:* `safety: 794`, `immutability_locks: 655`, `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.199
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.004925
  * `Imports (Out-Degree: 3):` MODULE_CONFIGURE, MODULE_MODEL_CONSTANTS, MODULE_MP_ETANEW
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `chem/module_mosaic_therm.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.114)
- **Top Global Matches:** file_cluster_6: 8.114, file_cluster_8: 13.586, file_cluster_4: 13.699
- **Magnitude:** 15766.12 | **LOC:** 17136 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.145; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.6%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `map_mosaic_species` **(Many-Argument Workhorses)** (Impact: 1416.0)
  * `equilibrium` **(Many-Argument Workhorses)** (Impact: 156.4)
  * `ions_to_electrolytes` **(Many-Argument Workhorses)** (Impact: 129.9)
  * `load_kappa_nonelectro` **(Compute Cores)** (Impact: 112.5)
  * `ASTEM_flux_mix` **(Compute Cores)** (Impact: 77.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2301 instances
* *State Mutation (weighted view):* 11783
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1679`, `structural_boundaries: 737`, `args: 253`, `func_start: 123`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 7181`, `dead_code: 47`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 61`, `api: 106`, `import: 32`
* *Defense:* `safety: 31`, `doc: 6`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001363
  * `Imports (Out-Degree: 6):` module_data_mosaic_asect, module_data_mosaic_other, module_data_mosaic_therm, module_mosaic_gly, module_mosaic_movesect, module_peg_util, module_state_description
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_mp_ntu.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.638)
- **Top Global Matches:** file_cluster_8: 6.638, file_cluster_6: 14.939, file_cluster_3: 22.796
- **Magnitude:** 15599.6 | **LOC:** 6907 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 0.363; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Complexity Load (formerly Cognitive Load) (90.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 3547`, `dead_code: 1`
* *Architecture:* `api: 32`, `import: 1`
* *Defense:* `safety: 222`, `immutability_locks: 184`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.363
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001893
  * `Imports (Out-Degree: 2):` module_wrf_error
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `phys/module_mp_fast_sbm.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.833)
- **Top Global Matches:** file_cluster_3: 6.833, file_cluster_8: 24.027, file_cluster_6: 36.935
- **Magnitude:** 14280.94 | **LOC:** 9054 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.136; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FAST_SBM` **(Many-Argument Workhorses)** (Impact: 2439.3)
  * `ONECOND2` **(Many-Argument Workhorses)** (Impact: 384.5)
  * `COAL_BOTT_NEW` **(Many-Argument Workhorses)** (Impact: 366.8)
  * `ONECOND3` **(Many-Argument Workhorses)** (Impact: 363.1)
  * `FAST_HUCMINIT` **(Many-Argument Workhorses)** (Impact: 302.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 17 instances
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 2188 instances
* *High Risk Execution (weighted view):* 73
* *Concurrency (weighted view):* 159
* *Memory Alloc (weighted view):* 91
* *State Mutation (weighted view):* 7222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1291`, `structural_boundaries: 720`, `args: 261`, `func_start: 45`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 75`, `state_mutation: 2846`, `dead_code: 21`, `planned_debt: 1`
* *Architecture:* `io: 124`, `api: 43`, `concurrency: 39`, `import: 13`
* *Defense:* `safety: 413`, `doc: 1`, `immutability_locks: 199`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000985
  * `Imports (Out-Degree: 3):` module_dm, module_domain, module_mp_SBM_Auxiliary, module_mp_SBM_BreakUp, module_mp_SBM_Collision, module_mp_SBM_Nucleation, module_mp_SBM_polar_radar, scatt_tables
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_physics_init.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 12.537)
- **Top Global Matches:** file_cluster_3: 12.537, file_cluster_8: 14.255, file_cluster_6: 26.448
- **Magnitude:** 13758.6 | **LOC:** 5751 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **117**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.4%), Guard Balance (formerly Safety Score) (50.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 560`, `dead_code: 21`
* *Architecture:* `io: 37`, `api: 19`, `concurrency: 25`, `import: 126`
* *Defense:* `safety: 699`, `immutability_locks: 246`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.000375
  * `Imports (Out-Degree: 106):` MODULE_CU_BMJ, constituents, microphy_p3, modal_aero_data, modal_aero_initialize_data_phys, module_bl_acm, module_bl_boulac, module_bl_camuwpbl_driver...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_lwf.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.051)
- **Top Global Matches:** file_cluster_6: 8.051, file_cluster_4: 10.904, file_cluster_8: 16.649
- **Magnitude:** 13692.38 | **LOC:** 18237 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **39**; blast radius 0.171; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RRTMG_LWRAD_FAST` **(Many-Argument Workhorses)** (Impact: 1939.1)
  * `deallocateGPUrtrnmcg` **(Many-Argument Workhorses)** (Impact: 704.9)
  * `mcica_subcol_lwg` **(Many-Argument Workhorses)** (Impact: 425.3)
  * `copyGPUcldprmcg` **(Many-Argument Workhorses)** (Impact: 209.6)
  * `rrtmg_lw_part` **(Many-Argument Workhorses)** (Impact: 165.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 53 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2582 instances
* *High Risk Execution (weighted view):* 18
* *Concurrency (weighted view):* 76
* *Memory Alloc (weighted view):* 52
* *State Mutation (weighted view):* 8612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1190`, `structural_boundaries: 2109`, `args: 607`, `func_start: 136`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 22`, `state_mutation: 3448`, `dead_code: 39`
* *Architecture:* `io: 49`, `api: 139`, `concurrency: 56`, `import: 256`
* *Defense:* `safety: 633`, `immutability_locks: 330`, `cleanup: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.171
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004261
  * `Imports (Out-Degree: 3):` MODULE_RA_CLWRF_SUPPORT, MersenneTwister_f, cudadevice, cudafor, gpu_mcica_subcol_gen_lw, gpu_rrtmg_lw_cldprmc, gpu_rrtmg_lw_rtrnmc, gpu_rrtmg_lw_setcoef...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `phys/module_cu_mskf.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.312)
- **Top Global Matches:** file_cluster_8: 6.312, file_cluster_6: 14.776, file_cluster_3: 22.759
- **Magnitude:** 13638.28 | **LOC:** 8042 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.138; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.3%), Complexity Load (formerly Cognitive Load) (87.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MSKF_eta_PARA` **(Many-Argument Workhorses)** (Impact: 3236.2)
  * `mskf_mphy` **(Many-Argument Workhorses)** (Impact: 1685.6)
  * `MSKF_CPS` **(Many-Argument Workhorses)** (Impact: 792.0)
  * `MSKF_CMT` **(Many-Argument Workhorses)** (Impact: 681.3)
  * `mskf_nucleati` **(Many-Argument Workhorses)** (Impact: 122.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 1936 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 6572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 858`, `structural_boundaries: 709`, `args: 140`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 2700`, `dead_code: 20`
* *Architecture:* `io: 46`, `api: 22`, `import: 5`
* *Defense:* `safety: 144`, `doc: 9`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000948
  * `Imports (Out-Degree: 2):` error_function, module_cu_mp, module_wrf_error, shr_kind_mod
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_lw.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.38)
- **Top Global Matches:** file_cluster_8: 10.38, file_cluster_3: 16.662, file_cluster_6: 21.655
- **Magnitude:** 13380.26 | **LOC:** 14634 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **37**; blast radius 0.165; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RRTMG_LWRAD` **(Many-Argument Workhorses)** (Impact: 2245.0)
  * `generate_stochastic_clouds` **(Many-Argument Workhorses)** (Impact: 344.3)
  * `setcoef` **(Many-Argument Workhorses)** (Impact: 256.3)
  * `rtrnmc` **(Many-Argument Workhorses)** (Impact: 190.0)
  * `inatm` **(Many-Argument Workhorses)** (Impact: 147.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2561 instances
* *High Risk Execution (weighted view):* 21
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 8339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1086`, `structural_boundaries: 1501`, `args: 513`, `func_start: 85`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 24`, `state_mutation: 3217`, `dead_code: 30`, `planned_debt: 2`
* *Architecture:* `io: 44`, `api: 90`, `concurrency: 56`, `import: 177`
* *Defense:* `safety: 558`, `immutability_locks: 331`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004261
  * `Imports (Out-Degree: 3):` MODULE_RA_CLWRF_SUPPORT, MersenneTwister, mcica_random_numbers, mcica_subcol_gen_lw, module_model_constants, module_state_description, module_wrf_error, parkind...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `var/obsproc/MAP_plot/Dir_map/plots.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.703)
- **Top Global Matches:** file_cluster_3: 6.703, file_cluster_8: 23.975, file_cluster_6: 36.88
- **Magnitude:** 13134.6 | **LOC:** 14120 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mrddet` **(Many-Argument Workhorses)** (Impact: 730.4)
  * `crddet` **(Many-Argument Workhorses)** (Impact: 611.5)
  * `crdclt` **(Many-Argument Workhorses)** (Impact: 577.8)
  * `mpdrml` **(Many-Argument Workhorses)** (Impact: 446.6)
  * `crdprt` **(Many-Argument Workhorses)** (Impact: 352.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2058 instances
* *State Mutation (weighted view):* 6420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2455`, `structural_boundaries: 619`, `args: 84`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 159`, `high_risk_execution: 1`, `state_mutation: 2304`, `dead_code: 4`, `fragile_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `io: 164`, `api: 62`
* *Defense:* `safety: 38`, `doc: 2`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001005
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `dyn_em/module_initialize_real.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.699)
- **Top Global Matches:** file_cluster_8: 6.699, file_cluster_6: 14.109, file_cluster_4: 22.625
- **Magnitude:** 12927.98 | **LOC:** 9207 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **16**; blast radius 0.205; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.2%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init_domain_rk` **(Many-Argument Workhorses)** (Impact: 2072.7)
  * `vert_interp` **(Many-Argument Workhorses)** (Impact: 1513.4)
  * `sfcprs` **(Many-Argument Workhorses)** (Impact: 576.2)
  * `compute_eta` **(Many-Argument Workhorses)** (Impact: 313.7)
    * *Intent:* #endif
  * `integ_moist` **(Many-Argument Workhorses)** (Impact: 279.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 1879 instances
* *Concurrency (weighted view):* 43
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 5979
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2120`, `structural_boundaries: 610`, `args: 219`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2221`, `dead_code: 16`
* *Architecture:* `io: 63`, `api: 41`, `concurrency: 8`, `import: 42`
* *Defense:* `safety: 256`, `doc: 2`, `immutability_locks: 176`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.000173 | `Ripple Effect (Closeness):` 0.004331
  * `Imports (Out-Degree: 16):` module_bc, module_comm_dm, module_configure, module_date_time, module_dm, module_domain, module_io_domain, module_llxy...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `chem/module_isrpia.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.312)
- **Top Global Matches:** file_cluster_8: 8.312, file_cluster_6: 10.409, file_cluster_4: 18.524
- **Magnitude:** 12819.66 | **LOC:** 14988 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ISRP3R` **(Many-Argument Workhorses)** (Impact: 124.5)
  * `ISRP3F` **(Many-Argument Workhorses)** (Impact: 110.7)
  * `CALCR1` **(I/O & Config Routines)** (Impact: 86.8)
  * `ISOROPIA` **(Many-Argument Workhorses)** (Impact: 78.5)
  * `ADJUST` **(Compute Cores)** (Impact: 67.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2677 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 9516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1561`, `structural_boundaries: 949`, `args: 310`, `func_start: 155`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 4162`, `dead_code: 65`, `unreferenced_by_name: 14`
* *Architecture:* `io: 36`, `api: 129`, `import: 1`
* *Defense:* `safety: 160`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` module_data_isrpia
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phys/module_sf_noahdrv.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 7.107)
- **Top Global Matches:** file_cluster_1: 7.107, file_cluster_3: 48.399, file_cluster_8: 70.171
- **Magnitude:** 12803.28 | **LOC:** 5355 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.136; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (71.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 1230`, `dead_code: 23`
* *Architecture:* `io: 97`, `api: 5`, `concurrency: 72`, `import: 11`
* *Defense:* `safety: 412`, `doc: 1`, `immutability_locks: 159`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000948
  * `Imports (Out-Degree: 8):` module_data_gocart_dust, module_ra_gfdleta, module_sf_bep, module_sf_bep_bem, module_sf_noahlsm, module_sf_noahlsm_glacial_only, module_sf_urban, module_wrf_error...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `dyn_em/module_big_step_utilities_em.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.214)
- **Top Global Matches:** file_cluster_3: 6.214, file_cluster_8: 23.985, file_cluster_6: 36.959
- **Magnitude:** 12747.78 | **LOC:** 6759 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **5**; blast radius 0.62; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 1583`, `dead_code: 15`, `fragile_debt: 3`
* *Architecture:* `io: 7`, `api: 43`, `import: 5`
* *Defense:* `safety: 336`, `doc: 72`, `immutability_locks: 232`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.62
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.006531
  * `Imports (Out-Degree: 5):` module_configure, module_llxy, module_model_constants, module_state_description, module_wrf_error
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `chem/module_isorev.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.683)
- **Top Global Matches:** file_cluster_3: 8.683, file_cluster_8: 28.506, file_cluster_6: 41.512
- **Magnitude:** 12734.02 | **LOC:** 11875 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ISRP4R2p1` **(Many-Argument Workhorses)** (Impact: 213.1)
  * `ISRP3R2p1` **(Many-Argument Workhorses)** (Impact: 124.5)
  * `CALCU12p1` **(I/O & Config Routines)** (Impact: 87.5)
  * `CALCR12p1` **(I/O & Config Routines)** (Impact: 86.8)
  * `ISRP2R2p1` **(Many-Argument Workhorses)** (Impact: 65.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2750 instances
* *State Mutation (weighted view):* 10349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1366`, `structural_boundaries: 228`, `args: 69`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 4849`, `unreferenced_by_name: 4`
* *Architecture:* `api: 68`, `import: 69`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` module_isrpia_inc.F
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `chem/chemics_init.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.061)
- **Top Global Matches:** file_cluster_3: 8.061, file_cluster_8: 21.3, file_cluster_6: 34.018
- **Magnitude:** 12492.2 | **LOC:** 3538 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **33**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chem_init` **(Many-Argument Workhorses)** (Impact: 11599.5)
  * `print_chem_species_index` **(I/O & Config Routines)** (Impact: 52.3)
    * *Intent:* #ifdef CHEM_DBG_I
  * `termite_initialize` **(Defensive Guards)** (Impact: 13.7)
  * `VPRM_par_initialize` **(Many-Argument Workhorses)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *State Mutation (weighted view):* 752
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1075`, `structural_boundaries: 93`, `args: 33`, `func_start: 4`
* *Risk/State:* `state_mutation: 326`, `dead_code: 15`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 4`, `import: 38`
* *Defense:* `safety: 31`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000375
  * `Imports (Out-Degree: 32):` module_HLawConst, module_aerosols_soa_vbs, module_aerosols_soa_vbs_het, module_aerosols_sorgam, module_aerosols_sorgam_vbs, module_cam_mam_init, module_cam_mam_initmixrats, module_cam_mam_wetscav...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phys/module_ra_rrtmg_swf.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.994)
- **Top Global Matches:** file_cluster_3: 8.994, file_cluster_8: 17.782, file_cluster_6: 30.376
- **Magnitude:** 12455.48 | **LOC:** 13799 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **35**; blast radius 0.141; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%), Complexity Load (formerly Cognitive Load) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RRTMG_SWRAD_FAST` **(Many-Argument Workhorses)** (Impact: 2421.2)
  * `rrtmg_sw_sub` **(Many-Argument Workhorses)** (Impact: 632.2)
  * `spcvmc_sw` **(Many-Argument Workhorses)** (Impact: 386.6)
  * `cldprmc_sw` **(Many-Argument Workhorses)** (Impact: 305.0)
  * `mcica_sw` **(Many-Argument Workhorses)** (Impact: 198.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1697 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 89
* *State Mutation (weighted view):* 5758
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 978`, `structural_boundaries: 1642`, `args: 813`, `func_start: 62`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 15`, `state_mutation: 2364`, `dead_code: 34`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 60`, `api: 64`, `concurrency: 74`, `import: 163`
* *Defense:* `safety: 861`, `doc: 1`, `immutability_locks: 598`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004163
  * `Imports (Out-Degree: 4):` MODULE_RA_CLWRF_SUPPORT, cudafor, mcica_random_numbers_f, mcica_subcol_gen_sw_f, module_model_constants, module_ra_rrtmg_lwf, module_wrf_error, parrrsw_f...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `phys/module_cu_sas.F` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.981)
- **Top Global Matches:** file_cluster_3: 9.981, file_cluster_8: 30.492, file_cluster_1: 40.133
- **Magnitude:** 12240.58 | **LOC:** 5606 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **6**; blast radius 0.266; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sascnvn` **(Many-Argument Workhorses)** (Impact: 2273.1)
  * `SASCNV` **(Many-Argument Workhorses)** (Impact: 1995.8)
  * `shalcnv` **(Many-Argument Workhorses)** (Impact: 1416.8)
  * `CU_SAS` **(Many-Argument Workhorses)** (Impact: 474.0)
  * `OLD_ARW_SHALCV` **(Many-Argument Workhorses)** (Impact: 135.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1746 instances
* *State Mutation (weighted view):* 5653
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1182`, `structural_boundaries: 177`, `args: 49`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 2161`, `dead_code: 24`
* *Architecture:* `io: 3`, `api: 10`, `import: 18`
* *Defense:* `safety: 64`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001903
  * `Imports (Out-Degree: 3):` MODULE_GFS_FUNCPHYS, MODULE_GFS_MACHINE, MODULE_GFS_PHYSCONS, MODULE_GFS_funcphys, MODULE_GFS_machine, MODULE_GFS_physcons
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `hydro/IO/netcdf_layer.F90` (FORTRAN) | Magnitude: 24.68 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 45, args: 30, safety: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `frame/module_nesting.F` (FORTRAN) | Magnitude: 64.82 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 23, state_mutation: 13, core_var_decl: 12
- `chem/KPP/kpp/kpp-2.1/util/util.c` (C) | Magnitude: 0.04 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 31, debug_prints: 11, branch: 6, structural_boundaries: 6
- `share/module_get_file_names.F` (FORTRAN) | Magnitude: 92.1 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 27, core_var_decl: 24, state_mutation: 14
- `frame/module_driver_constants.F` (FORTRAN) | Magnitude: 18.34 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 52, indent_spaces: 50, safety: 42, core_var_decl: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `external/io_grib1/test_write_grib.c` (C) | Magnitude: 0.05 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 54, pointers: 27, state_mutation: 24, core_var_decl: 19
- `var/external/bufr/lcmgdf.f` (FORTRAN) | Magnitude: 0.03 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 6, branch: 4, state_mutation: 4
- `tools/gen_scalar_derefs.c` (C) | Magnitude: 0.06 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 56, branch: 17, pointers: 14, structural_boundaries: 9
- `external/io_grib2/g2lib/enc_png.c` (C) | Magnitude: 0.09 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 60, pointers: 25, state_mutation: 20, core_var_decl: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `var/obsproc/MAP_plot/Map.csh` (SHELL) | Magnitude: 15.96 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: branch: 8, io: 8, core_var_decl: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `var/convertor/kma_wave2grid/WAVMAG.inc` (FORTRAN) | Magnitude: 22.26 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, io: 5, state_mutation: 5, structural_boundaries: 3
- `var/external/bufr/cmsgini.f` (FORTRAN) | Magnitude: 0.05 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 15, design_upper_case: 15, state_mutation: 13
- `var/da/da_radar/da_radzicevar_rain_adj.inc` (FORTRAN) | Magnitude: 11.62 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, state_mutation: 5, core_var_decl: 5
- `var/da/da_radar/da_radzicevar_parameter_zrx.inc` (FORTRAN) | Magnitude: 11.96 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 6, core_var_decl: 6, design_snake_case: 6
- `var/external/wavelet/l2norm.c` (C) | Magnitude: 0.03 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 8, core_var_decl: 5, design_snake_case: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `hydro/Routing/Subsurface/module_subsurface_input.F90` (FORTRAN) | Magnitude: 6.94 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 16, args: 8, safety: 7
- `hydro/Routing/Subsurface/module_subsurface_output.F90` (FORTRAN) | Magnitude: 6.94 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 16, args: 8, safety: 7
- `var/da/da_minimisation/da_sensitivity.inc` (FORTRAN) | Magnitude: 42.38 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 42, args: 16, structural_boundaries: 15, safety: 15
- `var/da/da_transfer_model/da_get_2nd_firstguess.inc` (FORTRAN) | Magnitude: 9.48 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 9, explicit_casts: 6, macros: 5
- `var/da/da_radiance/da_crtm_k.inc` (FORTRAN) | Magnitude: 21.38 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, args: 12, safety: 10, immutability_locks: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `chem/KPP/kpp/kpp-2.1/util/dJac_dRcoeff.m` (MATLAB) | Magnitude: 0.03 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, core_var_decl: 8, state_mutation: 6, design_snake_case: 6
- `var/external/bufr/readmm.f` (FORTRAN) | Magnitude: 0.01 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 2, args: 1, func_start: 1
- `var/obsproc/MAP_plot/Dir_map/DA_Setup_Obs_Structures.inc` (FORTRAN) | Magnitude: 5.76 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, core_var_decl: 3, args: 2
- `var/external/bufr/cadn30.f` (FORTRAN) | Magnitude: 0.01 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 3, args: 1, func_start: 1
- `var/da/da_radar/da_radzicevar_rain_tl.inc` (FORTRAN) | Magnitude: 7.84 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, args: 2, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `var/external/bufr/setblock.f` (FORTRAN) | Magnitude: 0.01 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 1, args: 1, func_start: 1
- `var/external/bufr/openmg.f` (FORTRAN) | Magnitude: 0.02 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, branch: 3, io: 3, structural_boundaries: 2
- `var/external/bufr/wrtree.f` (FORTRAN) | Magnitude: 0.07 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 57, branch: 14, state_mutation: 13, core_var_decl: 9
- `var/external/bufr/pkc.f` (FORTRAN) | Magnitude: 0.07 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 17, bitwise_ops: 12, core_var_decl: 12
- `var/external/bufr/nxtwin.f` (FORTRAN) | Magnitude: 0.03 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 5, core_var_decl: 5, design_upper_case: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dyn_em/module_em.F` (FORTRAN) | Magnitude: 4326.5 | Delta: **0.247** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_spaces: 2233, state_mutation: 472, core_var_decl: 381, branch: 355

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `external/atm_ocn/atm_comm_pom.F` (FORTRAN) | Magnitude: 0.48 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 373, structural_boundaries: 107, core_var_decl: 77, state_mutation: 66
- `var/external/bufr/gettagpr.f` (FORTRAN) | Magnitude: 0.04 | Delta: **0.231** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 9, state_mutation: 7, core_var_decl: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `phys/module_diag_functions.F` -> Churn: **100.0%** | Cog Load: 89.5041% | Debt: 74.3889%
- `share/wrf_timeseries.F` -> Churn: **100.0%** | Cog Load: 99.6857% | Debt: 9.2205%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `share/wrf_timeseries.F` -> **Massimo D'isidoro** (100.0% isolated ownership) | Magnitude: 1465.28
- `phys/module_diag_functions.F` -> **Yuxuan Xie** (100.0% isolated ownership) | Magnitude: 1023.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `external/RSL_LITE/module_dm.F` -> **Severity: 0.291** (Bridge: 0.0029 * Flux: 100.0%)
- `phys/module_fr_fire_util.F` -> **Severity: 0.209** (Bridge: 0.0021 * Flux: 100.0%)
- `frame/module_io.F` -> **Severity: 0.193** (Bridge: 0.0019 * Flux: 99.3372%)
- `external/io_grib2/io_grib2.F` -> **Severity: 0.162** (Bridge: 0.0016 * Flux: 99.9999%)
- `frame/module_domain.F` -> **Severity: 0.091** (Bridge: 0.0009 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `var/da/da_tracing/da_trace_entry.inc` -> **Severity: 19.429** (Embedded: 0.2702 * Error Risk: 71.9196%)
- `var/da/da_tracing/da_trace_exit.inc` -> **Severity: 17.453** (Embedded: 0.2704 * Error Risk: 64.5365%)
- `var/da/da_reporting/da_error.inc` -> **Severity: 7.955** (Embedded: 0.1569 * Error Risk: 50.7142%)
- `frame/module_wrf_error.F` -> **Severity: 7.877** (Embedded: 0.1588 * Error Risk: 49.6079%)
- `external/RSL_LITE/module_dm.F` -> **Severity: 4.789** (Embedded: 0.064 * Error Risk: 74.7835%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frame/module_wrf_error.F` -> **Severity: 8656.2** (Blast Radius: 86.562 * Doc Risk: 100.0%)
- `var/da/da_reporting/da_error.inc` -> **Severity: 8243.2** (Blast Radius: 82.432 * Doc Risk: 100.0%)
- `var/da/da_tracing/da_trace_exit.inc` -> **Severity: 4454.7** (Blast Radius: 44.547 * Doc Risk: 100.0%)
- `var/da/da_tracing/da_trace_entry.inc` -> **Severity: 4451.1** (Blast Radius: 44.511 * Doc Risk: 100.0%)
- `var/external/bufr/errwrt.f` -> **Severity: 1238.4** (Blast Radius: 12.384 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 13806 literal sites + 247 sites through wrappers = 14053
- **`memory_alloc`:** 14150 literal sites + 183 sites through wrappers = 14333
- **`panics_and_aborts`:** 10351 literal sites + 734 sites through wrappers = 11085

- `wrf_at_debug_level` (function, panics_and_aborts, primitive): 142 call sites in 5 files -- `frame/module_wrf_error.F`
- `wrf_error_fatal` (function, debug_prints, primitive): 74 call sites in 1 files -- `dyn_em/module_initialize_real.F`
- `wrf_error_fatal` (function, panics_and_aborts, primitive): 74 call sites in 1 files -- `dyn_em/module_initialize_real.F`
- `close_the_file` (function, debug_prints, primitive): 66 call sites in 13 files -- `tools/misc.c`
- `arr` (function, panics_and_aborts, primitive): 64 call sites in 1 files -- `chem/module_cbmz.F`
- `wrf_message` (function, debug_prints, primitive): 49 call sites in 1 files -- `dyn_em/module_initialize_real.F`
- `fatal_error` (function, panics_and_aborts, primitive): 46 call sites in 8 files -- `tools/manage_externals/manic/utils.py`
- `G2LIB_GBYTE` (function, panics_and_aborts, primitive): 44 call sites in 6 files -- `external/io_grib2/g2lib/gbytesc.F`
- `domain_clockprint` (function, panics_and_aborts, primitive): 40 call sites in 13 files -- `frame/module_domain.F`
- `INTGRL` (function, panics_and_aborts, primitive): 37 call sites in 1 files -- `phys/module_sf_gecros.F`
- `get_wrf_debug_level` (function, panics_and_aborts, primitive): 33 call sites in 17 files -- `frame/wrf_debug.F`
- `system` (function, panics_and_aborts, primitive): 29 call sites in 17 files -- `share/module_get_file_names.F`
*(+79 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 52573 call pairs -- scoped 23.9%, unique 18.5%, ambiguous 8.0%, external 49.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| fortran | 43774 | 26.1% | 20.7% | 6.0% | 47.2% |
| c | 6522 | 13.8% | 9.7% | 22.3% | 54.2% |
| shell | 1382 | 0.1% | 0.0% | 0.0% | 99.9% |
| python | 606 | 36.6% | 0.0% | 2.0% | 61.4% |
| yacc | 145 | 0.0% | 22.8% | 66.2% | 11.0% |
| matlab | 94 | 0.0% | 0.0% | 0.0% | 100.0% |
| m4 | 50 | 2.0% | 0.0% | 0.0% | 98.0% |

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
