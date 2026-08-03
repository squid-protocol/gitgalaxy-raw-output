# ARCHITECTURAL_BRIEF: element
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/element` |
| **Timestamp** | `2026-08-03T20:14:30.118590+00:00` |
| **Scan Duration** | `3.46s` |
| **Git Branch** | `dev` |
| **Git Commit** | `c345bb453bf11badb4831a6a3f600c9372b3a336` |
| **Git Remote** | `https://github.com/ElemeFE/element.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 412 malicious artifacts.

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
> **Architectural Drift Z-Score:** `6.393`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 558 | 74.7% |
| file_cluster_0 | 62 | 8.3% |
| file_cluster_13 | 39 | 5.2% |
| file_cluster_16 | 37 | 5.0% |
| file_cluster_17 | 28 | 3.7% |
| file_cluster_4 | 7 | 0.9% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 22.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.5 | 11.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.6 | 0.8 | 0.0 |
| API Exposure | 0.0 | 18.0 | 3.9 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 42.5 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 82.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.3 | 21.2 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `Popper` (@ `src/utils/popper.js`) -> Impact: **430.2** | LOC: 204
- `describe` (@ `test/unit/specs/select.spec.js`) -> Impact: **296.5** | LOC: 907
- `stop` (@ `src/utils/vue-popper.js`) -> Impact: **248.3** | LOC: 185
- `describe` (@ `test/unit/specs/table.spec.js`) -> Impact: **246.3** | LOC: 1635
- `xhr` (@ `examples/components/theme/loader/ajax.js`) -> Impact: **203.9** | LOC: 54
- `rows` (@ `packages/date-picker/src/basic/date-table.vue`) -> Impact: **202.3** | LOC: 86
- `install` (@ `packages/loading/src/directive.js`) -> Impact: **175.0** | LOC: 123
- `describe` (@ `test/unit/specs/form.spec.js`) -> Impact: **174.2** | LOC: 989
- `created` (@ `packages/tree/src/tree.vue`) -> Impact: **172.2** | LOC: 163
- `describe` (@ `test/unit/specs/menu.spec.js`) -> Impact: **168.3** | LOC: 422

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Popper` (@ `src/utils/popper.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `test/unit/specs/form.spec.js`) -> **O(2^N) [Recursive]**
- `data` (@ `examples/components/theme/components-preview.vue`) -> **O(2^N) [Recursive]**
- `lazyLoad` (@ `packages/cascader-panel/src/cascader-panel.vue`) -> **O(2^N) [Recursive]**
- `rows` (@ `packages/date-picker/src/basic/date-table.vue`) -> **O(2^N) [Recursive]**
- `minDate` (@ `packages/date-picker/src/panel/date-range.vue`) -> **O(2^N) [Recursive]**
- `visible` (@ `packages/select/src/select.vue`) -> **O(2^N) [Recursive]**
- `xhr` (@ `examples/components/theme/loader/ajax.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `test/unit/specs/drawer.spec.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `test/unit/specs/menu.spec.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `test/unit/specs/autocomplete.spec.js`) -> DB Complexity: **96**
- `stop` (@ `src/utils/vue-popper.js`) -> DB Complexity: **59**
- `describe` (@ `test/unit/specs/table.spec.js`) -> DB Complexity: **52**
- `mountPicker` (@ `packages/date-picker/src/picker.vue`) -> DB Complexity: **50**
- `visible` (@ `packages/select/src/select.vue`) -> DB Complexity: **41**
- `describe` (@ `test/unit/specs/tree.spec.js`) -> DB Complexity: **40**
- `mounted` (@ `packages/slider/src/main.vue`) -> DB Complexity: **35**
- `render` (@ `packages/upload/src/index.vue`) -> DB Complexity: **35**
- `handleQueryChange` (@ `packages/select/src/select.vue`) -> DB Complexity: **32**
- `created` (@ `packages/tree/src/tree.vue`) -> DB Complexity: **32**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `test/unit/specs` | 63 | 5390.18 | 8.46% | 0.0% |
| `src/utils` | 18 | 4532.88 | 49.19% | 48.96% |
| `packages/date-picker/src/panel` | 6 | 3321.96 | 72.88% | 8.0% |
| `packages/table/src` | 12 | 2920.68 | 64.59% | 40.11% |
| `packages/select/src` | 5 | 2348.62 | 66.99% | 34.19% |
| `packages/date-picker/src/basic` | 4 | 1581.44 | 70.4% | 50.98% |
| `packages/date-picker/src` | 1 | 1579.26 | 76.45% | 83.92% |
| `packages/tree/src/model` | 3 | 1516.58 | 72.25% | 30.45% |
| `packages/cascader-panel/src` | 5 | 1203.86 | 71.48% | 31.36% |
| `packages/menu/src` | 5 | 1202.1 | 71.25% | 35.16% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/divider/src/main.vue` -> **100.0%** Exposure
- `packages/pagination/src/pagination.js` -> **100.0%** Exposure
- `packages/table/src/config.js` -> **100.0%** Exposure
- `src/mixins/emitter.js` -> **100.0%** Exposure
- `src/utils/shared.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `examples/components/demo-block.vue` -> **100.0%** Exposure
- `examples/components/footer-nav.vue` -> **100.0%** Exposure
- `examples/components/search.vue` -> **100.0%** Exposure
- `examples/components/side-nav.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/borderRadius.vue` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/utils/date-util.js` -> **22** Orphaned Functions | **0** Duplicates
- `packages/pagination/src/pagination.js` -> **0** Orphaned Functions | **16** Duplicates
- `test/unit/specs/table.spec.js` -> **0** Orphaned Functions | **16** Duplicates
- `packages/date-picker/src/picker.vue` -> **0** Orphaned Functions | **14** Duplicates
- `packages/tree/src/model/tree-store.js` -> **13** Orphaned Functions | **0** Duplicates

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

### Exploit Generation Surface
- `examples/components/demo-block.vue` -> **100.0%** Exposure
- `examples/components/search.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/color-picker/src/main.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/fontLineHeight.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/fontSize.vue` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `packages/cascader-panel/src/cascader-menu.vue` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `examples/app.vue` -> **100.0%** Exposure
- `examples/components/demo-block.vue` -> **100.0%** Exposure
- `examples/components/footer-nav.vue` -> **100.0%** Exposure
- `examples/components/search.vue` -> **100.0%** Exposure
- `examples/components/theme-configurator/editor/borderRadius.vue` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `396` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/utils/popup/index.js` (JAVASCRIPT) -> Cumulative Risk: **855.41**
- **Archetype:** `file_cluster_4` (Distance: 13.372 IQR)
- **Magnitude:** 331.56 | **LOC:** 219 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `doOpen` (Impact: 50.5), `visible` (Impact: 17.7), `open` (Impact: 13.9)

### 2. `src/utils/popup/popup-manager.js` (JAVASCRIPT) -> Cumulative Risk: **838.23**
- **Archetype:** `file_cluster_8` (Distance: 12.206 IQR)
- **Magnitude:** 200.72 | **LOC:** 195 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `openModal` (Impact: 53.5), `closeModal` (Impact: 38.8), `getModal` (Impact: 8.2)

### 3. `packages/tooltip/src/main.js` (JAVASCRIPT) -> Cumulative Risk: **809.4**
- **Archetype:** `file_cluster_8` (Distance: 13.567 IQR)
- **Magnitude:** 372.18 | **LOC:** 243 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `mounted` (Impact: 29.1), `render` (Impact: 24.1), `getFirstElement` (Impact: 15.4)

### 4. `packages/select/src/navigation-mixin.js` (JAVASCRIPT) -> Cumulative Risk: **805.71**
- **Archetype:** `file_cluster_17` (Distance: 14.649 IQR)
- **Magnitude:** 156.12 | **LOC:** 55 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9962%)
- **Heaviest Functions:** `navigateOptions` (Impact: 74.9), `hoverIndex` (Impact: 8.9), `data` (Impact: 1.7)

### 5. `packages/tree/src/model/tree-store.js` (JAVASCRIPT) -> Cumulative Risk: **756.01**
- **Archetype:** `file_cluster_17` (Distance: 13.582 IQR)
- **Magnitude:** 478.96 | **LOC:** 341 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_setCheckedKeys` (Impact: 54.1), `filter` (Impact: 22.7), `getCheckedNodes` (Impact: 21.7)

### 6. `packages/tree/src/model/node.js` (JAVASCRIPT) -> Cumulative Risk: **735.29**
- **Archetype:** `file_cluster_17` (Distance: 14.651 IQR)
- **Magnitude:** 1008.64 | **LOC:** 485 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setChecked` (Impact: 154.7), `insertChild` (Impact: 97.5), `constructor` (Impact: 54.5)

### 7. `packages/table/src/table-footer.js` (JAVASCRIPT) -> Cumulative Risk: **728.98**
- **Archetype:** `file_cluster_8` (Distance: 12.521 IQR)
- **Magnitude:** 246.06 | **LOC:** 154 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `rightFixedCount` (Impact: 74.5), `render` (Impact: 54.6), `default` (Impact: 4.5)

### 8. `packages/table/src/store/index.js` (JAVASCRIPT) -> Cumulative Risk: **710.91**
- **Archetype:** `file_cluster_13` (Distance: 13.31 IQR)
- **Magnitude:** 201.4 | **LOC:** 148 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9998%), Tech Debt (94.8664%), Cognitive Load (91.6367%)
- **Heaviest Functions:** `insertColumn` (Impact: 16.8), `setData` (Impact: 14.1), `changeSortCondition` (Impact: 14.0)

### 9. `packages/table/src/table-header.js` (JAVASCRIPT) -> Cumulative Risk: **708.44**
- **Archetype:** `file_cluster_8` (Distance: 13.123 IQR)
- **Magnitude:** 607.52 | **LOC:** 512 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleMouseMove` (Impact: 53.4), `render` (Impact: 53.3), `handleSortClick` (Impact: 47.2)

### 10. `packages/table/src/store/watcher.js` (JAVASCRIPT) -> Cumulative Risk: **699.78**
- **Archetype:** `file_cluster_17` (Distance: 12.704 IQR)
- **Magnitude:** 417.22 | **LOC:** 382 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (95.4704%)
- **Heaviest Functions:** `updateAllSelected` (Impact: 41.5), `_toggleAllSelection` (Impact: 29.7), `clearFilter` (Impact: 27.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/utils/lodash.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.167 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.407 IQR)
- **Top Global Matches:** file_cluster_0: 14.167, file_cluster_8: 14.179, file_cluster_7: 14.312
- **Magnitude:** 1940.72 | **LOC:** 18076 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (46.9253%), Tech Debt (13.9048%)
**Top Internal Functions/Classes:**
  * `baseForOwn` (Impact: 128.1 | O(N^4) | DB: 11)
    * *Intent:* /** * Creates a `_.range` or `_.rangeRight` function. *
  * `arrayEach` (Impact: 34.8 | O(N^2) | DB: 16)
  * `arrayEach` (Impact: 32.5 | O(N^3) | DB: 7)
  * `slice` (Impact: 24.3 | O(N^2) | DB: 1)
    * *Intent:* /** * Creates a function that wraps `func` to invoke it with the `this` binding * of `thisArg` and `...
  * `arrayEach` (Impact: 11.7 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1111`, `structural_boundaries: 997`, `args: 425`, `func_start: 393`
* *Risk/State:* `safety_bypasses: 149`, `state_mutation: 1427`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 82`, `api: 1`, `concurrency: 53`, `import: 1`
* *Defense:* `safety: 215`, `doc: 1499`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/select/src/select.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.519 IQR)
- **Top Global Matches:** file_cluster_0: 14.519, file_cluster_11: 14.564, file_cluster_13: 14.607
- **Magnitude:** 1825.18 | **LOC:** 901 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (83.669%), Tech Debt (24.178%)
**Top Internal Functions/Classes:**
  * `visible` (Impact: 158.4 | O(2^N) | DB: 41)
  * `handleQueryChange` (Impact: 55.6 | O(N^3) | DB: 32)
  * `value` (Impact: 42.6 | O(N^3) | DB: 16)
  * `checkDefaultFirstOption` (Impact: 41.0 | O(N^3) | DB: 12)
  * `emptyText` (Impact: 40.3 | O(N^3) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 99`, `args: 85`, `func_start: 59`, `class_start: 12`
* *Risk/State:* `state_mutation: 956`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 55`, `doc: 1`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/picker.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.459 IQR)
- **Top Global Matches:** file_cluster_17: 14.459, file_cluster_0: 14.526, file_cluster_11: 14.609
- **Magnitude:** 1579.26 | **LOC:** 957 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (76.4507%), Tech Debt (83.9208%)
**Top Internal Functions/Classes:**
  * `handleKeydown` (Impact: 81.8 | O(2^N) | DB: 22)
  * `mountPicker` (Impact: 54.1 | O(N^3) | DB: 50)
  * `displayValue` (Impact: 34.8 | O(N^2) | DB: 12)
  * `selectionMode` (Impact: 26.3 | O(N^2) | DB: 6)
  * `isValidValue` (Impact: 21.7 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 126`, `args: 97`, `func_start: 72`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 846`, `dead_code: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 10`, `concurrency: 6`, `import: 7`
* *Defense:* `safety: 90`, `immutability_locks: 67`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/panel/date-range.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.19 IQR)
- **Top Global Matches:** file_cluster_0: 14.19, file_cluster_13: 14.443, file_cluster_11: 14.447
- **Magnitude:** 1194.7 | **LOC:** 681 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (72.2087%), Tech Debt (12.1767%)
**Top Internal Functions/Classes:**
  * `value` (Impact: 47.3 | O(N^4) | DB: 22)
  * `minDate` (Impact: 43.4 | O(2^N) | DB: 6)
  * `handleDateInput` (Impact: 39.4 | O(N^3) | DB: 16)
  * `resetView` (Impact: 30.1 | O(2^N) | DB: 11)
  * `isValidValue` (Impact: 28.8 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 71`, `args: 101`, `func_start: 52`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 667`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 6`, `import: 7`
* *Defense:* `safety: 39`, `immutability_locks: 33`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00134
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/date-picker/src/panel/date.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.202 IQR)
- **Top Global Matches:** file_cluster_0: 14.202, file_cluster_11: 14.381, file_cluster_13: 14.419
- **Magnitude:** 1022.22 | **LOC:** 610 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (68.012%), Tech Debt (13.877%)
**Top Internal Functions/Classes:**
  * `value` (Impact: 38.7 | O(2^N) | DB: 9)
  * `emit` (Impact: 37.0 | O(2^N) | DB: 4)
  * `confirm` (Impact: 34.6 | O(2^N) | DB: 11)
  * `handleDatePick` (Impact: 29.1 | O(N^3) | DB: 15)
  * `selectionMode` (Impact: 29.0 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 61`, `args: 74`, `func_start: 51`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 527`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 10`, `import: 9`
* *Defense:* `safety: 49`, `doc: 4`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/model/node.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.651 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.026 IQR)
- **Top Global Matches:** file_cluster_17: 14.651, file_cluster_8: 14.708, file_cluster_11: 14.743
- **Magnitude:** 1008.64 | **LOC:** 485 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (82.247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setChecked` (Impact: 154.7 | O(2^N) | DB: 16)
  * `insertChild` (Impact: 97.5 | O(2^N) | DB: 10)
  * `constructor` (Impact: 54.5 | O(N^2) | DB: 32)
  * `expand` (Impact: 36.0 | O(N^3) | DB: 8)
  * `reInitChecked` (Impact: 32.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 62`, `args: 38`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 424`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 50`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util, merge, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/popper.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.191 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.074 IQR)
- **Top Global Matches:** file_cluster_17: 16.191, file_cluster_11: 16.282, file_cluster_0: 16.39
- **Magnitude:** 858.72 | **LOC:** 1277 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (46.9671%), Tech Debt (12.7643%)
**Top Internal Functions/Classes:**
  * `Popper` (Impact: 430.2 | O(2^N) | DB: 29)
  * `value` (Impact: 50.7 | O(N^6) | DB: 7)
    * *Intent:* /** * Computed the boundaries limits and return them * @method * @memberof Popper
  * `applyStyle` (Impact: 36.1 | O(2^N) | DB: 10)
  * `isFixed` (Impact: 28.2 | O(2^N))
  * `setStyle` (Impact: 22.3 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 73`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 182`, `dead_code: 10`, `fragile_debt: 1`
* *Architecture:* `api: 4`
* *Defense:* `safety: 38`, `doc: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/specs/table.spec.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.251 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.55 IQR)
- **Top Global Matches:** file_cluster_8: 10.251, file_cluster_4: 10.69, file_cluster_7: 10.945
- **Magnitude:** 827.7 | **LOC:** 2258 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (34.5099%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 246.3 | O(2^N) | DB: 52)
  * `describe` (Impact: 23.0 | O(N^4) | DB: 2)
  * `it` (Impact: 10.8 | O(N^3) | DB: 5)
  * `it` (Impact: 8.0 | O(N^3))
  * `it` (Impact: 6.1 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 352`, `args: 329`, `func_start: 687`
* *Risk/State:* `state_mutation: 90`, `fragile_debt: 11`, `duplicate_logic: 16`
* *Architecture:* `concurrency: 353`, `import: 1`
* *Defense:* `safety: 9`, `test: 299`, `immutability_locks: 171`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/date-picker/src/basic/date-table.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.383 IQR)
- **Top Global Matches:** file_cluster_17: 14.383, file_cluster_0: 14.426, file_cluster_11: 14.54
- **Magnitude:** 812.06 | **LOC:** 442 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (79.3774%), Tech Debt (65.9028%)
**Top Internal Functions/Classes:**
  * `rows` (Impact: 202.3 | O(2^N) | DB: 28)
  * `getCellClasses` (Impact: 70.3 | O(N^3) | DB: 21)
  * `handleClick` (Impact: 59.1 | O(N^3) | DB: 15)
  * `markRange` (Impact: 42.7 | O(N^3) | DB: 7)
  * `handleMouseMove` (Impact: 24.3 | O(N^3) | DB: 10)
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

### `packages/slider/src/main.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.064 IQR)
- **Top Global Matches:** file_cluster_0: 14.064, file_cluster_17: 14.214, file_cluster_8: 14.266
- **Magnitude:** 775.26 | **LOC:** 428 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (77.763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setValues` (Impact: 64.1 | O(N^3) | DB: 30)
  * `stops` (Impact: 26.6 | O(N^3) | DB: 25)
  * `setPosition` (Impact: 26.2 | O(2^N) | DB: 11)
  * `mounted` (Impact: 20.5 | O(N^2) | DB: 35)
  * `value` (Impact: 13.4 | O(N^2) | DB: 2)
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

### `packages/cascader/src/cascader.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.377 IQR)
- **Top Global Matches:** file_cluster_13: 12.377, file_cluster_8: 12.403, file_cluster_0: 12.461
- **Magnitude:** 679.24 | **LOC:** 664 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (72.0057%), Tech Debt (18.5615%)
**Top Internal Functions/Classes:**
  * `config` (Impact: 40.5 | O(2^N) | DB: 2)
  * `handleSuggestionKeyDown` (Impact: 28.6 | O(N^2) | DB: 1)
  * `mounted` (Impact: 27.0 | O(N^2) | DB: 13)
  * `handleKeyDown` (Impact: 19.9 | O(N^2) | DB: 4)
  * `computePresentTags` (Impact: 18.7 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 69`, `args: 63`, `func_start: 46`, `class_start: 7`
* *Risk/State:* `state_mutation: 285`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 6`, `import: 16`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/table/src/table.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.994 IQR)
- **Top Global Matches:** file_cluster_0: 11.994, file_cluster_8: 12.149, file_cluster_13: 12.291
- **Magnitude:** 635.7 | **LOC:** 713 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (79.5239%), Tech Debt (89.2832%)
**Top Internal Functions/Classes:**
  * `fixedBodyHeight` (Impact: 46.3 | O(2^N) | DB: 11)
  * `bodyHeight` (Impact: 40.4 | O(2^N) | DB: 5)
  * `fixedHeight` (Impact: 26.5 | O(N^3) | DB: 10)
  * `handleFixedMousewheel` (Impact: 25.0 | O(N^3) | DB: 1)
  * `syncPostion` (Impact: 19.9 | O(N^2) | DB: 4)
    * *Intent:* // TODO 使用 CSS transform
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

### `packages/table/src/table-header.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.123 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.343 IQR)
- **Top Global Matches:** file_cluster_8: 13.123, file_cluster_17: 13.218, file_cluster_13: 13.246
- **Magnitude:** 607.52 | **LOC:** 512 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (77.0477%), Tech Debt (22.4692%)
**Top Internal Functions/Classes:**
  * `handleMouseMove` (Impact: 53.4 | O(N^3) | DB: 7)
  * `render` (Impact: 53.3 | O(N^6) | DB: 24)
  * `handleSortClick` (Impact: 47.2 | O(N^2) | DB: 7)
  * `getHeaderCellClass` (Impact: 28.4 | O(N^2) | DB: 8)
  * `handleMouseDown` (Impact: 27.9 | O(N^3) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 86`, `args: 50`, `func_start: 39`
* *Risk/State:* `state_mutation: 236`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 25`, `immutability_locks: 39`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` checkbox, vue, filter-panel.vue, helper, layout-observer, dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tree/src/tree.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.736 IQR)
- **Top Global Matches:** file_cluster_8: 12.736, file_cluster_13: 12.83, file_cluster_0: 12.84
- **Magnitude:** 602.44 | **LOC:** 497 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (94.9187%), Tech Debt (51.8584%)
**Top Internal Functions/Classes:**
  * `created` (Impact: 172.2 | O(N^3) | DB: 32)
  * `handleKeydown` (Impact: 29.6 | O(N^3) | DB: 5)
  * `getNodePath` (Impact: 21.8 | O(2^N) | DB: 15)
  * `getCurrentKey` (Impact: 13.0 | O(2^N) | DB: 3)
  * `setCheckedNodes` (Impact: 10.6 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 45`, `args: 44`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 180`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 6`, `import: 6`
* *Defense:* `safety: 29`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cascader-panel/src/cascader-panel.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.341 IQR)
- **Top Global Matches:** file_cluster_8: 12.341, file_cluster_17: 12.438, file_cluster_13: 12.459
- **Magnitude:** 551.02 | **LOC:** 392 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (72.264%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lazyLoad` (Impact: 114.5 | O(2^N) | DB: 14)
  * `handleKeyDown` (Impact: 52.8 | O(N^3))
  * `scrollIntoView` (Impact: 29.0 | O(2^N) | DB: 3)
  * `syncActivePath` (Impact: 17.8 | O(N^2) | DB: 7)
  * `handleExpand` (Impact: 11.5 | O(N^2) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 50`, `args: 50`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 187`
* *Architecture:* `io: 5`, `api: 8`, `import: 6`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 55`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/form/src/form-item.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.535 IQR)
- **Top Global Matches:** file_cluster_0: 13.535, file_cluster_11: 13.638, file_cluster_13: 13.668
- **Magnitude:** 535.56 | **LOC:** 325 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (76.9954%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validate` (Impact: 70.8 | O(2^N) | DB: 14)
  * `contentStyle` (Impact: 34.8 | O(N^3) | DB: 11)
  * `isRequired` (Impact: 23.4 | O(2^N) | DB: 3)
  * `getRules` (Impact: 17.5 | O(N^2) | DB: 7)
  * `getFilteredRule` (Impact: 14.7 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 51`, `args: 46`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `state_mutation: 244`
* *Architecture:* `io: 10`, `api: 15`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 22`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/menu/src/submenu.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.022 IQR)
- **Top Global Matches:** file_cluster_8: 13.022, file_cluster_13: 13.144, file_cluster_4: 13.165
- **Magnitude:** 532.12 | **LOC:** 350 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (78.0551%), Tech Debt (35.1653%)
**Top Internal Functions/Classes:**
  * `handleMouseleave` (Impact: 73.0 | O(2^N) | DB: 8)
  * `isFirstLevel` (Impact: 34.6 | O(2^N) | DB: 3)
  * `render` (Impact: 32.4 | O(N^3) | DB: 10)
  * `handleMouseenter` (Impact: 27.1 | O(N^2) | DB: 8)
  * `active` (Impact: 17.9 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 48`, `args: 41`, `func_start: 35`
* *Risk/State:* `state_mutation: 185`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 19`, `immutability_locks: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/rate/src/main.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.136 IQR)
- **Top Global Matches:** file_cluster_0: 13.136, file_cluster_8: 13.173, file_cluster_13: 13.293
- **Magnitude:** 513.7 | **LOC:** 349 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (77.9456%), Tech Debt (55.8327%)
**Top Internal Functions/Classes:**
  * `handleKey` (Impact: 38.2 | O(N^3) | DB: 7)
  * `setCurrentValue` (Impact: 28.7 | O(N^3) | DB: 8)
  * `getValueFromMap` (Impact: 17.9 | O(N^3) | DB: 1)
  * `showDecimalIcon` (Impact: 17.4 | O(N^2) | DB: 10)
  * `text` (Impact: 14.7 | O(N^3) | DB: 9)
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

### `packages/tree/src/model/tree-store.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.582 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.794 IQR)
- **Top Global Matches:** file_cluster_17: 13.582, file_cluster_8: 13.662, file_cluster_11: 13.897
- **Magnitude:** 478.96 | **LOC:** 341 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (76.2325%), Tech Debt (91.3419%)
**Top Internal Functions/Classes:**
  * `_setCheckedKeys` (Impact: 54.1 | O(N^3) | DB: 6)
  * `filter` (Impact: 22.7 | O(N^2) | DB: 3)
  * `getCheckedNodes` (Impact: 21.7 | O(N^2) | DB: 1)
  * `constructor` (Impact: 14.1 | O(N^2) | DB: 13)
  * `deregisterNode` (Impact: 11.8 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 41`, `args: 47`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 227`, `orphaned_logic: 13`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 47`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/input/src/input.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.559 IQR)
- **Top Global Matches:** file_cluster_0: 12.559, file_cluster_13: 12.858, file_cluster_8: 12.89
- **Magnitude:** 475.04 | **LOC:** 441 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (68.8069%), Tech Debt (57.145%)
**Top Internal Functions/Classes:**
  * `calcIconOffset` (Impact: 29.4 | O(N^3) | DB: 3)
  * `isWordLimitVisible` (Impact: 15.2 | O(N^2) | DB: 6)
  * `getSuffixVisible` (Impact: 15.2 | O(N^2) | DB: 6)
  * `showClear` (Impact: 13.1 | O(N^2) | DB: 6)
  * `resizeTextarea` (Impact: 12.1 | O(N^3) | DB: 2)
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

### `packages/date-picker/src/panel/month-range.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.535 IQR)
- **Top Global Matches:** file_cluster_0: 13.535, file_cluster_13: 13.717, file_cluster_11: 13.799
- **Magnitude:** 454.68 | **LOC:** 290 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (75.7011%), Tech Debt (21.9439%)
**Top Internal Functions/Classes:**
  * `value` (Impact: 43.6 | O(N^4) | DB: 20)
  * `isValidValue` (Impact: 28.8 | O(N^3) | DB: 3)
  * `resetView` (Impact: 21.6 | O(2^N) | DB: 8)
  * `handleRangePick` (Impact: 19.1 | O(N^2) | DB: 13)
  * `defaultValue` (Impact: 17.4 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 32`, `args: 35`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `state_mutation: 240`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 6`, `import: 6`
* *Defense:* `safety: 17`, `immutability_locks: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.544
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00134
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/menu/src/menu.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.157 IQR)
- **Top Global Matches:** file_cluster_8: 13.157, file_cluster_13: 13.291, file_cluster_17: 13.378
- **Magnitude:** 430.06 | **LOC:** 326 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (67.9365%), Tech Debt (40.9292%)
**Top Internal Functions/Classes:**
  * `handleItemClick` (Impact: 24.0 | O(N^3) | DB: 8)
  * `render` (Impact: 19.7 | O(N^4))
  * `render` (Impact: 18.6 | O(N^3) | DB: 5)
  * `getColorChannels` (Impact: 15.3 | O(N^3) | DB: 2)
  * `initOpenedMenu` (Impact: 11.3 | O(N^2) | DB: 8)
    * *Intent:* // 初始化展开菜单 // initialize opened menu
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 35`, `args: 36`, `func_start: 38`
* *Risk/State:* `state_mutation: 213`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 14`, `immutability_locks: 11`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dropdown/src/dropdown.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.063 IQR)
- **Top Global Matches:** file_cluster_8: 13.063, file_cluster_13: 13.141, file_cluster_4: 13.159
- **Magnitude:** 426.44 | **LOC:** 294 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (81.7574%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleItemKeyDown` (Impact: 32.5 | O(N^3) | DB: 12)
  * `render` (Impact: 27.3 | O(N^3) | DB: 3)
  * `focusing` (Impact: 23.1 | O(2^N))
  * `initEvent` (Impact: 21.3 | O(N^3) | DB: 14)
  * `handleTriggerKeyDown` (Impact: 13.4 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 33`, `args: 27`, `func_start: 24`
* *Risk/State:* `state_mutation: 216`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 8`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/vue-popper.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.54 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.843 IQR)
- **Top Global Matches:** file_cluster_13: 13.54, file_cluster_8: 13.547, file_cluster_11: 13.757
- **Magnitude:** 419.64 | **LOC:** 199 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (52.764%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stop` (Impact: 248.3 | O(2^N) | DB: 59)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 20`, `args: 15`, `func_start: 13`
* *Risk/State:* `state_mutation: 167`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 5`, `doc: 7`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.465
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.002681
  * `Imports (Out-Degree: 1):` popup, vue, popper
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/table/src/store/watcher.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.704 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.738 IQR)
- **Top Global Matches:** file_cluster_17: 12.704, file_cluster_13: 13.065, file_cluster_2: 13.167
- **Magnitude:** 417.22 | **LOC:** 382 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (87.5022%), Tech Debt (11.7359%)
**Top Internal Functions/Classes:**
  * `updateAllSelected` (Impact: 41.5 | O(N^3) | DB: 5)
  * `_toggleAllSelection` (Impact: 29.7 | O(N^3) | DB: 4)
  * `clearFilter` (Impact: 27.7 | O(N^3) | DB: 5)
  * `cleanSelection` (Impact: 20.9 | O(N^3) | DB: 5)
  * `updateColumns` (Impact: 18.2 | O(N^2) | DB: 2)
    * *Intent:* // 更新列
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 48`, `args: 40`, `func_start: 23`
* *Risk/State:* `state_mutation: 149`, `planned_debt: 2`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 19`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00134
  * `Imports (Out-Degree: 3):` tree, vue, expand, util, merge, current
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/components/footer.vue` (HTML) | Magnitude: 30.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 172, io: 37, decorators: 26, structural_boundaries: 18
- `packages/carousel/src/main.vue` (HTML) | Magnitude: 412.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 275, state_mutation: 227, branch: 60, args: 42
- `packages/loading/src/loading.vue` (HTML) | Magnitude: 12.98 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, decorators: 11, structural_boundaries: 5, args: 4
- `src/utils/lodash.js` (JAVASCRIPT) | Magnitude: 1940.72 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4874, doc: 1499, state_mutation: 1427, branch: 1111
- `packages/result/src/index.vue` (HTML) | Magnitude: 17.66 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 13, branch: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/utils/types.js` (JAVASCRIPT) | Magnitude: 31.86 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, safety: 15, indent_spaces: 11, branch: 8
- `src/utils/util.js` (JAVASCRIPT) | Magnitude: 273.12 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 93, branch: 67, state_mutation: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/extension/src/editor/editor.vue` (HTML) | Magnitude: 213.8 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 169, state_mutation: 120, branch: 24, structural_boundaries: 23
- `src/utils/vue-popper.js` (JAVASCRIPT) | Magnitude: 419.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 167, indent_spaces: 160, branch: 46, structural_boundaries: 20
- `types/popconfirm.d.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, indent_spaces: 8, structural_boundaries: 6, import: 2
- `packages/table/src/table-body.js` (JAVASCRIPT) | Magnitude: 42.18 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
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
- `packages/notification/src/main.js` (JAVASCRIPT) | Magnitude: 69.94 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 25, state_mutation: 25, branch: 15
- `packages/table/src/store/helper.js` (JAVASCRIPT) | Magnitude: 31.52 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 11, state_mutation: 9, branch: 6
- `packages/container/src/main.vue` (HTML) | Magnitude: 37.48 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, branch: 10, structural_boundaries: 7, state_mutation: 6
- `src/utils/menu/aria-menubar.js` (JAVASCRIPT) | Magnitude: 8.54 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, args: 4, state_mutation: 4
- `packages/date-picker/src/basic/date-table.vue` (HTML) | Magnitude: 812.06 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 364, state_mutation: 299, branch: 119, safety: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/backtop/src/main.vue` (HTML) | Magnitude: 126.62 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 92, state_mutation: 47, args: 15, func_start: 14
- `examples/components/theme-configurator/index.vue` (HTML) | Magnitude: 190.84 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 173, state_mutation: 92, structural_boundaries: 27, args: 24
- `src/utils/aria-dialog.js` (JAVASCRIPT) | Magnitude: 152.14 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 76, indent_spaces: 48, branch: 19, safety: 11
- `src/utils/popup/index.js` (JAVASCRIPT) | Magnitude: 331.56 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 187, indent_spaces: 172, branch: 43, structural_boundaries: 20
- `examples/components/theme/loader/loading/progress.vue` (HTML) | Magnitude: 123.92 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 58, structural_boundaries: 19, func_start: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/tooltip/src/main.js` (JAVASCRIPT) | Magnitude: 372.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 212, state_mutation: 210, branch: 51, func_start: 36
- `examples/components/demo-block.vue` (HTML) | Magnitude: 207.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 293, state_mutation: 89, structural_boundaries: 33, branch: 25
- `packages/theme-chalk/src/index.scss` (CSS) | Magnitude: 0.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 87
- `examples/demo-styles/index.scss` (CSS) | Magnitude: 0.8 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 48
- `packages/descriptions/src/index.js` (JAVASCRIPT) | Magnitude: 198.52 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 167, state_mutation: 55, branch: 48, structural_boundaries: 28

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

- `src/utils/merge.js` -> **Severity: 0.315** (Embedded: 0.0082 * Error Risk: 38.3086%)
- `packages/table/src/layout-observer.js` -> **Severity: 0.258** (Embedded: 0.004 * Error Risk: 64.2301%)
- `src/utils/vue-popper.js` -> **Severity: 0.241** (Embedded: 0.0027 * Error Risk: 89.8048%)
- `src/utils/dom.js` -> **Severity: 0.155** (Embedded: 0.0181 * Error Risk: 8.5825%)
- `src/utils/menu/aria-submenu.js` -> **Severity: 0.105** (Embedded: 0.0018 * Error Risk: 58.629%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/utils/dom.js` -> **Severity: 848.417** (Blast Radius: 10.542 * Doc Risk: 80.4797%)
- `src/utils/merge.js` -> **Severity: 346.319** (Blast Radius: 3.801 * Doc Risk: 91.1127%)
- `src/utils/types.js` -> **Severity: 323.081** (Blast Radius: 3.233 * Doc Risk: 99.9322%)
- `src/utils/scrollbar-width.js` -> **Severity: 212.776** (Blast Radius: 2.542 * Doc Risk: 83.704%)
- `packages/table/src/store/helper.js` -> **Severity: 208.829** (Blast Radius: 2.158 * Doc Risk: 96.7696%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
