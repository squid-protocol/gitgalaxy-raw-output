# ARCHITECTURAL_BRIEF: ngl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/ngl` |
| **Timestamp** | `2026-08-03T20:06:15.233112+00:00` |
| **Scan Duration** | `2.43s` |
| **Git Branch** | `master` |
| **Git Commit** | `60be69b5fe0e9c43cb3a06fe1cb691fa9478c790` |
| **Git Remote** | `https://github.com/nglviewer/ngl.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 503 malicious artifacts.

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
| Total Artifacts | 1128 |
| Analyzed Artifacts (Scanned) | 538 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 590 |
| Total LOC | 51439 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 47.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4367 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2246 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 31.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5957 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 301 | 39172 | 55.9% |
| JAVASCRIPT | 164 | 9736 | 30.5% |
| GLSL | 32 | 1279 | 5.9% |
| MARKDOWN | 16 | 0 | 3.0% |
| HTML | 6 | 355 | 1.1% |
| PLAINTEXT | 5 | 0 | 0.9% |
| JSON | 3 | 94 | 0.6% |
| CSS | 3 | 440 | 0.6% |
| PYTHON | 3 | 86 | 0.6% |
| SHELL | 3 | 57 | 0.6% |
| CSV | 1 | 220 | 0.2% |
| XML | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.263`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 271 | 50.4% |
| file_cluster_13 | 204 | 37.9% |
| file_cluster_4 | 26 | 4.8% |
| file_cluster_11 | 4 | 0.7% |
| file_cluster_9 | 4 | 0.7% |
| file_cluster_0 | 3 | 0.6% |
| file_cluster_17 | 3 | 0.6% |
| file_cluster_12 | 2 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 21 | 3.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 590*

