# ARCHITECTURAL_BRIEF: cryptography
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/cryptography` |
| **Timestamp** | `2026-08-07T05:22:03.722657+00:00` |
| **Scan Duration** | `1.9s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 315 malicious artifacts.

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
| Total Artifacts | 349 |
| Analyzed Artifacts (Scanned) | 315 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 34 |
| Total LOC | 73156 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5119 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1549 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1657 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 26 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 234 | 53402 | 74.3% |
| RUST | 81 | 19754 | 25.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.485`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 114 | 36.2% |
| file_cluster_0 | 96 | 30.5% |
| file_cluster_8 | 70 | 22.2% |
| file_cluster_9 | 18 | 5.7% |
| file_cluster_16 | 17 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 34*

**Composition by Extension & Reason:**
- `.rs`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 10x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.apache`: 1x Excluded (Unsupported Extension: '.APACHE')
- `.bsd`: 1x Excluded (Unsupported Extension: '.BSD')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 94.0 | 12.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 91.0 | 20.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.6 | 1.1 | 0.0 |
| API Exposure | 0.0 | 16.8 | 4.9 | 4.4 | 0.0 |
| Concurrency Exposure | 0.0 | 37.3 | 0.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 15.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 18.8 | 14.5 | 30.8 |
| Specification Exposure | 6.7 | 100.0 | 83.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.5 | 14.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cryptography-46.0.6/tests/x509/test_x509.py` (Hits: 226)
- `cryptography-46.0.6/tests/x509/test_x509_ext.py` (Hits: 114)
- `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` (Hits: 81)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **exceptions.py** (`cryptography-46.0.6/src/cryptography/exceptions.py`) — 61 inbound connections
2. **cryptography.py** (`cryptography-46.0.6/src/_cffi_src/openssl/cryptography.py`) — 45 inbound connections
3. **utils.py** (`cryptography-46.0.6/src/cryptography/utils.py`) — 26 inbound connections
4. **doubles.py** (`cryptography-46.0.6/tests/doubles.py`) — 20 inbound connections
5. **backend.py** (`cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/mod.rs`) — 66 outbound dependencies
2. **certificate.rs** (`cryptography-46.0.6/src/rust/src/x509/certificate.rs`) — 54 outbound dependencies
3. **extension.rs** (`cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/extension.rs`) — 39 outbound dependencies
4. **pkcs7.rs** (`cryptography-46.0.6/src/rust/src/pkcs7.rs`) — 37 outbound dependencies
5. **extension_policy.rs** (`cryptography-46.0.6/src/rust/src/x509/verify/extension_policy.rs`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_admissions_extension` (@ `cryptography-46.0.6/tests/x509/test_x509.py`) -> Impact: **533.9** | LOC: 5067
- `process_data` (@ `cryptography-46.0.6/src/rust/src/backend/aead.rs`) -> Impact: **417.8** | LOC: 1056
- `test_repr` (@ `cryptography-46.0.6/tests/x509/test_x509_ext.py`) -> Impact: **406.7** | LOC: 4912
- `test_boringssl_vectors` (@ `cryptography-46.0.6/tests/hazmat/primitives/test_aead.py`) -> Impact: **274.6** | LOC: 773
- `certificates` (@ `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs`) -> Impact: **271.6** | LOC: 755
- `pkey_private_bytes` (@ `cryptography-46.0.6/src/rust/src/backend/utils.rs`) -> Impact: **251.6** | LOC: 203
- `extensions` (@ `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs`) -> Impact: **207.7** | LOC: 621
- `compute_signature_algorithm` (@ `cryptography-46.0.6/src/rust/src/x509/sign.rs`) -> Impact: **185.2** | LOC: 424
- `load_hash_vectors` (@ `cryptography-46.0.6/tests/utils.py`) -> Impact: **152.8** | LOC: 250
- `pkey_public_bytes` (@ `cryptography-46.0.6/src/rust/src/backend/utils.rs`) -> Impact: **151.3** | LOC: 115

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `cryptography-46.0.6/tests/hazmat/primitives` | 48 | 6999.24 | 5.35% | 0.0% |
| `cryptography-46.0.6/src/rust/src/backend` | 20 | 4789.56 | 20.14% | 72.91% |
| `cryptography-46.0.6/tests/x509` | 7 | 3777.5 | 3.27% | 0.0% |
| `cryptography-46.0.6/src/rust/src/x509` | 11 | 3354.14 | 16.52% | 34.81% |
| `cryptography-46.0.6/src/cryptography/x509` | 9 | 2213.9 | 26.81% | 43.63% |
| `cryptography-46.0.6/src/rust/src` | 11 | 1642.22 | 11.86% | 33.59% |
| `cryptography-46.0.6/tests` | 9 | 1140.42 | 9.86% | 0.0% |
| `cryptography-46.0.6/src/rust/cryptography-x509/src` | 12 | 833.46 | 3.55% | 9.78% |
| `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization` | 5 | 638.26 | 15.22% | 33.1% |
| `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy` | 2 | 530.74 | 6.64% | 40.51% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/declarative_asn1.pyi` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/aead.pyi` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/ciphers.pyi` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/ec.pyi` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/x963kdf.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/concatkdf.py` -> **99.9998%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/pbkdf2.py` -> **99.9995%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-crypto/src/pkcs12.rs` -> **99.9923%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/utils.py` -> **99.9894%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cryptography-46.0.6/src/cryptography/x509/extensions.py` -> **0** Orphaned Functions | **241** Duplicates
- `cryptography-46.0.6/tests/x509/test_x509_ext.py` -> **36** Orphaned Functions | **67** Duplicates
- `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` -> **61** Orphaned Functions | **35** Duplicates
- `cryptography-46.0.6/tests/x509/test_ocsp.py` -> **74** Orphaned Functions | **4** Duplicates
- `cryptography-46.0.6/tests/hazmat/primitives/test_pkcs7.py` -> **58** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`cryptography-46.0.6/src/rust/src/x509/sign.rs`** -> AI Confidence: **99.34%**
2. **`cryptography-46.0.6/src/cryptography/hazmat/bindings/openssl/binding.py`** -> AI Confidence: **99.31%**
3. **`cryptography-46.0.6/src/cryptography/x509/ocsp.py`** -> AI Confidence: **99.31%**
4. **`cryptography-46.0.6/tests/hazmat/primitives/test_aead.py`** -> AI Confidence: **99.31%**
5. **`cryptography-46.0.6/tests/hazmat/primitives/test_argon2.py`** -> AI Confidence: **99.31%**
6. **`cryptography-46.0.6/tests/hazmat/primitives/test_kbkdf.py`** -> AI Confidence: **99.31%**
7. **`cryptography-46.0.6/tests/hazmat/primitives/test_keywrap.py`** -> AI Confidence: **99.31%**
8. **`cryptography-46.0.6/tests/utils.py`** -> AI Confidence: **99.31%**
9. **`cryptography-46.0.6/tests/wycheproof/test_aes.py`** -> AI Confidence: **99.31%**
10. **`cryptography-46.0.6/tests/x509/verification/test_limbo.py`** -> AI Confidence: **99.31%**
11. **`cryptography-46.0.6/src/rust/src/asn1.rs`** -> AI Confidence: **99.31%**
12. **`cryptography-46.0.6/src/rust/src/backend/aead.rs`** -> AI Confidence: **99.31%**
13. **`cryptography-46.0.6/src/rust/src/backend/ciphers.rs`** -> AI Confidence: **99.31%**
14. **`cryptography-46.0.6/src/rust/src/backend/dh.rs`** -> AI Confidence: **99.31%**
15. **`cryptography-46.0.6/src/rust/src/backend/dsa.rs`** -> AI Confidence: **99.31%**
16. **`cryptography-46.0.6/src/rust/src/backend/ec.rs`** -> AI Confidence: **99.31%**
17. **`cryptography-46.0.6/src/rust/src/backend/rsa.rs`** -> AI Confidence: **99.31%**
18. **`cryptography-46.0.6/src/rust/src/pkcs12.rs`** -> AI Confidence: **99.31%**
19. **`cryptography-46.0.6/src/rust/src/pkcs7.rs`** -> AI Confidence: **99.31%**
20. **`cryptography-46.0.6/src/rust/src/x509/ocsp_req.rs`** -> AI Confidence: **99.31%**
21. **`cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs`** -> AI Confidence: **99.31%**
22. **`cryptography-46.0.6/src/rust/src/backend/keys.rs`** -> AI Confidence: **99.25%**
23. **`cryptography-46.0.6/src/rust/src/x509/common.rs`** -> AI Confidence: **99.25%**
24. **`cryptography-46.0.6/src/rust/src/x509/crl.rs`** -> AI Confidence: **99.25%**
25. **`cryptography-46.0.6/src/rust/src/x509/extensions.rs`** -> AI Confidence: **99.25%**
26. **`cryptography-46.0.6/noxfile.py`** -> AI Confidence: **99.24%**
27. **`cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/pkcs7.py`** -> AI Confidence: **99.24%**
28. **`cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py`** -> AI Confidence: **99.24%**
29. **`cryptography-46.0.6/src/cryptography/x509/base.py`** -> AI Confidence: **99.24%**
30. **`cryptography-46.0.6/tests/hazmat/primitives/test_x25519.py`** -> AI Confidence: **99.24%**
31. **`cryptography-46.0.6/tests/x509/verification/test_verification.py`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/certificate.rs` -> **99.9995%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/ops.rs` -> **99.997%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` -> **87.5834%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` -> **51.9221%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1899` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON) -> Cumulative Risk: **660.36**
- **Archetype:** `file_cluster_16` (Distance: 12.804 IQR)
- **Magnitude:** 1410.44 | **LOC:** 2529 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.6494%), Documentation (85.0737%)
- **Heaviest Functions:** `__eq__` (Impact: 18.1), `__init__` (Impact: 16.8), `__eq__` (Impact: 14.6)

