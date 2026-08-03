# ARCHITECTURAL_BRIEF: blast
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/blast` |
| **Timestamp** | `2026-08-03T19:24:43.928441+00:00` |
| **Scan Duration** | `5.54s` |
| **Git Branch** | `main` |
| **Git Commit** | `0046959f6c628416d0fbb4f8f53b224c8244ace7` |
| **Git Remote** | `https://github.com/ncbi/ncbi-cxx-toolkit-public.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 582 malicious artifacts.

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
| Total Artifacts | 10406 |
| Analyzed Artifacts (Scanned) | 770 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9636 |
| Total LOC | 110803 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 7.4% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7333 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0698 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2801 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 48 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 310 | 71644 | 40.3% |
| PLAINTEXT | 180 | 1 | 23.4% |
| MAKEFILE | 170 | 1383 | 22.1% |
| C | 88 | 35478 | 11.4% |
| BINARY_THREAT | 8 | 8 | 1.0% |
| MARKDOWN | 5 | 0 | 0.6% |
| SHELL | 4 | 119 | 0.5% |
| PERL | 2 | 2062 | 0.3% |
| BATCH | 1 | 8 | 0.1% |
| XML | 1 | 0 | 0.1% |
| PYTHON | 1 | 100 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.732`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 429 | 55.7% |
| file_cluster_13 | 109 | 14.2% |
| file_cluster_9 | 16 | 2.1% |
| Unknown | 9 | 1.2% |
| file_cluster_7 | 9 | 1.2% |
| file_cluster_0 | 6 | 0.8% |
| file_cluster_17 | 2 | 0.3% |
| file_cluster_11 | 2 | 0.3% |
| file_cluster_16 | 2 | 0.3% |
| file_cluster_12 | 1 | 0.1% |
| file_cluster_6 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 184 | 23.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9636*

**Composition by Extension & Reason:**
- `.cpp`: 1554x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.hpp`: 1134x Excluded: Neighborhood Micro-Mass Limit Exceeded, 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 771x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 10152 commas in 2340 LOC)
- `.gz`: 752x Excluded (Explicitly Denied Extension: '.gz')
- `.app`: 659x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.asn`: 546x Excluded: Neighborhood Micro-Mass Limit Exceeded, 29x Unsupported Format (.asn)
- `.txt`: 490x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 385x Excluded: Neighborhood Micro-Mass Limit Exceeded, 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.errors`: 363x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 248x Excluded: Neighborhood Micro-Mass Limit Exceeded, 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.lib`: 283x Excluded (Explicitly Denied Extension: '.lib'), 1x Excluded (Explicitly Denied Extension: '.LIB')
- `.aln`: 173x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Monolithic Amalgamation: 38170 LOC exceeds safe regex boundaries), 1x Unsupported Format (.aln)
- `.msvc`: 163x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Unsupported Extension: '.msvc'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sql`: 104x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.ini`: 51x Excluded: Neighborhood Micro-Mass Limit Exceeded, 35x Unsupported Format (.ini)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 29.0 | 15.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 30.9 | 12.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 39.1 | 16.9 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.2 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.4 | 2.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 97.6 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 54.0 | 96.3 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 77.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.9 | 33.3 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 45.0 | 1.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.8 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/app/blast/get_species_taxids.sh` (Hits: 65)
- `src/app/blast/cleanup-blastdb-volumes.py` (Hits: 29)
- `src/app/blast/legacy_blast.pl` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **test_objmgr.hpp** (`src/algo/blast/unit_tests/api/test_objmgr.hpp`) — 40 inbound connections
2. **blast_setup.hpp** (`src/algo/blast/api/blast_setup.hpp`) — 33 inbound connections
3. **blast_objmgr_priv.hpp** (`src/algo/blast/api/blast_objmgr_priv.hpp`) — 31 inbound connections
4. **blast_test_util.hpp** (`src/algo/blast/unit_tests/api/blast_test_util.hpp`) — 19 inbound connections
5. **blast_app_util.hpp** (`src/app/blast/blast_app_util.hpp`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **traceback_unit_test.cpp** (`src/algo/blast/unit_tests/api/traceback_unit_test.cpp`) — 44 outbound dependencies
2. **rmblast_traceback_unit_test.cpp** (`src/algo/blast/unit_tests/api/rmblast_traceback_unit_test.cpp`) — 40 outbound dependencies
3. **pssmcreate_unit_test.cpp** (`src/algo/blast/unit_tests/api/pssmcreate_unit_test.cpp`) — 37 outbound dependencies
4. **blastengine_unit_test.cpp** (`src/algo/blast/unit_tests/api/blastengine_unit_test.cpp`) — 35 outbound dependencies
5. **blastinput_unit_test.cpp** (`src/algo/blast/blastinput/unit_test/blastinput_unit_test.cpp`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_files_from_json_metadata_1_1` (@ `src/app/blast/update_blastdb.pl`) -> Impact: **3677.8** | LOC: 810
- `handle_blastall` (@ `src/app/blast/legacy_blast.pl`) -> Impact: **2591.6** | LOC: 1153
  * *Intent:* # Handle the conversion from blastall arguments to the corresponding C++ # binaries
- `_PSIMsaNew` (@ `src/algo/blast/core/blast_psi_priv.c`) -> Impact: **1942.4** | LOC: 1297
- `s_AdjustEvaluesForComposition` (@ `src/algo/blast/core/blast_kappa.c`) -> Impact: **1773.6** | LOC: 1523
  * *Intent:* */ #include <float.h> #include <algo/blast/core/ncbi_math.h> #include <algo/blast/core/blast_hits.h> #include <algo/blast/core/blast_kappa.h> #include...
- `s_SetAdapter` (@ `src/algo/blast/core/hspfilter_mapper.c`) -> Impact: **1107.7** | LOC: 937
- `Blast_ApplyPseudocounts` (@ `src/algo/blast/composition_adjustment/composition_adjustment.c`) -> Impact: **1058.4** | LOC: 820
  * *Intent:* * Highest level functions to solve the optimization problem for * compositional score matrix adjustment. * * @author Yi-Kuo Yu, Alejandro Schaffer, E....
- `CRemoteBlast::x_GetRequestInfoFromFile` (@ `src/algo/blast/api/remote_blast.cpp`) -> Impact: **903.7** | LOC: 714
- `BlastKarlinLHtoK` (@ `src/algo/blast/core/blast_stat.c`) -> Impact: **836.0** | LOC: 484
- `s_QueryEndCompareHSPs` (@ `src/algo/blast/core/blast_hits.c`) -> Impact: **772.7** | LOC: 783
- `alp_sim::calculate_main_parameters2m` (@ `src/algo/blast/gumbel_params/sls_alp_sim.cpp`) -> Impact: **668.6** | LOC: 753

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Blast_FindDustFilterLoc` (@ `src/algo/blast/api/dust_filter.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* * Government have not placed any restriction on its use or reproduction. * * Although all reasonable efforts have been taken to ensure the accuracy * ...
- `Blast_FindRepeatFilterLoc` (@ `src/algo/blast/api/repeats_filter_cxx.cpp`) -> **O(2^N) [Recursive]**
- `s_SeqDbGetNextChunk` (@ `src/algo/blast/api/seqsrc_seqdb.cpp`) -> **O(2^N) [Recursive]**
- `Blast_FindWindowMaskerLoc_Fwd` (@ `src/algo/blast/api/winmask_filter.cpp`) -> **O(2^N) [Recursive]**
- `AssignMolType` (@ `src/algo/blast/blastinput/blast_fasta_input.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* /* $Id$ * =========================================================================== * * PUBLIC DOMAIN NOTICE * National Center for Biotechnology Inf...
- `SetArgumentDescriptions` (@ `src/algo/blast/blastinput/magicblast_args.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* * thus cannot be copyrighted. This software/database is freely available * to the public for use. The National Library of Medicine and the U.S. * Gove...
- `newtonRaphson` (@ `src/algo/blast/gumbel_params/njn_root.hpp`) -> **O(2^N) [Recursive]**
- `bisection` (@ `src/algo/blast/gumbel_params/njn_root.hpp`) -> **O(2^N) [Recursive]**
- `alp::degree` (@ `src/algo/blast/gumbel_params/sls_alp.cpp`) -> **O(2^N) [Recursive]**
- `alp` (@ `src/algo/blast/gumbel_params/sls_alp.cpp`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `s_AdjustEvaluesForComposition` (@ `src/algo/blast/core/blast_kappa.c`) -> DB Complexity: **378**
  * *Intent:* */ #include <float.h> #include <algo/blast/core/ncbi_math.h> #include <algo/blast/core/blast_hits.h> #include <algo/blast/core/blast_kappa.h> #include...
- `_PSIMsaNew` (@ `src/algo/blast/core/blast_psi_priv.c`) -> DB Complexity: **378**
- `alp_sim::calculate_main_parameters2m` (@ `src/algo/blast/gumbel_params/sls_alp_sim.cpp`) -> DB Complexity: **281**
- `get_files_from_json_metadata_1_1` (@ `src/app/blast/update_blastdb.pl`) -> DB Complexity: **260**
- `s_SetAdapter` (@ `src/algo/blast/core/hspfilter_mapper.c`) -> DB Complexity: **246**
- `s_QueryEndCompareHSPs` (@ `src/algo/blast/core/blast_hits.c`) -> DB Complexity: **226**
- `ALIGN_EX` (@ `src/algo/blast/core/blast_gapalign.c`) -> DB Complexity: **225**
- `Blast_ApplyPseudocounts` (@ `src/algo/blast/composition_adjustment/composition_adjustment.c`) -> DB Complexity: **216**
  * *Intent:* * Highest level functions to solve the optimization problem for * compositional score matrix adjustment. * * @author Yi-Kuo Yu, Alejandro Schaffer, E....
- `alp_sim::calculate_FSC` (@ `src/algo/blast/gumbel_params/sls_alp_sim.cpp`) -> DB Complexity: **205**
- `handle_blastall` (@ `src/app/blast/legacy_blast.pl`) -> DB Complexity: **202**
  * *Intent:* # Handle the conversion from blastall arguments to the corresponding C++ # binaries

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/algo/blast/core` | 77 | 61605.76 | 36.77% | 37.8% |
| `src/algo/blast/api` | 96 | 21590.38 | 27.64% | 58.44% |
| `src/algo/blast/unit_tests/api` | 219 | 20332.16 | 17.67% | 19.91% |
| `src/algo/blast/gumbel_params` | 44 | 20272.22 | 40.7% | 43.04% |
| `src/app/blast` | 65 | 12400.34 | 21.75% | 15.95% |
| `src/algo/blast/blastinput` | 24 | 9628.32 | 27.88% | 78.91% |
| `src/algo/blast/format` | 13 | 7719.24 | 45.16% | 68.47% |
| `src/algo/blast/composition_adjustment` | 13 | 6083.06 | 30.86% | 26.44% |
| `src/algo/blast/proteinkmer` | 12 | 5173.68 | 40.64% | 51.81% |
| `src/algo/blast/vdb` | 17 | 5064.38 | 25.63% | 34.46% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cmake-configure` -> **100.0%** Exposure
- `configure` -> **100.0%** Exposure
- `src/algo/blast/proteinkmer/demo/deploy.sh` -> **100.0%** Exposure
- `src/algo/blast/api/blast_rps_options.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/local_search.cpp` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cmake-configure` -> **100.0%** Exposure
- `src/algo/blast/proteinkmer/demo/deploy.sh` -> **100.0%** Exposure
- `src/algo/blast/api/bioseq_extract_data_priv.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_node.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_options_builder.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/algo/blast/api/blast_options_cxx.cpp` -> **134** Orphaned Functions | **2** Duplicates
- `src/algo/blast/unit_tests/api/optionshandle_unit_test.cpp` -> **75** Orphaned Functions | **12** Duplicates
- `src/algo/blast/unit_tests/api/blastfilter_unit_test.cpp` -> **67** Orphaned Functions | **0** Duplicates
- `src/algo/blast/blastinput/blast_args.cpp` -> **60** Orphaned Functions | **0** Duplicates
- `src/algo/blast/dbindex/dbindex_factory.cpp` -> **28** Orphaned Functions | **14** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/algo/blast/api/blast_options_handle.cpp`** -> AI Confidence: **99.48%**
2. **`src/algo/blast/api/blast_setup_cxx.cpp`** -> AI Confidence: **99.48%**
3. **`src/algo/blast/api/local_blast.cpp`** -> AI Confidence: **99.48%**
4. **`src/algo/blast/api/local_db_adapter.cpp`** -> AI Confidence: **99.48%**
5. **`src/algo/blast/api/magicblast.cpp`** -> AI Confidence: **99.48%**
6. **`src/algo/blast/api/msa_pssm_input.cpp`** -> AI Confidence: **99.48%**
7. **`src/algo/blast/api/psi_pssm_input.cpp`** -> AI Confidence: **99.48%**
8. **`src/algo/blast/api/pssm_engine.cpp`** -> AI Confidence: **99.48%**
9. **`src/algo/blast/api/setup_factory.cpp`** -> AI Confidence: **99.48%**
10. **`src/algo/blast/api/split_query_cxx.cpp`** -> AI Confidence: **99.48%**
11. **`src/algo/blast/blastinput/blast_args.cpp`** -> AI Confidence: **99.48%**
12. **`src/algo/blast/blastinput/blast_asn1_input.cpp`** -> AI Confidence: **99.48%**
13. **`src/algo/blast/blastinput/blast_fasta_input.cpp`** -> AI Confidence: **99.48%**
14. **`src/algo/blast/blastinput/blast_input_aux.cpp`** -> AI Confidence: **99.48%**
15. **`src/algo/blast/dbindex/makeindex/mkindex_app.cpp`** -> AI Confidence: **99.48%**
16. **`src/algo/blast/format/blast_format.cpp`** -> AI Confidence: **99.48%**
17. **`src/algo/blast/format/blastfmtutil.cpp`** -> AI Confidence: **99.48%**
18. **`src/algo/blast/format/blastxml_format.cpp`** -> AI Confidence: **99.48%**
19. **`src/algo/blast/format/vecscreen_run.cpp`** -> AI Confidence: **99.48%**
20. **`src/algo/blast/gumbel_params/pvalues.cpp`** -> AI Confidence: **99.48%**
21. **`src/algo/blast/igblast/igblast.cpp`** -> AI Confidence: **99.48%**
22. **`src/algo/blast/proteinkmer/blastkmerindex.cpp`** -> AI Confidence: **99.48%**
23. **`src/algo/blast/proteinkmer/blastkmerutils.cpp`** -> AI Confidence: **99.48%**
24. **`src/algo/blast/proteinkmer/kblastapi.cpp`** -> AI Confidence: **99.48%**
25. **`src/algo/blast/proteinkmer/unit_test/proteinkmer_unit_test.cpp`** -> AI Confidence: **99.48%**
26. **`src/algo/blast/unit_tests/api/aalookup_unit_test.cpp`** -> AI Confidence: **99.48%**
27. **`src/algo/blast/unit_tests/api/aascan_unit_test.cpp`** -> AI Confidence: **99.48%**
28. **`src/algo/blast/unit_tests/api/bl2seq_unit_test.cpp`** -> AI Confidence: **99.48%**
29. **`src/algo/blast/unit_tests/api/blast_unit_test.cpp`** -> AI Confidence: **99.48%**
30. **`src/algo/blast/unit_tests/api/ntscan_unit_test.cpp`** -> AI Confidence: **99.48%**
31. **`src/algo/blast/unit_tests/api/pssmcreate_unit_test.cpp`** -> AI Confidence: **99.48%**
32. **`src/algo/blast/unit_tests/api/remote_blast_unit_test.cpp`** -> AI Confidence: **99.48%**
33. **`src/app/blast/blast_app_util.cpp`** -> AI Confidence: **99.48%**
34. **`src/app/blast/blastn_app.cpp`** -> AI Confidence: **99.48%**
35. **`src/app/blast/blastp_app.cpp`** -> AI Confidence: **99.48%**
36. **`src/app/blast/blastx_app.cpp`** -> AI Confidence: **99.48%**
37. **`src/app/blast/deltablast_app.cpp`** -> AI Confidence: **99.48%**
38. **`src/app/blast/psiblast_app.cpp`** -> AI Confidence: **99.48%**
39. **`src/app/blast/rpsblast_app.cpp`** -> AI Confidence: **99.48%**
40. **`src/app/blast/rpstblastn_app.cpp`** -> AI Confidence: **99.48%**
41. **`src/app/blast/tblastn_app.cpp`** -> AI Confidence: **99.48%**
42. **`src/app/blast/tblastx_app.cpp`** -> AI Confidence: **99.48%**
43. **`src/algo/blast/composition_adjustment/redo_alignment.c`** -> AI Confidence: **99.48%**
44. **`src/algo/blast/core/blast_engine.c`** -> AI Confidence: **99.48%**
45. **`src/algo/blast/core/blast_gapalign.c`** -> AI Confidence: **99.48%**
46. **`src/algo/blast/core/blast_kappa.c`** -> AI Confidence: **99.48%**
47. **`src/algo/blast/core/blast_traceback.c`** -> AI Confidence: **99.48%**
48. **`src/algo/blast/core/lookup_wrap.c`** -> AI Confidence: **99.48%**
49. **`src/algo/blast/core/na_ungapped.c`** -> AI Confidence: **99.48%**
50. **`src/algo/blast/api/blast_seqalign.cpp`** -> AI Confidence: **99.39%**
51. **`src/algo/blast/api/psiblast_aux_priv.cpp`** -> AI Confidence: **99.39%**
52. **`src/algo/blast/api/remote_blast.cpp`** -> AI Confidence: **99.39%**
53. **`src/algo/blast/blastinput/blast_input.cpp`** -> AI Confidence: **99.39%**
54. **`src/algo/blast/dbindex/dbindex.cpp`** -> AI Confidence: **99.39%**
55. **`src/algo/blast/format/blastxml2_format.cpp`** -> AI Confidence: **99.39%**
56. **`src/algo/blast/format/build_archive.cpp`** -> AI Confidence: **99.39%**
57. **`src/algo/blast/gumbel_params/gumbel_params.cpp`** -> AI Confidence: **99.39%**
58. **`src/algo/blast/gumbel_params/njn_localmaxstatutil.cpp`** -> AI Confidence: **99.39%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/app/blast/cleanup-blastdb-volumes.py` -> **100.0%** Exposure
- `src/app/blast/legacy_blast.pl` -> **100.0%** Exposure
- `src/app/blast/update_blastdb.pl` -> **100.0%** Exposure
- `src/algo/blast/api/bioseq_extract_data_priv.cpp` -> **20.0%** Exposure
- `src/algo/blast/api/bl2seq.cpp` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `src/app/blast/update_blastdb.pl` -> **100.0%** Exposure
### Raw Memory Manipulation
- `src/algo/blast/api/seqsrc_seqdb.cpp` -> **10.0%** Exposure
- `src/algo/blast/gumbel_params/njn_matrix.hpp` -> **10.0%** Exposure
- `src/algo/blast/gumbel_params/sls_alp.cpp` -> **10.0%** Exposure
- `src/algo/blast/composition_adjustment/compo_heap.c` -> **10.0%** Exposure
- `src/algo/blast/core/blast_aalookup.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `src/app/blast/get_species_taxids.sh` -> **100.0%** Exposure
- `src/algo/blast/api/bioseq_extract_data_priv.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_options_builder.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_options_handle.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_options_local_priv.cpp` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3350` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/app/blast/update_blastdb.pl` (PERL) -> Cumulative Risk: **879.89**
- **Archetype:** `file_cluster_0` (Distance: 14.207 IQR)
- **Magnitude:** 4647.94 | **LOC:** 1070 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `get_files_from_json_metadata_1_1` (Impact: 3677.8), `showall_from_metadata_file_1_1` (Impact: 58.6)

### 2. `src/algo/blast/api/local_db_adapter.cpp` (CPP) -> Cumulative Risk: **791.15**
- **Archetype:** `file_cluster_13` (Distance: 16.763 IQR)
- **Magnitude:** 220.62 | **LOC:** 206 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9992%), Tech Debt (99.8348%)
- **Heaviest Functions:** `CLocalDbAdapter::CLocalDbAdapter` (Impact: 36.2), `CLocalDbAdapter::MakeSeqSrc` (Impact: 32.8), `CLocalDbAdapter::MakeSeqInfoSrc` (Impact: 31.3)

### 3. `src/algo/blast/blastinput/blast_args.cpp` (CPP) -> Cumulative Risk: **788.48**
- **Archetype:** `file_cluster_8` (Distance: 14.15 IQR)
- **Magnitude:** 5291.2 | **LOC:** 3844 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `CIgBlastArgs::ExtractAlgorithmOptions` (Impact: 354.7), `s_SetCompositionBasedStats` (Impact: 331.9), `CFormattingArgs::ExtractAlgorithmOptions` (Impact: 297.1)

### 4. `src/algo/blast/core/blast_hspstream.c` (C) -> Cumulative Risk: **783.38**
- **Archetype:** `file_cluster_8` (Distance: 14.186 IQR)
- **Magnitude:** 823.28 | **LOC:** 867 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9971%)
- **Heaviest Functions:** `BlastHSPStreamMerge` (Impact: 116.7), `BlastHSPStreamRegisterPipe` (Impact: 47.4), `BlastHSPStreamBatchRead` (Impact: 33.5)

### 5. `src/app/blast/get_species_taxids.sh` (SHELL) -> Cumulative Risk: **773.62**
- **Archetype:** `file_cluster_11` (Distance: 12.318 IQR)
- **Magnitude:** 117.04 | **LOC:** 153 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9999%), State Flux (99.9899%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 40.1), `Anonymous_Block` (Impact: 14.3), `Anonymous_Block` (Impact: 10.7)

