# ARCHITECTURAL_BRIEF: css_doom_typescript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/css_doom_typescript` |
| **Timestamp** | `2026-08-07T03:29:28.840776+00:00` |
| **Scan Duration** | `0.3s` |
| **Git Branch** | `master` |
| **Git Commit** | `217ef28c51e73c39d3d93fef3e7f6982f7634976` |
| **Git Remote** | `https://github.com/yurkagon/Doom-Nukem-CSS.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 106 malicious artifacts.

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
| Total Artifacts | 273 |
| Analyzed Artifacts (Scanned) | 138 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 135 |
| Total LOC | 3633 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6119 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9095 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 26 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 105 | 1469 | 76.1% |
| CSS | 28 | 2059 | 20.3% |
| MARKDOWN | 1 | 0 | 0.7% |
| PLAINTEXT | 1 | 0 | 0.7% |
| HTML | 1 | 20 | 0.7% |
| JSON | 1 | 18 | 0.7% |
| JAVASCRIPT | 1 | 67 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.511`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 69 | 50.0% |
| file_cluster_8 | 57 | 41.3% |
| file_cluster_4 | 7 | 5.1% |
| file_cluster_2 | 3 | 2.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 135*

**Composition by Extension & Reason:**
- `.ts`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 23x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 20x Excluded (Explicitly Denied Extension: '.png')
- `.wav`: 10x Excluded (Explicitly Denied Extension: '.wav')
- `.scss`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mp3`: 3x Excluded (Explicitly Denied Extension: '.mp3')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.template`: 1x Excluded (Unsupported Extension: '.template')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 12.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 95.5 | 11.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 3.0 | 1.4 | 1.4 | 0.2 |
| API Exposure | 0.0 | 13.4 | 4.7 | 5.8 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 40.8 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 59.2 | 60.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.8 | 30.1 | 21.4 | 3.2 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `webpack.config.js` (Hits: 6)
- `public/index.html` (Hits: 1)
- `src/ui/screens/Menu/Menu.tsx` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **State.ts** (`src/State/State.ts`) — 11 inbound connections
2. **Text.tsx** (`src/ui/components/Text/Text.tsx`) — 9 inbound connections
3. **Screen.tsx** (`src/ui/components/Screen/Screen.tsx`) — 7 inbound connections
4. **Guard.ts** (`src/enemies/Guard/Guard.ts`) — 4 inbound connections
5. **ShotgunItem.ts** (`src/items/ShotgunItem/ShotgunItem.ts`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **level.ts** (`src/levels/level_1/level.ts`) — 12 outbound dependencies
2. **preloadData.ts** (`src/ui/preloadData.ts`) — 12 outbound dependencies
3. **Menu.tsx** (`src/ui/screens/Menu/Menu.tsx`) — 11 outbound dependencies
4. **level.ts** (`src/levels/level_2/level.ts`) — 10 outbound dependencies
5. **Weapon.tsx** (`src/ui/screens/Game/Weapon/Weapon.tsx`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getCharClassName` (@ `src/ui/components/Text/getCharClassName.ts`) -> Impact: **39.9** | LOC: 37
- `render` (@ `src/ui/UserInterface.tsx`) -> Impact: **16.6** | LOC: 20
- `render` (@ `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx`) -> Impact: **9.4** | LOC: 18
- `setLevel` (@ `src/levels/level_1/level.ts`) -> Impact: **9.2** | LOC: 46
- `setLevel` (@ `src/levels/level_2/level.ts`) -> Impact: **9.2** | LOC: 46
- `handleUrl` (@ `src/utils/ResourceLoader/models/AudioLoader.ts`) -> Impact: **8.6** | LOC: 34
- `render` (@ `src/ui/screens/Game/Weapon/Weapon.tsx`) -> Impact: **8.4** | LOC: 27
- `load` (@ `src/utils/ResourceLoader/models/UrlLoader.ts`) -> Impact: **7.4** | LOC: 9
- `handler` (@ `src/utils/ResourceLoader/models/OperationHandler.ts`) -> Impact: **6.8** | LOC: 17
- `isAngleBetween` (@ `src/helpers/angle.ts`) -> Impact: **6.5** | LOC: 10

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 4 | 35.22 | 4.69% | 0.0% |
| `public` | 1 | 18.4 | 8.34% | 0.0% |
| `src/utils/ResourceLoader/models` | 4 | 14.23 | 88.12% | 0.0% |
| `src/State` | 4 | 9.46 | 33.69% | 0.0% |
| `src/ui/screens/Game/HUD/HealthBar/Face` | 4 | 9.46 | 27.5% | 0.0% |
| `src/ui/components/Text` | 6 | 8.3 | 7.63% | 0.0% |
| `src/utils/ResourceLoader` | 3 | 8.12 | 36.67% | 0.0% |
| `src/types` | 4 | 8.1 | 6.28% | 0.0% |
| `src/utils/ImageProcessor` | 2 | 7.97 | 52.5% | 0.0% |
| `src/levels/level_1` | 4 | 6.93 | 7.61% | 24.78% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/helpers/index.ts` -> **100.0%** Exposure
- `src/enemies/Guard/style.scss` -> **99.9996%** Exposure
- `src/enemies/Zombie/style.scss` -> **99.9996%** Exposure
- `src/ui/screens/Menu/Menu.tsx` -> **99.9967%** Exposure
- `src/helpers/angle.ts` -> **99.9729%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` -> **100.0%** Exposure
- `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` -> **100.0%** Exposure
- `src/ui/screens/Game/Weapon/BouncingWrapper.tsx` -> **100.0%** Exposure
- `src/ui/screens/Menu/Menu.tsx` -> **100.0%** Exposure
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/helpers/index.ts` -> **4** Orphaned Functions | **0** Duplicates
- `src/ui/screens/Menu/Menu.tsx` -> **0** Orphaned Functions | **4** Duplicates
- `src/helpers/angle.ts` -> **3** Orphaned Functions | **0** Duplicates
- `src/enemies/Guard/style.scss` -> **0** Orphaned Functions | **3** Duplicates
- `src/enemies/Zombie/style.scss` -> **0** Orphaned Functions | **3** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`webpack.config.js`** -> AI Confidence: **99.34%**
2. **`src/levels/level_1/level.ts`** -> AI Confidence: **99.18%**
3. **`src/levels/level_2/level.ts`** -> AI Confidence: **99.18%**
4. **`src/ui/screens/Game/Weapon/Weapon.tsx`** -> AI Confidence: **99.15%**
5. **`src/ui/preloadData.ts`** -> AI Confidence: **99.09%**
6. **`src/ui/screens/LevelSelect/LevelSelect.tsx`** -> AI Confidence: **99.08%**
7. **`src/ui/screens/Menu/Menu.tsx`** -> AI Confidence: **99.08%**
8. **`src/items/MedkitItem/MedkitItem.ts`** -> AI Confidence: **99.07%**
9. **`src/enemies/Guard/index.ts`** -> AI Confidence: **99.06%**
10. **`src/enemies/Zombie/index.ts`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `169` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` (TYPESCRIPT) -> Cumulative Risk: **602.16**
- **Archetype:** `file_cluster_13` (Distance: 12.744 IQR)
- **Magnitude:** 6.21 | **LOC:** 55 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getFaceState` (Impact: 5.8), `startIteration` (Impact: 5.7), `render` (Impact: 2.0)

### 2. `src/utils/ResourceLoader/models/UrlLoader.ts` (TYPESCRIPT) -> Cumulative Risk: **574.19**
- **Archetype:** `file_cluster_4` (Distance: 12.245 IQR)
- **Magnitude:** 3.29 | **LOC:** 23 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `load` (Impact: 7.4), `getExactPath` (Impact: 2.1)

### 3. `src/State/Loader.ts` (TYPESCRIPT) -> Cumulative Risk: **572.33**
- **Archetype:** `file_cluster_4` (Distance: 11.946 IQR)
- **Magnitude:** 4.24 | **LOC:** 37 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (99.1906%)
- **Heaviest Functions:** `loadResources` (Impact: 5.8), `addLoadedItem` (Impact: 2.1), `setLoadingStatus` (Impact: 2.1)

### 4. `src/utils/ResourceLoader/models/AudioLoader.ts` (TYPESCRIPT) -> Cumulative Risk: **550.19**
- **Archetype:** `file_cluster_4` (Distance: 12.31 IQR)
- **Magnitude:** 4.29 | **LOC:** 41 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `handleUrl` (Impact: 8.6), `onEnd` (Impact: 5.8), `clearTimeout` (Impact: 1.9)

### 5. `src/ui/screens/Menu/Menu.tsx` (TYPESCRIPT) -> Cumulative Risk: **536.51**
- **Archetype:** `file_cluster_13` (Distance: 10.995 IQR)
- **Magnitude:** 4.88 | **LOC:** 97 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9967%), Safety Score (78.3421%)
- **Heaviest Functions:** `render` (Impact: 6.2), `startMenu` (Impact: 3.9), `onMenuInit` (Impact: 2.4)

### 6. `src/utils/ResourceLoader/ResourceLoader.ts` (TYPESCRIPT) -> Cumulative Risk: **513.44**
- **Archetype:** `file_cluster_4` (Distance: 11.142 IQR)
- **Magnitude:** 4.94 | **LOC:** 48 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `handler` (Impact: 4.3), `onUpdate` (Impact: 4.0), `load` (Impact: 1.3)

### 7. `src/items/MedkitItem/MedkitItem.ts` (TYPESCRIPT) -> Cumulative Risk: **494.39**
- **Archetype:** `file_cluster_13` (Distance: 10.255 IQR)
- **Magnitude:** 2.81 | **LOC:** 44 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (99.4298%), State Flux (89.2461%)
- **Heaviest Functions:** `onPick` (Impact: 4.2), `constructor` (Impact: 2.2), `chance` (Impact: 1.7)

### 8. `src/utils/ResourceLoader/models/OperationHandler.ts` (TYPESCRIPT) -> Cumulative Risk: **482.4**
- **Archetype:** `file_cluster_4` (Distance: 11.727 IQR)
- **Magnitude:** 4.83 | **LOC:** 34 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `handler` (Impact: 6.8), `handleOperation` (Impact: 2.0)

### 9. `src/utils/ResourceLoader/models/ImageLoader.ts` (TYPESCRIPT) -> Cumulative Risk: **459.38**
- **Archetype:** `file_cluster_4` (Distance: 11.564 IQR)
- **Magnitude:** 1.82 | **LOC:** 26 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.6821%), Concurrency (82.5715%), Documentation (73.1059%)
- **Heaviest Functions:** `handleUrl` (Impact: 6.1), `onEnd` (Impact: 3.7)

