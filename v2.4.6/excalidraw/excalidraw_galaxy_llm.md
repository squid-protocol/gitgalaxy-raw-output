# ARCHITECTURAL_BRIEF: excalidraw
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/excalidraw` |
| **Timestamp** | `2026-08-03T20:03:10.650238+00:00` |
| **Scan Duration** | `3.31s` |
| **Git Branch** | `master` |
| **Git Commit** | `e18c1dd213000dde0ae94ef7eb00aab537b39708` |
| **Git Remote** | `https://github.com/excalidraw/excalidraw.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 525 malicious artifacts.

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
| Total Artifacts | 1225 |
| Analyzed Artifacts (Scanned) | 718 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 507 |
| Total LOC | 142932 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 58.6% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6069 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.244 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7529 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 60 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 502 | 91603 | 69.9% |
| CSS | 84 | 7715 | 11.7% |
| JSON | 73 | 41088 | 10.2% |
| JAVASCRIPT | 22 | 2223 | 3.1% |
| MARKDOWN | 13 | 0 | 1.8% |
| PLAINTEXT | 13 | 2 | 1.8% |
| XML | 6 | 20 | 0.8% |
| YAML | 2 | 25 | 0.3% |
| HTML | 2 | 246 | 0.3% |
| DOCKERFILE | 1 | 10 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.668`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 468 | 65.2% |
| file_cluster_13 | 145 | 20.2% |
| file_cluster_2 | 33 | 4.6% |
| file_cluster_4 | 17 | 2.4% |
| file_cluster_17 | 10 | 1.4% |
| file_cluster_16 | 10 | 1.4% |
| file_cluster_0 | 5 | 0.7% |
| Unknown | 2 | 0.3% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 24 | 3.3% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 507*

**Composition by Extension & Reason:**
- `.woff2`: 237x Excluded (Explicitly Denied Extension: '.woff2')
- `.tsx`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 43 exceeds 500 chars), 1x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.ts`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 97 LOC), 1x Excluded (Machine-Generated Source Code Signature: 161 LOC)
- `.mdx`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 32x Excluded (Explicitly Denied Extension: '.png')
- `.snap`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.snap)
- `no_extension`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpeg`: 5x Excluded (Explicitly Denied Extension: '.jpeg')
- `.ttf`: 5x Excluded (Explicitly Denied Extension: '.ttf')
- `.js`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 3x Excluded (Explicitly Denied Extension: '.ico')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 12.9 | 7.3 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 22.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.3 | 2.3 | 80.0 |
| API Exposure | 0.0 | 19.6 | 4.7 | 4.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 13.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.1 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.4 | 1.9 | 1.1 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.5 | 5.7 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 50.5 | 45.7 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 15.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/excalidraw/components/icons.tsx` (Hits: 614)
- `packages/excalidraw/components/TTDDialog/utils/TTDstreamFetch.test.ts` (Hits: 46)
- `packages/excalidraw/subset/woff2/woff2-bindings.ts` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **icons.tsx** (`packages/excalidraw/components/icons.tsx`) — 96 inbound connections
2. **i18n.ts** (`packages/excalidraw/i18n.ts`) — 95 inbound connections
3. **utility-types.ts** (`packages/common/src/utility-types.ts`) — 45 inbound connections
4. **editor-jotai.ts** (`packages/excalidraw/editor-jotai.ts`) — 37 inbound connections
5. **register.ts** (`packages/excalidraw/actions/register.ts`) — 36 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **App.tsx** (`packages/excalidraw/components/App.tsx`) — 80 outbound dependencies
2. **App.tsx** (`excalidraw-app/App.tsx`) — 51 outbound dependencies
3. **index.ts** (`packages/element/src/index.ts`) — 48 outbound dependencies
4. **LayerUI.tsx** (`packages/excalidraw/components/LayerUI.tsx`) — 46 outbound dependencies
5. **index.tsx** (`packages/excalidraw/index.tsx`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `textPropertiesUpdated` (@ `packages/excalidraw/wysiwyg/textWysiwyg.tsx`) -> Impact: **1549.2** | LOC: 785
- `renderElementToSvg` (@ `packages/excalidraw/renderer/staticSvgScene.ts`) -> Impact: **1422.4** | LOC: 620
- `updateEmbedValidationStatus` (@ `packages/excalidraw/components/hyperlink/Hyperlink.tsx`) -> Impact: **673.6** | LOC: 272
- `truncateText` (@ `packages/excalidraw/scene/export.ts`) -> Impact: **530.4** | LOC: 493
- `perform` (@ `packages/excalidraw/actions/actionFinalize.tsx`) -> Impact: **497.7** | LOC: 294
- `cropElement` (@ `packages/element/src/cropElement.ts`) -> Impact: **492.5** | LOC: 364
- `onClose` (@ `packages/excalidraw/components/IconPicker.tsx`) -> Impact: **477.9** | LOC: 205
- `generateDynamicAABBs` (@ `packages/element/src/elbowArrow.ts`) -> Impact: **392.9** | LOC: 177
- `renderElement` (@ `packages/element/src/renderElement.ts`) -> Impact: **389.6** | LOC: 293
- `SearchMenu` (@ `packages/excalidraw/components/SearchMenu.tsx`) -> Impact: **387.7** | LOC: 358

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `errorSplash` (@ `excalidraw-app/components/TopErrorBoundary.tsx`) -> **O(2^N) [Recursive]**
- `keyTest` (@ `packages/excalidraw/actions/actionStyles.ts`) -> **O(2^N) [Recursive]**
- `onChange` (@ `packages/excalidraw/components/ColorPicker/ColorInput.tsx`) -> **O(2^N) [Recursive]**
- `getOpenPopup` (@ `packages/excalidraw/components/ColorPicker/ColorPicker.tsx`) -> **O(2^N) [Recursive]**
- `getShortcutKey` (@ `packages/excalidraw/components/HelpDialog.tsx`) -> **O(2^N) [Recursive]**
- `onClose` (@ `packages/excalidraw/components/IconPicker.tsx`) -> **O(2^N) [Recursive]**
- `onDrag` (@ `packages/excalidraw/components/LibraryUnit.tsx`) -> **O(2^N) [Recursive]**
- `updateEmbedValidationStatus` (@ `packages/excalidraw/components/hyperlink/Hyperlink.tsx`) -> **O(2^N) [Recursive]**
- `setCanvasUrl` (@ `examples/with-script-in-browser/components/ExampleApp.tsx`) -> **O(2^N) [Recursive]**
- `onCollabDialogOpen` (@ `excalidraw-app/components/AppWelcomeScreen.tsx`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/excalidraw/components/TTDDialog/utils/TTDstreamFetch.test.ts`) -> DB Complexity: **146**
- `setup` (@ `scripts/woff2/woff2-esbuild-plugins.js`) -> DB Complexity: **64**
  * *Intent:* /** * Custom esbuild plugin to: * 1. inline all woff2 (url and relative imports) as base64 for server-side use cases (no need for additional font fetc...
- `hashSelectionOpts` (@ `packages/element/src/Scene.ts`) -> DB Complexity: **63**
- `handleIframeLikeCenterClick` (@ `packages/excalidraw/components/App.tsx`) -> DB Complexity: **31**
- `renderElementToSvg` (@ `packages/excalidraw/renderer/staticSvgScene.ts`) -> DB Complexity: **31**
- `updateElementsToBeErased` (@ `packages/excalidraw/eraser/index.ts`) -> DB Complexity: **30**
- `normalize` (@ `packages/excalidraw/subset/woff2/woff2-bindings.ts`) -> DB Complexity: **30**
- `maybeDragNewGenericElement` (@ `packages/excalidraw/components/App.tsx`) -> DB Complexity: **28**
- `handleAppOnDrop` (@ `packages/excalidraw/components/App.tsx`) -> DB Complexity: **26**
- `createIcon` (@ `packages/excalidraw/components/icons.tsx`) -> DB Complexity: **24**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 12 | 10073.0 | 8.39% | 9.84% |
| `packages/element/src` | 47 | 1679.52 | 20.01% | 17.44% |
| `packages/excalidraw/components` | 130 | 1056.51 | 8.93% | 17.87% |
| `packages/excalidraw/actions` | 41 | 469.56 | 9.45% | 28.25% |
| `packages/excalidraw` | 34 | 429.4 | 23.08% | 20.55% |
| `packages/excalidraw/subset/woff2` | 2 | 422.99 | 50.34% | 33.07% |
| `packages/excalidraw/renderer` | 8 | 323.45 | 11.63% | 23.43% |
| `scripts` | 11 | 318.92 | 28.44% | 26.89% |
| `packages/excalidraw/wysiwyg` | 1 | 169.7 | 34.0% | 8.84% |
| `excalidraw-app` | 15 | 164.71 | 7.88% | 13.31% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Dockerfile` -> **100.0%** Exposure
- `scripts/build-locales-coverage.js` -> **100.0%** Exposure
- `packages/excalidraw/actions/actionAlign.tsx` -> **100.0%** Exposure
- `packages/excalidraw/errors.ts` -> **100.0%** Exposure
- `packages/excalidraw/components/Spinner.scss` -> **99.9996%** Exposure
### Highest State Flux (Mutation/Volatility)
- `excalidraw-app/collab/Collab.tsx` -> **100.0%** Exposure
- `excalidraw-app/components/TopErrorBoundary.tsx` -> **100.0%** Exposure
- `excalidraw-app/data/Locker.ts` -> **100.0%** Exposure
- `excalidraw-app/data/fileStatusStore.ts` -> **100.0%** Exposure
- `packages/common/src/appEventBus.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/excalidraw/subset/woff2/woff2-bindings.ts` -> **0** Orphaned Functions | **39** Duplicates
- `packages/excalidraw/components/Actions.tsx` -> **0** Orphaned Functions | **30** Duplicates
- `packages/element/src/binding.ts` -> **0** Orphaned Functions | **27** Duplicates
- `packages/excalidraw/components/icons.tsx` -> **0** Orphaned Functions | **22** Duplicates
- `packages/excalidraw/tests/helpers/ui.ts` -> **22** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/element/src/embeddable.ts`** -> AI Confidence: **99.39%**
2. **`packages/excalidraw/renderer/staticSvgScene.ts`** -> AI Confidence: **99.39%**
3. **`packages/element/src/binding.ts`** -> AI Confidence: **99.35%**
4. **`packages/element/src/elbowArrow.ts`** -> AI Confidence: **99.35%**
5. **`scripts/woff2/woff2-esbuild-plugins.js`** -> AI Confidence: **99.31%**
6. **`excalidraw-app/components/DebugCanvas.tsx`** -> AI Confidence: **99.31%**
7. **`packages/element/src/arrows/focus.ts`** -> AI Confidence: **99.31%**
8. **`packages/element/src/collision.ts`** -> AI Confidence: **99.31%**
9. **`packages/element/src/delta.ts`** -> AI Confidence: **99.31%**
10. **`packages/element/src/dragElements.ts`** -> AI Confidence: **99.31%**
11. **`packages/element/src/frame.ts`** -> AI Confidence: **99.31%**
12. **`packages/element/src/linearElementEditor.ts`** -> AI Confidence: **99.31%**
13. **`packages/element/src/newElement.ts`** -> AI Confidence: **99.31%**
14. **`packages/element/src/renderElement.ts`** -> AI Confidence: **99.31%**
15. **`packages/element/src/resizeElements.ts`** -> AI Confidence: **99.31%**
16. **`packages/element/src/transform.ts`** -> AI Confidence: **99.31%**
17. **`packages/element/src/zindex.ts`** -> AI Confidence: **99.31%**
18. **`packages/excalidraw/actions/actionDeleteSelected.tsx`** -> AI Confidence: **99.31%**
19. **`packages/excalidraw/actions/actionFinalize.tsx`** -> AI Confidence: **99.31%**
20. **`packages/excalidraw/actions/actionStyles.ts`** -> AI Confidence: **99.31%**
21. **`packages/excalidraw/components/Actions.tsx`** -> AI Confidence: **99.31%**
22. **`packages/excalidraw/components/App.tsx`** -> AI Confidence: **99.31%**
23. **`packages/excalidraw/components/ElementLinkDialog.tsx`** -> AI Confidence: **99.31%**
24. **`packages/excalidraw/components/FilledButton.tsx`** -> AI Confidence: **99.31%**
25. **`packages/excalidraw/components/HintViewer.tsx`** -> AI Confidence: **99.31%**
26. **`packages/excalidraw/components/IconPicker.tsx`** -> AI Confidence: **99.31%**
27. **`packages/excalidraw/components/SearchMenu.tsx`** -> AI Confidence: **99.31%**
28. **`packages/excalidraw/components/Stats/Dimension.tsx`** -> AI Confidence: **99.31%**
29. **`packages/excalidraw/components/Stats/MultiDimension.tsx`** -> AI Confidence: **99.31%**
30. **`packages/excalidraw/components/Stats/MultiPosition.tsx`** -> AI Confidence: **99.31%**
31. **`packages/excalidraw/components/TTDDialog/Chat/ChatInterface.tsx`** -> AI Confidence: **99.31%**
32. **`packages/excalidraw/components/TTDDialog/hooks/useTextGeneration.ts`** -> AI Confidence: **99.31%**
33. **`packages/excalidraw/components/ToolButton.tsx`** -> AI Confidence: **99.31%**
34. **`packages/excalidraw/components/hyperlink/Hyperlink.tsx`** -> AI Confidence: **99.31%**
35. **`packages/excalidraw/data/restore.ts`** -> AI Confidence: **99.31%**
36. **`packages/excalidraw/eraser/index.ts`** -> AI Confidence: **99.31%**
37. **`packages/excalidraw/renderer/interactiveScene.ts`** -> AI Confidence: **99.31%**
38. **`packages/excalidraw/renderer/staticScene.ts`** -> AI Confidence: **99.31%**
39. **`packages/excalidraw/scene/export.ts`** -> AI Confidence: **99.31%**
40. **`packages/excalidraw/tests/helpers/api.ts`** -> AI Confidence: **99.31%**
41. **`packages/excalidraw/wysiwyg/textWysiwyg.tsx`** -> AI Confidence: **99.31%**
42. **`packages/utils/src/export.ts`** -> AI Confidence: **99.31%**
43. **`packages/excalidraw/subset/harfbuzz/harfbuzz-bindings.ts`** -> AI Confidence: **99.29%**
44. **`excalidraw-app/App.tsx`** -> AI Confidence: **99.24%**
45. **`packages/element/src/duplicate.ts`** -> AI Confidence: **99.24%**
46. **`packages/element/src/selection.ts`** -> AI Confidence: **99.24%**
47. **`packages/element/src/textElement.ts`** -> AI Confidence: **99.24%**
48. **`packages/element/src/utils.ts`** -> AI Confidence: **99.24%**
49. **`packages/excalidraw/actions/actionBoundText.tsx`** -> AI Confidence: **99.24%**
50. **`packages/excalidraw/actions/actionElementLock.ts`** -> AI Confidence: **99.24%**
51. **`packages/excalidraw/actions/actionNavigate.tsx`** -> AI Confidence: **99.24%**
52. **`packages/excalidraw/actions/actionProperties.tsx`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `scripts/release.js` -> **100.0%** Exposure
- `excalidraw-app/App.tsx` -> **100.0%** Exposure
- `excalidraw-app/collab/Collab.tsx` -> **100.0%** Exposure
- `excalidraw-app/components/TopErrorBoundary.tsx` -> **100.0%** Exposure
- `excalidraw-app/data/LocalData.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `excalidraw-app/data/index.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `scripts/woff2/woff2-esbuild-plugins.js` -> **100.0%** Exposure
- `excalidraw-app/App.tsx` -> **100.0%** Exposure
- `excalidraw-app/collab/Collab.tsx` -> **100.0%** Exposure
- `excalidraw-app/components/TopErrorBoundary.tsx` -> **100.0%** Exposure
- `excalidraw-app/data/FileManager.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `278` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1240` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/excalidraw/components/TTDDialog/hooks/useMermaidRenderer.ts` (TYPESCRIPT) -> Cumulative Risk: **911.3**
- **Archetype:** `file_cluster_13` (Distance: 12.281 IQR)
- **Magnitude:** 18.32 | **LOC:** 214 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `useEffect` (Impact: 21.8), `fn` (Impact: 21.7), `async` (Impact: 19.6)

### 2. `excalidraw-app/data/LocalData.ts` (TYPESCRIPT) -> Cumulative Risk: **903.34**
- **Archetype:** `file_cluster_13` (Distance: 11.485 IQR)
- **Magnitude:** 16.98 | **LOC:** 278 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9166%)
- **Heaviest Functions:** `saveDataStateToLocalStorage` (Impact: 19.9), `getFiles` (Impact: 19.3), `updateBrowserStateVersion` (Impact: 9.1)

### 3. `packages/excalidraw/components/App.tsx` (TYPESCRIPT) -> Cumulative Risk: **886.56**
- **Archetype:** `file_cluster_17` (Distance: 15.19 IQR)
- **Magnitude:** 494.54 | **LOC:** 12839 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 40.4%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Churn (100.0%)
- **Heaviest Functions:** `handleAppOnDrop` (Impact: 126.2), `handleIframeLikeCenterClick` (Impact: 114.9), `maybeDragNewGenericElement` (Impact: 72.9)

### 4. `excalidraw-app/collab/Collab.tsx` (TYPESCRIPT) -> Cumulative Risk: **844.3**
- **Archetype:** `file_cluster_13` (Distance: 12.951 IQR)
- **Magnitude:** 54.71 | **LOC:** 1052 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 37.7), `onVisibilityChange` (Impact: 14.0), `componentDidMount` (Impact: 13.0)

