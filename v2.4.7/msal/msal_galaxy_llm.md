# ARCHITECTURAL_BRIEF: msal
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/msal` |
| **Timestamp** | `2026-08-07T05:24:04.739458+00:00` |
| **Scan Duration** | `0.4s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 48 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 77.2 | 36.3 | 46.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.5 | 0.3 | 0.0 |
| API Exposure | 0.0 | 9.5 | 3.8 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 35.9 | 1.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.2 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 93.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 72.8 | 13.6 | 2.2 | 0.0 |
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

- `_build_client` (@ `msal-1.35.1/msal/application.py`) -> Impact: **533.5** | LOC: 1099
- `skipUnlessWithConfig` (@ `msal-1.35.1/tests/test_e2e.py`) -> Impact: **157.8** | LOC: 1077
- `_acquire_token_interactive` (@ `msal-1.35.1/msal/__main__.py`) -> Impact: **150.3** | LOC: 246
- `_obtain_token` (@ `msal-1.35.1/msal/oauth2cli/oauth2.py`) -> Impact: **150.2** | LOC: 288
- `_get_app_and_auth_code` (@ `msal-1.35.1/tests/test_e2e.py`) -> Impact: **138.3** | LOC: 279
- `__init__` (@ `msal-1.35.1/msal/authority.py`) -> Impact: **104.3** | LOC: 106
- `_process_auth_response` (@ `msal-1.35.1/msal/oauth2cli/authcode.py`) -> Impact: **103.4** | LOC: 232
- `test_unknown_family_app_will_attempt_frt` (@ `msal-1.35.1/tests/test_application.py`) -> Impact: **93.1** | LOC: 753
- `add` (@ `msal-1.35.1/msal/token_cache.py`) -> Impact: **85.8** | LOC: 195
- `test_canonicalize_tenant_followed_by_ext` (@ `msal-1.35.1/tests/test_authority.py`) -> Impact: **77.1** | LOC: 434

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `msal-1.35.1/msal` | 18 | 2501.38 | 15.78% | 24.9% |
| `msal-1.35.1/tests` | 23 | 1884.82 | 3.63% | 0.0% |
| `msal-1.35.1/msal/oauth2cli` | 6 | 847.4 | 15.04% | 37.17% |
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
- `msal-1.35.1/tests/test_application.py` -> **10** Orphaned Functions | **10** Duplicates
- `msal-1.35.1/tests/test_e2e_manual.py` -> **13** Orphaned Functions | **2** Duplicates
- `msal-1.35.1/tests/test_mi.py` -> **11** Orphaned Functions | **4** Duplicates
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

### Hardcoded Payload Artifacts
- `msal-1.35.1/tests/test_optional_thumbprint.py` -> **99.9295%** Exposure
- `msal-1.35.1/msal/application.py` -> **75.9921%** Exposure
- `msal-1.35.1/tests/test_application.py` -> **67.0021%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `294` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `msal-1.35.1/msal/throttled_http_client.py` (PYTHON) -> Cumulative Risk: **577.53**
- **Archetype:** `file_cluster_13` (Distance: 12.001 IQR)
- **Magnitude:** 118.88 | **LOC:** 180 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9348%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 25.9), `parse` (Impact: 14.2), `__init__` (Impact: 11.6)

### 2. `msal-1.35.1/msal/token_cache.py` (PYTHON) -> Cumulative Risk: **539.77**
- **Archetype:** `file_cluster_8` (Distance: 10.378 IQR)
- **Magnitude:** 295.48 | **LOC:** 446 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Documentation (72.7757%), State Flux (63.6338%)
- **Heaviest Functions:** `add` (Impact: 85.8), `search` (Impact: 55.1), `__init__` (Impact: 35.7)

