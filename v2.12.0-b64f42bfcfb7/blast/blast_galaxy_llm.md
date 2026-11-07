# ARCHITECTURAL_BRIEF: blast
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ncbi/ncbi-cxx-toolkit-public.git` |
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
- **Scope:** 764 analyzed artifact(s), 168961 LOC.
- **Load-bearing artifact:** `src/algo/blast/unit_tests/api/Makefile.blast_unit_test.app.unix` -- 47 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/algo/blast/unit_tests/api/traceback_unit_test.cpp` -- pulls in 44 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/algo/blast/core/blast_gapalign.c` at magnitude 6698.44 (structural weight, not risk).
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
| Total Artifacts | 10244 |
| Analyzed Artifacts (Scanned) | 764 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9480 |
| Total LOC | 168961 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 7.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5355 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0043 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.345 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 38 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 310 | 105400 | 40.6% |
| PLAINTEXT | 180 | 1 | 23.6% |
| MAKEFILE | 169 | 1383 | 22.1% |
| C | 90 | 59884 | 11.8% |
| MARKDOWN | 5 | 0 | 0.7% |
| SHELL | 4 | 122 | 0.5% |
| PERL | 2 | 2062 | 0.3% |
| YAML | 1 | 4 | 0.1% |
| BATCH | 1 | 5 | 0.1% |
| XML | 1 | 0 | 0.1% |
| PYTHON | 1 | 100 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 762 |
| cp1252 | cp1252-fallback | 1 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Large Core Modules (3) 19%, Declarative / Non-Code 16%, State Mutators Files 8%, Many-Argument Workhorses Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 579 | 75.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 184 | 24.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9480*

**Composition by Extension & Reason:**
- `.cpp`: 1554x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.hpp`: 1212x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 771x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.gz`: 752x Excluded (Explicitly Denied Extension: '.gz')
- `.app`: 659x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.asn`: 546x Excluded: Neighborhood Micro-Mass Limit Exceeded, 29x Unsupported Format (.asn)
- `.txt`: 490x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 397x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.errors`: 363x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 248x Excluded: Neighborhood Micro-Mass Limit Exceeded, 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.lib`: 283x Excluded (Explicitly Denied Extension: '.lib'), 1x Excluded (Explicitly Denied Extension: '.LIB')
- `.aln`: 173x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Unsupported Format (.aln)
- `.msvc`: 163x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (Unsupported Extension: '.msvc'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 51x Excluded: Neighborhood Micro-Mass Limit Exceeded, 35x Unsupported Format (.ini)
- `.in`: 81x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Statistical Anomaly (Z-Score: -4.86 < -4.75)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.1 | 20.3 | 6.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.6 | 37.7 | 52.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 36.4 | 18.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 24.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.7 | 5.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 20.1 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.7 | 22.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.9 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.6 | 70.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5213 | 293 | 19 | `src/algo/blast/core/blast_stat.c` |
| cleanup | 281 | 71 | 0 | `src/algo/blast/core/blast_nalookup.c` |
| guards | 9776 | 370 | 36 | `src/algo/blast/blastinput/unit_test/blastinput_unit_test.cpp` |
| danger | 1972 | 201 | 6 | `src/algo/blast/gumbel_params/sls_alp_sim.cpp` |
| concurrency | 28 | 8 | 0 | `src/algo/blast/api/blast_mtlock.cpp` |
| connectivity | 1599 | 194 | 6 | `src/algo/blast/api/blast_options_local_priv.hpp` |
| io | 133 | 11 | 0 | `src/app/blast/get_species_taxids.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 78 | 8 | 0 | `src/algo/blast/core/blast_hspstream.c` |
| time | 4 | 1 | 0 | `src/app/blast/update_blastdb.pl` |
| serialization | 0 | 0 | 0 | - |
| regex | 158 | 9 | 0 | `src/app/blast/legacy_blast.pl` |
| events | 42 | 4 | 0 | `src/algo/blast/core/blast_stat.c` |
| tests | 8 | 3 | 0 | `src/app/blast/cleanup-blastdb-volumes.py` |
| docs | 5399 | 350 | 19 | `src/algo/blast/api/blast_setup.hpp` |
| debt | 603 | 112 | 2 | `src/app/blast/update_blastdb.pl` |
| mutation | 51779 | 475 | 183 | `src/algo/blast/core/blast_gapalign.c` |
| dead_code | 3694 | 336 | 12 | `src/algo/blast/api/blast_options_cxx.cpp` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 125 | 21 | 0 | `src/algo/blast/core/blast_stat.c` |
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
2. **blast_util.c** (`src/algo/blast/core/blast_util.c`) — 47 inbound connections
3. **blast_program.c** (`src/algo/blast/core/blast_program.c`) — 43 inbound connections
4. **test_objmgr.hpp** (`src/algo/blast/unit_tests/api/test_objmgr.hpp`) — 40 inbound connections
5. **blast_options.c** (`src/algo/blast/core/blast_options.c`) — 38 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **traceback_unit_test.cpp** (`src/algo/blast/unit_tests/api/traceback_unit_test.cpp`) — 44 outbound dependencies
2. **rmblast_traceback_unit_test.cpp** (`src/algo/blast/unit_tests/api/rmblast_traceback_unit_test.cpp`) — 40 outbound dependencies
3. **pssmcreate_unit_test.cpp** (`src/algo/blast/unit_tests/api/pssmcreate_unit_test.cpp`) — 37 outbound dependencies
4. **blastengine_unit_test.cpp** (`src/algo/blast/unit_tests/api/blastengine_unit_test.cpp`) — 35 outbound dependencies
5. **blastinput_unit_test.cpp** (`src/algo/blast/blastinput/unit_test/blastinput_unit_test.cpp`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_PSIComputePositionExtents` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_psi_priv.c`) -> Impact: **617.5** | LOC: 1791
- `Blast_RedoAlignmentCore_MT` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_kappa.c`) -> Impact: **491.1** | LOC: 942
  * *Intent:* /** * Recompute alignments for each match found by the gapped BLAST * algorithm. */
