# ARCHITECTURAL_BRIEF: blast
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/blast` |
| **Timestamp** | `2026-08-07T03:47:15.165630+00:00` |
| **Scan Duration** | `5.23s` |
| **Git Branch** | `main` |
| **Git Commit** | `0046959f6c628416d0fbb4f8f53b224c8244ace7` |
| **Git Remote** | `https://github.com/ncbi/ncbi-cxx-toolkit-public.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 582 malicious artifacts.

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
| Modularity | 0.7335 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `4.715`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 427 | 55.5% |
| file_cluster_13 | 111 | 14.4% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 29.1 | 16.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 49.8 | 67.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 40.9 | 18.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.3 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.4 | 2.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 36.9 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 54.0 | 96.3 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 77.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.9 | 11.9 | 11.9 |
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

- `handle_blastall` (@ `src/app/blast/legacy_blast.pl`) -> Impact: **778.2** | LOC: 1153
  * *Intent:* # Handle the conversion from blastall arguments to the corresponding C++ # binaries
- `handle_seedtop` (@ `src/app/blast/legacy_blast.pl`) -> Impact: **651.7** | LOC: 978
- `_PSIMsaNew` (@ `src/algo/blast/core/blast_psi_priv.c`) -> Impact: **601.3** | LOC: 1297
- `handle_megablast` (@ `src/app/blast/legacy_blast.pl`) -> Impact: **577.3** | LOC: 876
- `s_AdjustEvaluesForComposition` (@ `src/algo/blast/core/blast_kappa.c`) -> Impact: **561.1** | LOC: 1523
  * *Intent:* */ #include <float.h> #include <algo/blast/core/ncbi_math.h> #include <algo/blast/core/blast_hits.h> #include <algo/blast/core/blast_kappa.h> #include...