### 3. `msal-1.35.1/msal/authority.py` (PYTHON) -> Cumulative Risk: **528.0**
- **Archetype:** `file_cluster_8` (Distance: 10.287 IQR)
- **Magnitude:** 233.86 | **LOC:** 306 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.4985%), Tech Debt (83.5956%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 104.3), `has_valid_issuer` (Impact: 33.5), `canonicalize` (Impact: 31.8)

### 4. `msal-1.35.1/msal/individual_cache.py` (PYTHON) -> Cumulative Risk: **525.5**
- **Archetype:** `file_cluster_13` (Distance: 11.934 IQR)
- **Magnitude:** 167.94 | **LOC:** 291 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9672%), Tech Debt (84.1131%), Verification (80.0%)
- **Heaviest Functions:** `__call__` (Impact: 15.5), `wrapper` (Impact: 15.3), `__init__` (Impact: 14.6)

### 5. `msal-1.35.1/msal/oauth2cli/assertion.py` (PYTHON) -> Cumulative Risk: **504.37**
- **Archetype:** `file_cluster_13` (Distance: 11.618 IQR)
- **Magnitude:** 48.72 | **LOC:** 138 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8653%), Tech Debt (98.6482%), Safety Score (70.6042%)
- **Heaviest Functions:** `__call__` (Impact: 5.6), `_str2bytes` (Impact: 3.8), `create_normal_assertion` (Impact: 3.5)

### 6. `msal-1.35.1/msal/oauth2cli/oauth2.py` (PYTHON) -> Cumulative Risk: **461.37**
- **Archetype:** `file_cluster_13` (Distance: 12.067 IQR)
- **Magnitude:** 393.84 | **LOC:** 879 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.7895%), Verification (80.0%), Safety Score (54.1295%)
- **Heaviest Functions:** `_obtain_token` (Impact: 150.2), `obtain_token_by_browser` (Impact: 76.8), `__init__` (Impact: 50.8)

### 7. `msal-1.35.1/msal/application.py` (PYTHON) -> Cumulative Risk: **452.63**
- **Archetype:** `file_cluster_8` (Distance: 11.458 IQR)
- **Magnitude:** 865.6 | **LOC:** 2556 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Secrets Risk (75.9921%), State Flux (58.5078%)
- **Heaviest Functions:** `_build_client` (Impact: 533.5), `_preferred_browser` (Impact: 31.4), `_get_regional_authority` (Impact: 25.9)

### 8. `msal-1.35.1/msal/telemetry.py` (PYTHON) -> Cumulative Risk: **426.86**
- **Archetype:** `file_cluster_8` (Distance: 10.664 IQR)
- **Magnitude:** 65.46 | **LOC:** 79 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9944%), Safety Score (77.2487%), Documentation (53.4253%)
- **Heaviest Functions:** `__init__` (Impact: 39.4), `_get_new_correlation_id` (Impact: 1.8)

### 9. `msal-1.35.1/msal/oauth2cli/authcode.py` (PYTHON) -> Cumulative Risk: **420.52**
- **Archetype:** `file_cluster_13` (Distance: 11.324 IQR)
- **Magnitude:** 227.9 | **LOC:** 440 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (73.3825%), Stability (50.0%)
- **Heaviest Functions:** `_process_auth_response` (Impact: 103.4), `_browse` (Impact: 24.5), `do_GET` (Impact: 13.1)

