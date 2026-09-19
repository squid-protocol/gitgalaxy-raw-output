# ARCHITECTURAL_BRIEF: ngl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nglviewer/ngl.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 578 analyzed artifact(s), 59170 LOC.
- **Load-bearing artifact:** `src/globals.ts` -- 153 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/ngl.ts` -- pulls in 84 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/pako_inflate.es6.js` at magnitude 3680.98 (structural weight, not risk).
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
| Total Artifacts | 1128 |
| Analyzed Artifacts (Scanned) | 578 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 550 |
| Total LOC | 59170 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 51.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4373 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2018 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 34.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8848 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 335 | 43665 | 58.0% |
| JAVASCRIPT | 166 | 12688 | 28.7% |
| GLSL | 32 | 1529 | 5.5% |
| MARKDOWN | 16 | 0 | 2.8% |
| HTML | 7 | 384 | 1.2% |
| PLAINTEXT | 6 | 0 | 1.0% |
| JSON | 4 | 97 | 0.7% |
| CSS | 3 | 439 | 0.5% |
| PYTHON | 3 | 86 | 0.5% |
| SHELL | 3 | 57 | 0.5% |
| CSV | 2 | 225 | 0.3% |
| XML | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.639`
> **Composition Archetype:** `Hub-Coupled App` (z +2.64; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 27%, Data / Markup / Trivial 17%, Large Core Modules (3) 16%, State Mutators Files 9%, Interface Declarations Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 556 | 96.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 550*

**Composition by Extension & Reason:**
- `.ts`: 300x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 66 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 4712 commas in 986 LOC)
- `.pdb`: 65x Excluded (Unsupported Extension: '.pdb')
- `.cif`: 23x Excluded (Unsupported Extension: '.cif')
- `.png`: 18x Excluded (Explicitly Denied Extension: '.png')
- `.gz`: 17x Excluded (Explicitly Denied Extension: '.gz')
- `.gro`: 15x Excluded (Unsupported Extension: '.gro')
- `.xvg`: 9x Excluded (Unsupported Extension: '.xvg')
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.sdf`: 6x Excluded (Unsupported Extension: '.sdf')
- `.mmtf`: 5x Excluded (Unsupported Extension: '.mmtf')
- `.ccp4`: 5x Excluded (Unsupported Extension: '.ccp4')
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.sublime-project')
- `.mol2`: 4x Excluded (Unsupported Extension: '.mol2')
- `.map`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.4 | 23.7 | 11.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 50.6 | 66.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.9 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.8 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 1.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.1 | 33.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 280 | 80 | 1 | `src/geometry/spline.ts` |
| cleanup | 100 | 32 | 0 | `examples/js/gui.js` |
| guards | 980 | 135 | 3 | `lib/pako_inflate.es6.js` |
| danger | 967 | 171 | 4 | `src/parser/cif-parser.ts` |
| concurrency | 332 | 182 | 2 | `examples/js/gui.js` |
| connectivity | 2010 | 320 | 8 | `src/proxy/atom-proxy.ts` |
| io | 332 | 85 | 2 | `src/loader/loader-utils.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 23 | 6 | 0 | `src/worker/worker.ts` |
| time | 39 | 17 | 0 | `examples/js/ui/ui.extra.js` |
| serialization | 26 | 13 | 0 | `examples/js/gui.js` |
| regex | 123 | 34 | 0 | `src/parser/kin-parser.ts` |
| events | 125 | 27 | 0 | `examples/js/ui/ui.js` |
| tests | 693 | 38 | 0 | `test/utils/tests-bitarray.spec.ts` |
| docs | 1316 | 316 | 5 | `src/proxy/atom-proxy.ts` |
| debt | 382 | 115 | 2 | `src/geometry/helixorient.ts` |
| mutation | 20443 | 435 | 85 | `lib/pako_inflate.es6.js` |
| dead_code | 279 | 92 | 2 | `lib/pako_inflate.es6.js` |
| credential | 0 | 0 | 0 | - |
| threat | 618 | 125 | 2 | `examples/js/ui/ui.extra.js` |
| ml_ai | 455 | 87 | 1 | `src/surface/av-surface.ts` |
| ui | 90 | 19 | 0 | `src/geometry/spline.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/loader/loader-utils.ts` (Hits: 18)
- `scripts/js/node/timeParsing.js` (Hits: 14)
- `examples/webapp.html` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **globals.ts** (`src/globals.ts`) — 153 inbound connections
2. **atom-proxy.ts** (`src/proxy/atom-proxy.ts`) — 63 inbound connections
3. **structure.ts** (`src/structure/structure.ts`) — 50 inbound connections
4. **viewer.ts** (`src/viewer/viewer.ts`) — 49 inbound connections
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

- `inflate` **(Many-Argument Workhorses)** (@ `lib/pako_inflate.es6.js`) -> Impact: **466.8** | LOC: 1091
- `EDTSurface` **(Many-Argument Workhorses)** (@ `src/surface/edt-surface.ts`) -> Impact: **435.2** | LOC: 788
- `getView` **(Compute Cores)** (@ `src/structure/structure.ts`) -> Impact: **342.3** | LOC: 1019
- `_parseChunkOfLines` **(Many-Argument Workhorses)** (@ `src/parser/pdb-parser.ts`) -> Impact: **279.5** | LOC: 430
- `_parse` **(I/O & Config Routines)** (@ `src/parser/pdb-parser.ts`) -> Impact: **178.8** | LOC: 617
- `getFieldAsFloat32` **(Many-Argument Workhorses)** (@ `src/parser/cif-parser.ts`) -> Impact: **164.6** | LOC: 171
- `inflate_table` **(Many-Argument Workhorses)** (@ `lib/pako_inflate.es6.js`) -> Impact: **158.6** | LOC: 291
  * *Intent:* // module.exports =
- `parseSele` **(Compute Cores)** (@ `src/selection/selection-parser.ts`) -> Impact: **156.3** | LOC: 468
- `atomTestFn` **(Compute Cores)** (@ `src/selection/selection-test.ts`) -> Impact: **140.0** | LOC: 63
- `calculateHydrogensCharge` **(Many-Argument Workhorses)** (@ `src/chemistry/valence-model.ts`) -> Impact: **138.9** | LOC: 179
  * *Intent:* /** * Attempts to produce a consistent charge and implicit * H-count for an atom. * * If both params.assignCharge and params.assignH, this * approxima...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/parser` | 37 | 7092.7 | 49.1% | 14.26% |
