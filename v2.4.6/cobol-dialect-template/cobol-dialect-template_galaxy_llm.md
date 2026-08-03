# ARCHITECTURAL_BRIEF: cobol-dialect-template
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cobol-dialect-template` |
| **Timestamp** | `2026-08-03T19:28:39.335075+00:00` |
| **Scan Duration** | `0.19s` |
| **Git Branch** | `develop` |
| **Git Commit** | `fe28bea4382cd42b9a0c93b60e7e473610c03b18` |
| **Git Remote** | `https://github.com/BroadcomMFD/cobol-dialect-template.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Total Artifacts | 49 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 1060 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 63.3% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2733 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2391 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1273 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 15 | 947 | 48.4% |
| MARKDOWN | 6 | 0 | 19.4% |
| PLAINTEXT | 4 | 1 | 12.9% |
| JSON | 3 | 79 | 9.7% |
| XML | 2 | 0 | 6.5% |
| TYPESCRIPT | 1 | 33 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.894`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 11 | 35.5% |
| file_cluster_8 | 9 | 29.0% |
| Unknown | 1 | 3.2% |
| file_cluster_0 | 1 | 3.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 29.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6105 LOC)
- `.g4`: 3x Unsupported Format (.g4)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 19.4 | 7.1 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 75.8 | 30.4 | 42.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.3 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 20.6 | 2.4 | 80.0 |
| API Exposure | 0.0 | 9.9 | 3.9 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 89.5 | 4.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 85.3 | 11.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.2 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 71.6 | 93.2 | 11.1 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 47.8 | 23.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 29.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `README.md` (Hits: 0)
- `client/example-dialect-support/CHANGELOG.md` (Hits: 0)
- `client/example-dialect-support/README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Level100Node.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java`) — 4 inbound connections
2. **RpcNode.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java`) — 3 inbound connections
3. **UnsetNode.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java`) — 3 inbound connections
4. **VisitorUtility.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java`) — 2 inbound connections
5. **ExampleDialect.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ExampleDialect.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`) — 28 outbound dependencies
2. **ExampleVisitor.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) — 24 outbound dependencies
3. **ProcessLevel100Node.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) — 15 outbound dependencies
4. **ErrorMessageHelper.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) — 14 outbound dependencies
5. **FindInjectsCommand.java** (`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java`) -> Impact: **57.1** | LOC: 51
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **51.3** | LOC: 57
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> Impact: **31.5** | LOC: 24
- `visitRpcParseStatement` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) -> Impact: **30.6** | LOC: 53
- `reportError` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) -> Impact: **28.6** | LOC: 17
- `getVariableUsageNode` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **26.6** | LOC: 12
- `checkSubordinatesIdentifier2` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **24.3** | LOC: 17
- `getExpectedText` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> Impact: **18.5** | LOC: 6
  * *Intent:* /** * Returns a message in case unwanted token found while parsing. * * @param recognizer Parser reference * @param currentToken current token * @retu...
- `getInputMismatchMessage` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> Impact: **17.1** | LOC: 7
- `reportMissingToken` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) -> Impact: **16.3** | LOC: 12

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `getOffendingToken` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) -> **O(2^N) [Recursive]**
- `getExpectedText` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Returns an input mismatch error message for a {@link InputMismatchException} * * @param recognizer parser reference
- `getExpectedText` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Returns a message in case unwanted token found while parsing. *
- `reportMissingToken` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) -> **O(N^6)**
- `getExpectedText` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> **O(N^6)**
  * *Intent:* /** * Returns a message in case unwanted token found while parsing. * * @param recognizer Parser reference * @param currentToken current token * @retu...
- `collectErrorTokens` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> **O(N^6)**
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> **O(N^6)**
- `addError` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> **O(N^6)**
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> **O(N^6)**
- `checkSubordinatesIdentifier2` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> DB Complexity: **4**
- `toCodeAction` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java`) -> DB Complexity: **3**
- `collectErrorTokens` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> DB Complexity: **2**
- `processText` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`) -> DB Complexity: **2**
- `buildErrorMessage` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> DB Complexity: **1**
  * *Intent:* /** * Returns an expected text, in case {@link InputMismatchException} is encountered while parsing. * * @param recognizer Parser ref * @return an exp...
- `visitBitwiseShiftstatement` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) -> DB Complexity: **1**
  * *Intent:* // Adds a custom node Level100Node. // Later we will enrich this node at POST_DEFINITION phase of analysis by adding a processor.
- `UnsetNode` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java`) -> DB Complexity: **1**
- `addError` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> DB Complexity: **1**
- `checkSubordinatesIdentifier2` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> DB Complexity: **1**
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `client/example-dialect-support` | 6 | 5019.62 | 0.83% | 0.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample` | 7 | 385.06 | 5.99% | 49.01% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor` | 4 | 255.1 | 9.07% | 8.04% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility` | 1 | 44.7 | 0.0% | 100.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes` | 3 | 21.18 | 5.07% | 0.0% |
| `server/dialect-example` | 2 | 21.04 | 5.0% | 0.0% |
| `client/example-dialect-support/snippets` | 1 | 15.96 | 7.02% | 0.0% |
| `client/example-dialect-support/syntaxes` | 1 | 15.34 | 13.9% | 0.0% |
| `__monolith__` | 1 | 2.1 | 0.0% | 0.0% |
| `client/example-dialect-support/src` | 1 | 1.6 | 19.4% | 97.24% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **99.9999%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **99.9986%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **97.9826%** Exposure
- `client/example-dialect-support/src/extension.ts` -> **97.2364%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` -> **96.5913%** Exposure
### Highest State Flux (Mutation/Volatility)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **85.3011%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java` -> **35.1082%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **27.4596%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **25.6038%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java` -> **21.6041%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **4** Orphaned Functions | **3** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` -> **5** Orphaned Functions | **0** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **0** Orphaned Functions | **4** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **3** Orphaned Functions | **0** Duplicates
- `client/example-dialect-support/src/extension.ts` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java`** -> AI Confidence: **99.18%**
2. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`** -> AI Confidence: **99.16%**
3. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`** -> AI Confidence: **99.16%**
4. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`** -> AI Confidence: **99.15%**
5. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`** -> AI Confidence: **99.09%**
6. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java`** -> AI Confidence: **99.09%**
7. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java`** -> AI Confidence: **99.08%**
8. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java`** -> AI Confidence: **99.08%**
9. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java`** -> AI Confidence: **99.08%**
10. **`server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`** -> AI Confidence: **99.07%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **100.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **100.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **99.9987%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **99.9971%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **99.4038%** Exposure
### Algorithmic DoS Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **100.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **100.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` -> **100.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **100.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `182` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` (JAVA) -> Cumulative Risk: **663.18**
- **Archetype:** `file_cluster_13` (Distance: 10.524 IQR)
- **Magnitude:** 121.32 | **LOC:** 116 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9971%), Documentation (99.9768%)
- **Heaviest Functions:** `accept` (Impact: 51.3), `getVariableUsageNode` (Impact: 26.6), `checkSubordinatesIdentifier2` (Impact: 24.3)

### 2. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA) -> Cumulative Risk: **634.08**
- **Archetype:** `file_cluster_0` (Distance: 9.952 IQR)
- **Magnitude:** 86.84 | **LOC:** 111 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9962%), Logic Bomb (97.4655%)
- **Heaviest Functions:** `reportError` (Impact: 28.6), `reportMissingToken` (Impact: 16.3), `reportUnwantedToken` (Impact: 9.4)

### 3. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` (JAVA) -> Cumulative Risk: **630.62**
- **Archetype:** `file_cluster_13` (Distance: 10.45 IQR)
- **Magnitude:** 105.38 | **LOC:** 150 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9986%), Documentation (99.8005%)
- **Heaviest Functions:** `getExpectedText` (Impact: 18.5), `getInputMismatchMessage` (Impact: 17.1), `getUnwantedTokenMessage` (Impact: 13.2)

