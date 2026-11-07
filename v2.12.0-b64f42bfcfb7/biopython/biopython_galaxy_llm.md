# ARCHITECTURAL_BRIEF: biopython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/biopython/biopython.git` |
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
- **Scope:** 1138 analyzed artifact(s), 343920 LOC.
- **Load-bearing artifact:** `Bio/__init__.py` -- 221 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Bio/PDB/__init__.py` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Bio/Align/_pairwisealigner.c` at magnitude 7552.34 (structural weight, not risk).
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
| Total Artifacts | 2414 |
| Analyzed Artifacts (Scanned) | 1138 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1276 |
| Total LOC | 343920 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 47.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5924 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1598 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3166 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 45 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 531 | 321079 | 46.7% |
| PLAINTEXT | 420 | 19 | 36.9% |
| XML | 131 | 0 | 11.5% |
| C | 17 | 18503 | 1.5% |
| MARKDOWN | 12 | 0 | 1.1% |
| HTML | 11 | 2551 | 1.0% |
| JSON | 5 | 5 | 0.4% |
| YAML | 3 | 343 | 0.3% |
| SHELL | 2 | 75 | 0.2% |
| SQLITE | 2 | 717 | 0.2% |
| CSV | 2 | 610 | 0.2% |
| MAKEFILE | 1 | 15 | 0.1% |
| CSS | 1 | 3 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 15 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1122 |
| cp1252 | cp1252-fallback | 15 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 53%, Large Core Modules (3) 12%, Parameter Forwarders Files 11%, Many-Argument Workhorses Files 6%, Large Core Modules 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 701 | 61.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 431 | 37.9% |
| Static: Minified & Vendor Opaque Mass | 6 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1276*

**Composition by Extension & Reason:**
- `.dtd`: 204x Excluded (Unsupported Extension: '.dtd')
- `.ent`: 83x Excluded (Unsupported Extension: '.ent')
- `.fastq`: 59x Excluded (Unsupported Extension: '.fastq')
- `no_extension`: 42x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unresolved Ambiguity (No Retainable Structure)
- `.exn`: 52x Excluded (Unsupported Extension: '.exn')
- `.xml`: 3x Excluded (Saturation: Line 30 exceeds 500 chars), 2x Excluded (Saturation: Line 49 exceeds 500 chars), 2x Excluded (Saturation: Line 50 exceeds 500 chars)
- `.fa`: 44x Excluded (Unsupported Extension: '.fa')
- `.ctl`: 42x Excluded (Unsupported Extension: '.ctl')
- `.png`: 39x Excluded (Explicitly Denied Extension: '.png')
- `.gb`: 38x Excluded (Unsupported Extension: '.gb')
- `.rst`: 36x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bb`: 29x Excluded (Unsupported Extension: '.bb')
- `.id`: 27x Excluded (Unsupported Extension: '.id')
- `.cif`: 19x Excluded (Unsupported Extension: '.cif')
- `.aln`: 18x Excluded (Unsupported Extension: '.aln')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.9 | 22.7 | 16.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.4 | 51.2 | 58.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.1 | 12.9 | 7.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.9 | 0.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 16.8 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 77.2 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7162 | 363 | 11 | `Tests/test_Align_tabular.py` |
| cleanup | 340 | 72 | 0 | `Tests/test_SeqIO_index.py` |
| guards | 8277 | 401 | 17 | `Bio/Align/_pairwisealigner.c` |
| danger | 5068 | 400 | 12 | `Bio/Align/_pairwisealigner.c` |
| concurrency | 330 | 112 | 0 | `Tests/test_GenBank.py` |
| connectivity | 8022 | 507 | 17 | `Tests/test_SeqIO.py` |
| io | 2796 | 237 | 5 | `Doc/cookbook/Restriction/Restriction.html` |
| crypto | 2 | 2 | 0 | `Bio/SeqIO/GfaIO.py` |
| ipc | 42 | 13 | 0 | `Bio/PDB/DSSP.py` |
| time | 36 | 15 | 0 | `Bio/Blast/NCBIWWW.py` |
| serialization | 14 | 7 | 0 | `Tests/test_SearchIO_model.py` |
| regex | 262 | 58 | 0 | `Bio/PDB/parse_pdb_header.py` |
| events | 94 | 30 | 0 | `Tests/Blast/html_msgid_29_blastx_001.html` |
| tests | 4624 | 205 | 12 | `Tests/test_seq.py` |
| docs | 12164 | 544 | 19 | `Tests/test_pairwise_aligner.py` |
| debt | 1089 | 207 | 2 | `Bio/Restriction/Restriction.py` |
| mutation | 99999 | 536 | 241 | `Bio/Align/_pairwisealigner.c` |
| dead_code | 3119 | 326 | 7 | `Tests/test_seq.py` |
| credential | 59 | 6 | 0 | `Tests/test_Blast_parser.py` |
| threat | 17 | 4 | 0 | `Tests/test_SeqIO_SffIO.py` |
| ml_ai | 244 | 110 | 0 | `Bio/Cluster/cluster.c` |
| ui | 183 | 8 | 0 | `Tests/Rebase/bamii.htm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Doc/cookbook/Restriction/Restriction.html` (Hits: 298)
- `Tests/test_Blast_parser.py` (Hits: 118)
- `Tests/Blast/html_msgid_29_blastx_001.html` (Hits: 78)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`Bio/__init__.py`) — 221 inbound connections
2. **Seq.py** (`Bio/Seq.py`) — 124 inbound connections
3. **SeqRecord.py** (`Bio/SeqRecord.py`) — 104 inbound connections
4. **_utils.py** (`Bio/_utils.py`) — 84 inbound connections
5. **__init__.py** (`Bio/Align/__init__.py`) — 78 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`Bio/PDB/__init__.py`) — 22 outbound dependencies
2. **test_PDB_internal_coords.py** (`Tests/test_PDB_internal_coords.py`) — 18 outbound dependencies
3. **__init__.py** (`Bio/Align/__init__.py`) — 16 outbound dependencies
4. **common_BioSQL.py** (`Tests/common_BioSQL.py`) — 16 outbound dependencies
5. **run_tests.py** (`Tests/run_tests.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_get_atom_radius` **(Compute Cores)** (@ `Bio/PDB/ResidueDepth.py`) -> Impact: **443.6** | LOC: 384
  * *Intent:* # Table 2: Resname/Aname to Atom Type # MSMS uses an awk/gawk pattern matching strategy that we cannot replicate # We will take advantage of our parse...
- `read_PIC` **(Many-Argument Workhorses)** (@ `Bio/PDB/PICIO.py`) -> Impact: **443.5** | LOC: 775
  * *Intent:* # @profile
- `test_P04439` **(Many-Argument Workhorses)** (@ `Tests/test_SwissProt.py`) -> Impact: **332.6** | LOC: 2891
  * *Intent:* """Parsing SwissProt file P04439.txt."""
- `clusterdistance` **(Many-Argument Workhorses)** (@ `Bio/Cluster/cluster.c`) -> Impact: **325.3** | LOC: 376
  * *Intent:* /* ******************************************************************** */
- `svd` **(Many-Argument Workhorses)** (@ `Bio/Cluster/cluster.c`) -> Impact: **318.1** | LOC: 483
  * *Intent:* /* ********************************************************************* */
- `AlignmentCounts_new` **(Many-Argument Workhorses)** (@ `Bio/Align/_alignmentcounts.c`) -> Impact: **296.1** | LOC: 483
- `_fetch_internal_id_list` **(Many-Argument Workhorses)** (@ `Bio/motifs/jaspar/db.py`) -> Impact: **235.6** | LOC: 296
- `_write_SCAD` **(Many-Argument Workhorses)** (@ `Bio/PDB/internal_coords.py`) -> Impact: **220.7** | LOC: 250
  * *Intent:* """Write self to file fp as OpenSCAD data matrices. See `OpenSCAD <https://www.openscad.org>`_. Works with :func:`.write_SCAD` and embedded OpenSCAD r...
