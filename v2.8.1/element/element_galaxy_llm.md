# ARCHITECTURAL_BRIEF: element
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ElemeFE/element.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1144 |
| Analyzed Artifacts (Scanned) | 762 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 382 |
| Total LOC | 84690 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6197 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4522 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3518 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 65 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 320 | 43832 | 42.0% |
| CSS | 165 | 12864 | 21.7% |
| HTML | 151 | 24996 | 19.8% |
| TYPESCRIPT | 91 | 1768 | 11.9% |
| JSON | 12 | 1170 | 1.6% |
| XML | 12 | 27 | 1.6% |
| MARKDOWN | 8 | 0 | 1.0% |
| PLAINTEXT | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 33 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.18; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Declarative / Non-Code 33%, Interface Declarations Files 5%, Callbacks & Closures Files 5%, Large Core Modules 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 747 | 98.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 1.3% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 382*

**Composition by Extension & Reason:**
- `.md`: 270x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 46x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.tpl`: 11x Excluded (Unsupported Extension: '.tpl')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vue`: 4x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff`: 2x Excluded (Explicitly Denied Extension: '.woff')
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1275 LOC), 1x Excluded (Massive Static Asset Blob: 4196 LOC)
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')
- `.svg`: 1x Excluded (Machine-Generated Source Code Signature: 14 LOC)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.8 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.2 | 32.0 | 34.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.9 | 3.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 42.5 | 0.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 79.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 50.7 | 85.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 64 | 30 | 0 | `test/unit/specs/date-picker.spec.js` |
| cleanup | 112 | 55 | 0 | `packages/notification/src/main.vue` |
| guards | 2322 | 227 | 8 | `src/utils/lodash.js` |
| danger | 425 | 75 | 0 | `src/utils/lodash.js` |
| concurrency | 1924 | 108 | 2 | `test/unit/specs/date-picker.spec.js` |
| connectivity | 2070 | 496 | 5 | `packages/theme-chalk/src/common/var.scss` |
| io | 128 | 29 | 0 | `examples/components/footer.vue` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1023 | 85 | 1 | `test/unit/specs/date-picker.spec.js` |
| serialization | 35 | 13 | 0 | `test/unit/specs/upload.spec.js` |
| regex | 197 | 52 | 0 | `src/utils/lodash.js` |
| events | 1709 | 192 | 7 | `packages/date-picker/src/panel/date.vue` |
| tests | 2968 | 65 | 0 | `test/unit/specs/date-picker.spec.js` |
| docs | 1789 | 114 | 3 | `src/utils/lodash.js` |
| debt | 424 | 77 | 1 | `test/unit/specs/table.spec.js` |
| mutation | 15097 | 438 | 49 | `src/utils/lodash.js` |
| dead_code | 230 | 72 | 0 | `src/utils/date-util.js` |
| credential | 5 | 2 | 0 | `examples/components/footer.vue` |
| threat | 566 | 141 | 1 | `src/utils/lodash.js` |
| ml_ai | 23 | 6 | 0 | `packages/empty/src/img-empty.vue` |
| ui | 874 | 185 | 3 | `packages/table/src/store/watcher.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `examples/components/footer.vue` (Hits: 34)
- `examples/components/header.vue` (Hits: 12)
- `packages/date-picker/src/basic/year-table.vue` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **var.scss** (`packages/theme-chalk/src/common/var.scss`) — 88 inbound connections
2. **mixins.scss** (`packages/theme-chalk/src/mixins/mixins.scss`) — 79 inbound connections
3. **utils.scss** (`packages/theme-chalk/src/mixins/utils.scss`) — 14 inbound connections
4. **dom.js** (`src/utils/dom.js`) — 13 inbound connections
5. **popup.scss** (`packages/theme-chalk/src/common/popup.scss`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`src/index.js`) — 91 outbound dependencies
2. **element-ui.d.ts** (`types/element-ui.d.ts`) — 90 outbound dependencies
3. **index.scss** (`packages/theme-chalk/src/index.scss`) — 87 outbound dependencies
4. **index.scss** (`examples/demo-styles/index.scss`) — 48 outbound dependencies
5. **entry.js** (`examples/entry.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fromHSV` **(Defensive Guards)** (@ `packages/color-picker/src/color.js`) -> Impact: **69.5** | LOC: 71
- `orderBy` **(Defensive Guards)** (@ `packages/table/src/util.js`) -> Impact: **66.5** | LOC: 56
- `fromHSV` **(Defensive Guards)** (@ `examples/components/theme-configurator/editor/color-picker/src/color.js`) -> Impact: **65.5** | LOC: 70
- `created` **(Defensive Guards)** (@ `packages/tree/src/tree.vue`) -> Impact: **61.1** | LOC: 163
- `wrappedRowRender` **(Defensive Guards)** (@ `packages/table/src/table-body.js`) -> Impact: **56.5** | LOC: 90
- `fromString` **(Defensive Guards)** (@ `packages/color-picker/src/color.js`) -> Impact: **52.1** | LOC: 81
- `fromString` **(Defensive Guards)** (@ `examples/components/theme-configurator/editor/color-picker/src/color.js`) -> Impact: **49.3** | LOC: 80
- `setChecked` **(Many-Argument Workhorses)** (@ `packages/tree/src/model/node.js`) -> Impact: **40.6** | LOC: 52
- `constructor` **(Defensive Guards)** (@ `packages/tree/src/model/node.js`) -> Impact: **37.5** | LOC: 71
- `openModal` **(Many-Argument Workhorses)** (@ `src/utils/popup/popup-manager.js`) -> Impact: **36.4** | LOC: 42

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/utils` | 18 | 483022.83 | 46.86% | 42.68% |
| `test/unit/specs` | 63 | 6540.02 | 16.25% | 0.0% |
| `packages/table/src` | 12 | 2128.2 | 51.13% | 17.5% |
| `packages/date-picker/src/panel` | 6 | 1293.88 | 41.09% | 6.16% |
| `packages/tree/src/model` | 3 | 862.88 | 52.58% | 32.66% |
| `packages/select/src` | 5 | 802.82 | 41.87% | 18.95% |
| `packages/date-picker/src/basic` | 4 | 737.58 | 49.33% | 6.7% |
| `packages/table/src/store` | 6 | 702.02 | 72.56% | 31.39% |
| `packages/date-picker/src` | 1 | 620.16 | 45.06% | 0.0% |
| `packages/cascader-panel/src` | 5 | 577.62 | 42.65% | 19.98% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `types/tree.d.ts` -> **100.0%** Exposure
- `src/utils/date-util.js` -> **99.9999%** Exposure
- `src/transitions/collapse-transition.js` -> **99.9945%** Exposure
- `src/utils/types.js` -> **99.9877%** Exposure
- `Makefile` -> **99.9089%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `examples/components/demo-block.vue` -> **100.0%** Exposure
- `examples/components/footer-nav.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/color-picker/src/components/alpha-slider.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/color-picker/src/components/hue-slider.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/color-picker/src/components/sv-panel.vue` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/specs/table.spec.js` -> **0** Orphaned Functions | **48** Duplicates
- `test/unit/specs/date-picker.spec.js` -> **4** Orphaned Functions | **40** Duplicates
- `test/unit/specs/autocomplete.spec.js` -> **0** Orphaned Functions | **42** Duplicates
- `test/unit/specs/form.spec.js` -> **1** Orphaned Functions | **23** Duplicates
- `src/utils/date-util.js` -> **23** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `397` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/utils/popup/popup-manager.js` (JAVASCRIPT) -> Cumulative Risk: **728.54**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.53)
- **Magnitude:** 161.82 | **LOC:** 195 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (96.7326%)
- **Heaviest Functions:** `openModal` (Many-Argument Workhorses, Impact: 36.4), `closeModal` (Defensive Guards, Impact: 19.0), `getModal` (Callbacks & Closures, Impact: 6.1)

### 2. `src/utils/popup/index.js` (JAVASCRIPT) -> Cumulative Risk: **701.78**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.27)
- **Magnitude:** 170.16 | **LOC:** 219 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.2776%)
- **Heaviest Functions:** `doOpen` (Compute Cores, Impact: 26.5), `open` (Compute Cores, Impact: 9.6), `visible` (Callbacks & Closures, Impact: 9.2)

### 3. `src/utils/util.js` (JAVASCRIPT) -> Cumulative Risk: **693.27**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.61)
- **Magnitude:** 235.32 | **LOC:** 246 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `isEmpty` (Defensive Guards, Impact: 18.5), `getPropByPath` (Compute Cores, Impact: 17.2), `valueEquals` (Defensive Guards, Impact: 12.8)

### 4. `packages/table/src/store/index.js` (JAVASCRIPT) -> Cumulative Risk: **688.84**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z -0.11)
- **Magnitude:** 128.8 | **LOC:** 148 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (95.7912%), Cognitive Load (90.371%)
- **Heaviest Functions:** `insertColumn` (Many-Argument Workhorses, Impact: 16.8), `removeColumn` (Compute Cores, Impact: 10.8), `setData` (State Mutators, Impact: 9.8)

### 5. `packages/tooltip/src/main.js` (JAVASCRIPT) -> Cumulative Risk: **649.74**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.59)
- **Magnitude:** 158.68 | **LOC:** 243 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.5739%), Concurrency (87.3739%)
- **Heaviest Functions:** `node` (Many-Argument Workhorses, Impact: 18.2), `mounted` (Callbacks & Closures, Impact: 14.6), `render` (Callbacks & Closures, Impact: 12.8)

### 6. `packages/table/src/table-header.js` (JAVASCRIPT) -> Cumulative Risk: **647.79**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.16)
- **Magnitude:** 418.02 | **LOC:** 512 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (83.0912%)
- **Heaviest Functions:** `handleSortClick` (Defensive Guards, Impact: 32.2), `handleMouseMove` (Compute Cores, Impact: 27.4), `getHeaderCellClass` (Many-Argument Workhorses, Impact: 19.4)

### 7. `packages/table/src/table-body.js` (JAVASCRIPT) -> Cumulative Risk: **647.44**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.23)
- **Magnitude:** 362.38 | **LOC:** 470 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9487%), Cognitive Load (83.478%)
- **Heaviest Functions:** `wrappedRowRender` (Defensive Guards, Impact: 56.5), `traverse` (Defensive Guards, Impact: 35.3), `getRowClass` (Defensive Guards, Impact: 22.5)

### 8. `src/directives/repeat-click.js` (JAVASCRIPT) -> Cumulative Risk: **629.51**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.59)
- **Magnitude:** 30.58 | **LOC:** 27 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.1837%), Concurrency (98.7872%)
- **Heaviest Functions:** `bind` (Callbacks & Closures, Impact: 9.1), `clear` (Callbacks & Closures, Impact: 3.9), `handler` (Callbacks & Closures, Impact: 1.1)

### 9. `packages/message-box/src/main.js` (JAVASCRIPT) -> Cumulative Risk: **617.18**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.49)
- **Magnitude:** 201.2 | **LOC:** 217 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (91.4012%)
- **Heaviest Functions:** `defaultCallback` (Defensive Guards, Impact: 19.6), `MessageBox` (Defensive Guards, Impact: 19.0), `callback` (Callbacks & Closures, Impact: 11.6)

### 10. `packages/table/src/table-layout.js` (JAVASCRIPT) -> Cumulative Risk: **616.48**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.29)
- **Magnitude:** 239.96 | **LOC:** 250 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.9494%)
- **Heaviest Functions:** `updateColumnsWidth` (Callbacks & Closures, Impact: 32.4), `updateElsHeight` (Compute Cores, Impact: 21.4), `setHeight` (Defensive Guards, Impact: 14.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/utils/lodash.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 475277.34 | **LOC:** 18076 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8483%), Tech Debt (8.0272%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 941 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 3250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1782`, `structural_boundaries: 1564`, `args: 689`, `func_start: 512`
* *Risk/State:* `safety_bypasses: 258`, `state_mutation: 1368`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 370`, `doc: 676`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/date.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5933.87 | **LOC:** 369 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6341%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 77`, `args: 57`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 53`
* *Architecture:* `api: 2`
* *Defense:* `safety: 19`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/date-picker.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 959.82 | **LOC:** 2856 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.5123%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMonthLabel` **(Tests & Verification)** (Impact: 8.5)
  * `testWeek` **(Callbacks & Closures)** (Impact: 4.2)
  * `keyDown` **(Callbacks & Closures)** (Impact: 3.1)
  * `numberOfHighlightRows` **(Callbacks & Closures)** (Impact: 2.8)
  * `clickAndWait` **(Callbacks & Closures)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 72 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 599
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 498`, `args: 401`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 141`, `planned_debt: 2`, `duplicate_logic: 40`, `unreferenced_by_name: 4`
* *Architecture:* `concurrency: 239`, `import: 2`
* *Defense:* `safety: 6`, `test: 415`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util, date-picker
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/table.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 704.9 | **LOC:** 2258 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.7364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createTable` **(Many-Argument Workhorses)** (Impact: 16.7)
  * `tableRowClassName` **(Defensive Guards)** (Impact: 6.1)
  * `sortMethod` **(Compute Cores)** (Impact: 5.7)
  * `getSummary` **(Callbacks & Closures)** (Impact: 5.1)
  * `createInstance` **(Callbacks & Closures)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 403
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 352`, `args: 329`, `func_start: 93`
* *Risk/State:* `state_mutation: 90`, `fragile_debt: 11`, `duplicate_logic: 48`
* *Architecture:* `concurrency: 143`, `import: 1`
* *Defense:* `safety: 9`, `test: 299`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/popper.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 637.18 | **LOC:** 1277 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.7829%), Tech Debt (10.4273%)
**Top Internal Functions/Classes:**
  * `Popper` **(Defensive Guards)** (Impact: 26.2)
    * *Intent:* * then, if even in its new placement, the popper is overlapping its reference element, it will be mo...
  * `_getBoundaries` **(Defensive Guards)** (Impact: 24.9)
    * *Intent:* /** * Computed the boundaries limits and return them * @method * @memberof Popper * @access private ...
  * `parse` **(Defensive Guards)** (Impact: 24.3)
    * *Intent:* /** * Helper used to generate poppers from a configuration file * @method * @memberof Popper * @para...
  * `flip` **(Defensive Guards)** (Impact: 22.7)
    * *Intent:* /** * Modifier used to flip the placement of the popper when the latter is starting overlapping its ...
  * `arrow` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* /** * Modifier used to move the arrows on the edge of the popper to make sure them are always betwee...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 83 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 164`, `args: 55`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 130`, `dead_code: 13`, `fragile_debt: 1`
* *Architecture:* `api: 6`
* *Defense:* `safety: 66`, `doc: 39`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/select/src/select.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 631.8 | **LOC:** 901 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visible` **(Compute Cores)** (Impact: 33.9)
  * `handleQueryChange` **(Defensive Guards)** (Impact: 28.7)
  * `value` **(Compute Cores)** (Impact: 21.8)
  * `handleOptionSelect` **(Compute Cores)** (Impact: 20.5)
  * `emptyText` **(Defensive Guards)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 77 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 103`, `args: 85`, `func_start: 56`, `class_start: 12`
* *Risk/State:* `state_mutation: 83`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 55`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/picker.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 620.16 | **LOC:** 957 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.0633%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mountPicker` **(Defensive Guards)** (Impact: 21.2)
  * `handleKeydown` **(Defensive Guards)** (Impact: 19.6)
  * `valueEquals` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* /* * Considers: * 1. Date object * 2. date string * 3. array of 1 or 2 */
  * `updateOptions` **(Defensive Guards)** (Impact: 17.4)
  * `displayValue` **(Defensive Guards)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 125`, `args: 97`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 90`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/model/node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 552.94 | **LOC:** 485 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.6657%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setChecked` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `constructor` **(Defensive Guards)** (Impact: 37.5)
  * `insertChild` **(Defensive Guards)** (Impact: 25.6)
  * `expand` **(Compute Cores)** (Impact: 18.7)
  * `reInitChecked` **(Defensive Guards)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 64`, `args: 38`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 75`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util, merge, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/panel/date-range.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 490.38 | **LOC:** 681 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.0949%), Tech Debt (10.2085%)
**Top Internal Functions/Classes:**
  * `handleDateInput` **(Defensive Guards)** (Impact: 20.3)
  * `value` **(Defensive Guards)** (Impact: 19.7)
  * `handleMinTimePick` **(Compute Cores)** (Impact: 14.7)
  * `handleMaxTimePick` **(Compute Cores)** (Impact: 14.7)
  * `isValidValue` **(Defensive Guards)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 71`, `args: 101`, `func_start: 49`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 83`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.562
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001971
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/table/src/table-header.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 418.02 | **LOC:** 512 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.2736%), Tech Debt (49.14%)
**Top Internal Functions/Classes:**
  * `handleSortClick` **(Defensive Guards)** (Impact: 32.2)
  * `handleMouseMove` **(Compute Cores)** (Impact: 27.4)
  * `getHeaderCellClass` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `render` **(Compute Cores)** (Impact: 18.0)
  * `traverse` **(Compute Cores)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 86`, `args: 50`, `func_start: 32`
