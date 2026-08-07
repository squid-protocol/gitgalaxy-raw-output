# ARCHITECTURAL_BRIEF: rsa
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/rsa` |
| **Timestamp** | `2026-08-07T05:26:14.378174+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 13 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 55.5 | 18.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Testing Exposure | 2.3 | 80.0 | 20.5 | 2.7 | 80.0 |
| API Exposure | 0.5 | 8.5 | 4.5 | 4.0 | 0.5 |
| Concurrency Exposure | 0.0 | 70.5 | 8.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.2 | 27.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 93.3 | 100.0 | 99.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.1 | 61.2 | 21.7 | 11.9 | 11.9 |
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

- `keygen` (@ `rsa-4.9.1/rsa/cli.py`) -> Impact: **48.6** | LOC: 175
- `_pem_lines` (@ `rsa-4.9.1/rsa/pem.py`) -> Impact: **31.9** | LOC: 79
  * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
- `sign_hash` (@ `rsa-4.9.1/rsa/pkcs1.py`) -> Impact: **29.2** | LOC: 104
- `__repr__` (@ `rsa-4.9.1/rsa/key.py`) -> Impact: **28.1** | LOC: 111
- `private_to_public` (@ `rsa-4.9.1/rsa/util.py`) -> Impact: **21.1** | LOC: 76
  * *Intent:* # Parse the CLI options parser = OptionParser( usage="usage: %prog [options]", description="Reads a private key and outputs the " "corresponding publi...
- `miller_rabin_primality_testing` (@ `rsa-4.9.1/rsa/prime.py`) -> Impact: **19.3** | LOC: 39
  * *Intent:* # Calculate number bitsize. bitsize = rsa.common.bit_size(number) # Set number of rounds. if bitsize >= 1536: return 3 if bitsize >= 1024: return 4 if...
- `read_infile` (@ `rsa-4.9.1/rsa/cli.py`) -> Impact: **11.5** | LOC: 23
- `getprime` (@ `rsa-4.9.1/rsa/parallel.py`) -> Impact: **11.5** | LOC: 23
  * *Intent:* # Test for primeness if rsa.prime.is_prime(integer): pipe.send(integer) return def getprime(nbits: int, poolsize: int) -> int: """Returns a prime numb...
- `randint` (@ `rsa-4.9.1/rsa/randnum.py`) -> Impact: **9.0** | LOC: 20
- `get_primality_testing_rounds` (@ `rsa-4.9.1/rsa/prime.py`) -> Impact: **8.8** | LOC: 15

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `rsa-4.9.1/rsa` | 13 | 665.18 | 10.79% | 34.38% |
| `rsa-4.9.1` | 2 | 7.2 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `rsa-4.9.1/rsa/transform.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/cli.py` -> **99.9922%** Exposure
- `rsa-4.9.1/rsa/key.py` -> **99.968%** Exposure
- `rsa-4.9.1/rsa/asn1.py` -> **99.9673%** Exposure
- `rsa-4.9.1/rsa/util.py` -> **47.0273%** Exposure
### Highest State Flux (Mutation/Volatility)
- `rsa-4.9.1/rsa/key.py` -> **99.2194%** Exposure
- `rsa-4.9.1/rsa/common.py` -> **98.4458%** Exposure
- `rsa-4.9.1/rsa/pem.py` -> **95.7083%** Exposure
- `rsa-4.9.1/rsa/pkcs1.py` -> **50.4713%** Exposure
- `rsa-4.9.1/rsa/cli.py` -> **15.4427%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rsa-4.9.1/rsa/cli.py` -> **3** Orphaned Functions | **5** Duplicates
- `rsa-4.9.1/rsa/key.py` -> **0** Orphaned Functions | **8** Duplicates
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

### Hardcoded Payload Artifacts
- `rsa-4.9.1/rsa/pem.py` -> **100.0%** Exposure
- `rsa-4.9.1/rsa/key.py` -> **91.7239%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `54` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rsa-4.9.1/rsa/key.py` (PYTHON) -> Cumulative Risk: **666.83**
- **Archetype:** `file_cluster_16` (Distance: 12.636 IQR)
- **Magnitude:** 188.1 | **LOC:** 859 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.968%), State Flux (99.2194%), Secrets Risk (91.7239%)
- **Heaviest Functions:** `__repr__` (Impact: 28.1), `__eq__` (Impact: 7.3), `calculate_keys_custom_exponent` (Impact: 7.2)

### 2. `rsa-4.9.1/rsa/pem.py` (PYTHON) -> Cumulative Risk: **432.78**
- **Archetype:** `file_cluster_16` (Distance: 11.103 IQR)
- **Magnitude:** 46.44 | **LOC:** 135 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Secrets Risk (100.0%), State Flux (95.7083%), Safety Score (54.4259%)
- **Heaviest Functions:** `_pem_lines` (Impact: 31.9), `_markers` (Impact: 4.5)

