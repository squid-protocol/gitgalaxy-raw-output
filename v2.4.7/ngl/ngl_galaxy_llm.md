# ARCHITECTURAL_BRIEF: ngl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/ngl` |
| **Timestamp** | `2026-08-07T04:27:01.811218+00:00` |
| **Scan Duration** | `2.34s` |
| **Git Branch** | `master` |
| **Git Commit** | `60be69b5fe0e9c43cb3a06fe1cb691fa9478c790` |
| **Git Remote** | `https://github.com/nglviewer/ngl.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 503 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.276`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 272 | 50.6% |
| file_cluster_13 | 204 | 37.9% |
| file_cluster_4 | 25 | 4.6% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 32.2 | 29.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 57.4 | 72.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.0 | 2.4 | 0.0 |
| API Exposure | 0.0 | 14.9 | 3.7 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 51.9 | 80.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.2 | 11.9 | 0.0 |
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

- `EDTSurface` (@ `src/surface/edt-surface.ts`) -> Impact: **444.0** | LOC: 786
- `_parse` (@ `src/parser/pdb-parser.ts`) -> Impact: **302.5** | LOC: 612
  * *Intent:* /** * Create a pdb parser * @param {Streamer} streamer - streamer object * @param {Object} params - params object * @param {Boolean} params.hex - hexa...
- `_parseChunkOfLines` (@ `src/parser/pdb-parser.ts`) -> Impact: **297.2** | LOC: 425
- `parseSele` (@ `src/selection/selection-parser.ts`) -> Impact: **296.2** | LOC: 468
- `_parse` (@ `src/parser/cif-parser.ts`) -> Impact: **227.7** | LOC: 273
  * *Intent:* //
- `calculateBonds` (@ `src/parser/cif-parser.ts`) -> Impact: **146.7** | LOC: 219
  * *Intent:* // IUCr core CIF schema
- `_parseChunkOfLines` (@ `src/parser/sdf-parser.ts`) -> Impact: **146.1** | LOC: 162
- `atomTestFn` (@ `src/selection/selection-test.ts`) -> Impact: **140.0** | LOC: 63
- `JacobiSVDImpl` (@ `src/math/matrix-utils.ts`) -> Impact: **136.4** | LOC: 209
- `_parse` (@ `src/parser/sdf-parser.ts`) -> Impact: **133.9** | LOC: 219

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `examples/js/ui` | 3 | 1910.12 | 97.74% | 0.0% |
| `examples/js` | 1 | 1403.28 | 81.2% | 0.0% |
| `examples/scripts/interactive` | 9 | 1378.72 | 65.27% | 0.0% |
| `examples/scripts/test` | 27 | 721.22 | 20.78% | 0.0% |
| `examples/scripts/parser` | 40 | 689.1 | 19.09% | 0.0% |
| `src/parser` | 37 | 601.82 | 49.75% | 40.28% |
| `src/representation` | 33 | 534.07 | 52.55% | 16.88% |
| `examples/scripts/representation` | 24 | 428.62 | 20.03% | 0.0% |
| `src/shader` | 24 | 365.15 | 4.94% | 0.0% |
| `src/surface` | 8 | 331.59 | 66.16% | 49.34% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/deploy.sh` -> **100.0%** Exposure
- `scripts/gallery.sh` -> **100.0%** Exposure
- `scripts/release.sh` -> **100.0%** Exposure
- `src/animation/animation.ts` -> **100.0%** Exposure
- `src/color/atomindex-colormaker.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `examples/scripts/component/shape-buffer.js` -> **100.0%** Exposure
- `examples/scripts/component/shape-cat.js` -> **100.0%** Exposure
- `examples/scripts/component/shape-wireframe.js` -> **100.0%** Exposure
- `scripts/js/lib/queue.js` -> **100.0%** Exposure
- `scripts/js/lib/utils.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/scripts/interactive/compvis-viewer.js` -> **2** Orphaned Functions | **66** Duplicates
- `src/utils/picker.ts` -> **0** Orphaned Functions | **65** Duplicates
- `examples/scripts/interactive/ligand-viewer.js` -> **1** Orphaned Functions | **60** Duplicates
- `examples/scripts/interactive/xray-viewer.js` -> **1** Orphaned Functions | **46** Duplicates
- `examples/js/ui/ui.js` -> **0** Orphaned Functions | **45** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `171` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/animation/animation.ts` (TYPESCRIPT) -> Cumulative Risk: **645.84**
- **Archetype:** `file_cluster_4` (Distance: 13.711 IQR)
- **Magnitude:** 40.08 | **LOC:** 359 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9923%)
- **Heaviest Functions:** `tick` (Impact: 10.9), `_tick` (Impact: 10.9), `pause` (Impact: 8.4)

### 2. `src/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **636.29**
- **Archetype:** `file_cluster_11` (Distance: 11.428 IQR)
- **Magnitude:** 59.3 | **LOC:** 577 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9997%), State Flux (96.7949%), Documentation (96.4364%)
- **Heaviest Functions:** `deepEqual` (Impact: 42.0), `download` (Impact: 30.4), `getBrowser` (Impact: 29.1)

### 3. `src/math/array-utils.ts` (TYPESCRIPT) -> Cumulative Risk: **633.09**
- **Archetype:** `file_cluster_8` (Distance: 11.957 IQR)
- **Magnitude:** 56.95 | **LOC:** 530 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9882%), Tech Debt (99.9787%), Documentation (95.7347%)
- **Heaviest Functions:** `quicksortIP` (Impact: 75.9), `quicksortCmp` (Impact: 51.1), `quickselectCmp` (Impact: 32.0)

### 4. `src/surface/edt-surface.ts` (TYPESCRIPT) -> Cumulative Risk: **609.06**
- **Archetype:** `file_cluster_8` (Distance: 12.729 IQR)
- **Magnitude:** 119.3 | **LOC:** 817 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (92.6139%), Cognitive Load (92.1356%)
- **Heaviest Functions:** `EDTSurface` (Impact: 444.0), `fastoneshell` (Impact: 115.2), `fillatom` (Impact: 59.7)

### 5. `src/surface/volume-slice.ts` (TYPESCRIPT) -> Cumulative Risk: **599.86**
- **Archetype:** `file_cluster_13` (Distance: 12.423 IQR)
- **Magnitude:** 21.45 | **LOC:** 215 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.4836%), Tech Debt (96.7148%)
- **Heaviest Functions:** `getData` (Impact: 55.6), `getPositionFromCoordinate` (Impact: 10.9), `setVec` (Impact: 7.6)

### 6. `src/streamer/streamer.ts` (TYPESCRIPT) -> Cumulative Risk: **594.24**
- **Archetype:** `file_cluster_4` (Distance: 13.222 IQR)
- **Magnitude:** 27.42 | **LOC:** 205 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.791%), Verification (80.0%)
- **Heaviest Functions:** `chunkToLines` (Impact: 21.8), `read` (Impact: 14.7), `peekLines` (Impact: 12.9)

### 7. `src/streamer/network-streamer.ts` (TYPESCRIPT) -> Cumulative Risk: **592.36**
- **Archetype:** `file_cluster_4` (Distance: 14.086 IQR)
- **Magnitude:** 5.5 | **LOC:** 56 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9992%), State Flux (99.9962%), Concurrency (99.7527%)
- **Heaviest Functions:** `_read` (Impact: 24.7), `reject` (Impact: 3.5), `reject` (Impact: 3.1)

### 8. `src/parser/obj-parser.ts` (TYPESCRIPT) -> Cumulative Risk: **592.27**
- **Archetype:** `file_cluster_8` (Distance: 13.394 IQR)
- **Magnitude:** 59.61 | **LOC:** 380 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6886%), Tech Debt (93.0862%)
- **Heaviest Functions:** `parse` (Impact: 112.2), `OBJLoader` (Impact: 95.2), `addFace` (Impact: 40.8)

### 9. `scripts/js/node/download.js` (JAVASCRIPT) -> Cumulative Risk: **591.17**
- **Archetype:** `file_cluster_4` (Distance: 11.936 IQR)
- **Magnitude:** 97.16 | **LOC:** 111 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9729%), Concurrency (99.9301%)
- **Heaviest Functions:** `getUrl` (Impact: 18.6), `downloadIds` (Impact: 13.3), `download` (Impact: 2.5)

### 10. `src/surface/volume.ts` (TYPESCRIPT) -> Cumulative Risk: **582.72**
- **Archetype:** `file_cluster_13` (Distance: 13.55 IQR)
- **Magnitude:** 71.06 | **LOC:** 530 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4567%), Verification (80.0%)
- **Heaviest Functions:** `callback` (Impact: 121.0), `getDataSize` (Impact: 29.9), `setData` (Impact: 27.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `examples/js/gui.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.396 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.134 IQR)
- **Top Global Matches:** file_cluster_8: 12.396, file_cluster_17: 12.693, file_cluster_11: 12.701
- **Magnitude:** 1403.28 | **LOC:** 2397 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.1955%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SidebarWidget` (Impact: 46.4)
  * `TrajectoryElementWidget` (Impact: 39.7)
  * `createParameterInput` (Impact: 38.6)
  * `DirectoryListingWidget` (Impact: 35.0)
  * `StageWidget` (Impact: 33.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 286`, `args: 203`, `func_start: 135`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 605`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 29`
* *Architecture:* `io: 27`, `api: 5`, `concurrency: 38`
* *Defense:* `safety: 54`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/js/ui/ui.extra.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.394 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.015 IQR)
- **Top Global Matches:** file_cluster_11: 13.394, file_cluster_8: 13.446, file_cluster_12: 13.529
- **Magnitude:** 941.42 | **LOC:** 1137 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.5474%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `VirtualTable` (Impact: 71.8)
  * `VirtualList` (Impact: 41.4)
  * `generatorFn` (Impact: 21.8)
  * `PopupMenu` (Impact: 17.8)
  * `setCollapsed` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 145`, `args: 94`, `func_start: 89`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 483`, `dead_code: 1`, `duplicate_logic: 20`
* *Architecture:* `api: 23`, `concurrency: 7`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/js/ui/ui.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.034 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.563 IQR)
- **Top Global Matches:** file_cluster_8: 13.034, file_cluster_11: 13.047, file_cluster_12: 13.122
- **Magnitude:** 767.2 | **LOC:** 1038 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.4325%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `FancySelect` (Impact: 23.3)
  * `Number` (Impact: 17.2)
  * `Integer` (Impact: 15.4)
  * `setValue` (Impact: 13.6)
  * `onMouseMove` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 158`, `args: 102`, `func_start: 87`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 420`, `planned_debt: 1`, `duplicate_logic: 45`
* *Architecture:* `api: 21`
* *Defense:* `safety: 14`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/interactive/compvis-viewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.353 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.637 IQR)
- **Top Global Matches:** file_cluster_8: 11.353, file_cluster_17: 11.912, file_cluster_7: 11.943
- **Magnitude:** 489.78 | **LOC:** 733 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.5283%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadStructure` (Impact: 42.1)
  * `atomColor` (Impact: 27.3)
  * `addElement` (Impact: 22.5)
  * `setLigandOptions` (Impact: 16.9)
  * `setResidueOptions` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 93`, `args: 51`, `func_start: 97`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 166`, `duplicate_logic: 66`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 3`
* *Defense:* `safety: 14`, `doc: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/interactive/xray-viewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.066 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.425 IQR)
- **Top Global Matches:** file_cluster_8: 11.066, file_cluster_7: 11.759, file_cluster_17: 11.764
- **Magnitude:** 318.92 | **LOC:** 456 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.1076%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addElement` (Impact: 16.2)
  * `onchange` (Impact: 15.8)
  * `onkeypress` (Impact: 14.8)
  * `loadExample` (Impact: 13.2)
  * `isolevelScroll` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 51`, `args: 32`, `func_start: 64`
* *Risk/State:* `state_mutation: 78`, `duplicate_logic: 46`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `concurrency: 6`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/interactive/ligand-viewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.884 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.479 IQR)
- **Top Global Matches:** file_cluster_8: 10.884, file_cluster_7: 11.54, file_cluster_17: 11.59
- **Magnitude:** 315.4 | **LOC:** 628 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.4072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setLigandOptions` (Impact: 16.9)
  * `setResidueOptions` (Impact: 12.9)
  * `setChainOptions` (Impact: 6.7)
  * `showLigand` (Impact: 5.9)
  * `addElement` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 68`, `args: 46`, `func_start: 91`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 125`, `duplicate_logic: 60`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/js/ui/ui.ngl.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.31 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.463 IQR)
- **Top Global Matches:** file_cluster_8: 12.31, file_cluster_11: 12.44, file_cluster_12: 12.486
- **Magnitude:** 201.5 | **LOC:** 369 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.2529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onEnter` (Impact: 25.0)
  * `ComponentPanel` (Impact: 4.9)
  * `SelectionInput` (Impact: 4.8)
  * `ColorPopupMenu` (Impact: 4.2)
    * *Intent:* /** * @file UI NGL * @author Alexander Rose <alexander.rose@weirdbyte.de> */
  * `setValue` (Impact: 3.9)
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