- `get_files_from_json_metadata_1_1` (@ `src/app/blast/update_blastdb.pl`) -> Impact: **525.5** | LOC: 810
- `_PSIUpdatePositionCounts` (@ `src/algo/blast/core/blast_psi_priv.c`) -> Impact: **490.9** | LOC: 1048
- `handle_blastpgp` (@ `src/app/blast/legacy_blast.pl`) -> Impact: **424.2** | LOC: 656
- `s_SetAdapter` (@ `src/algo/blast/core/hspfilter_mapper.c`) -> Impact: **350.0** | LOC: 937
- `Blast_ApplyPseudocounts` (@ `src/algo/blast/composition_adjustment/composition_adjustment.c`) -> Impact: **331.7** | LOC: 820
  * *Intent:* * Highest level functions to solve the optimization problem for * compositional score matrix adjustment. * * @author Yi-Kuo Yu, Alejandro Schaffer, E....

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/algo/blast/core` | 77 | 46955.46 | 37.12% | 39.18% |
| `src/algo/blast/unit_tests/api` | 219 | 15552.06 | 17.6% | 21.56% |
| `src/algo/blast/api` | 96 | 14589.78 | 27.81% | 60.22% |
| `src/algo/blast/gumbel_params` | 44 | 13640.42 | 39.19% | 43.05% |
| `src/app/blast` | 65 | 8487.54 | 22.74% | 18.49% |
| `src/algo/blast/blastinput` | 24 | 5528.32 | 27.61% | 79.7% |
| `src/sample/app/deployable_cgi/pkg` | 1 | 5000.0 | 0.0% | 0.0% |
| `src/algo/blast/format` | 13 | 4993.64 | 45.16% | 71.94% |
| `src/algo/blast/composition_adjustment` | 13 | 4211.16 | 30.86% | 27.25% |
| `src/algo/blast/proteinkmer` | 12 | 3709.38 | 40.64% | 51.81% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cmake-configure` -> **100.0%** Exposure
- `configure` -> **100.0%** Exposure
- `src/algo/blast/proteinkmer/demo/deploy.sh` -> **100.0%** Exposure
- `src/algo/blast/api/bioseq_extract_data_priv.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/bl2seq.cpp` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cmake-configure` -> **100.0%** Exposure
- `src/algo/blast/proteinkmer/demo/deploy.sh` -> **100.0%** Exposure
- `src/algo/blast/api/bioseq_extract_data_priv.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_node.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_options_builder.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/algo/blast/api/blast_options_cxx.cpp` -> **134** Orphaned Functions | **2** Duplicates
- `src/algo/blast/unit_tests/api/blastfilter_unit_test.cpp` -> **67** Orphaned Functions | **37** Duplicates
- `src/algo/blast/unit_tests/api/optionshandle_unit_test.cpp` -> **75** Orphaned Functions | **12** Duplicates
- `src/algo/blast/blastinput/blast_args.cpp` -> **60** Orphaned Functions | **10** Duplicates
- `src/algo/blast/api/remote_blast.cpp` -> **37** Orphaned Functions | **23** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3350` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/algo/blast/core/blast_options.c` (C) -> Cumulative Risk: **676.98**
- **Archetype:** `file_cluster_8` (Distance: 13.381 IQR)
- **Magnitude:** 1595.6 | **LOC:** 2015 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (91.9233%)
- **Heaviest Functions:** `LookupTableOptionsValidate` (Impact: 69.5), `BlastScoringOptionsValidate` (Impact: 33.6), `LookupTableOptionsNew` (Impact: 26.6)

### 2. `src/algo/blast/vdb/error_priv.c` (C) -> Cumulative Risk: **659.68**
- **Archetype:** `file_cluster_13` (Distance: 13.409 IQR)
- **Magnitude:** 336.86 | **LOC:** 252 | **CtrlFlow:** 92.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9198%), Safety Score (96.6573%)
- **Heaviest Functions:** `VDBSRC_FormatErrorMsg` (Impact: 113.7), `VDBSRC_InitErrorMsgWithContext` (Impact: 5.2), `VDBSRC_InitLocalErrorMsg` (Impact: 2.9)

### 3. `src/algo/blast/core/blast_hspstream.c` (C) -> Cumulative Risk: **655.23**
- **Archetype:** `file_cluster_8` (Distance: 14.186 IQR)
- **Magnitude:** 618.78 | **LOC:** 867 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.9202%), Documentation (98.4631%)
- **Heaviest Functions:** `BlastHSPStreamMerge` (Impact: 39.2), `BlastHSPCBSStreamClose` (Impact: 17.6), `BlastHSPStreamRegisterPipe` (Impact: 14.8)

### 4. `src/algo/blast/composition_adjustment/nlm_linear_algebra.c` (C) -> Cumulative Risk: **655.0**
- **Archetype:** `file_cluster_13` (Distance: 14.364 IQR)
- **Magnitude:** 314.74 | **LOC:** 240 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.525%), Safety Score (98.9633%)
- **Heaviest Functions:** `Nlm_SolveLtriangPosDef` (Impact: 11.2), `Nlm_DenseMatrixNew` (Impact: 9.8), `Nlm_LtriangMatrixNew` (Impact: 9.8)

### 5. `src/algo/blast/core/split_query.c` (C) -> Cumulative Risk: **646.78**
- **Archetype:** `file_cluster_8` (Distance: 13.13 IQR)
- **Magnitude:** 307.36 | **LOC:** 339 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9899%), Tech Debt (93.296%)
- **Heaviest Functions:** `SplitQueryBlkNew` (Impact: 16.6), `SplitQueryBlkFree` (Impact: 10.9), `SplitQueryBlk_GetQueryContextsForChunk` (Impact: 7.5)

### 6. `src/algo/blast/core/blast_extend.c` (C) -> Cumulative Risk: **636.0**
- **Archetype:** `file_cluster_8` (Distance: 13.564 IQR)
- **Magnitude:** 319.48 | **LOC:** 380 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.239%)
- **Heaviest Functions:** `score_compare_match` (Impact: 20.6), `Blast_ExtendWordExit` (Impact: 10.2), `BlastExtendWordNew` (Impact: 8.5)

### 7. `src/algo/blast/core/blast_parameters.c` (C) -> Cumulative Risk: **635.29**
- **Archetype:** `file_cluster_8` (Distance: 14.021 IQR)
- **Magnitude:** 890.16 | **LOC:** 1139 | **CtrlFlow:** 75.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.0791%), Safety Score (97.3722%)
- **Heaviest Functions:** `BlastHitSavingParametersUpdate` (Impact: 41.6), `BlastHitSavingParametersNew` (Impact: 23.4), `BlastInitialWordParametersNew` (Impact: 21.1)

### 8. `src/algo/blast/core/blast_seqsrc.c` (C) -> Cumulative Risk: **627.68**
- **Archetype:** `file_cluster_8` (Distance: 11.909 IQR)
- **Magnitude:** 296.28 | **LOC:** 582 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9942%), Tech Debt (99.9896%), Documentation (99.19%)
- **Heaviest Functions:** `BlastSeqSrcIteratorNewEx` (Impact: 9.2), `BlastSeqSrcSetRangesArgBuild` (Impact: 7.2), `BlastSeqSrcCopy` (Impact: 5.0)

### 9. `src/algo/blast/api/blast_node.cpp` (CPP) -> Cumulative Risk: **621.24**
- **Archetype:** `file_cluster_8` (Distance: 12.189 IQR)
- **Magnitude:** 323.54 | **LOC:** 323 | **CtrlFlow:** 80.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (89.1326%), Tech Debt (88.5488%)
- **Heaviest Functions:** `CBlastMasterNode::Processing` (Impact: 39.1), `NON_CONST_ITERATE` (Impact: 38.9), `CBlastMasterNode::FormatResults` (Impact: 23.9)

### 10. `src/algo/blast/blastinput/blast_args.cpp` (CPP) -> Cumulative Risk: **620.9**
- **Archetype:** `file_cluster_8` (Distance: 14.127 IQR)
- **Magnitude:** 2896.3 | **LOC:** 3844 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.8276%), Safety Score (97.3065%)
- **Heaviest Functions:** `CIgBlastArgs::ExtractAlgorithmOptions` (Impact: 107.9), `s_SetCompositionBasedStats` (Impact: 97.1), `CFormattingArgs::ExtractAlgorithmOptions` (Impact: 89.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/algo/blast/core/jumper.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.376 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.99 IQR)
- **Top Global Matches:** file_cluster_11: 15.376, file_cluster_0: 15.436, file_cluster_8: 15.448
- **Magnitude:** 5466.8 | **LOC:** 4583 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.5738%), Tech Debt (21.2855%)
**Top Internal Functions/Classes:**
  * `BlastNaExtendJumper` (Impact: 146.2)
  * `DoAnchoredScan` (Impact: 77.7)
  * `JumperExtendRightCompressedWithTraceback` (Impact: 76.7)
  * `JumperExtendLeftCompressedWithTracebackO` (Impact: 72.0)
  * `JumperExtendRightCompressedWithTraceback` (Impact: 65.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 957`, `structural_boundaries: 147`, `args: 1`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3561`, `dead_code: 33`, `fragile_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `api: 616`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 64`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` blast_gapalign_priv.h, hspfilter_mapper.h, blast_nalookup.h, blast_hits.h, jumper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sample/app/deployable_cgi/pkg/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Magnitude:** 3671.96 | **LOC:** 4781 | **CtrlFlow:** 86.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.3073%), Tech Debt (11.15%)