### 10. `msal-1.35.1/msal/managed_identity.py` (PYTHON) -> Cumulative Risk: **413.36**
- **Archetype:** `file_cluster_8` (Distance: 9.893 IQR)
- **Magnitude:** 151.12 | **LOC:** 689 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (91.9399%), Verification (80.0%), Stability (50.0%)
- **Heaviest Functions:** `__init__` (Impact: 27.6), `get_managed_identity_source` (Impact: 18.1), `_obtain_token_on_azure_vm` (Impact: 17.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `msal-1.35.1/msal/application.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.458 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.541 IQR)
- **Top Global Matches:** file_cluster_8: 11.458, file_cluster_13: 11.629, file_cluster_7: 11.684
- **Magnitude:** 865.6 | **LOC:** 2556 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0447%), Tech Debt (10.5121%)
**Top Internal Functions/Classes:**
  * `_build_client` (Impact: 533.5)
  * `_preferred_browser` (Impact: 31.4)
    * *Intent:* """Register Edge and return a name suitable for subsequent webbrowser.get(...) when appropriate. Oth...
  * `_get_regional_authority` (Impact: 25.9)
  * `_clean_up` (Impact: 14.7)
  * `obtain_token_by_auth_code_flow` (Impact: 14.1)
    * *Intent:* **kwargs)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 228`, `args: 67`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 93`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `api: 28`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 39`, `doc: 145`, `test: 6`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.586
  * `Choke Point (Betweenness):` 0.033171 | `Ripple Effect (Closeness):` 0.104167
  * `Imports (Out-Degree: 14):` .token_cache, , atexit, .oauth2cli, cryptography.hazmat.backends, threading, functools, .oauth2cli.oidc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_e2e.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.369 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.97 IQR)
- **Top Global Matches:** file_cluster_8: 10.369, file_cluster_13: 10.623, file_cluster_7: 10.627
- **Magnitude:** 508.12 | **LOC:** 1496 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5483%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `skipUnlessWithConfig` (Impact: 157.8)
  * `_get_app_and_auth_code` (Impact: 138.3)
  * `assertCacheWorksForUser` (Impact: 24.2)
  * `_test_username_password` (Impact: 23.0)
  * `_build_app` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 180`, `args: 85`, `func_start: 82`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 39`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 28`, `api: 76`, `import: 26`
* *Defense:* `safety: 17`, `doc: 86`, `test: 67`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.308
  * `Choke Point (Betweenness):` 0.00133 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 2):` unittest.mock, tests.http_client, msal.oauth2cli, dotenv, requests, msal.oauth2cli.oidc, sys, re...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/oauth2.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.067 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.719 IQR)
- **Top Global Matches:** file_cluster_13: 12.067, file_cluster_8: 12.174, file_cluster_7: 12.334
- **Magnitude:** 393.84 | **LOC:** 879 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.2799%), Tech Debt (47.5706%)
**Top Internal Functions/Classes:**
  * `_obtain_token` (Impact: 150.2)
  * `obtain_token_by_browser` (Impact: 76.8)
  * `__init__` (Impact: 50.8)
  * `_build_auth_request_params` (Impact: 8.7)
  * `session` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 96`, `args: 30`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 73`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 20`, `import: 16`
* *Defense:* `safety: 20`, `doc: 72`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 181.253
  * `Choke Point (Betweenness):` 0.002881 | `Ripple Effect (Closeness):` 0.179067
  * `Imports (Out-Degree: 1):` urlparse, base64, json, functools, hashlib, logging, .authcode, requests...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_application.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.764 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.976 IQR)
- **Top Global Matches:** file_cluster_8: 9.764, file_cluster_7: 10.123, file_cluster_0: 10.222
- **Magnitude:** 297.28 | **LOC:** 929 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2855%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unknown_family_app_will_attempt_frt` (Impact: 93.1)
  * `test_unknown_orphan_app_will_attempt_frt` (Impact: 6.7)
  * `setUp` (Impact: 2.7)
  * `setUp` (Impact: 2.6)
  * `tester` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 164`, `args: 95`, `func_start: 91`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 10`
