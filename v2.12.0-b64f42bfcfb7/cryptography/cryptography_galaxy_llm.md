# ARCHITECTURAL_BRIEF: cryptography
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 328 analyzed artifact(s), 75108 LOC.
- **Load-bearing artifact:** `cryptography-46.0.6/src/cryptography/hazmat/primitives/__init__.py` -- 86 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `cryptography-46.0.6/src/rust/src/lib.rs` -- pulls in 93 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cryptography-46.0.6/tests/x509/test_x509_ext.py` at magnitude 2650.96 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 349 |
| Analyzed Artifacts (Scanned) | 328 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21 |
| Total LOC | 75108 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5712 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2586 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3058 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 235 | 53442 | 71.6% |
| RUST | 93 | 21666 | 28.4% |

## 4.1 SOURCE ENCODINGS
All 328 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 27%, Data / Markup / Trivial 21%, Large Core Modules (2) 12%, Declarative / Non-Code 11%, Parameter Forwarders Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 328 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21*

**Composition by Extension & Reason:**
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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.7 | 6.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.0 | 40.4 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.0 | 11.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 82.1 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.7 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 916 | 72 | 3 | `cryptography-46.0.6/tests/test_utils.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 5012 | 193 | 23 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| danger | 1052 | 119 | 6 | `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/types.rs` |
| concurrency | 29 | 12 | 0 | `cryptography-46.0.6/src/cryptography/x509/name.py` |
| connectivity | 5246 | 273 | 32 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| io | 933 | 61 | 3 | `cryptography-46.0.6/tests/x509/test_x509.py` |
| crypto | 533 | 176 | 5 | `cryptography-46.0.6/src/cryptography/x509/extensions.py` |
| ipc | 5 | 3 | 0 | `cryptography-46.0.6/release.py` |
| time | 476 | 16 | 0 | `cryptography-46.0.6/tests/x509/test_x509.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 12 | 5 | 0 | `cryptography-46.0.6/src/cryptography/x509/name.py` |
| events | 0 | 0 | 0 | - |
| tests | 4877 | 131 | 31 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| docs | 631 | 87 | 4 | `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/types.rs` |
| debt | 392 | 63 | 2 | `cryptography-46.0.6/src/cryptography/x509/extensions.py` |
| mutation | 20404 | 260 | 126 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| dead_code | 1329 | 121 | 9 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| credential | 51 | 12 | 0 | `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` |
| threat | 292 | 21 | 0 | `cryptography-46.0.6/tests/x509/test_x509_ext.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 3 | 1 | 0 | `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.9616**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cryptography-46.0.6/tests/x509/test_x509.py` (Hits: 226)
- `cryptography-46.0.6/tests/x509/test_x509_ext.py` (Hits: 114)
- `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` (Hits: 81)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`cryptography-46.0.6/src/cryptography/hazmat/primitives/__init__.py`) — 86 inbound connections
2. **exceptions.py** (`cryptography-46.0.6/src/cryptography/exceptions.py`) — 61 inbound connections
3. **utils.py** (`cryptography-46.0.6/tests/utils.py`) — 53 inbound connections
4. **__init__.py** (`cryptography-46.0.6/src/cryptography/__init__.py`) — 45 inbound connections
5. **__init__.py** (`cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/__init__.py`) — 40 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`cryptography-46.0.6/src/rust/src/lib.rs`) — 93 outbound dependencies
2. **mod.rs** (`cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/mod.rs`) — 65 outbound dependencies
3. **certificate.rs** (`cryptography-46.0.6/src/rust/src/x509/certificate.rs`) — 54 outbound dependencies
4. **extension.rs** (`cryptography-46.0.6/src/rust/cryptography-x509-verification/src/policy/extension.rs`) — 39 outbound dependencies
5. **pkcs7.rs** (`cryptography-46.0.6/src/rust/src/pkcs7.rs`) — 37 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pkey_private_bytes` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/backend/utils.rs`) -> Impact: **322.1** | LOC: 203
- `create_ocsp_response` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs`) -> Impact: **167.3** | LOC: 211
- `get_cipher_registry` **(Compute Cores)** (@ `cryptography-46.0.6/src/rust/src/backend/cipher_registry.rs`) -> Impact: **165.9** | LOC: 207
- `pkey_public_bytes` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/backend/utils.rs`) -> Impact: **161.3** | LOC: 115
- `parse_cert_ext` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/x509/certificate.rs`) -> Impact: **151.0** | LOC: 179
- `setup_signature_ctx` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/backend/rsa.rs`) -> Impact: **146.3** | LOC: 122
- `encode_extension` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/x509/extensions.rs`) -> Impact: **145.2** | LOC: 184
- `sign_and_serialize` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/pkcs7.rs`) -> Impact: **123.9** | LOC: 198
- `serialize_key_and_certificates` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/pkcs12.rs`) -> Impact: **114.6** | LOC: 123
- `new` **(Many-Argument Workhorses)** (@ `cryptography-46.0.6/src/rust/src/backend/ciphers.rs`) -> Impact: **112.4** | LOC: 101

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cryptography-46.0.6/tests/hazmat/primitives` | 48 | 8832.74 | 12.48% | 0.0% |
| `cryptography-46.0.6/tests/x509` | 7 | 5915.1 | 7.71% | 0.0% |
| `cryptography-46.0.6/src/rust/src/backend` | 20 | 4478.46 | 13.97% | 32.16% |
| `cryptography-46.0.6/src/rust/src/x509` | 11 | 3536.4 | 17.02% | 3.86% |
| `cryptography-46.0.6/src/cryptography/x509` | 9 | 3497.1 | 32.8% | 33.42% |
| `cryptography-46.0.6/tests` | 10 | 1866.22 | 9.87% | 0.0% |
| `cryptography-46.0.6/src/rust/src` | 12 | 1847.46 | 9.94% | 6.2% |
| `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization` | 5 | 1388.96 | 23.33% | 13.81% |
| `cryptography-46.0.6/src/rust/cryptography-x509/src` | 13 | 828.56 | 1.69% | 1.97% |
| `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric` | 12 | 778.74 | 21.68% | 39.71% |

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
- `cryptography-46.0.6/src/cryptography/hazmat/bindings/_rust/x509.pyi` -> **51** Orphaned Functions | **36** Duplicates
- `cryptography-46.0.6/tests/hazmat/primitives/test_pkcs7.py` -> **78** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/ops.rs` -> **99.9977%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` -> **99.2548%** Exposure
- `cryptography-46.0.6/src/rust/cryptography-x509-verification/src/certificate.rs` -> **99.0918%** Exposure
- `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` -> **52.3975%** Exposure
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` -> **18.8232%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2013` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cryptography-46.0.6/tests/x509/test_x509_ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.469)
- **Top Global Matches:** file_cluster_15: 7.469, file_cluster_11: 8.973, file_cluster_12: 9.103
- **Magnitude:** 2650.96 | **LOC:** 7507 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 1.2; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.8%), Connectivity (formerly Api Exposure) (14.1%), Complexity Load (formerly Cognitive Load) (10.3%)
- **Documentation Coverage:** 99.7872% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_fullname_and_crl_issuer` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `test_public_bytes` **(I/O & Config Routines)** (Impact: 6.4)
  * `test_ne` **(I/O & Config Routines)** (Impact: 6.1)
  * `test_non_ascii_qualifier` **(Many-Argument Workhorses)** (Impact: 5.8)
  * `test_relativename_and_crl_issuer` **(Many-Argument Workhorses)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 929
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 1445`, `args: 480`, `func_start: 470`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 917`, `planned_debt: 2`, `unreferenced_by_name: 170`
* *Architecture:* `io: 114`, `api: 537`, `import: 19`
* *Defense:* `safety: 738`, `doc: 1`, `test: 614`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` ..hazmat.primitives.test_ec, ..hazmat.primitives.test_rsa, ..utils, .test_x509, binascii, cryptography, cryptography.hazmat._oid, cryptography.hazmat.bindings._rust...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_x509.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.503)
- **Top Global Matches:** file_cluster_15: 6.503, file_cluster_10: 8.116, file_cluster_16: 8.197
- **Magnitude:** 2223.2 | **LOC:** 6963 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **22**; blast radius 1.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.5%), Complexity Load (formerly Cognitive Load) (9.4%)
- **Documentation Coverage:** 98.503% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_build_cert` **(Many-Argument Workhorses)** (Impact: 9.3)
  * `test_subject_dn_asn1_types` **(Many-Argument Workhorses)** (Impact: 8.6)
  * `test_revoked_extensions` **(Defensive Guards)** (Impact: 8.2)
  * `test_build_cert_with_ec_private_key` **(Many-Argument Workhorses)** (Impact: 7.8)
  * `_generate_ca_and_leaf` **(Stateful Encapsulated Methods)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 1176`, `args: 374`, `func_start: 336`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 744`
* *Architecture:* `io: 226`, `api: 358`, `import: 22`
* *Defense:* `safety: 742`, `doc: 7`, `test: 549`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.635
  * `Choke Point (Betweenness):` 0.000865 | `Ripple Effect (Closeness):` 0.015291
  * `Imports (Out-Degree: 21):` ..hazmat.primitives.fixtures_dsa, ..hazmat.primitives.fixtures_ec, ..hazmat.primitives.fixtures_rsa, ..hazmat.primitives.test_ec, ..hazmat.primitives.test_rsa, ..utils, binascii, copy...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/cryptography/x509/extensions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.079)
- **Top Global Matches:** file_cluster_0: 8.079, file_cluster_16: 11.15, file_cluster_13: 11.729
- **Magnitude:** 1989.64 | **LOC:** 2529 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **17**; blast radius 2.191; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (91.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.5546% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 73.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 66.5)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 34.0)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 33.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 27.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 766`, `args: 309`, `func_start: 309`, `class_start: 48`
* *Risk/State:* `state_mutation: 252`, `duplicate_logic: 89`
* *Architecture:* `api: 181`, `import: 18`
* *Defense:* `safety: 114`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.191
  * `Choke Point (Betweenness):` 0.0012 | `Ripple Effect (Closeness):` 0.026464
  * `Imports (Out-Degree: 9):` __future__, abc, collections.abc, cryptography, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric.ec, cryptography.hazmat.primitives.asymmetric.rsa...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.316)