### `src/surface/edt-surface.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.729 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.768 IQR)
- **Top Global Matches:** file_cluster_8: 12.729, file_cluster_13: 12.851, file_cluster_11: 12.911
- **Magnitude:** 119.3 | **LOC:** 817 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.1356%), Tech Debt (90.4377%)
**Top Internal Functions/Classes:**
  * `EDTSurface` (Impact: 444.0)
  * `fastoneshell` (Impact: 115.2)
  * `fillatom` (Impact: 59.7)
  * `fillAtomWaals` (Impact: 55.5)
  * `fastdistancemap` (Impact: 51.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 130`, `args: 25`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 257`, `dead_code: 6`, `duplicate_logic: 12`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.832
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.109604
  * `Imports (Out-Degree: 3):` volume, grid, vector-utils, types, surface-utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/grid.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.915 IQR)
- **Top Global Matches:** file_cluster_4: 10.915, file_cluster_8: 10.96, file_cluster_17: 11.276
- **Magnitude:** 115.06 | **LOC:** 150 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.8362%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `appendImage` (Impact: 13.3)
  * `loadList` (Impact: 10.1)
  * `activate` (Impact: 7.5)
  * `sample` (Impact: 4.0)
  * `loadArchive` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 36`, `args: 19`, `func_start: 16`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 13`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ngl.dev.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/interactive/crosslinking.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.269 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.804 IQR)
