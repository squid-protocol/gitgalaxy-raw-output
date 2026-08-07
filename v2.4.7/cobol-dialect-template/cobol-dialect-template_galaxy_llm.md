# ARCHITECTURAL_BRIEF: cobol-dialect-template
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cobol-dialect-template` |
| **Timestamp** | `2026-08-07T03:50:52.071774+00:00` |
| **Scan Duration** | `0.14s` |
| **Git Branch** | `develop` |
| **Git Commit** | `fe28bea4382cd42b9a0c93b60e7e473610c03b18` |
| **Git Remote** | `https://github.com/BroadcomMFD/cobol-dialect-template.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 19.4 | 7.0 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 75.8 | 30.4 | 42.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 32.0 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 5.9 | 2.4 | 2.3 |
| API Exposure | 0.0 | 9.9 | 3.9 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 89.5 | 4.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 85.3 | 11.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.2 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 81.8 | 36.8 | 37.1 | 11.1 |
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

- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java`) -> Impact: **18.2** | LOC: 52
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **16.8** | LOC: 58
- `visitRpcParseStatement` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) -> Impact: **14.9** | LOC: 54
- `reportError` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) -> Impact: **14.8** | LOC: 18
- `getName` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) -> Impact: **11.3** | LOC: 3
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> Impact: **9.9** | LOC: 25
- `getVariableUsageNode` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **9.3** | LOC: 12
- `visitQualifiedVariableDataName` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) -> Impact: **8.2** | LOC: 6
- `addError` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> Impact: **7.9** | LOC: 20
- `checkSubordinatesIdentifier2` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **7.6** | LOC: 17

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `client/example-dialect-support` | 6 | 5019.62 | 0.83% | 0.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample` | 7 | 258.16 | 5.64% | 49.01% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor` | 4 | 123.7 | 9.07% | 32.91% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility` | 1 | 22.1 | 0.0% | 100.0% |
| `server/dialect-example` | 2 | 21.04 | 5.0% | 0.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes` | 3 | 17.58 | 5.07% | 0.0% |
| `client/example-dialect-support/snippets` | 1 | 15.96 | 7.02% | 0.0% |
| `client/example-dialect-support/syntaxes` | 1 | 15.34 | 13.9% | 0.0% |
| `__monolith__` | 1 | 2.1 | 0.0% | 0.0% |
| `client/example-dialect-support/src` | 1 | 1.6 | 19.4% | 97.24% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **99.9999%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **99.9986%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` -> **99.4472%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **97.9826%** Exposure
- `client/example-dialect-support/src/extension.ts` -> **97.2364%** Exposure
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `182` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `client/example-dialect-support/src/extension.ts` (TYPESCRIPT) -> Cumulative Risk: **392.46**
- **Archetype:** `file_cluster_8` (Distance: 8.749 IQR)
- **Magnitude:** 1.6 | **LOC:** 44 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.2364%), Concurrency (89.4536%), Safety Score (47.1728%)
- **Heaviest Functions:** `activate` (Impact: 7.4), `deactivate` (Impact: 1.9)

### 2. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA) -> Cumulative Risk: **373.37**
- **Archetype:** `file_cluster_8` (Distance: 8.212 IQR)
- **Magnitude:** 22.1 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Documentation (81.7574%), Safety Score (53.743%)
- **Heaviest Functions:** `constructRange` (Impact: 2.7), `constructRange` (Impact: 2.7), `addReplacementContext` (Impact: 2.2)

### 3. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA) -> Cumulative Risk: **370.42**
- **Archetype:** `file_cluster_13` (Distance: 9.24 IQR)
- **Magnitude:** 67.68 | **LOC:** 220 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.5913%), Verification (80.0%), Safety Score (56.3449%)
- **Heaviest Functions:** `visitRpcParseStatement` (Impact: 14.9), `getName` (Impact: 11.3), `visitQualifiedVariableDataName` (Impact: 8.2)

