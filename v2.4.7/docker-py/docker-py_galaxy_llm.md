# ARCHITECTURAL_BRIEF: docker-py
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/docker-py` |
| **Timestamp** | `2026-08-07T03:59:54.739891+00:00` |
| **Scan Duration** | `0.4s` |
| **Git Branch** | `main` |
| **Git Commit** | `df3f8e2abc5a03de482e37214dddef9e0cee1bb1` |
| **Git Remote** | `https://github.com/docker/docker-py.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 82 malicious artifacts.

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
| Total Artifacts | 193 |
| Analyzed Artifacts (Scanned) | 95 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 98 |
| Total LOC | 8077 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 49.2% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6003 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4843 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6746 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 77 | 7816 | 81.1% |
| PLAINTEXT | 10 | 7 | 10.5% |
| MARKDOWN | 2 | 0 | 2.1% |
| DOCKERFILE | 2 | 36 | 2.1% |
| SHELL | 2 | 42 | 2.1% |
| MAKEFILE | 1 | 157 | 1.1% |
| JSON | 1 | 19 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.116`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 52 | 54.7% |
| file_cluster_13 | 26 | 27.4% |
| Unknown | 7 | 7.4% |
| file_cluster_0 | 4 | 4.2% |
| file_cluster_7 | 1 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 5.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 98*

**Composition by Extension & Reason:**
- `.py`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.ini')
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 96.4 | 16.5 | 9.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 38.9 | 50.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.1 | 2.6 | 80.0 |
| API Exposure | 0.0 | 12.2 | 5.0 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.4 | 43.8 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `docker/context/context.py` (Hits: 25)
- `docker/utils/socket.py` (Hits: 24)
- `docker/api/client.py` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **resource.py** (`docker/models/resource.py`) — 10 inbound connections
2. **api.py** (`docker/context/api.py`) — 9 inbound connections
3. **socket.py** (`docker/utils/socket.py`) — 5 inbound connections
4. **tls.py** (`docker/tls.py`) — 4 inbound connections
5. **context.py** (`docker/context/context.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **client.py** (`docker/api/client.py`) — 30 outbound dependencies
2. **client.py** (`docker/client.py`) — 14 outbound dependencies
3. **utils.py** (`docker/utils/utils.py`) — 14 outbound dependencies
4. **sshconn.py** (`docker/transport/sshconn.py`) — 13 outbound dependencies
5. **helpers.py** (`tests/helpers.py`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `docker/types/containers.py`) -> Impact: **1116.7** | LOC: 398
- `__init__` (@ `docker/types/services.py`) -> Impact: **189.9** | LOC: 93
- `_check_api_features` (@ `docker/api/service.py`) -> Impact: **119.7** | LOC: 92
- `logs` (@ `docker/api/container.py`) -> Impact: **112.1** | LOC: 54
- `__init__` (@ `docker/types/swarm.py`) -> Impact: **108.8** | LOC: 84
- `load_config` (@ `docker/auth.py`) -> Impact: **107.0** | LOC: 216
- `update_service` (@ `docker/api/service.py`) -> Impact: **101.6** | LOC: 86
- `__init__` (@ `docker/types/services.py`) -> Impact: **85.3** | LOC: 60
- `__init__` (@ `docker/api/client.py`) -> Impact: **81.5** | LOC: 105
- `parse_host` (@ `docker/utils/utils.py`) -> Impact: **68.5** | LOC: 89

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/unit/testdata/certs` | 3 | 15000.0 | 0.0% | 0.0% |
| `tests/ssh/config/client` | 2 | 10000.0 | 0.0% | 0.0% |
| `tests/ssh/config/server` | 2 | 10000.0 | 0.0% | 0.0% |
| `docker/types` | 8 | 2189.16 | 16.52% | 62.24% |
| `docker/api` | 13 | 1887.44 | 7.96% | 11.3% |
| `docker/utils` | 10 | 1035.64 | 21.22% | 29.62% |
| `docker/models` | 12 | 941.14 | 18.23% | 24.88% |
| `docker` | 7 | 546.72 | 23.42% | 17.71% |
| `docker/transport` | 6 | 513.5 | 26.87% | 66.2% |
| `docker/context` | 4 | 346.66 | 27.34% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docker/errors.py` -> **100.0%** Exposure
- `docker/types/healthcheck.py` -> **100.0%** Exposure
- `scripts/release.sh` -> **100.0%** Exposure
- `docker/types/networks.py` -> **99.9999%** Exposure
- `docker/utils/decorators.py` -> **99.9994%** Exposure
### Highest State Flux (Mutation/Volatility)
- `docker/credentials/utils.py` -> **100.0%** Exposure
- `docker/utils/build.py` -> **100.0%** Exposure
- `docker/utils/decorators.py` -> **100.0%** Exposure
- `scripts/release.sh` -> **100.0%** Exposure
- `docker/transport/basehttpadapter.py` -> **99.9997%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `docker/types/containers.py` -> **0** Orphaned Functions | **23** Duplicates
- `docker/types/services.py` -> **0** Orphaned Functions | **16** Duplicates
- `docker/errors.py` -> **0** Orphaned Functions | **15** Duplicates
- `tests/helpers.py` -> **12** Orphaned Functions | **2** Duplicates
- `docker/types/healthcheck.py` -> **0** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`docker/utils/build.py`** -> AI Confidence: **99.31%**
2. **`docker/utils/utils.py`** -> AI Confidence: **99.31%**
3. **`tests/Dockerfile`** -> AI Confidence: **99.29%**
4. **`docker/api/service.py`** -> AI Confidence: **99.29%**
5. **`scripts/release.sh`** -> AI Confidence: **99.29%**
6. **`docker/models/images.py`** -> AI Confidence: **99.24%**
7. **`docker/transport/sshconn.py`** -> AI Confidence: **99.24%**
8. **`docker/types/containers.py`** -> AI Confidence: **99.23%**
9. **`docker/transport/npipesocket.py`** -> AI Confidence: **99.18%**
10. **`docker/types/swarm.py`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `155` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `docker/errors.py` (PYTHON) -> Cumulative Risk: **606.2**
- **Archetype:** `file_cluster_8` (Distance: 11.327 IQR)
- **Magnitude:** 145.58 | **LOC:** 210 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9194%), Documentation (99.1833%)
- **Heaviest Functions:** `create_api_error_from_http_exception` (Impact: 14.7), `__str__` (Impact: 11.3), `__init__` (Impact: 8.5)

