# ARCHITECTURAL_BRIEF: blast
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ncbi/ncbi-cxx-toolkit-public.git` |
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
| Total Artifacts | 10248 |
| Analyzed Artifacts (Scanned) | 769 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9479 |
| Total LOC | 165356 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 7.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7642 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2332 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3469 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 48 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 310 | 105400 | 40.3% |
| PLAINTEXT | 180 | 1 | 23.4% |
| MAKEFILE | 169 | 1383 | 22.0% |
| C | 88 | 56275 | 11.4% |
| BINARY_THREAT | 8 | 8 | 1.0% |
| MARKDOWN | 5 | 0 | 0.7% |
| SHELL | 4 | 122 | 0.5% |
| PERL | 2 | 2062 | 0.3% |
| BATCH | 1 | 5 | 0.1% |
| XML | 1 | 0 | 0.1% |
| PYTHON | 1 | 100 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.21; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 37%, Large Core Modules 21%, Declarative / Non-Code 16%, State Mutators Files 8%, Many-Argument Workhorses Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 576 | 74.9% |
| Unknown | 9 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 184 | 23.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9479*

**Composition by Extension & Reason:**
- `.cpp`: 1554x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.hpp`: 1206x Excluded: Neighborhood Micro-Mass Limit Exceeded, 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 771x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Embedded Array/Matrix Payload: 10152 commas in 2340 LOC), 1x Excluded (Embedded Array/Matrix Payload: 6283 commas in 1754 LOC)
- `.gz`: 752x Excluded (Explicitly Denied Extension: '.gz')
- `.app`: 659x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.asn`: 546x Excluded: Neighborhood Micro-Mass Limit Exceeded, 29x Unsupported Format (.asn)
- `.txt`: 490x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 396x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.errors`: 363x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 248x Excluded: Neighborhood Micro-Mass Limit Exceeded, 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.lib`: 283x Excluded (Explicitly Denied Extension: '.lib'), 1x Excluded (Explicitly Denied Extension: '.LIB')
- `.aln`: 173x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Monolithic Amalgamation: 38170 LOC exceeds safe regex boundaries), 1x Unsupported Format (.aln)
- `.msvc`: 163x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Unsupported Extension: '.msvc'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 51x Excluded: Neighborhood Micro-Mass Limit Exceeded, 35x Unsupported Format (.ini)
- `.in`: 81x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Statistical Anomaly (Z-Score: -4.86 < -4.75)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.4 | 20.4 | 6.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 46.8 | 63.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 38.1 | 19.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 24.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.9 | 4.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 20.1 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.2 | 20.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 68.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.9 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 52.0 | 69.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 46154 | 350 | 151 | `src/algo/blast/core/hspfilter_mapper.c` |
| cleanup | 281 | 71 | 0 | `src/algo/blast/core/blast_nalookup.c` |
| guards | 9706 | 368 | 35 | `src/algo/blast/blastinput/unit_test/blastinput_unit_test.cpp` |
| danger | 1944 | 199 | 6 | `src/algo/blast/gumbel_params/sls_alp_sim.cpp` |
| concurrency | 28 | 8 | 0 | `src/algo/blast/api/blast_mtlock.cpp` |
| connectivity | 1580 | 192 | 5 | `src/algo/blast/api/blast_options_local_priv.hpp` |
| io | 133 | 11 | 0 | `src/app/blast/get_species_taxids.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 78 | 8 | 0 | `src/algo/blast/core/blast_hspstream.c` |
| time | 4 | 1 | 0 | `src/app/blast/update_blastdb.pl` |
| serialization | 0 | 0 | 0 | - |
| regex | 158 | 9 | 0 | `src/app/blast/legacy_blast.pl` |
| events | 42 | 4 | 0 | `src/algo/blast/core/blast_stat.c` |
| tests | 8 | 3 | 0 | `src/app/blast/cleanup-blastdb-volumes.py` |
| docs | 5335 | 348 | 19 | `src/algo/blast/api/blast_setup.hpp` |
| debt | 600 | 111 | 1 | `src/app/blast/update_blastdb.pl` |
| mutation | 51382 | 473 | 172 | `src/algo/blast/core/blast_gapalign.c` |
| dead_code | 4012 | 350 | 14 | `src/algo/blast/api/blast_options_cxx.cpp` |
| credential | 0 | 0 | 0 | - |
| threat | 312 | 109 | 1 | `src/algo/blast/core/blast_nascan.c` |
| ml_ai | 123 | 20 | 0 | `src/algo/blast/core/blast_stat.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/app/blast/get_species_taxids.sh` (Hits: 67)
- `src/app/blast/cleanup-blastdb-volumes.py` (Hits: 23)
- `src/app/blast/legacy_blast.pl` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Makefile.blast_unit_test.app.unix** (`src/algo/blast/unit_tests/api/Makefile.blast_unit_test.app.unix`) — 47 inbound connections
2. **test_objmgr.hpp** (`src/algo/blast/unit_tests/api/test_objmgr.hpp`) — 40 inbound connections
3. **blast_setup.hpp** (`src/algo/blast/api/blast_setup.hpp`) — 33 inbound connections
4. **blast_objmgr_priv.hpp** (`src/algo/blast/api/blast_objmgr_priv.hpp`) — 31 inbound connections
5. **blast_test_util.hpp** (`src/algo/blast/unit_tests/api/blast_test_util.hpp`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **traceback_unit_test.cpp** (`src/algo/blast/unit_tests/api/traceback_unit_test.cpp`) — 44 outbound dependencies
2. **rmblast_traceback_unit_test.cpp** (`src/algo/blast/unit_tests/api/rmblast_traceback_unit_test.cpp`) — 40 outbound dependencies
3. **pssmcreate_unit_test.cpp** (`src/algo/blast/unit_tests/api/pssmcreate_unit_test.cpp`) — 37 outbound dependencies
4. **blastengine_unit_test.cpp** (`src/algo/blast/unit_tests/api/blastengine_unit_test.cpp`) — 35 outbound dependencies
5. **blastinput_unit_test.cpp** (`src/algo/blast/blastinput/unit_test/blastinput_unit_test.cpp`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_PSIComputePositionExtents` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_psi_priv.c`) -> Impact: **627.5** | LOC: 1791
- `Blast_RedoAlignmentCore_MT` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_kappa.c`) -> Impact: **503.1** | LOC: 942
  * *Intent:* /** * Recompute alignments for each match found by the gapped BLAST * algorithm. */
- `_PSIGetAlignedSequencesForPosition` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_psi_priv.c`) -> Impact: **479.7** | LOC: 1274
- `s_OutOfFrameAlignWithTraceback` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_gapalign.c`) -> Impact: **431.7** | LOC: 598
  * *Intent:* * @param A The query sequence [in] * @param B The subject sequence [in] * @param M Maximal extension length in query [in] * @param N Maximal extension...
- `BlastNaExtendJumper` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/jumper.c`) -> Impact: **410.0** | LOC: 568
  * *Intent:* /* for mapping this may only work if we hash genome and scan reads */