- **Top Global Matches:** file_cluster_8: 8.269, file_cluster_7: 9.17, file_cluster_1: 9.389
- **Magnitude:** 105.98 | **LOC:** 885 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.3854%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initColourSchemes` (Impact: 10.1)
    * *Intent:* // make a colour scheme that grabs the score of each link and uses it to return a colour
  * `linkColourScheme` (Impact: 9.9)
  * `bondColor` (Impact: 9.7)
  * `makeAtomSelection` (Impact: 2.2)
    * *Intent:* // return unique atom indices as a selection from a set of pairs of atom indices
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 35`, `args: 14`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 51`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/scripts/test/nci.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.138 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.695 IQR)
- **Top Global Matches:** file_cluster_8: 9.138, file_cluster_7: 9.977, file_cluster_1: 10.204
- **Magnitude:** 104.82 | **LOC:** 474 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addElement` (Impact: 4.2)
  * `addElement` (Impact: 4.2)
  * `onchange` (Impact: 4.0)
  * `onkeypress` (Impact: 3.9)
  * `onchange` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 23`, `args: 17`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 39`, `duplicate_logic: 14`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/geometry/spline.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.806 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.952 IQR)
- **Top Global Matches:** file_cluster_13: 13.806, file_cluster_2: 13.949, file_cluster_11: 13.975
- **Magnitude:** 99.24 | **LOC:** 667 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.0647%), Tech Debt (96.2993%)
**Top Internal Functions/Classes:**
  * `reset` (Impact: 59.5)
  * `getNormalDir` (Impact: 43.8)
  * `constructor` (Impact: 18.2)
  * `getAtomIterator` (Impact: 13.4)
  * `interpolateNormalDir` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 102`, `args: 38`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 653`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 16`, `import: 10`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.112652
  * `Imports (Out-Degree: 9):` picker, globals, atom-proxy, polymer, math-utils, types, radius-factory, colormaker...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `scripts/js/node/download.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.936 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.853 IQR)