* *Architecture:* `io: 4`, `api: 108`, `import: 11`
* *Defense:* `doc: 26`, `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` tests.test_token_cache, msal.telemetry, json, logging, unittest.mock, msal.application, tests.http_client, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/token_cache.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.378 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.396 IQR)
- **Top Global Matches:** file_cluster_8: 10.378, file_cluster_13: 10.537, file_cluster_7: 10.659
- **Magnitude:** 295.48 | **LOC:** 446 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.47%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 85.8)
  * `search` (Impact: 55.1)
  * `__init__` (Impact: 35.7)
  * `_is_matching` (Impact: 20.5)
  * `deserialize` (Impact: 7.3)
    * *Intent:* # See also https://github.com/AzureAD/microsoft-authentication-library-for-python/issues/690 "XDG_RU...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 64`, `args: 28`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 9`, `doc: 16`, `test: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.518
  * `Choke Point (Betweenness):` 0.011451 | `Ripple Effect (Closeness):` 0.148284
  * `Imports (Out-Degree: 3):` .oauth2cli.oidc, atexit, json, logging, .authority, .oauth2cli.oauth2, time, warnings...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/authority.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.287 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.308 IQR)
- **Top Global Matches:** file_cluster_8: 10.287, file_cluster_13: 10.619, file_cluster_7: 10.679
- **Magnitude:** 233.86 | **LOC:** 306 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.2311%), Tech Debt (83.5956%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 104.3)
  * `has_valid_issuer` (Impact: 33.5)
  * `canonicalize` (Impact: 31.8)
    * *Intent:* # 3a: Base host is a trusted Microsoft host
  * `user_realm_discovery` (Impact: 9.7)
    * *Intent:* % authority_url)
  * `_get_instance_discovery_host` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 41`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.140833
  * `Imports (Out-Degree: 0):` urllib.parse, logging, urlparse, json
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/authcode.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.324 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.342 IQR)
- **Top Global Matches:** file_cluster_13: 11.324, file_cluster_8: 11.64, file_cluster_7: 11.85
- **Magnitude:** 227.9 | **LOC:** 440 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.8306%), Tech Debt (10.8337%)
**Top Internal Functions/Classes:**
  * `_process_auth_response` (Impact: 103.4)
  * `_browse` (Impact: 24.5)
    * *Intent:* # "Official" way of detecting WSL: https://github.com/Microsoft/WSL/issues/423#issuecomment-22162736...
  * `do_GET` (Impact: 13.1)
    * *Intent:* # If an https request is sent to an http server, the text needs to be repr-ed return repr(text) if i...
  * `_is_inside_docker` (Impact: 9.3)
  * `_qs2kv` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 85`, `args: 22`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 13`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 17`, `doc: 29`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 191.506
  * `Choke Point (Betweenness):` 0.003694 | `Ripple Effect (Closeness):` 0.197917
  * `Imports (Out-Degree: 1):` argparse, threading, cgi, collections, html, http.server, .oauth2, sys...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_authority.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.885 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.267 IQR)
