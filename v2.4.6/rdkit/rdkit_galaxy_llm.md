# ARCHITECTURAL_BRIEF: rdkit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/rdkit` |
| **Timestamp** | `2026-08-03T19:40:38.245458+00:00` |
| **Scan Duration** | `13.12s` |
| **Git Branch** | `master` |
| **Git Commit** | `9e301c15d6c2f5cab848ffaa788300505d69ff94` |
| **Git Remote** | `https://github.com/rdkit/rdkit.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1966 malicious artifacts.

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
| Total Artifacts | 6141 |
| Analyzed Artifacts (Scanned) | 2281 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3860 |
| Total LOC | 471110 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 37.1% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8844 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1887 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8374 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 244 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1291 | 291933 | 56.6% |
| PYTHON | 473 | 61335 | 20.7% |
| PLAINTEXT | 234 | 0 | 10.3% |
| POWERSHELL | 91 | 99806 | 4.0% |
| CSV | 34 | 3069 | 1.5% |
| SQLITE | 31 | 2442 | 1.4% |
| MARKDOWN | 27 | 0 | 1.2% |
| M4 | 25 | 3763 | 1.1% |
| C | 20 | 5016 | 0.9% |
| JSON | 15 | 276 | 0.7% |
| MAKEFILE | 12 | 243 | 0.5% |
| YACC | 6 | 2325 | 0.3% |
| CSHARP | 5 | 161 | 0.2% |
| SHELL | 4 | 95 | 0.2% |
| JAVASCRIPT | 3 | 222 | 0.1% |
| BINARY_THREAT | 3 | 3 | 0.1% |
| YAML | 2 | 206 | 0.1% |
| FORTRAN | 2 | 179 | 0.1% |
| XML | 2 | 0 | 0.1% |
| HTML | 1 | 36 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.067`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1010 | 44.3% |
| file_cluster_13 | 943 | 41.3% |
| file_cluster_9 | 22 | 1.0% |
| file_cluster_11 | 12 | 0.5% |
| file_cluster_4 | 12 | 0.5% |
| file_cluster_17 | 9 | 0.4% |
| file_cluster_16 | 4 | 0.2% |
| Unknown | 3 | 0.1% |
| file_cluster_2 | 2 | 0.1% |
| file_cluster_0 | 1 | 0.0% |
| file_cluster_15 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 261 | 11.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3860*