- **Top Global Matches:** file_cluster_4: 11.936, file_cluster_13: 12.106, file_cluster_8: 12.313
- **Magnitude:** 97.16 | **LOC:** 111 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.0023%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `getUrl` (Impact: 18.6)
  * `downloadIds` (Impact: 13.3)
  * `download` (Impact: 2.5)
  * `parseIdListFile` (Impact: 2.4)
  * `downloadIdsChunked` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 8`, `func_start: 9`
* *Risk/State:* `state_mutation: 38`, `duplicate_logic: 4`
* *Architecture:* `io: 18`, `concurrency: 14`, `import: 7`
* *Defense:* `safety: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, zlib, utils.js, http, fs, download, performance-now
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/buffer/buffer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.176 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.89 IQR)
- **Top Global Matches:** file_cluster_8: 13.176, file_cluster_13: 13.262, file_cluster_11: 13.366
- **Magnitude:** 92.54 | **LOC:** 878 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.5468%), Tech Debt (36.8039%)
**Top Internal Functions/Classes:**
  * `setParameters` (Impact: 45.0)
  * `makeWireframeIndex` (Impact: 41.2)
  * `setUniforms` (Impact: 40.1)
  * `setAttributes` (Impact: 32.3)
  * `getDefines` (Impact: 25.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 71`, `args: 42`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 522`, `planned_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `import: 7`
* *Defense:* `safety: 3`, `doc: 20`, `immutability_locks: 55`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.283
  * `Choke Point (Betweenness):` 0.014956 | `Ripple Effect (Closeness):` 0.152911
  * `Imports (Out-Degree: 5):` picker, shader-utils, globals, types, three, array-utils, utils
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `src/store/residue-type.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.21 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.66 IQR)
- **Top Global Matches:** file_cluster_8: 13.21, file_cluster_13: 13.307, file_cluster_11: 13.368
- **Magnitude:** 89.93 | **LOC:** 752 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.6327%), Tech Debt (77.1889%)
**Top Internal Functions/Classes:**
  * `addRing` (Impact: 45.2)
  * `assignBondReferenceAtomIndices` (Impact: 41.2)
  * `getBackboneType` (Impact: 26.9)
  * `getMoleculeType` (Impact: 23.4)
  * `getBackboneIndexList` (Impact: 18.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 88`, `args: 49`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 466`, `planned_debt: 10`, `duplicate_logic: 4`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `doc: 15`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.06
  * `Choke Point (Betweenness):` 0.000143 | `Ripple Effect (Closeness):` 0.146723
  * `Imports (Out-Degree: 6):` structure, atom-proxy, structure-constants, matrix-utils, residue-proxy, principal-axes, utils, structure-utils
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/structure/structure-utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.173 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.663 IQR)
- **Top Global Matches:** file_cluster_8: 12.173, file_cluster_13: 12.383, file_cluster_11: 12.424
- **Magnitude:** 86.96 | **LOC:** 1112 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.577%), Tech Debt (96.5457%)
**Top Internal Functions/Classes:**
  * `assignSecondaryStructure` (Impact: 70.6)
  * `calculateBondsBetween` (Impact: 48.0)
  * `calculateChainnames` (Impact: 44.3)
  * `calculateBondsWithin` (Impact: 44.0)
  * `guessElement` (Impact: 37.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 98`, `args: 96`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 274`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 12`
* *Architecture:* `api: 18`, `import: 12`
* *Defense:* `doc: 6`, `immutability_locks: 147`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.803
  * `Choke Point (Betweenness):` 0.005065 | `Ripple Effect (Closeness):` 0.165195
  * `Imports (Out-Degree: 8):` symmetry-utils, structure, structure-builder, helixbundle, globals, polymer, assembly, structure-constants...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `scripts/js/node/timeParsing.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.846 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.748 IQR)
