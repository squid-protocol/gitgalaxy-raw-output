# ARCHITECTURAL_BRIEF: pyjwt
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 41 | 91.1% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 68.7 | 11.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.2 | 37.0 | 26.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.9 | 2.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 98.6 | 17.3 | 3.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 81.8 | 1.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 52.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 48.8 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 37.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 120 | 10 | 7 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| cleanup | 1 | 1 | 0 | `pyjwt-2.12.1/jwt/jwks_client.py` |
| guards | 511 | 15 | 49 | `pyjwt-2.12.1/tests/test_api_jws.py` |
| danger | 259 | 13 | 18 | `pyjwt-2.12.1/jwt/algorithms.py` |
| concurrency | 2 | 1 | 0 | `pyjwt-2.12.1/jwt/api_jwk.py` |
| connectivity | 456 | 23 | 24 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| io | 133 | 9 | 3 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| crypto | 9 | 8 | 1 | `pyjwt-2.12.1/jwt/algorithms.py` |
| ipc | 0 | 0 | 0 | - |
| time | 16 | 3 | 0 | `pyjwt-2.12.1/tests/test_api_jwt.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `pyjwt-2.12.1/jwt/utils.py` |
| events | 1 | 1 | 0 | `pyjwt-2.12.1/jwt/api_jws.py` |
| tests | 497 | 10 | 10 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| docs | 116 | 15 | 8 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| debt | 8 | 2 | 0 | `pyjwt-2.12.1/tests/test_api_jwk.py` |
| mutation | 2549 | 22 | 153 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| dead_code | 300 | 9 | 7 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| credential | 49 | 4 | 0 | `pyjwt-2.12.1/tests/test_algorithms.py` |
| threat | 36 | 6 | 1 | `pyjwt-2.12.1/jwt/algorithms.py` |
| ml_ai | 1 | 1 | 0 | `pyjwt-2.12.1/jwt/__init__.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

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