- **Top Global Matches:** file_cluster_6: 11.316, file_cluster_8: 13.161, file_cluster_4: 17.663
- **Magnitude:** 1320.98 | **LOC:** 977 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **53** in-repo importer(s); it depends on **10**; blast radius 17.556; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (92.0%), Connectivity (formerly Api Exposure) (89.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.9%)
- **Documentation Coverage:** 62.963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_pkcs1_vectors` **(Compute Cores)** (Impact: 59.8)
    * *Intent:* """ Loads data out of RSA PKCS #1 vector files. """
  * `load_kasvs_ecdh_vectors` **(Compute Cores)** (Impact: 54.7)
    * *Intent:* """ Loads data out of the KASVS key exchange vector data """
  * `load_rsa_nist_vectors` **(Type Conversions)** (Impact: 32.5)
  * `load_kasvs_dh_vectors` **(Type Conversions)** (Impact: 32.3)
    * *Intent:* """ Loads data out of the KASVS key exchange vector data """
  * `load_fips_dsa_sig_vectors` **(Compute Cores)** (Impact: 31.0)
    * *Intent:* """ Loads data out of the FIPS DSA SigVer vector files. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 838
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 121`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 292`
* *Architecture:* `io: 2`, `api: 28`, `import: 10`
* *Defense:* `safety: 17`, `doc: 10`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.556
  * `Choke Point (Betweenness):` 0.000147 | `Ripple Effect (Closeness):` 0.17129
  * `Imports (Out-Degree: 1):` binascii, collections, contextlib, cryptography.exceptions, cryptography_vectors, json, os, pytest...
  * `Imported By (In-Degree: 53):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.349)
