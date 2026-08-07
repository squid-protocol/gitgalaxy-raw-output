# ARCHITECTURAL_BRIEF: apex-recipes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/apex-recipes` |
| **Timestamp** | `2026-08-07T03:46:52.681393+00:00` |
| **Scan Duration** | `0.71s` |
| **Git Branch** | `main` |
| **Git Commit** | `3462c7d4bd72998b97da95bd613913a944c4bc0d` |
| **Git Remote** | `https://github.com/trailheadapps/apex-recipes` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 79 malicious artifacts.

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
| Total Artifacts | 568 |
| Analyzed Artifacts (Scanned) | 351 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 217 |
| Total LOC | 11552 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 61.8% |
| Dominant Lang | APEX |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| XML | 167 | 0 | 47.6% |
| MARKDOWN | 78 | 0 | 22.2% |
| APEX | 63 | 6911 | 17.9% |
| JAVASCRIPT | 13 | 1088 | 3.7% |
| JSON | 12 | 2144 | 3.4% |
| HTML | 7 | 851 | 2.0% |
| CSV | 4 | 269 | 1.1% |
| CSS | 3 | 191 | 0.9% |
| SHELL | 2 | 50 | 0.6% |
| BATCH | 1 | 48 | 0.3% |
| PLAINTEXT | 1 | 0 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.279`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 217 | 61.8% |
| file_cluster_13 | 49 | 14.0% |
| file_cluster_4 | 3 | 0.9% |
| file_cluster_17 | 1 | 0.3% |
| file_cluster_0 | 1 | 0.3% |
| file_cluster_9 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 79 | 22.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 217*

**Composition by Extension & Reason:**
- `.xml`: 88x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cls`: 78x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.dwl`: 14x Excluded (Unsupported Extension: '.dwl')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1055 LOC), 1x Excluded (Static Asset Blob without Intent: 1355 LOC)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 46 LOC)
- `.soql`: 1x Excluded (Unsupported Extension: '.soql')
- `.apex`: 1x Excluded (Unsupported Extension: '.apex')
- `.resource`: 1x Excluded (Unsupported Extension: '.resource')
- `.docx`: 1x Excluded (Explicitly Denied Extension: '.docx')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 6.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 12.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 0.7 | 0.2 | 0.0 |
| API Exposure | 0.0 | 6.0 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 39.2 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 68.5 | 6.6 | 3.2 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` (Hits: 22)
- `force-app/tests/Shared Code/RestClient_Tests.cls` (Hits: 9)
- `bin/generate-apex-docs.sh` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **getRecipeCode.json** (`force-app/main/default/lwc/formattedRecipeDisplay/__tests__/data/getRecipeCode.json`) — 1 inbound connections
2. **generateTreeData.json** (`force-app/main/default/lwc/recipeTreeView/__tests__/data/generateTreeData.json`) — 1 inbound connections
3. **ldsUtils.js** (`force-app/main/default/lwc/ldsUtils/ldsUtils.js`) — 1 inbound connections
4. **.prettierrc** (`.prettierrc`) — 0 inbound connections
5. **project-scratch-def.json** (`config/project-scratch-def.json`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **formattedDocsViewer.js** (`force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js`) — 5 outbound dependencies
2. **errorPanel.js** (`force-app/main/default/lwc/errorPanel/errorPanel.js`) — 4 outbound dependencies
3. **formattedRecipeDisplay.js** (`force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js`) — 4 outbound dependencies
4. **recipeTreeView.js** (`force-app/main/default/lwc/recipeTreeView/recipeTreeView.js`) — 2 outbound dependencies
5. **relatedCodeTabs.js** (`force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `matchGrammar` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **82.1** | LOC: 107
- `currentScript` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **63.4** | LOC: 125
  * *Intent:* /** * Creates a deep clone of the given object.
- `__global_context__` (@ `bin/install-scratch.sh`) -> Impact: **21.4** | LOC: 47
- `testStripInaccessibleFromSubQueryMinAcce` (@ `force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls`) -> Impact: **20.5** | LOC: 52
- `deepClone` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **19.4** | LOC: 41
  * *Intent:* /** * A namespace for utility methods. * * All function in this namespace that are not explicitly marked as _public_ are for __internal use only__ and...
- `callAtFutureCalloutPositive` (@ `force-app/tests/Async Apex Recipes/AtFutureRecipes_Tests.cls`) -> Impact: **18.7** | LOC: 31
- `Account` (@ `force-app/tests/Files Recipes/FilesRecipes_Tests.cls`) -> Impact: **15.9** | LOC: 25
- `reduceErrors` (@ `force-app/main/default/lwc/ldsUtils/ldsUtils.js`) -> Impact: **15.5** | LOC: 32
  * *Intent:* /**
- `testStripInaccessibleFromQueryMinAccessW` (@ `force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls`) -> Impact: **15.4** | LOC: 40
- `makeData` (@ `force-app/tests/Files Recipes/FilesRecipes_Tests.cls`) -> Impact: **14.9** | LOC: 29

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `force-app/tests/Shared Code` | 30 | 652.98 | 5.81% | 0.0% |
| `force-app/tests/Data Recipes` | 10 | 589.2 | 5.23% | 0.0% |
| `force-app/tests/Security Recipes` | 6 | 444.02 | 6.1% | 0.0% |
| `force-app/tests/Integration Recipes` | 10 | 379.46 | 4.34% | 0.0% |
| `force-app/main/default/staticresources/documentation` | 73 | 287.04 | 0.0% | 0.0% |
| `force-app/main/default/staticresources/highlight` | 2 | 252.24 | 6.05% | 28.81% |
| `data` | 11 | 205.86 | 3.31% | 0.0% |
| `force-app/tests/Async Apex Recipes` | 14 | 185.12 | 9.54% | 0.0% |
| `force-app/tests/Trigger Recipes` | 4 | 159.2 | 6.2% | 0.0% |
| `force-app/tests/DataWeaveInApex Recipes` | 13 | 157.12 | 5.67% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bin/generate-apex-docs.sh` -> **100.0%** Exposure
- `force-app/main/default/lwc/apexRecipesContainer/apexRecipesContainer.js` -> **100.0%** Exposure
- `force-app/main/default/lwc/errorPanel/errorPanel.js` -> **100.0%** Exposure
- `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` -> **100.0%** Exposure
- `force-app/main/default/triggers/AccountTrigger.trigger` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` -> **100.0%** Exposure
- `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` -> **100.0%** Exposure
- `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` -> **100.0%** Exposure
- `force-app/main/default/triggers/AccountTrigger.trigger` -> **100.0%** Exposure
- `force-app/main/default/triggers/LogTrigger.trigger` -> **99.9987%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` -> **16** Orphaned Functions | **24** Duplicates
- `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` -> **19** Orphaned Functions | **5** Duplicates
- `force-app/tests/Security Recipes/Safely_Tests.cls` -> **16** Orphaned Functions | **3** Duplicates
- `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls` -> **18** Orphaned Functions | **0** Duplicates
- `force-app/tests/Trigger Recipes/AccountTriggerHandler_Tests.cls` -> **9** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bin/install-scratch.sh`** -> AI Confidence: **99.29%**
2. **`jest.config.js`** -> AI Confidence: **99.29%**
3. **`force-app/tests/Data Recipes/DMLRecipes_Tests.cls`** -> AI Confidence: **99.29%**
4. **`force-app/tests/Data Recipes/SOQLRecipes_Tests.cls`** -> AI Confidence: **99.29%**
5. **`force-app/tests/Files Recipes/FilesRecipes_Tests.cls`** -> AI Confidence: **99.29%**
6. **`force-app/tests/Integration Recipes/AuraEnabledRecipes_Tests.cls`** -> AI Confidence: **99.29%**
7. **`force-app/tests/Platform Cache Recipes/PlatformCacheRecipes_Tests.cls`** -> AI Confidence: **99.29%**
8. **`force-app/tests/Platform Event Recipes/PlatformEventRecipes_Tests.cls`** -> AI Confidence: **99.29%**
9. **`force-app/tests/Security Recipes/Safely_Tests.cls`** -> AI Confidence: **99.29%**
10. **`force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `21` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT) -> Cumulative Risk: **610.08**
- **Archetype:** `file_cluster_4` (Distance: 12.549 IQR)
- **Magnitude:** 87.52 | **LOC:** 66 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `toggleExpandNode` (Impact: 11.1), `isTreeNode` (Impact: 11.0), `connectedCallback` (Impact: 5.5)

### 2. `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT) -> Cumulative Risk: **599.54**
- **Archetype:** `file_cluster_4` (Distance: 12.841 IQR)
- **Magnitude:** 115.28 | **LOC:** 93 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9988%), Cognitive Load (95.6166%)
- **Heaviest Functions:** `extractDescription` (Impact: 8.0), `loadPrism` (Impact: 6.7), `highlightCodeSegment` (Impact: 6.2)