- **Top Global Matches:** file_cluster_4: 11.846, file_cluster_13: 12.017, file_cluster_17: 12.101
- **Magnitude:** 85.86 | **LOC:** 109 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.8476%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFileObject` (Impact: 16.9)
  * `parseFiles` (Impact: 5.1)
  * `getDirFiles` (Impact: 5.0)
  * `isBinary` (Impact: 4.8)
  * `parseFilesChunked` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 29`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `io: 17`, `concurrency: 14`, `import: 8`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, zlib, file-api, utils.js, fs, path, ngl.dev.js, performance-now
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/js/slimer/gallery.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.675 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.407 IQR)
- **Top Global Matches:** file_cluster_8: 10.675, file_cluster_17: 10.774, file_cluster_4: 10.958
- **Magnitude:** 84.42 | **LOC:** 203 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5856%), Tech Debt (76.731%)
**Top Internal Functions/Classes:**
  * `renderExample` (Impact: 18.0)
  * `onCallback` (Impact: 8.5)
  * `setInterval` (Impact: 5.6)
  * `onLoadFinished` (Impact: 5.1)
  * `onConsoleMessage` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 19`, `args: 23`, `func_start: 12`
* *Risk/State:* `state_mutation: 24`, `orphaned_logic: 6`
* *Architecture:* `io: 18`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 4`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` system, fs, webpage
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/pdb-parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.371 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.562 IQR)
- **Top Global Matches:** file_cluster_8: 11.371, file_cluster_13: 11.569, file_cluster_7: 11.783
- **Magnitude:** 80.72 | **LOC:** 741 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.6951%), Tech Debt (26.0191%)
**Top Internal Functions/Classes:**
  * `_parse` (Impact: 302.5)
    * *Intent:* /** * Create a pdb parser * @param {Streamer} streamer - streamer object * @param {Object} params - ...
  * `_parseChunkOfLines` (Impact: 297.2)
  * `_parseChunkOfLines` (Impact: 14.7)
    * *Intent:* // const zValue = parseInt( line.substr( 66, 4 ) );
  * `getModresId` (Impact: 10.3)
  * `constructor` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 29`, `args: 17`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 148`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `doc: 7`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.299
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005587
  * `Imports (Out-Degree: 9):` parser, globals, structure-parser, unitcell, types, ngl, assembly, streamer...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/structure/structure.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.542 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.372 IQR)
- **Top Global Matches:** file_cluster_13: 13.542, file_cluster_11: 13.75, file_cluster_8: 13.941
- **Magnitude:** 78.62 | **LOC:** 1125 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.036%), Tech Debt (70.1883%)
**Top Internal Functions/Classes:**
  * `getBondData` (Impact: 52.7)
  * `getAtomData` (Impact: 38.8)
  * `getAtomSet` (Impact: 33.5)
  * `eachResidue` (Impact: 25.9)
  * `eachModel` (Impact: 25.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 89`, `args: 55`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 375`, `planned_debt: 11`, `duplicate_logic: 3`
* *Architecture:* `io: 6`, `api: 20`, `import: 37`
* *Defense:* `safety: 8`, `doc: 58`, `immutability_locks: 71`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.984
  * `Choke Point (Betweenness):` 0.036371 | `Ripple Effect (Closeness):` 0.214599
  * `Imports (Out-Degree: 29):` chain-proxy, picker, model-proxy, data, atom-store, unitcell, residue-map, bond-proxy...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `src/parser/cif-parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.438 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.334 IQR)