- `somworker` **(Many-Argument Workhorses)** (@ `Bio/Cluster/cluster.c`) -> Impact: **215.6** | LOC: 202
  * *Intent:* /* ******************************************************************* */
- `check_reading_psl_34_001` **(Many-Argument Workhorses)** (@ `Tests/test_Align_psl.py`) -> Impact: **200.2** | LOC: 3375
  * *Intent:* """Check parsing psl_34_001.psl or pslx_34_001.pslx."""

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Tests` | 206 | 53934.94 | 12.12% | 0.0% |
| `Bio/Align` | 29 | 27941.38 | 57.21% | 29.14% |
| `Bio/PDB` | 44 | 16728.44 | 41.63% | 8.92% |
| `Bio/Cluster` | 4 | 9885.64 | 44.41% | 5.19% |
| `Bio/SeqIO` | 23 | 8672.46 | 41.14% | 46.43% |
| `Bio/Phylo` | 15 | 6591.62 | 32.04% | 13.5% |
| `Bio` | 9 | 6540.64 | 46.49% | 39.79% |
| `Bio/Nexus` | 6 | 4649.4 | 41.57% | 21.95% |
| `Bio/Blast` | 5 | 4244.32 | 49.12% | 23.74% |
| `Bio/Graphics/GenomeDiagram` | 11 | 4104.16 | 37.49% | 11.16% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/ci.yml` -> **100.0%** Exposure
- `BioSQL/BioSeqDatabase.py` -> **99.9997%** Exposure
- `Bio/ExPASy/__init__.py` -> **99.9925%** Exposure
- `Bio/SeqFeature.py` -> **99.9868%** Exposure
- `Bio/bgzf.py` -> **99.9802%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Bio/Affy/CelFile.py` -> **100.0%** Exposure
- `Bio/Align/__init__.py` -> **100.0%** Exposure
- `Bio/Align/a2m.py` -> **100.0%** Exposure
- `Bio/Align/analysis.py` -> **100.0%** Exposure
- `Bio/Align/bed.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Tests/test_seq.py` -> **111** Orphaned Functions | **0** Duplicates
- `Tests/test_SearchIO_model.py` -> **102** Orphaned Functions | **2** Duplicates
- `Tests/test_GenBank.py` -> **94** Orphaned Functions | **0** Duplicates
- `Tests/test_pairwise_aligner.py` -> **68** Orphaned Functions | **10** Duplicates
- `Tests/test_Seq_objs.py` -> **68** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `Tests/test_Entrez_online.py` -> **77.196%** Exposure
- `Tests/test_Entrez.py` -> **47.6761%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2568` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Bio/Align/_pairwisealigner.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.541)
- **Top Global Matches:** file_cluster_4: 6.541, file_cluster_6: 7.57, file_cluster_16: 13.292
- **Magnitude:** 7552.34 | **LOC:** 7741 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.9%), Complexity Load (formerly Cognitive Load) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PathGenerator_next_waterman_smith_beyer_global` **(Compute Cores)** (Impact: 107.7)
  * `PathGenerator_next_waterman_smith_beyer_local` **(Compute Cores)** (Impact: 105.7)
  * `Aligner_score` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `Aligner_align` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `PathGenerator_next_gotoh_global` **(Compute Cores)** (Impact: 75.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1304 instances
* *State Mutation (weighted view):* 4899
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1258`, `structural_boundaries: 946`, `args: 506`, `func_start: 173`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 2291`, `dead_code: 2`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `immutability_locks: 314`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Python.h, _pairwisealigner.h, float.h, stdbool.h, _arraycore.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/Cluster/cluster.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.403)
- **Top Global Matches:** file_cluster_3: 9.403, file_cluster_8: 15.475, file_cluster_6: 28.232
- **Magnitude:** 7494.44 | **LOC:** 5075 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.744; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clusterdistance` **(Many-Argument Workhorses)** (Impact: 325.3)
    * *Intent:* /* ******************************************************************** */
  * `svd` **(Many-Argument Workhorses)** (Impact: 318.1)
    * *Intent:* /* ********************************************************************* */
  * `somworker` **(Many-Argument Workhorses)** (Impact: 215.6)
    * *Intent:* /* ******************************************************************* */
  * `kendall` **(Many-Argument Workhorses)** (Impact: 170.1)
    * *Intent:* /* ********************************************************************* */
  * `kmedians` **(Many-Argument Workhorses)** (Impact: 136.9)
    * *Intent:* /* ---------------------------------------------------------------------- */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1475 instances