### 4. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA) -> Cumulative Risk: **591.85**
- **Archetype:** `file_cluster_8` (Distance: 8.375 IQR)
- **Magnitude:** 44.7 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructRange` (Impact: 8.3), `constructRange` (Impact: 8.3), `addReplacementContext` (Impact: 6.6)

### 5. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA) -> Cumulative Risk: **524.11**
- **Archetype:** `file_cluster_13` (Distance: 9.397 IQR)
- **Magnitude:** 91.78 | **LOC:** 220 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9982%), Tech Debt (96.5913%), Verification (80.0%)
- **Heaviest Functions:** `visitRpcParseStatement` (Impact: 30.6), `visitQualifiedVariableDataName` (Impact: 11.3), `getName` (Impact: 11.3)

### 6. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java` (JAVA) -> Cumulative Risk: **474.27**
- **Archetype:** `file_cluster_13` (Distance: 9.355 IQR)
- **Magnitude:** 67.64 | **LOC:** 80 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9861%), Documentation (99.3282%), Verification (80.0%)
- **Heaviest Functions:** `accept` (Impact: 57.1), `ProcessUnsetNode` (Impact: 3.1)

### 7. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA) -> Cumulative Risk: **470.94**
- **Archetype:** `file_cluster_13` (Distance: 8.923 IQR)
- **Magnitude:** 24.54 | **LOC:** 57 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9987%), Documentation (99.7705%), Tech Debt (97.9826%)
- **Heaviest Functions:** `visitInjectStatement` (Impact: 6.3), `addTreeNode` (Impact: 6.2), `InjectRuleVisitor` (Impact: 2.1)

