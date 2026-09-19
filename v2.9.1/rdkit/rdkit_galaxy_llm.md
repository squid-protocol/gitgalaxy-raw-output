# ARCHITECTURAL_BRIEF: rdkit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rdkit/rdkit.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2401 analyzed artifact(s), 601595 LOC.
- **Load-bearing artifact:** `Code/GraphMol/RDKitBase.h` -- 441 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Code/MinimalLib/common.h` -- pulls in 51 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Code/GraphMol/Wrap/rough_test.py` at magnitude 5282.38 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 2401 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3740 |
| Total LOC | 601595 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 39.1% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4829 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1985 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1458 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 98 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1342 | 414686 | 55.9% |
| PYTHON | 519 | 72826 | 21.6% |
| PLAINTEXT | 268 | 0 | 11.2% |
| JAVA | 53 | 8280 | 2.2% |
| CSV | 37 | 3179 | 1.5% |
| SQLITE | 31 | 2800 | 1.3% |
| MARKDOWN | 28 | 0 | 1.2% |
| POWERSHELL | 22 | 80626 | 0.9% |
| C | 21 | 8975 | 0.9% |
| CSHARP | 17 | 1087 | 0.7% |
| JSON | 15 | 276 | 0.6% |
| MAKEFILE | 11 | 216 | 0.5% |
| M4 | 6 | 133 | 0.2% |
| HTML | 6 | 790 | 0.2% |
| YACC | 6 | 2712 | 0.2% |
| SHELL | 5 | 117 | 0.2% |
| JAVASCRIPT | 4 | 4528 | 0.2% |
| BINARY_THREAT | 3 | 3 | 0.1% |
| YAML | 2 | 170 | 0.1% |
| FORTRAN | 2 | 183 | 0.1% |
| XML | 2 | 0 | 0.1% |
| DB2_SQL | 1 | 8 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `3.841`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +3.84; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 19%, Large Core Modules (3) 19%, Declarative / Non-Code 13%, Parameter Forwarders Files 11%, Many-Argument Workhorses Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2101 | 87.5% |
| Unknown | 3 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 296 | 12.3% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3740*