### 2. `cryptography-46.0.6/src/cryptography/x509/general_name.py` (PYTHON) -> Cumulative Risk: **659.94**
- **Archetype:** `file_cluster_0` (Distance: 12.665 IQR)
- **Magnitude:** 195.96 | **LOC:** 282 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9237%), Cognitive Load (83.9442%)
- **Heaviest Functions:** `__init__` (Impact: 11.4), `__init__` (Impact: 7.6), `__init__` (Impact: 7.6)

### 3. `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` (PYTHON) -> Cumulative Risk: **618.52**
- **Archetype:** `file_cluster_0` (Distance: 11.099 IQR)
- **Magnitude:** 113.9 | **LOC:** 269 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (96.6216%), State Flux (81.7243%)
- **Heaviest Functions:** `validate_for_algorithm` (Impact: 12.7), `_check_aes_key_length` (Impact: 8.9), `validate_for_algorithm` (Impact: 7.6)

### 4. `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/padding.py` (PYTHON) -> Cumulative Risk: **600.5**
- **Archetype:** `file_cluster_0` (Distance: 12.249 IQR)
- **Magnitude:** 38.12 | **LOC:** 112 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.387%), Documentation (92.1757%)
- **Heaviest Functions:** `__init__` (Impact: 3.7), `mgf` (Impact: 1.8), `algorithm` (Impact: 1.8)

