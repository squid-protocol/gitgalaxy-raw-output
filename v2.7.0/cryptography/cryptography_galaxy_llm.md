# ARCHITECTURAL_BRIEF: cryptography
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
| Total Artifacts | 349 |
| Analyzed Artifacts (Scanned) | 316 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 33 |
| Total LOC | 74113 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5163 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1549 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1657 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 26 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 235 | 53442 | 74.4% |
| RUST | 81 | 20671 | 25.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 316 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 33*

**Composition by Extension & Reason:**
- `.rs`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 10x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.apache`: 1x Excluded (Unsupported Extension: '.APACHE')
- `.bsd`: 1x Excluded (Unsupported Extension: '.BSD')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.9 | 5.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 46.7 | 55.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.6 | 10.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 82.1 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 18.7 | 14.5 | 30.8 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 77.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 67.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1810 | 118 | 17 | `cryptography-46.0.6/tests/test_utils.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 4982 | 186 | 25 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| danger | 1034 | 115 | 6 | `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/types.rs` |
| concurrency | 28 | 11 | 0 | `cryptography-46.0.6/src/cryptography/x509/name.py` |
| connectivity | 5101 | 264 | 32 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| io | 933 | 61 | 4 | `cryptography-46.0.6/tests/x509/test_x509.py` |
| crypto | 136 | 73 | 1 | `cryptography-46.0.6/src/cryptography/x509/__init__.py` |
| ipc | 4 | 2 | 0 | `cryptography-46.0.6/release.py` |
| time | 476 | 16 | 0 | `cryptography-46.0.6/tests/x509/test_x509.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 12 | 5 | 0 | `cryptography-46.0.6/src/cryptography/x509/name.py` |
| events | 0 | 0 | 0 | - |
| tests | 4864 | 127 | 33 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| docs | 627 | 85 | 4 | `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/types.rs` |
| debt | 360 | 57 | 2 | `cryptography-46.0.6/src/cryptography/x509/extensions.py` |
| mutation | 20330 | 252 | 132 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| dead_code | 1716 | 311 | 10 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| credential | 50 | 12 | 0 | `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` |
| threat | 382 | 59 | 2 | `cryptography-46.0.6/src/cryptography/x509/extensions.py` |
| ml_ai | 81 | 8 | 0 | `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` |
| ui | 3 | 1 | 0 | `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

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

