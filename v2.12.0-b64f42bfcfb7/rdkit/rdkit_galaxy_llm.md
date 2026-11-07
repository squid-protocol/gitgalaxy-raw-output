# ARCHITECTURAL_BRIEF: rdkit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rdkit/rdkit.git` |
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
- **Scope:** 2367 analyzed artifact(s), 588201 LOC.
- **Load-bearing artifact:** `Code/GraphMol/RDKitBase.h` -- 432 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Code/MinimalLib/common.h` -- pulls in 51 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Code/GraphMol/Wrap/rough_test.py` at magnitude 5287.78 (structural weight, not risk).
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
| Total Artifacts | 6141 |
| Analyzed Artifacts (Scanned) | 2367 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3774 |
| Total LOC | 588201 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 38.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5123 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1903 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5192 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 84 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1294 | 400303 | 54.7% |
| PYTHON | 518 | 72585 | 21.9% |
| PLAINTEXT | 278 | 0 | 11.7% |
| JAVA | 53 | 8280 | 2.2% |
| CSV | 37 | 3179 | 1.6% |
| MARKDOWN | 32 | 0 | 1.4% |
| POSTGRESQL | 25 | 3993 | 1.1% |
| POWERSHELL | 22 | 80626 | 0.9% |
| C | 20 | 8741 | 0.8% |
| CSHARP | 17 | 1087 | 0.7% |
| JSON | 15 | 276 | 0.6% |
| MAKEFILE | 11 | 216 | 0.5% |
| SQLITE | 9 | 143 | 0.4% |
| YAML | 6 | 372 | 0.3% |
| HTML | 6 | 790 | 0.3% |
| YACC | 6 | 2712 | 0.3% |
| SHELL | 5 | 117 | 0.2% |
| JAVASCRIPT | 4 | 4528 | 0.2% |
| M4 | 3 | 62 | 0.1% |
| XML | 3 | 0 | 0.1% |
| FORTRAN | 2 | 183 | 0.1% |
| DB2_SQL | 1 | 8 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2352 |
| utf-8 | bom | 13 |
| cp1252 | cp1252-fallback | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 20%, Large Core Modules (3) 19%, Declarative / Non-Code 12%, Parameter Forwarders Files 11%, Many-Argument Workhorses Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2056 | 86.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 310 | 13.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3774*

