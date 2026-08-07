# ARCHITECTURAL_BRIEF: requests
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/requests` |
| **Timestamp** | `2026-08-07T05:26:07.658457+00:00` |
| **Scan Duration** | `0.45s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 41 malicious artifacts.

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
| Total Artifacts | 66 |
| Analyzed Artifacts (Scanned) | 49 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 6944 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2413 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1201 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2688 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 33 | 6870 | 67.3% |
| MAKEFILE | 8 | 74 | 16.3% |
| MARKDOWN | 5 | 0 | 10.2% |
| PLAINTEXT | 3 | 0 | 6.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.592`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 22 | 44.9% |
| file_cluster_13 | 16 | 32.7% |
| file_cluster_7 | 1 | 2.0% |
| file_cluster_0 | 1 | 2.0% |
| file_cluster_4 | 1 | 2.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 16.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.cnf`: 6x Excluded (Unsupported Extension: '.cnf')
- `.srl`: 3x Excluded (Unsupported Extension: '.srl')
- `.csr`: 3x Excluded (Unsupported Extension: '.csr')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 70.4 | 12.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 71.4 | 17.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 10.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.4 | 5.8 | 6.4 | 0.0 |
| Concurrency Exposure | 0.0 | 97.3 | 6.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 2.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 81.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.1 | 16.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `requests-2.33.1/tests/test_requests.py` (Hits: 337)
- `requests-2.33.1/src/requests/utils.py` (Hits: 34)
- `requests-2.33.1/tests/test_utils.py` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cookies.py** (`requests-2.33.1/src/requests/cookies.py`) — 8 inbound connections
2. **structures.py** (`requests-2.33.1/src/requests/structures.py`) — 8 inbound connections
3. **exceptions.py** (`requests-2.33.1/src/requests/exceptions.py`) — 7 inbound connections
4. **_internal_utils.py** (`requests-2.33.1/src/requests/_internal_utils.py`) — 6 inbound connections
5. **auth.py** (`requests-2.33.1/src/requests/auth.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_requests.py** (`requests-2.33.1/tests/test_requests.py`) — 30 outbound dependencies
2. **utils.py** (`requests-2.33.1/src/requests/utils.py`) — 22 outbound dependencies
3. **models.py** (`requests-2.33.1/src/requests/models.py`) — 20 outbound dependencies
4. **adapters.py** (`requests-2.33.1/src/requests/adapters.py`) — 18 outbound dependencies
5. **__init__.py** (`requests-2.33.1/src/requests/__init__.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `proxy_bypass_registry` (@ `requests-2.33.1/src/requests/utils.py`) -> Impact: **145.0** | LOC: 337
- `test_cookie_removed_on_expire` (@ `requests-2.33.1/tests/test_requests.py`) -> Impact: **138.4** | LOC: 724
- `set_cookie` (@ `requests-2.33.1/src/requests/cookies.py`) -> Impact: **74.1** | LOC: 140
- `parse_header_links` (@ `requests-2.33.1/src/requests/utils.py`) -> Impact: **72.3** | LOC: 165
- `build_digest_header` (@ `requests-2.33.1/src/requests/auth.py`) -> Impact: **57.4** | LOC: 108
- `prepare_body` (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **53.1** | LOC: 78
  * *Intent:* # In general, we want to try IDNA encoding the hostname if the string contains # non-ASCII characters. This allows users to automatically get the corr...
- `_encode_files` (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **48.1** | LOC: 61
- `cert_verify` (@ `requests-2.33.1/src/requests/adapters.py`) -> Impact: **43.9** | LOC: 46
- `test_preparing_url` (@ `requests-2.33.1/tests/test_requests.py`) -> Impact: **42.7** | LOC: 294
- `prepare_url` (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **41.7** | LOC: 74

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `requests-2.33.1/src/requests` | 18 | 2376.86 | 18.82% | 39.83% |
| `requests-2.33.1/tests` | 12 | 1646.88 | 7.0% | 0.0% |
| `requests-2.33.1/tests/testserver` | 2 | 132.16 | 19.35% | 0.0% |
| `requests-2.33.1` | 6 | 58.74 | 0.83% | 0.0% |
| `requests-2.33.1/tests/certs/expired` | 2 | 18.68 | 2.5% | 0.0% |
| `requests-2.33.1/tests/certs/expired/server` | 1 | 18.22 | 5.0% | 0.0% |
| `requests-2.33.1/tests/certs/mtls/client` | 1 | 18.22 | 5.0% | 0.0% |
| `requests-2.33.1/tests/certs/valid/server` | 1 | 18.22 | 5.0% | 0.0% |
| `requests-2.33.1/tests/certs/expired/ca` | 1 | 17.68 | 5.0% | 0.0% |
| `requests-2.33.1/tests/certs/mtls/client/ca` | 1 | 17.68 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `requests-2.33.1/src/requests/auth.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/structures.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/exceptions.py` -> **99.9991%** Exposure
- `requests-2.33.1/src/requests/hooks.py` -> **99.0462%** Exposure
- `requests-2.33.1/src/requests/adapters.py` -> **97.8803%** Exposure
### Highest State Flux (Mutation/Volatility)
- `requests-2.33.1/src/requests/exceptions.py` -> **99.9998%** Exposure
- `requests-2.33.1/src/requests/models.py` -> **99.444%** Exposure
- `requests-2.33.1/src/requests/structures.py` -> **99.1164%** Exposure
- `requests-2.33.1/src/requests/cookies.py` -> **97.3671%** Exposure
- `requests-2.33.1/src/requests/sessions.py` -> **75.2098%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `requests-2.33.1/tests/test_requests.py` -> **128** Orphaned Functions | **18** Duplicates
- `requests-2.33.1/tests/test_utils.py` -> **30** Orphaned Functions | **2** Duplicates
- `requests-2.33.1/tests/test_lowlevel.py` -> **10** Orphaned Functions | **2** Duplicates
- `requests-2.33.1/tests/test_structures.py` -> **6** Orphaned Functions | **6** Duplicates
- `requests-2.33.1/tests/test_testserver.py` -> **11** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`requests-2.33.1/src/requests/models.py`** -> AI Confidence: **99.31%**
2. **`requests-2.33.1/src/requests/sessions.py`** -> AI Confidence: **99.31%**
3. **`requests-2.33.1/src/requests/utils.py`** -> AI Confidence: **99.31%**
4. **`requests-2.33.1/src/requests/__version__.py`** -> AI Confidence: **99.29%**
5. **`requests-2.33.1/src/requests/adapters.py`** -> AI Confidence: **99.24%**
6. **`requests-2.33.1/src/requests/auth.py`** -> AI Confidence: **99.24%**
7. **`requests-2.33.1/src/requests/cookies.py`** -> AI Confidence: **99.24%**
8. **`requests-2.33.1/src/requests/help.py`** -> AI Confidence: **99.24%**
9. **`requests-2.33.1/src/requests/__init__.py`** -> AI Confidence: **99.18%**
10. **`requests-2.33.1/src/requests/packages.py`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `171` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `requests-2.33.1/src/requests/cookies.py` (PYTHON) -> Cumulative Risk: **657.79**
- **Archetype:** `file_cluster_13` (Distance: 12.707 IQR)
- **Magnitude:** 367.74 | **LOC:** 562 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.3671%), Documentation (94.7542%), Concurrency (91.0848%)
- **Heaviest Functions:** `set_cookie` (Impact: 74.1), `remove_cookie_by_name` (Impact: 18.6), `cookiejar_from_dict` (Impact: 14.7)

### 2. `requests-2.33.1/src/requests/auth.py` (PYTHON) -> Cumulative Risk: **562.41**
- **Archetype:** `file_cluster_13` (Distance: 10.805 IQR)
- **Magnitude:** 163.5 | **LOC:** 315 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Verification (80.0%), Concurrency (64.4462%)
- **Heaviest Functions:** `build_digest_header` (Impact: 57.4), `_basic_auth_str` (Impact: 14.3), `handle_401` (Impact: 12.0)

### 3. `requests-2.33.1/src/requests/structures.py` (PYTHON) -> Cumulative Risk: **558.74**
- **Archetype:** `file_cluster_13` (Distance: 11.76 IQR)
- **Magnitude:** 54.7 | **LOC:** 100 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.1164%), Documentation (96.6775%)
- **Heaviest Functions:** `__eq__` (Impact: 5.5), `__init__` (Impact: 4.2), `lower_items` (Impact: 3.7)

### 4. `requests-2.33.1/src/requests/exceptions.py` (PYTHON) -> Cumulative Risk: **549.69**
- **Archetype:** `file_cluster_13` (Distance: 13.789 IQR)
- **Magnitude:** 53.28 | **LOC:** 153 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9991%), Documentation (99.1435%)
- **Heaviest Functions:** `__init__` (Impact: 8.4), `__init__` (Impact: 2.2), `__reduce__` (Impact: 1.9)

### 5. `requests-2.33.1/src/requests/models.py` (PYTHON) -> Cumulative Risk: **511.28**
- **Archetype:** `file_cluster_13` (Distance: 12.931 IQR)
- **Magnitude:** 582.0 | **LOC:** 1042 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.444%), Verification (80.0%), Tech Debt (71.4362%)
- **Heaviest Functions:** `prepare_body` (Impact: 53.1), `_encode_files` (Impact: 48.1), `prepare_url` (Impact: 41.7)