### 6. `src/algo/blast/composition_adjustment/nlm_linear_algebra.c` (C) -> Cumulative Risk: **772.77**
- **Archetype:** `file_cluster_13` (Distance: 14.427 IQR)
- **Magnitude:** 437.14 | **LOC:** 240 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.999%)
- **Heaviest Functions:** `Nlm_SolveLtriangPosDef` (Impact: 36.2), `Nlm_DenseMatrixNew` (Impact: 31.4), `Nlm_Int4MatrixNew` (Impact: 31.3)

### 7. `src/algo/blast/gumbel_params/general_score_matrix.cpp` (CPP) -> Cumulative Risk: **772.67**
- **Archetype:** `file_cluster_8` (Distance: 13.696 IQR)
- **Magnitude:** 485.3 | **LOC:** 229 | **CtrlFlow:** 95.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9245%)
- **Heaviest Functions:** `CGeneralScoreMatrix::CGeneralScoreMatrix` (Impact: 111.7), `CGeneralScoreMatrix::CGeneralScoreMatrix` (Impact: 44.0), `CGeneralScoreMatrix::CGeneralScoreMatrix` (Impact: 43.1)

### 8. `src/algo/blast/core/blast_options.c` (C) -> Cumulative Risk: **772.07**
- **Archetype:** `file_cluster_8` (Distance: 13.381 IQR)
- **Magnitude:** 2341.9 | **LOC:** 2015 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `LookupTableOptionsValidate` (Impact: 224.5), `BlastScoringOptionsValidate` (Impact: 106.2), `SBlastFilterOptionsValidate` (Impact: 92.8)