### 5. `packages/excalidraw/components/AppStateObserver.ts` (TYPESCRIPT) -> Cumulative Risk: **842.06**
- **Archetype:** `file_cluster_4` (Distance: 12.706 IQR)
- **Magnitude:** 27.04 | **LOC:** 209 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `callback` (Impact: 153.0), `predicate` (Impact: 12.7), `callback` (Impact: 4.2)

### 6. `excalidraw-app/components/TopErrorBoundary.tsx` (TYPESCRIPT) -> Cumulative Risk: **788.76**
- **Archetype:** `file_cluster_13` (Distance: 10.773 IQR)
- **Magnitude:** 10.8 | **LOC:** 147 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `errorSplash` (Impact: 34.7), `createGithubIssue` (Impact: 15.9), `componentDidCatch` (Impact: 11.4)

### 7. `excalidraw-app/data/FileManager.ts` (TYPESCRIPT) -> Cumulative Risk: **779.09**
- **Archetype:** `file_cluster_13` (Distance: 11.437 IQR)
- **Magnitude:** 13.77 | **LOC:** 297 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9722%), State Flux (99.9719%)
- **Heaviest Functions:** `shouldPreventUnload` (Impact: 10.5), `isFileTracked` (Impact: 10.4), `reset` (Impact: 7.1)

