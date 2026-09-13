# ARCHITECTURAL_BRIEF: excalidraw
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/excalidraw/excalidraw.git` |
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
| Total Artifacts | 1225 |
| Analyzed Artifacts (Scanned) | 824 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 401 |
| Total LOC | 192857 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 67.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.632 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.196 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9392 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 123 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 597 | 140685 | 72.5% |
| CSS | 85 | 7992 | 10.3% |
| JSON | 75 | 41098 | 9.1% |
| JAVASCRIPT | 25 | 2793 | 3.0% |
| MARKDOWN | 14 | 0 | 1.7% |
| PLAINTEXT | 13 | 2 | 1.6% |
| XML | 10 | 23 | 1.2% |
| YAML | 2 | 25 | 0.2% |
| HTML | 2 | 229 | 0.2% |
| DOCKERFILE | 1 | 10 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 791 | 96.0% |
| Unknown | 2 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 3.0% |
| Static: Minified & Vendor Opaque Mass | 6 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 401*

**Composition by Extension & Reason:**
- `.woff2`: 237x Excluded (Explicitly Denied Extension: '.woff2')
- `.mdx`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 32x Excluded (Explicitly Denied Extension: '.png')
- `.snap`: 20x Excluded (Unsupported Extension: '.snap'), 4x Unsupported Format (.snap)
- `no_extension`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.excalidrawlib'), 1x Unsupported Format (.undeterminable)
- `.yml`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpeg`: 5x Excluded (Explicitly Denied Extension: '.jpeg')
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 97 LOC), 1x Excluded (Machine-Generated Source Code Signature: 161 LOC), 1x Excluded (Embedded Array/Matrix Payload: 11397 commas in 1325 LOC)
- `.ttf`: 5x Excluded (Explicitly Denied Extension: '.ttf')
- `.svg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 3x Excluded (Explicitly Denied Extension: '.ico')
- `.lock`: 3x Excluded (Unsupported Extension: '.lock')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rules`: 2x Excluded (Unsupported Extension: '.rules')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.3 | 6.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.0 | 30.5 | 20.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 2.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 24.6 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 17.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.1 | 0.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 77.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.3 | 1.7 | 0.9 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.1 | 5.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 58.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 998 | 220 | 3 | `packages/excalidraw/wysiwyg/textWysiwyg.test.tsx` |
| cleanup | 117 | 41 | 0 | `packages/excalidraw/components/App.tsx` |
| guards | 4043 | 395 | 12 | `packages/excalidraw/components/App.tsx` |
| danger | 1259 | 243 | 4 | `packages/excalidraw/subset/woff2/woff2-bindings.ts` |
| concurrency | 2281 | 194 | 7 | `packages/excalidraw/tests/flip.test.tsx` |
| connectivity | 3706 | 547 | 9 | `packages/excalidraw/components/icons.tsx` |
| io | 1163 | 101 | 1 | `packages/excalidraw/components/icons.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 11 | 0 | `packages/excalidraw/components/App.tsx` |
| time | 182 | 57 | 0 | `packages/excalidraw/components/TTDDialog/utils/chat.test.ts` |
| serialization | 103 | 52 | 0 | `packages/excalidraw/components/App.tsx` |
| regex | 203 | 63 | 0 | `packages/element/src/embeddable.ts` |
| events | 483 | 91 | 1 | `packages/excalidraw/components/App.tsx` |
| tests | 6405 | 111 | 11 | `packages/excalidraw/tests/history.test.tsx` |
| docs | 750 | 153 | 2 | `packages/excalidraw/types.ts` |
| debt | 396 | 139 | 1 | `packages/excalidraw/components/App.tsx` |
| mutation | 24536 | 585 | 69 | `packages/excalidraw/components/App.tsx` |
| dead_code | 231 | 115 | 1 | `packages/excalidraw/components/App.tsx` |
| credential | 28 | 8 | 0 | `packages/element/tests/embeddable.test.ts` |
| threat | 223 | 52 | 0 | `packages/excalidraw/subset/woff2/woff2-bindings.ts` |
| ml_ai | 941 | 121 | 2 | `packages/element/src/bounds.ts` |
| ui | 4589 | 385 | 12 | `packages/excalidraw/components/App.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/excalidraw/components/icons.tsx` (Hits: 616)
- `packages/excalidraw/components/TTDDialog/utils/TTDstreamFetch.test.ts` (Hits: 46)
- `packages/excalidraw/data/library.test.ts` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **i18n.ts** (`packages/excalidraw/i18n.ts`) — 106 inbound connections
2. **icons.tsx** (`packages/excalidraw/components/icons.tsx`) — 97 inbound connections
3. **api.ts** (`packages/excalidraw/tests/helpers/api.ts`) — 51 inbound connections
4. **utility-types.ts** (`packages/common/src/utility-types.ts`) — 47 inbound connections
5. **ui.ts** (`packages/excalidraw/tests/helpers/ui.ts`) — 41 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **App.tsx** (`packages/excalidraw/components/App.tsx`) — 80 outbound dependencies
2. **App.tsx** (`excalidraw-app/App.tsx`) — 51 outbound dependencies
3. **index.ts** (`packages/element/src/index.ts`) — 48 outbound dependencies
4. **LayerUI.tsx** (`packages/excalidraw/components/LayerUI.tsx`) — 46 outbound dependencies
5. **index.tsx** (`packages/excalidraw/index.tsx`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `bindOrUnbindBindingElementEdge` (@ `packages/element/src/binding.ts`) -> Impact: **511.6** | LOC: 777
- `textPropertiesUpdated` (@ `packages/excalidraw/wysiwyg/textWysiwyg.tsx`) -> Impact: **290.4** | LOC: 785
- `resizeMultipleElements` (@ `packages/element/src/resizeElements.ts`) -> Impact: **261.0** | LOC: 352
- `addToRoot` (@ `packages/excalidraw/renderer/staticSvgScene.ts`) -> Impact: **203.9** | LOC: 579
- `updateElbowArrowPoints` (@ `packages/element/src/elbowArrow.ts`) -> Impact: **202.1** | LOC: 286
  * *Intent:* /** * */
- `generateDynamicAABBs` (@ `packages/element/src/elbowArrow.ts`) -> Impact: **201.3** | LOC: 186
  * *Intent:* /** * Create dynamically resizing, always touching * bounding boxes having a minimum extent represented * by the given static bounds. */
- `convertToExcalidrawElements` (@ `packages/element/src/transform.ts`) -> Impact: **200.4** | LOC: 301
- `repairBinding` (@ `packages/excalidraw/data/restore.ts`) -> Impact: **192.0** | LOC: 214
- `handleEndpointDrag` (@ `packages/element/src/elbowArrow.ts`) -> Impact: **180.9** | LOC: 202
- `createIcon` (@ `packages/excalidraw/components/icons.tsx`) -> Impact: **180.6** | LOC: 2468

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/element/src` | 47 | 16797.62 | 25.45% | 7.34% |
| `__monolith__` | 13 | 10128.16 | 7.12% | 3.33% |
| `packages/excalidraw/components` | 134 | 7304.85 | 7.83% | 3.14% |
| `packages/excalidraw/actions` | 47 | 5041.73 | 8.33% | 3.19% |
| `packages/excalidraw/tests` | 33 | 3471.74 | 7.82% | 0.0% |
| `packages/element/tests` | 22 | 3382.65 | 3.35% | 0.0% |
| `packages/excalidraw` | 37 | 3138.6 | 22.57% | 1.4% |
| `packages/excalidraw/subset/woff2` | 2 | 3133.94 | 62.59% | 17.72% |
| `packages/excalidraw/data` | 14 | 2084.18 | 25.19% | 8.42% |
| `packages/common/src` | 21 | 1874.17 | 23.35% | 3.8% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/excalidraw/actions/actionAlign.tsx` -> **99.9146%** Exposure
- `packages/excalidraw/components/ButtonIconCycle.tsx` -> **88.0797%** Exposure
- `packages/element/src/sortElements.ts` -> **74.4868%** Exposure
- `dev-docs/src/components/Highlight.js` -> **73.1059%** Exposure
- `scripts/build-locales-coverage.js` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/common/debug.ts` -> **100.0%** Exposure
- `packages/common/src/appEventBus.ts` -> **100.0%** Exposure
- `packages/common/src/binary-heap.ts` -> **100.0%** Exposure
- `packages/common/src/queue.ts` -> **100.0%** Exposure
- `packages/common/src/url.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `excalidraw-app/tests/collab.test.tsx` -> **9** Orphaned Functions | **0** Duplicates
- `packages/element/tests/align.test.tsx` -> **8** Orphaned Functions | **0** Duplicates
- `packages/element/src/visualdebug.ts` -> **6** Orphaned Functions | **0** Duplicates
- `packages/excalidraw/actions/actionAlign.tsx` -> **0** Orphaned Functions | **6** Duplicates
- `packages/excalidraw/components/FontPicker/FontPicker.test.tsx` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `dev-docs/docusaurus.config.js` -> **99.8599%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `265` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1521` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/excalidraw/data/blob.ts` (TYPESCRIPT) -> Cumulative Risk: **707.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 429.22 | **LOC:** 508 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (91.2981%), Api Exposure (85.499%)
- **Heaviest Functions:** `loadSceneOrLibraryFromBlob` (Impact: 34.3), `getMimeType` (Impact: 22.5), `normalizeFile` (Impact: 22.5)

### 2. `packages/excalidraw/hooks/useLibraryItemSvg.ts` (TYPESCRIPT) -> Cumulative Risk: **664.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 61.22 | **LOC:** 102 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8786%), State Flux (96.7374%)
- **Heaviest Functions:** `useLibraryItemSvg` (Impact: 25.3), `exportLibraryItemToSvg` (Impact: 2.2), `deleteItemsFromLibraryCache` (Impact: 1.9)

### 3. `excalidraw-app/collab/Portal.tsx` (TYPESCRIPT) -> Cumulative Risk: **664.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 152.44 | **LOC:** 258 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8825%), State Flux (99.3803%)
- **Heaviest Functions:** `broadcastScene` (Impact: 18.1), `_broadcastSocketData` (Impact: 14.9), `broadcastMouseLocation` (Impact: 6.8)

### 4. `excalidraw-app/data/firebase.ts` (TYPESCRIPT) -> Cumulative Risk: **651.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 162.7 | **LOC:** 320 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9997%), State Flux (82.1204%)
- **Heaviest Functions:** `loadFilesFromFirebase` (Impact: 20.3), `saveToFirebase` (Impact: 11.0), `isSavedToFirebase` (Impact: 7.7)

### 5. `packages/excalidraw/components/ToolButton.tsx` (TYPESCRIPT) -> Cumulative Risk: **648.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 89.54 | **LOC:** 212 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.5962%), Concurrency (82.9123%)
- **Heaviest Functions:** `onClick` (Impact: 44.7), `onClick` (Impact: 2.0), `onClick` (Impact: 2.0)

### 6. `packages/common/debug.ts` (TYPESCRIPT) -> Cumulative Risk: **647.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 155.16 | **LOC:** 221 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (92.4634%), Documentation (91.554%)
- **Heaviest Functions:** `deepEqual` (Impact: 19.2), `debugLogger` (Impact: 11.8), `logTimeAverage` (Impact: 11.1)

### 7. `packages/utils/src/export.ts` (TYPESCRIPT) -> Cumulative Risk: **643.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 154.54 | **LOC:** 217 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `exportToBlob` (Impact: 22.9), `exportToCanvas` (Impact: 21.5), `exportToClipboard` (Impact: 13.6)

### 8. `excalidraw-app/data/FileManager.ts` (TYPESCRIPT) -> Cumulative Risk: **641.26**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 169.16 | **LOC:** 297 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9652%), State Flux (99.6256%)
- **Heaviest Functions:** `saveFiles` (Impact: 25.7), `isFileTracked` (Impact: 7.5), `updateStaleImageStatuses` (Impact: 6.9)

### 9. `packages/excalidraw/subset/woff2/woff2-bindings.ts` (TYPESCRIPT) -> Cumulative Risk: **633.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3105.64 | **LOC:** 4052 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9971%), Cognitive Load (89.845%)
- **Heaviest Functions:** `craftInvokerFunction` (Impact: 68.6), `__embind_register_std_string` (Impact: 53.5), `genericPointerToWireType` (Impact: 43.8)

### 10. `packages/excalidraw/components/AppStateObserver.ts` (TYPESCRIPT) -> Cumulative Risk: **631.26**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 139.68 | **LOC:** 209 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (82.048%)
- **Heaviest Functions:** `normalize` (Impact: 32.5), `getValue` (Impact: 12.5), `flush` (Impact: 9.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.env.production` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/subset/woff2/woff2-bindings.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3105.64 | **LOC:** 4052 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.845%), Tech Debt (8.5556%)
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` (Impact: 68.6)
  * `__embind_register_std_string` (Impact: 53.5)
  * `genericPointerToWireType` (Impact: 43.8)
  * `__embind_register_class` (Impact: 39.4)
  * `stringToUTF8Array` (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 389 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 1289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 684`, `structural_boundaries: 377`, `args: 393`, `func_start: 367`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 511`, `duplicate_logic: 2`
* *Architecture:* `io: 31`, `api: 38`, `concurrency: 8`, `import: 2`
* *Defense:* `safety: 40`, `doc: 1`, `test: 90`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004666
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/excalidraw/components/App.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2820.18 | **LOC:** 12839 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 44.7%
- **Risk Profile:** Cognitive Load (47.5842%), Tech Debt (8.2316%)
**Top Internal Functions/Classes:**
  * `handleDelayedBindModeChange` (Impact: 136.7)
  * `effector` (Impact: 80.9)
  * `maybeDragNewGenericElement` (Impact: 45.9)
  * `handleAppOnDrop` (Impact: 43.0)
  * `handleIframeLikeCenterClick` (Impact: 37.5)
    * *Intent:* /** @returns true if iframe-like element click handled */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 455 instances
* *Concurrency (weighted view):* 235
* *State Mutation (weighted view):* 1514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2358`, `structural_boundaries: 1167`, `args: 482`, `func_start: 216`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 604`, `dead_code: 31`, `planned_debt: 8`, `fragile_debt: 4`
* *Architecture:* `io: 17`, `api: 64`, `concurrency: 85`, `import: 83`
* *Defense:* `safety: 441`, `doc: 32`, `immutability_locks: 18`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.37
  * `Choke Point (Betweenness):` 0.014547 | `Ripple Effect (Closeness):` 0.069232
  * `Imports (Out-Degree: 49):` actions, actionBoundText, actionCanvas, actionClipboard, actionElementLink, actionElementLock, actionFrame, actionHistory...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `packages/element/tests/binding.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1856.73 | **LOC:** 698 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.1671%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 77`, `args: 30`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `concurrency: 18`, `import: 11`
* *Defense:* `safety: 28`, `test: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` dom, transformHandles, types, common, excalidraw, actionBoundText, i18n, api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/element/src/binding.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1829.86 | **LOC:** 2941 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (38.0253%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bindOrUnbindBindingElementEdge` (Impact: 511.6)
  * `updateBoundPoint` (Impact: 155.0)
  * `getBindingSideMidPoint` (Impact: 106.5)
  * `bindPointToSnapToElementOutline` (Impact: 75.7)
  * `snapToMid` (Impact: 67.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 539`, `structural_boundaries: 318`, `args: 71`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 110`
* *Architecture:* `api: 40`, `import: 20`
* *Defense:* `safety: 61`, `doc: 9`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.083
  * `Choke Point (Betweenness):` 0.001234 | `Ripple Effect (Closeness):` 0.026918
  * `Imports (Out-Degree: 10):` Scene, bounds, collision, distance, elbowArrow, heading, linearElementEditor, mutateElement...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/element/src/elbowArrow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1761.28 | **LOC:** 2310 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.156%), Tech Debt (8.043%)