* *Risk/State:* `state_mutation: 65`, `unreferenced_by_name: 10`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` filter-panel.vue, layout-observer, helper, checkbox, dom, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/color-picker/src/color.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 403.38 | **LOC:** 318 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.9925%), Tech Debt (63.441%)
**Top Internal Functions/Classes:**
  * `fromHSV` **(Defensive Guards)** (Impact: 69.5)
  * `fromString` **(Defensive Guards)** (Impact: 52.1)
  * `rgb2hsv` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* // `rgbToHsv` // Converts an RGB color value to HSV // *Assumes:* r, g, and b are contained in the s...
  * `doOnChange` **(I/O & Config Routines)** (Impact: 13.7)
  * `set` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 44`, `args: 24`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/components/theme-configurator/editor/color-picker/src/color.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 396.56 | **LOC:** 317 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.5279%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fromHSV` **(Defensive Guards)** (Impact: 65.5)
  * `fromString` **(Defensive Guards)** (Impact: 49.3)
  * `rgb2hsv` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* // `rgbToHsv` // Converts an RGB color value to HSV // *Assumes:* r, g, and b are contained in the s...
  * `doOnChange` **(I/O & Config Routines)** (Impact: 13.7)
  * `set` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 43`, `args: 24`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/table/src/table-body.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 362.38 | **LOC:** 470 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.478%), Tech Debt (62.8473%)
