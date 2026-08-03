# ARCHITECTURAL_BRIEF: cryptography
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/cryptography` |
| **Timestamp** | `2026-08-03T21:20:09.043166+00:00` |
| **Scan Duration** | `1.78s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 315 malicious artifacts.

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
| Total Artifacts | 349 |
| Analyzed Artifacts (Scanned) | 315 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 34 |
| Total LOC | 73156 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.3% |
| Dominant Lang | RUST |

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
> **Architectural Drift Z-Score:** `4.476`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 114 | 36.2% |
| file_cluster_0 | 95 | 30.2% |
| file_cluster_8 | 71 | 22.5% |
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
| Error & Exception Exposure | 0.0 | 80.0 | 12.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.5 | 1.1 | 0.0 |
| API Exposure | 0.0 | 16.8 | 4.9 | 4.4 | 0.0 |
| Concurrency Exposure | 0.0 | 55.5 | 0.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 18.8 | 14.5 | 30.8 |
| Specification Exposure | 6.7 | 100.0 | 83.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.7 | 31.1 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 51.2 | 62.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 28.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `process_data` (@ `cryptography-46.0.6/src/rust/src/backend/aead.rs`) -> Impact: **2607.6** | LOC: 1056
- `pkey_private_bytes` (@ `cryptography-46.0.6/src/rust/src/backend/utils.rs`) -> Impact: **1424.5** | LOC: 203
- `test_repr` (@ `cryptography-46.0.6/tests/x509/test_x509_ext.py`) -> Impact: **1373.2** | LOC: 4912
- `test_admissions_extension` (@ `cryptography-46.0.6/tests/x509/test_x509.py`) -> Impact: **1235.4** | LOC: 5067
- `permits` (@ `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/extension.rs`) -> Impact: **1042.0** | LOC: 646
- `certificates` (@ `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs`) -> Impact: **982.8** | LOC: 755
- `new` (@ `cryptography-46.0.6/src/rust/src/backend/ciphers.rs`) -> Impact: **955.4** | LOC: 101
- `compute_signature_algorithm` (@ `cryptography-46.0.6/src/rust/src/x509/sign.rs`) -> Impact: **882.2** | LOC: 424
- `test_boringssl_vectors` (@ `cryptography-46.0.6/tests/hazmat/primitives/test_aead.py`) -> Impact: **864.6** | LOC: 773
- `get_cipher_registry` (@ `cryptography-46.0.6/src/rust/src/backend/cipher_registry.rs`) -> Impact: **796.9** | LOC: 176

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `test_repr` (@ `cryptography-46.0.6/tests/x509/test_x509_ext.py`) -> **O(2^N) [Recursive]**
- `test_public_bytes` (@ `cryptography-46.0.6/tests/x509/test_x509_ext.py`) -> **O(2^N) [Recursive]**
- `permits` (@ `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/extension.rs`) -> **O(2^N) [Recursive]**
- `process_data` (@ `cryptography-46.0.6/src/rust/src/backend/aead.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `cryptography-46.0.6/src/rust/src/backend/ciphers.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `cryptography-46.0.6/src/rust/src/backend/hashes.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `cryptography-46.0.6/src/rust/src/backend/kdf.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `cryptography-46.0.6/src/rust/src/backend/kdf.rs`) -> **O(2^N) [Recursive]**
- `_escape_dn_value` (@ `cryptography-46.0.6/src/cryptography/x509/name.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Escape special characters in RFC4514 Distinguished Name value."""
- `matches` (@ `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/types.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Returns true if this `DNSConstraint` matches the given `DNSPattern`.

### Highest Data Gravity (Database Complexity)
- `test_admissions_extension` (@ `cryptography-46.0.6/tests/x509/test_x509.py`) -> DB Complexity: **354**
- `test_repr` (@ `cryptography-46.0.6/tests/x509/test_x509_ext.py`) -> DB Complexity: **273**
- `test_boringssl_vectors` (@ `cryptography-46.0.6/tests/hazmat/primitives/test_aead.py`) -> DB Complexity: **97**
- `test_loads_ssh_cert` (@ `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py`) -> DB Complexity: **36**
- `tests` (@ `cryptography-46.0.6/noxfile.py`) -> DB Complexity: **15**
- `test_no_circular_imports` (@ `cryptography-46.0.6/tests/test_meta.py`) -> DB Complexity: **15**
- `load_nist_ccm_vectors` (@ `cryptography-46.0.6/tests/utils.py`) -> DB Complexity: **14**
- `process_data` (@ `cryptography-46.0.6/src/rust/src/backend/aead.rs`) -> DB Complexity: **14**
- `test_partial_blocks` (@ `cryptography-46.0.6/tests/hazmat/primitives/test_chacha20.py`) -> DB Complexity: **13**
  * *Intent:* # Test that partial blocks and counter increments are handled # correctly. Successive calls to update should return the same # as if the entire input ...
- `_escape_dn_value` (@ `cryptography-46.0.6/src/cryptography/x509/name.py`) -> DB Complexity: **12**
  * *Intent:* """Escape special characters in RFC4514 Distinguished Name value."""

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `cryptography-46.0.6/src/rust/src/backend` | 20 | 16349.16 | 20.14% | 67.94% |
| `cryptography-46.0.6/tests/hazmat/primitives` | 48 | 12370.04 | 5.12% | 0.0% |
| `cryptography-46.0.6/src/rust/src/x509` | 11 | 7962.64 | 16.52% | 24.81% |
| `cryptography-46.0.6/tests/x509` | 7 | 7024.6 | 3.27% | 0.0% |
| `cryptography-46.0.6/src/rust/src` | 11 | 4620.52 | 12.23% | 33.52% |
| `cryptography-46.0.6/src/cryptography/x509` | 9 | 3494.9 | 26.77% | 43.63% |
| `cryptography-46.0.6/tests` | 9 | 2197.12 | 9.9% | 0.0% |
| `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy` | 2 | 1493.54 | 6.34% | 15.69% |
| `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization` | 5 | 1137.86 | 15.22% | 33.1% |
| `cryptography-46.0.6/src/rust/cryptography-x509/src` | 12 | 1009.46 | 3.58% | 9.78% |

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
- `cryptography-46.0.6/src/cryptography/x509/extensions.py` -> **0** Orphaned Functions | **199** Duplicates
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

### Obfuscation & Evasion Surface
- `cryptography-46.0.6/src/rust/cryptography-crypto/src/pkcs12.rs` -> **100.0%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_asym_utils.py` -> **99.72%** Exposure
- `cryptography-46.0.6/tests/hazmat/asn1/test_encoding.py` -> **99.5338%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_padding.py` -> **2.9213%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_hkdf.py` -> **0.0384%** Exposure
### Exploit Generation Surface
- `cryptography-46.0.6/noxfile.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/fernet.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/decrepit/ciphers/algorithms.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/_serialization.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `cryptography-46.0.6/src/_cffi_src/utils.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/certificate.rs` -> **99.9995%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/ops.rs` -> **99.997%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` -> **87.5834%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` -> **51.9221%** Exposure
### Algorithmic DoS Exposure
- `cryptography-46.0.6/noxfile.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/fernet.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/openssl/binding.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/decrepit/ciphers/algorithms.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1899` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cryptography-46.0.6/src/cryptography/x509/general_name.py` (PYTHON) -> Cumulative Risk: **833.59**
- **Archetype:** `file_cluster_0` (Distance: 12.665 IQR)
- **Magnitude:** 321.86 | **LOC:** 282 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 32.2), `__init__` (Impact: 21.5), `__init__` (Impact: 21.5)

