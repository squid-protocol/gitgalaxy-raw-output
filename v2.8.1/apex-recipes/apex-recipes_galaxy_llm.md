# ARCHITECTURAL_BRIEF: apex-recipes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/trailheadapps/apex-recipes` |
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
| Total Artifacts | 568 |
| Analyzed Artifacts (Scanned) | 375 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 193 |
| Total LOC | 13274 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 66.0% |
| Dominant Lang | XML |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8832 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3094 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2632 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| XML | 181 | 0 | 48.3% |
| MARKDOWN | 78 | 0 | 20.8% |
| APEX | 67 | 7685 | 17.9% |
| JAVASCRIPT | 19 | 2041 | 5.1% |
| JSON | 12 | 2144 | 3.2% |
| HTML | 7 | 851 | 1.9% |
| CSV | 4 | 269 | 1.1% |
| CSS | 3 | 191 | 0.8% |
| SHELL | 2 | 50 | 0.5% |
| BATCH | 1 | 43 | 0.3% |
| PLAINTEXT | 1 | 0 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +3.37; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 78%, Tests & Verification Files 15%, Declarative / Non-Code 2%, Large Core Modules 1%, Interface Declarations Files 1%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 296 | 78.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 79 | 21.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 193*

**Composition by Extension & Reason:**
- `.cls`: 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.xml`: 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dwl`: 14x Excluded (Unsupported Extension: '.dwl')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1055 LOC), 1x Excluded (Static Asset Blob without Intent: 1355 LOC)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 46 LOC)
- `.soql`: 1x Excluded (Unsupported Extension: '.soql')
- `.apex`: 1x Excluded (Unsupported Extension: '.apex')
- `.resource`: 1x Excluded (Unsupported Extension: '.resource')
- `.docx`: 1x Excluded (Explicitly Denied Extension: '.docx')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 1x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.7 | 9.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 95.3 | 1.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 46.6 | 1.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 558 | 58 | 2 | `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` |
| cleanup | 3 | 2 | 0 | `bin/generate-apex-docs.sh` |
| guards | 408 | 68 | 2 | `force-app/main/default/staticresources/highlight/prism.js` |
| danger | 116 | 26 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| concurrency | 111 | 16 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| connectivity | 161 | 14 | 0 | `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` |
| io | 143 | 39 | 1 | `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` |
| crypto | 0 | 0 | 0 | - |
| ipc | 6 | 2 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| time | 1 | 1 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| serialization | 4 | 2 | 0 | `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` |
| regex | 26 | 4 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| events | 31 | 15 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| tests | 1661 | 73 | 14 | `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` |
| docs | 136 | 24 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| debt | 62 | 8 | 0 | `bin/install-scratch.sh` |
| mutation | 2138 | 93 | 11 | `force-app/main/default/staticresources/highlight/prism.js` |
| dead_code | 361 | 69 | 3 | `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` |
| credential | 0 | 0 | 0 | - |
| threat | 20 | 6 | 0 | `force-app/main/default/staticresources/highlight/prism.js` |
| ml_ai | 153 | 3 | 0 | `force-app/main/default/lwc/errorPanel/templates/noDataIllustration.html` |
| ui | 6 | 3 | 0 | `force-app/main/default/staticresources/highlight/prism.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` (Hits: 22)
- `force-app/tests/Shared Code/RestClient_Tests.cls` (Hits: 9)
- `bin/generate-apex-docs.sh` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ApexClassUtilities.md** (`force-app/main/default/staticresources/documentation/ApexClassUtilities.md`) — 3 inbound connections
2. **getRecipeCode.json** (`force-app/main/default/lwc/formattedRecipeDisplay/__tests__/data/getRecipeCode.json`) — 2 inbound connections
3. **generateTreeData.json** (`force-app/main/default/lwc/recipeTreeView/__tests__/data/generateTreeData.json`) — 2 inbound connections
4. **LogSeverity.md** (`force-app/main/default/staticresources/documentation/LogSeverity.md`) — 2 inbound connections
5. **ldsUtils.js** (`force-app/main/default/lwc/ldsUtils/ldsUtils.js`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **formattedRecipeDisplay.test.js** (`force-app/main/default/lwc/formattedRecipeDisplay/__tests__/formattedRecipeDisplay.test.js`) — 6 outbound dependencies
2. **formattedDocsViewer.js** (`force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js`) — 5 outbound dependencies
3. **README.md** (`README.md`) — 4 outbound dependencies
4. **errorPanel.js** (`force-app/main/default/lwc/errorPanel/errorPanel.js`) — 4 outbound dependencies
5. **formattedRecipeDisplay.js** (`force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `stringify` **(Many-Argument Workhorses)** (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **86.6** | LOC: 243
  * *Intent:* */ /** * Converts the given token or token stream to an HTML representation. * * The following hooks will be run: * 1. `wrap`: On each {@link Token}. ...
- `insertBefore` **(Many-Argument Workhorses)** (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **24.1** | LOC: 35
  * *Intent:* * assert(newMarkup === Prism.languages.markup); * ``` * * @param {string} inside The property of `root` (e.g. a language id in `Prism.languages`) that...
- `DFS` **(Many-Argument Workhorses)** (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **23.8** | LOC: 28
  * *Intent:* // Traverse a language definition with Depth First Search
- `highlightElement` **(Many-Argument Workhorses)** (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **23.8** | LOC: 76
  * *Intent:* * @param {Element} element The element containing the code. * It must have a class of `language-xxxx` to be processed, where `xxxx` is a valid languag...
- `__global_context__` **(Unclassified)** (@ `bin/install-scratch.sh`) -> Impact: **21.4** | LOC: 47
- `deepClone` **(Compute Cores)** (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **19.4** | LOC: 41
  * *Intent:* /** * Creates a deep clone of the given object. * * The main intended use of this function is to clone language definitions. * * @param {T} o * @param...
- `handleMethodCall` **(Many-Argument Workhorses)** (@ `force-app/tests/Shared Code/ConnectApiWrapperMock.cls`) -> Impact: **18.3** | LOC: 49
- `createSObjectList` **(Many-Argument Workhorses)** (@ `force-app/tests/Shared Code/TestFactory.cls`) -> Impact: **14.1** | LOC: 42
  * *Intent:* /** * @description Creates a list of sObjects * @param sObj Type of sObjects to create * @param numberOfObjects Integer number of objects to create * ...
- `reduceErrors` **(Defensive Guards)** (@ `force-app/main/default/lwc/ldsUtils/ldsUtils.js`) -> Impact: **12.9** | LOC: 32
  * *Intent:* /** * Reduces one or more LDS errors into a string[] of error messages. * @param {FetchResponse|FetchResponse[]} errors * @return {String[]} Error mes...
- `toggleExpandNode` **(Defensive Guards)** (@ `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js`) -> Impact: **11.1** | LOC: 14

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Unclassified**: no dominant structural signature (too small or ambiguous)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `force-app/main/default/staticresources/highlight` | 2 | 759.7 | 25.76% | 7.58% |
| `force-app/tests/Shared Code` | 34 | 602.98 | 2.35% | 0.0% |
| `force-app/tests/Integration Recipes` | 12 | 350.34 | 2.4% | 0.0% |
| `force-app/tests/Data Recipes` | 10 | 310.02 | 1.17% | 0.0% |
| `force-app/main/default/staticresources/documentation` | 73 | 287.04 | 0.0% | 0.0% |
| `force-app/tests/Security Recipes` | 6 | 259.32 | 3.71% | 0.0% |
| `data` | 11 | 205.86 | 0.0% | 0.0% |
| `force-app/tests/Async Apex Recipes` | 14 | 148.52 | 4.58% | 0.0% |
| `force-app/main/default/dw` | 14 | 147.28 | 0.0% | 0.0% |
| `force-app/main/default/customMetadata` | 11 | 115.72 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` -> **95.2574%** Exposure
- `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` -> **82.0223%** Exposure
- `force-app/main/default/triggers/AccountTrigger.trigger` -> **50.0%** Exposure
- `force-app/main/default/triggers/LogTrigger.trigger` -> **50.0%** Exposure
- `force-app/main/default/triggers/PlatformEventRecipesTrigger.trigger` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` -> **100.0%** Exposure
- `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` -> **99.9999%** Exposure
- `force-app/main/default/staticresources/highlight/prism.js` -> **99.9944%** Exposure
- `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` -> **98.7973%** Exposure
- `jest.config.js` -> **91.6827%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` -> **40** Orphaned Functions | **0** Duplicates
- `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` -> **22** Orphaned Functions | **0** Duplicates
- `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls` -> **20** Orphaned Functions | **0** Duplicates
- `force-app/tests/Security Recipes/Safely_Tests.cls` -> **16** Orphaned Functions | **0** Duplicates
- `force-app/tests/Security Recipes/CanTheUser_Tests.cls` -> **15** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `61` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT) -> Cumulative Risk: **706.49**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.22)
- **Magnitude:** 83.42 | **LOC:** 66 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `toggleExpandNode` (Defensive Guards, Impact: 11.1), `isTreeNode` (Defensive Guards, Impact: 11.0), `handleTreeItemSelect` (Callbacks & Closures, Impact: 3.8)

### 2. `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT) -> Cumulative Risk: **621.74**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.45)
- **Magnitude:** 82.98 | **LOC:** 93 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.9986%)
- **Heaviest Functions:** `recipeFunc` (State Mutators, Impact: 6.2), `extractDescription` (Annotated Framework Methods, Impact: 6.0), `highlightCodeSegment` (I/O & Config Routines, Impact: 4.5)

### 3. `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT) -> Cumulative Risk: **568.0**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.96)
- **Magnitude:** 53.98 | **LOC:** 105 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9843%), State Flux (98.7973%)
- **Heaviest Functions:** `loadDocumentation` (Interface Declarations, Impact: 3.8), `formatMarkdown` (Callbacks & Closures, Impact: 3.8), `clearMarkdown` (Interface Declarations, Impact: 2.2)

### 4. `force-app/main/default/staticresources/highlight/prism.js` (JAVASCRIPT) -> Cumulative Risk: **535.23**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.58)
- **Magnitude:** 759.44 | **LOC:** 2050 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9944%), Safety Score (83.8676%), Concurrency (80.3163%)
- **Heaviest Functions:** `stringify` (Many-Argument Workhorses, Impact: 86.6), `insertBefore` (Many-Argument Workhorses, Impact: 24.1), `DFS` (Many-Argument Workhorses, Impact: 23.8)

### 5. `force-app/main/default/lwc/formattedDocsViewer/__tests__/formattedDocsViewer.test.js` (JAVASCRIPT) -> Cumulative Risk: **447.26**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +2.30)
- **Magnitude:** 25.72 | **LOC:** 68 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (93.0932%)
- **Heaviest Functions:** `mockFetch` (Callbacks & Closures, Impact: 3.6), `flushPromises` (Interface Declarations, Impact: 1.1)

### 6. `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` (JAVASCRIPT) -> Cumulative Risk: **389.01**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.40)
- **Magnitude:** 4.96 | **LOC:** 18 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (95.2574%), Safety Score (64.5656%)
- **Heaviest Functions:** `relatedClassesWireFunc` (State Mutators, Impact: 1.6), `testClassName` (Interface Declarations, Impact: 1.1)

### 7. `force-app/main/default/lwc/formattedRecipeDisplay/__tests__/formattedRecipeDisplay.test.js` (JAVASCRIPT) -> Cumulative Risk: **377.81**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.93)
- **Magnitude:** 18.28 | **LOC:** 164 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.4315%), Safety Score (34.2728%)
- **Heaviest Functions:** `flushPromises` (Interface Declarations, Impact: 1.1)

### 8. `force-app/tests/Async Apex Recipes/QueueableWithCalloutRecipes_Tests.cls` (APEX) -> Cumulative Risk: **374.5**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Tests & Verification Files` (z +0.03)
- **Magnitude:** 31.66 | **LOC:** 59 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (45.6803%)
- **Heaviest Functions:** `testQueueableWithCalloutRecipesPositive` (Tests & Verification, Impact: 3.4), `testQueuableWithCalloutNegativeDMLError` (Tests & Verification, Impact: 2.0), `makeData` (Tests & Verification, Impact: 1.2)

### 9. `force-app/main/default/lwc/recipeTreeView/__tests__/recipeTreeView.test.js` (JAVASCRIPT) -> Cumulative Risk: **351.65**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.84)
- **Magnitude:** 21.74 | **LOC:** 134 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9995%), Cognitive Load (51.6505%)
- **Heaviest Functions:** `flushPromises` (Interface Declarations, Impact: 1.1)

### 10. `force-app/main/default/lwc/apexRecipesContainer/__tests__/apexRecipesContainer.test.js` (JAVASCRIPT) -> Cumulative Risk: **324.27**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +2.42)
- **Magnitude:** 10.9 | **LOC:** 79 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.5792%), Cognitive Load (24.688%)
- **Heaviest Functions:** `mockFetch` (Callbacks & Closures, Impact: 1.8), `flushPromises` (Interface Declarations, Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `force-app/main/default/staticresources/highlight/prism.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 759.44 | **LOC:** 2050 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.2597%), Tech Debt (15.1569%)
**Top Internal Functions/Classes:**
  * `stringify` **(Many-Argument Workhorses)** (Impact: 86.6)
    * *Intent:* */ /** * Converts the given token or token stream to an HTML representation. * * The following hooks...
  * `insertBefore` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* * assert(newMarkup === Prism.languages.markup); * ``` * * @param {string} inside The property of `ro...
  * `DFS` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* // Traverse a language definition with Depth First Search
  * `highlightElement` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* * @param {Element} element The element containing the code. * It must have a class of `language-xxxx...
  * `deepClone` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* /** * Creates a deep clone of the given object. * * The main intended use of this function is to clo...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 125 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 242`, `args: 60`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 5`, `state_mutation: 147`, `dead_code: 6`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `concurrency: 18`, `import: 2`
* *Defense:* `safety: 67`, `doc: 64`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 205.7 | **LOC:** 691 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.0111%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `httpPatchUpdateAccountRecordsPositive` **(Tests & Verification)** (Impact: 4.5)
  * `httpPutUpsertContactRecordsPositive` **(Tests & Verification)** (Impact: 3.0)
  * `httpPatchUpdateAccountRecordsNegative` **(Tests & Verification)** (Impact: 3.0)
  * `httpPatchUpdateAccountRecordsNegativeCatchException` **(Tests & Verification)** (Impact: 3.0)
  * `httpPatchUpdateAccountRecordsNegativeNoAccess` **(Tests & Verification)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 3`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 135`, `dead_code: 2`, `unreferenced_by_name: 22`
* *Architecture:* `io: 8`
* *Defense:* `safety: 8`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 121.04 | **LOC:** 825 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDeleteAccountViaKeywordInSystemModePositive` **(Tests & Verification)** (Impact: 3.0)
  * `testDeleteAccountViaKeywordInUserModePositive` **(Tests & Verification)** (Impact: 3.0)
  * `testDeleteAccountViaDatabaseMethodInUserModePositive` **(Tests & Verification)** (Impact: 3.0)
  * `testDeleteAccountViaDatabaseMethodInSystemModePositive` **(Tests & Verification)** (Impact: 3.0)
  * `testInsertInSystemModePositive` **(Tests & Verification)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 1`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`, `unreferenced_by_name: 40`
* *Architecture:* `io: 22`
* *Defense:* `safety: 48`, `test: 187`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/TestFactory.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 114.54 | **LOC:** 319 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.3889%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createSObjectList` **(Many-Argument Workhorses)** (Impact: 14.1)
    * *Intent:* /** * @description Creates a list of sObjects * @param sObj Type of sObjects to create * @param numb...
  * `addFieldDefaults` **(Generic / Templated Code)** (Impact: 6.6)
    * *Intent:* /** * @description Sets field defaults on the sObj given the map of defaults. * @param sObj Obj to m...
  * `createSObjectList` **(Many-Argument Workhorses)** (Impact: 5.3)
    * *Intent:* /** * @description Creates a list of sObjects * @param sObj Type of sObjects to create * @param numb...
  * `createSObjectList` **(Many-Argument Workhorses)** (Impact: 4.8)
    * *Intent:* /** * @description Creates a list of sObjects * @param sObj Type of sObjects to create * @param numb...
  * `createSObject` **(Many-Argument Workhorses)** (Impact: 4.5)
    * *Intent:* /** * @description Create a single sObject * @param sObj Type of sObject to create * @param defaultC...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 18`, `args: 16`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `safety: 2`, `doc: 18`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Security Recipes/Safely_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 104.04 | **LOC:** 419 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.1878%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDoUpsertMethodsNoThrowPositive` **(Tests & Verification)** (Impact: 5.8)
  * `testMarketingProfileGeneratesInsertExceptionPositive` **(Tests & Verification)** (Impact: 3.0)
  * `testMarketingProfileGeneratesUpdateExceptionPositive` **(Tests & Verification)** (Impact: 3.0)
  * `testMarketingProfileGeneratesUpsertExceptionPositive` **(Tests & Verification)** (Impact: 3.0)
  * `testDoQueryThrowsRemovedFieldsException` **(Tests & Verification)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 1`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 50`, `unreferenced_by_name: 16`
* *Architecture:* None
* *Defense:* `safety: 8`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 101.32 | **LOC:** 526 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testGetAccountsAndContactsPositive` **(Tests & Verification)** (Impact: 7.1)
  * `testProfileDeniesAccountAccessNegative` **(Tests & Verification)** (Impact: 3.0)
  * `testQueryWithFilterNegativeNoPermsToAccountNegative` **(Tests & Verification)** (Impact: 3.0)
  * `testGetAccountFilterByStatePositive` **(Tests & Verification)** (Impact: 3.0)
  * `testgetSumOfOpportunityRecordsPositive` **(Tests & Verification)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 1`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`, `unreferenced_by_name: 20`
* *Architecture:* `io: 8`
* *Defense:* `safety: 7`, `doc: 6`, `test: 97`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 96.94 | **LOC:** 373 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4857%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testStripInaccessibleFromSubQueryMinAccessWithPermsetNegative` **(Tests & Verification)** (Impact: 7.5)
  * `testStripInaccessibleFromQueryMinAccessWithPermsetNegative` **(Tests & Verification)** (Impact: 6.0)
  * `testStripInaccessibleFromSubQueryMinAccessWithpermsetPositive` **(Tests & Verification)** (Impact: 5.8)
  * `testStripInaccessibleFromUntrustedDataMinAccessWithPermSetPositive` **(Tests & Verification)** (Impact: 4.5)
  * `testStripInaccessibleBeforeDMLMinAccessProfileNegative` **(Tests & Verification)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 1`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 11`
* *Architecture:* `io: 3`
* *Defense:* `safety: 13`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 83.42 | **LOC:** 66 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (82.0223%)
**Top Internal Functions/Classes:**
  * `toggleExpandNode` **(Defensive Guards)** (Impact: 11.1)
  * `isTreeNode` **(Defensive Guards)** (Impact: 11.0)
  * `handleTreeItemSelect` **(Callbacks & Closures)** (Impact: 3.8)
  * `connectedCallback` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 14`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` RecipeTreeViewController.generateTreeData, lwc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 82.98 | **LOC:** 93 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.2459%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `recipeFunc` **(State Mutators)** (Impact: 6.2)
  * `extractDescription` **(Annotated Framework Methods)** (Impact: 6.0)
  * `highlightCodeSegment` **(I/O & Config Routines)** (Impact: 4.5)
  * `loadPrism` **(Callbacks & Closures)** (Impact: 4.0)
  * `githubUrl` **(Interface Declarations)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 12`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 4`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` FormattedRecipeDisplayController.getRecipeCode, highlight, platformResourceLoader, lwc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/TriggerHandler_Test.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 56.4 | **LOC:** 387 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.141%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBypassAPI` **(Tests & Verification)** (Impact: 4.5)
    * *Intent:* // test bypass api
  * `testLoopCount` **(Tests & Verification)** (Impact: 3.0)
    * *Intent:* // instance method tests
  * `testBeforeInsert` **(Tests & Verification)** (Impact: 1.5)
    * *Intent:* /*************************************** * unit tests ***************************************/ // co...
  * `testBeforeUpdate` **(Tests & Verification)** (Impact: 1.5)
  * `testBeforeDelete` **(Tests & Verification)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `state_mutation: 10`, `dead_code: 1`, `unreferenced_by_name: 13`
* *Architecture:* None
* *Defense:* `safety: 9`, `doc: 4`, `test: 50`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 53.98 | **LOC:** 105 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.5081%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadDocumentation` **(Interface Declarations)** (Impact: 3.8)
  * `formatMarkdown` **(Callbacks & Closures)** (Impact: 3.8)
  * `clearMarkdown` **(Interface Declarations)** (Impact: 2.2)
  * `applyStyleTo` **(Callbacks & Closures)** (Impact: 2.1)
  * `renderedCallback` **(I/O & Config Routines)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 12`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` documentation, highlight, markdownIt, platformResourceLoader, lwc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Trigger Recipes/AccountTriggerHandler_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 44.88 | **LOC:** 272 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.9596%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `afterUpdateTestPositive` **(Tests & Verification)** (Impact: 4.5)
  * `testBeforeUpdatePositive` **(Tests & Verification)** (Impact: 3.5)
  * `afterInsertBulkTestPositive` **(Tests & Verification)** (Impact: 3.4)
  * `testAfterInsertPositive` **(Tests & Verification)** (Impact: 3.0)
  * `afterUpdateTestNegativeDMLException` **(Tests & Verification)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 5`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `unreferenced_by_name: 9`
* *Architecture:* `io: 8`
* *Defense:* `safety: 7`, `doc: 2`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Integration Recipes/CalloutRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 40.9 | **LOC:** 413 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.3782%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRawCalloutNegative` **(Tests & Verification)** (Impact: 3.5)
  * `insertAccountAndContactsFromUntypedResponsePositive` **(Tests & Verification)** (Impact: 3.0)
  * `testRawCalloutPositive` **(Tests & Verification)** (Impact: 2.0)
  * `httpGetCalloutToSecondSalesforceOrgPositive` **(Tests & Verification)** (Impact: 2.0)
  * `httpGetCalloutToSecondSalesforceOrgNegative` **(Tests & Verification)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 15`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 14`
* *Architecture:* `io: 2`
* *Defense:* `safety: 5`, `doc: 4`, `test: 72`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/ConnectApiWrapperMock.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 40.36 | **LOC:** 56 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.6618%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleMethodCall` **(Many-Argument Workhorses)** (Impact: 18.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/errorPanel/__tests__/errorPanel.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 39.7 | **LOC:** 119 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.3235%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 17`, `args: 12`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `concurrency: 6`, `import: 2`
* *Defense:* `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errorPanel, lwc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Platform Event Recipes/PlatformEventRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 32.58 | **LOC:** 180 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3231%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testEventPublishNegativeMinAccessUser` **(Tests & Verification)** (Impact: 4.5)
  * `testEventPublishCallbackFailsWhenNoEventUuid` **(Tests & Verification)** (Impact: 3.0)
  * `testEventPublishPositive` **(Tests & Verification)** (Impact: 1.5)
  * `testEventPublishNegativeInvalidFields` **(Tests & Verification)** (Impact: 1.5)
  * `testEventPublishCallbackSuccess` **(Tests & Verification)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 1`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 14`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`
* *Defense:* `safety: 7`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Async Apex Recipes/QueueableWithCalloutRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 31.66 | **LOC:** 59 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6803%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testQueueableWithCalloutRecipesPositive` **(Tests & Verification)** (Impact: 3.4)
  * `testQueuableWithCalloutNegativeDMLError` **(Tests & Verification)** (Impact: 2.0)
  * `makeData` **(Tests & Verification)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `concurrency: 7`
* *Defense:* `safety: 1`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Platform Cache Recipes/PlatformCacheRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 31.24 | **LOC:** 248 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.1725%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRemoveKeyFromSessionCacheNegativeNoKey` **(Tests & Verification)** (Impact: 2.9)
  * `testRemoveKeyFromOrgCacheNegativeNoKey` **(Tests & Verification)** (Impact: 2.9)
  * `testStoreValueInSessionCachePositive` **(Tests & Verification)** (Impact: 1.5)
  * `testStoreValueInSessionCacheWithTTLPositive` **(Tests & Verification)** (Impact: 1.5)
  * `testGetValueFromSessionCachePositive` **(Tests & Verification)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 12`
* *Architecture:* None
* *Defense:* `safety: 4`, `doc: 1`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/install-scratch.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 30.36 | **LOC:** 53 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.4344%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 21.4)
  * `Anonymous_Block` **(Unclassified)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`
* *Architecture:* `io: 1`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/RestClient_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 28.36 | **LOC:** 267 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.0191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testGetWithPathAndQueryPositive` **(Tests & Verification)** (Impact: 3.0)
    * *Intent:* /** * Convience, Instance Methods * These 6 methods are not utilized by our API service * class. */ ...
  * `testStaticMakeApiCallFullParamsPositive` **(Tests & Verification)** (Impact: 2.4)
    * *Intent:* /** * Note: we do not have a constructor test for the no param * constructor. Because it's access mo...
  * `testStaticMakeApiCallNoHeadersoOrBodyParamsPositive` **(Tests & Verification)** (Impact: 2.2)
  * `testStaticMakeApiCallNoHeadersoOrBodyOrQueryParamsPositive` **(Tests & Verification)** (Impact: 2.2)
  * `testDelWithPathPositive` **(Tests & Verification)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 10`
* *Architecture:* `io: 9`
* *Defense:* `safety: 1`, `doc: 6`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/CollectionUtils_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 27.58 | **LOC:** 143 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1571%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMapFromCollectionWithListOfValuesPostive` **(Tests & Verification)** (Impact: 6.0)
  * `testDemonstrateIdMapFromCollectionByKeyPositiveWithList` **(Tests & Verification)** (Impact: 4.5)
  * `testDemonstrateStringMapFromCollectionByKeyPositiveWithList` **(Tests & Verification)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 1`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/Opportunities.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 27.08 | **LOC:** 605 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Integration Recipes/ApiServiceRecipes_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 26.98 | **LOC:** 147 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3801%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testGetCurrentDataPositive200` **(Tests & Verification)** (Impact: 3.5)
  * `testGetCurrentDataNegative500TriggersWhenElse` **(Tests & Verification)** (Impact: 3.5)
  * `testGetCurrentDataNegativeJSONExceptionThrown` **(Tests & Verification)** (Impact: 3.4)
  * `testGetCurrentDataNegative404` **(Tests & Verification)** (Impact: 3.4)
  * `testConstructorAssignsNamedCredentialPositive` **(Tests & Verification)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 5`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 5`
* *Architecture:* None
* *Defense:* `safety: 6`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/TestDataHelpers.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 26.9 | **LOC:** 58 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.7935%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `genAccountWithOptions` **(Compute Cores)** (Impact: 4.3)
    * *Intent:* /** * @description Generates an Account with (optionally) the Country code Set * @param setCountry B...
  * `genXNumberOfAccounts` **(Generic / Templated Code)** (Impact: 3.2)
    * *Intent:* /** * @description Generates a list of Accounts. * @param numAccounts Nubmer of accounts to generate...
  * `createAccount` **(State Mutators)** (Impact: 1.9)
    * *Intent:* /** * @description Generates an Account object with an optional Country set * @param setCountry Bool...
  * `genContactForAccount` **(Interface Declarations)** (Impact: 1.8)
    * *Intent:* /** * @description Generates a contact associated with the acctId param. * @param acctId AccountID t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* `doc: 4`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Security Recipes/CanTheUser_Tests.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 26.78 | **LOC:** 167 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5578%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBulkFLSAccessibleWithAccountPositive` **(Tests & Verification)** (Impact: 2.7)
  * `getBulkFLSUpdatableWithAccountPositive` **(Tests & Verification)** (Impact: 2.7)
  * `getBulkFLSAccessibleWithAccountPositiveWithNegativeResults` **(Tests & Verification)** (Impact: 1.5)
  * `getBulkFLSUpdatableWithAccountPositiveWithNegativeResults` **(Tests & Verification)** (Impact: 1.5)
  * `memoizedFLSMDCcomparesAccesibleToUpdatable` **(Tests & Verification)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 15`
* *Architecture:* None
* *Defense:* `safety: 1`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
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

- `force-app/main/default/lwc/errorPanel/errorPanel.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 31.0026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `force-app/main/default/lwc/ldsUtils/ldsUtils.js` -> **Severity: 0.26** (Embedded: 0.006 * Error Risk: 43.1855%)
- `force-app/main/default/lwc/errorPanel/errorPanel.js` -> **Severity: 0.164** (Embedded: 0.0027 * Error Risk: 61.3692%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `force-app/main/default/lwc/errorPanel/errorPanel.js` -> **Severity: 282.4** (Blast Radius: 4.236 * Doc Risk: 66.6667%)
- `force-app/main/default/lwc/apexRecipesContainer/__tests__/apexRecipesContainer.test.js` -> **Severity: 229.0** (Blast Radius: 2.29 * Doc Risk: 100.0%)
- `force-app/main/default/lwc/apexRecipesContainer/apexRecipesContainer.js` -> **Severity: 229.0** (Blast Radius: 2.29 * Doc Risk: 100.0%)
- `force-app/main/default/lwc/formattedDocsViewer/__tests__/formattedDocsViewer.test.js` -> **Severity: 229.0** (Blast Radius: 2.29 * Doc Risk: 100.0%)
- `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` -> **Severity: 229.0** (Blast Radius: 2.29 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