**Top Internal Functions/Classes:**
  * `wrappedRowRender` **(Defensive Guards)** (Impact: 56.5)
  * `traverse` **(Defensive Guards)** (Impact: 35.3)
  * `getRowClass` **(Defensive Guards)** (Impact: 22.5)
  * `handleCellMouseEnter` **(Compute Cores)** (Impact: 20.8)
  * `getCellClass` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 73`, `args: 40`, `func_start: 28`
* *Risk/State:* `state_mutation: 36`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` layout-observer, helper, table-row.js, util, checkbox, tooltip, dom, util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/basic/date-table.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 357.08 | **LOC:** 442 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.6444%), Tech Debt (8.6217%)
**Top Internal Functions/Classes:**
  * `getCellClasses` **(Defensive Guards)** (Impact: 36.3)
  * `rows` **(Defensive Guards)** (Impact: 32.3)
  * `handleClick` **(Defensive Guards)** (Impact: 30.8)
  * `markRange` **(Defensive Guards)** (Impact: 20.2)
  * `isWeekActive` **(Defensive Guards)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 46`, `args: 27`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 52`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/panel/date.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 339.04 | **LOC:** 610 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.3454%), Tech Debt (11.6081%)
**Top Internal Functions/Classes:**
  * `selectionMode` **(Defensive Guards)** (Impact: 14.8)
  * `value` **(Defensive Guards)** (Impact: 13.2)
  * `emit` **(Defensive Guards)** (Impact: 12.7)
  * `handleDatePick` **(Defensive Guards)** (Impact: 12.2)
  * `handleTimePick` **(State Mutators)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 61`, `args: 74`, `func_start: 48`, `class_start: 9`
* *Risk/State:* `state_mutation: 46`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `safety: 45`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.562
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001971
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/cascader/src/cascader.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 327.84 | **LOC:** 664 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.907%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleSuggestionKeyDown` **(Compute Cores)** (Impact: 13.7)
  * `mounted` **(Compute Cores)** (Impact: 13.5)
  * `handleInput` **(Compute Cores)** (Impact: 10.9)
  * `genTag` **(Compute Cores)** (Impact: 9.9)
  * `filterMethod` **(Callbacks & Closures)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 76`, `args: 63`, `func_start: 45`, `class_start: 7`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/select.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 323.56 | **LOC:** 911 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSelectVm` **(Compute Cores)** (Impact: 11.5)
  * `getSelectComponentVm` **(Callbacks & Closures)** (Impact: 8.4)
  * `filterMethod` **(Callbacks & Closures)** (Impact: 7.5)
  * `data` **(I/O & Config Routines)** (Impact: 4.9)
  * `remoteMethod` **(Callbacks & Closures)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 158
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 124`, `args: 96`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `planned_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 38`, `import: 2`
* *Defense:* `safety: 3`, `test: 97`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util, select
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/tree.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 312.84 | **LOC:** 894 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.7919%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadNode` **(Defensive Guards)** (Impact: 5.9)
  * `loadNode` **(Defensive Guards)** (Impact: 5.9)
  * `loadNode` **(Defensive Guards)** (Impact: 5.9)
  * `loadNode` **(Defensive Guards)** (Impact: 5.8)
  * `loadNode` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 114
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 119`, `args: 101`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `duplicate_logic: 6`
* *Architecture:* `concurrency: 39`, `import: 1`
* *Defense:* `safety: 6`, `test: 154`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/table/src/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 310.9 | **LOC:** 274 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.383%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `orderBy` **(Defensive Guards)** (Impact: 66.5)
  * `toggleRowStatus` **(Defensive Guards)** (Impact: 21.4)
  * `walkTreeNode` **(Many-Argument Workhorses)** (Impact: 14.8)
  * `getRowIdentity` **(Defensive Guards)** (Impact: 13.0)
  * `removeRow` **(Defensive Guards)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 83`, `args: 34`, `func_start: 22`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/model/tree-store.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 283.96 | **LOC:** 341 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.7228%), Tech Debt (97.9864%)