- `x_ProcessOneOption` **(Compute Cores)** (@ `src/algo/blast/api/blast_options_builder.cpp`) -> Impact: **380.5** | LOC: 405
- `Blast_TracebackFromHSPList` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_traceback.c`) -> Impact: **362.2** | LOC: 466
  * *Intent:* */
- `s_BlastEvenGapLinkHSPs` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/link_hsps.c`) -> Impact: **353.5** | LOC: 678
  * *Intent:* /** Perform even gap linking on a list of HSPs * @param program_number The blast program that generated the HSPs [in] * @param hsp_list List of HSPs t...
- `BLAST_GetGappedScore` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_gapalign.c`) -> Impact: **337.0** | LOC: 455
- `CIgBlast::x_FindDJAln` **(Many-Argument Workhorses)** (@ `src/algo/blast/igblast/igblast.cpp`) -> Impact: **303.8** | LOC: 195
  * *Intent:* */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/algo/blast/core` | 77 | 70282.22 | 37.99% | 33.35% |
| `src/algo/blast/api` | 96 | 19101.68 | 20.06% | 64.73% |
| `src/algo/blast/unit_tests/api` | 219 | 13767.66 | 8.81% | 20.89% |
| `src/algo/blast/gumbel_params` | 44 | 10181.34 | 29.51% | 25.24% |
| `src/app/blast` | 65 | 5377.74 | 8.15% | 20.96% |
| `src/algo/blast/composition_adjustment` | 13 | 5168.48 | 27.05% | 27.27% |
| `src/sample/app/deployable_cgi/pkg` | 1 | 5000.0 | 0.0% | 0.0% |
| `src/algo/blast/blastinput` | 24 | 4593.16 | 21.44% | 73.61% |
| `src/algo/blast/format` | 13 | 4501.92 | 34.93% | 56.59% |
| `src/algo/blast/vdb` | 17 | 3159.64 | 24.11% | 29.01% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/algo/blast/api/blast_rps_options.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/local_search.cpp` -> **100.0%** Exposure
- `src/algo/blast/core/blast_program.c` -> **100.0%** Exposure
- `src/algo/blast/unit_tests/api/mockseqsrc1_unit_test.cpp` -> **99.9999%** Exposure
- `src/algo/blast/api/tblastx_options.cpp` -> **99.9995%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/algo/blast/api/blast_options_handle.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_seqalign.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_setup_cxx.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/blast_usage_report.cpp` -> **100.0%** Exposure
- `src/algo/blast/blastinput/blast_input_aux.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/algo/blast/api/blast_options_cxx.cpp` -> **195** Orphaned Functions | **0** Duplicates
- `src/algo/blast/unit_tests/seqdb_reader/seqdb_unit_test.cpp` -> **119** Orphaned Functions | **2** Duplicates
- `src/algo/blast/unit_tests/api/bl2seq_unit_test.cpp` -> **95** Orphaned Functions | **14** Duplicates
- `src/algo/blast/blastinput/unit_test/blastinput_unit_test.cpp` -> **96** Orphaned Functions | **2** Duplicates
- `src/algo/blast/blastinput/blast_args.cpp` -> **97** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

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

### 1. `src/algo/blast/api/blast_node.cpp` (CPP) -> Cumulative Risk: **678.35**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.20)
- **Magnitude:** 229.02 | **LOC:** 323 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9419%), Tech Debt (95.0317%)
- **Heaviest Functions:** `NON_CONST_ITERATE` (Many-Argument Workhorses, Impact: 38.9), `CBlastNodeInputReader::GetQueryBatch` (Compute Cores, Impact: 27.9), `CBlastMasterNode::Processing` (I/O & Config Routines, Impact: 21.1)

### 2. `src/algo/blast/gumbel_params/njn_localmaxstatutil.cpp` (CPP) -> Cumulative Risk: **658.34**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.61)
- **Magnitude:** 516.58 | **LOC:** 556 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.4329%)
- **Heaviest Functions:** `LocalMaxStatUtil::descendingLadderEpochRepeat` (Many-Argument Workhorses, Impact: 138.2), `LocalMaxStatUtil::flatten` (Many-Argument Workhorses, Impact: 49.3), `LocalMaxStatUtil::isLogarithmic` (Compute Cores, Impact: 10.7)

### 3. `src/algo/blast/blastinput/blast_args.cpp` (CPP) -> Cumulative Risk: **656.26**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.38)
- **Magnitude:** 2521.8 | **LOC:** 3844 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8137%), Documentation (93.9655%), Tech Debt (93.7008%)
- **Heaviest Functions:** `CIgBlastArgs::ExtractAlgorithmOptions` (Many-Argument Workhorses, Impact: 106.2), `CBlastDatabaseArgs::ExtractAlgorithmOptions` (Compute Cores, Impact: 106.1), `s_SetCompositionBasedStats` (Many-Argument Workhorses, Impact: 97.1)

### 4. `src/algo/blast/api/cdd_pssm_input.cpp` (CPP) -> Cumulative Risk: **654.95**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.36)
- **Magnitude:** 485.72 | **LOC:** 895 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Documentation (97.4359%), Safety Score (92.1985%)
- **Heaviest Functions:** `CCddInputData::CHit::Subtract` (Compute Cores, Impact: 38.0), `CCddInputData::CHit::IntersectWith` (Many-Argument Workhorses, Impact: 32.1), `CCddInputData::x_ValidateMsa` (I/O & Config Routines, Impact: 13.8)

### 5. `src/algo/blast/core/blast_options.c` (C) -> Cumulative Risk: **654.05**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.17)
- **Magnitude:** 1759.0 | **LOC:** 2015 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9963%), Documentation (94.5946%), Safety Score (88.6284%)
- **Heaviest Functions:** `LookupTableOptionsValidate` (Many-Argument Workhorses, Impact: 131.5), `BlastScoringOptionsValidate` (Many-Argument Workhorses, Impact: 62.6), `s_BlastExtensionScoringOptionsValidate` (Many-Argument Workhorses, Impact: 52.0)

### 6. `src/algo/blast/format/data4xmlformat.cpp` (CPP) -> Cumulative Risk: **653.6**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.80)
- **Magnitude:** 234.2 | **LOC:** 301 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.2042%)
- **Heaviest Functions:** `CCmdLineBlastXMLReportData::x_Init` (Many-Argument Workhorses, Impact: 39.6), `CCmdLineBlastXMLReportData::x_FillScoreMatrix` (Compute Cores, Impact: 39.3), `CCmdLineBlastXMLReportData::GetLambda` (Compute Cores, Impact: 7.9)

### 7. `src/algo/blast/api/blast_options_builder.cpp` (CPP) -> Cumulative Risk: **651.5**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.07)
- **Magnitude:** 836.32 | **LOC:** 819 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Tech Debt (99.9614%), Documentation (92.6829%)
- **Heaviest Functions:** `x_ProcessOneOption` (Compute Cores, Impact: 380.5), `CBlastOptionsBuilder::ComputeProgram` (Compute Cores, Impact: 61.0), `CBlastOptionsBuilder::AdjustProgram` (Many-Argument Workhorses, Impact: 37.0)

### 8. `src/algo/blast/composition_adjustment/nlm_linear_algebra.c` (C) -> Cumulative Risk: **650.13**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.34)
- **Magnitude:** 272.94 | **LOC:** 240 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6867%)
- **Heaviest Functions:** `Nlm_SolveLtriangPosDef` (Many-Argument Workhorses, Impact: 11.3), `Nlm_DenseMatrixNew` (Defensive Guards, Impact: 9.8), `Nlm_FactorLtriangPosDef` (Compute Cores, Impact: 9.8)

### 9. `src/algo/blast/vdb/error_priv.c` (C) -> Cumulative Risk: **650.0**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.46)
- **Magnitude:** 157.26 | **LOC:** 252 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9953%), Safety Score (90.9128%)
- **Heaviest Functions:** `VDBSRC_FormatErrorMsg` (Compute Cores, Impact: 65.2), `VDBSRC_InitErrorMsgWithContext` (Many-Argument Workhorses, Impact: 10.1), `VDBSRC_InitErrorMsg` (Many-Argument Workhorses, Impact: 4.8)

### 10. `src/algo/blast/core/blast_query_info.c` (C) -> Cumulative Risk: **644.43**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.02)
- **Magnitude:** 344.94 | **LOC:** 388 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.9055%), Safety Score (98.7467%)
- **Heaviest Functions:** `Blast_GetOneQueryStructs` (Many-Argument Workhorses, Impact: 30.0), `BSearchContextInfo` (Compute Cores, Impact: 15.1), `BlastQueryInfoGetQueryLength` (Compute Cores, Impact: 14.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/algo/blast/core/blast_gapalign.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6700.64 | **LOC:** 4781 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.6439%), Tech Debt (9.0248%)
**Top Internal Functions/Classes:**
  * `s_OutOfFrameAlignWithTraceback` **(Many-Argument Workhorses)** (Impact: 431.7)
    * *Intent:* * @param A The query sequence [in] * @param B The subject sequence [in] * @param M Maximal extension...
  * `BLAST_GetGappedScore` **(Many-Argument Workhorses)** (Impact: 337.0)
  * `ALIGN_EX` **(Many-Argument Workhorses)** (Impact: 250.0)
  * `s_OutOfFrameGappedAlign` **(Many-Argument Workhorses)** (Impact: 244.3)
    * *Intent:* * @param B The subject sequence [in] * @param M Maximal extension length in query [in] * @param N Ma...
  * `s_RestrictedGappedAlign` **(Many-Argument Workhorses)** (Impact: 204.6)
    * *Intent:* * </PRE> * @param A The query sequence [in] * @param B The subject sequence [in] * @param M Maximal ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 1228 instances
* *Memory Alloc (weighted view):* 39
* *State Mutation (weighted view):* 3847
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 797`, `structural_boundaries: 146`, `args: 54`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 1391`, `dead_code: 4`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 10`, `doc: 39`, `immutability_locks: 78`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` blast_gapalign.h, blast_util.h, greedy_align.h, ncbi_math.h, blast_gapalign_priv.h, blast_hits_priv.h, blast_itree.h, jumper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/jumper.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6285.3 | **LOC:** 4583 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8506%), Tech Debt (17.2513%)
**Top Internal Functions/Classes:**
  * `BlastNaExtendJumper` **(Many-Argument Workhorses)** (Impact: 410.0)
    * *Intent:* /* for mapping this may only work if we hash genome and scan reads */
  * `JumperExtendRightCompressedWithTracebackOptimal` **(Many-Argument Workhorses)** (Impact: 243.9)
    * *Intent:* } /* JumperExtendRightCompressedWithTraceback */
  * `JumperExtendLeftCompressedWithTracebackOptimal` **(Many-Argument Workhorses)** (Impact: 214.1)
    * *Intent:* } /* JumperExtendLeftCompressedWithTraceback */
  * `JumperExtendRightCompressedWithTraceback` **(Many-Argument Workhorses)** (Impact: 210.9)
    * *Intent:* } /* JumperExtendRightCompressed */
  * `DoAnchoredScan` **(Many-Argument Workhorses)** (Impact: 192.9)
    * *Intent:* #define MAX_NUM_MATCHES 10
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 30 instances
* *Amplified Cascading Flux:* 1010 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 3098
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 825`, `structural_boundaries: 252`, `args: 56`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1078`, `dead_code: 33`, `fragile_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 64`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` blast_hits.h, blast_nalookup.h, hspfilter_mapper.h, blast_gapalign_priv.h, jumper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sample/app/deployable_cgi/pkg/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/hspfilter_mapper.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4738.82 | **LOC:** 4942 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.9327%), Tech Debt (22.2007%)
**Top Internal Functions/Classes:**
  * `s_TrimHSP` **(Many-Argument Workhorses)** (Impact: 236.1)
    * *Intent:* #endif /* Trim HSP by a number of bases on query or subject, either from the start or from the end *...
  * `s_FindBestPairs` **(Many-Argument Workhorses)** (Impact: 216.2)
    * *Intent:* /* Find optimal pairs */
  * `s_FindSpliceJunctionsForOverlaps` **(Many-Argument Workhorses)** (Impact: 143.6)
    * *Intent:* */
  * `s_FindBestPath` **(Many-Argument Workhorses)** (Impact: 139.0)
    * *Intent:* /* Find the best scoring chain of HSPs for aligning a single RNA-Seq read to a genome on a single st...
  * `s_FindSpliceJunctionsForGap` **(Many-Argument Workhorses)** (Impact: 136.9)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 729 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 2308
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 852`, `structural_boundaries: 263`, `args: 64`, `func_start: 57`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 850`, `dead_code: 29`, `fragile_debt: 16`, `unreferenced_by_name: 4`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 13`, `doc: 19`, `immutability_locks: 83`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_hits.h, blast_util.h, hspfilter_mapper.h, spliced_hits.h, jumper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_stat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4587.0 | **LOC:** 5271 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.3825%), Tech Debt (23.077%)
**Top Internal Functions/Classes:**
  * `s_GetNuclValuesArray` **(Many-Argument Workhorses)** (Impact: 180.7)
    * *Intent:* * the gap costs, beyond which the ungapped statistics can be applied. * @param reward Match reward s...
  * `BlastScoreBlkNucleotideMatrixRead` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* * * # FREQS A 0.255 C 0.245 G 0.245 T 0.255 * A R G C Y T K M S W N X * A 9 1 -5 -12 -12 -13 -9 -1 -...
  * `Blast_GetMatrixValues` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* * the given matrix. Also obtains arrays of Lambda, K, and H. Any of these fields that * are not requ...
  * `Blast_KarlinBlkNuclGappedCalc` **(Many-Argument Workhorses)** (Impact: 68.2)
  * `NlmKarlinLambdaNR` **(Many-Argument Workhorses)** (Impact: 66.9)
    * *Intent:* * prevents convergence to x = 0, if the function is incorrectly * called with probs[high] == 0). * 3...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 847 instances
* *Memory Alloc (weighted view):* 36
* *State Mutation (weighted view):* 2632
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 669`, `structural_boundaries: 279`, `args: 119`, `func_start: 88`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 938`, `dead_code: 4`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 25`
* *Architecture:* `io: 4`, `api: 56`, `import: 4`
* *Defense:* `safety: 67`, `doc: 119`, `immutability_locks: 74`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` blast_stat.h, ncbi_math.h, blast_psi_priv.h, boost_erf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_hits.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4310.14 | **LOC:** 3892 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.9213%), Tech Debt (20.3844%)
**Top Internal Functions/Classes:**
  * `Blast_HSPListsMerge` **(Many-Argument Workhorses)** (Impact: 128.9)
  * `Blast_HSPReevaluateWithAmbiguitiesGapped` **(Many-Argument Workhorses)** (Impact: 98.5)
  * `Blast_HSPListReevaluateUngapped` **(Many-Argument Workhorses)** (Impact: 89.6)
  * `s_Blast_HSPGetOOFNumIdentitiesAndPositives` **(Many-Argument Workhorses)** (Impact: 82.5)
    * *Intent:* /** Calculate number of identities in an HSP for an out-of-frame alignment. * @param query The query...
  * `s_Blast_HSPGetNumIdentitiesAndPositives` **(Many-Argument Workhorses)** (Impact: 81.0)
    * *Intent:* /** Calculate number of identities in a regular HSP. * @param query The query sequence [in] * @param...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 764 instances
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 2369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 644`, `structural_boundaries: 296`, `args: 118`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 841`, `dead_code: 2`, `unreferenced_by_name: 32`
* *Architecture:* `api: 71`, `import: 8`
* *Defense:* `safety: 16`, `doc: 41`, `immutability_locks: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blast_def.h, blast_hits.h, blast_hspstream.h, blast_util.h, ncbi_math.h, blast_hits_priv.h, blast_itree.h, jumper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_psi_priv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3841.46 | **LOC:** 3177 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9164%), Tech Debt (46.2843%)
**Top Internal Functions/Classes:**
  * `_PSIComputePositionExtents` **(Many-Argument Workhorses)** (Impact: 627.5)
  * `_PSIGetAlignedSequencesForPosition` **(Many-Argument Workhorses)** (Impact: 479.7)
  * `_PSISaveDiagnostics` **(Many-Argument Workhorses)** (Impact: 83.5)
    * *Intent:* /****************************************************************************/
  * `_PSIScaleMatrix` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* */
  * `_PSIComputeFreqRatios` **(Many-Argument Workhorses)** (Impact: 65.0)
    * *Intent:* #define MAX_IND_OBSERVATIONS 400 /**< max number of independent observation for pseudocount calculat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 474 instances