**Composition by Extension & Reason:**
- `.sdf`: 737x Excluded (Unsupported Extension: '.sdf'), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mol`: 556x Excluded (Unsupported Extension: '.mol'), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mrv`: 412x Excluded (Unsupported Extension: '.mrv')
- `.cxsmi`: 357x Excluded (Unsupported Extension: '.cxsmi')
- `.rst`: 271x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 243x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 69x Unsupported Format (.undeterminable), 57x Excluded: Neighborhood Micro-Mass Limit Exceeded, 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cdx`: 119x Excluded (Unsupported Extension: '.CDX'), 7x Excluded (Unsupported Extension: '.cdx')
- `.i`: 101x Unsupported Format (.undeterminable)
- `.xyz`: 91x Excluded (Unsupported Extension: '.xyz')
- `.cdxml`: 5x Zero-Density Threshold (LOC: 208, Signals: 0), 4x Zero-Density Threshold (LOC: 124, Signals: 0), 2x Zero-Density Threshold (LOC: 98, Signals: 0)
- `.smi`: 54x Excluded (Unsupported Extension: '.smi'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pdb`: 48x Excluded (Unsupported Extension: '.pdb')
- `.cpp`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 9564 commas in 1282 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3492 LOC)
- `.rxn`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 21x Excluded (Unsupported Extension: '.rxn')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 28.2 | 17.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.8 | 46.0 | 53.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.2 | 9.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.6 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 56.5 | 87.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 90.2 | 3.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10582 | 1034 | 11 | `Code/MinimalLib/cffi_test.c` |
| cleanup | 1820 | 325 | 1 | `Code/MinimalLib/cffi_test.c` |
| guards | 36177 | 1476 | 40 | `Code/MinimalLib/cffi_test.c` |
| danger | 4729 | 736 | 5 | `Code/GraphMol/FileParsers/MolFileParser.cpp` |
| concurrency | 406 | 106 | 0 | `Code/GraphMol/DistGeomHelpers/Embedder.cpp` |
| connectivity | 7321 | 949 | 8 | `Code/GraphMol/Wrap/rough_test.py` |
| io | 2635 | 400 | 2 | `Code/GraphMol/MolDraw2D/catch_tests.cpp` |
| crypto | 2 | 2 | 0 | `rdkit/Chem/MolKey/MolKey.py` |
| ipc | 158 | 17 | 0 | `Code/GraphMol/molopstest.cpp` |
| time | 166 | 38 | 0 | `Regress/Scripts/timings.py` |
| serialization | 449 | 59 | 0 | `Code/MinimalLib/tests/tests.js` |
| regex | 458 | 74 | 0 | `Code/GraphMol/MolDraw2D/catch_tests.cpp` |
| events | 368 | 57 | 0 | `Regress/Scripts/timings.py` |
| tests | 25872 | 384 | 6 | `Code/GraphMol/molopstest.cpp` |
| docs | 5640 | 644 | 6 | `Code/GraphMol/MolOps.h` |
| debt | 2971 | 473 | 2 | `Code/GraphMol/MolDraw2D/test1.cpp` |
| mutation | 222240 | 1802 | 175 | `Code/GraphMol/test_data/CDXML/chemdraw_template9.cdxml` |
| dead_code | 6926 | 1083 | 8 | `Code/GraphMol/Wrap/rough_test.py` |
| credential | 14 | 7 | 0 | `Code/GraphMol/MolStandardize/Pipeline.h` |
| threat | 1 | 1 | 0 | `Code/GraphMol/MolDraw2D/Qt/catch_qt.cpp` |
| ml_ai | 218 | 95 | 0 | `Code/GraphMol/MolTransforms/MolTransforms.cpp` |
| ui | 207 | 18 | 0 | `rdkit/sping/SVG/pidSVG.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0769**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Code/GraphMol/MolDraw2D/catch_tests.cpp` (Hits: 307)
- `Code/GraphMol/Wrap/rough_test.py` (Hits: 175)
- `Code/GraphMol/MolDraw2D/test1.cpp` (Hits: 134)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **RDKitBase.h** (`Code/GraphMol/RDKitBase.h`) — 432 inbound connections
2. **export.h** (`External/GA/util/export.h`) — 396 inbound connections
3. **__init__.py** (`rdkit/__init__.py`) — 308 inbound connections
4. **SmilesParse.h** (`Code/GraphMol/SmilesParse/SmilesParse.h`) — 252 inbound connections
5. **SmilesWrite.h** (`Code/GraphMol/SmilesParse/SmilesWrite.h`) — 192 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.h** (`Code/MinimalLib/common.h`) — 51 outbound dependencies
2. **adapter.cpp** (`Code/PgSQL/rdkit/adapter.cpp`) — 43 outbound dependencies
3. **cffiwrapper.cpp** (`Code/MinimalLib/cffiwrapper.cpp`) — 40 outbound dependencies
4. **MolFileParser.cpp** (`Code/GraphMol/FileParsers/MolFileParser.cpp`) — 34 outbound dependencies
5. **Embedder.cpp** (`Code/GraphMol/DistGeomHelpers/Embedder.cpp`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseFragment` **(Many-Argument Workhorses)** (@ `External/ChemDraw/fragment.cpp`) -> Impact: **2299.7** | LOC: 973
- `MMFFMolProperties::setMMFFHeavyAtomType` **(Many-Argument Workhorses)** (@ `Code/GraphMol/ForceFieldHelpers/MMFF/AtomTyper.cpp`) -> Impact: **934.4** | LOC: 1575
  * *Intent:* // sets the MMFF atomType for a heavy atom
- `EmbeddedFrag::matchToTemplate` **(Many-Argument Workhorses)** (@ `Code/GraphMol/Depictor/EmbeddedFrag.cpp`) -> Impact: **613.5** | LOC: 1704
- `getTPSAAtomContribs` **(Many-Argument Workhorses)** (@ `Code/GraphMol/Descriptors/MolSurf.cpp`) -> Impact: **586.9** | LOC: 244
- `mmffValidationSuite` **(Many-Argument Workhorses)** (@ `Code/ForceField/MMFF/testMMFFForceField.cpp`) -> Impact: **560.1** | LOC: 1191
- `GenerateFP` **(Many-Argument Workhorses)** (@ `Code/GraphMol/Fingerprints/MACCS.cpp`) -> Impact: **495.4** | LOC: 625
- `addAtomChargeFlags` **(Many-Argument Workhorses)** (@ `Code/GraphMol/ForceFieldHelpers/UFF/AtomTyper.cpp`) -> Impact: **435.3** | LOC: 386
  * *Intent:* // ---------------------------------------------------------------
- `parseNode` **(Many-Argument Workhorses)** (@ `External/ChemDraw/node.cpp`) -> Impact: **356.7** | LOC: 289
- `parse_fragment` **(Many-Argument Workhorses)** (@ `Code/GraphMol/FileParsers/CDXMLParser.cpp`) -> Impact: **336.1** | LOC: 353
- `AddMol` **(Many-Argument Workhorses)** (@ `rdkit/Chem/Draw/MolDrawing.py`) -> Impact: **329.2** | LOC: 238

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Code/GraphMol` | 99 | 36904.9 | 32.89% | 22.11% |
| `Code/GraphMol/FileParsers` | 75 | 24777.02 | 35.67% | 23.35% |
| `rdkit/Chem` | 71 | 14133.42 | 42.43% | 51.93% |
| `Code/GraphMol/MolDraw2D` | 54 | 12436.04 | 30.51% | 35.34% |
| `Code/GraphMol/SmilesParse` | 26 | 11532.22 | 33.62% | 13.59% |
| `Code/GraphMol/Wrap` | 56 | 9395.0 | 17.04% | 27.07% |
| `Code/GraphMol/Descriptors` | 70 | 8356.36 | 25.86% | 18.73% |
| `Code/GraphMol/MolStandardize` | 27 | 6447.86 | 28.92% | 20.78% |
| `Code/GraphMol/Fingerprints` | 29 | 6325.58 | 27.33% | 28.93% |
| `Code/PgSQL/rdkit` | 21 | 5724.5 | 32.79% | 17.66% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Code/Features/Feature.h` -> **100.0%** Exposure
- `Code/GraphMol/CIPLabeler/Edge.cpp` -> **100.0%** Exposure
- `Code/GraphMol/CIPLabeler/Node.cpp` -> **100.0%** Exposure
- `rdkit/Chem/FragmentMatcher.py` -> **100.0%** Exposure
- `Code/Demos/boost/smartPtrsAndIters/test.py` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Code/DataManip/MetricMatrixCalc/testMatCalc.cpp` -> **100.0%** Exposure
- `Code/DataStructs/DiscreteDistMat.cpp` -> **100.0%** Exposure
- `Code/DataStructs/SparseIntVect.h` -> **100.0%** Exposure
- `Code/DataStructs/Utils.cpp` -> **100.0%** Exposure
- `Code/DataStructs/base64.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Code/GraphMol/Wrap/rough_test.py` -> **288** Orphaned Functions | **8** Duplicates
- `Code/GraphMol/MarvinParse/MarvinDefs.cpp` -> **135** Orphaned Functions | **0** Duplicates
- `Code/MinimalLib/minilib.cpp` -> **101** Orphaned Functions | **0** Duplicates
- `Code/PgSQL/rdkit/adapter.cpp` -> **89** Orphaned Functions | **0** Duplicates
- `Code/GraphMol/AtomIterators.cpp` -> **77** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `18` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12191` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Code/GraphMol/Wrap/rough_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.605)
- **Top Global Matches:** file_cluster_15: 6.605, file_cluster_12: 7.049, file_cluster_16: 8.359
- **Magnitude:** 5287.78 | **LOC:** 8717 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.4%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 90.8824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test25SDMolSupplier` **(I/O & Config Routines)** (Impact: 32.2)
  * `test88QueryAtoms` **(Type Conversions)** (Impact: 27.7)
  * `testContextManagers` **(Compute Cores)** (Impact: 26.5)
  * `testBondSetStereoAllHalogens` **(Compute Cores)** (Impact: 23.7)
    * *Intent:* # can't get much more brutal than this test from itertools import combinations, permutations halogen...
  * `test7Atom` **(Compute Cores)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 576 instances
* *High Risk Execution (weighted view):* 12
* *State Mutation (weighted view):* 3267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 669`, `args: 367`, `func_start: 341`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 17`, `state_mutation: 2115`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 288`
* *Architecture:* `io: 175`, `api: 337`, `import: 36`
* *Defense:* `safety: 70`, `doc: 65`, `test: 39`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` contextlib, copy, datetime, doctest, gc, gzip, importlib.util, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Chirality.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.639)
- **Top Global Matches:** file_cluster_8: 5.639, file_cluster_6: 15.832, file_cluster_3: 21.0
- **Magnitude:** 3871.22 | **LOC:** 3958 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.6%), Guard Balance (formerly Safety Score) (68.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.9%)
- **Documentation Coverage:** 98.7179% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assignNontetrahedralChiralTypeFrom3D` **(Many-Argument Workhorses)** (Impact: 237.5)
    * *Intent:* // The tolerance here is pretty high in order to accomodate things coming from // the dgeom code As ...
  * `legacyStereoPerception` **(Many-Argument Workhorses)** (Impact: 220.1)
    * *Intent:* */
  * `atomChiralTypeFromBondDirPseudo3D` **(Many-Argument Workhorses)** (Impact: 184.9)
  * `updateDoubleBondNeighbors` **(Many-Argument Workhorses)** (Impact: 137.8)
  * `assignChiralTypesFrom3D` **(Many-Argument Workhorses)** (Impact: 96.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 405 instances
* *State Mutation (weighted view):* 1230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1137`, `structural_boundaries: 338`, `args: 148`, `func_start: 78`, `class_start: 2`
* *Risk/State:* `state_mutation: 420`, `dead_code: 1`, `unreferenced_by_name: 18`
* *Architecture:* `import: 19`
* *Defense:* `safety: 8`, `doc: 3`, `immutability_locks: 182`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000814
  * `Imports (Out-Degree: 16):` Chirality.h, point.h, Atropisomers.h, QueryOps.h, RDKitBase.h, new_canon.h, Invariant.h, RDLog.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Code/GraphMol/ForceFieldHelpers/MMFF/AtomTyper.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.612)