### 6. `requests-2.33.1/src/requests/adapters.py` (PYTHON) -> Cumulative Risk: **477.37**
- **Archetype:** `file_cluster_13` (Distance: 11.705 IQR)
- **Magnitude:** 196.38 | **LOC:** 698 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.8803%), Verification (80.0%), State Flux (72.9437%)
- **Heaviest Functions:** `cert_verify` (Impact: 43.9), `get_connection_with_tls_context` (Impact: 16.2), `get_connection` (Impact: 15.6)

### 7. `requests-2.33.1/tests/testserver/server.py` (PYTHON) -> Cumulative Risk: **369.09**
- **Archetype:** `file_cluster_4` (Distance: 11.479 IQR)
- **Magnitude:** 121.64 | **LOC:** 177 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (97.3198%), Safety Score (71.4159%), Stability (50.0%)
- **Heaviest Functions:** `__exit__` (Impact: 9.6), `consume_socket_content` (Impact: 7.7), `run` (Impact: 7.6)

### 8. `requests-2.33.1/src/requests/utils.py` (PYTHON) -> Cumulative Risk: **361.15**
- **Archetype:** `file_cluster_13` (Distance: 11.496 IQR)
- **Magnitude:** 457.26 | **LOC:** 1084 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Stability (50.0%), Safety Score (31.9819%)
- **Heaviest Functions:** `proxy_bypass_registry` (Impact: 145.0), `parse_header_links` (Impact: 72.3), `should_bypass_proxies` (Impact: 37.4)

