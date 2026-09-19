# ARCHITECTURAL_BRIEF: biopython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/biopython/biopython.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1115 analyzed artifact(s), 310078 LOC.
- **Load-bearing artifact:** `Bio/Seq.py` -- 119 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Bio/PDB/__init__.py` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Bio/Align/_pairwisealigner.c` at magnitude 8795.64 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 1115 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1299 |
| Total LOC | 310078 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 46.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6283 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2065 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4832 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 62 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 520 | 287655 | 46.6% |
| PLAINTEXT | 417 | 19 | 37.4% |
| XML | 131 | 0 | 11.7% |
| C | 17 | 18503 | 1.5% |
| HTML | 11 | 2551 | 1.0% |
| MARKDOWN | 8 | 0 | 0.7% |
| JSON | 5 | 5 | 0.4% |
| SQLITE | 2 | 717 | 0.2% |
| CSV | 2 | 610 | 0.2% |
| MAKEFILE | 1 | 15 | 0.1% |
| CSS | 1 | 3 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `3.946`
> **Composition Archetype:** `Hub-Coupled App` (z +3.95; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 53%, Large Core Modules (3) 12%, Parameter Forwarders Files 12%, Many-Argument Workhorses Files 6%, Compute Cores Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 685 | 61.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 424 | 38.0% |
| Static: Minified & Vendor Opaque Mass | 6 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1299*

**Composition by Extension & Reason:**
- `.dtd`: 204x Excluded (Unsupported Extension: '.dtd')
- `.ent`: 83x Excluded (Unsupported Extension: '.ent')
- `.fastq`: 59x Excluded (Unsupported Extension: '.fastq')
- `no_extension`: 42x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unresolved Ambiguity (No Retainable Structure)
- `.exn`: 52x Excluded (Unsupported Extension: '.exn')
- `.xml`: 3x Excluded (Saturation: Line 30 exceeds 500 chars), 2x Excluded (Saturation: Line 49 exceeds 500 chars), 2x Excluded (Saturation: Line 50 exceeds 500 chars)
- `.fa`: 44x Excluded (Unsupported Extension: '.fa')
- `.ctl`: 42x Excluded (Unsupported Extension: '.ctl')
- `.png`: 39x Excluded (Explicitly Denied Extension: '.png')
- `.gb`: 38x Excluded (Unsupported Extension: '.gb')
- `.rst`: 36x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bb`: 29x Excluded (Unsupported Extension: '.bb')
- `.id`: 27x Excluded (Unsupported Extension: '.id')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 237 LOC), 1x Excluded (Machine-Generated Source Code Signature: 409 LOC), 1x Excluded (Machine-Generated Source Code Signature: 870 LOC)
- `.cif`: 19x Excluded (Unsupported Extension: '.cif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.8 | 22.5 | 16.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 62.7 | 76.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.1 | 12.6 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.9 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 27.3 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.3 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 21.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 77.2 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 9243 | 360 | 13 | `Bio/Align/_pairwisealigner.c` |
| cleanup | 332 | 69 | 0 | `Tests/test_SeqIO_index.py` |
| guards | 8120 | 389 | 17 | `Bio/Align/_pairwisealigner.c` |
| danger | 4851 | 390 | 12 | `Bio/Align/_pairwisealigner.c` |
| concurrency | 319 | 109 | 0 | `Tests/test_GenBank.py` |
| connectivity | 7935 | 496 | 17 | `Tests/test_SeqIO.py` |
| io | 2709 | 229 | 4 | `Doc/cookbook/Restriction/Restriction.html` |
| crypto | 2 | 2 | 0 | `Bio/SeqIO/GfaIO.py` |
| ipc | 40 | 11 | 0 | `Bio/PDB/DSSP.py` |
| time | 36 | 15 | 0 | `Bio/Blast/NCBIWWW.py` |
| serialization | 14 | 7 | 0 | `Tests/test_SearchIO_model.py` |
| regex | 236 | 55 | 0 | `Bio/Phylo/PAML/_parse_codeml.py` |
| events | 90 | 28 | 0 | `Tests/Blast/html_msgid_29_blastx_001.html` |
| tests | 4586 | 203 | 13 | `Tests/test_seq.py` |
| docs | 11391 | 531 | 20 | `Tests/test_pairwise_aligner.py` |
| debt | 1032 | 200 | 2 | `Bio/Restriction/Restriction.py` |
| mutation | 96235 | 523 | 246 | `Bio/Align/_pairwisealigner.c` |
| dead_code | 3413 | 381 | 9 | `Tests/test_seq.py` |
| credential | 59 | 6 | 0 | `Tests/test_Blast_parser.py` |
| threat | 1004 | 121 | 1 | `Bio/Align/_pairwisealigner.c` |
| ml_ai | 260 | 118 | 1 | `Bio/Cluster/cluster.c` |
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

1. **Seq.py** (`Bio/Seq.py`) — 119 inbound connections
2. **SeqRecord.py** (`Bio/SeqRecord.py`) — 99 inbound connections
3. **_utils.py** (`Bio/_utils.py`) — 84 inbound connections
4. **PDBExceptions.py** (`Bio/PDB/PDBExceptions.py`) — 35 inbound connections
5. **SeqFeature.py** (`Bio/SeqFeature.py`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`Bio/PDB/__init__.py`) — 22 outbound dependencies
2. **internal_coords.py** (`Bio/PDB/internal_coords.py`) — 22 outbound dependencies
3. **common_BioSQL.py** (`Tests/common_BioSQL.py`) — 19 outbound dependencies
4. **test_PDB_internal_coords.py** (`Tests/test_PDB_internal_coords.py`) — 18 outbound dependencies
5. **__init__.py** (`Bio/Align/__init__.py`) — 17 outbound dependencies

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
- `_check_corr` **(Many-Argument Workhorses)** (@ `Bio/codonalign/__init__.py`) -> Impact: **200.1** | LOC: 193

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Tests` | 204 | 49829.64 | 12.09% | 0.0% |
| `Bio/Align` | 27 | 28253.74 | 56.76% | 33.74% |
| `Bio/PDB` | 43 | 16248.38 | 41.33% | 9.96% |
| `Bio/Cluster` | 4 | 9887.64 | 46.66% | 5.3% |
| `Bio/SeqIO` | 20 | 7253.18 | 41.22% | 52.58% |
| `Bio/Phylo` | 15 | 6591.62 | 32.04% | 20.76% |
| `Bio` | 9 | 6557.54 | 45.55% | 42.26% |
| `Bio/Nexus` | 6 | 4649.4 | 41.57% | 36.4% |
| `Bio/Blast` | 5 | 4244.32 | 49.12% | 24.21% |
| `Bio/Graphics/GenomeDiagram` | 11 | 4104.16 | 37.49% | 15.77% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Bio/Nexus/Nodes.py` -> **99.9997%** Exposure
- `BioSQL/BioSeqDatabase.py` -> **99.9997%** Exposure
- `BioSQL/DBUtils.py` -> **99.9977%** Exposure
- `Bio/ExPASy/__init__.py` -> **99.9972%** Exposure
- `Bio/SCOP/Hie.py` -> **99.9925%** Exposure
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
- **Binary Anomalies (X-Ray):** `26` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2640` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Bio/Align/_pairwisealigner.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8795.64 | **LOC:** 7741 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PathGenerator_next_waterman_smith_beyer_global` **(Compute Cores)** (Impact: 107.7)
  * `PathGenerator_next_waterman_smith_beyer_local` **(Compute Cores)** (Impact: 105.7)
  * `Aligner_score` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `Aligner_align` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `PathGenerator_next_gotoh_global` **(Compute Cores)** (Impact: 75.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1920 instances
* *State Mutation (weighted view):* 6131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1673`, `structural_boundaries: 946`, `args: 506`, `func_start: 173`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 2291`, `dead_code: 5`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `immutability_locks: 314`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Python.h, _pairwisealigner.h, float.h, stdbool.h, _arraycore.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/Cluster/cluster.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 7494.44 | **LOC:** 5075 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
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
* *Structure:* `branch: 888`, `structural_boundaries: 213`, `args: 47`, `func_start: 47`
* *Risk/State:* `state_mutation: 1529`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 1`, `doc: 5`, `immutability_locks: 115`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Python.h, cluster.h, float.h, limits.h, math.h, stdlib.h, string.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/Align/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4140.92 | **LOC:** 4968 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.9%)
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
* *Risk/State:* `safety_bypasses: 85`, `state_mutation: 893`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 13`, `api: 54`, `import: 30`
* *Defense:* `safety: 203`, `doc: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Bio, Bio.Align, Bio.Data, Bio.Seq, Bio.SeqRecord, Bio.SeqUtils, Bio._utils, abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/PDB/internal_coords.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3801.16 | **LOC:** 4942 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **22**; blast radius 2.228; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (49.4%)
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
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 821`, `dead_code: 19`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 72`, `import: 25`
* *Defense:* `safety: 87`, `doc: 157`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.228
  * `Choke Point (Betweenness):` 0.00039 | `Ripple Effect (Closeness):` 0.012338
  * `Imports (Out-Degree: 12):` Bio.Data.PDBData, Bio.PDB.Atom, Bio.PDB.Chain, Bio.PDB.PDBIO, Bio.PDB.PDBParser, Bio.PDB.PICIO, Bio.PDB.Residue, Bio.PDB.SCADIO...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Bio/Nexus/Nexus.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2880.22 | **LOC:** 2134 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 1.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Debt Markers (formerly Tech Debt) (86.9%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 2`, `state_mutation: 485`, `dead_code: 12`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 37`
* *Architecture:* `io: 6`, `api: 40`, `import: 14`
* *Defense:* `safety: 33`, `doc: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.003575
  * `Imports (Out-Degree: 4):` , Bio, Bio.Data, Bio.Nexus.StandardData, Bio.Nexus.Trees, Bio.Seq, Bio._utils, copy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Bio/Align/bigbed.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2844.86 | **LOC:** 2244 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.838; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (85.0%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.838
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001787
  * `Imports (Out-Degree: 2):` Bio.Align, Bio.Seq, Bio.SeqRecord, collections, copy, io, itertools, numpy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Tests/Blast/html_msgid_29_blastx_001.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 2566.46 | **LOC:** 568 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.577; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.7%), Connectivity (formerly Api Exposure) (16.3%), Dead Code Surface (formerly Dead Code) (9.9%), Complexity Load (formerly Cognitive Load) (2.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 123`, `args: 316`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `dead_code: 5`
* *Architecture:* `io: 78`, `api: 176`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jig.min.js, InstrumentPageStarterJS.js, blastReq.css, blastReqIE.css, common.css, ie6_or_less.css, main.css, print.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/test_pairwise_aligner.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2504.28 | **LOC:** 22443 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.8%), Connectivity (formerly Api Exposure) (9.7%), Complexity Load (formerly Cognitive Load) (7.4%)
- **Documentation Coverage:** 98.0952% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_aligner_property_gapscores_deprecated` **(Compute Cores)** (Impact: 33.5)
  * `test_gap_here_only_2` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* # Force a bad alignment. # # Forces a bad alignment by having a very expensive gap penalty # where o...
  * `test_gap_here_only_local_2` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* # Force a bad alignment. # # Forces a bad alignment by having a very expensive gap penalty # where o...
  * `test_gap_here_only_local_1` **(Compute Cores)** (Impact: 5.6)
  * `test_gap_here_only_1` **(Type Conversions)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 1864
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 472`, `args: 105`, `func_start: 105`, `class_start: 23`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 1760`, `duplicate_logic: 10`, `unreferenced_by_name: 68`
* *Architecture:* `io: 2`, `api: 128`, `import: 25`
* *Defense:* `safety: 18`, `doc: 764`, `test: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bio, Bio.Align, Bio.Align.substitution_matrices, Bio.Seq, Bio.SeqRecord, array, numpy, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/test_SeqIO.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2303.96 | **LOC:** 5912 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 1.527; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (82.9%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (20.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.4%)
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
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1063`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 182`, `import: 19`
* *Defense:* `safety: 25`, `doc: 56`, `test: 166`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.527
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.00762
  * `Imports (Out-Degree: 3):` Bio, Bio.Align, Bio.AlignIO, Bio.PDB.PDBExceptions, Bio.Seq, Bio.SeqRecord, contextlib, copy...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Bio/Seq.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1826.84 | **LOC:** 3279 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **119** in-repo importer(s); it depends on **11**; blast radius 56.196; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (88.1%), Guard Balance (formerly Safety Score) (84.7%), Complexity Load (formerly Cognitive Load) (47.3%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 56.196
  * `Choke Point (Betweenness):` 0.000166 | `Ripple Effect (Closeness):` 0.102759
  * `Imports (Out-Degree: 2):` Bio, Bio.Data, Bio.Seq, Bio.SeqRecord, Bio._utils, abc, collections, doctest...
  * `Imported By (In-Degree: 119):` (Excluded from Brief to save tokens)

### `Tests/test_GenBank.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1817.9 | **LOC:** 8642 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.7%), Connectivity (formerly Api Exposure) (10.4%), Complexity Load (formerly Cognitive Load) (7.3%)
- **Documentation Coverage:** 47.5728% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_record_parser_07` **(I/O & Config Routines)** (Impact: 52.8)
  * `test_record_parser_14` **(I/O & Config Routines)** (Impact: 30.3)
  * `perform_feature_parser_test` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `perform_record_parser_test` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `do_comparison` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* """Compare two records to see if they are the same. This compares the two GenBank records line by li...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 1051
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 370`, `args: 103`, `func_start: 103`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 781`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 94`
* *Architecture:* `io: 70`, `api: 110`, `import: 15`
* *Defense:* `safety: 2`, `doc: 284`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Bio, Bio.Seq, Bio.SeqFeature, Bio.SeqRecord, datetime, io, os, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/codonalign/codonseq.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1776.78 | **LOC:** 1320 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.962; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.9%)
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
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 278`, `dead_code: 5`, `planned_debt: 3`
* *Architecture:* `api: 17`, `import: 13`
* *Defense:* `safety: 27`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.962
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002681
  * `Imports (Out-Degree: 3):` Bio.Data, Bio.Seq, Bio.SeqRecord, Bio._utils, collections, itertools, math, numpy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bio/Align/analysis.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1732.0 | **LOC:** 1300 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.74; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.3%)
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
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 324`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 7`, `import: 19`
* *Defense:* `safety: 15`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000894
  * `Imports (Out-Degree: 2):` Bio.Align, Bio.Data, Bio.Phylo.TreeConstruction, Bio._utils, collections, heapq, itertools, math...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bio/Restriction/Restriction.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1601.32 | **LOC:** 2639 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 1.453; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 6`, `state_mutation: 190`, `dead_code: 6`, `planned_debt: 25`, `duplicate_logic: 21`
* *Architecture:* `api: 148`, `import: 11`
* *Defense:* `safety: 34`, `doc: 185`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.453
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002681
  * `Imports (Out-Degree: 2):` Bio, Bio.Restriction, Bio.Restriction.PrintFormat, Bio.Restriction.Restriction, Bio.Restriction.Restriction_Dictionary, Bio.Seq, itertools, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Tests/test_Blast_parser.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1589.7 | **LOC:** 15168 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.7%), Connectivity (formerly Api Exposure) (9.2%), Complexity Load (formerly Cognitive Load) (4.9%)