### 10. `src/utils/ImageProcessor/ImageProcessor.ts` (TYPESCRIPT) -> Cumulative Risk: **409.82**
- **Archetype:** `file_cluster_4` (Distance: 9.347 IQR)
- **Magnitude:** 6.82 | **LOC:** 61 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Safety Score (58.992%)
- **Heaviest Functions:** `createImageElement` (Impact: 3.5), `createImageCanvasContext` (Impact: 3.1), `getImageData` (Impact: 2.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `public/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.871 IQR)
- **Top Global Matches:** file_cluster_8: 6.871, file_cluster_0: 7.244, file_cluster_7: 7.619
- **Magnitude:** 18.4 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.3442%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` icon.png, main.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `webpack.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.85 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.15 IQR)
- **Top Global Matches:** file_cluster_8: 6.85, file_cluster_13: 7.709, file_cluster_7: 7.835
- **Magnitude:** 17.34 | **LOC:** 70 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6205%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* `io: 6`, `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` copy-webpack-plugin, path, uglifyjs-webpack-plugin, clean-webpack-plugin, tsconfig-paths-webpack-plugin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.36 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.1371%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/ImageProcessor/ImageProcessor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.347 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.904 IQR)
- **Top Global Matches:** file_cluster_4: 9.347, file_cluster_8: 9.901, file_cluster_13: 9.969
- **Magnitude:** 6.82 | **LOC:** 61 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createImageElement` (Impact: 3.5)
  * `createImageCanvasContext` (Impact: 3.1)
  * `getImageData` (Impact: 2.8)
  * `applyBrightness` (Impact: 2.5)
  * `getUrlFromImageData` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 14`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 3`, `concurrency: 46`, `import: 2`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 0):` image-filter-core, image-brightness
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.744 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.364 IQR)
- **Top Global Matches:** file_cluster_13: 12.744, file_cluster_4: 12.818, file_cluster_2: 12.984
- **Magnitude:** 6.21 | **LOC:** 55 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFaceState` (Impact: 5.8)
  * `startIteration` (Impact: 5.7)
  * `render` (Impact: 2.0)
  * `componentDidMount` (Impact: 1.9)
  * `componentWillUnmount` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `api: 8`, `concurrency: 6`, `import: 2`
