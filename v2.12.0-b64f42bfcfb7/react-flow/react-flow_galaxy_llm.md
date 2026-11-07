# ARCHITECTURAL_BRIEF: react-flow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wbkd/react-flow.git` |
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
- **Scope:** 662 analyzed artifact(s), 36672 LOC.
- **Load-bearing artifact:** `packages/react/src/types/index.ts` -- 70 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `examples/react/src/App/routes.ts` -- pulls in 65 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 685 |
| Analyzed Artifacts (Scanned) | 662 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 23 |
| Total LOC | 36672 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 96.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7518 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2092 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7696 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 80 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 441 | 28255 | 66.6% |
| HTML | 129 | 6681 | 19.5% |
| CSS | 27 | 1097 | 4.1% |
| MARKDOWN | 17 | 0 | 2.6% |
| PLAINTEXT | 16 | 5 | 2.4% |
| YAML | 12 | 221 | 1.8% |
| JSON | 12 | 169 | 1.8% |
| JAVASCRIPT | 8 | 244 | 1.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 657 |
| unknown | unknown | 5 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 18%, Callbacks & Closures Files 12%, Generic / Templated Code Files 9%, Large Core Modules (2) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 629 | 95.0% |
| Unknown | 5 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 28 | 4.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 23*

**Composition by Extension & Reason:**
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2245 LOC)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14167 LOC)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.2 | 7.3 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 16.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.1 | 3.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.5 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 183 | 97 | 1 | `packages/react/src/hooks/useReactFlow.ts` |
| cleanup | 23 | 14 | 0 | `packages/react/src/hooks/useKeyPress.ts` |
| guards | 966 | 158 | 4 | `packages/system/src/utils/general.ts` |
| danger | 203 | 71 | 1 | `examples/react/cypress/components/utils/adopt-user-nodes.cy.ts` |
| concurrency | 447 | 43 | 0 | `tests/playwright/e2e/nodes.spec.ts` |
| connectivity | 1227 | 459 | 4 | `packages/system/src/types/general.ts` |
| io | 176 | 52 | 0 | `examples/react/src/App/routes.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 22 | 9 | 0 | `packages/system/src/xypanzoom/eventhandler.ts` |
| serialization | 6 | 4 | 0 | `tooling/rollup-config/src/index.js` |
| regex | 15 | 13 | 0 | `packages/react/src/hooks/useKeyPress.ts` |
| events | 263 | 87 | 1 | `packages/system/src/xypanzoom/XYPanZoom.ts` |
| tests | 602 | 35 | 0 | `tests/playwright/e2e/nodes.spec.ts` |
| docs | 869 | 141 | 2 | `packages/react/src/types/component-props.ts` |
| debt | 226 | 75 | 1 | `examples/react/src/examples/Overview/index.tsx` |
| mutation | 7058 | 492 | 27 | `packages/react/src/container/ReactFlow/index.tsx` |
| dead_code | 90 | 59 | 0 | `packages/react/src/store/index.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 239 | 54 | 0 | `packages/system/src/utils/general.ts` |
| ui | 1468 | 286 | 7 | `packages/svelte/src/lib/store/initial-store.svelte.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `examples/react/src/App/routes.ts` (Hits: 66)
- `packages/react/src/components/ConnectionLine/index.tsx` (Hits: 9)
- `examples/react/src/App/index.tsx` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.ts** (`packages/react/src/types/index.ts`) — 70 inbound connections
2. **useStore.ts** (`packages/react/src/hooks/useStore.ts`) — 57 inbound connections
3. **index.ts** (`packages/system/src/types/index.ts`) — 25 inbound connections
4. **general.ts** (`packages/system/src/utils/general.ts`) — 14 inbound connections
5. **index.ts** (`packages/system/src/utils/index.ts`) — 11 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **routes.ts** (`examples/react/src/App/routes.ts`) — 65 outbound dependencies
2. **index.ts** (`packages/react/src/index.ts`) — 37 outbound dependencies
3. **index.ts** (`packages/svelte/src/lib/index.ts`) — 33 outbound dependencies
4. **Controls.tsx** (`packages/react/src/additional-components/Controls/Controls.tsx`) — 14 outbound dependencies
5. **index.tsx** (`packages/react/src/components/NodeWrapper/index.tsx`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getDimensionsAfterResize` **(Many-Argument Workhorses)** (@ `packages/system/src/xyresizer/utils.ts`) -> Impact: **254.3** | LOC: 167
  * *Intent:* * with expandParent or extent: 'parent' set and oh yeah, these things also have to work with keepAspectRatio! * The way this is done is by determining...