**Top Internal Functions/Classes:**
  * `ALIGN_EX` (Impact: 149.9)
  * `s_OutOfFrameGappedAlign` (Impact: 85.2)
  * `BLAST_GetGappedScore` (Impact: 49.2)
  * `s_BlastAlignPackedNucl` (Impact: 42.5)
  * `s_BlastOOFTracebackToGapEditScript` (Impact: 40.4)
    * *Intent:* /** Set up a BLAST_SequenceBlk structure for a single query sequence * @param concatenated_query Que...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 511`, `structural_boundaries: 77`, `args: 2`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 2615`, `dead_code: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 359`
* *Defense:* `safety: 9`, `doc: 100`, `immutability_locks: 53`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` blast_gapalign_priv.h, blast_hits_priv.h, blast_gapalign.h, blast_util.h, blast_itree.h, ncbi_math.h, jumper.h, greedy_align.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/app/blast/legacy_blast.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.79 IQR)
- **Top Global Matches:** file_cluster_0: 12.79, file_cluster_8: 12.859, file_cluster_13: 13.095
- **Magnitude:** 3649.8 | **LOC:** 1360 | **CtrlFlow:** 81.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5482%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_blastall` (Impact: 778.2)
    * *Intent:* # Handle the conversion from blastall arguments to the corresponding C++ # binaries
  * `handle_seedtop` (Impact: 651.7)
  * `handle_megablast` (Impact: 577.3)
  * `handle_blastpgp` (Impact: 424.2)
  * `handle_bl2seq` (Impact: 246.9)
    * *Intent:* # Tested: all conversions should work
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 107`, `args: 34`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 535`, `dead_code: 5`
* *Architecture:* `io: 16`, `import: 7`
* *Defense:* `safety: 3`, `doc: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, sgi, Pod::Usage, or, strict, equivalent, File::Temp, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp_sim.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.17 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.696 IQR)
- **Top Global Matches:** file_cluster_8: 14.17, file_cluster_7: 14.581, file_cluster_13: 14.608
- **Magnitude:** 3551.84 | **LOC:** 4176 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.2597%), Tech Debt (15.4825%)
**Top Internal Functions/Classes:**
  * `alp_sim::calculate_main_parameters2m` (Impact: 216.0)
  * `alp_sim::alp_sim` (Impact: 138.2)
    * *Intent:* /* $Id$ * =========================================================================== * * PUBLIC DOM...
  * `alp_sim::get_minimal_simulation` (Impact: 107.2)
  * `alp_sim::calculate_FSC` (Impact: 104.9)
  * `alp_sim::calculate_C` (Impact: 63.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 65`, `args: 65`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 2418`, `dead_code: 1`, `orphaned_logic: 24`
* *Architecture:* `import: 2`
* *Defense:* `safety: 49`, `doc: 1`, `immutability_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sls_alp_sim.hpp, ncbi_pch.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_hits.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.756 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.468 IQR)
- **Top Global Matches:** file_cluster_8: 14.756, file_cluster_7: 14.854, file_cluster_13: 14.919
- **Magnitude:** 3448.08 | **LOC:** 3892 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4229%), Tech Debt (32.2503%)
**Top Internal Functions/Classes:**
  * `s_QueryEndCompareHSPs` (Impact: 248.7)
  * `s_BlastHSPListsCombineByScore` (Impact: 237.4)
    * *Intent:* ********************************************************************************/
  * `s_Blast_HSPGetOOFNumIdentitiesAndPositiv` (Impact: 38.5)
  * `Blast_HSPReevaluateWithAmbiguitiesGapped` (Impact: 38.0)
  * `s_Blast_HSPGetNumIdentitiesAndPositives` (Impact: 35.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 158`, `args: 9`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1899`, `dead_code: 2`, `orphaned_logic: 32`
* *Architecture:* `api: 446`
* *Defense:* `safety: 10`, `doc: 89`, `immutability_locks: 96`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blast_hits_priv.h, blast_util.h, blast_itree.h, blast_hspstream.h, ncbi_math.h, blast_def.h, blast_hits.h, jumper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_kappa.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.891 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.123 IQR)
- **Top Global Matches:** file_cluster_13: 14.891, file_cluster_8: 14.898, file_cluster_11: 14.92
- **Magnitude:** 3210.2 | **LOC:** 3925 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.746%), Tech Debt (10.2118%)
**Top Internal Functions/Classes:**
  * `s_AdjustEvaluesForComposition` (Impact: 561.1)
    * *Intent:* */ #include <float.h> #include <algo/blast/core/ncbi_math.h> #include <algo/blast/core/blast_hits.h>...
  * `s_MatchingSequenceInitialize` (Impact: 283.3)
  * `Blast_RedoAlignmentCore_MT` (Impact: 185.7)
  * `s_BlastScoreBlk_Copy` (Impact: 53.6)
  * `s_GetPosBasedStartFreqRatios` (Impact: 31.5)
    * *Intent:* #endif /** * Given a list of HSPs with (possibly) high-precision scores, rescale * the scores to hav...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 73`, `args: 2`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 1392`, `dead_code: 10`, `planned_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 448`, `import: 5`
