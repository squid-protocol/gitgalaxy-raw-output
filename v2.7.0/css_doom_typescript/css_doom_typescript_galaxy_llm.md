# ARCHITECTURAL_BRIEF: css_doom_typescript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/yurkagon/Doom-Nukem-CSS.git` |
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
| Modularity | 0.6147 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0137 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9231 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

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
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 136 | 98.6% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.4 | 5.1 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 76.9 | 8.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.7 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 80.0 | 14.2 | 5.6 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.8 | 0.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 58.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 33.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8 | 4 | 0 | `src/ui/screens/Menu/Menu.tsx` |
| cleanup | 4 | 3 | 0 | `src/utils/ResourceLoader/models/AudioLoader.ts` |
| guards | 37 | 16 | 1 | `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` |
| danger | 7 | 6 | 0 | `style/index.scss` |
| concurrency | 62 | 13 | 0 | `src/utils/ResourceLoader/models/OperationHandler.ts` |
| connectivity | 179 | 105 | 3 | `src/State/Loader.ts` |
| io | 35 | 20 | 1 | `src/models/House/style.scss` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 3 | 0 | `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `src/ui/components/Text/Text.tsx` |
| events | 1 | 1 | 0 | `src/utils/ResourceLoader/models/AudioLoader.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 1 | 1 | 0 | `public/index.html` |
| debt | 3 | 3 | 0 | `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` |
| mutation | 263 | 60 | 6 | `src/models/House/data.ts` |
| dead_code | 46 | 6 | 0 | `src/models/House/style.scss` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 17 | 4 | 0 | `src/helpers/index.ts` |
| ui | 132 | 35 | 4 | `src/ui/screens/About/About.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/models/House/style.scss` (Hits: 12)
- `webpack.config.js` (Hits: 3)
- `public/index.html` (Hits: 2)

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