### 3. `rsa-4.9.1/rsa/cli.py` (PYTHON) -> Cumulative Risk: **422.69**
- **Archetype:** `file_cluster_8` (Distance: 10.477 IQR)
- **Magnitude:** 104.94 | **LOC:** 322 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9922%), Verification (80.0%), Stability (50.0%)
- **Heaviest Functions:** `keygen` (Impact: 48.6), `read_infile` (Impact: 11.5), `parse_cli` (Impact: 8.7)

### 4. `rsa-4.9.1/rsa/pkcs1.py` (PYTHON) -> Cumulative Risk: **347.98**
- **Archetype:** `file_cluster_13` (Distance: 10.827 IQR)
- **Magnitude:** 84.88 | **LOC:** 486 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (50.4713%), Stability (50.0%)
- **Heaviest Functions:** `sign_hash` (Impact: 29.2), `_pad_for_encryption` (Impact: 8.5), `decrypt` (Impact: 6.9)

### 5. `rsa-4.9.1/rsa/common.py` (PYTHON) -> Cumulative Risk: **338.8**
- **Archetype:** `file_cluster_16` (Distance: 11.703 IQR)
- **Magnitude:** 52.42 | **LOC:** 185 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.4458%), Safety Score (54.4683%), Stability (50.0%)
- **Heaviest Functions:** `__init__` (Impact: 8.1), `extended_gcd` (Impact: 8.1), `crt` (Impact: 6.0)

### 6. `rsa-4.9.1/rsa/asn1.py` (PYTHON) -> Cumulative Risk: **304.04**
- **Archetype:** `file_cluster_8` (Distance: 7.825 IQR)
- **Magnitude:** 18.38 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9673%), Stability (50.0%), Documentation (41.3009%)

### 7. `rsa-4.9.1/rsa/transform.py` (PYTHON) -> Cumulative Risk: **264.64**
- **Archetype:** `file_cluster_16` (Distance: 10.279 IQR)
- **Magnitude:** 12.38 | **LOC:** 73 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (93.3333%), Stability (50.0%), Documentation (11.1256%)
- **Heaviest Functions:** `int2bytes` (Impact: 7.9), `bytes2int` (Impact: 2.2)

### 8. `rsa-4.9.1/rsa/parallel.py` (PYTHON) -> Cumulative Risk: **253.59**
- **Archetype:** `file_cluster_13` (Distance: 9.781 IQR)
- **Magnitude:** 21.78 | **LOC:** 97 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (70.5133%), Stability (50.0%), Cognitive Load (17.1826%)
- **Heaviest Functions:** `getprime` (Impact: 11.5), `_find_prime` (Impact: 5.6)

### 9. `rsa-4.9.1/rsa/core.py` (PYTHON) -> Cumulative Risk: **228.08**
- **Archetype:** `file_cluster_16` (Distance: 10.251 IQR)
- **Magnitude:** 14.88 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (61.1584%), Stability (50.0%), Api Exposure (8.0325%)
- **Heaviest Functions:** `assert_int` (Impact: 8.0), `decrypt_int` (Impact: 2.5)

### 10. `rsa-4.9.1/rsa/util.py` (PYTHON) -> Cumulative Risk: **219.02**
- **Archetype:** `file_cluster_8` (Distance: 7.561 IQR)
- **Magnitude:** 23.36 | **LOC:** 98 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Tech Debt (47.0273%), Documentation (11.9203%)
- **Heaviest Functions:** `private_to_public` (Impact: 21.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rsa-4.9.1/rsa/key.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.636 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.983 IQR)
- **Top Global Matches:** file_cluster_16: 12.636, file_cluster_13: 12.663, file_cluster_11: 12.964
- **Magnitude:** 188.1 | **LOC:** 859 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3592%), Tech Debt (99.968%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 28.1)
  * `__eq__` (Impact: 7.3)
  * `calculate_keys_custom_exponent` (Impact: 7.2)
    * *Intent:* # Instead of using the core functionality, use the Chinese Remainder # Theorem and be 2-4x faster. T...
  * `is_acceptable` (Impact: 5.8)
  * `load_pkcs1_openssl_der` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 134`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`, `planned_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 23`, `concurrency: 7`, `import: 20`
* *Defense:* `safety: 12`, `doc: 141`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 121.45
  * `Choke Point (Betweenness):` 0.098901 | `Ripple Effect (Closeness):` 0.214286
  * `Imports (Out-Degree: 6):` rsa.asn1, doctest, pyasn1.codec.der, typing, rsa.core, rsa.pem, pyasn1.type, warnings...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.477 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.506 IQR)
