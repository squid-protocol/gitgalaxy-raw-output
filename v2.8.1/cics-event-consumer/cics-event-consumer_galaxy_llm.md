# ARCHITECTURAL_BRIEF: cics-event-consumer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cicsdev/cics-event-consumer` |
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
| Total Artifacts | 85 |
| Analyzed Artifacts (Scanned) | 52 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 33 |
| Total LOC | 6671 |
| Volatility Index | 0.019 |
| % Scanned of codebase = | 61.2% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.375 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 27 | 6370 | 51.9% |
| XML | 10 | 0 | 19.2% |
| PLAINTEXT | 5 | 0 | 9.6% |
| MARKDOWN | 4 | 0 | 7.7% |
| COBOL | 4 | 228 | 7.7% |
| SHELL | 1 | 22 | 1.9% |
| HTML | 1 | 51 | 1.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +0.61; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 42%, Interface Declarations Files 25%, Large Core Modules 21%, Generic / Templated Code Files 4%, Many-Argument Workhorses Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 43 | 82.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 17.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 33*

**Composition by Extension & Reason:**
- `.md`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.mf`: 1x Excluded (Unsupported Extension: '.MF')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 79.7 | 16.1 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 53.6 | 65.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 32.5 | 19.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 44.7 | 5.0 | 3.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.4 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.8 | 31.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 72.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 23.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 52 | 9 | 6 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` |
| cleanup | 10 | 4 | 0 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| guards | 669 | 25 | 35 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| danger | 654 | 22 | 38 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| concurrency | 19 | 9 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Email.java` |
| connectivity | 478 | 31 | 33 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java` |
| io | 39 | 10 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 18 | 4 | 0 | `examples/CA1YCOB3.cbl` |
| time | 1 | 1 | 0 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSHTTP.java` |
| serialization | 10 | 4 | 0 | `examples/CA1YCOB3.cbl` |
| regex | 21 | 5 | 0 | `examples/CA1YCOB3.cbl` |
| events | 51 | 11 | 3 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| tests | 0 | 0 | 0 | - |
| docs | 586 | 25 | 46 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java` |
| debt | 54 | 12 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| mutation | 1962 | 30 | 111 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| dead_code | 326 | 29 | 14 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java` |
| credential | 5 | 2 | 0 | `examples/ca1y.sh` |
| threat | 38 | 12 | 1 | `examples/emailTemplate.html` |
| ml_ai | 14 | 6 | 2 | `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java` (Hits: 16)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` (Hits: 6)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/MVSJob.java` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CHANGELOG.md** (`CHANGELOG.md`) — 1 inbound connections
2. **README.md** (`README.md`) — 1 inbound connections
3. **SUMMARY.md** (`SUMMARY.md`) — 1 inbound connections
4. **pom.xml** (`cics-event-consumer-bundle/pom.xml`) — 1 inbound connections
5. **pom.xml** (`cics-event-consumer-ca1y/pom.xml`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Emit.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) — 48 outbound dependencies
2. **Event.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java`) — 22 outbound dependencies
3. **SUMMARY.md** (`SUMMARY.md`) — 20 outbound dependencies
4. **ConvertFOP.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java`) — 19 outbound dependencies
5. **Email.java** (`cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Email.java`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveTokensInKey` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **502.0** | LOC: 727
  * *Intent:* * - The string to search for tokens * @param pattern * - The pattern to use to find tokens * @param props * - The properties to use as the lookup tabl...
- `getFileUsingFTP` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **233.1** | LOC: 170
  * *Intent:* * @param trustmgr * - * @param datatimeout * - * @param proxyserver * - * @param proxyusername * - * @param proxypassword * - * @param anonymouspasswo...
