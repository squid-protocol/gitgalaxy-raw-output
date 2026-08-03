# ARCHITECTURAL_BRIEF: msal
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/msal` |
| **Timestamp** | `2026-08-03T21:22:27.521078+00:00` |
| **Scan Duration** | `0.46s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 48 malicious artifacts.

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
| Total Artifacts | 52 |
| Analyzed Artifacts (Scanned) | 49 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 9037 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4818 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1788 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8996 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 48 | 9037 | 98.0% |
| MARKDOWN | 1 | 0 | 2.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.277`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 33 | 67.3% |
| file_cluster_13 | 15 | 30.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 42 exceeds 500 chars)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 43.1 | 9.6 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 68.5 | 11.6 | 4.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.4 | 0.3 | 0.0 |
| API Exposure | 0.0 | 9.5 | 3.8 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 96.1 | 3.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.2 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 93.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.5 | 6.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 80.4 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 57.5 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.9 | 5.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `msal-1.35.1/msal/managed_identity.py` (Hits: 39)
- `msal-1.35.1/tests/test_mi.py` (Hits: 30)
- `msal-1.35.1/tests/test_e2e.py` (Hits: 28)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **authcode.py** (`msal-1.35.1/msal/oauth2cli/authcode.py`) — 7 inbound connections
2. **oidc.py** (`msal-1.35.1/msal/oauth2cli/oidc.py`) — 7 inbound connections
3. **application.py** (`msal-1.35.1/msal/application.py`) — 5 inbound connections
4. **token_cache.py** (`msal-1.35.1/msal/token_cache.py`) — 5 inbound connections
5. **mex.py** (`msal-1.35.1/msal/mex.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **application.py** (`msal-1.35.1/msal/application.py`) — 39 outbound dependencies
2. **authcode.py** (`msal-1.35.1/msal/oauth2cli/authcode.py`) — 21 outbound dependencies
3. **test_e2e.py** (`msal-1.35.1/tests/test_e2e.py`) — 20 outbound dependencies
4. **managed_identity.py** (`msal-1.35.1/msal/managed_identity.py`) — 16 outbound dependencies
5. **oauth2.py** (`msal-1.35.1/msal/oauth2cli/oauth2.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_build_client` (@ `msal-1.35.1/msal/application.py`) -> Impact: **3404.6** | LOC: 1099
- `_acquire_token_interactive` (@ `msal-1.35.1/msal/__main__.py`) -> Impact: **978.3** | LOC: 246
- `_obtain_token` (@ `msal-1.35.1/msal/oauth2cli/oauth2.py`) -> Impact: **829.0** | LOC: 288
- `skipUnlessWithConfig` (@ `msal-1.35.1/tests/test_e2e.py`) -> Impact: **677.4** | LOC: 1077
- `_get_app_and_auth_code` (@ `msal-1.35.1/tests/test_e2e.py`) -> Impact: **449.2** | LOC: 279
- `__init__` (@ `msal-1.35.1/msal/authority.py`) -> Impact: **351.8** | LOC: 106
- `_process_auth_response` (@ `msal-1.35.1/msal/oauth2cli/authcode.py`) -> Impact: **332.9** | LOC: 232
- `add` (@ `msal-1.35.1/msal/token_cache.py`) -> Impact: **275.8** | LOC: 195
- `obtain_token_by_authorization_code` (@ `msal-1.35.1/msal/oauth2cli/oidc.py`) -> Impact: **238.5** | LOC: 74
- `test_unknown_family_app_will_attempt_frt` (@ `msal-1.35.1/tests/test_application.py`) -> Impact: **231.6** | LOC: 753

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_acquire_token_interactive` (@ `msal-1.35.1/msal/__main__.py`) -> **O(2^N) [Recursive]**
- `_build_client` (@ `msal-1.35.1/msal/application.py`) -> **O(2^N) [Recursive]**
- `obtain_token_by_authorization_code` (@ `msal-1.35.1/msal/oauth2cli/oidc.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `msal-1.35.1/msal/throttled_http_client.py`) -> **O(2^N) [Recursive]**
- `initiate_device_flow` (@ `msal-1.35.1/msal/application.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `msal-1.35.1/msal/managed_identity.py`) -> **O(2^N) [Recursive]**
- `_obtain_token` (@ `msal-1.35.1/msal/oauth2cli/oauth2.py`) -> **O(2^N) [Recursive]**
- `skipUnlessWithConfig` (@ `msal-1.35.1/tests/test_e2e.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `msal-1.35.1/msal/managed_identity.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ def __init__(self): super(SystemAssignedManagedIdentity, self).__init__(id_type=self.SYSTEM_ASSIGNED) class UserAssignedManagedIdentity(ManagedIde...
- `_epoch_to_local` (@ `msal-1.35.1/msal/oauth2cli/oidc.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # On Python 2.7, argument of urlsafe_b64decode must be str, not unicode.

### Highest Data Gravity (Database Complexity)
- `skipUnlessWithConfig` (@ `msal-1.35.1/tests/test_e2e.py`) -> DB Complexity: **84**
- `test_happy_path` (@ `msal-1.35.1/tests/test_mi.py`) -> DB Complexity: **42**
- `_build_client` (@ `msal-1.35.1/msal/application.py`) -> DB Complexity: **37**
- `test_unknown_family_app_will_attempt_frt` (@ `msal-1.35.1/tests/test_application.py`) -> DB Complexity: **25**
- `_get_arc_endpoint` (@ `msal-1.35.1/msal/managed_identity.py`) -> DB Complexity: **24**
  * *Intent:* # This class only throttles excess token acquisition requests. # It does not provide retry. # Retry is the http_client or caller's responsibility, not...
- `get_managed_identity_source` (@ `msal-1.35.1/msal/managed_identity.py`) -> DB Complexity: **21**
- `_acquire_token_interactive` (@ `msal-1.35.1/msal/__main__.py`) -> DB Complexity: **18**
- `send_request` (@ `msal-1.35.1/msal/mex.py`) -> DB Complexity: **18**
- `_test_happy_path` (@ `msal-1.35.1/tests/test_mi.py`) -> DB Complexity: **18**
- `__init__` (@ `msal-1.35.1/msal/oauth2cli/oauth2.py`) -> DB Complexity: **15**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `msal-1.35.1/msal` | 18 | 8228.88 | 15.78% | 24.9% |
| `msal-1.35.1/tests` | 23 | 3662.22 | 3.51% | 0.0% |
| `msal-1.35.1/msal/oauth2cli` | 6 | 2468.6 | 15.04% | 37.17% |
| `msal-1.35.1` | 2 | 14.04 | 2.5% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `msal-1.35.1/msal/throttled_http_client.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/oauth2cli/assertion.py` -> **98.6482%** Exposure
- `msal-1.35.1/msal/managed_identity.py` -> **91.9399%** Exposure
- `msal-1.35.1/msal/individual_cache.py` -> **84.1131%** Exposure
- `msal-1.35.1/msal/authority.py` -> **83.5956%** Exposure
### Highest State Flux (Mutation/Volatility)
- `msal-1.35.1/msal/telemetry.py` -> **99.9944%** Exposure
- `msal-1.35.1/msal/individual_cache.py` -> **99.9672%** Exposure
- `msal-1.35.1/msal/throttled_http_client.py` -> **99.9348%** Exposure
- `msal-1.35.1/msal/oauth2cli/assertion.py` -> **99.8653%** Exposure
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **98.7895%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `msal-1.35.1/tests/test_authority.py` -> **11** Orphaned Functions | **10** Duplicates
- `msal-1.35.1/tests/test_e2e_manual.py` -> **13** Orphaned Functions | **2** Duplicates
- `msal-1.35.1/tests/test_mi.py` -> **11** Orphaned Functions | **4** Duplicates
- `msal-1.35.1/tests/test_application.py` -> **10** Orphaned Functions | **4** Duplicates
- `msal-1.35.1/tests/test_individual_cache.py` -> **12** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`msal-1.35.1/msal/__main__.py`** -> AI Confidence: **99.31%**
2. **`msal-1.35.1/msal/application.py`** -> AI Confidence: **99.31%**
3. **`msal-1.35.1/msal/broker.py`** -> AI Confidence: **99.31%**
4. **`msal-1.35.1/msal/managed_identity.py`** -> AI Confidence: **99.31%**
5. **`msal-1.35.1/msal/oauth2cli/authcode.py`** -> AI Confidence: **99.31%**
6. **`msal-1.35.1/msal/oauth2cli/oauth2.py`** -> AI Confidence: **99.31%**
7. **`msal-1.35.1/msal/token_cache.py`** -> AI Confidence: **99.31%**
8. **`msal-1.35.1/msal/cloudshell.py`** -> AI Confidence: **99.23%**
9. **`msal-1.35.1/msal/oauth2cli/oidc.py`** -> AI Confidence: **99.23%**
10. **`msal-1.35.1/tests/test_mi.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `msal-1.35.1/msal/__main__.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/application.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/authority.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/individual_cache.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/managed_identity.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `msal-1.35.1/tests/test_optional_thumbprint.py` -> **99.9295%** Exposure
- `msal-1.35.1/msal/application.py` -> **75.9921%** Exposure
- `msal-1.35.1/tests/test_application.py` -> **67.0021%** Exposure
### Algorithmic DoS Exposure
- `msal-1.35.1/msal/__main__.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/application.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/authority.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/individual_cache.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/managed_identity.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `294` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `msal-1.35.1/msal/throttled_http_client.py` (PYTHON) -> Cumulative Risk: **816.49**
- **Archetype:** `file_cluster_13` (Distance: 12.001 IQR)
- **Magnitude:** 314.88 | **LOC:** 180 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 160.0), `parse` (Impact: 34.3), `__init__` (Impact: 22.8)

### 2. `msal-1.35.1/msal/token_cache.py` (PYTHON) -> Cumulative Risk: **781.93**
- **Archetype:** `file_cluster_8` (Distance: 10.381 IQR)
- **Magnitude:** 719.38 | **LOC:** 446 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.8332%)
- **Heaviest Functions:** `add` (Impact: 275.8), `search` (Impact: 160.9), `__init__` (Impact: 117.9)

### 3. `msal-1.35.1/msal/oauth2cli/authcode.py` (PYTHON) -> Cumulative Risk: **775.28**
- **Archetype:** `file_cluster_13` (Distance: 11.324 IQR)
- **Magnitude:** 541.5 | **LOC:** 440 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `_process_auth_response` (Impact: 332.9), `_browse` (Impact: 58.3), `do_GET` (Impact: 31.3)

### 4. `msal-1.35.1/msal/individual_cache.py` (PYTHON) -> Cumulative Risk: **759.16**
- **Archetype:** `file_cluster_13` (Distance: 11.936 IQR)
- **Magnitude:** 286.84 | **LOC:** 291 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9958%)
- **Heaviest Functions:** `__init__` (Impact: 42.9), `__call__` (Impact: 36.3), `__getitem__` (Impact: 26.9)

### 5. `msal-1.35.1/msal/authority.py` (PYTHON) -> Cumulative Risk: **732.35**
- **Archetype:** `file_cluster_8` (Distance: 10.287 IQR)
- **Magnitude:** 612.96 | **LOC:** 306 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (96.4985%)
- **Heaviest Functions:** `__init__` (Impact: 351.8), `has_valid_issuer` (Impact: 95.8), `canonicalize` (Impact: 76.0)

### 6. `msal-1.35.1/msal/oauth2cli/assertion.py` (PYTHON) -> Cumulative Risk: **728.23**
- **Archetype:** `file_cluster_13` (Distance: 11.618 IQR)
- **Magnitude:** 64.22 | **LOC:** 138 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9967%), Logic Bomb (99.9432%), State Flux (99.8653%)
- **Heaviest Functions:** `__call__` (Impact: 10.8), `create_regenerative_assertion` (Impact: 7.0), `create_normal_assertion` (Impact: 6.6)

### 7. `msal-1.35.1/msal/telemetry.py` (PYTHON) -> Cumulative Risk: **693.85**
- **Archetype:** `file_cluster_8` (Distance: 10.664 IQR)
- **Magnitude:** 139.56 | **LOC:** 79 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9944%)
- **Heaviest Functions:** `__init__` (Impact: 113.5), `_get_new_correlation_id` (Impact: 1.8)

### 8. `msal-1.35.1/msal/oauth2cli/oidc.py` (PYTHON) -> Cumulative Risk: **642.74**
- **Archetype:** `file_cluster_8` (Distance: 10.035 IQR)
- **Magnitude:** 513.08 | **LOC:** 339 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (98.6312%)
- **Heaviest Functions:** `obtain_token_by_authorization_code` (Impact: 238.5), `decode_id_token` (Impact: 88.3), `obtain_token_by_browser` (Impact: 64.5)

### 9. `msal-1.35.1/msal/oauth2cli/oauth2.py` (PYTHON) -> Cumulative Risk: **639.54**
- **Archetype:** `file_cluster_13` (Distance: 12.067 IQR)
- **Magnitude:** 1314.44 | **LOC:** 879 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (98.7895%)
- **Heaviest Functions:** `_obtain_token` (Impact: 829.0), `obtain_token_by_browser` (Impact: 210.9), `__init__` (Impact: 148.1)

### 10. `msal-1.35.1/msal/managed_identity.py` (PYTHON) -> Cumulative Risk: **634.54**
- **Archetype:** `file_cluster_8` (Distance: 9.893 IQR)
- **Magnitude:** 352.52 | **LOC:** 689 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (91.9399%)
- **Heaviest Functions:** `__init__` (Impact: 135.4), `_obtain_token_on_azure_vm` (Impact: 38.8), `get_managed_identity_source` (Impact: 35.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `msal-1.35.1/msal/application.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.457 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.541 IQR)
- **Top Global Matches:** file_cluster_8: 11.457, file_cluster_13: 11.628, file_cluster_7: 11.683
- **Magnitude:** 3957.3 | **LOC:** 2556 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (14.0527%), Tech Debt (10.5121%)
**Top Internal Functions/Classes:**
  * `_build_client` (Impact: 3404.6 | O(2^N) | DB: 37)
  * `_preferred_browser` (Impact: 86.8 | O(N^5) | DB: 14)
    * *Intent:* """Register Edge and return a name suitable for subsequent webbrowser.get(...) when appropriate. Oth...
  * `_get_regional_authority` (Impact: 74.4 | O(N^5) | DB: 6)
  * `_clean_up` (Impact: 35.4 | O(N^4))
  * `initiate_device_flow` (Impact: 30.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 228`, `args: 67`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 93`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `api: 28`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 39`, `doc: 145`, `test: 6`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.586
  * `Choke Point (Betweenness):` 0.033171 | `Ripple Effect (Closeness):` 0.104167
  * `Imports (Out-Degree: 14):` requests, cryptography.hazmat.primitives.serialization, warnings, .mex, msal_extensions, os, .token_cache, .authority...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/oauth2.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.067 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.719 IQR)
- **Top Global Matches:** file_cluster_13: 12.067, file_cluster_8: 12.174, file_cluster_7: 12.334
- **Magnitude:** 1314.44 | **LOC:** 879 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (17.2799%), Tech Debt (47.5706%)
**Top Internal Functions/Classes:**
  * `_obtain_token` (Impact: 829.0 | O(2^N) | DB: 12)
  * `obtain_token_by_browser` (Impact: 210.9 | O(N^5) | DB: 12)
  * `__init__` (Impact: 148.1 | O(N^5) | DB: 15)
  * `_build_auth_request_params` (Impact: 16.6 | O(N^3) | DB: 1)
  * `encode_saml_assertion` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 96`, `args: 30`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 73`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 20`, `import: 16`
* *Defense:* `safety: 20`, `doc: 72`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 181.253
  * `Choke Point (Betweenness):` 0.002881 | `Ripple Effect (Closeness):` 0.179067
  * `Imports (Out-Degree: 1):` requests, random, string, urllib.parse, time, sys, .authcode, warnings...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_e2e.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.324 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.969 IQR)
- **Top Global Matches:** file_cluster_8: 10.324, file_cluster_13: 10.581, file_cluster_7: 10.584
- **Magnitude:** 1279.92 | **LOC:** 1496 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 84
- **Risk Profile:** Cognitive Load (2.5483%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `skipUnlessWithConfig` (Impact: 677.4 | O(2^N) | DB: 84)
  * `_get_app_and_auth_code` (Impact: 449.2 | O(N^6) | DB: 7)
  * `_get_shr_pop` (Impact: 11.7 | O(N^3))
    * *Intent:* # It is supposed to call app.is_pop_supported() first, # We skip it here because this test case has ...
  * `setUpClass` (Impact: 4.0 | O(N^3) | DB: 1)
    * *Intent:* # It now uses lab config + env vars so it can run automatically without local files. @classmethod de...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 180`, `args: 83`, `func_start: 82`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 39`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 28`, `api: 76`, `import: 26`
* *Defense:* `safety: 17`, `doc: 86`, `test: 67`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.308
  * `Choke Point (Betweenness):` 0.00133 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 2):` requests, unittest.mock, tests.http_client, unittest, base64, msal.oauth2cli, os, urllib.parse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/__main__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.371 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.472 IQR)
- **Top Global Matches:** file_cluster_8: 10.371, file_cluster_7: 10.789, file_cluster_1: 11.012
- **Magnitude:** 1095.54 | **LOC:** 348 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (10.8242%), Tech Debt (21.0561%)
**Top Internal Functions/Classes:**
  * `_acquire_token_interactive` (Impact: 978.3 | O(2^N) | DB: 18)
  * `_select_options` (Impact: 60.5 | O(N^4))
  * `_acquire_token_silent` (Impact: 22.3 | O(N^4))
  * `_select_account` (Impact: 10.9 | O(N^3))
  * `_input_scopes` (Impact: 5.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 45`, `args: 23`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 1`, `import: 2`
* *Defense:* `safety: 30`, `doc: 26`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, dotenv, base64, json, os, atexit, msal, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/token_cache.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.381 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.396 IQR)
- **Top Global Matches:** file_cluster_8: 10.381, file_cluster_13: 10.539, file_cluster_7: 10.661
- **Magnitude:** 719.38 | **LOC:** 446 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (25.5206%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 275.8 | O(N^6) | DB: 2)
  * `search` (Impact: 160.9 | O(N^5) | DB: 1)
  * `__init__` (Impact: 117.9 | O(N^6) | DB: 3)
  * `_is_matching` (Impact: 40.5 | O(N^3))
  * `deserialize` (Impact: 14.2 | O(N^3) | DB: 2)
    * *Intent:* # See also https://github.com/AzureAD/microsoft-authentication-library-for-python/issues/690 "XDG_RU...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 64`, `args: 28`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 9`, `doc: 16`, `test: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.518
  * `Choke Point (Betweenness):` 0.011451 | `Ripple Effect (Closeness):` 0.148284
  * `Imports (Out-Degree: 3):` .oauth2cli.oauth2, time, threading, .oauth2cli.oidc, warnings, json, os, atexit...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/authority.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.287 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.308 IQR)
- **Top Global Matches:** file_cluster_8: 10.287, file_cluster_13: 10.619, file_cluster_7: 10.679
- **Magnitude:** 612.96 | **LOC:** 306 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (23.2311%), Tech Debt (83.5956%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 351.8 | O(N^6) | DB: 13)
  * `has_valid_issuer` (Impact: 95.8 | O(N^5))
  * `canonicalize` (Impact: 76.0 | O(N^4))
    * *Intent:* # 3a: Base host is a trusted Microsoft host
  * `user_realm_discovery` (Impact: 32.1 | O(N^6))
    * *Intent:* % authority_url)
  * `_get_instance_discovery_host` (Impact: 5.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 41`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.140833
  * `Imports (Out-Degree: 0):` logging, urlparse, urllib.parse, json
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/authcode.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.324 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.342 IQR)
- **Top Global Matches:** file_cluster_13: 11.324, file_cluster_8: 11.64, file_cluster_7: 11.85
- **Magnitude:** 541.5 | **LOC:** 440 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (16.8306%), Tech Debt (10.8337%)
**Top Internal Functions/Classes:**
  * `_process_auth_response` (Impact: 332.9 | O(N^6) | DB: 13)
  * `_browse` (Impact: 58.3 | O(N^4) | DB: 6)
    * *Intent:* # "Official" way of detecting WSL: https://github.com/Microsoft/WSL/issues/423#issuecomment-22162736...
  * `do_GET` (Impact: 31.3 | O(N^4))
    * *Intent:* # If an https request is sent to an http server, the text needs to be repr-ed return repr(text) if i...
  * `_is_inside_docker` (Impact: 26.6 | O(N^5) | DB: 6)
  * `do_POST` (Impact: 14.4 | O(N^3))
    * *Intent:* # IdP may have error scenarios that result in a parameter-less GET request
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 85`, `args: 22`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 13`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 17`, `doc: 29`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 191.506
  * `Choke Point (Betweenness):` 0.003694 | `Ripple Effect (Closeness):` 0.197917
  * `Imports (Out-Degree: 1):` os, urlparse, string, urllib.parse, threading, html, socket, cgi...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/oidc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.035 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.842 IQR)
- **Top Global Matches:** file_cluster_8: 10.035, file_cluster_13: 10.163, file_cluster_7: 10.26
- **Magnitude:** 513.08 | **LOC:** 339 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.0136%), Tech Debt (65.9467%)
**Top Internal Functions/Classes:**
  * `obtain_token_by_authorization_code` (Impact: 238.5 | O(2^N) | DB: 1)
  * `decode_id_token` (Impact: 88.3 | O(N^4))
  * `obtain_token_by_browser` (Impact: 64.5 | O(2^N) | DB: 1)
    * *Intent:* # "If no openid scope value is present, # the request may still be a valid OAuth 2.0 request, # but ...
  * `_epoch_to_local` (Impact: 44.0 | O(2^N))
    * *Intent:* # On Python 2.7, argument of urlsafe_b64decode must be str, not unicode.
  * `_obtain_token` (Impact: 18.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 46`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 2`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.217742
  * `Imports (Out-Degree: 0):` random, string, time, base64, json, warnings, hashlib, ...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_application.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.762 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.99 IQR)
- **Top Global Matches:** file_cluster_8: 9.762, file_cluster_7: 10.122, file_cluster_0: 10.227
- **Magnitude:** 447.78 | **LOC:** 929 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (4.2543%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unknown_family_app_will_attempt_frt` (Impact: 231.6 | O(N^6) | DB: 25)
  * `test_unknown_orphan_app_will_attempt_frt` (Impact: 11.9 | O(N^3))
  * `setUp` (Impact: 5.3 | O(N^4) | DB: 9)
  * `setUp` (Impact: 5.2 | O(N^4) | DB: 8)
  * `test_acquire_token_silent_will_suppress_` (Impact: 3.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 164`, `args: 95`, `func_start: 91`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 10`
* *Architecture:* `io: 4`, `api: 108`, `import: 11`
* *Defense:* `doc: 26`, `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` tests.http_client, unittest.mock, time, sys, msal.telemetry, msal.application, tests.test_token_cache, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/tests/test_authority.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.885 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.267 IQR)
- **Top Global Matches:** file_cluster_8: 9.885, file_cluster_0: 10.084, file_cluster_7: 10.118
- **Magnitude:** 380.52 | **LOC:** 704 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (2.0928%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_canonicalize_tenant_followed_by_ext` (Impact: 160.3 | O(N^4) | DB: 4)
  * `test_unknown_host_wont_pass_instance_dis` (Impact: 16.0 | O(N^5))
  * `test_wellknown_host_and_tenant` (Impact: 13.9 | O(N^4))
    * *Intent:* # This test makes real HTTP calls to authority endpoints. # It is intentionally network-based to val...
  * `test_invalid_host_skipping_validation_ca` (Impact: 13.5 | O(N^4))
  * `test_new_sovereign_hosts_should_build_au` (Impact: 13.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 96`, `args: 64`, `func_start: 64`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`, `duplicate_logic: 10`, `orphaned_logic: 11`
* *Architecture:* `io: 2`, `api: 69`, `import: 8`
* *Defense:* `safety: 9`, `doc: 64`, `test: 117`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tests.http_client, unittest.mock, mock, os, tests, msal, msal.authority
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/managed_identity.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.893 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.878 IQR)
- **Top Global Matches:** file_cluster_8: 9.893, file_cluster_13: 10.125, file_cluster_7: 10.269
- **Magnitude:** 352.52 | **LOC:** 689 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (7.2118%), Tech Debt (91.9399%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 135.4 | O(2^N))
    * *Intent:* """ def __init__(self): super(SystemAssignedManagedIdentity, self).__init__(id_type=self.SYSTEM_ASSI...
  * `_obtain_token_on_azure_vm` (Impact: 38.8 | O(N^4) | DB: 3)
  * `get_managed_identity_source` (Impact: 35.4 | O(N^3) | DB: 21)
  * `_get_arc_endpoint` (Impact: 24.8 | O(N^3) | DB: 24)
    * *Intent:* # This class only throttles excess token acquisition requests. # It does not provide retry. # Retry ...
  * `is_user_assigned` (Impact: 14.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 85`, `args: 20`, `func_start: 19`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 39`, `api: 14`, `import: 13`
* *Defense:* `safety: 17`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.864
  * `Choke Point (Betweenness):` 0.002438 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 4):` .throttled_http_client, requests, urllib.parse, sys, time, .cloudshell, json, hashlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/throttled_http_client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.001 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.736 IQR)
- **Top Global Matches:** file_cluster_13: 12.001, file_cluster_11: 12.216, file_cluster_8: 12.385
- **Magnitude:** 314.88 | **LOC:** 180 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (30.211%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 160.0 | O(2^N) | DB: 3)
  * `parse` (Impact: 34.3 | O(N^4))
    * *Intent:* """Return seconds to throttle"""
  * `__init__` (Impact: 22.8 | O(N^3) | DB: 2)
  * `__init__` (Impact: 14.4 | O(2^N) | DB: 3)
  * `raise_for_status` (Impact: 9.0 | O(N^4))
    * *Intent:* ## Note: Don't use the following line, ## because when being pickled, it will indirectly pickle the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 39`, `args: 17`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 25`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 6`, `doc: 11`, `sync_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.994
  * `Choke Point (Betweenness):` 0.007092 | `Ripple Effect (Closeness):` 0.1125
  * `Imports (Out-Degree: 3):` .exceptions, threading, hashlib, .individual_cache, .oauth2cli.http
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/individual_cache.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.936 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.794 IQR)
- **Top Global Matches:** file_cluster_13: 11.936, file_cluster_8: 12.073, file_cluster_7: 12.22
- **Magnitude:** 286.84 | **LOC:** 291 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (30.586%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 42.9 | O(2^N) | DB: 4)
  * `__call__` (Impact: 36.3 | O(N^4))
  * `__getitem__` (Impact: 26.9 | O(N^5) | DB: 2)
  * `_maintenance` (Impact: 25.6 | O(N^4))
    * *Intent:* # Returns (sequence, timestamps) without triggering maintenance return self._mapping.get(self._INDEX...
  * `_set` (Impact: 23.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 39`, `args: 16`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 4`, `doc: 27`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.109601
  * `Imports (Out-Degree: 0):` heapq, time, threading, collections, functools, collections.abc
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_mi.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.924 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.052 IQR)
- **Top Global Matches:** file_cluster_8: 8.924, file_cluster_0: 9.279, file_cluster_13: 9.307
- **Magnitude:** 263.28 | **LOC:** 480 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (3.1199%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_happy_path` (Impact: 93.9 | O(2^N) | DB: 18)
  * `test_happy_path` (Impact: 40.5 | O(N^5) | DB: 42)
  * `test_error_out_on_invalid_input` (Impact: 13.3 | O(N^4) | DB: 6)
  * `test_helper_class_should_be_interchangab` (Impact: 11.2 | O(N^3))
  * `test_sf_error_should_be_normalized` (Impact: 9.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 82`, `args: 36`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 30`, `api: 41`, `import: 14`
* *Defense:* `safety: 6`, `doc: 6`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` requests, unittest, unittest.mock, time, sys, mock, msal.managed_identity, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/broker.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.448 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.778 IQR)
- **Top Global Matches:** file_cluster_8: 8.448, file_cluster_7: 9.043, file_cluster_13: 9.08
- **Magnitude:** 258.04 | **LOC:** 292 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (9.7186%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_read_account_by_id` (Impact: 176.7 | O(N^4) | DB: 7)
  * `_acquire_token_silently` (Impact: 43.5 | O(N^3))
  * `_signout_silently` (Impact: 12.8 | O(N^2))
  * `_convert_error` (Impact: 10.7 | O(N^3))
    * *Intent:* # On Mac, the native Python has a team_id which links to bundle id # com.apple.python3 however it wo...
  * `_enable_pii_log` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 39`, `args: 18`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 3`, `api: 5`, `import: 7`
* *Defense:* `safety: 3`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.041
  * `Choke Point (Betweenness):` 0.000443 | `Ripple Effect (Closeness):` 0.085069
  * `Imports (Out-Degree: 1):` .sku, time, sys, json, logging, uuid, pymsalruntime
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_token_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.895 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.435 IQR)
- **Top Global Matches:** file_cluster_8: 7.895, file_cluster_7: 8.574, file_cluster_13: 8.737
- **Magnitude:** 214.5 | **LOC:** 324 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (3.0247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_id_token` (Impact: 186.8 | O(2^N) | DB: 5)
    * *Intent:* # NOTE: These helpers were once implemented as static methods in TokenCacheTestCase. # That would ca...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `doc: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.073
  * `Choke Point (Betweenness):` 0.00495 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` time, ..., warnings, base64, json, tests, msal.token_cache, logging
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_throttled_http_client.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.277 IQR)
- **Top Global Matches:** file_cluster_8: 8.707, file_cluster_13: 9.076, file_cluster_7: 9.185
- **Magnitude:** 172.74 | **LOC:** 259 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (2.1109%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_build_dummy_response` (Impact: 13.4 | O(N^4))
  * `__init__` (Impact: 8.2 | O(2^N) | DB: 1)
  * `test_normalized_response_raise_for_statu` (Impact: 7.2 | O(N^3))
  * `test_throttled_http_client_should_provid` (Impact: 7.2 | O(N^3))
  * `test_400_with_RetryAfter_N_seconds_shoul` (Impact: 4.7 | O(N^4))
    * *Intent:* """Retry-After is supposed to only shown in http 429/5xx, but we choose to support Retry-After for a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 66`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4`, `duplicate_logic: 6`
* *Architecture:* `api: 45`, `import: 8`
* *Defense:* `safety: 1`, `doc: 9`, `test: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.925
  * `Choke Point (Betweenness):` 0.000887 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 2):` tests.http_client, random, time, msal.exceptions, tests, pickle, logging, msal.throttled_http_client
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.854 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.372 IQR)
- **Top Global Matches:** file_cluster_13: 9.854, file_cluster_8: 9.871, file_cluster_0: 9.915
- **Magnitude:** 152.64 | **LOC:** 301 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (4.1965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setUpClass` (Impact: 32.0 | O(N^6) | DB: 9)
  * `load_conf` (Impact: 31.8 | O(N^4) | DB: 11)
    * *Intent:* """ Example of a configuration file: { "Note": "the OpenID Discovery will be updated by following op...
  * `test_auth_code_flow_error_response` (Impact: 18.0 | O(N^4))
  * `test_device_flow` (Impact: 16.5 | O(N^4) | DB: 3)
  * `test_auth_code` (Impact: 10.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 39`, `args: 20`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `io: 9`, `api: 16`, `import: 11`
* *Defense:* `safety: 6`, `doc: 6`, `test: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` requests, tests.http_client, urllib.parse, time, json, msal.oauth2cli, os, tests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/telemetry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.664 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.469 IQR)
- **Top Global Matches:** file_cluster_8: 10.664, file_cluster_13: 10.874, file_cluster_7: 11.038
- **Magnitude:** 139.56 | **LOC:** 79 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (43.099%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 113.5 | O(N^5) | DB: 7)
  * `_get_new_correlation_id` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.658
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 0):` logging, uuid
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/mex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.598 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.598 IQR)
- **Top Global Matches:** file_cluster_8: 9.598, file_cluster_13: 9.668, file_cluster_7: 10.16
- **Magnitude:** 129.34 | **LOC:** 138 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (12.1813%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `send_request` (Impact: 116.6 | O(N^6) | DB: 18)
  * `_xpath_of_root` (Impact: 1.9 | O(N^1))
    * *Intent:* # Construct an xpath suitable to find a root node which has a specified leaf return '/'.join(route_t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 31`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `io: 5`, `api: 4`, `import: 5`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130208
  * `Imports (Out-Degree: 0):` logging, urlparse, xml.etree, urllib.parse
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/cloudshell.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.186 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.053 IQR)
- **Top Global Matches:** file_cluster_13: 9.186, file_cluster_8: 9.21, file_cluster_7: 9.774
- **Magnitude:** 118.86 | **LOC:** 127 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (8.6786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_obtain_token` (Impact: 84.6 | O(N^5))
  * `_scope_to_resource` (Impact: 28.5 | O(N^3))
  * `_is_running_in_cloud_shell` (Impact: 1.8 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 22`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 8`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.35
  * `Choke Point (Betweenness):` 0.000665 | `Ripple Effect (Closeness):` 0.1125
  * `Imports (Out-Degree: 1):` urllib.parse, time, .oauth2cli.oidc, base64, json, os, logging, urlparse
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_optional_thumbprint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.388 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.365 IQR)
- **Top Global Matches:** file_cluster_8: 8.388, file_cluster_7: 8.747, file_cluster_1: 8.974
- **Magnitude:** 114.7 | **LOC:** 216 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.6916%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_verify_assertion_params` (Impact: 47.7 | O(N^6))
  * `_setup_mocks` (Impact: 13.2 | O(N^3))
  * `test_pem_with_neither_raises_error` (Impact: 12.9 | O(N^5))
    * *Intent:* # Should raise ValueError when neither thumbprint nor certificate provided with self.assertRaises(Va...
  * `test_pem_with_certificate_only_uses_sha2` (Impact: 7.4 | O(N^4))
  * `test_pem_with_adfs_uses_sha1` (Impact: 7.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `doc: 22`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, msal.application, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/wstrust_request.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.645 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.64 IQR)
- **Top Global Matches:** file_cluster_8: 7.645, file_cluster_13: 8.054, file_cluster_7: 8.307
- **Magnitude:** 108.16 | **LOC:** 130 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (8.5093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wsu_time_format` (Impact: 62.0 | O(2^N) | DB: 6)
    * *Intent:* # WsTrust (http://docs.oasis-open.org/ws-sx/ws-trust/v1.4/ws-trust.html) # does not seem to define t...
  * `send_request` (Impact: 41.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`, `args: 4`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 4`, `import: 5`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.467
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.068182
  * `Imports (Out-Degree: 2):` .wstrust_response, .mex, datetime, logging, uuid
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_client_obtain_token_by_browser.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.163 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.906 IQR)
- **Top Global Matches:** file_cluster_13: 11.163, file_cluster_8: 11.471, file_cluster_1: 11.687
- **Magnitude:** 93.48 | **LOC:** 118 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.4145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_initiate_auth_code_flow_with_non_fo` (Impact: 21.8 | O(N^5))
  * `get_auth_response` (Impact: 18.1 | O(2^N) | DB: 3)
    * *Intent:* """ def __init__(self, *args, scheduled_action=None, **kwargs): super(_BrowserlessAuthCodeReceiver, ...
  * `test_http_post_should_work_with_obtain_t` (Impact: 16.7 | O(N^5) | DB: 3)
  * `__init__` (Impact: 6.9 | O(2^N) | DB: 1)
  * `setUp` (Impact: 6.3 | O(N^5) | DB: 3)
    * *Intent:* """Integration test for response_mode with end-to-end authentication flow"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 31`, `args: 8`, `func_start: 8`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 13`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` requests, urllib.parse, json, msal.oauth2cli, msal.oauth2cli.authcode, unittest, urlparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/tests/test_cryptography.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.168 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.111 IQR)
- **Top Global Matches:** file_cluster_13: 8.168, file_cluster_8: 8.195, file_cluster_7: 9.049
- **Magnitude:** 76.36 | **LOC:** 64 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (6.8921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_current_ceiling` (Impact: 30.8 | O(N^4))
  * `test_latest_cryptography_should_support_` (Impact: 22.2 | O(N^4) | DB: 3)
  * `test_should_be_run_with_latest_version_o` (Impact: 7.3 | O(N^3))
  * `test_ceiling_should_be_latest_cryptograp` (Impact: 7.3 | O(N^3))
  * `sibling` (Impact: 1.8 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 5`, `api: 6`, `import: 9`
* *Defense:* `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` requests, configparser, msal.application, warnings, os, xml.etree.ElementTree, cryptography, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `msal-1.35.1/tests/test_client.py` (PYTHON) | Magnitude: 152.64 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 39, test: 26, args: 20
- `msal-1.35.1/msal/cloudshell.py` (PYTHON) | Magnitude: 118.86 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 22, branch: 19, import: 8
- `msal-1.35.1/tests/test_cryptography.py` (PYTHON) | Magnitude: 76.36 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 23, branch: 12, import: 9
- `msal-1.35.1/msal/wstrust_response.py` (PYTHON) | Magnitude: 31.32 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 18, branch: 7, api: 5
- `msal-1.35.1/tests/test_assertion.py` (PYTHON) | Magnitude: 5.9 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 5, test: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `msal-1.35.1/tests/test_authcode.py` (PYTHON) | Magnitude: 65.2 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 16, doc: 10, io: 9
- `msal-1.35.1/msal/oauth2cli/http.py` (PYTHON) | Magnitude: 22.76 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 17, structural_boundaries: 10, indent_spaces: 10, api: 8
- `msal-1.35.1/msal/mex.py` (PYTHON) | Magnitude: 129.34 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 31, branch: 17, encapsulation: 15
- `msal-1.35.1/setup.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1, sec_reflection_metaprogramming: 1
- `msal-1.35.1/msal/oauth2cli/oidc.py` (PYTHON) | Magnitude: 513.08 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 46, branch: 38, doc: 35

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `msal-1.35.1/msal/application.py` -> **Severity: 1.941** (Bridge: 0.0332 * Flux: 58.5078%)
- `msal-1.35.1/msal/token_cache.py` -> **Severity: 0.729** (Bridge: 0.0115 * Flux: 63.6338%)
- `msal-1.35.1/msal/throttled_http_client.py` -> **Severity: 0.709** (Bridge: 0.0071 * Flux: 99.9348%)
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **Severity: 0.285** (Bridge: 0.0029 * Flux: 98.7895%)
- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **Severity: 0.271** (Bridge: 0.0037 * Flux: 73.3825%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `msal-1.35.1/msal/throttled_http_client.py` -> **Severity: 6.079** (Embedded: 0.1125 * Error Risk: 54.0385%)
- `msal-1.35.1/msal/oauth2cli/http.py` -> **Severity: 5.705** (Embedded: 0.0833 * Error Risk: 68.4615%)
- `msal-1.35.1/msal/region.py` -> **Severity: 3.111** (Embedded: 0.0682 * Error Risk: 45.625%)
- `msal-1.35.1/msal/exceptions.py` -> **Severity: 1.538** (Embedded: 0.1225 * Error Risk: 12.5519%)
- `msal-1.35.1/msal/telemetry.py` -> **Severity: 1.529** (Embedded: 0.075 * Error Risk: 20.3927%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **Severity: 14594.711** (Blast Radius: 191.506 * Doc Risk: 76.2102%)
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **Severity: 6716.747** (Blast Radius: 181.253 * Doc Risk: 37.0573%)
- `msal-1.35.1/msal/oauth2cli/oidc.py` -> **Severity: 4993.698** (Blast Radius: 50.63 * Doc Risk: 98.6312%)
- `msal-1.35.1/msal/mex.py` -> **Severity: 3583.914** (Blast Radius: 37.12 * Doc Risk: 96.5494%)
- `msal-1.35.1/msal/token_cache.py` -> **Severity: 3446.042** (Blast Radius: 34.518 * Doc Risk: 99.8332%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