* *State Mutation (weighted view):* 4479
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 887`, `structural_boundaries: 213`, `args: 47`, `func_start: 47`
* *Risk/State:* `state_mutation: 1529`, `planned_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 1`, `doc: 5`, `immutability_locks: 115`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.744
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000876
  * `Imports (Out-Degree: 1):` Python.h, cluster.h, float.h, limits.h, math.h, stdlib.h, string.h, time.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bio/Align/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.314)
- **Top Global Matches:** file_cluster_6: 8.314, file_cluster_4: 10.024, file_cluster_12: 16.069
- **Magnitude:** 4140.92 | **LOC:** 4968 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **78** in-repo importer(s); it depends on **16**; blast radius 12.3; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.3%), Connectivity (formerly Api Exposure) (57.2%), Complexity Load (formerly Cognitive Load) (49.9%)
- **Documentation Coverage:** 24.8276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_format_pretty` **(Many-Argument Workhorses)** (Impact: 121.9)
    * *Intent:* """Return default string representation (PRIVATE). Helper for self.format(). Arguments: - matrix - O...
  * `_get_row_cols_slice` **(Many-Argument Workhorses)** (Impact: 86.8)
  * `map` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `from_alignments_with_same_reference` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `__getitem__` **(Many-Argument Workhorses)** (Impact: 54.1)
    * *Intent:* """Return self[key]. Indices of the form self[:, :] return a copy of the Alignment object; self[:, i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 789 instances
* *State Mutation (weighted view):* 2471
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 649`, `structural_boundaries: 352`, `args: 93`, `func_start: 92`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 893`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 13`, `api: 54`, `import: 30`
* *Defense:* `safety: 203`, `doc: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.3
  * `Choke Point (Betweenness):` 0.000303 | `Ripple Effect (Closeness):` 0.078409
  * `Imports (Out-Degree: 6):` Bio, Bio.Align, Bio.Data, Bio.Seq, Bio.SeqRecord, Bio._utils, abc, copy...
  * `Imported By (In-Degree: 78):` (Excluded from Brief to save tokens)

### `Bio/PDB/internal_coords.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.735)
- **Top Global Matches:** file_cluster_4: 8.735, file_cluster_5: 11.736, file_cluster_12: 11.863
- **Magnitude:** 3801.16 | **LOC:** 4942 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 1.849; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (48.5%)
- **Documentation Coverage:** 16.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_write_SCAD` **(Many-Argument Workhorses)** (Impact: 220.7)
    * *Intent:* """Write self to file fp as OpenSCAD data matrices. See `OpenSCAD <https://www.openscad.org>`_. Work...
  * `_write_PIC` **(Many-Argument Workhorses)** (Impact: 106.2)
  * `_hedraDict2chain` **(Many-Argument Workhorses)** (Impact: 82.6)
  * `_cmp` **(Many-Argument Workhorses)** (Impact: 72.1)
    * *Intent:* # @profile """Comparison function ranking self vs. other. Priority is lower value, i.e. (CA, CB) giv...
  * `_create_edra` **(Many-Argument Workhorses)** (Impact: 70.6)
    * *Intent:* # @profile """Create IC_Chain and IC_Residue di/hedra for atom coordinates. AllBonds handled here. :...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 554 instances
* *State Mutation (weighted view):* 1929
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 699`, `structural_boundaries: 385`, `args: 121`, `func_start: 121`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 821`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 72`, `import: 25`
* *Defense:* `safety: 87`, `doc: 157`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 8.7e-05 | `Ripple Effect (Closeness):` 0.015972
  * `Imports (Out-Degree: 5):` Bio.Data.PDBData, Bio.PDB.Atom, Bio.PDB.Residue, Bio.PDB.ic_data, Bio.PDB.vectors, collections, copy, numbers...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Bio/Nexus/Nexus.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.003)
- **Top Global Matches:** file_cluster_6: 9.003, file_cluster_4: 9.37, file_cluster_12: 14.893
- **Magnitude:** 2880.22 | **LOC:** 2134 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 0.751; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.3%), Guard Balance (formerly Safety Score) (85.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 22.9508% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_nexus_data` **(Many-Argument Workhorses)** (Impact: 199.3)
  * `append_sets` **(Many-Argument Workhorses)** (Impact: 121.4)
  * `_matrix` **(Many-Argument Workhorses)** (Impact: 82.5)
    * *Intent:* """Create a matrix for NEXUS object (PRIVATE)."""
  * `_format` **(Many-Argument Workhorses)** (Impact: 69.2)
    * *Intent:* # print options # we first need to test respectcase, then symbols (which depends on respectcase) # t...
  * `constant` **(Many-Argument Workhorses)** (Impact: 56.6)
    * *Intent:* """Return a list with all constant characters."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 417 instances
* *State Mutation (weighted view):* 1319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 255`, `args: 88`, `func_start: 86`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 2`, `state_mutation: 485`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 37`
* *Architecture:* `io: 6`, `api: 40`, `import: 14`
* *Defense:* `safety: 33`, `doc: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.751
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.004897
  * `Imports (Out-Degree: 7):` .cnexus, Bio, Bio.Data, Bio.Nexus.StandardData, Bio.Nexus.Trees, Bio.Seq, Bio._utils, copy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bio/Align/bigbed.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.381)
- **Top Global Matches:** file_cluster_4: 5.381, file_cluster_6: 8.619, file_cluster_12: 12.338
- **Magnitude:** 2844.86 | **LOC:** 2244 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 0.907; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Complexity Load (formerly Cognitive Load) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 91.129% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_extract_fields` **(Many-Argument Workhorses)** (Impact: 88.8)
  * `_search_index` **(Many-Argument Workhorses)** (Impact: 75.5)
    * *Intent:* # Supplemental Table 12: Binary BED-data format # chromId 4 bytes, unsigned # chromStart 4 bytes, un...
  * `_create_alignment` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `rTreeFromChromRangeArray` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `write_alignments` **(Many-Argument Workhorses)** (Impact: 50.9)
    * *Intent:* """Write alignments to the output file, and return the number of alignments. alignments - A list or ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 517 instances
* *State Mutation (weighted view):* 1726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 233`, `args: 80`, `func_start: 77`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 692`
* *Architecture:* `io: 7`, `api: 50`, `import: 13`
* *Defense:* `safety: 60`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.907
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.003503
  * `Imports (Out-Degree: 3):` Bio.Align, Bio.Seq, Bio.SeqRecord, collections, copy, io, itertools, numpy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Tests/test_pairwise_aligner.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.156)