### 2. `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON) -> Cumulative Risk: **825.93**
- **Archetype:** `file_cluster_16` (Distance: 12.801 IQR)
- **Magnitude:** 1796.84 | **LOC:** 2529 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 40.8), `__eq__` (Impact: 35.4), `encipher_only` (Impact: 26.3)

### 3. `cryptography-46.0.6/src/rust/cryptography-crypto/src/pkcs12.rs` (RUST) -> Cumulative Risk: **820.04**
- **Archetype:** `file_cluster_0` (Distance: 11.564 IQR)
- **Magnitude:** 213.82 | **LOC:** 141 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Obscured Payload (100.0%), State Flux (99.9923%)
- **Heaviest Functions:** `kdf` (Impact: 166.1), `test_pkcs12_kdf` (Impact: 11.8)

### 4. `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/concatkdf.py` (PYTHON) -> Cumulative Risk: **775.19**
- **Archetype:** `file_cluster_13` (Distance: 11.934 IQR)
- **Magnitude:** 89.52 | **LOC:** 126 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.9998%), Documentation (99.955%)
- **Heaviest Functions:** `verify` (Impact: 8.2), `verify` (Impact: 8.2), `derive` (Impact: 7.3)

### 5. `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` (PYTHON) -> Cumulative Risk: **773.41**
- **Archetype:** `file_cluster_0` (Distance: 11.099 IQR)
- **Magnitude:** 167.3 | **LOC:** 269 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9996%)
- **Heaviest Functions:** `validate_for_algorithm` (Impact: 30.9), `validate_for_algorithm` (Impact: 18.0), `_check_aes_key_length` (Impact: 17.6)

### 6. `cryptography-46.0.6/src/rust/src/backend/ec.rs` (RUST) -> Cumulative Risk: **759.45**
- **Archetype:** `file_cluster_0` (Distance: 12.241 IQR)
- **Magnitude:** 1456.14 | **LOC:** 687 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9161%), Documentation (99.6105%)
- **Heaviest Functions:** `sign` (Impact: 206.4), `exchange` (Impact: 160.6), `verify` (Impact: 154.5)

### 7. `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` (PYTHON) -> Cumulative Risk: **745.03**
- **Archetype:** `file_cluster_16` (Distance: 11.152 IQR)
- **Magnitude:** 941.6 | **LOC:** 1620 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9998%), Tech Debt (99.7375%)
- **Heaviest Functions:** `sign` (Impact: 214.6), `valid_before` (Impact: 42.6), `valid_after` (Impact: 42.6)