### 9. `requests-2.33.1/src/requests/hooks.py` (PYTHON) -> Cumulative Risk: **337.14**
- **Archetype:** `file_cluster_8` (Distance: 10.203 IQR)
- **Magnitude:** 21.98 | **LOC:** 35 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (99.0462%), Spec Match (93.3333%), Documentation (82.7576%), Stability (50.0%)
- **Heaviest Functions:** `dispatch_hook` (Impact: 14.1), `default_hooks` (Impact: 3.6)

### 10. `requests-2.33.1/src/requests/sessions.py` (PYTHON) -> Cumulative Risk: **311.96**
- **Archetype:** `file_cluster_13` (Distance: 11.1 IQR)
- **Magnitude:** 295.26 | **LOC:** 835 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (75.2098%), Safety Score (54.4604%), Stability (50.0%)
- **Heaviest Functions:** `send` (Impact: 27.7), `merge_environment_settings` (Impact: 25.2), `should_strip_auth` (Impact: 21.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `requests-2.33.1/tests/test_requests.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.48 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.548 IQR)
- **Top Global Matches:** file_cluster_8: 12.48, file_cluster_0: 12.537, file_cluster_13: 12.657
- **Magnitude:** 1051.26 | **LOC:** 3045 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2569%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cookie_removed_on_expire` (Impact: 138.4)
  * `test_preparing_url` (Impact: 42.7)
  * `normalize_percent_encode` (Impact: 38.8)
  * `test_path_is_not_double_encoded` (Impact: 28.0)
  * `test_long_authinfo_in_url` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 854`, `args: 276`, `func_start: 274`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 43`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 18`, `orphaned_logic: 128`
* *Architecture:* `io: 337`, `api: 273`, `concurrency: 5`, `import: 32`
* *Defense:* `safety: 451`, `doc: 70`, `test: 736`, `sync_locks: 4`, `immutability_locks: 12`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` re, requests.packages.urllib3.poolmanager, requests.exceptions, contextlib, requests.models, urllib3.util, requests.cookies, tempfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.931 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.103 IQR)
- **Top Global Matches:** file_cluster_13: 12.931, file_cluster_0: 13.082, file_cluster_8: 13.217
- **Magnitude:** 582.0 | **LOC:** 1042 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.3713%), Tech Debt (71.4362%)
**Top Internal Functions/Classes:**
  * `prepare_body` (Impact: 53.1)
    * *Intent:* # In general, we want to try IDNA encoding the hostname if the string contains # non-ASCII character...
  * `_encode_files` (Impact: 48.1)
  * `prepare_url` (Impact: 41.7)
  * `iter_content` (Impact: 28.2)
  * `_encode_params` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 138`, `args: 44`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 112`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 45`, `import: 20`
* *Defense:* `safety: 65`, `doc: 82`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.287
  * `Choke Point (Betweenness):` 0.003435 | `Ripple Effect (Closeness):` 0.086806
  * `Imports (Out-Degree: 7):` urllib3.fields, ._internal_utils, .structures, encodings.idna, later., urllib3.util, .cookies, urllib3.filepost...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.496 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.245 IQR)
- **Top Global Matches:** file_cluster_13: 11.496, file_cluster_8: 11.677, file_cluster_7: 11.746
- **Magnitude:** 457.26 | **LOC:** 1084 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.9358%), Tech Debt (20.3328%)
**Top Internal Functions/Classes:**
  * `proxy_bypass_registry` (Impact: 145.0)
  * `parse_header_links` (Impact: 72.3)
  * `should_bypass_proxies` (Impact: 37.4)
  * `get_unicode_from_response` (Impact: 21.8)
  * `is_valid_cidr` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 170`, `args: 43`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 13`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* `io: 34`, `api: 48`, `import: 23`
* *Defense:* `safety: 60`, `doc: 99`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.531
  * `Choke Point (Betweenness):` 0.000887 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 5):` sys, re, ._internal_utils, .structures, netrc, contextlib, codecs, urllib3.util...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/cookies.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_13: 12.707, file_cluster_4: 12.774, file_cluster_7: 12.923
