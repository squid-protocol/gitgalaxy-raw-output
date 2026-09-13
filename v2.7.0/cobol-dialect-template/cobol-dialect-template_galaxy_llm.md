# ARCHITECTURAL_BRIEF: cobol-dialect-template
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/BroadcomMFD/cobol-dialect-template.git` |
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
| Total Artifacts | 49 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 1131 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 63.3% |
| Dominant Lang | JAVA |

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
| JAVA | 15 | 1018 | 48.4% |
| MARKDOWN | 6 | 0 | 19.4% |
| PLAINTEXT | 4 | 1 | 12.9% |
| JSON | 3 | 79 | 9.7% |
| XML | 2 | 0 | 6.5% |
| TYPESCRIPT | 1 | 33 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.28`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 21 | 67.7% |
| Unknown | 1 | 3.2% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 20.8 | 4.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.4 | 43.6 | 53.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.5 | 2.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 56.2 | 12.9 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 76.9 | 3.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 96.6 | 19.4 | 11.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.2 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 76.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 66.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4 | 2 | 0 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` |
| cleanup | 0 | 0 | 0 | - |
| guards | 102 | 14 | 12 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` |
| danger | 22 | 8 | 2 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` |
| concurrency | 3 | 1 | 0 | `client/example-dialect-support/src/extension.ts` |
| connectivity | 75 | 16 | 6 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 2 | 2 | 0 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` |
| tests | 0 | 0 | 0 | - |
| docs | 19 | 4 | 1 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` |
| debt | 3 | 1 | 0 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` |
| mutation | 135 | 16 | 11 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` |
| dead_code | 24 | 7 | 3 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

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

- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **16.8** | LOC: 58
- `reportError` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java`) -> Impact: **14.8** | LOC: 19
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java`) -> Impact: **9.9** | LOC: 25
- `visitRpcParseStatement` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java`) -> Impact: **9.8** | LOC: 54
- `accept` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java`) -> Impact: **7.8** | LOC: 52
- `checkSubordinatesIdentifier2` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java`) -> Impact: **7.6** | LOC: 17
- `injectCopybook` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java`) -> Impact: **7.2** | LOC: 46
- `getInputMismatchMessage` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> Impact: **7.1** | LOC: 7
  * *Intent:* /** * Returns an input mismatch error message for a {@link InputMismatchException} * * @param recognizer parser reference * @param e {@link InputMisma...
- `activate` (@ `client/example-dialect-support/src/extension.ts`) -> Impact: **5.6** | LOC: 28
  * *Intent:* // This method is called when your extension is activated // Your extension is activated the very first time the command is executed
- `getExpectedText` (@ `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java`) -> Impact: **5.5** | LOC: 6

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `client/example-dialect-support` | 6 | 5019.62 | 0.0% | 0.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample` | 7 | 238.18 | 5.62% | 53.41% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor` | 4 | 94.0 | 9.44% | 8.04% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes` | 3 | 24.58 | 0.0% | 0.0% |
| `server/dialect-example` | 2 | 21.04 | 0.0% | 0.0% |
| `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility` | 1 | 19.5 | 0.0% | 0.0% |
| `client/example-dialect-support/snippets` | 1 | 15.96 | 0.0% | 0.0% |
| `client/example-dialect-support/src` | 1 | 15.36 | 16.25% | 88.08% |
| `client/example-dialect-support/syntaxes` | 1 | 15.34 | 0.0% | 0.0% |
| `__monolith__` | 1 | 2.1 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` -> **99.9834%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **97.0688%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **90.5672%** Exposure
- `client/example-dialect-support/src/extension.ts` -> **88.0797%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **48.4761%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **96.5861%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **56.062%** Exposure
- `client/example-dialect-support/src/extension.ts` -> **50.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **50.0%** Exposure
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java` -> **40.1312%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` -> **10** Orphaned Functions | **0** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` -> **4** Orphaned Functions | **0** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` -> **3** Orphaned Functions | **0** Duplicates
- `client/example-dialect-support/src/extension.ts` -> **2** Orphaned Functions | **0** Duplicates
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

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

### 1. `client/example-dialect-support/src/extension.ts` (TYPESCRIPT) -> Cumulative Risk: **499.7**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 15.36 | **LOC:** 44 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (88.0797%), Concurrency (76.8525%)
- **Heaviest Functions:** `activate` (Impact: 5.6), `deactivate` (Impact: 1.1)

### 2. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` (JAVA) -> Cumulative Risk: **423.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 48.32 | **LOC:** 116 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.5861%), Safety Score (87.3679%)
- **Heaviest Functions:** `accept` (Impact: 16.8), `checkSubordinatesIdentifier2` (Impact: 7.6), `getVariableUsageNode` (Impact: 2.3)