- **Top Global Matches:** file_cluster_6: 6.612, file_cluster_4: 11.35, file_cluster_8: 14.742
- **Magnitude:** 3642.68 | **LOC:** 3731 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 0.225; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MMFFMolProperties::setMMFFHeavyAtomType` **(Many-Argument Workhorses)** (Impact: 934.4)
    * *Intent:* // sets the MMFF atomType for a heavy atom
  * `MMFFMolProperties::getMMFFTorsionEmpiricalRuleParams` **(Many-Argument Workhorses)** (Impact: 205.4)
    * *Intent:* // empirical rule to compute torsional parameters if // tabulated parameters could not be found // t...
  * `MMFFMolProperties::computeMMFFCharges` **(Many-Argument Workhorses)** (Impact: 168.0)
    * *Intent:* // populates the MMFFMolProperties object with MMFF // formal and partial charges
  * `getMMFFAngleBendEmpiricalRuleParams` **(Many-Argument Workhorses)** (Impact: 147.9)
    * *Intent:* // empirical rule to compute angle bending parameters if // tabulated parameters could not be found....
  * `MMFFMolProperties::setMMFFHydrogenType` **(Compute Cores)** (Impact: 98.8)
    * *Intent:* // finds the MMFF atomType for a hydrogen atom
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 480 instances
* *State Mutation (weighted view):* 1467
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1011`, `structural_boundaries: 77`, `args: 67`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `state_mutation: 507`, `dead_code: 9`, `unreferenced_by_name: 21`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 237`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.225
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.003282
  * `Imports (Out-Degree: 8):` AtomTyper.h, Nonbonded.h, MolOps.h, QueryOps.h, RDKitBase.h, Invariant.h, RDLog.h, dynamic_bitset.hpp...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `Code/GraphMol/FileParsers/MolFileParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.593)
- **Top Global Matches:** file_cluster_8: 5.593, file_cluster_6: 12.997, file_cluster_4: 21.747
- **Magnitude:** 3518.68 | **LOC:** 3779 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.174; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.9%), Guard Balance (formerly Safety Score) (62.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseV3000AtomProps` **(Many-Argument Workhorses)** (Impact: 270.9)
  * `ParseMolBlockProperties` **(Many-Argument Workhorses)** (Impact: 234.5)
  * `ParseV3000CTAB` **(Many-Argument Workhorses)** (Impact: 219.9)
  * `ParseV3000BondBlock` **(Many-Argument Workhorses)** (Impact: 175.9)
  * `ParseMolFileAtomLine` **(Many-Argument Workhorses)** (Impact: 169.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 349 instances
* *Memory Alloc (weighted view):* 24
* *State Mutation (weighted view):* 1097
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 938`, `structural_boundaries: 174`, `args: 99`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 399`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `import: 34`
* *Defense:* `safety: 137`, `doc: 1`, `test: 1`, `immutability_locks: 72`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.174
  * `Choke Point (Betweenness):` 0.000334 | `Ripple Effect (Closeness):` 0.015645
  * `Imports (Out-Degree: 23):` FileParserUtils.h, FileParsers.h, Atropisomers.h, Chirality.h, MolFileStereochem.h, GenericGroups.h, QueryOps.h, RDKitQueries.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Code/GraphMol/MolDraw2D/DrawMol.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.257)
- **Top Global Matches:** file_cluster_6: 7.257, file_cluster_8: 10.549, file_cluster_4: 14.724
- **Magnitude:** 3411.34 | **LOC:** 4077 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **23**; blast radius 0.229; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%), Guard Balance (formerly Safety Score) (72.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DrawMol::getAtomSymbol` **(Many-Argument Workhorses)** (Impact: 110.8)
    * *Intent:* // ****************************************************************************
  * `DrawMol::makeQueryBond` **(Many-Argument Workhorses)** (Impact: 59.1)
    * *Intent:* // ****************************************************************************
  * `DrawMol::transformAll` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* // ****************************************************************************
  * `DrawMol::getAtomOrientation` **(Compute Cores)** (Impact: 57.1)
    * *Intent:* // ****************************************************************************
  * `DrawMol::bondNonRing` **(Many-Argument Workhorses)** (Impact: 51.5)
    * *Intent:* // **************************************************************************** // bond is not in a ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 495 instances
* *Memory Alloc (weighted view):* 32
* *State Mutation (weighted view):* 1634
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 854`, `structural_boundaries: 378`, `args: 121`, `func_start: 106`
* *Risk/State:* `state_mutation: 644`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 73`
* *Architecture:* `import: 23`
* *Defense:* `safety: 17`, `immutability_locks: 239`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.229
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.002815
  * `Imports (Out-Degree: 30):` Transform2D.h, Transform3D.h, Atropisomers.h, Chirality.h, RDDepictor.h, FileParserUtils.h, MolFileStereochem.h, MolSGroupParsing.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Code/GraphMol/SmilesParse/CXSmilesOps.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.854)
