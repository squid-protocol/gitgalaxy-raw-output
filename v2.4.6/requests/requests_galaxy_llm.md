# ARCHITECTURAL_BRIEF: requests
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/requests` |
| **Timestamp** | `2026-08-03T21:24:45.869052+00:00` |
| **Scan Duration** | `0.51s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 41 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 70.4 | 12.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 47.2 | 3.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.4 | 5.8 | 6.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 2.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 81.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 44.9 | 4.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 31.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `proxy_bypass_registry` (@ `requests-2.33.1/src/requests/utils.py`) -> Impact: **914.1** | LOC: 337
- `set_cookie` (@ `requests-2.33.1/src/requests/cookies.py`) -> Impact: **476.6** | LOC: 140
- `test_cookie_removed_on_expire` (@ `requests-2.33.1/tests/test_requests.py`) -> Impact: **342.8** | LOC: 724
- `prepare_body` (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **176.1** | LOC: 78
  * *Intent:* # In general, we want to try IDNA encoding the hostname if the string contains # non-ASCII characters. This allows users to automatically get the corr...
- `parse_header_links` (@ `requests-2.33.1/src/requests/utils.py`) -> Impact: **168.5** | LOC: 165
- `build_digest_header` (@ `requests-2.33.1/src/requests/auth.py`) -> Impact: **161.4** | LOC: 108
- `_encode_files` (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **160.7** | LOC: 61
- `send` (@ `requests-2.33.1/src/requests/sessions.py`) -> Impact: **147.7** | LOC: 74
- `cert_verify` (@ `requests-2.33.1/src/requests/adapters.py`) -> Impact: **127.2** | LOC: 46
- `should_bypass_proxies` (@ `requests-2.33.1/src/requests/utils.py`) -> Impact: **124.0** | LOC: 56

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `set_cookie` (@ `requests-2.33.1/src/requests/cookies.py`) -> **O(2^N) [Recursive]**
- `proxy_bypass_registry` (@ `requests-2.33.1/src/requests/utils.py`) -> **O(2^N) [Recursive]**
- `get_connection` (@ `requests-2.33.1/src/requests/adapters.py`) -> **O(2^N) [Recursive]**
- `send` (@ `requests-2.33.1/src/requests/sessions.py`) -> **O(2^N) [Recursive]**
- `content` (@ `requests-2.33.1/src/requests/models.py`) -> **O(2^N) [Recursive]**
- `links` (@ `requests-2.33.1/src/requests/models.py`) -> **O(2^N) [Recursive]**
- `get_unicode_from_response` (@ `requests-2.33.1/src/requests/utils.py`) -> **O(2^N) [Recursive]**
- `__contains__` (@ `requests-2.33.1/src/requests/cookies.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `requests-2.33.1/src/requests/exceptions.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """There was an ambiguous exception that occurred while handling your request. """
- `close` (@ `requests-2.33.1/src/requests/models.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Decode unicode from given encoding.

### Highest Data Gravity (Database Complexity)
- `test_cookie_removed_on_expire` (@ `requests-2.33.1/tests/test_requests.py`) -> DB Complexity: **335**
- `test_preparing_url` (@ `requests-2.33.1/tests/test_requests.py`) -> DB Complexity: **85**
- `test_path_is_not_double_encoded` (@ `requests-2.33.1/tests/test_requests.py`) -> DB Complexity: **84**
- `proxy_bypass_registry` (@ `requests-2.33.1/src/requests/utils.py`) -> DB Complexity: **53**
- `test_long_authinfo_in_url` (@ `requests-2.33.1/tests/test_requests.py`) -> DB Complexity: **39**
- `test_not_vulnerable_to_bad_url_parsing` (@ `requests-2.33.1/tests/test_utils.py`) -> DB Complexity: **31**
- `test_entry_points` (@ `requests-2.33.1/tests/test_requests.py`) -> DB Complexity: **27**
- `override_environ` (@ `requests-2.33.1/tests/utils.py`) -> DB Complexity: **17**
- `test_fragment_not_sent_with_request` (@ `requests-2.33.1/tests/test_lowlevel.py`) -> DB Complexity: **15**
- `test_server_closes` (@ `requests-2.33.1/tests/test_testserver.py`) -> DB Complexity: **15**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `requests-2.33.1/src/requests` | 18 | 5605.96 | 19.49% | 39.83% |
| `requests-2.33.1/tests` | 12 | 2334.38 | 7.0% | 0.0% |
| `requests-2.33.1/tests/testserver` | 2 | 192.06 | 19.35% | 0.0% |
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
- `requests-2.33.1/tests/test_requests.py` -> **126** Orphaned Functions | **3** Duplicates
- `requests-2.33.1/tests/test_utils.py` -> **27** Orphaned Functions | **0** Duplicates
- `requests-2.33.1/tests/test_structures.py` -> **6** Orphaned Functions | **6** Duplicates
- `requests-2.33.1/tests/test_testserver.py` -> **11** Orphaned Functions | **0** Duplicates
- `requests-2.33.1/src/requests/auth.py` -> **0** Orphaned Functions | **10** Duplicates

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

### Exploit Generation Surface
- `requests-2.33.1/src/requests/adapters.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/auth.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/cookies.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/models.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/sessions.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `requests-2.33.1/tests/test_adapters.py` -> **100.0%** Exposure
- `requests-2.33.1/tests/test_lowlevel.py` -> **100.0%** Exposure
- `requests-2.33.1/tests/test_requests.py` -> **100.0%** Exposure
- `requests-2.33.1/tests/test_testserver.py` -> **100.0%** Exposure
- `requests-2.33.1/tests/test_utils.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `requests-2.33.1/src/requests/adapters.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/auth.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/cookies.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/help.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/models.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `171` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `requests-2.33.1/src/requests/cookies.py` (PYTHON) -> Cumulative Risk: **827.35**
- **Archetype:** `file_cluster_13` (Distance: 12.707 IQR)
- **Magnitude:** 942.74 | **LOC:** 562 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `set_cookie` (Impact: 476.6), `remove_cookie_by_name` (Impact: 36.5), `cookiejar_from_dict` (Impact: 35.6)

### 2. `requests-2.33.1/src/requests/auth.py` (PYTHON) -> Cumulative Risk: **810.64**
- **Archetype:** `file_cluster_13` (Distance: 10.807 IQR)
- **Magnitude:** 304.0 | **LOC:** 315 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `build_digest_header` (Impact: 161.4), `handle_401` (Impact: 27.0), `_basic_auth_str` (Impact: 26.4)

### 3. `requests-2.33.1/src/requests/models.py` (PYTHON) -> Cumulative Risk: **759.89**
- **Archetype:** `file_cluster_13` (Distance: 12.931 IQR)
- **Magnitude:** 1275.5 | **LOC:** 1042 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.5805%)
- **Heaviest Functions:** `prepare_body` (Impact: 176.1), `_encode_files` (Impact: 160.7), `prepare_url` (Impact: 98.7)

### 4. `requests-2.33.1/src/requests/adapters.py` (PYTHON) -> Cumulative Risk: **756.3**
- **Archetype:** `file_cluster_13` (Distance: 11.705 IQR)
- **Magnitude:** 431.08 | **LOC:** 698 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (97.8803%)
- **Heaviest Functions:** `cert_verify` (Impact: 127.2), `get_connection` (Impact: 85.5), `get_connection_with_tls_context` (Impact: 45.6)

### 5. `requests-2.33.1/src/requests/exceptions.py` (PYTHON) -> Cumulative Risk: **703.55**
- **Archetype:** `file_cluster_13` (Distance: 13.789 IQR)
- **Magnitude:** 84.88 | **LOC:** 153 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Algorithmic Dos (99.9992%), Tech Debt (99.9991%)
- **Heaviest Functions:** `__init__` (Impact: 32.5), `__init__` (Impact: 6.2), `__reduce__` (Impact: 5.4)

### 6. `requests-2.33.1/src/requests/sessions.py` (PYTHON) -> Cumulative Risk: **621.31**
- **Archetype:** `file_cluster_13` (Distance: 11.1 IQR)
- **Magnitude:** 597.96 | **LOC:** 835 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (91.2682%)
- **Heaviest Functions:** `send` (Impact: 147.7), `merge_environment_settings` (Impact: 72.8), `should_strip_auth` (Impact: 41.6)

### 7. `requests-2.33.1/src/requests/structures.py` (PYTHON) -> Cumulative Risk: **607.63**
- **Archetype:** `file_cluster_13` (Distance: 11.76 IQR)
- **Magnitude:** 82.0 | **LOC:** 100 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.997%)
- **Heaviest Functions:** `__eq__` (Impact: 10.7), `__init__` (Impact: 8.2), `get` (Impact: 6.1)

### 8. `requests-2.33.1/src/requests/utils.py` (PYTHON) -> Cumulative Risk: **596.04**
- **Archetype:** `file_cluster_13` (Distance: 11.496 IQR)
- **Magnitude:** 1563.86 | **LOC:** 1084 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (95.7487%)
- **Heaviest Functions:** `proxy_bypass_registry` (Impact: 914.1), `parse_header_links` (Impact: 168.5), `should_bypass_proxies` (Impact: 124.0)

### 9. `requests-2.33.1/src/requests/help.py` (PYTHON) -> Cumulative Risk: **528.58**
- **Archetype:** `file_cluster_8` (Distance: 9.487 IQR)
- **Magnitude:** 64.36 | **LOC:** 132 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (93.6873%), Tech Debt (93.0993%)
- **Heaviest Functions:** `_implementation` (Impact: 31.4), `info` (Impact: 27.1), `main` (Impact: 1.9)

### 10. `requests-2.33.1/tests/testserver/server.py` (PYTHON) -> Cumulative Risk: **513.86**
- **Archetype:** `file_cluster_4` (Distance: 11.479 IQR)
- **Magnitude:** 181.54 | **LOC:** 177 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (97.3198%)
- **Heaviest Functions:** `__exit__` (Impact: 23.0), `run` (Impact: 18.0), `consume_socket_content` (Impact: 14.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `requests-2.33.1/src/requests/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.496 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.245 IQR)
- **Top Global Matches:** file_cluster_13: 11.496, file_cluster_8: 11.677, file_cluster_7: 11.746
- **Magnitude:** 1563.86 | **LOC:** 1084 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (13.8805%), Tech Debt (20.3328%)
**Top Internal Functions/Classes:**
  * `proxy_bypass_registry` (Impact: 914.1 | O(2^N) | DB: 53)
  * `parse_header_links` (Impact: 168.5 | O(N^4) | DB: 1)
  * `should_bypass_proxies` (Impact: 124.0 | O(N^6) | DB: 9)
  * `get_unicode_from_response` (Impact: 98.0 | O(2^N) | DB: 4)
  * `set_environ` (Impact: 31.1 | O(N^4) | DB: 12)
    * *Intent:* # Fall back: try: return str(r.content, encoding, errors="replace") except TypeError: return r.conte...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 170`, `args: 43`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 13`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* `io: 34`, `api: 48`, `import: 23`
* *Defense:* `safety: 60`, `doc: 99`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.531
  * `Choke Point (Betweenness):` 0.000887 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 5):` contextlib, io, socket, netrc, .cookies, zipfile, os, codecs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_requests.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.481 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.566 IQR)
- **Top Global Matches:** file_cluster_8: 12.481, file_cluster_0: 12.544, file_cluster_13: 12.663
- **Magnitude:** 1517.26 | **LOC:** 3045 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 335
- **Risk Profile:** Cognitive Load (3.2493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cookie_removed_on_expire` (Impact: 342.8 | O(N^5) | DB: 335)
  * `test_preparing_url` (Impact: 84.7 | O(N^4) | DB: 85)
  * `test_path_is_not_double_encoded` (Impact: 54.0 | O(N^4) | DB: 84)
  * `test_long_authinfo_in_url` (Impact: 28.1 | O(N^3) | DB: 39)
  * `test_custom_redirect_mixin` (Impact: 22.5 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 854`, `args: 276`, `func_start: 274`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 43`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 3`, `orphaned_logic: 126`
* *Architecture:* `io: 337`, `api: 273`, `concurrency: 5`, `import: 32`
* *Defense:* `safety: 451`, `doc: 70`, `test: 736`, `sync_locks: 4`, `immutability_locks: 12`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` contextlib, requests.exceptions, requests.structures, io, requests.packages.urllib3.poolmanager, requests.cookies, pytest, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.931 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.103 IQR)
- **Top Global Matches:** file_cluster_13: 12.931, file_cluster_0: 13.082, file_cluster_8: 13.217
- **Magnitude:** 1275.5 | **LOC:** 1042 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (41.0937%), Tech Debt (71.4362%)
**Top Internal Functions/Classes:**
  * `prepare_body` (Impact: 176.1 | O(N^6) | DB: 3)
    * *Intent:* # In general, we want to try IDNA encoding the hostname if the string contains # non-ASCII character...
  * `_encode_files` (Impact: 160.7 | O(N^6) | DB: 2)
  * `prepare_url` (Impact: 98.7 | O(N^4) | DB: 2)
  * `iter_content` (Impact: 93.2 | O(N^6) | DB: 1)
  * `_encode_params` (Impact: 86.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 138`, `args: 44`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 112`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 45`, `import: 20`
* *Defense:* `safety: 65`, `doc: 82`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.287
  * `Choke Point (Betweenness):` 0.003435 | `Ripple Effect (Closeness):` 0.086806
  * `Imports (Out-Degree: 7):` io, urllib3.filepost, later., .hooks, encodings.idna, .status_codes, idna, datetime...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/cookies.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_13: 12.707, file_cluster_4: 12.774, file_cluster_7: 12.923
- **Magnitude:** 942.74 | **LOC:** 562 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (42.4062%), Tech Debt (35.0592%)
**Top Internal Functions/Classes:**
  * `set_cookie` (Impact: 476.6 | O(2^N) | DB: 7)
  * `remove_cookie_by_name` (Impact: 36.5 | O(N^3) | DB: 2)
  * `cookiejar_from_dict` (Impact: 35.6 | O(N^4))
  * `get_dict` (Impact: 30.5 | O(N^4))
    * *Intent:* """ return list(self.iterkeys()) def itervalues(self): """Dict-like itervalues() that returns an ite...
  * `merge_cookies` (Impact: 26.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 111`, `args: 49`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 43`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 63`, `concurrency: 18`, `import: 7`
* *Defense:* `safety: 18`, `doc: 91`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.817
  * `Choke Point (Betweenness):` 0.001293 | `Ripple Effect (Closeness):` 0.18006
  * `Imports (Out-Degree: 1):` threading, copy, dummy_threading, time, .compat, ._internal_utils, calendar
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/sessions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.1 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.505 IQR)
- **Top Global Matches:** file_cluster_13: 11.1, file_cluster_8: 11.177, file_cluster_7: 11.29
- **Magnitude:** 597.96 | **LOC:** 835 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (10.5039%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 147.7 | O(2^N) | DB: 3)
  * `merge_environment_settings` (Impact: 72.8 | O(N^5) | DB: 6)
  * `should_strip_auth` (Impact: 41.6 | O(N^3))
    * *Intent:* # Currently the underlying http module on py3 decode headers # rarely used with non-ASCII characters...
  * `rebuild_method` (Impact: 29.0 | O(N^3))
  * `prepare_request` (Impact: 27.7 | O(N^4))
    * *Intent:* #: SSL Verification default. #: Defaults to `True`, requiring requests to verify the TLS certificate...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 92`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 35`
* *Architecture:* `io: 3`, `api: 36`, `import: 16`
* *Defense:* `safety: 11`, `doc: 87`, `test: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.443
  * `Choke Point (Betweenness):` 0.002032 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 9):` .hooks, .status_codes, .auth, .exceptions, .adapters, datetime, .cookies, sys...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/adapters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.705 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.437 IQR)
- **Top Global Matches:** file_cluster_13: 11.705, file_cluster_8: 11.911, file_cluster_7: 12.1
- **Magnitude:** 431.08 | **LOC:** 698 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (15.8436%), Tech Debt (97.8803%)
**Top Internal Functions/Classes:**
  * `cert_verify` (Impact: 127.2 | O(N^5) | DB: 12)
  * `get_connection` (Impact: 85.5 | O(2^N) | DB: 3)
  * `get_connection_with_tls_context` (Impact: 45.6 | O(N^5))
  * `request_url` (Impact: 25.0 | O(N^3))
  * `proxy_manager_for` (Impact: 21.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 86`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 8`, `api: 19`, `import: 22`
* *Defense:* `safety: 31`, `doc: 81`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.624
  * `Choke Point (Betweenness):` 0.003546 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 5):` urllib3.exceptions, urllib3, .compat, urllib3.util.retry, socket, .auth, .exceptions, urllib3.poolmanager...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.75 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.939 IQR)
- **Top Global Matches:** file_cluster_8: 10.75, file_cluster_0: 10.801, file_cluster_13: 11.027
- **Magnitude:** 369.72 | **LOC:** 991 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (2.2182%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_not_vulnerable_to_bad_url_parsing` (Impact: 65.3 | O(N^5) | DB: 31)
  * `test_should_bypass_proxies_win_registry` (Impact: 48.0 | O(N^4) | DB: 3)
    * *Intent:* """Tests for function should_bypass_proxies to check if proxy can be bypassed or not with Windows re...
  * `test_should_bypass_proxies_win_registry_` (Impact: 22.2 | O(N^5))
  * `test_iter_slices` (Impact: 13.3 | O(N^2))
  * `test_tarfile_member` (Impact: 10.9 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 246`, `args: 78`, `func_start: 78`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 4`, `fragile_debt: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 27`, `api: 94`, `import: 18`
* *Defense:* `safety: 78`, `doc: 38`, `test: 184`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` requests.utils, unittest, requests.structures, io, requests._internal_utils, requests.cookies, winreg, filecmp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/auth.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.807 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_13: 10.807, file_cluster_8: 11.003, file_cluster_7: 11.269
- **Magnitude:** 304.0 | **LOC:** 315 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (29.6137%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `build_digest_header` (Impact: 161.4 | O(N^5) | DB: 3)
  * `handle_401` (Impact: 27.0 | O(N^4) | DB: 1)
  * `_basic_auth_str` (Impact: 26.4 | O(N^3))
  * `__call__` (Impact: 11.3 | O(N^3))
  * `handle_redirect` (Impact: 8.2 | O(N^3))
    * *Intent:* """Reset num_401_calls counter on redirects."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 58`, `args: 20`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 15`, `doc: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.005
  * `Choke Point (Betweenness):` 0.000406 | `Ripple Effect (Closeness):` 0.09375
  * `Imports (Out-Degree: 2):` .compat, re, threading, .cookies, .utils, base64, ._internal_utils, time...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_lowlevel.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.146 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.414 IQR)
- **Top Global Matches:** file_cluster_8: 11.146, file_cluster_13: 11.33, file_cluster_1: 11.372
- **Magnitude:** 185.48 | **LOC:** 429 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (3.5807%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fragment_not_sent_with_request` (Impact: 25.1 | O(N^3) | DB: 15)
  * `test_use_proxy_from_environment` (Impact: 20.8 | O(N^4) | DB: 6)
  * `test_digestauth_401_count_reset_on_redir` (Impact: 13.4 | O(N^5) | DB: 6)
    * *Intent:* """ text_401 = (b'HTTP/1.1 401 UNAUTHORIZED\r\n' b'Content-Length: 0\r\n' b'WWW-Authenticate: Digest...
  * `test_digestauth_401_only_sent_once` (Impact: 12.5 | O(N^5) | DB: 6)
  * `test_digestauth_only_on_4xx` (Impact: 12.0 | O(N^5) | DB: 6)
    * *Intent:* """Ensure we only send digestauth on 4xx challenges. See https://github.com/psf/requests/issues/3772...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 95`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `orphaned_logic: 10`
* *Architecture:* `io: 23`, `api: 22`, `concurrency: 18`, `import: 6`
* *Defense:* `safety: 44`, `doc: 22`, `test: 61`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` requests.compat, threading, .utils, pytest, tests.testserver.server, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/tests/testserver/server.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.479 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.477 IQR)
- **Top Global Matches:** file_cluster_4: 11.479, file_cluster_13: 11.702, file_cluster_0: 11.779
- **Magnitude:** 181.54 | **LOC:** 177 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (33.6921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__exit__` (Impact: 23.0 | O(N^4))
  * `run` (Impact: 18.0 | O(N^4) | DB: 2)
  * `consume_socket_content` (Impact: 14.7 | O(N^3))
  * `_handle_requests` (Impact: 13.5 | O(N^4) | DB: 1)
  * `_accept_connection` (Impact: 13.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 35`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 36`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 10`, `concurrency: 14`, `import: 4`
* *Defense:* `safety: 6`, `doc: 2`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 0):` socket, threading, select, ssl
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_testserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.042 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.919 IQR)
- **Top Global Matches:** file_cluster_13: 13.042, file_cluster_0: 13.156, file_cluster_6: 13.396
- **Magnitude:** 120.64 | **LOC:** 166 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (2.5423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multiple_requests` (Impact: 18.1 | O(N^4) | DB: 9)
  * `test_server_finishes_on_error` (Impact: 13.4 | O(N^4))
    * *Intent:* # and get killed by the jenkins timeout. def test_server_finishes_when_no_connections(self): """the ...
  * `test_server_closes` (Impact: 11.0 | O(N^3) | DB: 15)
  * `test_request_recovery` (Impact: 8.0 | O(N^3) | DB: 12)
  * `test_basic` (Impact: 7.8 | O(N^3) | DB: 6)
    * *Intent:* """messages are sent and received properly"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 11`
* *Architecture:* `io: 24`, `api: 13`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 15`, `doc: 22`, `test: 32`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` socket, threading, pytest, tests.testserver.server, time, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.789 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.887 IQR)
- **Top Global Matches:** file_cluster_13: 13.789, file_cluster_7: 14.013, file_cluster_8: 14.098
- **Magnitude:** 84.88 | **LOC:** 153 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (31.2734%), Tech Debt (99.9991%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 32.5 | O(2^N) | DB: 5)
    * *Intent:* """There was an ambiguous exception that occurred while handling your request. """
  * `__init__` (Impact: 6.2 | O(2^N))
  * `__reduce__` (Impact: 5.4 | O(2^N))
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

### `requests-2.33.1/src/requests/structures.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.76 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.831 IQR)
- **Top Global Matches:** file_cluster_13: 11.76, file_cluster_8: 11.944, file_cluster_7: 12.115
- **Magnitude:** 82.0 | **LOC:** 100 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (39.0677%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__eq__` (Impact: 10.7 | O(N^3))
  * `__init__` (Impact: 8.2 | O(N^3) | DB: 2)
    * *Intent:* """A case-insensitive ``dict``-like object. Implements all methods and operations of ``MutableMappin...
  * `get` (Impact: 6.1 | O(2^N))
    * *Intent:* # Compare insensitively # Copy is required def copy(self): return CaseInsensitiveDict(self._store.va...
  * `lower_items` (Impact: 5.4 | O(N^2))
  * `__iter__` (Impact: 5.3 | O(N^2))
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

### `requests-2.33.1/src/requests/help.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.487 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.698 IQR)
- **Top Global Matches:** file_cluster_8: 9.487, file_cluster_13: 9.558, file_cluster_7: 9.986
- **Magnitude:** 64.36 | **LOC:** 132 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (6.9938%), Tech Debt (93.0993%)
**Top Internal Functions/Classes:**
  * `_implementation` (Impact: 31.4 | O(N^4) | DB: 9)
  * `info` (Impact: 27.1 | O(N^3) | DB: 3)
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 20`, `args: 3`, `func_start: 3`
* *Risk/State:* `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 2`, `import: 12`
* *Defense:* `safety: 10`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.748
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 0):` urllib3, ssl, cryptography, idna, chardet, charset_normalizer, json, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_structures.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.09 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.837 IQR)
- **Top Global Matches:** file_cluster_0: 12.09, file_cluster_13: 12.41, file_cluster_8: 12.477
- **Magnitude:** 53.08 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lower_items` (Impact: 3.7 | O(N^3))
  * `test_instance_equality` (Impact: 3.1 | O(N^2) | DB: 1)
  * `test_getitem` (Impact: 3.1 | O(N^2))
  * `test_get` (Impact: 3.1 | O(N^2))
  * `setup` (Impact: 2.8 | O(N^2) | DB: 1)
    * *Intent:* """CaseInsensitiveDict instance with "Accept" header."""
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

### `requests-2.33.1/src/requests/api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_7` (Drift: 11.563 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.382 IQR)
- **Top Global Matches:** file_cluster_7: 11.563, file_cluster_8: 11.588, file_cluster_1: 11.77
- **Magnitude:** 49.42 | **LOC:** 158 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.4071%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 12.4 | O(2^N))
  * `post` (Impact: 4.7 | O(2^N))
  * `get` (Impact: 4.2 | O(2^N))
  * `put` (Impact: 4.2 | O(2^N))
  * `patch` (Impact: 4.2 | O(2^N))
    * *Intent:* # By using the 'with' statement we are sure the session is closed, thus we # avoid leaving sockets o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 19`, `args: 8`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 64`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.214
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 0):` requests, 
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.148 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.445 IQR)
- **Top Global Matches:** file_cluster_13: 11.148, file_cluster_8: 11.583, file_cluster_17: 11.901
- **Magnitude:** 46.66 | **LOC:** 184 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (11.1136%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_compatibility` (Impact: 29.6 | O(N^3) | DB: 1)
  * `_check_cryptography` (Impact: 11.0 | O(N^3))
    * *Intent:* # Sometimes, urllib3 only reports its version as 16.1. if len(urllib3_version) == 2: urllib3_version...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 44`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `safety: 18`, `doc: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` urllib3, urllib3.exceptions, ssl, logging, .status_codes, cryptography, .exceptions, charset_normalizer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/hooks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.203 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.907 IQR)
- **Top Global Matches:** file_cluster_8: 10.203, file_cluster_7: 10.463, file_cluster_6: 10.639
- **Magnitude:** 42.08 | **LOC:** 35 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `dispatch_hook` (Impact: 34.2 | O(N^4))
  * `default_hooks` (Impact: 3.6 | O(N^1))
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

### `requests-2.33.1/src/requests/status_codes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.925 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.394 IQR)
- **Top Global Matches:** file_cluster_8: 6.925, file_cluster_7: 7.739, file_cluster_1: 7.987
- **Magnitude:** 41.44 | **LOC:** 129 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.1022%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_init` (Impact: 35.5 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.335
  * `Choke Point (Betweenness):` 0.000148 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 1):` requests, .structures
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 41.02 | **LOC:** 2051 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

### `requests-2.33.1/tests/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.109 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.395 IQR)
- **Top Global Matches:** file_cluster_13: 12.109, file_cluster_0: 12.172, file_cluster_11: 12.573
- **Magnitude:** 29.7 | **LOC:** 18 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (43.3036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `override_environ` (Impact: 21.4 | O(N^3) | DB: 17)
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

### `requests-2.33.1/tests/test_help.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.033 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.304 IQR)
- **Top Global Matches:** file_cluster_13: 14.033, file_cluster_8: 14.539, file_cluster_7: 14.635
- **Magnitude:** 20.66 | **LOC:** 28 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_idna_without_version_attribute` (Impact: 5.4 | O(N^2) | DB: 3)
  * `test_idna_with_version_attribute` (Impact: 5.4 | O(N^2) | DB: 3)
    * *Intent:* """Verify we're actually setting idna version when it should be available."""
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
  * `test_system_ssl` (Impact: 1.9 | O(N^1))
    * *Intent:* """Verify we're actually setting system_ssl when it should be available."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 4`, `import: 2`
* *Defense:* `safety: 3`, `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.458
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, requests.help
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/compat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.026 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.898 IQR)
- **Top Global Matches:** file_cluster_13: 9.026, file_cluster_8: 9.129, file_cluster_7: 9.765
- **Magnitude:** 19.1 | **LOC:** 107 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.1586%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_resolve_char_detection` (Impact: 17.9 | O(N^4))
    * *Intent:* # ------------------- # Character Detection # ------------------- def _resolve_char_detection(): """...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 30`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 1`, `import: 15`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.832
  * `Choke Point (Betweenness):` 0.000887 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 1):` urllib3, importlib, io, simplejson, urllib.request, http, collections.abc, resolution...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/_internal_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.343 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.966 IQR)
- **Top Global Matches:** file_cluster_8: 11.343, file_cluster_13: 11.49, file_cluster_7: 11.665
- **Magnitude:** 18.3 | **LOC:** 52 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.9875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `to_native_string` (Impact: 8.2 | O(N^2))
  * `unicode_is_ascii` (Impact: 5.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 5`, `doc: 7`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 84.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.15
  * `Imports (Out-Degree: 0):` .compat, re
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/certs/expired/server/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.104 IQR)
- **Top Global Matches:** file_cluster_8: 7.104, file_cluster_7: 8.165, file_cluster_1: 8.328
- **Magnitude:** 18.22 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `requests-2.33.1/tests/test_structures.py` (PYTHON) | Magnitude: 53.08 | Delta: **0.32 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 29, test: 29, api: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `requests-2.33.1/tests/utils.py` (PYTHON) | Magnitude: 29.7 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 6, branch: 5, io: 5
- `requests-2.33.1/src/requests/cookies.py` (PYTHON) | Magnitude: 942.74 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 273, structural_boundaries: 111, doc: 91, branch: 74
- `requests-2.33.1/src/requests/sessions.py` (PYTHON) | Magnitude: 597.96 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 386, structural_boundaries: 92, branch: 91, doc: 87
- `requests-2.33.1/tests/test_hooks.py` (PYTHON) | Magnitude: 8.7 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, test: 6, args: 4
- `requests-2.33.1/src/requests/compat.py` (PYTHON) | Magnitude: 19.1 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 30, indent_spaces: 30, import: 15, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `requests-2.33.1/tests/testserver/server.py` (PYTHON) | Magnitude: 181.54 | Delta: **0.223 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, state_mutation: 36, structural_boundaries: 35, branch: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `requests-2.33.1/src/requests/api.py` (PYTHON) | Magnitude: 49.42 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 64, structural_boundaries: 19, indent_spaces: 17, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `requests-2.33.1/tests/test_utils.py` (PYTHON) | Magnitude: 369.72 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 697, structural_boundaries: 246, test: 184, api: 94
- `requests-2.33.1/tests/test_requests.py` (PYTHON) | Magnitude: 1517.26 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2335, structural_boundaries: 854, test: 736, safety: 451
- `requests-2.33.1/setup.py` (PYTHON) | Magnitude: 13.12 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, io: 3, branch: 2, import: 2
- `requests-2.33.1/src/requests/help.py` (PYTHON) | Magnitude: 64.36 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_13`
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

- `requests-2.33.1/src/requests/adapters.py` -> **Severity: 3.143** (Embedded: 0.0667 * Error Risk: 47.1504%)
- `requests-2.33.1/src/requests/structures.py` -> **Severity: 2.247** (Embedded: 0.1736 * Error Risk: 12.9431%)
- `requests-2.33.1/src/requests/exceptions.py` -> **Severity: 1.472** (Embedded: 0.1534 * Error Risk: 9.5921%)
- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 1.204** (Embedded: 0.1801 * Error Risk: 6.686%)
- `requests-2.33.1/tests/testserver/server.py` -> **Severity: 1.011** (Embedded: 0.0625 * Error Risk: 16.1807%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `requests-2.33.1/src/requests/_internal_utils.py` -> **Severity: 7414.416** (Blast Radius: 84.831 * Doc Risk: 87.4022%)
- `requests-2.33.1/src/requests/structures.py` -> **Severity: 5963.021** (Blast Radius: 59.632 * Doc Risk: 99.997%)
- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 5881.676** (Blast Radius: 58.817 * Doc Risk: 99.9996%)
- `requests-2.33.1/src/requests/exceptions.py` -> **Severity: 4944.36** (Blast Radius: 49.457 * Doc Risk: 99.9729%)
- `requests-2.33.1/src/requests/adapters.py` -> **Severity: 2653.813** (Blast Radius: 29.624 * Doc Risk: 89.5832%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
