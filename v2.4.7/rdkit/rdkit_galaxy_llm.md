# ARCHITECTURAL_BRIEF: rdkit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/rdkit` |
| **Timestamp** | `2026-08-07T04:01:51.054888+00:00` |
| **Scan Duration** | `12.39s` |
| **Git Branch** | `master` |
| **Git Commit** | `9e301c15d6c2f5cab848ffaa788300505d69ff94` |
| **Git Remote** | `https://github.com/rdkit/rdkit.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1966 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 99.7 | 37.5 | 33.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 63.5 | 75.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.8 | 25.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.4 | 2.3 | 80.0 |
| API Exposure | 0.0 | 17.5 | 1.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 67.7 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 94.5 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.1 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 74.5 | 4.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 24.3 | 17.3 | 11.9 |
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

- `parseFragment` (@ `External/ChemDraw/fragment.cpp`) -> Impact: **2299.7** | LOC: 973
- `parseEnhancedStereo` (@ `Code/GraphMol/FileParsers/MolFileParser.cpp`) -> Impact: **1209.8** | LOC: 1567
- `TEST_CASE` (@ `Code/GraphMol/MolDraw2D/catch_tests.cpp`) -> Impact: **830.8** | LOC: 1315
- `TEST_CASE` (@ `Code/GraphMol/Depictor/catch_tests.cpp`) -> Impact: **749.0** | LOC: 562
- `TEST_CASE` (@ `Code/GraphMol/RGroupDecomposition/testRGroupDecomp.cpp`) -> Impact: **604.7** | LOC: 1321
- `getTPSAAtomContribs` (@ `Code/GraphMol/Descriptors/MolSurf.cpp`) -> Impact: **586.9** | LOC: 244
- `mmffValidationSuite` (@ `Code/ForceField/MMFF/testMMFFForceField.cpp`) -> Impact: **561.8** | LOC: 1191
- `getBondFlags` (@ `Code/GraphMol/MolHash/hashfunctions.cpp`) -> Impact: **532.1** | LOC: 883
- `MMFFMolProperties::setMMFFHeavyAtomType` (@ `Code/GraphMol/ForceFieldHelpers/MMFF/AtomTyper.cpp`) -> Impact: **526.8** | LOC: 940
  * *Intent:* // sets the MMFF atomType for a heavy atom
- `DrawMol::partitionForLegend` (@ `Code/GraphMol/MolDraw2D/DrawMol.cpp`) -> Impact: **496.3** | LOC: 1336

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Code/GraphMol` | 90 | 36313.32 | 53.04% | 55.21% |
| `Code/GraphMol/FileParsers` | 74 | 33474.88 | 57.2% | 55.26% |
| `Code/GraphMol/MolDraw2D` | 54 | 19394.36 | 55.42% | 42.25% |
| `Code/GraphMol/MolStandardize` | 27 | 13680.92 | 62.24% | 52.33% |
| `rdkit/Chem` | 70 | 12875.83 | 13.25% | 55.3% |
| `Code/GraphMol/Descriptors` | 70 | 11840.62 | 44.32% | 25.44% |
| `Code/GraphMol/SmilesParse` | 24 | 10797.62 | 52.91% | 49.0% |
| `Code/GraphMol/Fingerprints` | 28 | 7867.88 | 40.6% | 31.51% |
| `Code/GraphMol/Wrap` | 55 | 7631.16 | 39.47% | 46.24% |
| `Code/GraphMol/ChemReactions` | 26 | 7448.78 | 55.28% | 53.27% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Code/Bench/descriptors.cpp` -> **100.0%** Exposure
- `Code/Bench/inchi.cpp` -> **100.0%** Exposure
- `Code/Bench/meta.cpp` -> **100.0%** Exposure
- `Code/Bench/mol.cpp` -> **100.0%** Exposure
- `Code/Bench/molops.cpp` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Code/Bench/bench_common.hpp` -> **100.0%** Exposure
- `Code/Bench/descriptors.cpp` -> **100.0%** Exposure
- `Code/Bench/fingerprint.cpp` -> **100.0%** Exposure
- `Code/Bench/inchi.cpp` -> **100.0%** Exposure
- `Code/Bench/mol.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Code/PgSQL/rdkit/sql/rdkit-91.sql` -> **0** Orphaned Functions | **234** Duplicates
- `Code/PgSQL/rdkit/update_sql/rdkit--4.7.0--4.8.0.sql.in` -> **0** Orphaned Functions | **220** Duplicates
- `Code/GraphMol/catch_graphmol.cpp` -> **0** Orphaned Functions | **218** Duplicates
- `Code/PgSQL/rdkit/sql/reaction.sql` -> **0** Orphaned Functions | **172** Duplicates
- `Code/GraphMol/catch_chirality.cpp` -> **0** Orphaned Functions | **148** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `33` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11492` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Code/DataStructs/MultiFPBReader.cpp` (CPP) -> Cumulative Risk: **670.91**
- **Archetype:** `file_cluster_8` (Distance: 13.144 IQR)
- **Magnitude:** 322.48 | **LOC:** 297 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.2758%), Tech Debt (99.0462%)
- **Heaviest Functions:** `get_containing_nbrs` (Impact: 21.4), `generic_nbr_helper` (Impact: 17.2), `tversky_helper` (Impact: 8.9)

