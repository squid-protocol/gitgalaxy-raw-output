# ARCHITECTURAL_BRIEF: rsa
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/rsa` |
| **Timestamp** | `2026-08-03T21:24:53.622323+00:00` |
| **Scan Duration** | `0.18s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 13 malicious artifacts.

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
| Total Artifacts | 20 |
| Analyzed Artifacts (Scanned) | 15 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 1084 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 75.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3044 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5972 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 13 | 1084 | 86.7% |
| MARKDOWN | 2 | 0 | 13.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.665`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_16 | 6 | 40.0% |
| file_cluster_8 | 5 | 33.3% |
| file_cluster_13 | 2 | 13.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 13.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 101 LOC)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 3.5 | 39.4 | 10.8 | 6.7 | 3.8 |
| Error & Exception Exposure | 0.0 | 8.0 | 2.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Testing Exposure | 2.3 | 80.0 | 38.4 | 3.2 | 80.0 |
| API Exposure | 0.5 | 8.5 | 4.5 | 4.0 | 0.5 |
| Concurrency Exposure | 0.0 | 70.5 | 10.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.2 | 27.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 93.3 | 100.0 | 99.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.1 | 99.9 | 41.1 | 12.8 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 63.1 | 99.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 30.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `rsa-4.9.1/rsa/cli.py` (Hits: 16)
- `rsa-4.9.1/rsa/util.py` (Hits: 7)
- `rsa-4.9.1/rsa/pkcs1.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **key.py** (`rsa-4.9.1/rsa/key.py`) — 3 inbound connections
2. **randnum.py** (`rsa-4.9.1/rsa/randnum.py`) — 3 inbound connections
3. **common.py** (`rsa-4.9.1/rsa/common.py`) — 2 inbound connections
4. **pkcs1.py** (`rsa-4.9.1/rsa/pkcs1.py`) — 2 inbound connections
5. **prime.py** (`rsa-4.9.1/rsa/prime.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **key.py** (`rsa-4.9.1/rsa/key.py`) — 14 outbound dependencies
2. **pkcs1.py** (`rsa-4.9.1/rsa/pkcs1.py`) — 8 outbound dependencies
3. **cli.py** (`rsa-4.9.1/rsa/cli.py`) — 7 outbound dependencies
4. **parallel.py** (`rsa-4.9.1/rsa/parallel.py`) — 6 outbound dependencies
5. **prime.py** (`rsa-4.9.1/rsa/prime.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_pem_lines` (@ `rsa-4.9.1/rsa/pem.py`) -> Impact: **143.9** | LOC: 79
  * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
- `keygen` (@ `rsa-4.9.1/rsa/cli.py`) -> Impact: **108.3** | LOC: 175
- `sign_hash` (@ `rsa-4.9.1/rsa/pkcs1.py`) -> Impact: **101.2** | LOC: 104
- `__repr__` (@ `rsa-4.9.1/rsa/key.py`) -> Impact: **61.8** | LOC: 111
- `miller_rabin_primality_testing` (@ `rsa-4.9.1/rsa/prime.py`) -> Impact: **45.3** | LOC: 39
  * *Intent:* # Calculate number bitsize. bitsize = rsa.common.bit_size(number) # Set number of rounds. if bitsize >= 1536: return 3 if bitsize >= 1024: return 4 if...
- `private_to_public` (@ `rsa-4.9.1/rsa/util.py`) -> Impact: **38.4** | LOC: 76
  * *Intent:* # Parse the CLI options parser = OptionParser( usage="usage: %prog [options]", description="Reads a private key and outputs the " "corresponding publi...
- `__init__` (@ `rsa-4.9.1/rsa/common.py`) -> Impact: **22.8** | LOC: 15
- `assert_int` (@ `rsa-4.9.1/rsa/core.py`) -> Impact: **21.9** | LOC: 22
- `getprime` (@ `rsa-4.9.1/rsa/parallel.py`) -> Impact: **21.9** | LOC: 23
  * *Intent:* # Test for primeness if rsa.prime.is_prime(integer): pipe.send(integer) return def getprime(nbits: int, poolsize: int) -> int: """Returns a prime numb...
- `randint` (@ `rsa-4.9.1/rsa/randnum.py`) -> Impact: **17.0** | LOC: 20

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_pem_lines` (@ `rsa-4.9.1/rsa/pem.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
- `sign_hash` (@ `rsa-4.9.1/rsa/pkcs1.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `rsa-4.9.1/rsa/common.py`) -> **O(2^N) [Recursive]**
- `assert_int` (@ `rsa-4.9.1/rsa/core.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `rsa-4.9.1/rsa/key.py`) -> **O(2^N) [Recursive]**
- `keygen` (@ `rsa-4.9.1/rsa/cli.py`) -> **O(N^4)**
- `__repr__` (@ `rsa-4.9.1/rsa/key.py`) -> **O(N^4)**
- `_save_pkcs1_der` (@ `rsa-4.9.1/rsa/key.py`) -> **O(N^4)**
- `miller_rabin_primality_testing` (@ `rsa-4.9.1/rsa/prime.py`) -> **O(N^4)**
  * *Intent:* # Calculate number bitsize. bitsize = rsa.common.bit_size(number) # Set number of rounds. if bitsize >= 1536: return 3 if bitsize >= 1024: return 4 if...
- `__eq__` (@ `rsa-4.9.1/rsa/key.py`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `keygen` (@ `rsa-4.9.1/rsa/cli.py`) -> DB Complexity: **45**
- `private_to_public` (@ `rsa-4.9.1/rsa/util.py`) -> DB Complexity: **21**
  * *Intent:* # Parse the CLI options parser = OptionParser( usage="usage: %prog [options]", description="Reads a private key and outputs the " "corresponding publi...
- `__repr__` (@ `rsa-4.9.1/rsa/key.py`) -> DB Complexity: **9**
- `__init__` (@ `rsa-4.9.1/rsa/key.py`) -> DB Complexity: **6**
- `read_random_bits` (@ `rsa-4.9.1/rsa/randnum.py`) -> DB Complexity: **6**
- `__init__` (@ `rsa-4.9.1/rsa/key.py`) -> DB Complexity: **5**
- `__init__` (@ `rsa-4.9.1/rsa/common.py`) -> DB Complexity: **3**
- `_pem_lines` (@ `rsa-4.9.1/rsa/pem.py`) -> DB Complexity: **3**
  * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
- `_pad_for_encryption` (@ `rsa-4.9.1/rsa/pkcs1.py`) -> DB Complexity: **3**
- `__eq__` (@ `rsa-4.9.1/rsa/key.py`) -> DB Complexity: **2**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `rsa-4.9.1/rsa` | 13 | 1112.18 | 10.79% | 34.37% |
| `rsa-4.9.1` | 2 | 7.2 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `rsa-4.9.1/rsa/transform.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/key.py` -> **99.968%** Exposure
- `rsa-4.9.1/rsa/asn1.py` -> **99.9673%** Exposure
- `rsa-4.9.1/rsa/cli.py` -> **99.7966%** Exposure
- `rsa-4.9.1/rsa/util.py` -> **47.0273%** Exposure
### Highest State Flux (Mutation/Volatility)
- `rsa-4.9.1/rsa/key.py` -> **99.2194%** Exposure
- `rsa-4.9.1/rsa/common.py` -> **98.4458%** Exposure
- `rsa-4.9.1/rsa/pem.py` -> **95.7083%** Exposure
- `rsa-4.9.1/rsa/pkcs1.py` -> **50.4713%** Exposure
- `rsa-4.9.1/rsa/cli.py` -> **15.4427%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rsa-4.9.1/rsa/key.py` -> **0** Orphaned Functions | **8** Duplicates
- `rsa-4.9.1/rsa/cli.py` -> **1** Orphaned Functions | **4** Duplicates
- `rsa-4.9.1/rsa/transform.py` -> **2** Orphaned Functions | **0** Duplicates
- `rsa-4.9.1/rsa/util.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`rsa-4.9.1/rsa/pkcs1.py`** -> AI Confidence: **99.23%**
2. **`rsa-4.9.1/rsa/key.py`** -> AI Confidence: **99.18%**
3. **`rsa-4.9.1/rsa/cli.py`** -> AI Confidence: **99.15%**
4. **`rsa-4.9.1/rsa/parallel.py`** -> AI Confidence: **99.13%**
5. **`rsa-4.9.1/rsa/pem.py`** -> AI Confidence: **99.06%**
6. **`rsa-4.9.1/rsa/prime.py`** -> AI Confidence: **98.96%**
7. **`rsa-4.9.1/rsa/randnum.py`** -> AI Confidence: **98.92%**
8. **`rsa-4.9.1/rsa/__init__.py`** -> AI Confidence: **98.9%**
9. **`rsa-4.9.1/rsa/util.py`** -> AI Confidence: **98.89%**
10. **`rsa-4.9.1/rsa/common.py`** -> AI Confidence: **98.85%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `rsa-4.9.1/rsa/pkcs1.py` -> **99.9996%** Exposure
### Exploit Generation Surface
- `rsa-4.9.1/rsa/cli.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/key.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/pkcs1.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/randnum.py` -> **99.9896%** Exposure
- `rsa-4.9.1/rsa/prime.py` -> **0.7031%** Exposure
### Hardcoded Payload Artifacts
- `rsa-4.9.1/rsa/pem.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/key.py` -> **91.7239%** Exposure
### Algorithmic DoS Exposure
- `rsa-4.9.1/rsa/cli.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/key.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/util.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/pem.py` -> **99.9999%** Exposure
- `rsa-4.9.1/rsa/randnum.py` -> **99.9896%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `54` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rsa-4.9.1/rsa/key.py` (PYTHON) -> Cumulative Risk: **850.1**
- **Archetype:** `file_cluster_16` (Distance: 12.637 IQR)
- **Magnitude:** 265.7 | **LOC:** 859 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.968%)
- **Heaviest Functions:** `__repr__` (Impact: 61.8), `__eq__` (Impact: 14.3), `calculate_keys_custom_exponent` (Impact: 13.2)

### 2. `rsa-4.9.1/rsa/cli.py` (PYTHON) -> Cumulative Risk: **624.62**
- **Archetype:** `file_cluster_8` (Distance: 10.455 IQR)
- **Magnitude:** 140.64 | **LOC:** 322 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.7966%)
- **Heaviest Functions:** `keygen` (Impact: 108.3), `perform_operation` (Impact: 3.5), `perform_operation` (Impact: 3.5)