### 5. `cryptography-46.0.6/src/cryptography/hazmat/decrepit/ciphers/algorithms.py` (PYTHON) -> Cumulative Risk: **591.86**
- **Archetype:** `file_cluster_0` (Distance: 10.96 IQR)
- **Magnitude:** 53.38 | **LOC:** 113 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (98.5283%), Cognitive Load (90.1225%)
- **Heaviest Functions:** `__init__` (Impact: 5.5), `__init__` (Impact: 1.8), `key_size` (Impact: 1.8)

### 6. `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/concatkdf.py` (PYTHON) -> Cumulative Risk: **584.77**
- **Archetype:** `file_cluster_13` (Distance: 11.934 IQR)
- **Magnitude:** 71.72 | **LOC:** 126 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.9998%), Safety Score (86.0959%)
- **Heaviest Functions:** `verify` (Impact: 4.2), `verify` (Impact: 4.2), `derive` (Impact: 3.8)

### 7. `cryptography-46.0.6/src/rust/cryptography-crypto/src/pkcs12.rs` (RUST) -> Cumulative Risk: **561.34**
- **Archetype:** `file_cluster_0` (Distance: 11.558 IQR)
- **Magnitude:** 101.12 | **LOC:** 141 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9923%), Verification (80.0%), Safety Score (78.4672%)
- **Heaviest Functions:** `kdf` (Impact: 58.6), `test_pkcs12_kdf` (Impact: 6.6)

### 8. `cryptography-46.0.6/src/rust/src/backend/ec.rs` (RUST) -> Cumulative Risk: **554.75**
- **Archetype:** `file_cluster_0` (Distance: 12.187 IQR)
- **Magnitude:** 483.64 | **LOC:** 687 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9161%), State Flux (99.3032%), Verification (80.0%)
- **Heaviest Functions:** `sign` (Impact: 46.6), `__eq__` (Impact: 25.1), `exchange` (Impact: 24.3)

### 9. `cryptography-46.0.6/src/cryptography/exceptions.py` (PYTHON) -> Cumulative Risk: **551.6**
- **Archetype:** `file_cluster_13` (Distance: 12.774 IQR)
- **Magnitude:** 13.76 | **LOC:** 53 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.5154%), Safety Score (90.4651%)
- **Heaviest Functions:** `__init__` (Impact: 2.1), `__init__` (Impact: 1.1)

### 10. `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/dh.pyi` (PYTHON) -> Cumulative Risk: **550.09**
- **Archetype:** `file_cluster_0` (Distance: 12.367 IQR)
- **Magnitude:** 19.2 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9614%), Tech Debt (99.8073%), Safety Score (83.8891%)
- **Heaviest Functions:** `__init__` (Impact: 1.1), `generate_parameters` (Impact: 1.1), `from_pem_parameters` (Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cryptography-46.0.6/tests/x509/test_x509_ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.081 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.944 IQR)
- **Top Global Matches:** file_cluster_8: 11.081, file_cluster_7: 11.714, file_cluster_0: 11.892
- **Magnitude:** 1485.66 | **LOC:** 7507 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.704%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_repr` (Impact: 406.7)
  * `test_public_bytes` (Impact: 111.3)
  * `test_key_agreement_false_encipher_deciph` (Impact: 8.9)
  * `test_invalid_hash_algorithm` (Impact: 7.4)
  * `test_invalid_signature_algorithm` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 1306`, `args: 480`, `func_start: 470`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 10`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 67`, `orphaned_logic: 36`