### 2. `docker/transport/sshconn.py` (PYTHON) -> Cumulative Risk: **598.15**
- **Archetype:** `file_cluster_13` (Distance: 11.195 IQR)
- **Magnitude:** 191.26 | **LOC:** 251 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9902%), Tech Debt (99.9612%), Documentation (83.0971%)
- **Heaviest Functions:** `_create_paramiko_client` (Impact: 18.8), `get_connection` (Impact: 13.3), `_get_conn` (Impact: 9.6)

### 3. `docker/utils/decorators.py` (PYTHON) -> Cumulative Risk: **590.96**
- **Archetype:** `file_cluster_13` (Distance: 10.365 IQR)
- **Magnitude:** 81.46 | **LOC:** 46 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9994%), Documentation (99.8122%)
- **Heaviest Functions:** `wrapped` (Impact: 11.7), `check_resource` (Impact: 9.4), `decorator` (Impact: 9.3)

### 4. `docker/utils/build.py` (PYTHON) -> Cumulative Risk: **560.9**
- **Archetype:** `file_cluster_13` (Distance: 10.096 IQR)
- **Magnitude:** 234.56 | **LOC:** 261 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.2229%), Verification (80.0%)
- **Heaviest Functions:** `create_archive` (Impact: 46.6), `walk` (Impact: 26.0), `rec_walk` (Impact: 25.8)

### 5. `scripts/release.sh` (SHELL) -> Cumulative Risk: **542.07**
- **Archetype:** `file_cluster_8` (Distance: 12.062 IQR)
- **Magnitude:** 4.86 | **LOC:** 42 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.5424%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 14.8), `Anonymous_Block` (Impact: 9.4), `Anonymous_Block` (Impact: 5.2)

