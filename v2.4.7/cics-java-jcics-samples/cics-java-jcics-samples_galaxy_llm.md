# ARCHITECTURAL_BRIEF: cics-java-jcics-samples
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cics-java-jcics-samples` |
| **Timestamp** | `2026-08-07T03:50:50.277980+00:00` |
| **Scan Duration** | `0.27s` |
| **Git Branch** | `main` |
| **Git Commit** | `11e86326f2600220cc610bdf4bee9afa77c206c0` |
| **Git Remote** | `https://github.com/cicsdev/cics-java-jcics-samples.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 40 malicious artifacts.

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
| Total Artifacts | 207 |
| Analyzed Artifacts (Scanned) | 76 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 131 |
| Total LOC | 1985 |
| Volatility Index | 0.013 |
| % Scanned of codebase = | 36.7% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2825 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3908 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2924 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 37 | 1789 | 48.7% |
| MARKDOWN | 18 | 0 | 23.7% |
| XML | 12 | 0 | 15.8% |
| PLAINTEXT | 6 | 0 | 7.9% |
| COBOL | 2 | 164 | 2.6% |
| JCL | 1 | 32 | 1.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.133`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 33 | 43.4% |
| file_cluster_13 | 19 | 25.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 24 | 31.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 131*

**Composition by Extension & Reason:**
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.program`: 27x Excluded (Unsupported Extension: '.program')
- `.transaction`: 27x Excluded (Unsupported Extension: '.transaction')
- `.prefs`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.osgibundle`: 6x Excluded (Unsupported Extension: '.osgibundle')
- `.mf`: 6x Excluded (Unsupported Extension: '.MF')
- `.properties`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jar`: 4x Excluded (Explicitly Denied Extension: '.jar')
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 79.1 | 7.8 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 82.6 | 15.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 45.1 | 48.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 3.4 | 2.4 | 0.2 |
| API Exposure | 0.0 | 8.5 | 3.1 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.8 | 16.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.0 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 77.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 2.2 | 35.9 | 11.1 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `etc/VSAM/DEFVSAM.jcl` (Hits: 2)
- `MAINTAINERS.md` (Hits: 0)
- `README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **StockPartHelper.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java`) — 15 inbound connections
2. **VsamExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/VsamExampleCommon.java`) — 3 inbound connections
3. **KsdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) — 1 inbound connections
4. **MAINTAINERS.md** (`MAINTAINERS.md`) — 0 inbound connections
5. **README.md** (`README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **KsdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) — 16 outbound dependencies
2. **EsdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java`) — 13 outbound dependencies
3. **RrdsExampleCommon.java** (`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java`) — 13 outbound dependencies
4. **LinkProg3.java** (`projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg3.java`) — 12 outbound dependencies
5. **LinkServEduchan.java** (`projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` (@ `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java`) -> Impact: **37.1** | LOC: 57
  * *Intent:* /** * Name of the container which will contain the CICS return code * as a response from this program.
- `deleteRecord` (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) -> Impact: **30.4** | LOC: 72
- `main` (@ `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java`) -> Impact: **30.3** | LOC: 67
  * *Intent:* /** * The name of the lock used to protect the shared resource. * * The name is defined by an application and has no special meaning
- `deleteRecord` (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java`) -> Impact: **30.3** | LOC: 69
  * *Intent:* // Start the browse of the file
- `updateQueue` (@ `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample4.java`) -> Impact: **20.2** | LOC: 45
  * *Intent:* // Completion message