### 4. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA) -> Cumulative Risk: **322.6**
- **Archetype:** `file_cluster_13` (Distance: 8.686 IQR)
- **Magnitude:** 34.8 | **LOC:** 73 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.4472%), Safety Score (50.0%), Documentation (47.0622%)
- **Heaviest Functions:** `accept` (Impact: 9.9), `addError` (Impact: 7.9), `registerVariable` (Impact: 6.3)

### 5. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` (JAVA) -> Cumulative Risk: **317.56**
- **Archetype:** `file_cluster_13` (Distance: 10.359 IQR)
- **Magnitude:** 52.82 | **LOC:** 116 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (85.3011%), Safety Score (75.7771%), Documentation (31.8754%)
- **Heaviest Functions:** `accept` (Impact: 16.8), `getVariableUsageNode` (Impact: 9.3), `checkSubordinatesIdentifier2` (Impact: 7.6)

### 6. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA) -> Cumulative Risk: **302.61**
- **Archetype:** `file_cluster_0` (Distance: 9.863 IQR)
- **Magnitude:** 49.94 | **LOC:** 111 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (65.6347%), Tech Debt (48.4761%), Documentation (45.8916%)
- **Heaviest Functions:** `reportError` (Impact: 14.8), `reportMissingToken` (Impact: 5.5), `reportUnwantedToken` (Impact: 5.4)

### 7. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA) -> Cumulative Risk: **284.72**
- **Archetype:** `file_cluster_13` (Distance: 8.844 IQR)
- **Magnitude:** 20.94 | **LOC:** 57 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.9826%), Documentation (72.8114%), Cognitive Load (6.5372%)
- **Heaviest Functions:** `addTreeNode` (Impact: 5.4), `visitInjectStatement` (Impact: 3.2), `defaultResult` (Impact: 2.4)

### 8. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` (JAVA) -> Cumulative Risk: **268.72**
- **Archetype:** `file_cluster_13` (Distance: 9.077 IQR)
- **Magnitude:** 6.18 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (93.3333%), Documentation (76.7126%), Safety Score (54.4004%), State Flux (27.4596%)
- **Heaviest Functions:** `UnsetNode` (Impact: 1.9)

### 9. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` (JAVA) -> Cumulative Risk: **265.91**
- **Archetype:** `file_cluster_13` (Distance: 10.36 IQR)
- **Magnitude:** 51.08 | **LOC:** 150 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9986%), Safety Score (42.8381%), Documentation (11.9203%)
- **Heaviest Functions:** `getInputMismatchMessage` (Impact: 7.1), `getExpectedText` (Impact: 5.5), `getUnwantedTokenMessage` (Impact: 5.4)