- **Top Global Matches:** file_cluster_0: 8.349, file_cluster_4: 9.194, file_cluster_5: 9.211
- **Magnitude:** 1019.9 | **LOC:** 1620 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **16**; blast radius 2.172; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%), Complexity Load (formerly Cognitive Load) (54.9%)
- **Documentation Coverage:** 78.9116% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_ssh_private_key` **(Many-Argument Workhorses)** (Impact: 54.8)
  * `sign` **(Many-Argument Workhorses)** (Impact: 48.4)
  * `_load_ssh_public_identity` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `_serialize_ssh_private_key` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `valid_principals` **(Compute Cores)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 215`, `args: 86`, `func_start: 84`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 219`
* *Architecture:* `io: 3`, `api: 66`, `import: 17`
* *Defense:* `safety: 46`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.172
  * `Choke Point (Betweenness):` 0.001088 | `Ripple Effect (Closeness):` 0.017793
  * `Imports (Out-Degree: 15):` __future__, base64, bcrypt, binascii, cryptography, cryptography.exceptions, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_rsa.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.868)
- **Top Global Matches:** file_cluster_15: 6.868, file_cluster_10: 7.982, file_cluster_13: 8.188
- **Magnitude:** 887.12 | **LOC:** 2798 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **13**; blast radius 1.76; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.2%), Complexity Load (formerly Cognitive Load) (10.3%)
- **Documentation Coverage:** 99.1736% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_generate_rsa_keys` **(Defensive Guards)** (Impact: 9.5)
  * `test_decrypt_oaep_sha2_vectors` **(Many-Argument Workhorses)** (Impact: 9.5)
  * `test_rsa_encrypt_oaep_sha2` **(Defensive Guards)** (Impact: 8.4)
  * `_build_oaep_sha2_vectors` **(I/O & Config Routines)** (Impact: 6.6)
  * `test_pss_signing` **(Many-Argument Workhorses)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 360`, `args: 196`, `func_start: 123`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 301`
* *Architecture:* `io: 33`, `api: 136`, `import: 14`
* *Defense:* `safety: 100`, `doc: 1`, `test: 291`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.76
  * `Choke Point (Betweenness):` 0.000616 | `Ripple Effect (Closeness):` 0.022519
  * `Imports (Out-Degree: 9):` ...doubles, ...utils, .fixtures_rsa, .utils, binascii, copy, cryptography.exceptions, cryptography.hazmat.primitives...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ssh.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.164)