- `MAIN-PROCESSING` (@ `src/Cobol/EDUCHAN.cbl`) -> Impact: **18.6** | LOC: 71
- `browse` (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`) -> Impact: **18.4** | LOC: 56
- `browse` (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java`) -> Impact: **18.2** | LOC: 52
  * *Intent:* /** * Provides a simple example of reading a single record from a VSAM ESDS file. * * @param rba the RBA of the record to locate in the VSAM file. * *...
- `browse` (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java`) -> Impact: **18.2** | LOC: 52
- `emptyFile` (@ `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java`) -> Impact: **17.8** | LOC: 35

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq` | 5 | 177.72 | 8.86% | 23.49% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds` | 6 | 173.72 | 3.64% | 76.43% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds` | 6 | 168.52 | 3.73% | 65.58% |
| `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq` | 4 | 135.1 | 7.54% | 21.74% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds` | 6 | 128.2 | 4.08% | 80.89% |
| `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link` | 6 | 126.9 | 6.23% | 59.76% |
| `src/Cobol` | 2 | 65.88 | 68.79% | 92.34% |
| `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam` | 2 | 64.22 | 2.35% | 48.67% |
| `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize` | 1 | 63.82 | 8.23% | 100.0% |
| `projects/com.ibm.cicsdev.terminal/src/com/ibm/cicsdev/terminal` | 1 | 22.48 | 7.65% | 60.85% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java` -> **99.9994%** Exposure
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExample4.java` -> **99.4472%** Exposure
- `src/Cobol/EC01.cbl` -> **97.9026%** Exposure
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` -> **97.7023%** Exposure
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` -> **97.334%** Exposure
### Highest State Flux (Mutation/Volatility)
- `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample3.java` -> **99.7916%** Exposure
- `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample3.java` -> **99.7086%** Exposure
- `src/Cobol/EDUCHAN.cbl` -> **99.678%** Exposure
- `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` -> **98.8738%** Exposure
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` -> **96.934%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` -> **6** Orphaned Functions | **0** Duplicates
- `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java` -> **1** Orphaned Functions | **4** Duplicates
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java` -> **4** Orphaned Functions | **0** Duplicates
- `src/Cobol/EC01.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `src/Cobol/EDUCHAN.cbl` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java`** -> AI Confidence: **99.24%**
2. **`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java`** -> AI Confidence: **99.24%**
3. **`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java`** -> AI Confidence: **99.24%**
4. **`projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample4.java`** -> AI Confidence: **99.18%**
5. **`src/Cobol/EDUCHAN.cbl`** -> AI Confidence: **99.17%**
6. **`projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java`** -> AI Confidence: **99.16%**
7. **`projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample2.java`** -> AI Confidence: **99.15%**
8. **`projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg3.java`** -> AI Confidence: **99.08%**
9. **`projects/com.ibm.cicsdev.terminal/src/com/ibm/cicsdev/terminal/TerminalExample1.java`** -> AI Confidence: **99.06%**
10. **`projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample3.java`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `45` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `203` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Cobol/EDUCHAN.cbl` (COBOL) -> Cumulative Risk: **460.93**
- **Archetype:** `file_cluster_8` (Distance: 11.473 IQR)
- **Magnitude:** 43.94 | **LOC:** 173 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.678%), Tech Debt (86.7777%), Cognitive Load (79.0824%)
- **Heaviest Functions:** `MAIN-PROCESSING` (Impact: 18.6), `RESP-ERROR` (Impact: 3.2), `ABEND-ROUTINE` (Impact: 1.2)

### 2. `src/Cobol/EC01.cbl` (COBOL) -> Cumulative Risk: **432.36**
- **Archetype:** `file_cluster_8` (Distance: 9.295 IQR)
- **Magnitude:** 21.94 | **LOC:** 119 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.9026%), State Flux (81.4888%), Safety Score (64.0909%)
- **Heaviest Functions:** `A-CONTROL` (Impact: 7.7), `ZZX-CICS-ERROR-ROUTINE` (Impact: 4.8), `ZZX-EXIT` (Impact: 1.1)

### 3. `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` (JAVA) -> Cumulative Risk: **384.72**
- **Archetype:** `file_cluster_8` (Distance: 10.84 IQR)
- **Magnitude:** 52.04 | **LOC:** 235 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.334%), State Flux (96.934%), Safety Score (66.1635%)
- **Heaviest Functions:** `generate` (Impact: 4.6), `generateDescription` (Impact: 3.3), `getKey` (Impact: 3.0)

### 4. `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` (JAVA) -> Cumulative Risk: **374.38**
- **Archetype:** `file_cluster_13` (Distance: 11.645 IQR)
- **Magnitude:** 19.84 | **LOC:** 128 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.8738%), Tech Debt (97.7023%), Safety Score (50.5769%)
- **Heaviest Functions:** `linkProg` (Impact: 7.3), `buildCommarea` (Impact: 2.7), `LinkProg2` (Impact: 2.2)

### 5. `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java` (JAVA) -> Cumulative Risk: **345.14**
- **Archetype:** `file_cluster_13` (Distance: 10.765 IQR)
- **Magnitude:** 63.82 | **LOC:** 181 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9994%), Verification (80.0%), Safety Score (23.1475%)
- **Heaviest Functions:** `main` (Impact: 30.3), `acquireLock` (Impact: 10.7), `randomSleep` (Impact: 7.4)

### 6. `projects/com.ibm.cicsdev.terminal/src/com/ibm/cicsdev/terminal/TerminalExample1.java` (JAVA) -> Cumulative Risk: **324.11**
- **Archetype:** `file_cluster_13` (Distance: 9.663 IQR)
- **Magnitude:** 22.48 | **LOC:** 127 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (75.573%), Safety Score (62.5067%), Tech Debt (60.8539%)
- **Heaviest Functions:** `main` (Impact: 11.1), `parseTerminalString` (Impact: 5.7)

### 7. `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample3.java` (JAVA) -> Cumulative Risk: **322.65**
- **Archetype:** `file_cluster_13` (Distance: 11.302 IQR)
- **Magnitude:** 49.8 | **LOC:** 161 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7916%), Safety Score (60.5077%), Tech Debt (25.5132%)
- **Heaviest Functions:** `readFromQueue` (Impact: 11.8), `writeToQueue` (Impact: 9.7), `main` (Impact: 3.7)

### 8. `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample3.java` (JAVA) -> Cumulative Risk: **321.41**
- **Archetype:** `file_cluster_13` (Distance: 11.298 IQR)
- **Magnitude:** 48.56 | **LOC:** 153 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7086%), Safety Score (59.102%), Tech Debt (26.3198%)
- **Heaviest Functions:** `readFromQueue` (Impact: 11.8), `writeToQueue` (Impact: 9.7), `main` (Impact: 3.5)

### 9. `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample4.java` (JAVA) -> Cumulative Risk: **304.65**
- **Archetype:** `file_cluster_13` (Distance: 11.201 IQR)
- **Magnitude:** 39.3 | **LOC:** 130 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.4978%), Safety Score (43.6347%), Tech Debt (33.5856%)
- **Heaviest Functions:** `updateQueue` (Impact: 20.2), `main` (Impact: 3.8), `TSQExample4` (Impact: 2.2)

### 10. `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java` (JAVA) -> Cumulative Risk: **239.19**
- **Archetype:** `file_cluster_13` (Distance: 11.23 IQR)
- **Magnitude:** 83.1 | **LOC:** 269 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (66.8188%), State Flux (24.6011%), Safety Score (20.604%)
- **Heaviest Functions:** `browse` (Impact: 18.2), `addRecord` (Impact: 17.5), `readRecord` (Impact: 17.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.377 IQR)
- **Top Global Matches:** file_cluster_13: 11.377, file_cluster_8: 11.416, file_cluster_7: 11.781
- **Magnitude:** 130.68 | **LOC:** 389 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6288%), Tech Debt (68.1542%)
**Top Internal Functions/Classes:**
  * `deleteRecord` (Impact: 30.3)
    * *Intent:* // Start the browse of the file
  * `browse` (Impact: 18.2)
  * `emptyFile` (Impact: 17.8)
  * `readRecord` (Impact: 17.5)
  * `updateRecord` (Impact: 14.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 54`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `orphaned_logic: 6`
* *Architecture:* `api: 8`, `import: 13`
* *Defense:* `safety: 28`, `doc: 22`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.RRDS_Browse, com.ibm.cicsdev.bean.StockPart, com.ibm.cics.server.RecordHolder, com.ibm.cics.server.Task, com.ibm.cics.server.RRDS, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.EndOfFileException, com.ibm.cics.server.RecordNotFoundException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.154 IQR)
- **Top Global Matches:** file_cluster_13: 11.154, file_cluster_8: 11.306, file_cluster_7: 11.661
- **Magnitude:** 120.92 | **LOC:** 362 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1523%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteRecord` (Impact: 30.4)
  * `browse` (Impact: 18.4)
  * `readRecord` (Impact: 17.6)
  * `addRecord` (Impact: 17.5)
    * *Intent:* /**
  * `updateRecord` (Impact: 14.6)
    * *Intent:* // File not addable
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 53`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 12`, `import: 16`
* *Defense:* `safety: 24`, `doc: 20`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.692
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.013333
  * `Imports (Out-Degree: 2):` com.ibm.cicsdev.bean.StockPart, com.ibm.cics.server.RecordHolder, com.ibm.cics.server.KeyHolder, com.ibm.cics.server.Task, com.ibm.cics.server.KSDS, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.EndOfFileException, com.ibm.cics.server.KeyedFileBrowse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExampleCommon.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.23 IQR)
- **Top Global Matches:** file_cluster_13: 11.23, file_cluster_8: 11.44, file_cluster_7: 11.777
- **Magnitude:** 83.1 | **LOC:** 269 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4859%), Tech Debt (66.8188%)
**Top Internal Functions/Classes:**
  * `browse` (Impact: 18.2)
    * *Intent:* /** * Provides a simple example of reading a single record from a VSAM ESDS file. * * @param rba the...
  * `addRecord` (Impact: 17.5)
    * *Intent:* /** * A field to hold a reference to the VSAM ESDS file this * instance will access. */
  * `readRecord` (Impact: 17.5)
    * *Intent:* // Rewrite the record with the updated data
  * `updateRecord` (Impact: 14.4)
  * `EsdsExampleCommon` (Impact: 2.0)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 42`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 13`