### 3. `rsa-4.9.1/rsa/pkcs1.py` (PYTHON) -> Cumulative Risk: **615.96**
- **Archetype:** `file_cluster_13` (Distance: 10.827 IQR)
- **Magnitude:** 177.58 | **LOC:** 486 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Obscured Payload (99.9996%), Algorithmic Dos (99.8143%)
- **Heaviest Functions:** `sign_hash` (Impact: 101.2), `_pad_for_encryption` (Impact: 15.5), `_find_method_hash` (Impact: 12.4)

### 4. `rsa-4.9.1/rsa/pem.py` (PYTHON) -> Cumulative Risk: **562.63**
- **Archetype:** `file_cluster_16` (Distance: 11.103 IQR)
- **Magnitude:** 160.44 | **LOC:** 135 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Secrets Risk (100.0%), Algorithmic Dos (99.9999%), State Flux (95.7083%)
- **Heaviest Functions:** `_pem_lines` (Impact: 143.9), `_markers` (Impact: 6.5)

### 5. `rsa-4.9.1/rsa/common.py` (PYTHON) -> Cumulative Risk: **467.54**
- **Archetype:** `file_cluster_16` (Distance: 11.703 IQR)
- **Magnitude:** 78.52 | **LOC:** 185 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (98.7672%), State Flux (98.4458%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 22.8), `extended_gcd` (Impact: 11.5), `crt` (Impact: 8.6)