**Composition by Extension & Reason:**
- `.ts`: 334x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 66 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 4712 commas in 986 LOC)
- `.pdb`: 54x Excluded (Unsupported Extension: '.pdb'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cif`: 19x Excluded (Unsupported Extension: '.cif'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 18x Excluded (Explicitly Denied Extension: '.png')
- `.gz`: 17x Excluded (Explicitly Denied Extension: '.gz')
- `.gro`: 13x Excluded (Unsupported Extension: '.gro'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xvg`: 9x Excluded (Unsupported Extension: '.xvg')
- `.js`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.sdf`: 4x Excluded (Unsupported Extension: '.sdf'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mmtf`: 4x Excluded (Unsupported Extension: '.mmtf'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ccp4`: 3x Excluded (Unsupported Extension: '.ccp4'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.sublime-project')
- `.mol2`: 3x Excluded (Unsupported Extension: '.mol2'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 31.7 | 29.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 49.9 | 63.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.3 | 2.4 | 0.0 |
| API Exposure | 0.0 | 14.9 | 3.7 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 51.9 | 80.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 26.5 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `examples/js/gui.js` (Hits: 27)
- `scripts/js/node/download.js` (Hits: 18)
- `scripts/js/slimer/gallery.js` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **globals.ts** (`src/globals.ts`) — 153 inbound connections
2. **atom-proxy.ts** (`src/proxy/atom-proxy.ts`) — 61 inbound connections
3. **viewer.ts** (`src/viewer/viewer.ts`) — 49 inbound connections
4. **structure.ts** (`src/structure/structure.ts`) — 48 inbound connections
5. **buffer.ts** (`src/buffer/buffer.ts`) — 42 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ngl.ts** (`src/ngl.ts`) — 84 outbound dependencies
2. **structure-component.ts** (`src/component/structure-component.ts`) — 38 outbound dependencies
3. **stage.ts** (`src/stage/stage.ts`) — 37 outbound dependencies
4. **structure.ts** (`src/structure/structure.ts`) — 37 outbound dependencies
5. **structure-view.ts** (`src/structure/structure-view.ts`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `EDTSurface` (@ `src/surface/edt-surface.ts`) -> Impact: **2872.4** | LOC: 786
- `_parse` (@ `src/parser/pdb-parser.ts`) -> Impact: **1390.3** | LOC: 612
  * *Intent:* /** * Create a pdb parser * @param {Streamer} streamer - streamer object * @param {Object} params - params object * @param {Boolean} params.hex - hexa...
- `_parse` (@ `src/parser/cif-parser.ts`) -> Impact: **869.6** | LOC: 273
  * *Intent:* //
- `parseSele` (@ `src/selection/selection-parser.ts`) -> Impact: **841.8** | LOC: 468
- `_parse` (@ `src/parser/sdf-parser.ts`) -> Impact: **625.8** | LOC: 219
- `_parse` (@ `src/parser/prmtop-parser.ts`) -> Impact: **453.2** | LOC: 196
- `_parse` (@ `src/parser/mmtf-parser.ts`) -> Impact: **416.0** | LOC: 352
- `_parse` (@ `src/parser/mol2-parser.ts`) -> Impact: **340.8** | LOC: 165
- `assignSecondaryStructure` (@ `src/structure/structure-utils.ts`) -> Impact: **320.0** | LOC: 164
- `_parse` (@ `src/parser/xtc-parser.ts`) -> Impact: **297.9** | LOC: 242

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `EDTSurface` (@ `src/surface/edt-surface.ts`) -> **O(2^N) [Recursive]**
- `getExampleNames` (@ `scripts/makeScriptsList.js`) -> **O(2^N) [Recursive]**
- `transform` (@ `src/align/superposition.ts`) -> **O(2^N) [Recursive]**
- `_parse` (@ `src/parser/dsn6-parser.ts`) -> **O(2^N) [Recursive]**
- `_parse` (@ `src/parser/mmtf-parser.ts`) -> **O(2^N) [Recursive]**
- `_parse` (@ `src/parser/pdb-parser.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Create a pdb parser * @param {Streamer} streamer - streamer object * @param {Object} params - params object * @param {Boolean} params.hex - hexa...
- `_parse` (@ `src/parser/sdf-parser.ts`) -> **O(2^N) [Recursive]**
- `_parse` (@ `src/parser/xtc-parser.ts`) -> **O(2^N) [Recursive]**
- `assignSecondaryStructure` (@ `src/structure/structure-utils.ts`) -> **O(2^N) [Recursive]**
- `calculateBondsBetween` (@ `src/structure/structure-utils.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `EDTSurface` (@ `src/surface/edt-surface.ts`) -> DB Complexity: **113**
- `reset` (@ `src/geometry/spline.ts`) -> DB Complexity: **89**
- `trace` (@ `src/align/alignment.ts`) -> DB Complexity: **78**
- `_createParserState` (@ `src/parser/obj-parser.ts`) -> DB Complexity: **72**
- `_parse` (@ `src/parser/pdb-parser.ts`) -> DB Complexity: **64**
  * *Intent:* /** * Create a pdb parser * @param {Streamer} streamer - streamer object * @param {Object} params - params object * @param {Boolean} params.hex - hexa...
- `describe` (@ `test/utils/tests-bitarray.spec.ts`) -> DB Complexity: **63**
- `StructureComponentWidget` (@ `examples/js/gui.js`) -> DB Complexity: **60**
- `getLabel` (@ `src/controls/picking-proxy.ts`) -> DB Complexity: **60**
  * *Intent:* //console.log(scaleFactor, cp.distanceTo(acp), radius/scaleFactor, radius)
- `addAtom` (@ `src/structure/structure-builder.ts`) -> DB Complexity: **59**
- `getFileInfo` (@ `src/loader/loader-utils.ts`) -> DB Complexity: **58**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `examples/js/ui` | 3 | 2075.82 | 97.78% | 0.0% |
| `examples/js` | 1 | 1424.38 | 61.46% | 0.0% |
| `examples/scripts/interactive` | 9 | 1224.02 | 66.43% | 0.0% |
| `src/parser` | 37 | 948.08 | 48.73% | 28.78% |
| `examples/scripts/test` | 27 | 710.02 | 21.08% | 0.0% |
| `examples/scripts/parser` | 40 | 691.1 | 19.09% | 0.0% |
| `src/representation` | 33 | 612.77 | 48.8% | 4.67% |
| `src/surface` | 8 | 551.96 | 56.14% | 2.88% |
| `examples/scripts/representation` | 24 | 428.62 | 20.03% | 0.0% |
| `src/structure` | 8 | 420.46 | 43.87% | 13.14% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/deploy.sh` -> **100.0%** Exposure
- `scripts/gallery.sh` -> **100.0%** Exposure
- `scripts/release.sh` -> **100.0%** Exposure
- `src/animation/animation.ts` -> **100.0%** Exposure
- `src/color/uniform-colormaker.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `examples/scripts/component/shape-buffer.js` -> **100.0%** Exposure
- `examples/scripts/component/shape-cat.js` -> **100.0%** Exposure
- `examples/scripts/component/shape-wireframe.js` -> **100.0%** Exposure
- `scripts/js/lib/queue.js` -> **100.0%** Exposure
- `scripts/js/lib/utils.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/utils/picker.ts` -> **0** Orphaned Functions | **56** Duplicates
- `examples/scripts/interactive/ligand-viewer.js` -> **0** Orphaned Functions | **45** Duplicates
- `examples/scripts/interactive/compvis-viewer.js` -> **0** Orphaned Functions | **42** Duplicates
- `examples/js/ui/ui.js` -> **0** Orphaned Functions | **33** Duplicates
- `src/proxy/atom-proxy.ts` -> **0** Orphaned Functions | **24** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/parser/cif-parser.ts`** -> AI Confidence: **99.48%**
2. **`src/parser/pdb-parser.ts`** -> AI Confidence: **99.48%**
3. **`src/chemistry/interactions/metal-binding.ts`** -> AI Confidence: **99.39%**
4. **`src/parser/mmtf-parser.ts`** -> AI Confidence: **99.39%**
5. **`src/structure/validation.ts`** -> AI Confidence: **99.39%**
6. **`src/buffer/geometry-buffer.ts`** -> AI Confidence: **99.34%**
7. **`src/parser/kin-parser.ts`** -> AI Confidence: **99.32%**
8. **`src/parser/mol2-parser.ts`** -> AI Confidence: **99.32%**
9. **`src/parser/prmtop-parser.ts`** -> AI Confidence: **99.32%**
10. **`src/parser/psf-parser.ts`** -> AI Confidence: **99.32%**
11. **`src/parser/sdf-parser.ts`** -> AI Confidence: **99.32%**
12. **`src/symmetry/symmetry-utils.ts`** -> AI Confidence: **99.32%**
13. **`src/buffer/buffer.ts`** -> AI Confidence: **99.31%**
14. **`src/buffer/text-buffer.ts`** -> AI Confidence: **99.31%**
15. **`src/chemistry/interactions/charged.ts`** -> AI Confidence: **99.31%**
16. **`src/chemistry/interactions/hydrogen-bonds.ts`** -> AI Confidence: **99.31%**
17. **`src/controls/animation-controls.ts`** -> AI Confidence: **99.31%**
18. **`src/geometry/helixbundle.ts`** -> AI Confidence: **99.31%**
19. **`src/proxy/chain-proxy.ts`** -> AI Confidence: **99.31%**
20. **`src/representation/angle-representation.ts`** -> AI Confidence: **99.31%**
21. **`src/representation/ballandstick-representation.ts`** -> AI Confidence: **99.31%**
22. **`src/representation/dihedral-representation.ts`** -> AI Confidence: **99.31%**
23. **`src/representation/dot-representation.ts`** -> AI Confidence: **99.31%**
24. **`src/representation/label-representation.ts`** -> AI Confidence: **99.31%**
25. **`src/representation/line-representation.ts`** -> AI Confidence: **99.31%**
26. **`src/representation/molecularsurface-representation.ts`** -> AI Confidence: **99.31%**
27. **`src/representation/structure-representation.ts`** -> AI Confidence: **99.31%**
28. **`src/representation/surface-representation.ts`** -> AI Confidence: **99.31%**
29. **`src/stage/stage.ts`** -> AI Confidence: **99.31%**
30. **`src/store/residue-type.ts`** -> AI Confidence: **99.31%**
31. **`src/structure/structure-utils.ts`** -> AI Confidence: **99.31%**
32. **`src/structure/structure.ts`** -> AI Confidence: **99.31%**
33. **`src/surface/surface.ts`** -> AI Confidence: **99.31%**
34. **`src/surface/volume.ts`** -> AI Confidence: **99.31%**
35. **`src/trajectory/trajectory-utils.ts`** -> AI Confidence: **99.31%**
36. **`src/trajectory/trajectory.ts`** -> AI Confidence: **99.31%**
37. **`src/viewer/viewer.ts`** -> AI Confidence: **99.31%**
38. **`examples/scripts/representation/contact.js`** -> AI Confidence: **99.29%**
39. **`src/align/alignment.ts`** -> AI Confidence: **99.29%**
40. **`src/selection/selection-parser.ts`** -> AI Confidence: **99.29%**
41. **`src/structure/structure-builder.ts`** -> AI Confidence: **99.29%**
42. **`src/symmetry/symmetry-constants.ts`** -> AI Confidence: **99.29%**
43. **`src/utils/edt.ts`** -> AI Confidence: **99.29%**
44. **`src/chemistry/interactions/contact.ts`** -> AI Confidence: **99.24%**
45. **`src/controls/picking-proxy.ts`** -> AI Confidence: **99.24%**
46. **`src/geometry/spline.ts`** -> AI Confidence: **99.24%**
47. **`src/representation/distance-representation.ts`** -> AI Confidence: **99.24%**
48. **`src/representation/measurement-representation.ts`** -> AI Confidence: **99.24%**
49. **`src/representation/representation-utils.ts`** -> AI Confidence: **99.24%**
50. **`src/chemistry/interactions/halogen-bonds.ts`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `examples/js/gui.js` -> **100.0%** Exposure
- `examples/js/ui/ui.extra.js` -> **100.0%** Exposure
- `examples/scripts/interactive/compvis-viewer.js` -> **100.0%** Exposure
- `scripts/js/node/download.js` -> **100.0%** Exposure
- `scripts/js/slimer/gallery.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `examples/js/gui.js` -> **100.0%** Exposure
- `examples/js/ui/ui.extra.js` -> **100.0%** Exposure
- `rollup.config.js` -> **100.0%** Exposure
- `scripts/js/lib/queue.js` -> **100.0%** Exposure
- `scripts/js/lib/utils.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `171` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/animation/animation.ts` (TYPESCRIPT) -> Cumulative Risk: **859.94**
- **Archetype:** `file_cluster_4` (Distance: 13.711 IQR)
- **Magnitude:** 42.7 | **LOC:** 359 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `then` (Impact: 25.1), `then` (Impact: 12.6), `tick` (Impact: 10.9)

### 2. `src/trajectory/trajectory-player.ts` (TYPESCRIPT) -> Cumulative Risk: **814.32**
- **Archetype:** `file_cluster_13` (Distance: 13.71 IQR)
- **Magnitude:** 47.37 | **LOC:** 273 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_animate` (Impact: 106.0), `_next` (Impact: 71.8), `play` (Impact: 22.1)

### 3. `scripts/js/node/download.js` (JAVASCRIPT) -> Cumulative Risk: **806.17**
- **Archetype:** `file_cluster_4` (Distance: 11.959 IQR)
- **Magnitude:** 120.06 | **LOC:** 111 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `getUrl` (Impact: 27.6), `downloadIds` (Impact: 25.4), `download` (Impact: 5.5)

### 4. `src/surface/volume.ts` (TYPESCRIPT) -> Cumulative Risk: **796.25**
- **Archetype:** `file_cluster_13` (Distance: 13.55 IQR)
- **Magnitude:** 70.6 | **LOC:** 530 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getSurfaceWorker` (Impact: 81.8), `getDataSize` (Impact: 43.7), `position` (Impact: 41.2)

### 5. `src/parser/cif-parser.ts` (TYPESCRIPT) -> Cumulative Risk: **775.63**
- **Archetype:** `file_cluster_8` (Distance: 12.441 IQR)
- **Magnitude:** 133.68 | **LOC:** 1149 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Safety Score (96.3813%)
- **Heaviest Functions:** `_parse` (Impact: 869.6), `getMatrixDict` (Impact: 91.3), `parseCore` (Impact: 54.5)

### 6. `src/buffer/mapped-buffer.ts` (TYPESCRIPT) -> Cumulative Risk: **769.91**
- **Archetype:** `file_cluster_13` (Distance: 12.469 IQR)
- **Magnitude:** 16.17 | **LOC:** 138 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setAttributes` (Impact: 49.8), `addAttributes` (Impact: 12.6), `makeIndex` (Impact: 8.7)

### 7. `src/stage/mouse-observer.ts` (TYPESCRIPT) -> Cumulative Risk: **757.27**
- **Archetype:** `file_cluster_13` (Distance: 13.818 IQR)
- **Magnitude:** 70.36 | **LOC:** 498 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getMouseButtons` (Impact: 58.3), `_onTouchmove` (Impact: 54.9), `_listen` (Impact: 47.7)

### 8. `src/parser/obj-parser.ts` (TYPESCRIPT) -> Cumulative Risk: **754.1**
- **Archetype:** `file_cluster_8` (Distance: 13.493 IQR)
- **Magnitude:** 65.97 | **LOC:** 380 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `parse` (Impact: 216.2), `OBJLoader` (Impact: 95.2), `_createParserState` (Impact: 72.3)

### 9. `src/proxy/chain-proxy.ts` (TYPESCRIPT) -> Cumulative Risk: **752.47**
- **Archetype:** `file_cluster_13` (Distance: 13.337 IQR)
- **Magnitude:** 37.88 | **LOC:** 309 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `eachPolymer` (Impact: 97.1), `eachResidue` (Impact: 50.6), `eachResidueN` (Impact: 13.9)

### 10. `src/surface/filtered-volume.ts` (TYPESCRIPT) -> Cumulative Risk: **744.63**
- **Archetype:** `file_cluster_12` (Distance: 13.304 IQR)
- **Magnitude:** 25.06 | **LOC:** 131 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setFilter` (Impact: 95.5), `constructor` (Impact: 9.1), `header` (Impact: 4.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `examples/js/gui.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.443 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.966 IQR)
- **Top Global Matches:** file_cluster_8: 12.443, file_cluster_4: 12.693, file_cluster_17: 12.751
- **Magnitude:** 1424.38 | **LOC:** 2397 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (61.4588%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SidebarWidget` (Impact: 122.6 | O(2^N) | DB: 29)
  * `DirectoryListingWidget` (Impact: 79.1 | O(N^4) | DB: 40)
  * `createParameterInput` (Impact: 75.0 | O(2^N) | DB: 2)
  * `TrajectoryElementWidget` (Impact: 51.9 | O(N^2) | DB: 36)
  * `StageWidget` (Impact: 46.9 | O(N^2) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 286`, `args: 203`, `func_start: 135`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 611`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 27`, `api: 4`, `concurrency: 63`
* *Defense:* `safety: 54`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/js/ui/ui.extra.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.399 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.864 IQR)
- **Top Global Matches:** file_cluster_11: 13.399, file_cluster_8: 13.438, file_cluster_12: 13.53
- **Magnitude:** 1037.02 | **LOC:** 1137 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (98.5961%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `VirtualTable` (Impact: 135.5 | O(N^3) | DB: 38)
  * `VirtualList` (Impact: 108.5 | O(2^N) | DB: 29)
  * `ColorPicker` (Impact: 30.5 | O(2^N) | DB: 23)
    * *Intent:* // Color picker (requires FlexiColorPicker) // https://github.com/DavidDurman/FlexiColorPicker
  * `setCollapsed` (Impact: 25.3 | O(2^N) | DB: 13)
  * `PopupMenu` (Impact: 23.8 | O(N^2) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 145`, `args: 94`, `func_start: 89`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 483`, `dead_code: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 17`, `concurrency: 7`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/js/ui/ui.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.032 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.543 IQR)
- **Top Global Matches:** file_cluster_8: 13.032, file_cluster_11: 13.047, file_cluster_12: 13.12
- **Magnitude:** 813.0 | **LOC:** 1038 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (98.4798%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `FancySelect` (Impact: 64.9 | O(2^N) | DB: 7)
  * `Number` (Impact: 29.3 | O(2^N) | DB: 23)
  * `setValue` (Impact: 19.6 | O(N^2) | DB: 15)
  * `Integer` (Impact: 15.4 | O(N^1) | DB: 22)
  * `Color` (Impact: 11.5 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 158`, `args: 102`, `func_start: 87`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 420`, `planned_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 21`
* *Defense:* `safety: 14`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/interactive/compvis-viewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.353 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.958 IQR)
- **Top Global Matches:** file_cluster_8: 11.353, file_cluster_17: 11.92, file_cluster_7: 11.943
- **Magnitude:** 432.48 | **LOC:** 733 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (71.2843%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadStructure` (Impact: 76.8 | O(N^3) | DB: 10)
  * `addElement` (Impact: 22.5 | O(N^1) | DB: 3)
  * `setLigandOptions` (Impact: 16.9 | O(N^1) | DB: 5)
  * `setResidueOptions` (Impact: 12.9 | O(N^1) | DB: 5)
  * `setChainOptions` (Impact: 6.7 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 93`, `args: 51`, `func_start: 97`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 166`, `duplicate_logic: 42`
* *Architecture:* `concurrency: 3`
* *Defense:* `safety: 14`, `doc: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/surface/edt-surface.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.766 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.771 IQR)
- **Top Global Matches:** file_cluster_8: 12.766, file_cluster_13: 12.898, file_cluster_11: 12.952
- **Magnitude:** 314.58 | **LOC:** 817 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (75.2351%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `EDTSurface` (Impact: 2872.4 | O(2^N) | DB: 113)
  * `getVolume` (Impact: 2.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 130`, `args: 26`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 257`, `dead_code: 6`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.832
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.109604
  * `Imports (Out-Degree: 3):` volume, types, vector-utils, surface-utils, grid
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/scripts/interactive/ligand-viewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.884 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.684 IQR)
- **Top Global Matches:** file_cluster_8: 10.884, file_cluster_7: 11.54, file_cluster_17: 11.596
- **Magnitude:** 288.8 | **LOC:** 628 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (61.258%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setLigandOptions` (Impact: 16.9 | O(N^1) | DB: 5)
  * `setResidueOptions` (Impact: 12.9 | O(N^1) | DB: 5)
  * `setChainOptions` (Impact: 6.7 | O(N^1) | DB: 4)
  * `showLigand` (Impact: 5.9 | O(N^1) | DB: 7)
  * `addElement` (Impact: 5.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 68`, `args: 46`, `func_start: 91`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 125`, `duplicate_logic: 45`
* *Architecture:* `concurrency: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/interactive/xray-viewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.103 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.751 IQR)
- **Top Global Matches:** file_cluster_8: 11.103, file_cluster_4: 11.724, file_cluster_7: 11.794
- **Magnitude:** 265.22 | **LOC:** 456 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (57.2696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addElement` (Impact: 23.1 | O(N^2) | DB: 3)
  * `onkeypress` (Impact: 21.7 | O(N^2) | DB: 2)
  * `loadExample` (Impact: 13.2 | O(N^1) | DB: 1)
  * `isolevelScroll` (Impact: 12.8 | O(N^1) | DB: 2)
  * `addElement` (Impact: 11.4 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 51`, `args: 32`, `func_start: 64`
* *Risk/State:* `state_mutation: 78`, `duplicate_logic: 19`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `concurrency: 11`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/js/ui/ui.ngl.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.313 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.463 IQR)
- **Top Global Matches:** file_cluster_8: 12.313, file_cluster_11: 12.442, file_cluster_12: 12.488
- **Magnitude:** 225.8 | **LOC:** 369 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (96.2637%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onEnter` (Impact: 36.3 | O(N^2) | DB: 8)
  * `SelectionInput` (Impact: 8.3 | O(2^N) | DB: 7)
  * `setValue` (Impact: 7.4 | O(2^N) | DB: 3)
  * `ComponentPanel` (Impact: 4.9 | O(N^1) | DB: 12)
  * `ColorPopupMenu` (Impact: 4.2 | O(N^1) | DB: 16)
    * *Intent:* /** * @file UI NGL * @author Alexander Rose <alexander.rose@weirdbyte.de> */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 41`, `args: 35`, `func_start: 20`
* *Risk/State:* `state_mutation: 120`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 2`
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/structure/structure-utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.198 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.673 IQR)
- **Top Global Matches:** file_cluster_8: 12.198, file_cluster_13: 12.416, file_cluster_11: 12.452
- **Magnitude:** 168.07 | **LOC:** 1112 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (58.9841%), Tech Debt (10.4645%)
**Top Internal Functions/Classes:**
  * `assignSecondaryStructure` (Impact: 320.0 | O(2^N) | DB: 17)
  * `calculateBondsBetween` (Impact: 223.9 | O(2^N) | DB: 4)
  * `calculateChainnames` (Impact: 158.6 | O(2^N) | DB: 11)
  * `calculateBondsWithin` (Impact: 124.0 | O(2^N) | DB: 7)
  * `reorderAtoms` (Impact: 102.3 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 98`, `args: 96`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 276`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `api: 18`, `import: 12`
* *Defense:* `doc: 6`, `immutability_locks: 147`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.803
  * `Choke Point (Betweenness):` 0.005065 | `Ripple Effect (Closeness):` 0.165195
  * `Imports (Out-Degree: 8):` structure-builder, polymer, utils, three, kdtree, residue-proxy, helixbundle, globals...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/parser/pdb-parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.412 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.585 IQR)
- **Top Global Matches:** file_cluster_8: 11.412, file_cluster_13: 11.615, file_cluster_7: 11.825
- **Magnitude:** 157.35 | **LOC:** 741 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (51.7397%), Tech Debt (8.2276%)
**Top Internal Functions/Classes:**
  * `_parse` (Impact: 1390.3 | O(2^N) | DB: 64)
    * *Intent:* /** * Create a pdb parser * @param {Streamer} streamer - streamer object * @param {Object} params - ...
  * `getModresId` (Impact: 10.3 | O(N^1) | DB: 1)
  * `constructor` (Impact: 5.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 29`, `args: 17`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 152`, `planned_debt: 1`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `doc: 7`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.299
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005587
  * `Imports (Out-Degree: 9):` structure-utils, structure-parser, unitcell, utils, three, streamer, types, structure-constants...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/parser/cif-parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.441 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.365 IQR)
- **Top Global Matches:** file_cluster_8: 12.441, file_cluster_13: 12.6, file_cluster_17: 12.725
- **Magnitude:** 133.68 | **LOC:** 1149 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (81.3172%), Tech Debt (17.1784%)
**Top Internal Functions/Classes:**
  * `_parse` (Impact: 869.6 | O(2^N) | DB: 31)
    * *Intent:* //
  * `getMatrixDict` (Impact: 91.3 | O(2^N) | DB: 9)
  * `parseCore` (Impact: 54.5 | O(N^2) | DB: 12)
  * `parseChemComp` (Impact: 46.6 | O(N^2) | DB: 6)
  * `getBondOrder` (Impact: 18.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 56`, `args: 35`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 133`, `state_mutation: 217`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 59`, `doc: 1`, `immutability_locks: 240`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` structure-builder, structure-utils, structure-parser, unitcell, three, chemcomp-map, utils, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/js/node/download.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.959 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.569 IQR)
- **Top Global Matches:** file_cluster_4: 11.959, file_cluster_13: 12.122, file_cluster_8: 12.324
- **Magnitude:** 120.06 | **LOC:** 111 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (92.3423%), Tech Debt (95.7395%)
**Top Internal Functions/Classes:**
  * `getUrl` (Impact: 27.6 | O(N^2) | DB: 12)
  * `downloadIds` (Impact: 25.4 | O(N^3) | DB: 20)
  * `download` (Impact: 5.5 | O(N^4) | DB: 2)
  * `downloadIdsChunked` (Impact: 2.9 | O(N^2) | DB: 2)
  * `parseIdListFile` (Impact: 2.4 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 8`, `func_start: 9`
* *Risk/State:* `state_mutation: 38`, `duplicate_logic: 2`
* *Architecture:* `io: 18`, `concurrency: 14`, `import: 7`
* *Defense:* `safety: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` performance-now, zlib, argparse, http, download, utils.js, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/grid.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.939 IQR)
- **Top Global Matches:** file_cluster_4: 10.939, file_cluster_8: 10.964, file_cluster_17: 11.3
- **Magnitude:** 110.46 | **LOC:** 150 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (87.0464%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `appendImage` (Impact: 19.4 | O(N^2) | DB: 6)
  * `makeImage` (Impact: 6.3 | O(2^N))
  * `sample` (Impact: 5.7 | O(N^2) | DB: 4)
  * `loadList` (Impact: 4.8 | O(N^3) | DB: 1)
  * `loadArchive` (Impact: 4.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 36`, `args: 19`, `func_start: 16`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 13`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ngl.dev.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/structure/structure.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.553 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.382 IQR)
- **Top Global Matches:** file_cluster_13: 13.553, file_cluster_11: 13.759, file_cluster_8: 13.948
- **Magnitude:** 109.7 | **LOC:** 1125 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (38.036%), Tech Debt (17.4602%)
**Top Internal Functions/Classes:**
  * `getBondData` (Impact: 100.7 | O(N^3) | DB: 14)
  * `eachResidue` (Impact: 99.7 | O(2^N) | DB: 7)
  * `getAtomSet` (Impact: 65.5 | O(N^3) | DB: 6)
  * `getAtomData` (Impact: 56.8 | O(N^2) | DB: 6)
  * `eachModel` (Impact: 50.5 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 89`, `args: 55`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 375`, `planned_debt: 11`
* *Architecture:* `io: 6`, `api: 20`, `import: 37`
* *Defense:* `safety: 8`, `doc: 58`, `immutability_locks: 71`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.984
  * `Choke Point (Betweenness):` 0.036371 | `Ripple Effect (Closeness):` 0.214599
  * `Imports (Out-Degree: 29):` unitcell, bond-proxy, volume, assembly, bitarray, atom-store, residue-store, principal-axes...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `src/geometry/spline.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.843 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.036 IQR)
- **Top Global Matches:** file_cluster_13: 13.843, file_cluster_2: 13.97, file_cluster_11: 14.008
- **Magnitude:** 106.64 | **LOC:** 667 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 89
- **Risk Profile:** Cognitive Load (68.0647%), Tech Debt (9.6901%)
**Top Internal Functions/Classes:**
  * `reset` (Impact: 153.0 | O(2^N) | DB: 89)
  * `getNormalDir` (Impact: 63.2 | O(N^2) | DB: 24)
  * `interpolateNormalDir` (Impact: 40.2 | O(N^6) | DB: 23)
  * `vectorSubdivide` (Impact: 38.4 | O(N^6) | DB: 8)
  * `interpolateTangent` (Impact: 11.4 | O(N^1) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 102`, `args: 38`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 653`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 10`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.112652
  * `Imports (Out-Degree: 9):` polymer, three, radius-factory, array-utils, colormaker, types, globals, math-utils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/buffer/buffer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.156 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.887 IQR)
- **Top Global Matches:** file_cluster_8: 13.156, file_cluster_13: 13.243, file_cluster_11: 13.349
- **Magnitude:** 105.37 | **LOC:** 878 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (64.559%), Tech Debt (36.8039%)
**Top Internal Functions/Classes:**
  * `setParameters` (Impact: 66.0 | O(N^2) | DB: 13)
  * `setAttributes` (Impact: 62.3 | O(N^3) | DB: 8)
  * `makeWireframeIndex` (Impact: 59.4 | O(N^2) | DB: 25)
  * `setUniforms` (Impact: 59.1 | O(N^2) | DB: 9)
  * `getDefines` (Impact: 37.6 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 71`, `args: 42`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 516`, `planned_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `import: 7`
* *Defense:* `safety: 3`, `doc: 20`, `immutability_locks: 55`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.283
  * `Choke Point (Betweenness):` 0.014956 | `Ripple Effect (Closeness):` 0.152911
  * `Imports (Out-Degree: 5):` utils, three, shader-utils, array-utils, types, globals, picker
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `scripts/js/node/timeParsing.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.862 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.748 IQR)
- **Top Global Matches:** file_cluster_4: 11.862, file_cluster_13: 12.032, file_cluster_17: 12.116
- **Magnitude:** 104.76 | **LOC:** 109 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (88.8476%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFileObject` (Impact: 24.7 | O(N^2) | DB: 12)
  * `parseFiles` (Impact: 9.6 | O(N^3) | DB: 1)
  * `getDirFiles` (Impact: 9.4 | O(N^3) | DB: 6)
  * `isBinary` (Impact: 7.0 | O(N^2) | DB: 3)
  * `parseFilesChunked` (Impact: 3.8 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 29`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `io: 17`, `concurrency: 14`, `import: 8`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` performance-now, zlib, ngl.dev.js, argparse, file-api, path, utils.js, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/store/residue-type.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.252 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.68 IQR)
- **Top Global Matches:** file_cluster_8: 13.252, file_cluster_13: 13.354, file_cluster_11: 13.411
- **Magnitude:** 99.09 | **LOC:** 752 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (64.6327%), Tech Debt (15.7951%)
**Top Internal Functions/Classes:**
  * `assignBondReferenceAtomIndices` (Impact: 79.3 | O(N^3) | DB: 9)
  * `addRing` (Impact: 45.2 | O(N^1) | DB: 14)
  * `getBackboneIndexList` (Impact: 27.2 | O(N^2) | DB: 7)
  * `getBackboneType` (Impact: 26.9 | O(N^1) | DB: 6)
  * `findRings` (Impact: 25.0 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 88`, `args: 60`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 468`, `planned_debt: 10`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `doc: 15`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.06
  * `Choke Point (Betweenness):` 0.000143 | `Ripple Effect (Closeness):` 0.146723
  * `Imports (Out-Degree: 6):` structure-utils, principal-axes, utils, residue-proxy, structure-constants, atom-proxy, matrix-utils, structure
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scripts/js/slimer/gallery.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.62 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.21 IQR)
- **Top Global Matches:** file_cluster_8: 10.62, file_cluster_17: 10.723, file_cluster_4: 10.901
- **Magnitude:** 95.62 | **LOC:** 203 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (33.5856%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderExample` (Impact: 57.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 19`, `args: 23`, `func_start: 12`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `io: 18`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 4`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` webpage, system, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/interactive/crosslinking.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.269 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.803 IQR)
- **Top Global Matches:** file_cluster_8: 8.269, file_cluster_7: 9.17, file_cluster_1: 9.39
- **Magnitude:** 95.08 | **LOC:** 885 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (8.5671%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initColourSchemes` (Impact: 18.8 | O(N^3) | DB: 9)
    * *Intent:* // make a colour scheme that grabs the score of each link and uses it to return a colour
  * `makeAtomSelection` (Impact: 2.2 | O(N^1) | DB: 4)
    * *Intent:* // return unique atom indices as a selection from a set of pairs of atom indices
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 35`, `args: 14`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 51`, `dead_code: 1`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/selection/selection-parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.619 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.967 IQR)
- **Top Global Matches:** file_cluster_8: 10.619, file_cluster_7: 11.18, file_cluster_13: 11.32
- **Magnitude:** 91.7 | **LOC:** 487 | **CtrlFlow:** 93.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (36.3803%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseSele` (Impact: 841.8 | O(N^5) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 9`, `args: 43`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 66`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001862
  * `Imports (Out-Degree: 2):` selection-test, selection-constants
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/scripts/test/nci.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.145 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.226 IQR)
- **Top Global Matches:** file_cluster_8: 9.145, file_cluster_7: 9.984, file_cluster_1: 10.212
- **Magnitude:** 91.62 | **LOC:** 474 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.2236%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createElement` (Impact: 4.3 | O(2^N) | DB: 1)
  * `addElement` (Impact: 4.2 | O(N^1) | DB: 1)
  * `addElement` (Impact: 4.2 | O(N^1) | DB: 2)
  * `onchange` (Impact: 3.8 | O(N^1))
  * `loadExample` (Impact: 3.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 23`, `args: 17`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 39`, `duplicate_logic: 6`
* *Architecture:* `concurrency: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proxy/atom-proxy.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.165 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.525 IQR)
- **Top Global Matches:** file_cluster_13: 14.165, file_cluster_8: 14.41, file_cluster_11: 14.451
- **Magnitude:** 89.41 | **LOC:** 813 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (44.2686%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getResidueBonds` (Impact: 28.6 | O(N^2) | DB: 8)
  * `isPolymer` (Impact: 26.6 | O(2^N) | DB: 3)
  * `connectedTo` (Impact: 25.5 | O(N^1) | DB: 4)
  * `qualifiedName` (Impact: 20.7 | O(N^1) | DB: 15)
  * `aromatic` (Impact: 16.4 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 116`, `args: 107`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 390`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 24`
* *Architecture:* `api: 32`, `import: 15`
* *Defense:* `safety: 2`, `doc: 117`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.737
  * `Choke Point (Betweenness):` 0.008451 | `Ripple Effect (Closeness):` 0.200543
  * `Imports (Out-Degree: 13):` chain-store, residue-store, atom-type, three, bond-proxy, residue-proxy, types, structure-constants...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `scripts/symop_lib.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.023 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.429 IQR)
- **Top Global Matches:** file_cluster_8: 9.023, file_cluster_13: 9.103, file_cluster_7: 9.752
- **Magnitude:** 83.46 | **LOC:** 71 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (30.2941%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 75.5 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 9`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` shlex, collections, json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/viewer/viewer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.202 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_13: 13.202, file_cluster_8: 13.229, file_cluster_4: 13.407
- **Magnitude:** 83.4 | **LOC:** 1410 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (63.6827%), Tech Debt (10.6315%)
**Top Internal Functions/Classes:**
  * `onBeforeRender` (Impact: 75.2 | O(N^2) | DB: 13)
  * `constructor` (Impact: 44.5 | O(N^2) | DB: 26)
  * `setCamera` (Impact: 40.5 | O(N^2) | DB: 22)
    * *Intent:* // console.log(gl.getContextAttributes().antialias)
  * `pick` (Impact: 26.7 | O(N^2) | DB: 7)
  * `animate` (Impact: 21.6 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 40`, `args: 23`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `state_mutation: 484`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 12`, `import: 11`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 37`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.254
  * `Choke Point (Betweenness):` 0.005078 | `Ripple Effect (Closeness):` 0.17986
  * `Imports (Out-Degree: 9):` stats, signals, three, gl-utils, shader-utils, colormaker, globals, viewer-utils...
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/color/uniform-colormaker.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, state_mutation: 7, args: 4
- `examples/mobile.html` (HTML) | Magnitude: 17.32 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 9, args: 7, state_mutation: 7
- `src/structure/data.ts` (TYPESCRIPT) | Magnitude: 2.45 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 13, decorators: 10, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/controls/mouse-controls.ts` (TYPESCRIPT) | Magnitude: 15.44 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 51, branch: 38, structural_boundaries: 37
- `examples/js/ui/ui.extra.js` (JAVASCRIPT) | Magnitude: 1037.02 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 663, state_mutation: 483, structural_boundaries: 145, reflection_metaprogramming: 103
- `src/parser/ply-parser.ts` (TYPESCRIPT) | Magnitude: 31.83 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 297, structural_boundaries: 89, branch: 79, state_mutation: 73
- `src/utils.ts` (TYPESCRIPT) | Magnitude: 65.52 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 368, structural_boundaries: 151, branch: 140, state_mutation: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/surface/filtered-volume.ts` (TYPESCRIPT) | Magnitude: 25.06 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 100, indent_spaces: 82, branch: 26, reflection_metaprogramming: 21
- `scripts/gallery.sh` (SHELL) | Magnitude: 1.56 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, branch: 3, structural_boundaries: 3, reflection_metaprogramming: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/buffer/doublesided-buffer.ts` (TYPESCRIPT) | Magnitude: 25.03 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 143, state_mutation: 130, branch: 19, args: 16
- `src/buffer/tubemesh-buffer.ts` (TYPESCRIPT) | Magnitude: 15.86 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 247, state_mutation: 107, immutability_locks: 45, branch: 41
- `src/store/model-store.ts` (TYPESCRIPT) | Magnitude: 0.45 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 2, doc: 2
- `src/representation/measurement-representation.ts` (TYPESCRIPT) | Magnitude: 21.28 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 299, state_mutation: 99, structural_boundaries: 47, branch: 38
- `src/geometry/primitive.ts` (TYPESCRIPT) | Magnitude: 20.36 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, structural_boundaries: 93, state_mutation: 80, args: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/component/component-collection.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 5, args: 4, func_start: 2
- `src/parser/parser-registry.ts` (TYPESCRIPT) | Magnitude: 7.71 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, state_mutation: 24, structural_boundaries: 20, args: 18
- `src/component/representation-collection.ts` (TYPESCRIPT) | Magnitude: 4.99 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 20, args: 14, state_mutation: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/scripts/color/bond-data.js` (JAVASCRIPT) | Magnitude: 24.24 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, concurrency: 6, structural_boundaries: 3, state_mutation: 3
- `examples/grid.html` (HTML) | Magnitude: 110.46 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 39, structural_boundaries: 36, args: 19
- `src/streamer/streamer.ts` (TYPESCRIPT) | Magnitude: 29.81 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 168, indent_spaces: 144, branch: 36, structural_boundaries: 26
- `src/worker/worker-utils.ts` (TYPESCRIPT) | Magnitude: 5.74 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 11, branch: 10, args: 7
- `examples/scripts/selection/spatialHash.js` (JAVASCRIPT) | Magnitude: 23.86 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 15, structural_boundaries: 9, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/parser/gro-parser.ts` (TYPESCRIPT) | Magnitude: 23.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, state_mutation: 90, structural_boundaries: 40, branch: 20
- `examples/scripts/test/alignment2.js` (JAVASCRIPT) | Magnitude: 31.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 15, concurrency: 14, structural_boundaries: 4, args: 3
- `src/symmetry/unitcell.ts` (TYPESCRIPT) | Magnitude: 9.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 146, state_mutation: 54, immutability_locks: 28, args: 26
- `examples/js/ui/ui.js` (JAVASCRIPT) | Magnitude: 813.0 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 553, state_mutation: 420, structural_boundaries: 158, args: 102
- `examples/scripts/test/superposition.js` (JAVASCRIPT) | Magnitude: 30.32 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: concurrency: 14, indent_spaces: 13, structural_boundaries: 3, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/utils/kdtree.ts` (TYPESCRIPT) | Magnitude: 28.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 159, state_mutation: 99, branch: 32, immutability_locks: 32
- `src/constants.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, immutability_locks: 3, doc: 1
- `src/chemistry/interactions/metal-binding.ts` (TYPESCRIPT) | Magnitude: 12.38 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 104, branch: 49, dead_code: 25, structural_boundaries: 18
- `src/geometry/grid.ts` (TYPESCRIPT) | Magnitude: 3.17 | Delta: **0.132 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 34, args: 12, state_mutation: 12, structural_boundaries: 11

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/representation/measurement-representation.ts` -> **Severity: 5.131** (Bridge: 0.0513 * Flux: 99.9883%)
- `src/structure/structure.ts` -> **Severity: 3.637** (Bridge: 0.0364 * Flux: 100.0%)
- `src/utils/picker.ts` -> **Severity: 2.827** (Bridge: 0.0283 * Flux: 100.0%)
- `src/stage/stage.ts` -> **Severity: 2.297** (Bridge: 0.023 * Flux: 99.9992%)
- `src/globals.ts` -> **Severity: 1.83** (Bridge: 0.0607 * Flux: 30.1207%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/globals.ts` -> **Severity: 24.676** (Embedded: 0.3288 * Error Risk: 75.0453%)
- `src/structure/structure.ts` -> **Severity: 20.899** (Embedded: 0.2146 * Error Risk: 97.3864%)
- `src/proxy/atom-proxy.ts` -> **Severity: 19.872** (Embedded: 0.2005 * Error Risk: 99.0903%)
- `src/worker/worker-registry.ts` -> **Severity: 18.091** (Embedded: 0.2006 * Error Risk: 90.2031%)
- `src/structure/structure-view.ts` -> **Severity: 17.936** (Embedded: 0.1794 * Error Risk: 99.9817%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/globals.ts` -> **Severity: 7790.092** (Blast Radius: 77.901 * Doc Risk: 99.9999%)
- `src/utils/registry.ts` -> **Severity: 2320.345** (Blast Radius: 25.738 * Doc Risk: 90.1525%)
- `src/types.ts` -> **Severity: 1450.663** (Blast Radius: 27.2 * Doc Risk: 53.3332%)
- `src/parser/parser-registry.ts` -> **Severity: 1279.729** (Blast Radius: 13.917 * Doc Risk: 91.9544%)
- `src/math/array-utils.ts` -> **Severity: 1275.042** (Blast Radius: 12.978 * Doc Risk: 98.2464%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