- **Top Global Matches:** file_cluster_8: 10.477, file_cluster_13: 10.522, file_cluster_16: 10.561
- **Magnitude:** 104.94 | **LOC:** 322 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.7361%), Tech Debt (99.9922%)
**Top Internal Functions/Classes:**
  * `keygen` (Impact: 48.6)
  * `read_infile` (Impact: 11.5)
  * `parse_cli` (Impact: 8.7)
  * `__call__` (Impact: 4.2)
  * `perform_operation` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 52`, `args: 12`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `planned_debt: 1`, `duplicate_logic: 5`, `orphaned_logic: 3`
* *Architecture:* `io: 16`, `api: 15`, `import: 7`
* *Defense:* `safety: 12`, `doc: 36`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typing, rsa.key, rsa.pkcs1, abc, sys, optparse, rsa
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/pkcs1.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.827 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.949 IQR)
- **Top Global Matches:** file_cluster_13: 10.827, file_cluster_16: 10.847, file_cluster_8: 10.933
- **Magnitude:** 84.88 | **LOC:** 486 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4934%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sign_hash` (Impact: 29.2)
  * `_pad_for_encryption` (Impact: 8.5)
  * `decrypt` (Impact: 6.9)
  * `_find_method_hash` (Impact: 6.5)
  * `_pad_for_signing` (Impact: 6.0)
    * *Intent:* # We remove 0-bytes, so we'll end up with less padding than we've asked for, # so keep adding data u...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 38`, `args: 11`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `io: 2`, `api: 12`, `import: 7`
* *Defense:* `safety: 5`, `doc: 60`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142857
  * `Imports (Out-Degree: 0):` doctest, hmac, , typing, os, sys, rsa, hashlib
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/prime.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.449 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.095 IQR)
- **Top Global Matches:** file_cluster_8: 9.449, file_cluster_16: 9.512, file_cluster_13: 9.728
- **Magnitude:** 55.58 | **LOC:** 199 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1213%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `miller_rabin_primality_testing` (Impact: 19.3)
    * *Intent:* # Calculate number bitsize. bitsize = rsa.common.bit_size(number) # Set number of rounds. if bitsize...
  * `get_primality_testing_rounds` (Impact: 8.8)
  * `is_prime` (Impact: 6.8)
  * `getprime` (Impact: 6.6)
    * *Intent:* # Exit inner loop and continue with next witness.
  * `gcd` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 27`, `args: 6`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 1`, `doc: 19`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 81.304
  * `Choke Point (Betweenness):` 0.005495 | `Ripple Effect (Closeness):` 0.223214
  * `Imports (Out-Degree: 2):` doctest, rsa.randnum, rsa.common, rsa
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/common.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.703 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.08 IQR)
- **Top Global Matches:** file_cluster_16: 11.703, file_cluster_13: 11.883, file_cluster_8: 12.002
- **Magnitude:** 52.42 | **LOC:** 185 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.6545%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 8.1)
  * `extended_gcd` (Impact: 8.1)
    * *Intent:* """ Returns the number of bytes required to hold a specific long number. The number of bytes is roun...
  * `crt` (Impact: 6.0)
  * `byte_size` (Impact: 4.3)
  * `inverse` (Impact: 4.0)
    * *Intent:* """ Returns the ceiling function of a division between `num` and `div`. Usage:: >>> ceil_div(100, 7)...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 2`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 96.741
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.257143
  * `Imports (Out-Degree: 0):` doctest, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/pem.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.103 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.437 IQR)
- **Top Global Matches:** file_cluster_16: 11.103, file_cluster_13: 11.143, file_cluster_7: 11.359
- **Magnitude:** 46.44 | **LOC:** 135 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_pem_lines` (Impact: 31.9)
    * *Intent:* """Generator over PEM lines between pem_start and pem_end."""
  * `_markers` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 2`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 0):` base64, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/randnum.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.637 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.346 IQR)
- **Top Global Matches:** file_cluster_16: 9.637, file_cluster_13: 9.722, file_cluster_8: 9.747
- **Magnitude:** 25.4 | **LOC:** 96 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `randint` (Impact: 9.0)
  * `read_random_bits` (Impact: 4.8)
  * `read_random_int` (Impact: 2.6)
  * `read_random_odd_int` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 6`, `import: 3`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 115.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.285714
  * `Imports (Out-Degree: 0):` rsa, struct, os
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rsa-4.9.1/rsa/util.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.561 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.784 IQR)
- **Top Global Matches:** file_cluster_8: 7.561, file_cluster_13: 8.134, file_cluster_7: 8.222
- **Magnitude:** 23.36 | **LOC:** 98 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.5496%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `private_to_public` (Impact: 21.1)
    * *Intent:* # Parse the CLI options parser = OptionParser( usage="usage: %prog [options]", description="Reads a ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 15`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 4`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` rsa.key, sys, optparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/parallel.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.781 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.931 IQR)
