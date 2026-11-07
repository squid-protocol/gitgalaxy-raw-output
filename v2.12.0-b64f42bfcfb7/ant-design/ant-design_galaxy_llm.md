# ARCHITECTURAL_BRIEF: ant-design
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ant-design/ant-design.git` |
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
- **Scope:** 3990 analyzed artifact(s), 203599 LOC.
- **Load-bearing artifact:** `tests/utils.tsx` -- 258 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 3990 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 773 |
| Total LOC | 203599 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6258 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.255 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.1456 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 68 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2738 | 200213 | 68.6% |
| MARKDOWN | 1190 | 0 | 29.8% |
| YAML | 35 | 1830 | 0.9% |
| JAVASCRIPT | 10 | 673 | 0.3% |
| JSON | 9 | 402 | 0.2% |
| HTML | 3 | 136 | 0.1% |
| PLAINTEXT | 2 | 1 | 0.1% |
| SHELL | 2 | 100 | 0.1% |
| CSS | 1 | 244 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3989 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Callbacks & Closures Files 18%, Generic / Templated Code Files 13%, Declarative / Non-Code 10%, Large Core Modules 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2798 | 70.1% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1191 | 29.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 773*

**Composition by Extension & Reason:**
- `.snap`: 307x Excluded (Unsupported Extension: '.snap'), 1x Unsupported Format (.snap)
- `.md`: 215x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 10 exceeds 500 chars), 1x Excluded (Saturation: Line 38 exceeds 500 chars)
- `.ts`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1836 LOC)
- `.yml`: 1x Excluded (Saturation: Line 32 exceeds 500 chars), 1x Excluded (Saturation: Line 85 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.less`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.7 | 7.2 | 5.1 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 14.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.0 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.6 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 55.9 | 3.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.7 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1402 | 601 | 1 | `components/index.ts` |
| cleanup | 99 | 62 | 0 | `components/message/__tests__/index.test.tsx` |
| guards | 3776 | 731 | 2 | `components/form/__tests__/index.test.tsx` |
| danger | 2540 | 451 | 1 | `components/table/__tests__/Table.filter.test.tsx` |
| concurrency | 2123 | 224 | 0 | `components/modal/__tests__/confirm.test.tsx` |
| connectivity | 4061 | 2114 | 2 | `components/index.ts` |
| io | 1040 | 239 | 0 | `components/upload/__tests__/uploadlist.test.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 8 | 5 | 0 | `tests/setup.ts` |
| time | 177 | 87 | 0 | `.dumi/scripts/mirror-notify.js` |
| serialization | 29 | 20 | 0 | `components/_util/__tests__/hooks.test.tsx` |
| regex | 117 | 60 | 0 | `scripts/generate-component-changelog.ts` |
| events | 271 | 103 | 0 | `eslint.config.mjs` |
| tests | 10896 | 391 | 0 | `components/form/__tests__/index.test.tsx` |
| docs | 1655 | 327 | 0 | `components/theme/interface/alias.ts` |
| debt | 842 | 366 | 0 | `components/upload/__tests__/uploadlist.test.tsx` |
| mutation | 33014 | 2242 | 21 | `components/form/__tests__/index.test.tsx` |
| dead_code | 221 | 135 | 0 | `components/modal/__tests__/confirm.test.tsx` |
| credential | 82 | 36 | 0 | `components/upload/__tests__/uploadlist.test.tsx` |
| threat | 19 | 3 | 0 | `components/locale/fa_IR.ts` |
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

1. **utils.tsx** (`tests/utils.tsx`) — 258 inbound connections
2. **demoTest.tsx** (`tests/shared/demoTest.tsx`) — 197 inbound connections
3. **internal.ts** (`components/theme/internal.ts`) — 177 inbound connections
4. **index.tsx** (`components/config-provider/index.tsx`) — 165 inbound connections
5. **warning.ts** (`components/_util/warning.ts`) — 133 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.test.tsx** (`components/locale/__tests__/index.test.tsx`) — 146 outbound dependencies
2. **index.ts** (`components/index.ts`) — 83 outbound dependencies
3. **context.ts** (`components/config-provider/context.ts`) — 68 outbound dependencies
4. **components.ts** (`components/theme/interface/components.ts`) — 67 outbound dependencies
5. **style.test.tsx** (`components/config-provider/__tests__/style.test.tsx`) — 63 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `copyTest` **(Many-Argument Workhorses)** (@ `components/typography/__tests__/index.test.tsx`) -> Impact: **126.7** | LOC: 99
  * *Intent:* /** */
- `InternalFormItem` **(Compute Cores)** (@ `components/form/FormItem/index.tsx`) -> Impact: **124.0** | LOC: 331
- `useResize` **(Many-Argument Workhorses)** (@ `components/splitter/hooks/useResize.ts`) -> Impact: **98.2** | LOC: 164
  * *Intent:* /** * Handle user drag resize logic. */
- `ProviderChildren` **(Many-Argument Workhorses)** (@ `components/config-provider/index.tsx`) -> Impact: **91.1** | LOC: 380
- `getSize` **(Defensive Guards)** (@ `components/progress/utils.ts`) -> Impact: **78.5** | LOC: 50
- `InternalSelect` **(Many-Argument Workhorses)** (@ `components/select/index.tsx`) -> Impact: **76.9** | LOC: 290
- `useMenu` **(Defensive Guards)** (@ `.dumi/hooks/useMenu.tsx`) -> Impact: **67.6** | LOC: 136
- `useSelection` **(Many-Argument Workhorses)** (@ `components/table/hooks/useSelection.tsx`) -> Impact: **66.8** | LOC: 227
- `injectSorter` **(Many-Argument Workhorses)** (@ `components/table/hooks/useSorter.tsx`) -> Impact: **66.8** | LOC: 71
- `testStep` **(Many-Argument Workhorses)** (@ `components/typography/__tests__/index.test.tsx`) -> Impact: **65.3** | LOC: 107

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 24 | 5323.28 | 4.26% | 2.55% |
| `scripts` | 18 | 996.09 | 40.57% | 17.17% |
| `components/input/__tests__` | 13 | 952.2 | 2.57% | 0.0% |
| `components/table/__tests__` | 18 | 894.75 | 2.21% | 0.0% |
| `components/message/__tests__` | 13 | 872.65 | 20.5% | 0.0% |
| `components/table/demo` | 101 | 845.5 | 3.18% | 8.58% |
| `components/_util` | 32 | 796.12 | 15.71% | 0.0% |
| `components/float-button/__tests__` | 9 | 760.6 | 1.15% | 0.0% |
| `components/table/hooks` | 6 | 691.6 | 22.91% | 1.36% |
| `components/modal/__tests__` | 11 | 669.72 | 10.74% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `components/modal/demo/confirm.tsx` -> **100.0%** Exposure
- `components/auto-complete/demo/variant.tsx` -> **99.9996%** Exposure
- `components/upload/demo/upload-custom-action-icon.tsx` -> **99.9993%** Exposure
- `components/input/demo/advance-count.tsx` -> **99.9925%** Exposure
- `components/upload/demo/component-token.tsx` -> **99.9925%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.dumi/theme/utils/index.ts` -> **100.0%** Exposure
- `components/_util/ActionButton.tsx` -> **100.0%** Exposure
- `components/_util/ContextIsolator.tsx` -> **100.0%** Exposure
- `components/_util/__tests__/easings.test.ts` -> **100.0%** Exposure
- `components/_util/__tests__/getScroll.test.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `components/table/__tests__/Table.rowSelection.test.tsx` -> **4** Orphaned Functions | **17** Duplicates
- `components/table/__tests__/Table.sorter.test.tsx` -> **1** Orphaned Functions | **18** Duplicates
- `components/table/__tests__/Table.filter.test.tsx` -> **2** Orphaned Functions | **11** Duplicates
- `components/tour/__tests__/index.test.tsx` -> **0** Orphaned Functions | **13** Duplicates
- `components/color-picker/__tests__/index.test.tsx` -> **0** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `45` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5336` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/input/__tests__/Password.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.041)
- **Top Global Matches:** file_cluster_5: 9.041, file_cluster_7: 9.608, file_cluster_14: 10.75
- **Magnitude:** 722.8 | **LOC:** 170 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.2%), Complexity Load (formerly Cognitive Load) (7.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 35`, `args: 17`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 21`
* *Architecture:* `concurrency: 11`, `import: 9`
* *Defense:* `safety: 16`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .., focusTest, mountTest, rtlTest, utils, Password, icons, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/float-button/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.203)
- **Top Global Matches:** file_cluster_5: 8.203, file_cluster_12: 9.726, file_cluster_0: 9.757
- **Magnitude:** 599.28 | **LOC:** 122 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (66.1%), Guard Balance (formerly Safety Score) (29.9%), Complexity Load (formerly Cognitive Load) (5.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 32`, `args: 16`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 1`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 15`, `test: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .., mountTest, rtlTest, utils, util, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/form/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.322)
- **Top Global Matches:** file_cluster_5: 8.322, file_cluster_0: 10.386, file_cluster_12: 10.444
- **Magnitude:** 408.54 | **LOC:** 2634 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (42.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.7%), Mutation Surface (formerly State Flux) (17.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `App` **(Generic / Templated Code)** (Impact: 8.2)
  * `App` **(Generic / Templated Code)** (Impact: 7.4)
  * `changeValue` **(Many-Argument Workhorses)** (Impact: 7.2)
  * `MockInput` **(Defensive Guards)** (Impact: 4.6)
  * `Demo` **(Callbacks & Closures)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 203
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 395`, `args: 215`, `func_start: 102`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 1`, `state_mutation: 27`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `concurrency: 138`, `import: 35`
* *Defense:* `safety: 112`, `test: 337`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` .., mountTest, rtlTest, utils, responsiveObserver, warning, button, cascader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/modal/__tests__/confirm.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.998)
- **Top Global Matches:** file_cluster_12: 8.998, file_cluster_5: 9.004, file_cluster_7: 10.444
- **Magnitude:** 313.64 | **LOC:** 1112 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.1%), Complexity Load (formerly Cognitive Load) (42.9%), Mutation Surface (formerly State Flux) (26.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockActionFn` **(Defensive Guards)** (Impact: 8.0)
  * `error` **(Callbacks & Closures)** (Impact: 4.8)
  * `open` **(Parameter Forwarders)** (Impact: 3.3)
  * `onOk` **(Callbacks & Closures)** (Impact: 3.1)
  * `configWarp` **(Callbacks & Closures)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 8 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 214
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 304`, `args: 132`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 7`, `state_mutation: 17`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `concurrency: 149`, `import: 11`
* *Defense:* `safety: 21`, `test: 192`, `immutability_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .., utils, app, config-provider, confirm, destroyFns, icons, util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useSelection.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.236)
- **Top Global Matches:** file_cluster_6: 9.236, file_cluster_4: 12.805, file_cluster_8: 16.592
- **Magnitude:** 291.9 | **LOC:** 757 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 0.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.1%), Connectivity (formerly Api Exposure) (38.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useSelection` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `renderCell` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `renderCell` **(Defensive Guards)** (Impact: 13.2)
  * `flattenData` **(Generic / Templated Code)** (Impact: 12.7)
  * `onSelect` **(I/O & Config Routines)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 129`, `args: 62`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 35`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 19`
* *Defense:* `safety: 33`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.060882
  * `Imports (Out-Degree: 8):` hooks, type, warning, checkbox, dropdown, radio, interface, DownOutlined...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scripts/visual-regression/build.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.508)
- **Top Global Matches:** file_cluster_15: 6.508, file_cluster_16: 8.5, file_cluster_2: 8.841
- **Magnitude:** 268.1 | **LOC:** 566 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.369; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.8%), Complexity Load (formerly Cognitive Load) (59.8%), Guard Balance (formerly Safety Score) (57.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateReport` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `boot` **(I/O & Config Routines)** (Impact: 24.4)
  * `generateLineReport` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `compareScreenshots` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `getMdImageTag` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 100`, `args: 23`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 26`, `dead_code: 1`
* *Architecture:* `io: 37`, `api: 1`, `concurrency: 44`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.369
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000251
  * `Imports (Out-Degree: 2):` convert, reportAdapter, core, chalk, fs-extra, difference, filter, minimist...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/message/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.509)