### 3. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA) -> Cumulative Risk: **368.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 15.84 | **LOC:** 57 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.0688%), Safety Score (52.1415%)
- **Heaviest Functions:** `visitInjectStatement` (Impact: 2.2), `addTreeNode` (Impact: 2.0), `aggregateResult` (Impact: 1.9)

### 4. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA) -> Cumulative Risk: **359.13**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 42.24 | **LOC:** 111 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (65.6347%), Tech Debt (48.4761%)
- **Heaviest Functions:** `reportError` (Impact: 14.8), `reportUnrecognizedException` (Impact: 3.7), `reportMissingToken` (Impact: 3.5)

### 5. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA) -> Cumulative Risk: **351.14**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 49.38 | **LOC:** 220 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9834%), Documentation (84.0%), Safety Score (53.0995%)
- **Heaviest Functions:** `visitRpcParseStatement` (Impact: 9.8), `visitUnsetStatement` (Impact: 2.3), `visitDataDescriptionEntry100` (Impact: 2.2)

### 6. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA) -> Cumulative Risk: **338.03**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 19.5 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Api Exposure (56.2499%), Safety Score (53.743%)
- **Heaviest Functions:** `addReplacementContext` (Impact: 2.2), `addReplacementContext` (Impact: 2.2), `constructLocality` (Impact: 2.1)

### 7. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA) -> Cumulative Risk: **323.88**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 12.76 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (62.5811%), State Flux (50.0%)
- **Heaviest Functions:** `RpcNode` (Impact: 4.1)

### 8. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java` (JAVA) -> Cumulative Risk: **316.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 15.84 | **LOC:** 80 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (58.0807%), Api Exposure (26.9398%)
- **Heaviest Functions:** `accept` (Impact: 7.8), `ProcessUnsetNode` (Impact: 1.6)

### 9. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` (JAVA) -> Cumulative Risk: **311.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 6.18 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (52.1415%), Api Exposure (45.034%)
- **Heaviest Functions:** `UnsetNode` (Impact: 1.9)