* *Defense:* `safety: 17`, `doc: 18`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` com.ibm.cicsdev.bean.StockPart, com.ibm.cics.server.RecordHolder, com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.EndOfFileException, com.ibm.cics.server.ESDS_Browse, com.ibm.cics.server.RecordNotFoundException, java.util.List...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.serialize/src/com/ibm/cicsdev/serialize/SerializeExample1.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.765 IQR)
- **Top Global Matches:** file_cluster_13: 10.765, file_cluster_8: 10.876, file_cluster_7: 11.163
- **Magnitude:** 63.82 | **LOC:** 181 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2343%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 30.3)
    * *Intent:* /** * The name of the lock used to protect the shared resource. * * The name is defined by an applic...
  * `acquireLock` (Impact: 10.7)
    * *Intent:* // No clever exception handling here - keep it simple for demo purposes
  * `randomSleep` (Impact: 7.4)
    * *Intent:* /**
  * `randomSleep` (Impact: 3.2)
    * *Intent:* // Get details about our current CICS task
  * `doUpdate` (Impact: 2.4)
    * *Intent:* // Attempt to acquire the lock
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 18`, `args: 4`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 10`, `doc: 11`, `sync_locks: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.LengthErrorException, com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, java.util.concurrent.ThreadLocalRandom, com.ibm.cics.server.NameResource, com.ibm.cics.server.ResourceUnavailableException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEduchan.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.415 IQR)
- **Top Global Matches:** file_cluster_13: 10.415, file_cluster_8: 10.709, file_cluster_7: 11.027
- **Magnitude:** 56.14 | **LOC:** 184 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2937%), Tech Debt (21.7467%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 37.1)
    * *Intent:* /** * Name of the container which will contain the CICS return code * as a response from this progra...
  * `buildRcContainer` (Impact: 6.2)
  * `ReturnCode` (Impact: 2.1)
  * `getNumVal` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 23`, `args: 4`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 8`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, java.util.Date, com.ibm.cics.server.Channel, com.ibm.cics.server.ContainerErrorException, com.ibm.cics.server.CCSIDErrorException, java.nio.ByteBuffer, com.ibm.cics.server.ChannelErrorException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.84 IQR)
- **Top Global Matches:** file_cluster_8: 10.84, file_cluster_13: 10.893, file_cluster_7: 11.002
- **Magnitude:** 52.04 | **LOC:** 235 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (97.334%)
**Top Internal Functions/Classes:**
  * `generate` (Impact: 4.6)
    * *Intent:* // Key zero is for stock part with ID of zero
  * `generateDescription` (Impact: 3.3)
    * *Intent:* /** * Generate a StockPart object which contains random, but valid data. * * @return A newly-created...
  * `getKey` (Impact: 3.0)
  * `generateKey` (Impact: 2.9)
  * `getKeyZero` (Impact: 2.8)
    * *Intent:* /** * A selection of possible object types for the description. Maximum length should be 6 character...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `doc: 23`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 144.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.2
  * `Imports (Out-Degree: 0):` java.math.BigDecimal, java.util.Calendar, com.ibm.cicsdev.bean.StockPart, java.util.concurrent.ThreadLocalRandom
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample3.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.302 IQR)
- **Top Global Matches:** file_cluster_13: 11.302, file_cluster_8: 11.602, file_cluster_7: 11.908
- **Magnitude:** 49.8 | **LOC:** 161 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3894%), Tech Debt (25.5132%)
**Top Internal Functions/Classes:**
  * `readFromQueue` (Impact: 11.8)
    * *Intent:* // Write several items to the queue
  * `writeToQueue` (Impact: 9.7)
  * `main` (Impact: 3.7)
    * *Intent:* /** * Name of the TSQ to use.
  * `TSQExample3` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 29`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 4`, `doc: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, com.ibm.cics.server.TSQType, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.TSQ, com.ibm.cics.server.ItemHolder, com.ibm.cicsdev.bean.TsqRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample3.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.298 IQR)
- **Top Global Matches:** file_cluster_13: 11.298, file_cluster_8: 11.558, file_cluster_7: 11.863
- **Magnitude:** 48.56 | **LOC:** 153 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.7758%), Tech Debt (26.3198%)
**Top Internal Functions/Classes:**
  * `readFromQueue` (Impact: 11.8)
    * *Intent:* // Extract the byte data from the wrapper object
  * `writeToQueue` (Impact: 9.7)
  * `main` (Impact: 3.5)
  * `TDQExample3` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 28`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 4`, `doc: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cicsdev.bean.TdqRecord, com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.TDQ, com.ibm.cics.server.DataHolder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cobol/EDUCHAN.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.473 IQR)
- **Top Global Matches:** file_cluster_8: 11.473, file_cluster_12: 11.748, file_cluster_0: 11.785
- **Magnitude:** 43.94 | **LOC:** 173 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0824%), Tech Debt (86.7777%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCESSING` (Impact: 18.6)
  * `RESP-ERROR` (Impact: 3.2)
  * `ABEND-ROUTINE` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 7`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* None
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample2.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.407 IQR)
- **Top Global Matches:** file_cluster_13: 10.407, file_cluster_8: 10.506, file_cluster_7: 10.865
- **Magnitude:** 41.64 | **LOC:** 162 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3775%), Tech Debt (24.7664%)
**Top Internal Functions/Classes:**
  * `readFromQueue` (Impact: 13.8)
  * `writeToQueue` (Impact: 13.5)
  * `main` (Impact: 3.7)
    * *Intent:* /** * Number of items to write to the queue. */
  * `TSQExample2` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 21`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 8`, `doc: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, java.io.UnsupportedEncodingException, com.ibm.cics.server.TSQType, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.TSQ, com.ibm.cics.server.ItemHolder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample2.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.281 IQR)
- **Top Global Matches:** file_cluster_8: 10.281, file_cluster_13: 10.288, file_cluster_7: 10.656
- **Magnitude:** 40.4 | **LOC:** 154 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9471%), Tech Debt (25.5132%)
**Top Internal Functions/Classes:**
  * `readFromQueue` (Impact: 13.8)
  * `writeToQueue` (Impact: 13.5)
  * `main` (Impact: 3.5)
    * *Intent:* /** * Number of items to write to the queue. */
  * `TDQExample2` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 20`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 8`, `doc: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, java.io.UnsupportedEncodingException, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.TDQ, com.ibm.cics.server.DataHolder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample4.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.201 IQR)