### 3. `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT) -> Cumulative Risk: **597.57**
- **Archetype:** `file_cluster_4` (Distance: 12.726 IQR)
- **Magnitude:** 54.84 | **LOC:** 105 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9988%)
- **Heaviest Functions:** `renderedCallback` (Impact: 9.7), `loadScript` (Impact: 2.4), `loadDocumentation` (Impact: 2.0)

### 4. `bin/install-scratch.sh` (SHELL) -> Cumulative Risk: **461.99**
- **Archetype:** `file_cluster_8` (Distance: 9.904 IQR)
- **Magnitude:** 33.36 | **LOC:** 53 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.8356%), State Flux (95.9424%), Safety Score (91.4834%)
- **Heaviest Functions:** `__global_context__` (Impact: 21.4), `Anonymous_Block` (Impact: 6.2)

### 5. `force-app/main/default/triggers/AccountTrigger.trigger` (APEX) -> Cumulative Risk: **451.48**
- **Archetype:** `file_cluster_9` (Distance: 18.809 IQR)
- **Magnitude:** 10.14 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Safety Score (99.6242%), Spec Match (80.0%)
- **Heaviest Functions:** `AccountTrigger` (Impact: 3.9)

### 6. `force-app/main/default/lwc/errorPanel/errorPanel.js` (JAVASCRIPT) -> Cumulative Risk: **435.55**
- **Archetype:** `file_cluster_13` (Distance: 12.236 IQR)
- **Magnitude:** 13.9 | **LOC:** 29 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.994%), Safety Score (68.8582%)
- **Heaviest Functions:** `render` (Impact: 3.0), `errorMessages` (Impact: 1.9), `handleShowDetailsClick` (Impact: 1.6)