* *Defense:* `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.771
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023358
  * `Imports (Out-Degree: 0):` types, react, style.scss
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/ResourceLoader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.142 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.041 IQR)
- **Top Global Matches:** file_cluster_4: 11.142, file_cluster_13: 11.515, file_cluster_8: 11.823
- **Magnitude:** 4.94 | **LOC:** 48 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 4.3)
  * `onUpdate` (Impact: 4.0)
  * `load` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 2`, `concurrency: 25`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.653
  * `Choke Point (Betweenness):` 0.010036 | `Ripple Effect (Closeness):` 0.074511
  * `Imports (Out-Degree: 4):` ImageLoader, types, sleep, AudioLoader, OperationHandler
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/ui/screens/Menu/Menu.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.995 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.997 IQR)
- **Top Global Matches:** file_cluster_13: 10.995, file_cluster_2: 11.366, file_cluster_8: 11.509
- **Magnitude:** 4.88 | **LOC:** 97 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.4305%), Tech Debt (99.9967%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 6.2)
  * `startMenu` (Impact: 3.9)
  * `onMenuInit` (Impact: 2.4)
  * `onClick` (Impact: 2.0)
  * `onClick` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 22`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 4`, `concurrency: 2`, `import: 10`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.372
  * `Choke Point (Betweenness):` 0.001369 | `Ripple Effect (Closeness):` 0.014599
  * `Imports (Out-Degree: 8):` State, sleep, react, Text, menu_music, Screen, start_menu, style.scss...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/OperationHandler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.727 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.443 IQR)