**Top Internal Functions/Classes:**
  * `updateElbowArrowPoints` (Impact: 202.1)
    * *Intent:* /** * */
  * `generateDynamicAABBs` (Impact: 201.3)
    * *Intent:* /** * Create dynamically resizing, always touching * bounding boxes having a minimum extent represen...
  * `handleEndpointDrag` (Impact: 180.9)
  * `handleSegmentMove` (Impact: 162.9)
    * *Intent:* /** * */
  * `estimateSegmentCount` (Impact: 131.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 540`, `structural_boundaries: 240`, `args: 87`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 92`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 3`, `import: 13`
* *Defense:* `safety: 69`, `doc: 9`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.022
  * `Choke Point (Betweenness):` 0.001098 | `Ripple Effect (Closeness):` 0.021871
  * `Imports (Out-Degree: 6):` binding, bounds, collision, distance, heading, mutateElement, typeChecks, types...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/excalidraw/actions/actionDuplicateSelection.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1527.31 | **LOC:** 532 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2743%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 79`, `args: 41`, `func_start: 4`
* *Risk/State:* `fragile_debt: 2`
* *Architecture:* `concurrency: 6`, `import: 5`
* *Defense:* `safety: 19`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index, api, test-utils, actionDuplicateSelection, common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/element/src/linearElementEditor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1371.88 | **LOC:** 2508 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.799%), Tech Debt (8.3368%)
**Top Internal Functions/Classes:**
  * `handlePointDragging` (Impact: 144.1)
  * `normalizeSelectedPoints` (Impact: 139.8)
  * `movePoints` (Impact: 85.1)
  * `handlePointerMove` (Impact: 81.0)
  * `handlePointerDown` (Impact: 71.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 150`, `args: 55`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 98`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 30`, `import: 18`
* *Defense:* `safety: 61`, `doc: 9`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.394
  * `Choke Point (Betweenness):` 0.0005 | `Ripple Effect (Closeness):` 0.029162
  * `Imports (Out-Degree: 7):` Scene, binding, bounds, heading, mutateElement, shape, sizeHelpers, textElement...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/element/src/delta.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1283.7 | **LOC:** 2067 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.0928%), Tech Debt (16.0673%)
**Top Internal Functions/Classes:**
  * `filterInvisibleChanges` (Impact: 79.5)
    * *Intent:* /** * Mutates `nextAppState` be filtering out state related to deleted elements. * * @returns `true`...
  * `mergeBoundElements` (Impact: 77.4)
  * `squash` (Impact: 65.8)
  * `squash` (Impact: 48.8)
  * `distinctKeysIterator` (Impact: 42.7)
    * *Intent:* /** * Iterator comparing values of object properties based on the passed joining strategy. * * @yiel...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 207`, `args: 100`, `func_start: 77`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 91`, `dead_code: 2`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 49`, `import: 16`
* *Defense:* `safety: 54`, `doc: 31`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.001006 | `Ripple Effect (Closeness):` 0.003645
  * `Imports (Out-Degree: 10):` Scene, binding, fractionalIndex, groups, linearElementEditor, mutateElement, store, textElement...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/excalidraw/renderer/interactiveScene.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 967.14 | **LOC:** 2091 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 61.5%
- **Risk Profile:** Cognitive Load (22.6049%), Tech Debt (7.8803%)
**Top Internal Functions/Classes:**
  * `renderResetAutoResizeHandle` (Impact: 174.0)
  * `renderBindingHighlightForBindableElement_simple` (Impact: 139.1)
  * `renderBindingHighlightForBindableElement_complex` (Impact: 127.0)
  * `renderLinearPointHandles` (Impact: 86.8)
  * `addSelectionForGroupId` (Impact: 56.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 147`, `args: 63`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 74`, `planned_debt: 1`
* *Architecture:* `api: 4`, `import: 18`
* *Defense:* `safety: 43`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007442
  * `Imports (Out-Degree: 6):` clients, renderSnaps, roundRect, scrollbars, types, textAutoResizeHandle, types, helpers...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/element/src/resizeElements.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 940.46 | **LOC:** 1501 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.6731%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resizeMultipleElements` (Impact: 261.0)
  * `resizeSingleElement` (Impact: 115.3)
  * `getResizeAnchor` (Impact: 61.5)
  * `getNextMultipleWidthAndHeightFromPointer` (Impact: 54.5)
  * `transformElements` (Impact: 54.3)
    * *Intent:* // Returns true when transform (resizing/rotation) happened
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 123`, `args: 26`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`
* *Architecture:* `api: 9`, `import: 18`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00243
  * `Imports (Out-Degree: 11):` Scene, binding, bounds, groups, linearElementEditor, mutateElement, textElement, textMeasurements...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/common/src/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 856.38 | **LOC:** 1332 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (29.1005%), Tech Debt (8.8286%)
**Top Internal Functions/Classes:**
  * `isShallowEqual` (Impact: 46.3)
    * *Intent:* /** * Returns whether object/array is shallow equal. * Considers empty object/arrays as equal (wheth...
  * `escapeDoubleQuotes` (Impact: 34.4)
    * *Intent:* /** * use when you need to render unsafe string as HTML attribute, but MAKE SURE * the attribute is ...
  * `normalizeEOL` (Impact: 25.6)
  * `updateActiveTool` (Impact: 22.5)
  * `addEventListener` (Impact: 16.9)
    * *Intent:* // implem
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 442`, `args: 126`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 67`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 97`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 37`, `doc: 28`, `immutability_locks: 26`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` constants, utility-types, types, types, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/snapping.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 764.04 | **LOC:** 1415 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.3177%), Tech Debt (8.0388%)
**Top Internal Functions/Classes:**
  * `snapResizingElements` (Impact: 81.0)
  * `getGapSnaps` (Impact: 70.8)
  * `getElementsCorners` (Impact: 39.9)
  * `createGapSnapLines` (Impact: 39.7)
  * `getPointSnaps` (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 195`, `args: 47`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 94`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 28`, `import: 11`
* *Defense:* `safety: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05857
  * `Imports (Out-Degree: 0):` types, common, element, types, math
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/excalidraw/tests/elementLocking.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 689.95 | **LOC:** 391 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7122%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 59`, `args: 18`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `concurrency: 10`, `import: 8`
* *Defense:* `safety: 14`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` actions, i18n, index, api, ui, test-utils, dom, common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/actions/actionProperties.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 662.64 | **LOC:** 2044 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (9.379%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `perform` (Impact: 92.4)
  * `perform` (Impact: 65.2)
  * `getFontFamily` (Impact: 50.5)
  * `getFormValue` (Impact: 26.4)
  * `perform` (Impact: 22.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 301`, `args: 141`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 29`
* *Architecture:* `api: 20`, `import: 31`
* *Defense:* `safety: 19`, `doc: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.911
  * `Choke Point (Betweenness):` 0.000545 | `Ripple Effect (Closeness):` 0.039964
  * `Imports (Out-Degree: 8):` analytics, ColorPicker, FontPicker, IconPicker, RadioSelection, Range, icons, fonts...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/element/src/shape.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 611.96 | **LOC:** 1235 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (18.5591%), Tech Debt (8.1005%)
**Top Internal Functions/Classes:**
  * `getArrowheadShapes` (Impact: 136.2)
  * `_generateElementShape` (Impact: 84.5)
    * *Intent:* /** * Generates the roughjs shape for given element. * * Low-level. Use `ShapeCache.generateElementS...
  * `generateRoughOptions` (Impact: 47.7)
  * `getElementShape` (Impact: 41.4)
    * *Intent:* /** * get the pure geometric shape of an excalidraw elementw * which is then used for hit detection ...
  * `generateElbowArrowShape` (Impact: 29.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 159`, `args: 31`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 44`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 10`, `import: 20`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bounds, collision, comparisons, heading, renderElement, typeChecks, types, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/element/src/renderElement.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 608.82 | **LOC:** 1129 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (22.5147%), Tech Debt (8.5711%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 147.7)
  * `drawElementOnCanvas` (Impact: 111.7)
  * `generateElementWithCanvas` (Impact: 47.6)
  * `generateElementCanvas` (Impact: 47.1)
  * `getRenderOpacity` (Impact: 44.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 77`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 54`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 6`, `api: 7`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00243
  * `Imports (Out-Degree: 6):` bounds, cropElement, frame, linearElementEditor, shape, textElement, textMeasurements, typeChecks...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/element/src/bounds.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 581.78 | **LOC:** 1315 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (17.0359%), Tech Debt (9.9367%)
**Top Internal Functions/Classes:**
  * `getElementLineSegments` (Impact: 45.8)
    * *Intent:* /* * for a given element, `getElementLineSegments` returns line segments * that can be used for visu...
  * `equation` (Impact: 35.5)
    * *Intent:* // B(t) = p0 * (1-t)^3 + 3p1 * t * (1-t)^2 + 3p2 * t^2 * (1-t) + p3 * t^3
  * `getMinMaxXYFromCurvePathOps` (Impact: 25.2)
  * `getArrowheadPoints` (Impact: 21.9)
  * `getBounds` (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 196`, `args: 51`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `state_mutation: 51`, `planned_debt: 6`
* *Architecture:* `api: 30`, `import: 19`
* *Defense:* `safety: 7`, `doc: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` linearElementEditor, shape, textElement, typeChecks, types, utils, common, utility-types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/element/src/frame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 580.42 | **LOC:** 950 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.3132%), Tech Debt (8.8382%)
**Top Internal Functions/Classes:**
  * `getElementsInResizingFrame` (Impact: 45.0)
  * `shouldApplyFrameClip` (Impact: 44.8)
  * `addElementsToFrame` (Impact: 44.0)
    * *Intent:* /** * Retains (or repairs for target frame) the ordering invriant where children * elements come rig...
  * `setGroupsInFrame` (Impact: 34.9)
  * `filterElementsEligibleAsFrameChildren` (Impact: 27.3)
    * *Intent:* // --------------------------- Frame Operations ------------------------------- /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 166`, `args: 65`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 39`, `dead_code: 10`, `planned_debt: 2`
* *Architecture:* `api: 33`, `import: 13`
* *Defense:* `safety: 12`, `doc: 8`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.412
  * `Choke Point (Betweenness):` 0.000403 | `Ripple Effect (Closeness):` 0.012725
  * `Imports (Out-Degree: 8):` Scene, bounds, groups, mutateElement, selection, textElement, typeChecks, types...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/excalidraw/data/restore.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 563.6 | **LOC:** 1029 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (20.9375%), Tech Debt (8.6971%)
**Top Internal Functions/Classes:**
  * `repairBinding` (Impact: 192.0)
  * `restoreElements` (Impact: 101.7)
  * `restoreAppState` (Impact: 58.1)
  * `restoreElement` (Impact: 24.3)
  * `repairBoundElement` (Impact: 21.1)
    * *Intent:* /** * Repairs target bound element's container's boundElements array, * or removes contaienrId if co...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 119`, `args: 23`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 25`, `dead_code: 7`, `planned_debt: 2`
* *Architecture:* `api: 8`, `import: 21`
* *Defense:* `safety: 49`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.063938
  * `Imports (Out-Degree: 2):` appState, scene, types, types, common, utility-types, element, types...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `packages/excalidraw/wysiwyg/textWysiwyg.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 546.92 | **LOC:** 1023 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (62.4027%), Tech Debt (9.0646%)
**Top Internal Functions/Classes:**
  * `textPropertiesUpdated` (Impact: 290.4)
  * `getLineCaretOffsetFromNativeLayout` (Impact: 15.2)
  * `getTransform` (Impact: 14.3)
  * `textWysiwyg` (Impact: 7.7)
  * `getLineDirection` (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 108`, `args: 34`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 21`
* *Defense:* `safety: 21`, `doc: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.000766 | `Ripple Effect (Closeness):` 0.049799
  * `Imports (Out-Degree: 4):` actions, actionCanvas, actionProperties, clipboard, App, types, common, element...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/excalidraw/components/CommandPalette/CommandPalette.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 523.54 | **LOC:** 1049 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (15.9238%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CommandPaletteInner` (Impact: 180.3)
  * `executeCommand` (Impact: 77.5)
  * `extract` (Impact: 23.6)
  * `getNextCommandsByCategory` (Impact: 20.7)
  * `perform` (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 183`, `args: 78`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `dead_code: 2`
* *Architecture:* `api: 10`, `concurrency: 2`, `import: 35`
* *Defense:* `safety: 23`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` actions, actionElementLink, actionToggleShapeSwitch, shortcuts, types, analytics, ui-appState, library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/element/src/transform.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 517.84 | **LOC:** 810 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.8654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convertToExcalidrawElements` (Impact: 200.4)
  * `bindTextToContainer` (Impact: 157.3)
  * `add` (Impact: 4.6)
  * `getElement` (Impact: 1.7)
  * `getElementsMap` (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 106`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 51`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 36`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.827
  * `Choke Point (Betweenness):` 0.001144 | `Ripple Effect (Closeness):` 0.003645
  * `Imports (Out-Degree: 9):` Scene, binding, bounds, fractionalIndex, linearElementEditor, newElement, textElement, textMeasurements...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/excalidraw/data/library.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 511.38 | **LOC:** 1002 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (58.4359%), Tech Debt (9.538%)
**Top Internal Functions/Classes:**
  * `onHashChange` (Impact: 26.6)
  * `updateLibrary` (Impact: 25.8)
  * `getMaxWidthPerCol` (Impact: 15.1)
  * `createLibraryUpdate` (Impact: 14.1)
    * *Intent:* /** * Returns { deletedItems, addedItems } maps of all added and deleted items * since last onLibrar...
  * `importLibraryFromURL` (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 156
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 154`, `args: 64`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 60`, `dead_code: 6`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 18`, `concurrency: 46`, `import: 14`
* *Defense:* `safety: 32`, `doc: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.004
  * `Choke Point (Betweenness):` 0.001906 | `Ripple Effect (Closeness):` 0.057668
  * `Imports (Out-Degree: 8):` App, editor-jotai, errors, useLibraryItemSvg, i18n, types, blob, restore...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/element/tests/binding.test.tsx` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 1856.73
- `packages/element/src/binding.ts` -> **Márk Tolmács** (88.9% isolated ownership) | Magnitude: 1829.86
- `packages/element/src/elbowArrow.ts` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 1761.28
- `packages/element/src/linearElementEditor.ts` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 1371.88
- `packages/element/src/resizeElements.ts` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 940.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/excalidraw/components/App.tsx` -> **Severity: 1.455** (Bridge: 0.0145 * Flux: 100.0%)
- `packages/element/src/Scene.ts` -> **Severity: 0.605** (Bridge: 0.0061 * Flux: 98.5907%)
- `packages/excalidraw/tests/helpers/api.ts` -> **Severity: 0.466** (Bridge: 0.0047 * Flux: 100.0%)
- `packages/excalidraw/tests/helpers/ui.ts` -> **Severity: 0.21** (Bridge: 0.0031 * Flux: 67.7012%)
- `packages/excalidraw/data/library.ts` -> **Severity: 0.189** (Bridge: 0.0019 * Flux: 99.192%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/common/src/utility-types.ts` -> **Severity: 17.548** (Embedded: 0.1827 * Error Risk: 96.0402%)
- `packages/excalidraw/i18n.ts` -> **Severity: 10.821** (Embedded: 0.1367 * Error Risk: 79.1522%)
- `packages/excalidraw/errors.ts` -> **Severity: 7.157** (Embedded: 0.0847 * Error Risk: 84.54%)
- `packages/excalidraw/components/icons.tsx` -> **Severity: 6.487** (Embedded: 0.1216 * Error Risk: 53.3477%)
- `packages/excalidraw/actions/register.ts` -> **Severity: 4.952** (Embedded: 0.0745 * Error Risk: 66.5013%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/excalidraw/components/icons.tsx` -> **Severity: 2031.6** (Blast Radius: 20.316 * Doc Risk: 100.0%)
- `packages/excalidraw/tests/helpers/api.ts` -> **Severity: 1360.7** (Blast Radius: 13.607 * Doc Risk: 100.0%)
- `packages/excalidraw/i18n.ts` -> **Severity: 1271.95** (Blast Radius: 25.439 * Doc Risk: 50.0%)
- `packages/element/src/typeChecks.ts` -> **Severity: 1103.351** (Blast Radius: 11.664 * Doc Risk: 94.5946%)
- `packages/excalidraw/data/blob.ts` -> **Severity: 1092.671** (Blast Radius: 12.827 * Doc Risk: 85.1852%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