### 7. `bin/generate-apex-docs.sh` (SHELL) -> Cumulative Risk: **428.71**
- **Archetype:** `file_cluster_8` (Distance: 11.474 IQR)
- **Magnitude:** 12.54 | **LOC:** 27 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (99.9629%), Safety Score (88.3397%), Spec Match (80.0%)
- **Heaviest Functions:** `__global_context__` (Impact: 9.3)

### 8. `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` (JAVASCRIPT) -> Cumulative Risk: **416.4**
- **Archetype:** `file_cluster_0` (Distance: 10.324 IQR)
- **Magnitude:** 6.26 | **LOC:** 18 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (97.9645%), Spec Match (86.6667%), Safety Score (69.385%)
- **Heaviest Functions:** `testClassName` (Impact: 1.9), `relatedClassesWireFunc` (Impact: 1.1)

### 9. `force-app/main/default/lwc/apexRecipesContainer/apexRecipesContainer.js` (JAVASCRIPT) -> Cumulative Risk: **358.91**
- **Archetype:** `file_cluster_13` (Distance: 9.941 IQR)
- **Magnitude:** 3.74 | **LOC:** 10 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (96.8759%), Safety Score (69.7059%), Spec Match (46.6667%)
- **Heaviest Functions:** `handleRecipeSelect` (Impact: 1.6)