- **Top Global Matches:** file_cluster_8: 11.854, file_cluster_3: 12.726, file_cluster_6: 24.38
- **Magnitude:** 2950.18 | **LOC:** 2650 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_it` **(Many-Argument Workhorses)** (Impact: 236.3)
  * `get_bond_config_block` **(Many-Argument Workhorses)** (Impact: 192.5)
  * `parse_polymer_sgroup` **(Many-Argument Workhorses)** (Impact: 108.5)
  * `parse_wedged_bonds` **(Many-Argument Workhorses)** (Impact: 98.3)
  * `get_ringbond_cistrans_block` **(Many-Argument Workhorses)** (Impact: 76.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 254 instances
* *State Mutation (weighted view):* 766
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 871`, `structural_boundaries: 369`, `args: 77`, `func_start: 54`
* *Risk/State:* `state_mutation: 258`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `import: 19`
* *Defense:* `safety: 4`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Atropisomers.h, Chirality.h, MolFileStereochem.h, LinkNode.h, RDKitBase.h, RDKitQueries.h, BoostEndInclude.h, BoostStartInclude.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rdkit/Chem/fmcs/fmcs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.624)
- **Top Global Matches:** file_cluster_4: 7.624, file_cluster_12: 9.921, file_cluster_5: 12.233
- **Magnitude:** 2558.08 | **LOC:** 2825 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.352; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.2%), Guard Balance (formerly Safety Score) (85.4%), Connectivity (formerly Api Exposure) (54.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 138.9)
  * `enumerate_subgraphs` **(Many-Argument Workhorses)** (Impact: 87.5)
    * *Intent:* ###### The engine of the entire system. Enumerate subgraphs and see if they match. #####
  * `fmcs` **(Many-Argument Workhorses)** (Impact: 80.4)
  * `check_completeRingsOnly` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* ### Check if there are any ring atoms; used in --complete-rings-only # This is (yet) another depth-f...
  * `compute_mcs` **(Many-Argument Workhorses)** (Impact: 42.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 406 instances
* *State Mutation (weighted view):* 1355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 318`, `args: 108`, `func_start: 100`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 543`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 4`
* *Architecture:* `io: 15`, `api: 94`, `import: 12`
* *Defense:* `safety: 41`, `doc: 1`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000814
  * `Imports (Out-Degree: 1):` argparse, collections, copy, fractions, heapq, itertools, rdkit, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Code/GraphMol/MarvinParse/MarvinDefs.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.585)
- **Top Global Matches:** file_cluster_4: 7.585, file_cluster_15: 10.14, file_cluster_11: 11.232
- **Magnitude:** 2374.84 | **LOC:** 4286 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.161; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.7%), Debt Markers (formerly Tech Debt) (85.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MarvinMolBase::parseAtomsAndBonds` **(Many-Argument Workhorses)** (Impact: 210.0)
  * `MarvinSuperatomSgroup::convertFromOneSuperAtom` **(I/O & Config Routines)** (Impact: 50.7)
  * `MarvinSuperatomSgroupExpanded::convertToOneSuperAtom` **(I/O & Config Routines)** (Impact: 48.9)
  * `MarvinMultipleSgroup::contractOneMultipleSgroup` **(I/O & Config Routines)** (Impact: 48.0)
  * `MarvinMultipleSgroup::expandOneMultipleSgroup` **(I/O & Config Routines)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 326 instances
* *Memory Alloc (weighted view):* 30
* *State Mutation (weighted view):* 1062
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 634`, `structural_boundaries: 424`, `args: 115`, `func_start: 169`
* *Risk/State:* `state_mutation: 410`, `dead_code: 1`, `unreferenced_by_name: 135`
* *Architecture:* `import: 5`
* *Defense:* `safety: 25`, `immutability_locks: 133`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000915
  * `Imports (Out-Degree: 5):` MarvinDefs.h, BoostEndInclude.h, BoostStartInclude.h, RDLog.h, string.hpp
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Code/GraphMol/FileParsers/SequenceParsers.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.532)
- **Top Global Matches:** file_cluster_3: 11.532, file_cluster_8: 13.077, file_cluster_6: 25.689
- **Magnitude:** 2360.18 | **LOC:** 1907 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreateAminoAcid` **(Many-Argument Workhorses)** (Impact: 322.4)
    * *Intent:* // aa is a three letter PDB residue code
  * `LookupHELMPeptideMonomer` **(Compute Cores)** (Impact: 223.7)
  * `AASequenceToMol` **(Many-Argument Workhorses)** (Impact: 211.8)
  * `ParseHELM` **(Compute Cores)** (Impact: 211.2)
  * `ParseHELMNucleic` **(Many-Argument Workhorses)** (Impact: 103.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 821
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 713`, `structural_boundaries: 145`, `args: 57`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 367`, `dead_code: 1`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` GraphMol.h, MolOps.h, MonomerInfo.h, SequenceParsers.h, cstring, map, string, vector
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Depictor/EmbeddedFrag.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.116)
- **Top Global Matches:** file_cluster_6: 6.116, file_cluster_4: 10.651, file_cluster_8: 14.913
- **Magnitude:** 2350.28 | **LOC:** 2159 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (75.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EmbeddedFrag::matchToTemplate` **(Many-Argument Workhorses)** (Impact: 613.5)
  * `checkStereoChemistry` **(Many-Argument Workhorses)** (Impact: 83.2)
    * *Intent:* // check if the stereochemistry of the template matches the stereochemistry of // the molecule
  * `EmbeddedFrag::randomSampleFlipsAndPermutations` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `EmbeddedFrag::openAngles` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `EmbeddedFrag::mergeWithCommon` **(Many-Argument Workhorses)** (Impact: 46.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 277 instances
* *State Mutation (weighted view):* 890
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 371`, `args: 55`, `func_start: 53`
* *Risk/State:* `state_mutation: 336`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 38`
* *Architecture:* `import: 18`
* *Defense:* `safety: 1`, `immutability_locks: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` DepictUtils.h, EmbeddedFrag.h, Transform2D.h, point.h, Bond.h, MolOps.h, ROMol.h, RWMol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.937)
- **Top Global Matches:** file_cluster_6: 6.937, file_cluster_8: 10.131, file_cluster_4: 14.619
- **Magnitude:** 2324.06 | **LOC:** 1983 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 0.173; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HBond::findAcceptorsUnfixed` **(Many-Argument Workhorses)** (Impact: 160.9)
  * `HBond::findDonorsUnfixed` **(Many-Argument Workhorses)** (Impact: 157.8)
  * `HBond::findAcceptors` **(Many-Argument Workhorses)** (Impact: 114.8)
    * *Intent:* /* General structure of findAcceptors, findAcceptorsUnfixed, findDonors, * findDonorsUnfixed functio...
  * `CoulombDielectric::CoulombDielectric` **(Many-Argument Workhorses)** (Impact: 95.9)
  * `CoulombDielectric::CoulombDielectric` **(Many-Argument Workhorses)** (Impact: 87.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 374 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 94`, `args: 85`, `func_start: 41`
* *Risk/State:* `state_mutation: 447`, `dead_code: 2`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `import: 14`
* *Defense:* `safety: 5`, `immutability_locks: 84`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.173
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.000814
  * `Imports (Out-Degree: 15):` Nonbonded.h, Nonbonded.h, Params.h, UniformRealValueGrid3D.h, point.h, AtomTyper.h, RDKitBase.h, SmilesParse.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.264)
- **Top Global Matches:** file_cluster_6: 6.264, file_cluster_8: 11.726, file_cluster_4: 13.349
- **Magnitude:** 2259.16 | **LOC:** 2251 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_setChain14Bounds` **(Many-Argument Workhorses)** (Impact: 167.6)
  * `set13Bounds` **(Many-Argument Workhorses)** (Impact: 115.8)
  * `_setMacrocycleAllInSameRing14Bounds` **(Many-Argument Workhorses)** (Impact: 108.6)
  * `_setInRing14Bounds` **(Many-Argument Workhorses)** (Impact: 102.5)
  * `set14Bounds` **(Many-Argument Workhorses)** (Impact: 93.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 291 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 948
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 176`, `args: 49`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `state_mutation: 366`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `doc: 15`, `immutability_locks: 153`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000407
  * `Imports (Out-Degree: 13):` BoundsMatrixBuilder.h, BoundsMatrix.h, TriangleSmooth.h, BondStretch.h, Utils.h, Chirality.h, AtomTyper.h, RDKitBase.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Code/GraphMol/MolDraw2D/catch_tests.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.192)