- **Top Global Matches:** file_cluster_13: 11.201, file_cluster_8: 11.568, file_cluster_7: 11.892
- **Magnitude:** 39.3 | **LOC:** 130 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.2053%), Tech Debt (33.5856%)
**Top Internal Functions/Classes:**
  * `updateQueue` (Impact: 20.2)
    * *Intent:* // Completion message
  * `main` (Impact: 3.8)
    * *Intent:* /**
  * `TSQExample4` (Impact: 2.2)
    * *Intent:* // Update the TSQ with a browse and rewrite
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 24`, `args: 3`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 5`, `doc: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, com.ibm.cics.server.TSQType, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.TSQ, com.ibm.cics.server.ItemErrorException, com.ibm.cics.server.ItemHolder, com.ibm.cicsdev.bean.TsqRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample1.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.091 IQR)
- **Top Global Matches:** file_cluster_13: 10.091, file_cluster_8: 10.232, file_cluster_7: 10.593
- **Magnitude:** 32.3 | **LOC:** 134 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1374%), Tech Debt (33.5856%)
**Top Internal Functions/Classes:**
  * `readFromQueue` (Impact: 9.3)
    * *Intent:* // Write several items to the queue
  * `writeToQueue` (Impact: 9.0)
  * `main` (Impact: 3.7)
  * `TSQExample1` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 4`, `doc: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, com.ibm.cics.server.TSQType, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.TSQ, com.ibm.cics.server.ItemHolder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample1.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.923 IQR)
- **Top Global Matches:** file_cluster_13: 9.923, file_cluster_8: 9.944, file_cluster_7: 10.324
- **Magnitude:** 30.96 | **LOC:** 126 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.5903%), Tech Debt (35.1328%)
**Top Internal Functions/Classes:**
  * `readFromQueue` (Impact: 9.2)
    * *Intent:* // Construct a message for writing to the queue
  * `writeToQueue` (Impact: 9.0)
  * `main` (Impact: 3.5)
  * `TDQExample1` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 16`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 4`, `doc: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.TDQ, com.ibm.cics.server.DataHolder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.terminal/src/com/ibm/cicsdev/terminal/TerminalExample1.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.663 IQR)
- **Top Global Matches:** file_cluster_13: 9.663, file_cluster_8: 10.17, file_cluster_7: 10.425
- **Magnitude:** 22.48 | **LOC:** 127 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6456%), Tech Debt (60.8539%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 11.1)
  * `parseTerminalString` (Impact: 5.7)
    * *Intent:* // Completion message
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 16`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, java.util.StringTokenizer, com.ibm.cics.server.EndOfChainIndicatorException, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.TerminalPrincipalFacility, java.util.List, java.util.ArrayList, com.ibm.cics.server.DataHolder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cobol/EC01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.295 IQR)
- **Top Global Matches:** file_cluster_8: 9.295, file_cluster_12: 9.987, file_cluster_7: 10.098
- **Magnitude:** 21.94 | **LOC:** 119 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.4988%), Tech Debt (97.9026%)
**Top Internal Functions/Classes:**
  * `A-CONTROL` (Impact: 7.7)
  * `ZZX-CICS-ERROR-ROUTINE` (Impact: 4.8)
  * `ZZX-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 3`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExample5.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.732 IQR)
- **Top Global Matches:** file_cluster_8: 7.732, file_cluster_13: 7.925, file_cluster_7: 8.272
- **Magnitude:** 19.92 | **LOC:** 103 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.7675%), Tech Debt (67.3884%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.List, com.ibm.cicsdev.vsam.StockPartHelper, com.ibm.cicsdev.bean.StockPart, com.ibm.cics.server.Task
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg2.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.645 IQR)
- **Top Global Matches:** file_cluster_13: 11.645, file_cluster_8: 12.024, file_cluster_7: 12.244
- **Magnitude:** 19.84 | **LOC:** 128 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.2485%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `linkProg` (Impact: 7.3)
  * `buildCommarea` (Impact: 2.7)
    * *Intent:* /** * Main entry point to a CICS OSGi program.
  * `LinkProg2` (Impact: 2.2)
    * *Intent:* /** * Provides a simple example of LINKing to a CICS program using JCICS, * passing a byte array for...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 3`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 2`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cicsdev.bean.JZOSCommareaWrapper, com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.Program
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkProg3.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.27 IQR)
- **Top Global Matches:** file_cluster_13: 10.27, file_cluster_8: 10.447, file_cluster_7: 10.782
- **Magnitude:** 18.54 | **LOC:** 216 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5971%), Tech Debt (85.2622%)
**Top Internal Functions/Classes:**
  * `linkProg` (Impact: 7.2)
  * `buildChannel` (Impact: 7.2)
  * `LinkProg3` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `args: 3`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* `safety: 4`, `doc: 14`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.Channel, java.text.MessageFormat, com.ibm.cics.server.ContainerErrorException, com.ibm.cics.server.CCSIDErrorException, java.nio.ByteBuffer, com.ibm.cics.server.ChannelErrorException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExample5.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.649 IQR)
- **Top Global Matches:** file_cluster_8: 7.649, file_cluster_13: 7.881, file_cluster_7: 8.208
- **Magnitude:** 17.44 | **LOC:** 97 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1722%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.List, com.ibm.cicsdev.vsam.StockPartHelper, com.ibm.cicsdev.bean.StockPart, com.ibm.cics.server.Task
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `etc/VSAM/DEFVSAM.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.207 IQR)
- **Top Global Matches:** file_cluster_8: 5.207, file_cluster_7: 6.752, file_cluster_1: 6.871
- **Magnitude:** 15.64 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.5099%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQCommon.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.056 IQR)
- **Top Global Matches:** file_cluster_13: 10.056, file_cluster_8: 10.149, file_cluster_7: 10.534
- **Magnitude:** 15.18 | **LOC:** 75 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8517%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteQueue` (Impact: 9.2)
    * *Intent:* /** * Constructor used to initialise this class with some * common data used by all TDQ examples. * ...
  * `TDQCommon` (Impact: 2.4)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 10`, `args: 2`, `func_start: 3`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 3`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.InvalidQueueIdException, com.ibm.cics.server.Task, com.ibm.cics.server.CicsConditionException, java.text.MessageFormat, com.ibm.cics.server.TDQ
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExample5.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.714 IQR)
- **Top Global Matches:** file_cluster_8: 7.714, file_cluster_13: 7.914, file_cluster_7: 8.263
- **Magnitude:** 14.9 | **LOC:** 95 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8026%), Tech Debt (69.7059%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 12.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.List, com.ibm.cicsdev.vsam.StockPartHelper, com.ibm.cicsdev.bean.StockPart, com.ibm.cics.server.Task
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQCommon.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.387 IQR)
- **Top Global Matches:** file_cluster_13: 10.387, file_cluster_8: 10.392, file_cluster_7: 10.739
- **Magnitude:** 14.68 | **LOC:** 69 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1722%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteQueue` (Impact: 8.8)
    * *Intent:* /**
  * `TSQCommon` (Impact: 2.4)
    * *Intent:* /** * Superclass used to provide common services used in all of the TSQ * examples. * * For the sake...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 2`, `func_start: 3`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 3`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.CicsConditionException, com.ibm.cics.server.InvalidQueueIdException, com.ibm.cics.server.TSQ
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/com.ibm.cicsdev.link/src/com/ibm/cicsdev/link/LinkServEC01.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.704 IQR)
- **Top Global Matches:** file_cluster_13: 9.704, file_cluster_8: 9.885, file_cluster_7: 10.191
- **Magnitude:** 13.52 | **LOC:** 80 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3362%), Tech Debt (79.35%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 6`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.ibm.cics.server.Task, java.io.UnsupportedEncodingException, java.util.Date, com.ibm.cics.server.CommAreaHolder, java.text.SimpleDateFormat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQCommon.java` (JAVA) | Magnitude: 14.68 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, doc: 5, branch: 3
- `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample1.java` (JAVA) | Magnitude: 30.96 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 16, doc: 8, branch: 6
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/rrds/RrdsExampleCommon.java` (JAVA) | Magnitude: 130.68 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 167, structural_boundaries: 54, branch: 44, safety: 28
- `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQCommon.java` (JAVA) | Magnitude: 15.18 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, doc: 5, import: 5
- `projects/com.ibm.cicsdev.tsq/src/com/ibm/cicsdev/tsq/TSQExample2.java` (JAVA) | Magnitude: 41.64 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 21, branch: 10, doc: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `projects/com.ibm.cicsdev.tdq/src/com/ibm/cicsdev/tdq/TDQExample2.java` (JAVA) | Magnitude: 40.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 20, branch: 10, doc: 9
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` (JAVA) | Magnitude: 52.04 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, doc: 23, structural_boundaries: 21, state_mutation: 16
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExample5.java` (JAVA) | Magnitude: 19.92 | Delta: **0.193 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 9, branch: 5, import: 4
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/esds/EsdsExample1.java` (JAVA) | Magnitude: 5.96 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, import: 3, api: 2
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExample1.java` (JAVA) | Magnitude: 5.96 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, import: 3, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` -> **Severity: 0.003** (Bridge: 0.0002 * Flux: 18.7806%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` -> **Severity: 13.233** (Embedded: 0.2 * Error Risk: 66.1635%)
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` -> **Severity: 0.248** (Embedded: 0.0133 * Error Risk: 18.5966%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/StockPartHelper.java` -> **Severity: 1929.086** (Blast Radius: 144.039 * Doc Risk: 13.3928%)
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/VsamExampleCommon.java` -> **Severity: 433.911** (Blast Radius: 36.401 * Doc Risk: 11.9203%)
- `etc/VSAM/DEFVSAM.jcl` -> **Severity: 395.549** (Blast Radius: 11.012 * Doc Risk: 35.9198%)
- `src/Cobol/EC01.cbl` -> **Severity: 275.774** (Blast Radius: 11.012 * Doc Risk: 25.043%)
- `projects/com.ibm.cicsdev.vsam/src/com/ibm/cicsdev/vsam/ksds/KsdsExampleCommon.java` -> **Severity: 187.053** (Blast Radius: 15.692 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
