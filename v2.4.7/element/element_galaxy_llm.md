# ARCHITECTURAL_BRIEF: element
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/element` |
| **Timestamp** | `2026-08-07T04:34:53.778806+00:00` |
| **Scan Duration** | `3.12s` |
| **Git Branch** | `dev` |
| **Git Commit** | `c345bb453bf11badb4831a6a3f600c9372b3a336` |
| **Git Remote** | `https://github.com/ElemeFE/element.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 412 malicious artifacts.

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
| Total Artifacts | 1144 |
| Analyzed Artifacts (Scanned) | 747 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 397 |
| Total LOC | 79090 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 65.3% |
| Dominant Lang | HTML |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4813 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2973 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6252 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 29 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 320 | 38712 | 42.8% |
| CSS | 162 | 12428 | 21.7% |
| HTML | 151 | 25103 | 20.2% |
| TYPESCRIPT | 91 | 1644 | 12.2% |
| JSON | 11 | 1157 | 1.5% |
| MARKDOWN | 8 | 0 | 1.1% |
| PLAINTEXT | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 33 | 0.1% |
| XML | 1 | 13 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.355`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 555 | 74.3% |
| file_cluster_0 | 63 | 8.4% |
| file_cluster_13 | 40 | 5.4% |
| file_cluster_16 | 37 | 5.0% |
| file_cluster_17 | 28 | 3.7% |
| file_cluster_4 | 8 | 1.1% |
| file_cluster_15 | 2 | 0.3% |
| file_cluster_11 | 2 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 1.3% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 397*

**Composition by Extension & Reason:**
- `.md`: 270x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 46x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.svg`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tpl`: 11x Excluded (Unsupported Extension: '.tpl')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vue`: 4x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff`: 2x Excluded (Explicitly Denied Extension: '.woff')
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1275 LOC), 1x Excluded (Massive Static Asset Blob: 4196 LOC)
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 22.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 27.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.7 | 0.8 | 0.0 |
| API Exposure | 0.0 | 18.0 | 3.9 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 42.5 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 82.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 24.4 | 19.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/utils/lodash.js` (Hits: 82)
- `examples/components/footer.vue` (Hits: 37)
- `examples/route.config.js` (Hits: 29)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **var.scss** (`packages/theme-chalk/src/common/var.scss`) — 86 inbound connections
2. **mixins.scss** (`packages/theme-chalk/src/mixins/mixins.scss`) — 78 inbound connections
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