| `lib` | 4 | 4881.37 | 38.68% | 51.7% |
| `src/representation` | 33 | 3973.54 | 41.89% | 2.46% |
| `src/surface` | 8 | 3521.68 | 66.63% | 0.0% |
| `src/buffer` | 35 | 3207.04 | 32.54% | 7.61% |
| `src/structure` | 8 | 2958.22 | 52.22% | 8.54% |
| `src/math` | 6 | 2188.82 | 57.13% | 7.89% |
| `src/utils` | 15 | 1867.32 | 44.1% | 3.13% |
| `src/viewer` | 7 | 1752.1 | 50.09% | 6.14% |
| `examples/js/ui` | 3 | 1721.82 | 96.94% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/pako_inflate.es6.d.ts` -> **100.0%** Exposure
- `src/geometry/primitive.ts` -> **99.9988%** Exposure
- `src/color/uniform-colormaker.ts` -> **99.7527%** Exposure
- `src/parser/validation-parser.ts` -> **99.7527%** Exposure
- `src/color/atomindex-colormaker.ts` -> **99.6827%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doc/plugins/header.js` -> **100.0%** Exposure
- `lib/mmtf.es6.js` -> **100.0%** Exposure
- `lib/pako_inflate.es6.js` -> **100.0%** Exposure
- `scripts/js/lib/queue.js` -> **100.0%** Exposure
- `src/align/align-utils.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/js/ui/ui.js` -> **22** Orphaned Functions | **24** Duplicates
- `src/geometry/primitive.ts` -> **0** Orphaned Functions | **12** Duplicates
- `examples/js/gui.js` -> **0** Orphaned Functions | **6** Duplicates
- `lib/pako_inflate.es6.d.ts` -> **0** Orphaned Functions | **6** Duplicates
- `scripts/js/slimer/gallery.js` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `234` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/pako_inflate.es6.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3680.98 | **LOC:** 2973 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.875; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (89.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 81.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate` **(Many-Argument Workhorses)** (Impact: 466.8)
  * `inflate_table` **(Many-Argument Workhorses)** (Impact: 158.6)
    * *Intent:* // module.exports =
  * `inflate_fast` **(Many-Argument Workhorses)** (Impact: 107.8)
    * *Intent:* */ // module.exports =
  * `push` **(Defensive Guards)** (Impact: 70.0)
    * *Intent:* * We strongly recommend to use `Uint8Array` on input for best speed (output * format is detected aut...
  * `string2buf` **(Defensive Guards)** (Impact: 28.1)
    * *Intent:* // convert string to array (typed, when possible)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 815 instances
* *State Mutation (weighted view):* 2561
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 345`, `args: 33`, `func_start: 33`
* *Risk/State:* `state_mutation: 931`, `dead_code: 34`, `planned_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 147`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.875
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001733
  * `Imports (Out-Degree: 1):` common, adler32, common, crc32, inffast, inftrees, common, strings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/surface/edt-surface.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1453.04 | **LOC:** 817 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.733; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EDTSurface` **(Many-Argument Workhorses)** (Impact: 435.2)
  * `fastoneshell` **(Many-Argument Workhorses)** (Impact: 115.2)
  * `fillatom` **(Compute Cores)** (Impact: 37.7)
  * `fillAtomWaals` **(Compute Cores)** (Impact: 35.2)
  * `marchingcubeinit` **(Compute Cores)** (Impact: 32.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 134`, `args: 15`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 244`, `dead_code: 6`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.733
  * `Choke Point (Betweenness):` 0.000916 | `Ripple Effect (Closeness):` 0.112369
  * `Imports (Out-Degree: 4):` grid, vector-utils, types, surface-utils, volume
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/mmtf.es6.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1196.08 | **LOC:** 1876 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.893; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.7%)
- **Documentation Coverage:** 42.623% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `traverseMmtf` **(Many-Argument Workhorses)** (Impact: 69.5)
    * *Intent:* /** * Traverse the MMTF structure data. */
  * `decodeMsgpack` **(Compute Cores)** (Impact: 60.5)
    * *Intent:* */ /** * msgpack decode module. */ /** * decode binary encoded MessagePack v5 (http://msgpack.org/) ...
  * `encode$1` **(I/O & Config Routines)** (Impact: 49.2)
    * *Intent:* /** * encode data value (recursively) into binary encoded MessagePack v5 (http://msgpack.org/) */
  * `encodedSize` **(Defensive Guards)** (Impact: 48.5)
  * `performDecoding` **(Many-Argument Workhorses)** (Impact: 39.9)
    * *Intent:* */ /** * [performDecoding description] */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 311`, `args: 60`, `func_start: 59`
* *Risk/State:* `state_mutation: 206`, `dead_code: 11`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 40`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004622
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/structure/structure.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1189.18 | **LOC:** 1125 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **37**; blast radius 28.089; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Connectivity (formerly Api Exposure) (87.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 56.3218% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getView` **(Compute Cores)** (Impact: 342.3)
  * `getBondData` **(Compute Cores)** (Impact: 84.9)
  * `getAtomData` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* //
  * `getAtomSet` **(Compute Cores)** (Impact: 24.2)
    * *Intent:* /** * Get a set of atoms * initialize the atom set. * Boolean: init with value; * Selection: init wi...
  * `getBoundingBox` **(Compute Cores)** (Impact: 22.5)
    * *Intent:* // /** * Gets the bounding box of the (selected) structure atoms */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 410
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 113`, `args: 66`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 168`, `planned_debt: 25`
* *Architecture:* `io: 6`, `api: 30`, `import: 37`
* *Defense:* `doc: 22`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.089
  * `Choke Point (Betweenness):` 0.033032 | `Ripple Effect (Closeness):` 0.21444
  * `Imports (Out-Degree: 32):` spatial-hash, globals, array-utils, matrix-utils, principal-axes, atom-proxy, bond-proxy, chain-proxy...
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `examples/js/gui.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1167.08 | **LOC:** 2397 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.688; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (71.6%), Concurrency Surface (formerly Concurrency) (49.6%), Connectivity (formerly Api Exposure) (26.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createParameterInput` **(Defensive Guards)** (Impact: 38.6)
  * `TrajectoryElementWidget` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* // Trajectory
  * `DirectoryListingWidget` **(Many-Argument Workhorses)** (Impact: 35.0)
    * *Intent:* // Listing
  * `SidebarWidget` **(Compute Cores)** (Impact: 30.9)
    * *Intent:* // Sidebar
  * `StageWidget` **(Compute Cores)** (Impact: 29.1)
    * *Intent:* // Stage
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 509
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 294`, `args: 203`, `func_start: 78`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 269`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 10`, `api: 5`, `concurrency: 13`
* *Defense:* `safety: 54`, `doc: 1`, `sync_locks: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001733
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser/cif-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1122.9 | **LOC:** 1149 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFieldAsFloat32` **(Many-Argument Workhorses)** (Impact: 164.6)
  * `_parse` **(I/O & Config Routines)** (Impact: 114.7)
  * `processSecondaryStructure` **(Many-Argument Workhorses)** (Impact: 87.5)
  * `processSymmetry` **(Many-Argument Workhorses)** (Impact: 81.1)
  * `processConnections` **(Many-Argument Workhorses)** (Impact: 66.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 464
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 69`, `args: 23`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 133`, `state_mutation: 200`, `planned_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 57`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.001191 | `Ripple Effect (Closeness):` 0.005199
  * `Imports (Out-Degree: 13):` globals, ngl, selection, chemcomp-map, entity, structure-builder, structure-utils, assembly...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/viewer/viewer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1025.52 | **LOC:** 1410 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **49** in-repo importer(s); it depends on **11**; blast radius 10.577; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.1%)
- **Documentation Coverage:** 82.8125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onBeforeRender` **(Many-Argument Workhorses)** (Impact: 51.4)
  * `_updateBoundingBox` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `setCamera` **(Compute Cores)** (Impact: 27.5)
  * `constructor` **(Compute Cores)** (Impact: 22.3)
  * `_initRenderer` **(I/O & Config Routines)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 144 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 52`, `args: 56`, `func_start: 51`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 240`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 2`
* *Architecture:* `api: 18`, `concurrency: 3`, `import: 11`
* *Defense:* `safety: 4`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.577
  * `Choke Point (Betweenness):` 0.006702 | `Ripple Effect (Closeness):` 0.181018
  * `Imports (Out-Degree: 9):` buffer, colormaker, globals, math-utils, shader-utils, gl-utils, stats, viewer-constants...
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `src/parser/pdb-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 983.64 | **LOC:** 741 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **13**; blast radius 2.278; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parseChunkOfLines` **(Many-Argument Workhorses)** (Impact: 279.5)
  * `_parse` **(I/O & Config Routines)** (Impact: 178.8)
  * `getModresId` **(Compute Cores)** (Impact: 10.3)
  * `constructor` **(Generic / Templated Code)** (Impact: 5.6)
    * *Intent:* /** * Create a pdb parser * atom numbers >99.999 and * residue numbers >9.999 * 'auto': If a hetgrou...
  * `type` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 492
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 38`, `args: 11`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 180`, `planned_debt: 1`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.278
  * `Choke Point (Betweenness):` 0.004157 | `Ripple Effect (Closeness):` 0.016638
  * `Imports (Out-Degree: 10):` globals, ngl, streamer, entity, structure-constants, structure-utils, assembly, unitcell...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/math/matrix-utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 975.1 | **LOC:** 736 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 4.052; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (85.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JacobiSVDImpl` **(Many-Argument Workhorses)** (Impact: 130.4)
  * `svd` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `multiply` **(Many-Argument Workhorses)** (Impact: 9.4)
    * *Intent:* // C = A * B
  * `multiplyAtB` **(Many-Argument Workhorses)** (Impact: 9.4)
    * *Intent:* // C = A' * B
  * `multiplyABt` **(Many-Argument Workhorses)** (Impact: 9.3)
    * *Intent:* // C = A * B'
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 41`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 266`, `dead_code: 1`
* *Architecture:* `api: 29`, `import: 3`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.052
  * `Choke Point (Betweenness):` 0.001058 | `Ripple Effect (Closeness):` 0.161047
  * `Imports (Out-Degree: 2):` types, vector-utils
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/structure/structure-utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 933.68 | **LOC:** 1112 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **12**; blast radius 8.362; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.4%)
- **Documentation Coverage:** 89.7436% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assignSecondaryStructure` **(Many-Argument Workhorses)** (Impact: 70.6)
  * `calculateBondsBetween` **(Many-Argument Workhorses)** (Impact: 48.0)
  * `calculateChainnames` **(Many-Argument Workhorses)** (Impact: 44.3)
    * *Intent:* /** * When no chain names are set for the given structure, calculates * chains based on: * - polymer...
  * `calculateBondsWithin` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `calculateResidueBonds` **(Compute Cores)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 127 instances
* *State Mutation (weighted view):* 440
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 103`, `args: 61`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 186`, `dead_code: 2`, `planned_debt: 6`
* *Architecture:* `api: 17`, `import: 12`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.362
  * `Choke Point (Betweenness):` 0.006111 | `Ripple Effect (Closeness):` 0.169271
  * `Imports (Out-Degree: 9):` helixbundle, kdtree, globals, polymer, residue-proxy, structure, structure-builder, assembly...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `examples/js/ui/ui.extra.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 922.02 | **LOC:** 1137 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.688; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (98.4%), Guard Balance (formerly Safety Score) (97.1%), Connectivity (formerly Api Exposure) (51.4%), Concurrency Surface (formerly Concurrency) (34.9%)