- **Top Global Matches:** file_cluster_4: 11.727, file_cluster_13: 12.483, file_cluster_8: 12.528
- **Magnitude:** 4.83 | **LOC:** 34 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 6.8)
  * `handleOperation` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 10`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `concurrency: 34`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.061793
  * `Imports (Out-Degree: 1):` sleep, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/AudioLoader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.31 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.578 IQR)
- **Top Global Matches:** file_cluster_4: 12.31, file_cluster_13: 12.834, file_cluster_8: 12.961
- **Magnitude:** 4.29 | **LOC:** 41 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleUrl` (Impact: 8.6)
  * `onEnd` (Impact: 5.8)
  * `clearTimeout` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 4`, `concurrency: 13`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.604
  * `Choke Point (Betweenness):` 0.001073 | `Ripple Effect (Closeness):` 0.062121
  * `Imports (Out-Degree: 1):` UrlLoader
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/State/Loader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.946 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_4: 11.946, file_cluster_0: 12.329, file_cluster_13: 12.398
- **Magnitude:** 4.24 | **LOC:** 37 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadResources` (Impact: 5.8)
  * `addLoadedItem` (Impact: 2.1)
  * `setLoadingStatus` (Impact: 2.1)
  * `onUpdate` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 8`, `concurrency: 12`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.708
  * `Choke Point (Betweenness):` 0.011325 | `Ripple Effect (Closeness):` 0.085999
  * `Imports (Out-Degree: 1):` mobx, types, ResourceLoader
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui/components/Text/getCharClassName.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.188 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.736 IQR)
- **Top Global Matches:** file_cluster_8: 6.188, file_cluster_7: 7.382, file_cluster_1: 7.614
- **Magnitude:** 4.16 | **LOC:** 40 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.7664%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCharClassName` (Impact: 39.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 17`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05194
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/UrlLoader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.245 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 4.898 IQR)
- **Top Global Matches:** file_cluster_4: 12.245, file_cluster_17: 12.885, file_cluster_8: 13.158
- **Magnitude:** 3.29 | **LOC:** 23 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 7.4)
  * `getExactPath` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 8`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `api: 5`, `concurrency: 12`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055982
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/types/image-filter-core.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.537 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.297 IQR)
- **Top Global Matches:** file_cluster_8: 6.537, file_cluster_7: 7.716, file_cluster_1: 7.949
- **Magnitude:** 3.24 | **LOC:** 8 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/items/MedkitItem/MedkitItem.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.255 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.763 IQR)
- **Top Global Matches:** file_cluster_13: 10.255, file_cluster_4: 10.284, file_cluster_8: 10.5
- **Magnitude:** 2.81 | **LOC:** 44 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.4298%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onPick` (Impact: 4.2)
  * `constructor` (Impact: 2.2)
  * `chance` (Impact: 1.7)
  * `super` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 2`, `concurrency: 12`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.106
  * `Choke Point (Betweenness):` 0.000322 | `Ripple Effect (Closeness):` 0.021898
  * `Imports (Out-Degree: 2):` helpers, sleep, Sound, Player, style.scss, Item, medkitVoice
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/levels/level_1/level.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.066 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.85 IQR)
- **Top Global Matches:** file_cluster_13: 9.066, file_cluster_8: 9.306, file_cluster_7: 10.009
- **Magnitude:** 2.49 | **LOC:** 92 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1275%), Tech Debt (99.1392%)
**Top Internal Functions/Classes:**
  * `setLevel` (Impact: 9.2)
  * `setLevel` (Impact: 1.7)
  * `start` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` MedkitItem, Zombie, preloadData, map, helpers, floor.jpg, Level, doom_e1m1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/levels/level_2/level.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.14 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.86 IQR)
- **Top Global Matches:** file_cluster_13: 9.14, file_cluster_8: 9.344, file_cluster_7: 10.039
- **Magnitude:** 2.48 | **LOC:** 87 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1629%), Tech Debt (99.4472%)
**Top Internal Functions/Classes:**
  * `setLevel` (Impact: 9.2)
  * `setLevel` (Impact: 1.7)
  * `start` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` MedkitItem, Zombie, preloadData, map, helpers, Level, ShotgunItem, skybox.jpg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/helpers/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.701 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 7.368 IQR)