- **Top Global Matches:** file_cluster_13: 9.781, file_cluster_8: 10.016, file_cluster_16: 10.258
- **Magnitude:** 21.78 | **LOC:** 97 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.1826%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getprime` (Impact: 11.5)
    * *Intent:* # Test for primeness if rsa.prime.is_prime(integer): pipe.send(integer) return def getprime(nbits: i...
  * `_find_prime` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest, rsa.prime, multiprocessing.connection, multiprocessing, rsa.randnum, rsa
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/asn1.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.825 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.67 IQR)
- **Top Global Matches:** file_cluster_8: 7.825, file_cluster_7: 8.226, file_cluster_1: 8.436
- **Magnitude:** 18.38 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Risk Profile:** Cognitive Load (3.7929%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` doctest, rsa.pkcs1, rsa.key
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/rsa/core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.251 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_16: 10.251, file_cluster_8: 10.361, file_cluster_7: 10.662
- **Magnitude:** 14.88 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_int` (Impact: 8.0)
  * `decrypt_int` (Impact: 2.5)
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

### `rsa-4.9.1/rsa/transform.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.279 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.275 IQR)
- **Top Global Matches:** file_cluster_16: 10.279, file_cluster_13: 10.361, file_cluster_8: 10.458
- **Magnitude:** 12.38 | **LOC:** 73 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `int2bytes` (Impact: 7.9)
  * `bytes2int` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 44.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` doctest, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rsa-4.9.1/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.04 | **LOC:** 252 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- `rsa-4.9.1/rsa/pkcs1.py` (PYTHON) | Magnitude: 84.88 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: sec_reflection_metaprogramming: 204, indent_spaces: 144, doc: 60, structural_boundaries: 38
- `rsa-4.9.1/rsa/parallel.py` (PYTHON) | Magnitude: 21.78 | Delta: **0.235 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, branch: 12, structural_boundaries: 12, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `rsa-4.9.1/rsa/key.py` (PYTHON) | Magnitude: 188.1 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 297, doc: 141, structural_boundaries: 134, generics: 60
- `rsa-4.9.1/rsa/pem.py` (PYTHON) | Magnitude: 46.44 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, doc: 16, branch: 14, structural_boundaries: 14
- `rsa-4.9.1/rsa/transform.py` (PYTHON) | Magnitude: 12.38 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 10, indent_spaces: 10, structural_boundaries: 7, branch: 3
- `rsa-4.9.1/rsa/randnum.py` (PYTHON) | Magnitude: 25.4 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, doc: 10, api: 6
- `rsa-4.9.1/rsa/core.py` (PYTHON) | Magnitude: 14.88 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, doc: 6, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `rsa-4.9.1/rsa/cli.py` (PYTHON) | Magnitude: 104.94 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 188, structural_boundaries: 52, doc: 36, branch: 29
- `rsa-4.9.1/rsa/prime.py` (PYTHON) | Magnitude: 55.58 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 27, branch: 22, doc: 19
- `rsa-4.9.1/rsa/asn1.py` (PYTHON) | Magnitude: 18.38 | Delta: **0.401 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, doc: 4, class_start: 3
- `rsa-4.9.1/rsa/util.py` (PYTHON) | Magnitude: 23.36 | Delta: **0.573 IQR** | Secondary Pull: `file_cluster_13`
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

- `rsa-4.9.1/rsa/common.py` -> **Severity: 14.006** (Embedded: 0.2571 * Error Risk: 54.4683%)
- `rsa-4.9.1/rsa/key.py` -> **Severity: 11.903** (Embedded: 0.2143 * Error Risk: 55.5491%)
- `rsa-4.9.1/rsa/pem.py` -> **Severity: 8.886** (Embedded: 0.1633 * Error Risk: 54.4259%)
- `rsa-4.9.1/rsa/pkcs1.py` -> **Severity: 6.302** (Embedded: 0.1429 * Error Risk: 44.1125%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rsa-4.9.1/rsa/randnum.py` -> **Severity: 5285.303** (Blast Radius: 115.858 * Doc Risk: 45.6188%)
- `rsa-4.9.1/rsa/core.py` -> **Severity: 3803.257** (Blast Radius: 62.187 * Doc Risk: 61.1584%)
- `rsa-4.9.1/rsa/asn1.py` -> **Severity: 2568.379** (Blast Radius: 62.187 * Doc Risk: 41.3009%)
- `rsa-4.9.1/rsa/key.py` -> **Severity: 1447.72** (Blast Radius: 121.45 * Doc Risk: 11.9203%)
- `rsa-4.9.1/rsa/cli.py` -> **Severity: 1189.572** (Blast Radius: 44.981 * Doc Risk: 26.4461%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