- `encode` (@ `pyjwt-2.12.1/jwt/api_jws.py`) -> Impact: **70.5** | LOC: 89
- `__init__` (@ `pyjwt-2.12.1/jwt/api_jwk.py`) -> Impact: **47.1** | LOC: 63
  * *Intent:* """A class that represents a `JSON Web Key <https://www.rfc-editor.org/rfc/rfc7517>`_. :param jwk_data: The decoded JWK data. :type jwk_data: dict[str...
- `_validate_aud` (@ `pyjwt-2.12.1/jwt/api_jwt.py`) -> Impact: **44.9** | LOC: 49
- `_validate_claims` (@ `pyjwt-2.12.1/jwt/api_jwt.py`) -> Impact: **44.5** | LOC: 41
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **41.8** | LOC: 72
- `decode_complete` (@ `pyjwt-2.12.1/jwt/api_jws.py`) -> Impact: **39.3** | LOC: 50
- `decode_complete` (@ `pyjwt-2.12.1/jwt/api_jwt.py`) -> Impact: **37.9** | LOC: 109
- `_verify_signature` (@ `pyjwt-2.12.1/jwt/api_jws.py`) -> Impact: **33.6** | LOC: 37
- `from_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **30.4** | LOC: 70
- `to_jwk` (@ `pyjwt-2.12.1/jwt/algorithms.py`) -> Impact: **24.6** | LOC: 42

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyjwt-2.12.1/tests` | 11 | 2163.28 | 10.96% | 0.0% |
| `pyjwt-2.12.1/jwt` | 12 | 1908.82 | 29.51% | 8.24% |
| `pyjwt-2.12.1/tests/keys` | 19 | 248.58 | 0.3% | 0.0% |
| `pyjwt-2.12.1` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyjwt-2.12.1/jwt/help.py` -> **98.9013%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pyjwt-2.12.1/jwt/api_jws.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/help.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/jwks_client.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **99.9998%** Exposure
- `pyjwt-2.12.1/jwt/utils.py` -> **99.9997%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyjwt-2.12.1/tests/test_algorithms.py` -> **103** Orphaned Functions | **0** Duplicates
- `pyjwt-2.12.1/tests/test_api_jwt.py` -> **81** Orphaned Functions | **0** Duplicates
- `pyjwt-2.12.1/tests/test_api_jws.py` -> **79** Orphaned Functions | **0** Duplicates
- `pyjwt-2.12.1/tests/test_api_jwk.py` -> **22** Orphaned Functions | **0** Duplicates
- `pyjwt-2.12.1/tests/test_utils.py` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `pyjwt-2.12.1/tests/test_advisory.py` -> **100.0%** Exposure
- `pyjwt-2.12.1/tests/test_api_jwt.py` -> **99.9871%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `129` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyjwt-2.12.1/jwt/api_jwk.py` (PYTHON) -> Cumulative Risk: **591.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 147.34 | **LOC:** 189 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Safety Score (87.1943%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 47.1), `__init__` (Impact: 11.5), `__getitem__` (Impact: 7.2)

### 2. `pyjwt-2.12.1/jwt/algorithms.py` (PYTHON) -> Cumulative Risk: **566.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 666.5 | **LOC:** 999 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9961%), Api Exposure (83.5888%), Safety Score (81.6939%)
- **Heaviest Functions:** `from_jwk` (Impact: 41.8), `from_jwk` (Impact: 30.4), `to_jwk` (Impact: 24.6)

### 3. `pyjwt-2.12.1/jwt/utils.py` (PYTHON) -> Cumulative Risk: **554.14**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 85.34 | **LOC:** 143 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (86.2463%)
- **Heaviest Functions:** `force_bytes` (Impact: 6.0), `to_base64url_uint` (Impact: 5.7), `raw_to_der_signature` (Impact: 4.0)

### 4. `pyjwt-2.12.1/jwt/jwks_client.py` (PYTHON) -> Cumulative Risk: **524.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 140.64 | **LOC:** 234 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.9479%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 22.8), `get_signing_keys` (Impact: 9.9), `get_jwk_set` (Impact: 9.8)

### 5. `pyjwt-2.12.1/tests/test_advisory.py` (PYTHON) -> Cumulative Risk: **505.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 16.74 | **LOC:** 120 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Secrets Risk (100.0%), Dead Code (81.7574%)
- **Heaviest Functions:** `test_ghsa_ffqj_6fqr_9h24` (Impact: 3.9)

### 6. `pyjwt-2.12.1/jwt/jwk_set_cache.py` (PYTHON) -> Cumulative Risk: **492.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 28.96 | **LOC:** 32 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.0834%), Safety Score (71.9676%)
- **Heaviest Functions:** `put` (Impact: 5.5), `is_expired` (Impact: 4.6), `get` (Impact: 4.5)

### 7. `pyjwt-2.12.1/jwt/api_jws.py` (PYTHON) -> Cumulative Risk: **492.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 386.6 | **LOC:** 408 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.7225%), Cognitive Load (60.9215%)
- **Heaviest Functions:** `encode` (Impact: 70.5), `decode_complete` (Impact: 39.3), `_verify_signature` (Impact: 33.6)

### 8. `pyjwt-2.12.1/jwt/help.py` (PYTHON) -> Cumulative Risk: **476.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 35.28 | **LOC:** 67 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.9013%), Safety Score (84.2905%)
- **Heaviest Functions:** `info` (Impact: 7.2), `main` (Impact: 1.1)

### 9. `pyjwt-2.12.1/jwt/exceptions.py` (PYTHON) -> Cumulative Risk: **466.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 26.12 | **LOC:** 114 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (99.1837%), Api Exposure (98.5623%)
- **Heaviest Functions:** `__init__` (Impact: 1.8), `__str__` (Impact: 1.5)

### 10. `pyjwt-2.12.1/jwt/api_jwt.py` (PYTHON) -> Cumulative Risk: **464.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 328.96 | **LOC:** 591 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7159%), Documentation (90.9091%), Safety Score (82.1236%)
- **Heaviest Functions:** `_validate_aud` (Impact: 44.9), `_validate_claims` (Impact: 44.5), `decode_complete` (Impact: 37.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyjwt-2.12.1/tests/test_algorithms.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 812.82 | **LOC:** 1624 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.5291%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ec_to_jwk_with_valid_curves` (Impact: 11.7)
  * `test_rsa_to_jwk_returns_correct_values_for_private_key` (Impact: 8.2)
  * `test_ec_jwk_fails_on_invalid_json` (Impact: 7.2)
  * `test_rsa_to_jwk_returns_correct_values_for_public_key` (Impact: 6.5)
  * `test_okp_ed25519_to_jwk_works_with_from_jwk` (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 419
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 521`, `args: 103`, `func_start: 103`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 331`, `unreferenced_by_name: 103`
* *Architecture:* `io: 81`, `api: 108`, `import: 42`
* *Defense:* `safety: 109`, `doc: 22`, `test: 180`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .keys, .utils, base64, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.asymmetric.ec, cryptography.hazmat.primitives.asymmetric.ed25519, cryptography.hazmat.primitives.asymmetric.ed448, cryptography.hazmat.primitives.asymmetric.rsa...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/algorithms.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 666.5 | **LOC:** 999 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.7187%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_jwk` (Impact: 41.8)
  * `from_jwk` (Impact: 30.4)
  * `to_jwk` (Impact: 24.6)
  * `to_jwk` (Impact: 23.0)
  * `prepare_key` (Impact: 20.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 192`, `args: 53`, `func_start: 53`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 91`
* *Architecture:* `io: 3`, `api: 55`, `import: 25`
* *Defense:* `safety: 64`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.273
  * `Choke Point (Betweenness):` 0.003171 | `Ripple Effect (Closeness):` 0.225936
  * `Imports (Out-Degree: 2):` .exceptions, .types, .utils, __future__, abc, cryptography.exceptions, cryptography.hazmat.backends, cryptography.hazmat.primitives...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/tests/test_api_jwt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 585.3 | **LOC:** 1103 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.2915%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decode_with_expiration_with_leeway` (Impact: 6.9)
  * `test_decode_strict_aud_does_not_match` (Impact: 6.8)
  * `test_decode_warns_on_unsupported_kwarg` (Impact: 6.7)
  * `test_decode_complete_warns_on_unsupported_kwarg` (Impact: 6.7)
  * `test_decode_strict_aud_forbids_list_claim` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 251
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 228`, `args: 84`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `state_mutation: 213`, `unreferenced_by_name: 81`
* *Architecture:* `io: 2`, `api: 85`, `import: 14`
* *Defense:* `safety: 49`, `doc: 8`, `test: 133`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .utils, calendar, datetime, decimal, json, jwt.api_jwk, jwt.api_jwt, jwt.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/test_api_jws.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 532.02 | **LOC:** 1119 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.4813%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decode_warns_on_unsupported_kwarg` (Impact: 7.0)
  * `test_decode_complete_warns_on_unuspported_kwarg` (Impact: 7.0)
  * `test_rsa_related_algorithms` (Impact: 6.1)
  * `test_ecdsa_related_algorithms` (Impact: 5.9)
  * `test_decode_rejects_unknown_crit_extension` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 304`, `args: 81`, `func_start: 81`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 188`, `unreferenced_by_name: 79`
* *Architecture:* `io: 12`, `api: 83`, `import: 14`
* *Defense:* `safety: 113`, `doc: 3`, `test: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .utils, cryptography.hazmat.primitives.asymmetric.ec, cryptography.hazmat.primitives.asymmetric.rsa, cryptography.hazmat.primitives.serialization, decimal, json, jwt.algorithms, jwt.api_jwk...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/api_jws.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 386.6 | **LOC:** 408 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.9215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode` (Impact: 70.5)
  * `decode_complete` (Impact: 39.3)
  * `_verify_signature` (Impact: 33.6)
  * `__init__` (Impact: 12.9)
  * `_validate_crit` (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 73`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 59`
* *Architecture:* `api: 10`, `import: 13`
* *Defense:* `safety: 26`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.611
  * `Choke Point (Betweenness):` 0.000617 | `Ripple Effect (Closeness):` 0.081169
  * `Imports (Out-Degree: 5):` .algorithms, .api_jwk, .exceptions, .types, .utils, .warnings, __future__, binascii...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/api_jwt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 328.96 | **LOC:** 591 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.7797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_validate_aud` (Impact: 44.9)
  * `_validate_claims` (Impact: 44.5)
  * `decode_complete` (Impact: 37.9)
  * `encode` (Impact: 20.2)
  * `_validate_iss` (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 73`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 34`
* *Architecture:* `io: 2`, `api: 5`, `import: 17`
* *Defense:* `safety: 26`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.493
  * `Choke Point (Betweenness):` 0.002731 | `Ripple Effect (Closeness):` 0.068182
  * `Imports (Out-Degree: 6):` .algorithms, .api_jwk, .api_jws, .exceptions, .types, .warnings, __future__, calendar...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/tests/test_api_jwk.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 163.3 | **LOC:** 342 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.2339%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_from_dict_should_throw_exception_if_arg_is_invalid` (Impact: 3.5)
  * `test_keyset_iterator` (Impact: 3.4)
  * `test_keyset_should_index_by_kid` (Impact: 2.5)
  * `test_should_load_key_from_jwk_data_dict` (Impact: 2.4)
  * `test_should_load_key_from_jwk_data_json_string` (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 150`, `args: 22`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 84`, `planned_debt: 5`, `unreferenced_by_name: 22`
* *Architecture:* `io: 20`, `api: 24`, `import: 7`
* *Defense:* `safety: 64`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .utils, json, jwt.algorithms, jwt.api_jwk, jwt.exceptions, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/api_jwk.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 147.34 | **LOC:** 189 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.4263%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 47.1)
    * *Intent:* """A class that represents a `JSON Web Key <https://www.rfc-editor.org/rfc/rfc7517>`_. :param jwk_da...
  * `__init__` (Impact: 11.5)
  * `__getitem__` (Impact: 7.2)
  * `from_json` (Impact: 2.3)
    * *Intent:* """Create a :class:`PyJWK` object from a JSON string. Implicitly calls :meth:`PyJWK.from_dict()`. :p...
  * `from_dict` (Impact: 2.2)
    * *Intent:* """Creates a :class:`PyJWK` object from a JSON-like dictionary. :param obj: The JWK data, as a dicti...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 45`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 20`