### 10. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java` (JAVA) -> Cumulative Risk: **247.19**
- **Archetype:** `file_cluster_8` (Distance: 6.755 IQR)
- **Magnitude:** 8.34 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (66.8476%), Documentation (39.137%), Tech Debt (32.1778%)
- **Heaviest Functions:** `generate` (Impact: 4.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `client/example-dialect-support/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.24 IQR)
- **Top Global Matches:** file_cluster_13: 9.24, file_cluster_8: 9.418, file_cluster_16: 9.743
- **Magnitude:** 67.68 | **LOC:** 220 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3492%), Tech Debt (96.5913%)
**Top Internal Functions/Classes:**
  * `visitRpcParseStatement` (Impact: 14.9)
  * `getName` (Impact: 11.3)
  * `visitQualifiedVariableDataName` (Impact: 8.2)
  * `addTreeNode` (Impact: 5.4)
  * `visitBitwiseShiftstatement` (Impact: 3.3)
    * *Intent:* // Adds a custom node Level100Node.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 48`, `args: 27`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `planned_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 8`, `import: 24`
* *Defense:* `safety: 1`, `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.eclipse.lsp.cobol.common.error.SyntaxError, java.util.LinkedList, org.broadcom.cobol.dialects.cobolExample.utility.VisitorUtility, java.util.function.Function, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, java.util.List, org.eclipse.lsp.cobol.common.model.tree.variable.VariableUsageNode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.359 IQR)
- **Top Global Matches:** file_cluster_13: 10.359, file_cluster_8: 10.725, file_cluster_17: 10.893
- **Magnitude:** 52.82 | **LOC:** 116 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.2659%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 16.8)
  * `getVariableUsageNode` (Impact: 9.3)
  * `checkSubordinatesIdentifier2` (Impact: 7.6)
  * `ProcessRpcNode` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 24`, `args: 10`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 11`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.059259
  * `Imports (Out-Degree: 1):` org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality, java.util.Optional.ofNullable, org.eclipse.lsp.cobol.common.error.SyntaxError, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, org.eclipse.lsp.cobol.common.processor.Processor, java.util.Objects, org.eclipse.lsp.cobol.common.model.tree.variable.VariableUsageNode, org.eclipse.lsp.cobol.common.error.ErrorSource...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.36 IQR)
- **Top Global Matches:** file_cluster_13: 10.36, file_cluster_8: 10.751, file_cluster_16: 10.851
- **Magnitude:** 51.08 | **LOC:** 150 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.669%), Tech Debt (99.9986%)
**Top Internal Functions/Classes:**
  * `getInputMismatchMessage` (Impact: 7.1)
  * `getExpectedText` (Impact: 5.5)
    * *Intent:* /** * Returns a message in case unwanted token found while parsing. * * @param recognizer Parser ref...
  * `getUnwantedTokenMessage` (Impact: 5.4)
  * `removeIdentifierTokens` (Impact: 4.7)
    * *Intent:* /** * Returns the last invocation rule while parsing. * * @param recognizer parser ref
  * `getRule` (Impact: 2.6)
    * *Intent:* /** * Returns an input mismatch error message for a {@link InputMismatchException} * * @param recogn...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 27`, `args: 15`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 3`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 14`
* *Defense:* `safety: 2`, `doc: 20`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.antlr.v4.runtime.Recognizer.EOF, java.util.stream.Collectors.joining, org.antlr.v4.runtime.InputMismatchException, org.antlr.v4.runtime.Token, java.util.List, java.util.stream.Collectors.toList, org.antlr.v4.runtime.misc.IntervalSet, org.eclipse.lsp.cobol.common.message.MessageService...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.863 IQR)
- **Top Global Matches:** file_cluster_0: 9.863, file_cluster_13: 10.179, file_cluster_8: 10.448
- **Magnitude:** 49.94 | **LOC:** 111 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.8691%), Tech Debt (48.4761%)
**Top Internal Functions/Classes:**
  * `reportError` (Impact: 14.8)
  * `reportMissingToken` (Impact: 5.5)
  * `reportUnwantedToken` (Impact: 5.4)
  * `reportUnrecognizedException` (Impact: 3.7)
  * `getOffendingToken` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 22`, `args: 8`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.antlr.v4.runtime.*, org.eclipse.lsp.cobol.common.message.MessageService, lombok.NoArgsConstructor, lombok.Setter, lombok.Getter, lombok.extern.slf4j.Slf4j, org.eclipse.lsp.cobol.common.message.MessageServiceProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.793 IQR)
- **Top Global Matches:** file_cluster_13: 9.793, file_cluster_16: 10.223, file_cluster_8: 10.372
- **Magnitude:** 48.22 | **LOC:** 299 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processText` (Impact: 3.4)
  * `extend` (Impact: 3.2)
    * *Intent:* // Add error encountered while visiting the parser. To be reported to COBOL LS engine.
  * `parseMyRule` (Impact: 2.8)
    * *Intent:* /** * Processing the text * * @param context is a DialectProcessingContext class with all needed dat...
  * `getName` (Impact: 2.4)
  * `getSettingsSections` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 19`, `import: 25`
* *Defense:* `doc: 16`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 82.504
  * `Choke Point (Betweenness):` 0.013793 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 6):` org.eclipse.lsp.cobol.common.mapping.ExtendedDocument, org.eclipse.lsp.cobol.common.error.*, org.eclipse.lsp4j.Range, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, com.google.common.collect.ImmutableMap, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, org.broadcom.cobol.dialects.cobolExample.processor.ProcessRpcNode, org.eclipse.lsp.cobol.common.message.MessageService...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.686 IQR)
- **Top Global Matches:** file_cluster_13: 8.686, file_cluster_8: 9.019, file_cluster_17: 9.462
- **Magnitude:** 34.8 | **LOC:** 73 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2853%), Tech Debt (99.4472%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 9.9)
  * `addError` (Impact: 7.9)
  * `registerVariable` (Impact: 6.3)
  * `addError` (Impact: 2.3)
  * `ProcessLevel100Node` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 24`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 15`
* *Defense:* `safety: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.059259
  * `Imports (Out-Degree: 1):` org.eclipse.lsp.cobol.common.model.SectionType, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNode, org.eclipse.lsp.cobol.common.processor.Processor, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.ErrorSeverity.ERROR...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.355 IQR)
- **Top Global Matches:** file_cluster_13: 9.355, file_cluster_8: 9.696, file_cluster_17: 9.825
- **Magnitude:** 27.74 | **LOC:** 80 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 18.2)
  * `ProcessUnsetNode` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 1):` org.eclipse.lsp4j.Location, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.model.tree.variable.VariableType, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNode, org.eclipse.lsp.cobol.common.processor.Processor, java.util.List, org.eclipse.lsp.cobol.common.model.tree.variable.VariableUsageNode, org.eclipse.lsp.cobol.common.model.NodeType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.212 IQR)
- **Top Global Matches:** file_cluster_8: 8.212, file_cluster_13: 8.291, file_cluster_7: 9.101
- **Magnitude:** 22.1 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `constructRange` (Impact: 2.7)
  * `constructRange` (Impact: 2.7)
  * `addReplacementContext` (Impact: 2.2)
  * `addReplacementContext` (Impact: 2.2)
  * `constructLocality` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` lombok.experimental.UtilityClass, org.eclipse.lsp4j.Location, org.eclipse.lsp4j.Position, org.eclipse.lsp.cobol.common.dialects.CobolDialect, org.antlr.v4.runtime.ParserRuleContext, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, org.antlr.v4.runtime.tree.TerminalNode, org.eclipse.lsp.cobol.common.model.Locality...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.844 IQR)
- **Top Global Matches:** file_cluster_13: 8.844, file_cluster_8: 9.041, file_cluster_16: 9.122
- **Magnitude:** 20.94 | **LOC:** 57 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.5372%), Tech Debt (97.9826%)
**Top Internal Functions/Classes:**
  * `addTreeNode` (Impact: 5.4)
  * `visitInjectStatement` (Impact: 3.2)
  * `defaultResult` (Impact: 2.4)
  * `InjectRuleVisitor` (Impact: 2.1)
  * `aggregateResult` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 22`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.function.Function, org.eclipse.lsp4j.Location, com.google.common.collect.ImmutableList, java.util.List, java.util.stream.Collectors.toList, org.eclipse.lsp.cobol.common.model.tree.CopyNode, java.util.ArrayList, org.antlr.v4.runtime.ParserRuleContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.276 IQR)
- **Top Global Matches:** file_cluster_13: 11.276, file_cluster_17: 11.652, file_cluster_0: 11.689
- **Magnitude:** 16.92 | **LOC:** 64 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0772%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `retrieveInjects` (Impact: 5.5)
  * `toCodeAction` (Impact: 2.2)
  * `createCommand` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 25`, `args: 7`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `safety: 9`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.function.Function, java.util.Arrays.asList, org.broadcom.cobol.dialects.cobolExample.ExampleDialect.MISSING_INJECTS, org.eclipse.lsp4j.CodeActionKind.QuickFix, org.eclipse.lsp4j.jsonrpc.messages.Either, org.eclipse.lsp4j.CodeAction, org.eclipse.lsp4j.Command, java.util.List...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/snippets/example-snippets.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.96 | **LOC:** 48 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_8` (Drift: 6.755 IQR)
- **Top Global Matches:** file_cluster_8: 6.755, file_cluster_13: 7.203, file_cluster_7: 7.876
- **Magnitude:** 8.34 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (32.1778%)
**Top Internal Functions/Classes:**
  * `generate` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.eclipse.lsp.cobol.common.model.tree.variable.ElementaryItemNode, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.eclipse.lsp.cobol.common.model.tree.variable.UsageFormat, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNode, org.eclipse.lsp.cobol.common.utils.ImplicitCodeUtils, lombok.AllArgsConstructor, lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.752 IQR)
- **Top Global Matches:** file_cluster_8: 6.752, file_cluster_13: 7.278, file_cluster_7: 7.84
- **Magnitude:** 6.76 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2168%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RpcNode` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.663
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.104167
  * `Imports (Out-Degree: 0):` org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.077 IQR)
- **Top Global Matches:** file_cluster_13: 9.077, file_cluster_8: 9.663, file_cluster_0: 9.853
- **Magnitude:** 6.18 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UnsetNode` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 69.663
  * `Choke Point (Betweenness):` 0.010345 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality, org.eclipse.lsp.cobol.common.model.NodeType, org.broadcom.cobol.dialects.cobolExample.ExampleDialect, org.eclipse.lsp.cobol.common.model.tree.Node, lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.027 IQR)
- **Top Global Matches:** file_cluster_13: 8.027, file_cluster_8: 8.127, file_cluster_0: 8.774
- **Magnitude:** 4.64 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Level100Node` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 89.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` org.eclipse.lsp.cobol.common.model.NodeType, lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.tree.Node
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/DialectParserListener.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.724 IQR)
- **Top Global Matches:** file_cluster_13: 7.724, file_cluster_8: 7.918, file_cluster_16: 8.447
- **Magnitude:** 3.38 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DialectParserListener` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.eclipse.lsp.cobol.common.error.SyntaxError, java.util.List, java.util.ArrayList, lombok.Getter, org.antlr.v4.runtime.BaseErrorListener
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.1 | **LOC:** 105 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Risk Profile:** Cognitive Load (19.3997%), Tech Debt (97.2364%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 7.4)
    * *Intent:* // This method is called when your extension is activated // Your extension is activated the very fi...
  * `deactivate` (Impact: 1.9)
    * *Intent:* // This method is called when your extension is deactivated
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vscode, cobol-dialect-api
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.34 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA) | Magnitude: 49.94 | Delta: **0.316 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 22, func_start: 12, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` (JAVA) | Magnitude: 4.64 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, import: 4, func_start: 2
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA) | Magnitude: 67.68 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 48, args: 27, import: 24
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/DialectParserListener.java` (JAVA) | Magnitude: 3.38 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, import: 5, immutability_locks: 2
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA) | Magnitude: 20.94 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 22, import: 12, generics: 8
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA) | Magnitude: 34.8 | Delta: **0.333 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 24, import: 15, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA) | Magnitude: 22.1 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 22, import: 9, api: 7
- `client/example-dialect-support/src/extension.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.243 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 9, immutability_locks: 6, args: 4
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java` (JAVA) | Magnitude: 8.34 | Delta: **0.448 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 16, import: 9, safety_bypasses: 3
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA) | Magnitude: 6.76 | Delta: **0.526 IQR** | Secondary Pull: `file_cluster_13`
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

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 5344.03** (Blast Radius: 69.663 * Doc Risk: 76.7126%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` -> **Severity: 4454.912** (Blast Radius: 89.462 * Doc Risk: 49.7967%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **Severity: 3927.707** (Blast Radius: 48.041 * Doc Risk: 81.7574%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **Severity: 2645.522** (Blast Radius: 69.663 * Doc Risk: 37.976%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **Severity: 1695.923** (Blast Radius: 23.292 * Doc Risk: 72.8114%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