- **Top Global Matches:** file_cluster_8: 10.701, file_cluster_15: 11.423, file_cluster_7: 11.452
- **Magnitude:** 2.33 | **LOC:** 21 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0117%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `generateCoordinateNoiseValue` (Impact: 6.2)
  * `chance` (Impact: 4.2)
  * `to` (Impact: 4.2)
  * `generateTranslate3d` (Impact: 2.5)
  * `Distance` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 5`, `func_start: 5`
* *Risk/State:* `orphaned_logic: 4`
* *Architecture:* `api: 4`
* *Defense:* `safety: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/helpers/angle.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.892 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.296 IQR)
- **Top Global Matches:** file_cluster_8: 8.892, file_cluster_7: 9.674, file_cluster_1: 9.927
- **Magnitude:** 2.22 | **LOC:** 40 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.3208%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `isAngleBetween` (Impact: 6.5)
  * `normalize` (Impact: 2.5)
  * `normalize180` (Impact: 2.5)
  * `getAngleBetween` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 7`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/State/State.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.72%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.46 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_13: 10.46, file_cluster_0: 10.621, file_cluster_8: 11.101
- **Magnitude:** 2.13 | **LOC:** 35 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7489%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lockCursor` (Impact: 3.8)
  * `setScreen` (Impact: 2.1)
  * `isPointerLocked` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.361
  * `Choke Point (Betweenness):` 0.012881 | `Ripple Effect (Closeness):` 0.120833
  * `Imports (Out-Degree: 1):` types, jquery, Loader, mobx, Settings
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/types/file-loader.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.523 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.648 IQR)
- **Top Global Matches:** file_cluster_8: 5.523, file_cluster_7: 6.851, file_cluster_1: 7.148
- **Magnitude:** 2.04 | **LOC:** 30 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1322%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`
* *Risk/State:* None
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/UserInterface.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.117 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.832 IQR)
- **Top Global Matches:** file_cluster_13: 8.117, file_cluster_2: 8.338, file_cluster_16: 8.377
- **Magnitude:** 2.01 | **LOC:** 33 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.8869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.848
  * `Choke Point (Betweenness):` 0.000429 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 1):` mobx-react, State, screens, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/models/House/style.scss` (CSS | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.02 IQR)
- **Top Global Matches:** file_cluster_8: 10.02, file_cluster_7: 10.82, file_cluster_9: 10.95
- **Magnitude:** 2.0 | **LOC:** 1288 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 12`, `class_start: 375`
* *Risk/State:* `dead_code: 32`
* *Architecture:* None
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/ResourceLoader/models/ImageLoader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.564 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.075 IQR)
- **Top Global Matches:** file_cluster_4: 11.564, file_cluster_13: 11.565, file_cluster_8: 11.772
- **Magnitude:** 1.82 | **LOC:** 26 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.5%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleUrl` (Impact: 6.1)
  * `onEnd` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.604
  * `Choke Point (Betweenness):` 0.001073 | `Ripple Effect (Closeness):` 0.062121
  * `Imports (Out-Degree: 1):` UrlLoader
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/State/types.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.124 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.42 IQR)
- **Top Global Matches:** file_cluster_8: 6.124, file_cluster_13: 7.118, file_cluster_7: 7.38
- **Magnitude:** 1.73 | **LOC:** 18 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.019%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ResourceLoader
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.315 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.42 IQR)
- **Top Global Matches:** file_cluster_8: 7.315, file_cluster_13: 7.695, file_cluster_4: 8.237
- **Magnitude:** 1.72 | **LOC:** 19 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 1`
* *Risk/State:* None
* *Architecture:* `concurrency: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.scss, State, Level, ui
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/enemies/Guard/Guard.ts` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 5, api: 3, import: 3
- `src/items/MedkitItem/MedkitItem.ts` (TYPESCRIPT) | Magnitude: 2.81 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, concurrency: 12, import: 6
- `src/ui/preloadData.ts` (TYPESCRIPT) | Magnitude: 1.65 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, import: 12, indent_spaces: 11, branch: 1
- `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` (TYPESCRIPT) | Magnitude: 6.21 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 30, structural_boundaries: 10, api: 8
- `src/enemies/Zombie/Zombie.ts` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 4, api: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/ui/screens/FakeQuit/FakeQuit.tsx` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, ui_framework: 8, structural_boundaries: 7, generics: 5
- `src/ui/components/Header/style.scss` (CSS) | Magnitude: 0.63 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3, ui_framework: 2, class_start: 1
- `src/ui/screens/About/About.tsx` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ui_framework: 19, indent_spaces: 13, generics: 10, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/utils/ResourceLoader/models/ImageLoader.ts` (TYPESCRIPT) | Magnitude: 1.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 8, args: 4, branch: 3
- `src/utils/ResourceLoader/ResourceLoader.ts` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.373 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, concurrency: 25, structural_boundaries: 13, state_mutation: 12
- `src/State/Loader.ts` (TYPESCRIPT) | Magnitude: 4.24 | Delta: **0.383 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, concurrency: 12, state_mutation: 10, structural_boundaries: 8
- `src/utils/ResourceLoader/models/AudioLoader.ts` (TYPESCRIPT) | Magnitude: 4.29 | Delta: **0.524 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, concurrency: 13, structural_boundaries: 10, state_mutation: 9
- `src/utils/ImageProcessor/ImageProcessor.ts` (TYPESCRIPT) | Magnitude: 6.82 | Delta: **0.554 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 46, indent_spaces: 41, structural_boundaries: 14, immutability_locks: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/ui/screens/Game/Weapon/weapon_styles/_index.scss` (CSS) | Magnitude: 0.55 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 2
- `src/utils/sleep.ts` (TYPESCRIPT) | Magnitude: 0.68 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, args: 4, func_start: 3
- `src/ui/components/BackButton/types.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, branch: 1, class_start: 1, api: 1
- `src/ui/screens/Game/HUD/HealthBar/style.scss` (CSS) | Magnitude: 0.76 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, ui_framework: 4, class_start: 2
- `src/ui/screens/About/style.scss` (CSS) | Magnitude: 0.76 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, ui_framework: 3, class_start: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/State/State.ts` -> **Severity: 1.004** (Bridge: 0.0129 * Flux: 77.9303%)
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 1.004** (Bridge: 0.01 * Flux: 100.0%)
- `src/State/Loader.ts` -> **Severity: 0.963** (Bridge: 0.0113 * Flux: 84.9997%)
- `src/ui/screens/Menu/Menu.tsx` -> **Severity: 0.137** (Bridge: 0.0014 * Flux: 100.0%)
- `src/utils/ResourceLoader/models/AudioLoader.ts` -> **Severity: 0.107** (Bridge: 0.0011 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/State/State.ts` -> **Severity: 6.842** (Embedded: 0.1208 * Error Risk: 56.6274%)
- `src/State/Loader.ts` -> **Severity: 6.323** (Embedded: 0.086 * Error Risk: 73.5221%)
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 5.497** (Embedded: 0.0745 * Error Risk: 73.7784%)
- `src/utils/ResourceLoader/models/AudioLoader.ts` -> **Severity: 3.789** (Embedded: 0.0621 * Error Risk: 60.9911%)
- `src/utils/ResourceLoader/models/UrlLoader.ts` -> **Severity: 3.584** (Embedded: 0.056 * Error Risk: 64.0219%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/State/State.ts` -> **Severity: 4225.624** (Blast Radius: 42.361 * Doc Risk: 99.7527%)
- `src/State/Loader.ts` -> **Severity: 3938.66** (Blast Radius: 39.708 * Doc Risk: 99.1906%)
- `src/utils/ResourceLoader/models/UrlLoader.ts` -> **Severity: 2584.498** (Blast Radius: 26.834 * Doc Risk: 96.3143%)
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 1456.293** (Blast Radius: 41.653 * Doc Risk: 34.9625%)
- `src/items/PistolItem/PistolItem.ts` -> **Severity: 1273.704** (Blast Radius: 16.411 * Doc Risk: 77.6128%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