* *Architecture:* `api: 14`, `import: 8`
* *Defense:* `safety: 7`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.354
  * `Choke Point (Betweenness):` 0.003524 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 3):` .algorithms, .exceptions, .types, __future__, collections.abc, json, time, typing
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/jwks_client.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 140.64 | **LOC:** 234 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3593%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 22.8)
  * `get_signing_keys` (Impact: 9.9)
    * *Intent:* """Return all signing keys from the JWK Set. Filters the JWK Set to keys whose ``use`` is ``"sig"`` ...
  * `get_jwk_set` (Impact: 9.8)
    * *Intent:* """Return the JWK Set, using the cache when available. :param refresh: Force a fresh fetch from the ...
  * `fetch_data` (Impact: 7.1)
    * *Intent:* """Fetch the JWK Set from the JWKS endpoint. Makes an HTTP request to the configured ``uri`` and ret...
  * `get_signing_key` (Impact: 6.5)
    * *Intent:* """Return the signing key matching the given ``kid``. If no match is found in the current JWK Set, t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 42`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`
* *Architecture:* `api: 8`, `import: 11`
* *Defense:* `safety: 4`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.577
  * `Choke Point (Betweenness):` 0.000529 | `Ripple Effect (Closeness):` 0.022727
  * `Imports (Out-Degree: 4):` .api_jwk, .api_jwt, .exceptions, .jwk_set_cache, __future__, functools, json, ssl...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 85.34 | **LOC:** 143 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.1762%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `force_bytes` (Impact: 6.0)
  * `to_base64url_uint` (Impact: 5.7)
  * `raw_to_der_signature` (Impact: 4.0)
  * `bytes_from_int` (Impact: 3.8)
  * `base64url_decode` (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 35`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.66
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.113636
  * `Imports (Out-Degree: 0):` base64, binascii, cryptography.hazmat.primitives.asymmetric.ec, cryptography.hazmat.primitives.asymmetric.utils, re, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/help.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 35.28 | **LOC:** 67 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.9213%), Tech Debt (98.9013%)
