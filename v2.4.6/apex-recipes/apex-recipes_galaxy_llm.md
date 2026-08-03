# ARCHITECTURAL_BRIEF: apex-recipes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/apex-recipes` |
| **Timestamp** | `2026-08-03T19:24:19.799127+00:00` |
| **Scan Duration** | `0.7s` |
| **Git Branch** | `main` |
| **Git Commit** | `3462c7d4bd72998b97da95bd613913a944c4bc0d` |
| **Git Remote** | `https://github.com/trailheadapps/apex-recipes` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 79 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 98.9 | 5.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.2 | 0.2 | 0.0 |
| API Exposure | 0.0 | 6.0 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 39.2 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 9.6 | 6.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `deepClone` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **123.3** | LOC: 41
  * *Intent:* /** * A namespace for utility methods. * * All function in this namespace that are not explicitly marked as _public_ are for __internal use only__ and...
- `currentScript` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> Impact: **120.6** | LOC: 125
  * *Intent:* /** * Creates a deep clone of the given object.
- `testNegativePSGTestsWithMetadata` (@ `force-app/tests/Testing Recipes/PSGAdvancedTestingRecipes.cls`) -> Impact: **81.0** | LOC: 54
- `testStripInaccessibleFromSubQueryMinAcce` (@ `force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls`) -> Impact: **65.2** | LOC: 52
- `toggleExpandNode` (@ `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js`) -> Impact: **52.7** | LOC: 14
- `testStripInaccessibleFromQueryMinAccessW` (@ `force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls`) -> Impact: **49.0** | LOC: 40
- `reduceErrors` (@ `force-app/main/default/lwc/ldsUtils/ldsUtils.js`) -> Impact: **43.2** | LOC: 32
  * *Intent:* /**
- `isTreeNode` (@ `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js`) -> Impact: **42.2** | LOC: 12
- `testQueryWithFilterNegativeNoPermsToAcco` (@ `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls`) -> Impact: **41.1** | LOC: 39
- `testEventPublishNegativeMinAccessUser` (@ `force-app/tests/Platform Event Recipes/PlatformEventRecipes_Tests.cls`) -> Impact: **40.7** | LOC: 31

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `deepClone` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * A namespace for utility methods. * * All function in this namespace that are not explicitly marked as _public_ are for __internal use only__ and...
- `testNegativePSGTestsWithMetadata` (@ `force-app/tests/Testing Recipes/PSGAdvancedTestingRecipes.cls`) -> **O(2^N) [Recursive]**
- `toggleExpandNode` (@ `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js`) -> **O(2^N) [Recursive]**
- `HttpCalloutMockFactory` (@ `force-app/tests/Shared Code/HttpCalloutMockFactory.cls`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `isTreeNode` (@ `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js`) -> **O(2^N) [Recursive]**
- `basicSOSLSearch` (@ `force-app/tests/Data Recipes/SOSLRecipes_Tests.cls`) -> **O(2^N) [Recursive]**
- `createTestUser` (@ `force-app/tests/Shared Code/TestFactory.cls`) -> **O(2^N) [Recursive]**
- `currentScript` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Creates a deep clone of the given object.
- `encode` (@ `force-app/main/default/staticresources/highlight/prism.js`) -> **O(2^N) [Recursive]**
- `testQueryWithFilterNegativeNoPermsToAcco` (@ `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `integrationTestPositive` (@ `force-app/tests/Email Recipes/InboundEmailHandlerRecipes_tests.cls`) -> DB Complexity: **15**
- `createTestUser` (@ `force-app/tests/Shared Code/TestFactory.cls`) -> DB Complexity: **12**
  * *Intent:* /**
- `testRecalculatePSG` (@ `force-app/tests/Testing Recipes/PSGTestingRecipes.cls`) -> DB Complexity: **12**
- `testDoQueryThrowsRemovedFieldsException` (@ `force-app/tests/Security Recipes/Safely_Tests.cls`) -> DB Complexity: **11**
- `testDoUpdateNegative` (@ `force-app/tests/Security Recipes/Safely_Tests.cls`) -> DB Complexity: **11**
- `handleTreeItemSelect` (@ `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js`) -> DB Complexity: **10**
- `httpPatchUpdateAccountRecordsPositive` (@ `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls`) -> DB Complexity: **10**
- `testPublishContent` (@ `force-app/tests/Files Recipes/FilesRecipes_Tests.cls`) -> DB Complexity: **9**
- `testDoUpsertMethodsNegative` (@ `force-app/tests/Security Recipes/Safely_Tests.cls`) -> DB Complexity: **9**
- `generateHttpResponse` (@ `force-app/tests/Shared Code/HttpCalloutMockFactory.cls`) -> DB Complexity: **9**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `force-app/tests/Data Recipes` | 10 | 1053.6 | 5.29% | 0.0% |
| `force-app/tests/Shared Code` | 30 | 959.28 | 6.05% | 0.0% |
| `force-app/tests/Security Recipes` | 6 | 762.12 | 6.53% | 0.0% |
| `force-app/tests/Integration Recipes` | 10 | 574.16 | 4.64% | 0.0% |
| `force-app/main/default/staticresources/highlight` | 2 | 332.64 | 6.11% | 20.08% |
| `force-app/tests/Testing Recipes` | 8 | 291.2 | 6.56% | 0.0% |
| `force-app/main/default/staticresources/documentation` | 73 | 287.04 | 0.0% | 0.0% |
| `force-app/tests/Async Apex Recipes` | 14 | 256.32 | 9.54% | 0.0% |
| `force-app/tests/Trigger Recipes` | 4 | 227.4 | 6.49% | 0.0% |
| `force-app/tests/DataWeaveInApex Recipes` | 13 | 218.32 | 5.45% | 0.0% |

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
- `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` -> **19** Orphaned Functions | **3** Duplicates
- `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls` -> **18** Orphaned Functions | **0** Duplicates
- `force-app/tests/Security Recipes/Safely_Tests.cls` -> **16** Orphaned Functions | **0** Duplicates
- `force-app/tests/Security Recipes/CanTheUser_Tests.cls` -> **15** Orphaned Functions | **0** Duplicates

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

### Exploit Generation Surface
- `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` -> **100.0%** Exposure
- `force-app/main/default/staticresources/highlight/prism.js` -> **100.0%** Exposure
- `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` -> **100.0%** Exposure
- `force-app/tests/Data Recipes/DynamicSOQLRecipes_Tests.cls` -> **100.0%** Exposure
- `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` -> **100.0%** Exposure
- `force-app/tests/Data Recipes/DynamicSOQLRecipes_Tests.cls` -> **100.0%** Exposure
- `force-app/tests/Email Recipes/InboundEmailHandlerRecipes_tests.cls` -> **100.0%** Exposure
- `force-app/tests/Integration Recipes/CustomRestEndpointRecipes_Tests.cls` -> **100.0%** Exposure
- `force-app/tests/Shared Code/ApexClassUtilities_Tests.cls` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` -> **100.0%** Exposure
- `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` -> **100.0%** Exposure
- `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` -> **100.0%** Exposure
- `force-app/tests/Security Recipes/Safely_Tests.cls` -> **100.0%** Exposure
- `force-app/tests/Data Recipes/SOQLRecipes_Tests.cls` -> **99.9998%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `21` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT) -> Cumulative Risk: **934.02**
- **Archetype:** `file_cluster_4` (Distance: 12.93 IQR)
- **Magnitude:** 155.38 | **LOC:** 93 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `extractDescription` (Impact: 22.2), `loadPrism` (Impact: 18.0), `highlightCodeSegment` (Impact: 14.7)

### 2. `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT) -> Cumulative Risk: **910.27**
- **Archetype:** `file_cluster_4` (Distance: 12.549 IQR)
- **Magnitude:** 169.82 | **LOC:** 66 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `toggleExpandNode` (Impact: 52.7), `isTreeNode` (Impact: 42.2), `connectedCallback` (Impact: 10.7)

### 3. `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT) -> Cumulative Risk: **832.45**
- **Archetype:** `file_cluster_4` (Distance: 12.737 IQR)
- **Magnitude:** 69.74 | **LOC:** 105 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `renderedCallback` (Impact: 22.7), `loadDocumentation` (Impact: 4.6), `recipeName` (Impact: 2.8)

### 4. `force-app/main/default/lwc/errorPanel/errorPanel.js` (JAVASCRIPT) -> Cumulative Risk: **502.95**
- **Archetype:** `file_cluster_13` (Distance: 12.236 IQR)
- **Magnitude:** 16.8 | **LOC:** 29 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.994%), Algorithmic Dos (94.8425%)
- **Heaviest Functions:** `render` (Impact: 4.4), `errorMessages` (Impact: 2.7), `handleShowDetailsClick` (Impact: 2.3)

### 5. `force-app/main/default/triggers/AccountTrigger.trigger` (APEX) -> Cumulative Risk: **490.78**
- **Archetype:** `file_cluster_9` (Distance: 18.809 IQR)
- **Magnitude:** 10.14 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Safety Score (98.8513%), Spec Match (80.0%)
- **Heaviest Functions:** `AccountTrigger` (Impact: 3.9)

### 6. `bin/install-scratch.sh` (SHELL) -> Cumulative Risk: **450.48**
- **Archetype:** `file_cluster_8` (Distance: 9.903 IQR)
- **Magnitude:** 31.36 | **LOC:** 53 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.8356%), State Flux (95.9424%), Safety Score (80.0%)
- **Heaviest Functions:** `__global_context__` (Impact: 21.4), `Anonymous_Block` (Impact: 4.2)

### 7. `force-app/tests/Testing Recipes/PSGAdvancedTestingRecipes.cls` (APEX) -> Cumulative Risk: **441.18**
- **Archetype:** `file_cluster_13` (Distance: 9.925 IQR)
- **Magnitude:** 135.7 | **LOC:** 107 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Algorithmic Dos (99.9991%)
- **Heaviest Functions:** `testNegativePSGTestsWithMetadata` (Impact: 81.0), `getMapOfPSGResultMetadata` (Impact: 18.3), `assignPermissionSetGroup` (Impact: 11.6)

### 8. `bin/generate-apex-docs.sh` (SHELL) -> Cumulative Risk: **438.28**
- **Archetype:** `file_cluster_8` (Distance: 11.474 IQR)
- **Magnitude:** 12.54 | **LOC:** 27 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (99.9629%), Spec Match (80.0%), Documentation (79.5515%)
- **Heaviest Functions:** `__global_context__` (Impact: 9.3)

### 9. `force-app/main/default/staticresources/highlight/prism.js` (JAVASCRIPT) -> Cumulative Risk: **423.44**
- **Archetype:** `file_cluster_8` (Distance: 9.771 IQR)
- **Magnitude:** 332.38 | **LOC:** 2050 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Verification (80.0%), Safety Score (63.5775%)
- **Heaviest Functions:** `deepClone` (Impact: 123.3), `currentScript` (Impact: 120.6), `encode` (Impact: 18.1)

### 10. `force-app/tests/Email Recipes/InboundEmailHandlerRecipes_tests.cls` (APEX) -> Cumulative Risk: **413.58**
- **Archetype:** `file_cluster_13` (Distance: 8.53 IQR)
- **Magnitude:** 51.06 | **LOC:** 154 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Algorithmic Dos (98.393%)
- **Heaviest Functions:** `createAttachment` (Impact: 13.6), `handleInboundEmailPositiveNewContactCrea` (Impact: 10.1), `integrationTestPositive` (Impact: 7.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `force-app/tests/Data Recipes/DMLRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.59 IQR)
- **Top Global Matches:** file_cluster_13: 11.59, file_cluster_8: 12.098, file_cluster_0: 12.122
- **Magnitude:** 647.24 | **LOC:** 825 | **CtrlFlow:** 98.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (6.9449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDeleteAccountViaKeywordInSystemModeP` (Impact: 27.9 | O(N^5) | DB: 4)
  * `testDeleteAccountViaDatabaseMethodInUser` (Impact: 27.9 | O(N^5) | DB: 4)
  * `testDeleteAccountViaDatabaseMethodInSyst` (Impact: 27.9 | O(N^5) | DB: 4)
  * `testDeleteAccountViaKeywordInUserModePos` (Impact: 27.8 | O(N^5) | DB: 4)
  * `testUpsertAccountViaUpsertKeywordInSyste` (Impact: 21.0 | O(N^5))
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

### `force-app/tests/Security Recipes/StripInaccessibleRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.978 IQR)
- **Top Global Matches:** file_cluster_13: 10.978, file_cluster_8: 11.432, file_cluster_0: 11.63
- **Magnitude:** 350.54 | **LOC:** 373 | **CtrlFlow:** 96.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (8.5887%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testStripInaccessibleFromSubQueryMinAcce` (Impact: 65.2 | O(N^6) | DB: 4)
  * `testStripInaccessibleFromQueryMinAccessW` (Impact: 49.0 | O(N^6) | DB: 3)
  * `testStripInaccessibleBeforeDMLMinAccessP` (Impact: 34.9 | O(N^5) | DB: 1)
  * `testStripInaccessibleFromUntrustedDataNe` (Impact: 28.4 | O(N^5) | DB: 1)
  * `testStripInaccessibleFromQueryNegative` (Impact: 28.0 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 1`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `duplicate_logic: 4`, `orphaned_logic: 7`
* *Architecture:* `io: 3`, `import: 97`
* *Defense:* `safety: 13`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/staticresources/highlight/prism.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.771 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.844 IQR)
- **Top Global Matches:** file_cluster_8: 9.771, file_cluster_7: 10.173, file_cluster_1: 10.467
- **Magnitude:** 332.38 | **LOC:** 2050 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (6.0718%), Tech Debt (12.4493%)
**Top Internal Functions/Classes:**
  * `deepClone` (Impact: 123.3 | O(2^N) | DB: 2)
    * *Intent:* /** * A namespace for utility methods. * * All function in this namespace that are not explicitly ma...
  * `currentScript` (Impact: 120.6 | O(2^N) | DB: 6)
    * *Intent:* /** * Creates a deep clone of the given object.
  * `encode` (Impact: 18.1 | O(2^N))
  * `getLanguage` (Impact: 9.3 | O(N^1))
    * *Intent:* /**
  * `objId` (Impact: 3.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 28`, `args: 11`, `func_start: 11`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 1`, `state_mutation: 39`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 11`, `doc: 58`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Security Recipes/Safely_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.243 IQR)
- **Top Global Matches:** file_cluster_13: 11.243, file_cluster_8: 11.728, file_cluster_0: 11.863
- **Magnitude:** 285.44 | **LOC:** 419 | **CtrlFlow:** 93.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (9.6632%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMarketingProfileGeneratesInsertExcep` (Impact: 32.7 | O(N^6) | DB: 3)
  * `testMarketingProfileGeneratesUpdateExcep` (Impact: 32.6 | O(N^6) | DB: 2)
  * `testMarketingProfileGeneratesUpsertExcep` (Impact: 32.6 | O(N^6) | DB: 2)
  * `testDoQueryThrowsRemovedFieldsException` (Impact: 29.1 | O(N^5) | DB: 11)
  * `testDoUpsertMethodsNoThrowPositive` (Impact: 24.2 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 1`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 61`, `orphaned_logic: 16`
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
- **Magnitude:** 272.82 | **LOC:** 526 | **CtrlFlow:** 92.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (11.0655%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testQueryWithFilterNegativeNoPermsToAcco` (Impact: 41.1 | O(N^6) | DB: 5)
  * `testGetAccountsAndContactsPositive` (Impact: 35.6 | O(N^5) | DB: 3)
  * `testProfileDeniesAccountAccessNegative` (Impact: 32.6 | O(N^6) | DB: 1)
  * `testgetSumOfOpportunityRecordsPositive` (Impact: 14.8 | O(N^5) | DB: 8)
  * `testGetAccountFilterByStatePositive` (Impact: 10.2 | O(N^3) | DB: 1)
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
- **Global Archetype:** `file_cluster_13` (Drift: 10.646 IQR)
- **Top Global Matches:** file_cluster_13: 10.646, file_cluster_8: 11.269, file_cluster_0: 11.373
- **Magnitude:** 215.7 | **LOC:** 691 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (6.5798%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `httpPatchUpdateAccountRecordsPositive` (Impact: 15.7 | O(N^3) | DB: 10)
  * `httpPatchUpdateAccountRecordsNegativeNoA` (Impact: 11.1 | O(N^3) | DB: 6)
  * `httpPatchUpdateAccountRecordsNegativeCat` (Impact: 10.9 | O(N^3) | DB: 6)
  * `httpPutUpsertContactRecordsNegativeMinAc` (Impact: 10.7 | O(N^3) | DB: 1)
  * `httpPatchUpdateAccountRecordsNegativeJSO` (Impact: 10.7 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 3`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 36`, `dead_code: 2`, `duplicate_logic: 3`, `orphaned_logic: 19`
* *Architecture:* `io: 8`, `import: 249`
* *Defense:* `safety: 8`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.549 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.867 IQR)
- **Top Global Matches:** file_cluster_4: 12.549, file_cluster_13: 13.09, file_cluster_0: 13.217
- **Magnitude:** 169.82 | **LOC:** 66 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `toggleExpandNode` (Impact: 52.7 | O(2^N) | DB: 2)
  * `isTreeNode` (Impact: 42.2 | O(2^N) | DB: 2)
  * `connectedCallback` (Impact: 10.7 | O(N^3) | DB: 2)
  * `handleTreeItemSelect` (Impact: 8.1 | O(N^4) | DB: 10)
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

### `force-app/tests/Trigger Recipes/AccountTriggerHandler_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.407 IQR)
- **Top Global Matches:** file_cluster_13: 10.407, file_cluster_8: 10.798, file_cluster_0: 10.99
- **Magnitude:** 157.18 | **LOC:** 272 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (6.5645%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBeforeUpdateWithAddErrorNegative` (Impact: 24.6 | O(N^6) | DB: 2)
  * `afterUpdateTestNegativeDMLException` (Impact: 23.5 | O(N^4) | DB: 2)
  * `afterUpdateTestPositive` (Impact: 18.5 | O(N^4) | DB: 4)
  * `testAfterInsertPositive` (Impact: 12.7 | O(N^4) | DB: 3)
  * `testBeforeUpdatePositive` (Impact: 12.7 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 5`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 24`, `orphaned_logic: 9`
* *Architecture:* `io: 8`, `import: 49`
* *Defense:* `safety: 7`, `doc: 3`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.93 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.003 IQR)
- **Top Global Matches:** file_cluster_4: 12.93, file_cluster_0: 13.209, file_cluster_13: 13.266
- **Magnitude:** 155.38 | **LOC:** 93 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (95.6166%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `extractDescription` (Impact: 22.2 | O(N^5) | DB: 3)
  * `loadPrism` (Impact: 18.0 | O(N^5) | DB: 7)
  * `highlightCodeSegment` (Impact: 14.7 | O(N^4) | DB: 6)
  * `githubUrl` (Impact: 7.4 | O(N^3) | DB: 5)
  * `renderedCallback` (Impact: 2.3 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 12`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` highlight, FormattedRecipeDisplayController.getRecipeCode, platformResourceLoader, lwc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Integration Recipes/CalloutRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.264 IQR)
- **Top Global Matches:** file_cluster_13: 9.264, file_cluster_8: 9.533, file_cluster_0: 9.901
- **Magnitude:** 135.7 | **LOC:** 413 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.0012%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRawCalloutNegative` (Impact: 35.0 | O(N^5) | DB: 1)
  * `insertAccountAndContactsFromUntypedRespo` (Impact: 10.5 | O(N^3) | DB: 6)
  * `calloutWithUntypedResponsePositive` (Impact: 6.7 | O(N^3))
  * `httpGetCalloutToSecondSalesforceOrgPosit` (Impact: 5.8 | O(N^3))
  * `httpDeleteCalloutToSecondSalesforceOrgNe` (Impact: 5.8 | O(N^3) | DB: 2)
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

### `force-app/tests/Testing Recipes/PSGAdvancedTestingRecipes.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.925 IQR)
- **Top Global Matches:** file_cluster_13: 9.925, file_cluster_8: 10.244, file_cluster_16: 10.455
- **Magnitude:** 135.7 | **LOC:** 107 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (16.1498%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testNegativePSGTestsWithMetadata` (Impact: 81.0 | O(2^N) | DB: 1)
  * `getMapOfPSGResultMetadata` (Impact: 18.3 | O(N^4) | DB: 4)
  * `assignPermissionSetGroup` (Impact: 11.6 | O(N^5) | DB: 9)
  * `getPermissionSetGroups` (Impact: 6.9 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 3`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 16`
* *Architecture:* `io: 3`, `import: 13`
* *Defense:* `safety: 2`, `doc: 1`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Platform Cache Recipes/PlatformCacheRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.515 IQR)
- **Top Global Matches:** file_cluster_13: 9.515, file_cluster_8: 9.558, file_cluster_0: 10.183
- **Magnitude:** 124.54 | **LOC:** 248 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.8875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRemoveKeyFromSessionCacheNegativeNoK` (Impact: 23.2 | O(N^4) | DB: 1)
  * `testRemoveKeyFromOrgCacheNegativeNoKey` (Impact: 23.2 | O(N^4) | DB: 1)
  * `testStoreValueInSessionCacheWithTTLPosit` (Impact: 8.1 | O(N^5))
  * `testStoreValueInOrgCacheWithTTLPositive` (Impact: 8.1 | O(N^5))
  * `testStoreValueInSessionCachePositive` (Impact: 8.0 | O(N^5))
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

### `force-app/tests/Shared Code/TestFactory.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.298 IQR)
- **Top Global Matches:** file_cluster_13: 12.298, file_cluster_16: 12.905, file_cluster_8: 12.945
- **Magnitude:** 114.94 | **LOC:** 319 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (14.4242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createSObject` (Impact: 18.9 | O(N^4) | DB: 1)
  * `invalidateSObjectList` (Impact: 15.0 | O(N^3) | DB: 1)
  * `createTestUser` (Impact: 14.3 | O(2^N) | DB: 3)
  * `createTestUser` (Impact: 11.3 | O(N^3) | DB: 12)
    * *Intent:* /**
  * `createMarketingUser` (Impact: 10.3 | O(N^3) | DB: 3)
    * *Intent:* /** * @description Creates a list of sObjects * @param sObj Type of sObjects to create * @param numb...
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

### `force-app/tests/Shared Code/AccountServiceLayer_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.79 IQR)
- **Top Global Matches:** file_cluster_13: 9.79, file_cluster_8: 9.934, file_cluster_16: 10.373
- **Magnitude:** 112.66 | **LOC:** 167 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.5163%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testChangeShippingStreetNegativeNoEditAc` (Impact: 21.5 | O(N^5))
  * `safelySaveNegativeNoAccessException` (Impact: 21.2 | O(N^5))
  * `safelySaveNegative` (Impact: 19.1 | O(N^3))
  * `incrementDescriptionOnBulkAccountsNegati` (Impact: 17.8 | O(N^4))
  * `incrementDescriptionOnBulkAccountsPositi` (Impact: 12.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 2`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `import: 47`
* *Defense:* `safety: 9`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Platform Event Recipes/PlatformEventRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.631 IQR)
- **Top Global Matches:** file_cluster_13: 10.631, file_cluster_8: 11.094, file_cluster_0: 11.278
- **Magnitude:** 111.28 | **LOC:** 180 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (7.3819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testEventPublishNegativeMinAccessUser` (Impact: 40.7 | O(N^6) | DB: 3)
  * `testEventPublishCallbackFailsWhenNoEvent` (Impact: 23.6 | O(N^4) | DB: 4)
  * `testEventPublishCallbackFailure` (Impact: 7.5 | O(N^4) | DB: 4)
  * `testEventPublishCallbackSuccess` (Impact: 7.4 | O(N^4) | DB: 4)
  * `testEventPublishPositive` (Impact: 5.6 | O(N^3) | DB: 3)
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

### `force-app/tests/Integration Recipes/ApiServiceRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.902 IQR)
- **Top Global Matches:** file_cluster_13: 9.902, file_cluster_8: 10.275, file_cluster_0: 10.55
- **Magnitude:** 110.28 | **LOC:** 147 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.8822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testGetCurrentDataNegative500TriggersWhe` (Impact: 28.3 | O(N^5) | DB: 1)
  * `testGetCurrentDataNegativeJSONExceptionT` (Impact: 28.2 | O(N^5) | DB: 1)
  * `testGetCurrentDataNegative404` (Impact: 23.7 | O(N^4) | DB: 1)
  * `testGetCurrentDataPositive200` (Impact: 13.3 | O(N^4))
  * `testConstructorAssignsNamedCredentialPos` (Impact: 5.1 | O(N^3))
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

### `force-app/tests/Security Recipes/CanTheUser_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.609 IQR)
- **Top Global Matches:** file_cluster_13: 9.609, file_cluster_8: 9.926, file_cluster_0: 10.147
- **Magnitude:** 94.58 | **LOC:** 167 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.9359%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBulkFLSAccessibleWithAccountPositive` (Impact: 11.9 | O(N^4))
  * `getBulkFLSUpdatableWithAccountPositive` (Impact: 11.9 | O(N^4))
  * `getBulkFLSAccessibleWithAccountPositiveW` (Impact: 5.4 | O(N^3))
  * `getBulkFLSUpdatableWithAccountPositiveWi` (Impact: 5.4 | O(N^3))
  * `memoizedFLSMDCcomparesAccesibleToUpdatab` (Impact: 5.1 | O(N^3))
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

### `force-app/tests/Shared Code/RestClient_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.758 IQR)
- **Top Global Matches:** file_cluster_13: 8.758, file_cluster_8: 8.94, file_cluster_16: 9.44
- **Magnitude:** 80.56 | **LOC:** 267 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (2.4869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testStaticMakeApiCallFullParamsPositive` (Impact: 10.3 | O(N^3) | DB: 3)
  * `testStaticMakeApiCallNoHeadersoOrBodyPar` (Impact: 10.2 | O(N^3) | DB: 3)
  * `testStaticMakeApiCallNoHeadersoOrBodyOrQ` (Impact: 10.1 | O(N^3) | DB: 3)
  * `testGetWithPathAndQueryPositive` (Impact: 10.0 | O(N^3) | DB: 3)
  * `testPostWithPathQueryAndBodyPositive` (Impact: 5.7 | O(N^3) | DB: 3)
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
- **Magnitude:** 77.9 | **LOC:** 202 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (4.5227%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAdvancedMultiCurrencyManagement` (Impact: 14.4 | O(N^3) | DB: 1)
  * `testPlatformCacheDisabledWhenSeeAllDataT` (Impact: 10.3 | O(N^3))
  * `testPlatformCachePositive` (Impact: 9.6 | O(N^3))
  * `testGetSafeDefaultCachePartitionMemoized` (Impact: 9.6 | O(N^3))
  * `testCacheIsUsedPositive` (Impact: 7.2 | O(N^4) | DB: 1)
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

### `force-app/tests/Testing Recipes/StubbingRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.68 IQR)
- **Top Global Matches:** file_cluster_13: 8.68, file_cluster_8: 9.299, file_cluster_11: 9.475
- **Magnitude:** 77.14 | **LOC:** 164 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (4.42%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testThrowingPositive` (Impact: 28.3 | O(N^5) | DB: 1)
  * `testStubbedMethodWithParametersPositive` (Impact: 13.0 | O(N^4))
  * `stubShouldReturnNonDefaultGreetingPositi` (Impact: 12.9 | O(N^4))
  * `stubShouldReturnTruePositive` (Impact: 9.8 | O(N^3))
  * `testStubbedOverloadedMethodsPositive` (Impact: 7.5 | O(N^4))
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

### `force-app/tests/Shared Code/CollectionUtils_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.439 IQR)
- **Top Global Matches:** file_cluster_13: 9.439, file_cluster_8: 9.768, file_cluster_16: 9.864
- **Magnitude:** 76.78 | **LOC:** 143 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.0154%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMapFromCollectionWithListOfValuesPos` (Impact: 29.5 | O(N^5) | DB: 2)
  * `testDemonstrateIdMapFromCollectionByKeyP` (Impact: 19.3 | O(N^4))
  * `testDemonstrateStringMapFromCollectionBy` (Impact: 18.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 1`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `orphaned_logic: 3`
* *Architecture:* `import: 43`
* *Defense:* `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.737 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.057 IQR)
- **Top Global Matches:** file_cluster_4: 12.737, file_cluster_13: 12.958, file_cluster_0: 13.009
- **Magnitude:** 69.74 | **LOC:** 105 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `renderedCallback` (Impact: 22.7 | O(N^4) | DB: 7)
  * `loadDocumentation` (Impact: 4.6 | O(N^4) | DB: 2)
  * `recipeName` (Impact: 2.8 | O(N^2) | DB: 2)
  * `recipeName` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 4`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` platformResourceLoader, lwc, markdownIt, documentation, highlight
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `force-app/tests/Files Recipes/FilesRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.198 IQR)
- **Top Global Matches:** file_cluster_13: 10.198, file_cluster_8: 10.727, file_cluster_0: 10.888
- **Magnitude:** 63.74 | **LOC:** 121 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (8.677%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeData` (Impact: 35.0 | O(N^4) | DB: 6)
  * `testGetFilteredAttachmentsForRecords` (Impact: 6.5 | O(N^3) | DB: 3)
  * `testPublishContent` (Impact: 5.8 | O(N^3) | DB: 9)
  * `testUploadFileFromText` (Impact: 5.3 | O(N^3) | DB: 6)
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

### `force-app/tests/Shared Code/TestDataHelpers.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.869 IQR)
- **Top Global Matches:** file_cluster_13: 12.869, file_cluster_16: 13.244, file_cluster_0: 13.317
- **Magnitude:** 62.38 | **LOC:** 58 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.4017%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `genXNumberOfAccounts` (Impact: 15.0 | O(N^3) | DB: 1)
  * `genAccountWithOptions` (Impact: 13.8 | O(N^4) | DB: 3)
  * `genContactForAccount` (Impact: 10.1 | O(N^3) | DB: 3)
  * `createAccount` (Impact: 2.7 | O(N^2) | DB: 1)
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

### `force-app/tests/Async Apex Recipes/AtFutureRecipes_Tests.cls` (APEX | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.505 IQR)
- **Top Global Matches:** file_cluster_13: 9.505, file_cluster_8: 9.532, file_cluster_0: 9.829
- **Magnitude:** 58.5 | **LOC:** 90 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.4537%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `callAtFutureCalloutPositive` (Impact: 35.8 | O(N^3))
  * `callAtFutureMethodWithCalloutNegative` (Impact: 14.4 | O(N^3))
    * *Intent:* /** * This is where you should have a system.assert* call. However,This test features a 'silent asse...
  * `callBasicAtFutureMethodTestPositive` (Impact: 5.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 4`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 3`
* *Architecture:* `concurrency: 2`, `import: 9`
* *Defense:* `safety: 1`, `doc: 9`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.828
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` (JAVASCRIPT) | Magnitude: 7.06 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, decorators: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `force-app/tests/Async Apex Recipes/AtFutureRecipes_Tests.cls` (APEX) | Magnitude: 58.5 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, test: 18, doc: 9, decorators: 9
- `force-app/tests/Async Apex Recipes/QueueableChainingRecipes_Tests.cls` (APEX) | Magnitude: 20.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, test: 8, import: 8, sec_high_risk_execution: 6
- `force-app/tests/Platform Cache Recipes/PlatformCacheRecipes_Tests.cls` (APEX) | Magnitude: 124.54 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 219, import: 56, test: 53, sec_high_risk_execution: 32
- `force-app/tests/Data Recipes/MetadataCatalogRecipes_Tests.cls` (APEX) | Magnitude: 6.38 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, test: 5, sec_high_risk_execution: 5, decorators: 2
- `force-app/tests/Data Recipes/DynamicSOQLRecipes_Tests.cls` (APEX) | Magnitude: 52.44 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 139, test: 34, import: 31, sec_high_risk_execution: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `force-app/main/default/lwc/ldsUtils/ldsUtils.js` (JAVASCRIPT) | Magnitude: 45.66 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 11, branch: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` (JAVASCRIPT) | Magnitude: 69.74 | Delta: **0.221 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 26, structural_boundaries: 10, concurrency: 9
- `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` (JAVASCRIPT) | Magnitude: 155.38 | Delta: **0.279 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 69, concurrency: 18, branch: 15
- `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` (JAVASCRIPT) | Magnitude: 169.82 | Delta: **0.541 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 30, concurrency: 24, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `force-app/tests/LDV Recipes/LDVRecipes_Tests.cls` (APEX) | Magnitude: 15.48 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, import: 8, test: 5, sec_high_risk_execution: 3
- `force-app/tests/Shared Code/FormattedRecipeDisplayController_Tests.cls` (APEX) | Magnitude: 33.56 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, import: 15, sec_high_risk_execution: 12, test: 10
- `force-app/tests/DataWeaveInApex Recipes/CsvToJsonConversionRecipes_Tests.cls` (APEX) | Magnitude: 18.34 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, import: 29, test: 20, sec_high_risk_execution: 12
- `force-app/tests/Custom Metadata Recipes/CustomMetadataRecipes_Tests.cls` (APEX) | Magnitude: 21.7 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, import: 13, test: 12, sec_high_risk_execution: 10
- `force-app/tests/Shared Code/RecipeTreeViewController_Tests.cls` (APEX) | Magnitude: 22.94 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
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

- `force-app/main/default/lwc/ldsUtils/ldsUtils.js` -> **Severity: 328.585** (Blast Radius: 5.233 * Doc Risk: 62.791%)
- `force-app/main/default/lwc/recipeTreeView/recipeTreeView.js` -> **Severity: 282.8** (Blast Radius: 2.828 * Doc Risk: 99.9999%)
- `force-app/main/default/lwc/formattedRecipeDisplay/formattedRecipeDisplay.js` -> **Severity: 282.773** (Blast Radius: 2.828 * Doc Risk: 99.9906%)
- `force-app/main/default/lwc/formattedDocsViewer/formattedDocsViewer.js` -> **Severity: 281.238** (Blast Radius: 2.828 * Doc Risk: 99.4477%)
- `force-app/main/default/lwc/relatedCodeTabs/relatedCodeTabs.js` -> **Severity: 240.409** (Blast Radius: 2.828 * Doc Risk: 85.0102%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
