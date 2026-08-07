# ARCHITECTURAL_BRIEF: pyasn1-modules
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pyasn1-modules` |
| **Timestamp** | `2026-08-07T05:25:12.178502+00:00` |
| **Scan Duration** | `0.84s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 271 malicious artifacts.

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
| Total Artifacts | 280 |
| Analyzed Artifacts (Scanned) | 276 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 21925 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2083 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9048 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 271 | 21925 | 98.2% |
| PLAINTEXT | 4 | 0 | 1.4% |
| MARKDOWN | 1 | 0 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.15`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 177 | 64.1% |
| file_cluster_13 | 94 | 34.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 37.2 | 4.7 | 4.4 | 0.0 |
| Error & Exception Exposure | 0.0 | 91.5 | 51.9 | 52.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 99.3 | 1.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.5 | 1.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.1 | 4.3 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 97.8 | 12.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 6.6 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.4 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.5 | 25.9 | 7.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyasn1_modules-0.4.2/tools/snmpget.py` (Hits: 10)
- `pyasn1_modules-0.4.2/tools/cmpdump.py` (Hits: 6)
- `pyasn1_modules-0.4.2/tools/ocspclient.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rfc2459.py** (`pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py`) — 5 inbound connections
2. **rfc2437.py** (`pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py`) — 1 inbound connections
3. **CHANGES.txt** (`pyasn1_modules-0.4.2/CHANGES.txt`) — 0 inbound connections
4. **LICENSE.txt** (`pyasn1_modules-0.4.2/LICENSE.txt`) — 0 inbound connections
5. **MANIFEST.in** (`pyasn1_modules-0.4.2/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_rfc2876.py** (`pyasn1_modules-0.4.2/tests/test_rfc2876.py`) — 7 outbound dependencies
2. **ocspclient.py** (`pyasn1_modules-0.4.2/tools/ocspclient.py`) — 7 outbound dependencies
3. **test_rfc2631.py** (`pyasn1_modules-0.4.2/tests/test_rfc2631.py`) — 6 outbound dependencies
4. **test_rfc2985.py** (`pyasn1_modules-0.4.2/tests/test_rfc2985.py`) — 6 outbound dependencies
5. **test_rfc2986.py** (`pyasn1_modules-0.4.2/tests/test_rfc2986.py`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `testDerCodec` (@ `pyasn1_modules-0.4.2/tests/test_rfc2985.py`) -> Impact: **42.0** | LOC: 113
- `testOpenTypes` (@ `pyasn1_modules-0.4.2/tests/test_rfc2985.py`) -> Impact: **40.5** | LOC: 82
- `testDerCodec` (@ `pyasn1_modules-0.4.2/tests/test_rfc3114.py`) -> Impact: **31.4** | LOC: 108
- `readPemBlocksFromFile` (@ `pyasn1_modules-0.4.2/pyasn1_modules/pem.py`) -> Impact: **20.5** | LOC: 29
  * *Intent:* # The markers parameters is in form ('start1', 'stop1'), ('start2', 'stop2')... # Return is (marker-index, substrate)
- `testDerCodec` (@ `pyasn1_modules-0.4.2/tests/test_rfc7229.py`) -> Impact: **19.5** | LOC: 44
- `testDerCodec` (@ `pyasn1_modules-0.4.2/tests/test_rfc5752.py`) -> Impact: **19.4** | LOC: 77
- `testDerCodec` (@ `pyasn1_modules-0.4.2/tests/test_rfc4073.py`) -> Impact: **16.3** | LOC: 48
- `testDerCodec` (@ `pyasn1_modules-0.4.2/tests/test_rfc5280.py`) -> Impact: **16.3** | LOC: 48
- `testDerCodec` (@ `pyasn1_modules-0.4.2/tests/test_rfc3852.py`) -> Impact: **15.9** | LOC: 76
- `testExtensionsMap` (@ `pyasn1_modules-0.4.2/tests/test_rfc3739.py`) -> Impact: **14.0** | LOC: 37

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyasn1_modules-0.4.2/pyasn1_modules` | 131 | 3856.96 | 5.88% | 2.07% |
| `pyasn1_modules-0.4.2/tests` | 125 | 3012.14 | 3.42% | 0.0% |
| `pyasn1_modules-0.4.2` | 6 | 23.0 | 0.83% | 0.0% |
| `pyasn1_modules-0.4.2/tools` | 14 | 0.29 | 5.85% | 7.09% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pyasn1_modules-0.4.2/tools/ocspclient.py` -> **99.2795%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/pem.py` -> **97.7023%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py` -> **88.5488%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc4210.py` -> **20.5776%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2251.py` -> **20.1995%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc5084.py` -> **97.8267%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc5751.py` -> **95.8661%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3537.py` -> **84.8129%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc5916.py` -> **84.8129%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc7633.py` -> **84.8129%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyasn1_modules-0.4.2/tests/test_rfc3279.py` -> **0** Orphaned Functions | **15** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc4055.py` -> **0** Orphaned Functions | **15** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc5280.py` -> **2** Orphaned Functions | **9** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc8419.py` -> **1** Orphaned Functions | **10** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc2459.py` -> **0** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pyasn1_modules-0.4.2/tests/test_rfc2985.py`** -> AI Confidence: **99.13%**
2. **`pyasn1_modules-0.4.2/tools/ocspclient.py`** -> AI Confidence: **99.08%**
3. **`pyasn1_modules-0.4.2/tests/test_rfc2876.py`** -> AI Confidence: **99.06%**
4. **`pyasn1_modules-0.4.2/pyasn1_modules/pem.py`** -> AI Confidence: **98.96%**
5. **`pyasn1_modules-0.4.2/tests/test_rfc2634.py`** -> AI Confidence: **98.96%**
6. **`pyasn1_modules-0.4.2/tests/test_rfc3739.py`** -> AI Confidence: **98.96%**
7. **`pyasn1_modules-0.4.2/tests/test_rfc3852.py`** -> AI Confidence: **98.96%**
8. **`pyasn1_modules-0.4.2/tests/test_rfc4043.py`** -> AI Confidence: **98.96%**
9. **`pyasn1_modules-0.4.2/tests/test_rfc4108.py`** -> AI Confidence: **98.96%**
10. **`pyasn1_modules-0.4.2/tests/test_rfc4334.py`** -> AI Confidence: **98.96%**
11. **`pyasn1_modules-0.4.2/tests/test_rfc4387.py`** -> AI Confidence: **98.96%**
12. **`pyasn1_modules-0.4.2/tests/test_rfc5035.py`** -> AI Confidence: **98.96%**
13. **`pyasn1_modules-0.4.2/tests/test_rfc5126.py`** -> AI Confidence: **98.96%**
14. **`pyasn1_modules-0.4.2/tests/test_rfc5275.py`** -> AI Confidence: **98.96%**
15. **`pyasn1_modules-0.4.2/tests/test_rfc5751.py`** -> AI Confidence: **98.96%**
16. **`pyasn1_modules-0.4.2/tests/test_rfc5755.py`** -> AI Confidence: **98.96%**
17. **`pyasn1_modules-0.4.2/tests/test_rfc5916.py`** -> AI Confidence: **98.96%**
18. **`pyasn1_modules-0.4.2/tests/test_rfc6187.py`** -> AI Confidence: **98.96%**
19. **`pyasn1_modules-0.4.2/tests/test_rfc6960.py`** -> AI Confidence: **98.96%**
20. **`pyasn1_modules-0.4.2/tests/test_rfc7191.py`** -> AI Confidence: **98.96%**
21. **`pyasn1_modules-0.4.2/tests/test_rfc7296.py`** -> AI Confidence: **98.96%**
22. **`pyasn1_modules-0.4.2/tests/test_rfc7894.py`** -> AI Confidence: **98.96%**
23. **`pyasn1_modules-0.4.2/tests/test_rfc8017.py`** -> AI Confidence: **98.96%**
24. **`pyasn1_modules-0.4.2/tests/test_rfc8520.py`** -> AI Confidence: **98.96%**
25. **`pyasn1_modules-0.4.2/tests/test_rfc3709.py`** -> AI Confidence: **98.94%**
26. **`pyasn1_modules-0.4.2/tests/test_rfc4476.py`** -> AI Confidence: **98.94%**
27. **`pyasn1_modules-0.4.2/tests/test_rfc5280.py`** -> AI Confidence: **98.94%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `pyasn1_modules-0.4.2/tools/ocspclient.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/pkcs1dump.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/pkcs8dump.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/x509dump-rfc5280.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/x509dump.py` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `926` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyasn1_modules-0.4.2/pyasn1_modules/pem.py` (PYTHON) -> Cumulative Risk: **606.45**
- **Archetype:** `file_cluster_8` (Distance: 9.335 IQR)
- **Magnitude:** 34.1 | **LOC:** 59 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Secrets Risk (99.97%), Tech Debt (97.7023%), Safety Score (72.6115%)
- **Heaviest Functions:** `readPemBlocksFromFile` (Impact: 20.5), `readPemFromFile` (Impact: 2.2), `readBase64fromText` (Impact: 1.8)

### 2. `pyasn1_modules-0.4.2/pyasn1_modules/rfc8226.py` (PYTHON) -> Cumulative Risk: **426.39**
- **Archetype:** `file_cluster_8` (Distance: 8.261 IQR)
- **Magnitude:** 26.2 | **LOC:** 150 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (84.6482%), Documentation (83.445%), State Flux (69.659%)
- **Heaviest Functions:** `_OID` (Impact: 7.4)

### 3. `pyasn1_modules-0.4.2/pyasn1_modules/rfc5084.py` (PYTHON) -> Cumulative Risk: **410.74**
- **Archetype:** `file_cluster_13` (Distance: 9.298 IQR)
- **Magnitude:** 19.32 | **LOC:** 98 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.8267%), Safety Score (83.4544%), Documentation (54.4954%)
- **Heaviest Functions:** `_OID` (Impact: 7.4)