- **Top Global Matches:** file_cluster_15: 7.164, file_cluster_10: 7.482, file_cluster_12: 8.674
- **Magnitude:** 802.98 | **LOC:** 1975 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.2; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (99.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.3%), Complexity Load (formerly Cognitive Load) (18.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_file` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `test_load_ssh_public_key` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `test_load_ssh_private_key` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `test_dsa_private_key_sizes` **(Defensive Guards)** (Impact: 7.8)
  * `test_invalid_signature` **(Defensive Guards)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 377`, `args: 146`, `func_start: 98`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 256`, `planned_debt: 2`, `unreferenced_by_name: 92`
* *Architecture:* `io: 28`, `api: 108`, `import: 14`
* *Defense:* `safety: 131`, `doc: 1`, `test: 240`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` ...doubles, ...utils, .fixtures_rsa, .test_ec, .test_rsa, base64, cryptography, cryptography.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/hazmat/primitives/test_aead.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.87)
- **Top Global Matches:** file_cluster_15: 5.87, file_cluster_16: 7.732, file_cluster_13: 7.879
- **Magnitude:** 757.0 | **LOC:** 1060 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 1.659; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (76.3%), Guard Balance (formerly Safety Score) (57.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_vectors` **(Defensive Guards)** (Impact: 13.3)
  * `test_boringssl_vectors` **(Defensive Guards)** (Impact: 13.2)
  * `test_vectors` **(Defensive Guards)** (Impact: 11.6)
  * `test_vectors_invalid` **(Many-Argument Workhorses)** (Impact: 11.6)
  * `test_vectors` **(Many-Argument Workhorses)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 424
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 250`, `args: 67`, `func_start: 67`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 298`
* *Architecture:* `io: 40`, `api: 71`, `import: 10`
* *Defense:* `safety: 59`, `test: 173`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.659
  * `Choke Point (Betweenness):` 0.000553 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 5):` ...utils, .utils, binascii, cryptography.exceptions, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives.ciphers.aead, mmap, os...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/x509/certificate.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.609)