* *Defense:* `safety: 50`, `doc: 163`, `immutability_locks: 41`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` blast_posit.h, blast_gapalign_priv.h, redo_alignment.h, blast_hits_priv.h, blast_traceback.h, unified_pvalues.h, ncbi_math.h, blast_hits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_psi_priv.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.308 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.284 IQR)
- **Top Global Matches:** file_cluster_8: 14.308, file_cluster_7: 14.399, file_cluster_13: 14.513
- **Magnitude:** 3008.9 | **LOC:** 3177 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.0772%), Tech Debt (64.2143%)
**Top Internal Functions/Classes:**
  * `_PSIMsaNew` (Impact: 601.3)
  * `_PSIUpdatePositionCounts` (Impact: 490.9)
  * `_PSIComputeScoreProbabilities` (Impact: 48.2)
  * `s_PSIPurgeSimilarAlignments` (Impact: 43.1)
  * `_PSISaveDiagnostics` (Impact: 37.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 111`, `args: 13`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1141`, `fragile_debt: 2`, `orphaned_logic: 22`
* *Architecture:* `io: 4`, `api: 309`
* *Defense:* `safety: 4`, `doc: 61`, `test: 1`, `immutability_locks: 82`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blast_posit.h, composition_constants.h, blast_util.h, blast_dynarray.h, matrix_frequency_data.h, ncbi_math.h, blast_psi_priv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/blastinput/blast_args.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.127 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.231 IQR)
- **Top Global Matches:** file_cluster_8: 14.127, file_cluster_7: 14.489, file_cluster_13: 14.53
- **Magnitude:** 2896.3 | **LOC:** 3844 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (87.738%), Tech Debt (98.8276%)
**Top Internal Functions/Classes:**
  * `CIgBlastArgs::ExtractAlgorithmOptions` (Impact: 107.9)
  * `s_SetCompositionBasedStats` (Impact: 97.1)
    * *Intent:* /* $Id$
  * `CFormattingArgs::ExtractAlgorithmOptions` (Impact: 89.2)
  * `CFormattingArgs::ParseFormattingString` (Impact: 73.0)
  * `CPsiBlastArgs::ExtractAlgorithmOptions` (Impact: 72.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 523`, `structural_boundaries: 80`, `args: 127`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 1670`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 10`, `orphaned_logic: 60`
* *Architecture:* None
* *Defense:* `safety: 16`, `doc: 12`, `immutability_locks: 65`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` seq_masker_istat_factory.hpp, line_reader.hpp, seqdb.hpp, objmgr_query_data.hpp, blast_nalookup.h, PssmWithParameters.hpp, hspfilter_besthit.h, msa_pssm_input.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/igblast/igblast.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.206 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.635 IQR)
- **Top Global Matches:** file_cluster_8: 15.206, file_cluster_11: 15.578, file_cluster_13: 15.578
- **Magnitude:** 2257.66 | **LOC:** 2090 | **CtrlFlow:** 93.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.4557%), Tech Debt (99.9671%)
**Top Internal Functions/Classes:**
  * `CIgBlast::x_AnnotateDomain` (Impact: 146.9)
  * `ITERATE` (Impact: 137.7)
  * `ITERATE` (Impact: 126.0)
  * `CIgBlast::x_ProcessDGeneResult` (Impact: 99.2)
  * `NON_CONST_ITERATE` (Impact: 88.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 15`, `args: 23`, `func_start: 28`