* *Architecture:* `io: 114`, `api: 537`, `import: 19`
* *Defense:* `safety: 739`, `doc: 2`, `test: 1344`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ipaddress, cryptography.hazmat.primitives.asymmetric, ..hazmat.primitives.test_ec, cryptography, cryptography.hazmat._oid, binascii, cryptography.x509.extensions, cryptography.x509.oid...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_x509.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.732 IQR)
- **Top Global Matches:** file_cluster_8: 11.398, file_cluster_7: 11.961, file_cluster_0: 11.989
- **Magnitude:** 1442.9 | **LOC:** 6963 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9112%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_admissions_extension` (Impact: 533.9)
  * `test_revoked_extensions` (Impact: 15.2)
  * `test_invalid_pem` (Impact: 9.2)
  * `test_invalid_unicode_name` (Impact: 9.1)
  * `test_revoked_basics` (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 988`, `args: 374`, `func_start: 336`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1`, `dead_code: 3`, `duplicate_logic: 18`
* *Architecture:* `io: 226`, `api: 427`, `import: 22`
* *Defense:* `safety: 742`, `doc: 14`, `test: 1116`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.78
  * `Choke Point (Betweenness):` 0.000438 | `Ripple Effect (Closeness):` 0.006369
  * `Imports (Out-Degree: 10):` ..hazmat.primitives.fixtures_ec, ipaddress, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.asymmetric.utils, ..hazmat.primitives.test_ec, cryptography, binascii, cryptography.x509.extensions...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.804 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.087 IQR)
- **Top Global Matches:** file_cluster_16: 12.804, file_cluster_0: 12.829, file_cluster_11: 13.033
- **Magnitude:** 1410.44 | **LOC:** 2529 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.7144%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__eq__` (Impact: 18.1)
  * `__init__` (Impact: 16.8)
  * `__eq__` (Impact: 14.6)
  * `__eq__` (Impact: 10.9)
  * `__hash__` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 765`, `args: 309`, `func_start: 309`, `class_start: 48`
* *Risk/State:* `state_mutation: 388`, `dead_code: 1`, `duplicate_logic: 241`
* *Architecture:* `api: 186`, `import: 18`
* *Defense:* `safety: 117`, `doc: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.427
  * `Choke Point (Betweenness):` 0.000634 | `Ripple Effect (Closeness):` 0.015605
  * `Imports (Out-Degree: 8):` ipaddress, cryptography.x509.general_name, cryptography.hazmat.primitives.asymmetric.ec, collections.abc, cryptography.x509.name, hashlib, cryptography.x509.certificate_transparency, abc...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.837 IQR)
- **Top Global Matches:** file_cluster_8: 11.837, file_cluster_16: 11.844, file_cluster_0: 11.86
- **Magnitude:** 928.58 | **LOC:** 1046 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.5036%), Tech Debt (99.9914%)
**Top Internal Functions/Classes:**
  * `certificates` (Impact: 271.6)
  * `extensions` (Impact: 207.7)
  * `create_ocsp_response` (Impact: 142.6)
  * `response_status` (Impact: 21.9)
  * `signature_hash_algorithm` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 160`, `args: 68`, `func_start: 55`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 24`, `orphaned_logic: 11`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 115`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cryptography_x509::common, py_to_datetime, crate::error::CryptographyError, crate::x509::certificate, OCSPResponse, CryptographyResult, x509, sct...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/aead.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.166 IQR)
- **Top Global Matches:** file_cluster_0: 12.166, file_cluster_8: 12.179, file_cluster_16: 12.277
- **Magnitude:** 915.06 | **LOC:** 1182 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0778%), Tech Debt (99.4658%)
**Top Internal Functions/Classes:**
  * `process_data` (Impact: 417.8)
  * `decrypt_with_context` (Impact: 44.9)
  * `encrypt_with_context` (Impact: 39.3)
  * `new` (Impact: 26.8)
  * `decrypt` (Impact: 26.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 147`, `args: 43`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `dead_code: 1`, `duplicate_logic: 31`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 153`, `test: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, crate::exceptions, AesGcm, AesSiv, AesOcb3, ChaCha20Poly1305, crate::error::CryptographyError, AesGcmSiv...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.188 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.793 IQR)
- **Top Global Matches:** file_cluster_8: 11.188, file_cluster_13: 11.334, file_cluster_0: 11.508
- **Magnitude:** 650.58 | **LOC:** 977 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.9628%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_hash_vectors` (Impact: 152.8)
  * `load_kasvs_dh_vectors` (Impact: 103.2)
  * `load_rfc6979_vectors` (Impact: 70.8)
  * `load_fips_dsa_sig_vectors` (Impact: 55.6)
  * `load_nist_ccm_vectors` (Impact: 45.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 118`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 99`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 37`, `import: 10`
* *Defense:* `safety: 17`, `doc: 20`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006369
  * `Imports (Out-Degree: 1):` cryptography_vectors, re, binascii, cryptography.exceptions, os, pytest, json, collections...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/rsa.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.977 IQR)
- **Top Global Matches:** file_cluster_0: 11.977, file_cluster_8: 12.081, file_cluster_16: 12.13
- **Magnitude:** 644.8 | **LOC:** 834 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.815%), Tech Debt (66.6298%)
**Top Internal Functions/Classes:**
  * `setup_signature_ctx` (Impact: 103.1)
  * `check_private_key_components` (Impact: 80.2)
  * `setup_encryption_ctx` (Impact: 61.1)
  * `decrypt` (Impact: 46.9)
  * `private_key` (Impact: 30.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 124`, `args: 42`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 73`, `dead_code: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 66`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, RsaPrivateKey, Hasher, crate::exceptions, crate::backend::hashes, std::hash::Hash, RsaPublicKey, crate::error::CryptographyError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_rsa.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.14 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.483 IQR)