- **Top Global Matches:** file_cluster_15: 7.192, file_cluster_16: 8.762, file_cluster_2: 8.775
- **Magnitude:** 2143.14 | **LOC:** 11099 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.8%), Guard Balance (formerly Safety Score) (48.6%), Mutation Surface (formerly State Flux) (46.5%), Complexity Load (formerly Cognitive Load) (9.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 53.0)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `TEST_CASE` **(Compute Cores)** (Impact: 23.2)
  * `TEST_CASE` **(Compute Cores)** (Impact: 20.2)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 151 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 635
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 629`, `args: 501`, `func_start: 275`
* *Risk/State:* `state_mutation: 333`, `dead_code: 2`, `fragile_debt: 17`
* *Architecture:* `io: 307`, `import: 24`
* *Defense:* `safety: 32`, `test: 867`, `immutability_locks: 97`, `cleanup: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` point.h, CIPLabeler.h, Reaction.h, ReactionParser.h, Chirality.h, RDDepictor.h, FileParsers.h, PNGParser.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/molopstest.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.574)
- **Top Global Matches:** file_cluster_15: 8.574, file_cluster_4: 9.642, file_cluster_16: 9.747
- **Magnitude:** 2088.1 | **LOC:** 8008 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.7%), Guard Balance (formerly Safety Score) (41.4%), Complexity Load (formerly Cognitive Load) (33.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Compute Cores)** (Impact: 52.0)
  * `TEST_CASE` **(Compute Cores)** (Impact: 45.8)
  * `TEST_CASE` **(Compute Cores)** (Impact: 39.3)
  * `TEST_CASE` **(I/O & Config Routines)** (Impact: 32.8)
  * `TEST_CASE` **(I/O & Config Routines)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 18 instances
* *Amplified Cascading Flux:* 192 instances
* *Memory Alloc (weighted view):* 137
* *State Mutation (weighted view):* 1321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 111`, `args: 448`, `func_start: 122`, `class_start: 1`
* *Risk/State:* `state_mutation: 937`, `dead_code: 7`, `fragile_debt: 4`
* *Architecture:* `import: 19`
* *Defense:* `safety: 38`, `test: 2479`, `immutability_locks: 410`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Chirality.h, FileParsers.h, MolSupplier.h, MolWriters.h, QueryOps.h, RDKitBase.h, RDKitQueries.h, SmartsWrite.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolPickler.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.146)
- **Top Global Matches:** file_cluster_6: 7.146, file_cluster_8: 11.019, file_cluster_4: 14.384
- **Magnitude:** 2082.82 | **LOC:** 2769 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.158; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.1%), Complexity Load (formerly Cognitive Load) (53.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MolPickler::_depickle` **(Many-Argument Workhorses)** (Impact: 187.7)
  * `buildBaseQuery` **(Many-Argument Workhorses)** (Impact: 134.4)
  * `MolPickler::_addAtomFromPickle` **(Many-Argument Workhorses)** (Impact: 104.3)
  * `MolPickler::_pickle` **(Many-Argument Workhorses)** (Impact: 72.1)
    * *Intent:* //-------------------------------------- // // Molecules // //--------------------------------------...
  * `MolPickler::_addBondFromPickle` **(Many-Argument Workhorses)** (Impact: 70.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 203 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 627
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 563`, `structural_boundaries: 216`, `args: 103`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 221`, `dead_code: 8`, `unreferenced_by_name: 25`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 18`
* *Defense:* `safety: 16`, `test: 2`, `sync_locks: 21`, `immutability_locks: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000407
  * `Imports (Out-Degree: 29):` DatastructsStreamOps.h, MolPickler.h, MonomerInfo.h, QueryOps.h, RDKitBase.h, RDKitQueries.h, StereoGroup.h, SubstanceGroup.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Scripts/patch_rdkit_docstrings/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.338)
- **Top Global Matches:** file_cluster_6: 7.338, file_cluster_4: 9.94, file_cluster_12: 16.718
- **Magnitude:** 2047.42 | **LOC:** 1580 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.337; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.2%), Connectivity (formerly Api Exposure) (62.2%), Complexity Load (formerly Cognitive Load) (44.1%)
- **Documentation Coverage:** 12.844% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_no_arg` **(Many-Argument Workhorses)** (Impact: 168.3)
    * *Intent:* """Insert the appropriate python::args where needed based on the C++ method parameter names. Args: i...
  * `find_cpp_func_r` **(Many-Argument Workhorses)** (Impact: 88.3)
    * *Intent:* """Find the C++ function corresponding to this cursor. Args: cursor (Cursor): current cursor positio...
  * `find_func_name_r` **(Many-Argument Workhorses)** (Impact: 82.0)
    * *Intent:* """Find the Python function name connected to this cursor. Args: cursor (Cursor): current cursor pos...
  * `find_cpp_func_params_r` **(Many-Argument Workhorses)** (Impact: 75.9)
  * `parse_ast` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* """Parse AST file generated by clang++. Args: arg1_func_byclass_dict (dict): dict relating class nam...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 276 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 919
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 241`, `args: 54`, `func_start: 54`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 5`, `state_mutation: 367`
* *Architecture:* `io: 60`, `api: 55`, `concurrency: 3`, `import: 18`
* *Defense:* `safety: 19`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.337
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000814
  * `Imports (Out-Degree: 1):` clang.cindex, glob, importlib, itertools, json, logging, multiprocessing, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Code/ForceField/MMFF/testMMFFForceField.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.563)
- **Top Global Matches:** file_cluster_4: 6.563, file_cluster_15: 8.476, file_cluster_16: 9.846
- **Magnitude:** 1796.82 | **LOC:** 1885 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mmffValidationSuite` **(Many-Argument Workhorses)** (Impact: 560.1)
  * `sortTorsionInstanceVec` **(Compute Cores)** (Impact: 16.7)
  * `sortAngleBendInstanceVec` **(Compute Cores)** (Impact: 13.1)
  * `sortStretchBendInstanceVec` **(Compute Cores)** (Impact: 13.1)
  * `sortOopBendInstanceVec` **(Compute Cores)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 341 instances
* *Memory Alloc (weighted view):* 34
* *State Mutation (weighted view):* 1072
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 48`, `args: 41`, `func_start: 19`
* *Risk/State:* `state_mutation: 390`, `unreferenced_by_name: 2`
* *Architecture:* `io: 28`, `import: 22`
* *Defense:* `safety: 4`, `immutability_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` AngleConstraints.h, DistanceConstraints.h, ForceField.h, Params.h, PositionConstraint.h, TorsionConstraint.h, Embedder.h, FileParsers.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/MinimalLib/cffi_test.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.147)
- **Top Global Matches:** file_cluster_4: 8.147, file_cluster_15: 8.721, file_cluster_16: 9.438
- **Magnitude:** 1775.4 | **LOC:** 4184 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.184; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (61.6%), Guard Balance (formerly Safety Score) (42.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_png_metadata` **(Defensive Guards)** (Impact: 73.7)
  * `find_wedged_bonds` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `_get_coord_array` **(Defensive Guards)** (Impact: 23.4)
  * `test_get_mol_remove_hs` **(Defensive Guards)** (Impact: 20.2)
  * `test_coords` **(I/O & Config Routines)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 407 instances
* *Amplified Cascading Flux:* 260 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 326`, `args: 166`, `func_start: 56`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 635`, `unreferenced_by_name: 2`
* *Architecture:* `io: 17`, `api: 56`, `import: 11`
* *Defense:* `safety: 901`, `immutability_locks: 68`, `cleanup: 394`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.184
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.001271
  * `Imports (Out-Degree: 2):` assert.h, cffiwrapper.h, fcntl.h, io.h, math.h, poll.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Code/GraphMol/FileParsers/file_parsers_catch.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.038)
- **Top Global Matches:** file_cluster_15: 8.038, file_cluster_16: 9.554, file_cluster_2: 9.694
- **Magnitude:** 1700.56 | **LOC:** 8062 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.5%), Guard Balance (formerly Safety Score) (40.5%), Mutation Surface (formerly State Flux) (17.8%), Debt Markers (formerly Tech Debt) (17.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* #endif
  * `SECTION` **(Compute Cores)** (Impact: 31.9)
  * `check_roundtripped_properties` **(Type Conversions)** (Impact: 30.2)
  * `SECTION` **(I/O & Config Routines)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 41 instances
* *Memory Alloc (weighted view):* 31
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 417`, `args: 371`, `func_start: 349`
* *Risk/State:* `state_mutation: 115`, `fragile_debt: 25`, `duplicate_logic: 4`
* *Architecture:* `io: 16`, `import: 28`
* *Defense:* `safety: 106`, `doc: 1`, `test: 1424`, `immutability_locks: 71`, `cleanup: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` Chirality.h, RDDepictor.h, FileParsers.h, MolFileStereochem.h, MolSupplier.h, MolWriters.h, PNGParser.h, SequenceParsers.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/PgSQL/rdkit/adapter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.846)
- **Top Global Matches:** file_cluster_12: 7.846, file_cluster_4: 9.46, file_cluster_7: 10.206
- **Magnitude:** 1656.16 | **LOC:** 2472 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **43**; blast radius 0.427; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Complexity Load (formerly Cognitive Load) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 48.5577% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `computeNMMolHash` **(Compute Cores)** (Impact: 67.0)
  * `calcSparseStringDiceSml` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `parseMolCTAB` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `molcmp` **(Compute Cores)** (Impact: 32.8)
  * `ReactionSubstruct` **(Compute Cores)** (Impact: 29.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 239 instances
* *State Mutation (weighted view):* 812
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 253`, `args: 342`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 334`, `dead_code: 16`, `fragile_debt: 4`, `unreferenced_by_name: 89`
* *Architecture:* `api: 1`, `import: 43`
* *Defense:* `safety: 154`, `doc: 4`, `immutability_locks: 81`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.427
  * `Choke Point (Betweenness):` 0.000239 | `Ripple Effect (Closeness):` 0.003295
  * `Imports (Out-Degree: 38):` AvalonTools.h, BitOps.h, SparseIntVect.h, Reaction.h, ReactionFingerprints.h, ReactionParser.h, ReactionPickler.h, ReactionUtils.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Code/GraphMol/FMCS/Wrap/testFMCS.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.201)