- `isString` (@ `packages/date-picker/src/picker.vue`) -> Impact: **286.2** | LOC: 605
- `describe` (@ `test/unit/specs/table.spec.js`) -> Impact: **114.7** | LOC: 1635
- `removeResizeListener` (@ `packages/cascader/src/cascader.vue`) -> Impact: **110.2** | LOC: 281
- `describe` (@ `test/unit/specs/select.spec.js`) -> Impact: **95.6** | LOC: 907
- `created` (@ `packages/tree/src/tree.vue`) -> Impact: **90.2** | LOC: 163
- `describe` (@ `test/unit/specs/tree.spec.js`) -> Impact: **89.5** | LOC: 889
- `stop` (@ `src/utils/vue-popper.js`) -> Impact: **88.9** | LOC: 185
- `Popper` (@ `src/utils/popper.js`) -> Impact: **80.2** | LOC: 204
- `install` (@ `packages/loading/src/directive.js`) -> Impact: **73.7** | LOC: 123
- `describe` (@ `test/unit/specs/form.spec.js`) -> Impact: **70.2** | LOC: 989

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `test/unit/specs` | 63 | 9443.18 | 8.47% | 0.0% |
| `src/utils` | 18 | 3781.48 | 49.85% | 61.18% |
| `packages/date-picker/src/panel` | 6 | 2656.46 | 72.88% | 13.44% |
| `packages/table/src` | 12 | 2446.98 | 64.37% | 59.3% |
| `packages/select/src` | 5 | 1841.52 | 66.99% | 36.72% |
| `packages/date-picker/src` | 1 | 1645.76 | 93.37% | 94.26% |
| `packages/tree/src/model` | 3 | 1259.38 | 72.25% | 64.19% |
| `packages/date-picker/src/basic` | 4 | 1106.04 | 70.47% | 54.21% |
| `packages/slider/src` | 3 | 991.16 | 82.56% | 33.3% |
| `packages/menu/src` | 5 | 942.8 | 71.25% | 52.58% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/divider/src/main.vue` -> **100.0%** Exposure
- `packages/pagination/src/pagination.js` -> **100.0%** Exposure
- `packages/table/src/config.js` -> **100.0%** Exposure
- `src/mixins/emitter.js` -> **100.0%** Exposure
- `src/utils/date-util.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `examples/components/demo-block.vue` -> **100.0%** Exposure
- `examples/components/footer-nav.vue` -> **100.0%** Exposure
- `examples/components/search.vue` -> **100.0%** Exposure
- `examples/components/side-nav.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/borderRadius.vue` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/specs/table.spec.js` -> **1** Orphaned Functions | **308** Duplicates
- `test/unit/specs/date-picker.spec.js` -> **1** Orphaned Functions | **128** Duplicates
- `test/unit/specs/form.spec.js` -> **3** Orphaned Functions | **102** Duplicates
- `test/unit/specs/tree.spec.js` -> **2** Orphaned Functions | **93** Duplicates
- `test/unit/specs/select.spec.js` -> **1** Orphaned Functions | **86** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`test/ssr/require.test.js`** -> AI Confidence: **99.29%**
2. **`test/unit/index.js`** -> AI Confidence: **99.29%**
3. **`packages/table/src/store/index.js`** -> AI Confidence: **99.2%**
4. **`packages/table/src/table-body.js`** -> AI Confidence: **99.18%**
5. **`examples/components/theme-configurator/editor/color-picker/src/color.js`** -> AI Confidence: **99.17%**
6. **`packages/color-picker/src/color.js`** -> AI Confidence: **99.17%**
7. **`packages/descriptions/src/descriptions-item.js`** -> AI Confidence: **99.17%**
8. **`packages/popover/src/directive.js`** -> AI Confidence: **99.17%**
9. **`src/directives/mousewheel.js`** -> AI Confidence: **99.17%**
10. **`src/utils/aria-dialog.js`** -> AI Confidence: **99.17%**
11. **`src/utils/menu/aria-menuitem.js`** -> AI Confidence: **99.17%**
12. **`src/utils/menu/aria-submenu.js`** -> AI Confidence: **99.17%**
13. **`packages/tree/src/model/node.js`** -> AI Confidence: **99.14%**
14. **`src/utils/vue-popper.js`** -> AI Confidence: **99.14%**
15. **`packages/loading/src/directive.js`** -> AI Confidence: **99.13%**
16. **`packages/loading/src/index.js`** -> AI Confidence: **99.13%**
17. **`packages/pagination/src/pagination.js`** -> AI Confidence: **99.13%**
18. **`packages/table/src/store/watcher.js`** -> AI Confidence: **99.13%**
19. **`packages/table/src/table-header.js`** -> AI Confidence: **99.13%**
20. **`packages/tooltip/src/main.js`** -> AI Confidence: **99.13%**
21. **`src/utils/popup/index.js`** -> AI Confidence: **99.13%**
22. **`packages/table/src/store/tree.js`** -> AI Confidence: **99.11%**
23. **`examples/entry.js`** -> AI Confidence: **99.09%**
24. **`packages/date-picker/src/picker/time-picker.js`** -> AI Confidence: **99.09%**
25. **`packages/infinite-scroll/src/main.js`** -> AI Confidence: **99.09%**
26. **`packages/table/src/table-column.js`** -> AI Confidence: **99.09%**
27. **`packages/table/src/table-layout.js`** -> AI Confidence: **99.09%**
28. **`src/index.js`** -> AI Confidence: **99.09%**
29. **`types/element-ui.d.ts`** -> AI Confidence: **99.09%**
30. **`examples/extension/src/entry.js`** -> AI Confidence: **99.06%**
31. **`packages/cascader-panel/src/node.js`** -> AI Confidence: **99.06%**
32. **`packages/col/src/col.js`** -> AI Confidence: **99.06%**
33. **`packages/date-picker/src/picker/date-picker.js`** -> AI Confidence: **99.06%**
34. **`packages/descriptions/src/index.js`** -> AI Confidence: **99.06%**
35. **`packages/input/src/calcTextareaHeight.js`** -> AI Confidence: **99.06%**
36. **`packages/menu/src/menu-mixin.js`** -> AI Confidence: **99.06%**
37. **`packages/message-box/src/main.js`** -> AI Confidence: **99.06%**
38. **`packages/row/src/row.js`** -> AI Confidence: **99.06%**
39. **`packages/scrollbar/src/main.js`** -> AI Confidence: **99.06%**
40. **`packages/select/src/navigation-mixin.js`** -> AI Confidence: **99.06%**
41. **`packages/table/src/dropdown.js`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `396` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/tooltip/src/main.js` (JAVASCRIPT) -> Cumulative Risk: **683.14**
- **Archetype:** `file_cluster_13` (Distance: 13.492 IQR)
- **Magnitude:** 383.88 | **LOC:** 243 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6728%), Safety Score (97.6059%)
- **Heaviest Functions:** `removeClass` (Impact: 29.6), `mounted` (Impact: 19.9), `on` (Impact: 18.6)