**Top Internal Functions/Classes:**
  * `info` (Impact: 7.2)
    * *Intent:* """ Generate information for a bug report. Based on the requests package help utility module. """
  * `main` (Impact: 1.1)
    * *Intent:* """Pretty-print the bug information as JSON."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 10`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , cryptography, json, platform, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/jwk_set_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.96 | **LOC:** 32 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.7816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `put` (Impact: 5.5)
  * `is_expired` (Impact: 4.6)
  * `get` (Impact: 4.5)
  * `__init__` (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 1):` .api_jwk, time, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.4 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .api_jwk, .api_jws, .api_jwt, .exceptions, .jwks_client, .warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/jwt/exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 26.12 | **LOC:** 114 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1.8)
  * `__str__` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 40`, `args: 2`, `func_start: 2`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1`
* *Architecture:* `api: 21`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 104.541
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.284091
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/jwt/types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 20.6 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.193676
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyjwt-2.12.1/tests/keys/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 18.24 | **LOC:** 53 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.7533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `decode_value` (Impact: 1.6)
  * `load_ec_pub_key_p_521` (Impact: 1.4)
  * `load_hmac_key` (Impact: 1.2)
  * `load_rsa_pub_key` (Impact: 1.1)
  * `load_rsa_pub_key` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 9`, `api: 6`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cryptography.hazmat.primitives.asymmetric, json, jwt.algorithms, jwt.utils, os, sys, typing, typing_extensions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/test_advisory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.74 | **LOC:** 120 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ghsa_ffqj_6fqr_9h24` (Impact: 3.9)
    * *Intent:* # Generate ed25519 private key # private_key = ed25519.Ed25519PrivateKey.generate() # Get private ke...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `doc: 3`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .utils, jwt, jwt.algorithms, jwt.exceptions, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyjwt-2.12.1/tests/keys/jwk_rsa_key.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.26 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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

### `pyjwt-2.12.1/jwt/warnings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.08 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.139205
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyjwt-2.12.1/jwt/api_jwk.py` -> **Severity: 0.352** (Bridge: 0.0035 * Flux: 99.9998%)
- `pyjwt-2.12.1/jwt/algorithms.py` -> **Severity: 0.317** (Bridge: 0.0032 * Flux: 99.9961%)
- `pyjwt-2.12.1/jwt/api_jwt.py` -> **Severity: 0.272** (Bridge: 0.0027 * Flux: 99.7159%)
- `pyjwt-2.12.1/jwt/api_jws.py` -> **Severity: 0.062** (Bridge: 0.0006 * Flux: 100.0%)
- `pyjwt-2.12.1/jwt/jwks_client.py` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyjwt-2.12.1/jwt/exceptions.py` -> **Severity: 28.177** (Embedded: 0.2841 * Error Risk: 99.1837%)
- `pyjwt-2.12.1/jwt/algorithms.py` -> **Severity: 18.458** (Embedded: 0.2259 * Error Risk: 81.6939%)
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **Severity: 15.853** (Embedded: 0.1818 * Error Risk: 87.1943%)
- `pyjwt-2.12.1/jwt/types.py` -> **Severity: 14.267** (Embedded: 0.1937 * Error Risk: 73.6639%)
- `pyjwt-2.12.1/jwt/utils.py` -> **Severity: 9.801** (Embedded: 0.1136 * Error Risk: 86.2463%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyjwt-2.12.1/jwt/exceptions.py` -> **Severity: 10454.1** (Blast Radius: 104.541 * Doc Risk: 100.0%)
- `pyjwt-2.12.1/jwt/algorithms.py` -> **Severity: 5810.185** (Blast Radius: 72.273 * Doc Risk: 80.3922%)
- `pyjwt-2.12.1/jwt/utils.py` -> **Severity: 4266.0** (Blast Radius: 42.66 * Doc Risk: 100.0%)
- `pyjwt-2.12.1/jwt/api_jwk.py` -> **Severity: 2931.824** (Blast Radius: 52.354 * Doc Risk: 56.0%)
- `pyjwt-2.12.1/jwt/api_jwt.py` -> **Severity: 2135.727** (Blast Radius: 23.493 * Doc Risk: 90.9091%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