### 6. `docker/transport/npipesocket.py` (PYTHON) -> Cumulative Risk: **539.74**
- **Archetype:** `file_cluster_0` (Distance: 10.661 IQR)
- **Magnitude:** 194.86 | **LOC:** 231 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9962%), Tech Debt (97.2598%), State Flux (80.5248%)
- **Heaviest Functions:** `recv_into` (Impact: 15.1), `connect` (Impact: 9.5), `settimeout` (Impact: 9.1)

### 7. `docker/transport/unixconn.py` (PYTHON) -> Cumulative Risk: **526.17**
- **Archetype:** `file_cluster_13` (Distance: 10.201 IQR)
- **Magnitude:** 49.16 | **LOC:** 87 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9963%), State Flux (99.9286%), Documentation (93.403%)
- **Heaviest Functions:** `get_connection` (Impact: 6.7), `__init__` (Impact: 5.5), `__init__` (Impact: 2.8)

### 8. `docker/models/resource.py` (PYTHON) -> Cumulative Risk: **524.91**
- **Archetype:** `file_cluster_0` (Distance: 13.216 IQR)
- **Magnitude:** 71.06 | **LOC:** 93 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Tech Debt (99.9871%), Documentation (99.5625%)
- **Heaviest Functions:** `prepare_model` (Impact: 7.5), `__init__` (Impact: 5.0), `__call__` (Impact: 4.3)

### 9. `docker/context/context.py` (PYTHON) -> Cumulative Risk: **503.78**
- **Archetype:** `file_cluster_0` (Distance: 10.562 IQR)
- **Magnitude:** 190.3 | **LOC:** 250 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (90.7344%), State Flux (83.6925%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 28.6), `_load_certs` (Impact: 18.6), `_load_meta` (Impact: 13.4)

### 10. `docker/utils/ports.py` (PYTHON) -> Cumulative Risk: **489.95**
- **Archetype:** `file_cluster_8` (Distance: 8.652 IQR)
- **Magnitude:** 68.3 | **LOC:** 84 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9881%), Verification (80.0%), Documentation (67.3604%)
- **Heaviest Functions:** `_raise_invalid_port` (Impact: 38.6), `add_port` (Impact: 10.4), `add_port_mapping` (Impact: 6.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/ssh/config/client/id_rsa` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ssh/config/client/id_rsa.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ssh/config/server/known_ed25519.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ssh/config/server/unknown_ed25519.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit/testdata/certs/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit/testdata/certs/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/unit/testdata/certs/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/types/containers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.812 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.73 IQR)
- **Top Global Matches:** file_cluster_8: 10.812, file_cluster_0: 11.0, file_cluster_7: 11.254
- **Magnitude:** 1272.22 | **LOC:** 791 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.1111%), Tech Debt (99.9528%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1116.7)
  * `__init__` (Impact: 20.8)
  * `__init__` (Impact: 11.1)
  * `__init__` (Impact: 7.5)
  * `host_config_version_error` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 65`, `args: 30`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 12`, `duplicate_logic: 23`
* *Architecture:* `api: 33`, `import: 4`
* *Defense:* `safety: 51`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .base, docker.types, .., ..utils.utils, .healthcheck
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/types/services.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.95 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.52 IQR)
- **Top Global Matches:** file_cluster_8: 10.95, file_cluster_0: 11.1, file_cluster_7: 11.223
- **Magnitude:** 626.66 | **LOC:** 871 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.3492%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 189.9)
  * `__init__` (Impact: 85.3)
  * `__init__` (Impact: 38.3)
  * `__init__` (Impact: 30.7)
  * `__init__` (Impact: 28.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 89`, `args: 25`, `func_start: 25`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 34`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `api: 25`, `import: 3`
* *Defense:* `safety: 21`, `doc: 34`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., ..utils, ..constants
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/api/container.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.618 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.599 IQR)
- **Top Global Matches:** file_cluster_8: 9.618, file_cluster_7: 9.847, file_cluster_0: 9.997
- **Magnitude:** 427.7 | **LOC:** 1349 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.9316%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `logs` (Impact: 112.1)
  * `containers` (Impact: 47.6)
  * `attach` (Impact: 32.4)
  * `create_container` (Impact: 27.5)
  * `stats` (Impact: 25.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 72`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `fragile_debt: 2`
* *Architecture:* `api: 43`, `import: 4`
* *Defense:* `safety: 10`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014184
  * `Imports (Out-Degree: 0):` .., ..constants, datetime, ..types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/utils/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.548 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.884 IQR)