### 6. `rsa-4.9.1/rsa/randnum.py` (PYTHON) -> Cumulative Risk: **466.41**
- **Archetype:** `file_cluster_16` (Distance: 9.637 IQR)
- **Magnitude:** 35.4 | **LOC:** 96 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9896%), Logic Bomb (99.9896%), Documentation (99.93%)
- **Heaviest Functions:** `randint` (Impact: 17.0), `read_random_bits` (Impact: 6.8), `read_random_int` (Impact: 2.6)

### 7. `rsa-4.9.1/rsa/prime.py` (PYTHON) -> Cumulative Risk: **356.26**
- **Archetype:** `file_cluster_8` (Distance: 9.449 IQR)
- **Magnitude:** 96.28 | **LOC:** 199 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.0167%), Verification (80.0%), Stability (50.0%)
- **Heaviest Functions:** `miller_rabin_primality_testing` (Impact: 45.3), `get_primality_testing_rounds` (Impact: 12.8), `getprime` (Impact: 12.6)

### 8. `rsa-4.9.1/rsa/parallel.py` (PYTHON) -> Cumulative Risk: **353.37**
- **Archetype:** `file_cluster_13` (Distance: 9.781 IQR)
- **Magnitude:** 37.38 | **LOC:** 97 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (94.0522%), Concurrency (70.5133%), Stability (50.0%)
- **Heaviest Functions:** `getprime` (Impact: 21.9), `_find_prime` (Impact: 10.8)