- **Top Global Matches:** file_cluster_4: 8.609, file_cluster_0: 10.026, file_cluster_16: 11.54
- **Magnitude:** 734.94 | **LOC:** 1091 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **54**; blast radius 2.267; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (41.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_cert_ext` **(Many-Argument Workhorses)** (Impact: 151.0)
  * `create_x509_certificate` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `parse_profession_infos` **(Defensive Guards)** (Impact: 30.0)
  * `parse_user_notice` **(Defensive Guards)** (Impact: 21.8)
  * `parse_admissions` **(Defensive Guards)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 177`, `args: 48`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 16`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 34`, `import: 15`
* *Defense:* `safety: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.267
  * `Choke Point (Betweenness):` 0.001809 | `Ripple Effect (Closeness):` 0.039633
  * `Imports (Out-Degree: 17):` crate::asn1::big_byte_slice_to_py_int, crate::asn1::encode_der_data, crate::asn1::oid_to_py_oid, crate::asn1::py_uint_to_big_endian_bytes, crate::backend::hashes, crate::backend::keys, crate::error::CryptographyError, crate::error::CryptographyResult...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/rsa.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.434)
- **Top Global Matches:** file_cluster_4: 10.434, file_cluster_6: 10.664, file_cluster_5: 14.12
- **Magnitude:** 654.58 | **LOC:** 834 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 1.266; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (34.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup_signature_ctx` **(Many-Argument Workhorses)** (Impact: 146.3)
  * `check_private_key_components` **(Many-Argument Workhorses)** (Impact: 97.2)
  * `setup_encryption_ctx` **(Many-Argument Workhorses)** (Impact: 70.0)
  * `private_numbers` **(Compute Cores)** (Impact: 32.5)
  * `private_key` **(Many-Argument Workhorses)** (Impact: 30.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 134`, `args: 45`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.266
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.006116
  * `Imports (Out-Degree: 6):` crate::backend::hashes, crate::backend::utils, crate::buf::CffiBuf, crate::error::CryptographyError, crate::error::CryptographyResult, crate::exceptions, crate::types, pyo3::types::PyAnyMethods...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_ec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.181)
- **Top Global Matches:** file_cluster_15: 7.181, file_cluster_10: 7.7, file_cluster_16: 8.398
- **Magnitude:** 652.74 | **LOC:** 1582 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **17**; blast radius 1.724; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (81.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.3%), Complexity Load (formerly Cognitive Load) (16.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_key_exchange_with_vectors` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `test_deterministic_nonce` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `test_load_invalid_ec_key_from_pem` **(Compute Cores)** (Impact: 11.8)
  * `test_derive_point_at_infinity` **(Compute Cores)** (Impact: 10.7)
  * `test_signature_failures` **(Many-Argument Workhorses)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 280`, `args: 117`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `state_mutation: 210`
* *Architecture:* `io: 43`, `api: 90`, `import: 18`
* *Defense:* `safety: 96`, `doc: 3`, `test: 165`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.000721 | `Ripple Effect (Closeness):` 0.020642
  * `Imports (Out-Degree: 11):` ...doubles, ...utils, .fixtures_ec, .utils, binascii, copy, cryptography, cryptography.hazmat.bindings._rust...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/x509/extensions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.889)
- **Top Global Matches:** file_cluster_8: 12.889, file_cluster_3: 14.656, file_cluster_6: 24.578
- **Magnitude:** 642.24 | **LOC:** 768 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **15**; blast radius 1.523; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Mutation Surface (formerly State Flux) (51.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_extension` **(Many-Argument Workhorses)** (Impact: 145.2)
  * `encode_certificate_policies` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `encode_profession_info` **(Many-Argument Workhorses)** (Impact: 61.3)
  * `encode_issuing_distribution_point` **(Compute Cores)** (Impact: 56.6)
  * `encode_key_usage` **(Compute Cores)** (Impact: 50.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 192`, `args: 16`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.523
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.030025
  * `Imports (Out-Degree: 11):` crate::asn1::py_oid_to_oid, crate::asn1::py_uint_to_big_endian_bytes, crate::error::CryptographyError, crate::error::CryptographyResult, crate::types, crate::x509, crate::x509::certificate, crate::x509::sct...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/pkcs12.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.101)
- **Top Global Matches:** file_cluster_8: 7.101, file_cluster_6: 14.144, file_cluster_4: 22.623
- **Magnitude:** 594.84 | **LOC:** 830 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 1.279; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize_key_and_certificates` **(Many-Argument Workhorses)** (Impact: 114.6)
  * `decode_encryption_algorithm` **(Compute Cores)** (Impact: 69.6)
  * `serialize_safebags` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `load_pkcs12` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `encrypt` **(Many-Argument Workhorses)** (Impact: 45.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 150`, `args: 30`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 28`
* *Architecture:* `api: 5`, `import: 14`
* *Defense:* `safety: 19`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.279
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.006116
  * `Imports (Out-Degree: 14):` crate::backend::ciphers, crate::backend::hashes, crate::backend::hmac, crate::backend::kdf, crate::backend::keys, crate::buf::CffiBuf, crate::error::CryptographyError, crate::error::CryptographyResult...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_pkcs7.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.954)
- **Top Global Matches:** file_cluster_12: 6.954, file_cluster_15: 7.868, file_cluster_10: 8.31
- **Magnitude:** 586.12 | **LOC:** 1520 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.2; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.9%), Complexity Load (formerly Cognitive Load) (13.7%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_smime_encrypt_smime_encoding` **(Defensive Guards)** (Impact: 12.2)
  * `test_smime_encrypt_der_encoding` **(Defensive Guards)** (Impact: 11.7)
  * `test_smime_encrypt_pem_encoding` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `test_rsa_pkcs_padding_options` **(Defensive Guards)** (Impact: 8.7)
  * `test_load_pkcs7_der` **(Defensive Guards)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 265`, `args: 121`, `func_start: 87`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 185`, `unreferenced_by_name: 78`
* *Architecture:* `io: 26`, `api: 95`, `import: 17`
* *Defense:* `safety: 82`, `doc: 1`, `test: 161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ...hazmat.primitives.fixtures_rsa, ...hazmat.primitives.test_rsa, ...utils, contextlib, cryptography, cryptography.exceptions, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/tests/x509/test_ocsp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.113)
- **Top Global Matches:** file_cluster_15: 7.113, file_cluster_16: 8.414, file_cluster_10: 8.6
- **Magnitude:** 564.16 | **LOC:** 1762 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.2; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.7%), Connectivity (formerly Api Exposure) (11.4%), Complexity Load (formerly Cognitive Load) (10.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_ocsp_response_times` **(Stateful Encapsulated Methods)** (Impact: 12.5)
  * `test_multi_valued_responses` **(Defensive Guards)** (Impact: 8.7)
  * `test_invalid_add_response` **(I/O & Config Routines)** (Impact: 7.3)
  * `_generate_root` **(Stateful Encapsulated Methods)** (Impact: 4.8)
  * `test_load_response` **(Defensive Guards)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 355`, `args: 90`, `func_start: 83`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 218`, `unreferenced_by_name: 75`
* *Architecture:* `io: 41`, `api: 85`, `import: 16`
* *Defense:* `safety: 142`, `test: 185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ..hazmat.primitives.fixtures_ec, ..utils, .test_x509, base64, cryptography, cryptography.exceptions, cryptography.hazmat.backends.openssl.backend, cryptography.hazmat.primitives...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/backend/utils.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.794)
- **Top Global Matches:** file_cluster_8: 7.794, file_cluster_6: 13.774, file_cluster_4: 22.087
- **Magnitude:** 548.4 | **LOC:** 406 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **6**; blast radius 3.069; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.0%), Complexity Load (formerly Cognitive Load) (29.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pkey_private_bytes` **(Many-Argument Workhorses)** (Impact: 322.1)
  * `pkey_public_bytes` **(Many-Argument Workhorses)** (Impact: 161.3)
  * `calculate_digest_and_algorithm` **(Stateful Encapsulated Methods)** (Impact: 25.4)
  * `py_int_to_bn` **(Stateful Encapsulated Methods)** (Impact: 11.1)
  * `bn_to_py_int` **(Stateful Encapsulated Methods)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 80`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.069
  * `Choke Point (Betweenness):` 0.0001 | `Ripple Effect (Closeness):` 0.027801
  * `Imports (Out-Degree: 3):` crate::backend::hashes::Hash, crate::error::CryptographyError, crate::error::CryptographyResult, crate::types, pyo3::types::PyAnyMethods, pyo3::types::PyBytesMethods
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_serialization.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.369)
- **Top Global Matches:** file_cluster_10: 7.369, file_cluster_15: 7.977, file_cluster_13: 9.126
- **Magnitude:** 544.1 | **LOC:** 1847 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.2; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (52.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.7%), Connectivity (formerly Api Exposure) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_skip_fips_format` **(Stateful Encapsulated Methods)** (Impact: 14.8)
  * `test_dh_public_key` **(Compute Cores)** (Impact: 10.2)
  * `test_dh_private_key` **(Compute Cores)** (Impact: 10.0)
  * `test_rsa_traditional_encrypted_values` **(Defensive Guards)** (Impact: 5.3)
  * `test_rsa_pkcs8_encrypted_values` **(Defensive Guards)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 312`, `args: 189`, `func_start: 97`, `class_start: 10`