- **Top Global Matches:** file_cluster_15: 6.156, file_cluster_2: 7.018, file_cluster_11: 8.021
- **Magnitude:** 2615.48 | **LOC:** 22443 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.7%), Connectivity (formerly Api Exposure) (9.7%), Complexity Load (formerly Cognitive Load) (7.3%)
- **Documentation Coverage:** 98.0952% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_aligner_property_gapscores_deprecated` **(Compute Cores)** (Impact: 33.5)
  * `test_aligner_array_errors` **(I/O & Config Routines)** (Impact: 18.7)
  * `test_gap_here_only_1` **(I/O & Config Routines)** (Impact: 10.2)
  * `test_gap_here_only_2` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* # Force a bad alignment. # # Forces a bad alignment by having a very expensive gap penalty # where o...
  * `test_gap_here_only_3` **(I/O & Config Routines)** (Impact: 9.7)
    * *Intent:* # Check if gap open and gap extend penalties are handled correctly. seq1 = "TTCCAA" seq2 = "TTGGAA" ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 1864
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 472`, `args: 105`, `func_start: 105`, `class_start: 23`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 1760`, `duplicate_logic: 10`, `unreferenced_by_name: 68`
* *Architecture:* `io: 2`, `api: 128`, `import: 25`
* *Defense:* `safety: 18`, `doc: 764`, `test: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Bio, Bio.Align, Bio.Align.substitution_matrices, Bio.Seq, Bio.SeqRecord, array, numpy, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/test_SeqIO.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.133)
- **Top Global Matches:** file_cluster_15: 8.133, file_cluster_2: 9.12, file_cluster_16: 9.194
- **Magnitude:** 2303.96 | **LOC:** 5912 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 1.157; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (82.9%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (20.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.4%)
- **Documentation Coverage:** 85.3107% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_simple_write_read` **(Many-Argument Workhorses)** (Impact: 128.9)
  * `perform_test` **(Many-Argument Workhorses)** (Impact: 106.4)
  * `compare_record` **(Many-Argument Workhorses)** (Impact: 25.1)
    * *Intent:* """Compare old SeqRecord to new SeqRecord."""
  * `test_nexus1` **(I/O & Config Routines)** (Impact: 10.7)
  * `get_mode` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* """Determine if file mode should be text ("t") or binary ("b") based on format."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 1229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 289`, `args: 177`, `func_start: 177`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1063`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 182`, `import: 19`
* *Defense:* `safety: 25`, `doc: 56`, `test: 166`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.157
  * `Choke Point (Betweenness):` 0.000283 | `Ripple Effect (Closeness):` 0.007466
  * `Imports (Out-Degree: 7):` Bio, Bio.Align, Bio.AlignIO, Bio.PDB.PDBExceptions, Bio.Seq, Bio.SeqRecord, contextlib, copy...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Tests/test_Align_tabular.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.779)
- **Top Global Matches:** file_cluster_6: 8.779, file_cluster_8: 12.447, file_cluster_4: 14.976
- **Magnitude:** 2022.0 | **LOC:** 43593 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.6%), Connectivity (formerly Api Exposure) (5.9%), Complexity Load (formerly Cognitive Load) (2.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_m8CB` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `test_m8CC` **(I/O & Config Routines)** (Impact: 49.4)
    * *Intent:* # Alignment file obtained by running # fasta36 -q -m 8CB seq/mgstm1.aa seq/prot_test.lseg # in the f...
  * `test_m8CB` **(I/O & Config Routines)** (Impact: 49.4)
    * *Intent:* # Alignment file obtained by running # fasta36 -m 8CB seq/mgstm1.nt seq/gst.nlib # in the fasta36 so...
  * `test_m8CC` **(I/O & Config Routines)** (Impact: 49.4)
    * *Intent:* # Alignment file obtained by running # fasta36 -m 8CC seq/mgstm1.nt seq/gst.nlib # in the fasta36 so...
  * `test_2228_tblastx_001` **(Many-Argument Workhorses)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 1118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 100`, `args: 19`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1006`, `unreferenced_by_name: 14`
* *Architecture:* `io: 16`, `api: 23`, `import: 10`
* *Defense:* `safety: 2`, `doc: 665`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Bio, Bio.Align, Bio.Seq, io, numpy, os, tempfile, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/test_Blast_parser.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.865)
- **Top Global Matches:** file_cluster_4: 6.865, file_cluster_15: 9.485, file_cluster_16: 10.811
- **Magnitude:** 1987.4 | **LOC:** 15168 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (9.2%), Complexity Load (formerly Cognitive Load) (5.0%)
- **Documentation Coverage:** 35.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_xml_21500_blastn_001_record` **(Many-Argument Workhorses)** (Impact: 154.5)
  * `check_xml_21500_blastp_001_record` **(Many-Argument Workhorses)** (Impact: 96.0)
  * `check_xml_2222_blastx_001` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `check_xml_21500_tblastn_001_record` **(Many-Argument Workhorses)** (Impact: 70.0)
  * `check_xml_21500_psiblast_001_record` **(Many-Argument Workhorses)** (Impact: 65.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 862
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 482`, `args: 93`, `func_start: 76`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 728`, `unreferenced_by_name: 49`
* *Architecture:* `io: 118`, `api: 84`, `import: 7`
* *Defense:* `doc: 234`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bio, Bio.SeqRecord, io, numpy, os, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/test_GenBank.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.921)
- **Top Global Matches:** file_cluster_15: 6.921, file_cluster_12: 7.935, file_cluster_2: 8.533
- **Magnitude:** 1955.5 | **LOC:** 8642 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.3%), Connectivity (formerly Api Exposure) (10.4%), Complexity Load (formerly Cognitive Load) (7.1%)
- **Documentation Coverage:** 47.5728% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_record_parser_07` **(I/O & Config Routines)** (Impact: 52.8)
  * `test_record_parser_14` **(I/O & Config Routines)** (Impact: 30.3)
  * `test_feature_parser_02` **(I/O & Config Routines)** (Impact: 26.9)
  * `perform_feature_parser_test` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `perform_record_parser_test` **(Many-Argument Workhorses)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 1051
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 370`, `args: 103`, `func_start: 103`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 781`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 94`
* *Architecture:* `io: 70`, `api: 110`, `import: 15`
* *Defense:* `safety: 2`, `doc: 284`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Bio, Bio.Seq, Bio.SeqFeature, Bio.SeqRecord, datetime, io, os, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/Seq.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.654)
- **Top Global Matches:** file_cluster_12: 7.654, file_cluster_15: 8.535, file_cluster_4: 8.952
- **Magnitude:** 1826.84 | **LOC:** 3279 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **124** in-repo importer(s); it depends on **10**; blast radius 28.718; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (88.2%), Guard Balance (formerly Safety Score) (63.7%), Complexity Load (formerly Cognitive Load) (47.3%)
- **Documentation Coverage:** 15.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_translate_str` **(Many-Argument Workhorses)** (Impact: 110.7)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 64.1)
  * `__getitem__` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `count_overlap` **(Many-Argument Workhorses)** (Impact: 23.7)
    * *Intent:* """Return an overlapping count. Returns an integer, the number of occurrences of substring argument ...
  * `search` **(Defensive Guards)** (Impact: 19.3)
    * *Intent:* """Search the substrings subs in self and yield the index and substring found. Arguments: - subs - a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 664
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 396`, `args: 136`, `func_start: 136`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 244`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 93`, `import: 18`
* *Defense:* `safety: 176`, `doc: 116`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.718
  * `Choke Point (Betweenness):` 0.000302 | `Ripple Effect (Closeness):` 0.13475
  * `Imports (Out-Degree: 4):` Bio, Bio.Data, Bio.SeqRecord, Bio._utils, abc, collections, doctest, numbers...
  * `Imported By (In-Degree: 124):` (Excluded from Brief to save tokens)