### 9. `rsa-4.9.1/rsa/asn1.py` (PYTHON) -> Cumulative Risk: **342.7**
- **Archetype:** `file_cluster_8` (Distance: 7.825 IQR)
- **Magnitude:** 18.38 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9673%), Documentation (79.9582%), Stability (50.0%)

### 10. `rsa-4.9.1/rsa/util.py` (PYTHON) -> Cumulative Risk: **319.22**
- **Archetype:** `file_cluster_8` (Distance: 7.561 IQR)
- **Magnitude:** 40.66 | **LOC:** 98 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Stability (50.0%), Tech Debt (47.0273%)
- **Heaviest Functions:** `private_to_public` (Impact: 38.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rsa-4.9.1/rsa/key.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.637 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.983 IQR)
- **Top Global Matches:** file_cluster_16: 12.637, file_cluster_13: 12.664, file_cluster_11: 12.965
- **Magnitude:** 265.7 | **LOC:** 859 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (39.3592%), Tech Debt (99.968%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 61.8 | O(N^4) | DB: 9)
  * `__eq__` (Impact: 14.3 | O(N^3) | DB: 2)
  * `calculate_keys_custom_exponent` (Impact: 13.2 | O(N^3))
    * *Intent:* # Instead of using the core functionality, use the Chinese Remainder # Theorem and be 2-4x faster. T...
  * `is_acceptable` (Impact: 11.0 | O(N^3))
  * `__init__` (Impact: 8.4 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 134`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`, `planned_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 23`, `concurrency: 7`, `import: 20`
* *Defense:* `safety: 12`, `doc: 141`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 121.45
  * `Choke Point (Betweenness):` 0.098901 | `Ripple Effect (Closeness):` 0.214286
  * `Imports (Out-Degree: 6):` rsa.pem, typing, rsa.core, rsa, rsa.prime, base64, doctest, pyasn1.type...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/pkcs1.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.827 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.949 IQR)
- **Top Global Matches:** file_cluster_13: 10.827, file_cluster_16: 10.847, file_cluster_8: 10.933
- **Magnitude:** 177.58 | **LOC:** 486 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.4934%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sign_hash` (Impact: 101.2 | O(2^N) | DB: 2)
  * `_pad_for_encryption` (Impact: 15.5 | O(N^3) | DB: 3)
  * `_find_method_hash` (Impact: 12.4 | O(N^3))
  * `_pad_for_signing` (Impact: 11.2 | O(N^3))
    * *Intent:* # We remove 0-bytes, so we'll end up with less padding than we've asked for, # so keep adding data u...
  * `decrypt` (Impact: 9.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 38`, `args: 11`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `io: 2`, `api: 12`, `import: 7`