- `_PSIGetAlignedSequencesForPosition` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_psi_priv.c`) -> Impact: **471.7** | LOC: 1274
- `s_OutOfFrameAlignWithTraceback` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_gapalign.c`) -> Impact: **431.7** | LOC: 598
  * *Intent:* * @param A The query sequence [in] * @param B The subject sequence [in] * @param M Maximal extension length in query [in] * @param N Maximal extension...
- `BlastNaExtendJumper` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/jumper.c`) -> Impact: **410.0** | LOC: 568
  * *Intent:* /* for mapping this may only work if we hash genome and scan reads */
- `x_ProcessOneOption` **(Many-Argument Workhorses)** (@ `src/algo/blast/api/blast_options_builder.cpp`) -> Impact: **373.6** | LOC: 405
- `Blast_TracebackFromHSPList` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_traceback.c`) -> Impact: **362.2** | LOC: 466
  * *Intent:* */
- `s_BlastEvenGapLinkHSPs` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/link_hsps.c`) -> Impact: **353.5** | LOC: 678
  * *Intent:* /** Perform even gap linking on a list of HSPs * @param program_number The blast program that generated the HSPs [in] * @param hsp_list List of HSPs t...
- `BLAST_GetGappedScore` **(Many-Argument Workhorses)** (@ `src/algo/blast/core/blast_gapalign.c`) -> Impact: **337.0** | LOC: 455
- `CIgBlast::x_FindDJAln` **(Many-Argument Workhorses)** (@ `src/algo/blast/igblast/igblast.cpp`) -> Impact: **303.8** | LOC: 195
  * *Intent:* */

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/algo/blast/core` | 79 | 71275.0 | 37.33% | 30.47% |
| `src/algo/blast/api` | 96 | 18928.68 | 19.74% | 62.16% |
| `src/algo/blast/unit_tests/api` | 219 | 13686.46 | 8.69% | 19.6% |
| `src/algo/blast/gumbel_params` | 44 | 10143.04 | 29.39% | 22.92% |
| `src/app/blast` | 65 | 5330.34 | 7.92% | 19.51% |
| `src/algo/blast/composition_adjustment` | 13 | 5159.68 | 26.99% | 25.85% |
| `src/sample/app/deployable_cgi/pkg` | 1 | 5000.0 | 0.0% | 0.0% |
| `src/algo/blast/format` | 13 | 4478.72 | 34.82% | 54.93% |
| `src/algo/blast/blastinput` | 24 | 4383.86 | 18.87% | 71.3% |
| `src/algo/blast/vdb` | 17 | 3134.94 | 23.97% | 27.69% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/algo/blast/api/blast_rps_options.cpp` -> **100.0%** Exposure
- `src/algo/blast/api/local_search.cpp` -> **100.0%** Exposure
- `src/algo/blast/core/blast_program.c` -> **100.0%** Exposure
- `src/algo/blast/unit_tests/api/mockseqsrc1_unit_test.cpp` -> **99.9999%** Exposure
- `src/algo/blast/api/tblastx_options.cpp` -> **99.9987%** Exposure
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
- **Unknown Dependencies:** `3348` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/algo/blast/core/blast_gapalign.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.226)
- **Top Global Matches:** file_cluster_3: 8.226, file_cluster_8: 16.352, file_cluster_6: 29.205
- **Magnitude:** 6698.44 | **LOC:** 4781 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **8**; blast radius 1.351; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 52.8302% of unit weight undocumented
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
* *Structure:* `branch: 796`, `structural_boundaries: 146`, `args: 54`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 1391`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 10`, `doc: 39`, `immutability_locks: 78`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.351
  * `Choke Point (Betweenness):` 0.001078 | `Ripple Effect (Closeness):` 0.061927
  * `Imports (Out-Degree: 14):` blast_gapalign.h, blast_util.h, greedy_align.h, ncbi_math.h, blast_gapalign_priv.h, blast_hits_priv.h, blast_itree.h, jumper.h
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/jumper.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.362)
- **Top Global Matches:** file_cluster_8: 5.362, file_cluster_6: 15.796, file_cluster_3: 20.879
- **Magnitude:** 6283.3 | **LOC:** 4583 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 2.29; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Amplified Cascading Flux:* 1009 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 3096
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 821`, `structural_boundaries: 252`, `args: 56`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1078`, `fragile_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 64`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.004228 | `Ripple Effect (Closeness):` 0.084147
  * `Imports (Out-Degree: 9):` blast_hits.h, blast_nalookup.h, hspfilter_mapper.h, blast_gapalign_priv.h, jumper.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/sample/app/deployable_cgi/pkg/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.648
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/hspfilter_mapper.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.86)
- **Top Global Matches:** file_cluster_8: 6.86, file_cluster_3: 17.976, file_cluster_6: 18.611
- **Magnitude:** 4694.92 | **LOC:** 4942 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.939; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (68.6%)
- **Documentation Coverage:** 84.127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `s_TrimHSP` **(Many-Argument Workhorses)** (Impact: 230.1)
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
* *Amplified Cascading Flux:* 724 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 2298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 835`, `structural_boundaries: 263`, `args: 64`, `func_start: 57`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 850`, `dead_code: 2`, `fragile_debt: 16`, `unreferenced_by_name: 4`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 13`, `doc: 19`, `immutability_locks: 83`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.000528 | `Ripple Effect (Closeness):` 0.066345
  * `Imports (Out-Degree: 6):` blast_hits.h, blast_util.h, hspfilter_mapper.h, spliced_hits.h, jumper.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_stat.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.68)