**Top Internal Functions/Classes:**
  * `_setCheckedKeys` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `filter` **(Defensive Guards)** (Impact: 15.6)
  * `traverse` **(Defensive Guards)** (Impact: 15.3)
  * `getCheckedNodes` **(Callbacks & Closures)** (Impact: 14.8)
  * `traverse` **(Callbacks & Closures)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 43`, `args: 47`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 17`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/tree.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 277.18 | **LOC:** 497 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `created` **(Defensive Guards)** (Impact: 61.1)
  * `handleKeydown` **(Defensive Guards)** (Impact: 15.4)
  * `getNodePath` **(Defensive Guards)** (Impact: 7.7)
  * `setCheckedNodes` **(State Mutators)** (Impact: 3.7)
  * `setCheckedKeys` **(State Mutators)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 45`, `args: 44`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001752
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/table/src/store/watcher.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 275.52 | **LOC:** 382 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.6867%), Tech Debt (12.5945%)
**Top Internal Functions/Classes:**
  * `clearFilter` **(Defensive Guards)** (Impact: 15.0)
  * `updateAllSelected` **(Defensive Guards)** (Impact: 14.9)
  * `_toggleAllSelection` **(I/O & Config Routines)** (Impact: 11.4)
  * `updateColumns` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* // 更新列
  * `toggleRowSelection` **(State Mutators)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 49`, `args: 40`, `func_start: 23`