* *Defense:* `safety: 5`, `doc: 60`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142857
  * `Imports (Out-Degree: 0):` , typing, rsa, doctest, sys, os, hashlib, hmac
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/pem.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.103 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.437 IQR)
- **Top Global Matches:** file_cluster_16: 11.103, file_cluster_13: 11.143, file_cluster_7: 11.359
- **Magnitude:** 160.44 | **LOC:** 135 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_pem_lines` (Impact: 143.9 | O(2^N) | DB: 3)
    * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
  * `_markers` (Impact: 6.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 2`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 0):` typing, base64
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.455 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.529 IQR)
- **Top Global Matches:** file_cluster_8: 10.455, file_cluster_13: 10.503, file_cluster_16: 10.539
- **Magnitude:** 140.64 | **LOC:** 322 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (6.7132%), Tech Debt (99.7966%)
**Top Internal Functions/Classes:**
  * `keygen` (Impact: 108.3 | O(N^4) | DB: 45)
  * `perform_operation` (Impact: 3.5 | O(N^2))
  * `perform_operation` (Impact: 3.5 | O(N^2))
  * `perform_operation` (Impact: 1.6 | O(N^2))
  * `perform_operation` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 52`, `args: 12`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 16`, `api: 15`, `import: 7`
* *Defense:* `safety: 12`, `doc: 36`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typing, rsa, abc, sys, rsa.key, rsa.pkcs1, optparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/prime.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.449 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.095 IQR)
- **Top Global Matches:** file_cluster_8: 9.449, file_cluster_16: 9.512, file_cluster_13: 9.728
- **Magnitude:** 96.28 | **LOC:** 199 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.1213%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `miller_rabin_primality_testing` (Impact: 45.3 | O(N^4))
    * *Intent:* # Calculate number bitsize. bitsize = rsa.common.bit_size(number) # Set number of rounds. if bitsize...
  * `get_primality_testing_rounds` (Impact: 12.8 | O(N^2))
  * `getprime` (Impact: 12.6 | O(N^3))
    * *Intent:* # Exit inner loop and continue with next witness.
  * `is_prime` (Impact: 9.8 | O(N^2))
  * `gcd` (Impact: 5.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 27`, `args: 6`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 1`, `doc: 19`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 81.304
  * `Choke Point (Betweenness):` 0.005495 | `Ripple Effect (Closeness):` 0.223214
  * `Imports (Out-Degree: 2):` rsa.common, rsa, rsa.randnum, doctest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/common.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.703 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.08 IQR)
- **Top Global Matches:** file_cluster_16: 11.703, file_cluster_13: 11.883, file_cluster_8: 12.002
- **Magnitude:** 78.52 | **LOC:** 185 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (15.6545%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 22.8 | O(2^N) | DB: 3)
  * `extended_gcd` (Impact: 11.5 | O(N^2))
    * *Intent:* """ Returns the number of bytes required to hold a specific long number. The number of bytes is roun...
  * `crt` (Impact: 8.6 | O(N^2))
  * `byte_size` (Impact: 6.3 | O(N^2))
  * `inverse` (Impact: 5.7 | O(N^2))
    * *Intent:* """ Returns the ceiling function of a division between `num` and `div`. Usage:: >>> ceil_div(100, 7)...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 2`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 96.741
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.257143
  * `Imports (Out-Degree: 0):` typing, doctest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/util.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.561 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.784 IQR)