- `createStore` **(Defensive Guards)** (@ `packages/svelte/src/lib/store/index.ts`) -> Impact: **136.8** | LOC: 389
- `update` **(Compute Cores)** (@ `packages/system/src/xydrag/XYDrag.ts`) -> Impact: **136.1** | LOC: 289
  * *Intent:* // public functions
- `getInitialStore` **(Defensive Guards)** (@ `packages/svelte/src/lib/store/initial-store.svelte.ts`) -> Impact: **128.6** | LOC: 366
- `Pane` **(Defensive Guards)** (@ `packages/react/src/container/Pane/index.tsx`) -> Impact: **96.5** | LOC: 232
- `XYResizer` **(Compute Cores)** (@ `packages/system/src/xyresizer/XYResizer.ts`) -> Impact: **95.9** | LOC: 249
- `update` **(Many-Argument Workhorses)** (@ `packages/system/src/xyresizer/XYResizer.ts`) -> Impact: **94.7** | LOC: 225
- `EdgeWrapper` **(Compute Cores)** (@ `packages/react/src/components/EdgeWrapper/index.tsx`) -> Impact: **94.5** | LOC: 249
- `NodeWrapper` **(Compute Cores)** (@ `packages/react/src/components/NodeWrapper/index.tsx`) -> Impact: **93.5** | LOC: 229
- `XYPanZoom` **(Defensive Guards)** (@ `packages/system/src/xypanzoom/XYPanZoom.ts`) -> Impact: **79.8** | LOC: 266

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/svelte` | 9 | 10085.58 | 1.02% | 0.0% |
| `examples/svelte` | 8 | 5081.36 | 1.79% | 0.0% |
| `__monolith__` | 10 | 5051.44 | 0.0% | 0.0% |
| `packages/react` | 5 | 5040.7 | 0.0% | 0.0% |
| `tests/playwright/e2e` | 7 | 1298.67 | 12.42% | 0.0% |
| `packages/system/src/utils` | 11 | 1254.4 | 24.85% | 0.0% |
| `packages/svelte/src/lib/store` | 5 | 791.77 | 41.06% | 2.0% |
| `packages/react/src/hooks` | 29 | 769.58 | 8.9% | 1.26% |
| `packages/system/src/xyresizer` | 4 | 709.37 | 35.36% | 0.0% |
| `packages/system/src/xypanzoom` | 5 | 471.44 | 20.89% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **100.0%** Exposure
- `packages/svelte/src/lib/plugins/Minimap/interactive.ts` -> **97.0688%** Exposure
- `packages/svelte/src/lib/utils/index.ts` -> **97.0688%** Exposure
- `packages/svelte/src/lib/hooks/useNodesEdgesViewport.svelte.ts` -> **95.5022%** Exposure
- `packages/svelte/src/lib/hooks/useUpdateNodeInternals.svelte.ts` -> **88.0797%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/react/src/components/BatchProvider/index.tsx` -> **100.0%** Exposure
- `packages/react/src/components/NodeWrapper/useNodeObserver.ts` -> **100.0%** Exposure
- `packages/react/src/utils/changes.ts` -> **100.0%** Exposure
- `packages/system/src/utils/edges/positions.ts` -> **100.0%** Exposure
- `packages/system/src/utils/edges/smoothstep-edge.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/react/src/store/index.ts` -> **13** Orphaned Functions | **0** Duplicates
- `packages/react/src/container/ZoomPane/index.tsx` -> **5** Orphaned Functions | **0** Duplicates
- `packages/react/src/components/Handle/index.tsx` -> **3** Orphaned Functions | **0** Duplicates
- `packages/svelte/src/lib/hooks/useNodesEdgesViewport.svelte.ts` -> **3** Orphaned Functions | **0** Duplicates
- `packages/svelte/src/lib/plugins/Minimap/interactive.ts` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `714` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/playwright/e2e/node-toolbar.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.423)
- **Top Global Matches:** file_cluster_7: 6.423, file_cluster_12: 9.64, file_cluster_5: 9.71
- **Magnitude:** 506.8 | **LOC:** 95 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.893; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (37.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 32`, `args: 9`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1`
* *Architecture:* `concurrency: 17`, `import: 2`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` constants, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/system/src/utils/store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.634)
- **Top Global Matches:** file_cluster_6: 7.634, file_cluster_8: 10.968, file_cluster_4: 14.958
- **Magnitude:** 465.22 | **LOC:** 601 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 1.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateNodeInternals` **(Many-Argument Workhorses)** (Impact: 76.0)
  * `handleExpandParent` **(Many-Argument Workhorses)** (Impact: 51.3)
  * `adoptUserNodes` **(Many-Argument Workhorses)** (Impact: 45.7)
  * `updateChildNode` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* /** * Updates positionAbsolute and zIndex of a child node and the parentLookup. */
  * `parseHandles` **(Defensive Guards)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 57`, `args: 17`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 14`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.678
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.014551
  * `Imports (Out-Degree: 5):` .., types, dom, general, graph, types
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/store/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.179)
- **Top Global Matches:** file_cluster_4: 7.179, file_cluster_15: 11.043, file_cluster_0: 11.697
- **Magnitude:** 422.86 | **LOC:** 420 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 1.814; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (93.2%), Mutation Surface (formerly State Flux) (84.9%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (79.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStore` **(Defensive Guards)** (Impact: 136.8)
  * `updateNodeInternals` **(Defensive Guards)** (Impact: 25.5)
  * `moveSelectedNodes` **(Defensive Guards)** (Impact: 21.5)
  * `handleNodeSelection` **(Defensive Guards)** (Impact: 20.9)
  * `setCenter` **(Defensive Guards)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 60`, `args: 33`, `func_start: 25`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.814
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.002017
  * `Imports (Out-Degree: 3):` types, useStore, initial-store.svelte, types, system
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/xyresizer/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.888)
- **Top Global Matches:** file_cluster_6: 6.888, file_cluster_4: 8.709, file_cluster_15: 15.715
- **Magnitude:** 397.56 | **LOC:** 281 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 1.136; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.4%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDimensionsAfterResize` **(Many-Argument Workhorses)** (Impact: 254.3)
    * *Intent:* * with expandParent or extent: 'parent' set and oh yeah, these things also have to work with keepAsp...
  * `getResizeDirection` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* /** * Get all connecting edges for a given set of nodes */
  * `getControlDirection` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* /** * Parses the control position that is being dragged to dimensions that are being resized */
  * `xor` **(Parameter Forwarders)** (Impact: 3.6)
  * `getSizeClamp` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 16`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006423
  * `Imports (Out-Degree: 3):` types, utils, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/playwright/e2e/nodes.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.23)