- **Top Global Matches:** file_cluster_8: 9.885, file_cluster_0: 10.084, file_cluster_7: 10.118
- **Magnitude:** 226.42 | **LOC:** 704 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.0928%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_canonicalize_tenant_followed_by_ext` (Impact: 77.1)
  * `test_wellknown_host_and_tenant` (Impact: 6.1)
    * *Intent:* # This test makes real HTTP calls to authority endpoints. # It is intentionally network-based to val...
  * `test_invalid_host_skipping_validation_ca` (Impact: 5.7)
  * `test_unknown_host_wont_pass_instance_dis` (Impact: 5.6)
  * `test_new_sovereign_hosts_should_build_au` (Impact: 5.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 96`, `args: 64`, `func_start: 64`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`, `duplicate_logic: 10`, `orphaned_logic: 11`
* *Architecture:* `io: 2`, `api: 69`, `import: 8`
* *Defense:* `safety: 9`, `doc: 64`, `test: 117`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest.mock, mock, tests.http_client, msal.authority, tests, msal, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/__main__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.378 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.473 IQR)
- **Top Global Matches:** file_cluster_8: 10.378, file_cluster_7: 10.796, file_cluster_1: 11.02
- **Magnitude:** 210.24 | **LOC:** 348 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.8242%), Tech Debt (21.0561%)
**Top Internal Functions/Classes:**
  * `_acquire_token_interactive` (Impact: 150.3)
  * `_select_options` (Impact: 24.8)
  * `_acquire_token_silent` (Impact: 9.3)
  * `_select_account` (Impact: 5.7)
  * `_input_scopes` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 45`, `args: 24`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 1`, `import: 2`
* *Defense:* `safety: 30`, `doc: 26`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dotenv, base64, json, atexit, logging, getpass, msal, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/individual_cache.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.934 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.794 IQR)
- **Top Global Matches:** file_cluster_13: 11.934, file_cluster_8: 12.071, file_cluster_7: 12.218
- **Magnitude:** 167.94 | **LOC:** 291 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.586%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 15.5)
  * `wrapper` (Impact: 15.3)
  * `__init__` (Impact: 14.6)
  * `_set` (Impact: 12.1)
  * `_maintenance` (Impact: 10.7)
    * *Intent:* # Returns (sequence, timestamps) without triggering maintenance return self._mapping.get(self._INDEX...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 39`, `args: 16`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 4`, `doc: 27`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.109601
  * `Imports (Out-Degree: 0):` collections, collections.abc, time, heapq, threading, functools
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/managed_identity.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.893 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.878 IQR)
- **Top Global Matches:** file_cluster_8: 9.893, file_cluster_13: 10.125, file_cluster_7: 10.269
- **Magnitude:** 151.12 | **LOC:** 689 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2118%), Tech Debt (91.9399%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 27.6)
    * *Intent:* """ def __init__(self): super(SystemAssignedManagedIdentity, self).__init__(id_type=self.SYSTEM_ASSI...
  * `get_managed_identity_source` (Impact: 18.1)
  * `_obtain_token_on_azure_vm` (Impact: 17.8)
  * `_get_arc_endpoint` (Impact: 12.7)
    * *Intent:* # This class only throttles excess token acquisition requests. # It does not provide retry. # Retry ...
  * `is_user_assigned` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 85`, `args: 20`, `func_start: 19`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 39`, `api: 14`, `import: 13`
* *Defense:* `safety: 17`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.864
  * `Choke Point (Betweenness):` 0.002438 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 4):` .token_cache, hashlib, json, collections, logging, requests, .individual_cache, requests.adapters...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/oidc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.035 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.842 IQR)
- **Top Global Matches:** file_cluster_8: 10.035, file_cluster_13: 10.163, file_cluster_7: 10.26
- **Magnitude:** 145.18 | **LOC:** 339 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0136%), Tech Debt (65.9467%)
**Top Internal Functions/Classes:**
  * `obtain_token_by_authorization_code` (Impact: 37.2)
  * `decode_id_token` (Impact: 36.8)
  * `obtain_token_by_browser` (Impact: 17.1)
    * *Intent:* # "If no openid scope value is present, # the request may still be a valid OAuth 2.0 request, # but ...
  * `_epoch_to_local` (Impact: 9.4)
    * *Intent:* # On Python 2.7, argument of urlsafe_b64decode must be str, not unicode.
  * `_obtain_token` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 46`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 2`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.217742
  * `Imports (Out-Degree: 0):` , base64, json, hashlib, logging, time, random, warnings...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_mi.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.924 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.052 IQR)