- **Top Global Matches:** file_cluster_8: 7.561, file_cluster_13: 8.134, file_cluster_7: 8.222
- **Magnitude:** 40.66 | **LOC:** 98 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (4.5496%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `private_to_public` (Impact: 38.4 | O(N^3) | DB: 21)
    * *Intent:* # Parse the CLI options parser = OptionParser( usage="usage: %prog [options]", description="Reads a ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 15`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 4`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, rsa.key, optparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/parallel.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.781 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.931 IQR)
- **Top Global Matches:** file_cluster_13: 9.781, file_cluster_8: 10.016, file_cluster_16: 10.258
- **Magnitude:** 37.38 | **LOC:** 97 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.1826%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getprime` (Impact: 21.9 | O(N^3))
    * *Intent:* # Test for primeness if rsa.prime.is_prime(integer): pipe.send(integer) return def getprime(nbits: i...
  * `_find_prime` (Impact: 10.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` multiprocessing, rsa, rsa.prime, doctest, rsa.randnum, multiprocessing.connection
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/randnum.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.637 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.346 IQR)
- **Top Global Matches:** file_cluster_16: 9.637, file_cluster_13: 9.722, file_cluster_8: 9.747
- **Magnitude:** 35.4 | **LOC:** 96 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (4.9875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `randint` (Impact: 17.0 | O(N^3))
  * `read_random_bits` (Impact: 6.8 | O(N^2) | DB: 6)
  * `read_random_int` (Impact: 2.6 | O(N^1))
  * `read_random_odd_int` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 6`, `import: 3`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 115.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.285714
  * `Imports (Out-Degree: 0):` struct, rsa, os
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.251 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_16: 10.251, file_cluster_8: 10.361, file_cluster_7: 10.662
- **Magnitude:** 28.78 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_int` (Impact: 21.9 | O(2^N))
  * `decrypt_int` (Impact: 2.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 4`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/asn1.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.825 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.67 IQR)
- **Top Global Matches:** file_cluster_8: 7.825, file_cluster_7: 8.226, file_cluster_1: 8.436
- **Magnitude:** 18.38 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.5253%), Tech Debt (99.9673%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `class_start: 3`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.9%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.1 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.687 IQR)
- **Top Global Matches:** file_cluster_8: 6.1, file_cluster_13: 6.763, file_cluster_7: 6.946
- **Magnitude:** 16.64 | **LOC:** 61 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.7929%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` rsa.key, rsa.pkcs1, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/transform.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.279 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.275 IQR)
- **Top Global Matches:** file_cluster_16: 10.279, file_cluster_13: 10.361, file_cluster_8: 10.458
- **Magnitude:** 15.78 | **LOC:** 73 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `int2bytes` (Impact: 11.3 | O(N^2))
  * `bytes2int` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math, doctest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.04 | **LOC:** 252 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.16 | **LOC:** 108 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `rsa-4.9.1/rsa/pkcs1.py` (PYTHON) | Magnitude: 177.58 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: sec_reflection_metaprogramming: 204, indent_spaces: 144, doc: 60, structural_boundaries: 38
- `rsa-4.9.1/rsa/parallel.py` (PYTHON) | Magnitude: 37.38 | Delta: **0.235 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, branch: 12, structural_boundaries: 12, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `rsa-4.9.1/rsa/key.py` (PYTHON) | Magnitude: 265.7 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 297, doc: 141, structural_boundaries: 134, generics: 60
- `rsa-4.9.1/rsa/pem.py` (PYTHON) | Magnitude: 160.44 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, doc: 16, branch: 14, structural_boundaries: 14
- `rsa-4.9.1/rsa/transform.py` (PYTHON) | Magnitude: 15.78 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 10, indent_spaces: 10, structural_boundaries: 7, branch: 3
- `rsa-4.9.1/rsa/randnum.py` (PYTHON) | Magnitude: 35.4 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, doc: 10, api: 6
- `rsa-4.9.1/rsa/core.py` (PYTHON) | Magnitude: 28.78 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, doc: 6, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `rsa-4.9.1/rsa/cli.py` (PYTHON) | Magnitude: 140.64 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 188, structural_boundaries: 52, doc: 36, branch: 29
- `rsa-4.9.1/rsa/prime.py` (PYTHON) | Magnitude: 96.28 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 27, branch: 22, doc: 19
- `rsa-4.9.1/rsa/asn1.py` (PYTHON) | Magnitude: 18.38 | Delta: **0.401 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, doc: 4, class_start: 3
- `rsa-4.9.1/rsa/util.py` (PYTHON) | Magnitude: 40.66 | Delta: **0.573 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 15, branch: 9, io: 7
- `rsa-4.9.1/rsa/__init__.py` (PYTHON) | Magnitude: 16.64 | Delta: **0.663 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, encapsulation: 6, structural_boundaries: 5, import: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rsa-4.9.1/rsa/key.py` -> **Severity: 9.813** (Bridge: 0.0989 * Flux: 99.2194%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rsa-4.9.1/rsa/common.py` -> **Severity: 1.838** (Embedded: 0.2571 * Error Risk: 7.1478%)
- `rsa-4.9.1/rsa/key.py` -> **Severity: 1.715** (Embedded: 0.2143 * Error Risk: 8.0039%)
- `rsa-4.9.1/rsa/pem.py` -> **Severity: 1.136** (Embedded: 0.1633 * Error Risk: 6.9569%)
- `rsa-4.9.1/rsa/pkcs1.py` -> **Severity: 0.613** (Embedded: 0.1429 * Error Risk: 4.2895%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rsa-4.9.1/rsa/randnum.py` -> **Severity: 11577.69** (Blast Radius: 115.858 * Doc Risk: 99.93%)
- `rsa-4.9.1/rsa/core.py` -> **Severity: 5934.027** (Blast Radius: 62.187 * Doc Risk: 95.4223%)
- `rsa-4.9.1/rsa/asn1.py` -> **Severity: 4972.361** (Blast Radius: 62.187 * Doc Risk: 79.9582%)
- `rsa-4.9.1/rsa/parallel.py` -> **Severity: 4230.562** (Blast Radius: 44.981 * Doc Risk: 94.0522%)
- `rsa-4.9.1/rsa/cli.py` -> **Severity: 2759.171** (Blast Radius: 44.981 * Doc Risk: 61.3408%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