**Composition by Extension & Reason:**
- `.sdf`: 711x Excluded (Unsupported Extension: '.sdf'), 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mol`: 555x Excluded (Unsupported Extension: '.mol'), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mrv`: 401x Excluded (Unsupported Extension: '.mrv'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cxsmi`: 352x Excluded (Unsupported Extension: '.cxsmi'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 271x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 243x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 62x Unsupported Format (.undeterminable), 57x Excluded: Neighborhood Micro-Mass Limit Exceeded, 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cdx`: 119x Excluded (Unsupported Extension: '.CDX'), 7x Excluded (Unsupported Extension: '.cdx')
- `.i`: 99x Excluded (Unsupported Extension: '.i'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xyz`: 91x Excluded (Unsupported Extension: '.xyz')
- `.cpp`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2190 LOC), 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.smi`: 51x Excluded (Unsupported Extension: '.smi'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Saturation: Line 60 exceeds 500 chars)
- `.java`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pdb`: 47x Excluded (Unsupported Extension: '.pdb'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.7 | 37.8 | 33.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 36.3 | 24.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 42.6 | 22.9 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 27.3 | 2.4 | 80.0 |
| API Exposure | 0.0 | 17.5 | 1.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 67.7 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 94.5 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.1 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 74.5 | 4.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 49.4 | 39.2 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 49.7 | 37.1 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Code/PgSQL/rdkit/sql/rdkit-91.sql` (Hits: 217)
- `Code/GraphMol/MolDraw2D/catch_tests.cpp` (Hits: 169)
- `Code/PgSQL/rdkit/sql/reaction.sql` (Hits: 142)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rdkit.h** (`Code/PgSQL/rdkit/rdkit.h`) — 301 inbound connections
2. **pickle.cpp** (`Code/Bench/pickle.cpp`) — 56 inbound connections
3. **FileParsers.h** (`Code/GraphMol/FileParsers/FileParsers.h`) — 27 inbound connections
4. **DbConnection.py** (`rdkit/Dbase/DbConnection.py`) — 23 inbound connections
5. **RDLogger.py** (`rdkit/RDLogger.py`) — 17 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **adapter.cpp** (`Code/PgSQL/rdkit/adapter.cpp`) — 43 outbound dependencies
2. **MolFileParser.cpp** (`Code/GraphMol/FileParsers/MolFileParser.cpp`) — 34 outbound dependencies
3. **Embedder.cpp** (`Code/GraphMol/DistGeomHelpers/Embedder.cpp`) — 32 outbound dependencies
4. **RDKitSVMainWindow.cc** (`Code/GraphMol/MolDraw2D/Qt/Demo/RDKitSVMainWindow.cc`) — 30 outbound dependencies
5. **test1.cpp** (`Code/GraphMol/FileParsers/test1.cpp`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseFragment` (@ `External/ChemDraw/fragment.cpp`) -> Impact: **7927.4** | LOC: 973
- `TEST_CASE` (@ `Code/GraphMol/MolDraw2D/catch_tests.cpp`) -> Impact: **5421.3** | LOC: 1315
- `parseEnhancedStereo` (@ `Code/GraphMol/FileParsers/MolFileParser.cpp`) -> Impact: **4038.4** | LOC: 1567
- `TEST_CASE` (@ `Code/GraphMol/RGroupDecomposition/testRGroupDecomp.cpp`) -> Impact: **3836.8** | LOC: 1321
- `getBondFlags` (@ `Code/GraphMol/MolHash/hashfunctions.cpp`) -> Impact: **3460.2** | LOC: 883
- `checkRings` (@ `Code/GraphMol/RascalMCES/RascalMCES.cpp`) -> Impact: **2823.3** | LOC: 632
  * *Intent:* // make the line graph for the molecule, as an adjacency matrix. Each // row/column is a bond, with a connection between 2 bonds if they share an
- `setTerminalAtomCoords` (@ `Code/GraphMol/AddHs.cpp`) -> Impact: **2581.9** | LOC: 679
- `LoadSDF` (@ `rdkit/Chem/PandasTools.py`) -> Impact: **2365.6** | LOC: 414
- `rdChemReactions` (@ `Code/GraphMol/ChemReactions/Wrap/rdChemReactions.cpp`) -> Impact: **2314.6** | LOC: 792
- `DrawMol::partitionForLegend` (@ `Code/GraphMol/MolDraw2D/DrawMol.cpp`) -> Impact: **2193.0** | LOC: 1336

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `SimilarityWrapper` (@ `Code/DataStructs/Wrap/wrap_BitOps.cpp`) -> **O(2^N) [Recursive]**
- `SimilarityWrapper` (@ `Code/DataStructs/Wrap/wrap_BitOps.cpp`) -> **O(2^N) [Recursive]**
- `CleanupMolecule` (@ `Code/Demos/RDKit/GettingStarted/sample.cpp`) -> **O(2^N) [Recursive]**
- `addLongRangeDistanceConstraints` (@ `Code/DistGeom/DistGeomUtils.cpp`) -> **O(2^N) [Recursive]**
- `computeInitialCoords` (@ `Code/DistGeom/DistGeomUtils.cpp`) -> **O(2^N) [Recursive]**
- `pickRandomDistMat` (@ `Code/DistGeom/DistGeomUtils.cpp`) -> **O(2^N) [Recursive]**
- `computeRandomCoords` (@ `Code/DistGeom/DistGeomUtils.cpp`) -> **O(2^N) [Recursive]**
- `applyMatches` (@ `Code/GraphMol/Abbreviations/Abbreviations.cpp`) -> **O(2^N) [Recursive]**
- `setTerminalAtomCoords` (@ `Code/GraphMol/AddHs.cpp`) -> **O(2^N) [Recursive]**
- `preprocessReaction` (@ `Code/GraphMol/ChemReactions/PreprocessRxn.cpp`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `testMetalDisconnectorLigandExpo` (@ `Code/GraphMol/MolStandardize/test1.cpp`) -> DB Complexity: **2705**
- `main` (@ `Code/GraphMol/FileParsers/testMolWriter.cpp`) -> DB Complexity: **1240**
- `main` (@ `Code/GraphMol/DistGeomHelpers/testDgeomHelpers.cpp`) -> DB Complexity: **816**
- `test9MolLegends` (@ `Code/GraphMol/MolDraw2D/test1.cpp`) -> DB Complexity: **694**
- `DrawMol::partitionForLegend` (@ `Code/GraphMol/MolDraw2D/DrawMol.cpp`) -> DB Complexity: **598**
- `mmffValidationSuite` (@ `Code/ForceField/MMFF/testMMFFForceField.cpp`) -> DB Complexity: **571**
- `testJnk1LigandsDistance` (@ `Code/GraphMol/FMCS/testFMCS_Unit.cpp`) -> DB Complexity: **510**
  * *Intent:* /* TODO: best practice on where to put a test data file into the repo? */
- `TEST_CASE` (@ `Code/GraphMol/SmilesParse/catch_tests.cpp`) -> DB Complexity: **461**
- `testEnumerator` (@ `Code/GraphMol/MolStandardize/testTautomer.cpp`) -> DB Complexity: **427**
- `TEST_CASE` (@ `Code/GraphMol/MolDraw2D/catch_tests.cpp`) -> DB Complexity: **419**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Code/GraphMol` | 90 | 54737.32 | 52.65% | 51.06% |
| `Code/GraphMol/FileParsers` | 74 | 48844.08 | 57.61% | 49.97% |
| `Code/GraphMol/MolDraw2D` | 54 | 30018.16 | 55.0% | 39.31% |
| `rdkit/Chem` | 70 | 22312.73 | 13.4% | 54.68% |
| `Code/GraphMol/SmilesParse` | 24 | 19626.12 | 51.8% | 47.59% |
| `Code/GraphMol/Descriptors` | 70 | 16921.32 | 44.38% | 25.22% |
| `Code/GraphMol/MolStandardize` | 27 | 16672.62 | 62.38% | 49.38% |
| `Code/GraphMol/RGroupDecomposition` | 26 | 13003.58 | 50.95% | 52.82% |
| `Code/GraphMol/Wrap` | 55 | 11337.76 | 39.55% | 46.4% |
| `Code/GraphMol/ChemReactions` | 26 | 10439.58 | 55.19% | 51.98% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Code/Bench/descriptors.cpp` -> **100.0%** Exposure
- `Code/Bench/meta.cpp` -> **100.0%** Exposure
- `Code/Bench/molops.cpp` -> **100.0%** Exposure
- `Code/Bench/smiles.cpp` -> **100.0%** Exposure
- `Code/ChemicalFeatures/ChemicalFeature.h` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Code/Bench/bench_common.hpp` -> **100.0%** Exposure
- `Code/Bench/descriptors.cpp` -> **100.0%** Exposure
- `Code/Bench/fingerprint.cpp` -> **100.0%** Exposure
- `Code/Bench/inchi.cpp` -> **100.0%** Exposure
- `Code/Bench/mol.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Code/PgSQL/rdkit/sql/rdkit-91.sql` -> **0** Orphaned Functions | **234** Duplicates
- `Code/PgSQL/rdkit/update_sql/rdkit--4.7.0--4.8.0.sql.in` -> **0** Orphaned Functions | **220** Duplicates
- `Code/PgSQL/rdkit/sql/reaction.sql` -> **0** Orphaned Functions | **172** Duplicates
- `Code/GraphMol/MarvinParse/MarvinDefs.cpp` -> **77** Orphaned Functions | **21** Duplicates
- `Code/PgSQL/rdkit/sql/btree.sql` -> **0** Orphaned Functions | **69** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Code/DataStructs/BitVect.cpp`** -> AI Confidence: **99.48%**
2. **`Code/Demos/RDKit/MPI/rdkexample1.cpp`** -> AI Confidence: **99.48%**
3. **`Code/ForceField/MMFF/Params.cpp`** -> AI Confidence: **99.48%**
4. **`Code/ForceField/MMFF/testMMFFForceField.cpp`** -> AI Confidence: **99.48%**
5. **`Code/ForceField/UFF/AngleBend.cpp`** -> AI Confidence: **99.48%**
6. **`Code/GraphMol/AdjustQuery.cpp`** -> AI Confidence: **99.48%**
7. **`Code/GraphMol/ChemReactions/MDLParser.cpp`** -> AI Confidence: **99.48%**
8. **`Code/GraphMol/Descriptors/testAUTOCORR3D.cpp`** -> AI Confidence: **99.48%**
9. **`Code/GraphMol/Descriptors/testGETAWAY.cpp`** -> AI Confidence: **99.48%**
10. **`Code/GraphMol/Descriptors/testMORSE.cpp`** -> AI Confidence: **99.48%**
11. **`Code/GraphMol/Descriptors/testRDF.cpp`** -> AI Confidence: **99.48%**
12. **`Code/GraphMol/Descriptors/testRDFcustom.cpp`** -> AI Confidence: **99.48%**
13. **`Code/GraphMol/DistGeomHelpers/Wrap/rdDistGeom.cpp`** -> AI Confidence: **99.48%**
14. **`Code/GraphMol/FileParsers/Mol2FileParser.cpp`** -> AI Confidence: **99.48%**
15. **`Code/GraphMol/FileParsers/MolFileParser.cpp`** -> AI Confidence: **99.48%**
16. **`Code/GraphMol/FileParsers/PDBParser.cpp`** -> AI Confidence: **99.48%**
17. **`Code/GraphMol/FileParsers/PDBWriter.cpp`** -> AI Confidence: **99.48%**
18. **`Code/GraphMol/FileParsers/SequenceParsers.cpp`** -> AI Confidence: **99.48%**
19. **`Code/GraphMol/FileParsers/TDTWriter.cpp`** -> AI Confidence: **99.48%**
20. **`Code/GraphMol/FileParsers/testMolSupplier.cpp`** -> AI Confidence: **99.48%**
21. **`Code/GraphMol/Fingerprints/Fingerprints.cpp`** -> AI Confidence: **99.48%**
22. **`Code/GraphMol/Fingerprints/MACCS.cpp`** -> AI Confidence: **99.48%**
23. **`Code/GraphMol/ForceFieldHelpers/MMFF/AtomTyper.cpp`** -> AI Confidence: **99.48%**
24. **`Code/GraphMol/ForceFieldHelpers/MMFF/Builder.cpp`** -> AI Confidence: **99.48%**
25. **`Code/GraphMol/ForceFieldHelpers/UFF/AtomTyper.cpp`** -> AI Confidence: **99.48%**
26. **`Code/GraphMol/ForceFieldHelpers/UFF/Builder.cpp`** -> AI Confidence: **99.48%**
27. **`Code/GraphMol/FragCatalog/FragCatGenerator.cpp`** -> AI Confidence: **99.48%**
28. **`Code/GraphMol/MarvinParse/MarvinParser.cpp`** -> AI Confidence: **99.48%**
29. **`Code/GraphMol/MarvinParse/MarvinWriter.cpp`** -> AI Confidence: **99.48%**
30. **`Code/GraphMol/MolAlign/Wrap/rdMolAlign.cpp`** -> AI Confidence: **99.48%**
31. **`Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp`** -> AI Confidence: **99.48%**
32. **`Code/GraphMol/MolStandardize/testPCS.cpp`** -> AI Confidence: **99.48%**
33. **`Code/GraphMol/QueryOps.cpp`** -> AI Confidence: **99.48%**
34. **`Code/GraphMol/SLNParse/SLNAttribs.cpp`** -> AI Confidence: **99.48%**
35. **`Code/GraphMol/SmilesParse/SmilesWrite.cpp`** -> AI Confidence: **99.48%**
36. **`Code/GraphMol/StructChecker/Stereo.cpp`** -> AI Confidence: **99.48%**
37. **`Code/GraphMol/StructChecker/StructChecker.cpp`** -> AI Confidence: **99.48%**
38. **`Code/GraphMol/SynthonSpaceSearch/MemoryMappedFileReader.cpp`** -> AI Confidence: **99.48%**
39. **`Code/GraphMol/Trajectory/Trajectory.cpp`** -> AI Confidence: **99.48%**
40. **`Contrib/PBF/demo.cpp`** -> AI Confidence: **99.48%**
41. **`External/INCHI-API/inchi.cpp`** -> AI Confidence: **99.48%**
42. **`rdkit/Chem/BuildFragmentCatalog.py`** -> AI Confidence: **99.48%**
43. **`Code/PgSQL/rdkit/bfp_gin.c`** -> AI Confidence: **99.48%**
44. **`Code/Demos/RDKit/Basement/Minimize/MinimizeCLI.cpp`** -> AI Confidence: **99.39%**
45. **`Code/Demos/RDKit/GettingStarted/sample.cpp`** -> AI Confidence: **99.39%**
46. **`Code/Demos/RDKit/MPI/rdkexample2.cpp`** -> AI Confidence: **99.39%**
47. **`Code/DistGeom/DistGeomUtils.cpp`** -> AI Confidence: **99.39%**
48. **`Code/GraphMol/AddHs.cpp`** -> AI Confidence: **99.39%**
49. **`Code/GraphMol/Atropisomers.cpp`** -> AI Confidence: **99.39%**
50. **`Code/GraphMol/ChemReactions/Reaction.cpp`** -> AI Confidence: **99.39%**
51. **`Code/GraphMol/ChemReactions/ReactionRunner.cpp`** -> AI Confidence: **99.39%**
52. **`Code/GraphMol/ChemTransforms/MolFragmenter.cpp`** -> AI Confidence: **99.39%**
53. **`Code/GraphMol/Chirality.cpp`** -> AI Confidence: **99.39%**
54. **`Code/GraphMol/ConjugHybrid.cpp`** -> AI Confidence: **99.39%**
55. **`Code/GraphMol/Descriptors/GETAWAY.cpp`** -> AI Confidence: **99.39%**
56. **`Code/GraphMol/Descriptors/Lipinski.cpp`** -> AI Confidence: **99.39%**
57. **`Code/GraphMol/Descriptors/testWHIM.cpp`** -> AI Confidence: **99.39%**
58. **`Code/GraphMol/FMCS/MaximumCommonSubgraph.cpp`** -> AI Confidence: **99.39%**
59. **`Code/GraphMol/FileParsers/ForwardSDMolSupplier.cpp`** -> AI Confidence: **99.39%**
60. **`Code/GraphMol/FileParsers/MolFileWriter.cpp`** -> AI Confidence: **99.39%**
61. **`Code/GraphMol/FileParsers/PNGParser.cpp`** -> AI Confidence: **99.39%**
62. **`Code/GraphMol/FileParsers/SDMolSupplier.cpp`** -> AI Confidence: **99.39%**
63. **`Code/GraphMol/FileParsers/SmilesWriter.cpp`** -> AI Confidence: **99.39%**
64. **`Code/GraphMol/FindStereo.cpp`** -> AI Confidence: **99.39%**
65. **`Code/GraphMol/Fingerprints/FingerprintUtil.cpp`** -> AI Confidence: **99.39%**
66. **`Code/GraphMol/ForceFieldHelpers/CrystalFF/TorsionPreferences.cpp`** -> AI Confidence: **99.39%**
67. **`Code/GraphMol/FragCatalog/FragFPGenerator.cpp`** -> AI Confidence: **99.39%**
68. **`Code/GraphMol/MolHash/hashfunctions.cpp`** -> AI Confidence: **99.39%**
69. **`Code/GraphMol/MolPickler.cpp`** -> AI Confidence: **99.39%**
70. **`Code/GraphMol/MolStandardize/Fragment.cpp`** -> AI Confidence: **99.39%**
71. **`Code/GraphMol/RascalMCES/mces_cluster_catch.cpp`** -> AI Confidence: **99.39%**
72. **`Code/GraphMol/ReducedGraphs/ReducedGraphs.cpp`** -> AI Confidence: **99.39%**
73. **`Code/GraphMol/SmilesParse/SmartsWrite.cpp`** -> AI Confidence: **99.39%**
74. **`Code/GraphMol/Subgraphs/Subgraphs.cpp`** -> AI Confidence: **99.39%**
75. **`Code/GraphMol/Subgraphs/testSubgraphs2.cpp`** -> AI Confidence: **99.39%**
76. **`Code/GraphMol/Substruct/cmd_match.cpp`** -> AI Confidence: **99.39%**
77. **`Projects/DbCLI/SearchDb.py`** -> AI Confidence: **99.39%**
78. **`Regress/Scripts/new_timings.py`** -> AI Confidence: **99.39%**
79. **`Regress/Scripts/timings.py`** -> AI Confidence: **99.39%**
80. **`rdkit/Chem/BRICS.py`** -> AI Confidence: **99.39%**
81. **`Code/PgSQL/rdkit/low_gist.c`** -> AI Confidence: **99.39%**
82. **`Code/PgSQL/rdkit/rdkit_gist.c`** -> AI Confidence: **99.39%**
83. **`Code/Demos/RDKit/Draw/qtDemo/RDKitMolToQPainter.cc`** -> AI Confidence: **99.35%**
84. **`Code/GraphMol/Descriptors/Crippen.cpp`** -> AI Confidence: **99.35%**
85. **`Code/GraphMol/Descriptors/testEEM.cpp`** -> AI Confidence: **99.35%**
86. **`Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp`** -> AI Confidence: **99.35%**
87. **`Code/GraphMol/FileParsers/XYZFileParser.cpp`** -> AI Confidence: **99.35%**
88. **`Code/GraphMol/FindRings.cpp`** -> AI Confidence: **99.35%**
89. **`Code/GraphMol/MolDraw2D/DrawMol.cpp`** -> AI Confidence: **99.35%**
90. **`Code/GraphMol/MolStandardize/Tautomer.cpp`** -> AI Confidence: **99.35%**
91. **`Code/GraphMol/WedgeBonds.cpp`** -> AI Confidence: **99.35%**
92. **`Code/ForceField/UFF/TorsionAngle.cpp`** -> AI Confidence: **99.34%**
93. **`Code/GraphMol/Aromaticity.cpp`** -> AI Confidence: **99.34%**
94. **`Code/GraphMol/Descriptors/MQN.cpp`** -> AI Confidence: **99.34%**
95. **`Code/GraphMol/Descriptors/MolSurf.cpp`** -> AI Confidence: **99.34%**
96. **`Code/GraphMol/Kekulize.cpp`** -> AI Confidence: **99.34%**
97. **`Code/GraphMol/MMPA/Wrap/rdMMPA.cpp`** -> AI Confidence: **99.34%**
98. **`Code/GraphMol/MolDraw2D/DrawTextJS.cpp`** -> AI Confidence: **99.34%**
99. **`Code/GraphMol/MolEnumerator/LinkNode.h`** -> AI Confidence: **99.34%**
100. **`Code/GraphMol/PartialCharges/GasteigerCharges.cpp`** -> AI Confidence: **99.34%**
101. **`Code/GraphMol/PeriodicTable.cpp`** -> AI Confidence: **99.34%**
102. **`Code/GraphMol/StructChecker/StripSmallFragments.cpp`** -> AI Confidence: **99.34%**
103. **`Code/Numerics/Alignment/AlignPoints.cpp`** -> AI Confidence: **99.34%**
104. **`Code/Numerics/EigenSolvers/PowerEigenSolver.cpp`** -> AI Confidence: **99.34%**
105. **`Code/RDGeneral/Invariant.h`** -> AI Confidence: **99.34%**
106. **`rdkit/Chem/ChemUtils/TemplateExpand.py`** -> AI Confidence: **99.34%**
107. **`rdkit/Chem/Draw/MolDrawing.py`** -> AI Confidence: **99.34%**
108. **`rdkit/Chem/MolSurf.py`** -> AI Confidence: **99.34%**
109. **`rdkit/Dbase/DbUtils.py`** -> AI Confidence: **99.34%**
110. **`rdkit/ML/Data/SplitData.py`** -> AI Confidence: **99.34%**
111. **`Code/DataStructs/DiscreteDistMat.cpp`** -> AI Confidence: **99.32%**
112. **`Code/GraphMol/ChemReactions/Enumerate/EvenSamplePairs.cpp`** -> AI Confidence: **99.32%**
113. **`Code/GraphMol/StructChecker/Pattern.cpp`** -> AI Confidence: **99.32%**
114. **`Code/GraphMol/StructChecker/ReCharge.cpp`** -> AI Confidence: **99.32%**
115. **`External/ChemDraw/fragment.cpp`** -> AI Confidence: **99.32%**
116. **`Contrib/efgs/efgs.py`** -> AI Confidence: **99.32%**
117. **`Code/DataManip/MetricMatrixCalc/Wrap/rdMetricMatrixCalc.cpp`** -> AI Confidence: **99.31%**
118. **`Code/DataStructs/DiscreteValueVect.cpp`** -> AI Confidence: **99.31%**
119. **`Code/DataStructs/FPBReader.cpp`** -> AI Confidence: **99.31%**
120. **`Code/DataStructs/SparseBitVect.cpp`** -> AI Confidence: **99.31%**
121. **`Code/DataStructs/SparseIntVect.h`** -> AI Confidence: **99.31%**
122. **`Code/DataStructs/testDatastructs.cpp`** -> AI Confidence: **99.31%**
123. **`Code/Demos/RDKit/Basement/xpcom/RDMolImpl.cpp`** -> AI Confidence: **99.31%**
124. **`Code/Demos/sqlite/rdk_funcs.cpp`** -> AI Confidence: **99.31%**
125. **`Code/DistGeom/Wrap/DistGeom.cpp`** -> AI Confidence: **99.31%**
126. **`Code/ForceField/MMFF/Nonbonded.cpp`** -> AI Confidence: **99.31%**
127. **`Code/ForceField/MMFF/Params.h`** -> AI Confidence: **99.31%**
128. **`Code/ForceField/TorsionConstraint.cpp`** -> AI Confidence: **99.31%**
129. **`Code/ForceField/Wrap/ForceField.cpp`** -> AI Confidence: **99.31%**
130. **`Code/Geometry/GridUtils.cpp`** -> AI Confidence: **99.31%**
131. **`Code/Geometry/UniformGrid3D.cpp`** -> AI Confidence: **99.31%**
132. **`Code/Geometry/testTransforms.cpp`** -> AI Confidence: **99.31%**
133. **`Code/GraphMol/Atom.cpp`** -> AI Confidence: **99.31%**
134. **`Code/GraphMol/Basement/FeatTrees/FeatTreeUtils.cpp`** -> AI Confidence: **99.31%**
135. **`Code/GraphMol/CIPLabeler/CIPLabeler.cpp`** -> AI Confidence: **99.31%**
136. **`Code/GraphMol/Canon.cpp`** -> AI Confidence: **99.31%**
137. **`Code/GraphMol/ChemReactions/CDXMLParser.cpp`** -> AI Confidence: **99.31%**
138. **`Code/GraphMol/ChemReactions/DaylightParser.cpp`** -> AI Confidence: **99.31%**
139. **`Code/GraphMol/ChemReactions/Enumerate/Enumerate.cpp`** -> AI Confidence: **99.31%**
140. **`Code/GraphMol/ChemReactions/Enumerate/testEnumerate.cpp`** -> AI Confidence: **99.31%**
141. **`Code/GraphMol/ChemReactions/ReactionFingerprints.cpp`** -> AI Confidence: **99.31%**
142. **`Code/GraphMol/ChemReactions/ReactionPickler.cpp`** -> AI Confidence: **99.31%**
143. **`Code/GraphMol/ChemReactions/ReactionWriter.cpp`** -> AI Confidence: **99.31%**
144. **`Code/GraphMol/ChemReactions/Wrap/Enumerate.cpp`** -> AI Confidence: **99.31%**
145. **`Code/GraphMol/ChemReactions/Wrap/rdChemReactions.cpp`** -> AI Confidence: **99.31%**
146. **`Code/GraphMol/ChemTransforms/ChemTransforms.cpp`** -> AI Confidence: **99.31%**
147. **`Code/GraphMol/ChemTransforms/MolZip.cpp`** -> AI Confidence: **99.31%**
148. **`Code/GraphMol/Depictor/DepictUtils.cpp`** -> AI Confidence: **99.31%**
149. **`Code/GraphMol/Depictor/EmbeddedFrag.cpp`** -> AI Confidence: **99.31%**
150. **`Code/GraphMol/Depictor/RDDepictor.cpp`** -> AI Confidence: **99.31%**
151. **`Code/GraphMol/Descriptors/AUTOCORR3D.cpp`** -> AI Confidence: **99.31%**
152. **`Code/GraphMol/Descriptors/AtomFeat.cpp`** -> AI Confidence: **99.31%**
153. **`Code/GraphMol/Descriptors/ConnectivityDescriptors.cpp`** -> AI Confidence: **99.31%**
154. **`Code/GraphMol/Descriptors/DCLV.cpp`** -> AI Confidence: **99.31%**
155. **`Code/GraphMol/Descriptors/PBF.cpp`** -> AI Confidence: **99.31%**
156. **`Code/GraphMol/Descriptors/USRDescriptor.cpp`** -> AI Confidence: **99.31%**
157. **`Code/GraphMol/Descriptors/Wrap/rdMolDescriptors.cpp`** -> AI Confidence: **99.31%**
158. **`Code/GraphMol/Descriptors/testAUTOCORR2D.cpp`** -> AI Confidence: **99.31%**
159. **`Code/GraphMol/Descriptors/testPBF.cpp`** -> AI Confidence: **99.31%**
160. **`Code/GraphMol/DetermineBonds/DetermineBonds.cpp`** -> AI Confidence: **99.31%**
161. **`Code/GraphMol/DetermineBonds/catch_tests.cpp`** -> AI Confidence: **99.31%**
162. **`Code/GraphMol/DistGeomHelpers/Embedder.cpp`** -> AI Confidence: **99.31%**
163. **`Code/GraphMol/EnumerateStereoisomers/EnumerateStereoisomers.cpp`** -> AI Confidence: **99.31%**
164. **`Code/GraphMol/FMCS/FMCS.cpp`** -> AI Confidence: **99.31%**
165. **`Code/GraphMol/FMCS/testFMCS_Unit.cpp`** -> AI Confidence: **99.31%**
166. **`Code/GraphMol/FileParsers/CDXMLParser.cpp`** -> AI Confidence: **99.31%**
167. **`Code/GraphMol/FileParsers/CMLWriter.cpp`** -> AI Confidence: **99.31%**
168. **`Code/GraphMol/FileParsers/GeneralFileReader.h`** -> AI Confidence: **99.31%**
169. **`Code/GraphMol/FileParsers/MaeMolSupplier.cpp`** -> AI Confidence: **99.31%**
170. **`Code/GraphMol/FileParsers/MolFileStereochem.cpp`** -> AI Confidence: **99.31%**
171. **`Code/GraphMol/FileParsers/SCSRMolFileParser.cpp`** -> AI Confidence: **99.31%**
172. **`Code/GraphMol/FileParsers/SDWriter.cpp`** -> AI Confidence: **99.31%**
173. **`Code/GraphMol/FileParsers/SVGParser.cpp`** -> AI Confidence: **99.31%**
174. **`Code/GraphMol/FileParsers/SequenceWriters.cpp`** -> AI Confidence: **99.31%**
175. **`Code/GraphMol/FileParsers/SmilesMolSupplier.cpp`** -> AI Confidence: **99.31%**
176. **`Code/GraphMol/FileParsers/TDTMolSupplier.cpp`** -> AI Confidence: **99.31%**
177. **`Code/GraphMol/FileParsers/TplFileParser.cpp`** -> AI Confidence: **99.31%**
178. **`Code/GraphMol/FileParsers/testAtropisomers.cpp`** -> AI Confidence: **99.31%**
179. **`Code/GraphMol/FileParsers/testMolWriter.cpp`** -> AI Confidence: **99.31%**
180. **`Code/GraphMol/FileParsers/testMultithreadedMolSupplier.cpp`** -> AI Confidence: **99.31%**
181. **`Code/GraphMol/FileParsers/testPropertyLists.cpp`** -> AI Confidence: **99.31%**
182. **`Code/GraphMol/FilterCatalog/Filters.cpp`** -> AI Confidence: **99.31%**
183. **`Code/GraphMol/Fingerprints/AtomPairs.cpp`** -> AI Confidence: **99.31%**
184. **`Code/GraphMol/Fingerprints/FingerprintGenerator.cpp`** -> AI Confidence: **99.31%**
185. **`Code/GraphMol/Fingerprints/MHFP.cpp`** -> AI Confidence: **99.31%**
186. **`Code/GraphMol/Fingerprints/MorganGenerator.cpp`** -> AI Confidence: **99.31%**
187. **`Code/GraphMol/Fingerprints/PatternFingerprints.cpp`** -> AI Confidence: **99.31%**
188. **`Code/GraphMol/Fingerprints/testFingerprintGenerators.cpp`** -> AI Confidence: **99.31%**
189. **`Code/GraphMol/ForceFieldHelpers/CrystalFF/TorsionAngleContribs.cpp`** -> AI Confidence: **99.31%**
190. **`Code/GraphMol/ForceFieldHelpers/CrystalFF/TorsionAngleM6.cpp`** -> AI Confidence: **99.31%**
191. **`Code/GraphMol/ForceFieldHelpers/MMFF/testMMFFHelpers.cpp`** -> AI Confidence: **99.31%**
192. **`Code/GraphMol/ForceFieldHelpers/MMFF/testMultiThread.cpp`** -> AI Confidence: **99.31%**
193. **`Code/GraphMol/ForceFieldHelpers/Wrap/rdForceFields.cpp`** -> AI Confidence: **99.31%**
194. **`Code/GraphMol/FragCatalog/FragCatalogEntry.cpp`** -> AI Confidence: **99.31%**
195. **`Code/GraphMol/FragCatalog/FragCatalogUtils.cpp`** -> AI Confidence: **99.31%**
196. **`Code/GraphMol/FragCatalog/test1.cpp`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `Code/DataStructs/testDatastructs.cpp` -> **99.9999%** Exposure
- `Code/GraphMol/SmilesParse/smitest1.cpp` -> **0.1534%** Exposure
- `Code/GraphMol/FileParsers/file_parsers_catch.cpp` -> **0.0004%** Exposure
- `Code/DataStructs/testMultiFPB.cpp` -> **0.0003%** Exposure
- `Code/JavaWrappers/csharp_wrapper/RdkitTests/TestSubstanceGroup.cs` -> **0.0002%** Exposure
### Exploit Generation Surface
- `Code/ChemicalFeatures/Wrap/testFeatures.py` -> **100.0%** Exposure
- `Code/DataStructs/Wrap/testBV.py` -> **100.0%** Exposure
- `Code/DataStructs/Wrap/testFPB.py` -> **100.0%** Exposure
- `Code/DataStructs/Wrap/testRealValueVect.py` -> **100.0%** Exposure
- `Code/DataStructs/Wrap/testSparseIntVect.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Code/ChemicalFeatures/Wrap/testFeatures.py` -> **100.0%** Exposure
- `Code/DataStructs/Wrap/testRealValueVect.py` -> **100.0%** Exposure
- `Code/DataStructs/Wrap/testSparseIntVect.py` -> **100.0%** Exposure
- `Code/GraphMol/PartialCharges/Wrap/testPartialCharges.py` -> **100.0%** Exposure
- `Code/GraphMol/UnitTestQueryMol.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `Code/GraphMol/ChemReactions/catch_tests.cpp` -> **10.0%** Exposure
- `Code/GraphMol/ChemTransforms/ChemTransforms.cpp` -> **10.0%** Exposure
- `Code/GraphMol/ChemTransforms/catch_tests.cpp` -> **10.0%** Exposure
- `Code/GraphMol/Depictor/catch_tests.cpp` -> **10.0%** Exposure
- `Code/GraphMol/DistGeomHelpers/catch_tests.cpp` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `Code/Bench/stereo.cpp` -> **100.0%** Exposure
- `Code/Catalogs/Catalog.h` -> **100.0%** Exposure
- `Code/ChemicalFeatures/FreeChemicalFeature.h` -> **100.0%** Exposure
- `Code/ChemicalFeatures/Wrap/FreeChemicalFeature.cpp` -> **100.0%** Exposure
- `Code/DataManip/MetricMatrixCalc/MetricFuncs.h` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `33` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11492` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Code/GraphMol/SynthonSpaceSearch/SynthonSpaceSearch_details.cpp` (CPP) -> Cumulative Risk: **897.45**
- **Archetype:** `file_cluster_11` (Distance: 14.588 IQR)
- **Magnitude:** 1692.28 | **LOC:** 895 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `flagRingBonds` (Impact: 349.1), `checkConnectorsInDifferentFrags` (Impact: 92.7), `splitMolecule` (Impact: 68.3)

### 2. `Code/GraphMol/MolAlign/AlignMolecules.cpp` (CPP) -> Cumulative Risk: **863.66**
- **Archetype:** `file_cluster_8` (Distance: 14.096 IQR)
- **Magnitude:** 1321.44 | **LOC:** 479 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `getBestRMSInternal` (Impact: 209.8), `alignMolConformers` (Impact: 141.5), `getAllConformerBestRMS` (Impact: 100.3)

### 3. `Code/DataStructs/MultiFPBReader.cpp` (CPP) -> Cumulative Risk: **857.51**
- **Archetype:** `file_cluster_8` (Distance: 13.215 IQR)
- **Magnitude:** 518.38 | **LOC:** 297 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `get_containing_nbrs` (Impact: 75.9), `generic_nbr_helper` (Impact: 56.3), `tversky_helper` (Impact: 28.9)

### 4. `Code/GraphMol/RascalMCES/RascalCluster.cpp` (CPP) -> Cumulative Risk: **856.75**
- **Archetype:** `file_cluster_11` (Distance: 13.809 IQR)
- **Magnitude:** 647.3 | **LOC:** 383 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9853%)
- **Heaviest Functions:** `buildProximityGraph` (Impact: 82.1), `formInitialClusters` (Impact: 41.8), `makeSubClusters` (Impact: 36.7)

### 5. `External/YAeHMOP/EHTTools.cpp` (CPP) -> Cumulative Risk: **837.63**
- **Archetype:** `file_cluster_4` (Distance: 13.141 IQR)
- **Magnitude:** 0.23 | **LOC:** 210 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.7905%)
- **Heaviest Functions:** `runMol` (Impact: 61.5), `randomstring` (Impact: 5.5), `Tempfile` (Impact: 4.7)

### 6. `Code/ForceField/UFF/Utils.cpp` (CPP) -> Cumulative Risk: **829.92**
- **Archetype:** `file_cluster_9` (Distance: 18.643 IQR)
- **Magnitude:** 159.2 | **LOC:** 90 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (95.5663%)
- **Heaviest Functions:** `calcInversionCoefficientsAndForceConstan` (Impact: 41.3), `calculateCosY` (Impact: 34.6)

### 7. `Code/GraphMol/FileParsers/testMultithreadedMolSupplier.cpp` (CPP) -> Cumulative Risk: **824.99**
- **Archetype:** `file_cluster_13` (Distance: 14.158 IQR)
- **Magnitude:** 757.12 | **LOC:** 506 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (98.8692%)
- **Heaviest Functions:** `testPerformance` (Impact: 53.7), `testSDConcurrent` (Impact: 48.0), `testSmiConcurrent` (Impact: 44.9)

### 8. `Code/GraphMol/Substruct/SubstructUtils.cpp` (CPP) -> Cumulative Risk: **814.59**
- **Archetype:** `file_cluster_13` (Distance: 14.033 IQR)
- **Magnitude:** 818.48 | **LOC:** 343 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `bondCompat` (Impact: 276.2), `atomCompat` (Impact: 61.5), `propertyCompat` (Impact: 49.0)

### 9. `Code/Geometry/Transform3D.cpp` (CPP) -> Cumulative Risk: **795.72**
- **Archetype:** `file_cluster_8` (Distance: 13.347 IQR)
- **Magnitude:** 210.34 | **LOC:** 165 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `Transform3D::SetRotation` (Impact: 15.2), `Transform3D::Reflect` (Impact: 11.3), `operator*` (Impact: 6.4)

### 10. `rdkit/Dbase/DbUtils.py` (PYTHON) -> Cumulative Risk: **793.75**
- **Archetype:** `file_cluster_8` (Distance: 11.71 IQR)
- **Magnitude:** 765.52 | **LOC:** 469 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `DatabaseToText` (Impact: 236.8), `GetData` (Impact: 197.4), `_AddDataToDb` (Impact: 160.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Code/GraphMol/MolDraw2D/catch_tests.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.344 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.643 IQR)
- **Top Global Matches:** file_cluster_8: 13.344, file_cluster_7: 13.835, file_cluster_13: 13.887
- **Magnitude:** 10062.3 | **LOC:** 11099 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 419
- **Risk Profile:** Cognitive Load (62.678%), Tech Debt (46.4306%)
**Top Internal Functions/Classes:**
  * `TEST_CASE` (Impact: 5421.3 | O(2^N) | DB: 317)
  * `TEST_CASE` (Impact: 1547.3 | O(2^N) | DB: 419)
  * `TEST_CASE` (Impact: 221.7 | O(N^6) | DB: 42)
  * `TEST_CASE` (Impact: 202.0 | O(N^6) | DB: 7)
  * `TEST_CASE` (Impact: 172.1 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 379`, `args: 379`, `func_start: 138`
* *Risk/State:* `state_mutation: 1973`, `dead_code: 1`, `fragile_debt: 10`, `duplicate_logic: 35`
* *Architecture:* `io: 169`, `import: 24`
* *Defense:* `safety: 27`, `test: 533`, `immutability_locks: 69`, `cleanup: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MolDraw2DCairo.h, catch_all.hpp, point.h, hash.hpp, MolDraw2DUtils.h, Chirality.h, MolDraw2D.h, DrawMol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/ForceFieldHelpers/MMFF/AtomTyper.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.996 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.582 IQR)
- **Top Global Matches:** file_cluster_11: 16.996, file_cluster_0: 17.09, file_cluster_17: 17.099
- **Magnitude:** 6434.8 | **LOC:** 3731 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 265
- **Risk Profile:** Cognitive Load (96.4416%), Tech Debt (12.516%)
**Top Internal Functions/Classes:**
  * `MMFFMolProperties::setMMFFHeavyAtomType` (Impact: 1726.2 | O(N^6) | DB: 265)
    * *Intent:* // sets the MMFF atomType for a heavy atom
  * `MMFFMolProperties::computeMMFFCharges` (Impact: 989.1 | O(N^6) | DB: 246)
    * *Intent:* // Phosphorus
  * `MMFFMolProperties::getMMFFTorsionEmpiric` (Impact: 695.4 | O(N^6) | DB: 119)
  * `isTorsionInRingOfSize4or5` (Impact: 96.6 | O(N^6) | DB: 14)
    * *Intent:* // if the dihedral angle formed by atoms with indexes idx1, // idx2, idx3, idx4 is in a ring of {4,5...
  * `isAngleInRingOfSize3or4` (Impact: 80.4 | O(N^6) | DB: 12)
    * *Intent:* // if the angle formed by atoms with indexes idx1, idx2, idx3 // is in a ring of {3,4} atoms returns...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 651`, `structural_boundaries: 73`, `args: 67`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `state_mutation: 2413`, `dead_code: 46`, `orphaned_logic: 9`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 190`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dynamic_bitset.hpp, AtomTyper.h, Invariant.h, QueryOps.h, Nonbonded.h, MolOps.h, RDKitBase.h, cstdarg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolDraw2D/DrawMol.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.235 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.19 IQR)
- **Top Global Matches:** file_cluster_8: 15.235, file_cluster_13: 15.287, file_cluster_11: 15.32
- **Magnitude:** 6218.42 | **LOC:** 4077 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 598
- **Risk Profile:** Cognitive Load (92.6371%), Tech Debt (16.4117%)
**Top Internal Functions/Classes:**
  * `DrawMol::partitionForLegend` (Impact: 2193.0 | O(N^6) | DB: 598)
  * `DrawMol::getAtomSymbol` (Impact: 376.6 | O(N^6) | DB: 65)
    * *Intent:* // ****************************************************************************
  * `DrawMol::createDrawObjects` (Impact: 235.5 | O(N^6) | DB: 58)
    * *Intent:* // ****************************************************************************
  * `DrawMol::getAtomOrientation` (Impact: 189.8 | O(N^4) | DB: 44)
  * `DrawMol::extractStereoGroups` (Impact: 163.6 | O(N^3) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 241`, `args: 102`, `func_start: 66`
* *Risk/State:* `state_mutation: 2558`, `dead_code: 15`, `orphaned_logic: 19`
* *Architecture:* `import: 23`
* *Defense:* `safety: 6`, `immutability_locks: 168`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Transform3D.h, MolFileStereochem.h, Atropisomers.h, RWMol.h, QueryOps.h, MolTransforms.h, MolDraw2DUtils.h, LinkNode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Chirality.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.996 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.015 IQR)
- **Top Global Matches:** file_cluster_8: 14.996, file_cluster_13: 15.06, file_cluster_11: 15.112
- **Magnitude:** 6127.14 | **LOC:** 3958 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 204
- **Risk Profile:** Cognitive Load (81.4967%), Tech Debt (18.713%)
**Top Internal Functions/Classes:**
  * `atomChiralTypeFromBondDirPseudo3D` (Impact: 954.0 | O(N^6) | DB: 204)
  * `updateDoubleBondNeighbors` (Impact: 898.5 | O(2^N) | DB: 61)
  * `assignNontetrahedralChiralTypeFrom3D` (Impact: 807.7 | O(N^6) | DB: 67)
  * `OctahedralPermFrom3D` (Impact: 281.7 | O(N^6))
  * `controllingBondFromAtom` (Impact: 257.0 | O(N^6) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 617`, `structural_boundaries: 185`, `args: 98`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1698`, `dead_code: 13`, `orphaned_logic: 17`
* *Architecture:* `import: 19`
* *Defense:* `safety: 3`, `immutability_locks: 108`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cstdlib, point.h, Atropisomers.h, Invariant.h, Ranking.h, QueryOps.h, utility, new_canon.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/SmilesParse/CXSmilesOps.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.464 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.782 IQR)
- **Top Global Matches:** file_cluster_8: 14.464, file_cluster_13: 14.602, file_cluster_11: 14.719
- **Magnitude:** 6043.12 | **LOC:** 2650 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 96
- **Risk Profile:** Cognitive Load (81.2066%), Tech Debt (10.3948%)
**Top Internal Functions/Classes:**
  * `parse_wedged_bonds` (Impact: 2119.8 | O(2^N) | DB: 95)
  * `get_sgroup_data_block` (Impact: 678.0 | O(2^N) | DB: 96)
  * `parse_polymer_sgroup` (Impact: 365.6 | O(N^6) | DB: 37)
  * `parse_variable_attachments` (Impact: 206.7 | O(N^6) | DB: 26)
  * `processCXSmilesLabels` (Impact: 142.6 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 222`, `args: 63`, `func_start: 31`
* *Risk/State:* `state_mutation: 1471`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `import: 19`
* *Defense:* `safety: 3`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` BoostStartInclude.h, MolFileStereochem.h, lexical_cast.hpp, Chirality.h, Atropisomers.h, SmilesWrite.h, algorithm, array...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rdkit/Chem/BRICS.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.989 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.494 IQR)
- **Top Global Matches:** file_cluster_8: 8.989, file_cluster_7: 9.561, file_cluster_13: 9.737
- **Magnitude:** 6015.89 | **LOC:** 1051 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.4173%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 46`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 24`
* *Architecture:* `io: 2`, `api: 19`, `import: 9`
* *Defense:* `safety: 4`, `doc: 14`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` doctest, re, rdkit.Chem, sys, unittest, copy, rdkit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/MolFileParser.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.788 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_8: 14.788, file_cluster_13: 14.809, file_cluster_11: 14.994
- **Magnitude:** 5515.62 | **LOC:** 3779 | **CtrlFlow:** 87.3% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 405
- **Risk Profile:** Cognitive Load (95.8635%), Tech Debt (12.0441%)
**Top Internal Functions/Classes:**
  * `parseEnhancedStereo` (Impact: 4038.4 | O(N^6) | DB: 405)
  * `toInt` (Impact: 32.7 | O(N^2) | DB: 15)
  * `MolFromMolFile` (Impact: 31.1 | O(N^6) | DB: 6)
  * `getV3000Line` (Impact: 22.4 | O(N^3) | DB: 9)
    * *Intent:* *txt == '+') {
  * `MolFromMolBlock` (Impact: 6.4 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 82`, `args: 56`, `func_start: 25`
* *Risk/State:* `state_mutation: 1340`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `import: 34`
* *Defense:* `safety: 66`, `doc: 1`, `immutability_locks: 31`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cstdlib, MolSGroupParsing.h, MolFileStereochem.h, FileParseException.h, Atropisomers.h, QueryOps.h, SubstanceGroup.h, trim.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/RGroupDecomposition/testRGroupDecomp.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.305 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.651 IQR)
- **Top Global Matches:** file_cluster_8: 13.305, file_cluster_13: 13.791, file_cluster_7: 13.815
- **Magnitude:** 5148.34 | **LOC:** 3908 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 253
- **Risk Profile:** Cognitive Load (53.3253%), Tech Debt (20.1927%)
**Top Internal Functions/Classes:**
  * `TEST_CASE` (Impact: 3836.8 | O(2^N) | DB: 253)
  * `TEST_CASE` (Impact: 113.9 | O(2^N) | DB: 38)
  * `TEST_CASE` (Impact: 39.0 | O(N^6) | DB: 18)
  * `CHECK_RGROUP` (Impact: 36.3 | O(N^4) | DB: 12)
    * *Intent:* #define UPTR(m) std::unique_ptr<ROMol>(m)
  * `TEST_CASE` (Impact: 22.4 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 190`, `args: 166`, `func_start: 33`
* *Risk/State:* `state_mutation: 997`, `duplicate_logic: 9`, `orphaned_logic: 1`
* *Architecture:* `import: 16`
* *Defense:* `safety: 4`, `test: 177`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` catch_all.hpp, regex, string, RGroupUtils.h, tokenizer.hpp, RGroupDecompData.h, RDKitBase.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MarvinParse/MarvinDefs.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.034 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.202 IQR)
- **Top Global Matches:** file_cluster_8: 14.034, file_cluster_13: 14.395, file_cluster_11: 14.417
- **Magnitude:** 4829.7 | **LOC:** 4286 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 140
- **Risk Profile:** Cognitive Load (93.4343%), Tech Debt (95.9954%)
**Top Internal Functions/Classes:**
  * `MarvinMolBase::cleanUpNumberingMolsAtoms` (Impact: 993.3 | O(N^6) | DB: 140)
  * `MarvinMolBase::parseAtomsAndBonds` (Impact: 983.6 | O(N^6) | DB: 138)
  * `MarvinDataSgroup::MarvinDataSgroup` (Impact: 125.1 | O(N^6) | DB: 21)
  * `MarvinSruCoModSgroup::MarvinSruCoModSgro` (Impact: 123.0 | O(N^6) | DB: 15)
  * `MarvinSuperatomSgroup::MarvinSuperatomSg` (Impact: 119.1 | O(N^6) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 529`, `structural_boundaries: 281`, `args: 103`, `func_start: 126`
* *Risk/State:* `state_mutation: 1624`, `dead_code: 5`, `duplicate_logic: 21`, `orphaned_logic: 77`
* *Architecture:* `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BoostStartInclude.h, MarvinDefs.h, RDLog.h, string.hpp, BoostEndInclude.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolHash/hashfunctions.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.715 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.82 IQR)
- **Top Global Matches:** file_cluster_8: 13.715, file_cluster_13: 13.969, file_cluster_11: 14.085
- **Magnitude:** 4668.54 | **LOC:** 1471 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 211
- **Risk Profile:** Cognitive Load (95.4115%), Tech Debt (23.8104%)
**Top Internal Functions/Classes:**
  * `getBondFlags` (Impact: 3460.2 | O(2^N) | DB: 211)
  * `NMMolecularFormula` (Impact: 114.7 | O(N^6) | DB: 17)
  * `NormalizeHCount` (Impact: 69.6 | O(N^2) | DB: 13)
  * `AnonymousGraph` (Impact: 48.9 | O(N^6) | DB: 4)
  * `NMDetermineComponents` (Impact: 43.5 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 119`, `args: 65`, `func_start: 28`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 795`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `import: 12`
* *Defense:* `immutability_locks: 27`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cstdlib, string, cstring, nmmolhash.h, RDKitBase.h, SubstructMatch.h, mf.h, cstdio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.135 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.49 IQR)
- **Top Global Matches:** file_cluster_13: 15.135, file_cluster_8: 15.156, file_cluster_11: 15.255
- **Magnitude:** 4086.46 | **LOC:** 2251 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 177
- **Risk Profile:** Cognitive Load (66.0242%), Tech Debt (25.5603%)
**Top Internal Functions/Classes:**
  * `_setMacrocycleTwoInSameRing14Bounds` (Impact: 894.0 | O(N^6) | DB: 177)
  * `_setChain14Bounds` (Impact: 408.2 | O(N^6) | DB: 82)
  * `_set13BoundsHelper` (Impact: 299.9 | O(2^N) | DB: 17)
  * `_checkMacrocycleAllInSameRingAmideEster1` (Impact: 190.5 | O(N^6) | DB: 19)
  * `_checkAndSetBounds` (Impact: 122.5 | O(N^6) | DB: 11)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 135`, `args: 46`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `state_mutation: 1350`, `dead_code: 10`, `fragile_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `doc: 15`, `immutability_locks: 123`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dynamic_bitset.hpp, SymmMatrix.h, Chirality.h, Utils.h, unordered_set, BondStretch.h, algorithm, RDKitBase.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/ForceField/MMFF/testMMFFForceField.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.626 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.876 IQR)
- **Top Global Matches:** file_cluster_8: 14.626, file_cluster_13: 14.836, file_cluster_7: 15.002
- **Magnitude:** 4086.12 | **LOC:** 1885 | **CtrlFlow:** 87.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 571
- **Risk Profile:** Cognitive Load (91.8344%), Tech Debt (11.1166%)
**Top Internal Functions/Classes:**
  * `mmffValidationSuite` (Impact: 1817.6 | O(N^6) | DB: 571)
  * `testMMFFButaneScan` (Impact: 47.5 | O(N^6) | DB: 37)
  * `sortStretchBendInstanceVec` (Impact: 43.4 | O(N^6) | DB: 5)
  * `sortBondStretchInstanceVec` (Impact: 31.1 | O(N^6) | DB: 4)
  * `sortTorsionInstanceVec` (Impact: 24.5 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 343`, `structural_boundaries: 48`, `args: 52`, `func_start: 19`
* *Risk/State:* `state_mutation: 1927`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 28`, `import: 22`
* *Defense:* `safety: 4`, `immutability_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AtomTyper.h, utility, ForceField.h, MolTransforms.h, MolSupplier.h, Builder.h, MolWriters.h, AngleConstraints.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.319 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.434 IQR)
- **Top Global Matches:** file_cluster_8: 14.319, file_cluster_13: 14.533, file_cluster_11: 14.64
- **Magnitude:** 4086.04 | **LOC:** 1983 | **CtrlFlow:** 80.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (91.6802%), Tech Debt (36.6815%)
**Top Internal Functions/Classes:**
  * `HBond::findAcceptorsUnfixed` (Impact: 531.0 | O(N^6) | DB: 81)
  * `HBond::findAcceptors` (Impact: 379.8 | O(N^6) | DB: 54)
    * *Intent:* /* General structure of findAcceptors, findAcceptorsUnfixed, findDonors,
  * `CoulombDielectric::CoulombDielectric` (Impact: 336.2 | O(N^6) | DB: 23)
  * `HBond::findDonorsUnfixed` (Impact: 244.6 | O(N^6) | DB: 42)
    * *Intent:* // because operator() needs length of vector in case of // donors
  * `CoulombDielectric::CoulombDielectric` (Impact: 177.6 | O(N^3) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 94`, `args: 104`, `func_start: 36`
* *Risk/State:* `state_mutation: 1539`, `dead_code: 6`, `duplicate_logic: 4`, `orphaned_logic: 21`
* *Architecture:* `io: 2`, `import: 14`
* *Defense:* `safety: 5`, `immutability_locks: 84`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AtomTyper.h, FileParseException.h, point.h, Params.h, BadFileException.h, Nonbonded.h, RDKitBase.h, SubstructMatch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/RascalMCES/RascalMCES.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.596 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.643 IQR)
- **Top Global Matches:** file_cluster_13: 14.596, file_cluster_8: 14.675, file_cluster_11: 14.786
- **Magnitude:** 4059.68 | **LOC:** 1213 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 238
- **Risk Profile:** Cognitive Load (91.3319%), Tech Debt (14.1497%)
**Top Internal Functions/Classes:**
  * `checkRings` (Impact: 2823.3 | O(2^N) | DB: 238)
    * *Intent:* // make the line graph for the molecule, as an adjacency matrix. Each // row/column is a bond, with ...
  * `getBondLabels` (Impact: 70.1 | O(2^N) | DB: 11)
  * `assignCosts` (Impact: 40.7 | O(N^4) | DB: 14)
  * `tier1Sim` (Impact: 37.1 | O(N^5) | DB: 16)
  * `tier2Sim` (Impact: 35.9 | O(N^6) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 126`, `args: 53`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `state_mutation: 893`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 8`, `immutability_locks: 127`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RascalOptions.h, vector, BoostEndInclude.h, stdexcept, functional, unordered_set, BoostStartInclude.h, new_canon.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Wrap/MolOps.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.524 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.209 IQR)
- **Top Global Matches:** file_cluster_8: 13.524, file_cluster_13: 13.893, file_cluster_7: 13.957
- **Magnitude:** 3905.9 | **LOC:** 3536 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 323
- **Risk Profile:** Cognitive Load (85.9644%), Tech Debt (7.9344%)
**Top Internal Functions/Classes:**
  * `sanitizeMol` (Impact: 2096.5 | O(2^N) | DB: 323)
  * `fragmentOnSomeBondsHelper` (Impact: 131.9 | O(N^6) | DB: 22)
  * `addRecursiveQuery` (Impact: 34.5 | O(N^5) | DB: 7)
  * `splitMolByPDBResidues` (Impact: 29.1 | O(N^6) | DB: 11)
  * `splitMolByPDBChainId` (Impact: 29.1 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 154`, `args: 120`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 1418`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `import: 28`
* *Defense:* `safety: 13`, `immutability_locks: 80`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MolFileStereochem.h, Fingerprints.h, PySequenceHolder.h, rdmolops.h, Chirality.h, CanonicalizeStereoGroups.h, SubstructMatch.h, MonomerInfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FindStereo.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.211 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.011 IQR)
- **Top Global Matches:** file_cluster_8: 14.211, file_cluster_13: 14.303, file_cluster_11: 14.468
- **Magnitude:** 3806.5 | **LOC:** 1281 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 195
- **Risk Profile:** Cognitive Load (81.2918%), Tech Debt (55.1508%)
**Top Internal Functions/Classes:**
  * `getStereoInfo` (Impact: 2043.2 | O(2^N) | DB: 195)
  * `getStereoInfo` (Impact: 861.5 | O(2^N) | DB: 46)
  * `isAtomPotentialTetrahedralCenter` (Impact: 110.7 | O(N^3) | DB: 18)
  * `isAtomPotentialNontetrahedralCenter` (Impact: 19.1 | O(N^1) | DB: 11)
  * `isAtomPotentialStereoAtom` (Impact: 18.5 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 90`, `args: 32`, `func_start: 12`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 736`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `import: 10`
* *Defense:* `doc: 1`, `immutability_locks: 49`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` new_canon.h, dynamic_bitset.hpp, types.h, algorithm, Invariant.h, QueryOps.h, RDKitBase.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/SmilesParse/SmilesWrite.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.492 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.853 IQR)
- **Top Global Matches:** file_cluster_13: 14.492, file_cluster_8: 14.559, file_cluster_11: 14.692
- **Magnitude:** 3764.46 | **LOC:** 1048 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (80.6738%), Tech Debt (11.5557%)
**Top Internal Functions/Classes:**
  * `FragmentSmilesConstruct` (Impact: 1443.4 | O(2^N) | DB: 67)
  * `GetBondSmiles` (Impact: 488.6 | O(N^6) | DB: 39)
  * `MolFragmentToSmiles` (Impact: 416.3 | O(N^6) | DB: 40)
  * `GetAtomSmiles` (Impact: 223.0 | O(N^6) | DB: 37)
  * `getAtomChiralityInfo` (Impact: 177.2 | O(N^6) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 55`, `args: 30`, `func_start: 11`
* *Risk/State:* `state_mutation: 689`, `dead_code: 7`, `orphaned_logic: 3`
* *Architecture:* `import: 20`
* *Defense:* `immutability_locks: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MolFileStereochem.h, Canon.h, ptree.hpp, Atropisomers.h, QueryOps.h, BoostEndInclude.h, new_canon.h, BoostStartInclude.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/AddHs.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.923 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_13: 14.923, file_cluster_11: 14.989, file_cluster_8: 15.008
- **Magnitude:** 3594.7 | **LOC:** 1403 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 198
- **Risk Profile:** Cognitive Load (78.6289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setTerminalAtomCoords` (Impact: 2581.9 | O(2^N) | DB: 198)
  * `AssignHsResidueInfo` (Impact: 112.2 | O(N^6) | DB: 34)
  * `getIsoMap` (Impact: 53.5 | O(N^3) | DB: 18)
  * `pickBisector` (Impact: 21.8 | O(N^6) | DB: 8)
  * `may_need_extra_H` (Impact: 21.5 | O(N^2) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 96`, `args: 28`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 787`, `dead_code: 8`
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `safety: 6`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` classification.hpp, Transform3D.h, QueryOps.h, QueryAtom.h, list, RDKitBase.h, point.h, dynamic_bitset.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/ForceFieldHelpers/UFF/AtomTyper.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.677 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.494 IQR)
- **Top Global Matches:** file_cluster_8: 13.677, file_cluster_13: 13.844, file_cluster_11: 14.066
- **Magnitude:** 3566.72 | **LOC:** 736 | **CtrlFlow:** 95.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 152
- **Risk Profile:** Cognitive Load (88.2143%), Tech Debt (9.4623%)
**Top Internal Functions/Classes:**
  * `addAtomChargeFlags` (Impact: 1657.3 | O(N^6) | DB: 50)
    * *Intent:* // ---------------------------------------------------------------
  * `getAtomLabel` (Impact: 1329.0 | O(2^N) | DB: 152)
    * *Intent:* // ---------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 17`, `args: 8`, `func_start: 7`
* *Risk/State:* `state_mutation: 568`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TorsionAngle.h, AtomTyper.h, Params.h, BondStretch.h, Invariant.h, RDKitBase.h, Nonbonded.h, RDLog.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rdkit/Chem/fmcs/fmcs.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.836 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.724 IQR)
- **Top Global Matches:** file_cluster_8: 11.836, file_cluster_17: 12.037, file_cluster_13: 12.06
- **Magnitude:** 3541.28 | **LOC:** 2825 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (61.5651%), Tech Debt (97.0252%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1130.1 | O(2^N) | DB: 37)
  * `_check_atom_classes` (Impact: 439.2 | O(N^6) | DB: 34)
  * `enumerate_subgraphs` (Impact: 290.1 | O(N^6) | DB: 2)
  * `get_canonical_bondtypes` (Impact: 286.2 | O(2^N) | DB: 4)
    * *Intent:* # The SMILES "", means "single or aromatic" as SMARTS.
  * `all_subgraph_extensions` (Impact: 140.3 | O(N^6) | DB: 2)
    * *Intent:* # I've identified the closure bonds. # Use a stack machine to traverse the graph and build the SMART...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 311`, `args: 106`, `func_start: 100`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 281`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 22`
* *Architecture:* `io: 16`, `api: 92`, `import: 12`
* *Defense:* `safety: 42`, `doc: 2`, `test: 12`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` argparse, re, collections, heapq, time, weakref, fractions, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Descriptors/MolSurf.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.343 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.822 IQR)
- **Top Global Matches:** file_cluster_8: 15.343, file_cluster_13: 15.48, file_cluster_11: 15.628
- **Magnitude:** 3385.86 | **LOC:** 480 | **CtrlFlow:** 94.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 307
- **Risk Profile:** Cognitive Load (98.4676%), Tech Debt (26.5811%)
**Top Internal Functions/Classes:**
  * `getTPSAAtomContribs` (Impact: 2023.5 | O(N^6) | DB: 307)
  * `getLabuteAtomContribs` (Impact: 114.7 | O(N^6) | DB: 41)
  * `calcCustomProp_VSA` (Impact: 32.4 | O(N^6) | DB: 7)
  * `calcSlogP_VSA` (Impact: 22.3 | O(N^6) | DB: 2)
  * `calcSMR_VSA` (Impact: 22.2 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 16`, `args: 21`, `func_start: 9`
* *Risk/State:* `state_mutation: 1110`, `orphaned_logic: 6`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vector, algorithm, format.hpp, RDKitBase.h, MolDescriptors.h, GasteigerCharges.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/SequenceParsers.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.914 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.262 IQR)
- **Top Global Matches:** file_cluster_8: 13.914, file_cluster_13: 14.289, file_cluster_7: 14.332
- **Magnitude:** 3340.68 | **LOC:** 1907 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 172
- **Risk Profile:** Cognitive Load (96.3612%), Tech Debt (10.0498%)
**Top Internal Functions/Classes:**
  * `CreateAminoAcid` (Impact: 1063.2 | O(N^6) | DB: 172)
    * *Intent:* // aa is a three letter PDB residue code
  * `ParseHELM` (Impact: 412.1 | O(N^3) | DB: 168)
  * `CreateNucleicAcid` (Impact: 175.8 | O(N^6) | DB: 75)
  * `CreateAABackbone` (Impact: 37.9 | O(N^6) | DB: 9)
  * `IsHELMMonomerIDChar` (Impact: 12.7 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 713`, `structural_boundaries: 145`, `args: 61`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 1590`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` SequenceParsers.h, string, cstring, MolOps.h, GraphMol.h, MonomerInfo.h, map, vector
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/ChemReactions/Wrap/rdChemReactions.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.944 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.208 IQR)
- **Top Global Matches:** file_cluster_8: 12.944, file_cluster_13: 13.233, file_cluster_7: 13.447
- **Magnitude:** 3283.82 | **LOC:** 1322 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 168
- **Risk Profile:** Cognitive Load (85.7093%), Tech Debt (9.2095%)
**Top Internal Functions/Classes:**
  * `rdChemReactions` (Impact: 2314.6 | O(2^N) | DB: 168)
  * `PreprocessReaction` (Impact: 51.2 | O(N^6) | DB: 15)
  * `AddRecursiveQueriesToReaction` (Impact: 48.8 | O(N^6) | DB: 12)
  * `RemoveUnmappedReactantTemplates` (Impact: 40.1 | O(N^6) | DB: 3)
  * `RemoveUnmappedProductTemplates` (Impact: 40.1 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 88`, `args: 72`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 554`, `orphaned_logic: 2`
* *Architecture:* `import: 18`
* *Defense:* `safety: 22`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SanitException.h, FunctionalGroupHierarchy.h, ReactionFingerprints.h, ReactionUtils.h, FileParseException.h, python.h, SanitizeRxn.h, props.hpp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Code/GraphMol/Descriptors/Wrap/rdMolDescriptors.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.709 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.358 IQR)
- **Top Global Matches:** file_cluster_8: 13.709, file_cluster_13: 14.002, file_cluster_7: 14.158
- **Magnitude:** 3244.58 | **LOC:** 1971 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 349
- **Risk Profile:** Cognitive Load (84.9003%), Tech Debt (9.2036%)
**Top Internal Functions/Classes:**
  * `rdMolDescriptors` (Impact: 974.1 | O(2^N) | DB: 349)
  * `MorganFingerprintHelper` (Impact: 221.9 | O(N^6) | DB: 24)
  * `GetMorganFingerprintBV` (Impact: 112.1 | O(N^5) | DB: 19)
  * `GetUSRDistributionsFromPoints` (Impact: 82.8 | O(N^6) | DB: 9)
  * `GetUSRScore` (Impact: 67.6 | O(N^4) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 98`, `args: 84`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1196`, `orphaned_logic: 3`
* *Architecture:* `import: 18`
* *Defense:* `safety: 19`, `immutability_locks: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.557
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vector, BoostStartInclude.h, OxidationNumbers.h, AtomFeat.h, DCLV.h, BitVects.h, MACCS.h, GraphMol.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Code/GraphMol/MolStandardize/test1.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.314 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.643 IQR)
- **Top Global Matches:** file_cluster_8: 15.314, file_cluster_13: 15.657, file_cluster_7: 15.762
- **Magnitude:** 3198.66 | **LOC:** 1556 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2705
- **Risk Profile:** Cognitive Load (78.5789%), Tech Debt (9.2534%)
**Top Internal Functions/Classes:**
  * `testMetalDisconnectorLigandExpo` (Impact: 24.3 | O(N^6) | DB: 2705)
  * `testCleanup` (Impact: 8.1 | O(N^6) | DB: 26)
  * `testStandardizeSm` (Impact: 6.4 | O(N^6) | DB: 40)
  * `testMetalDisconnector` (Impact: 6.4 | O(N^6) | DB: 53)
  * `testNormalize` (Impact: 6.4 | O(N^6) | DB: 89)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `args: 1198`, `func_start: 10`
* *Risk/State:* `state_mutation: 3099`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 12`
* *Defense:* `safety: 4`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Normalize.h, Invariant.h, RDKitBase.h, MolStandardize.h, ROMol.h, Metal.h, MolSupplier.h, SmilesParse.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Code/GraphMol/DetermineBonds/Wrap/testDetermineBonds.py` (PYTHON) | Magnitude: 146.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 86, branch: 18, structural_boundaries: 13, io: 8
- `Code/GraphMol/Descriptors/Wrap/test3D.py` (PYTHON) | Magnitude: 160.56 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 35, branch: 33, state_mutation: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Code/GraphMol/Aromaticity.cpp` (CPP) | Magnitude: 1944.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 520, indent_spaces: 407, branch: 150, pointers: 109
- `Code/GraphMol/MolDraw2D/StringRect.h` (CPP) | Magnitude: 327.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 207, indent_spaces: 84, branch: 38, structural_boundaries: 9
- `Code/GraphMol/MolDraw2D/DrawShape.h` (CPP) | Magnitude: 575.38 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 549, indent_spaces: 129, args: 68, immutability_locks: 68
- `Code/RDGeneral/RDValue.h` (CPP) | Magnitude: 289.34 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, state_mutation: 151, structural_boundaries: 62, branch: 56
- `Code/GraphMol/Substruct/vf2.hpp` (CPP) | Magnitude: 1002.08 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 562, indent_spaces: 467, branch: 111, pointers: 93

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Code/Demos/boost/EBV_err/classA.h` (CPP) | Magnitude: 15.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, macros: 8, state_mutation: 6, structural_boundaries: 4
- `Code/Demos/boost/cross_mod_err/classA.h` (CPP) | Magnitude: 15.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, macros: 8, state_mutation: 6, structural_boundaries: 4
- `rdkit/Chem/UnitTestSurf.py` (PYTHON) | Magnitude: 218.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 180, branch: 49, structural_boundaries: 36, encapsulation: 36
- `rdkit/ML/Data/test_data/populate.py` (PYTHON) | Magnitude: 14.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 4, import: 3
- `Code/GraphMol/Basement/FeatTrees/FeatTree.h` (CPP) | Magnitude: 19.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 8, import: 5, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `rdkit/Chem/Descriptors3D.py` (PYTHON) | Magnitude: 29.24 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, doc: 26, encapsulation: 26, args: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `External/GA/ga/StringChromosomeBase.h` (CPP) | Magnitude: 0.02 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 4, immutability_locks: 3, generics: 2
- `Code/DataStructs/BitOps.h` (CPP) | Magnitude: 221.1 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 123, pointers: 82, structural_boundaries: 78, immutability_locks: 73
- `Code/GraphMol/SmilesParse/smarts.ll` (YACC) | Magnitude: 134.34 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 128, bitwise_ops: 117, branch: 114, pointers: 114
- `Code/GraphMol/SmilesParse/smiles.ll` (YACC) | Magnitude: 227.62 | Delta: **0.355 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 220, pointers: 204, structural_boundaries: 188, globals: 185

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Code/GraphMol/MolDraw2D/DrawText.cpp` (CPP) | Magnitude: 872.64 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 262, state_mutation: 258, branch: 83, pointers: 52
- `Code/GraphMol/MolDraw2D/DrawMolMCHLasso.cpp` (CPP) | Magnitude: 630.48 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 209, indent_spaces: 206, pointers: 68, branch: 45
- `rdkit/ML/Cluster/Butina.py` (PYTHON) | Magnitude: 150.76 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, branch: 31, state_mutation: 15, structural_boundaries: 12
- `rdkit/TestRunner.py` (PYTHON) | Magnitude: 84.8 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 27, encapsulation: 23, structural_boundaries: 17
- `Code/GraphMol/RGroupDecomposition/RGroupMatch.h` (CPP) | Magnitude: 195.88 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 112, state_mutation: 91, pointers: 46, structural_boundaries: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `rdkit/sping/pid.py` (PYTHON) | Magnitude: 413.48 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 266, structural_boundaries: 72, state_mutation: 57, branch: 50
- `Contrib/pzc/p_con.html` (HTML) | Magnitude: 0.33 | Delta: **0.62 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 52, args: 38, ui_framework: 23, io: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Code/GraphMol/RGroupDecomposition/RGroupFingerprintScore.cpp` (CPP) | Magnitude: 388.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 205, indent_spaces: 197, pointers: 58, structural_boundaries: 39
- `Code/GraphMol/SynthonSpaceSearch/SynthonSpaceSearcher.cpp` (CPP) | Magnitude: 897.64 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 278, indent_spaces: 265, pointers: 91, branch: 77
- `External/YAeHMOP/EHTTools.cpp` (CPP) | Magnitude: 0.23 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 137, indent_spaces: 130, pointers: 43, structural_boundaries: 23
- `Code/Demos/RDKit/MPI/rdkpympi.py` (PYTHON) | Magnitude: 56.3 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, branch: 15, structural_boundaries: 15, concurrency: 12
- `Code/GraphMol/DistGeomHelpers/Embedder.cpp` (CPP) | Magnitude: 1038.64 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 436, state_mutation: 401, pointers: 148, branch: 90

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Code/ForceField/DistanceConstraints.cpp` (CPP) | Magnitude: 163.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 90, indent_spaces: 68, branch: 14, pointers: 14
- `Code/GraphMol/Deprotect/Wrap/rdDeprotect.h` (CPP) | Magnitude: 13.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, reflection_metaprogramming: 2, import: 2, structural_boundaries: 1
- `Code/GraphMol/FragCatalog/Wrap/rdfragcatalog.h` (CPP) | Magnitude: 13.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, reflection_metaprogramming: 2, import: 2, structural_boundaries: 1
- `Code/GraphMol/MolCatalog/Wrap/rdMolCatalog.h` (CPP) | Magnitude: 13.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 3, reflection_metaprogramming: 2, import: 2, structural_boundaries: 1
- `Code/GraphMol/Conformer.cpp` (CPP) | Magnitude: 19.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 15, pointers: 10, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Code/GraphMol/MolDraw2D/Qt/DrawTextQt.h` (CPP) | Magnitude: 65.5 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 49, pointers: 11, indent_spaces: 11, structural_boundaries: 7
- `Code/RDGeneral/BoostEndInclude.h` (CPP) | Magnitude: 27.36 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 15, state_mutation: 12, branch: 9, ownership: 5
- `Code/GraphMol/FileParsers/MolSupplier.v1API.h` (CPP) | Magnitude: 226.42 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 161, state_mutation: 62, structural_boundaries: 38, pointers: 30
- `Code/ForceField/UFF/Utils.cpp` (CPP) | Magnitude: 159.2 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 82, indent_spaces: 52, branch: 18, structural_boundaries: 11
- `Code/GraphMol/Descriptors/GETAWAY.h` (CPP) | Magnitude: 22.3 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 7, structural_boundaries: 5, ownership: 5, macros: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Code/GraphMol/Wrap/MolOps.cpp` -> Churn: **74.49%** | Cog Load: 85.9644% | Debt: 7.9344%
- `Code/GraphMol/Canon.cpp` -> Churn: **72.49%** | Cog Load: 93.5676% | Debt: 13.6802%
- `Code/GraphMol/DistGeomHelpers/catch_tests.cpp` -> Churn: **71.08%** | Cog Load: 80.3144% | Debt: 99.4457%
- `Code/GraphMol/catch_graphmol.cpp` -> Churn: **71.08%** | Cog Load: 69.4828% | Debt: 96.0219%
- `Code/GraphMol/SmilesParse/catch_tests.cpp` -> Churn: **69.75%** | Cog Load: 79.8717% | Debt: 88.779%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rdkit/Chem/BRICS.py` -> **Greg Landrum** (100.0% isolated ownership) | Magnitude: 6015.89
- `Code/GraphMol/MarvinParse/MarvinDefs.cpp` -> **tadhurst-cdd** (100.0% isolated ownership) | Magnitude: 4829.7
- `Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp` -> **Katharina Buchthal** (100.0% isolated ownership) | Magnitude: 4086.46
- `Code/ForceField/MMFF/testMMFFForceField.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 4086.12
- `Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 4086.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Code/RDGeneral/Dict.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `Code/Bench/pickle.cpp` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `Code/GraphMol/CIPLabeler/CIPMol.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `Code/GraphMol/RGroupDecomposition/RGroupData.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 95.6305%)
- `Code/GraphMol/RGroupDecomposition/RGroupDecomp.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9999%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Code/PgSQL/rdkit/rdkit.h` -> **Severity: 6097.0** (Blast Radius: 60.97 * Doc Risk: 100.0%)
- `rdkit/sping/pid.py` -> **Severity: 397.407** (Blast Radius: 4.159 * Doc Risk: 95.5534%)
- `Code/GraphMol/MolStandardize/FragmentCatalog/FragmentCatalogParams.h` -> **Severity: 327.087** (Blast Radius: 3.881 * Doc Risk: 84.2791%)
- `Code/GraphMol/MolStandardize/AcidBaseCatalog/AcidBaseCatalogParams.h` -> **Severity: 319.005** (Blast Radius: 3.881 * Doc Risk: 82.1965%)
- `Code/GraphMol/RGroupDecomposition/RGroupDecomp.h` -> **Severity: 299.092** (Blast Radius: 3.152 * Doc Risk: 94.8895%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
