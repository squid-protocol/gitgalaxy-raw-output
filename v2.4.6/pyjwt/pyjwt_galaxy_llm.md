# ARCHITECTURAL_BRIEF: pyjwt
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pyjwt` |
| **Timestamp** | `2026-08-03T21:23:56.279490+00:00` |
| **Scan Duration** | `0.33s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 24 malicious artifacts.

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
| Total Artifacts | 62 |
| Analyzed Artifacts (Scanned) | 45 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 5394 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 72.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1898 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2607 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9684 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 24 | 5276 | 53.3% |
| JSON | 18 | 118 | 40.0% |
| MARKDOWN | 2 | 0 | 4.4% |
| PLAINTEXT | 1 | 0 | 2.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.117`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 26 | 57.8% |
| file_cluster_13 | 9 | 20.0% |
| file_cluster_0 | 3 | 6.7% |
| file_cluster_16 | 3 | 6.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 6.7% |
| Static: Minified & Vendor Opaque Mass | 1 | 2.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 2x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.priv`: 3x Excluded (Unsupported Extension: '.priv')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (Saturation: Line 31 exceeds 500 chars)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 69.6 | 7.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 90.9 | 11.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.6 | 3.8 | 1.1 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 81.8 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 68.9 | 73.3 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 48.8 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.5 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 23.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyjwt-2.12.1/tests/test_algorithms.py` (Hits: 81)
- `pyjwt-2.12.1/tests/test_api_jwk.py` (Hits: 20)
- `pyjwt-2.12.1/tests/test_api_jws.py` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **exceptions.py** (`pyjwt-2.12.1/jwt/exceptions.py`) — 12 inbound connections
2. **algorithms.py** (`pyjwt-2.12.1/jwt/algorithms.py`) — 9 inbound connections
3. **api_jwk.py** (`pyjwt-2.12.1/jwt/api_jwk.py`) — 8 inbound connections
4. **warnings.py** (`pyjwt-2.12.1/jwt/warnings.py`) — 6 inbound connections
5. **types.py** (`pyjwt-2.12.1/jwt/types.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **algorithms.py** (`pyjwt-2.12.1/jwt/algorithms.py`) — 22 outbound dependencies
2. **test_algorithms.py** (`pyjwt-2.12.1/tests/test_algorithms.py`) — 17 outbound dependencies
3. **api_jwt.py** (`pyjwt-2.12.1/jwt/api_jwt.py`) — 16 outbound dependencies
4. **test_api_jws.py** (`pyjwt-2.12.1/tests/test_api_jws.py`) — 13 outbound dependencies
5. **test_api_jwt.py** (`pyjwt-2.12.1/tests/test_api_jwt.py`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_decodes_complete_valid_jwt` (@ `pyjwt-2.12.1/tests/test_api_jwt.py`) -> Impact: **410.1** | LOC: 1031
- `test_decodes_complete_valid_jws` (@ `pyjwt-2.12.1/tests/test_api_jws.py`) -> Impact: **298.9** | LOC: 779
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **243.6** | LOC: 72
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **175.0** | LOC: 70
- `__init__` (@ `pyjwt-2.12.1/jwt/api_jwk.py`) -> Impact: **140.8** | LOC: 55
  * *Intent:* """A class that represents a `JSON Web Key <https://www.rfc-editor.org/rfc/rfc7517>`_. :param jwk_data: The decoded JWK data. :type jwk_data: dict[str...
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **113.1** | LOC: 33
- `to_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **69.6** | LOC: 42
- `verify` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **67.9** | LOC: 16
- `test_ec_jwk_fails_on_invalid_json` (@ `pyjwt-2.12.1/tests/test_algorithms.py`) -> Impact: **65.3** | LOC: 59
- `to_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **64.6** | LOC: 45

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `verify` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(2^N) [Recursive]**
- `verify` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(2^N) [Recursive]**
- `sign` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(2^N) [Recursive]**
- `verify` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(2^N) [Recursive]**
- `sign` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(2^N) [Recursive]**
- `sign` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(2^N) [Recursive]**
- `number_to_bytes` (@ `pyjwt-2.12.1/jwt/utils.py`) -> **O(2^N) [Recursive]**
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(N^6)**
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(N^6)**
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `test_decodes_complete_valid_jws` (@ `pyjwt-2.12.1/tests/test_api_jws.py`) -> DB Complexity: **24**
- `test_jwt_encode_decode_rejects_wrong_cur` (@ `pyjwt-2.12.1/tests/test_algorithms.py`) -> DB Complexity: **12**
  * *Intent:* # P-192 PEM key should be rejected
- `test_ec_algorithm_without_expected_curve` (@ `pyjwt-2.12.1/tests/test_algorithms.py`) -> DB Complexity: **12**
- `test_from_dict_should_throw_exception_if` (@ `pyjwt-2.12.1/tests/test_api_jwk.py`) -> DB Complexity: **9**
- `key_path` (@ `pyjwt-2.12.1/tests/utils.py`) -> DB Complexity: **9**
- `load_ec_pub_key_p_521` (@ `pyjwt-2.12.1/tests/keys/__init__.py`) -> DB Complexity: **6**
- `load_rsa_pub_key` (@ `pyjwt-2.12.1/tests/keys/__init__.py`) -> DB Complexity: **6**
- `load_hmac_key` (@ `pyjwt-2.12.1/tests/keys/__init__.py`) -> DB Complexity: **6**
- `test_ec_to_jwk_with_valid_curves` (@ `pyjwt-2.12.1/tests/test_algorithms.py`) -> DB Complexity: **6**
- `test_okp_ed25519_jwk_fails_on_invalid_js` (@ `pyjwt-2.12.1/tests/test_algorithms.py`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyjwt-2.12.1/tests` | 11 | 2496.58 | 3.7% | 0.0% |
| `pyjwt-2.12.1/jwt` | 12 | 2212.52 | 16.81% | 24.92% |
| `pyjwt-2.12.1/tests/keys` | 19 | 265.28 | 4.78% | 0.0% |
| `pyjwt-2.12.1` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **99.9997%** Exposure
- `pyjwt-2.12.1/jwt/algorithms.py` -> **99.9894%** Exposure
- `pyjwt-2.12.1/jwt/help.py` -> **99.0462%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pyjwt-2.12.1/jwt/jwk_set_cache.py` -> **99.995%** Exposure
- `pyjwt-2.12.1/jwt/jwks_client.py` -> **99.7415%** Exposure
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **97.1584%** Exposure
- `pyjwt-2.12.1/jwt/api_jws.py` -> **65.7761%** Exposure
- `pyjwt-2.12.1/jwt/api_jwt.py` -> **21.3872%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyjwt-2.12.1/tests/test_algorithms.py` -> **80** Orphaned Functions | **23** Duplicates
- `pyjwt-2.12.1/jwt/algorithms.py` -> **0** Orphaned Functions | **35** Duplicates
- `pyjwt-2.12.1/tests/test_api_jws.py` -> **26** Orphaned Functions | **0** Duplicates
- `pyjwt-2.12.1/tests/test_api_jwk.py` -> **22** Orphaned Functions | **0** Duplicates
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **0** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pyjwt-2.12.1/jwt/api_jws.py`** -> AI Confidence: **99.31%**
2. **`pyjwt-2.12.1/jwt/api_jwt.py`** -> AI Confidence: **99.31%**
3. **`pyjwt-2.12.1/jwt/algorithms.py`** -> AI Confidence: **99.24%**
4. **`pyjwt-2.12.1/jwt/api_jwk.py`** -> AI Confidence: **99.24%**
5. **`pyjwt-2.12.1/tests/test_api_jws.py`** -> AI Confidence: **99.18%**
6. **`pyjwt-2.12.1/tests/test_api_jwt.py`** -> AI Confidence: **99.18%**
7. **`pyjwt-2.12.1/jwt/jwks_client.py`** -> AI Confidence: **99.16%**
8. **`pyjwt-2.12.1/tests/test_algorithms.py`** -> AI Confidence: **99.16%**
9. **`pyjwt-2.12.1/tests/keys/__init__.py`** -> AI Confidence: **99.06%**
10. **`pyjwt-2.12.1/jwt/help.py`** -> AI Confidence: **99.03%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `pyjwt-2.12.1/tests/test_compressed_jwt.py` -> **0.0078%** Exposure
### Exploit Generation Surface
- `pyjwt-2.12.1/jwt/algorithms.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/api_jws.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/api_jwt.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/jwks_client.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `pyjwt-2.12.1/tests/test_advisory.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/tests/test_api_jwt.py` -> **99.9871%** Exposure
### Algorithmic DoS Exposure
- `pyjwt-2.12.1/jwt/algorithms.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/jwk_set_cache.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/tests/keys/__init__.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/tests/test_algorithms.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `129` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyjwt-2.12.1/jwt/api_jwk.py` (PYTHON) -> Cumulative Risk: **784.94**
- **Archetype:** `file_cluster_13` (Distance: 12.096 IQR)
- **Magnitude:** 263.84 | **LOC:** 189 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9997%)
- **Heaviest Functions:** `__init__` (Impact: 140.8), `__init__` (Impact: 37.5), `__getitem__` (Impact: 17.6)

### 2. `pyjwt-2.12.1/jwt/jwks_client.py` (PYTHON) -> Cumulative Risk: **715.73**
- **Archetype:** `file_cluster_13` (Distance: 12.336 IQR)
- **Magnitude:** 134.24 | **LOC:** 234 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9575%), State Flux (99.7415%)
- **Heaviest Functions:** `fetch_data` (Impact: 31.4), `get_jwk_set` (Impact: 18.0), `get_signing_keys` (Impact: 18.0)

### 3. `pyjwt-2.12.1/jwt/jwk_set_cache.py` (PYTHON) -> Cumulative Risk: **649.69**
- **Archetype:** `file_cluster_13` (Distance: 10.934 IQR)
- **Magnitude:** 47.16 | **LOC:** 32 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9987%)
- **Heaviest Functions:** `put` (Impact: 10.7), `is_expired` (Impact: 10.7), `get` (Impact: 10.6)

### 4. `pyjwt-2.12.1/jwt/algorithms.py` (PYTHON) -> Cumulative Risk: **596.09**
- **Archetype:** `file_cluster_0` (Distance: 11.445 IQR)
- **Magnitude:** 1302.3 | **LOC:** 999 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9894%)
- **Heaviest Functions:** `from_jwk` (Impact: 243.6), `from_jwk` (Impact: 175.0), `from_jwk` (Impact: 113.1)

### 5. `pyjwt-2.12.1/jwt/api_jws.py` (PYTHON) -> Cumulative Risk: **589.62**
- **Archetype:** `file_cluster_13` (Distance: 11.348 IQR)
- **Magnitude:** 184.1 | **LOC:** 408 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.5195%), Documentation (92.1758%)
- **Heaviest Functions:** `_validate_crit` (Impact: 42.6), `_load` (Impact: 33.0), `get_algorithm_by_name` (Impact: 21.3)

### 6. `pyjwt-2.12.1/jwt/api_jwt.py` (PYTHON) -> Cumulative Risk: **551.83**
- **Archetype:** `file_cluster_16` (Distance: 10.901 IQR)
- **Magnitude:** 96.06 | **LOC:** 591 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.8743%), Verification (80.0%)
- **Heaviest Functions:** `_decode_payload` (Impact: 12.5), `_validate_jti` (Impact: 12.4), `_merge_options` (Impact: 11.1)

### 7. `pyjwt-2.12.1/tests/test_api_jwt.py` (PYTHON) -> Cumulative Risk: **465.38**
- **Archetype:** `file_cluster_8` (Distance: 10.319 IQR)
- **Magnitude:** 528.2 | **LOC:** 1103 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Secrets Risk (99.9871%)
- **Heaviest Functions:** `test_decodes_complete_valid_jwt` (Impact: 410.1), `test_encode_with_jwk_uses_key_algorithm` (Impact: 5.1), `test_decodes_valid_jwt` (Impact: 4.0)

### 8. `pyjwt-2.12.1/tests/test_advisory.py` (PYTHON) -> Cumulative Risk: **400.49**
- **Archetype:** `file_cluster_13` (Distance: 19.059 IQR)
- **Magnitude:** 18.84 | **LOC:** 120 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Secrets Risk (100.0%), Dead Code (81.7574%), Algorithmic Dos (62.2459%)
- **Heaviest Functions:** `test_ghsa_ffqj_6fqr_9h24` (Impact: 16.0)

### 9. `pyjwt-2.12.1/jwt/help.py` (PYTHON) -> Cumulative Risk: **395.06**
- **Archetype:** `file_cluster_8` (Distance: 8.986 IQR)
- **Magnitude:** 38.08 | **LOC:** 67 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9934%), Tech Debt (99.0462%), Stability (50.0%)
- **Heaviest Functions:** `info` (Impact: 33.2), `main` (Impact: 1.9)

### 10. `pyjwt-2.12.1/jwt/exceptions.py` (PYTHON) -> Cumulative Risk: **391.96**
- **Archetype:** `file_cluster_8` (Distance: 10.535 IQR)
- **Magnitude:** 28.22 | **LOC:** 114 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9993%), Safety Score (90.9013%), Stability (50.0%)
- **Heaviest Functions:** `__init__` (Impact: 2.7), `__str__` (Impact: 2.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyjwt-2.12.1/jwt/algorithms.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.445 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.748 IQR)
- **Top Global Matches:** file_cluster_0: 11.445, file_cluster_16: 11.452, file_cluster_13: 11.492
- **Magnitude:** 1302.3 | **LOC:** 999 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (15.2341%), Tech Debt (99.9894%)
**Top Internal Functions/Classes:**
  * `from_jwk` (Impact: 243.6 | O(N^6))
  * `from_jwk` (Impact: 175.0 | O(N^6))
  * `from_jwk` (Impact: 113.1 | O(N^6))
  * `to_jwk` (Impact: 69.6 | O(N^5))
  * `verify` (Impact: 67.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 192`, `args: 53`, `func_start: 53`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 12`, `duplicate_logic: 35`
* *Architecture:* `io: 3`, `api: 57`, `import: 25`
* *Defense:* `safety: 66`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.273
  * `Choke Point (Betweenness):` 0.003171 | `Ripple Effect (Closeness):` 0.225936
  * `Imports (Out-Degree: 2):` __future__, cryptography.hazmat.primitives.asymmetric, .exceptions, cryptography.hazmat.primitives.asymmetric.ec, .types, abc, cryptography.hazmat.primitives.asymmetric.types, typing...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/tests/test_algorithms.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.622 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.308 IQR)
- **Top Global Matches:** file_cluster_0: 11.622, file_cluster_8: 11.716, file_cluster_13: 11.754
- **Magnitude:** 1117.92 | **LOC:** 1624 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (2.9649%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ec_jwk_fails_on_invalid_json` (Impact: 65.3 | O(N^5))
  * `test_ec_to_jwk_with_valid_curves` (Impact: 42.9 | O(N^5) | DB: 6)
  * `test_okp_ed25519_jwk_fails_on_invalid_js` (Impact: 40.7 | O(N^3) | DB: 6)
  * `test_okp_ed448_jwk_fails_on_invalid_json` (Impact: 40.7 | O(N^3) | DB: 6)
  * `test_jwt_encode_decode_rejects_wrong_cur` (Impact: 26.2 | O(N^3) | DB: 12)
    * *Intent:* # P-192 PEM key should be rejected
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 375`, `args: 103`, `func_start: 103`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `duplicate_logic: 23`, `orphaned_logic: 80`
* *Architecture:* `io: 81`, `api: 108`, `import: 42`
* *Defense:* `safety: 112`, `doc: 44`, `test: 280`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` jwt.exceptions, .utils, .keys, json, jwt.utils, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.serialization, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/test_api_jws.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.231 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.391 IQR)
- **Top Global Matches:** file_cluster_8: 11.231, file_cluster_16: 11.425, file_cluster_0: 11.6
- **Magnitude:** 539.72 | **LOC:** 1119 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (3.4598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decodes_complete_valid_jws` (Impact: 298.9 | O(N^4) | DB: 24)
  * `test_bad_secret` (Impact: 12.7 | O(N^3))
  * `test_encode_with_headers_alg_es256` (Impact: 12.6 | O(N^3) | DB: 6)
  * `test_decode_invalid_token_type_is_none` (Impact: 9.3 | O(N^4))
  * `test_decode_invalid_token_type_is_int` (Impact: 9.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 252`, `args: 81`, `func_start: 81`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 26`
* *Architecture:* `io: 12`, `api: 83`, `import: 14`
* *Defense:* `safety: 113`, `doc: 7`, `test: 228`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` jwt.exceptions, decimal, .utils, json, jwt.api_jws, jwt.utils, cryptography.hazmat.primitives.serialization, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/test_api_jwt.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.319 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.258 IQR)
- **Top Global Matches:** file_cluster_8: 10.319, file_cluster_16: 10.45, file_cluster_13: 10.872
- **Magnitude:** 528.2 | **LOC:** 1103 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (3.1077%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decodes_complete_valid_jwt` (Impact: 410.1 | O(N^5) | DB: 6)
  * `test_encode_with_jwk_uses_key_algorithm` (Impact: 5.1 | O(N^4))
  * `test_decodes_valid_jwt` (Impact: 4.0 | O(N^3))
  * `test_jwt_with_options` (Impact: 2.9 | O(N^2))
  * `payload` (Impact: 1.9 | O(N^1))
    * *Intent:* """Creates a sample JWT claimset for use as a payload during tests"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 179`, `args: 84`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 85`, `import: 14`
* *Defense:* `safety: 49`, `doc: 15`, `test: 179`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` jwt.api_jwt, jwt.exceptions, decimal, calendar, datetime, .utils, json, jwt.utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/api_jwk.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.096 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.132 IQR)
- **Top Global Matches:** file_cluster_13: 12.096, file_cluster_16: 12.262, file_cluster_0: 12.3
- **Magnitude:** 263.84 | **LOC:** 189 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (44.0911%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 140.8 | O(N^5) | DB: 4)
    * *Intent:* """A class that represents a `JSON Web Key <https://www.rfc-editor.org/rfc/rfc7517>`_. :param jwk_da...
  * `__init__` (Impact: 37.5 | O(N^5) | DB: 1)
  * `__getitem__` (Impact: 17.6 | O(N^4))
  * `from_json` (Impact: 3.1 | O(N^2))
  * `from_dict` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 45`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 17`, `duplicate_logic: 7`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 7`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.354
  * `Choke Point (Betweenness):` 0.003524 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 3):` .algorithms, __future__, json, .exceptions, .types, collections.abc, time, typing
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/tests/test_api_jwk.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.689 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.256 IQR)
- **Top Global Matches:** file_cluster_0: 11.689, file_cluster_8: 12.02, file_cluster_13: 12.162
- **Magnitude:** 239.9 | **LOC:** 342 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (4.1742%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_from_dict_should_throw_exception_if` (Impact: 36.7 | O(N^3) | DB: 9)
  * `test_keyset_with_unknown_alg` (Impact: 18.1 | O(N^4) | DB: 6)
    * *Intent:* # first keyset with unusable key and usable key with open(key_path("jwk_keyset_with_unknown_alg.json...
  * `test_keyset_should_index_by_kid` (Impact: 11.4 | O(N^3) | DB: 3)
  * `test_keyset_iterator` (Impact: 11.0 | O(N^3) | DB: 3)
  * `test_should_load_key_from_jwk_data_dict` (Impact: 7.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 117`, `args: 22`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 5`, `orphaned_logic: 22`
* *Architecture:* `io: 20`, `api: 24`, `import: 7`
* *Defense:* `safety: 64`, `test: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jwt.exceptions, .utils, json, pytest, jwt.algorithms, jwt.api_jwk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/api_jws.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.348 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.437 IQR)
- **Top Global Matches:** file_cluster_13: 11.348, file_cluster_16: 11.374, file_cluster_8: 11.392
- **Magnitude:** 184.1 | **LOC:** 408 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (18.0742%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_validate_crit` (Impact: 42.6 | O(N^5))
  * `_load` (Impact: 33.0 | O(N^3))
  * `get_algorithm_by_name` (Impact: 21.3 | O(N^5))
  * `register_algorithm` (Impact: 12.6 | O(N^3))
    * *Intent:* """ Registers a new Algorithm for use when creating and verifying tokens. :param str alg_id: the ID ...
  * `unregister_algorithm` (Impact: 9.2 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 73`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 22`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 29`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.611
  * `Choke Point (Betweenness):` 0.000617 | `Ripple Effect (Closeness):` 0.081169
  * `Imports (Out-Degree: 5):` .algorithms, __future__, .warnings, .utils, binascii, json, .api_jwk, .exceptions...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/jwks_client.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.336 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.925 IQR)
- **Top Global Matches:** file_cluster_13: 12.336, file_cluster_16: 12.683, file_cluster_8: 12.923
- **Magnitude:** 134.24 | **LOC:** 234 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.7998%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetch_data` (Impact: 31.4 | O(N^4))
  * `get_jwk_set` (Impact: 18.0 | O(N^3))
  * `get_signing_keys` (Impact: 18.0 | O(N^3))
  * `get_signing_key` (Impact: 16.4 | O(N^5))
  * `match_kid` (Impact: 13.5 | O(N^4))
    * *Intent:* """ data = None if self.jwk_set_cache is not None and not refresh: data = self.jwk_set_cache.get() i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 41`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`
* *Architecture:* `api: 9`, `import: 11`
* *Defense:* `safety: 5`, `doc: 52`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.577
  * `Choke Point (Betweenness):` 0.000529 | `Ripple Effect (Closeness):` 0.022727
  * `Imports (Out-Degree: 4):` __future__, json, ssl, urllib.error, .api_jwk, functools, .exceptions, .jwk_set_cache...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/api_jwt.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.901 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.532 IQR)
- **Top Global Matches:** file_cluster_16: 10.901, file_cluster_8: 10.936, file_cluster_13: 10.997
- **Magnitude:** 96.06 | **LOC:** 591 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (9.7606%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_decode_payload` (Impact: 12.5 | O(N^3))
  * `_validate_jti` (Impact: 12.4 | O(N^3))
  * `_merge_options` (Impact: 11.1 | O(N^3))
  * `__init__` (Impact: 7.3 | O(N^3) | DB: 3)
  * `_get_sig_options` (Impact: 4.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 73`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 5`, `import: 17`
* *Defense:* `safety: 26`, `doc: 59`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.493
  * `Choke Point (Betweenness):` 0.002731 | `Ripple Effect (Closeness):` 0.068182
  * `Imports (Out-Degree: 6):` typing_extensions, __future__, .api_jws, .algorithms, calendar, datetime, os, json...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.867 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.378 IQR)
- **Top Global Matches:** file_cluster_16: 8.867, file_cluster_8: 8.886, file_cluster_13: 9.181
- **Magnitude:** 68.44 | **LOC:** 143 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9933%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `number_to_bytes` (Impact: 19.6 | O(2^N))
  * `force_bytes` (Impact: 10.7 | O(N^2))
  * `to_base64url_uint` (Impact: 9.5 | O(N^2))
  * `base64url_decode` (Impact: 5.6 | O(N^2))
  * `base64url_encode` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 35`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.66
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.113636
  * `Imports (Out-Degree: 0):` binascii, cryptography.hazmat.primitives.asymmetric.utils, base64, cryptography.hazmat.primitives.asymmetric.ec, re, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/jwk_set_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.934 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.76 IQR)
- **Top Global Matches:** file_cluster_13: 10.934, file_cluster_16: 11.012, file_cluster_8: 11.314
- **Magnitude:** 47.16 | **LOC:** 32 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (69.5527%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `put` (Impact: 10.7 | O(N^3) | DB: 2)
  * `is_expired` (Impact: 10.7 | O(N^3))
  * `get` (Impact: 10.6 | O(N^3))
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 1):` typing, .api_jwk, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/help.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.986 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.223 IQR)
- **Top Global Matches:** file_cluster_8: 8.986, file_cluster_13: 9.056, file_cluster_16: 9.343
- **Magnitude:** 38.08 | **LOC:** 67 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.7019%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `info` (Impact: 33.2 | O(N^5) | DB: 3)
    * *Intent:* """ Generate information for a bug report. Based on the requests package help utility module. """
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 10`, `args: 2`, `func_start: 2`
* *Risk/State:* `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cryptography, json, platform, , sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.375 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.626 IQR)
- **Top Global Matches:** file_cluster_13: 8.375, file_cluster_8: 8.7, file_cluster_16: 8.722
- **Magnitude:** 34.94 | **LOC:** 53 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.8197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_ec_pub_key_p_521` (Impact: 7.4 | O(N^3) | DB: 6)
  * `load_rsa_pub_key` (Impact: 7.1 | O(N^3) | DB: 6)
  * `load_hmac_key` (Impact: 5.4 | O(N^2) | DB: 6)
  * `load_rsa_pub_key` (Impact: 2.7 | O(N^2))
  * `load_ec_pub_key_p_521` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 30`, `args: 6`, `func_start: 6`
* *Risk/State:* `duplicate_logic: 4`
* *Architecture:* `io: 9`, `api: 7`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typing_extensions, os, json, jwt.utils, cryptography.hazmat.primitives.asymmetric, jwt.algorithms, typing, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.535 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.298 IQR)
- **Top Global Matches:** file_cluster_8: 10.535, file_cluster_7: 10.553, file_cluster_16: 10.585
- **Magnitude:** 28.22 | **LOC:** 114 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.4257%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
  * `__str__` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 40`, `args: 2`, `func_start: 2`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1`
* *Architecture:* `api: 21`
* *Defense:* `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 104.541
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.284091
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/tests/test_advisory.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 19.059 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.953 IQR)
- **Top Global Matches:** file_cluster_13: 19.059, file_cluster_0: 19.131, file_cluster_9: 19.303
- **Magnitude:** 18.84 | **LOC:** 120 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.6981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ghsa_ffqj_6fqr_9h24` (Impact: 16.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `dead_code: 6`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jwt.exceptions, .utils, pytest, jwt.algorithms, jwt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.515 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.416 IQR)
- **Top Global Matches:** file_cluster_16: 9.515, file_cluster_8: 9.639, file_cluster_7: 9.769
- **Magnitude:** 18.6 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.0517%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.193676
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.18 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.684 IQR)
- **Top Global Matches:** file_cluster_8: 5.18, file_cluster_13: 6.337, file_cluster_7: 6.586
- **Magnitude:** 17.4 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .api_jws, .warnings, .jwks_client, .api_jwk, .exceptions, .api_jwt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/test_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.207 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.22 IQR)
- **Top Global Matches:** file_cluster_8: 9.207, file_cluster_13: 9.382, file_cluster_0: 9.467
- **Magnitude:** 15.42 | **LOC:** 63 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.5593%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_force_bytes_raises_error_on_invalid` (Impact: 5.3 | O(N^2))
  * `test_is_ssh_key` (Impact: 2.1 | O(N^1))
  * `test_from_base64url_uint` (Impact: 1.9 | O(N^1))
  * `test_to_base64url_uint` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`
* *Risk/State:* `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 4`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jwt.utils, pytest, contextlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_rsa_key.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.26 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_okp_key_Ed448.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_ec_key_P-256.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_ec_key_P-384.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_ec_key_P-521.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_ec_key_secp256k1.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_okp_pub_Ed448.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pyjwt-2.12.1/jwt/algorithms.py` (PYTHON) | Magnitude: 1302.3 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 733, structural_boundaries: 192, branch: 163, generics: 79
- `pyjwt-2.12.1/tests/test_algorithms.py` (PYTHON) | Magnitude: 1117.92 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1139, structural_boundaries: 375, test: 280, branch: 173
- `pyjwt-2.12.1/tests/test_api_jwk.py` (PYTHON) | Magnitude: 239.9 | Delta: **0.331 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 235, structural_boundaries: 117, test: 91, safety: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyjwt-2.12.1/jwt/api_jws.py` (PYTHON) | Magnitude: 184.1 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 276, branch: 78, structural_boundaries: 73, encapsulation: 44
- `pyjwt-2.12.1/tests/test_advisory.py` (PYTHON) | Magnitude: 18.84 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, dead_code: 6, doc: 6
- `pyjwt-2.12.1/jwt/jwk_set_cache.py` (PYTHON) | Magnitude: 47.16 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, state_mutation: 7, branch: 6
- `pyjwt-2.12.1/tests/test_exceptions.py` (PYTHON) | Magnitude: 2.98 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 4, test: 2, indent_spaces: 2, args: 1
- `pyjwt-2.12.1/jwt/api_jwk.py` (PYTHON) | Magnitude: 263.84 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 45, branch: 31, doc: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pyjwt-2.12.1/jwt/utils.py` (PYTHON) | Magnitude: 68.44 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 35, generics: 17, api: 15
- `pyjwt-2.12.1/jwt/api_jwt.py` (PYTHON) | Magnitude: 96.06 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 349, branch: 79, structural_boundaries: 73, doc: 59
- `pyjwt-2.12.1/jwt/types.py` (PYTHON) | Magnitude: 18.6 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 30, indent_spaces: 24, structural_boundaries: 5, generics: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyjwt-2.12.1/jwt/exceptions.py` (PYTHON) | Magnitude: 28.22 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 40, doc: 30, indent_spaces: 22, api: 21
- `pyjwt-2.12.1/jwt/warnings.py` (PYTHON) | Magnitude: 14.08 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 4, class_start: 2, safety_bypasses: 2
- `pyjwt-2.12.1/jwt/help.py` (PYTHON) | Magnitude: 38.08 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 10, branch: 7, import: 5
- `pyjwt-2.12.1/tests/test_api_jwt.py` (PYTHON) | Magnitude: 528.2 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 851, structural_boundaries: 179, test: 179, generics: 104
- `pyjwt-2.12.1/tests/test_utils.py` (PYTHON) | Magnitude: 15.42 | Delta: **0.175 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 16, test: 14, args: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyjwt-2.12.1/jwt/api_jwk.py` -> **Severity: 0.342** (Bridge: 0.0035 * Flux: 97.1584%)
- `pyjwt-2.12.1/jwt/api_jwt.py` -> **Severity: 0.058** (Bridge: 0.0027 * Flux: 21.3872%)
- `pyjwt-2.12.1/jwt/jwks_client.py` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 99.7415%)
- `pyjwt-2.12.1/jwt/algorithms.py` -> **Severity: 0.051** (Bridge: 0.0032 * Flux: 16.1889%)
- `pyjwt-2.12.1/jwt/api_jws.py` -> **Severity: 0.041** (Bridge: 0.0006 * Flux: 65.7761%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyjwt-2.12.1/jwt/exceptions.py` -> **Severity: 25.824** (Embedded: 0.2841 * Error Risk: 90.9013%)
- `pyjwt-2.12.1/jwt/types.py` -> **Severity: 15.494** (Embedded: 0.1937 * Error Risk: 80.0%)
- `pyjwt-2.12.1/jwt/warnings.py` -> **Severity: 11.136** (Embedded: 0.1392 * Error Risk: 80.0%)
- `pyjwt-2.12.1/jwt/api_jws.py` -> **Severity: 4.87** (Embedded: 0.0812 * Error Risk: 60.0%)
- `pyjwt-2.12.1/jwt/api_jwt.py` -> **Severity: 4.269** (Embedded: 0.0682 * Error Risk: 62.6087%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyjwt-2.12.1/jwt/exceptions.py` -> **Severity: 10454.027** (Blast Radius: 104.541 * Doc Risk: 99.9993%)
- `pyjwt-2.12.1/jwt/algorithms.py` -> **Severity: 7225.948** (Blast Radius: 72.273 * Doc Risk: 99.9813%)
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **Severity: 5223.212** (Blast Radius: 52.354 * Doc Risk: 99.7672%)
- `pyjwt-2.12.1/jwt/utils.py` -> **Severity: 4210.879** (Blast Radius: 42.66 * Doc Risk: 98.7079%)
- `pyjwt-2.12.1/jwt/api_jws.py` -> **Severity: 2084.187** (Blast Radius: 22.611 * Doc Risk: 92.1758%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