### 10. `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java` (JAVA) -> Cumulative Risk: **308.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 7.34 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (66.8476%), Tech Debt (32.1778%)
- **Heaviest Functions:** `generate` (Impact: 3.2)

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

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 63.48 | **LOC:** 299 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.4713%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `injectCopybook` (Impact: 7.2)
  * `getKeywords` (Impact: 3.6)
    * *Intent:* /** * Returns dialect keywords map where key is a keyword and a value is a description * * @return k...
  * `parseMyRule` (Impact: 2.8)
  * `extend` (Impact: 2.7)
    * *Intent:* /** * This implementation is specific to copybooks. * Use this when an external source content needs...
  * `processText` (Impact: 2.4)
    * *Intent:* /** * Processing the text * * @param context is a DialectProcessingContext class with all needed dat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 74`, `args: 17`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `api: 15`, `import: 25`
* *Defense:* `safety: 2`, `doc: 11`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 82.504
  * `Choke Point (Betweenness):` 0.013793 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 6):` com.google.common.collect.ImmutableList, com.google.common.collect.ImmutableMap, java.io.IOException, java.util.*, java.util.stream.Collectors, lombok.extern.slf4j.Slf4j, org.antlr.v4.runtime.CharStreams, org.antlr.v4.runtime.CommonTokenStream...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 49.38 | **LOC:** 220 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6344%), Tech Debt (99.9834%)
**Top Internal Functions/Classes:**
  * `visitRpcParseStatement` (Impact: 9.8)
  * `visitUnsetStatement` (Impact: 2.3)
  * `visitDataDescriptionEntry100` (Impact: 2.2)
  * `visitBitwiseShiftstatement` (Impact: 2.0)
  * `addTreeNode` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 51`, `args: 33`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 3`, `unreferenced_by_name: 10`
* *Architecture:* `api: 12`, `import: 24`
* *Defense:* `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` com.google.common.collect.ImmutableList, java.util.ArrayList, java.util.LinkedList, java.util.List, java.util.Objects, java.util.Optional.ofNullable, java.util.function.Function, java.util.stream.Collectors.toList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 48.32 | **LOC:** 116 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.8081%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 16.8)
  * `checkSubordinatesIdentifier2` (Impact: 7.6)
  * `getVariableUsageNode` (Impact: 2.3)
  * `ProcessRpcNode` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 24`, `args: 10`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 7`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.059259
  * `Imports (Out-Degree: 1):` java.util.Objects, java.util.Optional, java.util.Optional.ofNullable, org.broadcom.cobol.dialects.cobolExample.nodes.RpcNode, org.eclipse.lsp.cobol.common.error.ErrorSeverity.ERROR, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.message.MessageService...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ErrorMessageHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 47.38 | **LOC:** 150 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.3575%), Tech Debt (90.5672%)
**Top Internal Functions/Classes:**
  * `getInputMismatchMessage` (Impact: 7.1)
    * *Intent:* /** * Returns an input mismatch error message for a {@link InputMismatchException} * * @param recogn...
  * `getExpectedText` (Impact: 5.5)
  * `getUnwantedTokenMessage` (Impact: 5.4)
    * *Intent:* /** * Returns a message in case unwanted token found while parsing. * * @param recognizer Parser ref...
  * `removeIdentifierTokens` (Impact: 3.1)
  * `collectErrorTokens` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 27`, `args: 15`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 14`
* *Defense:* `doc: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.google.common.collect.ImmutableSet, java.util.Arrays, java.util.List, java.util.Optional, java.util.Set, java.util.stream.Collectors.joining, java.util.stream.Collectors.toList, org.antlr.v4.runtime.InputMismatchException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/CobolErrorStrategy.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 42.24 | **LOC:** 111 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.3305%), Tech Debt (48.4761%)
**Top Internal Functions/Classes:**
  * `reportError` (Impact: 14.8)
  * `reportUnrecognizedException` (Impact: 3.7)
  * `reportMissingToken` (Impact: 3.5)
  * `reportUnwantedToken` (Impact: 3.3)
  * `reportInputMismatch` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 22`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lombok.Getter, lombok.NoArgsConstructor, lombok.Setter, lombok.extern.slf4j.Slf4j, org.antlr.v4.runtime.*, org.eclipse.lsp.cobol.common.message.MessageService, org.eclipse.lsp.cobol.common.message.MessageServiceProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.5 | **LOC:** 73 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.8153%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 9.9)
  * `registerVariable` (Impact: 2.4)
  * `addError` (Impact: 2.3)
  * `ProcessLevel100Node` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 24`, `args: 8`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.059259
  * `Imports (Out-Degree: 1):` java.util.Optional, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.eclipse.lsp.cobol.common.error.ErrorSeverity.ERROR, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.message.MessageService, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.SectionType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.5 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addReplacementContext` (Impact: 2.2)
  * `addReplacementContext` (Impact: 2.2)
  * `constructLocality` (Impact: 2.1)
  * `constructRange` (Impact: 1.9)
  * `constructRange` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` lombok.experimental.UtilityClass, org.antlr.v4.runtime.ParserRuleContext, org.antlr.v4.runtime.tree.TerminalNode, org.eclipse.lsp.cobol.common.dialects.CobolDialect, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp4j.Location, org.eclipse.lsp4j.Position...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/FindInjectsCommand.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.98 | **LOC:** 64 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.5438%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `retrieveInjects` (Impact: 3.1)
  * `createCommand` (Impact: 2.1)
  * `collectCommandsOrActions` (Impact: 1.9)
    * *Intent:* /** * Create a list of commands or code actions according to the diagnostic's type. May be empty if ...
  * `toCodeAction` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 24`, `args: 7`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Arrays.asList, java.util.Collections.singletonList, java.util.List, java.util.function.Function, java.util.stream.Collectors.toList, lombok.NonNull, org.broadcom.cobol.dialects.cobolExample.ExampleDialect.MISSING_INJECTS, org.eclipse.lsp.cobol.common.action.CodeActionProvider...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/snippets/example-snippets.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.96 | **LOC:** 48 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/InjectRuleVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.84 | **LOC:** 57 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (97.0688%)
**Top Internal Functions/Classes:**
  * `visitInjectStatement` (Impact: 2.2)
  * `addTreeNode` (Impact: 2.0)
  * `aggregateResult` (Impact: 1.9)
  * `InjectRuleVisitor` (Impact: 1.6)
  * `defaultResult` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.google.common.collect.ImmutableList, java.util.ArrayList, java.util.List, java.util.function.Function, java.util.stream.Collectors.toList, java.util.stream.Stream, org.antlr.v4.runtime.ParserRuleContext, org.broadcom.cobol.dialects.cobolExample.utility.VisitorUtility...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessUnsetNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.84 | **LOC:** 80 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1466%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `accept` (Impact: 7.8)
  * `ProcessUnsetNode` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 21`, `args: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 1):` java.util.List, java.util.Optional, org.broadcom.cobol.dialects.cobolExample.nodes.UnsetNode, org.eclipse.lsp.cobol.common.error.ErrorSeverity.ERROR, org.eclipse.lsp.cobol.common.error.ErrorSource, org.eclipse.lsp.cobol.common.error.SyntaxError, org.eclipse.lsp.cobol.common.message.MessageService, org.eclipse.lsp.cobol.common.model.NodeType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `client/example-dialect-support/src/extension.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.36 | **LOC:** 44 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2465%), Tech Debt (88.0797%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 5.6)
    * *Intent:* // This method is called when your extension is activated // Your extension is activated the very fi...
  * `deactivate` (Impact: 1.1)
    * *Intent:* // This method is called when your extension is deactivated
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cobol-dialect-api, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/example-dialect-support/syntaxes/example.injection.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.34 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `client/example-dialect-support/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.28 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 12.76 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RpcNode` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.663
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.104167
  * `Imports (Out-Degree: 0):` lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `server/dialect-example/lombok.config` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `server/dialect-example/pom.xml` (XML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 102 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/Level100Transformer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7.34 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (32.1778%)
**Top Internal Functions/Classes:**
  * `generate` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lombok.AllArgsConstructor, lombok.Getter, org.broadcom.cobol.dialects.cobolExample.nodes.Level100Node, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.tree.variable.ElementaryItemNode, org.eclipse.lsp.cobol.common.model.tree.variable.GroupItemNode, org.eclipse.lsp.cobol.common.model.tree.variable.UsageFormat, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6.18 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UnsetNode` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 69.663
  * `Choke Point (Betweenness):` 0.010345 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` lombok.Getter, org.broadcom.cobol.dialects.cobolExample.ExampleDialect, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node, org.eclipse.lsp.cobol.common.model.tree.variable.VariableNameAndLocality
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.64 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Level100Node` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 89.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` lombok.Getter, org.eclipse.lsp.cobol.common.model.Locality, org.eclipse.lsp.cobol.common.model.NodeType, org.eclipse.lsp.cobol.common.model.tree.Node
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/DialectParserListener.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3.88 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DialectParserListener` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, lombok.Getter, org.antlr.v4.runtime.BaseErrorListener, org.eclipse.lsp.cobol.common.error.SyntaxError
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

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **Severity: 0.773** (Bridge: 0.0138 * Flux: 56.062%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 0.123** (Bridge: 0.0103 * Flux: 11.9203%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` -> **Severity: 6.952** (Embedded: 0.1333 * Error Risk: 52.1415%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **Severity: 6.519** (Embedded: 0.1042 * Error Risk: 62.5811%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 5.214** (Embedded: 0.1 * Error Risk: 52.1415%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessRpcNode.java` -> **Severity: 5.177** (Embedded: 0.0593 * Error Risk: 87.3679%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/ExampleDialect.java` -> **Severity: 3.631** (Embedded: 0.06 * Error Risk: 60.511%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/Level100Node.java` -> **Severity: 8946.2** (Blast Radius: 89.462 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/RpcNode.java` -> **Severity: 6966.3** (Blast Radius: 69.663 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/nodes/UnsetNode.java` -> **Severity: 6966.3** (Blast Radius: 69.663 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/utility/VisitorUtility.java` -> **Severity: 4804.1** (Blast Radius: 48.041 * Doc Risk: 100.0%)
- `server/dialect-example/src/main/java/org/broadcom/cobol/dialects/cobolExample/processor/ProcessLevel100Node.java` -> **Severity: 3498.0** (Blast Radius: 34.98 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