- `addPropertiesFromDFHEP_DESCRIPTOR` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **221.0** | LOC: 367
  * *Intent:* /** * Add name / value properties from contents of container DFHEP.DESCRIPTOR and business information items from * containers DFHEP.DATA.nnnnn * * @p...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv1.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `evaluateFormula` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java`) -> Impact: **62.0** | LOC: 96
  * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more arguments, and the first argument refers to a level...
- `callAdapters` **(Compute Cores)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **59.7** | LOC: 147
  * *Intent:* /** * Call a set of adapters in a pre-defined sequence providing the properties required by the adapter are present. * * @param props * - properties t...
- `emit` **(Many-Argument Workhorses)** (@ `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java`) -> Impact: **57.7** | LOC: 154
  * *Intent:* /** * Emit a message using configuration from a set of properties, and data from the CICS channel. * * @param props * - properties to use * @param cic...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y` | 15 | 3697.74 | 28.7% | 33.83% |
| `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface` | 5 | 1870.4 | 30.86% | 99.43% |
| `examples` | 10 | 106.52 | 5.4% | 0.0% |
| `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe` | 5 | 93.92 | 2.94% | 66.88% |
| `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web` | 3 | 86.64 | 13.1% | 18.93% |
| `examples/schemas` | 4 | 42.08 | 0.0% | 0.0% |
| `cics-event-consumer-ca1y/WebContent/WEB-INF` | 2 | 21.04 | 0.0% | 0.0% |
| `__monolith__` | 5 | 15.96 | 0.0% | 0.0% |
| `cics-event-consumer-bundle` | 1 | 10.52 | 0.0% | 0.0% |
| `cics-event-consumer-ca1y` | 1 | 10.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/ContextInfoType.java` -> **100.0%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` -> **99.9985%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java` -> **99.977%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv1.java` -> **99.9508%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java` -> **99.9432%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSHTTP.java` -> **99.9999%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java` -> **99.9994%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSFile.java` -> **99.9992%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java` -> **99.9873%** Exposure
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` -> **99.9758%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java` -> **73** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` -> **63** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv1.java` -> **61** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java` -> **37** Orphaned Functions | **0** Duplicates
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` -> **25** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `265` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Email.java` (JAVA) -> Cumulative Risk: **543.61**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.28)
- **Magnitude:** 135.86 | **LOC:** 367 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7848%), Concurrency (99.3902%), Safety Score (90.0792%)
- **Heaviest Functions:** `send` (I/O & Config Routines, Impact: 22.7), `addAttachments` (Compute Cores, Impact: 19.1), `getMessageSummary` (I/O & Config Routines, Impact: 11.1)

### 2. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java` (JAVA) -> Cumulative Risk: **519.6**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.02)
- **Magnitude:** 305.32 | **LOC:** 673 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9432%), State Flux (99.9363%), Safety Score (91.1532%)
- **Heaviest Functions:** `evaluateFormula` (Many-Argument Workhorses, Impact: 62.0), `wrappedGetNumber` (Defensive Guards, Impact: 8.8), `match` (Defensive Guards, Impact: 8.0)

### 3. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` (JAVA) -> Cumulative Risk: **519.11**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.10)
- **Magnitude:** 329.44 | **LOC:** 694 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9758%), Tech Debt (97.2561%), Safety Score (91.3594%)
- **Heaviest Functions:** `evaluateFormula` (Many-Argument Workhorses, Impact: 62.0), `setEpde__item` (Compute Cores, Impact: 9.7), `wrappedGetNumber` (Defensive Guards, Impact: 8.8)

### 4. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java` (JAVA) -> Cumulative Risk: **511.04**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.34)
- **Magnitude:** 154.58 | **LOC:** 357 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Safety Score (92.9629%), Tech Debt (92.6317%)
- **Heaviest Functions:** `getHexDump` (Many-Argument Workhorses, Impact: 21.6), `getChunks` (Defensive Guards, Impact: 13.9), `getChunks` (Defensive Guards, Impact: 13.9)

### 5. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` (JAVA) -> Cumulative Risk: **509.52**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.06)
- **Magnitude:** 377.46 | **LOC:** 885 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9985%), State Flux (99.7584%), Safety Score (86.6839%)
- **Heaviest Functions:** `evaluateFormula` (Many-Argument Workhorses, Impact: 62.0), `wrappedGetNumber` (Defensive Guards, Impact: 8.8), `match` (Defensive Guards, Impact: 8.0)

### 6. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv1.java` (JAVA) -> Cumulative Risk: **500.4**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.04)
- **Magnitude:** 409.86 | **LOC:** 1042 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9508%), State Flux (98.7042%), Safety Score (87.3038%)
- **Heaviest Functions:** `evaluateFormula` (Many-Argument Workhorses, Impact: 62.0), `wrappedGetNumber` (Defensive Guards, Impact: 8.8), `match` (Defensive Guards, Impact: 8.0)

### 7. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java` (JAVA) -> Cumulative Risk: **496.19**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.06)
- **Magnitude:** 448.32 | **LOC:** 1170 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.977%), State Flux (97.7465%), Safety Score (86.2839%)
- **Heaviest Functions:** `evaluateFormula` (Many-Argument Workhorses, Impact: 62.0), `wrappedGetNumber` (Defensive Guards, Impact: 8.8), `match` (Defensive Guards, Impact: 8.0)

### 8. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSQueue.java` (JAVA) -> Cumulative Risk: **491.65**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.78)
- **Magnitude:** 113.98 | **LOC:** 283 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9532%), Safety Score (94.1774%), Verification (80.0%)
- **Heaviest Functions:** `send` (I/O & Config Routines, Impact: 27.1), `CICSQueue` (Compute Cores, Impact: 19.1), `getMessageSummary` (Compute Cores, Impact: 14.2)

### 9. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSFile.java` (JAVA) -> Cumulative Risk: **479.82**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.18)
- **Magnitude:** 92.44 | **LOC:** 209 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Safety Score (93.615%), Documentation (80.0%)
- **Heaviest Functions:** `send` (I/O & Config Routines, Impact: 13.8), `CICSFile` (Defensive Guards, Impact: 13.0), `getMessageSummary` (Interface Declarations, Impact: 7.6)

### 10. `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` (JAVA) -> Cumulative Risk: **452.2**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.24)
- **Magnitude:** 290.52 | **LOC:** 725 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.925%), Safety Score (99.3366%), Verification (80.0%)
- **Heaviest Functions:** `getPropertySummary` (Compute Cores, Impact: 34.9), `setPropertyMimeDefault` (Compute Cores, Impact: 8.0), `setPropertyAttachment` (Compute Cores, Impact: 7.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2290.0 | **LOC:** 3009 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.7046%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveTokensInKey` **(Many-Argument Workhorses)** (Impact: 502.0)
    * *Intent:* * - The string to search for tokens * @param pattern * - The pattern to use to find tokens * @param ...
  * `getFileUsingFTP` **(Many-Argument Workhorses)** (Impact: 233.1)
    * *Intent:* * @param trustmgr * - * @param datatimeout * - * @param proxyserver * - * @param proxyusername * - *...
  * `addPropertiesFromDFHEP_DESCRIPTOR` **(Many-Argument Workhorses)** (Impact: 221.0)
    * *Intent:* /** * Add name / value properties from contents of container DFHEP.DESCRIPTOR and business informati...
  * `callAdapters` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* /** * Call a set of adapters in a pre-defined sequence providing the properties required by the adap...
  * `emit` **(Many-Argument Workhorses)** (Impact: 57.7)
    * *Intent:* /** * Emit a message using configuration from a set of properties, and data from the CICS channel. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 249 instances
* *State Mutation (weighted view):* 794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 219`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 207`, `high_risk_execution: 1`, `state_mutation: 296`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 11`, `import: 46`
* *Defense:* `safety: 117`, `doc: 42`, `immutability_locks: 46`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.515
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` com.fasterxml.jackson.databind.ObjectMapper, com.ibm.cics.ca1y.epadapterinterface.*, com.ibm.cics.server.*, com.ibm.cics.server.invocation.CICSProgram, com.ibm.etools.marshall.util.MarshallExternalDecimalUtils, com.ibm.etools.marshall.util.MarshallFloatUtils, com.ibm.etools.marshall.util.MarshallIntegerUtils, com.ibm.etools.marshall.util.MarshallPackedDecimalUtils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv2.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 448.32 | **LOC:** 1170 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.6124%), Tech Debt (99.977%)
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
  * `setEpcx__strucid` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* /** * @generated */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 131`, `args: 79`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 51`, `unreferenced_by_name: 73`