### `Bio/codonalign/codonseq.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.279)
- **Top Global Matches:** file_cluster_8: 7.279, file_cluster_6: 14.976, file_cluster_3: 23.219
- **Magnitude:** 1776.78 | **LOC:** 1320 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.9%)
- **Documentation Coverage:** 24.4898% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_count_diff_YN00` **(Many-Argument Workhorses)** (Impact: 134.5)
    * *Intent:* """Count differences between two codons (three-letter string; PRIVATE). The function will weighted m...
  * `_yn00` **(Many-Argument Workhorses)** (Impact: 65.8)
    * *Intent:* ################################################################# # private functions for YN00 metho...
  * `_count_diff_NG86` **(Many-Argument Workhorses)** (Impact: 65.0)
    * *Intent:* """Count differences between two codons, three-letter string (PRIVATE). The function will take multi...
  * `_q` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* """Q matrix for codon substitution (PRIVATE). Arguments: - i, j : three letter codon string - pi : e...
  * `cal_dn_ds` **(Many-Argument Workhorses)** (Impact: 56.2)
    * *Intent:* """Calculate dN and dS of the given two sequences. Available methods: - NG86 - `Nei and Gojobori (19...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 263 instances
* *State Mutation (weighted view):* 804
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 137`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 278`, `dead_code: 4`, `planned_debt: 3`
* *Architecture:* `api: 17`, `import: 13`
* *Defense:* `safety: 27`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002627
  * `Imports (Out-Degree: 4):` Bio.Data, Bio.Seq, Bio.SeqRecord, Bio._utils, collections, itertools, math, numpy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bio/Align/analysis.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.51)