- **Documentation Coverage:** 35.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_xml_21500_psiblast_001_record` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `check_xml_21500_rpsblast_001_record` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `check_xml_21500_blastn_001_record` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `check_xml_21500_tblastx_001_record` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `check_xml_21500_tblastn_001_record` **(Many-Argument Workhorses)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 862
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 482`, `args: 93`, `func_start: 76`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 728`, `unreferenced_by_name: 49`
* *Architecture:* `io: 118`, `api: 84`, `import: 7`
* *Defense:* `doc: 234`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bio, Bio.SeqRecord, io, numpy, os, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/GenBank/Scanner.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1478.12 | **LOC:** 1930 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.873; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.8%)
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
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 243`, `dead_code: 8`, `planned_debt: 9`, `fragile_debt: 12`
* *Architecture:* `io: 2`, `api: 17`, `import: 10`
* *Defense:* `safety: 38`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.873
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.002383
  * `Imports (Out-Degree: 4):` Bio, Bio.File, Bio.GenBank, Bio.GenBank.utils, Bio.Seq, Bio.SeqRecord, collections, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Bio/Graphics/GenomeDiagram/_LinearDrawer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1466.38 | **LOC:** 1585 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.76; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.1%)
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
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 345`, `dead_code: 6`, `planned_debt: 2`
* *Architecture:* `api: 20`, `import: 17`
* *Defense:* `safety: 8`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.76
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001192
  * `Imports (Out-Degree: 3):` ._AbstractDrawer, ._FeatureSet, ._GraphSet, math, reportlab.graphics.shapes, reportlab.lib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Tests/test_SwissProt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1462.56 | **LOC:** 6789 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (7.8%), Connectivity (formerly Api Exposure) (6.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bio, Bio.SeqRecord, os, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/PDB/PICIO.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1397.84 | **LOC:** 1120 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 0.85; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.85
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.009677
  * `Imports (Out-Degree: 7):` Bio, Bio.Data.PDBData, Bio.File, Bio.PDB.PDBExceptions, Bio.PDB.Residue, Bio.PDB.Structure, Bio.PDB.StructureBuilder, Bio.PDB.ic_data...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bio/Nexus/Trees.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1359.66 | **LOC:** 996 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.896; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (47.6%)
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
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 206`, `dead_code: 13`
* *Architecture:* `io: 1`, `api: 36`, `import: 4`
* *Defense:* `safety: 12`, `doc: 45`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.896
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002482
  * `Imports (Out-Degree: 0):` , random, re, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bio/Blast/_parser.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1352.24 | **LOC:** 1227 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.822; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Complexity Load (formerly Cognitive Load) (75.3%), Connectivity (formerly Api Exposure) (27.5%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000894
  * `Imports (Out-Degree: 3):` Bio, Bio.Align, Bio.Blast, Bio.Seq, Bio.SeqFeature, Bio.SeqRecord, collections, html...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bio/Cluster/clustermodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1348.0 | **LOC:** 2475 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyTree_new` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `py_treecluster` **(Many-Argument Workhorses)** (Impact: 48.3)
  * `py_kcluster` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `py_pca` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `py_clustercentroids` **(Many-Argument Workhorses)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 191`, `args: 204`, `func_start: 42`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 214`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Python.h, cluster.h, float.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bio/Entrez/Parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1347.52 | **LOC:** 1166 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 1.313; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Debt Markers (formerly Tech Debt) (80.7%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 308`, `dead_code: 1`, `fragile_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `io: 28`, `api: 46`, `import: 13`
* *Defense:* `safety: 70`, `doc: 70`, `immutability_locks: 9`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.313
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001787
  * `Imports (Out-Degree: 0):` Bio, collections, io, os, platform, urllib.parse, urllib.request, warnings...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Bio/Graphics/GenomeDiagram/_CircularDrawer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1315.72 | **LOC:** 1732 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.76; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.8%)
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
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 285`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 18`, `import: 17`
* *Defense:* `safety: 5`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.76
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001192
  * `Imports (Out-Degree: 3):` ._AbstractDrawer, ._FeatureSet, ._GraphSet, math, reportlab.graphics.shapes, reportlab.lib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bio/Align/_alignmentcounts.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1264.6 | **LOC:** 1695 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.577; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.8%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AlignmentCounts_new` **(Many-Argument Workhorses)** (Impact: 296.1)
  * `add_gaps` **(Many-Argument Workhorses)** (Impact: 72.7)
  * `sequence_converter` **(Stateful Encapsulated Methods)** (Impact: 29.3)
  * `AlignmentCounts_str` **(Compute Cores)** (Impact: 23.6)
  * `AlignmentCounts_repr` **(Compute Cores)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 175 instances
* *State Mutation (weighted view):* 571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 175`, `args: 83`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 221`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Python.h, _pairwisealigner.h, float.h, inttypes.h, stdbool.h, _arraycore.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Bio/PDB/internal_coords.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 3801.16
- `Tests/test_SeqIO.py` -> **mdehoon** (100.0% isolated ownership) | Magnitude: 2303.96
- `Bio/Seq.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 1826.84
- `Bio/Nexus/Trees.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 1359.66
- `Bio/codonalign/__init__.py` -> **Peter J. A. Cock** (100.0% isolated ownership) | Magnitude: 1110.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Bio/PDB/internal_coords.py` -> **Severity: 0.039** (Bridge: 0.0004 * Flux: 100.0%)
- `Bio/SeqRecord.py` -> **Severity: 0.039** (Bridge: 0.0004 * Flux: 100.0%)
- `Bio/PDB/StructureBuilder.py` -> **Severity: 0.037** (Bridge: 0.0004 * Flux: 99.9999%)
- `Bio/PDB/Chain.py` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 99.9992%)
- `Bio/PDB/Model.py` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.1837%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Bio/_utils.py` -> **Severity: 10.667** (Embedded: 0.114 * Error Risk: 93.5492%)
- `Bio/SeqRecord.py` -> **Severity: 9.342** (Embedded: 0.0974 * Error Risk: 95.8919%)
- `Bio/Seq.py` -> **Severity: 8.706** (Embedded: 0.1028 * Error Risk: 84.7258%)
- `BioSQL/BioSeq.py` -> **Severity: 6.39** (Embedded: 0.0647 * Error Risk: 98.6847%)
- `Bio/SeqFeature.py` -> **Severity: 6.338** (Embedded: 0.0705 * Error Risk: 89.9049%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Bio/SeqRecord.py` -> **Severity: 1935.055** (Blast Radius: 57.172 * Doc Risk: 33.8462%)
- `BioSQL/BioSeq.py` -> **Severity: 872.297** (Blast Radius: 12.721 * Doc Risk: 68.5714%)
- `Bio/Seq.py` -> **Severity: 849.183** (Blast Radius: 56.196 * Doc Risk: 15.1111%)
- `Tests/requires_internet.py` -> **Severity: 597.7** (Blast Radius: 5.977 * Doc Risk: 100.0%)
- `Bio/Data/IUPACData.py` -> **Severity: 256.8** (Blast Radius: 2.568 * Doc Risk: 100.0%)

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