- **Top Global Matches:** file_cluster_15: 6.201, file_cluster_12: 7.278, file_cluster_16: 7.927
- **Magnitude:** 1598.62 | **LOC:** 1322 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.6%), Complexity Load (formerly Cognitive Load) (93.2%), Guard Balance (formerly Safety Score) (84.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test4RingMatches` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 24.5)
  * `test7Seed` **(Compute Cores)** (Impact: 23.1)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 277 instances
* *State Mutation (weighted view):* 922
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 179`, `args: 110`, `func_start: 100`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 368`, `duplicate_logic: 5`, `unreferenced_by_name: 48`
* *Architecture:* `api: 105`, `import: 4`
* *Defense:* `safety: 30`, `doc: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` rdkit, rdkit.Chem, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/catch_chirality.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.101)
- **Top Global Matches:** file_cluster_15: 8.101, file_cluster_16: 9.882, file_cluster_13: 9.966
- **Magnitude:** 1545.68 | **LOC:** 6557 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.0%), Guard Balance (formerly Safety Score) (36.2%), Debt Markers (formerly Tech Debt) (15.4%), Mutation Surface (formerly State Flux) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Compute Cores)** (Impact: 42.4)
  * `TEST_CASE` **(Compute Cores)** (Impact: 25.9)
  * `TEST_CASE` **(Compute Cores)** (Impact: 23.7)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `TEST_CASE` **(Compute Cores)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 579`, `args: 525`, `func_start: 343`
* *Risk/State:* `state_mutation: 81`, `dead_code: 6`, `fragile_debt: 18`, `duplicate_logic: 2`
* *Architecture:* `import: 17`
* *Defense:* `safety: 39`, `test: 1737`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` CIPLabeler.h, Chirality.h, FileParsers.h, MolFileStereochem.h, MolSupplier.h, MolOps.h, RDKitBase.h, SmilesParse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Canon.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.352)
- **Top Global Matches:** file_cluster_8: 5.352, file_cluster_6: 14.682, file_cluster_3: 22.19
- **Magnitude:** 1518.68 | **LOC:** 1760 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 90.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canonicalizeFragment` **(Many-Argument Workhorses)** (Impact: 247.7)
  * `canonicalizeDoubleBond` **(Many-Argument Workhorses)** (Impact: 159.7)
    * *Intent:* // FIX: this may only be of interest from the SmilesWriter, should we // move it there? // //
  * `dfsBuildStack` **(Many-Argument Workhorses)** (Impact: 105.3)
  * `handleDirConflictsAcrossDoubleBond` **(Many-Argument Workhorses)** (Impact: 89.0)
  * `dfsFindCycles` **(Many-Argument Workhorses)** (Impact: 82.1)
    * *Intent:* // finds cycles
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 172`, `args: 63`, `func_start: 26`
* *Risk/State:* `state_mutation: 134`, `dead_code: 2`, `unreferenced_by_name: 3`
* *Architecture:* `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Canon.h, Chirality.h, RDKitBase.h, RDKitQueries.h, SmilesParseOps.h, new_canon.h, Exceptions.h, hash.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/MolFileWriter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.304)
- **Top Global Matches:** file_cluster_8: 7.304, file_cluster_6: 10.629, file_cluster_4: 19.062
- **Magnitude:** 1467.12 | **LOC:** 1478 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **24**; blast radius 0.176; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.1%), Guard Balance (formerly Safety Score) (70.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AtomGetMolFileSymbol` **(Many-Argument Workhorses)** (Impact: 143.2)
  * `outputMolToMolBlock` **(Many-Argument Workhorses)** (Impact: 113.6)
    * *Intent:* //------------------------------------------------ // // gets a mol block as a string // //---------...
  * `GetV3000MolFileAtomLine` **(Many-Argument Workhorses)** (Impact: 98.8)
  * `getQueryBondSymbol` **(Compute Cores)** (Impact: 52.3)
    * *Intent:* // returns 0 if there's a basic bond-order query
  * `GetV3000MolFileBondLine` **(Many-Argument Workhorses)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 558
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 409`, `structural_boundaries: 92`, `args: 34`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 200`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `import: 24`
* *Defense:* `safety: 3`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.001627
  * `Imports (Out-Degree: 20):` FileParserUtils.h, FileParsers.h, Atropisomers.h, Chirality.h, RDDepictor.h, MolFileStereochem.h, GenericGroups.h, RDKitQueries.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Code/GraphMol/MolAlign/O3AAlignMolecules.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.116)
- **Top Global Matches:** file_cluster_8: 7.116, file_cluster_6: 11.816, file_cluster_4: 20.285
- **Magnitude:** 1452.76 | **LOC:** 1721 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.164; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%), Complexity Load (formerly Cognitive Load) (64.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `O3A::O3A` **(Many-Argument Workhorses)** (Impact: 155.3)
  * `LAP::computeMinCostPath` **(I/O & Config Routines)** (Impact: 77.2)
    * *Intent:* //---------------------------------------------------- // Taken from Jonker, R.; Volgenant, A. // A ...
  * `O3A::O3A` **(Many-Argument Workhorses)** (Impact: 68.7)
  * `LAP::computeCostMatrix` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `SDM::fillFromDist` **(Many-Argument Workhorses)** (Impact: 41.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 272 instances
* *Concurrency (weighted view):* 7
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 833
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 62`, `args: 25`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 289`, `unreferenced_by_name: 11`
* *Architecture:* `concurrency: 2`, `import: 15`
* *Defense:* `immutability_locks: 82`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.164
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000814
  * `Imports (Out-Degree: 13):` AtomIterators.h, Conformer.h, MolOps.h, MolTransforms.h, ROMol.h, SubstructMatch.h, AlignPoints.h, Vector.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Code/GraphMol/Fingerprints/RDKitFPGenerator.h` (CPP) | Magnitude: 8.0 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 63, immutability_locks: 32, pointers: 27, structural_boundaries: 22
- `Code/JavaWrappers/gmwrapper/src-test/org/RDKit/SuppliersTests.java` (JAVA) | Magnitude: 93.86 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 106, structural_boundaries: 33, core_var_decl: 31, design_snake_case: 24
- `Code/GraphMol/FileParsers/MultithreadedMolSupplier.h` (CPP) | Magnitude: 33.26 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 40, core_var_decl: 16, immutability_locks: 14
- `External/GA/ga/LinkedPopLinearSel.h` (CPP) | Magnitude: 0.21 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 231, structural_boundaries: 80, pointers: 56, state_mutation: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `rdkit/ML/Descriptors/UnitTestDescriptors.py` (PYTHON) | Magnitude: 20.28 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 14, state_mutation: 6, test: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Code/GraphMol/MolStandardize/TransformCatalog/TransformCatalogEntry.cpp` (CPP) | Magnitude: 13.3 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, args: 7, import: 7, structural_boundaries: 6
- `Code/GraphMol/MolStandardize/Wrap/Normalize.cpp` (CPP) | Magnitude: 9.84 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, pointers: 12, structural_boundaries: 10, func_start: 5
- `Code/GraphMol/Depictor/Templates.h` (CPP) | Magnitude: 30.24 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 14, pointers: 12, args: 9
- `Code/GraphMol/MolStandardize/AcidBaseCatalog/AcidBaseCatalogEntry.cpp` (CPP) | Magnitude: 12.22 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, args: 7, structural_boundaries: 6, import: 6
- `Code/SimDivPickers/Wrap/MaxMinPicker.cpp` (CPP) | Magnitude: 87.36 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 24, import: 12, pointers: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Code/ChemicalFeatures/Wrap/testFeatures.py` (PYTHON) | Magnitude: 48.8 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 26, core_var_decl: 25, design_snake_case: 21
- `rdkit/Chem/Subshape/UnitTestSubshape.py` (PYTHON) | Magnitude: 136.5 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 37, core_var_decl: 27, branch: 16
- `Code/GraphMol/ReducedGraphs/Wrap/rdReducedGraphs.cpp` (CPP) | Magnitude: 22.38 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 59, pointers: 19, structural_boundaries: 11, import: 8
- `Code/PgSQL/rdkit/sql/fpgist.sql` (POSTGRESQL) | Magnitude: 24.24 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 16, explicit_casts: 16, core_var_decl: 9, design_snake_case: 9
- `Code/GraphMol/MolEnumerator/Wrap/rough_test.py` (PYTHON) | Magnitude: 26.7 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, state_mutation: 11, core_var_decl: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Code/JavaWrappers/gmwrapper/src-test/org/RDKit/GraphMolTestSuite.java` (JAVA) | Magnitude: 16.68 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 31, indent_tabs: 27, decorators: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `rdkit/VLib/UnitTestVLib.py` (PYTHON) | Magnitude: 55.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 92, core_var_decl: 27, design_snake_case: 27, state_mutation: 17
- `Code/Demos/RDKit/Basement/TemplEnum/main.cpp` (CPP) | Magnitude: 116.48 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 236, pointers: 117, state_mutation: 64, core_var_decl: 19
- `Code/GraphMol/Wrap/SmilesWriter.cpp` (CPP) | Magnitude: 18.68 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 73, pointers: 12, structural_boundaries: 11, import: 8
- `Code/GraphMol/MolStandardize/FragmentCatalog/FragmentCatalogEntry.cpp` (CPP) | Magnitude: 13.3 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 26, args: 7, import: 7, structural_boundaries: 6
- `Code/GraphMol/Descriptors/test3D.cpp` (CPP) | Magnitude: 103.16 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 395, core_var_decl: 111, pointers: 89, design_snake_case: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `rdkit/sping/PDF/pidPDF.py` (PYTHON) | Magnitude: 556.38 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 356, branch: 89, core_var_decl: 84, state_mutation: 77

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Code/GraphMol/MolAlign/AlignMolecules.h` (CPP) | Magnitude: 17.26 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 101, indent_spaces: 70, pointers: 49, immutability_locks: 38
- `Code/GraphMol/Substruct/SubstructMatch.h` (CPP) | Magnitude: 71.6 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 120, pointers: 46, immutability_locks: 41, core_var_decl: 34
- `External/INCHI-API/inchi.h` (CPP) | Magnitude: 0.0 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 13, indent_spaces: 13, pointers: 12, immutability_locks: 8
- `Code/JavaWrappers/MorganFingerprints.h` (CPP) | Magnitude: 3.48 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, import: 6, pointers: 5, structural_boundaries: 2
- `Contrib/ConformerParser/test.cpp` (CPP) | Magnitude: 0.16 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 47, pointers: 17, import: 15, core_var_decl: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Contrib/SA_Score/UnitTestSAScore.py` (PYTHON) | Magnitude: 0.37 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 12, branch: 10, state_mutation: 10
- `rdkit/Chem/Pharm2D/__init__.py` (PYTHON) | Magnitude: 13.62 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, core_var_decl: 5, import: 4
- `Code/Fuzz/standalone_fuzz_target_runner.cpp` (CPP) | Magnitude: 7.7 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, import: 3, pointers: 3, args: 2
- `External/YAeHMOP/test1.cpp` (CPP) | Magnitude: 0.03 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 74, test: 53, core_var_decl: 15, design_camel_case: 8
- `Code/Demos/RDKit/GettingStarted/sample.cpp` (CPP) | Magnitude: 124.32 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 168, pointers: 95, state_mutation: 30, core_var_decl: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `rdkit/sping/PIL/pidPIL.py` (PYTHON) | Magnitude: 564.46 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 300, core_var_decl: 133, state_mutation: 116, design_snake_case: 114
- `Code/GraphMol/FileParsers/testMolSupplier.cpp` (CPP) | Magnitude: 737.88 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 2117, test: 545, pointers: 482, core_var_decl: 284
- `Code/GraphMol/Resonance.cpp` (CPP) | Magnitude: 1405.3 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1251, pointers: 505, branch: 329, state_mutation: 247

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `Code/GraphMol/FMCS/Seed.cpp` (CPP) | Magnitude: 316.36 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 307, branch: 76, pointers: 71, core_var_decl: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `rdkit/Chem/SpacialScore.py` (PYTHON) | Magnitude: 92.82 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 32, state_mutation: 23, core_var_decl: 15
- `Code/PgSQL/rdkit/bfp_gin.c` (C) | Magnitude: 148.74 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 87, state_mutation: 31, branch: 21, core_var_decl: 19
- `Code/GraphMol/MolAlign/O3AAlignMolecules.h` (CPP) | Magnitude: 121.32 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 231, pointers: 130, immutability_locks: 97, structural_boundaries: 68
- `Code/PgSQL/rdkit/sql/btree.sql` (POSTGRESQL) | Magnitude: 114.0 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 72, core_var_decl: 39, design_snake_case: 39, branch: 36
- `Code/GraphMol/SynthonSpaceSearch/SynthonSpaceFingerprintSearcher.h` (CPP) | Magnitude: 16.54 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, pointers: 12, immutability_locks: 11, safety: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Code/GraphMol/Canon.cpp` -> Churn: **90.17%** | Cog Load: 60.9323% | Debt: 9.4507%
- `Code/GraphMol/Wrap/rough_test.py` -> Churn: **88.42%** | Cog Load: 74.6976% | Debt: 98.9073%
- `Code/GraphMol/FindRings.cpp` -> Churn: **72.11%** | Cog Load: 72.2431% | Debt: 9.298%
- `Code/GraphMol/MolStandardize/Tautomer.cpp` -> Churn: **55.79%** | Cog Load: 61.9805% | Debt: 46.2477%
- `Code/GraphMol/Substruct/SubstructMatch.cpp` -> Churn: **55.79%** | Cog Load: 52.2157% | Debt: 14.9889%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Code/GraphMol/Depictor/EmbeddedFrag.cpp` -> **Nic Zonta** (100.0% isolated ownership) | Magnitude: 2350.28
- `Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp` -> **Katharina Buchthal** (100.0% isolated ownership) | Magnitude: 2259.16
- `Scripts/patch_rdkit_docstrings/__init__.py` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 2047.42
- `Code/GraphMol/Canon.cpp` -> **Ricardo Rodriguez** (90.9% isolated ownership) | Magnitude: 1518.68
- `Code/GraphMol/FindStereo.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 1417.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Code/GraphMol/ROMol.cpp` -> **Severity: 0.166** (Bridge: 0.0017 * Flux: 98.3807%)
- `Code/GraphMol/QueryAtom.h` -> **Severity: 0.114** (Bridge: 0.0011 * Flux: 99.9964%)
- `Code/RDGeneral/Dict.h` -> **Severity: 0.079** (Bridge: 0.0008 * Flux: 99.985%)
- `Code/GraphMol/Bond.h` -> **Severity: 0.072** (Bridge: 0.0007 * Flux: 98.5211%)
- `Code/GraphMol/ROMol.h` -> **Severity: 0.063** (Bridge: 0.0021 * Flux: 29.4857%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Code/RDGeneral/RDLog.h` -> **Severity: 8.999** (Embedded: 0.1605 * Error Risk: 56.0598%)
- `Code/Numerics/Vector.h` -> **Severity: 8.893** (Embedded: 0.115 * Error Risk: 77.3452%)
- `Code/GraphMol/Bond.h` -> **Severity: 8.736** (Embedded: 0.1448 * Error Risk: 60.3108%)
- `Code/RDGeneral/Dict.h` -> **Severity: 8.092** (Embedded: 0.1258 * Error Risk: 64.3351%)
- `rdkit/__init__.py` -> **Severity: 7.955** (Embedded: 0.1258 * Error Risk: 63.2477%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rdkit/__init__.py` -> **Severity: 4706.6** (Blast Radius: 47.066 * Doc Risk: 100.0%)
- `rdkit/RDLogger.py` -> **Severity: 2198.8** (Blast Radius: 21.988 * Doc Risk: 100.0%)
- `rdkit/Chem/Draw/__init__.py` -> **Severity: 1899.334** (Blast Radius: 20.72 * Doc Risk: 91.6667%)
- `Code/RDGeneral/Invariant.h` -> **Severity: 1482.5** (Blast Radius: 14.825 * Doc Risk: 100.0%)
- `rdkit/Chem/__init__.py` -> **Severity: 1395.375** (Blast Radius: 18.605 * Doc Risk: 75.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2338 literal sites + 71 sites through wrappers = 2409
- **`memory_alloc`:** 3328 literal sites + 549 sites through wrappers = 3877
- **`panics_and_aborts`:** 1864 literal sites + 11 sites through wrappers = 1875

- `CreateAABond` (function, memory_alloc, primitive): 264 call sites in 1 files -- `Code/GraphMol/FileParsers/SequenceParsers.cpp`
- `LPT_OPT_GET` (macro, memory_alloc, via get): 60 call sites in 1 files -- `Code/MinimalLib/common.h`
- `REGISTER_DESCRIPTOR` (macro, memory_alloc, primitive): 43 call sites in 1 files -- `Code/GraphMol/Descriptors/RegisterDescriptor.h`
- `printTime` (function, debug_prints, primitive): 28 call sites in 1 files -- `Code/GraphMol/FMCS/testFMCS_Unit.cpp`
- `printTime` (function, debug_prints, primitive): 22 call sites in 1 files -- `Code/GraphMol/FMCS/Test/testFMCS.cpp`
- `makeBondOrderEqualsQuery` (function, memory_alloc, primitive): 20 call sites in 8 files -- `Code/GraphMol/QueryOps.cpp`
- `makeAtomNullQuery` (function, memory_alloc, primitive): 19 call sites in 11 files -- `Code/GraphMol/QueryOps.cpp`
- `LPT_OPT_GET2` (macro, memory_alloc, via get): 12 call sites in 1 files -- `Code/MinimalLib/common.h`
- `makeBondNullQuery` (function, memory_alloc, primitive): 11 call sites in 6 files -- `Code/GraphMol/QueryOps.cpp`
- `makeBondIsInRingQuery` (function, memory_alloc, primitive): 8 call sites in 5 files -- `Code/GraphMol/QueryOps.cpp`
- `makeSingleOrAromaticBondQuery` (function, memory_alloc, primitive): 8 call sites in 5 files -- `Code/GraphMol/QueryOps.cpp`
- `molFromBlobArg` (function, memory_alloc, primitive): 7 call sites in 1 files -- `Code/Demos/sqlite/rdk_funcs.cpp`
*(+60 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 114963 call pairs -- scoped 15.8%, unique 2.1%, ambiguous 35.2%, external 46.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 82964 | 17.5% | 2.2% | 46.9% | 33.3% |
| python | 24682 | 13.3% | 0.0% | 4.4% | 82.2% |
| java | 2958 | 2.5% | 0.0% | 2.3% | 95.2% |
| c | 1818 | 7.5% | 24.4% | 3.2% | 64.9% |
| postgresql | 836 | 4.8% | 14.8% | 0.0% | 80.4% |
| javascript | 775 | 4.9% | 0.0% | 0.0% | 95.1% |
| yacc | 439 | 8.7% | 4.8% | 64.0% | 22.6% |
| csharp | 295 | 2.0% | 0.0% | 0.0% | 98.0% |
| html | 170 | 12.4% | 0.0% | 0.0% | 87.6% |
| shell | 20 | 0.0% | 0.0% | 0.0% | 100.0% |

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