- **Top Global Matches:** file_cluster_4: 6.68, file_cluster_6: 7.913, file_cluster_12: 14.069
- **Magnitude:** 4575.2 | **LOC:** 5271 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **4**; blast radius 8.219; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (45.3%)
- **Documentation Coverage:** 62.4113% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `s_GetNuclValuesArray` **(Many-Argument Workhorses)** (Impact: 180.7)
    * *Intent:* * the gap costs, beyond which the ungapped statistics can be applied. * @param reward Match reward s...
  * `BlastScoreBlkNucleotideMatrixRead` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* * * # FREQS A 0.255 C 0.245 G 0.245 T 0.255 * A R G C Y T K M S W N X * A 9 1 -5 -12 -12 -13 -9 -1 -...
  * `Blast_GetMatrixValues` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* * the given matrix. Also obtains arrays of Lambda, K, and H. Any of these fields that * are not requ...
  * `NlmKarlinLambdaNR` **(Many-Argument Workhorses)** (Impact: 66.9)
    * *Intent:* * prevents convergence to x = 0, if the function is incorrectly * called with probs[high] == 0). * 3...
  * `BlastScoreBlkProteinMatrixRead` **(Many-Argument Workhorses)** (Impact: 65.9)
    * *Intent:* /** Read in the matrix from the FILE *fp. * This function ASSUMES that the matrices are in the ncbis...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 846 instances
* *Memory Alloc (weighted view):* 36
* *State Mutation (weighted view):* 2630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 664`, `structural_boundaries: 279`, `args: 119`, `func_start: 88`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 938`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 25`
* *Architecture:* `io: 4`, `api: 56`, `import: 4`
* *Defense:* `safety: 67`, `doc: 119`, `immutability_locks: 74`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.219
  * `Choke Point (Betweenness):` 0.004037 | `Ripple Effect (Closeness):` 0.111443
  * `Imports (Out-Degree: 9):` blast_stat.h, ncbi_math.h, blast_psi_priv.h, boost_erf.h
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_hits.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.825)
- **Top Global Matches:** file_cluster_6: 5.825, file_cluster_4: 7.194, file_cluster_16: 15.447
- **Magnitude:** 4302.94 | **LOC:** 3892 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **8**; blast radius 4.793; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.9%)
- **Documentation Coverage:** 76.1628% of unit weight undocumented
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
* *Amplified Cascading Flux:* 763 instances
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 2367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 296`, `args: 118`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 841`, `unreferenced_by_name: 32`
* *Architecture:* `api: 71`, `import: 8`
* *Defense:* `safety: 16`, `doc: 41`, `immutability_locks: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.793
  * `Choke Point (Betweenness):` 0.001952 | `Ripple Effect (Closeness):` 0.072498
  * `Imports (Out-Degree: 12):` blast_def.h, blast_hits.h, blast_hspstream.h, blast_util.h, ncbi_math.h, blast_hits_priv.h, blast_itree.h, jumper.h
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_psi_priv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.022)
- **Top Global Matches:** file_cluster_6: 6.022, file_cluster_4: 9.79, file_cluster_8: 16.001
- **Magnitude:** 3806.06 | **LOC:** 3177 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 2.965; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (63.8%)
- **Documentation Coverage:** 69.3694% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_PSIComputePositionExtents` **(Many-Argument Workhorses)** (Impact: 617.5)
  * `_PSIGetAlignedSequencesForPosition` **(Many-Argument Workhorses)** (Impact: 471.7)
  * `_PSISaveDiagnostics` **(Many-Argument Workhorses)** (Impact: 83.5)
    * *Intent:* /****************************************************************************/
  * `_PSIScaleMatrix` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* */
  * `_PSIComputeFreqRatios` **(Many-Argument Workhorses)** (Impact: 65.0)
    * *Intent:* #define MAX_IND_OBSERVATIONS 400 /**< max number of independent observation for pseudocount calculat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 469 instances
