# ARCHITECTURAL_BRIEF: ant-design
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ant-design/ant-design.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 3948 analyzed artifact(s), 201582 LOC.
- **Load-bearing artifact:** `tests/utils.tsx` -- 252 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `components/locale/__tests__/index.test.tsx` -- pulls in 146 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 4763 |
| Analyzed Artifacts (Scanned) | 3948 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 815 |
| Total LOC | 201582 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 82.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7321 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2864 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7899 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 101 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2737 | 200020 | 69.3% |
| MARKDOWN | 1183 | 0 | 30.0% |
| JAVASCRIPT | 10 | 673 | 0.3% |
| JSON | 9 | 402 | 0.2% |
| HTML | 3 | 136 | 0.1% |
| PLAINTEXT | 2 | 1 | 0.1% |
| SHELL | 2 | 100 | 0.1% |
| YAML | 1 | 6 | 0.0% |
| CSS | 1 | 244 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.203`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.20; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Callbacks & Closures Files 17%, Generic / Templated Code Files 14%, Declarative / Non-Code 10%, Large Core Modules 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2763 | 70.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1184 | 30.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 815*

**Composition by Extension & Reason:**
- `.snap`: 307x Excluded (Unsupported Extension: '.snap'), 1x Unsupported Format (.snap)
- `.md`: 221x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 137 LOC)
- `.tsx`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 10 exceeds 500 chars), 1x Excluded (Saturation: Line 38 exceeds 500 chars)
- `.ts`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Packed Payload Guard (Impossible Density: 3.09 hits/line)
- `.yml`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1836 LOC)
- `.less`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.7 | 7.3 | 5.1 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.9 | 15.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.7 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 43.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.9 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 65.2 | 4.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.9 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1322 | 600 | 1 | `components/theme/interface/components.ts` |
| cleanup | 97 | 60 | 0 | `components/message/__tests__/index.test.tsx` |
| guards | 3694 | 702 | 2 | `components/form/__tests__/index.test.tsx` |
| danger | 2533 | 446 | 1 | `components/table/__tests__/Table.filter.test.tsx` |
| concurrency | 2101 | 207 | 0 | `components/modal/__tests__/confirm.test.tsx` |
| connectivity | 4103 | 2104 | 2 | `components/config-provider/context.ts` |
| io | 1039 | 238 | 0 | `components/upload/__tests__/uploadlist.test.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 8 | 5 | 0 | `tests/setup.ts` |
| time | 177 | 87 | 0 | `.dumi/scripts/mirror-notify.js` |
| serialization | 29 | 20 | 0 | `components/_util/__tests__/hooks.test.tsx` |
| regex | 117 | 60 | 0 | `scripts/generate-component-changelog.ts` |
| events | 255 | 95 | 0 | `eslint.config.mjs` |
| tests | 10895 | 390 | 0 | `components/form/__tests__/index.test.tsx` |
| docs | 1578 | 295 | 0 | `components/theme/interface/alias.ts` |
| debt | 664 | 325 | 0 | `components/upload/__tests__/uploadlist.test.tsx` |
| mutation | 32915 | 2225 | 22 | `components/form/__tests__/index.test.tsx` |
| dead_code | 1304 | 1084 | 1 | `components/form/__tests__/index.test.tsx` |
| credential | 79 | 34 | 0 | `components/upload/__tests__/uploadlist.test.tsx` |
| threat | 87 | 38 | 0 | `components/avatar/__tests__/Avatar.test.tsx` |
| ml_ai | 169 | 68 | 0 | `components/watermark/useClips.ts` |
| ui | 17382 | 1757 | 11 | `components/form/__tests__/index.test.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `components/upload/__tests__/uploadlist.test.tsx` (Hits: 65)
- `components/result/serverError.tsx` (Hits: 59)
- `components/result/unauthorized.tsx` (Hits: 52)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utils.tsx** (`tests/utils.tsx`) — 252 inbound connections
2. **demoTest.tsx** (`tests/shared/demoTest.tsx`) — 197 inbound connections
3. **internal.ts** (`components/theme/internal.ts`) — 178 inbound connections
4. **cssinjs.js** (`alias/cssinjs.js`) — 177 inbound connections
5. **warning.ts** (`components/_util/warning.ts`) — 129 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.test.tsx** (`components/locale/__tests__/index.test.tsx`) — 146 outbound dependencies
2. **context.ts** (`components/config-provider/context.ts`) — 70 outbound dependencies
3. **components.ts** (`components/theme/interface/components.ts`) — 67 outbound dependencies
4. **style.test.tsx** (`components/config-provider/__tests__/style.test.tsx`) — 63 outbound dependencies
5. **index.en-US.md** (`components/config-provider/index.en-US.md`) — 61 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `defaultSearchRender` **(Many-Argument Workhorses)** (@ `components/cascader/index.tsx`) -> Impact: **151.9** | LOC: 399
- `copyTest` **(Many-Argument Workhorses)** (@ `components/typography/__tests__/index.test.tsx`) -> Impact: **126.7** | LOC: 99
  * *Intent:* /** */
- `InternalFormItem` **(Compute Cores)** (@ `components/form/FormItem/index.tsx`) -> Impact: **125.4** | LOC: 331
- `useResize` **(Many-Argument Workhorses)** (@ `components/splitter/hooks/useResize.ts`) -> Impact: **106.1** | LOC: 164
  * *Intent:* /** * Handle user drag resize logic. */
- `onEdit` **(Defensive Guards)** (@ `components/tabs/index.tsx`) -> Impact: **105.9** | LOC: 143
- `InternalSelect` **(Many-Argument Workhorses)** (@ `components/select/index.tsx`) -> Impact: **102.9** | LOC: 325
- `renderInternalItem` **(Many-Argument Workhorses)** (@ `components/list/index.tsx`) -> Impact: **93.7** | LOC: 211
- `ProviderChildren` **(Many-Argument Workhorses)** (@ `components/config-provider/index.tsx`) -> Impact: **93.5** | LOC: 400
- `getSize` **(Defensive Guards)** (@ `components/progress/utils.ts`) -> Impact: **88.5** | LOC: 50
- `useItems` **(Many-Argument Workhorses)** (@ `components/timeline/useItems.tsx`) -> Impact: **83.7** | LOC: 91

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 24 | 5323.28 | 4.26% | 2.96% |
| `components/table/__tests__` | 18 | 1486.95 | 3.26% | 0.0% |
| `components/input/__tests__` | 13 | 1090.6 | 2.56% | 0.0% |
| `scripts` | 18 | 1076.19 | 40.29% | 22.59% |
| `components/table/demo` | 101 | 1063.6 | 3.17% | 17.19% |
| `components/message/__tests__` | 13 | 982.22 | 20.55% | 0.0% |
| `components/_util` | 32 | 851.12 | 15.47% | 0.0% |
| `components/float-button/__tests__` | 9 | 850.07 | 1.23% | 0.0% |
| `components/table/hooks` | 6 | 828.7 | 23.24% | 1.41% |
| `components/modal/__tests__` | 11 | 763.52 | 10.9% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `components/modal/demo/confirm.tsx` -> **100.0%** Exposure
- `components/upload/demo/upload-custom-action-icon.tsx` -> **100.0%** Exposure
- `components/upload/demo/component-token.tsx` -> **99.9998%** Exposure
- `components/upload/demo/defaultFileList.tsx` -> **99.9998%** Exposure
- `components/upload/demo/picture-circle.tsx` -> **99.998%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.dumi/theme/utils/index.ts` -> **100.0%** Exposure
- `components/_util/ActionButton.tsx` -> **100.0%** Exposure
- `components/_util/ContextIsolator.tsx` -> **100.0%** Exposure
- `components/_util/__tests__/easings.test.ts` -> **100.0%** Exposure
- `components/_util/__tests__/getScroll.test.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `components/table/__tests__/Table.sorter.test.tsx` -> **5** Orphaned Functions | **8** Duplicates
- `components/table/__tests__/Table.rowSelection.test.tsx` -> **5** Orphaned Functions | **7** Duplicates
- `components/table/__tests__/Table.filter.test.tsx` -> **3** Orphaned Functions | **6** Duplicates
- `components/form/__tests__/index.test.tsx` -> **8** Orphaned Functions | **0** Duplicates
- `components/modal/demo/confirm.tsx` -> **0** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `35` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5272` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/input/__tests__/Password.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 722.8 | **LOC:** 170 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (37.5%), Complexity Load (formerly Cognitive Load) (7.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 35`, `args: 17`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 21`
* *Architecture:* `concurrency: 11`, `import: 9`
* *Defense:* `safety: 16`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .., focusTest, mountTest, rtlTest, utils, Password, icons, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/float-button/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 681.75 | **LOC:** 122 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (66.1%), Guard Balance (formerly Safety Score) (7.9%), Complexity Load (formerly Cognitive Load) (5.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (4.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 32`, `args: 16`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 1`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 15`, `test: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .., mountTest, rtlTest, utils, util, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/form/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 505.74 | **LOC:** 2634 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.5%), Guard Balance (formerly Safety Score) (29.9%), Mutation Surface (formerly State Flux) (17.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `App` **(Defensive Guards)** (Impact: 17.8)
    * *Intent:* // base size
  * `App` **(Defensive Guards)** (Impact: 15.4)
    * *Intent:* // base size
  * `validator` **(Defensive Guards)** (Impact: 10.1)
  * `App` **(Generic / Templated Code)** (Impact: 8.8)
  * `changeValue` **(Callbacks & Closures)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 208
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 395`, `args: 215`, `func_start: 102`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 1`, `state_mutation: 27`, `dead_code: 3`, `unreferenced_by_name: 8`
* *Architecture:* `io: 3`, `concurrency: 138`, `import: 35`
* *Defense:* `safety: 112`, `test: 337`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .., mountTest, rtlTest, utils, responsiveObserver, warning, button, cascader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/__tests__/Table.filter.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 447.36 | **LOC:** 3162 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.0%), Concurrency Surface (formerly Concurrency) (27.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.6%), Mutation Surface (formerly State Flux) (12.2%)
- **Documentation Coverage:** 98.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `filterSearch` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `sorter` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `onFilter` **(Defensive Guards)** (Impact: 20.8)
  * `onFilter` **(I/O & Config Routines)** (Impact: 20.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 301`, `args: 239`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 224`, `state_mutation: 14`, `duplicate_logic: 6`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 20`, `import: 13`
* *Defense:* `safety: 88`, `doc: 1`, `test: 315`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .., utils, warning, button, config-provider, input, menu, select...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useSelection.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 369.5 | **LOC:** 757 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 55.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.9%), Connectivity (formerly Api Exposure) (41.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useSelection` **(Many-Argument Workhorses)** (Impact: 68.5)
  * `renderCell` **(Many-Argument Workhorses)** (Impact: 48.8)
  * `renderSelectionCell` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `onClick` **(Defensive Guards)** (Impact: 23.6)
  * `renderCell` **(Defensive Guards)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 129`, `args: 62`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 35`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 19`
* *Defense:* `safety: 33`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hooks, type, warning, checkbox, dropdown, radio, interface, DownOutlined...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/modal/__tests__/confirm.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 330.14 | **LOC:** 1112 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (41.8%), Guard Balance (formerly Safety Score) (38.6%), Mutation Surface (formerly State Flux) (24.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockActionFn` **(Defensive Guards)** (Impact: 8.0)
  * `error` **(Callbacks & Closures)** (Impact: 5.8)
  * `open` **(Compute Cores)** (Impact: 4.7)
  * `configWarp` **(Callbacks & Closures)** (Impact: 4.1)
  * `holderRender` **(Defensive Guards)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 214
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 304`, `args: 132`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 7`, `state_mutation: 17`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 149`, `import: 11`
* *Defense:* `safety: 21`, `test: 192`, `immutability_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., utils, app, config-provider, confirm, destroyFns, icons, util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/message/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 315.94 | **LOC:** 251 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (28.9%), Guard Balance (formerly Safety Score) (23.1%), Mutation Surface (formerly State Flux) (16.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 67`, `args: 32`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `concurrency: 47`, `import: 5`
* *Defense:* `test: 48`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., utils, util, icons, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useSorter.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 303.16 | **LOC:** 524 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.182; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.2%), Connectivity (formerly Api Exposure) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `injectSorter` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `getSortData` **(Generic / Templated Code)** (Impact: 28.5)
  * `onKeyDown` **(Defensive Guards)** (Impact: 19.7)
  * `pushState` **(Generic / Templated Code)** (Impact: 19.5)
  * `title` **(Generic / Templated Code)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 98`, `args: 36`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.182
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000887
  * `Imports (Out-Degree: 1):` type, locale, tooltip, interface, util, CaretDownOutlined, CaretUpOutlined, KeyCode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/table/InternalTable.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 298.84 | **LOC:** 772 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 47.6%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **36**; blast radius 0.451; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.7%), Connectivity (formerly Api Exposure) (59.0%), Guard Balance (formerly Safety Score) (58.5%)
- **Documentation Coverage:** 39.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InternalTable` **(Many-Argument Workhorses)** (Impact: 55.7)
  * `normalizePlacement` **(Compute Cores)** (Impact: 55.5)
  * `internalRowClassName` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `triggerOnChange` **(Defensive Guards)** (Impact: 23.3)
  * `onPaginationChange` **(Defensive Guards)** (Impact: 20.7)
    * *Intent:* // ========================== Pagination ==========================
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 146`, `args: 37`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`
* *Architecture:* `api: 17`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 29`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.451
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.001303
  * `Imports (Out-Degree: 20):` hooks, responsiveObserver, scrollTo, type, warning, config-provider, SizeContext, context...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scripts/visual-regression/build.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 297.2 | **LOC:** 566 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.398; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.4%), Guard Balance (formerly Safety Score) (71.5%), Complexity Load (formerly Cognitive Load) (63.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateReport` **(Many-Argument Workhorses)** (Impact: 48.1)
  * `generateLineReport` **(Many-Argument Workhorses)** (Impact: 34.7)
  * `boot` **(I/O & Config Routines)** (Impact: 27.4)
  * `compareScreenshots` **(Many-Argument Workhorses)** (Impact: 10.8)
  * `getMdImageTag` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 100`, `args: 23`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 26`, `dead_code: 1`
* *Architecture:* `io: 37`, `api: 1`, `concurrency: 44`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.398
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000253
  * `Imports (Out-Degree: 3):` convert, reportAdapter, core, chalk, fs-extra, difference, filter, minimist...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/table/__tests__/Table.rowSelection.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 294.72 | **LOC:** 2148 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (42.8%), Mutation Surface (formerly State Flux) (30.1%), Concurrency Surface (formerly Concurrency) (24.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `allElement` **(I/O & Config Routines)** (Impact: 12.3)
  * `getIndeterminateSelection` **(Callbacks & Closures)** (Impact: 11.4)
  * `renderedNames` **(Defensive Guards)** (Impact: 10.4)
  * `getCheckboxProps` **(Defensive Guards)** (Impact: 10.4)
  * `onRow` **(I/O & Config Routines)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 214`, `args: 154`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 37`, `duplicate_logic: 7`, `unreferenced_by_name: 5`
* *Architecture:* `concurrency: 6`, `import: 7`
* *Defense:* `safety: 38`, `test: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., utils, warning, config-provider, interface, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/__tests__/Table.sorter.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 280.22 | **LOC:** 1338 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (37.3%), Mutation Surface (formerly State Flux) (15.2%), Complexity Load (formerly Cognitive Load) (4.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare` **(Defensive Guards)** (Impact: 26.0)
  * `getNameColumn` **(Defensive Guards)** (Impact: 23.1)
  * `getIcon` **(Defensive Guards)** (Impact: 20.6)
  * `getIcon` **(Defensive Guards)** (Impact: 20.4)
  * `sorter` **(Many-Argument Workhorses)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 120`, `args: 104`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 8`, `duplicate_logic: 8`, `unreferenced_by_name: 5`
* *Architecture:* `import: 5`
* *Defense:* `safety: 98`, `test: 210`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., utils, interface, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/shared/imageTest.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 271.5 | **LOC:** 357 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **66** in-repo importer(s); it depends on **16**; blast radius 9.306; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (88.5%), Connectivity (formerly Api Exposure) (80.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `imageTest` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* // eslint-disable-next-line jest/no-export
  * `requestListener` **(Compute Cores)** (Impact: 40.3)
  * `imageDemoTest` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* // eslint-disable-next-line jest/no-export
  * `getTestOption` **(Callbacks & Closures)** (Impact: 17.8)
  * `onRequestHandle` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 79`, `args: 43`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 19`
* *Architecture:* `io: 15`, `api: 12`, `concurrency: 23`, `import: 16`
* *Defense:* `safety: 5`, `doc: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.306
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.016717
  * `Imports (Out-Degree: 3):` components, setup, utils, demoTestContext, cssinjs, util, antd-style, dayjs...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `components/form/FormItem/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 270.16 | **LOC:** 459 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.0%), Guard Balance (formerly Safety Score) (81.5%), Connectivity (formerly Api Exposure) (56.7%), Complexity Load (formerly Cognitive Load) (37.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InternalFormItem` **(Compute Cores)** (Impact: 125.4)
  * `[eventName]` **(Defensive Guards)** (Impact: 19.4)
  * `onMetaChange` **(Compute Cores)** (Impact: 17.0)
  * `renderLayout` **(Many-Argument Workhorses)** (Impact: 12.1)
    * *Intent:* // ======================== Render ========================
  * `onSubItemMetaChange` **(Callbacks & Closures)** (Impact: 10.6)
    * *Intent:* // >>>>> Collect noStyle Field error to the top FormItem
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 79`, `args: 20`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 22`
* *Architecture:* `io: 2`, `api: 5`, `import: 26`
* *Defense:* `safety: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` isNonNullable, reactNode, warning, config-provider, useCSSVarCls, Form, FormItemInput, FormItemLabel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/print-changelog.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 267.7 | **LOC:** 392 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (85.5%), Guard Balance (formerly Safety Score) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printLog` **(I/O & Config Routines)** (Impact: 66.8)
  * `validate` **(Defensive Guards)** (Impact: 25.3)
  * `validate` **(Compute Cores)** (Impact: 13.6)
  * `printPR` **(Compute Cores)** (Impact: 13.5)
  * `fetchPullRequest` **(Callbacks & Closures)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 60`, `args: 29`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 20`, `concurrency: 17`, `import: 10`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` prompts, chalk, fs-extra, isomorphic-fetch, jquery, jsdom, node:child_process, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.dumi/theme/utils/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 263.26 | **LOC:** 217 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.4%), Complexity Load (formerly Cognitive Load) (84.0%), Connectivity (formerly Api Exposure) (74.9%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMenuItems` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `sortFn` **(Defensive Guards)** (Impact: 44.9)
  * `getLocalizedPathname` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `getMetaDescription` **(Callbacks & Closures)** (Impact: 11.1)
  * `matchDeprecated` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 80`, `args: 23`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 28`
* *Architecture:* `io: 5`, `api: 7`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BUG_VERSIONS.json, flatten, flattenDeep, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useFilter/FilterDropdown.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 240.46 | **LOC:** 592 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.209; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (58.4%), Guard Balance (formerly Safety Score) (51.1%), Connectivity (formerly Api Exposure) (41.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFilterComponent` **(I/O & Config Routines)** (Impact: 22.6)
  * `renderFilterItems` **(Compute Cores)** (Impact: 15.4)
  * `onVisibleChange` **(Compute Cores)** (Impact: 14.9)
  * `triggerVisible` **(Defensive Guards)** (Impact: 14.6)
  * `internalTriggerFilter` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* // ======================= Submit ========================
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 107`, `args: 37`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `api: 9`, `import: 27`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.209
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000253
  * `Imports (Out-Degree: 10):` , extendsObject, hooks, warning, Button, checkbox, context, dropdown...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/typography/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 236.98 | **LOC:** 552 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (52.3%), Guard Balance (formerly Safety Score) (45.3%), Mutation Surface (formerly State Flux) (25.9%), Complexity Load (formerly Cognitive Load) (9.2%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyTest` **(Many-Argument Workhorses)** (Impact: 126.7)
    * *Intent:* /** */
  * `testStep` **(Many-Argument Workhorses)** (Impact: 65.3)
  * `getComputedStyle` **(Callbacks & Closures)** (Impact: 4.4)
  * `DynamicPropsTestCase` **(Callbacks & Closures)** (Impact: 3.7)
  * `fn` **(Type Conversions)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 82`, `args: 46`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 8`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 11`, `import: 15`
* *Defense:* `safety: 16`, `doc: 1`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` mountTest, rtlTest, utils, copy, Base, Link, Paragraph, Text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/typography/__tests__/ellipsis.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 236.26 | **LOC:** 736 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (74.9%), Guard Balance (formerly Safety Score) (64.5%), Complexity Load (formerly Cognitive Load) (29.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `symbol` **(Defensive Guards)** (Impact: 8.2)
  * `getContentHeight` **(Compute Cores)** (Impact: 7.3)
  * `getTooltipContent` **(Callbacks & Closures)** (Impact: 5.3)
  * `App` **(I/O & Config Routines)** (Impact: 4.2)
  * `get` **(Callbacks & Closures)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 124
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 131`, `args: 68`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 28`, `unreferenced_by_name: 5`
* *Architecture:* `concurrency: 59`, `import: 8`
* *Defense:* `safety: 47`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utils, config-provider, zh_CN, Base, domHook, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/splitter/hooks/useResize.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 234.32 | **LOC:** 174 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.195; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useResize` **(Many-Argument Workhorses)** (Impact: 106.1)
    * *Intent:* /** * Handle user drag resize logic. */
  * `onOffsetUpdate` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `onCollapse` **(Compute Cores)** (Impact: 30.4)
    * *Intent:* // ======================= Collapse =======================
  * `getLimitSize` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* // ======================== Resize ========================
  * `onOffsetStart` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 25`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 5`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.195
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000338
  * `Imports (Out-Degree: 2):` useItems, useResizable, useSizes, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/upload/Upload.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 220.8 | **LOC:** 548 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 0.558; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.2%), Connectivity (formerly Api Exposure) (36.3%)
- **Documentation Coverage:** 45.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InternalUpload` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `onInternalChange` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `renderUploadList` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `onFileDrop` **(I/O & Config Routines)** (Impact: 14.9)
  * `handleRemove` **(Defensive Guards)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 77`, `args: 26`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 28`, `fragile_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 16`
* *Defense:* `safety: 10`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.558
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.00076
  * `Imports (Out-Degree: 4):` hooks, warning, DisabledContext, context, locale, en_US, UploadList, interface...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/transfer/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 217.4 | **LOC:** 617 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 70.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (93.3%), Guard Balance (formerly Safety Score) (57.0%), Mutation Surface (formerly State Flux) (46.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLocale` **(I/O & Config Routines)** (Impact: 27.3)
  * `Transfer` **(Compute Cores)** (Impact: 21.2)
  * `onItemSelect` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `setPrevSelectedIndex` **(Defensive Guards)** (Impact: 11.4)
  * `onItemSelectAll` **(Many-Argument Workhorses)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 129`, `args: 48`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`
* *Architecture:* `api: 21`, `import: 27`
* *Defense:* `safety: 18`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` hooks, statusUtils, transKeys, warning, DisabledContext, context, defaultRenderEmpty, context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/cascader/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 214.7 | **LOC:** 514 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 63.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (82.0%), Mutation Surface (formerly State Flux) (74.0%), Guard Balance (formerly Safety Score) (62.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defaultSearchRender` **(Many-Argument Workhorses)** (Impact: 151.9)
  * `highlightKeyword` **(Many-Argument Workhorses)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 110`, `args: 19`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`
* *Architecture:* `io: 2`, `api: 13`, `import: 36`
* *Defense:* `safety: 8`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` PurePanel, hooks, motion, statusUtils, warning, config-provider, DisabledContext, SizeContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/upload/__tests__/upload.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 212.22 | **LOC:** 1205 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (38.5%), Mutation Surface (formerly State Flux) (18.2%), Complexity Load (formerly Cognitive Load) (15.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onChange` **(Compute Cores)** (Impact: 15.2)
  * `onChange` **(I/O & Config Routines)** (Impact: 12.6)
  * `onChange` **(Callbacks & Closures)** (Impact: 7.5)
  * `onChange` **(Callbacks & Closures)** (Impact: 4.7)
  * `onChange` **(Generic / Templated Code)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 99
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 212`, `args: 107`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 10`, `fragile_debt: 7`, `duplicate_logic: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 21`, `concurrency: 69`, `import: 14`
* *Defense:* `safety: 34`, `test: 138`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .., mountTest, rtlTest, utils, warning, config-provider, form, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `eslint.config.mjs` -> Churn: **65.18%** | Cog Load: 3.2425% | Debt: 71.1436%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `components/float-button/__tests__/index.test.tsx` -> **二货爱吃白萝卜** (100.0% isolated ownership) | Magnitude: 681.75
- `components/table/hooks/useSorter.tsx` -> **lijianan** (100.0% isolated ownership) | Magnitude: 303.16
- `components/table/hooks/useFilter/index.tsx` -> **thinkasany** (100.0% isolated ownership) | Magnitude: 160.54
- `components/config-provider/__tests__/theme.test.tsx` -> **lijianan** (100.0% isolated ownership) | Magnitude: 152.32
- `.dumi/scripts/mirror-notify.js` -> **lijianan** (100.0% isolated ownership) | Magnitude: 142.64

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `components/theme/util/genStyleUtils.ts` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 100.0%)
- `components/radio/radio.tsx` -> **Severity: 0.036** (Bridge: 0.0004 * Flux: 100.0%)
- `components/theme/useToken.ts` -> **Severity: 0.024** (Bridge: 0.0004 * Flux: 63.3705%)
- `tests/shared/demoTest.tsx` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)
- `components/_util/ContextIsolator.tsx` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alias/cssinjs.js` -> **Severity: 6.217** (Embedded: 0.0885 * Error Risk: 70.2063%)
- `components/_util/warning.ts` -> **Severity: 5.638** (Embedded: 0.0736 * Error Risk: 76.6221%)
- `components/_util/type.ts` -> **Severity: 3.577** (Embedded: 0.0418 * Error Risk: 85.5202%)
- `tests/utils.tsx` -> **Severity: 3.452** (Embedded: 0.0638 * Error Risk: 54.0818%)
- `tests/shared/demoTest.tsx` -> **Severity: 3.41** (Embedded: 0.0499 * Error Risk: 68.3394%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/utils.tsx` -> **Severity: 1527.12** (Blast Radius: 21.816 * Doc Risk: 70.0%)
- `tests/shared/imageTest.tsx` -> **Severity: 930.6** (Blast Radius: 9.306 * Doc Risk: 100.0%)
- `tests/shared/accessibilityTest.tsx` -> **Severity: 882.0** (Blast Radius: 9.8 * Doc Risk: 90.0%)
- `components/upload/__tests__/mock.ts` -> **Severity: 717.2** (Blast Radius: 7.172 * Doc Risk: 100.0%)
- `components/_util/warning.ts` -> **Severity: 642.35** (Blast Radius: 12.847 * Doc Risk: 50.0%)

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