- **Top Global Matches:** file_cluster_10: 6.509, file_cluster_13: 8.991, file_cluster_2: 9.086
- **Magnitude:** 258.49 | **LOC:** 251 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (39.7%), Complexity Load (formerly Cognitive Load) (28.6%), Mutation Surface (formerly State Flux) (16.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 67`, `args: 32`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `concurrency: 47`, `import: 5`
* *Defense:* `test: 48`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., utils, util, icons, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useSorter.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.468)
- **Top Global Matches:** file_cluster_0: 8.468, file_cluster_4: 9.917, file_cluster_10: 11.037
- **Magnitude:** 255.46 | **LOC:** 524 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.138; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.9%), Complexity Load (formerly Cognitive Load) (29.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `injectSorter` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `getSortData` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `title` **(Generic / Templated Code)** (Impact: 8.8)
  * `generateSorterInfo` **(Generic / Templated Code)** (Impact: 8.4)
  * `triggerSorter` **(Generic / Templated Code)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 98`, `args: 36`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.054924
  * `Imports (Out-Degree: 5):` type, locale, tooltip, interface, util, CaretDownOutlined, CaretUpOutlined, KeyCode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/form/FormItem/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.434)
- **Top Global Matches:** file_cluster_6: 10.434, file_cluster_4: 11.928, file_cluster_5: 16.158
- **Magnitude:** 247.36 | **LOC:** 459 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **24**; blast radius 3.916; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.7%), Guard Balance (formerly Safety Score) (61.6%), Complexity Load (formerly Cognitive Load) (57.5%), Connectivity (formerly Api Exposure) (56.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InternalFormItem` **(Compute Cores)** (Impact: 124.0)
  * `onMetaChange` **(Compute Cores)** (Impact: 16.9)
  * `renderLayout` **(Many-Argument Workhorses)** (Impact: 12.1)
    * *Intent:* // ======================== Render ========================
  * `isSimilarControl` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* // https://github.com/ant-design/ant-design/issues/46417 // `getValueProps` may modify the value pro...
  * `onSubItemMetaChange` **(Callbacks & Closures)** (Impact: 6.3)
    * *Intent:* // >>>>> Collect noStyle Field error to the top FormItem
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 79`, `args: 20`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 22`
* *Architecture:* `io: 2`, `api: 5`, `import: 26`
* *Defense:* `safety: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.916
  * `Choke Point (Betweenness):` 0.001069 | `Ripple Effect (Closeness):` 0.072431
  * `Imports (Out-Degree: 17):` isNonNullable, reactNode, warning, config-provider, useCSSVarCls, Form, FormItemInput, FormItemLabel...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `components/typography/__tests__/index.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.355)
- **Top Global Matches:** file_cluster_8: 12.355, file_cluster_6: 19.979, file_cluster_3: 22.672
- **Magnitude:** 230.18 | **LOC:** 552 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (52.3%), Guard Balance (formerly Safety Score) (48.0%), Mutation Surface (formerly State Flux) (22.6%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyTest` **(Many-Argument Workhorses)** (Impact: 126.7)
    * *Intent:* /** */
  * `testStep` **(Many-Argument Workhorses)** (Impact: 65.3)
  * `getComputedStyle` **(Callbacks & Closures)** (Impact: 1.7)
  * `DynamicPropsTestCase` **(Callbacks & Closures)** (Impact: 1.6)
  * `fn` **(Type Conversions)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 82`, `args: 46`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 8`
* *Architecture:* `concurrency: 11`, `import: 15`
* *Defense:* `safety: 16`, `doc: 1`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` mountTest, rtlTest, utils, copy, Base, Link, Paragraph, Text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/print-changelog.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.585)
- **Top Global Matches:** file_cluster_6: 8.585, file_cluster_4: 10.094, file_cluster_12: 16.343
- **Magnitude:** 229.4 | **LOC:** 392 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.127; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (97.1%), Guard Balance (formerly Safety Score) (59.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printLog` **(I/O & Config Routines)** (Impact: 63.9)
  * `printPR` **(Compute Cores)** (Impact: 13.5)
  * `getDescription` **(Callbacks & Closures)** (Impact: 4.7)
  * `fetchPullRequest` **(Callbacks & Closures)** (Impact: 3.2)
  * `validate` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 60`, `args: 29`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 20`, `concurrency: 17`, `import: 10`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` prompts, chalk, fs-extra, isomorphic-fetch, jquery, jsdom, node:child_process, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/__tests__/Table.filter.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.489)
- **Top Global Matches:** file_cluster_5: 8.489, file_cluster_7: 8.596, file_cluster_12: 8.966
- **Magnitude:** 224.16 | **LOC:** 3162 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.0%), Concurrency Surface (formerly Concurrency) (22.1%), Mutation Surface (formerly State Flux) (12.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.0%)
- **Documentation Coverage:** 98.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderedNames` **(Defensive Guards)** (Impact: 7.6)
  * `filter` **(Callbacks & Closures)** (Impact: 5.8)
  * `onFilter` **(Defensive Guards)** (Impact: 5.5)
  * `filter` **(Callbacks & Closures)** (Impact: 4.6)
  * `onFilter` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* // specify the condition of filtering result // here is that finding the name started with `value`
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 301`, `args: 239`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 224`, `state_mutation: 14`, `dead_code: 1`, `duplicate_logic: 11`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 20`, `import: 13`
* *Defense:* `safety: 88`, `doc: 1`, `test: 315`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` .., utils, warning, button, config-provider, input, menu, select...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.dumi/theme/utils/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.851)
- **Top Global Matches:** file_cluster_6: 8.851, file_cluster_8: 11.219, file_cluster_4: 15.939
- **Magnitude:** 223.56 | **LOC:** 217 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.0%), Connectivity (formerly Api Exposure) (74.9%), Guard Balance (formerly Safety Score) (68.3%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMenuItems` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `getLocalizedPathname` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `getMetaDescription` **(Callbacks & Closures)** (Impact: 11.1)
  * `sortFn` **(Compute Cores)** (Impact: 5.2)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BUG_VERSIONS.json, flatten, flattenDeep, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/typography/__tests__/ellipsis.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.185)
- **Top Global Matches:** file_cluster_5: 8.185, file_cluster_7: 9.867, file_cluster_12: 10.028
- **Magnitude:** 221.96 | **LOC:** 736 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (74.9%), Guard Balance (formerly Safety Score) (50.0%), Complexity Load (formerly Cognitive Load) (29.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getContentHeight` **(Compute Cores)** (Impact: 7.3)
  * `getWrapper` **(Generic / Templated Code)** (Impact: 3.4)
  * `getTooltipContent` **(Defensive Guards)** (Impact: 3.1)
  * `getBoundingClientRect` **(I/O & Config Routines)** (Impact: 3.0)
  * `getBoundingClientRect` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 124
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 131`, `args: 68`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 28`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 59`, `import: 8`
* *Defense:* `safety: 47`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` utils, config-provider, zh_CN, Base, domHook, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/splitter/hooks/useResize.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.27)
- **Top Global Matches:** file_cluster_8: 8.27, file_cluster_6: 9.929, file_cluster_4: 17.969
- **Magnitude:** 218.02 | **LOC:** 174 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.139; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.0%), Complexity Load (formerly Cognitive Load) (61.5%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useResize` **(Many-Argument Workhorses)** (Impact: 98.2)
    * *Intent:* /** * Handle user drag resize logic. */
  * `onOffsetUpdate` **(Many-Argument Workhorses)** (Impact: 30.8)
  * `onCollapse` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* // ======================= Collapse =======================
  * `getLimitSize` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* // ======================== Resize ========================
  * `onOffsetStart` **(Callbacks & Closures)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 25`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 5`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.139
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.054126
  * `Imports (Out-Degree: 3):` useItems, useResizable, useSizes, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/shared/imageTest.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.763)
- **Top Global Matches:** file_cluster_12: 10.763, file_cluster_5: 10.813, file_cluster_4: 11.159
- **Magnitude:** 217.3 | **LOC:** 357 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **66** in-repo importer(s); it depends on **16**; blast radius 7.247; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (89.8%), Connectivity (formerly Api Exposure) (75.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `imageTest` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* // eslint-disable-next-line jest/no-export
  * `imageDemoTest` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* // eslint-disable-next-line jest/no-export
  * `onRequestHandle` **(Defensive Guards)** (Impact: 7.6)
  * `getTestOption` **(Compute Cores)** (Impact: 4.6)
  * `test` **(Callbacks & Closures)** (Impact: 2.6)
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
* *Architecture:* `io: 15`, `api: 10`, `concurrency: 23`, `import: 16`
* *Defense:* `safety: 5`, `doc: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.247
  * `Choke Point (Betweenness):` 0.002717 | `Ripple Effect (Closeness):` 0.016546
  * `Imports (Out-Degree: 4):` components, setup, utils, demoTestContext, cssinjs, util, antd-style, dayjs...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `components/table/hooks/useFilter/FilterDropdown.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.734)
- **Top Global Matches:** file_cluster_0: 7.734, file_cluster_10: 8.225, file_cluster_15: 8.253
- **Magnitude:** 205.56 | **LOC:** 592 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (58.4%), Guard Balance (formerly Safety Score) (50.2%), Connectivity (formerly Api Exposure) (37.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFilterComponent` **(I/O & Config Routines)** (Impact: 20.6)
  * `renderFilterItems` **(Compute Cores)** (Impact: 15.4)
  * `internalTriggerFilter` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* // ======================= Submit ========================
  * `onVisibleChange` **(Compute Cores)** (Impact: 12.8)
  * `onReset` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 107`, `args: 37`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `api: 7`, `import: 27`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.000191 | `Ripple Effect (Closeness):` 0.046843
  * `Imports (Out-Degree: 16):` , extendsObject, hooks, warning, Button, checkbox, context, dropdown...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/config-provider/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.663)
- **Top Global Matches:** file_cluster_4: 7.663, file_cluster_6: 9.666, file_cluster_12: 13.471
- **Magnitude:** 202.8 | **LOC:** 777 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **165** in-repo importer(s); it depends on **22**; blast radius 13.327; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.5%), Connectivity (formerly Api Exposure) (74.8%), Guard Balance (formerly Safety Score) (53.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProviderChildren` **(Many-Argument Workhorses)** (Impact: 91.1)
  * `getPrefixCls` **(Compute Cores)** (Impact: 9.0)
  * `setGlobalConfig` **(Compute Cores)** (Impact: 7.9)
  * `getRootPrefixCls` **(Callbacks & Closures)** (Impact: 2.5)
  * `getGlobalPrefixCls` **(Interface Declarations)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 92`, `args: 26`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 23`
* *Architecture:* `api: 12`, `import: 27`
* *Defense:* `safety: 10`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.327
  * `Choke Point (Betweenness):` 0.013648 | `Ripple Effect (Closeness):` 0.111445
  * `Imports (Out-Degree: 17):` warning, validateMessagesContext, locale, context, en_US, context, seed, UniqueProvider...
  * `Imported By (In-Degree: 165):` (Excluded from Brief to save tokens)

### `components/table/__tests__/Table.rowSelection.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.308)
- **Top Global Matches:** file_cluster_12: 7.308, file_cluster_5: 8.157, file_cluster_7: 9.225
- **Magnitude:** 192.62 | **LOC:** 2148 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.5%), Mutation Surface (formerly State Flux) (30.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.2%), Concurrency Surface (formerly Concurrency) (17.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderedNames` **(Defensive Guards)** (Impact: 10.4)
  * `getSelections` **(Defensive Guards)** (Impact: 9.2)
  * `getIndeterminateSelection` **(Callbacks & Closures)** (Impact: 7.8)
  * `getCheckboxProps` **(Callbacks & Closures)** (Impact: 3.3)
  * `clickFilter` **(Callbacks & Closures)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 214`, `args: 154`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 37`, `dead_code: 1`, `duplicate_logic: 17`, `unreferenced_by_name: 4`
* *Architecture:* `concurrency: 6`, `import: 7`
* *Defense:* `safety: 38`, `test: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .., utils, warning, config-provider, interface, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/upload/Upload.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.719)
- **Top Global Matches:** file_cluster_12: 7.719, file_cluster_5: 8.882, file_cluster_7: 9.99
- **Magnitude:** 190.4 | **LOC:** 548 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 0.331; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.6%), Connectivity (formerly Api Exposure) (32.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.4%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onInternalChange` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `InternalUpload` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `handleRemove` **(Defensive Guards)** (Impact: 13.9)
  * `mergedBeforeUpload` **(Type Conversions)** (Impact: 11.8)
  * `renderUploadList` **(Compute Cores)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 77`, `args: 26`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 28`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 3`, `import: 16`
* *Defense:* `safety: 10`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.331
  * `Choke Point (Betweenness):` 0.000503 | `Ripple Effect (Closeness):` 0.065287
  * `Imports (Out-Degree: 10):` hooks, warning, DisabledContext, context, locale, en_US, UploadList, interface...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/transfer/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.438)