- **Top Global Matches:** file_cluster_8: 10.548, file_cluster_13: 10.671, file_cluster_17: 10.888
- **Magnitude:** 372.78 | **LOC:** 518 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.2801%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_host` (Impact: 68.5)
  * `convert_volume_binds` (Impact: 37.2)
  * `parse_bytes` (Impact: 27.9)
  * `parse_env_file` (Impact: 25.4)
  * `_convert_port_binding` (Impact: 22.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 95`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 15`
* *Architecture:* `io: 8`, `api: 39`, `import: 14`
* *Defense:* `safety: 24`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` urllib.parse, json, string, os.path, itertools, ..constants, ..tls, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/api/client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.558 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.235 IQR)
- **Top Global Matches:** file_cluster_13: 11.558, file_cluster_0: 11.918, file_cluster_8: 12.085
- **Magnitude:** 335.76 | **LOC:** 533 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.5132%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 81.5)
  * `_read_from_socket` (Impact: 23.1)
    * *Intent:* """A generator of multiplexed data blocks coming from a response stream."""
  * `_stream_helper` (Impact: 17.1)
  * `_post_json` (Impact: 16.4)
  * `_get_result_tty` (Impact: 14.2)
    * *Intent:* # Wait for all frames, concatenate them, and return the result return consume_socket_output(gen, dem...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 139`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 49`, `dead_code: 1`
* *Architecture:* `io: 19`, `api: 12`, `import: 31`
* *Defense:* `safety: 34`, `doc: 20`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.217
  * `Choke Point (Betweenness):` 0.001544 | `Ripple Effect (Closeness):` 0.010638
  * `Imports (Out-Degree: 13):` ..transport, .container, ..utils.socket, ..utils.json_stream, .network, ..utils.proxy, requests.exceptions, .exec_api...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/models/containers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.272 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.397 IQR)