- **Top Global Matches:** file_cluster_8: 10.14, file_cluster_0: 10.567, file_cluster_7: 10.778
- **Magnitude:** 615.42 | **LOC:** 2798 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.3665%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_invalid_oaep_decryption_data_to_lar` (Impact: 77.1)
  * `test_decrypt_oaep_sha2_vectors` (Impact: 11.5)
  * `_build_oaep_sha2_vectors` (Impact: 10.3)
  * `test_generate_rsa_keys` (Impact: 9.5)
  * `test_pss_signing` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 262`, `args: 196`, `func_start: 123`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`, `dead_code: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 33`, `api: 203`, `import: 14`
* *Defense:* `safety: 100`, `doc: 2`, `test: 384`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .utils, binascii, cryptography.exceptions, ...utils, cryptography.hazmat.primitives.asymmetric, os, pytest, copy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/extensions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.622 IQR)
- **Top Global Matches:** file_cluster_8: 12.622, file_cluster_16: 12.751, file_cluster_13: 12.843
- **Magnitude:** 608.6 | **LOC:** 768 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.8251%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode_extension` (Impact: 127.0)
  * `encode_certificate_policies` (Impact: 65.2)
  * `encode_issuing_distribution_point` (Impact: 56.6)
  * `encode_key_usage` (Impact: 50.5)
  * `encode_profession_info` (Impact: 48.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 190`, `args: 15`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 70`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 151`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CryptographyResult, pyo3::pybacked::PyBackedStr, py_uint_to_big_endian_bytes, oid, cryptography_x509::crl, cryptography_x509::common::Asn1Write, crate::types, x509...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ec.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.332 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.944 IQR)
- **Top Global Matches:** file_cluster_8: 10.332, file_cluster_0: 10.872, file_cluster_13: 10.949
- **Magnitude:** 596.84 | **LOC:** 1582 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2234%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_key_exchange_with_vectors` (Impact: 28.9)
  * `test_deterministic_nonce` (Impact: 21.6)
  * `test_load_invalid_ec_key_from_pem` (Impact: 14.9)
  * `test_derive_point_at_infinity` (Impact: 14.7)
  * `test_signature_failures` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 210`, `args: 117`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `io: 43`, `api: 168`, `import: 18`
* *Defense:* `safety: 96`, `doc: 6`, `test: 245`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.000682 | `Ripple Effect (Closeness):` 0.020382
  * `Imports (Out-Degree: 5):` .utils, binascii, ...utils, cryptography.hazmat.primitives.asymmetric.ec, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.asymmetric.utils, textwrap, os...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.712 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.65 IQR)
- **Top Global Matches:** file_cluster_8: 10.712, file_cluster_0: 11.159, file_cluster_7: 11.322
- **Magnitude:** 585.48 | **LOC:** 1975 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_loads_ssh_cert` (Impact: 132.9)
  * `test_load_ssh_public_key` (Impact: 44.3)
  * `test_load_ssh_private_key` (Impact: 40.4)
  * `test_dsa_private_key_sizes` (Impact: 14.5)
  * `test_ssh_errors_pubpriv_mismatch` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 254`, `args: 146`, `func_start: 98`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 43`
* *Architecture:* `io: 28`, `api: 108`, `import: 14`
* *Defense:* `safety: 131`, `doc: 2`, `test: 338`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ...doubles, cryptography.exceptions, ...utils, cryptography.hazmat.primitives.asymmetric, os, base64, pytest, .test_ec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.836 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.267 IQR)
- **Top Global Matches:** file_cluster_8: 10.836, file_cluster_0: 11.128, file_cluster_7: 11.413
- **Magnitude:** 542.4 | **LOC:** 1847 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.7776%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_skip_fips_format` (Impact: 14.8)
  * `test_dh_public_key` (Impact: 11.9)
  * `test_dh_private_key` (Impact: 11.7)
  * `test_invalid_kdf_rounds` (Impact: 7.3)
  * `test_invalid_encoding_with_traditional` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 231`, `args: 189`, `func_start: 97`, `class_start: 10`
* *Risk/State:* `dead_code: 1`, `duplicate_logic: 35`, `orphaned_logic: 61`
* *Architecture:* `io: 81`, `api: 107`, `import: 16`
* *Defense:* `safety: 122`, `doc: 16`, `test: 323`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cryptography.hazmat.primitives.ciphers, .utils, cryptography.hazmat.primitives.hashes, ...utils, cryptography.hazmat.decrepit.ciphers.algorithms, cryptography.hazmat.primitives.asymmetric, textwrap, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_ocsp.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.321 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.104 IQR)
- **Top Global Matches:** file_cluster_8: 10.321, file_cluster_7: 11.029, file_cluster_13: 11.128
- **Magnitude:** 512.36 | **LOC:** 1762 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_load_unauthorized` (Impact: 42.3)
  * `test_invalid_add_response` (Impact: 25.0)
  * `test_multi_valued_responses` (Impact: 15.2)
  * `test_add_response_by_hash_bad_hash` (Impact: 11.3)
  * `test_add_cert_by_hash_bad_hash` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 254`, `args: 90`, `func_start: 83`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 74`
* *Architecture:* `io: 41`, `api: 85`, `import: 16`
* *Defense:* `safety: 142`, `test: 318`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ..hazmat.primitives.fixtures_ec, .test_x509, cryptography.exceptions, cryptography.hazmat.primitives.asymmetric, ..utils, os, base64, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/pkcs12.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.327 IQR)
- **Top Global Matches:** file_cluster_8: 12.327, file_cluster_0: 12.396, file_cluster_16: 12.502
- **Magnitude:** 496.46 | **LOC:** 830 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.8496%), Tech Debt (10.9201%)
**Top Internal Functions/Classes:**
  * `serialize_key_and_certificates` (Impact: 90.2)
  * `decode_encryption_algorithm` (Impact: 69.6)
  * `serialize_safebags` (Impact: 53.2)
  * `load_pkcs12` (Impact: 47.0)
  * `load_key_and_certificates` (Impact: 36.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 150`, `args: 30`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `import: 14`