### 2. `Code/GraphMol/MolPickler.cpp` (CPP) -> Cumulative Risk: **670.49**
- **Archetype:** `file_cluster_8` (Distance: 12.733 IQR)
- **Magnitude:** 368.68 | **LOC:** 2769 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9982%), Cognitive Load (96.098%), Tech Debt (84.6048%)
- **Heaviest Functions:** `unpickleAtomPDBResidueInfo` (Impact: 28.3), `pickleAtomPDBResidueInfo` (Impact: 25.1), `streamRead` (Impact: 12.8)

### 3. `Code/GraphMol/SynthonSpaceSearch/SynthonSpaceSearch_details.cpp` (CPP) -> Cumulative Risk: **669.47**
- **Archetype:** `file_cluster_11` (Distance: 14.568 IQR)
- **Magnitude:** 1207.28 | **LOC:** 895 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6543%), Safety Score (98.2227%)
- **Heaviest Functions:** `flagRingBonds` (Impact: 109.2), `buildConnRegion` (Impact: 29.9), `checkConnectorsInDifferentFrags` (Impact: 27.7)

### 4. `Code/GraphMol/MolAlign/AlignMolecules.cpp` (CPP) -> Cumulative Risk: **662.17**
- **Archetype:** `file_cluster_8` (Distance: 14.076 IQR)
- **Magnitude:** 758.34 | **LOC:** 479 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0817%), Concurrency (91.3829%)
- **Heaviest Functions:** `getBestRMSInternal` (Impact: 62.6), `alignMolConformers` (Impact: 42.5), `getAllConformerBestRMS` (Impact: 31.1)

### 5. `Code/GraphMol/SynthonSpaceSearch/SynthonSpaceSearcher.cpp` (CPP) -> Cumulative Risk: **661.37**
- **Archetype:** `file_cluster_4` (Distance: 14.4 IQR)
- **Magnitude:** 607.24 | **LOC:** 630 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (97.9313%), Safety Score (96.1128%)
- **Heaviest Functions:** `SynthonSpaceSearcher::SynthonSpaceSearch` (Impact: 112.9), `SynthonSpaceSearcher::buildAllHits` (Impact: 56.4), `SynthonSpaceSearcher::quickVerify` (Impact: 35.2)

### 6. `Code/PgSQL/rdkit/bitstring.c` (C) -> Cumulative Risk: **661.31**
- **Archetype:** `file_cluster_13` (Distance: 15.451 IQR)
- **Magnitude:** 1060.6 | **LOC:** 538 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9962%), Documentation (99.9828%)
- **Heaviest Functions:** `bitstringGrayCmp` (Impact: 23.8), `bitstringRandomSubset` (Impact: 16.8), `bitstringTanimotoSimilarity` (Impact: 15.1)

### 7. `Code/GraphMol/QueryOps.h` (CPP) -> Cumulative Risk: **638.38**
- **Archetype:** `file_cluster_13` (Distance: 13.544 IQR)
- **Magnitude:** 650.26 | **LOC:** 1208 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (95.3398%), Safety Score (89.6645%)
- **Heaviest Functions:** `Match` (Impact: 19.6), `Match` (Impact: 19.6), `queryAtomHasAliphaticHeteroatomNbrs` (Impact: 10.7)

### 8. `Code/GraphMol/RascalMCES/RascalCluster.cpp` (CPP) -> Cumulative Risk: **633.14**
- **Archetype:** `file_cluster_11` (Distance: 13.788 IQR)
- **Magnitude:** 473.0 | **LOC:** 383 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.8345%), Safety Score (97.8215%)
- **Heaviest Functions:** `buildProximityGraph` (Impact: 25.8), `formInitialClusters` (Impact: 17.8), `makeSubClusters` (Impact: 16.0)

### 9. `Code/GraphMol/ROMol.cpp` (CPP) -> Cumulative Risk: **628.27**
- **Archetype:** `file_cluster_13` (Distance: 12.764 IQR)
- **Magnitude:** 172.92 | **LOC:** 715 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9967%), Safety Score (91.7583%)
- **Heaviest Functions:** `ROMol::addAtom` (Impact: 15.2), `ROMol::addBond` (Impact: 10.2), `ROMol::initFromOther` (Impact: 6.9)

### 10. `Code/GraphMol/MolDraw2D/StringRect.h` (CPP) -> Cumulative Risk: **624.8**
- **Archetype:** `file_cluster_11` (Distance: 15.023 IQR)
- **Magnitude:** 291.58 | **LOC:** 124 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9759%), Tech Debt (96.614%)
- **Heaviest Functions:** `doesItIntersect` (Impact: 62.5), `isPointInside` (Impact: 9.2), `calcCorners` (Impact: 3.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rdkit/Chem/BRICS.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.989 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.494 IQR)
- **Top Global Matches:** file_cluster_8: 8.989, file_cluster_7: 9.561, file_cluster_13: 9.737
- **Magnitude:** 6015.89 | **LOC:** 1051 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.4173%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 46`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 24`
* *Architecture:* `io: 2`, `api: 19`, `import: 9`
* *Defense:* `safety: 4`, `doc: 14`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` copy, doctest, sys, unittest, rdkit.Chem, rdkit, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolDraw2D/DrawMol.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.221 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.163 IQR)
- **Top Global Matches:** file_cluster_8: 15.221, file_cluster_13: 15.272, file_cluster_11: 15.305
- **Magnitude:** 4728.92 | **LOC:** 4077 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (92.6769%), Tech Debt (54.5713%)
**Top Internal Functions/Classes:**
  * `DrawMol::partitionForLegend` (Impact: 496.3)
  * `DrawMol::makeDoubleBondLines` (Impact: 468.1)
  * `DrawMol::smoothBondJoins` (Impact: 195.4)
  * `DrawMol::getAtomSymbol` (Impact: 112.5)
    * *Intent:* // ****************************************************************************
  * `DrawMol::getAtomOrientation` (Impact: 78.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 241`, `args: 81`, `func_start: 66`