* *Risk/State:* `state_mutation: 47`, `planned_debt: 2`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.894
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001314
  * `Imports (Out-Degree: 3):` util, current, expand, tree, merge, vue
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/unit/specs/form.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 273.78 | **LOC:** 994 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.9093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkName` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `checkName` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `checkName` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `validator` **(Callbacks & Closures)** (Impact: 4.5)
  * `keyDown` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 99
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 130`, `args: 100`, `func_start: 40`
* *Risk/State:* `state_mutation: 56`, `duplicate_logic: 23`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 24`, `import: 2`
* *Defense:* `safety: 4`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util, es6-promise
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/cascader.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 255.74 | **LOC:** 417 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `filterMethod` **(Parameter Forwarders)** (Impact: 3.7)
  * `getCloseButton` **(Tests & Verification)** (Impact: 3.0)
  * `getOptions` **(Parameter Forwarders)** (Impact: 1.9)
  * `getMenus` **(Interface Declarations)** (Impact: 1.5)
  * `data` **(Interface Declarations)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 198
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 62`, `args: 31`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`, `duplicate_logic: 7`
* *Architecture:* `concurrency: 43`, `import: 2`
* *Defense:* `test: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util, cascader
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/date-util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 241.78 | **LOC:** 283 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.7644%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `getRangeMinutes` **(Defensive Guards)** (Impact: 25.5)
  * `limitTimeRange` **(Callbacks & Closures)** (Impact: 11.2)
  * `getRangeHours` **(Callbacks & Closures)** (Impact: 9.6)
  * `extractDateFormat` **(Callbacks & Closures)** (Impact: 8.8)
  * `extractTimeFormat` **(Callbacks & Closures)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 106`, `args: 49`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `planned_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 33`, `import: 2`
* *Defense:* `safety: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` locale, date
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/date-picker/src/picker/date-picker.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 96.0834%)
- `packages/date-picker/src/picker/time-picker.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9994%)
- `src/utils/vue-popper.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/utils/dom.js` -> **Severity: 1.166** (Embedded: 0.0177 * Error Risk: 65.8618%)
- `src/utils/merge.js` -> **Severity: 0.565** (Embedded: 0.008 * Error Risk: 70.2063%)
- `packages/main/index.js` -> **Severity: 0.539** (Embedded: 0.0079 * Error Risk: 68.383%)
- `src/utils/aria-utils.js` -> **Severity: 0.359** (Embedded: 0.0042 * Error Risk: 85.442%)
- `packages/table/src/layout-observer.js` -> **Severity: 0.355** (Embedded: 0.0039 * Error Risk: 89.9811%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/utils/dom.js` -> **Severity: 934.1** (Blast Radius: 9.341 * Doc Risk: 100.0%)
- `packages/main/index.js` -> **Severity: 374.2** (Blast Radius: 3.742 * Doc Risk: 100.0%)
- `src/utils/types.js` -> **Severity: 254.583** (Blast Radius: 3.055 * Doc Risk: 83.3333%)
- `src/mixins/locale.js` -> **Severity: 233.9** (Blast Radius: 2.339 * Doc Risk: 100.0%)
- `src/utils/vue-popper.js` -> **Severity: 233.0** (Blast Radius: 2.33 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