* *State Mutation (weighted view):* 1476
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 462`, `structural_boundaries: 226`, `args: 94`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 4`, `state_mutation: 528`, `dead_code: 6`, `fragile_debt: 7`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `api: 43`, `import: 7`
* *Defense:* `safety: 18`, `doc: 65`, `immutability_locks: 162`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` composition_constants.h, matrix_frequency_data.h, blast_util.h, ncbi_math.h, blast_dynarray.h, blast_posit.h, blast_psi_priv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_kappa.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3218.72 | **LOC:** 3925 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.532%), Tech Debt (8.5831%)
**Top Internal Functions/Classes:**
  * `Blast_RedoAlignmentCore_MT` **(Many-Argument Workhorses)** (Impact: 503.1)
    * *Intent:* /** * Recompute alignments for each match found by the gapped BLAST * algorithm. */
  * `s_BlastScoreBlk_Copy` **(Many-Argument Workhorses)** (Impact: 109.2)
    * *Intent:* * Create a "deep" copy of a BlastScoreBlk structure. * * Non-pointer structure members are copied. P...
  * `s_ExtendRight` **(Many-Argument Workhorses)** (Impact: 63.8)
    * *Intent:* * alignment implemented in NCBI Magic * https://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/Download/D...
  * `s_ExtendLeft` **(Many-Argument Workhorses)** (Impact: 63.5)
    * *Intent:* * mismatches or mismatches or gaps are not followed by two identical matches. * See description for ...
  * `s_SequenceGetProteinRange` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* * * @param self a protein sequence [in] * @param range the range to get [in] * @param seqData the re...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 490 instances
* *Memory Alloc (weighted view):* 55
* *State Mutation (weighted view):* 1606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 128`, `args: 52`, `func_start: 47`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 626`, `dead_code: 17`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 22`
* *Defense:* `safety: 52`, `doc: 71`, `immutability_locks: 85`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` compo_heap.h, matrix_frequency_data.h, nlm_linear_algebra.h, redo_alignment.h, unified_pvalues.h, blast_filter.h, blast_gapalign.h, blast_hits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/igblast/igblast.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2774.32 | **LOC:** 2090 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.841%), Tech Debt (64.3782%)
**Top Internal Functions/Classes:**
  * `CIgBlast::x_FindDJAln` **(Many-Argument Workhorses)** (Impact: 303.8)
    * *Intent:* */
  * `CIgBlast::x_AnnotateDomain` **(Many-Argument Workhorses)** (Impact: 146.9)
    * *Intent:* // query chain type and domain is annotated by germline alignment
  * `ITERATE` **(Many-Argument Workhorses)** (Impact: 137.7)
  * `ITERATE` **(Many-Argument Workhorses)** (Impact: 126.0)
  * `CIgBlast::x_ProcessDGeneResult` **(Many-Argument Workhorses)** (Impact: 99.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 798
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 50`, `args: 70`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 284`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 27`
* *Architecture:* `import: 10`
* *Defense:* `safety: 6`, `doc: 9`, `immutability_locks: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bl2seq.hpp, local_blast.hpp, objmgr_query_data.hpp, remote_blast.hpp, composition_constants.h, igblast.hpp, ncbi_pch.hpp, object_manager.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp_sim.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2708.04 | **LOC:** 4176 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.415%), Tech Debt (15.9161%)
**Top Internal Functions/Classes:**
  * `alp_sim::calculate_main_parameters2m` **(Many-Argument Workhorses)** (Impact: 198.0)
  * `alp_sim::alp_sim` **(Compute Cores)** (Impact: 175.8)
  * `alp_sim::get_minimal_simulation` **(Many-Argument Workhorses)** (Impact: 101.5)
  * `alp_sim::calculate_FSC` **(Many-Argument Workhorses)** (Impact: 95.4)
  * `alp_sim::calculate_C` **(Many-Argument Workhorses)** (Impact: 56.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1608
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 66`, `args: 65`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 832`, `dead_code: 1`, `unreferenced_by_name: 25`
* *Architecture:* `import: 2`
* *Defense:* `safety: 49`, `doc: 1`, `immutability_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ncbi_pch.hpp, sls_alp_sim.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/blastinput/blast_args.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2521.8 | **LOC:** 3844 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.9105%), Tech Debt (93.7008%)
**Top Internal Functions/Classes:**
  * `CIgBlastArgs::ExtractAlgorithmOptions` **(Many-Argument Workhorses)** (Impact: 106.2)
  * `CBlastDatabaseArgs::ExtractAlgorithmOptions` **(Compute Cores)** (Impact: 106.1)
  * `s_SetCompositionBasedStats` **(Many-Argument Workhorses)** (Impact: 97.1)
    * *Intent:* /** * @brief Auxiliary function to set the composition based statistics and smith * waterman options...
  * `CFormattingArgs::ExtractAlgorithmOptions` **(Compute Cores)** (Impact: 89.2)
  * `CFormattingArgs::ParseFormattingString` **(Many-Argument Workhorses)** (Impact: 70.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 224 instances
* *Memory Alloc (weighted view):* 76
* *State Mutation (weighted view):* 736
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 777`, `structural_boundaries: 130`, `args: 205`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 288`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 97`
* *Architecture:* `import: 21`
* *Defense:* `safety: 23`, `doc: 12`, `immutability_locks: 113`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_aux.hpp, blast_exception.hpp, msa_pssm_input.hpp, objmgr_query_data.hpp, pssm_engine.hpp, version.hpp, blast_args.hpp, blast_input.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_nascan.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2457.0 | **LOC:** 3008 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.6462%), Tech Debt (8.4839%)
**Top Internal Functions/Classes:**
  * `s_MBScanSubject_Any` **(Many-Argument Workhorses)** (Impact: 66.0)
    * *Intent:* /** Scan the compressed subject sequence, returning 9-to-12 letter word hits * with arbitrary stride...
  * `s_BlastNaHashLookupRetieveHits` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `s_MBChooseScanSubject` **(Type Conversions)** (Impact: 45.0)
    * *Intent:* /** Choose the most appropriate function to scan through * subject sequences, assuming a megablast l...
  * `s_SmallNaChooseScanSubject` **(Type Conversions)** (Impact: 43.6)
    * *Intent:* /** Choose the most appropriate function to scan through * subject sequences, assuming a small-query...
  * `s_BlastNaScanSubject_Any` **(Many-Argument Workhorses)** (Impact: 43.3)
    * *Intent:* /** Scan the compressed subject sequence, returning 4-to-8 letter word hits * at arbitrary stride. A...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 466 instances
* *State Mutation (weighted view):* 1481
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 181`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 549`, `dead_code: 6`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 43`, `immutability_locks: 98`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_nalookup.h, blast_nascan.h, blast_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/na_ungapped.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2423.7 | **LOC:** 2332 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (60.3799%), Tech Debt (9.7401%)
**Top Internal Functions/Classes:**
  * `s_BlastnDiagHashExtendInitialHit` **(Many-Argument Workhorses)** (Impact: 147.6)
    * *Intent:* * @param q_off The offset in the query sequence [in] * @param s_off The offset in the subject sequen...
  * `JumperNaWordFinder` **(Many-Argument Workhorses)** (Impact: 143.5)
  * `s_BlastnDiagTableExtendInitialHit` **(Many-Argument Workhorses)** (Impact: 139.5)
    * *Intent:* * @param s_off The offset in the subject sequence [in] * @param query_mask Structure containing quer...
  * `s_BlastNaExtendAligned` **(Many-Argument Workhorses)** (Impact: 93.1)
    * *Intent:* * @param num_hits Size of the above arrays [in] * @param word_params Parameters for word extension [...
  * `s_NuclUngappedExtendExact` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* /** Perform ungapped extension of a word hit, using a score * matrix and extending one base at a tim...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 380 instances
* *State Mutation (weighted view):* 1187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 104`, `args: 30`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 427`, `dead_code: 13`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 4`, `doc: 19`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` blast_nalookup.h, blast_nascan.h, blast_util.h, mb_indexed_lookup.h, na_ungapped.h, index_ungapped.h, jumper.h, masksubj.inl
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_nalookup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2218.34 | **LOC:** 2346 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (59.9383%), Tech Debt (11.4737%)
**Top Internal Functions/Classes:**
  * `BlastChooseNaLookupTable` **(Many-Argument Workhorses)** (Impact: 116.7)
    * *Intent:* #include <algo/blast/core/blast_nalookup.h> #include <algo/blast/core/lookup_util.h> #include <algo/...
  * `BlastMBLookupTableNew` **(Many-Argument Workhorses)** (Impact: 85.2)
    * *Intent:* /* Documentation in mb_lookup.h */
  * `s_GetDiscTemplateType` **(Compute Cores)** (Impact: 78.0)
    * *Intent:* */
  * `s_FillDiscMBTable` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* /** Fills in the hashtable and next_pos fields of BlastMBLookupTable* * for the discontiguous case. ...
  * `s_BlastNaHashLookupFinalize` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* /** Pack the data structures comprising a nucleotide lookup table * into their final form * @param t...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 25 instances
* *Amplified Cascading Flux:* 412 instances
* *Memory Alloc (weighted view):* 30
* *State Mutation (weighted view):* 1270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 128`, `args: 36`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 446`, `dead_code: 16`, `unreferenced_by_name: 7`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 34`, `doc: 23`, `immutability_locks: 35`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_encoding.h, blast_filter.h, blast_nalookup.h, blast_util.h, lookup_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/link_hsps.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1890.34 | **LOC:** 1815 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.7224%), Tech Debt (8.5247%)
**Top Internal Functions/Classes:**
  * `s_BlastEvenGapLinkHSPs` **(Many-Argument Workhorses)** (Impact: 353.5)
    * *Intent:* /** Perform even gap linking on a list of HSPs * @param program_number The blast program that genera...
  * `s_BlastUnevenGapLinkHSPs` **(Many-Argument Workhorses)** (Impact: 78.0)
    * *Intent:* * an HSP that produces the best sum e-value when added to the HSP set under * consideration. The nei...
  * `s_LinkedHSPSetsAdmissible` **(Many-Argument Workhorses)** (Impact: 49.3)
    * *Intent:* /** Checks if new candidate HSP is admissible to be linked to a set of HSPs on * the left. The new H...
  * `s_RevCompareHSPsTbx` **(Compute Cores)** (Impact: 28.3)
    * *Intent:* /** Callback used by qsort to sort a list of HSPs (encapsulated in * LinkHSPStruct structures) in or...
  * `BLAST_LinkHsps` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* /* see description in link_hsps.h */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 341 instances