### 8. `cryptography-46.0.6/src/rust/src/backend/ciphers.rs` (RUST) -> Cumulative Risk: **739.68**
- **Archetype:** `file_cluster_0` (Distance: 13.021 IQR)
- **Magnitude:** 2055.94 | **LOC:** 619 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.999%), Documentation (99.8791%)
- **Heaviest Functions:** `new` (Impact: 955.4), `create_decryption_ctx` (Impact: 107.5), `update_into` (Impact: 87.5)

### 9. `cryptography-46.0.6/src/cryptography/hazmat/decrepit/ciphers/algorithms.py` (PYTHON) -> Cumulative Risk: **738.55**
- **Archetype:** `file_cluster_0` (Distance: 10.96 IQR)
- **Magnitude:** 70.28 | **LOC:** 113 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 10.7), `__init__` (Impact: 2.7), `key_size` (Impact: 2.7)

### 10. `cryptography-46.0.6/src/cryptography/fernet.py` (PYTHON) -> Cumulative Risk: **737.61**
- **Archetype:** `file_cluster_13` (Distance: 11.501 IQR)
- **Magnitude:** 206.4 | **LOC:** 225 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `_get_unverified_token_data` (Impact: 35.1), `decrypt` (Impact: 30.4), `extract_timestamp` (Impact: 26.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cryptography-46.0.6/tests/x509/test_x509_ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.081 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.944 IQR)
- **Top Global Matches:** file_cluster_8: 11.081, file_cluster_7: 11.714, file_cluster_0: 11.892
- **Magnitude:** 3005.36 | **LOC:** 7507 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 273
- **Risk Profile:** Cognitive Load (2.704%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_repr` (Impact: 1373.2 | O(2^N) | DB: 273)
  * `test_public_bytes` (Impact: 423.0 | O(2^N) | DB: 9)
  * `test_key_agreement_false_encipher_deciph` (Impact: 19.3 | O(N^4))
  * `test_invalid_signature_algorithm` (Impact: 14.4 | O(N^3) | DB: 3)
  * `test_invalid_hash_algorithm` (Impact: 14.3 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 1306`, `args: 480`, `func_start: 470`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 10`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 67`, `orphaned_logic: 36`
* *Architecture:* `io: 114`, `api: 537`, `import: 19`
* *Defense:* `safety: 739`, `doc: 2`, `test: 1344`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` os, .test_x509, binascii, ipaddress, typing, cryptography.hazmat.primitives, cryptography, cryptography.x509.oid...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/aead.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.226 IQR)
- **Top Global Matches:** file_cluster_8: 12.226, file_cluster_0: 12.231, file_cluster_16: 12.323
- **Magnitude:** 2783.16 | **LOC:** 1182 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (13.0778%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process_data` (Impact: 2607.6 | O(2^N) | DB: 14)
  * `new` (Impact: 49.9 | O(2^N) | DB: 2)
  * `process_aad` (Impact: 49.0 | O(N^5) | DB: 1)
  * `check_length` (Impact: 10.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 147`, `args: 51`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 153`, `test: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AesGcm, PyListMethods, super::AesCcm, crate::error::CryptographyError, ChaCha20Poly1305, CryptographyResult, AesOcb3, pyo3::types::PyAnyMethods...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_x509.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.732 IQR)
- **Top Global Matches:** file_cluster_8: 11.398, file_cluster_7: 11.962, file_cluster_0: 11.989
- **Magnitude:** 2489.4 | **LOC:** 6963 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 354
- **Risk Profile:** Cognitive Load (2.9112%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_admissions_extension` (Impact: 1235.4 | O(N^6) | DB: 354)
  * `test_revoked_extensions` (Impact: 45.5 | O(N^6) | DB: 3)
  * `test_revoked_basics` (Impact: 18.4 | O(N^4) | DB: 3)
  * `test_verify_directly_issued_by_rsa_misma` (Impact: 18.0 | O(N^4) | DB: 3)
  * `test_invalid_pem` (Impact: 17.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 988`, `args: 374`, `func_start: 336`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1`, `dead_code: 3`, `duplicate_logic: 18`
* *Architecture:* `io: 226`, `api: 427`, `import: 22`
* *Defense:* `safety: 742`, `doc: 14`, `test: 1116`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.78
  * `Choke Point (Betweenness):` 0.000438 | `Ripple Effect (Closeness):` 0.006369
  * `Imports (Out-Degree: 10):` os, cryptography.exceptions, binascii, ipaddress, cryptography.hazmat.primitives.asymmetric.utils, cryptography.x509.name, typing, copy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/rsa.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.05 IQR)
- **Top Global Matches:** file_cluster_0: 12.05, file_cluster_8: 12.157, file_cluster_16: 12.204
- **Magnitude:** 2322.1 | **LOC:** 834 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (32.815%), Tech Debt (66.6298%)
**Top Internal Functions/Classes:**
  * `setup_signature_ctx` (Impact: 625.9 | O(N^6) | DB: 1)
  * `check_private_key_components` (Impact: 267.3 | O(N^3))
  * `setup_encryption_ctx` (Impact: 246.4 | O(N^5) | DB: 1)
  * `sign` (Impact: 181.3 | O(2^N) | DB: 2)
  * `decrypt` (Impact: 177.5 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 124`, `args: 47`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 73`, `dead_code: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 66`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RsaPrivateKey, RsaPublicKey, Hasher, RsaPrivateNumbers, super::
        generate_private_key, utils, crate::error::CryptographyError, crate::backend::hashes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/utils.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.976 IQR)
- **Top Global Matches:** file_cluster_8: 10.976, file_cluster_16: 11.202, file_cluster_13: 11.349
- **Magnitude:** 2248.2 | **LOC:** 406 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (33.3978%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pkey_private_bytes` (Impact: 1424.5 | O(N^6))
  * `pkey_public_bytes` (Impact: 672.6 | O(N^6) | DB: 2)
  * `calculate_digest_and_algorithm` (Impact: 74.9 | O(N^4) | DB: 1)
  * `py_int_to_bn` (Impact: 20.9 | O(N^2))
  * `as_bytes` (Impact: 14.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 80`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `dead_code: 1`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `safety: 55`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::backend::hashes::Hash, crate::error::CryptographyError, crate::types, CryptographyResult, pyo3::types::PyAnyMethods, PyBytesMethods
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/ciphers.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.021 IQR)
- **Top Global Matches:** file_cluster_0: 13.021, file_cluster_16: 13.089, file_cluster_11: 13.096
- **Magnitude:** 2055.94 | **LOC:** 619 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (41.717%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 955.4 | O(2^N) | DB: 4)
  * `create_decryption_ctx` (Impact: 107.5 | O(N^4) | DB: 1)
  * `update_into` (Impact: 87.5 | O(N^6) | DB: 5)
  * `create_encryption_ctx` (Impact: 80.8 | O(N^4))
  * `finalize_with_tag` (Impact: 76.0 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 103`, `args: 41`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 97`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 19`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CffiMutBuf, PyCipherContext, cipher_supported, crate::backend::cipher_registry, create_encryption_ctx, _advance_aad, create_decryption_ctx, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/extensions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.697 IQR)
- **Top Global Matches:** file_cluster_8: 12.697, file_cluster_16: 12.824, file_cluster_13: 12.913
- **Magnitude:** 1907.8 | **LOC:** 768 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (35.8251%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode_extension` (Impact: 508.9 | O(N^5) | DB: 1)
  * `encode_certificate_policies` (Impact: 278.5 | O(N^6) | DB: 3)
  * `encode_profession_info` (Impact: 244.0 | O(N^6) | DB: 2)
  * `encode_key_usage` (Impact: 154.7 | O(N^4) | DB: 10)
  * `encode_issuing_distribution_point` (Impact: 141.5 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 190`, `args: 17`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 70`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 151`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` extensions, crate::asn1::py_oid_to_oid, py_uint_to_big_endian_bytes, crate::x509::certificate, oid, x509, cryptography_x509::common::Asn1Write, cryptography_x509::crl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/pkcs7.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.364 IQR)
- **Top Global Matches:** file_cluster_8: 11.364, file_cluster_13: 11.502, file_cluster_0: 11.52
- **Magnitude:** 1800.54 | **LOC:** 884 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (16.3246%), Tech Debt (8.5323%)
**Top Internal Functions/Classes:**
  * `sign_and_serialize` (Impact: 545.4 | O(N^6) | DB: 4)
  * `decrypt_der` (Impact: 349.4 | O(N^6) | DB: 1)
  * `encrypt_and_serialize` (Impact: 328.4 | O(N^4) | DB: 1)
  * `check_decrypt_parameters` (Impact: 201.2 | O(N^5))
  * `load_der_pkcs7_certificates` (Impact: 43.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 161`, `args: 26`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 24`
* *Defense:* `safety: 59`, `test: 7`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::ops::Deref, crate::backend::ciphers, AlgorithmParameters, load_der_pkcs7_certificates, load_pem_pkcs7_certificates, pyo3::types::PyAnyMethods, sign_and_serialize, openssl::pkcs7::Pkcs7...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.801 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.074 IQR)
- **Top Global Matches:** file_cluster_16: 12.801, file_cluster_0: 12.828, file_cluster_11: 13.031
- **Magnitude:** 1796.84 | **LOC:** 2529 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (77.3502%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 40.8 | O(N^4) | DB: 2)
  * `__eq__` (Impact: 35.4 | O(N^3) | DB: 9)
  * `encipher_only` (Impact: 26.3 | O(2^N))
  * `decipher_only` (Impact: 26.3 | O(2^N))
  * `_validate_ip_name` (Impact: 22.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 765`, `args: 309`, `func_start: 309`, `class_start: 48`
* *Risk/State:* `state_mutation: 388`, `dead_code: 1`, `duplicate_logic: 199`
* *Architecture:* `api: 186`, `import: 18`
* *Defense:* `safety: 117`, `doc: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.427
  * `Choke Point (Betweenness):` 0.000634 | `Ripple Effect (Closeness):` 0.015605
  * `Imports (Out-Degree: 8):` datetime, cryptography.x509.name, typing, __future__, cryptography.x509.general_name, cryptography.hazmat.primitives.asymmetric.types, cryptography.x509.oid, hashlib...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/pkcs12.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.393 IQR)
- **Top Global Matches:** file_cluster_8: 12.393, file_cluster_0: 12.457, file_cluster_16: 12.565
- **Magnitude:** 1649.46 | **LOC:** 830 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (19.8496%), Tech Debt (10.9201%)
**Top Internal Functions/Classes:**
  * `serialize_key_and_certificates` (Impact: 493.7 | O(N^6) | DB: 3)
  * `serialize_safebags` (Impact: 217.8 | O(N^6) | DB: 4)
  * `decode_encryption_algorithm` (Impact: 216.2 | O(N^4))
  * `load_pkcs12` (Impact: 148.5 | O(N^4))
  * `encrypt` (Impact: 137.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 150`, `args: 31`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `import: 14`
* *Defense:* `safety: 124`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::backend::ciphers, crate::padding::PKCS7PaddingContext, hashes, crate::types, serialize_java_truststore, pyo3::IntoPyObject, std::hash::Hash, pyo3::types::PyAnyMethods...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.188 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.793 IQR)
- **Top Global Matches:** file_cluster_8: 11.188, file_cluster_13: 11.334, file_cluster_0: 11.508
- **Magnitude:** 1468.08 | **LOC:** 977 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (14.9628%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_hash_vectors` (Impact: 433.4 | O(N^5) | DB: 10)
  * `load_kasvs_dh_vectors` (Impact: 293.7 | O(N^5) | DB: 3)
  * `load_rfc6979_vectors` (Impact: 167.0 | O(N^4) | DB: 7)
  * `load_fips_dsa_sig_vectors` (Impact: 156.0 | O(N^5) | DB: 4)
  * `load_nist_ccm_vectors` (Impact: 105.5 | O(N^4) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 118`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 99`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 37`, `import: 10`
* *Defense:* `safety: 17`, `doc: 20`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006369
  * `Imports (Out-Degree: 1):` os, json, typing, re, cryptography.exceptions, binascii, pytest, contextlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/ec.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.241 IQR)
- **Top Global Matches:** file_cluster_0: 12.241, file_cluster_16: 12.437, file_cluster_11: 12.455
- **Magnitude:** 1456.14 | **LOC:** 687 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (40.8491%), Tech Debt (99.9161%)
**Top Internal Functions/Classes:**
  * `sign` (Impact: 206.4 | O(N^6) | DB: 1)
  * `exchange` (Impact: 160.6 | O(2^N) | DB: 1)
  * `verify` (Impact: 154.5 | O(2^N) | DB: 1)
  * `private_key` (Impact: 109.5 | O(2^N) | DB: 3)
  * `new` (Impact: 109.0 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 145`, `args: 45`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 108`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 12`, `orphaned_logic: 7`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 40`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ECPublicKey, ECPrivateKey, derive_private_key, Hasher, from_public_bytes, EllipticCurvePrivateNumbers, crate::backend::utils, crate::error::CryptographyError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.842 IQR)
- **Top Global Matches:** file_cluster_8: 11.842, file_cluster_16: 11.849, file_cluster_0: 11.886
- **Magnitude:** 1258.78 | **LOC:** 1046 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (16.3059%), Tech Debt (16.9752%)
**Top Internal Functions/Classes:**
  * `certificates` (Impact: 982.8 | O(N^6) | DB: 6)
  * `response_status` (Impact: 73.1 | O(2^N))
  * `load_der_ocsp_response` (Impact: 37.2 | O(N^6))
  * `signature_hash_algorithm` (Impact: 31.1 | O(N^5))
  * `responses` (Impact: 21.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 160`, `args: 65`, `func_start: 55`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 115`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` SingleResponse, ocsp, std::sync::Arc, pyo3::types::PyAnyMethods, crate::x509::certificate, cryptography_x509::common, PyListMethods, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_aead.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.276 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.536 IQR)
- **Top Global Matches:** file_cluster_8: 10.276, file_cluster_0: 10.649, file_cluster_13: 10.882
- **Magnitude:** 1216.1 | **LOC:** 1060 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 97
- **Risk Profile:** Cognitive Load (6.0754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_boringssl_vectors` (Impact: 864.6 | O(N^6) | DB: 97)
  * `test_vectors_invalid` (Impact: 55.6 | O(N^5) | DB: 3)
  * `test_openssl_vectors` (Impact: 43.1 | O(N^6) | DB: 3)
  * `test_vectors` (Impact: 37.6 | O(N^5) | DB: 3)
  * `test_bad_key` (Impact: 26.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 152`, `args: 67`, `func_start: 67`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 40`, `api: 77`, `import: 10`
* *Defense:* `safety: 59`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` os, cryptography.hazmat.primitives.ciphers.aead, mmap, ...utils, .utils, cryptography.exceptions, binascii, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/common.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.579 IQR)
- **Top Global Matches:** file_cluster_16: 11.579, file_cluster_8: 11.658, file_cluster_13: 11.829
- **Magnitude:** 1155.18 | **LOC:** 558 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (25.4658%), Tech Debt (8.2965%)
**Top Internal Functions/Classes:**
  * `encode_general_name` (Impact: 280.2 | O(N^5))
  * `encode_name_entry` (Impact: 208.5 | O(N^6))
  * `parse_general_name` (Impact: 158.4 | O(N^5))
  * `parse_name_attribute` (Impact: 91.9 | O(N^5))
  * `py_to_datetime` (Impact: 61.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 93`, `args: 27`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `safety: 62`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DuplicateExtensionsError, pyo3::types::IntoPyDict, NameReadable, cryptography_x509::extensions::
    AccessDescription, Extensions, RawTlv, Name, Extension...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.713 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.65 IQR)
- **Top Global Matches:** file_cluster_8: 10.713, file_cluster_0: 11.16, file_cluster_7: 11.323
- **Magnitude:** 1147.78 | **LOC:** 1975 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (4.0083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_loads_ssh_cert` (Impact: 278.4 | O(N^4) | DB: 36)
  * `test_load_ssh_public_key` (Impact: 145.0 | O(N^6) | DB: 6)
  * `test_load_ssh_private_key` (Impact: 130.3 | O(N^6) | DB: 6)
  * `test_dsa_private_key_sizes` (Impact: 48.0 | O(N^6) | DB: 3)
  * `test_ssh_errors_pubpriv_mismatch` (Impact: 28.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 254`, `args: 146`, `func_start: 98`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 43`
* *Architecture:* `io: 28`, `api: 108`, `import: 14`
* *Defense:* `safety: 131`, `doc: 2`, `test: 338`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .fixtures_rsa, datetime, os, ...utils, cryptography.hazmat.primitives.serialization, ...doubles, cryptography.exceptions, base64...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/extension.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.852 IQR)
- **Top Global Matches:** file_cluster_16: 11.852, file_cluster_13: 11.907, file_cluster_8: 12.02
- **Magnitude:** 1131.9 | **LOC:** 938 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (9.1782%), Tech Debt (8.1058%)
**Top Internal Functions/Classes:**
  * `permits` (Impact: 1042.0 | O(2^N) | DB: 10)
  * `new_default_webpki_ee` (Impact: 10.7 | O(N^4))
  * `new_default_webpki_ca` (Impact: 5.8 | O(N^4))
  * `new_permit_all` (Impact: 5.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 123`, `args: 31`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 30`, `concurrency: 4`, `import: 28`
* *Defense:* `safety: 130`, `doc: 12`, `test: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SimpleAsn1Writable, std::sync::Arc, cryptography_x509::extensions::
        AuthorityKeyIdentifier, crate::ValidationError, Extensions, SUBJECT_ALTERNATIVE_NAME_OID, NameConstraints, ExtendedKeyUsage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ec.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.332 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.944 IQR)
- **Top Global Matches:** file_cluster_8: 10.332, file_cluster_0: 10.872, file_cluster_13: 10.949
- **Magnitude:** 1079.74 | **LOC:** 1582 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (3.2234%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_key_exchange_with_vectors` (Impact: 93.9 | O(N^6) | DB: 3)
  * `test_deterministic_nonce` (Impact: 66.6 | O(N^6) | DB: 3)
  * `test_signature_failures` (Impact: 43.4 | O(N^6) | DB: 3)
  * `test_load_invalid_ec_key_from_pem` (Impact: 35.7 | O(N^4))
  * `test_derive_point_at_infinity` (Impact: 28.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 210`, `args: 117`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `io: 43`, `api: 168`, `import: 18`
* *Defense:* `safety: 96`, `doc: 6`, `test: 245`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.000682 | `Ripple Effect (Closeness):` 0.020382
  * `Imports (Out-Degree: 5):` os, typing, .utils, ...utils, copy, cryptography, ...doubles, .fixtures_ec...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/kdf.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.458 IQR)
- **Top Global Matches:** file_cluster_0: 11.458, file_cluster_8: 11.632, file_cluster_13: 11.815
- **Magnitude:** 1047.68 | **LOC:** 686 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (12.0788%), Tech Debt (92.1788%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 203.7 | O(2^N))
  * `new` (Impact: 171.3 | O(2^N))
  * `new` (Impact: 137.2 | O(2^N))
  * `new` (Impact: 115.2 | O(2^N))
  * `verify_phc_encoded` (Impact: 93.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 117`, `args: 37`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `dead_code: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 77`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::buf::CffiBuf, base64::engine::general_purpose::STANDARD_NO_PAD, cryptography_crypto::constant_time, super::Scrypt, super::HkdfExpand, base64::engine::Engine, crate::backend::hmac::Hmac, crate::error::CryptographyError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/sign.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.595 IQR)
- **Top Global Matches:** file_cluster_8: 11.595, file_cluster_16: 11.882, file_cluster_13: 11.97
- **Magnitude:** 1038.4 | **LOC:** 668 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (13.9689%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compute_signature_algorithm` (Impact: 882.2 | O(N^6) | DB: 1)
  * `compute_pss_salt_length` (Impact: 91.2 | O(N^3))
  * `identify_hash_type` (Impact: 46.3 | O(N^3))
    * *Intent:* #[derive(Debug, PartialEq)]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 44`, `args: 31`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 106`, `test: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.283
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009554
  * `Imports (Out-Degree: 0):` KeyType, identify_key_type_for_algorithm_params, pyo3::pybacked::PyBackedBytes, oid, std::collections::HashMap, once_cell::sync::Lazy, cryptography_x509::common, types...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.836 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.267 IQR)
- **Top Global Matches:** file_cluster_8: 10.836, file_cluster_0: 11.128, file_cluster_7: 11.413
- **Magnitude:** 1036.1 | **LOC:** 1847 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (2.7776%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_skip_fips_format` (Impact: 35.9 | O(N^4))
  * `test_dh_public_key` (Impact: 32.7 | O(N^5) | DB: 3)
  * `test_dh_private_key` (Impact: 32.5 | O(N^5) | DB: 3)
  * `test_invalid_encoding_with_traditional` (Impact: 16.4 | O(N^5) | DB: 3)
  * `test_invalid_kdf_rounds` (Impact: 14.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 231`, `args: 189`, `func_start: 97`, `class_start: 10`
* *Risk/State:* `dead_code: 1`, `duplicate_logic: 35`, `orphaned_logic: 61`
* *Architecture:* `io: 81`, `api: 107`, `import: 16`
* *Defense:* `safety: 122`, `doc: 16`, `test: 323`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` os, cryptography.hazmat.primitives.hashes, .utils, ...utils, cryptography.hazmat.primitives.serialization, cryptography.hazmat.primitives.serialization.pkcs12, cryptography.hazmat.primitives.ciphers, base64...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_rsa.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.14 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.483 IQR)
- **Top Global Matches:** file_cluster_8: 10.14, file_cluster_0: 10.567, file_cluster_7: 10.778
- **Magnitude:** 1031.22 | **LOC:** 2798 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (3.3665%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_invalid_oaep_decryption_data_to_lar` (Impact: 177.6 | O(N^5))
  * `test_decrypt_oaep_sha2_vectors` (Impact: 36.5 | O(N^6))
  * `_build_oaep_sha2_vectors` (Impact: 27.6 | O(N^5) | DB: 7)
  * `test_pss_signing` (Impact: 23.2 | O(N^6) | DB: 3)
  * `test_generate_rsa_keys` (Impact: 23.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 262`, `args: 196`, `func_start: 123`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`, `dead_code: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 33`, `api: 203`, `import: 14`
* *Defense:* `safety: 100`, `doc: 2`, `test: 384`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .fixtures_rsa, os, .utils, ...utils, copy, ...doubles, cryptography.exceptions, binascii...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.684 IQR)
- **Top Global Matches:** file_cluster_16: 11.152, file_cluster_8: 11.209, file_cluster_13: 11.413
- **Magnitude:** 941.6 | **LOC:** 1620 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.242%), Tech Debt (99.7375%)
**Top Internal Functions/Classes:**
  * `sign` (Impact: 214.6 | O(2^N) | DB: 3)
  * `valid_before` (Impact: 42.6 | O(2^N))
  * `valid_after` (Impact: 42.6 | O(2^N))
  * `_parse_exts_opts` (Impact: 35.9 | O(N^4))
  * `serial` (Impact: 35.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 214`, `args: 86`, `func_start: 84`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 72`, `dead_code: 1`, `duplicate_logic: 42`
* *Architecture:* `io: 3`, `api: 73`, `import: 17`
* *Defense:* `safety: 49`, `doc: 102`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.58
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.003185
  * `Imports (Out-Degree: 2):` os, typing, __future__, cryptography.hazmat.primitives.serialization, re, enum, warnings, cryptography.exceptions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/x509/crl.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.472 IQR)
- **Top Global Matches:** file_cluster_0: 12.472, file_cluster_16: 12.567, file_cluster_8: 12.619
- **Magnitude:** 912.26 | **LOC:** 710 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (21.3607%), Tech Debt (50.7022%)
**Top Internal Functions/Classes:**
  * `create_x509_crl` (Impact: 229.4 | O(N^4) | DB: 1)
  * `extensions` (Impact: 153.9 | O(N^5))
  * `__getitem__` (Impact: 93.6 | O(N^4) | DB: 3)
  * `parse_crl_entry_ext` (Impact: 57.1 | O(N^3))
  * `get_revoked_certificate_by_serial_number` (Impact: 45.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 105`, `args: 49`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 29`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 19`, `import: 13`
* *Defense:* `safety: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std::sync::Arc, PySliceMethods, sign, cryptography_x509::crl::
    self, Asn1Read, cryptography_x509::certificate::SerialNumber, pyo3::types::PyAnyMethods, cryptography_x509::extensions::Extension...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_ocsp.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.321 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.104 IQR)
- **Top Global Matches:** file_cluster_8: 10.321, file_cluster_7: 11.029, file_cluster_13: 11.128
- **Magnitude:** 904.86 | **LOC:** 1762 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (3.093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_load_unauthorized` (Impact: 82.2 | O(N^3) | DB: 3)
  * `test_invalid_add_response` (Impact: 53.5 | O(N^4))
  * `test_multi_valued_responses` (Impact: 45.5 | O(N^6) | DB: 12)
  * `test_add_response_by_hash_bad_hash` (Impact: 24.3 | O(N^4))
  * `test_add_cert_by_hash_bad_hash` (Impact: 22.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 254`, `args: 90`, `func_start: 83`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 74`
* *Architecture:* `io: 41`, `api: 85`, `import: 16`
* *Defense:* `safety: 142`, `test: 318`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` datetime, os, typing, cryptography.x509, .test_x509, cryptography.hazmat.primitives.asymmetric.padding, cryptography.hazmat.backends.openssl.backend, ..hazmat.primitives.fixtures_ec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `cryptography-46.0.6/src/rust/src/x509/verify/mod.rs` (RUST) | Magnitude: 462.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 373, structural_boundaries: 83, generics: 73, safety: 68
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/dsa.py` (PYTHON) | Magnitude: 32.84 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 37, doc: 32, api: 22
- `cryptography-46.0.6/src/cryptography/hazmat/asn1/asn1.py` (PYTHON) | Magnitude: 29.62 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 25, branch: 12, generics: 12
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/padding.py` (PYTHON) | Magnitude: 45.42 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, encapsulation: 31, structural_boundaries: 30, state_mutation: 14
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/utils.py` (PYTHON) | Magnitude: 17.18 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, encapsulation: 6, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cryptography-46.0.6/src/cryptography/x509/name.py` (PYTHON) | Magnitude: 808.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 296, encapsulation: 154, structural_boundaries: 106, branch: 66
- `cryptography-46.0.6/tests/hazmat/primitives/test_poly1305.py` (PYTHON) | Magnitude: 133.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 104, test: 36, structural_boundaries: 26, state_mutation: 20
- `cryptography-46.0.6/tests/wycheproof/test_aes.py` (PYTHON) | Magnitude: 151.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 108, branch: 32, structural_boundaries: 29, test: 26
- `cryptography-46.0.6/src/_cffi_src/openssl/engine.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 8, dead_code: 5, structural_boundaries: 2, import: 1
- `cryptography-46.0.6/tests/hazmat/primitives/test_camellia.py` (PYTHON) | Magnitude: 20.32 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 13, args: 12, closures: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/ec.py` (PYTHON) | Magnitude: 89.54 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 260, structural_boundaries: 82, api: 55, doc: 38
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/__init__.pyi` (PYTHON) | Magnitude: 76.9 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 14, api: 12, generics: 10
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/ops.rs` (RUST) | Magnitude: 75.58 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 23, generics: 22, args: 15
- `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON) | Magnitude: 1796.84 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1855, structural_boundaries: 765, encapsulation: 500, generics: 419
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/declarative_asn1.pyi` (PYTHON) | Magnitude: 9.6 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 13, api: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cryptography-46.0.6/src/rust/src/backend/aead.rs` (RUST) | Magnitude: 2783.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 944, branch: 160, safety: 153, generics: 148
- `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs` (RUST) | Magnitude: 1258.78 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 811, generics: 184, branch: 168, structural_boundaries: 160
- `cryptography-46.0.6/src/rust/src/x509/ocsp_req.rs` (RUST) | Magnitude: 265.16 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 173, structural_boundaries: 33, branch: 32, generics: 25
- `cryptography-46.0.6/tests/hazmat/primitives/test_hash_vectors.py` (PYTHON) | Magnitude: 56.98 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 30, test: 22, args: 19
- `cryptography-46.0.6/src/rust/src/x509/verify/extension_policy.rs` (RUST) | Magnitude: 202.54 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 208, structural_boundaries: 40, generics: 36, safety: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/asn1.pyi` (PYTHON) | Magnitude: 24.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: generics: 4, structural_boundaries: 3, args: 3, func_start: 3
- `cryptography-46.0.6/src/_cffi_src/openssl/cryptography.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 8, dead_code: 7, structural_boundaries: 2, import: 1
- `cryptography-46.0.6/src/_cffi_src/openssl/ssl.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 17, doc: 8, structural_boundaries: 2, import: 1
- `cryptography-46.0.6/src/rust/cryptography-crypto/src/constant_time.rs` (RUST) | Magnitude: 6.62 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_6`
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

- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 15.497** (Embedded: 0.1937 * Error Risk: 80.0%)
- `cryptography-46.0.6/tests/doubles.py` -> **Severity: 4.78** (Embedded: 0.0645 * Error Risk: 74.1176%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 0.472** (Embedded: 0.0706 * Error Risk: 6.6907%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/algorithms.py` -> **Severity: 0.461** (Embedded: 0.0487 * Error Risk: 9.4816%)
- `cryptography-46.0.6/src/cryptography/hazmat/decrepit/ciphers/algorithms.py` -> **Severity: 0.442** (Embedded: 0.0432 * Error Risk: 10.2457%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 6184.039** (Blast Radius: 61.842 * Doc Risk: 99.9974%)
- `cryptography-46.0.6/src/cryptography/utils.py` -> **Severity: 4269.262** (Blast Radius: 42.693 * Doc Risk: 99.9991%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 1848.699** (Blast Radius: 18.491 * Doc Risk: 99.9783%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/_cipheralgorithm.py` -> **Severity: 1777.341** (Blast Radius: 17.857 * Doc Risk: 99.5319%)
- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **Severity: 1420.9** (Blast Radius: 14.209 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