- **Magnitude:** 367.74 | **LOC:** 562 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.4062%), Tech Debt (35.0592%)
**Top Internal Functions/Classes:**
  * `set_cookie` (Impact: 74.1)
  * `remove_cookie_by_name` (Impact: 18.6)
  * `cookiejar_from_dict` (Impact: 14.7)
  * `get_dict` (Impact: 12.5)
    * *Intent:* """ return list(self.iterkeys()) def itervalues(self): """Dict-like itervalues() that returns an ite...
  * `merge_cookies` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 111`, `args: 49`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 43`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 63`, `concurrency: 18`, `import: 7`
* *Defense:* `safety: 18`, `doc: 91`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.817
  * `Choke Point (Betweenness):` 0.001293 | `Ripple Effect (Closeness):` 0.18006
  * `Imports (Out-Degree: 1):` dummy_threading, ._internal_utils, copy, .compat, time, calendar, threading
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/sessions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.1 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.505 IQR)
- **Top Global Matches:** file_cluster_13: 11.1, file_cluster_8: 11.177, file_cluster_7: 11.29
- **Magnitude:** 295.26 | **LOC:** 835 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5039%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 27.7)
  * `merge_environment_settings` (Impact: 25.2)
  * `should_strip_auth` (Impact: 21.6)
    * *Intent:* # Currently the underlying http module on py3 decode headers # rarely used with non-ASCII characters...
  * `merge_setting` (Impact: 17.3)
  * `rebuild_method` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 92`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 35`
* *Architecture:* `io: 3`, `api: 36`, `import: 16`
* *Defense:* `safety: 11`, `doc: 87`, `test: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.443
  * `Choke Point (Betweenness):` 0.002032 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 9):` .adapters, sys, datetime, ._internal_utils, .cookies, .status_codes, .structures, .auth...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.757 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.942 IQR)
- **Top Global Matches:** file_cluster_8: 10.757, file_cluster_0: 10.804, file_cluster_13: 11.031
- **Magnitude:** 276.92 | **LOC:** 991 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.2319%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_not_vulnerable_to_bad_url_parsing` (Impact: 37.4)
  * `test_should_bypass_proxies_win_registry` (Impact: 21.2)
    * *Intent:* """Tests for function should_bypass_proxies to check if proxy can be bypassed or not with Windows re...
  * `test_iter_slices` (Impact: 9.0)
  * `test_should_bypass_proxies_win_registry_` (Impact: 8.3)
  * `QueryValueEx` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 246`, `args: 78`, `func_start: 78`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 4`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 30`
* *Architecture:* `io: 27`, `api: 94`, `import: 18`
* *Defense:* `safety: 78`, `doc: 38`, `test: 184`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` requests.utils, requests.structures, requests.cookies, unittest, tarfile, copy, zipfile, .compat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/adapters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.705 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.437 IQR)
- **Top Global Matches:** file_cluster_13: 11.705, file_cluster_8: 11.911, file_cluster_7: 12.1
- **Magnitude:** 196.38 | **LOC:** 698 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.8436%), Tech Debt (97.8803%)
**Top Internal Functions/Classes:**
  * `cert_verify` (Impact: 43.9)
  * `get_connection_with_tls_context` (Impact: 16.2)
  * `get_connection` (Impact: 15.6)
  * `request_url` (Impact: 13.0)
  * `proxy_manager_for` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 86`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 8`, `api: 19`, `import: 22`
* *Defense:* `safety: 31`, `doc: 81`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.624
  * `Choke Point (Betweenness):` 0.003546 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 5):` urllib3.util, urllib3.util.retry, .exceptions, urllib3.contrib.socks, .cookies, .structures, .auth, urllib3...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/auth.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.805 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_13: 10.805, file_cluster_8: 11.001, file_cluster_7: 11.267
- **Magnitude:** 163.5 | **LOC:** 315 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.1631%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `build_digest_header` (Impact: 57.4)
  * `_basic_auth_str` (Impact: 14.3)
  * `handle_401` (Impact: 12.0)
  * `__call__` (Impact: 6.1)
  * `handle_redirect` (Impact: 4.2)
    * *Intent:* """Reset num_401_calls counter on redirects."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 58`, `args: 20`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 15`, `doc: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.005
  * `Choke Point (Betweenness):` 0.000406 | `Ripple Effect (Closeness):` 0.09375
  * `Imports (Out-Degree: 2):` base64, re, ._internal_utils, .cookies, .compat, time, .utils, os...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_lowlevel.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.142 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.39 IQR)