### 2. `src/utils/popup/index.js` (JAVASCRIPT) -> Cumulative Risk: **671.55**
- **Archetype:** `file_cluster_4` (Distance: 13.354 IQR)
- **Magnitude:** 298.16 | **LOC:** 219 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.3837%), Safety Score (98.3427%)
- **Heaviest Functions:** `doOpen` (Impact: 26.5), `open` (Impact: 9.6), `close` (Impact: 9.5)

### 3. `packages/table/src/store/index.js` (JAVASCRIPT) -> Cumulative Risk: **618.61**
- **Archetype:** `file_cluster_13` (Distance: 13.31 IQR)
- **Magnitude:** 188.8 | **LOC:** 148 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (95.8142%), Tech Debt (94.8664%), Cognitive Load (91.6367%)
- **Heaviest Functions:** `insertColumn` (Impact: 16.8), `removeColumn` (Impact: 10.8), `setData` (Impact: 9.8)

### 4. `packages/table/src/util.js` (JAVASCRIPT) -> Cumulative Risk: **604.15**
- **Archetype:** `file_cluster_17` (Distance: 12.964 IQR)
- **Magnitude:** 345.5 | **LOC:** 274 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9632%), State Flux (99.9499%), Documentation (94.628%)
- **Heaviest Functions:** `orderBy` (Impact: 66.5), `toggleRowStatus` (Impact: 21.4), `walkTreeNode` (Impact: 14.8)

### 5. `src/utils/util.js` (JAVASCRIPT) -> Cumulative Risk: **594.68**
- **Archetype:** `file_cluster_11` (Distance: 12.572 IQR)
- **Magnitude:** 260.32 | **LOC:** 246 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.7662%), Cognitive Load (84.5261%)
- **Heaviest Functions:** `getPropByPath` (Impact: 21.2), `isEmpty` (Impact: 18.5), `getValueByPath` (Impact: 13.0)

### 6. `packages/tree/src/model/node.js` (JAVASCRIPT) -> Cumulative Risk: **588.51**
- **Archetype:** `file_cluster_17` (Distance: 14.617 IQR)
- **Magnitude:** 781.94 | **LOC:** 485 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.426%), Tech Debt (92.6685%)
- **Heaviest Functions:** `setChecked` (Impact: 40.6), `constructor` (Impact: 37.5), `insertChild` (Impact: 25.6)

### 7. `src/utils/popup/popup-manager.js` (JAVASCRIPT) -> Cumulative Risk: **587.24**
- **Archetype:** `file_cluster_8` (Distance: 12.039 IQR)
- **Magnitude:** 182.02 | **LOC:** 195 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9964%), Cognitive Load (88.7214%)
- **Heaviest Functions:** `openModal` (Impact: 36.4), `closeModal` (Impact: 20.4), `getModal` (Impact: 8.2)

### 8. `packages/message-box/src/main.js` (JAVASCRIPT) -> Cumulative Risk: **580.28**
- **Archetype:** `file_cluster_8` (Distance: 11.638 IQR)
- **Magnitude:** 188.0 | **LOC:** 217 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9669%), State Flux (93.3583%), Concurrency (92.5782%)
- **Heaviest Functions:** `showNextMsg` (Impact: 24.7), `defaultCallback` (Impact: 23.7), `initInstance` (Impact: 22.8)

### 9. `packages/table/src/table-header.js` (JAVASCRIPT) -> Cumulative Risk: **571.35**
- **Archetype:** `file_cluster_8` (Distance: 13.113 IQR)
- **Magnitude:** 502.42 | **LOC:** 512 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (94.1322%), Safety Score (85.9266%)
- **Heaviest Functions:** `handleSortClick` (Impact: 32.2), `handleMouseMove` (Impact: 27.4), `getHeaderCellClass` (Impact: 19.4)