- **Top Global Matches:** file_cluster_8: 8.51, file_cluster_6: 17.178, file_cluster_3: 21.77
- **Magnitude:** 1732.0 | **LOC:** 1300 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.596; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.3%)
- **Documentation Coverage:** 17.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_count_diff_YN00` **(Many-Argument Workhorses)** (Impact: 104.0)
    * *Intent:* """Count differences between two codons (three-letter string; PRIVATE). The function will weighted m...
  * `calculate_dn_ds` **(Many-Argument Workhorses)** (Impact: 59.9)
    * *Intent:* """Calculate dN and dS of the given two sequences. Available methods: - NG86 - `Nei and Gojobori (19...
  * `_q` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* """Q matrix for codon substitution (PRIVATE). Arguments: - codon1, codon2 : three letter codon strin...
  * `_yn00` **(Many-Argument Workhorses)** (Impact: 51.2)
    * *Intent:* ################################################################# # private functions for YN00 metho...
  * `count_TV` **(Many-Argument Workhorses)** (Impact: 50.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 285 instances
* *State Mutation (weighted view):* 894
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 135`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 324`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 7`, `import: 19`
* *Defense:* `safety: 15`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.596
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000876
  * `Imports (Out-Degree: 4):` Bio.Align, Bio.Data, Bio.Phylo.TreeConstruction, Bio._utils, collections, heapq, itertools, math...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bio/Restriction/Restriction.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.555)
- **Top Global Matches:** file_cluster_12: 7.555, file_cluster_15: 8.755, file_cluster_16: 9.172
- **Magnitude:** 1601.32 | **LOC:** 2639 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 1.359; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 2.027% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elucidate` **(Compute Cores)** (Impact: 40.1)
    * *Intent:* """Return a string representing the recognition site and cuttings. Return a representation of the si...
  * `search` **(Defensive Guards)** (Impact: 23.5)
    * *Intent:* """Return a dic of cutting sites in the seq for the batch enzymes."""
  * `show_only_between` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* """Return only results from within start, end. Enzymes must cut inside start/end and may also cut ou...
  * `change` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* """Change parameters of print output. It is possible to change the width of the shell by setting sel...
  * `_mod2` **(Stateful Encapsulated Methods)** (Impact: 18.6)
    * *Intent:* """Test if other enzyme produces compatible ends for enzyme (PRIVATE). For internal use only. Test f...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 174 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 538
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 428`, `args: 166`, `func_start: 166`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 6`, `state_mutation: 190`, `dead_code: 2`, `planned_debt: 25`, `duplicate_logic: 21`
* *Architecture:* `api: 148`, `import: 11`
* *Defense:* `safety: 34`, `doc: 185`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.359
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.002802
  * `Imports (Out-Degree: 3):` Bio, Bio.Restriction.PrintFormat, Bio.Restriction.Restriction_Dictionary, Bio.Seq, itertools, re, string, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Tests/test_Align_psl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.162)
- **Top Global Matches:** file_cluster_6: 7.162, file_cluster_4: 9.376, file_cluster_15: 16.432
- **Magnitude:** 1589.18 | **LOC:** 13780 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.4%), Connectivity (formerly Api Exposure) (7.3%), Complexity Load (formerly Cognitive Load) (3.5%)
- **Documentation Coverage:** 11.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_reading_psl_34_001` **(Many-Argument Workhorses)** (Impact: 200.2)
    * *Intent:* """Check parsing psl_34_001.psl or pslx_34_001.pslx."""
  * `check_reading_psl_34_005` **(Many-Argument Workhorses)** (Impact: 200.2)
    * *Intent:* """Check parsing psl_34_005.psl or pslx_34_005.pslx."""
  * `check_reading_psl_34_004` **(Many-Argument Workhorses)** (Impact: 173.4)
    * *Intent:* """Check parsing psl_34_004.psl or pslx_34_004.pslx."""
  * `check_reading_psl_35_001` **(Many-Argument Workhorses)** (Impact: 61.3)
    * *Intent:* """Check parsing psl_35_001.psl or pslx_35_001.pslx."""
  * `check_reading_psl_34_003` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* """Check parsing psl_34_003.psl or pslx_34_003.pslx."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 105`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 347`, `unreferenced_by_name: 18`
* *Architecture:* `io: 9`, `api: 31`, `import: 15`
* *Defense:* `safety: 4`, `doc: 416`, `test: 28`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Bio, Bio.Align, Bio.Seq, Bio.SeqFeature, Bio.SeqRecord, io, numpy, tempfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/GenBank/Scanner.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.214)
- **Top Global Matches:** file_cluster_8: 6.214, file_cluster_6: 16.937, file_cluster_3: 19.893
- **Magnitude:** 1478.12 | **LOC:** 1930 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.85; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%), Complexity Load (formerly Cognitive Load) (59.8%)
- **Documentation Coverage:** 36.9565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_feed_header_lines` **(Many-Argument Workhorses)** (Impact: 162.7)
    * *Intent:* # Following dictionary maps GenBank lines to the associated # consumer methods - the special cases l...
  * `_feed_first_line` **(Many-Argument Workhorses)** (Impact: 138.8)
    * *Intent:* """Scan over and parse GenBank LOCUS line (PRIVATE). This must cope with several variants, primarily...
  * `_feed_header_lines` **(Many-Argument Workhorses)** (Impact: 62.4)
  * `parse_feature` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `parse_features` **(Many-Argument Workhorses)** (Impact: 42.4)
    * *Intent:* """Return list of tuples for the features (if present). Each feature is returned as a tuple (key, lo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 187 instances
* *State Mutation (weighted view):* 617
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 142`, `args: 30`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 243`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 12`
* *Architecture:* `io: 2`, `api: 17`, `import: 10`
* *Defense:* `safety: 38`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.85
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.003503
  * `Imports (Out-Degree: 6):` Bio, Bio.File, Bio.GenBank, Bio.GenBank.utils, Bio.Seq, Bio.SeqRecord, collections, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bio/Graphics/GenomeDiagram/_LinearDrawer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.719)
- **Top Global Matches:** file_cluster_4: 7.719, file_cluster_6: 11.343, file_cluster_12: 11.467
- **Magnitude:** 1466.38 | **LOC:** 1585 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.1%)
- **Documentation Coverage:** 6.9767% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw_cross_link` **(Many-Argument Workhorses)** (Impact: 129.8)
    * *Intent:* """Draw cross-link between two features."""
  * `draw_scale` **(Many-Argument Workhorses)** (Impact: 53.3)
    * *Intent:* """Draw scale. Argument: - track Track object Returns a tuple of (list of elements in the scale, lis...
  * `get_feature_sigil` **(Many-Argument Workhorses)** (Impact: 45.5)
    * *Intent:* """Get feature sigil. Arguments: - feature Feature object - x0 Start X coordinate on diagram - x1 En...
  * `draw_tick` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* """Draw tick. Arguments: - tickpos Int, position of the tick on the sequence - ctr Float, Y co-ord o...
  * `draw_greytrack` **(Many-Argument Workhorses)** (Impact: 28.1)
    * *Intent:* """Draw greytrack. Arguments: - track Track object Put in a grey background to the current track in ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 268 instances
* *State Mutation (weighted view):* 881
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 102`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 345`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 20`, `import: 17`
* *Defense:* `safety: 8`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.749
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.003408
  * `Imports (Out-Degree: 3):` ._AbstractDrawer, ._FeatureSet, ._GraphSet, math, reportlab.graphics.shapes, reportlab.lib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Tests/test_SwissProt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.657)