### 10. `force-app/main/default/staticresources/highlight/prism.js` (JAVASCRIPT) -> Cumulative Risk: **346.95**
- **Archetype:** `file_cluster_8` (Distance: 9.778 IQR)
- **Magnitude:** 251.98 | **LOC:** 2050 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Safety Score (71.8734%), State Flux (39.5541%)
- **Heaviest Functions:** `matchGrammar` (Impact: 82.1), `currentScript` (Impact: 63.4), `deepClone` (Impact: 19.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.59 IQR)
- **Top Global Matches:** file_cluster_13: 11.59, file_cluster_8: 12.098, file_cluster_0: 12.122
- **Magnitude:** 332.04 | **LOC:** 825 | **CtrlFlow:** 98.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.3328%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDeleteAccountViaKeywordInSystemModeP` (Impact: 10.0)
  * `testDeleteAccountViaDatabaseMethodInUser` (Impact: 10.0)
  * `testDeleteAccountViaDatabaseMethodInSyst` (Impact: 10.0)
  * `testDeleteAccountViaKeywordInUserModePos` (Impact: 9.9)
  * `testDatabaseMethodInsertInSystemModeNega` (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 1`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 72`, `duplicate_logic: 24`, `orphaned_logic: 16`
* *Architecture:* `io: 22`, `import: 248`
* *Defense:* `safety: 48`, `test: 187`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/staticresources/highlight/prism.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.778 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.835 IQR)
- **Top Global Matches:** file_cluster_8: 9.778, file_cluster_7: 10.179, file_cluster_1: 10.473
- **Magnitude:** 251.98 | **LOC:** 2050 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9412%), Tech Debt (29.9087%)
**Top Internal Functions/Classes:**
  * `matchGrammar` (Impact: 82.1)
  * `currentScript` (Impact: 63.4)
    * *Intent:* /** * Creates a deep clone of the given object.
  * `deepClone` (Impact: 19.4)
    * *Intent:* /** * A namespace for utility methods. * * All function in this namespace that are not explicitly ma...
  * `encode` (Impact: 9.5)
  * `getLanguage` (Impact: 9.3)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 28`, `args: 11`, `func_start: 11`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 1`, `state_mutation: 39`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* `safety: 11`, `doc: 58`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.962 IQR)
- **Top Global Matches:** file_cluster_13: 10.962, file_cluster_8: 11.421, file_cluster_0: 11.613
- **Magnitude:** 185.54 | **LOC:** 373 | **CtrlFlow:** 96.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.5887%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testStripInaccessibleFromSubQueryMinAcce` (Impact: 20.5)
  * `testStripInaccessibleFromQueryMinAccessW` (Impact: 15.4)
  * `testStripInaccessibleBeforeDMLMinAccessP` (Impact: 12.5)
  * `testStripInaccessibleFromSubQueryMinAcce` (Impact: 10.8)
  * `testStripInaccessibleFromUntrustedDataNe` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 1`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `duplicate_logic: 8`, `orphaned_logic: 7`
* *Architecture:* `io: 3`, `import: 97`
* *Defense:* `safety: 13`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Security Recipes/Safely_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.223 IQR)
- **Top Global Matches:** file_cluster_13: 11.223, file_cluster_8: 11.715, file_cluster_0: 11.843
- **Magnitude:** 174.64 | **LOC:** 419 | **CtrlFlow:** 93.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.8829%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDoQueryThrowsRemovedFieldsException` (Impact: 11.2)
  * `testDoUpsertMethodsNoThrowPositive` (Impact: 10.8)
  * `testMarketingProfileGeneratesInsertExcep` (Impact: 10.3)
  * `testMarketingProfileGeneratesUpdateExcep` (Impact: 10.2)
  * `testMarketingProfileGeneratesUpsertExcep` (Impact: 10.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 1`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 61`, `duplicate_logic: 3`, `orphaned_logic: 16`
* *Architecture:* `import: 105`
* *Defense:* `safety: 8`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.063 IQR)
- **Top Global Matches:** file_cluster_13: 11.063, file_cluster_8: 11.532, file_cluster_16: 11.677
- **Magnitude:** 155.12 | **LOC:** 526 | **CtrlFlow:** 92.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.0655%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testGetAccountsAndContactsPositive` (Impact: 13.3)
  * `testQueryWithFilterNegativeNoPermsToAcco` (Impact: 13.1)
  * `testProfileDeniesAccountAccessNegative` (Impact: 10.2)
  * `testgetSumOfOpportunityRecordsPositive` (Impact: 5.9)
  * `testGetAccountFilterByStatePositive` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 1`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`, `orphaned_logic: 18`
* *Architecture:* `io: 6`, `import: 113`
* *Defense:* `safety: 6`, `doc: 6`, `test: 87`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.638 IQR)
- **Top Global Matches:** file_cluster_13: 10.638, file_cluster_8: 11.263, file_cluster_0: 11.364
- **Magnitude:** 153.9 | **LOC:** 691 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.826%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `httpPatchUpdateAccountRecordsPositive` (Impact: 9.0)
  * `httpPatchUpdateAccountRecordsNegativeNoA` (Impact: 6.6)
  * `httpPatchUpdateAccountRecordsNegativeCat` (Impact: 6.5)
  * `httpPatchUpdateAccountRecordsNegativeJSO` (Impact: 6.3)
  * `httpPutUpsertContactRecordsNegativeMinAc` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 3`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 36`, `dead_code: 2`, `duplicate_logic: 5`, `orphaned_logic: 19`
* *Architecture:* `io: 8`, `import: 249`
* *Defense:* `safety: 8`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Trigger Recipes/AccountTriggerHandler_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.223 IQR)
- **Top Global Matches:** file_cluster_13: 10.223, file_cluster_8: 10.629, file_cluster_0: 10.799
- **Magnitude:** 119.08 | **LOC:** 272 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `afterUpdateTestNegativeDMLException` (Impact: 10.1)
  * `afterUpdateTestPositive` (Impact: 8.4)
  * `testBeforeUpdateWithAddErrorNegative` (Impact: 7.9)
  * `Account` (Impact: 6.5)
  * `Account` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 5`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 20`, `duplicate_logic: 7`, `orphaned_logic: 9`
* *Architecture:* `io: 8`, `import: 49`
* *Defense:* `safety: 7`, `doc: 3`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.841 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.001 IQR)
- **Top Global Matches:** file_cluster_4: 12.841, file_cluster_0: 13.118, file_cluster_13: 13.176
- **Magnitude:** 115.28 | **LOC:** 93 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.6166%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `extractDescription` (Impact: 8.0)
  * `loadPrism` (Impact: 6.7)
  * `highlightCodeSegment` (Impact: 6.2)
  * `githubUrl` (Impact: 3.9)
  * `loadScript` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 12`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` platformResourceLoader, highlight, FormattedRecipeDisplayController.getRecipeCode, lwc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.549 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.867 IQR)
- **Top Global Matches:** file_cluster_4: 12.549, file_cluster_13: 13.09, file_cluster_0: 13.217
- **Magnitude:** 87.52 | **LOC:** 66 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `toggleExpandNode` (Impact: 11.1)
  * `isTreeNode` (Impact: 11.0)
  * `connectedCallback` (Impact: 5.5)
  * `handleTreeItemSelect` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 14`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 24`, `import: 2`
* *Defense:* `safety: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` RecipeTreeViewController.generateTreeData, lwc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/AccountServiceLayer_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.77 IQR)
- **Top Global Matches:** file_cluster_13: 9.77, file_cluster_8: 9.928, file_cluster_16: 10.368
- **Magnitude:** 85.26 | **LOC:** 167 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5163%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `safelySaveNegative` (Impact: 10.2)
  * `testChangeShippingStreetNegativeNoEditAc` (Impact: 8.1)
  * `incrementDescriptionOnBulkAccountsNegati` (Impact: 7.8)
  * `safelySaveNegativeNoAccessException` (Impact: 7.8)
  * `Account` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 2`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `duplicate_logic: 8`, `orphaned_logic: 5`