- **Top Global Matches:** file_cluster_13: 11.272, file_cluster_8: 11.321, file_cluster_7: 11.458
- **Magnitude:** 298.52 | **LOC:** 1199 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.1136%), Tech Debt (26.6607%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 65.5)
  * `_create_container_args` (Impact: 37.6)
    * *Intent:* """ Start this container. Similar to the ``docker start`` command, but doesn't support attach option...
  * `list` (Impact: 21.9)
  * `exec_run` (Impact: 12.7)
  * `_host_volume_from_bind` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 100`, `args: 35`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`, `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 40`, `import: 10`
* *Defense:* `safety: 10`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.217
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.010638
  * `Imports (Out-Degree: 3):` ..api, ntpath, ..types, copy, .resource, ..constants, ..utils, .images...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/api/service.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.711 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.072 IQR)
- **Top Global Matches:** file_cluster_8: 8.711, file_cluster_7: 9.093, file_cluster_0: 9.177
- **Magnitude:** 297.08 | **LOC:** 487 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5323%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_api_features` (Impact: 119.7)
  * `update_service` (Impact: 101.6)
  * `_merge_task_template` (Impact: 14.5)
  * `services` (Impact: 10.7)
  * `service_logs` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 25`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `safety: 6`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014184
  * `Imports (Out-Degree: 0):` .., ..types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/utils/build.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.096 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.47 IQR)
- **Top Global Matches:** file_cluster_13: 10.096, file_cluster_8: 10.228, file_cluster_17: 10.494
- **Magnitude:** 234.56 | **LOC:** 261 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2522%), Tech Debt (96.2229%)
**Top Internal Functions/Classes:**
  * `create_archive` (Impact: 46.6)
  * `walk` (Impact: 26.0)
  * `rec_walk` (Impact: 25.8)
  * `matches` (Impact: 21.7)
  * `tar` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 53`, `args: 17`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 22`, `duplicate_logic: 4`
* *Architecture:* `io: 16`, `api: 18`, `import: 7`
* *Defense:* `safety: 4`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.407
  * `Choke Point (Betweenness):` 0.000343 | `Ripple Effect (Closeness):` 0.023936
  * `Imports (Out-Degree: 1):` tempfile, tarfile, .fnmatch, ..constants, re, io, os
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docker/api/image.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.121 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.381 IQR)
- **Top Global Matches:** file_cluster_8: 9.121, file_cluster_7: 9.407, file_cluster_13: 9.649
- **Magnitude:** 233.26 | **LOC:** 602 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5617%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `import_image` (Impact: 35.6)
  * `images` (Impact: 33.0)
  * `pull` (Impact: 32.2)
  * `push` (Impact: 17.4)
  * `_import_image_params` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 56`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* `io: 2`, `api: 32`, `import: 5`
* *Defense:* `safety: 5`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014184
  * `Imports (Out-Degree: 0):` ..constants, .., from., from, os, logging
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/auth.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.886 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.808 IQR)
- **Top Global Matches:** file_cluster_8: 10.886, file_cluster_13: 10.967, file_cluster_0: 11.001
- **Magnitude:** 231.1 | **LOC:** 379 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5505%), Tech Debt (23.9787%)
**Top Internal Functions/Classes:**
  * `load_config` (Impact: 107.0)
  * `parse_auth` (Impact: 22.4)
    * *Intent:* """ Parses authentication entries Args: entries: Dict of authentication entries. raise_on_error: If ...
  * `resolve_repository_name` (Impact: 11.0)
  * `get_config_header` (Impact: 9.7)
  * `split_repo_name` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 78`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 33`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 22`, `import: 5`
* *Defense:* `safety: 11`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base64, json, .utils, , logging
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/transport/npipesocket.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.661 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.452 IQR)
- **Top Global Matches:** file_cluster_0: 10.661, file_cluster_13: 10.732, file_cluster_8: 10.943
- **Magnitude:** 194.86 | **LOC:** 231 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.0527%), Tech Debt (97.2598%)
**Top Internal Functions/Classes:**
  * `recv_into` (Impact: 15.1)
  * `connect` (Impact: 9.5)
  * `settimeout` (Impact: 9.1)
  * `send` (Impact: 8.7)
  * `makefile` (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 73`, `args: 36`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 16`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 59`, `import: 8`
* *Defense:* `safety: 8`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021277
  * `Imports (Out-Degree: 0):` time, win32event, win32file, win32api, win32pipe, io, pywintypes, functools
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docker/models/images.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.384 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.333 IQR)
- **Top Global Matches:** file_cluster_13: 10.384, file_cluster_8: 10.473, file_cluster_7: 10.651
- **Magnitude:** 191.84 | **LOC:** 506 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.6539%), Tech Debt (99.8516%)
**Top Internal Functions/Classes:**
  * `pull` (Impact: 25.8)
  * `build` (Impact: 20.2)
  * `load` (Impact: 16.5)
  * `save` (Impact: 14.7)
    * *Intent:* """ return self.client.api.history(self.id) def remove(self, force=False, noprune=False): """
  * `has_platform` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 72`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 5`, `duplicate_logic: 6`
* *Architecture:* `api: 33`, `import: 9`
* *Defense:* `safety: 3`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.545
  * `Choke Point (Betweenness):` 0.000216 | `Ripple Effect (Closeness):` 0.021277
  * `Imports (Out-Degree: 3):` warnings, .resource, itertools, ..constants, re, ..utils, ..api, ..errors...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docker/transport/sshconn.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.195 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.991 IQR)