- **Top Global Matches:** file_cluster_8: 11.142, file_cluster_13: 11.319, file_cluster_1: 11.367
- **Magnitude:** 133.98 | **LOC:** 429 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5807%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fragment_not_sent_with_request` (Impact: 14.7)
  * `test_use_proxy_from_environment` (Impact: 8.8)
  * `test_chunked_upload_uses_only_specified_` (Impact: 7.0)
  * `test_digestauth_401_count_reset_on_redir` (Impact: 6.5)
    * *Intent:* """ text_401 = (b'HTTP/1.1 401 UNAUTHORIZED\r\n' b'Content-Length: 0\r\n' b'WWW-Authenticate: Digest...
  * `test_conflicting_content_lengths` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 95`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `duplicate_logic: 2`, `orphaned_logic: 10`
* *Architecture:* `io: 23`, `api: 22`, `concurrency: 18`, `import: 6`
* *Defense:* `safety: 44`, `doc: 22`, `test: 61`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tests.testserver.server, requests.compat, threading, requests, .utils, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/tests/testserver/server.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.479 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.477 IQR)
- **Top Global Matches:** file_cluster_4: 11.479, file_cluster_13: 11.702, file_cluster_0: 11.779
- **Magnitude:** 121.64 | **LOC:** 177 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.6921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__exit__` (Impact: 9.6)
  * `consume_socket_content` (Impact: 7.7)
  * `run` (Impact: 7.6)
  * `_handle_requests` (Impact: 5.7)
  * `_accept_connection` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 35`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 36`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 10`, `concurrency: 14`, `import: 4`