- **Top Global Matches:** file_cluster_8: 8.924, file_cluster_0: 9.279, file_cluster_13: 9.307
- **Magnitude:** 131.38 | **LOC:** 480 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.1199%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_happy_path` (Impact: 24.6)
  * `test_happy_path` (Impact: 16.2)
  * `test_helper_class_should_be_interchangab` (Impact: 6.0)
  * `test_error_out_on_invalid_input` (Impact: 5.5)
  * `test_sf_error_should_be_normalized` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 82`, `args: 36`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 30`, `api: 41`, `import: 14`
* *Defense:* `safety: 6`, `doc: 6`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hashlib, json, msal.token_cache, unittest.mock, requests, mock, msal.managed_identity, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/broker.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.448 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.778 IQR)
- **Top Global Matches:** file_cluster_8: 8.448, file_cluster_7: 9.043, file_cluster_13: 9.08
- **Magnitude:** 126.54 | **LOC:** 292 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.7186%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_read_account_by_id` (Impact: 75.3)
  * `_acquire_token_silently` (Impact: 22.6)
  * `_signout_silently` (Impact: 8.8)
  * `_convert_error` (Impact: 5.5)
    * *Intent:* # On Mac, the native Python has a team_id which links to bundle id # com.apple.python3 however it wo...
  * `_enable_pii_log` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 39`, `args: 18`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 3`, `api: 5`, `import: 7`