* *Architecture:* `io: 2`, `api: 80`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 86`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPCXv1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 409.86 | **LOC:** 1042 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.2418%), Tech Debt (99.9508%)
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
  * `setEpcx__strucid` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* /** * @generated */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 117`, `args: 67`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 49`, `unreferenced_by_name: 61`
* *Architecture:* `io: 2`, `api: 68`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 74`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/Epde_epde__item.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 377.46 | **LOC:** 885 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.5116%), Tech Debt (99.9985%)
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
  * `setEpde__dataname` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* /** * @generated */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 111`, `args: 69`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 41`, `unreferenced_by_name: 63`
* *Architecture:* `io: 2`, `api: 70`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 76`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPDEv1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 329.44 | **LOC:** 694 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.6458%), Tech Debt (97.2561%)
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `setEpde__item` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* /** * @generated */
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 91`, `args: 39`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 46`, `unreferenced_by_name: 25`
* *Architecture:* `io: 2`, `api: 40`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 46`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/epadapterinterface/EPAPv1.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 305.32 | **LOC:** 673 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.2857%), Tech Debt (99.9432%)
**Top Internal Functions/Classes:**
  * `evaluateFormula` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* * The val function returns the value of a field in the model. The val function takes one * or more a...
  * `wrappedGetNumber` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * @generated * wrappedGetNumber */
  * `match` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @generated */
  * `evaluateMap` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /** * @generated * evaluateMap */
  * `setEpap__strucid` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* /** * @generated */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 82`, `args: 43`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 38`, `unreferenced_by_name: 37`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 50`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.etools.marshall.util.*, java.beans.BeanInfo, java.beans.IntrospectionException, java.beans.Introspector, java.beans.PropertyDescriptor, java.lang.reflect.Method
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 290.52 | **LOC:** 725 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.2431%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPropertySummary` **(Compute Cores)** (Impact: 34.9)
    * *Intent:* /** * Summary of property. * * @param props * @param key * @return summary of the properties */
  * `setPropertyMimeDefault` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* /** * Associate the property with a MIME associated with the provided file name. * * @param key * - ...
  * `setPropertyAttachment` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /** * Associate the property key with an attachment. * * @param key * - property key * @param attach...
  * `setPropertyAlternateName` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /** * Associate the property key with an alternate name. * * @param key * - property key * @param at...
  * `setPropertyReturnContainer` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /** * Associate the property key with the name of a container. * * @param key * - property key * @pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 84`, `args: 28`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 26`
* *Architecture:* `api: 33`, `concurrency: 1`, `import: 9`
* *Defense:* `doc: 46`, `sync_locks: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.515
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` java.net.FileNameMap, java.net.URLConnection, java.util.Collections, java.util.Enumeration, java.util.Hashtable, java.util.LinkedHashMap, java.util.Map, java.util.Properties...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSHTTP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 178.78 | **LOC:** 380 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9049%), Tech Debt (17.287%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 51.5)
  * `getMessageSummary` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* /** * Return a short summary of the contents to be written to the queue. * * @return short summary o...
  * `CICSHTTP` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 35`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 16`, `doc: 13`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.HttpClientRequest, com.ibm.cics.server.HttpClientResponse, com.ibm.cics.server.HttpSession, com.ibm.cics.server.IOErrorException, com.ibm.cics.server.TimedOutException, java.net.URI, java.util.logging.Level, java.util.logging.Logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Util.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 154.58 | **LOC:** 357 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.7273%), Tech Debt (92.6317%)
**Top Internal Functions/Classes:**
  * `getHexDump` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* /** * Return a string of hexadecimal of byteArray with line separators suitable for trace. * * @para...
  * `getChunks` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* /** * Return an 2 dimensional array. The first ordinal is the number of chunks * the supplied string...
  * `getChunks` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* /** * Return an 2 dimensional array. The first ordinal is the number of chunks * the supplied byte a...
  * `loadProperties` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /* * Add name / value properties from the byte array. * * @param props - The properties to add to. *...
  * `getOptions` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* /** * Extract the command options from a string into an array. * * @param commandLine * - String in ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 44`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`, `unreferenced_by_name: 8`
* *Architecture:* `api: 12`, `import: 8`
* *Defense:* `safety: 10`, `doc: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.IsCICS, com.ibm.jzos.RcException, java.io.StringReader, java.util.Arrays, java.util.Date, java.util.Properties, javax.xml.bind.DatatypeConverter, org.apache.commons.io.IOUtils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Email.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 135.86 | **LOC:** 367 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2908%), Tech Debt (30.691%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 22.7)
    * *Intent:* /** * Send a mail using the information in properties. * * @return boolean - true if the mail was su...
  * `addAttachments` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* /** * Add attachments in the properties to the multipart message. * * @param multipart * - The multi...
  * `getMessageSummary` **(I/O & Config Routines)** (Impact: 11.1)
    * *Intent:* /** * Return a short text summary of the mail. * * @return short summary of the mail. */
  * `addBody` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * Add property mail.content to to the multipart message. * * @param multipart * - The multipart ...
  * `Email` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** * @author Mark Cocker <mark_cocker@uk.ibm.com> * @version 1.0 * @since 2012-02-10 * @param p * -...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 45`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 20`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 18`
* *Defense:* `safety: 6`, `doc: 21`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Date, java.util.Enumeration, java.util.logging.Level, java.util.logging.Logger, javax.activation.DataHandler, javax.mail.Authenticator, javax.mail.BodyPart, javax.mail.Message...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/MVSWriteToOperator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 116.54 | **LOC:** 247 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.9586%), Tech Debt (27.1931%)
**Top Internal Functions/Classes:**
  * `getDescriptorCode` **(Compute Cores)** (Impact: 42.3)
    * *Intent:* /** * Return an int representing the provided descriptor code. * * @param route * - number or string...
  * `getRouteCode` **(Compute Cores)** (Impact: 39.3)
    * *Intent:* /** * Return an int representing the provided route code. * * @param route * - number or string cons...
  * `send` **(I/O & Config Routines)** (Impact: 5.3)
  * `getMessageSummary` **(Interface Declarations)** (Impact: 4.7)
    * *Intent:* /** * Return a short summary of the WTO message. * * @return short summary of the WTO message. */
  * `MVSWriteToOperator` **(State Mutators)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 45`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 6`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.jzos.MvsConsole, com.ibm.jzos.WtoConstants, com.ibm.jzos.WtoMessage, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSQueue.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 113.98 | **LOC:** 283 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.4773%), Tech Debt (23.9082%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 27.1)
  * `CICSQueue` **(Compute Cores)** (Impact: 19.1)
  * `getMessageSummary` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* /** * Return a short summary of the contents to be written to the queue. * * @return short summary o...
  * `validForEmission` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 15`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 6`, `doc: 13`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.*, java.util.Arrays, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/CICSFile.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 92.44 | **LOC:** 209 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.1244%), Tech Debt (42.6996%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 13.8)
  * `CICSFile` **(Defensive Guards)** (Impact: 13.0)
  * `getMessageSummary` **(Interface Declarations)** (Impact: 7.6)
    * *Intent:* /** * Return a short summary of the contents to be written to the file. * * @return short summary of...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 14`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 6`, `doc: 12`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.*, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/JZOSFile.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 82.92 | **LOC:** 257 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.2796%), Tech Debt (26.3198%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 28.9)
  * `getMessageSummary` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* /** * Return a short summary of the contents to be written to the queue. * * @return short summary o...
  * `JZOSFile` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 11`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 12`, `doc: 10`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.jzos.ZFile, com.ibm.jzos.ZFileConstants, com.ibm.jzos.ZFileException, java.util.Arrays, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 76.1 | **LOC:** 178 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.0903%), Tech Debt (19.0407%)
**Top Internal Functions/Classes:**
  * `createEvent` **(Many-Argument Workhorses)** (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 31`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 5`, `import: 22`
* *Defense:* `safety: 3`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` com.ibm.cics.ca1y.Emit, com.ibm.cics.ca1y.EmitProperties, java.io.StringReader, java.util.Iterator, java.util.List, java.util.ResourceBundle, java.util.logging.Level, java.util.logging.Logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/ConvertFOP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 72.82 | **LOC:** 207 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.0825%), Tech Debt (15.7951%)
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* /** * Minimal test harness to convert a FO file to a PDF using the Java * command line. * * @param a...
  * `convertFOP` **(Many-Argument Workhorses)** (Impact: 12.7)
    * *Intent:* /** * Convert an XML or FO input stream to an output stream based on the specified xslt and target M...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 35`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 12`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 16`, `api: 4`, `import: 19`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.BufferedOutputStream, java.io.File, java.io.FileInputStream, java.io.FileOutputStream, java.io.InputStream, java.io.OutputStream, java.util.Arrays, java.util.List...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/JavaHTTP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 65.3 | **LOC:** 269 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.8934%), Tech Debt (28.905%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 25.8)
  * `getMessageSummary` **(Interface Declarations)** (Impact: 6.8)
    * *Intent:* /** * Return a short summary of the contents to be sent to the HTTP server. * * @return String */
  * `JavaHTTP` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit using this class. * * @return boolean */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 23`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 8`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 10`, `doc: 17`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.IOException, java.io.InputStream, java.nio.charset.StandardCharsets, java.util.Enumeration, java.util.logging.Level, java.util.logging.Logger, javax.ws.rs.client.Client, javax.ws.rs.client.ClientBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/XMPP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 55.68 | **LOC:** 158 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5141%), Tech Debt (66.6298%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 10.0)
  * `getMessageSummary` **(Compute Cores)** (Impact: 8.4)
  * `XMPP` **(I/O & Config Routines)** (Impact: 3.3)
  * `destroy` **(Interface Declarations)** (Impact: 2.2)
  * `processMessage` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 27`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `unreferenced_by_name: 3`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 4`, `doc: 3`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Properties, java.util.logging.Level, java.util.logging.Logger, org.jivesoftware.smack.Chat, org.jivesoftware.smack.ChatManager, org.jivesoftware.smack.ConnectionConfiguration, org.jivesoftware.smack.MessageListener, org.jivesoftware.smack.XMPPConnection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/ContextInfoType.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 49.42 | **LOC:** 241 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `setEventname` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the eventname property. * * @param value * allowed object is * {@link String...
  * `setUsertag` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the usertag property. * * @param value * allowed object is * {@link String }...
  * `setNetworkapplid` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the networkapplid property. * * @param value * allowed object is * {@link St...
  * `setTimestamp` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the timestamp property. * * @param value * allowed object is * {@link XMLGre...
  * `setBindingname` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the bindingname property. * * @param value * allowed object is * {@link Stri...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 14`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` javax.xml.bind.annotation.XmlAccessType, javax.xml.bind.annotation.XmlAccessorType, javax.xml.bind.annotation.XmlElement, javax.xml.bind.annotation.XmlSchemaType, javax.xml.bind.annotation.XmlType, javax.xml.datatype.XMLGregorianCalendar
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/MVSJob.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 36.48 | **LOC:** 141 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.0855%), Tech Debt (59.8339%)
**Top Internal Functions/Classes:**
  * `send` **(I/O & Config Routines)** (Impact: 9.8)
  * `getMessageSummary` **(Interface Declarations)** (Impact: 3.1)
    * *Intent:* /** * Return a short summary of the MVS job. * * @return short summary of the MVS job. */
  * `MVSJob` **(State Mutators)** (Impact: 1.6)
  * `validForEmission` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Return true if we should attempt to emit * * @return true if the entries in EmitProperties are...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 4`, `import: 6`