- `getCharClassName` (@ `src/ui/components/Text/getCharClassName.ts`) -> Impact: **27.4** | LOC: 39
- `render` (@ `src/ui/UserInterface.tsx`) -> Impact: **10.0** | LOC: 20
- `load` (@ `src/utils/ResourceLoader/ResourceLoader.ts`) -> Impact: **8.6** | LOC: 31
- `handleUrl` (@ `src/utils/ResourceLoader/models/AudioLoader.ts`) -> Impact: **8.6** | LOC: 34
- `setLevel` (@ `src/levels/level_1/level.ts`) -> Impact: **7.4** | LOC: 48
- `setLevel` (@ `src/levels/level_2/level.ts`) -> Impact: **7.4** | LOC: 48
- `load` (@ `src/utils/ResourceLoader/models/UrlLoader.ts`) -> Impact: **7.4** | LOC: 9
- `render` (@ `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx`) -> Impact: **6.9** | LOC: 18
- `handler` (@ `src/utils/ResourceLoader/ResourceLoader.ts`) -> Impact: **6.7** | LOC: 20
- `isAngleBetween` (@ `src/helpers/angle.ts`) -> Impact: **6.5** | LOC: 10

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/utils/ResourceLoader/models` | 4 | 112.98 | 54.51% | 0.0% |
| `src/levels/level_1` | 4 | 65.3 | 7.62% | 0.0% |
| `src/levels/level_2` | 4 | 65.22 | 7.88% | 0.0% |
| `src/State` | 4 | 53.37 | 8.34% | 0.0% |
| `src/utils/ImageProcessor` | 2 | 53.34 | 52.69% | 0.0% |
| `src/sounds/menu` | 4 | 52.32 | 5.12% | 0.0% |
| `src/ui/components/Text` | 6 | 51.33 | 6.19% | 0.0% |
| `src/ui/screens/Game/HUD/HealthBar/Face` | 4 | 44.27 | 17.07% | 0.0% |
| `src/utils/ResourceLoader` | 3 | 42.31 | 11.76% | 0.0% |
| `src/helpers` | 2 | 39.78 | 6.56% | 99.97% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/helpers/angle.ts` -> **99.9665%** Exposure
- `src/helpers/index.ts` -> **99.9665%** Exposure
- `src/models/House/index.ts` -> **88.0797%** Exposure
- `src/sounds/player/steps.ts` -> **50.0%** Exposure
- `src/ui/index.tsx` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` -> **100.0%** Exposure
- `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` -> **100.0%** Exposure
- `src/utils/ResourceLoader/models/AudioLoader.ts` -> **100.0%** Exposure
- `src/utils/ResourceLoader/models/ImageLoader.ts` -> **100.0%** Exposure
- `src/levels/level_2/level.ts` -> **95.8452%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/helpers/angle.ts` -> **5** Orphaned Functions | **0** Duplicates
- `src/helpers/index.ts` -> **5** Orphaned Functions | **0** Duplicates
- `src/models/House/index.ts` -> **2** Orphaned Functions | **0** Duplicates
- `src/sounds/player/steps.ts` -> **1** Orphaned Functions | **0** Duplicates
- `src/ui/index.tsx` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `173` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/utils/ResourceLoader/models/AudioLoader.ts` (TYPESCRIPT) -> Cumulative Risk: **616.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 45.38 | **LOC:** 41 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `handleUrl` (Impact: 8.6), `onEnd` (Impact: 5.2)

### 2. `src/utils/ResourceLoader/models/ImageLoader.ts` (TYPESCRIPT) -> Cumulative Risk: **591.9**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 32.3 | **LOC:** 26 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.5792%)
- **Heaviest Functions:** `handleUrl` (Impact: 6.1), `onEnd` (Impact: 3.8)

### 3. `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` (TYPESCRIPT) -> Cumulative Risk: **567.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 31.28 | **LOC:** 55 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `getFaceState` (Impact: 3.6), `startIteration` (Impact: 3.5), `render` (Impact: 1.2)

### 4. `src/utils/ImageProcessor/ImageProcessor.ts` (TYPESCRIPT) -> Cumulative Risk: **530.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 41.82 | **LOC:** 61 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `applyBrightness` (Impact: 2.5), `createImageElement` (Impact: 2.1), `createImageCanvasContext` (Impact: 1.9)

### 5. `src/utils/ResourceLoader/ResourceLoader.ts` (TYPESCRIPT) -> Cumulative Risk: **469.67**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 27.06 | **LOC:** 48 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (96.5555%), Safety Score (60.5532%)
- **Heaviest Functions:** `load` (Impact: 8.6), `handler` (Impact: 6.7)

### 6. `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` (TYPESCRIPT) -> Cumulative Risk: **452.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 21.32 | **LOC:** 31 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (76.8525%)
- **Heaviest Functions:** `render` (Impact: 6.9)

### 7. `src/State/Loader.ts` (TYPESCRIPT) -> Cumulative Risk: **425.76**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 25.34 | **LOC:** 37 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (63.9941%), Api Exposure (60.2192%)
- **Heaviest Functions:** `loadResources` (Impact: 5.8), `onUpdate` (Impact: 4.8), `addLoadedItem` (Impact: 1.6)

### 8. `src/ui/screens/Menu/Menu.tsx` (TYPESCRIPT) -> Cumulative Risk: **417.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 25.96 | **LOC:** 97 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (72.9357%), Safety Score (62.0058%)
- **Heaviest Functions:** `render` (Impact: 4.0), `startMenu` (Impact: 2.5), `onClick` (Impact: 1.4)

### 9. `src/levels/level_2/level.ts` (TYPESCRIPT) -> Cumulative Risk: **414.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 20.8 | **LOC:** 87 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (95.8452%), Safety Score (68.4919%)
- **Heaviest Functions:** `setLevel` (Impact: 7.4), `start` (Impact: 1.1)

### 10. `src/levels/level_1/level.ts` (TYPESCRIPT) -> Cumulative Risk: **410.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 20.88 | **LOC:** 92 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (94.3608%), Safety Score (67.734%)
- **Heaviest Functions:** `setLevel` (Impact: 7.4), `start` (Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/utils/ResourceLoader/models/AudioLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 45.38 | **LOC:** 41 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleUrl` (Impact: 8.6)
  * `onEnd` (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 3`, `concurrency: 3`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.417
  * `Choke Point (Betweenness):` 0.001073 | `Ripple Effect (Closeness):` 0.062121
  * `Imports (Out-Degree: 1):` UrlLoader
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/utils/ImageProcessor/ImageProcessor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 41.82 | **LOC:** 61 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applyBrightness` (Impact: 2.5)
  * `createImageElement` (Impact: 2.1)
  * `createImageCanvasContext` (Impact: 1.9)
  * `getImageData` (Impact: 1.8)
  * `getUrlFromImageData` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 14`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `concurrency: 11`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.876
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 0):` image-brightness, image-filter-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/ImageLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 32.3 | **LOC:** 26 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.3388%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleUrl` (Impact: 6.1)
  * `onEnd` (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 10`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.417
  * `Choke Point (Betweenness):` 0.001073 | `Ripple Effect (Closeness):` 0.062121
  * `Imports (Out-Degree: 1):` UrlLoader
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/ui/screens/Game/HUD/HealthBar/Face/Face.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 31.28 | **LOC:** 55 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.6501%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFaceState` (Impact: 3.6)
  * `startIteration` (Impact: 3.5)
  * `render` (Impact: 1.2)
  * `componentDidMount` (Impact: 1.1)
  * `componentWillUnmount` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 5`, `concurrency: 1`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023358
  * `Imports (Out-Degree: 0):` style.scss, types, react
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/ui/components/Text/getCharClassName.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 29.12 | **LOC:** 40 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2465%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCharClassName` (Impact: 27.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 17`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05194
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/ResourceLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 27.06 | **LOC:** 48 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.9206%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 8.6)
  * `handler` (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 3`, `concurrency: 5`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.683
  * `Choke Point (Betweenness):` 0.010036 | `Ripple Effect (Closeness):` 0.074511
  * `Imports (Out-Degree: 4):` AudioLoader, ImageLoader, OperationHandler, types, sleep
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/ui/screens/Menu/Menu.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 25.96 | **LOC:** 97 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.1235%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 4.0)
  * `startMenu` (Impact: 2.5)
  * `onClick` (Impact: 1.4)
  * `onClick` (Impact: 1.4)
  * `onClick` (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 22`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 2`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.402
  * `Choke Point (Betweenness):` 0.001369 | `Ripple Effect (Closeness):` 0.014599
  * `Imports (Out-Degree: 8):` style.scss, State, BackgroundMusic, react, menu_music, start_menu, ButtonGroup, types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/State/Loader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 25.34 | **LOC:** 37 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.1987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadResources` (Impact: 5.8)
  * `onUpdate` (Impact: 4.8)
  * `addLoadedItem` (Impact: 1.6)
  * `setLoadingStatus` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 38.527
  * `Choke Point (Betweenness):` 0.011325 | `Ripple Effect (Closeness):` 0.085999
  * `Imports (Out-Degree: 1):` ResourceLoader, types, mobx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/helpers/angle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.66 | **LOC:** 40 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8644%), Tech Debt (99.9665%)