- **Top Global Matches:** file_cluster_13: 11.195, file_cluster_8: 11.384, file_cluster_0: 11.759
- **Magnitude:** 191.26 | **LOC:** 251 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.7669%), Tech Debt (99.9612%)
**Top Internal Functions/Classes:**
  * `_create_paramiko_client` (Impact: 18.8)
  * `get_connection` (Impact: 13.3)
  * `_get_conn` (Impact: 9.6)
    * *Intent:* # When re-using connections, urllib3 calls fileno() on our # SSH channel instance, quickly overloadi...
  * `__init__` (Impact: 8.9)
  * `connect` (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 52`, `args: 20`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 57`, `duplicate_logic: 8`
* *Architecture:* `io: 11`, `api: 19`, `import: 13`
* *Defense:* `safety: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.249
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.010638
  * `Imports (Out-Degree: 2):` signal, urllib.parse, requests.adapters, queue, .basehttpadapter, socket, paramiko, subprocess...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docker/context/context.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.562 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.462 IQR)
- **Top Global Matches:** file_cluster_0: 10.562, file_cluster_13: 10.706, file_cluster_8: 10.925
- **Magnitude:** 190.3 | **LOC:** 250 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.5232%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 28.6)
  * `_load_certs` (Impact: 18.6)
  * `_load_meta` (Impact: 13.4)
  * `save` (Impact: 13.4)
  * `set_endpoint` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 57`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 33`, `dead_code: 1`
* *Architecture:* `io: 25`, `api: 24`, `import: 6`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.48
  * `Choke Point (Betweenness):` 0.002059 | `Ripple Effect (Closeness):` 0.064362
  * `Imports (Out-Degree: 2):` json, shutil, docker.errors, .config, docker.tls, os
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/unit/fake_api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.616 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.438 IQR)
- **Top Global Matches:** file_cluster_8: 6.616, file_cluster_7: 7.731, file_cluster_1: 7.97
- **Magnitude:** 176.14 | **LOC:** 643 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.4238%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_fake_network_list` (Impact: 3.4)
  * `get_fake_version` (Impact: 3.3)
    * *Intent:* # Each method is prefixed with HTTP method (get, post...) # for clarity and readability
  * `get_fake_inspect_image` (Impact: 3.3)
  * `get_fake_inspect_container` (Impact: 3.0)
  * `get_fake_top` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 113`, `args: 54`, `func_start: 54`
* *Risk/State:* `high_risk_execution: 4`, `dead_code: 1`
* *Architecture:* `api: 54`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docker, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/api/swarm.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.511 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.344 IQR)
- **Top Global Matches:** file_cluster_8: 9.511, file_cluster_0: 9.615, file_cluster_7: 9.675
- **Magnitude:** 146.28 | **LOC:** 463 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.0287%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `init_swarm` (Impact: 56.6)
  * `join_swarm` (Impact: 11.7)
  * `update_swarm` (Impact: 11.7)
  * `leave_swarm` (Impact: 9.4)
  * `unlock_swarm` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 34`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `fragile_debt: 2`
* *Architecture:* `api: 24`, `import: 4`
* *Defense:* `safety: 2`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.628
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` logging, ..constants, http.client, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/errors.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.327 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.419 IQR)
- **Top Global Matches:** file_cluster_8: 11.327, file_cluster_17: 11.456, file_cluster_13: 11.512
- **Magnitude:** 145.58 | **LOC:** 210 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.9423%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `create_api_error_from_http_exception` (Impact: 14.7)
    * *Intent:* """ def create_api_error_from_http_exception(e): """
  * `__str__` (Impact: 11.3)
    * *Intent:* # requests 1.1 doesn't super().__init__(message) self.response = response self.explanation = explana...
  * `__init__` (Impact: 8.5)
  * `create_unexpected_kwargs_error` (Impact: 7.4)
  * `is_client_error` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 64`, `args: 21`, `func_start: 21`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 32`, `duplicate_logic: 15`
* *Architecture:* `io: 2`, `api: 28`, `import: 1`
* *Defense:* `safety: 2`, `doc: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.061996
  * `Imports (Out-Degree: 0):` requests
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `docker/api/network.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.683 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.008 IQR)
- **Top Global Matches:** file_cluster_8: 8.683, file_cluster_7: 8.975, file_cluster_13: 9.22
- **Magnitude:** 116.6 | **LOC:** 278 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_network` (Impact: 60.9)
  * `inspect_network` (Impact: 12.0)
  * `networks` (Impact: 9.6)
    * *Intent:* """ List networks. Similar to the ``docker network ls`` command. Args: names (:py:class:`list`): Lis...
  * `disconnect_container_from_network` (Impact: 7.4)
  * `connect_container_to_network` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 18`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `api: 14`, `import: 3`
* *Defense:* `safety: 2`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014184
  * `Imports (Out-Degree: 0):` .., ..utils, ..errors
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `docker/transport/npipesocket.py` (PYTHON) | Magnitude: 194.86 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 73, api: 59, args: 36
- `docker/context/context.py` (PYTHON) | Magnitude: 190.3 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 197, structural_boundaries: 57, branch: 43, state_mutation: 33
- `docker/models/resource.py` (PYTHON) | Magnitude: 71.06 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 23, state_mutation: 17, api: 16
- `docker/types/healthcheck.py` (PYTHON) | Magnitude: 36.18 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 19, args: 11, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `docker/models/containers.py` (PYTHON) | Magnitude: 298.52 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 316, structural_boundaries: 100, doc: 70, branch: 60
- `docker/context/api.py` (PYTHON) | Magnitude: 83.38 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 25, branch: 21, doc: 14
- `docker/utils/socket.py` (PYTHON) | Magnitude: 92.86 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 39, branch: 35, io: 24
- `docker/models/images.py` (PYTHON) | Magnitude: 191.84 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 159, structural_boundaries: 72, branch: 48, doc: 38
- `tests/helpers.py` (PYTHON) | Magnitude: 110.74 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 51, branch: 26, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `docker/models/plugins.py` (PYTHON) | Magnitude: 64.94 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 32, doc: 28, api: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `docker/context/config.py` (PYTHON) | Magnitude: 61.94 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 36, branch: 18, api: 13
- `tests/unit/fake_api_client.py` (PYTHON) | Magnitude: 16.32 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 15, doc: 6, import: 5
- `docker/api/config.py` (PYTHON) | Magnitude: 22.56 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 12, encapsulation: 12, api: 8
- `docker/utils/config.py` (PYTHON) | Magnitude: 28.84 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 20, io: 10, branch: 8
- `docker/models/volumes.py` (PYTHON) | Magnitude: 26.68 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 19, doc: 14, api: 11

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `docker/context/context.py` -> **Severity: 0.172** (Bridge: 0.0021 * Flux: 83.6925%)
- `docker/context/api.py` -> **Severity: 0.168** (Bridge: 0.0024 * Flux: 70.1151%)
- `docker/api/client.py` -> **Severity: 0.147** (Bridge: 0.0015 * Flux: 95.1418%)
- `docker/utils/build.py` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 100.0%)
- `docker/transport/sshconn.py` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 99.9902%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `docker/models/resource.py` -> **Severity: 7.215** (Embedded: 0.1073 * Error Risk: 67.2607%)
- `docker/context/api.py` -> **Severity: 5.896** (Embedded: 0.0967 * Error Risk: 60.9638%)
- `docker/errors.py` -> **Severity: 5.205** (Embedded: 0.062 * Error Risk: 83.9627%)
- `docker/context/context.py` -> **Severity: 4.724** (Embedded: 0.0644 * Error Risk: 73.3984%)
- `docker/tls.py` -> **Severity: 4.371** (Embedded: 0.0673 * Error Risk: 64.9888%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `docker/models/resource.py` -> **Severity: 4649.668** (Blast Radius: 46.701 * Doc Risk: 99.5625%)
- `docker/context/context.py` -> **Severity: 3763.663** (Blast Radius: 41.48 * Doc Risk: 90.7344%)
- `docker/errors.py` -> **Severity: 3082.518** (Blast Radius: 31.079 * Doc Risk: 99.1833%)
- `docker/types/healthcheck.py` -> **Severity: 2015.028** (Blast Radius: 20.594 * Doc Risk: 97.8454%)
- `docker/tls.py` -> **Severity: 1650.249** (Blast Radius: 33.9 * Doc Risk: 48.6799%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