### 10. `packages/tree/src/model/tree-store.js` (JAVASCRIPT) -> Cumulative Risk: **568.74**
- **Archetype:** `file_cluster_17` (Distance: 13.52 IQR)
- **Magnitude:** 448.46 | **LOC:** 341 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8944%), Safety Score (95.1979%)
- **Heaviest Functions:** `_setCheckedKeys` (Impact: 28.1), `filter` (Impact: 15.6), `traverse` (Impact: 15.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/utils/lodash.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.151 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.402 IQR)
- **Top Global Matches:** file_cluster_0: 14.151, file_cluster_8: 14.162, file_cluster_7: 14.296
- **Magnitude:** 1776.62 | **LOC:** 18076 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.7859%), Tech Debt (14.8513%)
**Top Internal Functions/Classes:**
  * `baseForOwn` (Impact: 46.4)
    * *Intent:* /** * Creates a `_.range` or `_.rangeRight` function. *
  * `slice` (Impact: 16.5)
    * *Intent:* /** * Creates a function that wraps `func` to invoke it with the `this` binding * of `thisArg` and `...
  * `arrayEach` (Impact: 14.8)
  * `arrayEach` (Impact: 13.3)
  * `times` (Impact: 7.8)
    * *Intent:* /** * Creates a clone of `dataView`. * * @private * @param {Object} dataView The data view to clone.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1111`, `structural_boundaries: 997`, `args: 425`, `func_start: 393`
* *Risk/State:* `safety_bypasses: 149`, `state_mutation: 1427`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 82`, `api: 1`, `concurrency: 53`, `import: 1`
* *Defense:* `safety: 215`, `doc: 1499`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/picker.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.538 IQR)
- **Top Global Matches:** file_cluster_17: 14.538, file_cluster_0: 14.603, file_cluster_11: 14.676
- **Magnitude:** 1645.76 | **LOC:** 957 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.3681%), Tech Debt (94.2558%)
**Top Internal Functions/Classes:**
  * `isString` (Impact: 286.2)
  * `mountPicker` (Impact: 28.7)
  * `displayValue` (Impact: 23.5)
  * `handleKeydown` (Impact: 22.4)
  * `valueEquals` (Impact: 18.7)
    * *Intent:* /* * Considers: * 1. Date object * 2. date string * 3. array of 1 or 2 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 126`, `args: 97`, `func_start: 72`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 844`, `dead_code: 1`, `duplicate_logic: 18`
* *Architecture:* `api: 11`, `concurrency: 6`, `import: 7`
* *Defense:* `safety: 90`, `immutability_locks: 67`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/select/src/select.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.517 IQR)
- **Top Global Matches:** file_cluster_0: 14.517, file_cluster_11: 14.563, file_cluster_13: 14.605
- **Magnitude:** 1440.88 | **LOC:** 901 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.669%), Tech Debt (36.8232%)
**Top Internal Functions/Classes:**
  * `visible` (Impact: 33.9)
  * `handleQueryChange` (Impact: 28.7)
  * `value` (Impact: 21.8)
  * `checkDefaultFirstOption` (Impact: 21.2)
  * `emptyText` (Impact: 20.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 99`, `args: 85`, `func_start: 59`, `class_start: 12`
* *Risk/State:* `state_mutation: 956`, `duplicate_logic: 6`
* *Architecture:* `api: 15`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 55`, `doc: 1`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/table.spec.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.125 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.585 IQR)
- **Top Global Matches:** file_cluster_8: 10.125, file_cluster_4: 10.681, file_cluster_7: 10.826
- **Magnitude:** 1399.6 | **LOC:** 2258 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.4047%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 114.7)
  * `describe` (Impact: 51.7)
  * `describe` (Impact: 19.5)
  * `describe` (Impact: 18.4)
  * `createTable` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 352`, `args: 329`, `func_start: 687`
* *Risk/State:* `state_mutation: 88`, `fragile_debt: 11`, `duplicate_logic: 308`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 218`, `import: 1`
* *Defense:* `safety: 9`, `test: 299`, `immutability_locks: 171`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/panel/date-range.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.191 IQR)
- **Top Global Matches:** file_cluster_0: 14.191, file_cluster_13: 14.433, file_cluster_11: 14.447
- **Magnitude:** 972.8 | **LOC:** 681 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2087%), Tech Debt (12.1767%)
**Top Internal Functions/Classes:**
  * `handleDateInput` (Impact: 20.3)
  * `value` (Impact: 19.7)
  * `handleRangePick` (Impact: 14.9)
  * `handleMinTimePick` (Impact: 14.7)
  * `handleMaxTimePick` (Impact: 14.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 71`, `args: 101`, `func_start: 52`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 663`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 6`, `import: 7`
* *Defense:* `safety: 39`, `immutability_locks: 33`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00134
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/date-picker/src/panel/date.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.197 IQR)
- **Top Global Matches:** file_cluster_0: 14.197, file_cluster_11: 14.379, file_cluster_13: 14.416
- **Magnitude:** 800.82 | **LOC:** 610 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.012%), Tech Debt (46.5209%)
**Top Internal Functions/Classes:**
  * `handleDatePick` (Impact: 15.0)
  * `selectionMode` (Impact: 14.8)
  * `value` (Impact: 13.2)
  * `emit` (Impact: 12.7)
  * `handleTimePick` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 61`, `args: 74`, `func_start: 51`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 527`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 9`
* *Defense:* `safety: 49`, `doc: 4`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/model/node.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.617 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.205 IQR)
- **Top Global Matches:** file_cluster_17: 14.617, file_cluster_8: 14.69, file_cluster_11: 14.721
- **Magnitude:** 781.94 | **LOC:** 485 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.247%), Tech Debt (92.6685%)
**Top Internal Functions/Classes:**
  * `setChecked` (Impact: 40.6)
  * `constructor` (Impact: 37.5)
  * `insertChild` (Impact: 25.6)
  * `expand` (Impact: 18.7)
  * `getChildren` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 62`, `args: 38`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 422`, `duplicate_logic: 8`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 50`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util, util, merge
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cascader/src/cascader.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.43 IQR)
- **Top Global Matches:** file_cluster_13: 12.43, file_cluster_8: 12.493, file_cluster_0: 12.529
- **Magnitude:** 671.74 | **LOC:** 664 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.9399%), Tech Debt (18.5615%)
**Top Internal Functions/Classes:**
  * `removeResizeListener` (Impact: 110.2)
  * `handleSuggestionKeyDown` (Impact: 19.4)
  * `mounted` (Impact: 18.5)
  * `handleKeyDown` (Impact: 13.5)
  * `updateStyle` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 69`, `args: 63`, `func_start: 46`, `class_start: 7`
* *Risk/State:* `state_mutation: 287`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 6`, `import: 16`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/slider/src/main.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.064 IQR)
- **Top Global Matches:** file_cluster_0: 14.064, file_cluster_17: 14.214, file_cluster_8: 14.266
- **Magnitude:** 667.86 | **LOC:** 428 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setValues` (Impact: 33.0)
  * `mounted` (Impact: 14.2)
  * `stops` (Impact: 13.8)
  * `setPosition` (Impact: 9.2)
  * `value` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 50`, `args: 45`, `func_start: 26`, `class_start: 6`
* *Risk/State:* `state_mutation: 506`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* `safety: 16`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/date-picker.spec.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.222 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.25 IQR)
- **Top Global Matches:** file_cluster_8: 9.222, file_cluster_7: 10.013, file_cluster_1: 10.055
- **Magnitude:** 549.04 | **LOC:** 2856 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.2575%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it` (Impact: 26.0)
  * `setTimeout` (Impact: 25.5)
  * `setTimeout` (Impact: 25.3)
    * *Intent:* // check timestamp is parsed internally
  * `describe` (Impact: 22.2)
  * `it` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 143`, `args: 120`, `func_start: 280`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `duplicate_logic: 128`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 75`, `import: 2`
* *Defense:* `test: 130`, `immutability_locks: 101`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` date-picker, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/basic/date-table.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.383 IQR)
- **Top Global Matches:** file_cluster_17: 14.383, file_cluster_0: 14.426, file_cluster_11: 14.54
- **Magnitude:** 522.16 | **LOC:** 442 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.3774%), Tech Debt (65.9028%)
**Top Internal Functions/Classes:**
  * `rows` (Impact: 43.9)
  * `getCellClasses` (Impact: 36.3)
  * `handleClick` (Impact: 30.8)
  * `markRange` (Impact: 21.9)
  * `isWeekActive` (Impact: 14.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 47`, `args: 27`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 299`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 63`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/tree.spec.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.199 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.457 IQR)
- **Top Global Matches:** file_cluster_8: 10.199, file_cluster_4: 10.712, file_cluster_2: 10.751
- **Magnitude:** 517.94 | **LOC:** 894 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.2604%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 89.5)
  * `it` (Impact: 7.2)
  * `it` (Impact: 6.9)
  * `it` (Impact: 6.6)
  * `it` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 119`, `args: 101`, `func_start: 233`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 48`, `duplicate_logic: 93`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 69`, `import: 1`
* *Defense:* `safety: 6`, `test: 154`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/table/src/table-header.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.113 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.504 IQR)
- **Top Global Matches:** file_cluster_8: 13.113, file_cluster_17: 13.192, file_cluster_13: 13.226
- **Magnitude:** 502.42 | **LOC:** 512 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.0477%), Tech Debt (94.1322%)
**Top Internal Functions/Classes:**
  * `handleSortClick` (Impact: 32.2)
  * `handleMouseMove` (Impact: 27.4)
  * `getHeaderCellClass` (Impact: 19.4)
  * `render` (Impact: 18.0)
  * `handleFilterClick` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 86`, `args: 50`, `func_start: 39`
* *Risk/State:* `state_mutation: 236`, `duplicate_logic: 7`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 25`, `immutability_locks: 39`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` checkbox, dom, filter-panel.vue, helper, vue, layout-observer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/form.spec.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.967 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_8: 8.967, file_cluster_7: 9.788, file_cluster_1: 9.972
- **Magnitude:** 497.98 | **LOC:** 994 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.0452%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 70.2)
  * `describe` (Impact: 44.3)
  * `it` (Impact: 8.6)
  * `it` (Impact: 7.6)
  * `it` (Impact: 6.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 130`, `args: 100`, `func_start: 177`
* *Risk/State:* `state_mutation: 42`, `duplicate_logic: 102`, `orphaned_logic: 3`
* *Architecture:* `concurrency: 24`, `import: 2`
* *Defense:* `safety: 4`, `test: 89`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` es6-promise, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/table/src/table.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.994 IQR)
- **Top Global Matches:** file_cluster_0: 11.994, file_cluster_8: 12.151, file_cluster_13: 12.284
- **Magnitude:** 463.2 | **LOC:** 713 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5239%), Tech Debt (89.2832%)
**Top Internal Functions/Classes:**
  * `fixedHeight` (Impact: 13.8)
  * `syncPostion` (Impact: 13.5)
    * *Intent:* // TODO 使用 CSS transform
  * `handleFixedMousewheel` (Impact: 12.9)
  * `fixedBodyHeight` (Impact: 12.3)
  * `resizeListener` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 62`, `args: 47`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `state_mutation: 266`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 14`, `concurrency: 6`, `import: 12`
* *Defense:* `safety: 8`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/model/tree-store.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.52 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_17: 13.52, file_cluster_8: 13.614, file_cluster_11: 13.849
- **Magnitude:** 448.46 | **LOC:** 341 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.2325%), Tech Debt (99.8944%)
**Top Internal Functions/Classes:**
  * `_setCheckedKeys` (Impact: 28.1)
  * `filter` (Impact: 15.6)
  * `traverse` (Impact: 15.3)
  * `getCheckedNodes` (Impact: 14.8)
  * `traverse` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 41`, `args: 47`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 221`, `duplicate_logic: 5`, `orphaned_logic: 13`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 47`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/autocomplete.spec.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.113 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.865 IQR)
- **Top Global Matches:** file_cluster_8: 11.113, file_cluster_17: 11.563, file_cluster_4: 11.582
- **Magnitude:** 445.28 | **LOC:** 624 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.4247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 50.1)
  * `describe` (Impact: 7.6)
  * `it` (Impact: 7.2)
  * `createVm` (Impact: 6.9)
  * `it` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 114`, `args: 84`, `func_start: 135`
* *Risk/State:* `state_mutation: 142`, `duplicate_logic: 77`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `concurrency: 22`, `import: 1`
* *Defense:* `safety: 11`, `test: 43`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/popper.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.179 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.961 IQR)
- **Top Global Matches:** file_cluster_17: 16.179, file_cluster_11: 16.264, file_cluster_0: 16.362
- **Magnitude:** 439.42 | **LOC:** 1277 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.9671%), Tech Debt (97.782%)
**Top Internal Functions/Classes:**
  * `Popper` (Impact: 80.2)
  * `parse` (Impact: 23.6)
    * *Intent:* /** * Create a new Popper.js instance * @constructor Popper * @param {HTMLElement} reference - The r...
  * `_getOffsets` (Impact: 16.4)
    * *Intent:* // make sure to apply the popper position before any computation
  * `value` (Impact: 15.3)
    * *Intent:* /** * Computed the boundaries limits and return them * @method * @memberof Popper
  * `applyStyle` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 73`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 182`, `dead_code: 10`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 8`
* *Defense:* `safety: 38`, `doc: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/select.spec.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.053 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.105 IQR)
- **Top Global Matches:** file_cluster_8: 9.053, file_cluster_7: 9.847, file_cluster_1: 9.909
- **Magnitude:** 433.26 | **LOC:** 911 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0679%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 95.6)
  * `describe` (Impact: 10.0)
  * `it` (Impact: 8.8)
  * `it` (Impact: 8.1)
  * `it` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 124`, `args: 96`, `func_start: 180`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `planned_debt: 4`, `duplicate_logic: 86`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 38`, `import: 2`
* *Defense:* `safety: 3`, `test: 97`, `immutability_locks: 36`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` select, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/tree.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.718 IQR)
- **Top Global Matches:** file_cluster_8: 12.718, file_cluster_13: 12.809, file_cluster_0: 12.819
- **Magnitude:** 426.24 | **LOC:** 497 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.6764%), Tech Debt (85.7003%)
**Top Internal Functions/Classes:**
  * `created` (Impact: 90.2)
  * `removeClass` (Impact: 28.3)
  * `handleKeydown` (Impact: 15.4)
  * `getNodePath` (Impact: 7.7)
  * `initTabIndex` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 45`, `args: 44`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 178`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 6`, `import: 6`
* *Defense:* `safety: 29`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/rate/src/main.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.136 IQR)
- **Top Global Matches:** file_cluster_0: 13.136, file_cluster_8: 13.173, file_cluster_13: 13.293
- **Magnitude:** 423.2 | **LOC:** 349 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.9456%), Tech Debt (55.8327%)
**Top Internal Functions/Classes:**
  * `handleKey` (Impact: 19.8)
  * `setCurrentValue` (Impact: 14.9)
  * `showDecimalIcon` (Impact: 11.8)
  * `getValueFromMap` (Impact: 9.2)
  * `classes` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 42`, `args: 32`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 280`, `duplicate_logic: 3`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 9`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cascader-panel/src/cascader-panel.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.336 IQR)
- **Top Global Matches:** file_cluster_8: 12.336, file_cluster_17: 12.422, file_cluster_13: 12.447
- **Magnitude:** 410.62 | **LOC:** 392 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.264%), Tech Debt (48.0965%)
**Top Internal Functions/Classes:**
  * `handleKeyDown` (Impact: 27.3)
  * `lazyLoad` (Impact: 24.5)
  * `resolve` (Impact: 20.5)
  * `syncActivePath` (Impact: 12.1)
  * `checkNode` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 50`, `args: 50`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 187`, `duplicate_logic: 3`
* *Architecture:* `io: 5`, `api: 8`, `import: 6`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 55`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/form/src/form-item.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.522 IQR)
- **Top Global Matches:** file_cluster_0: 13.522, file_cluster_11: 13.625, file_cluster_13: 13.655
- **Magnitude:** 401.86 | **LOC:** 325 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.9954%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validate` (Impact: 18.9)
  * `contentStyle` (Impact: 17.8)
  * `getRules` (Impact: 11.8)
  * `getFilteredRule` (Impact: 7.7)
  * `resetField` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 51`, `args: 46`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `state_mutation: 242`
* *Architecture:* `io: 10`, `api: 15`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 22`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tooltip/src/main.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.492 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.743 IQR)
- **Top Global Matches:** file_cluster_13: 13.492, file_cluster_4: 13.504, file_cluster_8: 13.508
- **Magnitude:** 383.88 | **LOC:** 243 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.5562%), Tech Debt (99.6728%)
**Top Internal Functions/Classes:**
  * `removeClass` (Impact: 29.6)
  * `mounted` (Impact: 19.9)
  * `on` (Impact: 18.6)
  * `render` (Impact: 12.8)
  * `getFirstElement` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 29`, `args: 26`, `func_start: 36`
* *Risk/State:* `state_mutation: 202`, `duplicate_logic: 7`
* *Architecture:* `api: 5`, `concurrency: 12`, `import: 5`
* *Defense:* `safety: 4`, `immutability_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dom, debounce, vue, vue-popper, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/input/src/input.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.559 IQR)
- **Top Global Matches:** file_cluster_0: 12.559, file_cluster_13: 12.858, file_cluster_8: 12.89
- **Magnitude:** 382.94 | **LOC:** 441 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.8069%), Tech Debt (57.145%)
**Top Internal Functions/Classes:**
  * `calcIconOffset` (Impact: 15.3)
  * `isWordLimitVisible` (Impact: 10.3)
  * `getSuffixVisible` (Impact: 10.3)
  * `showClear` (Impact: 8.8)
  * `showPwdVisible` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 49`, `args: 49`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `state_mutation: 207`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 15`, `import: 5`
* *Defense:* `safety: 19`, `doc: 3`, `immutability_locks: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/components/footer.vue` (HTML) | Magnitude: 25.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 172, io: 37, decorators: 26, structural_boundaries: 18
- `examples/components/demo-block.vue` (HTML) | Magnitude: 178.98 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 293, state_mutation: 89, structural_boundaries: 33, branch: 25
- `packages/carousel/src/main.vue` (HTML) | Magnitude: 376.06 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 275, state_mutation: 227, branch: 60, args: 42
- `packages/loading/src/loading.vue` (HTML) | Magnitude: 10.88 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, decorators: 11, structural_boundaries: 5, args: 4
- `src/utils/lodash.js` (JAVASCRIPT) | Magnitude: 1776.62 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4874, doc: 1499, state_mutation: 1427, branch: 1111

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/utils/types.js` (JAVASCRIPT) | Magnitude: 31.86 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, safety: 15, indent_spaces: 11, branch: 8
- `src/utils/util.js` (JAVASCRIPT) | Magnitude: 260.32 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 93, branch: 67, state_mutation: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/extension/src/editor/editor.vue` (HTML) | Magnitude: 199.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 169, state_mutation: 120, branch: 24, structural_boundaries: 23
- `src/utils/vue-popper.js` (JAVASCRIPT) | Magnitude: 333.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 163, indent_spaces: 160, branch: 46, structural_boundaries: 20
- `types/popconfirm.d.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, indent_spaces: 8, structural_boundaries: 6, import: 2
- `packages/table/src/table-body.js` (JAVASCRIPT) | Magnitude: 38.28 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 27, state_mutation: 21, func_start: 10
- `packages/container/index.js` (JAVASCRIPT) | Magnitude: 3.7 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: dependency_injection: 5, structural_boundaries: 2, api: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/unit/util.js` (JAVASCRIPT) | Magnitude: 53.64 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, doc: 24, structural_boundaries: 21, immutability_locks: 14
- `src/utils/after-leave.js` (JAVASCRIPT) | Magnitude: 11.88 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 17, branch: 7, doc: 5, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `types/checkbox-group.d.ts` (TYPESCRIPT) | Magnitude: 1.57 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 5, class_start: 1
- `types/submenu.d.ts` (TYPESCRIPT) | Magnitude: 1.57 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, indent_spaces: 6, structural_boundaries: 5, class_start: 1
- `types/link.d.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 8, indent_spaces: 6, api: 2
- `types/row.d.ts` (TYPESCRIPT) | Magnitude: 1.82 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, doc: 8, indent_spaces: 5, api: 3
- `types/color-picker.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, doc: 6, indent_spaces: 5, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/notification/src/main.js` (JAVASCRIPT) | Magnitude: 63.74 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 27, structural_boundaries: 25, branch: 15
- `packages/table/src/store/helper.js` (JAVASCRIPT) | Magnitude: 25.52 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 11, branch: 6, args: 6
- `packages/container/src/main.vue` (HTML) | Magnitude: 23.38 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, branch: 10, structural_boundaries: 7, state_mutation: 6
- `src/utils/menu/aria-menubar.js` (JAVASCRIPT) | Magnitude: 8.54 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, args: 4, state_mutation: 4
- `packages/date-picker/src/basic/date-table.vue` (HTML) | Magnitude: 522.16 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 364, state_mutation: 299, branch: 119, safety: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/components/theme-configurator/index.vue` (HTML) | Magnitude: 171.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 173, state_mutation: 92, structural_boundaries: 26, args: 24
- `examples/extension/src/editor/gallery.vue` (HTML) | Magnitude: 139.74 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 47, args: 28, branch: 23
- `packages/backtop/src/main.vue` (HTML) | Magnitude: 118.12 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 92, state_mutation: 43, args: 15, func_start: 14
- `src/utils/aria-dialog.js` (JAVASCRIPT) | Magnitude: 125.94 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 48, branch: 19, safety: 11
- `src/utils/popup/index.js` (JAVASCRIPT) | Magnitude: 298.16 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 187, indent_spaces: 172, branch: 43, structural_boundaries: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/slider/src/button.vue` (HTML) | Magnitude: 302.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 210, state_mutation: 209, branch: 28, args: 26
- `packages/theme-chalk/src/index.scss` (CSS) | Magnitude: 0.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 87
- `examples/demo-styles/index.scss` (CSS) | Magnitude: 0.8 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 48
- `packages/descriptions/src/index.js` (JAVASCRIPT) | Magnitude: 137.42 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 167, state_mutation: 55, branch: 48, structural_boundaries: 28
- `examples/components/theme-configurator/editor/color-picker/src/components/predefine.vue` (HTML) | Magnitude: 22.86 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 12, structural_boundaries: 11, args: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/utils/vue-popper.js` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 100.0%)
- `src/utils/menu/aria-menuitem.js` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/utils/dom.js` -> **Severity: 1.04** (Embedded: 0.0181 * Error Risk: 57.5839%)
- `src/utils/merge.js` -> **Severity: 0.706** (Embedded: 0.0082 * Error Risk: 86.0284%)
- `packages/table/src/layout-observer.js` -> **Severity: 0.377** (Embedded: 0.004 * Error Risk: 93.6376%)
- `src/utils/vue-popper.js` -> **Severity: 0.262** (Embedded: 0.0027 * Error Risk: 97.6056%)
- `src/utils/scrollbar-width.js` -> **Severity: 0.251** (Embedded: 0.004 * Error Risk: 62.4136%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/utils/dom.js` -> **Severity: 789.175** (Blast Radius: 10.542 * Doc Risk: 74.8601%)
- `src/utils/types.js` -> **Severity: 313.084** (Blast Radius: 3.233 * Doc Risk: 96.84%)
- `src/utils/merge.js` -> **Severity: 208.361** (Blast Radius: 3.801 * Doc Risk: 54.8175%)
- `packages/table/src/store/helper.js` -> **Severity: 175.499** (Blast Radius: 2.158 * Doc Risk: 81.3247%)
- `packages/table/src/layout-observer.js` -> **Severity: 154.606** (Blast Radius: 2.158 * Doc Risk: 71.6432%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