**Top Internal Functions/Classes:**
  * `isAngleBetween` (Impact: 6.5)
  * `getAngleBetween` (Impact: 2.1)
  * `normalize` (Impact: 1.7)
  * `normalize180` (Impact: 1.7)
  * `toRad` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 5`
* *Architecture:* `api: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/screens/Game/HUD/HealthColorFilter/HealthColorFilter.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21.32 | **LOC:** 31 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.9778%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.269
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021898
  * `Imports (Out-Degree: 0):` style.scss, Player, mobx-react, react
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/levels/level_1/level.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 20.88 | **LOC:** 92 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1275%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setLevel` (Impact: 7.4)
  * `start` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` floor.jpg, map, preloadData, skybox.jpg, Level, Guard, Zombie, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/levels/level_2/level.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 20.8 | **LOC:** 87 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1629%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setLevel` (Impact: 7.4)
  * `start` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` map, preloadData, skybox.jpg, Level, Guard, Zombie, helpers, MedkitItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/ResourceLoader/models/UrlLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.06 | **LOC:** 23 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 7.4)
  * `handleUrl` (Impact: 3.7)
  * `getExactPath` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 4`, `concurrency: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055982
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `public/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 18.4 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` icon.png, main.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `webpack.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 18.34 | **LOC:** 70 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6205%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` clean-webpack-plugin, copy-webpack-plugin, path, tsconfig-paths-webpack-plugin, uglifyjs-webpack-plugin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.24 | **LOC:** 19 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.0173%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 1`
* *Risk/State:* None
* *Architecture:* `concurrency: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` index.scss, State, Level, ui
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/helpers/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.12 | **LOC:** 21 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2501%), Tech Debt (99.9665%)
**Top Internal Functions/Classes:**
  * `generateCoordinateNoiseValue` (Impact: 4.5)
  * `to` (Impact: 3.0)
  * `Distance` (Impact: 2.0)
  * `generateTranslate3d` (Impact: 1.8)
  * `chance` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`