- **Top Global Matches:** file_cluster_6: 8.657, file_cluster_8: 10.884, file_cluster_4: 15.742
- **Magnitude:** 1462.56 | **LOC:** 6789 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.9%), Complexity Load (formerly Cognitive Load) (7.8%), Connectivity (formerly Api Exposure) (6.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_P04439` **(Many-Argument Workhorses)** (Impact: 332.6)
    * *Intent:* """Parsing SwissProt file P04439.txt."""
  * `test_P62258` **(I/O & Config Routines)** (Impact: 58.4)
    * *Intent:* """Parsing SwissProt file P62258."""
  * `test_P16235` **(Many-Argument Workhorses)** (Impact: 54.5)
    * *Intent:* """Parsing SwissProt file P16235.txt."""
  * `test_O95832` **(I/O & Config Routines)** (Impact: 43.9)
    * *Intent:* """Parsing SwissProt file O95832.txt."""
  * `test_Q13454` **(I/O & Config Routines)** (Impact: 37.8)
    * *Intent:* """Parsing SwissProt file Q13454.txt."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 655
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 556`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 629`, `unreferenced_by_name: 18`
* *Architecture:* `io: 73`, `api: 19`, `import: 5`
* *Defense:* `doc: 19`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bio, Bio.SeqRecord, os, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/PDB/PICIO.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.73)
- **Top Global Matches:** file_cluster_8: 8.73, file_cluster_6: 16.889, file_cluster_3: 22.364
- **Magnitude:** 1397.84 | **LOC:** 1120 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.607; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (59.2%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_PIC` **(Many-Argument Workhorses)** (Impact: 443.5)
    * *Intent:* # @profile
  * `write_PIC` **(Many-Argument Workhorses)** (Impact: 62.5)
  * `default_dihedron` **(Many-Argument Workhorses)** (Impact: 60.6)
    * *Intent:* """Create Dihedron based on same residue class dihedra in ref database. Adds Dihedron to current Cha...
  * `dihedra_check` **(Compute Cores)** (Impact: 58.7)
    * *Intent:* """Look for required dihedra in residue, generate defaults if set."""
  * `read_PIC_seq` **(Many-Argument Workhorses)** (Impact: 37.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 157 instances
* *State Mutation (weighted view):* 511
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 102`, `args: 20`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 197`, `fragile_debt: 1`
* *Architecture:* `api: 17`, `import: 27`
* *Defense:* `safety: 8`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.607
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001751
  * `Imports (Out-Degree: 10):` Bio, Bio.Data.PDBData, Bio.File, Bio.PDB.PDBExceptions, Bio.PDB.Residue, Bio.PDB.Structure, Bio.PDB.StructureBuilder, Bio.PDB.ic_data...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Bio/Nexus/Trees.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.813)
- **Top Global Matches:** file_cluster_6: 6.813, file_cluster_4: 9.041, file_cluster_12: 16.056
- **Magnitude:** 1359.66 | **LOC:** 996 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (47.6%)
- **Documentation Coverage:** 10.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_string` **(Many-Argument Workhorses)** (Impact: 103.9)
  * `root_with_outgroup` **(Compute Cores)** (Impact: 57.6)
    * *Intent:* """Define a tree's root with a reference group outgroup."""
  * `is_compatible` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* """Compare branches with support>threshold for compatibility. result = is_compatible(self,tree2,thre...
  * `_parse` **(Many-Argument Workhorses)** (Impact: 44.8)
    * *Intent:* """Parse (a,b,c...)[[[xx]:]yy] into subcomponents and travels down recursively (PRIVATE)."""
  * `consensus` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* """Compute a majority rule consensus tree of all clades with relative frequency>=threshold from a li...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 111`, `args: 43`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 206`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 36`, `import: 4`
* *Defense:* `safety: 12`, `doc: 45`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.808
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.005201
  * `Imports (Out-Degree: 1):` .Nodes, random, re, sys
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bio/Blast/_parser.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.75)
- **Top Global Matches:** file_cluster_12: 7.75, file_cluster_16: 8.561, file_cluster_15: 10.275
- **Magnitude:** 1352.24 | **LOC:** 1227 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.783; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (75.3%), Guard Balance (formerly Safety Score) (69.9%), Connectivity (formerly Api Exposure) (27.5%)
- **Documentation Coverage:** 96.4187% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_end_hsp` **(Defensive Guards)** (Impact: 40.2)
  * `_startElementHandler` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* """Found XML start tag. Arguments: - name -- name of the tag - attributes -- tag attributes """...
  * `_end_query_frame` **(Stateful Encapsulated Methods)** (Impact: 16.5)
  * `_end_hit_frame` **(Stateful Encapsulated Methods)** (Impact: 16.3)
  * `__repr__` **(Defensive Guards)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 632
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 396`, `args: 188`, `func_start: 188`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 430`
* *Architecture:* `io: 9`, `api: 174`, `import: 15`
* *Defense:* `safety: 137`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.783
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.002002
  * `Imports (Out-Degree: 6):` Bio, Bio.Align, Bio.Blast, Bio.Seq, Bio.SeqFeature, Bio.SeqRecord, collections, html...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bio/Entrez/Parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.115)
- **Top Global Matches:** file_cluster_12: 7.115, file_cluster_4: 8.947, file_cluster_15: 9.647
- **Magnitude:** 1347.52 | **LOC:** 1166 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 1.166; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.2%)
- **Documentation Coverage:** 4.0404% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elementDecl` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* """Call a call-back function for each element declaration in a DTD. This is used for each element de...
  * `startElementHandler` **(Many-Argument Workhorses)** (Impact: 60.3)
    * *Intent:* """Handle start of an XML element."""
  * `parse` **(Defensive Guards)** (Impact: 30.3)
    * *Intent:* """Set up the parser and let it read the XML results."""
  * `parse_xsd` **(Defensive Guards)** (Impact: 26.6)
    * *Intent:* """Parse an XSD file."""
  * `read` **(Defensive Guards)** (Impact: 21.5)
    * *Intent:* """Set up the parser and let it read the XML results."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 232 instances
* *State Mutation (weighted view):* 772
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 198`, `args: 59`, `func_start: 59`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 308`, `fragile_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `io: 28`, `api: 46`, `import: 13`
* *Defense:* `safety: 70`, `doc: 70`, `immutability_locks: 9`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.166
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002627
  * `Imports (Out-Degree: 1):` Bio, collections, io, os, platform, urllib.parse, urllib.request, warnings...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bio/Cluster/clustermodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.581)