* *Defense:* `safety: 4`, `doc: 9`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.jzos.MvsJobSubmitter, java.io.IOException, java.util.Scanner, java.util.StringTokenizer, java.util.logging.Level, java.util.logging.Logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/ca1y.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 32.54 | **LOC:** 68 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.9915%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 3.7)
    * *Intent:* # Set Java environment if not already defined
  * `__global_context__` **(Unclassified)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/CA1YCOB3.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 20.88 | **LOC:** 141 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Main-program` **(I/O & Config Routines)** (Impact: 2.0)
  * `Main-program-exit` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/emailTemplate.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.02 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/Event.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.0 | **LOC:** 100 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8026%), Tech Debt (99.593%)
**Top Internal Functions/Classes:**
  * `setContextInfo` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the contextInfo property. * * @param value * allowed object is * {@link Cont...
  * `setPayloadData` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * Sets the value of the payloadData property. * * @param value * allowed object is * {@link Payl...
  * `getContextInfo` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /** * Gets the value of the contextInfo property. * * @return * possible object is * {@link ContextI...
  * `getPayloadData` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /** * Gets the value of the payloadData property. * * @return * possible object is * {@link PayloadD...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` javax.xml.bind.annotation.XmlAccessType, javax.xml.bind.annotation.XmlAccessorType, javax.xml.bind.annotation.XmlElement, javax.xml.bind.annotation.XmlRootElement, javax.xml.bind.annotation.XmlType
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics-event-consumer-ca1y/src/main/java/com/ibm/xmlns/prod/cics/events/cbe/package-info.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 11.04 | **LOC:** 10 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6291%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.905
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

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/EmitProperties.java` -> **Severity: 1.948** (Embedded: 0.0196 * Error Risk: 99.3366%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/Emit.java` -> **Severity: 1.923** (Embedded: 0.0196 * Error Risk: 98.0629%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/XMPP.java` -> **Severity: 1790.5** (Blast Radius: 17.905 * Doc Risk: 100.0%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/Event.java` -> **Severity: 1790.5** (Blast Radius: 17.905 * Doc Risk: 100.0%)
- `cics-event-consumer-ca1y/src/main/java/com/ibm/cics/ca1y/web/EventConfig.java` -> **Severity: 1790.5** (Blast Radius: 17.905 * Doc Risk: 100.0%)
- `examples/CA1YCOB1.cbl` -> **Severity: 1790.5** (Blast Radius: 17.905 * Doc Risk: 100.0%)
- `examples/CA1YCOB2.cbl` -> **Severity: 1790.5** (Blast Radius: 17.905 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