* *Defense:* `safety: 124`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::hash::Hash, keys, crate::error::CryptographyError, CryptographyResult, x509, cryptography_x509::common::Utf8StoredBMPString, Hasher, hmac...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.684 IQR)
- **Top Global Matches:** file_cluster_16: 11.152, file_cluster_8: 11.209, file_cluster_13: 11.413
- **Magnitude:** 486.1 | **LOC:** 1620 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.242%), Tech Debt (99.7375%)
**Top Internal Functions/Classes:**
  * `sign` (Impact: 48.4)
  * `_get_ssh_key_type` (Impact: 18.0)
  * `_parse_exts_opts` (Impact: 14.9)
  * `verify_cert_signature` (Impact: 13.7)
  * `valid_before` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 214`, `args: 86`, `func_start: 84`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 72`, `dead_code: 1`, `duplicate_logic: 42`
* *Architecture:* `io: 3`, `api: 73`, `import: 17`
* *Defense:* `safety: 49`, `doc: 102`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.58
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.003185
  * `Imports (Out-Degree: 2):` warnings, re, binascii, cryptography.exceptions, cryptography.hazmat.primitives.ciphers, enum, cryptography.hazmat.primitives.asymmetric, bcrypt...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/ec.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.187 IQR)
- **Top Global Matches:** file_cluster_0: 12.187, file_cluster_16: 12.382, file_cluster_11: 12.403
- **Magnitude:** 483.64 | **LOC:** 687 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8491%), Tech Debt (99.9161%)
**Top Internal Functions/Classes:**
  * `sign` (Impact: 46.6)
  * `__eq__` (Impact: 25.1)
  * `exchange` (Impact: 24.3)
  * `private_key` (Impact: 23.8)
  * `private_numbers` (Impact: 22.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 145`, `args: 44`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 108`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 12`, `orphaned_logic: 7`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 40`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, Hasher, crate::exceptions, EllipticCurvePublicNumbers, crate::backend::utils, std::hash::Hash, derive_private_key, from_public_bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_aead.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.276 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.536 IQR)
- **Top Global Matches:** file_cluster_8: 10.276, file_cluster_0: 10.649, file_cluster_13: 10.882
- **Magnitude:** 481.4 | **LOC:** 1060 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.0754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_boringssl_vectors` (Impact: 274.6)
  * `test_vectors_invalid` (Impact: 19.6)
  * `test_vectors` (Impact: 13.6)
  * `test_openssl_vectors` (Impact: 13.1)
  * `test_bad_key` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 152`, `args: 67`, `func_start: 67`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 40`, `api: 77`, `import: 10`
* *Defense:* `safety: 59`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .utils, binascii, cryptography.exceptions, ...utils, cryptography.hazmat.primitives.ciphers.aead, os, pytest, cryptography.hazmat.bindings._rust...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/pkcs7.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.251 IQR)
- **Top Global Matches:** file_cluster_8: 11.251, file_cluster_13: 11.396, file_cluster_0: 11.414
- **Magnitude:** 481.14 | **LOC:** 884 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.3246%), Tech Debt (8.5323%)
**Top Internal Functions/Classes:**
  * `sign_and_serialize` (Impact: 111.9)
  * `encrypt_and_serialize` (Impact: 83.0)
  * `decrypt_der` (Impact: 68.3)
  * `check_decrypt_parameters` (Impact: 47.2)
  * `symmetric_decrypt` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 161`, `args: 25`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 24`
* *Defense:* `safety: 59`, `test: 7`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::HashMap, cryptography_x509::common, std::borrow::Cow, crate::error::CryptographyError, pyo3::PyTypeInfo, decrypt_pem, CryptographyResult, x509...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/utils.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.886 IQR)
- **Top Global Matches:** file_cluster_8: 10.886, file_cluster_16: 11.116, file_cluster_13: 11.266
- **Magnitude:** 474.1 | **LOC:** 406 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.3978%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pkey_private_bytes` (Impact: 251.6)
  * `pkey_public_bytes` (Impact: 151.3)
  * `calculate_digest_and_algorithm` (Impact: 18.4)
  * `py_int_to_bn` (Impact: 11.1)
  * `bn_to_big_endian_bytes` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 80`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `dead_code: 1`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `safety: 55`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, crate::types, crate::backend::hashes::Hash, PyBytesMethods, crate::error::CryptographyError, pyo3::types::PyAnyMethods
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/ciphers.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.982 IQR)
- **Top Global Matches:** file_cluster_0: 12.982, file_cluster_16: 13.048, file_cluster_11: 13.057
- **Magnitude:** 454.14 | **LOC:** 619 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.717%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 88.2)
  * `create_decryption_ctx` (Impact: 29.4)
  * `create_encryption_ctx` (Impact: 22.2)
  * `finalize_with_tag` (Impact: 21.3)
  * `update_into` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 103`, `args: 41`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 97`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 19`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, crate::exceptions, CffiMutBuf, pyo3::IntoPyObject, crate::error::CryptographyError, types, _advance_aad, crate::buf::CffiBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/common.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.515 IQR)