* *Risk/State:* `state_mutation: 136`, `duplicate_logic: 4`, `unreferenced_by_name: 61`
* *Architecture:* `io: 81`, `api: 107`, `import: 16`
* *Defense:* `safety: 122`, `doc: 8`, `test: 229`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` ...utils, .test_ec, .test_rsa, .utils, base64, cryptography.hazmat.bindings._rust, cryptography.hazmat.decrepit.ciphers.algorithms, cryptography.hazmat.primitives.asymmetric...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/pkcs7.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.405)
- **Top Global Matches:** file_cluster_8: 7.405, file_cluster_6: 13.578, file_cluster_4: 22.022
- **Magnitude:** 531.62 | **LOC:** 884 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 1.225; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sign_and_serialize` **(Many-Argument Workhorses)** (Impact: 123.9)
  * `encrypt_and_serialize` **(Many-Argument Workhorses)** (Impact: 100.6)
  * `decrypt_der` **(Many-Argument Workhorses)** (Impact: 77.3)
  * `check_decrypt_parameters` **(Many-Argument Workhorses)** (Impact: 41.3)
  * `symmetric_decrypt` **(Stateful Encapsulated Methods)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 160`, `args: 25`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 24`
* *Defense:* `safety: 4`, `test: 7`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.003058
  * `Imports (Out-Degree: 15):` crate::asn1::encode_der_data, crate::backend::ciphers, crate::buf::CffiBuf, crate::error::CryptographyError, crate::error::CryptographyResult, crate::exceptions, crate::padding::PKCS7UnpaddingContext, crate::pkcs12::symmetric_encrypt...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/x509/ocsp_resp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.418)
- **Top Global Matches:** file_cluster_0: 7.418, file_cluster_5: 8.338, file_cluster_12: 9.804
- **Magnitude:** 523.88 | **LOC:** 1046 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 1.345; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (35.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_ocsp_response` **(Many-Argument Workhorses)** (Impact: 167.3)
  * `response_status` **(Generic / Templated Code)** (Impact: 21.9)
  * `single_extensions` **(Compute Cores)** (Impact: 15.4)
  * `certificates` **(Generic / Templated Code)** (Impact: 12.2)
  * `load_der_ocsp_response` **(Stateful Encapsulated Methods)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 162`, `args: 71`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 5`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 9`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.345
  * `Choke Point (Betweenness):` 0.000203 | `Ripple Effect (Closeness):` 0.024771
  * `Imports (Out-Degree: 15):` crate::asn1::big_byte_slice_to_py_int, crate::asn1::oid_to_py_oid, crate::asn1::py_uint_to_big_endian_bytes, crate::error::CryptographyError, crate::error::CryptographyResult, crate::exceptions, crate::types, crate::utils::cstr_from_literal...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/aead.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.981)