### 4. `pyasn1_modules-0.4.2/tools/ocspclient.py` (PYTHON) -> Cumulative Risk: **405.2**
- **Archetype:** `file_cluster_8` (Distance: 8.202 IQR)
- **Magnitude:** 0.03 | **LOC:** 170 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Secrets Risk (100.0%), Tech Debt (99.2795%), Stability (50.0%)
- **Heaviest Functions:** `mkOcspRequest` (Impact: 11.1), `encodeValue` (Impact: 2.0), `encodeTag` (Impact: 1.8)

### 5. `pyasn1_modules-0.4.2/pyasn1_modules/rfc5751.py` (PYTHON) -> Cumulative Risk: **396.38**
- **Archetype:** `file_cluster_13` (Distance: 8.921 IQR)
- **Magnitude:** 20.48 | **LOC:** 125 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.8661%), Safety Score (85.2033%), Stability (50.0%)
- **Heaviest Functions:** `_OID` (Impact: 7.3)

### 6. `pyasn1_modules-0.4.2/pyasn1_modules/rfc4010.py` (PYTHON) -> Cumulative Risk: **395.13**
- **Archetype:** `file_cluster_13` (Distance: 8.182 IQR)
- **Magnitude:** 20.44 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (79.5168%), Safety Score (78.3421%), Documentation (69.1627%)