- `pkey_private_bytes` (@ `cryptography-46.0.6/src/rust/src/backend/utils.rs`) -> Impact: **334.1** | LOC: 203
- `create_ocsp_response` (@ `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs`) -> Impact: **169.8** | LOC: 211
- `get_cipher_registry` (@ `cryptography-46.0.6/src/rust/src/backend/cipher_registry.rs`) -> Impact: **165.9** | LOC: 207
- `pkey_public_bytes` (@ `cryptography-46.0.6/src/rust/src/backend/utils.rs`) -> Impact: **161.3** | LOC: 115
- `setup_signature_ctx` (@ `cryptography-46.0.6/src/rust/src/backend/rsa.rs`) -> Impact: **154.3** | LOC: 122
- `parse_cert_ext` (@ `cryptography-46.0.6/src/rust/src/x509/certificate.rs`) -> Impact: **151.0** | LOC: 179
- `encode_extension` (@ `cryptography-46.0.6/src/rust/src/x509/extensions.rs`) -> Impact: **145.2** | LOC: 184
- `sign_and_serialize` (@ `cryptography-46.0.6/src/rust/src/pkcs7.rs`) -> Impact: **123.9** | LOC: 198
- `serialize_key_and_certificates` (@ `cryptography-46.0.6/src/rust/src/pkcs12.rs`) -> Impact: **117.3** | LOC: 123
- `new` (@ `cryptography-46.0.6/src/rust/src/backend/ciphers.rs`) -> Impact: **112.4** | LOC: 101

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cryptography-46.0.6/tests/hazmat/primitives` | 48 | 8831.34 | 12.48% | 0.0% |
| `cryptography-46.0.6/tests/x509` | 7 | 5915.1 | 7.71% | 0.0% |
| `cryptography-46.0.6/src/rust/src/backend` | 20 | 4491.36 | 14.21% | 48.82% |
| `cryptography-46.0.6/src/rust/src/x509` | 11 | 3540.9 | 17.16% | 11.13% |
| `cryptography-46.0.6/src/cryptography/x509` | 9 | 3497.1 | 32.8% | 28.49% |
| `cryptography-46.0.6/tests` | 10 | 1866.22 | 9.87% | 0.0% |
| `cryptography-46.0.6/src/rust/src` | 11 | 1798.14 | 10.22% | 24.71% |
| `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization` | 5 | 1393.96 | 23.33% | 0.0% |
| `cryptography-46.0.6/src/rust/cryptography-x509/src` | 12 | 801.26 | 1.83% | 2.14% |
| `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric` | 12 | 778.74 | 21.68% | 40.09% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/__init__.pyi` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/ocsp.pyi` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/aead.pyi` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/ec.pyi` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/openssl/kdf.pyi` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cryptography-46.0.6/src/_cffi_src/utils.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/_oid.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/asn1/asn1.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/decrepit/ciphers/algorithms.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/_serialization.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cryptography-46.0.6/tests/x509/test_x509_ext.py` -> **170** Orphaned Functions | **0** Duplicates
- `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` -> **92** Orphaned Functions | **0** Duplicates
- `cryptography-46.0.6/src/cryptography/x509/extensions.py` -> **0** Orphaned Functions | **89** Duplicates
- `cryptography-46.0.6/tests/hazmat/primitives/test_pkcs7.py` -> **78** Orphaned Functions | **0** Duplicates
- `cryptography-46.0.6/tests/x509/test_ocsp.py` -> **75** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` -> **100.0%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/certificate.rs` -> **99.9996%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/ops.rs` -> **99.9977%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` -> **87.5834%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` -> **51.9221%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1902` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON) -> Cumulative Risk: **773.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1989.64 | **LOC:** 2529 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9939%), Tech Debt (99.9878%), Documentation (99.5546%)
- **Heaviest Functions:** `__init__` (Impact: 73.2), `__init__` (Impact: 66.5), `__init__` (Impact: 34.0)

### 2. `cryptography-46.0.6/src/cryptography/hazmat/decrepit/ciphers/algorithms.py` (PYTHON) -> Cumulative Risk: **733.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 78.28 | **LOC:** 113 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 5.5), `__init__` (Impact: 1.8), `__init__` (Impact: 1.8)

### 3. `cryptography-46.0.6/src/cryptography/x509/general_name.py` (PYTHON) -> Cumulative Risk: **729.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 191.86 | **LOC:** 282 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9854%), State Flux (99.9783%), Documentation (96.2963%)
- **Heaviest Functions:** `__init__` (Impact: 9.7), `__init__` (Impact: 6.4), `__init__` (Impact: 6.0)

### 4. `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/concatkdf.py` (PYTHON) -> Cumulative Risk: **721.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 123.12 | **LOC:** 126 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.6498%)
- **Heaviest Functions:** `__init__` (Impact: 19.7), `__init__` (Impact: 8.0), `_common_args_checks` (Impact: 6.5)

### 5. `cryptography-46.0.6/src/cryptography/hazmat/primitives/keywrap.py` (PYTHON) -> Cumulative Risk: **719.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 189.94 | **LOC:** 178 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.1969%)
- **Heaviest Functions:** `aes_key_unwrap_with_padding` (Impact: 26.2), `aes_key_unwrap` (Impact: 13.1), `aes_key_wrap_with_padding` (Impact: 11.2)

### 6. `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` (PYTHON) -> Cumulative Risk: **715.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 182.7 | **LOC:** 269 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9966%), State Flux (99.9375%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 21.4), `validate_for_algorithm` (Impact: 12.7), `_check_aes_key_length` (Impact: 8.9)

### 7. `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/algorithms.py` (PYTHON) -> Cumulative Risk: **709.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 63.92 | **LOC:** 137 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.975%)
- **Heaviest Functions:** `__init__` (Impact: 4.4), `__init__` (Impact: 1.8), `__init__` (Impact: 1.8)

### 8. `cryptography-46.0.6/src/cryptography/hazmat/bindings/openssl/binding.py` (PYTHON) -> Cumulative Risk: **675.94**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 66.1 | **LOC:** 138 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9775%), Safety Score (85.6927%)
- **Heaviest Functions:** `build_conditional_library` (Impact: 9.5), `_verify_package_version` (Impact: 6.9), `_openssl_assert` (Impact: 3.5)

### 9. `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/padding.py` (PYTHON) -> Cumulative Risk: **670.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 78.42 | **LOC:** 112 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.131%)
- **Heaviest Functions:** `__init__` (Impact: 12.9), `calculate_max_pss_salt_length` (Impact: 5.7), `__init__` (Impact: 5.1)

### 10. `cryptography-46.0.6/src/cryptography/x509/name.py` (PYTHON) -> Cumulative Risk: **668.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 393.02 | **LOC:** 477 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.7941%), Documentation (90.566%)
- **Heaviest Functions:** `__init__` (Impact: 41.8), `__init__` (Impact: 14.8), `_read_re` (Impact: 10.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cryptography-46.0.6/tests/x509/test_x509_ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2650.96 | **LOC:** 7507 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.28%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fullname_and_crl_issuer` (Impact: 6.5)
  * `test_public_bytes` (Impact: 6.4)
  * `test_ne` (Impact: 6.1)
  * `test_non_ascii_qualifier` (Impact: 5.8)
  * `test_relativename_and_crl_issuer` (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 929
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 1445`, `args: 480`, `func_start: 470`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 917`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 170`
* *Architecture:* `io: 114`, `api: 537`, `import: 19`
* *Defense:* `safety: 738`, `doc: 1`, `test: 614`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ..hazmat.primitives.test_ec, ..hazmat.primitives.test_rsa, ..utils, .test_x509, binascii, cryptography, cryptography.hazmat._oid, cryptography.hazmat.bindings._rust...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_x509.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2223.2 | **LOC:** 6963 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3644%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_build_cert` (Impact: 9.3)
  * `test_subject_dn_asn1_types` (Impact: 8.6)
  * `test_revoked_extensions` (Impact: 8.2)
  * `test_build_cert_with_ec_private_key` (Impact: 7.8)
  * `_generate_ca_and_leaf` (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 1176`, `args: 374`, `func_start: 336`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 744`, `dead_code: 3`
* *Architecture:* `io: 226`, `api: 358`, `import: 22`
* *Defense:* `safety: 742`, `doc: 7`, `test: 549`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.774
  * `Choke Point (Betweenness):` 0.000435 | `Ripple Effect (Closeness):` 0.006349
  * `Imports (Out-Degree: 10):` ..hazmat.primitives.fixtures_dsa, ..hazmat.primitives.fixtures_ec, ..hazmat.primitives.fixtures_rsa, ..hazmat.primitives.test_ec, ..hazmat.primitives.test_rsa, ..utils, binascii, copy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1989.64 | **LOC:** 2529 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.6101%), Tech Debt (99.9878%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 73.2)
  * `__init__` (Impact: 66.5)
  * `__init__` (Impact: 34.0)
  * `__init__` (Impact: 33.9)
  * `__init__` (Impact: 27.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 766`, `args: 309`, `func_start: 309`, `class_start: 48`
* *Risk/State:* `state_mutation: 252`, `dead_code: 1`, `duplicate_logic: 89`
* *Architecture:* `api: 181`, `import: 18`
* *Defense:* `safety: 114`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.42
  * `Choke Point (Betweenness):` 0.00063 | `Ripple Effect (Closeness):` 0.015556
  * `Imports (Out-Degree: 8):` __future__, abc, collections.abc, cryptography, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric.ec, cryptography.hazmat.primitives.asymmetric.rsa...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1320.98 | **LOC:** 977 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.9432%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_pkcs1_vectors` (Impact: 59.8)
    * *Intent:* """ Loads data out of RSA PKCS #1 vector files. """
  * `load_kasvs_ecdh_vectors` (Impact: 54.7)
    * *Intent:* """ Loads data out of the KASVS key exchange vector data """
  * `load_rsa_nist_vectors` (Impact: 32.5)
  * `load_kasvs_dh_vectors` (Impact: 32.3)
    * *Intent:* """ Loads data out of the KASVS key exchange vector data """
  * `load_fips_dsa_sig_vectors` (Impact: 31.0)
    * *Intent:* """ Loads data out of the FIPS DSA SigVer vector files. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 838
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 121`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 292`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 28`, `import: 10`
* *Defense:* `safety: 17`, `doc: 10`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006349
  * `Imports (Out-Degree: 1):` binascii, collections, contextlib, cryptography.exceptions, cryptography_vectors, json, os, pytest...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1019.9 | **LOC:** 1620 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.8884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_ssh_private_key` (Impact: 54.8)
  * `sign` (Impact: 48.4)
  * `_load_ssh_public_identity` (Impact: 37.6)
  * `_serialize_ssh_private_key` (Impact: 19.8)
  * `valid_principals` (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 215`, `args: 86`, `func_start: 84`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 219`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 66`, `import: 17`
* *Defense:* `safety: 46`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.575
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.003175
  * `Imports (Out-Degree: 2):` __future__, base64, bcrypt, binascii, cryptography, cryptography.exceptions, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_rsa.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 887.12 | **LOC:** 2798 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2686%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_generate_rsa_keys` (Impact: 9.5)
  * `test_decrypt_oaep_sha2_vectors` (Impact: 9.5)
  * `test_rsa_encrypt_oaep_sha2` (Impact: 8.4)
  * `_build_oaep_sha2_vectors` (Impact: 6.6)
  * `test_pss_signing` (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 360`, `args: 196`, `func_start: 123`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 301`, `dead_code: 1`
* *Architecture:* `io: 33`, `api: 136`, `import: 14`
* *Defense:* `safety: 100`, `doc: 1`, `test: 291`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ...doubles, ...utils, .fixtures_rsa, .utils, binascii, copy, cryptography.exceptions, cryptography.hazmat.primitives...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 802.98 | **LOC:** 1975 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9721%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_file` (Impact: 32.2)
  * `test_load_ssh_public_key` (Impact: 28.7)
  * `test_load_ssh_private_key` (Impact: 28.4)
  * `test_dsa_private_key_sizes` (Impact: 7.8)
  * `test_invalid_signature` (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 377`, `args: 146`, `func_start: 98`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 256`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 92`
* *Architecture:* `io: 28`, `api: 108`, `import: 14`
* *Defense:* `safety: 131`, `doc: 1`, `test: 240`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ...doubles, ...utils, .fixtures_rsa, .test_ec, .test_rsa, base64, cryptography, cryptography.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_aead.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 757.0 | **LOC:** 1060 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.5722%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_vectors` (Impact: 13.3)
  * `test_boringssl_vectors` (Impact: 13.2)
  * `test_vectors` (Impact: 11.6)
  * `test_vectors_invalid` (Impact: 11.6)
  * `test_vectors` (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 424
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 250`, `args: 67`, `func_start: 67`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 298`, `dead_code: 1`
* *Architecture:* `io: 40`, `api: 71`, `import: 10`
* *Defense:* `safety: 59`, `test: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ...utils, .utils, binascii, cryptography.exceptions, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives.ciphers.aead, mmap, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/certificate.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 731.54 | **LOC:** 1091 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.133%), Tech Debt (66.2712%)
**Top Internal Functions/Classes:**
  * `parse_cert_ext` (Impact: 151.0)
  * `create_x509_certificate` (Impact: 75.4)
  * `parse_profession_infos` (Impact: 30.0)
  * `parse_user_notice` (Impact: 21.8)
  * `parse_policy_qualifiers` (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 177`, `args: 48`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 16`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 19`
* *Architecture:* `api: 20`, `import: 15`
* *Defense:* `safety: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Admissions, Asn1Read, Asn1ReadableOrWritable, AuthorityKeyIdentifier, BasicConstraints, CryptographyResult, DisplayText, DistributionPoint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/rsa.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 667.48 | **LOC:** 834 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.6933%), Tech Debt (24.6237%)
**Top Internal Functions/Classes:**
  * `setup_signature_ctx` (Impact: 154.3)
  * `check_private_key_components` (Impact: 97.2)
  * `setup_encryption_ctx` (Impact: 70.0)
  * `private_numbers` (Impact: 32.5)
  * `private_key` (Impact: 30.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 134`, `args: 45`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 4`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, Hasher, RsaPrivateKey, RsaPrivateNumbers, RsaPublicKey, RsaPublicNumbers, crate::backend::hashes, crate::buf::CffiBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 652.34 | **LOC:** 1582 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.7465%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_key_exchange_with_vectors` (Impact: 22.9)
  * `test_deterministic_nonce` (Impact: 17.6)
  * `test_load_invalid_ec_key_from_pem` (Impact: 11.8)
  * `test_derive_point_at_infinity` (Impact: 10.7)
  * `test_signature_failures` (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 280`, `args: 117`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `state_mutation: 210`, `dead_code: 1`
* *Architecture:* `io: 43`, `api: 90`, `import: 18`
* *Defense:* `safety: 96`, `doc: 3`, `test: 165`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.488
  * `Choke Point (Betweenness):` 0.000677 | `Ripple Effect (Closeness):` 0.020317
  * `Imports (Out-Degree: 5):` ...doubles, ...utils, .fixtures_ec, .utils, binascii, copy, cryptography, cryptography.hazmat.bindings._rust...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/x509/extensions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 642.24 | **LOC:** 768 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.7624%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode_extension` (Impact: 145.2)
  * `encode_certificate_policies` (Impact: 65.2)
  * `encode_profession_info` (Impact: 61.3)
  * `encode_issuing_distribution_point` (Impact: 56.6)
  * `encode_key_usage` (Impact: 50.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 192`, `args: 16`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CryptographyResult, crate::asn1::py_oid_to_oid, crate::error::CryptographyError, crate::types, crate::x509::certificate, cryptography_x509::certificate::SerialNumber, cryptography_x509::common::Asn1Write, cryptography_x509::crl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/pkcs12.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 594.54 | **LOC:** 830 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.4968%), Tech Debt (10.9253%)
**Top Internal Functions/Classes:**
  * `serialize_key_and_certificates` (Impact: 117.3)
  * `decode_encryption_algorithm` (Impact: 69.6)
  * `serialize_safebags` (Impact: 60.5)
  * `load_pkcs12` (Impact: 52.2)
  * `encrypt` (Impact: 45.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 150`, `args: 30`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 28`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 2`, `import: 14`
* *Defense:* `safety: 19`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, Hasher, PKCS12Certificate, PyBytesMethods, PyListMethods, PyTypeInfo, crate::backend::ciphers, crate::buf::CffiBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_pkcs7.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 585.92 | **LOC:** 1520 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.6772%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_smime_encrypt_smime_encoding` (Impact: 12.2)
  * `test_smime_encrypt_der_encoding` (Impact: 11.7)
  * `test_smime_encrypt_pem_encoding` (Impact: 11.1)
  * `test_rsa_pkcs_padding_options` (Impact: 8.7)
  * `test_load_pkcs7_der` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 265`, `args: 121`, `func_start: 87`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 185`, `dead_code: 1`, `unreferenced_by_name: 78`
* *Architecture:* `io: 26`, `api: 95`, `import: 17`
* *Defense:* `safety: 82`, `doc: 1`, `test: 161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ...hazmat.primitives.fixtures_rsa, ...hazmat.primitives.test_rsa, ...utils, contextlib, cryptography, cryptography.exceptions, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_ocsp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 564.16 | **LOC:** 1762 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_ocsp_response_times` (Impact: 12.5)
  * `test_multi_valued_responses` (Impact: 8.7)
  * `test_invalid_add_response` (Impact: 7.3)
  * `_generate_root` (Impact: 4.8)
  * `test_load_response` (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 355`, `args: 90`, `func_start: 83`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 218`, `dead_code: 1`, `unreferenced_by_name: 75`
* *Architecture:* `io: 41`, `api: 85`, `import: 16`
* *Defense:* `safety: 142`, `test: 185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ..hazmat.primitives.fixtures_ec, ..utils, .test_x509, base64, cryptography, cryptography.exceptions, cryptography.hazmat.backends.openssl.backend, cryptography.hazmat.primitives...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/utils.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 560.4 | **LOC:** 406 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.4204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pkey_private_bytes` (Impact: 334.1)
  * `pkey_public_bytes` (Impact: 161.3)
  * `calculate_digest_and_algorithm` (Impact: 25.4)
  * `py_int_to_bn` (Impact: 11.1)
  * `bn_to_py_int` (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 80`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `dead_code: 1`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptographyResult, PyBytesMethods, crate::backend::hashes::Hash, crate::error::CryptographyError, crate::types, pyo3::types::PyAnyMethods
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 544.1 | **LOC:** 1847 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.4658%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_skip_fips_format` (Impact: 14.8)
  * `test_dh_public_key` (Impact: 10.2)
  * `test_dh_private_key` (Impact: 10.0)
  * `test_rsa_traditional_encrypted_values` (Impact: 5.3)
  * `test_rsa_pkcs8_encrypted_values` (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 312`, `args: 189`, `func_start: 97`, `class_start: 10`
* *Risk/State:* `state_mutation: 136`, `dead_code: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 61`
* *Architecture:* `io: 81`, `api: 107`, `import: 16`
* *Defense:* `safety: 122`, `doc: 8`, `test: 229`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ...utils, .test_ec, .test_rsa, .utils, base64, cryptography.hazmat.bindings._rust, cryptography.hazmat.decrepit.ciphers.algorithms, cryptography.hazmat.primitives.asymmetric...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/pkcs7.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 540.52 | **LOC:** 884 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.5332%), Tech Debt (8.5532%)
**Top Internal Functions/Classes:**
  * `sign_and_serialize` (Impact: 123.9)
  * `encrypt_and_serialize` (Impact: 100.6)
  * `decrypt_der` (Impact: 82.2)
  * `check_decrypt_parameters` (Impact: 43.5)
  * `symmetric_decrypt` (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 160`, `args: 25`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 24`
* *Defense:* `safety: 4`, `test: 7`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AlgorithmParameters, CryptographyResult, PyBytesMethods, PyListMethods, crate::asn1::encode_der_data, crate::backend::ciphers, crate::buf::CffiBuf, crate::error::CryptographyError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 517.38 | **LOC:** 1046 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.8572%), Tech Debt (30.7102%)
**Top Internal Functions/Classes:**
  * `create_ocsp_response` (Impact: 169.8)
  * `response_status` (Impact: 21.9)
  * `single_extensions` (Impact: 15.4)
  * `certificates` (Impact: 12.2)
  * `load_der_ocsp_response` (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 162`, `args: 71`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 5`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 9`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CryptographyResult, OCSPResponse, PyBytesMethods, PyListMethods, SingleResponse, crate::asn1::big_byte_slice_to_py_int, crate::error::CryptographyError, crate::exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/aead.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 516.44 | **LOC:** 1182 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1086%), Tech Debt (17.7846%)
**Top Internal Functions/Classes:**
  * `decrypt_with_context` (Impact: 44.5)
  * `encrypt_with_context` (Impact: 44.2)
  * `decrypt` (Impact: 28.8)
  * `encrypt` (Impact: 26.0)
  * `process_data` (Impact: 22.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 159`, `args: 46`, `func_start: 38`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 10`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AesGcm, AesGcmSiv, AesOcb3, AesSiv, ChaCha20Poly1305, CryptographyResult, PyListMethods, crate::buf::CffiBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/cryptography/x509/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 493.62 | **LOC:** 849 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.7977%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sign` (Impact: 42.1)
  * `sign` (Impact: 33.6)
  * `sign` (Impact: 28.2)
  * `add_attribute` (Impact: 17.2)
  * `not_valid_after` (Impact: 13.6)
    * *Intent:* """ Sets the certificate expiration time. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 127`, `args: 50`, `func_start: 50`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 58`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 46`, `import: 15`
* *Defense:* `safety: 30`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.916
  * `Choke Point (Betweenness):` 0.00017 | `Ripple Effect (Closeness):` 0.006349
  * `Imports (Out-Degree: 5):` __future__, abc, collections.abc, cryptography, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.asymmetric.types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/ciphers.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 457.42 | **LOC:** 619 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.3318%), Tech Debt (99.1112%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 112.4)
  * `create_decryption_ctx` (Impact: 33.7)
  * `create_encryption_ctx` (Impact: 25.4)
  * `finalize_with_tag` (Impact: 24.2)
  * `update_into` (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 103`, `args: 41`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 23`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 9`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CffiMutBuf, CryptographyResult, PyAEADDecryptionContext, PyAEADEncryptionContext, PyCipherContext, _advance_aad, cipher_supported, crate::backend::cipher_registry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_dh.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 446.2 | **LOC:** 991 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.705%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dh_parameters_allows_rfc3526_groups` (Impact: 13.2)
  * `test_dh_vectors` (Impact: 10.8)
  * `test_public_bytes` (Impact: 10.3)
  * `test_bad_exchange` (Impact: 9.3)
  * `test_private_bytes_values` (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 187`, `args: 63`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `state_mutation: 163`, `dead_code: 2`, `unreferenced_by_name: 44`
* *Architecture:* `io: 48`, `api: 50`, `import: 11`
* *Defense:* `safety: 103`, `doc: 1`, `test: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ...doubles, ...utils, .fixtures_dh, binascii, copy, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/common.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 440.74 | **LOC:** 558 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.0806%), Tech Debt (8.2994%)
**Top Internal Functions/Classes:**
  * `encode_general_name` (Impact: 78.4)
  * `encode_name_entry` (Impact: 50.8)
  * `parse_general_name` (Impact: 45.7)
  * `py_to_datetime` (Impact: 32.3)
  * `parse_name_attribute` (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 93`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AttributeTypeValue, AttributeValue, CryptographyResult, DuplicateExtensionsError, Extension, Extensions, Name, NameReadable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 410.8 | **LOC:** 566 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.1892%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `aead_test` (Impact: 18.6)
  * `generate_aead_test` (Impact: 10.5)
  * `generate_rsa_verification_test` (Impact: 10.4)
  * `_kbkdf_cmac_counter_mode_test` (Impact: 9.0)
  * `test_rsa_verification` (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 144`, `args: 44`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 40`, `import: 13`
* *Defense:* `safety: 45`, `doc: 1`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ...utils, binascii, cryptography.exceptions, cryptography.hazmat.decrepit.ciphers, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.ciphers, cryptography.hazmat.primitives.ciphers.modes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **Severity: 0.125** (Bridge: 0.002 * Flux: 64.1632%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/ec.py` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 99.9768%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/algorithms.py` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 99.975%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 99.9375%)
- `cryptography-46.0.6/src/cryptography/x509/extensions.py` -> **Severity: 0.063** (Bridge: 0.0006 * Flux: 99.9939%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 17.573** (Embedded: 0.1931 * Error Risk: 91.0053%)
- `cryptography-46.0.6/src/_cffi_src/openssl/cryptography.py` -> **Severity: 10.616** (Embedded: 0.1634 * Error Risk: 64.9568%)
- `cryptography-46.0.6/src/cryptography/utils.py` -> **Severity: 8.43** (Embedded: 0.0903 * Error Risk: 93.3529%)
- `cryptography-46.0.6/tests/doubles.py` -> **Severity: 5.643** (Embedded: 0.0643 * Error Risk: 87.7764%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 5.362** (Embedded: 0.0704 * Error Risk: 76.2059%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 6171.8** (Blast Radius: 61.718 * Doc Risk: 100.0%)
- `cryptography-46.0.6/src/cryptography/utils.py` -> **Severity: 4260.7** (Blast Radius: 42.607 * Doc Risk: 100.0%)
- `cryptography-46.0.6/tests/doubles.py` -> **Severity: 1422.6** (Blast Radius: 14.226 * Doc Risk: 100.0%)
- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **Severity: 1373.081** (Blast Radius: 14.181 * Doc Risk: 96.8254%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/ciphers/modes.py` -> **Severity: 1353.293** (Blast Radius: 18.454 * Doc Risk: 73.3333%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