### 8. `packages/excalidraw/actions/manager.tsx` (TYPESCRIPT) -> Cumulative Risk: **764.48**
- **Archetype:** `file_cluster_13` (Distance: 12.471 IQR)
- **Magnitude:** 28.59 | **LOC:** 202 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `trackAction` (Impact: 58.0), `renderAction` (Impact: 50.6), `handleKeyDown` (Impact: 46.8)

### 9. `packages/excalidraw/history.ts` (TYPESCRIPT) -> Cumulative Risk: **758.88**
- **Archetype:** `file_cluster_13` (Distance: 11.347 IQR)
- **Magnitude:** 14.7 | **LOC:** 250 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9997%), Logic Bomb (99.9931%), State Flux (99.9868%)
- **Heaviest Functions:** `record` (Impact: 17.1), `applyTo` (Impact: 14.7), `pop` (Impact: 14.1)

### 10. `packages/excalidraw/eraser/index.ts` (TYPESCRIPT) -> Cumulative Risk: **756.51**
- **Archetype:** `file_cluster_13` (Distance: 11.871 IQR)
- **Magnitude:** 27.58 | **LOC:** 307 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9997%), State Flux (99.999%)
- **Heaviest Functions:** `updateElementsToBeErased` (Impact: 101.2), `eraserTest` (Impact: 55.8), `constructor` (Impact: 8.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.env.production` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/components/App.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.19 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.387 IQR)
- **Top Global Matches:** file_cluster_17: 15.19, file_cluster_2: 15.297, file_cluster_13: 15.314
- **Magnitude:** 494.54 | **LOC:** 12839 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 40.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (75.388%), Tech Debt (9.6025%)
**Top Internal Functions/Classes:**
  * `handleAppOnDrop` (Impact: 126.2 | O(N^3) | DB: 26)
  * `handleIframeLikeCenterClick` (Impact: 114.9 | O(N^3) | DB: 31)
  * `maybeDragNewGenericElement` (Impact: 72.9 | O(N^2) | DB: 28)
  * `renderEmbeddables` (Impact: 68.3 | O(N^4) | DB: 13)
  * `handleCanvasContextMenu` (Impact: 65.9 | O(N^5) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1140`, `structural_boundaries: 717`, `args: 430`, `func_start: 308`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 3505`, `dead_code: 14`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 57`, `concurrency: 285`, `import: 83`
* *Defense:* `safety: 226`, `doc: 21`, `immutability_locks: 415`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` AppStateObserver, clipboard, Sidebar, react-dom, gesture, cursor, types, utility-types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/subset/woff2/woff2-bindings.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.389 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.997 IQR)
- **Top Global Matches:** file_cluster_8: 12.389, file_cluster_11: 12.892, file_cluster_7: 12.909
- **Magnitude:** 415.77 | **LOC:** 4052 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (65.3375%), Tech Debt (47.8952%)
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` (Impact: 147.8 | O(N^3) | DB: 18)
  * `genericPointerToWireType` (Impact: 139.0 | O(N^5) | DB: 19)
  * `__embind_register_std_string` (Impact: 126.2 | O(N^4) | DB: 9)
  * `stringToUTF8Array` (Impact: 114.3 | O(N^4) | DB: 2)
  * `__embind_register_class` (Impact: 110.3 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 720`, `structural_boundaries: 362`, `args: 745`, `func_start: 733`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 743`, `duplicate_logic: 39`
* *Architecture:* `io: 32`, `api: 32`, `concurrency: 8`, `import: 2`
* *Defense:* `safety: 48`, `doc: 1`, `test: 90`, `immutability_locks: 215`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.845
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00186
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/element/src/elbowArrow.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.568 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.957 IQR)
- **Top Global Matches:** file_cluster_8: 11.568, file_cluster_17: 11.732, file_cluster_13: 11.943
- **Magnitude:** 261.92 | **LOC:** 2310 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (20.1136%), Tech Debt (46.5456%)
**Top Internal Functions/Classes:**
  * `generateDynamicAABBs` (Impact: 392.9 | O(N^2))
  * `handleEndpointDrag` (Impact: 367.9 | O(N^3) | DB: 11)
  * `handleSegmentMove` (Impact: 253.8 | O(N^2) | DB: 5)
    * *Intent:* /**
  * `estimateSegmentCount` (Impact: 211.5 | O(N^2))
  * `handleSegmentRelease` (Impact: 192.3 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 236`, `args: 128`, `func_start: 112`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 164`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `io: 7`, `api: 4`, `import: 13`
* *Defense:* `safety: 69`, `doc: 22`, `immutability_locks: 197`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.402
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.021453
  * `Imports (Out-Degree: 6):` collision, types, mutateElement, heading, math, bounds, typeChecks, types...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/element/src/binding.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.228 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.871 IQR)
- **Top Global Matches:** file_cluster_8: 11.228, file_cluster_13: 11.659, file_cluster_2: 11.777
- **Magnitude:** 172.96 | **LOC:** 2941 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 88.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (15.2442%), Tech Debt (66.4288%)
**Top Internal Functions/Classes:**
  * `getBindingSideMidPoint` (Impact: 245.6 | O(N^2) | DB: 6)
  * `snapToMid` (Impact: 189.7 | O(N^2) | DB: 2)
  * `visitor` (Impact: 156.7 | O(N^4))
  * `bindPointToSnapToElementOutline` (Impact: 153.9 | O(N^3) | DB: 5)
  * `updateElementWith` (Impact: 142.9 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 493`, `structural_boundaries: 217`, `args: 128`, `func_start: 119`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 100`, `duplicate_logic: 27`
* *Architecture:* `api: 34`, `import: 20`
* *Defense:* `safety: 62`, `doc: 4`, `immutability_locks: 262`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.623
  * `Choke Point (Betweenness):` 0.000334 | `Ripple Effect (Closeness):` 0.026519
  * `Imports (Out-Degree: 10):` Scene, collision, elbowArrow, types, textElement, mutateElement, heading, bounds...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/excalidraw/wysiwyg/textWysiwyg.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.139 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.358 IQR)
- **Top Global Matches:** file_cluster_8: 11.139, file_cluster_13: 11.322, file_cluster_0: 11.465
- **Magnitude:** 169.7 | **LOC:** 1023 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 55.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (34.0022%), Tech Debt (8.8385%)
**Top Internal Functions/Classes:**
  * `textPropertiesUpdated` (Impact: 1549.2 | O(2^N) | DB: 23)
  * `getTransform` (Impact: 15.1 | O(N^1) | DB: 2)
  * `getLineDirection` (Impact: 5.7 | O(N^1))
  * `getViewportCoords` (Impact: 5.5 | O(N^1))
    * *Intent:* /** * textWysiwyg only deals with `originalText` *
  * `getCaretBoundaryOffsets` (Impact: 4.5 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 103`, `args: 67`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 86`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 21`
* *Defense:* `safety: 24`, `doc: 3`, `immutability_locks: 106`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.85
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 3):` App, actionCanvas, types, math, clipboard, actionProperties, element, types...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/excalidraw/renderer/staticSvgScene.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.892 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.9 IQR)
- **Top Global Matches:** file_cluster_8: 9.892, file_cluster_13: 10.22, file_cluster_0: 10.286
- **Magnitude:** 155.91 | **LOC:** 787 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (12.7024%), Tech Debt (9.2574%)
**Top Internal Functions/Classes:**
  * `renderElementToSvg` (Impact: 1422.4 | O(2^N) | DB: 31)
  * `renderSceneToSvg` (Impact: 71.8 | O(N^3))
  * `maybeWrapNodesInFrameClipPath` (Impact: 11.6 | O(N^1) | DB: 3)
  * `roughSVGDrawWithPrecision` (Impact: 7.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 47`, `args: 31`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 30`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 2`, `import: 18`
* *Defense:* `safety: 10`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.936
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 0):` core, types, types, svg, element, types, common
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.637 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 6.213 IQR)
- **Top Global Matches:** file_cluster_13: 10.637, file_cluster_0: 10.674, file_cluster_8: 10.708
- **Magnitude:** 130.6 | **LOC:** 240 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (23.9476%), Tech Debt (97.0688%)
**Top Internal Functions/Classes:**
  * `getArguments` (Impact: 37.9 | O(N^1) | DB: 3)
    * *Intent:* /**
  * `updatePackageJsons` (Impact: 19.5 | O(N^2) | DB: 6)
  * `askToCommit` (Impact: 18.9 | O(N^3))
  * `askToPublish` (Impact: 11.5 | O(N^2))
  * `buildPackages` (Impact: 4.2 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 26`, `args: 14`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 12`, `duplicate_logic: 4`
* *Architecture:* `io: 10`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 8`, `doc: 3`, `immutability_locks: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` readline, updateChangelog, child_process, fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/renderer/interactiveScene.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.352 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.766 IQR)
- **Top Global Matches:** file_cluster_8: 10.352, file_cluster_17: 11.039, file_cluster_7: 11.062
- **Magnitude:** 111.23 | **LOC:** 2091 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 61.5%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (12.1295%), Tech Debt (84.1437%)
**Top Internal Functions/Classes:**
  * `renderBindingHighlightForBindableElement` (Impact: 380.3 | O(N^4) | DB: 1)
  * `renderLinearPointHandles` (Impact: 182.6 | O(N^3) | DB: 1)
  * `renderLinearPointHandles` (Impact: 134.1 | O(N^4) | DB: 4)
  * `clamp` (Impact: 50.4 | O(N^4))
  * `renderCropHandles` (Impact: 39.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 135`, `args: 117`, `func_start: 78`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `planned_debt: 1`, `duplicate_logic: 20`
* *Architecture:* `api: 2`, `import: 18`
* *Defense:* `safety: 45`, `doc: 1`, `immutability_locks: 165`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00186
  * `Imports (Out-Degree: 5):` helpers, scrollbars, types, math, clients, renderSnaps, types, element...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/element/src/delta.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.808 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.558 IQR)
- **Top Global Matches:** file_cluster_13: 11.808, file_cluster_16: 11.821, file_cluster_8: 11.958
- **Magnitude:** 100.43 | **LOC:** 2067 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (34.2909%), Tech Debt (18.7922%)
**Top Internal Functions/Classes:**
  * `isEmpty` (Impact: 300.0 | O(2^N) | DB: 14)
  * `groupBy` (Impact: 131.7 | O(2^N) | DB: 2)
    * *Intent:* /**
  * `setValue` (Impact: 120.0 | O(2^N) | DB: 2)
  * `applyLatestChanges` (Impact: 84.8 | O(N^3) | DB: 5)
  * `postProcess` (Impact: 45.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 114`, `args: 52`, `func_start: 58`, `class_start: 3`
* *Risk/State:* `state_mutation: 111`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 45`, `import: 16`
* *Defense:* `safety: 32`, `doc: 27`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.052
  * `Choke Point (Betweenness):` 0.000149 | `Ripple Effect (Closeness):` 0.002789
  * `Imports (Out-Degree: 10):` Scene, groups, textElement, fractionalIndex, mutateElement, typeChecks, types, store...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/excalidraw/snapping.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.732 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.089 IQR)
- **Top Global Matches:** file_cluster_8: 10.732, file_cluster_13: 11.126, file_cluster_17: 11.131
- **Magnitude:** 98.33 | **LOC:** 1415 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (16.0973%), Tech Debt (23.5288%)
**Top Internal Functions/Classes:**
  * `snapResizingElements` (Impact: 159.6 | O(N^2) | DB: 9)
  * `getGapSnaps` (Impact: 143.4 | O(N^2) | DB: 6)
  * `createGapSnapLines` (Impact: 127.0 | O(N^4) | DB: 6)
  * `getVisibleGaps` (Impact: 74.4 | O(N^3) | DB: 9)
  * `getPointSnaps` (Impact: 68.8 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 170`, `args: 117`, `func_start: 98`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 112`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 36`, `import: 11`
* *Defense:* `safety: 15`, `immutability_locks: 163`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.103
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006376
  * `Imports (Out-Degree: 0):` types, math, element, types, common
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/element/src/comparisons.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.376 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.645 IQR)
- **Top Global Matches:** file_cluster_8: 7.376, file_cluster_13: 8.358, file_cluster_0: 8.406
- **Magnitude:** 93.5 | **LOC:** 52 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 61`, `args: 7`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.97
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002789
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/excalidraw/actions/actionProperties.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.066 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.794 IQR)
- **Top Global Matches:** file_cluster_8: 10.066, file_cluster_13: 10.397, file_cluster_2: 10.492
- **Magnitude:** 90.0 | **LOC:** 2044 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (10.5054%), Tech Debt (74.7563%)
**Top Internal Functions/Classes:**
  * `getNewFontSize` (Impact: 311.1 | O(2^N) | DB: 10)
  * `perform` (Impact: 177.0 | O(N^5) | DB: 1)
  * `getAttribute` (Impact: 61.8 | O(2^N) | DB: 1)
  * `restoreCaretPosition` (Impact: 30.2 | O(N^4))
  * `getBoundTextElement` (Impact: 28.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 198`, `args: 116`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 36`, `duplicate_logic: 18`
* *Architecture:* `api: 10`, `import: 31`
* *Defense:* `safety: 11`, `doc: 3`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.158
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004463
  * `Imports (Out-Degree: 8):` scene, element, common, icons, FontPicker, register, ColorPicker, fonts...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/element/src/renderElement.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.484 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.726 IQR)
- **Top Global Matches:** file_cluster_8: 9.484, file_cluster_13: 9.985, file_cluster_7: 10.164
- **Magnitude:** 83.48 | **LOC:** 1129 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.6587%), Tech Debt (8.5087%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 389.6 | O(N^4) | DB: 2)
  * `drawElementOnCanvas` (Impact: 250.8 | O(N^3) | DB: 2)
  * `generateElementWithCanvas` (Impact: 73.0 | O(N^2))
  * `getRenderOpacity` (Impact: 25.1 | O(N^1) | DB: 1)
  * `getCanvasPadding` (Impact: 24.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 63`, `args: 35`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 16`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 6`, `api: 10`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 11`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.97
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002789
  * `Imports (Out-Degree: 6):` rough, cropElement, types, textElement, types, shape, utils, math...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `excalidraw-app/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.287 IQR)
- **Top Global Matches:** file_cluster_0: 10.287, file_cluster_8: 10.296, file_cluster_13: 10.695
- **Magnitude:** 78.38 | **LOC:** 253 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (9.0032%), Tech Debt (94.3118%)
**Top Internal Functions/Classes:**
  * `getTheme` (Impact: 21.3 | O(N^3) | DB: 3)
  * `WebSocket` (Impact: 14.3 | O(N^3))
  * `setTheme` (Impact: 10.7 | O(N^3))
  * `media` (Impact: 3.5 | O(N^2))
  * `setTheme` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 11`, `args: 17`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 17`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.tsx, fonts.googleapis.com, favicon-16x16.png, favicon-32x32.png, fonts.css, apple-touch-icon.png, excalidraw.com, fonts.gstatic.com
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/components/hyperlink/Hyperlink.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.075 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.257 IQR)
- **Top Global Matches:** file_cluster_8: 10.075, file_cluster_13: 10.104, file_cluster_2: 10.428
- **Magnitude:** 77.47 | **LOC:** 496 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (17.5134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateEmbedValidationStatus` (Impact: 673.6 | O(2^N) | DB: 3)
  * `shouldHideLinkPopup` (Impact: 28.6 | O(N^1))
  * `renderTooltip` (Impact: 8.9 | O(N^1) | DB: 1)
  * `getContextMenuLabel` (Impact: 8.6 | O(N^1))
  * `hideHyperlinkToolip` (Impact: 5.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 73`, `args: 49`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 21`
* *Defense:* `safety: 8`, `immutability_locks: 48`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ToolButton, Tooltip, helpers, App, icons, scene, math, Hyperlink.scss...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/woff2/woff2-esbuild-plugins.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.124 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.439 IQR)
- **Top Global Matches:** file_cluster_13: 10.124, file_cluster_4: 10.15, file_cluster_8: 10.219
- **Magnitude:** 68.76 | **LOC:** 253 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (40.9048%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 39.7 | O(N^3) | DB: 64)
    * *Intent:* /** * Custom esbuild plugin to: * 1. inline all woff2 (url and relative imports) as base64 for serve...
  * `woff2ServerPlugin` (Impact: 1.1 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 10`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `io: 25`, `api: 2`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 0):` fonteditor-core, child_process, which, fs, path, wawoff2, esbuild
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/element/src/zindex.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.987 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.315 IQR)
- **Top Global Matches:** file_cluster_8: 10.987, file_cluster_13: 11.095, file_cluster_17: 11.219
- **Magnitude:** 66.67 | **LOC:** 605 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (22.4349%), Tech Debt (8.3067%)
**Top Internal Functions/Classes:**
  * `shiftFunction` (Impact: 162.5 | O(2^N) | DB: 6)
  * `getTargetIndex` (Impact: 115.5 | O(N^2))
  * `shiftElementsToEnd` (Impact: 75.7 | O(N^2) | DB: 4)
  * `shiftElementsByOne` (Impact: 62.8 | O(N^3) | DB: 2)
    * *Intent:* // assumes getElementsInGroup() returned elements are sorted // by zIndex (ascending)
  * `getTargetIndexAccountingForBinding` (Impact: 55.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 87`, `args: 39`, `func_start: 25`
* *Risk/State:* `state_mutation: 71`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 11`
* *Defense:* `safety: 11`, `doc: 6`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003138
  * `Imports (Out-Degree: 7):` selection, Scene, groups, collision, types, textElement, math, typeChecks...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/element/src/frame.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.2 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.757 IQR)
- **Top Global Matches:** file_cluster_17: 12.2, file_cluster_11: 12.369, file_cluster_13: 12.396
- **Magnitude:** 64.61 | **LOC:** 950 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (35.6078%), Tech Debt (8.7132%)
**Top Internal Functions/Classes:**
  * `updateFrameMembershipOfSelectedElements` (Impact: 234.6 | O(N^2) | DB: 9)
  * `getElementsInResizingFrame` (Impact: 70.8 | O(N^2) | DB: 6)
  * `filterElementsEligibleAsFrameChildren` (Impact: 39.0 | O(N^1) | DB: 3)
  * `omitPartialGroups` (Impact: 28.8 | O(N^3) | DB: 3)
  * `bindElementsToFramesAfterDuplication` (Impact: 26.9 | O(N^2))
    * *Intent:* // --------------------------- Frame State ------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 152`, `args: 95`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 84`, `dead_code: 9`, `planned_debt: 2`
* *Architecture:* `api: 42`, `import: 13`
* *Defense:* `safety: 12`, `doc: 5`, `immutability_locks: 128`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.626
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.011892
  * `Imports (Out-Degree: 8):` selection, Scene, groups, types, bbox, textElement, mutateElement, math...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/excalidraw/components/SearchMenu.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.934 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.381 IQR)
- **Top Global Matches:** file_cluster_8: 10.934, file_cluster_2: 11.011, file_cluster_13: 11.045
- **Magnitude:** 62.18 | **LOC:** 877 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (14.3981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SearchMenu` (Impact: 387.7 | O(N^6) | DB: 8)
  * `cb` (Impact: 49.2 | O(N^3) | DB: 6)
  * `getMatchedLines` (Impact: 30.1 | O(N^3) | DB: 4)
  * `MatchListBase` (Impact: 18.7 | O(N^3))
  * `getMatchPreview` (Impact: 18.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 101`, `args: 71`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`
* *Architecture:* `api: 2`, `import: 20`
* *Defense:* `safety: 18`, `immutability_locks: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` TextField, icons, SearchMenu.scss, App, frame, i18n, types, editor-jotai...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/updateChangelog.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.374 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.861 IQR)
- **Top Global Matches:** file_cluster_4: 10.374, file_cluster_17: 10.601, file_cluster_13: 10.76
- **Magnitude:** 59.92 | **LOC:** 107 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (61.2619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLibraryCommitsSinceLastRelease` (Impact: 15.1 | O(N^2) | DB: 6)
  * `getCommitHashForLastVersion` (Impact: 7.5 | O(N^1))
  * `updateChangelog` (Impact: 6.4 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 11`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 17`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 0):` util, child_process, fs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/element/src/cropElement.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.624 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.912 IQR)
- **Top Global Matches:** file_cluster_8: 9.624, file_cluster_7: 10.287, file_cluster_13: 10.358
- **Magnitude:** 59.9 | **LOC:** 630 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (18.5987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cropElement` (Impact: 492.5 | O(N^3) | DB: 5)
  * `recomputeOrigin` (Impact: 24.6 | O(N^1) | DB: 1)
  * `getFlipAdjustedCropPosition` (Impact: 11.8 | O(N^1) | DB: 2)
  * `getUncroppedImageElement` (Impact: 9.5 | O(N^2))
  * `adjustCropPosition` (Impact: 7.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 32`, `args: 33`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003138
  * `Imports (Out-Degree: 1):` types, bounds, math, transformHandles, points-on-curve
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/excalidraw/data/blob.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.373 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.853 IQR)
- **Top Global Matches:** file_cluster_4: 11.373, file_cluster_13: 11.498, file_cluster_8: 11.691
- **Magnitude:** 59.27 | **LOC:** 508 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (57.3316%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadSceneOrLibraryFromBlob` (Impact: 113.1 | O(N^4) | DB: 3)
  * `parseFileContents` (Impact: 81.8 | O(N^3) | DB: 1)
  * `getMimeType` (Impact: 40.8 | O(N^1) | DB: 1)
  * `normalizeFile` (Impact: 33.2 | O(N^1))
  * `getFileHandle` (Impact: 21.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 183`, `args: 44`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 17`
* *Architecture:* `io: 3`, `api: 41`, `concurrency: 94`, `import: 17`
* *Defense:* `safety: 31`, `doc: 9`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.488
  * `Choke Point (Betweenness):` 0.000717 | `Ripple Effect (Closeness):` 0.067344
  * `Imports (Out-Degree: 7):` errors, encode, types, filesystem, scene, json, nanoid, types...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `packages/excalidraw/components/CommandPalette/CommandPalette.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.816 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.104 IQR)
- **Top Global Matches:** file_cluster_8: 10.816, file_cluster_13: 10.869, file_cluster_17: 10.918
- **Magnitude:** 58.73 | **LOC:** 1049 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (14.7015%), Tech Debt (40.6885%)
**Top Internal Functions/Classes:**
  * `useEffect` (Impact: 159.1 | O(N^5) | DB: 4)
  * `onClick` (Impact: 132.2 | O(2^N) | DB: 1)
  * `useEffect` (Impact: 66.6 | O(N^4) | DB: 5)
  * `setCurrentCommand` (Impact: 52.7 | O(2^N))
  * `useEffect` (Impact: 19.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 178`, `args: 109`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `dead_code: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 8`, `concurrency: 2`, `import: 35`
* *Defense:* `safety: 28`, `sync_locks: 1`, `immutability_locks: 68`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` shortcuts, Ellipsify, scene, defaultCommandPaletteItems, useStable, types, common, ui-appState...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `excalidraw-app/index.html` (HTML) | Magnitude: 78.38 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 207, globals: 26, branch: 25, listeners: 23
- `packages/utils/src/export.ts` (TYPESCRIPT) | Magnitude: 6.81 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 157, branch: 49, structural_boundaries: 45, concurrency: 18
- `excalidraw-app/data/localStorage.ts` (TYPESCRIPT) | Magnitude: 8.68 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, branch: 23, structural_boundaries: 23, safety: 17
- `scripts/buildWasm.js` (JAVASCRIPT) | Magnitude: 23.26 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, immutability_locks: 20, io: 12, branch: 10
- `packages/common/src/url.ts` (TYPESCRIPT) | Magnitude: 2.85 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 14, branch: 7, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/excalidraw/components/TTDDialog/hooks/useMermaidRenderer.ts` (TYPESCRIPT) | Magnitude: 18.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 152, state_mutation: 53, structural_boundaries: 41, immutability_locks: 33
- `packages/excalidraw/actions/actionToggleObjectsSnapMode.tsx` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, args: 5, func_start: 5
- `packages/excalidraw/components/MobileMenu.tsx` (TYPESCRIPT) | Magnitude: 6.99 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 37, branch: 18, ui_framework: 17
- `packages/excalidraw/components/ButtonIcon.tsx` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 11, branch: 5, ui_framework: 4
- `packages/excalidraw/hooks/useScrollPosition.ts` (TYPESCRIPT) | Magnitude: 0.73 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, immutability_locks: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/math/src/vector.ts` (TYPESCRIPT) | Magnitude: 6.76 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 43, indent_spaces: 36, structural_boundaries: 30, api: 20
- `packages/math/src/rectangle.ts` (TYPESCRIPT) | Magnitude: 2.37 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 18, generics: 12, args: 10
- `packages/math/src/types.ts` (TYPESCRIPT) | Magnitude: 3.21 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 39, indent_spaces: 23, api: 16, doc: 15
- `packages/math/src/triangle.ts` (TYPESCRIPT) | Magnitude: 1.77 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, immutability_locks: 6, branch: 5
- `excalidraw-app/data/Locker.ts` (TYPESCRIPT) | Magnitude: 2.39 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 11, indent_spaces: 11, structural_boundaries: 7, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/element/src/visualdebug.ts` (TYPESCRIPT) | Magnitude: 13.22 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 195, branch: 86, structural_boundaries: 44, func_start: 38
- `packages/excalidraw/components/ToolPopover.tsx` (TYPESCRIPT) | Magnitude: 1.45 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 49, args: 15, branch: 12
- `packages/excalidraw/actions/actionElementLock.ts` (TYPESCRIPT) | Magnitude: 28.86 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 44, branch: 31, immutability_locks: 26
- `packages/element/src/positionElementsOnGrid.ts` (TYPESCRIPT) | Magnitude: 5.71 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 19, immutability_locks: 15, state_mutation: 14
- `packages/excalidraw/components/App.tsx` (TYPESCRIPT) | Magnitude: 494.54 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6234, state_mutation: 3505, branch: 1140, structural_boundaries: 717

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/excalidraw/components/Sidebar/SidebarHeader.tsx` (TYPESCRIPT) | Magnitude: 0.33 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, ui_framework: 14, structural_boundaries: 12, import: 8
- `packages/excalidraw/components/PasteChartDialog.tsx` (TYPESCRIPT) | Magnitude: 11.74 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 211, structural_boundaries: 58, ui_framework: 40, args: 37
- `packages/excalidraw/hooks/useEmitter.ts` (TYPESCRIPT) | Magnitude: 0.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, args: 6, ui_framework: 6
- `packages/excalidraw/components/LaserPointerButton.tsx` (TYPESCRIPT) | Magnitude: 0.69 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 10, ui_framework: 9, branch: 4
- `packages/common/src/appEventBus.test.ts` (TYPESCRIPT) | Magnitude: 3.87 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 49, concurrency: 30, structural_boundaries: 16, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/common/src/appEventBus.ts` (TYPESCRIPT) | Magnitude: 15.09 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 62, structural_boundaries: 41, generics: 28
- `packages/excalidraw/subset/subset-main.ts` (TYPESCRIPT) | Magnitude: 9.07 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, concurrency: 35, structural_boundaries: 32, immutability_locks: 11
- `packages/excalidraw/components/AppStateObserver.ts` (TYPESCRIPT) | Magnitude: 27.04 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 171, state_mutation: 65, structural_boundaries: 54, args: 40
- `excalidraw-app/data/firebase.ts` (TYPESCRIPT) | Magnitude: 22.07 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 86, immutability_locks: 57, concurrency: 54
- `packages/excalidraw/data/blob.ts` (TYPESCRIPT) | Magnitude: 59.27 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 346, structural_boundaries: 183, branch: 110, concurrency: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scripts/locales-coverage-description.js` (JAVASCRIPT) | Magnitude: 18.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: debug_prints: 5, indent_spaces: 5, branch: 3, state_mutation: 3
- `packages/element/src/elementLink.ts` (TYPESCRIPT) | Magnitude: 5.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 34, branch: 16, immutability_locks: 11
- `packages/common/global.d.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, decorators: 2
- `packages/element/global.d.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, decorators: 2
- `packages/math/global.d.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, decorators: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/excalidraw/subset/harfbuzz/harfbuzz-bindings.ts` (TYPESCRIPT) | Magnitude: 8.0 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 65, dead_code: 12, immutability_locks: 11, branch: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/excalidraw/components/App.tsx` -> Churn: **100.0%** | Cog Load: 75.388% | Debt: 9.6025%
- `packages/excalidraw/renderer/interactiveScene.ts` -> Churn: **61.24%** | Cog Load: 12.1295% | Debt: 84.1437%
- `packages/element/src/binding.ts` -> Churn: **56.15%** | Cog Load: 15.2442% | Debt: 66.4288%
- `packages/excalidraw/actions/actionProperties.tsx` -> Churn: **53.71%** | Cog Load: 10.5054% | Debt: 74.7563%
- `packages/excalidraw/components/dropdownMenu/DropdownMenu.scss` -> Churn: **51.21%** | Cog Load: 5.566% | Debt: 90.4377%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/element/src/binding.ts` -> **Márk Tolmács** (88.9% isolated ownership) | Magnitude: 172.96
- `scripts/release.js` -> **Marcel Mraz** (100.0% isolated ownership) | Magnitude: 130.6
- `packages/element/src/delta.ts` -> **Marcel Mraz** (100.0% isolated ownership) | Magnitude: 100.43
- `excalidraw-app/index.html` -> **David Luzar** (100.0% isolated ownership) | Magnitude: 78.38
- `packages/excalidraw/components/hyperlink/Hyperlink.tsx` -> **Ryan Di** (100.0% isolated ownership) | Magnitude: 77.47

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/excalidraw/i18n.ts` -> **Severity: 0.039** (Bridge: 0.001 * Flux: 37.866%)
- `excalidraw-app/collab/Portal.tsx` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 99.9995%)
- `excalidraw-app/collab/Collab.tsx` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)
- `excalidraw-app/data/FileManager.ts` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 99.9719%)
- `packages/excalidraw/shortcut.ts` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 97.0181%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/common/src/utility-types.ts` -> **Severity: 12.777** (Embedded: 0.1469 * Error Risk: 86.9723%)
- `packages/excalidraw/i18n.ts` -> **Severity: 8.68** (Embedded: 0.1343 * Error Risk: 64.6478%)
- `packages/excalidraw/components/icons.tsx` -> **Severity: 6.809** (Embedded: 0.1356 * Error Risk: 50.2045%)
- `packages/excalidraw/errors.ts` -> **Severity: 5.962** (Embedded: 0.0703 * Error Risk: 84.8076%)
- `packages/excalidraw/data/json.ts` -> **Severity: 4.663** (Embedded: 0.0867 * Error Risk: 53.8142%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/common/src/utility-types.ts` -> **Severity: 4301.9** (Blast Radius: 43.019 * Doc Risk: 100.0%)
- `packages/excalidraw/components/icons.tsx` -> **Severity: 2724.7** (Blast Radius: 27.247 * Doc Risk: 100.0%)
- `packages/excalidraw/data/blob.ts` -> **Severity: 1748.8** (Blast Radius: 17.488 * Doc Risk: 100.0%)
- `packages/excalidraw/data/json.ts` -> **Severity: 1675.2** (Blast Radius: 16.752 * Doc Risk: 100.0%)
- `packages/excalidraw/appState.ts` -> **Severity: 1329.3** (Blast Radius: 13.293 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