* *Defense:* `safety: 6`, `doc: 2`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 0):` threading, select, ssl, socket
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_testserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.042 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.919 IQR)
- **Top Global Matches:** file_cluster_13: 13.042, file_cluster_0: 13.156, file_cluster_6: 13.396
- **Magnitude:** 71.64 | **LOC:** 166 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multiple_requests` (Impact: 7.7)
  * `test_server_closes` (Impact: 5.8)
  * `test_server_finishes_on_error` (Impact: 5.6)
    * *Intent:* # and get killed by the jenkins timeout. def test_server_finishes_when_no_connections(self): """the ...
  * `test_request_recovery` (Impact: 4.6)
  * `test_basic` (Impact: 4.4)
    * *Intent:* """messages are sent and received properly"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 11`
* *Architecture:* `io: 24`, `api: 13`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 15`, `doc: 22`, `test: 32`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tests.testserver.server, time, threading, requests, pytest, socket
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/structures.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.76 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.831 IQR)
- **Top Global Matches:** file_cluster_13: 11.76, file_cluster_8: 11.944, file_cluster_7: 12.115
- **Magnitude:** 54.7 | **LOC:** 100 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.0677%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__eq__` (Impact: 5.5)
  * `__init__` (Impact: 4.2)
    * *Intent:* """A case-insensitive ``dict``-like object. Implements all methods and operations of ``MutableMappin...
  * `lower_items` (Impact: 3.7)
  * `__iter__` (Impact: 3.6)
  * `__setitem__` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 32`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `duplicate_logic: 6`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.173611
  * `Imports (Out-Degree: 0):` collections, .compat
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.789 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.887 IQR)
- **Top Global Matches:** file_cluster_13: 13.789, file_cluster_7: 14.013, file_cluster_8: 14.098
- **Magnitude:** 53.28 | **LOC:** 153 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.2734%), Tech Debt (99.9991%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 8.4)
    * *Intent:* """There was an ambiguous exception that occurred while handling your request. """
  * `__init__` (Impact: 2.2)
  * `__reduce__` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 35`, `args: 3`, `func_start: 3`, `class_start: 25`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 2`
* *Architecture:* `api: 25`, `import: 2`
* *Defense:* `safety: 1`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 49.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.153409
  * `Imports (Out-Degree: 0):` urllib3.exceptions, .compat
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_structures.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.09 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.837 IQR)
- **Top Global Matches:** file_cluster_0: 12.09, file_cluster_13: 12.41, file_cluster_8: 12.477
- **Magnitude:** 41.38 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_instance_equality` (Impact: 2.1)
  * `test_getitem` (Impact: 2.1)
  * `test_get` (Impact: 2.1)
  * `setup` (Impact: 2.0)
    * *Intent:* """CaseInsensitiveDict instance with "Accept" header."""
  * `setup` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 29`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 6`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 14`, `import: 2`
* *Defense:* `safety: 11`, `doc: 4`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` requests.structures, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 41.02 | **LOC:** 2051 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/help.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.487 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.698 IQR)
- **Top Global Matches:** file_cluster_8: 9.487, file_cluster_13: 9.558, file_cluster_7: 9.986
- **Magnitude:** 34.06 | **LOC:** 132 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9938%), Tech Debt (93.0993%)
**Top Internal Functions/Classes:**
  * `info` (Impact: 15.0)
  * `_implementation` (Impact: 13.2)
  * `main` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 20`, `args: 3`, `func_start: 3`
* *Risk/State:* `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 2`, `import: 12`
* *Defense:* `safety: 10`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 0):` sys, urllib3.contrib, platform, urllib3, cryptography, OpenSSL, , idna...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/status_codes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.925 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.394 IQR)
- **Top Global Matches:** file_cluster_8: 6.925, file_cluster_7: 7.739, file_cluster_1: 7.987
- **Magnitude:** 29.74 | **LOC:** 129 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1022%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_init` (Impact: 14.7)
  * `doc` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.335
  * `Choke Point (Betweenness):` 0.000148 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 1):` .structures, requests
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_7` (Drift: 11.563 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.382 IQR)
- **Top Global Matches:** file_cluster_7: 11.563, file_cluster_8: 11.588, file_cluster_1: 11.77
- **Magnitude:** 28.12 | **LOC:** 158 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.4071%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 4.5)
  * `post` (Impact: 2.5)
  * `get` (Impact: 2.2)
  * `put` (Impact: 2.2)
  * `patch` (Impact: 2.2)
    * *Intent:* # By using the 'with' statement we are sure the session is closed, thus we # avoid leaving sockets o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 19`, `args: 8`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 64`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.214
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 0):` , requests
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.148 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.445 IQR)
- **Top Global Matches:** file_cluster_13: 11.148, file_cluster_8: 11.583, file_cluster_17: 11.901
- **Magnitude:** 27.56 | **LOC:** 184 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.1136%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_compatibility` (Impact: 15.7)
  * `_check_cryptography` (Impact: 5.8)
    * *Intent:* # Sometimes, urllib3 only reports its version as 16.1. if len(urllib3_version) == 2: urllib3_version...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 44`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `safety: 18`, `doc: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .sessions, urllib3.contrib, .status_codes, urllib3, urllib3.exceptions, cryptography, logging, charset_normalizer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/hooks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.203 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.907 IQR)
- **Top Global Matches:** file_cluster_8: 10.203, file_cluster_7: 10.463, file_cluster_6: 10.639
- **Magnitude:** 21.98 | **LOC:** 35 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `dispatch_hook` (Impact: 14.1)
  * `default_hooks` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 4`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.809
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.109 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.395 IQR)
- **Top Global Matches:** file_cluster_13: 12.109, file_cluster_0: 12.172, file_cluster_11: 12.573
- **Magnitude:** 19.3 | **LOC:** 18 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.3036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `override_environ` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 5`, `api: 2`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` contextlib, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/tests/certs/expired/server/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.104 IQR)
- **Top Global Matches:** file_cluster_8: 7.104, file_cluster_7: 8.165, file_cluster_1: 8.328
- **Magnitude:** 18.22 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/tests/certs/mtls/client/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.104 IQR)
- **Top Global Matches:** file_cluster_8: 7.104, file_cluster_7: 8.165, file_cluster_1: 8.328
- **Magnitude:** 18.22 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/tests/certs/valid/server/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.104 IQR)
- **Top Global Matches:** file_cluster_8: 7.104, file_cluster_7: 8.165, file_cluster_1: 8.328
- **Magnitude:** 18.22 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/tests/certs/expired/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.887 IQR)
- **Top Global Matches:** file_cluster_8: 6.887, file_cluster_7: 7.986, file_cluster_1: 8.152
- **Magnitude:** 17.68 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `requests-2.33.1/tests/test_structures.py` (PYTHON) | Magnitude: 41.38 | Delta: **0.32 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 29, test: 29, api: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `requests-2.33.1/tests/utils.py` (PYTHON) | Magnitude: 19.3 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 6, branch: 5, io: 5
- `requests-2.33.1/src/requests/cookies.py` (PYTHON) | Magnitude: 367.74 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 273, structural_boundaries: 111, doc: 91, branch: 74
- `requests-2.33.1/src/requests/sessions.py` (PYTHON) | Magnitude: 295.26 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 386, structural_boundaries: 92, branch: 91, doc: 87
- `requests-2.33.1/tests/test_hooks.py` (PYTHON) | Magnitude: 8.7 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, test: 6, args: 4
- `requests-2.33.1/src/requests/compat.py` (PYTHON) | Magnitude: 8.7 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 30, indent_spaces: 30, import: 15, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `requests-2.33.1/tests/testserver/server.py` (PYTHON) | Magnitude: 121.64 | Delta: **0.223 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, state_mutation: 36, structural_boundaries: 35, branch: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `requests-2.33.1/src/requests/api.py` (PYTHON) | Magnitude: 28.12 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 64, structural_boundaries: 19, indent_spaces: 17, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `requests-2.33.1/tests/test_utils.py` (PYTHON) | Magnitude: 276.92 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 697, structural_boundaries: 246, test: 184, api: 94
- `requests-2.33.1/tests/test_requests.py` (PYTHON) | Magnitude: 1051.26 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2335, structural_boundaries: 854, test: 736, safety: 451
- `requests-2.33.1/setup.py` (PYTHON) | Magnitude: 13.12 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, io: 3, branch: 2, import: 2
- `requests-2.33.1/src/requests/help.py` (PYTHON) | Magnitude: 34.06 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 20, branch: 17, import: 12
- `requests-2.33.1/src/requests/certs.py` (PYTHON) | Magnitude: 12.08 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, encapsulation: 2, branch: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `requests-2.33.1/src/requests/models.py` -> **Severity: 0.342** (Bridge: 0.0034 * Flux: 99.444%)
- `requests-2.33.1/src/requests/adapters.py` -> **Severity: 0.259** (Bridge: 0.0035 * Flux: 72.9437%)
- `requests-2.33.1/src/requests/sessions.py` -> **Severity: 0.153** (Bridge: 0.002 * Flux: 75.2098%)
- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 0.126** (Bridge: 0.0013 * Flux: 97.3671%)
- `requests-2.33.1/src/requests/auth.py` -> **Severity: 0.017** (Bridge: 0.0004 * Flux: 41.8537%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `requests-2.33.1/src/requests/structures.py` -> **Severity: 11.769** (Embedded: 0.1736 * Error Risk: 67.787%)
- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 9.235** (Embedded: 0.1801 * Error Risk: 51.2882%)
- `requests-2.33.1/src/requests/exceptions.py` -> **Severity: 8.713** (Embedded: 0.1534 * Error Risk: 56.7967%)
- `requests-2.33.1/tests/testserver/server.py` -> **Severity: 4.463** (Embedded: 0.0625 * Error Risk: 71.4159%)
- `requests-2.33.1/src/requests/status_codes.py` -> **Severity: 4.22** (Embedded: 0.075 * Error Risk: 56.2618%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `requests-2.33.1/src/requests/structures.py` -> **Severity: 5765.073** (Blast Radius: 59.632 * Doc Risk: 96.6775%)
- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 5573.158** (Blast Radius: 58.817 * Doc Risk: 94.7542%)
- `requests-2.33.1/src/requests/exceptions.py` -> **Severity: 4903.34** (Blast Radius: 49.457 * Doc Risk: 99.1435%)
- `requests-2.33.1/src/requests/_internal_utils.py` -> **Severity: 4637.448** (Blast Radius: 84.831 * Doc Risk: 54.6669%)
- `requests-2.33.1/src/requests/hooks.py` -> **Severity: 1639.345** (Blast Radius: 19.809 * Doc Risk: 82.7576%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