### 8. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` (JAVA) -> Cumulative Risk: **462.81**
- **Archetype:** `file_cluster_13` (Distance: 9.766 IQR)
- **Magnitude:** 49.02 | **LOC:** 299 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9998%), Documentation (85.7682%)
- **Heaviest Functions:** `processText` (Impact: 6.5), `extend` (Impact: 5.2), `getName` (Impact: 2.1)

### 9. `client/example-dialect-support/src/extension.ts` (TYPESCRIPT) -> Cumulative Risk: **409.6**
- **Archetype:** `file_cluster_8` (Distance: 8.749 IQR)
- **Magnitude:** 1.6 | **LOC:** 44 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.2364%), Concurrency (89.4536%), Documentation (48.107%)
- **Heaviest Functions:** `activate` (Impact: 7.4), `deactivate` (Impact: 1.9)

### 10. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA) -> Cumulative Risk: **378.78**
- **Archetype:** `file_cluster_13` (Distance: 8.823 IQR)
- **Magnitude:** 55.8 | **LOC:** 73 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.982%), Safety Score (50.0%)
- **Heaviest Functions:** `accept` (Impact: 31.5), `registerVariable` (Impact: 9.3), `addError` (Impact: 6.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `client/example-dialect-support/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.524 IQR)
- **Top Global Matches:** file_cluster_13: 10.524, file_cluster_8: 10.89, file_cluster_17: 11.048
- **Magnitude:** 121.32 | **LOC:** 116 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (18.2659%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 51.3 | O(N^6) | DB: 4)
  * `getVariableUsageNode` (Impact: 26.6 | O(N^5))
  * `checkSubordinatesIdentifier2` (Impact: 24.3 | O(N^6) | DB: 1)
  * `ProcessRpcNode` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 24`, `args: 10`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 11`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.059259
  * `Imports (Out-Degree: 1):` java.util.Objects, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.utils.RangeUtils, org.eclipse.lsp4j.Range, java.util.Optional.ofNullable, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, org.eclipse.lsp.cobol.common.message.MessageService...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.45 IQR)
- **Top Global Matches:** file_cluster_13: 10.45, file_cluster_8: 10.84, file_cluster_16: 10.938
- **Magnitude:** 105.38 | **LOC:** 150 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.669%), Tech Debt (99.9986%)
**Top Internal Functions/Classes:**
  * `getExpectedText` (Impact: 18.5 | O(N^6))
    * *Intent:* /** * Returns a message in case unwanted token found while parsing. * * @param recognizer Parser ref...
  * `getInputMismatchMessage` (Impact: 17.1 | O(N^4))
  * `getUnwantedTokenMessage` (Impact: 13.2 | O(N^4))
  * `removeIdentifierTokens` (Impact: 7.0 | O(N^2))
    * *Intent:* /** * Returns the last invocation rule while parsing. * * @param recognizer parser ref
  * `getExpectedText` (Impact: 6.9 | O(2^N))
    * *Intent:* /** * Returns an input mismatch error message for a {@link InputMismatchException} * * @param recogn...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 27`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 3`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 14`
* *Defense:* `safety: 2`, `doc: 20`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Arrays, java.util.stream.Collectors.joining, java.util.List, java.util.Set, org.antlr.v4.runtime.Parser, java.util.stream.Collectors.toList, org.antlr.v4.runtime.NoViableAltException, org.antlr.v4.runtime.InputMismatchException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.397 IQR)
- **Top Global Matches:** file_cluster_13: 9.397, file_cluster_8: 9.574, file_cluster_16: 9.894
- **Magnitude:** 91.78 | **LOC:** 220 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (7.3492%), Tech Debt (96.5913%)
**Top Internal Functions/Classes:**
  * `visitRpcParseStatement` (Impact: 30.6 | O(N^4))
  * `visitQualifiedVariableDataName` (Impact: 11.3 | O(N^2))
  * `getName` (Impact: 11.3 | O(N^1))
  * `visitBitwiseShiftstatement` (Impact: 7.5 | O(N^5) | DB: 1)
    * *Intent:* // Adds a custom node Level100Node. // Later we will enrich this node at POST_DEFINITION phase of an...
  * `addTreeNode` (Impact: 6.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 48`, `args: 33`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `planned_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 8`, `import: 24`
* *Defense:* `safety: 1`, `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.antlr.v4.runtime.ParserRuleContext, java.util.ArrayList, lombok.Getter, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, org.broadcom.cobol.dialects.cobolExample.nodes.UnsetNode, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, java.util.function.Function, org.eclipse.lsp.cobol.common.error.SyntaxError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.952 IQR)
- **Top Global Matches:** file_cluster_0: 9.952, file_cluster_13: 10.265, file_cluster_8: 10.534
- **Magnitude:** 86.84 | **LOC:** 111 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.3305%), Tech Debt (48.4761%)
**Top Internal Functions/Classes:**
  * `reportError` (Impact: 28.6 | O(N^3))
  * `reportMissingToken` (Impact: 16.3 | O(N^6))
  * `reportUnwantedToken` (Impact: 9.4 | O(N^3))
  * `getOffendingToken` (Impact: 6.9 | O(2^N))
  * `reportUnrecognizedException` (Impact: 5.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 22`, `args: 9`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.eclipse.lsp.cobol.common.message.MessageServiceProvider, lombok.Setter, lombok.Getter, lombok.extern.slf4j.Slf4j, org.antlr.v4.runtime.*, org.eclipse.lsp.cobol.common.message.MessageService, lombok.NoArgsConstructor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.355 IQR)
- **Top Global Matches:** file_cluster_13: 9.355, file_cluster_8: 9.696, file_cluster_17: 9.825
- **Magnitude:** 67.64 | **LOC:** 80 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (9.724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 57.1 | O(N^6) | DB: 1)
  * `ProcessUnsetNode` (Impact: 3.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 1):` org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp4j.Location, java.util.List, org.broadcom.cobol.dialects.cobolExample.nodes.UnsetNode, org.eclipse.lsp.cobol.common.model.tree.variable.VariableType, org.eclipse.lsp.cobol.common.message.MessageService...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.823 IQR)