* *Risk/State:* `state_mutation: 2530`, `dead_code: 15`, `duplicate_logic: 5`, `orphaned_logic: 47`
* *Architecture:* `import: 23`
* *Defense:* `safety: 6`, `immutability_locks: 168`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Transform3D.h, DrawMol.h, MolDraw2DUtils.h, AtomSymbol.h, Atropisomers.h, DrawShape.h, DrawText.h, MolFileStereochem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolDraw2D/catch_tests.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.431 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.616 IQR)
- **Top Global Matches:** file_cluster_8: 13.431, file_cluster_7: 13.913, file_cluster_13: 13.961
- **Magnitude:** 4256.0 | **LOC:** 11099 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (64.8412%), Tech Debt (94.1288%)
**Top Internal Functions/Classes:**
  * `TEST_CASE` (Impact: 830.8)
  * `TEST_CASE` (Impact: 285.6)
  * `TEST_CASE` (Impact: 189.6)
  * `TEST_CASE` (Impact: 67.1)
  * `TEST_CASE` (Impact: 59.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 379`, `args: 352`, `func_start: 138`
* *Risk/State:* `state_mutation: 1969`, `dead_code: 1`, `fragile_debt: 10`, `duplicate_logic: 86`
* *Architecture:* `io: 169`, `import: 24`
* *Defense:* `safety: 27`, `test: 533`, `immutability_locks: 69`, `cleanup: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DrawMol.h, RDKitBase.h, MolDraw2DUtils.h, regex, SmilesParse.h, ReactionParser.h, point.h, cairo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/ForceFieldHelpers/MMFF/AtomTyper.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.997 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.579 IQR)
- **Top Global Matches:** file_cluster_11: 16.997, file_cluster_0: 17.09, file_cluster_17: 17.101
- **Magnitude:** 4073.4 | **LOC:** 3731 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.2987%), Tech Debt (21.3968%)
**Top Internal Functions/Classes:**
  * `MMFFMolProperties::setMMFFHeavyAtomType` (Impact: 526.8)
    * *Intent:* // sets the MMFF atomType for a heavy atom
  * `MMFFMolProperties::computeMMFFCharges` (Impact: 304.1)
    * *Intent:* // Phosphorus
  * `MMFFMolProperties::getMMFFTorsionEmpiric` (Impact: 205.4)
  * `MMFFMolProperties::setMMFFHydrogenType` (Impact: 135.1)
  * `MMFFMolProperties::getMMFFStretchBendPar` (Impact: 51.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 651`, `structural_boundaries: 73`, `args: 54`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `state_mutation: 2401`, `dead_code: 46`, `orphaned_logic: 20`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 190`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Invariant.h, Nonbonded.h, RDKitBase.h, QueryOps.h, cstdarg, dynamic_bitset.hpp, RDLog.h, MolOps.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/MolFileParser.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.787 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_8: 14.787, file_cluster_13: 14.807, file_cluster_11: 14.991
- **Magnitude:** 3496.32 | **LOC:** 3779 | **CtrlFlow:** 87.3% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (95.4055%), Tech Debt (13.3791%)
**Top Internal Functions/Classes:**
  * `parseEnhancedStereo` (Impact: 1209.8)
  * `ParseV3000AtomProps` (Impact: 297.3)
  * `tokenizeV3000Line` (Impact: 149.6)
  * `MolFromMolDataStream` (Impact: 104.6)
  * `ParseSubstitutionCountLine` (Impact: 49.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 82`, `args: 40`, `func_start: 25`
* *Risk/State:* `state_mutation: 1342`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 1`, `import: 34`
* *Defense:* `safety: 66`, `doc: 1`, `immutability_locks: 31`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fstream, locale, Atropisomers.h, regex, RDKitQueries.h, SmilesParse.h, SubstanceGroup.h, MolFileStereochem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Chirality.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.98 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.013 IQR)
- **Top Global Matches:** file_cluster_8: 14.98, file_cluster_13: 15.043, file_cluster_11: 15.096
- **Magnitude:** 3268.54 | **LOC:** 3958 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (81.3184%), Tech Debt (20.5721%)
**Top Internal Functions/Classes:**
  * `atomChiralTypeFromBondDirPseudo3D` (Impact: 293.9)
  * `assignNontetrahedralChiralTypeFrom3D` (Impact: 237.5)
  * `updateDoubleBondNeighbors` (Impact: 136.5)
  * `assignChiralTypesFrom3D` (Impact: 84.9)
    * *Intent:* // because we're only going to hit each ring atom once, the first atom we // encounter in a ring is ...
  * `OctahedralPermFrom3D` (Impact: 82.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 617`, `structural_boundaries: 185`, `args: 84`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1694`, `dead_code: 13`, `orphaned_logic: 19`
* *Architecture:* `import: 19`
* *Defense:* `safety: 3`, `immutability_locks: 108`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utility, RDKitBase.h, Atropisomers.h, optional, point.h, Ranking.h, Invariant.h, utils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolStandardize/test1.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.312 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.643 IQR)
- **Top Global Matches:** file_cluster_8: 15.312, file_cluster_13: 15.655, file_cluster_7: 15.76
- **Magnitude:** 3163.76 | **LOC:** 1556 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (78.5789%), Tech Debt (9.2534%)
**Top Internal Functions/Classes:**
  * `testMetalDisconnectorLigandExpo` (Impact: 10.2)
  * `testOrganometallics` (Impact: 5.8)
  * `testCleanup` (Impact: 3.4)
  * `testStandardizeSm` (Impact: 2.9)
  * `testMetalDisconnector` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `args: 1198`, `func_start: 10`
* *Risk/State:* `state_mutation: 3099`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 12`
* *Defense:* `safety: 4`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Invariant.h, FileParsers.h, MolStandardize.h, RDKitBase.h, ROMol.h, Charge.h, SmilesWrite.h, Fragment.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MarvinParse/MarvinDefs.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.024 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.199 IQR)
- **Top Global Matches:** file_cluster_8: 14.024, file_cluster_13: 14.384, file_cluster_11: 14.407
- **Magnitude:** 2970.7 | **LOC:** 4286 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.2434%), Tech Debt (98.6774%)
**Top Internal Functions/Classes:**
  * `MarvinMolBase::parseAtomsAndBonds` (Impact: 299.5)
  * `MarvinMolBase::cleanUpNumberingMolsAtoms` (Impact: 260.6)
  * `MarvinMolBase::getExplicitValence` (Impact: 46.0)
  * `MarvinMolBase::processSgroupsFromRDKit` (Impact: 43.1)
    * *Intent:* // Now the data groups
  * `MarvinAtom::toPtree` (Impact: 39.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 529`, `structural_boundaries: 281`, `args: 82`, `func_start: 126`
* *Risk/State:* `state_mutation: 1618`, `dead_code: 5`, `duplicate_logic: 25`, `orphaned_logic: 93`
* *Architecture:* `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BoostStartInclude.h, MarvinDefs.h, string.hpp, RDLog.h, BoostEndInclude.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/SmilesParse/CXSmilesOps.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.417 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.783 IQR)
- **Top Global Matches:** file_cluster_8: 14.417, file_cluster_13: 14.555, file_cluster_11: 14.673
- **Magnitude:** 2904.62 | **LOC:** 2650 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (81.2066%), Tech Debt (13.6266%)
**Top Internal Functions/Classes:**
  * `parse_wedged_bonds` (Impact: 312.1)
  * `parse_it` (Impact: 236.3)
  * `parse_polymer_sgroup` (Impact: 108.4)
  * `get_sgroup_data_block` (Impact: 106.4)
  * `get_sgroup_polymer_block` (Impact: 63.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 222`, `args: 40`, `func_start: 31`
* *Risk/State:* `state_mutation: 1467`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `import: 19`
* *Defense:* `safety: 3`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` SmilesParseOps.h, algorithm, RDKitBase.h, MolFileStereochem.h, BoostStartInclude.h, Atropisomers.h, string.hpp, LinkNode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/ForceField/MMFF/testMMFFForceField.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.607 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.883 IQR)
- **Top Global Matches:** file_cluster_8: 14.607, file_cluster_13: 14.818, file_cluster_7: 14.984
- **Magnitude:** 2671.62 | **LOC:** 1885 | **CtrlFlow:** 87.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.8344%), Tech Debt (11.1166%)
**Top Internal Functions/Classes:**
  * `mmffValidationSuite` (Impact: 561.8)
  * `sortTorsionInstanceVec` (Impact: 16.7)
  * `testMMFFButaneScan` (Impact: 14.0)
  * `sortAngleBendInstanceVec` (Impact: 13.1)
  * `sortStretchBendInstanceVec` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 343`, `structural_boundaries: 48`, `args: 41`, `func_start: 19`
* *Risk/State:* `state_mutation: 1927`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 28`, `import: 22`
* *Defense:* `safety: 4`, `immutability_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utility, fstream, RDKitBase.h, testMMFFForceField.h, MolWriters.h, MolSupplier.h, string, test.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/catch_chirality.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.876 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_8: 12.876, file_cluster_7: 13.391, file_cluster_13: 13.462
- **Magnitude:** 2498.14 | **LOC:** 6557 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (49.0976%), Tech Debt (99.998%)
**Top Internal Functions/Classes:**
  * `TEST_CASE` (Impact: 141.0)
  * `SECTION` (Impact: 136.7)
  * `TEST_CASE` (Impact: 121.0)
  * `SECTION` (Impact: 120.8)
  * `TEST_CASE` (Impact: 45.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 422`, `args: 357`, `func_start: 254`
* *Risk/State:* `state_mutation: 1081`, `dead_code: 3`, `fragile_debt: 17`, `duplicate_logic: 148`
* *Architecture:* `import: 17`
* *Defense:* `safety: 30`, `test: 1165`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FileParsers.h, SmilesParse.h, RDKitBase.h, CIPLabeler.h, noncopyable.hpp, MolFileStereochem.h, test_fixtures.h, ranges...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolDraw2D/test1.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.826 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.525 IQR)
- **Top Global Matches:** file_cluster_8: 13.826, file_cluster_13: 14.149, file_cluster_7: 14.259
- **Magnitude:** 2457.22 | **LOC:** 4714 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (83.0429%), Tech Debt (10.1521%)
**Top Internal Functions/Classes:**
  * `test9MolLegends` (Impact: 269.6)
  * `test11DrawMolGrid` (Impact: 231.3)
  * `testDeuteriumTritium` (Impact: 54.2)
  * `check_file_hash` (Impact: 16.7)
  * `test1` (Impact: 15.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 162`, `args: 104`, `func_start: 35`
* *Risk/State:* `state_mutation: 1747`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 94`, `import: 25`
* *Defense:* `safety: 7`, `immutability_locks: 18`, `cleanup: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fstream, RDKitBase.h, MolDraw2DUtils.h, regex, SmilesParse.h, MolSupplier.h, cairo.h, map...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.277 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.432 IQR)
- **Top Global Matches:** file_cluster_8: 14.277, file_cluster_13: 14.492, file_cluster_11: 14.599
- **Magnitude:** 2446.14 | **LOC:** 1983 | **CtrlFlow:** 80.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.6802%), Tech Debt (36.6815%)
**Top Internal Functions/Classes:**
  * `HBond::findAcceptorsUnfixed` (Impact: 160.9)
  * `HBond::findAcceptors` (Impact: 114.8)
    * *Intent:* /* General structure of findAcceptors, findAcceptorsUnfixed, findDonors,
  * `CoulombDielectric::CoulombDielectric` (Impact: 99.0)
  * `CoulombDielectric::CoulombDielectric` (Impact: 90.5)
  * `HBond::findDonorsUnfixed` (Impact: 74.6)
    * *Intent:* // because operator() needs length of vector in case of // donors
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 94`, `args: 75`, `func_start: 36`
* *Risk/State:* `state_mutation: 1539`, `dead_code: 6`, `duplicate_logic: 4`, `orphaned_logic: 21`
* *Architecture:* `io: 2`, `import: 14`
* *Defense:* `safety: 5`, `immutability_locks: 84`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BadFileException.h, Nonbonded.h, SubstructMatch.h, fstream, RDKitBase.h, AtomTyper.h, Params.h, vector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Depictor/catch_tests.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.689 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 5.545 IQR)
- **Top Global Matches:** file_cluster_8: 12.689, file_cluster_7: 13.231, file_cluster_13: 13.296
- **Magnitude:** 2421.6 | **LOC:** 2526 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (43.6552%), Tech Debt (99.097%)
**Top Internal Functions/Classes:**
  * `TEST_CASE` (Impact: 749.0)
  * `SECTION` (Impact: 226.1)
  * `SECTION` (Impact: 192.1)
    * *Intent:* // the "rebuild" alignment should succeed and preserve molblock wedging // (inverted with respect to...
  * `TEST_CASE` (Impact: 125.5)
  * `TEST_CASE` (Impact: 85.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 219`, `args: 95`, `func_start: 63`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 495`, `duplicate_logic: 63`
* *Architecture:* `import: 13`
* *Defense:* `safety: 7`, `test: 603`, `immutability_locks: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` FileParsers.h, RDKitBase.h, AlignMolecules.h, MolFileStereochem.h, test_fixtures.h, ranges, SmilesWrite.h, DepictUtils.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/DistGeomHelpers/testDgeomHelpers.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.763 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.816 IQR)
- **Top Global Matches:** file_cluster_8: 14.763, file_cluster_13: 14.932, file_cluster_0: 15.179
- **Magnitude:** 2352.3 | **LOC:** 2592 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (79.9043%), Tech Debt (9.5716%)
**Top Internal Functions/Classes:**
  * `testGithub971` (Impact: 23.5)
  * `runblock` (Impact: 17.2)
  * `testMultiThread` (Impact: 16.2)
  * `test2` (Impact: 14.4)
  * `test1` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 91`, `args: 159`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 2065`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 12`, `import: 29`
* *Defense:* `safety: 14`, `immutability_locks: 28`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` RDKitBase.h, versions.h, AlignMolecules.h, MolWriters.h, Builder.h, SmilesParse.h, BoundsMatrix.h, MolSupplier.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Wrap/MolOps.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.481 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.218 IQR)
- **Top Global Matches:** file_cluster_8: 13.481, file_cluster_13: 13.852, file_cluster_7: 13.915
- **Magnitude:** 2322.9 | **LOC:** 3536 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (86.1381%), Tech Debt (7.9344%)
**Top Internal Functions/Classes:**
  * `sanitizeMol` (Impact: 356.5)
  * `wrap` (Impact: 272.9)
  * `fragmentOnSomeBondsHelper` (Impact: 40.0)
  * `GetMolFragsWithMapping` (Impact: 36.1)
  * `addRecursiveQuery` (Impact: 12.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 154`, `args: 83`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 1416`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `import: 28`
* *Defense:* `safety: 13`, `immutability_locks: 80`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CanonicalizeStereoGroups.h, RDKitBase.h, substructmethods.h, RDKitQueries.h, SubgraphUtils.h, string, ChemTransforms.h, MolFileStereochem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/SequenceParsers.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.909 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.264 IQR)
- **Top Global Matches:** file_cluster_8: 13.909, file_cluster_13: 14.283, file_cluster_7: 14.327
- **Magnitude:** 2253.48 | **LOC:** 1907 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3612%), Tech Debt (10.0498%)
**Top Internal Functions/Classes:**
  * `CreateAminoAcid` (Impact: 322.4)
    * *Intent:* // aa is a three letter PDB residue code
  * `ParseHELM` (Impact: 211.2)
  * `CreateNucleicAcid` (Impact: 56.7)
  * `IsHELMMonomerIDChar` (Impact: 12.7)
  * `CreateAABackbone` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 713`, `structural_boundaries: 145`, `args: 57`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 1590`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cstring, MonomerInfo.h, string, vector, GraphMol.h, MolOps.h, map, SequenceParsers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/DistGeomHelpers/BoundsMatrixBuilder.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.124 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.492 IQR)
- **Top Global Matches:** file_cluster_13: 15.124, file_cluster_8: 15.145, file_cluster_11: 15.243
- **Magnitude:** 2209.26 | **LOC:** 2251 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.0242%), Tech Debt (25.5603%)
**Top Internal Functions/Classes:**
  * `_setMacrocycleTwoInSameRing14Bounds` (Impact: 271.7)
  * `_setChain14Bounds` (Impact: 123.2)
  * `_checkMacrocycleAllInSameRingAmideEster1` (Impact: 56.2)
  * `_set13BoundsHelper` (Impact: 45.3)
  * `_checkAndSetBounds` (Impact: 36.5)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 135`, `args: 40`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `state_mutation: 1350`, `dead_code: 10`, `fragile_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `doc: 15`, `immutability_locks: 123`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Exceptions.h, algorithm, RDKitBase.h, TriangleSmooth.h, BondStretch.h, utils.h, RDLog.h, dynamic_bitset.hpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/MolStandardize/testTautomer.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.739 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.239 IQR)
- **Top Global Matches:** file_cluster_8: 14.739, file_cluster_13: 14.984, file_cluster_11: 15.087
- **Magnitude:** 2088.54 | **LOC:** 1791 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.8524%), Tech Debt (10.0839%)
**Top Internal Functions/Classes:**
  * `testEnumeratorParams` (Impact: 137.5)
  * `testEnumeratorCallback` (Impact: 23.3)
  * `testEnumerator` (Impact: 22.4)
  * `testCanonicalizePreservesNonTautomericBo` (Impact: 21.2)
  * `testCanonicalizeInvariantAcrossInputTaut` (Impact: 19.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 151`, `args: 293`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 1746`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 26`, `immutability_locks: 92`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RDKitBase.h, CIPLabeler.h, test_fixtures.h, SmilesWrite.h, ctime, Tautomer.h, SmilesParse.h, cstdlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/testMolWriter.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.467 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.133 IQR)
- **Top Global Matches:** file_cluster_8: 14.467, file_cluster_13: 14.782, file_cluster_7: 14.935
- **Magnitude:** 2030.06 | **LOC:** 1855 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (53.704%), Tech Debt (8.2866%)
**Top Internal Functions/Classes:**
  * `testRGPMolFileWriterV2KV3K` (Impact: 21.9)
  * `testIssue3525000` (Impact: 21.0)
  * `testMolFileGithub8265` (Impact: 18.7)
  * `testSmilesWriterStrm` (Impact: 12.7)
  * `testSmilesWriter` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 57`, `args: 18`, `func_start: 32`
* *Risk/State:* `state_mutation: 1807`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `import: 15`
* *Defense:* `safety: 20`, `immutability_locks: 2`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` test.h, fstream, RDKitBase.h, MolWriters.h, CIPLabeler.h, test_fixtures.h, StreamOps.h, RDLog.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/RascalMCES/RascalMCES.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.549 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.631 IQR)
- **Top Global Matches:** file_cluster_13: 14.549, file_cluster_8: 14.627, file_cluster_11: 14.739
- **Magnitude:** 2009.48 | **LOC:** 1213 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.7263%), Tech Debt (26.0676%)
**Top Internal Functions/Classes:**
  * `checkRings` (Impact: 430.4)
    * *Intent:* // make the line graph for the molecule, as an adjacency matrix. Each // row/column is a bond, with ...
  * `calcLowerBound` (Impact: 224.2)
  * `updateMaxClique` (Impact: 52.9)
  * `buildPairs` (Impact: 49.8)
    * *Intent:* // make sure that mol1_bond in mol1 and mol2_bond in mol2 are, in at least one // ring that is the s...
  * `makeModularProduct` (Impact: 46.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 126`, `args: 49`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `state_mutation: 881`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 8`, `immutability_locks: 127`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RascalDetails.h, regex, SmilesParse.h, unordered_set, map, stdexcept, RascalMCES.h, RascalResult.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/Fingerprints/testFingerprintGenerators.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.004 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.238 IQR)
- **Top Global Matches:** file_cluster_8: 14.004, file_cluster_13: 14.444, file_cluster_7: 14.463
- **Magnitude:** 2004.06 | **LOC:** 2511 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.3962%), Tech Debt (9.2547%)
**Top Internal Functions/Classes:**
  * `testGitHubIssue695` (Impact: 31.0)
  * `testBulkFP` (Impact: 15.6)
  * `testRDKFPUnfolded` (Impact: 9.5)
  * `testAtomPairNonSparseBitvector` (Impact: 8.7)
    * *Intent:* // todo this test needs to be updated since the fingerprint size logic is // changed, count simulati...
  * `testAtomPairFPDifference` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 71`, `args: 74`, `func_start: 35`
* *Risk/State:* `state_mutation: 1783`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `import: 14`
* *Defense:* `safety: 4`, `immutability_locks: 21`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomPairGenerator.h, FileParsers.h, test.h, RDKitBase.h, MorganFingerprints.h, Fingerprints.h, RDLog.h, TopologicalTorsionGenerator.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/FileParsers/file_parsers_catch.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.947 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 4.87 IQR)
- **Top Global Matches:** file_cluster_8: 12.947, file_cluster_7: 13.481, file_cluster_13: 13.487
- **Magnitude:** 1999.7 | **LOC:** 8062 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (41.5122%), Tech Debt (99.3181%)
**Top Internal Functions/Classes:**
  * `TEST_CASE` (Impact: 250.8)
  * `SECTION` (Impact: 75.5)
  * `TEST_CASE` (Impact: 74.7)
  * `TEST_CASE` (Impact: 74.6)
  * `TEST_CASE` (Impact: 67.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 261`, `args: 174`, `func_start: 199`
* *Risk/State:* `state_mutation: 903`, `dead_code: 1`, `fragile_debt: 14`, `duplicate_logic: 71`
* *Architecture:* `io: 6`, `import: 28`
* *Defense:* `safety: 41`, `test: 833`, `immutability_locks: 41`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fstream, RDKitBase.h, MolWriters.h, streambuf, SmilesParse.h, SequenceParsers.h, MolSupplier.h, string...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/StructChecker/Stereo.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.651 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.503 IQR)
- **Top Global Matches:** file_cluster_8: 14.651, file_cluster_13: 14.865, file_cluster_11: 14.977
- **Magnitude:** 1939.72 | **LOC:** 973 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.9359%), Tech Debt (23.6391%)
**Top Internal Functions/Classes:**
  * `FixDubious3DMolecule` (Impact: 100.2)
  * `Atom4Parity` (Impact: 91.7)
  * `CisTransPerception` (Impact: 90.6)
  * `DubiousStereochemistry` (Impact: 67.9)
  * `AtomParity` (Impact: 64.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 43`, `args: 31`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `state_mutation: 1290`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` StructChecker.h, Stereo.h, RDKitBase.h, Utilites.h, point.h, cmath, types.h, format.hpp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Code/GraphMol/catch_graphmol.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.34 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 5.367 IQR)
- **Top Global Matches:** file_cluster_8: 13.34, file_cluster_13: 13.793, file_cluster_7: 13.849
- **Magnitude:** 1915.66 | **LOC:** 5020 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (67.3298%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `TEST_CASE` (Impact: 150.4)
  * `TEST_CASE` (Impact: 26.7)
  * `SECTION` (Impact: 24.6)
  * `TEST_CASE` (Impact: 23.6)
  * `SECTION` (Impact: 22.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 240`, `args: 262`, `func_start: 219`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 912`, `fragile_debt: 18`, `duplicate_logic: 218`
* *Architecture:* `import: 22`
* *Defense:* `safety: 58`, `test: 892`, `immutability_locks: 61`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fstream, RDKitBase.h, SmilesParse.h, RDKitQueries.h, SequenceParsers.h, string, MolPickler.h, random...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Code/GraphMol/DetermineBonds/Wrap/testDetermineBonds.py` (PYTHON) | Magnitude: 50.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 86, branch: 18, structural_boundaries: 13, io: 8
- `Code/GraphMol/Descriptors/Wrap/test3D.py` (PYTHON) | Magnitude: 124.26 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 35, branch: 33, state_mutation: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Code/GraphMol/Aromaticity.cpp` (CPP) | Magnitude: 1025.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 520, indent_spaces: 407, branch: 150, pointers: 109
- `Code/GraphMol/MolDraw2D/StringRect.h` (CPP) | Magnitude: 291.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 207, indent_spaces: 84, branch: 38, structural_boundaries: 9
- `Code/GraphMol/MolDraw2D/DrawShape.h` (CPP) | Magnitude: 575.38 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 549, indent_spaces: 129, args: 68, immutability_locks: 68
- `Code/RDGeneral/RDValue.h` (CPP) | Magnitude: 227.04 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, state_mutation: 151, structural_boundaries: 62, branch: 56
- `Code/GraphMol/Substruct/vf2.hpp` (CPP) | Magnitude: 785.78 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 562, indent_spaces: 467, branch: 111, pointers: 93

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Code/Demos/boost/EBV_err/classA.h` (CPP) | Magnitude: 15.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, macros: 8, state_mutation: 6, structural_boundaries: 4
- `Code/Demos/boost/cross_mod_err/classA.h` (CPP) | Magnitude: 15.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, macros: 8, state_mutation: 6, structural_boundaries: 4
- `rdkit/Chem/UnitTestSurf.py` (PYTHON) | Magnitude: 153.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
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
- `Code/DataStructs/BitOps.h` (CPP) | Magnitude: 154.5 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 123, pointers: 82, structural_boundaries: 78, immutability_locks: 73
- `Code/GraphMol/SmilesParse/smarts.ll` (YACC) | Magnitude: 134.34 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 128, bitwise_ops: 117, branch: 114, pointers: 114
- `Code/GraphMol/SmilesParse/smiles.ll` (YACC) | Magnitude: 227.62 | Delta: **0.355 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 220, pointers: 204, structural_boundaries: 188, globals: 185

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Code/GraphMol/MolDraw2D/DrawText.cpp` (CPP) | Magnitude: 526.54 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 262, state_mutation: 256, branch: 83, pointers: 52
- `Code/GraphMol/MolDraw2D/DrawMolMCHLasso.cpp` (CPP) | Magnitude: 422.38 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 209, indent_spaces: 206, pointers: 68, branch: 45
- `rdkit/ML/Cluster/Butina.py` (PYTHON) | Magnitude: 111.06 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, branch: 31, state_mutation: 15, structural_boundaries: 12
- `rdkit/TestRunner.py` (PYTHON) | Magnitude: 75.3 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 27, encapsulation: 23, structural_boundaries: 17
- `Code/GraphMol/RGroupDecomposition/RGroupMatch.h` (CPP) | Magnitude: 130.68 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 112, state_mutation: 91, pointers: 46, structural_boundaries: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `rdkit/sping/pid.py` (PYTHON) | Magnitude: 222.98 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 266, structural_boundaries: 72, state_mutation: 57, branch: 50
- `Contrib/pzc/p_con.html` (HTML) | Magnitude: 0.33 | Delta: **0.62 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 52, args: 38, ui_framework: 23, io: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Code/GraphMol/RGroupDecomposition/RGroupFingerprintScore.cpp` (CPP) | Magnitude: 323.36 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 205, indent_spaces: 197, pointers: 58, structural_boundaries: 39
- `Code/GraphMol/SynthonSpaceSearch/SynthonSpaceSearcher.cpp` (CPP) | Magnitude: 607.24 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 278, indent_spaces: 265, pointers: 91, branch: 77
- `External/YAeHMOP/EHTTools.cpp` (CPP) | Magnitude: 0.19 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 137, indent_spaces: 130, pointers: 43, structural_boundaries: 23
- `Code/Demos/RDKit/MPI/rdkpympi.py` (PYTHON) | Magnitude: 47.3 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, branch: 15, structural_boundaries: 15, concurrency: 12
- `Code/GraphMol/DistGeomHelpers/Embedder.cpp` (CPP) | Magnitude: 677.54 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 436, state_mutation: 401, pointers: 148, branch: 90

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Code/ForceField/DistanceConstraints.cpp` (CPP) | Magnitude: 131.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
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
- `Code/GraphMol/FileParsers/MolSupplier.v1API.h` (CPP) | Magnitude: 124.12 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 161, state_mutation: 62, structural_boundaries: 38, pointers: 30
- `Code/ForceField/UFF/Utils.cpp` (CPP) | Magnitude: 123.9 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 82, indent_spaces: 52, branch: 18, structural_boundaries: 11
- `Code/GraphMol/Descriptors/GETAWAY.h` (CPP) | Magnitude: 22.3 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 7, structural_boundaries: 5, ownership: 5, macros: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Code/GraphMol/Wrap/MolOps.cpp` -> Churn: **74.49%** | Cog Load: 86.1381% | Debt: 7.9344%
- `Code/GraphMol/Canon.cpp` -> Churn: **72.49%** | Cog Load: 76.5886% | Debt: 17.5129%
- `Code/GraphMol/DistGeomHelpers/catch_tests.cpp` -> Churn: **71.08%** | Cog Load: 81.6035% | Debt: 100.0%
- `Code/GraphMol/catch_graphmol.cpp` -> Churn: **71.08%** | Cog Load: 67.3298% | Debt: 100.0%
- `Code/GraphMol/SmilesParse/catch_tests.cpp` -> Churn: **69.75%** | Cog Load: 81.9612% | Debt: 99.9991%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rdkit/Chem/BRICS.py` -> **Greg Landrum** (100.0% isolated ownership) | Magnitude: 6015.89
- `Code/GraphMol/MolStandardize/test1.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 3163.76
- `Code/GraphMol/MarvinParse/MarvinDefs.cpp` -> **tadhurst-cdd** (100.0% isolated ownership) | Magnitude: 2970.7
- `Code/ForceField/MMFF/testMMFFForceField.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 2671.62
- `Code/GraphMol/MolInteractionFields/MIFDescriptors.cpp` -> **Ricardo Rodriguez** (100.0% isolated ownership) | Magnitude: 2446.14

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
- `rdkit/sping/pid.py` -> **Severity: 364.297** (Blast Radius: 4.159 * Doc Risk: 87.5925%)
- `rdkit/sping/colors.py` -> **Severity: 250.044** (Blast Radius: 4.016 * Doc Risk: 62.2619%)
- `Code/GraphMol/MolStandardize/FragmentCatalog/FragmentCatalogParams.h` -> **Severity: 217.933** (Blast Radius: 3.881 * Doc Risk: 56.1539%)
- `Code/GraphMol/MolStandardize/AcidBaseCatalog/AcidBaseCatalogParams.h` -> **Severity: 214.566** (Blast Radius: 3.881 * Doc Risk: 55.2863%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