**Composition by Extension & Reason:**
- `.sdf`: 740x Excluded (Unsupported Extension: '.sdf'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mol`: 560x Excluded (Unsupported Extension: '.mol'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mrv`: 412x Excluded (Unsupported Extension: '.mrv')
- `.cxsmi`: 357x Excluded (Unsupported Extension: '.cxsmi')
- `.rst`: 271x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 243x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 69x Unsupported Format (.undeterminable), 57x Excluded: Neighborhood Micro-Mass Limit Exceeded, 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cdx`: 119x Excluded (Unsupported Extension: '.CDX'), 7x Excluded (Unsupported Extension: '.cdx')
- `.i`: 101x Excluded (Unsupported Extension: '.i')
- `.xyz`: 91x Excluded (Unsupported Extension: '.xyz')
- `.cdxml`: 5x Zero-Density Threshold (LOC: 208, Signals: 0), 4x Zero-Density Threshold (LOC: 124, Signals: 0), 2x Zero-Density Threshold (LOC: 98, Signals: 0)
- `.smi`: 54x Excluded (Unsupported Extension: '.smi'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pdb`: 48x Excluded (Unsupported Extension: '.pdb')
- `.rxn`: 42x Excluded (Unsupported Extension: '.rxn'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pkl`: 42x Excluded (Unsupported Extension: '.pkl')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 28.9 | 19.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 55.8 | 66.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 30.3 | 9.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.6 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 56.9 | 88.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.3 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.6 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 89.0 | 4.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 115847 | 1599 | 108 | `Code/GraphMol/molopstest.cpp` |
| cleanup | 1818 | 321 | 1 | `Code/MinimalLib/cffi_test.c` |
| guards | 37223 | 1518 | 40 | `Code/MinimalLib/cffi_test.c` |
| danger | 4778 | 749 | 5 | `Code/GraphMol/FileParsers/MolFileParser.cpp` |
| concurrency | 401 | 104 | 0 | `Code/GraphMol/DistGeomHelpers/Embedder.cpp` |
| connectivity | 7572 | 965 | 9 | `Code/GraphMol/Wrap/rough_test.py` |
| io | 2558 | 397 | 2 | `Code/GraphMol/MolDraw2D/catch_tests.cpp` |
| crypto | 2 | 2 | 0 | `rdkit/Chem/MolKey/MolKey.py` |
| ipc | 149 | 18 | 0 | `Code/GraphMol/molopstest.cpp` |
| time | 168 | 39 | 0 | `Regress/Scripts/timings.py` |
| serialization | 462 | 64 | 0 | `Code/MinimalLib/tests/tests.js` |
| regex | 465 | 73 | 0 | `Code/GraphMol/MolDraw2D/catch_tests.cpp` |
| events | 369 | 59 | 0 | `Regress/Scripts/timings.py` |
| tests | 26493 | 388 | 6 | `Code/GraphMol/molopstest.cpp` |
| docs | 5674 | 653 | 6 | `Code/GraphMol/MolOps.h` |
| debt | 2996 | 478 | 2 | `Code/GraphMol/MolDraw2D/test1.cpp` |
| mutation | 226177 | 1841 | 175 | `Code/GraphMol/test_data/CDXML/chemdraw_template9.cdxml` |
| dead_code | 7606 | 1189 | 8 | `Code/GraphMol/Wrap/rough_test.py` |
| credential | 14 | 7 | 0 | `Code/GraphMol/MolStandardize/Pipeline.h` |
| threat | 1097 | 657 | 1 | `Code/PgSQL/rdkit/rdkit.h` |
| ml_ai | 757 | 123 | 0 | `Code/GraphMol/Wrap/rough_test.py` |
| ui | 233 | 28 | 0 | `rdkit/sping/SVG/pidSVG.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Code/GraphMol/MolDraw2D/catch_tests.cpp` (Hits: 307)
- `Code/GraphMol/Wrap/rough_test.py` (Hits: 175)
- `Code/GraphMol/MolDraw2D/test1.cpp` (Hits: 134)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **RDKitBase.h** (`Code/GraphMol/RDKitBase.h`) — 441 inbound connections
2. **export.h** (`External/GA/util/export.h`) — 411 inbound connections
3. **rdkit.h** (`Code/PgSQL/rdkit/rdkit.h`) — 326 inbound connections
4. **SmilesParse.h** (`Code/GraphMol/SmilesParse/SmilesParse.h`) — 255 inbound connections
5. **SmilesWrite.h** (`Code/GraphMol/SmilesParse/SmilesWrite.h`) — 197 inbound connections

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
- `EmbeddedFrag::matchToTemplate` **(Many-Argument Workhorses)** (@ `Code/GraphMol/Depictor/EmbeddedFrag.cpp`) -> Impact: **615.2** | LOC: 1704
- `getTPSAAtomContribs` **(Many-Argument Workhorses)** (@ `Code/GraphMol/Descriptors/MolSurf.cpp`) -> Impact: **586.9** | LOC: 244
- `mmffValidationSuite` **(Many-Argument Workhorses)** (@ `Code/ForceField/MMFF/testMMFFForceField.cpp`) -> Impact: **561.8** | LOC: 1191
- `GenerateFP` **(Many-Argument Workhorses)** (@ `Code/GraphMol/Fingerprints/MACCS.cpp`) -> Impact: **495.4** | LOC: 625
- `addAtomChargeFlags` **(Many-Argument Workhorses)** (@ `Code/GraphMol/ForceFieldHelpers/UFF/AtomTyper.cpp`) -> Impact: **487.3** | LOC: 386
  * *Intent:* // ---------------------------------------------------------------
- `parseNode` **(Many-Argument Workhorses)** (@ `External/ChemDraw/node.cpp`) -> Impact: **356.7** | LOC: 289
- `MolToMarvinMol` **(Many-Argument Workhorses)** (@ `Code/GraphMol/MarvinParse/MarvinWriter.cpp`) -> Impact: **342.0** | LOC: 438
- `parse_fragment` **(Many-Argument Workhorses)** (@ `Code/GraphMol/FileParsers/CDXMLParser.cpp`) -> Impact: **336.1** | LOC: 353

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Code/GraphMol` | 99 | 37001.7 | 32.99% | 22.91% |
| `Code/GraphMol/FileParsers` | 74 | 25323.08 | 35.9% | 25.78% |
| `rdkit/Chem` | 70 | 14056.6 | 42.54% | 56.81% |
| `Code/GraphMol/MolDraw2D` | 54 | 12718.14 | 30.64% | 36.36% |
| `Code/GraphMol/SmilesParse` | 26 | 11674.62 | 33.76% | 15.96% |
| `Code/GraphMol/Wrap` | 56 | 10033.6 | 18.54% | 33.04% |
| `Code/GraphMol/Descriptors` | 70 | 8381.86 | 25.88% | 21.96% |
| `Code/GraphMol/ChemReactions` | 26 | 6663.26 | 31.78% | 19.47% |
| `Code/GraphMol/MolStandardize` | 27 | 6532.26 | 29.11% | 22.76% |
| `Code/PgSQL/rdkit` | 21 | 5909.9 | 33.81% | 19.52% |

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
- `Code/DataStructs/DiscreteValueVect.cpp` -> **100.0%** Exposure
- `Code/DataStructs/SparseIntVect.h` -> **100.0%** Exposure
- `Code/DataStructs/Utils.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Code/GraphMol/Wrap/rough_test.py` -> **288** Orphaned Functions | **8** Duplicates
- `Code/GraphMol/MarvinParse/MarvinDefs.cpp` -> **135** Orphaned Functions | **0** Duplicates
- `Code/MinimalLib/minilib.cpp` -> **101** Orphaned Functions | **0** Duplicates
- `Code/PgSQL/rdkit/adapter.cpp` -> **89** Orphaned Functions | **0** Duplicates
- `Code/GraphMol/MolDraw2D/DrawMol.cpp` -> **73** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `21` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12620` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Code/GraphMol/Wrap/rough_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 5282.38 | **LOC:** 8717 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 35.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.9%), Guard Balance (formerly Safety Score) (95.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.0%)
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
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 17`, `state_mutation: 2115`, `dead_code: 4`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 288`
* *Architecture:* `io: 175`, `api: 337`, `import: 36`
* *Defense:* `safety: 70`, `doc: 65`, `test: 39`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` contextlib, copy, datetime, doctest, gc, gzip, importlib.util, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Chirality.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3878.42 | **LOC:** 3958 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.3%), Complexity Load (formerly Cognitive Load) (80.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.9%)
- **Documentation Coverage:** 98.7179% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assignNontetrahedralChiralTypeFrom3D` **(Many-Argument Workhorses)** (Impact: 237.5)
    * *Intent:* // The tolerance here is pretty high in order to accomodate things coming from // the dgeom code As ...
  * `legacyStereoPerception` **(Many-Argument Workhorses)** (Impact: 220.1)
    * *Intent:* */
  * `atomChiralTypeFromBondDirPseudo3D` **(Many-Argument Workhorses)** (Impact: 188.9)
  * `updateDoubleBondNeighbors` **(Many-Argument Workhorses)** (Impact: 137.8)
  * `assignChiralTypesFrom3D` **(Many-Argument Workhorses)** (Impact: 96.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 405 instances
* *State Mutation (weighted view):* 1230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1141`, `structural_boundaries: 338`, `args: 148`, `func_start: 78`, `class_start: 2`
* *Risk/State:* `state_mutation: 420`, `dead_code: 29`, `unreferenced_by_name: 18`
* *Architecture:* `import: 19`
* *Defense:* `safety: 8`, `doc: 3`, `immutability_locks: 182`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Chirality.h, point.h, Atropisomers.h, QueryOps.h, RDKitBase.h, new_canon.h, Invariant.h, RDLog.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/ForceFieldHelpers/MMFF/AtomTyper.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3659.18 | **LOC:** 3731 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.2%), Guard Balance (formerly Safety Score) (96.9%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 1019`, `structural_boundaries: 77`, `args: 67`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `state_mutation: 507`, `dead_code: 111`, `unreferenced_by_name: 21`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 237`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` AtomTyper.h, Nonbonded.h, MolOps.h, QueryOps.h, RDKitBase.h, Invariant.h, RDLog.h, dynamic_bitset.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/MolFileParser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3570.78 | **LOC:** 3779 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseV3000AtomProps` **(Many-Argument Workhorses)** (Impact: 292.0)
  * `ParseMolBlockProperties` **(Many-Argument Workhorses)** (Impact: 234.5)
  * `ParseV3000CTAB` **(Many-Argument Workhorses)** (Impact: 219.9)
  * `ParseV3000BondBlock` **(Many-Argument Workhorses)** (Impact: 175.9)
  * `ParseMolFileAtomLine` **(Many-Argument Workhorses)** (Impact: 169.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 351 instances
* *Memory Alloc (weighted view):* 24
* *State Mutation (weighted view):* 1101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 960`, `structural_boundaries: 174`, `args: 99`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 399`, `dead_code: 8`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `import: 34`
* *Defense:* `safety: 137`, `doc: 1`, `test: 1`, `immutability_locks: 72`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` FileParserUtils.h, FileParsers.h, Atropisomers.h, Chirality.h, MolFileStereochem.h, GenericGroups.h, QueryOps.h, RDKitQueries.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolDraw2D/DrawMol.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3414.04 | **LOC:** 4077 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DrawMol::getAtomSymbol` **(Many-Argument Workhorses)** (Impact: 112.5)
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
* *Structure:* `branch: 856`, `structural_boundaries: 378`, `args: 121`, `func_start: 106`
* *Risk/State:* `state_mutation: 644`, `dead_code: 20`, `fragile_debt: 1`, `unreferenced_by_name: 73`
* *Architecture:* `import: 23`
* *Defense:* `safety: 17`, `immutability_locks: 239`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` Transform2D.h, Transform3D.h, Atropisomers.h, Chirality.h, RDDepictor.h, FileParserUtils.h, MolFileStereochem.h, MolSGroupParsing.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/SmilesParse/CXSmilesOps.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2963.78 | **LOC:** 2650 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.4%)
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
* *Structure:* `branch: 873`, `structural_boundaries: 369`, `args: 77`, `func_start: 57`
* *Risk/State:* `state_mutation: 258`, `dead_code: 5`, `unreferenced_by_name: 3`
* *Architecture:* `import: 19`
* *Defense:* `safety: 4`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Atropisomers.h, Chirality.h, MolFileStereochem.h, LinkNode.h, RDKitBase.h, RDKitQueries.h, BoostEndInclude.h, BoostStartInclude.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rdkit/Chem/fmcs/fmcs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2558.08 | **LOC:** 2825 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (92.2%), Connectivity (formerly Api Exposure) (54.8%)
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
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 543`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 4`
* *Architecture:* `io: 15`, `api: 94`, `import: 12`
* *Defense:* `safety: 41`, `doc: 1`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` argparse, collections, copy, fractions, heapq, itertools, rdkit, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MarvinParse/MarvinDefs.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2492.54 | **LOC:** 4286 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Guard Balance (formerly Safety Score) (87.6%), Debt Markers (formerly Tech Debt) (86.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MarvinMolBase::parseAtomsAndBonds` **(Compute Cores)** (Impact: 249.6)
  * `MarvinSuperatomSgroup::convertFromOneSuperAtom` **(I/O & Config Routines)** (Impact: 53.7)
  * `MarvinMultipleSgroup::contractOneMultipleSgroup` **(I/O & Config Routines)** (Impact: 49.0)
  * `MarvinSuperatomSgroupExpanded::convertToOneSuperAtom` **(I/O & Config Routines)** (Impact: 48.9)
  * `MarvinMultipleSgroup::expandOneMultipleSgroup` **(I/O & Config Routines)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 334 instances
* *Memory Alloc (weighted view):* 30
* *State Mutation (weighted view):* 1078
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 699`, `structural_boundaries: 424`, `args: 115`, `func_start: 169`
* *Risk/State:* `state_mutation: 410`, `dead_code: 10`, `unreferenced_by_name: 135`
* *Architecture:* `import: 5`
* *Defense:* `safety: 25`, `immutability_locks: 133`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MarvinDefs.h, BoostEndInclude.h, BoostStartInclude.h, RDLog.h, string.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/SequenceParsers.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 2360.18 | **LOC:** 1907 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.3%), Guard Balance (formerly Safety Score) (94.0%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` GraphMol.h, MolOps.h, MonomerInfo.h, SequenceParsers.h, cstring, map, string, vector
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Depictor/EmbeddedFrag.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2351.98 | **LOC:** 2159 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Complexity Load (formerly Cognitive Load) (92.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EmbeddedFrag::matchToTemplate` **(Many-Argument Workhorses)** (Impact: 615.2)
  * `checkStereoChemistry` **(Many-Argument Workhorses)** (Impact: 83.2)
    * *Intent:* // check if the stereochemistry of the template matches the stereochemistry of // the molecule
  * `EmbeddedFrag::randomSampleFlipsAndPermutations` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `EmbeddedFrag::openAngles` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `EmbeddedFrag::mergeWithCommon` **(Many-Argument Workhorses)** (Impact: 46.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 277 instances
* *State Mutation (weighted view):* 890
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 371`, `args: 55`, `func_start: 53`
* *Risk/State:* `state_mutation: 336`, `dead_code: 13`, `fragile_debt: 1`, `unreferenced_by_name: 38`
* *Architecture:* `import: 18`
* *Defense:* `safety: 1`, `immutability_locks: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` DepictUtils.h, EmbeddedFrag.h, Transform2D.h, point.h, Bond.h, MolOps.h, ROMol.h, RWMol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2343.86 | **LOC:** 1983 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HBond::findAcceptorsUnfixed` **(Many-Argument Workhorses)** (Impact: 160.9)
  * `HBond::findDonorsUnfixed` **(Many-Argument Workhorses)** (Impact: 157.8)
  * `HBond::findAcceptors` **(Many-Argument Workhorses)** (Impact: 114.8)
    * *Intent:* /* General structure of findAcceptors, findAcceptorsUnfixed, findDonors, * findDonorsUnfixed functio...
  * `CoulombDielectric::CoulombDielectric` **(Many-Argument Workhorses)** (Impact: 99.0)
  * `CoulombDielectric::CoulombDielectric` **(Many-Argument Workhorses)** (Impact: 90.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 376 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 94`, `args: 85`, `func_start: 41`
* *Risk/State:* `state_mutation: 447`, `dead_code: 6`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `import: 14`
* *Defense:* `safety: 5`, `immutability_locks: 84`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Nonbonded.h, Nonbonded.h, Params.h, UniformRealValueGrid3D.h, point.h, AtomTyper.h, RDKitBase.h, SmilesParse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2262.06 | **LOC:** 2251 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_setChain14Bounds` **(Many-Argument Workhorses)** (Impact: 167.6)
  * `set13Bounds` **(Many-Argument Workhorses)** (Impact: 115.8)
  * `_setMacrocycleAllInSameRing14Bounds` **(Many-Argument Workhorses)** (Impact: 111.5)
  * `_setInRing14Bounds` **(Many-Argument Workhorses)** (Impact: 102.5)
  * `set14Bounds` **(Many-Argument Workhorses)** (Impact: 93.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 291 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 948
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 432`, `structural_boundaries: 176`, `args: 49`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `state_mutation: 366`, `dead_code: 15`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `doc: 15`, `immutability_locks: 153`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` BoundsMatrixBuilder.h, BoundsMatrix.h, TriangleSmooth.h, BondStretch.h, Utils.h, Chirality.h, AtomTyper.h, RDKitBase.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolDraw2D/catch_tests.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2246.24 | **LOC:** 11099 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.9%), Mutation Surface (formerly State Flux) (46.7%), Guard Balance (formerly Safety Score) (45.8%), Complexity Load (formerly Cognitive Load) (10.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 54.9)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `TEST_CASE` **(I/O & Config Routines)** (Impact: 29.0)
  * `TEST_CASE` **(Compute Cores)** (Impact: 23.9)
  * `TEST_CASE` **(Compute Cores)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 152 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 637
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 629`, `args: 501`, `func_start: 275`
* *Risk/State:* `state_mutation: 333`, `dead_code: 4`, `fragile_debt: 17`
* *Architecture:* `io: 307`, `import: 24`
* *Defense:* `safety: 32`, `test: 867`, `immutability_locks: 97`, `cleanup: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` point.h, CIPLabeler.h, Reaction.h, ReactionParser.h, Chirality.h, RDDepictor.h, FileParsers.h, PNGParser.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolPickler.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2107.62 | **LOC:** 2769 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.4%)
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
* *Structure:* `branch: 576`, `structural_boundaries: 216`, `args: 103`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 221`, `dead_code: 4`, `unreferenced_by_name: 25`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 18`
* *Defense:* `safety: 16`, `test: 2`, `sync_locks: 21`, `immutability_locks: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` DatastructsStreamOps.h, MolPickler.h, MonomerInfo.h, QueryOps.h, RDKitBase.h, RDKitQueries.h, StereoGroup.h, SubstanceGroup.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/molopstest.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2099.0 | **LOC:** 8008 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.6%), Complexity Load (formerly Cognitive Load) (33.4%), Guard Balance (formerly Safety Score) (26.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Compute Cores)** (Impact: 52.0)
  * `TEST_CASE` **(Compute Cores)** (Impact: 45.8)
  * `TEST_CASE` **(Compute Cores)** (Impact: 39.3)
  * `TEST_CASE` **(I/O & Config Routines)** (Impact: 32.8)
  * `TEST_CASE` **(I/O & Config Routines)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 18 instances
* *Amplified Cascading Flux:* 193 instances
* *Memory Alloc (weighted view):* 137
* *State Mutation (weighted view):* 1323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 111`, `args: 448`, `func_start: 122`, `class_start: 1`
* *Risk/State:* `state_mutation: 937`, `dead_code: 4`, `fragile_debt: 4`
* *Architecture:* `import: 19`
* *Defense:* `safety: 38`, `test: 2479`, `immutability_locks: 410`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` Chirality.h, FileParsers.h, MolSupplier.h, MolWriters.h, QueryOps.h, RDKitBase.h, RDKitQueries.h, SmartsWrite.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/ChemReactions/testReaction.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1875.32 | **LOC:** 8001 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (36.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test45SmilesWriter` **(I/O & Config Routines)** (Impact: 19.2)
  * `testGithub4114` **(I/O & Config Routines)** (Impact: 17.3)
  * `testOtherBondStereo` **(I/O & Config Routines)** (Impact: 15.5)
  * `test12DoubleBondStereochem` **(I/O & Config Routines)** (Impact: 9.5)
  * `test60RunSingleReactant` **(I/O & Config Routines)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 64 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 1413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 214`, `args: 726`, `func_start: 98`
* *Risk/State:* `state_mutation: 1285`, `dead_code: 2`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `import: 18`
* *Defense:* `safety: 55`, `immutability_locks: 74`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` point.h, Atom.h, Reaction.h, ReactionParser.h, ReactionPickler.h, ReactionRunner.h, ReactionUtils.h, SanitizeRxn.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/file_parsers_catch.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1860.56 | **LOC:** 8062 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.8%), Guard Balance (formerly Safety Score) (24.1%), Mutation Surface (formerly State Flux) (18.3%), Debt Markers (formerly Tech Debt) (17.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* #endif
  * `SECTION` **(Compute Cores)** (Impact: 31.9)
  * `check_roundtripped_properties` **(Type Conversions)** (Impact: 30.2)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 44 instances
* *Memory Alloc (weighted view):* 31
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 417`, `args: 371`, `func_start: 349`
* *Risk/State:* `state_mutation: 115`, `dead_code: 4`, `fragile_debt: 25`, `duplicate_logic: 4`
* *Architecture:* `io: 16`, `import: 28`
* *Defense:* `safety: 106`, `doc: 1`, `test: 1424`, `immutability_locks: 71`, `cleanup: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` Chirality.h, RDDepictor.h, FileParsers.h, MolFileStereochem.h, MolSupplier.h, MolWriters.h, PNGParser.h, SequenceParsers.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/ForceField/MMFF/testMMFFForceField.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1804.02 | **LOC:** 1885 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mmffValidationSuite` **(Many-Argument Workhorses)** (Impact: 561.8)
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
* *Structure:* `branch: 343`, `structural_boundaries: 48`, `args: 41`, `func_start: 19`
* *Risk/State:* `state_mutation: 390`, `unreferenced_by_name: 2`
* *Architecture:* `io: 28`, `import: 22`
* *Defense:* `safety: 4`, `immutability_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` AngleConstraints.h, DistanceConstraints.h, ForceField.h, Params.h, PositionConstraint.h, TorsionConstraint.h, Embedder.h, FileParsers.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/MinimalLib/cffi_test.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1794.4 | **LOC:** 4184 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.8%), Guard Balance (formerly Safety Score) (28.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_png_metadata` **(Defensive Guards)** (Impact: 76.7)
  * `find_wedged_bonds` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `_get_coord_array` **(Defensive Guards)** (Impact: 23.4)
  * `test_get_mol_remove_hs` **(Defensive Guards)** (Impact: 20.2)
  * `test_coords` **(I/O & Config Routines)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 407 instances
* *Amplified Cascading Flux:* 266 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 326`, `args: 166`, `func_start: 56`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 635`, `unreferenced_by_name: 2`
* *Architecture:* `io: 17`, `api: 56`, `import: 11`
* *Defense:* `safety: 901`, `immutability_locks: 68`, `cleanup: 394`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, cffiwrapper.h, fcntl.h, io.h, math.h, poll.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/PgSQL/rdkit/adapter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1660.96 | **LOC:** 2472 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Guard Balance (formerly Safety Score) (88.9%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 274`, `structural_boundaries: 253`, `args: 342`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 334`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 89`
* *Architecture:* `api: 1`, `import: 43`
* *Defense:* `safety: 154`, `doc: 4`, `immutability_locks: 81`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` AvalonTools.h, BitOps.h, SparseIntVect.h, Reaction.h, ReactionFingerprints.h, ReactionParser.h, ReactionPickler.h, ReactionUtils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FMCS/Wrap/testFMCS.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1598.62 | **LOC:** 1322 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Debt Markers (formerly Tech Debt) (96.7%), Complexity Load (formerly Cognitive Load) (93.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` rdkit, rdkit.Chem, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/catch_chirality.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1571.38 | **LOC:** 6557 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.2%), Debt Markers (formerly Tech Debt) (15.6%), Guard Balance (formerly Safety Score) (15.6%), Mutation Surface (formerly State Flux) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TEST_CASE` **(Compute Cores)** (Impact: 42.4)
  * `TEST_CASE` **(Compute Cores)** (Impact: 27.3)
  * `TEST_CASE` **(Compute Cores)** (Impact: 25.1)
  * `TEST_CASE` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `TEST_CASE` **(Compute Cores)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 579`, `args: 525`, `func_start: 343`
* *Risk/State:* `state_mutation: 81`, `dead_code: 4`, `fragile_debt: 18`, `duplicate_logic: 2`
* *Architecture:* `import: 17`
* *Defense:* `safety: 39`, `test: 1737`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` CIPLabeler.h, Chirality.h, FileParsers.h, MolFileStereochem.h, MolSupplier.h, MolOps.h, RDKitBase.h, SmilesParse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Canon.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1526.18 | **LOC:** 1760 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 90.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (84.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canonicalizeFragment` **(Many-Argument Workhorses)** (Impact: 251.1)
  * `canonicalizeDoubleBond` **(Many-Argument Workhorses)** (Impact: 159.7)
    * *Intent:* // FIX: this may only be of interest from the SmilesWriter, should we // move it there? // //
  * `dfsBuildStack` **(Many-Argument Workhorses)** (Impact: 105.3)
  * `handleDirConflictsAcrossDoubleBond` **(Many-Argument Workhorses)** (Impact: 89.0)
  * `canonicalizeDoubleBonds` **(Many-Argument Workhorses)** (Impact: 83.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 172`, `args: 63`, `func_start: 26`
* *Risk/State:* `state_mutation: 134`, `dead_code: 9`, `unreferenced_by_name: 3`
* *Architecture:* `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Canon.h, Chirality.h, RDKitBase.h, RDKitQueries.h, SmilesParseOps.h, new_canon.h, Exceptions.h, hash.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/MolFileWriter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1469.12 | **LOC:** 1478 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%)
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
* *Structure:* `branch: 410`, `structural_boundaries: 92`, `args: 34`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 200`, `dead_code: 6`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `import: 24`
* *Defense:* `safety: 3`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` FileParserUtils.h, FileParsers.h, Atropisomers.h, Chirality.h, RDDepictor.h, MolFileStereochem.h, GenericGroups.h, RDKitQueries.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MarvinParse/MarvinWriter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1450.8 | **LOC:** 1254 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (80.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MolToMarvinMol` **(Many-Argument Workhorses)** (Impact: 342.0)
  * `GetMarvinAtomInfo` **(Many-Argument Workhorses)** (Impact: 138.1)
  * `getMarvinQueryBondSymbol` **(Compute Cores)** (Impact: 58.1)
  * `GetMarvinBondSymbol` **(Many-Argument Workhorses)** (Impact: 54.3)
  * `AddMarvinPluses` **(Many-Argument Workhorses)** (Impact: 41.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 203 instances
* *State Mutation (weighted view):* 646
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 340`, `structural_boundaries: 92`, `args: 28`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 240`, `dead_code: 10`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 27`
* *Defense:* `safety: 12`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Atropisomers.h, Chirality.h, RDDepictor.h, FileParsers.h, MolFileStereochem.h, MolSGroupWriting.h, GenericGroups.h, RDKitQueries.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Code/GraphMol/Wrap/rough_test.py` -> Churn: **88.95%** | Cog Load: 74.6976% | Debt: 98.9194%
- `Code/GraphMol/Canon.cpp` -> Churn: **73.6%** | Cog Load: 61.2329% | Debt: 9.7989%
- `Code/GraphMol/FindRings.cpp` -> Churn: **58.85%** | Cog Load: 72.2431% | Debt: 9.7773%
- `Code/MinimalLib/minilib.cpp` -> Churn: **58.85%** | Cog Load: 29.9183% | Debt: 99.9836%
- `Code/GraphMol/MolOps.cpp` -> Churn: **55.59%** | Cog Load: 60.3016% | Debt: 19.8606%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Code/GraphMol/MarvinParse/MarvinDefs.cpp` -> **tadhurst-cdd** (100.0% isolated ownership) | Magnitude: 2492.54
- `Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 2343.86
- `Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp` -> **Katharina Buchthal** (100.0% isolated ownership) | Magnitude: 2262.06
- `Code/GraphMol/ChemReactions/testReaction.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 1875.32
- `Code/ForceField/MMFF/testMMFFForceField.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 1804.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Code/RDGeneral/Dict.h` -> **Severity: 0.088** (Bridge: 0.0009 * Flux: 99.985%)
- `Code/GraphMol/Bond.h` -> **Severity: 0.078** (Bridge: 0.0008 * Flux: 98.5211%)
- `Code/Bench/pickle.cpp` -> **Severity: 0.062** (Bridge: 0.0007 * Flux: 91.6827%)
- `Code/RDGeneral/RDValue.h` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 99.9328%)
- `Code/Geometry/point.h` -> **Severity: 0.042** (Bridge: 0.0004 * Flux: 97.6018%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Code/GraphMol/Bond.h` -> **Severity: 12.06** (Embedded: 0.1514 * Error Risk: 79.6717%)
- `Code/Numerics/Vector.h` -> **Severity: 12.006** (Embedded: 0.1228 * Error Risk: 97.7615%)
- `Code/RDGeneral/RDLog.h` -> **Severity: 11.036** (Embedded: 0.1559 * Error Risk: 70.7778%)
- `Code/RDGeneral/Dict.h` -> **Severity: 10.979** (Embedded: 0.1271 * Error Risk: 86.3572%)
- `Code/Geometry/point.h` -> **Severity: 10.776** (Embedded: 0.1434 * Error Risk: 75.137%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Code/RDGeneral/Invariant.h` -> **Severity: 1530.6** (Blast Radius: 15.306 * Doc Risk: 100.0%)
- `Code/RDGeneral/types.h` -> **Severity: 1047.6** (Blast Radius: 10.476 * Doc Risk: 100.0%)
- `Code/GraphMol/ROMol.h` -> **Severity: 676.104** (Blast Radius: 6.85 * Doc Risk: 98.7013%)
- `Code/Geometry/point.h` -> **Severity: 642.218** (Blast Radius: 7.015 * Doc Risk: 91.5493%)
- `Code/RDGeneral/RDLog.h` -> **Severity: 547.1** (Blast Radius: 5.471 * Doc Risk: 100.0%)

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