* *Risk/State:* `unreferenced_by_name: 5`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/models/House/data.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.0 | **LOC:** 53 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 43`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.876
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007299
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/levels/level_1/map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.68 | **LOC:** 38 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MapHandler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/levels/level_2/map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.68 | **LOC:** 38 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MapHandler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/preloadData.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.52 | **LOC:** 33 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` background.jpg, State, menu_back, menu_click, menu_music, start_menu, font.png, about.jpg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/screens/About/About.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.44 | **LOC:** 33 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.402
  * `Choke Point (Betweenness):` 0.00093 | `Ripple Effect (Closeness):` 0.014599
  * `Imports (Out-Degree: 4):` style.scss, react, BackButton, Header, Screen, Text
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/ui/screens/FakeQuit/FakeQuit.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.36 | **LOC:** 25 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.402
  * `Choke Point (Betweenness):` 0.00085 | `Ripple Effect (Closeness):` 0.014599
  * `Imports (Out-Degree: 3):` style.scss, react, BackButton, Screen, Text
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/utils/ResourceLoader/models/OperationHandler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.24 | **LOC:** 34 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4579%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 2.7)
  * `handleOperation` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 12`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.061793
  * `Imports (Out-Degree: 1):` types, sleep
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/levels/level_1/preloadData.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.22 | **LOC:** 16 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` State, Front.png, Side.png, sidingTexture.jpg, doom_e1m1, medkitVoice
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

- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 0.577** (Bridge: 0.01 * Flux: 57.5%)
- `src/State/Loader.ts` -> **Severity: 0.298** (Bridge: 0.0113 * Flux: 26.3522%)
- `src/ui/components/BackButton/BackButton.tsx` -> **Severity: 0.204** (Bridge: 0.0037 * Flux: 55.0%)
- `src/utils/ResourceLoader/models/AudioLoader.ts` -> **Severity: 0.107** (Bridge: 0.0011 * Flux: 100.0%)
- `src/utils/ResourceLoader/models/ImageLoader.ts` -> **Severity: 0.107** (Bridge: 0.0011 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/State/State.ts` -> **Severity: 6.814** (Embedded: 0.1208 * Error Risk: 56.3934%)
- `src/State/Loader.ts` -> **Severity: 5.03** (Embedded: 0.086 * Error Risk: 58.4884%)
- `src/utils/ResourceLoader/models/ImageLoader.ts` -> **Severity: 4.566** (Embedded: 0.0621 * Error Risk: 73.4973%)
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 4.512** (Embedded: 0.0745 * Error Risk: 60.5532%)
- `src/utils/ResourceLoader/models/AudioLoader.ts` -> **Severity: 4.383** (Embedded: 0.0621 * Error Risk: 70.5637%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/State/State.ts` -> **Severity: 4095.5** (Blast Radius: 40.955 * Doc Risk: 100.0%)
- `src/utils/ResourceLoader/ResourceLoader.ts` -> **Severity: 4068.3** (Blast Radius: 40.683 * Doc Risk: 100.0%)
- `src/ui/components/Text/Text.tsx` -> **Severity: 3902.3** (Blast Radius: 39.023 * Doc Risk: 100.0%)
- `src/State/Loader.ts` -> **Severity: 3852.7** (Blast Radius: 38.527 * Doc Risk: 100.0%)
- `src/ui/components/Text/Char.tsx` -> **Severity: 3688.4** (Blast Radius: 36.884 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