* *Defense:* `safety: 3`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.041
  * `Choke Point (Betweenness):` 0.000443 | `Ripple Effect (Closeness):` 0.085069
  * `Imports (Out-Degree: 1):` json, logging, uuid, pymsalruntime, .sku, time, sys
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/throttled_http_client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.001 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.736 IQR)
- **Top Global Matches:** file_cluster_13: 12.001, file_cluster_11: 12.216, file_cluster_8: 12.385
- **Magnitude:** 118.88 | **LOC:** 180 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.211%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 25.9)
  * `parse` (Impact: 14.2)
    * *Intent:* """Return seconds to throttle"""
  * `__init__` (Impact: 11.6)
  * `_extract_data` (Impact: 6.2)
  * `__init__` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 39`, `args: 17`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 25`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 6`, `doc: 11`, `sync_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.994
  * `Choke Point (Betweenness):` 0.007092 | `Ripple Effect (Closeness):` 0.1125
  * `Imports (Out-Degree: 3):` .oauth2cli.http, hashlib, .individual_cache, .exceptions, threading
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_throttled_http_client.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.277 IQR)
- **Top Global Matches:** file_cluster_8: 8.707, file_cluster_13: 9.076, file_cluster_7: 9.185
- **Magnitude:** 117.54 | **LOC:** 259 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.1109%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_build_dummy_response` (Impact: 5.6)
  * `test_normalized_response_raise_for_statu` (Impact: 3.7)
  * `test_throttled_http_client_should_provid` (Impact: 3.7)
  * `test_one_invalid_grant_should_block_a_si` (Impact: 2.8)
  * `post` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 66`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4`, `duplicate_logic: 6`
* *Architecture:* `api: 45`, `import: 8`
* *Defense:* `safety: 1`, `doc: 9`, `test: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.925
  * `Choke Point (Betweenness):` 0.000887 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 2):` msal.exceptions, logging, tests.http_client, msal.throttled_http_client, time, random, pickle, tests
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.893 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.38 IQR)
- **Top Global Matches:** file_cluster_13: 9.893, file_cluster_8: 9.91, file_cluster_0: 9.954
- **Magnitude:** 85.04 | **LOC:** 301 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_conf` (Impact: 13.6)
    * *Intent:* """ Example of a configuration file: { "Note": "the OpenID Discovery will be updated by following op...
  * `setUpClass` (Impact: 10.3)
  * `test_device_flow` (Impact: 8.7)
  * `test_auth_code_flow_error_response` (Impact: 7.6)
  * `test_auth_code` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 39`, `args: 24`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `io: 9`, `api: 16`, `import: 11`
* *Defense:* `safety: 6`, `doc: 6`, `test: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` urlparse, json, logging, requests, tests.http_client, os, msal.oauth2cli, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/mex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.61 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.597 IQR)
- **Top Global Matches:** file_cluster_8: 9.61, file_cluster_13: 9.668, file_cluster_7: 10.164
- **Magnitude:** 83.64 | **LOC:** 138 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.1813%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `send_request` (Impact: 36.6)
  * `_get_endpoints` (Impact: 12.6)
  * `get_wstrust_username_password_endpoint` (Impact: 9.1)
    * *Intent:* """Returns {"address": "https://...", "action": "the soapAction value"}"""
  * `_get_bindings` (Impact: 7.5)
  * `_get_username_password_policy_ids` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 31`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `io: 5`, `api: 5`, `import: 5`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130208
  * `Imports (Out-Degree: 0):` logging, xml.etree, urlparse, urllib.parse
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_token_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.895 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.435 IQR)
- **Top Global Matches:** file_cluster_8: 7.895, file_cluster_7: 8.574, file_cluster_13: 8.737
- **Magnitude:** 76.9 | **LOC:** 324 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_id_token` (Impact: 49.2)
    * *Intent:* # NOTE: These helpers were once implemented as static methods in TokenCacheTestCase. # That would ca...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `doc: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.073
  * `Choke Point (Betweenness):` 0.00495 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` ..., base64, json, logging, time, warnings, tests, msal.token_cache
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/telemetry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.664 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.469 IQR)
- **Top Global Matches:** file_cluster_8: 10.664, file_cluster_13: 10.874, file_cluster_7: 11.038
- **Magnitude:** 65.46 | **LOC:** 79 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.099%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 39.4)
  * `_get_new_correlation_id` (Impact: 1.8)
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

### `msal-1.35.1/tests/test_individual_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.897 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.97 IQR)
- **Top Global Matches:** file_cluster_8: 8.897, file_cluster_13: 9.292, file_cluster_7: 9.655
- **Magnitude:** 54.88 | **LOC:** 111 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.6067%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_get_should_not_purge_and_should_ret` (Impact: 5.6)
  * `test_should_disallow_accessing_reserved_` (Impact: 3.6)
  * `foo` (Impact: 2.5)
  * `test_old_item_can_be_updated_with_new_ex` (Impact: 2.3)
  * `test_setitem` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 30`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `orphaned_logic: 12`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, time, random, msal.individual_cache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/tests/test_client_obtain_token_by_browser.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.168 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.877 IQR)
- **Top Global Matches:** file_cluster_13: 11.168, file_cluster_8: 11.492, file_cluster_1: 11.708
- **Magnitude:** 53.98 | **LOC:** 118 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.4145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_initiate_auth_code_flow_with_non_fo` (Impact: 7.9)
  * `test_http_post_should_work_with_obtain_t` (Impact: 6.3)
  * `get_auth_response` (Impact: 4.2)
    * *Intent:* """ def __init__(self, *args, scheduled_action=None, **kwargs): super(_BrowserlessAuthCodeReceiver, ...
  * `setUp` (Impact: 2.9)
    * *Intent:* """Integration test for response_mode with end-to-end authentication flow"""
  * `__init__` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 31`, `args: 9`, `func_start: 8`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 13`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` urlparse, json, requests, msal.oauth2cli, msal.oauth2cli.authcode, unittest, urllib.parse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/tests/test_optional_thumbprint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.411 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.367 IQR)
- **Top Global Matches:** file_cluster_8: 8.411, file_cluster_7: 8.769, file_cluster_1: 8.996
- **Magnitude:** 52.3 | **LOC:** 216 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.6916%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_verify_assertion_params` (Impact: 14.6)
  * `_setup_mocks` (Impact: 7.2)
  * `test_pem_with_neither_raises_error` (Impact: 5.0)
    * *Intent:* # Should raise ValueError when neither thumbprint nor certificate provided with self.assertRaises(Va...
  * `test_pem_with_certificate_only_uses_sha2` (Impact: 3.7)
  * `test_pem_with_adfs_uses_sha1` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `args: 9`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `doc: 22`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest.mock, unittest, msal.application
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/cloudshell.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.186 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.053 IQR)
- **Top Global Matches:** file_cluster_13: 9.186, file_cluster_8: 9.21, file_cluster_7: 9.774
- **Magnitude:** 51.36 | **LOC:** 127 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.6786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_obtain_token` (Impact: 30.9)
  * `_scope_to_resource` (Impact: 14.7)
  * `_is_running_in_cloud_shell` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 22`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 8`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.35
  * `Choke Point (Betweenness):` 0.000665 | `Ripple Effect (Closeness):` 0.1125
  * `Imports (Out-Degree: 1):` .oauth2cli.oidc, urlparse, base64, json, logging, urllib.parse, time, os
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_e2e_manual.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.33 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.182 IQR)
- **Top Global Matches:** file_cluster_8: 9.33, file_cluster_0: 9.601, file_cluster_13: 9.769
- **Magnitude:** 50.18 | **LOC:** 85 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_auth_code` (Impact: 1.8)
  * `test_auth_code_with_matching_nonce` (Impact: 1.8)
  * `test_auth_code_with_mismatching_nonce` (Impact: 1.8)
  * `test_device_flow` (Impact: 1.8)
  * `test_cloud_acquire_token_interactive` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `args: 15`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `duplicate_logic: 2`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 22`, `import: 3`
* *Defense:* `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tests.test_e2e, unittest, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `msal-1.35.1/tests/test_client.py` (PYTHON) | Magnitude: 85.04 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 39, test: 26, args: 24
- `msal-1.35.1/msal/cloudshell.py` (PYTHON) | Magnitude: 51.36 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 22, branch: 19, import: 8
- `msal-1.35.1/tests/test_cryptography.py` (PYTHON) | Magnitude: 38.26 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 23, branch: 12, import: 9
- `msal-1.35.1/msal/wstrust_response.py` (PYTHON) | Magnitude: 20.82 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 18, branch: 7, api: 5
- `msal-1.35.1/tests/test_assertion.py` (PYTHON) | Magnitude: 4.2 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 5, test: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `msal-1.35.1/tests/test_authcode.py` (PYTHON) | Magnitude: 28.9 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 16, doc: 10, io: 9
- `msal-1.35.1/msal/oauth2cli/http.py` (PYTHON) | Magnitude: 19.16 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 17, structural_boundaries: 10, indent_spaces: 10, api: 8
- `msal-1.35.1/msal/mex.py` (PYTHON) | Magnitude: 83.64 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 31, branch: 17, encapsulation: 15
- `msal-1.35.1/setup.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1, sec_reflection_metaprogramming: 1
- `msal-1.35.1/msal/oauth2cli/oidc.py` (PYTHON) | Magnitude: 145.18 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
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

- `msal-1.35.1/msal/oauth2cli/oidc.py` -> **Severity: 11.71** (Embedded: 0.2177 * Error Risk: 53.7814%)
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **Severity: 9.693** (Embedded: 0.1791 * Error Risk: 54.1295%)
- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **Severity: 9.634** (Embedded: 0.1979 * Error Risk: 48.6749%)
- `msal-1.35.1/msal/authority.py` -> **Severity: 8.447** (Embedded: 0.1408 * Error Risk: 59.9798%)
- `msal-1.35.1/msal/exceptions.py` -> **Severity: 8.44** (Embedded: 0.1225 * Error Risk: 68.8715%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **Severity: 3337.241** (Blast Radius: 191.506 * Doc Risk: 17.4263%)
- `msal-1.35.1/msal/token_cache.py` -> **Severity: 2512.072** (Blast Radius: 34.518 * Doc Risk: 72.7757%)
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **Severity: 2160.59** (Blast Radius: 181.253 * Doc Risk: 11.9203%)
- `msal-1.35.1/msal/mex.py` -> **Severity: 1223.323** (Blast Radius: 37.12 * Doc Risk: 32.9559%)
- `msal-1.35.1/msal/authority.py` -> **Severity: 925.796** (Blast Radius: 27.555 * Doc Risk: 33.5981%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