- **Top Global Matches:** file_cluster_8: 12.438, file_cluster_13: 12.593, file_cluster_17: 12.716
- **Magnitude:** 77.8 | **LOC:** 1149 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.9097%), Tech Debt (52.806%)
**Top Internal Functions/Classes:**
  * `_parse` (Impact: 227.7)
    * *Intent:* //
  * `calculateBonds` (Impact: 146.7)
    * *Intent:* // IUCr core CIF schema
  * `parseCore` (Impact: 38.5)
  * `parseChemComp` (Impact: 32.6)
  * `getMatrixDict` (Impact: 25.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 56`, `args: 35`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 133`, `state_mutation: 217`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 59`, `doc: 1`, `immutability_locks: 240`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` structure-builder, globals, structure-parser, unitcell, chemcomp-map, ngl, types, pdb-parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proxy/atom-proxy.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.161 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.524 IQR)
- **Top Global Matches:** file_cluster_13: 14.161, file_cluster_8: 14.407, file_cluster_11: 14.447
- **Magnitude:** 76.06 | **LOC:** 813 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.2686%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `connectedTo` (Impact: 25.5)
  * `qualifiedName` (Impact: 20.7)
  * `getResidueBonds` (Impact: 19.6)
  * `eachBond` (Impact: 9.6)
  * `eachBondedAtom` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 116`, `args: 105`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 390`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 24`
* *Architecture:* `api: 32`, `import: 15`
* *Defense:* `safety: 2`, `doc: 117`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.737
  * `Choke Point (Betweenness):` 0.008451 | `Ripple Effect (Closeness):` 0.200543
  * `Imports (Out-Degree: 13):` structure, atom-store, atom-map, types, residue-map, bond-proxy, atom-type, entity...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `src/viewer/viewer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.202 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_13: 13.202, file_cluster_8: 13.229, file_cluster_4: 13.407