- **Top Global Matches:** file_cluster_16: 11.515, file_cluster_8: 11.592, file_cluster_13: 11.768
- **Magnitude:** 393.08 | **LOC:** 558 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.3157%), Tech Debt (8.2965%)
**Top Internal Functions/Classes:**
  * `encode_general_name` (Impact: 61.2)
  * `parse_general_name` (Impact: 47.4)
  * `encode_name_entry` (Impact: 36.7)
  * `py_to_datetime` (Impact: 32.3)
  * `parse_name_attribute` (Impact: 27.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 93`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `safety: 62`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyo3::types::IntoPyDict, crate::asn1::oid_to_py_oid, OtherName, NameReadable, crate::error::CryptographyError, Extensions, CryptographyResult, x509...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/sign.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.478 IQR)
- **Top Global Matches:** file_cluster_8: 11.478, file_cluster_16: 11.758, file_cluster_13: 11.849
- **Magnitude:** 384.8 | **LOC:** 668 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8687%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compute_signature_algorithm` (Impact: 185.2)
  * `identify_public_key_type` (Impact: 37.4)
  * `compute_pss_salt_length` (Impact: 31.2)
  * `identify_signature_algorithm_parameters` (Impact: 28.5)
  * `verify_signature_with_signature_algorith` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 44`, `args: 31`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `safety: 106`, `test: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.283
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009554
  * `Imports (Out-Degree: 0):` CryptographyResult, oid, HashType, std::collections::HashMap, crate::exceptions, cryptography_x509::common, crate::asn1::oid_to_py_oid, KeyType...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_pkcs7.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.222 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.951 IQR)