- **Top Global Matches:** file_cluster_5: 7.438, file_cluster_12: 7.821, file_cluster_0: 8.828
- **Magnitude:** 179.3 | **LOC:** 617 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **19**; blast radius 0.561; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.9%), Guard Balance (formerly Safety Score) (52.2%), Mutation Surface (formerly State Flux) (46.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Transfer` **(I/O & Config Routines)** (Impact: 19.7)
  * `onItemSelect` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `onItemSelectAll` **(Compute Cores)** (Impact: 11.1)
  * `handleSingleSelect` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `moveTo` **(Defensive Guards)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 129`, `args: 48`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`
* *Architecture:* `api: 20`, `import: 27`
* *Defense:* `safety: 18`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.561
  * `Choke Point (Betweenness):` 0.001144 | `Ripple Effect (Closeness):` 0.083129
  * `Imports (Out-Degree: 17):` hooks, statusUtils, transKeys, warning, DisabledContext, context, defaultRenderEmpty, context...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `components/upload/__tests__/upload.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.521)
- **Top Global Matches:** file_cluster_5: 8.521, file_cluster_12: 8.834, file_cluster_7: 10.202
- **Magnitude:** 178.42 | **LOC:** 1205 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.0%), Mutation Surface (formerly State Flux) (18.2%), Complexity Load (formerly Cognitive Load) (13.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onChange` **(Compute Cores)** (Impact: 14.2)
  * `onChange` **(Callbacks & Closures)** (Impact: 3.2)
  * `onChange` **(State Mutators)** (Impact: 3.1)
  * `onChange` **(Callbacks & Closures)** (Impact: 3.1)
  * `onChange` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 89
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 212`, `args: 107`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 10`, `fragile_debt: 7`, `duplicate_logic: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 21`, `concurrency: 69`, `import: 14`
* *Defense:* `safety: 34`, `test: 138`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .., mountTest, rtlTest, utils, warning, config-provider, form, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/InternalTable.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.565)
- **Top Global Matches:** file_cluster_4: 10.565, file_cluster_6: 11.808, file_cluster_5: 13.14
- **Magnitude:** 172.54 | **LOC:** 772 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 36.4%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **36**; blast radius 0.437; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.7%), Connectivity (formerly Api Exposure) (53.9%), Guard Balance (formerly Safety Score) (52.7%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InternalTable` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `triggerOnChange` **(Defensive Guards)** (Impact: 23.3)
  * `normalizePlacement` **(Callbacks & Closures)** (Impact: 6.0)
  * `internalRowClassName` **(Callbacks & Closures)** (Impact: 4.5)
  * `onSorterChange` **(Generic / Templated Code)** (Impact: 2.4)
    * *Intent:* /** * Controlled state in `columns` is not a good idea that makes too many code (1000+ line?) to rea...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 146`, `args: 37`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`
* *Architecture:* `api: 13`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 29`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.437
  * `Choke Point (Betweenness):` 0.001973 | `Ripple Effect (Closeness):` 0.066386
  * `Imports (Out-Degree: 33):` hooks, responsiveObserver, scrollTo, type, warning, config-provider, SizeContext, context...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `components/upload/__tests__/uploadlist.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.327)
- **Top Global Matches:** file_cluster_12: 8.327, file_cluster_5: 8.346, file_cluster_10: 10.078
- **Magnitude:** 169.48 | **LOC:** 1756 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (90.4%), Guard Balance (formerly Safety Score) (47.3%), Mutation Surface (formerly State Flux) (15.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Defensive Guards)** (Impact: 6.7)
  * `validator` **(State Mutators)** (Impact: 5.4)
  * `onChange` **(Callbacks & Closures)** (Impact: 4.8)
  * `itemRender` **(Many-Argument Workhorses)** (Impact: 3.3)
  * `drawImage` **(State Mutators)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 65
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 227`, `args: 124`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 18`, `fragile_debt: 39`, `unreferenced_by_name: 4`
* *Architecture:* `io: 65`, `concurrency: 60`, `import: 12`
* *Defense:* `safety: 26`, `test: 175`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .., utils, config-provider, form, UploadList, interface, utils, mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `components/modal/demo/confirm-router.tsx` (TYPESCRIPT) | Magnitude: 17.2 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, args: 6, func_start: 5
- `components/date-picker/__tests__/demo.test.tsx` (TYPESCRIPT) | Magnitude: 2.52 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, args: 4, ui_framework: 4
- `components/masonry/Masonry.tsx` (TYPESCRIPT) | Magnitude: 32.86 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 83, core_var_decl: 49, branch: 36
- `components/card/index.tsx` (TYPESCRIPT) | Magnitude: 26.52 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 11, import: 6, api: 5
- `components/popconfirm/__tests__/type.test.tsx` (TYPESCRIPT) | Magnitude: 14.16 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, test: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `components/slider/__tests__/type.test.tsx` (TYPESCRIPT) | Magnitude: 5.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, core_var_decl: 17, structural_boundaries: 11, design_camel_case: 9
- `components/steps/demo/style-class.tsx` (TYPESCRIPT) | Magnitude: 7.18 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, core_var_decl: 5, safety: 4
- `components/carousel/style/index.ts` (TYPESCRIPT) | Magnitude: 31.96 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 370, structural_boundaries: 29, doc: 8, args: 7
- `components/input/style/otp.ts` (TYPESCRIPT) | Magnitude: 6.28 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 15, import: 5, args: 2
- `components/cascader/__tests__/demo.test.tsx` (TYPESCRIPT) | Magnitude: 1.28 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, args: 2, ui_framework: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `components/date-picker/__tests__/DatePicker.test.tsx` (TYPESCRIPT) | Magnitude: 27.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 461, test: 111, core_var_decl: 70, structural_boundaries: 65
- `components/modal/__tests__/confirm.test.tsx` (TYPESCRIPT) | Magnitude: 313.64 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 850, structural_boundaries: 304, test: 192, concurrency: 149
- `components/upload/__tests__/uploadlist.test.tsx` (TYPESCRIPT) | Magnitude: 169.48 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 1533, core_var_decl: 352, structural_boundaries: 227, design_camel_case: 223
- `components/tooltip/__tests__/semantic.test.tsx` (TYPESCRIPT) | Magnitude: 7.34 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 14, core_var_decl: 10, test: 9
- `tests/setup.ts` (TYPESCRIPT) | Magnitude: 124.6 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 28, branch: 19, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `components/input-number/style/token.ts` (TYPESCRIPT) | Magnitude: 10.46 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 14, doc: 11, import: 4
- `components/checkbox/index.tsx` (TYPESCRIPT) | Magnitude: 28.46 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 8, import: 5, api: 4
- `alias/cssinjs.js` (JAVASCRIPT) | Magnitude: 27.68 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 6, safety: 4, state_mutation: 4, indent_spaces: 3
- `components/table/style/rtl.ts` (TYPESCRIPT) | Magnitude: 5.2 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 10, import: 4, branch: 1
- `components/menu/style/horizontal.ts` (TYPESCRIPT) | Magnitude: 5.88 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 11, import: 4, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `components/form/hooks/useChildren.ts` (TYPESCRIPT) | Magnitude: 7.42 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, branch: 4, import: 2
- `components/descriptions/style/index.ts` (TYPESCRIPT) | Magnitude: 17.12 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 22, doc: 11, import: 5
- `components/drawer/style/index.ts` (TYPESCRIPT) | Magnitude: 16.84 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 272, structural_boundaries: 20, import: 6, api: 4
- `components/mentions/style/index.ts` (TYPESCRIPT) | Magnitude: 19.54 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 250, structural_boundaries: 26, import: 9, doc: 5
- `components/theme/util/getAlphaColor.ts` (TYPESCRIPT) | Magnitude: 18.82 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 15, branch: 7, structural_boundaries: 6, scientific: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/issue-close-require.yml` (YAML) | Magnitude: 15.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, args: 7, structural_boundaries: 2, import: 2
- `components/theme/interface/components.ts` (TYPESCRIPT) | Magnitude: 18.72 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 136, branch: 67, import: 67, explicit_casts: 67
- `.github/workflows/size-limit.yml` (YAML) | Magnitude: 18.6 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 3, args: 3, import: 3
- `.github/workflows/release-x.yml` (YAML) | Magnitude: 15.38 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, args: 5, globals: 4, dependency_injection: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `components/badge/style/index.ts` (TYPESCRIPT) | Magnitude: 19.92 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 282, structural_boundaries: 24, doc: 20, core_var_decl: 16
- `components/table/style/radius.ts` (TYPESCRIPT) | Magnitude: 5.48 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 10, import: 4, decorators: 2
- `components/breadcrumb/demo/component-token.tsx` (TYPESCRIPT) | Magnitude: 17.58 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 72, core_var_decl: 9, design_snake_case: 8, structural_boundaries: 5
- `.github/workflows/verify-package-version.yml` (YAML) | Magnitude: 16.42 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 17, args: 3, branch: 2, structural_boundaries: 2
- `components/table/style/sticky.ts` (TYPESCRIPT) | Magnitude: 8.44 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 12, import: 4, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `components/date-picker/demo/buddhist-era.tsx` (TYPESCRIPT) | Magnitude: 5.04 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 12, core_var_decl: 12, ui_framework: 9
- `components/modal/locale.ts` (TYPESCRIPT) | Magnitude: 18.86 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, core_var_decl: 7, args: 6
- `components/form/demo/nest-messages.tsx` (TYPESCRIPT) | Magnitude: 6.1 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, core_var_decl: 14, ui_framework: 13, generics: 13
- `components/mentions/__tests__/demo.test.tsx` (TYPESCRIPT) | Magnitude: 4.04 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 9, core_var_decl: 5, args: 4
- `components/notification/__tests__/hooks.test.tsx` (TYPESCRIPT) | Magnitude: 32.32 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 58, ui_framework: 40, args: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `components/notification/__tests__/util.ts` (TYPESCRIPT) | Magnitude: 49.8 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, concurrency: 6, branch: 5
- `components/switch/__tests__/wave.test.tsx` (TYPESCRIPT) | Magnitude: 8.32 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 9, concurrency: 6, safety_bypasses: 5
- `components/_util/throttleByAnimationFrame.ts` (TYPESCRIPT) | Magnitude: 20.18 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, core_var_decl: 6, args: 5
- `components/transfer/__tests__/dropdown.test.tsx` (TYPESCRIPT) | Magnitude: 4.46 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 19, args: 17, test: 17
- `components/table/__tests__/Table.IE.test.tsx` (TYPESCRIPT) | Magnitude: 17.34 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, test: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `components/collapse/__tests__/semantic.test.tsx` (TYPESCRIPT) | Magnitude: 15.14 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 81, test: 23, core_var_decl: 22, design_camel_case: 17
- `components/pagination/Pagination.tsx` (TYPESCRIPT) | Magnitude: 43.3 | Delta: **0.16** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 201, structural_boundaries: 63, core_var_decl: 56, branch: 37

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/test.yml` -> Churn: **54.96%** | Cog Load: 14.6322% | Debt: 52.6018%
- `eslint.config.mjs` -> Churn: **54.02%** | Cog Load: 3.1714% | Debt: 61.2677%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/visual-regression/build.ts` -> **thinkasany** (100.0% isolated ownership) | Magnitude: 268.1
- `components/table/__tests__/Table.filter.test.tsx` -> **thinkasany** (100.0% isolated ownership) | Magnitude: 224.16
- `components/upload/__tests__/uploadlist.test.tsx` -> **lijianan** (100.0% isolated ownership) | Magnitude: 169.48
- `scripts/pre-publish.ts` -> **二货机器人** (100.0% isolated ownership) | Magnitude: 125.7
- `scripts/generate-token-meta.ts` -> **lijianan** (100.0% isolated ownership) | Magnitude: 112.0

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `components/config-provider/index.tsx` -> **Severity: 1.125** (Bridge: 0.0136 * Flux: 82.4522%)
- `tests/shared/demoTest.tsx` -> **Severity: 0.741** (Bridge: 0.0074 * Flux: 100.0%)
- `components/date-picker/generatePicker/index.tsx` -> **Severity: 0.728** (Bridge: 0.0073 * Flux: 100.0%)
- `tests/shared/rootPropsTest.tsx` -> **Severity: 0.71** (Bridge: 0.0074 * Flux: 96.3228%)
- `components/theme/util/genStyleUtils.ts` -> **Severity: 0.394** (Bridge: 0.0039 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `components/_util/type.ts` -> **Severity: 8.431** (Embedded: 0.1054 * Error Risk: 80.0%)
- `components/locale/index.tsx` -> **Severity: 7.591** (Embedded: 0.0955 * Error Risk: 79.4505%)
- `components/_util/warning.ts` -> **Severity: 7.252** (Embedded: 0.1235 * Error Risk: 58.7269%)
- `components/tooltip/UniqueProvider/index.tsx` -> **Severity: 6.798** (Embedded: 0.085 * Error Risk: 80.0%)
- `components/_util/hooks/useProxyImperativeHandle.ts` -> **Severity: 6.143** (Embedded: 0.0768 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/utils.tsx` -> **Severity: 1543.306** (Blast Radius: 22.556 * Doc Risk: 68.4211%)
- `components/date-picker/generatePicker/index.tsx` -> **Severity: 1048.5** (Blast Radius: 10.485 * Doc Risk: 100.0%)
- `tests/shared/imageTest.tsx` -> **Severity: 724.7** (Blast Radius: 7.247 * Doc Risk: 100.0%)
- `tests/shared/accessibilityTest.tsx` -> **Severity: 681.432** (Blast Radius: 7.616 * Doc Risk: 89.4737%)
- `components/config-provider/index.tsx` -> **Severity: 666.35** (Blast Radius: 13.327 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 494 literal sites + 11 sites through wrappers = 505
- **`panics_and_aborts`:** 67 literal sites + 5 sites through wrappers = 72

- `exitProcess` (function, debug_prints, primitive): 5 call sites in 1 files -- `scripts/check-repo.ts`
- `exitProcess` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `scripts/check-repo.ts`
- `onChangeComplete` (function, debug_prints, primitive): 5 call sites in 4 files -- `components/slider/demo/event.tsx`
- `handleAreaClick` (function, debug_prints, primitive): 1 call sites in 1 files -- `components/cascader/demo/custom-render.tsx`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 8463 call pairs -- scoped 16.9%, unique 0.0%, ambiguous 5.3%, external 77.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 8353 | 16.9% | 0.0% | 5.3% | 77.8% |
| javascript | 86 | 14.0% | 0.0% | 1.2% | 84.9% |
| shell | 24 | 41.7% | 0.0% | 0.0% | 58.3% |

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