- **Documentation Coverage:** 98.4127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VirtualTable` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* // Virtual Table
  * `VirtualList` **(Many-Argument Workhorses)** (Impact: 41.4)
    * *Intent:* // Virtual List
  * `generatorFn` **(Defensive Guards)** (Impact: 18.3)
    * *Intent:* // list
  * `PopupMenu` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* // Popup Menu (requires Tether)
  * `setCollapsed` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 122 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 518
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 145`, `args: 94`, `func_start: 74`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 274`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 23`, `concurrency: 2`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001733
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/math/array-utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 733.26 | **LOC:** 530 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **3**; blast radius 12.611; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Connectivity (formerly Api Exposure) (87.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quicksortIP` **(Many-Argument Workhorses)** (Impact: 71.0)
    * *Intent:* * Complexity: http://bigocheatsheet.com/ see Quicksort * * points: [x, y, z, x, y, z, x, y, z, ...] ...
  * `quicksortCmp` **(Many-Argument Workhorses)** (Impact: 60.2)
  * `quickselectCmp` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `circularMean` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `serialBlockArray` **(Many-Argument Workhorses)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 70`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 133`, `duplicate_logic: 2`
* *Architecture:* `api: 25`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.611
  * `Choke Point (Betweenness):` 0.002974 | `Ripple Effect (Closeness):` 0.199142
  * `Imports (Out-Degree: 2):` types, math-constants, three
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `examples/js/ui/ui.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 671.8 | **LOC:** 1038 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.688; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (96.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Number` **(Callbacks & Closures)** (Impact: 14.9)
    * *Intent:* // Number
  * `Integer` **(Callbacks & Closures)** (Impact: 13.5)
    * *Intent:* // Integer
  * `FancySelect` **(I/O & Config Routines)** (Impact: 12.5)
    * *Intent:* // FancySelect
  * `setValue` **(Compute Cores)** (Impact: 11.3)
  * `createOption` **(Compute Cores)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 160`, `args: 102`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 243`, `planned_debt: 1`, `duplicate_logic: 24`, `unreferenced_by_name: 22`
* *Architecture:* None
* *Defense:* `safety: 14`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.688
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001733
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/buffer/buffer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 641.78 | **LOC:** 878 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **42** in-repo importer(s); it depends on **7**; blast radius 17.271; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.0%)
- **Documentation Coverage:** 75.5102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setParameters` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* /** * Set buffer parameters */
  * `setUniforms` **(Compute Cores)** (Impact: 29.0)
  * `makeWireframeIndex` **(I/O & Config Routines)** (Impact: 25.9)
  * `setAttributes` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* /** * Sets buffer attributes * and the values are the attribute data. * var buffer = new Buffer(); *...
  * `getDefines` **(Compute Cores)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 75`, `args: 39`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 141`, `planned_debt: 8`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `safety: 3`, `doc: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.271
  * `Choke Point (Betweenness):` 0.015161 | `Ripple Effect (Closeness):` 0.152555
  * `Imports (Out-Degree: 5):` globals, array-utils, shader-utils, types, utils, picker, three
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `src/surface/av-surface.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 593.12 | **LOC:** 629 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.733; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AVSurface` **(Many-Argument Workhorses)** (Impact: 134.0)
  * `makeAVHash` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `obscured` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `projectTorus` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `init` **(Many-Argument Workhorses)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 157`, `args: 22`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 97`, `dead_code: 2`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.733
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.112369
  * `Imports (Out-Degree: 4):` array-utils, vector-utils, types, utils, surface-utils, volume
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 573.96 | **LOC:** 577 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.135; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.2264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deepEqual` **(Compute Cores)** (Impact: 42.0)
  * `throttle` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `download` **(Compute Cores)** (Impact: 30.4)
  * `getTypedArray` **(Compute Cores)** (Impact: 18.3)
  * `uint8ToLines` **(Many-Argument Workhorses)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 158`, `args: 74`, `func_start: 58`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 59`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 42`, `concurrency: 1`, `import: 1`
* *Defense:* `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001733
  * `Imports (Out-Degree: 0):` three
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/selection/selection-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 561.9 | **LOC:** 377 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 4.575; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.1%), Complexity Load (formerly Cognitive Load) (54.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `atomTestFn` **(Compute Cores)** (Impact: 140.0)
  * `residueTestFn` **(Compute Cores)** (Impact: 101.2)
  * `makeTest` **(Compute Cores)** (Impact: 71.3)
  * `test` **(Compute Cores)** (Impact: 49.3)
    * *Intent:* // ( x and y ) can short circuit on false // ( x or y ) can short circuit on true // not ( x and y )
  * `chainTestFn` **(Compute Cores)** (Impact: 32.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 149`, `args: 18`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 16`, `dead_code: 2`, `planned_debt: 6`
* *Architecture:* `io: 3`, `api: 6`, `import: 6`
* *Defense:* `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.575
  * `Choke Point (Betweenness):` 0.001344 | `Ripple Effect (Closeness):` 0.146649
  * `Imports (Out-Degree: 5):` atom-proxy, chain-proxy, model-proxy, residue-proxy, utils, selection-constants
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/geometry/spline.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 552.9 | **LOC:** 667 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 1.012; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getNormalDir` **(Many-Argument Workhorses)** (Impact: 43.8)
  * `constructor` **(Compute Cores)** (Impact: 18.2)
  * `getAtomIterator` **(Compute Cores)** (Impact: 13.4)
  * `interpolateNormalDir` **(Many-Argument Workhorses)** (Impact: 12.1)
  * `interpolateTangent` **(Stateful Encapsulated Methods)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 106`, `args: 37`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 111`, `fragile_debt: 1`
* *Architecture:* `api: 16`, `import: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.012
  * `Choke Point (Betweenness):` 0.000118 | `Ripple Effect (Closeness):` 0.115133
  * `Imports (Out-Degree: 9):` colormaker, globals, array-utils, math-utils, atom-proxy, polymer, types, picker...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/parser/ply-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 546.22 | **LOC:** 899 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.614; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.5%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleElement` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `getBinaryReader` **(Compute Cores)** (Impact: 41.1)
  * `parseASCIINumber` **(Compute Cores)** (Impact: 31.8)
  * `parseHeader` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `postProcess` **(I/O & Config Routines)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 102`, `args: 36`, `func_start: 34`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`, `dead_code: 7`, `planned_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.614
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` globals, surface-parser, three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser/kin-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 526.98 | **LOC:** 794 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.875; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Complexity Load (formerly Cognitive Load) (69.2%), Connectivity (formerly Api Exposure) (11.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hsvToRgb` **(Compute Cores)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 148 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 30`, `args: 19`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 199`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.875
  * `Choke Point (Betweenness):` 0.000668 | `Ripple Effect (Closeness):` 0.001733
  * `Imports (Out-Degree: 2):` globals, parser, three
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/store/residue-type.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 516.4 | **LOC:** 752 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 3.586; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (91.2%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.2%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addRing` **(Many-Argument Workhorses)** (Impact: 35.2)
    * *Intent:* // /** * Ring finding code below adapted from MolQL * Copyright (c) 2017 MolQL contributors, license...
  * `assignBondReferenceAtomIndices` **(I/O & Config Routines)** (Impact: 21.1)
    * *Intent:* /** * For bonds with order > 1, pick a reference atom */
  * `getBackboneType` **(Compute Cores)** (Impact: 19.2)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* /** * to the atoms of the residue */
  * `getMoleculeType` **(Compute Cores)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 103`, `args: 47`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 81`, `planned_debt: 10`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `doc: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.586
  * `Choke Point (Betweenness):` 0.000252 | `Ripple Effect (Closeness):` 0.146649
  * `Imports (Out-Degree: 6):` matrix-utils, principal-axes, atom-proxy, residue-proxy, structure, structure-constants, structure-utils, utils
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/stage/stage.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 468.08 | **LOC:** 958 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **37**; blast radius 9.059; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.8%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toggleFullscreen` **(Compute Cores)** (Impact: 47.6)
    * *Intent:* /** * Toggle fullscreen * defaults to the viewer container */
  * `defaultFileRepresentation` **(I/O & Config Routines)** (Impact: 44.3)
    * *Intent:* /** * Create default representations for the given component */
  * `setParameters` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* /** * Set stage parameters */
  * `loadFile` **(Defensive Guards)** (Impact: 8.9)
    * *Intent:* * * // load from URL and add a 'ball+stick' representation with double/triple bonds * stage.loadFile...
  * `setSize` **(State Mutators)** (Impact: 7.4)
    * *Intent:* /** * Set width and height */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 115`, `args: 64`, `func_start: 45`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 66`, `planned_debt: 3`
* *Architecture:* `io: 7`, `api: 23`, `concurrency: 4`, `import: 37`
* *Defense:* `safety: 2`, `doc: 29`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.059
  * `Choke Point (Betweenness):` 0.025893 | `Ripple Effect (Closeness):` 0.154031
  * `Imports (Out-Degree: 34):` animation, component, component-collection, representation-collection, representation-element, structure-component, surface-component, volume-component...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/trajectory/trajectory.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 449.72 | **LOC:** 626 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **11**; blast radius 3.073; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (47.9%)
- **Documentation Coverage:** 54.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setFrameInterpolated` **(Many-Argument Workhorses)** (Impact: 32.3)
    * *Intent:* /** * Interpolated and set trajectory to frame indices */
  * `_process` **(Many-Argument Workhorses)** (Impact: 21.5)
  * `removePbc` **(Compute Cores)** (Impact: 20.6)
  * `loadFrame` **(Callbacks & Closures)** (Impact: 16.6)
    * *Intent:* /** * Load frame index */
  * `setParameters` **(Compute Cores)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 52`, `args: 43`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 88`, `planned_debt: 2`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `doc: 15`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.073
  * `Choke Point (Betweenness):` 0.001883 | `Ripple Effect (Closeness):` 0.119098
  * `Imports (Out-Degree: 9):` superposition, globals, array-utils, math-utils, atom-proxy, selection, structure, types...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/parser/sdf-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 440.06 | **LOC:** 246 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 1.005; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parseChunkOfLines` **(Many-Argument Workhorses)** (Impact: 136.1)
  * `_parse` **(I/O & Config Routines)** (Impact: 77.0)
  * `type` **(Interface Declarations)** (Impact: 1.1)
  * `_postProcess` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 14`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 75`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.000728 | `Ripple Effect (Closeness):` 0.003466
  * `Imports (Out-Degree: 3):` globals, structure-utils, structure-parser
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/parser/xtc-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 431.9 | **LOC:** 380 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.614; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse` **(I/O & Config Routines)** (Impact: 44.1)
  * `decodeInts` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `decodeBits` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `sizeOfInts` **(Compute Cores)** (Impact: 10.0)
  * `sizeOfInt` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* // const LastIdx = MagicInts.length
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 338
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 15`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 134`, `dead_code: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.614
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` globals, types, utils, trajectory-parser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/representation/measurement-representation.ts` -> **Severity: 4.715** (Bridge: 0.0473 * Flux: 99.7579%)
- `src/globals.ts` -> **Severity: 3.957** (Bridge: 0.0589 * Flux: 67.192%)
- `src/utils/picker.ts` -> **Severity: 3.516** (Bridge: 0.0355 * Flux: 98.9128%)
- `src/structure/structure.ts` -> **Severity: 3.303** (Bridge: 0.033 * Flux: 100.0%)
- `src/stage/stage.ts` -> **Severity: 2.588** (Bridge: 0.0259 * Flux: 99.9617%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/globals.ts` -> **Severity: 23.284** (Embedded: 0.3261 * Error Risk: 71.4117%)
- `src/structure/structure.ts` -> **Severity: 20.898** (Embedded: 0.2144 * Error Risk: 97.4547%)
- `src/math/array-utils.ts` -> **Severity: 19.849** (Embedded: 0.1991 * Error Risk: 99.6714%)
- `src/surface/volume.ts` -> **Severity: 17.784** (Embedded: 0.1835 * Error Risk: 96.9044%)
- `src/structure/structure-view.ts` -> **Severity: 17.448** (Embedded: 0.1806 * Error Risk: 96.6075%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/globals.ts` -> **Severity: 4838.72** (Blast Radius: 75.269 * Doc Risk: 64.2857%)
- `src/utils/registry.ts` -> **Severity: 2171.575** (Blast Radius: 24.818 * Doc Risk: 87.5%)
- `src/structure/structure.ts` -> **Severity: 1582.023** (Blast Radius: 28.089 * Doc Risk: 56.3218%)
- `src/streamer/streamer.ts` -> **Severity: 1397.2** (Blast Radius: 13.972 * Doc Risk: 100.0%)
- `src/worker/worker-registry.ts` -> **Severity: 1341.5** (Blast Radius: 13.415 * Doc Risk: 100.0%)

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