### 9. `src/algo/blast/vdb/error_priv.c` (C) -> Cumulative Risk: **765.52**
- **Archetype:** `file_cluster_13` (Distance: 13.419 IQR)
- **Magnitude:** 627.56 | **LOC:** 252 | **CtrlFlow:** 92.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.999%)
- **Heaviest Functions:** `VDBSRC_FormatErrorMsg` (Impact: 386.5), `VDBSRC_InitErrorMsgWithContext` (Impact: 15.2), `VDBSRC_InitLocalErrorMsg` (Impact: 7.8)

### 10. `src/algo/blast/format/data4xmlformat.cpp` (CPP) -> Cumulative Risk: **757.6**
- **Archetype:** `file_cluster_13` (Distance: 13.782 IQR)
- **Magnitude:** 698.24 | **LOC:** 301 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.7435%)
- **Heaviest Functions:** `CCmdLineBlastXMLReportData::x_FillScoreM` (Impact: 184.5), `CCmdLineBlastXMLReportData::x_Init` (Impact: 182.2), `CCmdLineBlastXMLReportData::GetEntropy` (Impact: 31.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/algo/blast/core/jumper.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.376 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.99 IQR)
- **Top Global Matches:** file_cluster_11: 15.376, file_cluster_0: 15.436, file_cluster_8: 15.448
- **Magnitude:** 7844.8 | **LOC:** 4583 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 131
- **Risk Profile:** Cognitive Load (78.5738%), Tech Debt (21.2855%)
**Top Internal Functions/Classes:**
  * `BlastNaExtendJumper` (Impact: 446.2 | O(N^6) | DB: 131)
  * `DoAnchoredScan` (Impact: 240.2 | O(N^6) | DB: 69)
  * `JumperExtendRightCompressedWithTraceback` (Impact: 236.7 | O(N^6) | DB: 100)
  * `JumperExtendLeftCompressedWithTracebackO` (Impact: 221.9 | O(N^6) | DB: 93)
  * `JumperExtendRightCompressedWithTraceback` (Impact: 202.7 | O(N^6) | DB: 64)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 957`, `structural_boundaries: 147`, `args: 1`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3561`, `dead_code: 33`, `fragile_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `api: 616`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 64`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jumper.h, blast_hits.h, blast_gapalign_priv.h, hspfilter_mapper.h, blast_nalookup.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp_sim.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.175 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.693 IQR)