- **Top Global Matches:** file_cluster_7: 7.23, file_cluster_12: 8.824, file_cluster_5: 9.79
- **Magnitude:** 392.63 | **LOC:** 289 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.893; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.4%), Guard Balance (formerly Safety Score) (40.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 147`, `args: 28`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 12`
* *Architecture:* `concurrency: 125`, `import: 2`
* *Defense:* `test: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` constants, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/plugins/NodeToolbar/NodeToolbar.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.723)
- **Top Global Matches:** file_cluster_10: 4.723, file_cluster_13: 5.33, file_cluster_2: 5.522
- **Magnitude:** 348.97 | **LOC:** 85 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.273; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.7%), Debt Markers (formerly Tech Debt) (43.5%), Mutation Surface (formerly State Flux) (35.2%), Complexity Load (formerly Cognitive Load) (12.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 23`, `args: 7`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`, `fragile_debt: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.273
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001513
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/xydrag/XYDrag.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.337)
- **Top Global Matches:** file_cluster_3: 10.337, file_cluster_8: 30.493, file_cluster_1: 40.391
- **Magnitude:** 322.06 | **LOC:** 410 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 1.961; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (70.4%), Complexity Load (formerly Cognitive Load) (62.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Compute Cores)** (Impact: 136.1)
    * *Intent:* // public functions
  * `updateNodes` **(Compute Cores)** (Impact: 43.2)
  * `startDrag` **(Defensive Guards)** (Impact: 30.6)
  * `autoPan` **(Defensive Guards)** (Impact: 9.3)
  * `destroy` **(Defensive Guards)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 46`, `args: 16`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 28`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 15`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.961
  * `Choke Point (Betweenness):` 0.000142 | `Ripple Effect (Closeness):` 0.007549
  * `Imports (Out-Degree: 7):` types, utils, utils, d3-drag, d3-selection
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.245)
- **Top Global Matches:** file_cluster_4: 8.245, file_cluster_0: 11.404, file_cluster_15: 11.794
- **Magnitude:** 309.4 | **LOC:** 489 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 5.284; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.9%), Complexity Load (formerly Cognitive Load) (80.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.8%), Concurrency Surface (formerly Concurrency) (66.9%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getInitialStore` **(Defensive Guards)** (Impact: 128.6)
  * `getInitialViewport` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `filter` **(Compute Cores)** (Impact: 5.7)
  * `warnIfDeeplyReactive` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* // Only way to check if an object is a proxy // is to see if it fails to perform a structured clone
  * `resolveFitView` **(I/O & Config Routines)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 76`, `args: 24`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 45`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.284
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.003458
  * `Imports (Out-Degree: 2):` edges, DefaultNode.svelte, GroupNode.svelte, InputNode.svelte, OutputNode.svelte, types, types, visibleElements...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/system/src/xyresizer/XYResizer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.839)
- **Top Global Matches:** file_cluster_8: 7.839, file_cluster_6: 17.514, file_cluster_3: 20.607
- **Magnitude:** 297.34 | **LOC:** 353 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 1.427; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%), Complexity Load (formerly Cognitive Load) (58.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `XYResizer` **(Compute Cores)** (Impact: 95.9)
  * `update` **(Many-Argument Workhorses)** (Impact: 94.7)
  * `nodeToChildExtent` **(Defensive Guards)** (Impact: 6.7)
  * `getStoreItems` **(Callbacks & Closures)** (Impact: 2.4)
  * `nodeToParentExtent` **(Parameter Forwarders)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 38`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 29`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.427
  * `Choke Point (Betweenness):` 0.00014 | `Ripple Effect (Closeness):` 0.007549
  * `Imports (Out-Degree: 5):` types, utils, types, utils, d3-drag, d3-selection
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/utils/general.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.994)
- **Top Global Matches:** file_cluster_4: 8.994, file_cluster_12: 9.243, file_cluster_15: 9.347
- **Magnitude:** 268.84 | **LOC:** 427 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **3**; blast radius 7.184; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.2%), Concurrency Surface (formerly Concurrency) (43.5%), Guard Balance (formerly Safety Score) (37.1%), Mutation Surface (formerly State Flux) (36.1%)
- **Documentation Coverage:** 70.3704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parsePaddings` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* /** * Parses the paddings to an object with top, right, bottom, left, x and y paddings */
  * `getNodeDimensions` **(Defensive Guards)** (Impact: 23.2)
  * `evaluateAbsolutePosition` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* /** * Convert child position to absolute position * */
  * `nodeToRect` **(Defensive Guards)** (Impact: 17.9)
  * `nodeToBox` **(Defensive Guards)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 94`, `args: 35`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`
* *Architecture:* `io: 1`, `api: 26`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 50`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.184
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.025648
  * `Imports (Out-Degree: 3):` constants, types, graph
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `packages/system/src/utils/graph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.248)
- **Top Global Matches:** file_cluster_6: 9.248, file_cluster_4: 11.775, file_cluster_8: 17.589
- **Magnitude:** 259.06 | **LOC:** 526 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **3**; blast radius 4.502; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.5%), Guard Balance (formerly Safety Score) (48.6%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getNodesInside` **(Defensive Guards)** (Impact: 46.1)
  * `calculateNodePosition` **(Defensive Guards)** (Impact: 36.9)
    * *Intent:* /** * This function calculates the next position of a node, taking into account the node's extent, p...
  * `getElementsToRemove` **(Compute Cores)** (Impact: 22.9)
    * *Intent:* /** * Pass in nodes & edges to delete, get arrays of nodes and edges that actually can be deleted */
  * `fitViewport` **(Defensive Guards)** (Impact: 22.4)
  * `getNodesBounds` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* * height: 25, * }, * { * id: 'b', * position: { x: 100, y: 100 }, * data: { label: 'b' }, * width: 5...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 96`, `args: 29`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`
* *Architecture:* `api: 15`, `concurrency: 8`, `import: 4`
* *Defense:* `safety: 28`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.502
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.020052
  * `Imports (Out-Degree: 3):` constants, types, general
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/hooks/useSvelteFlow.svelte.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.352)
- **Top Global Matches:** file_cluster_0: 9.352, file_cluster_4: 9.791, file_cluster_12: 9.884
- **Magnitude:** 244.78 | **LOC:** 578 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.893; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (87.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.6%)
- **Documentation Coverage:** 82.7586% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useSvelteFlow` **(I/O & Config Routines)** (Impact: 28.0)
    * *Intent:* /** * Hook for accessing the SvelteFlow instance. * */
  * `getIntersectingNodes` **(Many-Argument Workhorses)** (Impact: 23.4)
    * *Intent:* /** * Partial is defined as "the 2 nodes/areas are intersecting partially". * If a is contained in b...
  * `fitBounds` **(Defensive Guards)** (Impact: 15.0)
  * `isNodeIntersecting` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `updateNode` **(Generic / Templated Code)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 118`, `args: 63`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 21`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` store, types, utils, system, svelte
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/src/hooks/useReactFlow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.139)
- **Top Global Matches:** file_cluster_4: 9.139, file_cluster_12: 9.472, file_cluster_0: 9.671
- **Magnitude:** 238.44 | **LOC:** 316 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 1.65; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.8%), Connectivity (formerly Api Exposure) (65.0%), Guard Balance (formerly Safety Score) (49.9%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useReactFlow` **(Callbacks & Closures)** (Impact: 62.9)
    * *Intent:* * setCount(reactFlow.getNodes().length); * // you need to pass it as a dependency if you are using i...
  * `getIntersectingNodes` **(Many-Argument Workhorses)** (Impact: 25.4)
    * *Intent:* /** * Partial is defined as "the 2 nodes/areas are intersecting partially". * If a is contained in b...
  * `deleteElements` **(Defensive Guards)** (Impact: 13.4)
  * `isNodeIntersecting` **(Compute Cores)** (Impact: 12.8)
  * `updateNode` **(Callbacks & Closures)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 79`, `args: 40`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 16`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.65
  * `Choke Point (Betweenness):` 0.000181 | `Ripple Effect (Closeness):` 0.008714
  * `Imports (Out-Degree: 6):` BatchProvider, types, utils, useStore, useViewportHelper, system, react
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/react/src/container/Pane/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.134)
- **Top Global Matches:** file_cluster_6: 9.134, file_cluster_8: 11.166, file_cluster_4: 16.072
- **Magnitude:** 227.58 | **LOC:** 293 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 1.016; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Complexity Load (formerly Cognitive Load) (32.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Pane` **(Defensive Guards)** (Impact: 96.5)
  * `onPointerMove` **(Compute Cores)** (Impact: 30.9)
  * `onPointerDownCapture` **(Defensive Guards)** (Impact: 21.6)
    * *Intent:* // We are using capture here in order to prevent other pointer events // to be able to create a sele...
  * `onPointerUp` **(Defensive Guards)** (Impact: 15.5)
  * `onContextMenu` **(Defensive Guards)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 42`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.016
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.004118
  * `Imports (Out-Degree: 6):` UserSelection, useStore, utils, types, utils, system, classcat, react...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react/src/store/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.76)
- **Top Global Matches:** file_cluster_4: 7.76, file_cluster_10: 8.68, file_cluster_15: 8.998
- **Magnitude:** 209.62 | **LOC:** 455 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 10.431; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (73.2%), Guard Balance (formerly Safety Score) (47.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateNodePositions` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `createStore` **(Compute Cores)** (Impact: 21.3)
  * `setCenter` **(Defensive Guards)** (Impact: 15.0)
  * `updateNodeInternals` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* /* * Every node gets registered at a ResizeObserver. Whenever a node * changes its dimensions, this ...
  * `unselectNodesAndEdges` **(Compute Cores)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 48`, `args: 27`, `func_start: 22`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 13`
* *Architecture:* `api: 1`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 19`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.431
  * `Choke Point (Betweenness):` 0.00032 | `Ripple Effect (Closeness):` 0.03687
  * `Imports (Out-Degree: 3):` types, changes, initialState, system, traditional
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/system/src/xyhandle/XYHandle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.794)
- **Top Global Matches:** file_cluster_8: 5.794, file_cluster_6: 12.766, file_cluster_4: 21.461
- **Magnitude:** 204.28 | **LOC:** 324 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 1.961; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%), Concurrency Surface (formerly Concurrency) (42.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onPointerDown` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `isValidHandle` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* // checks if and returns connection in form of an object { source: 123, target: 312 }
  * `onPointerMove` **(Compute Cores)** (Impact: 22.0)
  * `onPointerUp` **(Defensive Guards)** (Impact: 20.5)
  * `autoPan` **(Interface Declarations)** (Impact: 3.5)
    * *Intent:* // when the user is moving the mouse close to the edge of the canvas while connecting we move the ca...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 19`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 9`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.961
  * `Choke Point (Betweenness):` 0.000197 | `Ripple Effect (Closeness):` 0.007549
  * `Imports (Out-Degree: 8):` types, utils, types, utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/xypanzoom/XYPanZoom.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.11)
- **Top Global Matches:** file_cluster_4: 8.11, file_cluster_9: 11.506, file_cluster_12: 11.533
- **Magnitude:** 202.78 | **LOC:** 302 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 2.165; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (90.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (44.8%), Connectivity (formerly Api Exposure) (24.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `XYPanZoom` **(Defensive Guards)** (Impact: 79.8)
  * `update` **(I/O & Config Routines)** (Impact: 22.4)
    * *Intent:* // public functions
  * `setTransform` **(Defensive Guards)** (Impact: 14.5)
  * `scaleTo` **(Defensive Guards)** (Impact: 14.5)
  * `scaleBy` **(Defensive Guards)** (Impact: 14.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 35`, `args: 21`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 2`, `concurrency: 15`, `import: 9`
* *Defense:* `safety: 17`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.165
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.007873
  * `Imports (Out-Degree: 6):` types, utils, eventhandler, filter, utils, d3-interpolate, d3-selection, d3-transition...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/components/ConnectionLine/ConnectionLine.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.103)
- **Top Global Matches:** file_cluster_13: 4.103, file_cluster_2: 4.138, file_cluster_10: 5.276
- **Magnitude:** 194.0 | **LOC:** 79 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.653; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.5%), Mutation Surface (formerly State Flux) (15.0%), Complexity Load (formerly Cognitive Load) (9.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001513
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/container/Zoom/Zoom.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.604)
- **Top Global Matches:** file_cluster_2: 3.604, file_cluster_13: 4.17, file_cluster_10: 4.743
- **Magnitude:** 189.45 | **LOC:** 82 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.653; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.1%), Mutation Surface (formerly State Flux) (44.1%), Complexity Load (formerly Cognitive Load) (10.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001513
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react/src/utils/changes.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.113)
- **Top Global Matches:** file_cluster_4: 12.113, file_cluster_5: 12.518, file_cluster_7: 13.487
- **Magnitude:** 178.18 | **LOC:** 325 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 5.425; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.7%), Complexity Load (formerly Cognitive Load) (54.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyChanges` **(Many-Argument Workhorses)** (Impact: 33.7)
    * *Intent:* /* * This function applies changes to nodes or edges that are triggered by React Flow internally. * ...
  * `applyChange` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // Applies a single change to an element. This is a *mutable* update.
  * `getElementsDiffChanges` **(Defensive Guards)** (Impact: 15.8)
  * `getSelectionChanges` **(Many-Argument Workhorses)** (Impact: 13.3)
  * `createSelectionChange` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 41`, `args: 12`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 22`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 3`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.425
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.033129
  * `Imports (Out-Degree: 1):` types, system
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/react/src/hooks/useVisibleNodeIds.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 7, import: 5, args: 4
- `packages/react/src/components/NodesSelection/index.tsx` (TYPESCRIPT) | Magnitude: 30.4 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 27, core_var_decl: 16, branch: 14
- `packages/react/src/components/ReactFlowProvider/index.tsx` (TYPESCRIPT) | Magnitude: 6.62 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, branch: 13, structural_boundaries: 13, doc: 13
- `examples/react/cypress/components/reactflow/storeAvailabilityOnRemount.cy.tsx` (TYPESCRIPT) | Magnitude: 13.84 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 30, ui_framework: 21, core_var_decl: 21
- `examples/react/src/examples/CustomMiniMapNode/index.tsx` (TYPESCRIPT) | Magnitude: 13.62 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 65, core_var_decl: 26, structural_boundaries: 24, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `examples/react/cypress/components/reactflow/uncontrolled.cy.tsx` (TYPESCRIPT) | Magnitude: 15.56 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 13, args: 7, test: 7
- `examples/react/cypress/components/reactflow/on-nodes-change.cy.tsx` (TYPESCRIPT) | Magnitude: 8.46 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 27, core_var_decl: 17, args: 16
- `examples/react/src/examples/FloatingEdges/index.tsx` (TYPESCRIPT) | Magnitude: 5.6 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 12, core_var_decl: 12, design_camel_case: 9
- `packages/react/src/components/Edges/StepEdge.tsx` (TYPESCRIPT) | Magnitude: 9.96 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, ui_framework: 5, core_var_decl: 5
- `examples/react/src/examples/FloatingEdges/FloatingEdge.tsx` (TYPESCRIPT) | Magnitude: 7.26 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 8, io: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `examples/react/src/examples/EdgeToolbar/CustomEdge.tsx` (TYPESCRIPT) | Magnitude: 21.62 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 12, branch: 10, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/svelte/src/lib/components/ConnectionLine/ConnectionLine.svelte` (HTML) | Magnitude: 194.0 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 11, branch: 10, core_var_decl: 10
- `examples/svelte/src/routes/examples/usenodesdata/+page.svelte` (HTML) | Magnitude: 9.48 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 78, structural_boundaries: 11, core_var_decl: 10, decorators: 5
- `packages/svelte/src/lib/plugins/Background/LinePattern.svelte` (HTML) | Magnitude: 30.4 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, core_var_decl: 3, design_snake_case: 3
- `packages/svelte/src/lib/container/EdgeRenderer/MarkerDefinition/MarkerDefinition.svelte` (HTML) | Magnitude: 15.2 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 2, import: 2, core_var_decl: 2
- `packages/svelte/src/lib/plugins/EdgeToolbar/EdgeToolbar.svelte` (HTML) | Magnitude: 62.19 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, core_var_decl: 9, structural_boundaries: 8, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `examples/react/src/examples/EasyConnect/FloatingEdge.tsx` (TYPESCRIPT) | Magnitude: 6.56 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 5, branch: 3, core_var_decl: 3
- `packages/react/src/container/EdgeRenderer/MarkerDefinitions.tsx` (TYPESCRIPT) | Magnitude: 17.5 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 62, core_var_decl: 32, structural_boundaries: 22, design_snake_case: 16
- `packages/react/src/hooks/useNodesInitialized.ts` (TYPESCRIPT) | Magnitude: 13.76 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 14, branch: 6, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/system/src/types/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/svelte/src/lib/components/edges/index.ts` (TYPESCRIPT) | Magnitude: 23.68 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 9, structural_boundaries: 9, api: 9, import: 9
- `packages/system/src/index.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/svelte/src/lib/plugins/NodeResizer/NodeResizer.svelte` (HTML) | Magnitude: 15.84 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, core_var_decl: 9, decorators: 6, design_snake_case: 6
- `packages/react/src/components/Edges/SimpleBezierEdge.tsx` (TYPESCRIPT) | Magnitude: 20.42 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 101, core_var_decl: 19, structural_boundaries: 16, design_camel_case: 12
- `examples/react/src/examples/Validation/ConnectionStatus.tsx` (TYPESCRIPT) | Magnitude: 14.08 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 12, branch: 7, safety: 4
- `packages/react/src/components/Edges/SmoothStepEdge.tsx` (TYPESCRIPT) | Magnitude: 14.28 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, core_var_decl: 19, design_camel_case: 12, structural_boundaries: 9
- `examples/svelte/src/routes/examples/a11y/+page.svelte` (HTML) | Magnitude: 42.14 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 53, core_var_decl: 10, design_snake_case: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/svelte/src/lib/container/Pane/Pane.svelte` (HTML) | Magnitude: 150.3 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 198, branch: 60, core_var_decl: 40, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/react/src/additional-components/Background/Background.tsx` (TYPESCRIPT) | Magnitude: 24.84 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 66, core_var_decl: 29, design_snake_case: 16, structural_boundaries: 13
- `packages/react/src/additional-components/EdgeToolbar/EdgeToolbar.tsx` (TYPESCRIPT) | Magnitude: 17.0 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 14, core_var_decl: 11, import: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react/src/store/index.ts` -> Churn: **100.0%** | Cog Load: 21.3054% | Debt: 73.1853%
- `packages/system/src/utils/store.ts` -> Churn: **84.51%** | Cog Load: 54.9873% | Debt: 0.0%
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> Churn: **77.82%** | Cog Load: 80.7733% | Debt: 0.0%
- `packages/react/src/components/SelectionListener/index.tsx` -> Churn: **54.75%** | Cog Load: 22.0296% | Debt: 86.1395%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/system/src/utils/general.ts` -> **Yaroslav Halchenko** (100.0% isolated ownership) | Magnitude: 268.84
- `packages/react/src/utils/changes.ts` -> **moklick** (100.0% isolated ownership) | Magnitude: 178.18
- `tests/playwright/e2e/edges.spec.ts` -> **Yaroslav Halchenko** (100.0% isolated ownership) | Magnitude: 177.11
- `packages/react/src/components/Handle/index.tsx` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 177.0
- `packages/system/src/xypanzoom/eventhandler.ts` -> **Yaroslav Halchenko** (100.0% isolated ownership) | Magnitude: 150.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/system/src/utils/node-toolbar.ts` -> **Severity: 0.057** (Bridge: 0.0006 * Flux: 100.0%)
- `packages/system/src/utils/edges/general.ts` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 82.5414%)
- `packages/system/src/xyhandle/XYHandle.ts` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 96.9785%)
- `packages/system/src/xydrag/XYDrag.ts` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.8633%)
- `packages/system/src/xyresizer/XYResizer.ts` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.9903%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/react/src/types/general.ts` -> **Severity: 3.625** (Embedded: 0.0666 * Error Risk: 54.3902%)
- `packages/react/src/types/nodes.ts` -> **Severity: 3.561** (Embedded: 0.0665 * Error Risk: 53.5384%)
- `packages/react/src/types/edges.ts` -> **Severity: 3.331** (Embedded: 0.0653 * Error Risk: 51.02%)
- `packages/react/src/utils/changes.ts` -> **Severity: 2.474** (Embedded: 0.0331 * Error Risk: 74.6927%)
- `packages/react/src/store/index.ts` -> **Severity: 1.762** (Embedded: 0.0369 * Error Risk: 47.8019%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/react/src/store/index.ts` -> **Severity: 1043.1** (Blast Radius: 10.431 * Doc Risk: 100.0%)
- `packages/system/src/utils/general.ts` -> **Severity: 505.541** (Blast Radius: 7.184 * Doc Risk: 70.3704%)
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> **Severity: 495.375** (Blast Radius: 5.284 * Doc Risk: 93.75%)
- `packages/system/src/constants.ts` -> **Severity: 475.5** (Blast Radius: 4.755 * Doc Risk: 100.0%)
- `packages/svelte/src/lib/store/types.ts` -> **Severity: 457.4** (Blast Radius: 4.574 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 200 literal sites + 2 sites through wrappers = 202

- `onBeforeDelete` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/react/src/examples/Overview/index.tsx`
- `onSelectionContextMenu` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/react/src/examples/Overview/index.tsx`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2500 call pairs -- scoped 16.9%, unique 0.0%, ambiguous 20.7%, external 62.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 2358 | 17.7% | 0.0% | 22.0% | 60.3% |
| html | 135 | 4.4% | 0.0% | 0.0% | 95.6% |
| javascript | 7 | 0.0% | 0.0% | 0.0% | 100.0% |

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