* *Risk/State:* `state_mutation: 1278`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 14`, `orphaned_logic: 14`
* *Architecture:* None
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alnvec.hpp, alnmap.hpp, composition_constants.h, bl2seq.hpp, remote_blast.hpp, ncbi_pch.hpp, igblast.hpp, local_blast.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/na_ungapped.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.007 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_13: 15.007, file_cluster_8: 15.088, file_cluster_0: 15.1
- **Magnitude:** 2254.68 | **LOC:** 2332 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.0413%), Tech Debt (9.9768%)
**Top Internal Functions/Classes:**
  * `JumperNaWordFinder` (Impact: 46.0)
  * `s_BlastnDiagHashExtendInitialHit` (Impact: 44.2)
    * *Intent:* /** Test to see if seed->q_off exists in lookup table * @param lookup_wrap The lookup table wrap str...
  * `s_BlastnDiagTableExtendInitialHit` (Impact: 42.2)
    * *Intent:* /* record the start point of the extension */
  * `s_BlastNaExtendAligned` (Impact: 40.8)
    * *Intent:* /** Perform ungapped extension given an offset pair, and save the initial * hit information if the h...
  * `BlastChooseNaExtend` (Impact: 26.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 65`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 1400`, `dead_code: 12`, `orphaned_logic: 4`
* *Architecture:* `api: 404`, `import: 8`
* *Defense:* `safety: 4`, `doc: 137`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` masksubj.inl, blast_nascan.h, index_ungapped.h, na_ungapped.h, blast_util.h, blast_nalookup.h, jumper.h, mb_indexed_lookup.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_nalookup.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.972 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.832 IQR)
- **Top Global Matches:** file_cluster_0: 14.972, file_cluster_11: 15.016, file_cluster_8: 15.052
- **Magnitude:** 2041.7 | **LOC:** 2346 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (51.031%), Tech Debt (11.3569%)
**Top Internal Functions/Classes:**
  * `s_GetDiscTemplateType` (Impact: 40.0)
  * `s_FillDiscMBTable` (Impact: 35.5)
  * `s_BlastNaHashLookupFinalize` (Impact: 35.0)
  * `BlastMBLookupTableNew` (Impact: 32.7)
    * *Intent:* /* The user probably specified a much larger word size (like 28)
  * `s_FillContigMBTable` (Impact: 31.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 96`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1278`, `dead_code: 13`, `orphaned_logic: 6`
* *Architecture:* `api: 312`
* *Defense:* `safety: 34`, `doc: 46`, `immutability_locks: 34`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_encoding.h, blast_util.h, lookup_util.h, blast_nalookup.h, blast_filter.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_stat.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.54 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.579 IQR)
- **Top Global Matches:** file_cluster_8: 14.54, file_cluster_7: 14.575, file_cluster_13: 14.678
- **Magnitude:** 1820.82 | **LOC:** 5271 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.8515%), Tech Debt (39.5835%)
**Top Internal Functions/Classes:**
  * `BlastKarlinLHtoK` (Impact: 140.2)
  * `s_BlastSumPCalc` (Impact: 54.3)
    * *Intent:* /** Allocates a new SBlastScoreMatrix structure of the specified dimensions. * @param ncols number o...
  * `s_BuildCompressedScoreMatrix` (Impact: 51.5)
  * `RPSRescalePssm` (Impact: 24.4)
  * `Blast_ScoreBlkKbpUngappedCalc` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 94`, `args: 12`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1050`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 242`
* *Defense:* `safety: 6`, `doc: 102`, `test: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` blast_psi_priv.h, ncbi_math.h, blast_stat.h, boost_erf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/app/blast/update_blastdb.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.117 IQR)
- **Top Global Matches:** file_cluster_0: 14.117, file_cluster_13: 14.152, file_cluster_4: 14.367
- **Magnitude:** 1759.24 | **LOC:** 1070 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.1972%), Tech Debt (10.627%)
**Top Internal Functions/Classes:**
  * `get_files_from_json_metadata_1_1` (Impact: 525.5)
  * `download` (Impact: 61.1)
    * *Intent:* # Download the requested files only if their checksum files are missing or if # these (or the archiv...
  * `get_files_to_download` (Impact: 27.8)
    * *Intent:* # Obtains the list of files to download
  * `get_blastdb_metadata` (Impact: 21.7)
    * *Intent:* # Fetches the JSON text containing the BLASTDB metadata
  * `showall_from_metadata_file_1_1` (Impact: 20.5)
    * *Intent:* # Display metadata from version 1.1 of BLASTDB metadata files
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 350`, `structural_boundaries: 315`, `args: 39`, `func_start: 32`
* *Risk/State:* `high_risk_execution: 27`, `state_mutation: 868`, `dead_code: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 14`, `concurrency: 12`, `import: 31`
* *Defense:* `safety: 4`, `doc: 24`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` longer, the, warnings, File::stat, Archive::Tar, Time::Local, or, Net::FTP...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_options.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.381 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.116 IQR)
- **Top Global Matches:** file_cluster_8: 13.381, file_cluster_0: 13.619, file_cluster_7: 13.644
- **Magnitude:** 1595.6 | **LOC:** 2015 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.5576%), Tech Debt (82.2604%)
**Top Internal Functions/Classes:**
  * `LookupTableOptionsValidate` (Impact: 69.5)
  * `BlastScoringOptionsValidate` (Impact: 33.6)
  * `LookupTableOptionsNew` (Impact: 26.6)
  * `s_BlastExtensionScoringOptionsValidate` (Impact: 24.8)
  * `BLAST_GetSuggestedThreshold` (Impact: 22.8)
    * *Intent:* /* By default cross_match-like complexity adjusted scoring is turned off. RMBlastN is currently the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 185`, `args: 2`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 711`, `dead_code: 2`, `planned_debt: 2`, `orphaned_logic: 34`
* *Architecture:* `api: 312`
* *Defense:* `safety: 14`, `doc: 18`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_options.h, hspfilter_collector.h, blast_stat.h, composition_constants.h, hspfilter_besthit.h, blast_util.h, blast_filter.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/api/remote_blast.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.747 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.876 IQR)
- **Top Global Matches:** file_cluster_8: 13.747, file_cluster_7: 14.085, file_cluster_13: 14.127
- **Magnitude:** 1558.86 | **LOC:** 2699 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.5388%), Tech Debt (99.9977%)
**Top Internal Functions/Classes:**
  * `CRemoteBlast::x_GetRequestInfoFromFile` (Impact: 283.7)
  * `CRemoteBlast::LoadFromArchive` (Impact: 44.5)
  * `CRemoteBlast::GetResultSet` (Impact: 42.8)
  * `ITERATE` (Impact: 37.5)
    * *Intent:* // CBlast4Option states: // 0. start (no rid, no errors)
  * `ExtractBlast4Request` (Impact: 36.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 82`, `args: 103`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 656`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 23`, `orphaned_logic: 37`
* *Architecture:* None
* *Defense:* `safety: 14`, `doc: 12`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast__.hpp, stream_utils.hpp, remote_blast.hpp, unistd.h, search_strategy.hpp, objistrasn.hpp, objmgr_query_data.hpp, PssmWithParameters.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.666 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.993 IQR)
- **Top Global Matches:** file_cluster_8: 13.666, file_cluster_7: 14.12, file_cluster_13: 14.151
- **Magnitude:** 1518.16 | **LOC:** 1995 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.691%), Tech Debt (27.3206%)
**Top Internal Functions/Classes:**
  * `alp::increment_H_weights_with_sentinels` (Impact: 59.5)
  * `alp::one_step_of_importance_sampling_wit` (Impact: 35.2)
  * `alp::kill_upto_level` (Impact: 27.9)
  * `alp::increment_H_weights` (Impact: 22.0)
  * `alp::check_time_function` (Impact: 17.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 38`, `args: 15`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1170`, `orphaned_logic: 21`
* *Architecture:* `import: 2`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ncbi_pch.hpp, sls_alp.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/composition_adjustment/composition_adjustment.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.314 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.951 IQR)
- **Top Global Matches:** file_cluster_8: 14.314, file_cluster_7: 14.365, file_cluster_13: 14.471
- **Magnitude:** 1502.7 | **LOC:** 1532 | **CtrlFlow:** 77.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.897%), Tech Debt (19.8283%)
**Top Internal Functions/Classes:**
  * `Blast_ApplyPseudocounts` (Impact: 331.7)
    * *Intent:* * Highest level functions to solve the optimization problem for * compositional score matrix adjustm...
  * `Blast_CalcLambdaFullPrecision` (Impact: 62.9)
    * *Intent:* /**
  * `Blast_CompositionMatrixAdj` (Impact: 51.2)
    * *Intent:* /* A double precision score matrix */
  * `Blast_GetCompositionRange` (Impact: 31.2)
  * `Blast_CompositionWorkspaceNew` (Impact: 20.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 37`, `args: 22`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 633`, `dead_code: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 160`
* *Defense:* `safety: 2`, `doc: 57`, `immutability_locks: 30`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nlm_linear_algebra.h, composition_constants.h, composition_adjustment.h, ncbi_std.h, optimize_target_freq.h, limits.h, matrix_frequency_data.h, unified_pvalues.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/hspfilter_mapper.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.358 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.463 IQR)
- **Top Global Matches:** file_cluster_8: 14.358, file_cluster_0: 14.383, file_cluster_11: 14.417
- **Magnitude:** 1455.2 | **LOC:** 4942 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.9338%), Tech Debt (16.1822%)
**Top Internal Functions/Classes:**
  * `s_SetAdapter` (Impact: 350.0)
  * `s_BlastHSPMapperSplicedPairedRun` (Impact: 83.2)
  * `s_FindBestPairs` (Impact: 82.8)
  * `FindPartialyCoveredQueries` (Impact: 33.0)
  * `s_TrimChainEndToSubjPos` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 52`, `args: 4`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 655`, `dead_code: 6`, `orphaned_logic: 6`