- **Top Global Matches:** file_cluster_8: 14.175, file_cluster_7: 14.587, file_cluster_13: 14.614
- **Magnitude:** 5855.54 | **LOC:** 4176 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 281
- **Risk Profile:** Cognitive Load (60.2597%), Tech Debt (15.4825%)
**Top Internal Functions/Classes:**
  * `alp_sim::calculate_main_parameters2m` (Impact: 668.6 | O(N^6) | DB: 281)
  * `alp_sim::alp_sim` (Impact: 537.2 | O(N^6) | DB: 148)
    * *Intent:* /* $Id$ * =========================================================================== * * PUBLIC DOM...
  * `alp_sim::get_minimal_simulation` (Impact: 340.5 | O(N^6) | DB: 86)
  * `alp_sim::calculate_FSC` (Impact: 317.0 | O(N^6) | DB: 205)
  * `alp_sim::calculate_C` (Impact: 188.1 | O(N^6) | DB: 101)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 65`, `args: 71`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 2418`, `dead_code: 1`, `orphaned_logic: 24`
* *Architecture:* `import: 2`
* *Defense:* `safety: 49`, `doc: 1`, `immutability_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sls_alp_sim.hpp, ncbi_pch.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/blastinput/blast_args.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.15 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.282 IQR)
- **Top Global Matches:** file_cluster_8: 14.15, file_cluster_7: 14.512, file_cluster_13: 14.557
- **Magnitude:** 5291.2 | **LOC:** 3844 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (70.2427%), Tech Debt (93.147%)
**Top Internal Functions/Classes:**
  * `CIgBlastArgs::ExtractAlgorithmOptions` (Impact: 354.7 | O(N^6) | DB: 90)
  * `s_SetCompositionBasedStats` (Impact: 331.9 | O(N^6) | DB: 21)
    * *Intent:* /* $Id$
  * `CFormattingArgs::ExtractAlgorithmOptions` (Impact: 297.1 | O(N^6) | DB: 56)
  * `CFormattingArgs::ParseFormattingString` (Impact: 246.3 | O(N^6) | DB: 26)
  * `CPsiBlastArgs::ExtractAlgorithmOptions` (Impact: 241.1 | O(N^6) | DB: 38)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 523`, `structural_boundaries: 80`, `args: 147`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 1670`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 6`, `orphaned_logic: 60`
* *Architecture:* None
* *Defense:* `safety: 16`, `doc: 12`, `immutability_locks: 65`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` align_format_util.hpp, ncbi_pch.hpp, tax4blastsqlite.hpp, blast_exception.hpp, PssmWithParameters.hpp, line_reader.hpp, blast_aux.hpp, blast_nalookup.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sample/app/deployable_cgi/pkg/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_gapalign.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.933 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.006 IQR)
- **Top Global Matches:** file_cluster_8: 14.933, file_cluster_7: 15.042, file_cluster_13: 15.118
- **Magnitude:** 4833.96 | **LOC:** 4781 | **CtrlFlow:** 86.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 225
- **Risk Profile:** Cognitive Load (44.3073%), Tech Debt (11.15%)
**Top Internal Functions/Classes:**
  * `ALIGN_EX` (Impact: 457.4 | O(N^6) | DB: 225)
  * `s_OutOfFrameGappedAlign` (Impact: 250.2 | O(N^6) | DB: 159)
  * `BLAST_GetGappedScore` (Impact: 149.2 | O(N^6) | DB: 49)
  * `s_BlastAlignPackedNucl` (Impact: 125.0 | O(N^6) | DB: 66)
  * `s_BlastOOFTracebackToGapEditScript` (Impact: 120.4 | O(N^6) | DB: 59)
    * *Intent:* /** Set up a BLAST_SequenceBlk structure for a single query sequence * @param concatenated_query Que...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 511`, `structural_boundaries: 77`, `args: 2`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 2615`, `dead_code: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 359`
* *Defense:* `safety: 9`, `doc: 100`, `immutability_locks: 53`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` blast_gapalign.h, blast_itree.h, blast_util.h, jumper.h, blast_hits_priv.h, ncbi_math.h, blast_gapalign_priv.h, greedy_align.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/app/blast/update_blastdb.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.207 IQR)
- **Top Global Matches:** file_cluster_0: 14.207, file_cluster_13: 14.24, file_cluster_4: 14.458
- **Magnitude:** 4647.94 | **LOC:** 1070 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 260
- **Risk Profile:** Cognitive Load (77.6516%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_files_from_json_metadata_1_1` (Impact: 3677.8 | O(2^N) | DB: 260)
  * `showall_from_metadata_file_1_1` (Impact: 58.6 | O(N^5) | DB: 13)
    * *Intent:* # Display metadata from version 1.1 of BLASTDB metadata files
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 388`, `structural_boundaries: 283`, `args: 39`, `func_start: 32`
* *Risk/State:* `high_risk_execution: 27`, `state_mutation: 882`, `dead_code: 3`
* *Architecture:* `io: 14`, `concurrency: 12`, `import: 31`
* *Defense:* `safety: 4`, `doc: 24`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constant, File::Temp, output, longer, JSON::PP, Time::Local, files, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_hits.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.75 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.466 IQR)
- **Top Global Matches:** file_cluster_8: 14.75, file_cluster_7: 14.849, file_cluster_13: 14.913
- **Magnitude:** 4225.68 | **LOC:** 3892 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 226
- **Risk Profile:** Cognitive Load (41.4229%), Tech Debt (23.596%)
**Top Internal Functions/Classes:**
  * `s_QueryEndCompareHSPs` (Impact: 772.7 | O(N^6) | DB: 226)
  * `ScoreCompareHSPs` (Impact: 113.2 | O(N^6) | DB: 20)
    * *Intent:* /** Adjust start and end of an HSP in a translated sequence segment. * @param segment BlastSeg struc...
  * `Blast_HSPReevaluateWithAmbiguitiesGapped` (Impact: 113.0 | O(N^6) | DB: 82)
  * `s_Blast_HSPGetNumIdentitiesAndPositives` (Impact: 113.0 | O(N^6) | DB: 37)
  * `s_Blast_HSPGetOOFNumIdentitiesAndPositiv` (Impact: 89.5 | O(N^4) | DB: 33)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 158`, `args: 9`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1905`, `dead_code: 2`, `orphaned_logic: 24`
* *Architecture:* `api: 446`
* *Defense:* `safety: 10`, `doc: 89`, `immutability_locks: 96`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blast_hspstream.h, blast_itree.h, blast_util.h, jumper.h, blast_hits_priv.h, ncbi_math.h, blast_hits.h, blast_def.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_kappa.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.938 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.106 IQR)
- **Top Global Matches:** file_cluster_13: 14.938, file_cluster_8: 14.946, file_cluster_11: 14.965
- **Magnitude:** 3662.8 | **LOC:** 3925 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 378
- **Risk Profile:** Cognitive Load (35.2729%), Tech Debt (8.9575%)
**Top Internal Functions/Classes:**
  * `s_AdjustEvaluesForComposition` (Impact: 1773.6 | O(N^6) | DB: 378)
    * *Intent:* */ #include <float.h> #include <algo/blast/core/ncbi_math.h> #include <algo/blast/core/blast_hits.h>...
  * `s_HSPListNormalizeScores` (Impact: 7.8 | O(N^6) | DB: 5)
    * *Intent:* * and reliability of the software and data, the NLM and the U.S. * Government do not and cannot warr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 73`, `args: 12`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 1392`, `dead_code: 10`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 448`, `import: 5`
* *Defense:* `safety: 50`, `doc: 163`, `immutability_locks: 41`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` blast_posit.h, matrix_frequency_data.h, link_hsps.h, blast_psi_priv.h, blast_hits_priv.h, blast_hits.h, nlm_linear_algebra.h, compo_heap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_psi_priv.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.293 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.284 IQR)
- **Top Global Matches:** file_cluster_8: 14.293, file_cluster_7: 14.384, file_cluster_13: 14.498
- **Magnitude:** 3566.2 | **LOC:** 3177 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 378
- **Risk Profile:** Cognitive Load (53.4818%), Tech Debt (16.8998%)
**Top Internal Functions/Classes:**
  * `_PSIMsaNew` (Impact: 1942.4 | O(N^6) | DB: 378)
  * `_PSIPackedMsaNew` (Impact: 41.1 | O(N^6) | DB: 16)
  * `_PSIAllocateMatrix` (Impact: 26.1 | O(N^4) | DB: 7)
    * *Intent:* * * This software/database is a "United States Government Work" under the * terms of the United Stat...
  * `_PSIPackedMsaFree` (Impact: 22.2 | O(N^6) | DB: 1)
    * *Intent:* _PSIPackedMsa* retval = NULL; /* the return value */
  * `__printPackedMsaFP` (Impact: 18.8 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 111`, `args: 14`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1141`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 309`
* *Defense:* `safety: 4`, `doc: 61`, `test: 1`, `immutability_locks: 82`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blast_dynarray.h, composition_constants.h, blast_posit.h, matrix_frequency_data.h, blast_psi_priv.h, blast_util.h, ncbi_math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/app/blast/legacy_blast.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.869 IQR)
- **Top Global Matches:** file_cluster_0: 12.869, file_cluster_8: 12.937, file_cluster_13: 13.173
- **Magnitude:** 3257.6 | **LOC:** 1360 | **CtrlFlow:** 84.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 202
- **Risk Profile:** Cognitive Load (90.7148%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_blastall` (Impact: 2591.6 | O(N^6) | DB: 202)
    * *Intent:* # Handle the conversion from blastall arguments to the corresponding C++ # binaries
  * `convert_filter_string` (Impact: 29.1 | O(N^3) | DB: 10)
  * `convert_sequence_locations` (Impact: 18.2 | O(N^3) | DB: 5)
  * `convert_float_to_int` (Impact: 18.1 | O(N^3) | DB: 8)
    * *Intent:* # Converts floating point numbers to integers
  * `convert_strand` (Impact: 11.0 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 471`, `structural_boundaries: 85`, `args: 34`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 555`, `dead_code: 5`
* *Architecture:* `io: 16`, `import: 7`
* *Defense:* `safety: 3`, `doc: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constant, File::Temp, sgi, warnings, Pod::Usage, Getopt::Long, or, equivalent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/na_ungapped.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.007 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_13: 15.007, file_cluster_8: 15.088, file_cluster_0: 15.1
- **Magnitude:** 3048.38 | **LOC:** 2332 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (35.0413%), Tech Debt (9.9768%)
**Top Internal Functions/Classes:**
  * `s_BlastnDiagHashExtendInitialHit` (Impact: 136.8 | O(N^6) | DB: 41)
    * *Intent:* /** Test to see if seed->q_off exists in lookup table * @param lookup_wrap The lookup table wrap str...
  * `JumperNaWordFinder` (Impact: 133.5 | O(N^6) | DB: 60)
  * `s_BlastnDiagTableExtendInitialHit` (Impact: 129.7 | O(N^6) | DB: 47)
    * *Intent:* /* record the start point of the extension */
  * `s_BlastNaExtendAligned` (Impact: 128.3 | O(N^6) | DB: 43)
    * *Intent:* /** Perform ungapped extension given an offset pair, and save the initial * hit information if the h...
  * `s_BlastNaExtend` (Impact: 72.0 | O(N^6) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 65`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 1400`, `dead_code: 12`, `orphaned_logic: 4`
* *Architecture:* `api: 404`, `import: 8`
* *Defense:* `safety: 4`, `doc: 137`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blast_util.h, index_ungapped.h, na_ungapped.h, mb_indexed_lookup.h, jumper.h, blast_nascan.h, masksubj.inl, blast_nalookup.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/igblast/igblast.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.246 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.697 IQR)
- **Top Global Matches:** file_cluster_8: 15.246, file_cluster_11: 15.621, file_cluster_7: 15.623
- **Magnitude:** 2848.76 | **LOC:** 2090 | **CtrlFlow:** 93.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 132
- **Risk Profile:** Cognitive Load (77.4557%), Tech Debt (65.8289%)
**Top Internal Functions/Classes:**
  * `CIgBlast::x_AnnotateDomain` (Impact: 481.9 | O(N^6) | DB: 132)
  * `CIgBlast::x_ProcessDGeneResult` (Impact: 334.0 | O(N^6) | DB: 69)
  * `CIgBlast::s_AppendResults` (Impact: 215.1 | O(N^6) | DB: 32)
  * `CIgBlast::x_FillJDomain` (Impact: 119.2 | O(N^6) | DB: 27)
  * `CIgBlast::x_AnnotateC` (Impact: 87.0 | O(N^6) | DB: 40)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 15`, `args: 31`, `func_start: 28`
* *Risk/State:* `state_mutation: 1278`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 14`
* *Architecture:* None
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` composition_constants.h, local_blast.hpp, ncbi_pch.hpp, remote_blast.hpp, igblast.hpp, bl2seq.hpp, alnmap.hpp, objmgr_query_data.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_stat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.555 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.58 IQR)
- **Top Global Matches:** file_cluster_8: 14.555, file_cluster_7: 14.591, file_cluster_11: 14.693
- **Magnitude:** 2834.52 | **LOC:** 5271 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 151
- **Risk Profile:** Cognitive Load (35.8515%), Tech Debt (26.5745%)
**Top Internal Functions/Classes:**
  * `BlastKarlinLHtoK` (Impact: 836.0 | O(2^N) | DB: 151)
  * `s_BuildCompressedScoreMatrix` (Impact: 161.8 | O(N^6) | DB: 58)
  * `s_BlastSumPCalc` (Impact: 104.5 | O(N^3) | DB: 17)
    * *Intent:* /** Allocates a new SBlastScoreMatrix structure of the specified dimensions. * @param ncols number o...
  * `RPSRescalePssm` (Impact: 77.3 | O(N^6) | DB: 18)
  * `RPSFillScores` (Impact: 71.4 | O(N^6) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 94`, `args: 16`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1054`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 242`
* *Defense:* `safety: 6`, `doc: 102`, `test: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ncbi_math.h, boost_erf.h, blast_psi_priv.h, blast_stat.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_nalookup.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.972 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.832 IQR)
- **Top Global Matches:** file_cluster_0: 14.972, file_cluster_11: 15.016, file_cluster_8: 15.052
- **Magnitude:** 2741.2 | **LOC:** 2346 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (51.031%), Tech Debt (11.3569%)
**Top Internal Functions/Classes:**
  * `s_GetDiscTemplateType` (Impact: 116.0 | O(N^5))
  * `s_FillDiscMBTable` (Impact: 103.0 | O(N^6) | DB: 59)
  * `s_BlastNaHashLookupFinalize` (Impact: 100.0 | O(N^6) | DB: 73)
  * `BlastMBLookupTableNew` (Impact: 97.7 | O(N^6) | DB: 25)
    * *Intent:* /* The user probably specified a much larger word size (like 28)
  * `s_FillContigMBTable` (Impact: 91.0 | O(N^6) | DB: 43)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 96`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1278`, `dead_code: 13`, `orphaned_logic: 6`
* *Architecture:* `api: 312`
* *Defense:* `safety: 34`, `doc: 46`, `immutability_locks: 34`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_filter.h, blast_util.h, lookup_util.h, blast_nalookup.h, blast_encoding.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_options.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.381 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.116 IQR)
- **Top Global Matches:** file_cluster_8: 13.381, file_cluster_0: 13.619, file_cluster_7: 13.644
- **Magnitude:** 2341.9 | **LOC:** 2015 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (68.5576%), Tech Debt (82.2604%)
**Top Internal Functions/Classes:**
  * `LookupTableOptionsValidate` (Impact: 224.5 | O(N^6) | DB: 2)
  * `BlastScoringOptionsValidate` (Impact: 106.2 | O(N^6) | DB: 5)
  * `SBlastFilterOptionsValidate` (Impact: 92.8 | O(2^N) | DB: 1)
  * `s_BlastExtensionScoringOptionsValidate` (Impact: 79.8 | O(N^6))
  * `BLAST_ValidateOptions` (Impact: 62.6 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 185`, `args: 2`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 711`, `dead_code: 2`, `planned_debt: 2`, `orphaned_logic: 34`
* *Architecture:* `api: 312`
* *Defense:* `safety: 14`, `doc: 18`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` composition_constants.h, hspfilter_collector.h, blast_filter.h, blast_util.h, hspfilter_besthit.h, blast_stat.h, blast_options.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/dbindex_search/sr_search.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.785 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.857 IQR)
- **Top Global Matches:** file_cluster_8: 14.785, file_cluster_13: 15.016, file_cluster_11: 15.134
- **Magnitude:** 2312.02 | **LOC:** 482 | **CtrlFlow:** 89.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (88.132%), Tech Debt (83.4065%)
**Top Internal Functions/Classes:**
  * `CSRSearch::getNMer` (Impact: 519.3 | O(N^5) | DB: 33)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::combine` (Impact: 396.6 | O(N^6) | DB: 46)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::getNMer` (Impact: 186.7 | O(N^4) | DB: 23)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::reportResults` (Impact: 122.0 | O(N^5) | DB: 14)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::mergeResults` (Impact: 113.7 | O(N^6) | DB: 14)
    * *Intent:* //----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 24`, `args: 15`, `func_start: 10`
* *Risk/State:* `state_mutation: 809`, `duplicate_logic: 4`, `orphaned_logic: 6`
* *Architecture:* `import: 3`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sr_search.hpp, ncbi_pch.hpp, sr_search_impl.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/format/blast_format.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.761 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.834 IQR)
- **Top Global Matches:** file_cluster_8: 13.761, file_cluster_7: 14.172, file_cluster_13: 14.27
- **Magnitude:** 2303.24 | **LOC:** 2562 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 94
- **Risk Profile:** Cognitive Load (70.2524%), Tech Debt (78.7364%)
**Top Internal Functions/Classes:**
  * `CBlastFormat::PrintOneResultSet` (Impact: 478.4 | O(N^6) | DB: 94)
  * `CBlastFormat::PrintPhiResult` (Impact: 240.7 | O(N^6) | DB: 29)
  * `CBlastFormat::x_PrintXML2Report` (Impact: 115.0 | O(N^6) | DB: 7)
  * `CBlastFormat::WriteArchive` (Impact: 105.5 | O(N^6) | DB: 18)
  * `CBlastFormat::PrintReport` (Impact: 82.7 | O(N^6) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 54`, `args: 79`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 834`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 20`
* *Architecture:* None
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsonwrapp.hpp, ncbi_pch.hpp, blastxml2_format.hpp, ncbiutil.hpp, Seq_annot.hpp, ncbistre.hpp, build_archive.hpp, data4xmlformat.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/proteinkmer/blastkmerutils.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.568 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.275 IQR)
- **Top Global Matches:** file_cluster_8: 14.568, file_cluster_13: 14.641, file_cluster_11: 14.766
- **Magnitude:** 2249.98 | **LOC:** 954 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (68.5172%), Tech Debt (26.8706%)
**Top Internal Functions/Classes:**
  * `neighbor_query` (Impact: 189.2 | O(N^5) | DB: 44)
    * *Intent:* // find candidate matches with LSH
  * `BlastKmerGetKmerSetStats` (Impact: 124.9 | O(N^6) | DB: 41)
  * `BlastKmerGetKmerSet2` (Impact: 112.4 | O(N^6) | DB: 26)
  * `s_HashHashQuery` (Impact: 112.0 | O(N^5) | DB: 14)
  * `BlastKmerGetKmerSet` (Impact: 104.9 | O(N^6) | DB: 27)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 45`, `args: 49`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1087`, `dead_code: 5`, `orphaned_logic: 12`
* *Architecture:* `import: 11`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_filter.h, mhfile.hpp, random_gen.hpp, ncbi_pch.hpp, pearson.hpp, math.h, blast_encoding.h, seqdb.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.666 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.993 IQR)
- **Top Global Matches:** file_cluster_8: 13.666, file_cluster_7: 14.12, file_cluster_13: 14.151
- **Magnitude:** 2184.76 | **LOC:** 1995 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 132
- **Risk Profile:** Cognitive Load (59.691%), Tech Debt (27.3206%)
**Top Internal Functions/Classes:**
  * `alp::increment_H_weights_with_sentinels` (Impact: 179.6 | O(N^6) | DB: 84)
  * `alp::one_step_of_importance_sampling_wit` (Impact: 108.9 | O(N^6) | DB: 33)
  * `alp::kill_upto_level` (Impact: 88.6 | O(N^6) | DB: 12)
  * `alp::degree` (Impact: 73.9 | O(2^N))
  * `alp::John2_weight_calculation` (Impact: 64.2 | O(2^N) | DB: 38)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 38`, `args: 15`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1170`, `orphaned_logic: 21`
* *Architecture:* `import: 2`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sls_alp.hpp, ncbi_pch.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/api/remote_blast.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.751 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.906 IQR)
- **Top Global Matches:** file_cluster_8: 13.751, file_cluster_7: 14.09, file_cluster_13: 14.136
- **Magnitude:** 2143.06 | **LOC:** 2699 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 150
- **Risk Profile:** Cognitive Load (82.6753%), Tech Debt (97.5968%)
**Top Internal Functions/Classes:**
  * `CRemoteBlast::x_GetRequestInfoFromFile` (Impact: 903.7 | O(N^6) | DB: 150)
  * `CRemoteBlast::LoadFromArchive` (Impact: 86.5 | O(N^3) | DB: 3)
  * `CRemoteBlast::ConvertToRemoteMasks` (Impact: 58.2 | O(N^6) | DB: 7)
    * *Intent:* * purpose. * * Please cite the author in any work or product based on this material. * * ===========...
  * `FlattenBioseqSet` (Impact: 52.9 | O(2^N) | DB: 8)
  * `CRemoteBlast::x_InitQueries` (Impact: 50.6 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 82`, `args: 117`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 660`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 24`
* *Architecture:* None
* *Defense:* `safety: 14`, `doc: 12`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` psiblast_aux_priv.hpp, names.hpp, ncbi_pch.hpp, objistrasn.hpp, PssmWithParameters.hpp, objistrasnb.hpp, iterator.hpp, seq_loc_util.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/dbindex/dbindex_factory.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.45 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.978 IQR)
- **Top Global Matches:** file_cluster_8: 14.45, file_cluster_7: 14.562, file_cluster_13: 14.762
- **Magnitude:** 2084.14 | **LOC:** 1808 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (43.2496%), Tech Debt (96.8431%)
**Top Internal Functions/Classes:**
  * `CDbIndex_Factory::do_create_1_2` (Impact: 143.8 | O(N^6) | DB: 20)
    * *Intent:* /** Save the offset lists into the binary output stream. */
  * `CSubjectMap_Factory::AddSequenceChunk` (Impact: 114.6 | O(N^6) | DB: 29)
  * `CSubjectMap_Factory_TBase::AddSequenceCh` (Impact: 110.6 | O(N^5) | DB: 25)
  * `COffsetList::Save` (Impact: 102.2 | O(N^5) | DB: 15)
  * `COffsetData_Factory::Save` (Impact: 69.8 | O(N^4) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 157`, `args: 109`, `func_start: 67`, `class_start: 15`
* *Risk/State:* `state_mutation: 911`, `dead_code: 1`, `duplicate_logic: 14`, `orphaned_logic: 28`
* *Architecture:* `api: 14`
* *Defense:* `safety: 2`, `doc: 206`, `immutability_locks: 85`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_gapalign.h, sequence.hpp, dbindex.hpp, string, sequence_istream_fasta.hpp, ncbi_limits.hpp, sstream, ncbi_pch.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/hspfilter_mapper.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.357 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.466 IQR)
- **Top Global Matches:** file_cluster_8: 14.357, file_cluster_0: 14.385, file_cluster_11: 14.417
- **Magnitude:** 1993.4 | **LOC:** 4942 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 246
- **Risk Profile:** Cognitive Load (63.473%), Tech Debt (10.238%)
**Top Internal Functions/Classes:**
  * `s_SetAdapter` (Impact: 1107.7 | O(N^6) | DB: 246)
  * `s_FindAdapterInSequence` (Impact: 62.5 | O(N^6) | DB: 21)
    * *Intent:* /* $Id$
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 52`, `args: 4`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 657`, `dead_code: 6`, `orphaned_logic: 2`
* *Architecture:* `api: 151`
* *Defense:* `safety: 4`, `doc: 12`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_util.h, jumper.h, blast_hits.h, spliced_hits.h, hspfilter_mapper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp_data.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.57 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.209 IQR)
- **Top Global Matches:** file_cluster_8: 13.57, file_cluster_13: 13.989, file_cluster_7: 14.036
- **Magnitude:** 1919.76 | **LOC:** 1514 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (64.5451%), Tech Debt (62.3687%)
**Top Internal Functions/Classes:**
  * `alp_data::alp_data` (Impact: 289.4 | O(N^6) | DB: 75)
  * `alp_data::alp_data` (Impact: 158.1 | O(N^6) | DB: 90)
  * `importance_sampling::importance_sampling` (Impact: 147.1 | O(N^6) | DB: 105)
  * `alp_data::read_RR` (Impact: 69.3 | O(N^6) | DB: 18)
  * `alp_data::check_out_file` (Impact: 64.6 | O(N^6) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 40`, `args: 40`, `func_start: 15`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 913`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `import: 3`
* *Defense:* `safety: 28`, `doc: 1`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sls_alp_data.hpp, ncbi_pch.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/composition_adjustment/smith_waterman.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.081 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.461 IQR)
- **Top Global Matches:** file_cluster_8: 14.081, file_cluster_13: 14.17, file_cluster_7: 14.302
- **Magnitude:** 1866.72 | **LOC:** 616 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (60.8344%), Tech Debt (20.8784%)
**Top Internal Functions/Classes:**
  * `BLspecialSmithWatermanFindStart` (Impact: 340.9 | O(N^6) | DB: 43)
  * `BLspecialSmithWatermanScoreOnly` (Impact: 266.5 | O(N^6) | DB: 43)
  * `BLSmithWatermanFindStart` (Impact: 239.9 | O(N^6) | DB: 38)
    * *Intent:* /* testing scores with a gap in matchSeq, either starting a * new gap or extending an existing gap*/
  * `BLbasicSmithWatermanScoreOnly` (Impact: 173.6 | O(N^6) | DB: 38)
    * *Intent:* * PUBLIC DOMAIN NOTICE * National Center for Biotechnology Information * * This software/database is...
  * `Blast_SmithWatermanFindStart` (Impact: 42.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 20`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 563`, `orphaned_logic: 5`
* *Architecture:* `api: 121`, `import: 3`
* *Defense:* `safety: 2`, `doc: 8`, `immutability_locks: 16`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` smith_waterman.h, composition_constants.h, ncbi_std.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/composition_adjustment/composition_adjustment.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.322 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.929 IQR)
- **Top Global Matches:** file_cluster_8: 14.322, file_cluster_7: 14.381, file_cluster_13: 14.49
- **Magnitude:** 1865.0 | **LOC:** 1532 | **CtrlFlow:** 77.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 216
- **Risk Profile:** Cognitive Load (36.897%), Tech Debt (9.2842%)
**Top Internal Functions/Classes:**
  * `Blast_ApplyPseudocounts` (Impact: 1058.4 | O(N^6) | DB: 216)
    * *Intent:* * Highest level functions to solve the optimization problem for * compositional score matrix adjustm...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 37`, `args: 30`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 633`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 160`
* *Defense:* `safety: 2`, `doc: 57`, `immutability_locks: 30`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` limits.h, composition_constants.h, matrix_frequency_data.h, nlm_linear_algebra.h, unified_pvalues.h, ncbi_std.h, composition_adjustment.h, optimize_target_freq.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/algo/blast/core/blast_lookup.c` (C) | Magnitude: 356.36 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 170, indent_spaces: 166, api: 53, pointers: 38
- `src/algo/blast/composition_adjustment/redo_alignment.c` (C) | Magnitude: 621.96 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 382, state_mutation: 204, pointers: 144, api: 108
- `src/app/blast/update_blastdb.pl` (PERL) | Magnitude: 4647.94 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 882, indent_spaces: 634, branch: 388, structural_boundaries: 283
- `src/algo/blast/core/blast_nalookup.c` (C) | Magnitude: 2741.2 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1306, state_mutation: 1278, pointers: 519, api: 312
- `src/algo/blast/core/blast_aascan.c` (C) | Magnitude: 432.54 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 224, indent_spaces: 200, pointers: 89, api: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/app/blast/get_species_taxids.sh` (SHELL) | Magnitude: 117.04 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: io: 65, indent_spaces: 65, branch: 40, safety_bypasses: 33
- `src/algo/blast/core/jumper.c` (C) | Magnitude: 7844.8 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 3561, indent_spaces: 3263, pointers: 1297, branch: 957

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cmake-configure` (SHELL) | Magnitude: 3.78 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 4, reflection_metaprogramming: 3, state_mutation: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/algo/blast/core/hspfilter_besthit.c` (C) | Magnitude: 1138.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 610, indent_spaces: 375, pointers: 281, api: 89
- `src/algo/blast/api/bioseq_extract_data_priv.hpp` (CPP) | Magnitude: 23.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 182, indent_spaces: 37, structural_boundaries: 27, immutability_locks: 17
- `src/algo/blast/unit_tests/api/tracebacksearch_unit_test.cpp` (CPP) | Magnitude: 280.7 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 212, state_mutation: 182, pointers: 76, args: 30
- `src/algo/blast/api/seqinfosrc_bioseq.hpp` (CPP) | Magnitude: 9.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 53, indent_spaces: 17, structural_boundaries: 12, immutability_locks: 12
- `src/algo/blast/core/blast_kappa.c` (C) | Magnitude: 3662.8 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1887, state_mutation: 1392, pointers: 772, api: 448

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/algo/blast/gumbel_params/njn_approx.hpp` (CPP) | Magnitude: 19.72 | Delta: **0.27 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 54, args: 22, indent_spaces: 22, generics: 18
- `src/algo/blast/gumbel_params/njn_function.hpp` (CPP) | Magnitude: 22.32 | Delta: **0.484 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 140, args: 52, indent_spaces: 50, generics: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/algo/blast/api/magicblast.cpp` (CPP) | Magnitude: 468.64 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 223, indent_spaces: 134, branch: 50, pointers: 50
- `src/algo/blast/proteinkmer/demo/deploy.sh` (SHELL) | Magnitude: 25.9 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 9, branch: 7, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/algo/blast/unit_tests/api/blastsetup_unit_test.cpp` (CPP) | Magnitude: 10.52 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: planned_debt: 2, dead_code: 1, doc: 1, ownership: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/algo/blast/vdb/vdb_priv.h` (C) | Magnitude: 86.2 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 112, api: 69, indent_spaces: 27, structural_boundaries: 25
- `src/algo/blast/api/psiblast_aux_priv.hpp` (CPP) | Magnitude: 27.6 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 32, indent_spaces: 16, state_mutation: 10, structural_boundaries: 9
- `src/algo/blast/api/blast_setup.hpp` (CPP) | Magnitude: 32.2 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 81, indent_spaces: 36, args: 18, structural_boundaries: 17
- `src/algo/blast/vdb/vdbsequtil.h` (C) | Magnitude: 61.26 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 76, api: 45, indent_spaces: 25, structural_boundaries: 8
- `src/algo/blast/api/blast_seqalign.hpp` (CPP) | Magnitude: 10.52 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: doc: 60, ownership: 1, macros: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/app/blast/blastn_node.cpp` (CPP) | Magnitude: 203.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 68, pointers: 55, indent_tabs: 23
- `src/algo/blast/unit_tests/api/gencode_singleton_unit_test.cpp` (CPP) | Magnitude: 17.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 12, import: 6, args: 2
- `src/algo/blast/composition_adjustment/optimize_target_freq.c` (C) | Magnitude: 396.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 156, indent_spaces: 138, api: 59, pointers: 35
- `src/algo/blast/api/effsearchspace_calc.cpp` (CPP) | Magnitude: 73.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, pointers: 26, state_mutation: 22, doc: 14
- `src/algo/blast/core/blast_gapalign_priv.h` (C) | Magnitude: 42.96 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 49, api: 27, indent_spaces: 17, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/algo/blast/unit_tests/api/Makefile.aascan_unit_test.app` (MAKEFILE) | Magnitude: 15.22 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 2, dead_code: 1
- `src/algo/blast/unit_tests/api/Makefile.blastdiag_unit_test.app` (MAKEFILE) | Magnitude: 15.22 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 2, dead_code: 1
- `src/algo/blast/unit_tests/api/Makefile.rmblast_blasthits_unit_test.app` (MAKEFILE) | Magnitude: 15.22 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 2, dead_code: 1
- `src/algo/blast/api/prelim_search_runner.hpp` (CPP) | Magnitude: 10.52 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, ownership: 1, macros: 1
- `src/algo/blast/unit_tests/api/seqsrc_mock.hpp` (CPP) | Magnitude: 10.52 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, ownership: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/algo/blast/unit_tests/api/remote_blast_unit_test.cpp` -> Churn: **100.0%** | Cog Load: 86.0548% | Debt: 96.1509%
- `src/algo/blast/api/blast_node.cpp` -> Churn: **75.66%** | Cog Load: 69.9061% | Debt: 79.7712%
- `src/algo/blast/core/blast_nalookup.c` -> Churn: **52.48%** | Cog Load: 51.031% | Debt: 11.3569%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/algo/blast/blastinput/blast_args.cpp` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 5291.2
- `src/algo/blast/core/blast_gapalign.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 4833.96
- `src/algo/blast/core/na_ungapped.c` -> **Amelia Fong** (100.0% isolated ownership) | Magnitude: 3048.38
- `src/algo/blast/core/blast_stat.c` -> **Christiam Camacho** (100.0% isolated ownership) | Magnitude: 2834.52
- `src/algo/blast/core/blast_nalookup.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 2741.2

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/algo/blast/api/blast_objmgr_priv.hpp` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.89%)
- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `src/algo/blast/gumbel_params/sls_alp_sim.hpp` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9986%)
- `src/algo/blast/unit_tests/api/test_objmgr.hpp` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9964%)
- `src/algo/blast/gumbel_params/njn_dynprogproblim.hpp` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9128%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/app/blast/blast_app_util.hpp` -> **Severity: 1.551** (Embedded: 0.0234 * Error Risk: 66.2494%)
- `src/algo/blast/unit_tests/api/test_objmgr.hpp` -> **Severity: 1.211** (Embedded: 0.052 * Error Risk: 23.2891%)
- `src/algo/blast/gumbel_params/njn_ioutil.hpp` -> **Severity: 0.92** (Embedded: 0.01 * Error Risk: 92.0633%)
- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 0.633** (Embedded: 0.0142 * Error Risk: 44.73%)
- `src/algo/blast/gumbel_params/njn_memutil.hpp` -> **Severity: 0.611** (Embedded: 0.0065 * Error Risk: 93.9053%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 2774.22** (Blast Radius: 27.861 * Doc Risk: 99.5736%)
- `src/algo/blast/gumbel_params/sls_alp_regression.hpp` -> **Severity: 1531.305** (Blast Radius: 27.197 * Doc Risk: 56.3042%)
- `src/algo/blast/core/jumper.h` -> **Severity: 401.2** (Blast Radius: 4.012 * Doc Risk: 100.0%)
- `src/algo/blast/api/blast_setup.hpp` -> **Severity: 366.287** (Blast Radius: 30.728 * Doc Risk: 11.9203%)
- `src/algo/blast/core/blast_dynarray.h` -> **Severity: 354.695** (Blast Radius: 3.552 * Doc Risk: 99.8577%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