- **Top Global Matches:** file_cluster_8: 10.222, file_cluster_0: 10.687, file_cluster_13: 10.878
- **Magnitude:** 377.42 | **LOC:** 1520 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0251%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_smime_encrypt_smime_encoding` (Impact: 12.2)
  * `test_smime_encrypt_der_encoding` (Impact: 11.7)
  * `test_smime_encrypt_pem_encoding` (Impact: 11.1)
  * `test_load_pkcs7_der` (Impact: 9.4)
  * `test_rsa_pkcs_padding_options` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 204`, `args: 121`, `func_start: 87`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 13`, `dead_code: 1`, `duplicate_logic: 7`, `orphaned_logic: 58`
* *Architecture:* `io: 26`, `api: 95`, `import: 17`
* *Defense:* `safety: 82`, `doc: 2`, `test: 232`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` email.parser, cryptography.hazmat.primitives.ciphers, cryptography.exceptions, tests.x509.test_x509, ...utils, ...hazmat.primitives.test_rsa, cryptography.hazmat.primitives.asymmetric, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/crl.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.429 IQR)
- **Top Global Matches:** file_cluster_0: 12.429, file_cluster_16: 12.526, file_cluster_8: 12.577
- **Magnitude:** 368.76 | **LOC:** 710 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.4481%), Tech Debt (77.4158%)
**Top Internal Functions/Classes:**
  * `create_x509_crl` (Impact: 56.2)
  * `extensions` (Impact: 53.4)
  * `__getitem__` (Impact: 31.8)
  * `parse_crl_entry_ext` (Impact: 25.3)
  * `get_revoked_certificate_by_serial_number` (Impact: 13.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 105`, `args: 48`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 29`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 19`, `import: 13`
* *Defense:* `safety: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` encode_der_data, IssuerAlternativeName, crate::error::CryptographyError, crate::x509::certificate, PySliceMethods, CryptographyResult, x509, cryptography_x509::crl::
    self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/extension.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.821 IQR)
- **Top Global Matches:** file_cluster_16: 11.821, file_cluster_13: 11.871, file_cluster_8: 11.996
- **Magnitude:** 367.1 | **LOC:** 938 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3782%), Tech Debt (44.1812%)
**Top Internal Functions/Classes:**
  * `permits` (Impact: 134.3)
  * `authority_key_identifier` (Impact: 32.6)
  * `extended_key_usage` (Impact: 14.9)
    * *Intent:* // CABF: AKI is required on all CA certificates *except* root CA certificates, // where is it merely...
  * `permits` (Impact: 13.2)
  * `name_constraints` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 123`, `args: 30`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 35`, `concurrency: 4`, `import: 28`
* *Defense:* `safety: 130`, `doc: 12`, `test: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NameConstraints, asn1::ObjectIdentifier, epoch, v1_cert_pem, ExtendedKeyUsage, crate::types::DNSName, Extensions, cryptography_x509::oid::
    AUTHORITY_INFORMATION_ACCESS_OID...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `cryptography-46.0.6/src/rust/src/x509/verify/mod.rs` (RUST) | Magnitude: 147.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 373, structural_boundaries: 83, generics: 73, safety: 68
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/dsa.py` (PYTHON) | Magnitude: 30.64 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 37, doc: 32, api: 22
- `cryptography-46.0.6/src/cryptography/hazmat/asn1/asn1.py` (PYTHON) | Magnitude: 17.52 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 25, branch: 12, generics: 12
- `cryptography-46.0.6/src/rust/src/backend/aead.rs` (RUST) | Magnitude: 915.06 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 944, branch: 160, safety: 153, generics: 148
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/padding.py` (PYTHON) | Magnitude: 38.12 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, encapsulation: 31, structural_boundaries: 30, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cryptography-46.0.6/src/cryptography/x509/name.py` (PYTHON) | Magnitude: 196.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 296, encapsulation: 154, structural_boundaries: 106, branch: 66
- `cryptography-46.0.6/tests/hazmat/primitives/test_poly1305.py` (PYTHON) | Magnitude: 88.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 104, test: 36, structural_boundaries: 26, state_mutation: 20
- `cryptography-46.0.6/tests/wycheproof/test_aes.py` (PYTHON) | Magnitude: 91.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 108, branch: 32, structural_boundaries: 29, test: 26
- `cryptography-46.0.6/src/_cffi_src/openssl/engine.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 8, dead_code: 5, structural_boundaries: 2, import: 1
- `cryptography-46.0.6/tests/hazmat/primitives/test_camellia.py` (PYTHON) | Magnitude: 20.32 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 13, args: 12, closures: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/ec.py` (PYTHON) | Magnitude: 80.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 260, structural_boundaries: 82, api: 55, doc: 38
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/__init__.pyi` (PYTHON) | Magnitude: 76.9 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 14, api: 12, generics: 10
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/ops.rs` (RUST) | Magnitude: 47.28 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 23, generics: 22, args: 15
- `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON) | Magnitude: 1410.44 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1855, structural_boundaries: 765, encapsulation: 500, generics: 419
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/declarative_asn1.pyi` (PYTHON) | Magnitude: 8.6 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 13, api: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs` (RUST) | Magnitude: 928.58 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 811, generics: 184, branch: 168, structural_boundaries: 160
- `cryptography-46.0.6/src/rust/src/x509/ocsp_req.rs` (RUST) | Magnitude: 89.36 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 173, structural_boundaries: 33, branch: 32, generics: 25
- `cryptography-46.0.6/tests/hazmat/primitives/test_hash_vectors.py` (PYTHON) | Magnitude: 38.98 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 30, test: 22, args: 19
- `cryptography-46.0.6/tests/hazmat/primitives/test_aes_gcm.py` (PYTHON) | Magnitude: 90.5 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 33, test: 33, state_mutation: 21
- `cryptography-46.0.6/src/rust/src/x509/verify/extension_policy.rs` (RUST) | Magnitude: 96.04 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 208, structural_boundaries: 40, generics: 36, safety: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/asn1.pyi` (PYTHON) | Magnitude: 24.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: generics: 4, structural_boundaries: 3, args: 3, func_start: 3
- `cryptography-46.0.6/src/_cffi_src/openssl/cryptography.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 8, dead_code: 7, structural_boundaries: 2, import: 1
- `cryptography-46.0.6/src/_cffi_src/openssl/ssl.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 17, doc: 8, structural_boundaries: 2, import: 1
- `cryptography-46.0.6/src/rust/cryptography-crypto/src/constant_time.rs` (RUST) | Magnitude: 4.92 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 4, branch: 1, structural_boundaries: 1, args: 1
- `cryptography-46.0.6/src/rust/src/declarative_asn1/mod.rs` (RUST) | Magnitude: 14.56 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, encapsulation: 3, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cryptography-46.0.6/src/cryptography/x509/extensions.py` -> **Severity: 0.063** (Bridge: 0.0006 * Flux: 99.6494%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 0.053** (Bridge: 0.0006 * Flux: 81.7243%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/algorithms.py` -> **Severity: 0.046** (Bridge: 0.0006 * Flux: 70.8543%)
- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **Severity: 0.039** (Bridge: 0.002 * Flux: 19.7371%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/pbkdf2.py` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 99.9995%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 17.525** (Embedded: 0.1937 * Error Risk: 90.4651%)
- `cryptography-46.0.6/tests/doubles.py` -> **Severity: 4.918** (Embedded: 0.0645 * Error Risk: 76.2542%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 3.894** (Embedded: 0.0706 * Error Risk: 55.164%)
- `cryptography-46.0.6/src/cryptography/utils.py` -> **Severity: 3.843** (Embedded: 0.0906 * Error Risk: 42.4212%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/algorithms.py` -> **Severity: 3.095** (Embedded: 0.0487 * Error Risk: 63.5955%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 6154.231** (Blast Radius: 61.842 * Doc Risk: 99.5154%)
- `cryptography-46.0.6/src/cryptography/utils.py` -> **Severity: 4226.24** (Blast Radius: 42.693 * Doc Risk: 98.9914%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 1786.63** (Blast Radius: 18.491 * Doc Risk: 96.6216%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/_cipheralgorithm.py` -> **Severity: 1611.978** (Blast Radius: 17.857 * Doc Risk: 90.2715%)
- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **Severity: 1417.145** (Blast Radius: 14.209 * Doc Risk: 99.7357%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