* *Architecture:* `api: 151`
* *Defense:* `safety: 4`, `doc: 12`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` spliced_hits.h, blast_util.h, hspfilter_mapper.h, blast_hits.h, jumper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/format/blast_format.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.741 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.783 IQR)
- **Top Global Matches:** file_cluster_8: 13.741, file_cluster_7: 14.152, file_cluster_13: 14.245
- **Magnitude:** 1453.34 | **LOC:** 2562 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.2524%), Tech Debt (99.3648%)
**Top Internal Functions/Classes:**
  * `CBlastFormat::PrintOneResultSet` (Impact: 148.4)
  * `CBlastFormat::PrintPhiResult` (Impact: 75.7)
  * `CBlastFormat::LogBlastSearchInfo` (Impact: 50.1)
  * `CBlastFormat::x_PrintXML2Report` (Impact: 35.0)
  * `s_GetMolType` (Impact: 27.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 54`, `args: 67`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 834`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 13`, `orphaned_logic: 21`
* *Architecture:* None
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` seqdb.hpp, objostrxml.hpp, create_defline.hpp, objmgr_query_data.hpp, build_archive.hpp, Seq_descr.hpp, blastxml2_format.hpp, blast_stat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/dbindex/dbindex_factory.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.413 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.985 IQR)
- **Top Global Matches:** file_cluster_8: 14.413, file_cluster_7: 14.526, file_cluster_13: 14.726
- **Magnitude:** 1402.74 | **LOC:** 1808 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.2496%), Tech Debt (96.8431%)
**Top Internal Functions/Classes:**
  * `CDbIndex_Factory::do_create_1_2` (Impact: 44.8)
    * *Intent:* /** Save the offset lists into the binary output stream. */
  * `CSubjectMap_Factory_TBase::AddSequenceCh` (Impact: 39.0)
  * `COffsetList::Save` (Impact: 35.1)
  * `CSubjectMap_Factory::AddSequenceChunk` (Impact: 35.0)
  * `COffsetData_Factory::Save` (Impact: 29.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 157`, `args: 86`, `func_start: 67`, `class_start: 15`
