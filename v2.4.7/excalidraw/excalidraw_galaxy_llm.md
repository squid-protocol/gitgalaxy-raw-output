# ARCHITECTURAL_BRIEF: excalidraw
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/excalidraw` |
| **Timestamp** | `2026-08-07T04:24:01.501265+00:00` |
| **Scan Duration** | `3.28s` |
| **Git Branch** | `master` |
| **Git Commit** | `e18c1dd213000dde0ae94ef7eb00aab537b39708` |
| **Git Remote** | `https://github.com/excalidraw/excalidraw.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 525 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.625`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 463 | 64.5% |
| file_cluster_13 | 150 | 20.9% |
| file_cluster_2 | 31 | 4.3% |
| file_cluster_4 | 19 | 2.6% |
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
| Error & Exception Exposure | 0.0 | 99.9 | 22.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.6 | 4.8 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.1 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.4 | 1.9 | 1.1 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.5 | 5.7 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.5 | 25.7 | 0.0 |
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

- `renderElementToSvg` (@ `packages/excalidraw/renderer/staticSvgScene.ts`) -> Impact: **378.9** | LOC: 620
- `textPropertiesUpdated` (@ `packages/excalidraw/wysiwyg/textWysiwyg.tsx`) -> Impact: **341.2** | LOC: 785
- `cropElement` (@ `packages/element/src/cropElement.ts`) -> Impact: **255.4** | LOC: 364
- `generateDynamicAABBs` (@ `packages/element/src/elbowArrow.ts`) -> Impact: **211.2** | LOC: 177
- `handleEndpointDrag` (@ `packages/element/src/elbowArrow.ts`) -> Impact: **188.8** | LOC: 195
- `perform` (@ `packages/excalidraw/actions/actionFinalize.tsx`) -> Impact: **175.7** | LOC: 294
- `handleSegmentMove` (@ `packages/element/src/elbowArrow.ts`) -> Impact: **173.2** | LOC: 240
  * *Intent:* /**
- `getBindingSideMidPoint` (@ `packages/element/src/binding.ts`) -> Impact: **168.6** | LOC: 292
- `renderElement` (@ `packages/element/src/renderElement.ts`) -> Impact: **164.7** | LOC: 293
- `renderBindingHighlightForBindableElement` (@ `packages/excalidraw/renderer/interactiveScene.ts`) -> Impact: **162.1** | LOC: 331

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 12 | 10072.59 | 6.36% | 9.84% |
| `packages/element/src` | 47 | 1406.79 | 20.4% | 48.13% |
| `packages/excalidraw/components` | 130 | 898.38 | 8.94% | 27.03% |
| `packages/excalidraw/subset/woff2` | 2 | 439.39 | 38.33% | 100.0% |
| `packages/excalidraw` | 34 | 393.12 | 24.26% | 25.97% |
| `packages/excalidraw/actions` | 41 | 319.09 | 9.93% | 39.94% |
| `scripts` | 11 | 305.72 | 23.35% | 27.15% |
| `packages/excalidraw/renderer` | 8 | 223.6 | 11.6% | 62.28% |
| `packages/common/src` | 21 | 160.77 | 30.01% | 14.68% |
| `excalidraw-app` | 15 | 141.17 | 8.26% | 27.14% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Dockerfile` -> **100.0%** Exposure
- `scripts/build-locales-coverage.js` -> **100.0%** Exposure
- `scripts/release.js` -> **100.0%** Exposure
- `packages/common/src/promise-pool.ts` -> **100.0%** Exposure
- `packages/excalidraw/actions/actionAlign.tsx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `excalidraw-app/collab/Collab.tsx` -> **100.0%** Exposure
- `excalidraw-app/components/TopErrorBoundary.tsx` -> **100.0%** Exposure
- `excalidraw-app/data/Locker.ts` -> **100.0%** Exposure
- `excalidraw-app/data/fileStatusStore.ts` -> **100.0%** Exposure
- `packages/common/src/appEventBus.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/excalidraw/subset/woff2/woff2-bindings.ts` -> **0** Orphaned Functions | **295** Duplicates
- `packages/common/src/colors.test.ts` -> **0** Orphaned Functions | **57** Duplicates
- `packages/element/src/__tests__/transform.test.ts` -> **0** Orphaned Functions | **54** Duplicates
- `packages/element/src/binding.ts` -> **0** Orphaned Functions | **47** Duplicates
- `packages/excalidraw/components/CommandPalette/CommandPalette.tsx` -> **0** Orphaned Functions | **46** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `278` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1240` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/excalidraw/components/AppStateObserver.ts` (TYPESCRIPT) -> Cumulative Risk: **753.61**
- **Archetype:** `file_cluster_4` (Distance: 12.536 IQR)
- **Magnitude:** 23.17 | **LOC:** 209 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9985%)
- **Heaviest Functions:** `callback` (Impact: 56.0), `flush` (Impact: 13.1), `getValue` (Impact: 12.6)

### 2. `packages/common/src/versionedSnapshotStore.ts` (TYPESCRIPT) -> Cumulative Risk: **715.92**
- **Archetype:** `file_cluster_4` (Distance: 13.264 IQR)
- **Magnitude:** 9.99 | **LOC:** 71 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `set` (Impact: 9.0), `pull` (Impact: 4.9), `subscriber` (Impact: 3.1)

### 3. `packages/excalidraw/components/TTDDialog/hooks/useMermaidRenderer.ts` (TYPESCRIPT) -> Cumulative Risk: **697.61**
- **Archetype:** `file_cluster_4` (Distance: 12.273 IQR)
- **Magnitude:** 17.3 | **LOC:** 214 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8115%)
- **Heaviest Functions:** `useEffect` (Impact: 14.7), `async` (Impact: 13.7), `fn` (Impact: 11.7)

### 4. `packages/excalidraw/components/App.tsx` (TYPESCRIPT) -> Cumulative Risk: **691.12**
- **Archetype:** `file_cluster_17` (Distance: 15.167 IQR)
- **Magnitude:** 465.51 | **LOC:** 12839 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 40.4%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (94.9251%)
- **Heaviest Functions:** `handleAppOnDrop` (Impact: 66.2), `handleIframeLikeCenterClick` (Impact: 61.2), `maybeDragNewGenericElement` (Impact: 50.5)

### 5. `excalidraw-app/collab/Collab.tsx` (TYPESCRIPT) -> Cumulative Risk: **649.02**
- **Archetype:** `file_cluster_13` (Distance: 12.879 IQR)
- **Magnitude:** 50.91 | **LOC:** 1052 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.5597%), Safety Score (95.7674%)
- **Heaviest Functions:** `constructor` (Impact: 17.0), `onVisibilityChange` (Impact: 9.7), `componentDidMount` (Impact: 9.4)

### 6. `excalidraw-app/data/LocalData.ts` (TYPESCRIPT) -> Cumulative Risk: **643.33**
- **Archetype:** `file_cluster_13` (Distance: 11.483 IQR)
- **Magnitude:** 16.77 | **LOC:** 278 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.889%), Concurrency (99.8499%), State Flux (88.7466%)
- **Heaviest Functions:** `saveDataStateToLocalStorage` (Impact: 19.9), `async` (Impact: 13.7), `getFiles` (Impact: 8.7)

### 7. `packages/excalidraw/errors.ts` (TYPESCRIPT) -> Cumulative Risk: **618.63**
- **Archetype:** `file_cluster_4` (Distance: 11.472 IQR)
- **Magnitude:** 8.67 | **LOC:** 91 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9958%), Concurrency (99.9396%)
- **Heaviest Functions:** `super` (Impact: 6.8), `super` (Impact: 2.7), `constructor` (Impact: 2.6)

### 8. `packages/common/src/promise-pool.ts` (TYPESCRIPT) -> Cumulative Risk: **612.23**
- **Archetype:** `file_cluster_4` (Distance: 13.155 IQR)
- **Magnitude:** 3.87 | **LOC:** 51 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `all` (Impact: 4.5), `constructor` (Impact: 2.5), `setTimeout` (Impact: 1.6)

### 9. `packages/common/src/appEventBus.ts` (TYPESCRIPT) -> Cumulative Risk: **612.06**
- **Archetype:** `file_cluster_4` (Distance: 13.436 IQR)
- **Magnitude:** 14.65 | **LOC:** 137 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9888%)
- **Heaviest Functions:** `on` (Impact: 17.4), `emit` (Impact: 15.1), `getEmitter` (Impact: 5.7)

### 10. `packages/element/src/store.ts` (TYPESCRIPT) -> Cumulative Risk: **601.6**
- **Archetype:** `file_cluster_13` (Distance: 11.997 IQR)
- **Magnitude:** 50.71 | **LOC:** 1038 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9864%), State Flux (84.9463%), Safety Score (81.8589%)
- **Heaviest Functions:** `super` (Impact: 20.4), `maybeClone` (Impact: 16.0), `emitDurableIncrement` (Impact: 14.9)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.834
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/components/App.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.167 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.377 IQR)
- **Top Global Matches:** file_cluster_17: 15.167, file_cluster_2: 15.276, file_cluster_13: 15.291
- **Magnitude:** 465.51 | **LOC:** 12839 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 40.4%
- **Risk Profile:** Cognitive Load (75.388%), Tech Debt (19.4368%)
**Top Internal Functions/Classes:**
  * `handleAppOnDrop` (Impact: 66.2)
  * `handleIframeLikeCenterClick` (Impact: 61.2)
  * `maybeDragNewGenericElement` (Impact: 50.5)
  * `isIframeLikeElementCenter` (Impact: 35.3)
  * `maybeHandleCrop` (Impact: 34.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1140`, `structural_boundaries: 717`, `args: 430`, `func_start: 308`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 3479`, `dead_code: 14`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 16`
* *Architecture:* `io: 2`, `api: 57`, `concurrency: 285`, `import: 83`
* *Defense:* `safety: 226`, `doc: 21`, `immutability_locks: 415`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` types, blob, filesystem, types, animation-frame-handler, mermaid, textAutoResizeHandle, icons...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/subset/woff2/woff2-bindings.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.427 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.104 IQR)
- **Top Global Matches:** file_cluster_8: 12.427, file_cluster_11: 12.912, file_cluster_7: 12.941
- **Magnitude:** 434.33 | **LOC:** 4052 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3114%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` (Impact: 76.3)
  * `__embind_register_std_string` (Impact: 53.5)
  * `registerType` (Impact: 53.3)
  * `genericPointerToWireType` (Impact: 49.0)
  * `stringToUTF8Array` (Impact: 47.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 720`, `structural_boundaries: 362`, `args: 743`, `func_start: 733`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 739`, `duplicate_logic: 295`
* *Architecture:* `io: 32`, `api: 40`, `concurrency: 8`, `import: 2`
* *Defense:* `safety: 48`, `doc: 1`, `test: 90`, `immutability_locks: 215`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.845
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00186
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/element/src/elbowArrow.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.57 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.973 IQR)
- **Top Global Matches:** file_cluster_8: 11.57, file_cluster_17: 11.722, file_cluster_13: 11.939
- **Magnitude:** 189.05 | **LOC:** 2310 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (20.1136%), Tech Debt (99.1945%)
**Top Internal Functions/Classes:**
  * `generateDynamicAABBs` (Impact: 211.2)
  * `handleEndpointDrag` (Impact: 188.8)
  * `handleSegmentMove` (Impact: 173.2)
    * *Intent:* /**
  * `estimateSegmentCount` (Impact: 142.9)
  * `handleSegmentRelease` (Impact: 100.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 236`, `args: 148`, `func_start: 112`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 164`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 38`
* *Architecture:* `io: 7`, `api: 4`, `import: 13`
* *Defense:* `safety: 69`, `doc: 22`, `immutability_locks: 197`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.402
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.021453
  * `Imports (Out-Degree: 6):` heading, types, collision, types, binding, distance, common, typeChecks...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/element/src/binding.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.198 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.883 IQR)
- **Top Global Matches:** file_cluster_8: 11.198, file_cluster_13: 11.627, file_cluster_2: 11.748
- **Magnitude:** 135.34 | **LOC:** 2941 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (15.1474%), Tech Debt (95.4342%)
**Top Internal Functions/Classes:**
  * `getBindingSideMidPoint` (Impact: 168.6)
  * `snapToMid` (Impact: 128.9)
  * `bindPointToSnapToElementOutline` (Impact: 80.4)
  * `visitor` (Impact: 64.9)
  * `normalizeFixedPoint` (Impact: 44.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 493`, `structural_boundaries: 217`, `args: 126`, `func_start: 119`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 98`, `duplicate_logic: 47`
* *Architecture:* `api: 35`, `import: 20`
* *Defense:* `safety: 62`, `doc: 4`, `immutability_locks: 262`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.623
  * `Choke Point (Betweenness):` 0.000334 | `Ripple Effect (Closeness):` 0.026519
  * `Imports (Out-Degree: 10):` heading, linearElementEditor, types, collision, Scene, mutateElement, types, typeChecks...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `scripts/release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.612 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.306 IQR)
- **Top Global Matches:** file_cluster_13: 10.612, file_cluster_0: 10.647, file_cluster_8: 10.694
- **Magnitude:** 124.0 | **LOC:** 240 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.0322%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getArguments` (Impact: 37.9)
    * *Intent:* /**
  * `updatePackageJsons` (Impact: 13.5)
  * `askToCommit` (Impact: 10.3)
  * `askToPublish` (Impact: 8.1)
  * `buildPackages` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 26`, `args: 14`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 12`, `duplicate_logic: 12`
* *Architecture:* `io: 10`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 8`, `doc: 3`, `immutability_locks: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` updateChangelog, readline, path, fs, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/renderer/interactiveScene.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.354 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.782 IQR)
- **Top Global Matches:** file_cluster_8: 10.354, file_cluster_17: 11.032, file_cluster_7: 11.063
- **Magnitude:** 94.26 | **LOC:** 2091 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 61.5%
- **Risk Profile:** Cognitive Load (11.8802%), Tech Debt (99.628%)
**Top Internal Functions/Classes:**
  * `renderBindingHighlightForBindableElement` (Impact: 162.1)
  * `renderLinearPointHandles` (Impact: 94.4)
  * `renderLinearPointHandles` (Impact: 57.0)
  * `isBindableElement` (Impact: 46.4)
  * `pointsEqual` (Impact: 34.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 135`, `args: 117`, `func_start: 78`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `planned_debt: 1`, `duplicate_logic: 39`
* *Architecture:* `api: 2`, `import: 18`
* *Defense:* `safety: 45`, `doc: 1`, `immutability_locks: 165`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00186
  * `Imports (Out-Degree: 5):` scrollbars, types, types, textAutoResizeHandle, roundRect, renderSnaps, helpers, clients...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/element/src/comparisons.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.376 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.645 IQR)
- **Top Global Matches:** file_cluster_8: 7.376, file_cluster_13: 8.358, file_cluster_0: 8.406
- **Magnitude:** 93.5 | **LOC:** 52 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 50.0%
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

### `packages/excalidraw/snapping.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.721 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.119 IQR)
- **Top Global Matches:** file_cluster_8: 10.721, file_cluster_17: 11.097, file_cluster_13: 11.101
- **Magnitude:** 91.49 | **LOC:** 1415 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (23.6391%), Tech Debt (99.9862%)
**Top Internal Functions/Classes:**
  * `snapResizingElements` (Impact: 108.7)
  * `getGapSnaps` (Impact: 98.5)
  * `createGapSnapLines` (Impact: 56.6)
  * `rangeInclusive` (Impact: 42.4)
  * `getVisibleGaps` (Impact: 40.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 170`, `args: 117`, `func_start: 98`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 112`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 36`
* *Architecture:* `api: 36`, `import: 11`
* *Defense:* `safety: 15`, `immutability_locks: 163`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.103
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006376
  * `Imports (Out-Degree: 0):` types, element, types, common, math
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/excalidraw/renderer/staticSvgScene.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.808 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.905 IQR)
- **Top Global Matches:** file_cluster_8: 9.808, file_cluster_13: 10.125, file_cluster_0: 10.189
- **Magnitude:** 79.21 | **LOC:** 787 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (12.7024%), Tech Debt (99.8531%)
**Top Internal Functions/Classes:**
  * `renderElementToSvg` (Impact: 378.9)
  * `addToRoot` (Impact: 49.8)
  * `addToRoot` (Impact: 41.6)
  * `renderSceneToSvg` (Impact: 37.9)
  * `isInitializedImageElement` (Impact: 36.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 47`, `args: 31`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 30`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `io: 8`, `api: 2`, `import: 18`
* *Defense:* `safety: 10`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.936
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 0):` types, types, svg, core, element, types, common
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/element/src/renderElement.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.439 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.713 IQR)
- **Top Global Matches:** file_cluster_8: 9.439, file_cluster_13: 9.932, file_cluster_7: 10.122
- **Magnitude:** 74.07 | **LOC:** 1129 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (10.6587%), Tech Debt (91.4426%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 164.7)
  * `drawElementOnCanvas` (Impact: 130.8)
  * `getContainingFrame` (Impact: 95.1)
  * `drawElementFromCanvas` (Impact: 86.5)
  * `generateElementWithCanvas` (Impact: 49.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 63`, `args: 35`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 16`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 6`, `api: 10`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 11`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.97
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002789
  * `Imports (Out-Degree: 6):` linearElementEditor, types, shape, cropElement, canvas, types, typeChecks, common...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/element/src/frame.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.116 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.747 IQR)
- **Top Global Matches:** file_cluster_17: 12.116, file_cluster_11: 12.299, file_cluster_13: 12.317
- **Magnitude:** 67.42 | **LOC:** 950 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.3838%), Tech Debt (99.3814%)
**Top Internal Functions/Classes:**
  * `updateFrameMembershipOfSelectedElements` (Impact: 160.8)
  * `getElementsInResizingFrame` (Impact: 48.7)
  * `shouldApplyFrameClip` (Impact: 47.9)
  * `filterElementsEligibleAsFrameChildren` (Impact: 39.0)
  * `getTargetFrame` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 152`, `args: 93`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 80`, `dead_code: 9`, `planned_debt: 2`, `duplicate_logic: 13`
* *Architecture:* `api: 46`, `import: 13`
* *Defense:* `safety: 12`, `doc: 5`, `immutability_locks: 128`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.626
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.011892
  * `Imports (Out-Degree: 8):` bounds, types, Scene, groups, mutateElement, types, selection, common...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/element/src/delta.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.799 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.564 IQR)
- **Top Global Matches:** file_cluster_13: 11.799, file_cluster_16: 11.819, file_cluster_8: 11.955
- **Magnitude:** 66.98 | **LOC:** 2067 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.3434%), Tech Debt (99.4129%)
**Top Internal Functions/Classes:**
  * `isEmpty` (Impact: 68.1)
  * `squash` (Impact: 67.5)
  * `groupBy` (Impact: 45.5)
    * *Intent:* /**
  * `applyLatestChanges` (Impact: 44.5)
  * `setValue` (Impact: 41.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 114`, `args: 63`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `state_mutation: 107`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `api: 45`, `import: 16`
* *Defense:* `safety: 32`, `doc: 27`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.052
  * `Choke Point (Betweenness):` 0.000149 | `Ripple Effect (Closeness):` 0.002789
  * `Imports (Out-Degree: 10):` types, fractionalIndex, store, types, linearElementEditor, Scene, groups, mutateElement...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/woff2/woff2-esbuild-plugins.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.138 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.439 IQR)
- **Top Global Matches:** file_cluster_13: 10.138, file_cluster_4: 10.164, file_cluster_8: 10.254
- **Magnitude:** 66.96 | **LOC:** 253 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9048%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 22.8)
    * *Intent:* /** * Custom esbuild plugin to: * 1. inline all woff2 (url and relative imports) as base64 for serve...
  * `async` (Impact: 7.6)
  * `getNameField` (Impact: 4.0)
  * `execSync` (Impact: 2.5)
  * `woff2ServerPlugin` (Impact: 1.1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 10`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `io: 25`, `api: 3`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 0):` esbuild, path, wawoff2, fs, child_process, which, fonteditor-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/excalidraw/actions/actionProperties.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.057 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.825 IQR)
- **Top Global Matches:** file_cluster_8: 10.057, file_cluster_13: 10.38, file_cluster_2: 10.48
- **Magnitude:** 57.67 | **LOC:** 2044 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (10.4185%), Tech Debt (99.5799%)
**Top Internal Functions/Classes:**
  * `getNewFontSize` (Impact: 71.1)
  * `perform` (Impact: 65.2)
  * `perform` (Impact: 45.8)
  * `withCaretPositionPreservation` (Impact: 22.0)
  * `getAttribute` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 198`, `args: 107`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 36`, `duplicate_logic: 40`
* *Architecture:* `api: 10`, `import: 31`
* *Defense:* `safety: 11`, `doc: 3`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.158
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004463
  * `Imports (Out-Degree: 8):` types, icons, register, react, math, analytics, Range, RadioSelection...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scripts/updateChangelog.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.374 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.861 IQR)
- **Top Global Matches:** file_cluster_4: 10.374, file_cluster_17: 10.601, file_cluster_13: 10.76
- **Magnitude:** 53.92 | **LOC:** 107 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.2619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLibraryCommitsSinceLastRelease` (Impact: 10.8)
  * `getCommitHashForLastVersion` (Impact: 7.5)
  * `updateChangelog` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 11`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 17`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 0):` fs, child_process, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `excalidraw-app/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.287 IQR)
- **Top Global Matches:** file_cluster_0: 10.287, file_cluster_8: 10.296, file_cluster_13: 10.695
- **Magnitude:** 53.88 | **LOC:** 253 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.0032%), Tech Debt (94.3118%)
**Top Internal Functions/Classes:**
  * `getTheme` (Impact: 10.9)
  * `WebSocket` (Impact: 7.4)
  * `setTheme` (Impact: 5.5)
  * `media` (Impact: 2.5)
  * `setTheme` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 11`, `args: 17`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 17`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fonts.googleapis.com, excalidraw.com, fonts.css, index.tsx, apple-touch-icon.png, fonts.gstatic.com, favicon-32x32.png, favicon-16x16.png
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/components/SearchMenu.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.858 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.404 IQR)
- **Top Global Matches:** file_cluster_8: 10.858, file_cluster_2: 10.93, file_cluster_17: 10.945
- **Magnitude:** 51.52 | **LOC:** 877 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.7682%), Tech Debt (99.8103%)
**Top Internal Functions/Classes:**
  * `SearchMenu` (Impact: 123.6)
  * `eventHandler` (Impact: 40.6)
  * `useEffect` (Impact: 31.8)
  * `useEffect` (Impact: 30.0)
  * `cb` (Impact: 26.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 101`, `args: 66`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`, `duplicate_logic: 25`
* *Architecture:* `api: 2`, `import: 20`
* *Defense:* `safety: 18`, `immutability_locks: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` useStable, i18n, types, App, frame, editor-jotai, icons, clsx...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `excalidraw-app/collab/Collab.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.879 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.277 IQR)
- **Top Global Matches:** file_cluster_13: 12.879, file_cluster_4: 12.982, file_cluster_11: 13.124
- **Magnitude:** 50.91 | **LOC:** 1052 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (92.9646%), Tech Debt (26.0985%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 17.0)
  * `onVisibilityChange` (Impact: 9.7)
  * `componentDidMount` (Impact: 9.4)
  * `componentWillUnmount` (Impact: 6.7)
  * `onPointerMove` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 107`, `args: 56`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 285`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 25`, `concurrency: 50`, `import: 31`
* *Defense:* `safety: 5`, `doc: 2`, `immutability_locks: 26`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.146
  * `Choke Point (Betweenness):` 0.000161 | `Ripple Effect (Closeness):` 0.004463
  * `Imports (Out-Degree: 16):` ErrorDialog, types, CollabError, react, firebase, tabSync, types, lodash.throttle...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/element/src/store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.997 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.313 IQR)
- **Top Global Matches:** file_cluster_13: 11.997, file_cluster_8: 12.033, file_cluster_11: 12.192
- **Magnitude:** 50.71 | **LOC:** 1038 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.9833%), Tech Debt (99.9864%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 20.4)
  * `maybeClone` (Impact: 16.0)
  * `emitDurableIncrement` (Impact: 14.9)
  * `getChangedElements` (Impact: 11.1)
  * `maybeCloneSnapshot` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 91`, `args: 59`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `state_mutation: 205`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 20`
* *Architecture:* `api: 61`, `import: 10`
* *Defense:* `safety: 11`, `doc: 31`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.941
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002789
  * `Imports (Out-Degree: 4):` delta, duplicate, types, mutateElement, types, App, common, utility-types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/element/src/resizeElements.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.692 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.016 IQR)
- **Top Global Matches:** file_cluster_8: 9.692, file_cluster_13: 10.31, file_cluster_7: 10.426
- **Magnitude:** 49.52 | **LOC:** 1501 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.9387%), Tech Debt (98.2534%)
**Top Internal Functions/Classes:**
  * `transformElements` (Impact: 56.2)
    * *Intent:* // Returns true when transform (resizing/rotation) happened
  * `rotateMultipleElements` (Impact: 51.7)
  * `getResizeAnchor` (Impact: 40.0)
  * `getResizeOffsetXY` (Impact: 37.3)
  * `rotateSingleElement` (Impact: 29.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 101`, `args: 62`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`, `duplicate_logic: 28`
* *Architecture:* `api: 11`, `import: 18`
* *Defense:* `safety: 3`, `immutability_locks: 114`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.852
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 11):` linearElementEditor, types, Scene, groups, mutateElement, types, binding, common...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/excalidraw/data/blob.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.348 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.843 IQR)
- **Top Global Matches:** file_cluster_4: 11.348, file_cluster_13: 11.48, file_cluster_8: 11.682
- **Magnitude:** 49.42 | **LOC:** 508 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (57.3316%), Tech Debt (45.7851%)
**Top Internal Functions/Classes:**
  * `loadSceneOrLibraryFromBlob` (Impact: 47.0)
  * `parseFileContents` (Impact: 42.1)
  * `getMimeType` (Impact: 40.8)
  * `normalizeFile` (Impact: 33.2)
  * `ImageURLToFile` (Impact: 17.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 183`, `args: 44`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 17`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 42`, `concurrency: 94`, `import: 17`
* *Defense:* `safety: 31`, `doc: 9`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.488
  * `Choke Point (Betweenness):` 0.000717 | `Ripple Effect (Closeness):` 0.067344
  * `Imports (Out-Degree: 7):` appState, types, json, nanoid, restore, export, image-blob-reduce, scene...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `packages/excalidraw/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 49.34 | **LOC:** 2467 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `packages/excalidraw/wysiwyg/textWysiwyg.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.139 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.358 IQR)
- **Top Global Matches:** file_cluster_8: 11.139, file_cluster_13: 11.322, file_cluster_0: 11.465
- **Magnitude:** 48.9 | **LOC:** 1023 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (34.0022%), Tech Debt (8.8385%)
**Top Internal Functions/Classes:**
  * `textPropertiesUpdated` (Impact: 341.2)
  * `getTransform` (Impact: 15.1)
  * `getLineDirection` (Impact: 5.7)
  * `getViewportCoords` (Impact: 5.5)
    * *Intent:* /** * textWysiwyg only deals with `originalText` *
  * `getCaretBoundaryOffsets` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 103`, `args: 67`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 86`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 21`
* *Defense:* `safety: 24`, `doc: 3`, `immutability_locks: 106`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.85
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001395
  * `Imports (Out-Degree: 3):` actionCanvas, types, App, clipboard, element, types, common, actions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `excalidraw-app/index.html` (HTML) | Magnitude: 53.88 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 207, globals: 26, branch: 25, listeners: 23
- `packages/utils/src/export.ts` (TYPESCRIPT) | Magnitude: 5.83 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 157, branch: 49, structural_boundaries: 45, concurrency: 18
- `excalidraw-app/data/localStorage.ts` (TYPESCRIPT) | Magnitude: 7.9 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, branch: 23, structural_boundaries: 23, safety: 17
- `scripts/buildWasm.js` (JAVASCRIPT) | Magnitude: 23.26 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, immutability_locks: 20, io: 12, branch: 10
- `packages/common/src/url.ts` (TYPESCRIPT) | Magnitude: 2.85 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 14, branch: 7, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/excalidraw/components/ButtonIcon.tsx` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 11, branch: 5, ui_framework: 4
- `packages/excalidraw/tests/helpers/api.ts` (TYPESCRIPT) | Magnitude: 19.53 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 452, branch: 204, structural_boundaries: 147, safety: 65
- `packages/excalidraw/actions/actionToggleObjectsSnapMode.tsx` (TYPESCRIPT) | Magnitude: 0.79 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, args: 5, func_start: 5
- `packages/excalidraw/components/MobileMenu.tsx` (TYPESCRIPT) | Magnitude: 3.6 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 37, branch: 18, ui_framework: 17
- `packages/excalidraw/components/EyeDropper.tsx` (TYPESCRIPT) | Magnitude: 5.17 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 160, structural_boundaries: 41, immutability_locks: 20, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/math/src/vector.ts` (TYPESCRIPT) | Magnitude: 6.61 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 43, indent_spaces: 36, structural_boundaries: 30, api: 20
- `packages/math/src/rectangle.ts` (TYPESCRIPT) | Magnitude: 2.21 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 18, generics: 12, args: 10
- `packages/math/src/types.ts` (TYPESCRIPT) | Magnitude: 3.21 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 39, indent_spaces: 23, api: 16, doc: 15
- `packages/math/src/triangle.ts` (TYPESCRIPT) | Magnitude: 1.51 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, immutability_locks: 6, branch: 5
- `excalidraw-app/data/Locker.ts` (TYPESCRIPT) | Magnitude: 2.39 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 11, indent_spaces: 11, structural_boundaries: 7, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/element/src/visualdebug.ts` (TYPESCRIPT) | Magnitude: 14.08 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 195, branch: 86, structural_boundaries: 44, func_start: 38
- `packages/excalidraw/components/ToolPopover.tsx` (TYPESCRIPT) | Magnitude: 1.49 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 49, args: 15, branch: 12
- `packages/excalidraw/actions/actionElementLock.ts` (TYPESCRIPT) | Magnitude: 17.14 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 44, branch: 31, immutability_locks: 26
- `packages/element/src/positionElementsOnGrid.ts` (TYPESCRIPT) | Magnitude: 4.11 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 19, immutability_locks: 15, state_mutation: 14
- `packages/excalidraw/components/App.tsx` (TYPESCRIPT) | Magnitude: 465.51 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6234, state_mutation: 3479, branch: 1140, structural_boundaries: 717

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/excalidraw/components/Sidebar/SidebarHeader.tsx` (TYPESCRIPT) | Magnitude: 0.33 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, ui_framework: 14, structural_boundaries: 12, import: 8
- `packages/excalidraw/hooks/useEmitter.ts` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, args: 6, ui_framework: 6
- `packages/excalidraw/components/LaserPointerButton.tsx` (TYPESCRIPT) | Magnitude: 0.59 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 10, ui_framework: 9, branch: 4
- `packages/excalidraw/components/Toast.tsx` (TYPESCRIPT) | Magnitude: 4.31 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 20, ui_framework: 12, branch: 9
- `excalidraw-app/share/ShareDialog.tsx` (TYPESCRIPT) | Magnitude: 10.7 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 222, structural_boundaries: 58, ui_framework: 44, args: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/excalidraw/components/TTDDialog/hooks/useMermaidRenderer.ts` (TYPESCRIPT) | Magnitude: 17.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 152, state_mutation: 53, structural_boundaries: 41, immutability_locks: 33
- `packages/common/src/appEventBus.ts` (TYPESCRIPT) | Magnitude: 14.65 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 62, structural_boundaries: 41, generics: 28
- `packages/common/src/appEventBus.test.ts` (TYPESCRIPT) | Magnitude: 4.99 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 49, concurrency: 30, structural_boundaries: 16, args: 16
- `packages/excalidraw/subset/subset-main.ts` (TYPESCRIPT) | Magnitude: 8.12 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, concurrency: 35, structural_boundaries: 32, immutability_locks: 11
- `examples/with-script-in-browser/utils.ts` (TYPESCRIPT) | Magnitude: 6.88 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 55, args: 29, generics: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scripts/locales-coverage-description.js` (JAVASCRIPT) | Magnitude: 18.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: debug_prints: 5, indent_spaces: 5, branch: 3, state_mutation: 3
- `packages/element/src/elementLink.ts` (TYPESCRIPT) | Magnitude: 5.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 34, branch: 16, immutability_locks: 11
- `packages/excalidraw/components/LibraryUnit.tsx` (TYPESCRIPT) | Magnitude: 4.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 25, branch: 15, args: 13
- `packages/excalidraw/components/TTDDialog/types.ts` (TYPESCRIPT) | Magnitude: 5.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 52, api: 19, branch: 15
- `packages/common/global.d.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, decorators: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/excalidraw/subset/harfbuzz/harfbuzz-bindings.ts` (TYPESCRIPT) | Magnitude: 3.59 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 65, dead_code: 12, immutability_locks: 11, branch: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/excalidraw/components/App.tsx` -> Churn: **100.0%** | Cog Load: 75.388% | Debt: 19.4368%
- `packages/excalidraw/renderer/interactiveScene.ts` -> Churn: **61.24%** | Cog Load: 11.8802% | Debt: 99.628%
- `packages/element/src/linearElementEditor.ts` -> Churn: **59.44%** | Cog Load: 10.8595% | Debt: 90.1421%
- `packages/excalidraw/actions/actionFinalize.tsx` -> Churn: **58.02%** | Cog Load: 22.4191% | Debt: 63.341%
- `packages/element/src/binding.ts` -> Churn: **56.15%** | Cog Load: 15.1474% | Debt: 95.4342%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/element/src/binding.ts` -> **Márk Tolmács** (88.9% isolated ownership) | Magnitude: 135.34
- `scripts/release.js` -> **Marcel Mraz** (100.0% isolated ownership) | Magnitude: 124.0
- `packages/element/src/frame.ts` -> **David Luzar** (100.0% isolated ownership) | Magnitude: 67.42
- `packages/element/src/delta.ts` -> **Marcel Mraz** (100.0% isolated ownership) | Magnitude: 66.98
- `excalidraw-app/index.html` -> **David Luzar** (100.0% isolated ownership) | Magnitude: 53.88

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

- `packages/common/src/utility-types.ts` -> **Severity: 4301.78** (Blast Radius: 43.019 * Doc Risk: 99.9972%)
- `packages/excalidraw/components/icons.tsx` -> **Severity: 2724.7** (Blast Radius: 27.247 * Doc Risk: 100.0%)
- `packages/excalidraw/data/blob.ts` -> **Severity: 1748.8** (Blast Radius: 17.488 * Doc Risk: 100.0%)
- `packages/excalidraw/data/json.ts` -> **Severity: 1675.2** (Blast Radius: 16.752 * Doc Risk: 100.0%)
- `packages/excalidraw/appState.ts` -> **Severity: 1329.3** (Blast Radius: 13.293 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