* *Architecture:* `import: 47`
* *Defense:* `safety: 9`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Integration Recipes/CalloutRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.264 IQR)
- **Top Global Matches:** file_cluster_13: 9.264, file_cluster_8: 9.533, file_cluster_0: 9.901
- **Magnitude:** 81.3 | **LOC:** 413 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7636%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRawCalloutNegative` (Impact: 12.6)
  * `insertAccountAndContactsFromUntypedRespo` (Impact: 6.1)
  * `calloutWithUntypedResponsePositive` (Impact: 4.4)
  * `httpGetCalloutToSecondSalesforceOrgPosit` (Impact: 3.5)
  * `httpDeleteCalloutToSecondSalesforceOrgNe` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 13`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `import: 75`
* *Defense:* `safety: 5`, `doc: 4`, `test: 72`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/TestFactory.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.298 IQR)
- **Top Global Matches:** file_cluster_13: 12.298, file_cluster_16: 12.905, file_cluster_8: 12.945
- **Magnitude:** 69.34 | **LOC:** 319 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.4242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createSObject` (Impact: 7.9)
  * `invalidateSObjectList` (Impact: 7.6)
  * `createTestUser` (Impact: 6.1)
    * *Intent:* /**
  * `createMarketingUser` (Impact: 5.4)
    * *Intent:* /** * @description Creates a list of sObjects * @param sObj Type of sObjects to create * @param numb...
  * `createMinAccessUser` (Impact: 5.3)
    * *Intent:* /** * @description Create a single sObject
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 10`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `state_mutation: 29`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 4`, `import: 19`
* *Defense:* `safety: 2`, `doc: 29`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Platform Cache Recipes/PlatformCacheRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.515 IQR)
- **Top Global Matches:** file_cluster_13: 9.515, file_cluster_8: 9.558, file_cluster_0: 10.183
- **Magnitude:** 61.84 | **LOC:** 248 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRemoveKeyFromSessionCacheNegativeNoK` (Impact: 9.8)
  * `testRemoveKeyFromOrgCacheNegativeNoKey` (Impact: 9.8)
  * `testStoreValueInSessionCacheWithTTLPosit` (Impact: 3.6)
  * `testStoreValueInOrgCacheWithTTLPositive` (Impact: 3.6)
  * `testStoreValueInSessionCachePositive` (Impact: 3.5)
    * *Intent:* /** * @description This test class exists not only to test the Platform Cache
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 1`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 12`
* *Architecture:* `import: 56`
* *Defense:* `safety: 4`, `doc: 2`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/CollectionUtils_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.385 IQR)
- **Top Global Matches:** file_cluster_13: 9.385, file_cluster_8: 9.735, file_cluster_16: 9.831
- **Magnitude:** 60.78 | **LOC:** 143 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0154%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMapFromCollectionWithListOfValuesPos` (Impact: 11.6)
  * `testDemonstrateIdMapFromCollectionByKeyP` (Impact: 9.3)
  * `Contact` (Impact: 8.7)
  * `testDemonstrateStringMapFromCollectionBy` (Impact: 8.4)
  * `Contact` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 1`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 4`, `orphaned_logic: 3`
* *Architecture:* `import: 43`
* *Defense:* `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Platform Event Recipes/PlatformEventRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.631 IQR)
- **Top Global Matches:** file_cluster_13: 10.631, file_cluster_8: 11.094, file_cluster_0: 11.278
- **Magnitude:** 58.58 | **LOC:** 180 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testEventPublishNegativeMinAccessUser` (Impact: 12.7)
  * `testEventPublishCallbackFailsWhenNoEvent` (Impact: 10.2)
  * `testEventPublishCallbackFailure` (Impact: 4.1)
  * `testEventPublishCallbackSuccess` (Impact: 4.0)
  * `testEventPublishPositive` (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 1`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `import: 47`
* *Defense:* `safety: 7`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.726 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.057 IQR)
- **Top Global Matches:** file_cluster_4: 12.726, file_cluster_13: 12.948, file_cluster_0: 12.999
- **Magnitude:** 54.84 | **LOC:** 105 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `renderedCallback` (Impact: 9.7)
  * `loadScript` (Impact: 2.4)
  * `loadDocumentation` (Impact: 2.0)
  * `recipeName` (Impact: 1.9)
  * `recipeName` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 4`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` platformResourceLoader, documentation, lwc, highlight, markdownIt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Files Recipes/FilesRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.204 IQR)
- **Top Global Matches:** file_cluster_13: 10.204, file_cluster_8: 10.733, file_cluster_0: 10.894
- **Magnitude:** 52.94 | **LOC:** 121 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2099%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Account` (Impact: 15.9)
  * `makeData` (Impact: 14.9)
  * `testGetFilteredAttachmentsForRecords` (Impact: 4.3)
  * `testPublishContent` (Impact: 3.6)
  * `testUploadFileFromText` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 1`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `import: 39`
* *Defense:* `safety: 6`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Security Recipes/CanTheUser_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.609 IQR)
- **Top Global Matches:** file_cluster_13: 9.609, file_cluster_8: 9.926, file_cluster_0: 10.147
- **Magnitude:** 52.28 | **LOC:** 167 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1481%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBulkFLSAccessibleWithAccountPositive` (Impact: 5.2)
  * `getBulkFLSUpdatableWithAccountPositive` (Impact: 5.2)
  * `getBulkFLSAccessibleWithAccountPositiveW` (Impact: 3.1)
  * `getBulkFLSUpdatableWithAccountPositiveWi` (Impact: 3.1)
  * `memoizedFLSMDCcomparesAccesibleToUpdatab` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 4`, `orphaned_logic: 15`
* *Architecture:* `import: 47`
* *Defense:* `safety: 1`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Integration Recipes/ApiServiceRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.902 IQR)
- **Top Global Matches:** file_cluster_13: 9.902, file_cluster_8: 10.275, file_cluster_0: 10.55
- **Magnitude:** 52.08 | **LOC:** 147 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testGetCurrentDataNegative500TriggersWhe` (Impact: 10.4)
  * `testGetCurrentDataNegativeJSONExceptionT` (Impact: 10.3)
  * `testGetCurrentDataNegative404` (Impact: 10.3)
  * `testGetCurrentDataPositive200` (Impact: 6.6)
  * `testConstructorAssignsNamedCredentialPos` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 5`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 5`
* *Architecture:* `import: 33`
* *Defense:* `safety: 6`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Testing Recipes/PSGAdvancedTestingRecipes.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.89 IQR)
- **Top Global Matches:** file_cluster_13: 9.89, file_cluster_8: 10.225, file_cluster_16: 10.437
- **Magnitude:** 51.7 | **LOC:** 107 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testNegativePSGTestsWithMetadata` (Impact: 13.9)
  * `getMapOfPSGResultMetadata` (Impact: 6.6)
  * `assignPermissionSetGroup` (Impact: 4.7)
  * `getPermissionSetGroups` (Impact: 4.6)
  * `assignPermissionSetGroup` (Impact: 4.0)
    * *Intent:* // assign current PSG to user /** * *** WARNING *** * This call to assignPermissionSetGroup does bot...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 3`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 16`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `import: 13`
* *Defense:* `safety: 2`, `doc: 1`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/RestClient_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.758 IQR)
- **Top Global Matches:** file_cluster_13: 8.758, file_cluster_8: 8.94, file_cluster_16: 9.44
- **Magnitude:** 49.36 | **LOC:** 267 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.4869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testStaticMakeApiCallFullParamsPositive` (Impact: 5.8)
  * `testStaticMakeApiCallNoHeadersoOrBodyPar` (Impact: 5.7)
  * `testStaticMakeApiCallNoHeadersoOrBodyOrQ` (Impact: 5.7)
  * `testGetWithPathAndQueryPositive` (Impact: 5.5)
  * `testPostWithPathQueryAndBodyPositive` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 10`
* *Architecture:* `io: 9`, `import: 41`
* *Defense:* `safety: 1`, `doc: 7`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/OrgShape_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.351 IQR)
- **Top Global Matches:** file_cluster_13: 9.351, file_cluster_8: 9.924, file_cluster_0: 9.997
- **Magnitude:** 47.1 | **LOC:** 202 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0972%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAdvancedMultiCurrencyManagement` (Impact: 7.7)
  * `testPlatformCacheDisabledWhenSeeAllDataT` (Impact: 5.4)
  * `testPlatformCachePositive` (Impact: 5.2)
  * `testGetSafeDefaultCachePartitionMemoized` (Impact: 5.1)
  * `testOrgShapeProperties` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 3`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 6`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `import: 73`
* *Defense:* `safety: 4`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Shared Code/TestDataHelpers.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.869 IQR)
- **Top Global Matches:** file_cluster_13: 12.869, file_cluster_16: 13.244, file_cluster_0: 13.317
- **Magnitude:** 41.58 | **LOC:** 58 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.4017%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `genXNumberOfAccounts` (Impact: 7.7)
  * `genAccountWithOptions` (Impact: 6.0)
  * `genContactForAccount` (Impact: 5.2)
  * `createAccount` (Impact: 1.9)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 4`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `orphaned_logic: 3`
* *Architecture:* `import: 5`
* *Defense:* `doc: 14`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Testing Recipes/StubbingRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.68 IQR)
- **Top Global Matches:** file_cluster_13: 8.68, file_cluster_8: 9.299, file_cluster_11: 9.475
- **Magnitude:** 38.04 | **LOC:** 164 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8464%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testThrowingPositive` (Impact: 10.4)
  * `testStubbedMethodWithParametersPositive` (Impact: 6.3)
  * `stubShouldReturnNonDefaultGreetingPositi` (Impact: 6.2)
  * `stubShouldReturnTruePositive` (Impact: 5.3)
  * `testStubbedOverloadedMethodsPositive` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 3`, `planned_debt: 12`, `orphaned_logic: 5`
* *Architecture:* `import: 51`
* *Defense:* `safety: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Email Recipes/InboundEmailHandlerRecipes_tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.666 IQR)
- **Top Global Matches:** file_cluster_13: 8.666, file_cluster_8: 9.069, file_cluster_0: 9.434
- **Magnitude:** 37.86 | **LOC:** 154 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleInboundEmailPositiveNewContactCrea` (Impact: 5.6)
  * `createEmail` (Impact: 5.4)
  * `createEnvelope` (Impact: 4.7)
  * `integrationTestPositive` (Impact: 4.1)
  * `createAttachment` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 6`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 8`, `import: 39`
* *Defense:* `safety: 1`, `doc: 1`, `test: 20`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` (JAVASCRIPT) | Magnitude: 6.26 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, decorators: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `force-app/tests/Async Apex Recipes/AtFutureRecipes_Tests.cls` (APEX) | Magnitude: 32.5 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, test: 18, doc: 9, decorators: 9
- `force-app/tests/Async Apex Recipes/QueueableChainingRecipes_Tests.cls` (APEX) | Magnitude: 10.02 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, test: 8, import: 8, sec_high_risk_execution: 6
- `force-app/tests/Platform Cache Recipes/PlatformCacheRecipes_Tests.cls` (APEX) | Magnitude: 61.84 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 219, import: 56, test: 53, sec_high_risk_execution: 32
- `force-app/tests/Data Recipes/MetadataCatalogRecipes_Tests.cls` (APEX) | Magnitude: 4.18 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, test: 5, sec_high_risk_execution: 5, decorators: 2
- `force-app/tests/Data Recipes/DynamicSOQLRecipes_Tests.cls` (APEX) | Magnitude: 33.34 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 139, test: 34, import: 31, sec_high_risk_execution: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `force-app/main/default/lwc/ldsUtils/ldsUtils.js` (JAVASCRIPT) | Magnitude: 17.96 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 11, branch: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT) | Magnitude: 54.84 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 26, structural_boundaries: 10, concurrency: 9
- `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT) | Magnitude: 115.28 | Delta: **0.277 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 65, concurrency: 18, branch: 15
- `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT) | Magnitude: 87.52 | Delta: **0.541 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 30, concurrency: 24, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `force-app/tests/LDV Recipes/LDVRecipes_Tests.cls` (APEX) | Magnitude: 12.78 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, import: 8, test: 5, sec_high_risk_execution: 3
- `force-app/tests/Shared Code/FormattedRecipeDisplayController_Tests.cls` (APEX) | Magnitude: 13.66 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, import: 15, sec_high_risk_execution: 12, test: 10
- `force-app/tests/DataWeaveInApex Recipes/CsvToJsonConversionRecipes_Tests.cls` (APEX) | Magnitude: 11.64 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, import: 29, test: 20, sec_high_risk_execution: 12
- `force-app/tests/Custom Metadata Recipes/CustomMetadataRecipes_Tests.cls` (APEX) | Magnitude: 14.6 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, import: 13, test: 12, sec_high_risk_execution: 10
- `force-app/tests/Shared Code/RecipeTreeViewController_Tests.cls` (APEX) | Magnitude: 9.54 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, import: 11, sec_high_risk_execution: 10, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `force-app/main/default/triggers/AccountTrigger.trigger` (APEX) | Magnitude: 10.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 9, state_mutation: 6, args: 3, func_start: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `force-app/main/default/lwc/ldsUtils/ldsUtils.js` -> **Severity: 179.445** (Blast Radius: 5.233 * Doc Risk: 34.2911%)
- `bin/generate-apex-docs.sh` -> **Severity: 150.763** (Blast Radius: 2.828 * Doc Risk: 53.3107%)
- `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` -> **Severity: 143.136** (Blast Radius: 2.828 * Doc Risk: 50.6139%)
- `force-app/main/default/triggers/AccountTrigger.trigger` -> **Severity: 96.174** (Blast Radius: 2.828 * Doc Risk: 34.0079%)
- `force-app/main/default/lwc/apexRecipesContainer/apexRecipesContainer.js` -> **Severity: 95.511** (Blast Radius: 2.828 * Doc Risk: 33.7734%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