- **Top Global Matches:** file_cluster_13: 8.823, file_cluster_8: 9.13, file_cluster_17: 9.6
- **Magnitude:** 55.8 | **LOC:** 73 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.2853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 31.5 | O(N^6))
  * `registerVariable` (Impact: 9.3 | O(N^2))
  * `addError` (Impact: 6.6 | O(N^6) | DB: 1)
  * `ProcessLevel100Node` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 24`, `args: 9`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 4`, `import: 15`
* *Defense:* `safety: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.059259
  * `Imports (Out-Degree: 1):` org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, org.eclipse.lsp.cobol.common.symbols.VariableAccumulator, org.eclipse.lsp.cobol.common.processor.Processor, org.eclipse.lsp.cobol.common.model.tree.SectionNode, org.eclipse.lsp.cobol.common.message.MessageService...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.766 IQR)
- **Top Global Matches:** file_cluster_13: 9.766, file_cluster_16: 10.198, file_cluster_8: 10.346
- **Magnitude:** 49.02 | **LOC:** 299 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processText` (Impact: 6.5 | O(N^4) | DB: 2)
  * `extend` (Impact: 5.2 | O(N^3))
  * `getName` (Impact: 2.1 | O(N^1))
  * `getSettingsSections` (Impact: 2.1 | O(N^1))
  * `getWatchingFolderSettings` (Impact: 2.1 | O(N^1))
    * *Intent:* /** * This implementation is specific to copybooks. * Use this when an external source content needs...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `args: 8`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 19`, `import: 25`
* *Defense:* `doc: 16`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 82.504
  * `Choke Point (Betweenness):` 0.013793 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 6):` org.eclipse.lsp.cobol.common.ResultWithErrors, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, org.broadcom.cobol.dialects.cobolExample.nodes.UnsetNode, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, org.broadcom.cobol.dialects.cobolExample.processor.ProcessRpcNode, org.eclipse.lsp4j.Range, org.antlr.v4.runtime.CommonTokenStream, org.eclipse.lsp.cobol.common.mapping.ExtendedDocument...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.375 IQR)
- **Top Global Matches:** file_cluster_8: 8.375, file_cluster_13: 8.452, file_cluster_7: 9.249
- **Magnitude:** 44.7 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `constructRange` (Impact: 8.3 | O(N^6))
  * `constructRange` (Impact: 8.3 | O(N^6))
  * `addReplacementContext` (Impact: 6.6 | O(N^6) | DB: 1)
  * `addReplacementContext` (Impact: 6.6 | O(N^6) | DB: 1)
  * `constructLocality` (Impact: 4.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 9`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` org.eclipse.lsp4j.Location, org.antlr.v4.runtime.ParserRuleContext, org.antlr.v4.runtime.tree.TerminalNode, org.eclipse.lsp4j.Position, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, lombok.experimental.UtilityClass, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp4j.Range...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.923 IQR)
- **Top Global Matches:** file_cluster_13: 8.923, file_cluster_8: 9.12, file_cluster_16: 9.2
- **Magnitude:** 24.54 | **LOC:** 57 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.5372%), Tech Debt (97.9826%)
**Top Internal Functions/Classes:**
  * `visitInjectStatement` (Impact: 6.3 | O(N^4))
  * `addTreeNode` (Impact: 6.2 | O(N^1))
  * `InjectRuleVisitor` (Impact: 2.1 | O(N^1))
  * `defaultResult` (Impact: 2.1 | O(N^1))
  * `aggregateResult` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 22`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.google.common.collect.ImmutableList, org.eclipse.lsp4j.Location, org.antlr.v4.runtime.ParserRuleContext, java.util.ArrayList, java.util.List, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, java.util.function.Function, java.util.stream.Stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.277 IQR)
- **Top Global Matches:** file_cluster_13: 11.277, file_cluster_17: 11.652, file_cluster_0: 11.69
- **Magnitude:** 23.12 | **LOC:** 64 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.0772%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `retrieveInjects` (Impact: 7.5 | O(N^2))
  * `createCommand` (Impact: 4.6 | O(N^4))
  * `toCodeAction` (Impact: 3.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 25`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `safety: 9`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.eclipse.lsp4j.Command, lombok.NonNull, java.util.Collections.singletonList, org.broadcom.cobol.dialects.cobolExample.ExampleDialect.MISSING_INJECTS, org.eclipse.lsp4j.CodeActionParams, java.util.List, java.util.Arrays.asList, java.util.stream.Collectors.toList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/snippets/example-snippets.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.96 | **LOC:** 48 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.0219%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/syntaxes/example.injection.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.34 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.9011%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.28 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/lombok.config` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/pom.xml` (XML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 102 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.057 IQR)
- **Top Global Matches:** file_cluster_8: 7.057, file_cluster_13: 7.487, file_cluster_7: 8.137
- **Magnitude:** 10.34 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (32.1778%)
**Top Internal Functions/Classes:**
  * `generate` (Impact: 6.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 5`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.eclipse.lsp.cobol.common.model.tree.variable.ElementaryItemNode, lombok.Getter, org.eclipse.lsp.cobol.common.model.tree.variable.GroupItemNode, org.eclipse.lsp.cobol.common.model.tree.variable.UsageFormat, lombok.AllArgsConstructor, org.eclipse.lsp.cobol.common.utils.ImplicitCodeUtils, org.eclipse.lsp.cobol.common.model.Locality...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.752 IQR)
- **Top Global Matches:** file_cluster_8: 6.752, file_cluster_13: 7.278, file_cluster_7: 7.84
- **Magnitude:** 8.26 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.2168%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RpcNode` (Impact: 5.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.663
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.104167
  * `Imports (Out-Degree: 0):` org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.077 IQR)
- **Top Global Matches:** file_cluster_13: 9.077, file_cluster_8: 9.663, file_cluster_0: 9.853
- **Magnitude:** 7.08 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UnsetNode` (Impact: 2.8 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 69.663
  * `Choke Point (Betweenness):` 0.010345 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, lombok.Getter, org.broadcom.cobol.dialects.cobolExample.ExampleDialect, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.027 IQR)
- **Top Global Matches:** file_cluster_13: 8.027, file_cluster_8: 8.127, file_cluster_0: 8.774
- **Magnitude:** 5.84 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Level100Node` (Impact: 3.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 89.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` org.eclipse.lsp.cobol.common.model.Locality, lombok.Getter, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/DialectParserListener.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.724 IQR)
- **Top Global Matches:** file_cluster_13: 7.724, file_cluster_8: 7.918, file_cluster_16: 8.447
- **Magnitude:** 4.38 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DialectParserListener` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.eclipse.lsp.cobol.common.error.SyntaxError, java.util.ArrayList, lombok.Getter, java.util.List, org.antlr.v4.runtime.BaseErrorListener
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.1 | **LOC:** 105 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/src/extension.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.749 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.661 IQR)
- **Top Global Matches:** file_cluster_8: 8.749, file_cluster_13: 8.992, file_cluster_4: 9.032
- **Magnitude:** 1.6 | **LOC:** 44 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.3997%), Tech Debt (97.2364%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 7.4 | O(N^1))
    * *Intent:* // This method is called when your extension is activated // Your extension is activated the very fi...
  * `deactivate` (Impact: 1.9 | O(N^1))
    * *Intent:* // This method is called when your extension is deactivated
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cobol-dialect-api, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.34 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA) | Magnitude: 86.84 | Delta: **0.313 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 22, func_start: 15, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` (JAVA) | Magnitude: 5.84 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, import: 4, func_start: 2
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA) | Magnitude: 91.78 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 48, args: 33, import: 24
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/DialectParserListener.java` (JAVA) | Magnitude: 4.38 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, import: 5, immutability_locks: 2
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA) | Magnitude: 24.54 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 22, import: 12, args: 8
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA) | Magnitude: 55.8 | Delta: **0.307 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 24, import: 15, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA) | Magnitude: 44.7 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 22, args: 9, import: 9
- `client/example-dialect-support/src/extension.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.243 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 9, immutability_locks: 6, args: 4
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java` (JAVA) | Magnitude: 10.34 | Delta: **0.43 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 16, import: 9, args: 5
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA) | Magnitude: 8.26 | Delta: **0.526 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 8, immutability_locks: 6, encapsulation: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 0.284** (Bridge: 0.0103 * Flux: 27.4596%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **Severity: 0.2** (Bridge: 0.0138 * Flux: 14.4922%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 5.44** (Embedded: 0.1 * Error Risk: 54.4004%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **Severity: 4.49** (Embedded: 0.0593 * Error Risk: 75.7771%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **Severity: 3.583** (Embedded: 0.0667 * Error Risk: 53.743%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **Severity: 3.062** (Embedded: 0.06 * Error Risk: 51.0343%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` -> **Severity: 2.963** (Embedded: 0.0593 * Error Risk: 50.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` -> **Severity: 7090.284** (Blast Radius: 89.462 * Doc Risk: 79.2547%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **Severity: 7076.22** (Blast Radius: 82.504 * Doc Risk: 85.7682%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 6492.794** (Blast Radius: 69.663 * Doc Risk: 93.2029%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **Severity: 4804.1** (Blast Radius: 48.041 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **Severity: 4211.114** (Blast Radius: 69.663 * Doc Risk: 60.4498%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