* *Risk/State:* `state_mutation: 911`, `dead_code: 1`, `duplicate_logic: 14`, `orphaned_logic: 28`
* *Architecture:* `api: 14`
* *Defense:* `safety: 2`, `doc: 206`, `immutability_locks: 85`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sstream, seq_vector.hpp, dbindex.hpp, sequence_istream_fasta.hpp, dbindex.hpp, Seq_interval.hpp, iostream, string...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/link_hsps.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.563 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 6.159 IQR)
- **Top Global Matches:** file_cluster_8: 14.563, file_cluster_7: 14.594, file_cluster_13: 14.688
- **Magnitude:** 1393.44 | **LOC:** 1815 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5529%), Tech Debt (11.1122%)
**Top Internal Functions/Classes:**
  * `s_MergeLinkedHSPSets` (Impact: 76.0)
    * *Intent:* /* list is sorted by q_off, so q_off should only increase. * q_off_t can only differ from q_off by t...
  * `s_LinkedHSPSetsAdmissible` (Impact: 70.9)
  * `s_BlastUnevenGapLinkHSPs` (Impact: 33.8)
  * `s_RevCompareHSPsTbx` (Impact: 28.3)
  * `s_RevCompareHSPsTbn` (Impact: 28.1)
    * *Intent:* /** The helper array contains the info used frequently in the inner * for loops of the HSP linking a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 86`, `args: 5`, `func_start: 16`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 850`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 177`
* *Defense:* `safety: 9`, `doc: 105`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_hits_priv.h, link_hsps.h, blast_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/proteinkmer/blastkmerutils.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.394 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.324 IQR)
- **Top Global Matches:** file_cluster_8: 14.394, file_cluster_13: 14.471, file_cluster_11: 14.6
- **Magnitude:** 1372.18 | **LOC:** 954 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.5172%), Tech Debt (26.8706%)
**Top Internal Functions/Classes:**
  * `s_BlastKmerVerifyVolume` (Impact: 33.4)
  * `neighbor_query` (Impact: 30.4)
    * *Intent:* // find candidate matches with LSH
  * `BlastKmerGetKmerSetStats` (Impact: 23.6)
  * `BlastKmerGetKmerSet2` (Impact: 16.9)
  * `s_HashHashQuery` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 45`, `args: 9`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1087`, `dead_code: 5`, `orphaned_logic: 12`
* *Architecture:* `import: 11`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_seg.h, random_gen.hpp, math.h, pearson.hpp, mhfile.hpp, seqdb.hpp, blast_encoding.h, blastkmerutils.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/dbindex_search/sr_search.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.756 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.867 IQR)
- **Top Global Matches:** file_cluster_8: 14.756, file_cluster_13: 14.988, file_cluster_11: 15.106
- **Magnitude:** 1332.32 | **LOC:** 482 | **CtrlFlow:** 89.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.132%), Tech Debt (83.4065%)
**Top Internal Functions/Classes:**
  * `CSRSearch::getNMer` (Impact: 175.3)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::combine` (Impact: 117.1)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::getNMer` (Impact: 76.0)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::reportResults` (Impact: 42.0)
    * *Intent:* //----------------------------------------------------------------------------
  * `CSRSearch::mergeResults` (Impact: 33.6)
    * *Intent:* //----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 24`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 809`, `duplicate_logic: 4`, `orphaned_logic: 6`
* *Architecture:* `import: 3`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sr_search_impl.hpp, ncbi_pch.hpp, sr_search.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp_data.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.557 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.213 IQR)
- **Top Global Matches:** file_cluster_8: 13.557, file_cluster_13: 13.976, file_cluster_7: 14.023
- **Magnitude:** 1281.26 | **LOC:** 1514 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.5451%), Tech Debt (62.3687%)
**Top Internal Functions/Classes:**
  * `alp_data::alp_data` (Impact: 93.5)
  * `alp_data::alp_data` (Impact: 55.6)
  * `importance_sampling::importance_sampling` (Impact: 51.7)
  * `alp_data::read_RR` (Impact: 23.4)
  * `alp_data::check_out_file` (Impact: 22.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 40`, `args: 34`, `func_start: 15`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 913`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `import: 3`
* *Defense:* `safety: 28`, `doc: 1`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sls_alp_data.hpp, ncbi_pch.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/algo/blast/core/blast_lookup.c` (C) | Magnitude: 275.86 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 170, indent_spaces: 166, api: 53, pointers: 38
- `src/algo/blast/composition_adjustment/redo_alignment.c` (C) | Magnitude: 421.96 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 382, state_mutation: 204, pointers: 144, api: 108
- `src/app/blast/update_blastdb.pl` (PERL) | Magnitude: 1759.24 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 868, indent_spaces: 634, branch: 350, structural_boundaries: 315
- `src/algo/blast/core/blast_nalookup.c` (C) | Magnitude: 2041.7 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1306, state_mutation: 1278, pointers: 519, api: 312
- `src/algo/blast/core/blast_aascan.c` (C) | Magnitude: 345.14 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 224, indent_spaces: 200, pointers: 89, api: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/algo/blast/core/jumper.c` (C) | Magnitude: 5466.8 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 3561, indent_spaces: 3263, pointers: 1297, branch: 957
- `src/app/blast/get_species_taxids.sh` (SHELL) | Magnitude: 116.64 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 72, io: 65, indent_spaces: 65, safety_bypasses: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cmake-configure` (SHELL) | Magnitude: 3.78 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 4, reflection_metaprogramming: 3, state_mutation: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/algo/blast/core/hspfilter_besthit.c` (C) | Magnitude: 902.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 610, indent_spaces: 375, pointers: 281, api: 89
- `src/algo/blast/api/bioseq_extract_data_priv.hpp` (CPP) | Magnitude: 23.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 182, indent_spaces: 37, structural_boundaries: 27, immutability_locks: 17
- `src/algo/blast/api/remote_search.cpp` (CPP) | Magnitude: 146.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 137, state_mutation: 78, pointers: 42, branch: 25
- `src/algo/blast/core/blast_kappa.c` (C) | Magnitude: 3210.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1887, state_mutation: 1392, pointers: 772, api: 448
- `src/algo/blast/api/seqinfosrc_bioseq.hpp` (CPP) | Magnitude: 9.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 53, indent_spaces: 17, structural_boundaries: 12, immutability_locks: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/algo/blast/gumbel_params/njn_approx.hpp` (CPP) | Magnitude: 25.22 | Delta: **0.233 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 54, args: 22, indent_spaces: 22, generics: 18
- `src/algo/blast/gumbel_params/njn_function.hpp` (CPP) | Magnitude: 69.52 | Delta: **0.541 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 140, args: 52, indent_spaces: 50, generics: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/algo/blast/api/magicblast.cpp` (CPP) | Magnitude: 308.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 223, indent_spaces: 134, branch: 50, pointers: 50
- `src/algo/blast/proteinkmer/demo/deploy.sh` (SHELL) | Magnitude: 28.9 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 12, branch: 10, indent_spaces: 9, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/algo/blast/unit_tests/api/blastsetup_unit_test.cpp` (CPP) | Magnitude: 10.52 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: planned_debt: 2, dead_code: 1, doc: 1, ownership: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/algo/blast/vdb/vdb_priv.h` (C) | Magnitude: 86.2 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 112, api: 69, indent_spaces: 27, structural_boundaries: 25
- `src/algo/blast/api/psiblast_aux_priv.hpp` (CPP) | Magnitude: 27.6 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 32, indent_spaces: 16, state_mutation: 10, structural_boundaries: 9
- `src/algo/blast/api/blast_setup.hpp` (CPP) | Magnitude: 27.2 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 81, indent_spaces: 36, args: 18, structural_boundaries: 17
- `src/algo/blast/vdb/vdbsequtil.h` (C) | Magnitude: 61.26 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 76, api: 45, indent_spaces: 25, structural_boundaries: 8
- `src/algo/blast/api/blast_seqalign.hpp` (CPP) | Magnitude: 10.52 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: doc: 60, ownership: 1, macros: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/app/blast/blastn_node.cpp` (CPP) | Magnitude: 122.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 68, pointers: 55, indent_tabs: 23
- `src/algo/blast/unit_tests/api/gencode_singleton_unit_test.cpp` (CPP) | Magnitude: 17.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 12, import: 6, args: 2
- `src/algo/blast/api/effsearchspace_calc.cpp` (CPP) | Magnitude: 45.54 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, pointers: 26, state_mutation: 22, doc: 14
- `src/algo/blast/composition_adjustment/optimize_target_freq.c` (C) | Magnitude: 287.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 156, indent_spaces: 138, api: 59, pointers: 35
- `src/algo/blast/unit_tests/api/pssmcreate_cdd_unit_test.cpp` (CPP) | Magnitude: 989.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 811, state_mutation: 707, pointers: 238, branch: 91

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

- `src/algo/blast/unit_tests/api/remote_blast_unit_test.cpp` -> Churn: **100.0%** | Cog Load: 83.2998% | Debt: 99.926%
- `src/algo/blast/api/blast_node.cpp` -> Churn: **75.66%** | Cog Load: 68.5671% | Debt: 88.5488%
- `src/algo/blast/core/blast_nalookup.c` -> Churn: **52.48%** | Cog Load: 51.031% | Debt: 11.3569%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/algo/blast/core/blast_gapalign.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 3671.96
- `src/algo/blast/blastinput/blast_args.cpp` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 2896.3
- `src/algo/blast/core/na_ungapped.c` -> **Amelia Fong** (100.0% isolated ownership) | Magnitude: 2254.68
- `src/algo/blast/core/blast_nalookup.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 2041.7
- `src/algo/blast/core/blast_stat.c` -> **Christiam Camacho** (100.0% isolated ownership) | Magnitude: 1820.82

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

- `src/algo/blast/unit_tests/api/test_objmgr.hpp` -> **Severity: 4.126** (Embedded: 0.052 * Error Risk: 79.3263%)
- `src/algo/blast/unit_tests/api/ensure_enough_corelib.hpp` -> **Severity: 2.979** (Embedded: 0.0429 * Error Risk: 69.4708%)
- `src/algo/blast/api/blast_setup.hpp` -> **Severity: 2.688** (Embedded: 0.0544 * Error Risk: 49.46%)
- `src/algo/blast/api/blast_objmgr_priv.hpp` -> **Severity: 2.37** (Embedded: 0.0404 * Error Risk: 58.7395%)
- `src/app/blast/blast_app_util.hpp` -> **Severity: 2.152** (Embedded: 0.0234 * Error Risk: 91.9585%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 521.94** (Blast Radius: 27.861 * Doc Risk: 18.7337%)
- `src/algo/blast/unit_tests/api/ensure_enough_corelib.hpp` -> **Severity: 472.004** (Blast Radius: 28.498 * Doc Risk: 16.5627%)
- `src/algo/blast/core/jumper.h` -> **Severity: 401.2** (Blast Radius: 4.012 * Doc Risk: 100.0%)
- `src/algo/blast/api/blast_setup.hpp` -> **Severity: 366.287** (Blast Radius: 30.728 * Doc Risk: 11.9203%)
- `src/algo/blast/gumbel_params/sls_alp_regression.hpp` -> **Severity: 365.696** (Blast Radius: 27.197 * Doc Risk: 13.4462%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