- **Top Global Matches:** file_cluster_0: 6.981, file_cluster_9: 9.656, file_cluster_15: 9.978
- **Magnitude:** 510.24 | **LOC:** 1182 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 1.266; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.5%), Debt Markers (formerly Tech Debt) (17.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decrypt_with_context` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `encrypt_with_context` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `decrypt` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `encrypt` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `process_data` **(Many-Argument Workhorses)** (Impact: 22.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 159`, `args: 46`, `func_start: 38`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `duplicate_logic: 4`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 10`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.266
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.006116
  * `Imports (Out-Degree: 3):` crate::buf::CffiBuf, crate::error::CryptographyError, crate::error::CryptographyResult, crate::exceptions, pyo3::types::PyAnyMethods, pyo3::types::PyListMethods, self::AesCcm, self::AesGcm...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/cryptography/x509/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.855)
- **Top Global Matches:** file_cluster_5: 7.855, file_cluster_0: 8.429, file_cluster_12: 8.487
- **Magnitude:** 493.62 | **LOC:** 849 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **15**; blast radius 2.717; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.5814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sign` **(Many-Argument Workhorses)** (Impact: 42.1)
  * `sign` **(Many-Argument Workhorses)** (Impact: 33.6)
  * `sign` **(Many-Argument Workhorses)** (Impact: 28.2)
  * `add_attribute` **(Many-Argument Workhorses)** (Impact: 17.2)
  * `not_valid_after` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* """ Sets the certificate expiration time. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 127`, `args: 50`, `func_start: 50`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 58`
* *Architecture:* `io: 1`, `api: 46`, `import: 15`
* *Defense:* `safety: 30`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.717
  * `Choke Point (Betweenness):` 0.000511 | `Ripple Effect (Closeness):` 0.027245
  * `Imports (Out-Degree: 7):` __future__, abc, collections.abc, cryptography, cryptography.hazmat.bindings._rust, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.asymmetric.types...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/src/rust/src/backend/ciphers.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.847)
- **Top Global Matches:** file_cluster_4: 8.847, file_cluster_0: 10.675, file_cluster_5: 11.152
- **Magnitude:** 456.22 | **LOC:** 619 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **17**; blast radius 1.394; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.6%), Guard Balance (formerly Safety Score) (53.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 112.4)
  * `create_decryption_ctx` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `create_encryption_ctx` **(Generic / Templated Code)** (Impact: 25.4)
  * `finalize_with_tag` **(Many-Argument Workhorses)** (Impact: 24.2)
  * `update_into` **(Stateful Encapsulated Methods)** (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 103`, `args: 41`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 23`, `fragile_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `api: 6`, `import: 7`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.394
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.012232
  * `Imports (Out-Degree: 5):` crate::backend::cipher_registry, crate::buf::CffiBuf, crate::buf::CffiMutBuf, crate::error::CryptographyError, crate::error::CryptographyResult, crate::exceptions, crate::types, pyo3::IntoPyObject...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/test_dh.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.068)
- **Top Global Matches:** file_cluster_15: 7.068, file_cluster_10: 7.783, file_cluster_11: 8.306
- **Magnitude:** 446.2 | **LOC:** 991 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.2; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.3%), Complexity Load (formerly Cognitive Load) (23.7%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 97.8495% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_dh_parameters_allows_rfc3526_groups` **(Defensive Guards)** (Impact: 13.2)
  * `test_dh_vectors` **(Type Conversions)** (Impact: 10.8)
  * `test_public_bytes` **(Defensive Guards)** (Impact: 10.3)
  * `test_bad_exchange` **(Type Conversions)** (Impact: 9.3)
  * `test_private_bytes_values` **(Defensive Guards)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 187`, `args: 63`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `state_mutation: 163`, `dead_code: 1`, `unreferenced_by_name: 44`
* *Architecture:* `io: 48`, `api: 50`, `import: 11`
* *Defense:* `safety: 103`, `doc: 1`, `test: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ...doubles, ...utils, .fixtures_dh, binascii, copy, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cryptography-46.0.6/src/rust/src/x509/common.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.177)
- **Top Global Matches:** file_cluster_6: 8.177, file_cluster_8: 13.01, file_cluster_4: 14.374
- **Magnitude:** 437.24 | **LOC:** 558 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **25**; blast radius 2.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (48.6%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_general_name` **(Many-Argument Workhorses)** (Impact: 78.4)
  * `encode_name_entry` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `parse_general_name` **(Stateful Encapsulated Methods)** (Impact: 45.7)
  * `py_to_datetime` **(Stateful Encapsulated Methods)** (Impact: 32.3)
  * `parse_name_attribute` **(Compute Cores)** (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 93`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.808
  * `Choke Point (Betweenness):` 0.000215 | `Ripple Effect (Closeness):` 0.029142
  * `Imports (Out-Degree: 8):` asn1::SimpleAsn1Readable, crate::asn1::oid_to_py_oid, crate::asn1::py_oid_to_oid, crate::error::CryptographyError, crate::error::CryptographyResult, crate::exceptions, crate::types, crate::x509...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `cryptography-46.0.6/tests/hazmat/primitives/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.76)
- **Top Global Matches:** file_cluster_15: 5.76, file_cluster_16: 7.114, file_cluster_12: 7.666
- **Magnitude:** 410.8 | **LOC:** 566 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **13**; blast radius 6.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.7%), Guard Balance (formerly Safety Score) (54.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (27.2%)
- **Documentation Coverage:** 98.8095% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aead_test` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `generate_aead_test` **(Defensive Guards)** (Impact: 10.5)
  * `generate_rsa_verification_test` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `_kbkdf_cmac_counter_mode_test` **(Stateful Encapsulated Methods)** (Impact: 9.0)
  * `test_rsa_verification` **(Compute Cores)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 144`, `args: 44`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`
* *Architecture:* `io: 1`, `api: 40`, `import: 13`
* *Defense:* `safety: 45`, `doc: 1`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.393
  * `Choke Point (Betweenness):` 0.005314 | `Ripple Effect (Closeness):` 0.076453
  * `Imports (Out-Degree: 14):` ...utils, binascii, cryptography.exceptions, cryptography.hazmat.decrepit.ciphers, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric, cryptography.hazmat.primitives.ciphers, cryptography.hazmat.primitives.ciphers.modes...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `cryptography-46.0.6/src/rust/cryptography-key-parsing/src/lib.rs` (RUST) | Magnitude: 13.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, api: 8, decorators: 5
- `cryptography-46.0.6/src/rust/cryptography-cffi/src/lib.rs` (RUST) | Magnitude: 8.8 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, decorators: 5, pointers: 4
- `cryptography-46.0.6/src/rust/src/types.rs` (RUST) | Magnitude: 217.8 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 277, api: 189, core_var_decl: 189, globals: 185
- `cryptography-46.0.6/tests/hazmat/asn1/test_api.py` (PYTHON) | Magnitude: 39.82 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 25, api: 13, test: 11
- `cryptography-46.0.6/release.py` (PYTHON) | Magnitude: 46.26 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 20, branch: 9, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `cryptography-46.0.6/tests/wycheproof/test_x448.py` (PYTHON) | Magnitude: 21.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 19, safety: 7, core_var_decl: 6
- `cryptography-46.0.6/tests/wycheproof/test_x25519.py` (PYTHON) | Magnitude: 16.58 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 15, safety: 5, core_var_decl: 5
- `cryptography-46.0.6/tests/bench/test_x509.py` (PYTHON) | Magnitude: 39.06 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 18, core_var_decl: 16, design_snake_case: 16
- `cryptography-46.0.6/tests/hazmat/primitives/test_x448.py` (PYTHON) | Magnitude: 104.72 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 253, structural_boundaries: 70, core_var_decl: 48, design_snake_case: 48
- `cryptography-46.0.6/tests/hazmat/primitives/test_cmac.py` (PYTHON) | Magnitude: 86.46 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 151, core_var_decl: 60, design_snake_case: 60, state_mutation: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cryptography-46.0.6/tests/test_cryptography_utils.py` (PYTHON) | Magnitude: 23.46 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 37, safety: 21, state_mutation: 8
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/_serialization.py` (PYTHON) | Magnitude: 117.92 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 36, core_var_decl: 35, state_mutation: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cryptography-46.0.6/tests/wycheproof/test_eddsa.py` (PYTHON) | Magnitude: 24.54 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 17, test: 7, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cryptography-46.0.6/tests/wycheproof/test_utils.py` (PYTHON) | Magnitude: 3.18 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 2, args: 1, func_start: 1
- `cryptography-46.0.6/tests/hazmat/primitives/test_ed448.py` (PYTHON) | Magnitude: 111.02 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 263, structural_boundaries: 77, core_var_decl: 50, design_snake_case: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `cryptography-46.0.6/src/rust/src/x509/mod.rs` (RUST) | Magnitude: 27.3 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, api: 12, encapsulation: 12, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `cryptography-46.0.6/tests/test_utils.py` (PYTHON) | Magnitude: 229.6 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2578, explicit_casts: 257, structural_boundaries: 112, core_var_decl: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/twofactor/hotp.py` (PYTHON) | Magnitude: 96.1 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 27, branch: 15, state_mutation: 15
- `cryptography-46.0.6/src/rust/src/backend/hashes.rs` (RUST) | Magnitude: 128.92 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 189, structural_boundaries: 48, branch: 41, generics: 28

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cryptography-46.0.6/src/cryptography/hazmat/backends/openssl/backend.py` -> **Severity: 0.298** (Bridge: 0.0046 * Flux: 64.1632%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/kdf/kbkdf.py` -> **Severity: 0.176** (Bridge: 0.0018 * Flux: 99.9994%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/asymmetric/ec.py` -> **Severity: 0.135** (Bridge: 0.0014 * Flux: 99.9768%)
- `cryptography-46.0.6/src/cryptography/x509/extensions.py` -> **Severity: 0.12** (Bridge: 0.0012 * Flux: 99.9939%)
- `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py` -> **Severity: 0.109** (Bridge: 0.0011 * Flux: 99.9985%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 16.529** (Embedded: 0.2066 * Error Risk: 80.0%)
- `cryptography-46.0.6/tests/utils.py` -> **Severity: 15.763** (Embedded: 0.1713 * Error Risk: 92.0241%)
- `cryptography-46.0.6/src/cryptography/utils.py` -> **Severity: 10.49** (Embedded: 0.1517 * Error Risk: 69.1542%)
- `cryptography-46.0.6/src/cryptography/__init__.py` -> **Severity: 8.607** (Embedded: 0.1697 * Error Risk: 50.7142%)
- `cryptography-46.0.6/src/cryptography/__about__.py` -> **Severity: 6.718** (Embedded: 0.1149 * Error Risk: 58.4884%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cryptography-46.0.6/src/rust/src/error.rs` -> **Severity: 7430.1** (Blast Radius: 74.301 * Doc Risk: 100.0%)
- `cryptography-46.0.6/src/rust/src/exceptions.rs` -> **Severity: 6835.4** (Blast Radius: 68.354 * Doc Risk: 100.0%)
- `cryptography-46.0.6/src/cryptography/exceptions.py` -> **Severity: 3113.2** (Blast Radius: 31.132 * Doc Risk: 100.0%)
- `cryptography-46.0.6/src/cryptography/utils.py` -> **Severity: 2242.5** (Blast Radius: 22.425 * Doc Risk: 100.0%)
- `cryptography-46.0.6/src/rust/cryptography-x509/src/common.rs` -> **Severity: 2020.806** (Blast Radius: 21.793 * Doc Risk: 92.7273%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 29 literal sites + 2 sites through wrappers = 31
- **`panics_and_aborts`:** 473 literal sites + 3 sites through wrappers = 476

- `_check_byteslike` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `cryptography-46.0.6/src/cryptography/utils.py`
- `run` (function, debug_prints, primitive): 2 call sites in 1 files -- `cryptography-46.0.6/release.py`
- `_bcrypt_kdf` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `cryptography-46.0.6/src/cryptography/hazmat/primitives/serialization/ssh.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 20087 call pairs -- scoped 28.2%, unique 0.0%, ambiguous 11.7%, external 60.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 14030 | 33.7% | 0.0% | 15.6% | 50.8% |
| rust | 6057 | 15.4% | 0.0% | 2.7% | 81.9% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