* *State Mutation (weighted view):* 1090
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 137`, `args: 24`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 408`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 9`, `doc: 63`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_util.h, link_hsps.h, blast_hits_priv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_traceback.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1859.42 | **LOC:** 1855 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6868%), Tech Debt (18.9966%)
**Top Internal Functions/Classes:**
  * `Blast_TracebackFromHSPList` **(Many-Argument Workhorses)** (Impact: 362.2)
    * *Intent:* */
  * `BLAST_ComputeTraceback_MT` **(Many-Argument Workhorses)** (Impact: 230.3)
  * `s_RPSComputeTraceback` **(Many-Argument Workhorses)** (Impact: 157.7)
    * *Intent:* * @param rps_info Extra information about RPS database. [in] * @param results Results structure cont...
  * `s_PHITracebackFromHSPList` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* /** Performs traceback alignment for one HSP list in a PHI BLAST search. * @param program_number eBl...
  * `Blast_RunTracebackSearchWithInterrupt` **(Many-Argument Workhorses)** (Impact: 37.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 821
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 64`, `args: 31`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 309`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 11`, `import: 18`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` blast_encoding.h, blast_kappa.h, blast_seqsrc.h, blast_seqsrc_impl.h, blast_setup.h, blast_sw.h, blast_traceback.h, blast_util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/app/blast/legacy_blast.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1804.2 | **LOC:** 1360 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.0267%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_megablast` **(Compute Cores)** (Impact: 154.7)
  * `handle_blastpgp` **(Compute Cores)** (Impact: 128.7)
  * `handle_blastall` **(Compute Cores)** (Impact: 128.2)
    * *Intent:* # Handle the conversion from blastall arguments to the corresponding C++ # binaries
  * `handle_bl2seq` **(Compute Cores)** (Impact: 91.5)
    * *Intent:* # Tested: all conversions should work
  * `handle_seedtop` **(Compute Cores)** (Impact: 76.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 307 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 930
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 108`, `args: 34`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 316`, `dead_code: 5`
* *Architecture:* `io: 14`, `api: 14`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Getopt::Long, Pod::Usage, constant, equivalent, or, sgi, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/format/blast_format.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1790.52 | **LOC:** 2562 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.1949%), Tech Debt (78.9117%)
**Top Internal Functions/Classes:**
  * `CBlastFormat::PrintOneResultSet` **(Many-Argument Workhorses)** (Impact: 207.8)
  * `CBlastFormat::PrintOneResultSet` **(Many-Argument Workhorses)** (Impact: 107.0)
  * `CBlastFormat::PrintPhiResult` **(Many-Argument Workhorses)** (Impact: 83.5)
  * `CBlastFormat::CBlastFormat` **(Many-Argument Workhorses)** (Impact: 75.1)
  * `CBlastFormat::PrintEpilog` **(Compute Cores)** (Impact: 48.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 170 instances
* *Memory Alloc (weighted view):* 38
* *State Mutation (weighted view):* 577
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 89`, `args: 98`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 237`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 5`, `unreferenced_by_name: 34`
* *Architecture:* `import: 20`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` objmgr_query_data.hpp, sseqloc.hpp, blast_stat.h, blast_format.hpp, blastxml2_format.hpp, blastxml_format.hpp, build_archive.hpp, data4xml2format.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1789.72 | **LOC:** 1414 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.4679%), Tech Debt (46.8679%)
**Top Internal Functions/Classes:**
  * `BLAST_TranslateCompressedSequence` **(Many-Argument Workhorses)** (Impact: 120.2)
    * *Intent:* */
  * `BLAST_GetAllTranslations` **(Many-Argument Workhorses)** (Impact: 61.3)
  * `BlastProgram2Number` **(Compute Cores)** (Impact: 45.0)
  * `Blast_GetPartialTranslation` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `BLAST_ContextToFrame` **(Compute Cores)** (Impact: 36.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 332 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 1080
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 115`, `args: 39`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 416`, `dead_code: 1`, `unreferenced_by_name: 26`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `safety: 9`, `doc: 8`, `immutability_locks: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` blast_filter.h, blast_stat.h, blast_util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_options.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1759.0 | **LOC:** 2015 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (64.9578%), Tech Debt (76.2348%)
**Top Internal Functions/Classes:**
  * `LookupTableOptionsValidate` **(Many-Argument Workhorses)** (Impact: 131.5)
  * `BlastScoringOptionsValidate` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `s_BlastExtensionScoringOptionsValidate` **(Many-Argument Workhorses)** (Impact: 52.0)
    * *Intent:* /** Checks that the extension and scoring options are consistent with each other * @param program_nu...
  * `BLAST_ValidateOptions` **(Many-Argument Workhorses)** (Impact: 51.3)
  * `BLAST_GetSuggestedThreshold` **(Compute Cores)** (Impact: 43.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 166 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 513
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 459`, `structural_boundaries: 219`, `args: 78`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 181`, `dead_code: 2`, `planned_debt: 3`, `unreferenced_by_name: 36`
* *Architecture:* `api: 71`, `import: 7`
* *Defense:* `safety: 18`, `doc: 10`, `immutability_locks: 47`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` composition_constants.h, blast_filter.h, blast_options.h, blast_stat.h, blast_util.h, hspfilter_besthit.h, hspfilter_collector.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/unit_tests/seqdb_reader/seqdb_unit_test.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1724.82 | **LOC:** 4617 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.5946%), Tech Debt (77.7104%)
**Top Internal Functions/Classes:**
  * `GiListOidRange` **(Compute Cores)** (Impact: 38.1)
  * `OidRanges` **(Compute Cores)** (Impact: 32.6)
  * `s_TestMaskingLimits` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `s_MaskingTest` **(Compute Cores)** (Impact: 29.7)
  * `ComplexComputedList` **(Compute Cores)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 230 instances
* *Memory Alloc (weighted view):* 27
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 54`, `args: 285`, `func_start: 163`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 326`, `duplicate_logic: 2`, `unreferenced_by_name: 119`
* *Architecture:* `api: 6`, `import: 17`
* *Defense:* `safety: 26`, `doc: 7`, `immutability_locks: 80`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` algorithm, chrono, cmath, ncbifile.hpp, test_boost.hpp, ncbi_pch.hpp, defline_extra.hpp, seq__.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_engine.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1655.76 | **LOC:** 1797 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.968%), Tech Debt (11.7805%)
**Top Internal Functions/Classes:**
  * `BLAST_PreliminarySearchEngine` **(Many-Argument Workhorses)** (Impact: 213.1)
  * `s_BlastSearchEngineCore` **(Many-Argument Workhorses)** (Impact: 204.7)
    * *Intent:* * @param word_params Initial word finding and ungapped extension * parameters [in] * @param ext_para...
  * `s_BlastSearchEngineOneContext` **(Many-Argument Workhorses)** (Impact: 132.7)
    * *Intent:* * @param word_params Initial word finding and ungapped extension * parameters [in] * @param ext_para...
  * `s_BlastSetUpAuxStructures` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* /** Setup of the auxiliary BLAST structures; * also calculates internally used parameters from optio...
  * `s_RPSPreliminarySearchEngine` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* * @param word_params Parameters for processing initial word hits [in] * @param ext_params Parameters...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 694
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 71`, `args: 24`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 262`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 21`
* *Defense:* `safety: 2`, `doc: 46`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` aa_ungapped.h, blast_aalookup.h, blast_aascan.h, blast_engine.h, blast_gapalign.h, blast_nalookup.h, blast_nascan.h, blast_parameters.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/api/blast_seqalign.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1599.86 | **LOC:** 2152 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.8121%), Tech Debt (17.6196%)
**Top Internal Functions/Classes:**
  * `s_OOFBlastHSP2SeqAlign` **(Many-Argument Workhorses)** (Impact: 137.8)
    * *Intent:* /// This function is used for out-of-frame traceback conversion /// Converts an OOF editing script c...
  * `s_CollectSeqAlignData` **(Many-Argument Workhorses)** (Impact: 73.9)
    * *Intent:* /// Note that even though the edit_block is passed in, data for seqalign is /// collected from the e...
  * `MakeSplicedSeg` **(Many-Argument Workhorses)** (Impact: 64.4)
    * *Intent:* #endif
  * `s_BlastHSP2SeqAlign` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* /// Converts a traceback editing block to a Seq-align, provided the 2 sequence /// identifiers. /// ...
  * `BlastHitList2SeqAlign_OMF` **(Many-Argument Workhorses)** (Impact: 53.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 212 instances
* *State Mutation (weighted view):* 695
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 53`, `args: 51`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `state_mutation: 271`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 4`
* *Architecture:* `import: 13`
* *Defense:* `doc: 182`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jumper.h, blast_aux.hpp, query_data.hpp, algorithm, blast_seqalign.hpp, ncbi_pch.hpp, Object_id.hpp, User_object.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/api/blast_setup_cxx.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1566.24 | **LOC:** 1776 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.8458%), Tech Debt (52.2507%)
**Top Internal Functions/Classes:**
  * `SetupQueries_OMF` **(Many-Argument Workhorses)** (Impact: 96.1)
  * `SetupQueryInfo_OMF` **(Many-Argument Workhorses)** (Impact: 82.1)
  * `s_SeqLoc2MaskedSubjRanges` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `SetupSubjects_OMF` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `CBlastQueryFilteredFrames::x_VerifyFrame` **(Compute Cores)** (Impact: 44.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 204 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 640
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 68`, `args: 73`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 232`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 17`
* *Architecture:* `import: 11`
* *Defense:* `safety: 12`, `doc: 46`, `immutability_locks: 42`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_options.hpp, blast_setup.h, blast_util.h, gencode_singleton.h, blast_setup.hpp, metareg.hpp, ncbiapp.hpp, ncbi_pch.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/api/remote_blast.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1533.42 | **LOC:** 2699 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.8251%), Tech Debt (96.4057%)
**Top Internal Functions/Classes:**
  * `ITERATE` **(Compute Cores)** (Impact: 37.5)
  * `CRemoteBlast::x_PollUntilDone` **(Compute Cores)** (Impact: 34.2)
    * *Intent:* // not know how long it has been since the request was submitted. In // this case, we check the resu...
  * `CRemoteBlast::x_SearchErrors` **(Compute Cores)** (Impact: 29.3)
  * `ExtractBlast4Request` **(Compute Cores)** (Impact: 29.2)
  * `CRemoteBlast::GetResultSet` **(I/O & Config Routines)** (Impact: 23.8)
    * *Intent:* /// Submit the search and return the results. /// @return Search results.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 163 instances
* *Memory Alloc (weighted view):* 56
* *State Mutation (weighted view):* 547
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 183`, `args: 165`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 221`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 72`
* *Architecture:* `import: 25`
* *Defense:* `safety: 22`, `doc: 16`, `immutability_locks: 74`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blast_options_builder.hpp, objmgr_query_data.hpp, remote_blast.hpp, search_strategy.hpp, ncbi_system.hpp, ncbitime.hpp, stream_utils.hpp, ncbi_pch.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/algo/blast/unit_tests/api/remote_blast_unit_test.cpp` -> Churn: **100.0%** | Cog Load: 31.8096% | Debt: 97.5353%
- `src/algo/blast/api/blast_node.cpp` -> Churn: **75.66%** | Cog Load: 46.1315% | Debt: 95.0317%
- `src/algo/blast/api/rps_aux.cpp` -> Churn: **75.66%** | Cog Load: 19.9883% | Debt: 99.0093%
- `src/algo/blast/core/blast_filter.c` -> Churn: **59.44%** | Cog Load: 58.2727% | Debt: 17.8319%
- `src/algo/blast/core/blast_nalookup.c` -> Churn: **52.48%** | Cog Load: 59.9383% | Debt: 11.4737%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/algo/blast/core/blast_gapalign.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 6700.64
- `src/algo/blast/core/hspfilter_mapper.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 4738.82
- `src/algo/blast/core/blast_stat.c` -> **Christiam Camacho** (100.0% isolated ownership) | Magnitude: 4587.0
- `src/algo/blast/blastinput/blast_args.cpp` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 2521.8
- `src/algo/blast/core/na_ungapped.c` -> **Amelia Fong** (100.0% isolated ownership) | Magnitude: 2423.7

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/algo/blast/gumbel_params/njn_matrix.hpp` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9996%)
- `src/algo/blast/api/blast_memento_priv.hpp` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.6669%)
- `src/algo/blast/gumbel_params/njn_memutil.hpp` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 93.5798%)
- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9992%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/algo/blast/api/blast_setup.hpp` -> **Severity: 2.302** (Embedded: 0.0544 * Error Risk: 42.3503%)
- `src/app/blast/blast_app_util.hpp` -> **Severity: 1.346** (Embedded: 0.0234 * Error Risk: 57.5069%)
- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 1.242** (Embedded: 0.0142 * Error Risk: 87.743%)
- `src/algo/blast/gumbel_params/njn_ioutil.hpp` -> **Severity: 0.938** (Embedded: 0.01 * Error Risk: 93.9509%)
- `src/algo/blast/api/blast_memento_priv.hpp` -> **Severity: 0.776** (Embedded: 0.0092 * Error Risk: 83.8686%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/algo/blast/unit_tests/api/ensure_enough_corelib.hpp` -> **Severity: 2738.4** (Blast Radius: 27.384 * Doc Risk: 100.0%)
- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 2663.2** (Blast Radius: 26.632 * Doc Risk: 100.0%)
- `src/algo/blast/gumbel_params/sls_alp_regression.hpp` -> **Severity: 2593.6** (Blast Radius: 25.936 * Doc Risk: 100.0%)
- `src/app/blast/blast_app_util.hpp` -> **Severity: 997.3** (Blast Radius: 9.973 * Doc Risk: 100.0%)
- `src/algo/blast/gumbel_params/njn_ioutil.hpp` -> **Severity: 528.5** (Blast Radius: 5.285 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