### 7. `pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py` (PYTHON) -> Cumulative Risk: **378.61**
- **Archetype:** `file_cluster_8` (Distance: 6.287 IQR)
- **Magnitude:** 19.88 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (88.5488%), Documentation (62.5136%), Safety Score (62.0622%)

### 8. `pyasn1_modules-0.4.2/pyasn1_modules/rfc5652.py` (PYTHON) -> Cumulative Risk: **374.18**
- **Archetype:** `file_cluster_8` (Distance: 6.754 IQR)
- **Magnitude:** 94.82 | **LOC:** 762 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.5565%), Safety Score (91.4611%), Stability (50.0%)
- **Heaviest Functions:** `_buildOid` (Impact: 7.4)

### 9. `pyasn1_modules-0.4.2/pyasn1_modules/rfc6031.py` (PYTHON) -> Cumulative Risk: **373.98**
- **Archetype:** `file_cluster_8` (Distance: 6.923 IQR)
- **Magnitude:** 65.16 | **LOC:** 470 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.5432%), Safety Score (89.5922%), Stability (50.0%)
- **Heaviest Functions:** `_OID` (Impact: 7.3)

### 10. `pyasn1_modules-0.4.2/pyasn1_modules/rfc3852.py` (PYTHON) -> Cumulative Risk: **373.82**
- **Archetype:** `file_cluster_8` (Distance: 6.744 IQR)
- **Magnitude:** 92.1 | **LOC:** 707 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.4657%), Safety Score (91.3812%), Stability (50.0%)
- **Heaviest Functions:** `_buildOid` (Impact: 7.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.917 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.741 IQR)
- **Top Global Matches:** file_cluster_8: 5.917, file_cluster_7: 7.095, file_cluster_1: 7.355
- **Magnitude:** 164.94 | **LOC:** 1340 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (9.7855%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 192`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 130`, `import: 8`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018701
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5280.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.262 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.468 IQR)
- **Top Global Matches:** file_cluster_8: 6.262, file_cluster_7: 7.313, file_cluster_1: 7.619
- **Magnitude:** 163.04 | **LOC:** 1659 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.162%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 282`, `args: 1`, `func_start: 1`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 132`, `state_mutation: 9`
* *Architecture:* `api: 126`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc3280.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.211 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.497 IQR)
- **Top Global Matches:** file_cluster_8: 6.211, file_cluster_7: 7.27, file_cluster_1: 7.577
- **Magnitude:** 159.2 | **LOC:** 1544 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0803%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 283`, `args: 1`, `func_start: 1`, `class_start: 127`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 6`
* *Architecture:* `api: 127`, `import: 7`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc2985.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.361 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.433 IQR)
- **Top Global Matches:** file_cluster_8: 8.361, file_cluster_13: 8.617, file_cluster_7: 9.01
- **Magnitude:** 100.42 | **LOC:** 320 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.5619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` (Impact: 42.0)
  * `testOpenTypes` (Impact: 40.5)
  * `setUp` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 37`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 4`, `import: 10`
* *Defense:* `doc: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pyasn1.type, unittest, pyasn1.codec.der.decoder, pyasn1_modules, pyasn1.codec.der.encoder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5652.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.754 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.357 IQR)
- **Top Global Matches:** file_cluster_8: 6.754, file_cluster_7: 7.724, file_cluster_13: 7.819
- **Magnitude:** 94.82 | **LOC:** 762 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6165%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 167`, `args: 1`, `func_start: 1`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 8`
* *Architecture:* `api: 70`, `import: 9`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc3852.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.744 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.3 IQR)
- **Top Global Matches:** file_cluster_8: 6.744, file_cluster_7: 7.72, file_cluster_13: 7.834
- **Magnitude:** 92.1 | **LOC:** 707 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 164`, `args: 1`, `func_start: 1`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 6`
* *Architecture:* `api: 70`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc2251.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.365 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.713 IQR)
- **Top Global Matches:** file_cluster_8: 6.365, file_cluster_7: 7.531, file_cluster_1: 7.768
- **Magnitude:** 72.88 | **LOC:** 564 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9928%), Tech Debt (20.1995%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 80`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 10`, `fragile_debt: 3`
* *Architecture:* `api: 49`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5934.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.516 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.145 IQR)
- **Top Global Matches:** file_cluster_8: 6.516, file_cluster_7: 7.548, file_cluster_1: 7.849
- **Magnitude:** 72.44 | **LOC:** 787 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.633%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 106`, `args: 1`, `func_start: 1`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 9`
* *Architecture:* `api: 46`, `import: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc5280.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.94%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.08 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.534 IQR)
- **Top Global Matches:** file_cluster_8: 9.08, file_cluster_13: 9.288, file_cluster_7: 9.487
- **Magnitude:** 72.16 | **LOC:** 254 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.357%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` (Impact: 16.3)
  * `testDerCodec` (Impact: 10.3)
    * *Intent:* """ def setUp(self): self.asn1Spec = rfc5280.CertificateList() def testDerCodec(self): substrate = p...
  * `testExtensionsMap` (Impact: 6.2)
  * `testDecodeOpenTypes` (Impact: 2.4)
  * `testDerCodec` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 35`, `args: 11`, `func_start: 11`, `class_start: 5`
* *Risk/State:* `state_mutation: 5`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 16`, `import: 7`
* *Defense:* `doc: 10`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pyasn1.type, unittest, pyasn1.codec.der.decoder, pyasn1_modules, pyasn1.codec.der.encoder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc3125.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.11 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.844 IQR)
- **Top Global Matches:** file_cluster_8: 6.11, file_cluster_7: 7.323, file_cluster_1: 7.56
- **Magnitude:** 69.72 | **LOC:** 470 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 75`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `api: 48`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5126.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.24 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.236 IQR)
- **Top Global Matches:** file_cluster_8: 6.24, file_cluster_13: 7.32, file_cluster_7: 7.376
- **Magnitude:** 69.34 | **LOC:** 578 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 94`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 2`
* *Architecture:* `api: 46`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4210.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.975 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.871 IQR)
- **Top Global Matches:** file_cluster_8: 6.975, file_cluster_7: 7.556, file_cluster_1: 7.788
- **Magnitude:** 66.7 | **LOC:** 804 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (20.5776%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 76`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 8`, `fragile_debt: 3`
* *Architecture:* `api: 43`, `import: 10`
* *Defense:* `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc3279.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.928 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.106 IQR)
- **Top Global Matches:** file_cluster_8: 7.928, file_cluster_13: 8.509, file_cluster_7: 8.529
- **Magnitude:** 65.18 | **LOC:** 386 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.6667%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` (Impact: 3.3)
  * `testDerCodec` (Impact: 3.2)
  * `testDerCodec` (Impact: 2.9)
  * `testDerCodec` (Impact: 2.8)
  * `testDerCodec` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 37`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `state_mutation: 5`, `duplicate_logic: 15`
* *Architecture:* `io: 1`, `api: 20`, `import: 8`
* *Defense:* `doc: 10`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pyasn1.type, unittest, pyasn1.codec.der.decoder, pyasn1_modules, pyasn1.codec.der.encoder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc6031.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.022 IQR)
- **Top Global Matches:** file_cluster_8: 6.923, file_cluster_13: 7.697, file_cluster_7: 7.855
- **Magnitude:** 65.16 | **LOC:** 470 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.0619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 120`, `args: 1`, `func_start: 1`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 7`
* *Architecture:* `api: 45`, `import: 10`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc6402.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.53 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.958 IQR)
- **Top Global Matches:** file_cluster_8: 6.53, file_cluster_7: 7.537, file_cluster_13: 7.55
- **Magnitude:** 61.42 | **LOC:** 629 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.7838%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 108`, `args: 1`, `func_start: 1`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 8`
* *Architecture:* `api: 38`, `import: 11`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc4055.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.036 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.611 IQR)
- **Top Global Matches:** file_cluster_8: 8.036, file_cluster_13: 8.49, file_cluster_7: 8.918
- **Magnitude:** 59.3 | **LOC:** 182 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4569%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testOpenTypes` (Impact: 2.7)
  * `testOpenTypes` (Impact: 2.4)
  * `testDerCodec` (Impact: 2.3)
  * `testDerCodec` (Impact: 2.2)
  * `testOpenTypes` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 37`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `state_mutation: 5`, `duplicate_logic: 15`
* *Architecture:* `io: 2`, `api: 20`, `import: 8`
* *Defense:* `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pyasn1.type, unittest, pyasn1_modules, pyasn1.codec.der
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc2315.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.193 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.895 IQR)
- **Top Global Matches:** file_cluster_8: 6.193, file_cluster_7: 7.327, file_cluster_1: 7.612
- **Magnitude:** 58.92 | **LOC:** 295 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 57`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 1`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pyasn1_modules.rfc2459
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc7906.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.827 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.986 IQR)
- **Top Global Matches:** file_cluster_8: 5.827, file_cluster_7: 7.077, file_cluster_13: 7.196
- **Magnitude:** 58.18 | **LOC:** 737 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 100`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 1`
* *Architecture:* `api: 34`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc7191.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.776 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.12 IQR)
- **Top Global Matches:** file_cluster_8: 7.776, file_cluster_13: 8.37, file_cluster_7: 8.427
- **Magnitude:** 56.86 | **LOC:** 314 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.4082%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testOpenTypes` (Impact: 7.0)
    * *Intent:* # Since receipt is inside an OCTET STRING, decodeOpenTypes=True cannot
  * `testOpenTypes` (Impact: 6.9)
  * `testDerCodec` (Impact: 6.6)
  * `testOpenTypes` (Impact: 6.1)
  * `testDerCodec` (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 9`
* *Architecture:* `io: 2`, `api: 12`, `import: 7`
* *Defense:* `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, unittest, pyasn1.codec.der.decoder, pyasn1_modules, pyasn1.codec.der.encoder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc5755.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.663 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.413 IQR)
- **Top Global Matches:** file_cluster_8: 7.663, file_cluster_13: 8.042, file_cluster_7: 8.325
- **Magnitude:** 51.84 | **LOC:** 212 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.1848%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` (Impact: 12.7)
  * `testOpenTypes` (Impact: 12.3)
  * `testOpenTypes` (Impact: 6.2)
  * `testDerCodec` (Impact: 4.7)
  * `setUp` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 36`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 8`, `import: 8`
* *Defense:* `doc: 4`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, unittest, pyasn1.codec.der.decoder, pyasn1_modules, pyasn1.codec.der.encoder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4211.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.834 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.699 IQR)
- **Top Global Matches:** file_cluster_8: 6.834, file_cluster_13: 7.68, file_cluster_7: 7.802
- **Magnitude:** 48.48 | **LOC:** 397 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1095%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 85`, `args: 1`, `func_start: 1`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 6`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc3370.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.931 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.424 IQR)
- **Top Global Matches:** file_cluster_8: 7.931, file_cluster_13: 8.248, file_cluster_7: 8.53
- **Magnitude:** 47.52 | **LOC:** 235 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.6371%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` (Impact: 10.6)
  * `testOpenTypes` (Impact: 6.0)
  * `testDerCodec` (Impact: 3.4)
  * `testOpenTypes` (Impact: 2.8)
  * `testDerCodec` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 32`, `args: 8`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 2`, `api: 11`, `import: 10`
* *Defense:* `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pyasn1.type, unittest, pyasn1.codec.der.decoder, pyasn1_modules, pyasn1.codec.der.encoder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4357.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.772 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.887 IQR)
- **Top Global Matches:** file_cluster_8: 5.772, file_cluster_7: 7.024, file_cluster_1: 7.28
- **Magnitude:** 46.7 | **LOC:** 478 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 67`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 1`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc3709.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.94%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.282 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.91 IQR)
- **Top Global Matches:** file_cluster_13: 9.282, file_cluster_8: 9.335, file_cluster_7: 9.786
- **Magnitude:** 46.26 | **LOC:** 195 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.5642%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` (Impact: 6.6)
  * `testDerCodec` (Impact: 6.6)
  * `testExtensionsMap` (Impact: 5.9)
  * `testExtensionsMap` (Impact: 5.9)
  * `setUp` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 22`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 8`, `import: 7`
* *Defense:* `doc: 4`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, unittest, pyasn1.codec.der.decoder, pyasn1_modules, pyasn1.codec.der.encoder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4108.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.117 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.185 IQR)
- **Top Global Matches:** file_cluster_8: 6.117, file_cluster_7: 7.249, file_cluster_13: 7.535
- **Magnitude:** 46.06 | **LOC:** 351 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 55`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 3`
* *Architecture:* `api: 24`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `pyasn1_modules-0.4.2/pyasn1_modules/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyasn1_modules-0.4.2/tests/test_rfc6955.py` (PYTHON) | Magnitude: 13.66 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 25, import: 10, test: 5
- `pyasn1_modules-0.4.2/tests/test_rfc2459.py` (PYTHON) | Magnitude: 34.82 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 24, api: 12, args: 9
- `pyasn1_modules-0.4.2/tests/test_rfc8702.py` (PYTHON) | Magnitude: 25.4 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 30, import: 12, test: 7
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3274.py` (PYTHON) | Magnitude: 18.42 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 6, import: 4, class_start: 2
- `pyasn1_modules-0.4.2/tests/test_rfc6019.py` (PYTHON) | Magnitude: 12.2 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 18, import: 7, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc6032.py` (PYTHON) | Magnitude: 19.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 9, import: 5, encapsulation: 4
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2876.py` (PYTHON) | Magnitude: 18.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 6, import: 4, encapsulation: 4
- `pyasn1_modules-0.4.2/tests/test_rfc3274.py` (PYTHON) | Magnitude: 12.98 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 18, import: 7, test: 5
- `pyasn1_modules-0.4.2/tools/pkcs10dump.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 11, import: 5, branch: 4
- `pyasn1_modules-0.4.2/tools/x509dump-rfc5280.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 11, import: 5, branch: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py` -> **Severity: 1.202** (Embedded: 0.0187 * Error Risk: 64.2597%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py` -> **Severity: 0.226** (Embedded: 0.0036 * Error Risk: 62.0622%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py` -> **Severity: 2062.527** (Blast Radius: 21.197 * Doc Risk: 97.3028%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py` -> **Severity: 410.339** (Blast Radius: 6.564 * Doc Risk: 62.5136%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2315.py` -> **Severity: 352.903** (Blast Radius: 3.548 * Doc Risk: 99.4652%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc5208.py` -> **Severity: 352.135** (Blast Radius: 3.548 * Doc Risk: 99.2488%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc5958.py` -> **Severity: 351.35** (Blast Radius: 3.548 * Doc Risk: 99.0276%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