* *State Mutation (weighted view):* 1466
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 454`, `structural_boundaries: 226`, `args: 94`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 4`, `state_mutation: 528`, `fragile_debt: 7`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `api: 43`, `import: 7`
* *Defense:* `safety: 18`, `doc: 65`, `immutability_locks: 162`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.965
  * `Choke Point (Betweenness):` 0.001919 | `Ripple Effect (Closeness):` 0.081849
  * `Imports (Out-Degree: 11):` composition_constants.h, matrix_frequency_data.h, blast_util.h, ncbi_math.h, blast_dynarray.h, blast_posit.h, blast_psi_priv.h
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_kappa.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.579)
- **Top Global Matches:** file_cluster_4: 6.579, file_cluster_6: 8.569, file_cluster_9: 13.306
- **Magnitude:** 3206.72 | **LOC:** 3925 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 0.705; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%), Complexity Load (formerly Cognitive Load) (51.4%)
- **Documentation Coverage:** 5.1948% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Blast_RedoAlignmentCore_MT` **(Many-Argument Workhorses)** (Impact: 491.1)
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
* *Structure:* `branch: 433`, `structural_boundaries: 128`, `args: 52`, `func_start: 47`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 626`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 22`
* *Defense:* `safety: 52`, `doc: 71`, `immutability_locks: 85`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.705
  * `Choke Point (Betweenness):` 0.000152 | `Ripple Effect (Closeness):` 0.004928
  * `Imports (Out-Degree: 31):` compo_heap.h, matrix_frequency_data.h, nlm_linear_algebra.h, redo_alignment.h, unified_pvalues.h, blast_filter.h, blast_gapalign.h, blast_hits.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/algo/blast/igblast/igblast.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.046)
- **Top Global Matches:** file_cluster_6: 6.046, file_cluster_8: 11.932, file_cluster_4: 13.122
- **Magnitude:** 2774.32 | **LOC:** 2090 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.648; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.648
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bl2seq.hpp, local_blast.hpp, objmgr_query_data.hpp, remote_blast.hpp, composition_constants.h, igblast.hpp, ncbi_pch.hpp, object_manager.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/gumbel_params/sls_alp_sim.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.629)
- **Top Global Matches:** file_cluster_8: 8.629, file_cluster_6: 8.974, file_cluster_4: 17.195
- **Magnitude:** 2702.44 | **LOC:** 4176 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.797; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%), Complexity Load (formerly Cognitive Load) (59.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alp_sim::calculate_main_parameters2m` **(Many-Argument Workhorses)** (Impact: 198.0)
  * `alp_sim::alp_sim` **(Many-Argument Workhorses)** (Impact: 175.8)
  * `alp_sim::get_minimal_simulation` **(Many-Argument Workhorses)** (Impact: 95.9)
  * `alp_sim::calculate_FSC` **(Many-Argument Workhorses)** (Impact: 95.4)
  * `alp_sim::calculate_C` **(Many-Argument Workhorses)** (Impact: 56.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1608
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 66`, `args: 65`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 832`, `unreferenced_by_name: 25`
* *Architecture:* `import: 2`
* *Defense:* `safety: 49`, `doc: 1`, `immutability_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.797
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.002356
  * `Imports (Out-Degree: 6):` ncbi_pch.hpp, sls_alp_sim.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_nascan.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.891)
- **Top Global Matches:** file_cluster_4: 8.891, file_cluster_6: 10.873, file_cluster_12: 13.281
- **Magnitude:** 2449.0 | **LOC:** 3008 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 0.778; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.5%)
- **Documentation Coverage:** 4.8077% of unit weight undocumented
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
* *Amplified Cascading Flux:* 462 instances
* *State Mutation (weighted view):* 1473
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 181`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 549`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 43`, `immutability_locks: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004712
  * `Imports (Out-Degree: 0):` blast_nalookup.h, blast_nascan.h, blast_util.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/na_ungapped.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.531)
- **Top Global Matches:** file_cluster_8: 8.531, file_cluster_3: 18.782, file_cluster_6: 19.236
- **Magnitude:** 2423.7 | **LOC:** 2332 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.756; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.4%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 427`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 4`, `doc: 19`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.756
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.00409
  * `Imports (Out-Degree: 10):` blast_nalookup.h, blast_nascan.h, blast_util.h, mb_indexed_lookup.h, na_ungapped.h, index_ungapped.h, jumper.h, masksubj.inl
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/algo/blast/blastinput/blast_args.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.646)
- **Top Global Matches:** file_cluster_4: 6.646, file_cluster_6: 7.93, file_cluster_15: 13.511
- **Magnitude:** 2345.2 | **LOC:** 3844 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **21**; blast radius 2.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (93.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.6%)
- **Documentation Coverage:** 93.9655% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CIgBlastArgs::ExtractAlgorithmOptions` **(Many-Argument Workhorses)** (Impact: 102.7)
  * `CBlastDatabaseArgs::ExtractAlgorithmOptions` **(Many-Argument Workhorses)** (Impact: 100.9)
  * `s_SetCompositionBasedStats` **(Many-Argument Workhorses)** (Impact: 94.9)
    * *Intent:* /** * @brief Auxiliary function to set the composition based statistics and smith * waterman options...
  * `CFormattingArgs::ExtractAlgorithmOptions` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `CFormattingArgs::ParseFormattingString` **(Many-Argument Workhorses)** (Impact: 70.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 220 instances
* *Memory Alloc (weighted view):* 76
* *State Mutation (weighted view):* 728
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 671`, `structural_boundaries: 130`, `args: 205`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 288`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 97`
* *Architecture:* `import: 21`
* *Defense:* `safety: 23`, `doc: 12`, `immutability_locks: 113`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.662
  * `Choke Point (Betweenness):` 0.00065 | `Ripple Effect (Closeness):` 0.01731
  * `Imports (Out-Degree: 9):` blast_aux.hpp, blast_exception.hpp, msa_pssm_input.hpp, objmgr_query_data.hpp, pssm_engine.hpp, version.hpp, blast_args.hpp, blast_input.hpp...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_nalookup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.276)
- **Top Global Matches:** file_cluster_8: 6.276, file_cluster_6: 11.455, file_cluster_4: 20.202
- **Magnitude:** 2211.64 | **LOC:** 2346 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 1.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.8%)
- **Documentation Coverage:** 61.9048% of unit weight undocumented
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
* *Structure:* `branch: 339`, `structural_boundaries: 128`, `args: 36`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 446`, `dead_code: 3`, `unreferenced_by_name: 7`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 34`, `doc: 23`, `immutability_locks: 35`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.111
  * `Choke Point (Betweenness):` 0.000686 | `Ripple Effect (Closeness):` 0.06602
  * `Imports (Out-Degree: 7):` blast_encoding.h, blast_filter.h, blast_nalookup.h, blast_util.h, lookup_util.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/link_hsps.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.239)
- **Top Global Matches:** file_cluster_6: 7.239, file_cluster_4: 9.86, file_cluster_9: 15.915
- **Magnitude:** 1890.34 | **LOC:** 1815 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 0.764; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (35.7%)
- **Documentation Coverage:** 9.0909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `s_BlastEvenGapLinkHSPs` **(Many-Argument Workhorses)** (Impact: 353.5)
    * *Intent:* /** Perform even gap linking on a list of HSPs * @param program_number The blast program that genera...
  * `s_BlastUnevenGapLinkHSPs` **(Many-Argument Workhorses)** (Impact: 78.0)
    * *Intent:* * an HSP that produces the best sum e-value when added to the HSP set under * consideration. The nei...
  * `s_LinkedHSPSetsAdmissible` **(Many-Argument Workhorses)** (Impact: 49.3)
    * *Intent:* /** Checks if new candidate HSP is admissible to be linked to a set of HSPs on * the left. The new H...
  * `s_RevCompareHSPsTbx` **(Stateful Encapsulated Methods)** (Impact: 28.3)
    * *Intent:* /** Callback used by qsort to sort a list of HSPs (encapsulated in * LinkHSPStruct structures) in or...
  * `BLAST_LinkHsps` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* /* see description in link_hsps.h */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 341 instances
* *State Mutation (weighted view):* 1090
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 137`, `args: 24`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 408`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 9`, `doc: 63`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.764
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.007699
  * `Imports (Out-Degree: 4):` blast_util.h, link_hsps.h, blast_hits_priv.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_traceback.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.512)
- **Top Global Matches:** file_cluster_6: 5.512, file_cluster_4: 7.909, file_cluster_16: 16.008
- **Magnitude:** 1845.82 | **LOC:** 1855 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **18**; blast radius 0.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (77.6%)
- **Documentation Coverage:** 53.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Blast_TracebackFromHSPList` **(Many-Argument Workhorses)** (Impact: 362.2)
    * *Intent:* */
  * `BLAST_ComputeTraceback_MT` **(Many-Argument Workhorses)** (Impact: 219.5)
  * `s_RPSComputeTraceback` **(Many-Argument Workhorses)** (Impact: 157.7)
    * *Intent:* * @param rps_info Extra information about RPS database. [in] * @param results Results structure cont...
  * `s_PHITracebackFromHSPList` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* /** Performs traceback alignment for one HSP list in a PHI BLAST search. * @param program_number eBl...
  * `Blast_RunTracebackSearchWithInterrupt` **(Many-Argument Workhorses)** (Impact: 37.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 821
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 64`, `args: 31`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 309`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 11`, `import: 18`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.804
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.006981
  * `Imports (Out-Degree: 26):` blast_encoding.h, blast_kappa.h, blast_seqsrc.h, blast_seqsrc_impl.h, blast_setup.h, blast_sw.h, blast_traceback.h, blast_util.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/app/blast/legacy_blast.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.907)
- **Top Global Matches:** file_cluster_3: 7.907, file_cluster_8: 27.499, file_cluster_6: 40.515
- **Magnitude:** 1804.2 | **LOC:** 1360 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.648; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Complexity Load (formerly Cognitive Load) (82.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_megablast` **(Many-Argument Workhorses)** (Impact: 154.7)
  * `handle_blastpgp` **(Many-Argument Workhorses)** (Impact: 128.7)
  * `handle_blastall` **(Many-Argument Workhorses)** (Impact: 128.2)
    * *Intent:* # Handle the conversion from blastall arguments to the corresponding C++ # binaries
  * `handle_bl2seq` **(Many-Argument Workhorses)** (Impact: 91.5)
  * `handle_seedtop` **(Compute Cores)** (Impact: 76.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 307 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 930
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 108`, `args: 34`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 316`, `dead_code: 4`
* *Architecture:* `io: 14`, `api: 14`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.648
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Getopt::Long, Pod::Usage, constant, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/algo/blast/core/blast_util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.875)
- **Top Global Matches:** file_cluster_6: 5.875, file_cluster_4: 10.609, file_cluster_8: 15.118
- **Magnitude:** 1789.72 | **LOC:** 1414 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **3**; blast radius 22.517; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.5%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 416`, `unreferenced_by_name: 26`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `safety: 9`, `doc: 8`, `immutability_locks: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.517
  * `Choke Point (Betweenness):` 0.005322 | `Ripple Effect (Closeness):` 0.134175
  * `Imports (Out-Degree: 6):` blast_filter.h, blast_stat.h, blast_util.h
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `src/algo/blast/format/blast_format.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.738)
- **Top Global Matches:** file_cluster_6: 5.738, file_cluster_4: 9.932, file_cluster_8: 15.279
- **Magnitude:** 1780.32 | **LOC:** 2562 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 1.009; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.3%), Guard Balance (formerly Safety Score) (63.2%)
- **Documentation Coverage:** 95.082% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CBlastFormat::PrintOneResultSet` **(Many-Argument Workhorses)** (Impact: 205.2)
  * `CBlastFormat::PrintOneResultSet` **(Many-Argument Workhorses)** (Impact: 107.0)
  * `CBlastFormat::PrintPhiResult` **(Many-Argument Workhorses)** (Impact: 81.3)
  * `CBlastFormat::CBlastFormat` **(Many-Argument Workhorses)** (Impact: 75.1)
  * `CBlastFormat::x_PrintStructuredReport` **(Compute Cores)** (Impact: 47.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 169 instances
* *Memory Alloc (weighted view):* 38
* *State Mutation (weighted view):* 575
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 89`, `args: 98`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 237`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 5`, `unreferenced_by_name: 34`
* *Architecture:* `import: 20`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.009
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.012117
  * `Imports (Out-Degree: 7):` objmgr_query_data.hpp, sseqloc.hpp, blast_stat.h, blast_format.hpp, blastxml2_format.hpp, blastxml_format.hpp, build_archive.hpp, data4xml2format.hpp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_options.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.372)
- **Top Global Matches:** file_cluster_4: 6.372, file_cluster_6: 7.69, file_cluster_12: 13.844
- **Magnitude:** 1723.5 | **LOC:** 2015 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **38** in-repo importer(s); it depends on **7**; blast radius 5.264; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (75.3%), Guard Balance (formerly Safety Score) (66.4%)
- **Documentation Coverage:** 94.5946% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LookupTableOptionsValidate` **(Many-Argument Workhorses)** (Impact: 117.5)
  * `BlastScoringOptionsValidate` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `BLAST_ValidateOptions` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `s_BlastExtensionScoringOptionsValidate` **(Many-Argument Workhorses)** (Impact: 45.3)
    * *Intent:* /** Checks that the extension and scoring options are consistent with each other * @param program_nu...
  * `BLAST_GetSuggestedThreshold` **(Compute Cores)** (Impact: 43.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 166 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 513
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 219`, `args: 78`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 181`, `planned_debt: 3`, `unreferenced_by_name: 36`
* *Architecture:* `api: 71`, `import: 7`
* *Defense:* `safety: 18`, `doc: 10`, `immutability_locks: 47`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.264
  * `Choke Point (Betweenness):` 0.000789 | `Ripple Effect (Closeness):` 0.090959
  * `Imports (Out-Degree: 6):` composition_constants.h, blast_filter.h, blast_options.h, blast_stat.h, blast_util.h, hspfilter_besthit.h, hspfilter_collector.h
  * `Imported By (In-Degree: 38):` (Excluded from Brief to save tokens)

### `src/algo/blast/unit_tests/seqdb_reader/seqdb_unit_test.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.222)
- **Top Global Matches:** file_cluster_15: 7.222, file_cluster_16: 8.454, file_cluster_2: 8.585
- **Magnitude:** 1690.72 | **LOC:** 4617 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 1.199; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (77.4%), Guard Balance (formerly Safety Score) (61.0%), Complexity Load (formerly Cognitive Load) (55.1%)
- **Documentation Coverage:** 98.773% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GiListOidRange` **(I/O & Config Routines)** (Impact: 38.1)
  * `OidRanges` **(I/O & Config Routines)** (Impact: 32.6)
  * `s_TestMaskingLimits` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `s_MaskingTest` **(Compute Cores)** (Impact: 29.7)
  * `ComplexComputedList` **(I/O & Config Routines)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 228 instances
* *Memory Alloc (weighted view):* 27
* *State Mutation (weighted view):* 782
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 54`, `args: 285`, `func_start: 163`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 326`, `dead_code: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 119`
* *Architecture:* `api: 6`, `import: 17`
* *Defense:* `safety: 26`, `doc: 7`, `immutability_locks: 80`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.199
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001309
  * `Imports (Out-Degree: 0):` algorithm, chrono, cmath, ncbifile.hpp, test_boost.hpp, ncbi_pch.hpp, defline_extra.hpp, seq__.hpp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algo/blast/core/blast_engine.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.384)
- **Top Global Matches:** file_cluster_8: 6.384, file_cluster_6: 11.372, file_cluster_4: 19.986
- **Magnitude:** 1651.66 | **LOC:** 1797 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.764; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (42.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BLAST_PreliminarySearchEngine` **(Many-Argument Workhorses)** (Impact: 213.1)
  * `s_BlastSearchEngineCore` **(Many-Argument Workhorses)** (Impact: 204.7)
    * *Intent:* * @param word_params Initial word finding and ungapped extension * parameters [in] * @param ext_para...
  * `s_BlastSearchEngineOneContext` **(Many-Argument Workhorses)** (Impact: 128.6)
    * *Intent:* * @param word_params Initial word finding and ungapped extension * parameters [in] * @param ext_para...
  * `s_BlastSetUpAuxStructures` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* /** Setup of the auxiliary BLAST structures; * also calculates internally used parameters from optio...
  * `s_RPSPreliminarySearchEngine` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* * @param word_params Parameters for processing initial word hits [in] * @param ext_params Parameters...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 694
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 71`, `args: 24`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 262`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 21`
* *Defense:* `safety: 2`, `doc: 46`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.764
  * `Choke Point (Betweenness):` 0.000139 | `Ripple Effect (Closeness):` 0.001745
  * `Imports (Out-Degree: 21):` aa_ungapped.h, blast_aalookup.h, blast_aascan.h, blast_engine.h, blast_gapalign.h, blast_nalookup.h, blast_nascan.h, blast_parameters.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/algo/blast/api/blast_seqalign.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.001)
- **Top Global Matches:** file_cluster_4: 6.001, file_cluster_6: 8.942, file_cluster_15: 12.512
- **Magnitude:** 1585.96 | **LOC:** 2152 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 0.943; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Complexity Load (formerly Cognitive Load) (33.7%)
- **Documentation Coverage:** 35.8974% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `s_OOFBlastHSP2SeqAlign` **(Many-Argument Workhorses)** (Impact: 137.8)
    * *Intent:* /// This function is used for out-of-frame traceback conversion /// Converts an OOF editing script c...
  * `s_CollectSeqAlignData` **(Many-Argument Workhorses)** (Impact: 73.9)
    * *Intent:* /// Note that even though the edit_block is passed in, data for seqalign is /// collected from the e...
  * `s_BlastHSP2SeqAlign` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* /// Converts a traceback editing block to a Seq-align, provided the 2 sequence /// identifiers. /// ...
  * `MakeSplicedSeg` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* #endif
  * `s_BLAST_OneSubjectResults2CSeqAlign` **(Many-Argument Workhorses)** (Impact: 50.7)
    * *Intent:* /** Extracts results from the BlastHSPResults structure for only one subject * sequence, identified ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 689
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 53`, `args: 51`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `state_mutation: 271`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 4`
* *Architecture:* `import: 13`
* *Defense:* `doc: 182`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.943
  * `Choke Point (Betweenness):` 8.2e-05 | `Ripple Effect (Closeness):` 0.005236
  * `Imports (Out-Degree: 5):` jumper.h, blast_aux.hpp, query_data.hpp, algorithm, blast_seqalign.hpp, ncbi_pch.hpp, Object_id.hpp, User_object.hpp...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/algo/blast/api/blast_setup_cxx.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.766)
- **Top Global Matches:** file_cluster_6: 5.766, file_cluster_4: 8.144, file_cluster_9: 15.834
- **Magnitude:** 1556.94 | **LOC:** 1776 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **11**; blast radius 2.238; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Debt Markers (formerly Tech Debt) (50.8%)
- **Documentation Coverage:** 67.3469% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetupQueries_OMF` **(Many-Argument Workhorses)** (Impact: 96.1)
  * `SetupQueryInfo_OMF` **(Many-Argument Workhorses)** (Impact: 82.1)
  * `s_SeqLoc2MaskedSubjRanges` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `SetupSubjects_OMF` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `CBlastQueryFilteredFrames::x_VerifyFrame` **(Compute Cores)** (Impact: 44.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 202 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 636
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 68`, `args: 73`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 232`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 17`
* *Architecture:* `import: 11`
* *Defense:* `safety: 12`, `doc: 46`, `immutability_locks: 42`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.238
  * `Choke Point (Betweenness):` 0.001403 | `Ripple Effect (Closeness):` 0.057802
  * `Imports (Out-Degree: 10):` blast_options.hpp, blast_setup.h, blast_util.h, gencode_singleton.h, blast_setup.hpp, metareg.hpp, ncbiapp.hpp, ncbi_pch.hpp...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/algo/blast/api/remote_blast.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.11)
- **Top Global Matches:** file_cluster_4: 6.11, file_cluster_15: 8.406, file_cluster_11: 9.783
- **Magnitude:** 1515.12 | **LOC:** 2699 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **24**; blast radius 2.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (96.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ITERATE` **(Compute Cores)** (Impact: 37.5)
  * `CRemoteBlast::x_PollUntilDone` **(Many-Argument Workhorses)** (Impact: 34.2)
    * *Intent:* // not know how long it has been since the request was submitted. In // this case, we check the resu...
  * `CRemoteBlast::x_SearchErrors` **(Compute Cores)** (Impact: 29.3)
  * `ExtractBlast4Request` **(Compute Cores)** (Impact: 29.2)
  * `CRemoteBlast::GetResultSet` **(I/O & Config Routines)** (Impact: 23.8)
    * *Intent:* /// Submit the search and return the results. /// @return Search results.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 160 instances
* *Memory Alloc (weighted view):* 56
* *State Mutation (weighted view):* 541
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 183`, `args: 165`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 221`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 72`
* *Architecture:* `import: 25`
* *Defense:* `safety: 22`, `doc: 16`, `immutability_locks: 74`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.5
  * `Choke Point (Betweenness):` 0.00055 | `Ripple Effect (Closeness):` 0.017533
  * `Imports (Out-Degree: 8):` blast_options_builder.hpp, objmgr_query_data.hpp, remote_blast.hpp, search_strategy.hpp, ncbi_system.hpp, ncbitime.hpp, stream_utils.hpp, ncbi_pch.hpp...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/algo/blast/vdb/blastn_vdb_args.cpp` (CPP) | Magnitude: 33.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 20, memory_alloc: 18, immutability_locks: 7
- `src/algo/blast/unit_tests/api/pssmenginefreqratios_unit_test.cpp` (CPP) | Magnitude: 41.06 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, pointers: 19, core_var_decl: 13, import: 12
- `src/algo/blast/blastinput/demo/blastinput_demo.cpp` (CPP) | Magnitude: 36.56 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 22, pointers: 17, args: 11
- `src/algo/blast/api/psibl2seq.cpp` (CPP) | Magnitude: 19.88 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, func_start: 6, import: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/algo/blast/api/seqinfosrc_bioseq.cpp` (CPP) | Magnitude: 18.04 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 20, immutability_locks: 12, func_start: 9, args: 8
- `src/algo/blast/unit_tests/api/bl2seq_unit_test.cpp` (CPP) | Magnitude: 1080.86 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 2378, pointers: 920, args: 354, core_var_decl: 329
- `src/algo/blast/unit_tests/api/hspstream_unit_test.cpp` (CPP) | Magnitude: 100.92 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 120, core_var_decl: 55, design_snake_case: 48, state_mutation: 40
- `src/algo/blast/composition_adjustment/compo_heap.c` (C) | Magnitude: 311.06 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 219, pointers: 139, state_mutation: 67, branch: 49
- `src/algo/blast/unit_tests/api/stat_unit_test.cpp` (CPP) | Magnitude: 14.44 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 21, core_var_decl: 14, design_snake_case: 11, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/algo/blast/core/lookup_util.c` (C) | Magnitude: 128.3 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 83, state_mutation: 25, branch: 15, pointers: 14
- `src/algo/blast/core/blast_seg.c` (C) | Magnitude: 908.9 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1697, state_mutation: 224, pointers: 212, branch: 110

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/algo/blast/gumbel_params/unit_test/general_score_matrix_unit_test.cpp` (CPP) | Magnitude: 27.74 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, core_var_decl: 8, design_snake_case: 7, branch: 5
- `src/algo/blast/unit_tests/api/hspfilter_besthit_unit_test.cpp` (CPP) | Magnitude: 14.68 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, core_var_decl: 19, design_snake_case: 15, pointers: 12
- `src/algo/blast/unit_tests/api/hspfilter_culling_unit_test.cpp` (CPP) | Magnitude: 14.78 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, core_var_decl: 19, design_snake_case: 15, pointers: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/algo/blast/unit_tests/api/queryinfo_unit_test.cpp` (CPP) | Magnitude: 28.34 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 116, pointers: 50, core_var_decl: 28, args: 23
- `src/algo/blast/unit_tests/api/subj_ranges_unit_test.cpp` (CPP) | Magnitude: 18.44 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 90, pointers: 19, immutability_locks: 18, core_var_decl: 15
- `src/algo/blast/unit_tests/api/msa2pssm_unit_test.cpp` (CPP) | Magnitude: 43.3 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 87, pointers: 28, core_var_decl: 11, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/algo/blast/unit_tests/api/seqalign_cmp.cpp` (CPP) | Magnitude: 216.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 250, branch: 47, structural_boundaries: 42, pointers: 41

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/algo/blast/unit_tests/api/remote_blast_unit_test.cpp` -> Churn: **100.0%** | Cog Load: 31.8096% | Debt: 97.4176%
- `src/algo/blast/api/blast_node.cpp` -> Churn: **75.66%** | Cog Load: 45.4096% | Debt: 94.0652%
- `src/algo/blast/api/rps_aux.cpp` -> Churn: **75.66%** | Cog Load: 18.9907% | Debt: 98.8688%
- `src/algo/blast/core/blast_filter.c` -> Churn: **59.44%** | Cog Load: 58.2727% | Debt: 17.1636%
- `src/algo/blast/core/blast_nalookup.c` -> Churn: **52.48%** | Cog Load: 59.8054% | Debt: 11.168%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/algo/blast/core/blast_gapalign.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 6698.44
- `src/algo/blast/core/hspfilter_mapper.c` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 4694.92
- `src/algo/blast/core/blast_stat.c` -> **Christiam Camacho** (100.0% isolated ownership) | Magnitude: 4575.2
- `src/algo/blast/core/na_ungapped.c` -> **Amelia Fong** (100.0% isolated ownership) | Magnitude: 2423.7
- `src/algo/blast/blastinput/blast_args.cpp` -> **Grzegorz (Greg) Boratyn** (100.0% isolated ownership) | Magnitude: 2345.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/algo/blast/core/blast_util.c` -> **Severity: 0.532** (Bridge: 0.0053 * Flux: 100.0%)
- `src/algo/blast/core/blast_filter.c` -> **Severity: 0.528** (Bridge: 0.0053 * Flux: 100.0%)
- `src/algo/blast/api/blast_aux.cpp` -> **Severity: 0.428** (Bridge: 0.0045 * Flux: 95.7129%)
- `src/algo/blast/core/jumper.c` -> **Severity: 0.423** (Bridge: 0.0042 * Flux: 100.0%)
- `src/algo/blast/core/blast_stat.c` -> **Severity: 0.404** (Bridge: 0.004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/algo/blast/core/blast_util.c` -> **Severity: 11.863** (Embedded: 0.1342 * Error Risk: 88.4157%)
- `src/algo/blast/gumbel_params/njn_ioutil.hpp` -> **Severity: 9.334** (Embedded: 0.1339 * Error Risk: 69.6916%)
- `src/algo/blast/core/blast_stat.c` -> **Severity: 9.068** (Embedded: 0.1114 * Error Risk: 81.3652%)
- `src/algo/blast/core/blast_filter.c` -> **Severity: 8.75** (Embedded: 0.1105 * Error Risk: 79.1651%)
- `src/algo/blast/core/blast_query_info.c` -> **Severity: 8.238** (Embedded: 0.1022 * Error Risk: 80.6389%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/algo/blast/gumbel_params/njn_ioutil.hpp` -> **Severity: 6412.9** (Blast Radius: 64.129 * Doc Risk: 100.0%)
- `src/algo/blast/gumbel_params/njn_ioutil.cpp` -> **Severity: 5551.7** (Blast Radius: 55.517 * Doc Risk: 100.0%)
- `src/algo/blast/core/blast_util.c` -> **Severity: 2153.801** (Blast Radius: 22.517 * Doc Risk: 95.6522%)
- `src/algo/blast/gumbel_params/sls_alp_data.hpp` -> **Severity: 1876.9** (Blast Radius: 18.769 * Doc Risk: 100.0%)
- `src/algo/blast/core/blast_program.c` -> **Severity: 1244.786** (Blast Radius: 13.337 * Doc Risk: 93.3333%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 262 literal sites + 1 sites through wrappers = 263
- **`memory_alloc`:** 3029 literal sites + 274 sites through wrappers = 3303

- `BlastSeqLocNew` (function, memory_alloc, primitive): 49 call sites in 14 files -- `src/algo/blast/core/blast_filter.c`
- `Blast_KarlinBlkNew` (function, memory_alloc, primitive): 28 call sites in 9 files -- `src/algo/blast/core/blast_stat.c`
- `Blast_HSPNew` (function, memory_alloc, primitive): 19 call sites in 8 files -- `src/algo/blast/core/blast_hits.c`
- `Blast_HitListNew` (function, memory_alloc, primitive): 13 call sites in 7 files -- `src/algo/blast/core/blast_hits.c`
- `Nlm_DenseMatrixFree` (function, memory_alloc, primitive): 9 call sites in 2 files -- `src/algo/blast/composition_adjustment/nlm_linear_algebra.c`
- `BLAST_InitHitListNew` (function, memory_alloc, primitive): 8 call sites in 4 files -- `src/algo/blast/core/blast_extend.c`
- `BlastHSPCollectorInfoNew` (function, memory_alloc, primitive): 8 call sites in 5 files -- `src/algo/blast/core/hspfilter_collector.c`
- `HSPContainerNew` (function, memory_alloc, primitive): 8 call sites in 2 files -- `src/algo/blast/core/spliced_hits.c`
- `BlastEffectiveLengthsParametersNew` (function, memory_alloc, primitive): 6 call sites in 5 files -- `src/algo/blast/core/blast_parameters.c`
- `s_SequenceDataRelease` (function, memory_alloc, primitive): 6 call sites in 1 files -- `src/algo/blast/composition_adjustment/redo_alignment.c`
- `x_MakeStream` (function, memory_alloc, via BlastHSPCollectorInfoNew): 6 call sites in 1 files -- `src/algo/blast/unit_tests/api/traceback_unit_test.cpp`
- `BlastHSPMappingInfoNew` (function, memory_alloc, primitive): 5 call sites in 3 files -- `src/algo/blast/core/blast_hits.c`
*(+68 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 35468 call pairs -- scoped 13.3%, unique 10.8%, ambiguous 20.9%, external 55.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 30838 | 10.9% | 8.7% | 24.0% | 56.4% |
| c | 4329 | 29.7% | 27.1% | 0.0% | 43.2% |
| perl | 236 | 25.4% | 0.0% | 0.0% | 74.6% |
| python | 41 | 17.1% | 0.0% | 0.0% | 82.9% |
| shell | 24 | 29.2% | 0.0% | 0.0% | 70.8% |

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
