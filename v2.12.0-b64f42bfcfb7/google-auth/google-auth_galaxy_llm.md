# ARCHITECTURAL_BRIEF: google-auth
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
- **Scope:** 164 analyzed artifact(s), 31260 LOC.
- **Load-bearing artifact:** `google_auth-2.49.1/google/auth/__init__.py` -- 110 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `google_auth-2.49.1/google/auth/transport/requests.py` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `google_auth-2.49.1/tests/test_external_account.py` at magnitude 805.1 (structural weight, not risk).
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
| Total Artifacts | 187 |
| Analyzed Artifacts (Scanned) | 164 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 23 |
| Total LOC | 31260 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3915 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3335 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0437 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 141 | 31065 | 86.0% |
| JSON | 21 | 195 | 12.8% |
| PLAINTEXT | 2 | 0 | 1.2% |

## 4.1 SOURCE ENCODINGS
All 164 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 33%, Data / Markup / Trivial 21%, Parameter Forwarders Files 18%, Large Core Modules (3) 10%, Many-Argument Workhorses Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 162 | 98.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 23*

**Composition by Extension & Reason:**
- `.pem`: 9x Excluded (Unsupported Extension: '.pem')
- `no_extension`: 3x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 288 LOC), 1x Excluded (Machine-Generated Source Code Signature: 374 LOC), 1x Excluded (Saturation: Line 44 exceeds 500 chars)
- `.typed`: 2x Excluded (Unsupported Extension: '.typed')
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.pickle`: 1x Excluded (Unsupported Extension: '.pickle')
- `.pub`: 1x Excluded (Unsupported Extension: '.pub')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.5 | 20.7 | 17.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 41.8 | 48.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 78.8 | 12.2 | 8.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.4 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.7 | 56.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 256 | 48 | 4 | `google_auth-2.49.1/tests/test__default.py` |
| cleanup | 24 | 8 | 0 | `google_auth-2.49.1/tests/transport/aio/test_sessions.py` |
| guards | 4021 | 118 | 52 | `google_auth-2.49.1/tests/test__default.py` |
| danger | 635 | 97 | 11 | `google_auth-2.49.1/tests/test_pluggable.py` |
| concurrency | 431 | 36 | 6 | `google_auth-2.49.1/tests/transport/aio/test_sessions.py` |
| connectivity | 2760 | 130 | 41 | `google_auth-2.49.1/tests/test__default.py` |
| io | 541 | 67 | 10 | `google_auth-2.49.1/tests/compute_engine/test__mtls.py` |
| crypto | 47 | 22 | 1 | `google_auth-2.49.1/google/auth/crypt/es.py` |
| ipc | 90 | 9 | 0 | `google_auth-2.49.1/tests/test_pluggable.py` |
| time | 275 | 38 | 4 | `google_auth-2.49.1/tests/test_external_account.py` |
| serialization | 9 | 5 | 0 | `google_auth-2.49.1/tests/oauth2/test_credentials.py` |
| regex | 16 | 6 | 0 | `google_auth-2.49.1/google/auth/transport/_mtls_helper.py` |
| events | 64 | 14 | 0 | `google_auth-2.49.1/tests/compute_engine/test__mtls.py` |
| tests | 4497 | 62 | 96 | `google_auth-2.49.1/tests/transport/test__mtls_helper.py` |
| docs | 874 | 97 | 15 | `google_auth-2.49.1/google/auth/credentials.py` |
| debt | 84 | 20 | 1 | `google_auth-2.49.1/google/oauth2/service_account.py` |
| mutation | 14344 | 134 | 233 | `google_auth-2.49.1/tests/test_external_account.py` |
| dead_code | 1346 | 90 | 22 | `google_auth-2.49.1/tests/test_external_account.py` |
| credential | 79 | 19 | 1 | `google_auth-2.49.1/tests/test_aws.py` |
| threat | 1 | 1 | 0 | `google_auth-2.49.1/tests/test_aws.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.225**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `google_auth-2.49.1/tests/compute_engine/test__mtls.py` (Hits: 30)
- `google_auth-2.49.1/tests/test__default.py` (Hits: 29)
- `google_auth-2.49.1/tests/transport/test__mtls_helper.py` (Hits: 26)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`google_auth-2.49.1/google/auth/__init__.py`) — 110 inbound connections
2. **__init__.py** (`google_auth-2.49.1/google/oauth2/__init__.py`) — 39 inbound connections
3. **__init__.py** (`google_auth-2.49.1/google/auth/transport/__init__.py`) — 15 inbound connections
4. **credentials.py** (`google_auth-2.49.1/google/auth/credentials.py`) — 14 inbound connections
5. **credentials.py** (`google_auth-2.49.1/google/auth/aio/credentials.py`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **requests.py** (`google_auth-2.49.1/google/auth/transport/requests.py`) — 18 outbound dependencies
2. **_default.py** (`google_auth-2.49.1/google/auth/_default.py`) — 15 outbound dependencies
3. **sessions.py** (`google_auth-2.49.1/google/auth/aio/transport/sessions.py`) — 13 outbound dependencies
4. **aws.py** (`google_auth-2.49.1/google/auth/aws.py`) — 13 outbound dependencies
5. **urllib3.py** (`google_auth-2.49.1/google/auth/transport/urllib3.py`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `assert_underlying_credentials_refresh` **(Many-Argument Workhorses)** (@ `google_auth-2.49.1/tests/test_identity_pool.py`) -> Impact: **84.3** | LOC: 136
- `get` **(Many-Argument Workhorses)** (@ `google_auth-2.49.1/google/auth/compute_engine/_metadata.py`) -> Impact: **67.5** | LOC: 149
- `__init__` **(Many-Argument Workhorses)** (@ `google_auth-2.49.1/google/auth/aws.py`) -> Impact: **56.2** | LOC: 105
- `__init__` **(Stateful Encapsulated Methods)** (@ `google_auth-2.49.1/google/auth/identity_pool.py`) -> Impact: **54.2** | LOC: 124
- `request` **(Many-Argument Workhorses)** (@ `google_auth-2.49.1/google/auth/transport/requests.py`) -> Impact: **46.3** | LOC: 146
- `make_mock_request` **(Many-Argument Workhorses)** (@ `google_auth-2.49.1/tests/test_aws.py`) -> Impact: **45.6** | LOC: 88
- `__init__` **(Stateful Encapsulated Methods)** (@ `google_auth-2.49.1/google/auth/compute_engine/credentials.py`) -> Impact: **45.0** | LOC: 78
- `request` **(Many-Argument Workhorses)** (@ `google_auth-2.49.1/google/auth/transport/_aiohttp_requests.py`) -> Impact: **44.4** | LOC: 129
- `__init__` **(Stateful Encapsulated Methods)** (@ `google_auth-2.49.1/google/auth/pluggable.py`) -> Impact: **39.1** | LOC: 103
- `decode` **(Many-Argument Workhorses)** (@ `google_auth-2.49.1/google/auth/jwt.py`) -> Impact: **38.6** | LOC: 86
  * *Intent:* """Decode and verify a JWT. Args: token (str): The encoded JWT. certs (Union[str, bytes, Mapping[str, Union[str, bytes]]]): The certificate used to va...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `google_auth-2.49.1/tests` | 28 | 6498.24 | 17.8% | 0.0% |
| `google_auth-2.49.1/google/auth` | 31 | 4366.16 | 28.33% | 36.12% |
| `google_auth-2.49.1/google/oauth2` | 16 | 2185.2 | 30.75% | 39.1% |
| `google_auth-2.49.1/tests/oauth2` | 13 | 2133.6 | 12.57% | 0.0% |
| `google_auth-2.49.1/google/auth/transport` | 10 | 1390.8 | 34.74% | 25.31% |
| `google_auth-2.49.1/tests/transport` | 8 | 1130.68 | 10.69% | 0.0% |
| `google_auth-2.49.1/tests/compute_engine` | 4 | 1051.16 | 12.73% | 0.0% |
| `google_auth-2.49.1/tests/transport/aio` | 3 | 1002.94 | 33.33% | 0.0% |
| `google_auth-2.49.1/google/auth/compute_engine` | 4 | 635.68 | 24.98% | 33.12% |
| `google_auth-2.49.1/google/auth/aio/transport` | 4 | 572.82 | 43.36% | 28.84% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `google_auth-2.49.1/google/auth/metrics.py` -> **100.0%** Exposure
- `google_auth-2.49.1/google/auth/transport/_aiohttp_requests.py` -> **99.9975%** Exposure
- `google_auth-2.49.1/google/auth/_helpers.py` -> **99.9952%** Exposure
- `google_auth-2.49.1/google/auth/aio/credentials.py` -> **99.9447%** Exposure
- `google_auth-2.49.1/google/auth/api_key.py` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `google_auth-2.49.1/google/auth/_agent_identity_utils.py` -> **100.0%** Exposure
- `google_auth-2.49.1/google/auth/_cloud_sdk.py` -> **100.0%** Exposure
- `google_auth-2.49.1/google/auth/_helpers.py` -> **100.0%** Exposure
- `google_auth-2.49.1/google/auth/aws.py` -> **100.0%** Exposure
- `google_auth-2.49.1/google/auth/compute_engine/_metadata.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `google_auth-2.49.1/tests/test_external_account.py` -> **81** Orphaned Functions | **0** Duplicates
- `google_auth-2.49.1/tests/test_identity_pool.py` -> **79** Orphaned Functions | **0** Duplicates
- `google_auth-2.49.1/tests/test__helpers.py` -> **76** Orphaned Functions | **2** Duplicates
- `google_auth-2.49.1/tests/test_aws.py` -> **56** Orphaned Functions | **0** Duplicates
- `google_auth-2.49.1/tests/test_impersonated_credentials.py` -> **56** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `google_auth-2.49.1/google/auth/crypt/_python_rsa.py` -> **100.0%** Exposure
- `google_auth-2.49.1/google/auth/metrics.py` -> **100.0%** Exposure
- `google_auth-2.49.1/tests/test_aws.py` -> **100.0%** Exposure
- `google_auth-2.49.1/google/auth/transport/_mtls_helper.py` -> **99.9999%** Exposure
- `google_auth-2.49.1/google/auth/environment_vars.py` -> **99.9925%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `807` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `google_auth-2.49.1/tests/test_external_account.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.623)
- **Top Global Matches:** file_cluster_15: 7.623, file_cluster_12: 7.727, file_cluster_13: 8.605
- **Magnitude:** 805.1 | **LOC:** 2429 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.7%), Complexity Load (formerly Cognitive Load) (13.0%), Connectivity (formerly Api Exposure) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_token_request_kwargs` **(Defensive Guards)** (Impact: 10.5)
  * `make_mock_request` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `assert_impersonation_request_kwargs` **(Defensive Guards)** (Impact: 8.0)
  * `test_get_project_id_cloud_resource_manager_success` **(Many-Argument Workhorses)** (Impact: 6.7)
  * `test_refresh_impersonation_with_mtls_success` **(Many-Argument Workhorses)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 429`, `args: 89`, `func_start: 89`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 341`, `unreferenced_by_name: 81`
* *Architecture:* `api: 125`, `import: 14`
* *Defense:* `safety: 223`, `doc: 37`, `test: 157`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` datetime, google.auth, google.auth.credentials, http.client, json, os, pytest, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/test_identity_pool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.253)
- **Top Global Matches:** file_cluster_15: 8.253, file_cluster_12: 8.328, file_cluster_16: 9.044
- **Magnitude:** 757.92 | **LOC:** 1830 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.5%), Complexity Load (formerly Cognitive Load) (15.9%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_underlying_credentials_refresh` **(Many-Argument Workhorses)** (Impact: 84.3)
  * `make_mock_response` **(Defensive Guards)** (Impact: 6.4)
  * `get_subject_token` **(Defensive Guards)** (Impact: 6.3)
  * `make_mock_request` **(Many-Argument Workhorses)** (Impact: 5.4)
  * `assert_token_request_kwargs` **(Defensive Guards)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 297`, `args: 87`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 204`, `planned_debt: 1`, `unreferenced_by_name: 79`
* *Architecture:* `io: 23`, `api: 101`, `import: 15`
* *Defense:* `safety: 90`, `doc: 6`, `test: 133`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` OpenSSL, base64, datetime, google.auth, google.auth.credentials, http.client, json, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/test_aws.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.124)
- **Top Global Matches:** file_cluster_15: 7.124, file_cluster_16: 8.03, file_cluster_13: 8.222
- **Magnitude:** 754.22 | **LOC:** 2459 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Guard Balance (formerly Safety Score) (50.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_mock_request` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `assert_aws_metadata_request_kwargs` **(Defensive Guards)** (Impact: 10.4)
  * `make_serialized_aws_signed_request` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `test_refresh_success_with_impersonation_ignore_default_scopes` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `test_refresh_success_with_impersonation_use_default_scopes` **(Many-Argument Workhorses)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 330
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 247`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 270`, `planned_debt: 1`, `unreferenced_by_name: 56`
* *Architecture:* `api: 97`, `import: 13`
* *Defense:* `safety: 102`, `doc: 16`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, google.auth, google.auth.credentials, http.client, json, os, pytest, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/transport/aio/test_sessions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.292)
- **Top Global Matches:** file_cluster_15: 8.292, file_cluster_11: 8.705, file_cluster_13: 8.867
- **Magnitude:** 658.3 | **LOC:** 337 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Many-Argument Workhorses)** (Impact: 6.7)
  * `test_constructor_raises_no_auth_request_error` **(Compute Cores)** (Impact: 4.6)
  * `test_constructor_raises_incorrect_credentials_error` **(Compute Cores)** (Impact: 4.6)
  * `test_timeout_with_simple_async_task_out_of_bounds` **(Defensive Guards)** (Impact: 4.3)
  * `test_timeout_with_async_task_timing_out_before_context` **(Defensive Guards)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 75 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 465
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 157`, `args: 34`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `state_mutation: 65`, `unreferenced_by_name: 20`
* *Architecture:* `io: 1`, `api: 34`, `concurrency: 90`, `import: 8`
* *Defense:* `safety: 21`, `test: 67`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` aioresponses, asyncio, google.auth.aio.credentials, google.auth.aio.transport, google.auth.exceptions, pytest, typing, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/test_impersonated_credentials.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.31)
- **Top Global Matches:** file_cluster_12: 6.31, file_cluster_15: 8.204, file_cluster_11: 8.916
- **Magnitude:** 583.3 | **LOC:** 1313 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.0%), Complexity Load (formerly Cognitive Load) (28.7%), Credential Material (formerly Secrets Risk) (24.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_request` **(Many-Argument Workhorses)** (Impact: 11.5)
  * `test_refresh_source_credentials` **(Compute Cores)** (Impact: 6.8)
  * `test_refresh_success` **(Many-Argument Workhorses)** (Impact: 5.3)
  * `test_refresh_failure_subject_with_nondefault_domain` **(Defensive Guards)** (Impact: 4.8)
  * `test_refresh_failure_unauthorzed` **(Defensive Guards)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 289`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 282`, `unreferenced_by_name: 56`
* *Architecture:* `io: 15`, `api: 71`, `import: 17`
* *Defense:* `safety: 122`, `test: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` copy, datetime, google.auth, google.auth.impersonated_credentials, google.oauth2, http.client, json, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/compute_engine/test_credentials.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.005)
- **Top Global Matches:** file_cluster_15: 8.005, file_cluster_12: 8.203, file_cluster_13: 8.316
- **Magnitude:** 510.22 | **LOC:** 1426 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.7%), Complexity Load (formerly Cognitive Load) (14.3%), Connectivity (formerly Api Exposure) (13.5%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_build_trust_boundary_lookup_url_get_service_account_info_fails` **(Compute Cores)** (Impact: 5.9)
  * `test_refresh_error` **(Many-Argument Workhorses)** (Impact: 5.5)
  * `test_refresh_trust_boundary_lookup_fails_no_cache` **(Defensive Guards)** (Impact: 5.3)
  * `test_refresh_trust_boundary_lookup_fails_with_cached_data` **(Many-Argument Workhorses)** (Impact: 4.7)
  * `test_transport_error_from_metadata` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 244`, `args: 50`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 192`, `unreferenced_by_name: 40`
* *Architecture:* `io: 5`, `api: 132`, `import: 14`
* *Defense:* `safety: 139`, `doc: 2`, `test: 185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` base64, datetime, google.auth, google.auth.compute_engine, google.auth.transport, google.oauth2, os, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/test__default.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.995)
- **Top Global Matches:** file_cluster_15: 7.995, file_cluster_13: 8.329, file_cluster_11: 8.346
- **Magnitude:** 502.62 | **LOC:** 1465 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 2.182; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (76.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (25.0%), Complexity Load (formerly Cognitive Load) (7.5%)
- **Documentation Coverage:** 97.3545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_get_gcloud_sdk_credentials_suppresses_deprecation_warning` **(Defensive Guards)** (Impact: 6.7)
  * `test_get_explicit_environ_credentials_suppresses_deprecation_warning` **(Defensive Guards)** (Impact: 4.9)
  * `test_load_credentials_from_file_authorized_user_bad_format` **(Defensive Guards)** (Impact: 4.7)
  * `test_load_credentials_from_file_service_account_bad_format` **(Defensive Guards)** (Impact: 4.7)
  * `test_default_fail` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 446`, `args: 94`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `io: 29`, `api: 141`, `import: 24`
* *Defense:* `safety: 270`, `doc: 10`, `test: 183`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.182
  * `Choke Point (Betweenness):` 0.000322 | `Ripple Effect (Closeness):` 0.006135
  * `Imports (Out-Degree: 4):` google.auth, google.oauth2, google.oauth2.credentials, json, os, pytest, sys, unittest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `google_auth-2.49.1/tests/oauth2/test_service_account.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.261)
- **Top Global Matches:** file_cluster_12: 7.261, file_cluster_15: 7.963, file_cluster_13: 8.83
- **Magnitude:** 500.34 | **LOC:** 1124 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.8%), Complexity Load (formerly Cognitive Load) (24.6%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_refresh_trust_boundary_lookup_fails_no_cache` **(Many-Argument Workhorses)** (Impact: 5.2)
  * `test__with_always_use_jwt_access_non_default_universe_domain` **(Defensive Guards)** (Impact: 4.6)
  * `test_refresh_trust_boundary_lookup_fails_with_cached_data` **(Many-Argument Workhorses)** (Impact: 4.6)
  * `test__with_use_iam_endpoint_non_default_universe_domain` **(Defensive Guards)** (Impact: 4.6)
  * `test_refresh_success_with_valid_trust_boundary` **(Defensive Guards)** (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 296`, `args: 72`, `func_start: 72`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 211`, `duplicate_logic: 8`, `unreferenced_by_name: 42`
* *Architecture:* `io: 12`, `api: 104`, `import: 15`
* *Defense:* `safety: 170`, `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` datetime, google.auth, google.auth.credentials, google.oauth2, json, os, pytest, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/google/auth/aws.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.017)
- **Top Global Matches:** file_cluster_12: 8.017, file_cluster_4: 8.36, file_cluster_16: 9.98
- **Magnitude:** 472.56 | **LOC:** 864 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 15.407; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 48.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 56.2)
  * `get_request_options` **(Many-Argument Workhorses)** (Impact: 27.2)
  * `_generate_authentication_header_map` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `get_aws_region` **(Many-Argument Workhorses)** (Impact: 17.9)
    * *Intent:* # The AWS metadata server is not available in some AWS environments # such as AWS lambda. Instead, i...
  * `_get_metadata_security_credentials` **(Many-Argument Workhorses)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 70`, `args: 21`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 103`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 16`
* *Defense:* `safety: 3`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.248221
  * `Imports (Out-Degree: 1):` abc, dataclasses, google.auth, hashlib, hmac, http.client, json, os...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `google_auth-2.49.1/tests/transport/test__mtls_helper.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.197)
- **Top Global Matches:** file_cluster_15: 8.197, file_cluster_13: 8.767, file_cluster_12: 9.364
- **Magnitude:** 463.98 | **LOC:** 995 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (99.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (36.2%), Connectivity (formerly Api Exposure) (14.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_cert_and_key` **(Compute Cores)** (Impact: 10.5)
  * `test_check_use_client_cert_config_fallback` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* # Test fallback for config file when determining if client cert should be used cloudsdk_path = "/pat...
  * `test_use_client_cert_fallback` **(Type Conversions)** (Impact: 5.1)
    * *Intent:* # Fallback to CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE if GOOGLE_API_USE_CLIENT_CERTIFICATE is ...
  * `test_success_with_certificate_config_cloud_run_patch_skipped_if_cert_exists` **(Many-Argument Workhorses)** (Impact: 4.4)
  * `test_success_with_certificate_config_cloud_run_patch` **(Many-Argument Workhorses)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 215`, `args: 64`, `func_start: 64`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 10`, `state_mutation: 134`, `unreferenced_by_name: 52`
* *Architecture:* `io: 26`, `api: 140`, `import: 7`
* *Defense:* `safety: 93`, `doc: 6`, `test: 257`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` OpenSSL, google.auth, google.auth.transport, os, pytest, re, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/test_pluggable.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.457)
- **Top Global Matches:** file_cluster_12: 6.457, file_cluster_15: 8.959, file_cluster_7: 8.96
- **Magnitude:** 458.56 | **LOC:** 1262 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (10.9%), Complexity Load (formerly Cognitive Load) (9.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_retrieve_subject_token_successfully` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `test_revoke_failed` **(I/O & Config Routines)** (Impact: 6.9)
  * `make_pluggable` **(Many-Argument Workhorses)** (Impact: 5.4)
  * `test_retrieve_subject_token_missing_error_code_message` **(Defensive Guards)** (Impact: 5.2)
  * `test_retrieve_subject_token_failed_interactive_mode` **(Compute Cores)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 15 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 220`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 21`, `state_mutation: 160`, `unreferenced_by_name: 46`
* *Architecture:* `io: 12`, `api: 48`, `import: 9`
* *Defense:* `safety: 52`, `doc: 14`, `test: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` google.auth, google.auth.credentials, json, os, pytest, subprocess, tests.test__default, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/google/auth/external_account.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.549)
- **Top Global Matches:** file_cluster_12: 6.549, file_cluster_16: 6.657, file_cluster_15: 7.157
- **Magnitude:** 456.42 | **LOC:** 717 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Debt Markers (formerly Tech Debt) (65.7%)
- **Documentation Coverage:** 40.4255% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 38.0)
  * `_perform_refresh_token` **(Stateful Encapsulated Methods)** (Impact: 28.6)
  * `get_project_id` **(Stateful Encapsulated Methods)** (Impact: 19.7)
    * *Intent:* """Retrieves the project ID corresponding to the workload identity or workforce pool. For workforce ...
  * `_build_trust_boundary_lookup_url` **(Stateful Encapsulated Methods)** (Impact: 10.1)
    * *Intent:* """Builds and returns the URL for the trust boundary lookup API."""
  * `service_account_email` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """Returns the service account email if service account impersonation is used. Returns: Optional[str...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 92`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 107`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 20`, `import: 16`
* *Defense:* `safety: 4`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` abc, copy, dataclasses, datetime, functools, google.auth, google.oauth2, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/oauth2/test_credentials.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.336)
- **Top Global Matches:** file_cluster_15: 7.336, file_cluster_12: 7.889, file_cluster_13: 8.209
- **Magnitude:** 421.32 | **LOC:** 1094 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.8%), Complexity Load (formerly Cognitive Load) (29.4%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pickle_and_unpickle_with_refresh_handler` **(Defensive Guards)** (Impact: 8.3)
  * `test_pickle_and_unpickle` **(Defensive Guards)** (Impact: 6.3)
  * `test_credentials_with_scopes_refresh_different_granted_scopes` **(Many-Argument Workhorses)** (Impact: 5.2)
  * `test_credentials_with_scopes_requested_refresh_success` **(Many-Argument Workhorses)** (Impact: 5.1)
  * `test_invalid_refresh_handler` **(Defensive Guards)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 250`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 5`, `state_mutation: 185`, `unreferenced_by_name: 39`
* *Architecture:* `io: 8`, `api: 65`, `import: 12`
* *Defense:* `safety: 167`, `test: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` datetime, google.auth, google.auth.credentials, google.oauth2, json, os, pickle, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/google/oauth2/service_account.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.715)
- **Top Global Matches:** file_cluster_16: 6.715, file_cluster_15: 6.94, file_cluster_12: 7.85
- **Magnitude:** 414.5 | **LOC:** 881 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.054; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 53.4247% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_create_self_signed_jwt` **(Stateful Encapsulated Methods)** (Impact: 24.4)
    * *Intent:* """Create a self-signed JWT from the credentials if requirements are met. Args: audience (str): The ...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 22.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 20.8)
  * `_perform_refresh_token` **(Stateful Encapsulated Methods)** (Impact: 15.1)
  * `_with_use_iam_endpoint` **(Stateful Encapsulated Methods)** (Impact: 8.3)
    * *Intent:* """Create a copy of these credentials with the use_iam_endpoint value. Args: use_iam_endpoint (bool)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 102`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 93`, `duplicate_logic: 16`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.054
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.006135
  * `Imports (Out-Degree: 2):` copy, datetime, google.auth, google.oauth2
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `google_auth-2.49.1/google/auth/jwt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.268)
- **Top Global Matches:** file_cluster_12: 7.268, file_cluster_15: 7.403, file_cluster_16: 7.592
- **Magnitude:** 397.38 | **LOC:** 878 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 34.4828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Many-Argument Workhorses)** (Impact: 38.6)
    * *Intent:* """Decode and verify a JWT. Args: token (str): The encoded JWT. certs (Union[str, bytes, Mapping[str...
  * `with_claims` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `encode` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* """Make a signed JWT. Args: signer (google.auth.crypt.Signer): The signer used to sign the JWT. payl...
  * `with_claims` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* """Returns a copy of these credentials with modified claims. Args: issuer (str): The `iss` claim. If...
  * `_verify_iat_and_exp` **(Stateful Encapsulated Methods)** (Impact: 10.7)
    * *Intent:* """Verifies the ``iat`` (Issued At) and ``exp`` (Expires) claims in a token payload. Args: payload (...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 91`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `duplicate_logic: 12`, `unreferenced_by_name: 3`
* *Architecture:* `api: 26`, `import: 13`
* *Defense:* `safety: 13`, `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collections, collections.abc, copy, datetime, google.auth, google.auth.credentials, google.auth.crypt, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/compute_engine/test__metadata.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.607)
- **Top Global Matches:** file_cluster_11: 7.607, file_cluster_15: 7.895, file_cluster_13: 8.069
- **Magnitude:** 390.64 | **LOC:** 972 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.6%), Credential Material (formerly Secrets Risk) (40.7%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 98.2301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_request` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `test_validate_gce_mds_configured_environment` **(Many-Argument Workhorses)** (Impact: 7.4)
  * `test_get_universe_domain_retryable_error_success` **(Stateful Encapsulated Methods)** (Impact: 4.4)
    * *Intent:* # Test that if the universe domain endpoint returns a retryable error # we should retry. # # In this...
  * `request` **(Parameter Forwarders)** (Impact: 4.3)
  * `test_get_universe_domain_retryable_error_failure` **(Defensive Guards)** (Impact: 3.8)
    * *Intent:* # Test that if the universe domain endpoint returns a retryable error # we should retry. # # In this...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 190`, `args: 57`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `state_mutation: 133`, `unreferenced_by_name: 55`
* *Architecture:* `io: 18`, `api: 96`, `import: 15`
* *Defense:* `safety: 67`, `doc: 2`, `test: 107`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` datetime, google.auth, google.auth.compute_engine, google.auth.transport, http.client, importlib, json, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/test_jwt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.118)
- **Top Global Matches:** file_cluster_15: 7.118, file_cluster_12: 7.664, file_cluster_11: 7.767
- **Magnitude:** 366.76 | **LOC:** 703 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (29.1%), Complexity Load (formerly Cognitive Load) (23.5%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `factory` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `token_factory` **(Compute Cores)** (Impact: 13.4)
  * `test_decode_no_cert` **(Defensive Guards)** (Impact: 4.5)
  * `test_decode_bad_token_too_early` **(Defensive Guards)** (Impact: 3.4)
  * `test_decode_bad_token_expired` **(Defensive Guards)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 280`, `args: 71`, `func_start: 69`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 112`, `duplicate_logic: 8`, `unreferenced_by_name: 34`
* *Architecture:* `io: 20`, `api: 69`, `import: 10`
* *Defense:* `safety: 136`, `test: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` base64, datetime, google.auth, json, os, pytest, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/google/oauth2/credentials.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.759)
- **Top Global Matches:** file_cluster_16: 6.759, file_cluster_15: 6.962, file_cluster_4: 7.931
- **Magnitude:** 365.14 | **LOC:** 618 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **7**; blast radius 14.915; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 31.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `refresh` **(Stateful Encapsulated Methods)** (Impact: 33.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 30.5)
  * `from_authorized_user_info` **(Many-Argument Workhorses)** (Impact: 16.7)
    * *Intent:* """Creates a Credentials instance from parsed authorized user info. Args: info (Mapping[str, str]): ...
  * `to_json` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* """Utility function that creates a JSON representation of a Credentials object. Args: strip (Sequenc...
  * `refresh_handler` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* """Updates the current refresh handler. Args: value (Optional[Callable[[google.auth.transport.Reques...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 84`, `args: 31`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `state_mutation: 83`
* *Architecture:* `io: 1`, `api: 30`, `import: 11`
* *Defense:* `safety: 4`, `doc: 24`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.915
  * `Choke Point (Betweenness):` 0.004159 | `Ripple Effect (Closeness):` 0.248221
  * `Imports (Out-Degree: 3):` datetime, google.auth, google.oauth2, io, json, logging, warnings
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `google_auth-2.49.1/tests/test__helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.805)
- **Top Global Matches:** file_cluster_12: 6.805, file_cluster_11: 8.185, file_cluster_15: 8.601
- **Magnitude:** 362.02 | **LOC:** 727 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.5%), Credential Material (formerly Secrets Risk) (23.7%), Complexity Load (formerly Cognitive Load) (19.2%)
- **Documentation Coverage:** 90.6433% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_get_bool_from_env` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* # Test default value when environment variable is not set. assert _helpers.get_bool_from_env("TEST_V...
  * `test_scopes_to_string` **(Defensive Guards)** (Impact: 5.7)
  * `test_padded_urlsafe_b64decode` **(Defensive Guards)** (Impact: 4.7)
  * `test_string_to_scopes` **(Defensive Guards)** (Impact: 4.2)
  * `test_unpadded_urlsafe_b64encode` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 238`, `args: 86`, `func_start: 86`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 109`, `duplicate_logic: 2`, `unreferenced_by_name: 76`
* *Architecture:* `api: 90`, `import: 7`
* *Defense:* `safety: 103`, `doc: 9`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` datetime, google.auth, json, logging, pytest, unittest, urllib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/tests/test_downscoped.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.277)
- **Top Global Matches:** file_cluster_15: 6.277, file_cluster_12: 7.586, file_cluster_11: 7.741
- **Magnitude:** 354.5 | **LOC:** 794 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.0%), Complexity Load (formerly Cognitive Load) (24.3%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_request_kwargs` **(Defensive Guards)** (Impact: 5.1)
  * `test_invalid_availability_condition_type` **(Defensive Guards)** (Impact: 4.7)
  * `test_invalid_title_type` **(Defensive Guards)** (Impact: 4.5)
  * `test_invalid_description_type` **(Defensive Guards)** (Impact: 4.5)
  * `test_before_request_expired` **(Defensive Guards)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 221`, `args: 46`, `func_start: 46`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 141`, `unreferenced_by_name: 27`
* *Architecture:* `api: 54`, `import: 13`
* *Defense:* `safety: 103`, `doc: 5`, `test: 60`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` datetime, google.auth, google.auth.credentials, http.client, json, pytest, unittest, urllib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/google/auth/identity_pool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.209)
- **Top Global Matches:** file_cluster_4: 7.209, file_cluster_12: 7.672, file_cluster_16: 7.769
- **Magnitude:** 344.22 | **LOC:** 576 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (92.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 54.2)
  * `get_subject_token` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* # Import OpennSSL inline because it is an extra import only required by customers # using mTLS. from...
  * `_validate_file_or_url_config` **(Stateful Encapsulated Methods)** (Impact: 13.4)
  * `_validate_certificate_config` **(Stateful Encapsulated Methods)** (Impact: 9.4)
  * `_create_default_metrics_options` **(Stateful Encapsulated Methods)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 82`, `args: 25`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 66`, `unreferenced_by_name: 7`
* *Architecture:* `io: 4`, `api: 10`, `import: 15`
* *Defense:* `safety: 9`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` OpenSSL, abc, base64, collections, collections.abc, google.auth, google.auth.transport, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/google/auth/aio/transport/sessions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.339)
- **Top Global Matches:** file_cluster_5: 7.339, file_cluster_12: 8.484, file_cluster_0: 9.502
- **Magnitude:** 321.16 | **LOC:** 577 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 2.564; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (64.6%)
- **Documentation Coverage:** 68.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 14.9)
  * `configure_mtls_channel` **(Stateful Encapsulated Methods)** (Impact: 14.0)
    * *Intent:* """Configure the client certificate and key for SSL connection. The function does nothing unless `GO...
  * `_do_configure` **(Stateful Encapsulated Methods)** (Impact: 7.1)
    * *Intent:* # Run the blocking check in an executor use_client_cert = await mtls._run_in_executor( google.auth.t...
  * `get` **(Many-Argument Workhorses)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 123
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 79`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 31`, `unreferenced_by_name: 8`
* *Architecture:* `io: 8`, `api: 12`, `concurrency: 33`, `import: 16`
* *Defense:* `safety: 12`, `doc: 11`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.564
  * `Choke Point (Betweenness):` 0.000606 | `Ripple Effect (Closeness):` 0.01227
  * `Imports (Out-Degree: 7):` aiohttp, asyncio, contextlib, functools, google.auth, google.auth.aio, google.auth.aio.credentials, google.auth.aio.transport...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `google_auth-2.49.1/google/auth/impersonated_credentials.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.31)
- **Top Global Matches:** file_cluster_12: 6.31, file_cluster_16: 6.917, file_cluster_15: 6.995
- **Magnitude:** 320.52 | **LOC:** 713 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 2.373; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (64.5%), Guard Balance (formerly Safety Score) (62.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 82.9268% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_impersonated_service_account_info` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* """Creates a Credentials instance from parsed impersonated service account credentials info. **IMPOR...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 20.3)
  * `_make_iam_token_request` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `_perform_refresh_token` **(Many-Argument Workhorses)** (Impact: 13.9)
    * *Intent:* """Updates credentials with a new access_token representing the impersonated account. Args: request ...
  * `_sign_jwt_request` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* """Makes a request to the Google Cloud IAM service to sign a JWT using a service account's system-ma...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 89`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 83`
* *Architecture:* `io: 2`, `api: 20`, `import: 18`
* *Defense:* `safety: 12`, `doc: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.373
  * `Choke Point (Betweenness):` 0.000417 | `Ripple Effect (Closeness):` 0.01227
  * `Imports (Out-Degree: 5):` base64, copy, datetime, google.auth, google.auth.transport.requests, google.oauth2, http.client, json
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `google_auth-2.49.1/tests/oauth2/test__client.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.578)
- **Top Global Matches:** file_cluster_15: 7.578, file_cluster_11: 7.657, file_cluster_13: 8.318
- **Magnitude:** 317.36 | **LOC:** 808 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.799; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.8%), Complexity Load (formerly Cognitive Load) (24.1%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test__token_endpoint_request_no_throw_with_retry` **(Defensive Guards)** (Impact: 5.2)
  * `test__can_retry_retryable` **(Defensive Guards)** (Impact: 4.3)
  * `verify_request_params` **(Defensive Guards)** (Impact: 3.8)
  * `test_lookup_trust_boundary_internal_failure_and_retry_failure_error` **(I/O & Config Routines)** (Impact: 3.4)
  * `test_refresh_grant_with_scopes` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 156`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 142`, `unreferenced_by_name: 39`
* *Architecture:* `io: 4`, `api: 55`, `import: 14`
* *Defense:* `safety: 60`, `test: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, google.auth, google.oauth2, http.client, json, os, pytest, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `google_auth-2.49.1/google/auth/compute_engine/credentials.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.137)
- **Top Global Matches:** file_cluster_16: 6.137, file_cluster_15: 6.413, file_cluster_12: 7.895
- **Magnitude:** 279.94 | **LOC:** 557 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 24.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 60.4651% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 45.0)
  * `_build_trust_boundary_lookup_url` **(Stateful Encapsulated Methods)** (Impact: 8.6)
    * *Intent:* """Builds and returns the URL for the trust boundary lookup API for GCE."""
  * `_retrieve_info` **(Stateful Encapsulated Methods)** (Impact: 8.1)
    * *Intent:* """Retrieve information about the service account. Updates the scopes and retrieves the full service...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 7.4)
  * `with_target_audience` **(Compute Cores)** (Impact: 6.7)
    * *Intent:* """Create a copy of these credentials with the specified target audience. Args: target_audience (str...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 79`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 58`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 21`, `import: 11`
* *Defense:* `safety: 6`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.99
  * `Choke Point (Betweenness):` 0.000581 | `Ripple Effect (Closeness):` 0.246811
  * `Imports (Out-Degree: 5):` datetime, google.auth, google.auth.compute_engine, google.auth.transport, google.oauth2
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `google_auth-2.49.1/google/auth/credentials.py` (PYTHON) | Magnitude: 246.3 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 190, structural_boundaries: 107, doc: 50, args: 43
- `google_auth-2.49.1/google/auth/external_account.py` (PYTHON) | Magnitude: 456.42 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 356, state_mutation: 107, core_var_decl: 105, design_snake_case: 100
- `google_auth-2.49.1/tests/oauth2/test_challenges.py` (PYTHON) | Magnitude: 101.2 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 83, state_mutation: 57, core_var_decl: 52
- `google_auth-2.49.1/google/auth/jwt.py` (PYTHON) | Magnitude: 397.38 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 320, core_var_decl: 92, structural_boundaries: 91, design_snake_case: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `google_auth-2.49.1/google/auth/exceptions.py` (PYTHON) | Magnitude: 30.04 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 24, api: 20, doc: 19, class_start: 18
- `google_auth-2.49.1/tests/transport/test_aio_mtls_helper.py` (PYTHON) | Magnitude: 208.22 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 71, test: 42, safety: 31
- `google_auth-2.49.1/tests/test__cloud_sdk.py` (PYTHON) | Magnitude: 80.04 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 54, core_var_decl: 43, design_snake_case: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `google_auth-2.49.1/tests/test__cache.py` (PYTHON) | Magnitude: 36.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 34, safety: 25, state_mutation: 20
- `google_auth-2.49.1/google/auth/_service_account_info.py` (PYTHON) | Magnitude: 32.22 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, core_var_decl: 9, design_snake_case: 9
- `google_auth-2.49.1/tests/test__refresh_worker.py` (PYTHON) | Magnitude: 102.0 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 46, state_mutation: 31, core_var_decl: 25
- `google_auth-2.49.1/google/oauth2/_credentials_async.py` (PYTHON) | Magnitude: 52.14 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 19, branch: 9, state_mutation: 8
- `google_auth-2.49.1/tests/transport/test__custom_tls_signer.py` (PYTHON) | Magnitude: 107.6 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 153, structural_boundaries: 73, state_mutation: 57, test_skip: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `google_auth-2.49.1/google/auth/transport/urllib3.py` (PYTHON) | Magnitude: 215.62 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 69, state_mutation: 42, core_var_decl: 34
- `google_auth-2.49.1/google/auth/compute_engine/_mtls.py` (PYTHON) | Magnitude: 69.0 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 42, core_var_decl: 20, state_mutation: 17
- `google_auth-2.49.1/google/auth/_exponential_backoff.py` (PYTHON) | Magnitude: 84.58 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 29, state_mutation: 16, encapsulation: 15
- `google_auth-2.49.1/google/auth/transport/grpc.py` (PYTHON) | Magnitude: 113.16 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 28, state_mutation: 20, core_var_decl: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `google_auth-2.49.1/tests/crypt/test_crypt.py` (PYTHON) | Magnitude: 15.34 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 14, state_mutation: 10, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `google_auth-2.49.1/tests/test_api_key.py` (PYTHON) | Magnitude: 11.5 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 15, safety: 8, test: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `google_auth-2.49.1/google/auth/_default.py` -> **Severity: 7.604** (Bridge: 0.076 * Flux: 99.9907%)
- `google_auth-2.49.1/google/auth/__init__.py` -> **Severity: 3.922** (Bridge: 0.0784 * Flux: 50.0%)
- `google_auth-2.49.1/google/auth/credentials.py` -> **Severity: 1.306** (Bridge: 0.0131 * Flux: 99.9671%)
- `google_auth-2.49.1/google/auth/transport/requests.py` -> **Severity: 0.888** (Bridge: 0.0089 * Flux: 99.9998%)
- `google_auth-2.49.1/google/auth/compute_engine/_metadata.py` -> **Severity: 0.475** (Bridge: 0.0048 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `google_auth-2.49.1/google/auth/__init__.py` -> **Severity: 35.787** (Embedded: 0.6735 * Error Risk: 53.1387%)
- `google_auth-2.49.1/google/auth/_default.py` -> **Severity: 18.914** (Embedded: 0.3546 * Error Risk: 53.3376%)
- `google_auth-2.49.1/google/auth/aws.py` -> **Severity: 17.963** (Embedded: 0.2482 * Error Risk: 72.3652%)
- `google_auth-2.49.1/google/oauth2/credentials.py` -> **Severity: 17.466** (Embedded: 0.2482 * Error Risk: 70.3657%)
- `google_auth-2.49.1/google/oauth2/__init__.py` -> **Severity: 16.949** (Embedded: 0.3224 * Error Risk: 52.5692%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `google_auth-2.49.1/google/auth/_default.py` -> **Severity: 11263.175** (Blast Radius: 172.702 * Doc Risk: 65.2174%)
- `google_auth-2.49.1/google/auth/transport/requests.py` -> **Severity: 1583.506** (Blast Radius: 17.698 * Doc Risk: 89.4737%)
- `google_auth-2.49.1/google/auth/compute_engine/credentials.py` -> **Severity: 1511.023** (Blast Radius: 24.99 * Doc Risk: 60.4651%)
- `google_auth-2.49.1/google/auth/transport/_http_client.py` -> **Severity: 1360.2** (Blast Radius: 13.602 * Doc Risk: 100.0%)
- `google_auth-2.49.1/google/auth/transport/__init__.py` -> **Severity: 1227.0** (Blast Radius: 30.675 * Doc Risk: 40.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7491 call pairs -- scoped 25.9%, unique 0.0%, ambiguous 8.8%, external 65.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 7491 | 25.9% | 0.0% | 8.8% | 65.3% |

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