- **Magnitude:** 75.33 | **LOC:** 1410 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.6827%), Tech Debt (10.6315%)
**Top Internal Functions/Classes:**
  * `onBeforeRender` (Impact: 51.4)
  * `constructor` (Impact: 30.6)
  * `setCamera` (Impact: 27.5)
    * *Intent:* // console.log(gl.getContextAttributes().antialias)
  * `setClip` (Impact: 20.1)
  * `pick` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 40`, `args: 23`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `state_mutation: 484`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 12`, `import: 11`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 37`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.254
  * `Choke Point (Betweenness):` 0.005078 | `Ripple Effect (Closeness):` 0.17986
  * `Imports (Out-Degree: 9):` gl-utils, stats, globals, buffer, math-utils, viewer-utils, viewer-constants, colormaker...
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `src/surface/volume.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.55 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.311 IQR)
- **Top Global Matches:** file_cluster_13: 13.55, file_cluster_11: 13.839, file_cluster_4: 13.845
- **Magnitude:** 71.06 | **LOC:** 530 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8942%), Tech Debt (79.8343%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 121.0)
  * `getDataSize` (Impact: 29.9)
  * `setData` (Impact: 27.8)
  * `getSurfaceWorker` (Impact: 22.4)
  * `constructor` (Impact: 17.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 48`, `args: 41`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 315`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 5`, `api: 16`, `concurrency: 7`, `import: 13`
* *Defense:* `safety: 5`, `doc: 28`, `immutability_locks: 42`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` picker, globals, vector-utils, worker-pool, types, marching-cubes, surface, colormaker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/js/lib/queue.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.421 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.942 IQR)
- **Top Global Matches:** file_cluster_8: 13.421, file_cluster_4: 13.577, file_cluster_15: 13.691
- **Magnitude:** 67.76 | **LOC:** 44 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.799%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Queue` (Impact: 12.4)
  * `next` (Impact: 5.6)
  * `push` (Impact: 4.2)
    * *Intent:* // API
  * `run` (Impact: 2.4)
  * `kill` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 5`, `args: 7`, `func_start: 9`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `api: 3`, `concurrency: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/color/uniform-colormaker.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, state_mutation: 7, args: 4
- `examples/mobile.html` (HTML) | Magnitude: 13.22 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 9, args: 7, state_mutation: 7
- `src/structure/data.ts` (TYPESCRIPT) | Magnitude: 1.65 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 13, decorators: 10, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/parser/ply-parser.ts` (TYPESCRIPT) | Magnitude: 31.38 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 297, structural_boundaries: 89, branch: 79, state_mutation: 73
- `src/controls/mouse-controls.ts` (TYPESCRIPT) | Magnitude: 13.79 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 51, branch: 38, structural_boundaries: 37
- `examples/js/ui/ui.extra.js` (JAVASCRIPT) | Magnitude: 941.42 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 663, state_mutation: 483, structural_boundaries: 145, reflection_metaprogramming: 103
- `src/utils.ts` (TYPESCRIPT) | Magnitude: 59.3 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 368, structural_boundaries: 151, branch: 140, state_mutation: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/surface/filtered-volume.ts` (TYPESCRIPT) | Magnitude: 18.46 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 100, indent_spaces: 82, branch: 26, reflection_metaprogramming: 21
- `scripts/gallery.sh` (SHELL) | Magnitude: 1.77 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, branch: 5, structural_boundaries: 3, reflection_metaprogramming: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/buffer/doublesided-buffer.ts` (TYPESCRIPT) | Magnitude: 20.69 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 143, state_mutation: 130, branch: 19, args: 16
- `src/buffer/tubemesh-buffer.ts` (TYPESCRIPT) | Magnitude: 14.82 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 247, state_mutation: 107, immutability_locks: 45, branch: 41
- `src/store/model-store.ts` (TYPESCRIPT) | Magnitude: 0.45 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 2, doc: 2
- `src/representation/measurement-representation.ts` (TYPESCRIPT) | Magnitude: 18.2 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 299, state_mutation: 101, structural_boundaries: 47, branch: 38
- `src/geometry/primitive.ts` (TYPESCRIPT) | Magnitude: 18.93 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, structural_boundaries: 93, state_mutation: 80, args: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/component/component-collection.ts` (TYPESCRIPT) | Magnitude: 0.72 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 5, args: 4, func_start: 2
- `src/parser/parser-registry.ts` (TYPESCRIPT) | Magnitude: 6.51 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, state_mutation: 24, structural_boundaries: 20, args: 18
- `src/component/representation-collection.ts` (TYPESCRIPT) | Magnitude: 3.14 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 20, args: 14, state_mutation: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/scripts/color/bond-data.js` (JAVASCRIPT) | Magnitude: 24.24 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, concurrency: 6, structural_boundaries: 3, state_mutation: 3
- `examples/grid.html` (HTML) | Magnitude: 115.06 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 39, structural_boundaries: 36, args: 19
- `src/streamer/streamer.ts` (TYPESCRIPT) | Magnitude: 27.42 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 168, indent_spaces: 144, branch: 36, structural_boundaries: 26
- `src/worker/worker-utils.ts` (TYPESCRIPT) | Magnitude: 5.2 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 11, branch: 10, args: 7
- `examples/scripts/selection/spatialHash.js` (JAVASCRIPT) | Magnitude: 23.86 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 15, structural_boundaries: 9, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/parser/gro-parser.ts` (TYPESCRIPT) | Magnitude: 17.37 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, state_mutation: 90, structural_boundaries: 40, branch: 20
- `examples/scripts/test/alignment2.js` (JAVASCRIPT) | Magnitude: 31.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 15, concurrency: 14, structural_boundaries: 4, args: 3
- `src/symmetry/unitcell.ts` (TYPESCRIPT) | Magnitude: 8.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 146, state_mutation: 54, immutability_locks: 28, args: 26
- `examples/js/ui/ui.js` (JAVASCRIPT) | Magnitude: 767.2 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 553, state_mutation: 420, structural_boundaries: 158, args: 102
- `examples/scripts/test/superposition.js` (JAVASCRIPT) | Magnitude: 30.32 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: concurrency: 14, indent_spaces: 13, structural_boundaries: 3, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/utils/kdtree.ts` (TYPESCRIPT) | Magnitude: 21.89 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 159, state_mutation: 99, branch: 32, immutability_locks: 32
- `src/constants.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, immutability_locks: 3, doc: 1
- `src/chemistry/interactions/metal-binding.ts` (TYPESCRIPT) | Magnitude: 10.54 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 104, branch: 49, dead_code: 25, structural_boundaries: 18
- `src/geometry/grid.ts` (TYPESCRIPT) | Magnitude: 4.91 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 11, args: 11, func_start: 11

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/representation/measurement-representation.ts` -> **Severity: 5.131** (Bridge: 0.0513 * Flux: 99.9909%)
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

- `src/globals.ts` -> **Severity: 7789.897** (Blast Radius: 77.901 * Doc Risk: 99.9974%)
- `src/utils/registry.ts` -> **Severity: 1388.696** (Blast Radius: 25.738 * Doc Risk: 53.9551%)
- `src/types.ts` -> **Severity: 1316.752** (Blast Radius: 27.2 * Doc Risk: 48.41%)
- `src/math/array-utils.ts` -> **Severity: 1242.445** (Blast Radius: 12.978 * Doc Risk: 95.7347%)
- `src/ngl.ts` -> **Severity: 1186.147** (Blast Radius: 31.006 * Doc Risk: 38.2554%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