- **Top Global Matches:** file_cluster_6: 6.581, file_cluster_4: 9.024, file_cluster_16: 16.049
- **Magnitude:** 1346.0 | **LOC:** 2475 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.522; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (61.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyTree_new` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `py_treecluster` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `py_kcluster` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `py_pca` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `py_clustercentroids` **(Many-Argument Workhorses)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 191`, `args: 204`, `func_start: 42`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 214`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.522
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Python.h, cluster.h, float.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/Graphics/GenomeDiagram/_CircularDrawer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.167)
- **Top Global Matches:** file_cluster_6: 6.167, file_cluster_4: 9.742, file_cluster_8: 16.224
- **Magnitude:** 1315.72 | **LOC:** 1732 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 25.5814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_draw_arc_arrow` **(Many-Argument Workhorses)** (Impact: 92.3)
  * `get_feature_sigil` **(Many-Argument Workhorses)** (Impact: 55.4)
    * *Intent:* """Return graphics for feature, and any required label for it. Arguments: - feature Feature object -...
  * `draw_scale` **(Many-Argument Workhorses)** (Impact: 52.9)
    * *Intent:* """Return list of elements in the scale and list of their labels. Arguments: - track Track object ""...
  * `_draw_sigil_jaggy` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `draw_cross_link` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* """Draw a cross-link between features."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 697
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 109`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 285`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 18`, `import: 17`
* *Defense:* `safety: 5`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.749
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.003408
  * `Imports (Out-Degree: 3):` ._AbstractDrawer, ._FeatureSet, ._GraphSet, math, reportlab.graphics.shapes, reportlab.lib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Tests/test_GraphicsBitmaps.py` (PYTHON) | Magnitude: 57.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 40, state_mutation: 18, branch: 16
- `Tests/test_PAML_tools.py` (PYTHON) | Magnitude: 92.9 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 73, state_mutation: 32, io: 29, structural_boundaries: 27
- `Bio/KEGG/Gene/__init__.py` (PYTHON) | Magnitude: 126.5 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 36, core_var_decl: 24, design_snake_case: 24
- `Tests/test_PAML_codeml.py` (PYTHON) | Magnitude: 510.1 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 470, state_mutation: 173, core_var_decl: 147, design_snake_case: 144
- `Tests/test_PDB_Superimposer.py` (PYTHON) | Magnitude: 36.6 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 14, core_var_decl: 13, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `Bio/Phylo/CDAO.py` (PYTHON) | Magnitude: 21.66 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 20, core_var_decl: 7, design_snake_case: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Tests/test_ExPASy_offline.py` (PYTHON) | Magnitude: 6.9 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, test: 4, state_mutation: 3
- `Bio/Phylo/Newick.py` (PYTHON) | Magnitude: 15.18 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, core_var_decl: 7, design_snake_case: 7, structural_boundaries: 6
- `Tests/test_Align_bigmaf.py` (PYTHON) | Magnitude: 642.46 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9877, core_var_decl: 428, design_snake_case: 428, state_mutation: 388
- `Tests/test_motifs.py` (PYTHON) | Magnitude: 391.26 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4394, core_var_decl: 346, design_snake_case: 346, state_mutation: 154
- `Tests/test_align_substitution_matrices.py` (PYTHON) | Magnitude: 325.0 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 2324, state_mutation: 95, core_var_decl: 82, design_snake_case: 82

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Bio/Graphics/Comparative.py` (PYTHON) | Magnitude: 105.2 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 41, structural_boundaries: 35, core_var_decl: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Tests/requires_internet.py` (PYTHON) | Magnitude: 12.24 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, io: 5, safety: 4
- `Tests/test_SearchIO_exonerate.py` (PYTHON) | Magnitude: 446.96 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 2377, core_var_decl: 148, state_mutation: 144, design_snake_case: 143
- `Tests/test_mmtf_online.py` (PYTHON) | Magnitude: 10.14 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, test: 6, import: 5
- `Tests/test_SearchIO_hmmer3_text.py` (PYTHON) | Magnitude: 341.94 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 2502, core_var_decl: 201, state_mutation: 190, design_snake_case: 188

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Bio/SeqFeature.py` (PYTHON) | Magnitude: 1080.34 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 738, structural_boundaries: 291, branch: 211, core_var_decl: 151

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `Bio/AlignIO/MafIO.py` (PYTHON) | Magnitude: 592.14 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 475, branch: 117, state_mutation: 111, core_var_decl: 106

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Bio/Phylo/PAML/_parse_yn00.py` (PYTHON) | Magnitude: 173.82 | Delta: **0.167** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 50, core_var_decl: 26, design_snake_case: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Bio/SearchIO/HmmerIO/_base.py` (PYTHON) | Magnitude: 32.88 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 8, branch: 7, state_mutation: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/deploy_docs.sh` -> Churn: **100.0%** | Cog Load: 39.5403% | Debt: 83.3354%
- `.github/workflows/ci.yml` -> Churn: **93.58%** | Cog Load: 7.1194% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Bio/Align/__init__.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 4140.92
- `Bio/PDB/internal_coords.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 3801.16
- `Tests/test_SeqIO.py` -> **mdehoon** (100.0% isolated ownership) | Magnitude: 2303.96
- `Bio/Nexus/Trees.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 1359.66
- `Bio/codonalign/__init__.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 1110.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Bio/SeqRecord.py` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 100.0%)
- `Bio/Align/__init__.py` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 100.0%)
- `Bio/Seq.py` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 100.0%)
- `Bio/AlignIO/__init__.py` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 99.9984%)
- `Bio/SearchIO/_model/hsp.py` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Bio/__init__.py` -> **Severity: 12.785** (Embedded: 0.2256 * Error Risk: 56.6742%)
- `Bio/_utils.py` -> **Severity: 11.757** (Embedded: 0.147 * Error Risk: 80.0%)
- `Bio/SeqRecord.py` -> **Severity: 9.306** (Embedded: 0.1261 * Error Risk: 73.8015%)
- `Bio/Seq.py` -> **Severity: 8.589** (Embedded: 0.1348 * Error Risk: 63.7424%)
- `Bio/Align/__init__.py` -> **Severity: 6.844** (Embedded: 0.0784 * Error Risk: 87.2849%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Bio/SeqRecord.py` -> **Severity: 876.786** (Blast Radius: 25.905 * Doc Risk: 33.8462%)
- `Bio/Seq.py` -> **Severity: 433.961** (Blast Radius: 28.718 * Doc Risk: 15.1111%)
- `Tests/requires_internet.py` -> **Severity: 356.0** (Blast Radius: 3.56 * Doc Risk: 100.0%)
- `Bio/Data/IUPACData.py` -> **Severity: 350.0** (Blast Radius: 3.5 * Doc Risk: 100.0%)
- `BioSQL/BioSeq.py` -> **Severity: 345.668** (Blast Radius: 5.041 * Doc Risk: 68.5714%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 37546 call pairs -- scoped 24.1%, unique 0.0%, ambiguous 23.5%, external 52.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 36086 | 24.3% | 0.0% | 24.5% | 51.2% |
| c | 1442 | 17.7% | 0.7% | 0.0% | 81.6% |
| shell | 18 | 0.0% | 0.0% | 0.0% | 100.0% |

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
