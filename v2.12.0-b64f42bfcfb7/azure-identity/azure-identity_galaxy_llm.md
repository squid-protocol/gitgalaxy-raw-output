# ARCHITECTURAL_BRIEF: azure-identity
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
- **Scope:** 191 analyzed artifact(s), 21688 LOC.
- **Load-bearing artifact:** `azure_identity-1.25.3/azure/identity/__init__.py` -- 85 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `azure_identity-1.25.3/azure/identity/_credentials/__init__.py` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `azure_identity-1.25.3/tests/test_managed_identity_async.py` at magnitude 1186.46 (structural weight, not risk).
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
| Total Artifacts | 198 |
| Analyzed Artifacts (Scanned) | 191 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 21688 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3241 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1922 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0067 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 183 | 21688 | 95.8% |
| MARKDOWN | 7 | 0 | 3.7% |
| PLAINTEXT | 1 | 0 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 191 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 30%, Generic / Templated Code Files 27%, Parameter Forwarders Files 8%, Encapsulated Accessors Files 7%, Data / Markup / Trivial 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 183 | 95.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 4.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 72 exceeds 500 chars)
- `.py`: 1x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (Saturation: Line 37 exceeds 500 chars)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 30.5 | 28.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.7 | 57.6 | 55.7 | 80.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.2 | 22.8 | 12.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 68.4 | 77.8 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 3.7 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 540 | 99 | 8 | `azure_identity-1.25.3/tests/test_managed_identity_async.py` |
| cleanup | 92 | 52 | 2 | `azure_identity-1.25.3/azure/identity/_credentials/shared_cache.py` |
| guards | 2439 | 151 | 36 | `azure_identity-1.25.3/tests/test_managed_identity_async.py` |
| danger | 775 | 112 | 13 | `azure_identity-1.25.3/azure/identity/_internal/aad_client_base.py` |
| concurrency | 1266 | 67 | 19 | `azure_identity-1.25.3/tests/test_managed_identity_async.py` |
| connectivity | 1580 | 178 | 19 | `azure_identity-1.25.3/tests/test_shared_cache_credential.py` |
| io | 286 | 61 | 5 | `azure_identity-1.25.3/tests/test_managed_identity_async.py` |
| crypto | 19 | 4 | 0 | `azure_identity-1.25.3/azure/identity/_credentials/certificate.py` |
| ipc | 44 | 11 | 0 | `azure_identity-1.25.3/azure/identity/_credentials/azd_cli.py` |
| time | 115 | 38 | 2 | `azure_identity-1.25.3/tests/test_managed_identity_async.py` |
| serialization | 4 | 2 | 0 | `azure_identity-1.25.3/tests/test_pickling.py` |
| regex | 8 | 4 | 0 | `azure_identity-1.25.3/tests/test_powershell_credential_async.py` |
| events | 376 | 36 | 6 | `azure_identity-1.25.3/tests/test_aad_client_async.py` |
| tests | 3423 | 82 | 57 | `azure_identity-1.25.3/tests/test_managed_identity_async.py` |
| docs | 713 | 132 | 9 | `azure_identity-1.25.3/tests/test_azd_cli_credential.py` |
| debt | 101 | 28 | 2 | `azure_identity-1.25.3/tests/integration/azure-kubernetes-service/app.py` |
| mutation | 12449 | 181 | 177 | `azure_identity-1.25.3/tests/test_shared_cache_credential.py` |
| dead_code | 648 | 77 | 13 | `azure_identity-1.25.3/tests/test_managed_identity_async.py` |
| credential | 39 | 19 | 0 | `azure_identity-1.25.3/tests/integration/azure-vms/app.py` |
| threat | 8 | 5 | 0 | `azure_identity-1.25.3/tests/test_cli_credential.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `azure_identity-1.25.3/tests/test_managed_identity_async.py` (Hits: 25)
- `azure_identity-1.25.3/tests/test_shared_cache_credential.py` (Hits: 23)
- `azure_identity-1.25.3/tests/test_shared_cache_credential_async.py` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`azure_identity-1.25.3/azure/identity/__init__.py`) — 85 inbound connections
2. **_constants.py** (`azure_identity-1.25.3/azure/identity/_constants.py`) — 64 inbound connections
3. **helpers.py** (`azure_identity-1.25.3/tests/helpers.py`) — 52 inbound connections
4. **__init__.py** (`azure_identity-1.25.3/azure/identity/_internal/__init__.py`) — 44 inbound connections
5. **_exceptions.py** (`azure_identity-1.25.3/azure/identity/_exceptions.py`) — 35 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`azure_identity-1.25.3/azure/identity/_credentials/__init__.py`) — 19 outbound dependencies
2. **default.py** (`azure_identity-1.25.3/azure/identity/_credentials/default.py`) — 18 outbound dependencies
3. **test_imds_credential_async.py** (`azure_identity-1.25.3/tests/test_imds_credential_async.py`) — 18 outbound dependencies
4. **test_powershell_credential_async.py** (`azure_identity-1.25.3/tests/test_powershell_credential_async.py`) — 18 outbound dependencies
5. **aad_client_base.py** (`azure_identity-1.25.3/azure/identity/_internal/aad_client_base.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `azure_identity-1.25.3/azure/identity/_credentials/default.py`) -> Impact: **48.3** | LOC: 170
- `__init__` **(Stateful Encapsulated Methods)** (@ `azure_identity-1.25.3/azure/identity/_credentials/managed_identity.py`) -> Impact: **46.4** | LOC: 79
- `__init__` **(Stateful Encapsulated Methods)** (@ `azure_identity-1.25.3/azure/identity/aio/_credentials/managed_identity.py`) -> Impact: **46.4** | LOC: 78
- `__init__` **(Many-Argument Workhorses)** (@ `azure_identity-1.25.3/azure/identity/_credentials/on_behalf_of.py`) -> Impact: **45.6** | LOC: 49
- `__init__` **(Stateful Encapsulated Methods)** (@ `azure_identity-1.25.3/azure/identity/aio/_credentials/on_behalf_of.py`) -> Impact: **43.3** | LOC: 44
- `resolve_tenant` **(Many-Argument Workhorses)** (@ `azure_identity-1.25.3/azure/identity/_internal/utils.py`) -> Impact: **42.8** | LOC: 51
- `__init__` **(Stateful Encapsulated Methods)** (@ `azure_identity-1.25.3/azure/identity/_internal/msal_credentials.py`) -> Impact: **39.8** | LOC: 37
- `get_client_credential` **(Many-Argument Workhorses)** (@ `azure_identity-1.25.3/azure/identity/_credentials/certificate.py`) -> Impact: **39.5** | LOC: 55
- `_process_response` **(Many-Argument Workhorses)** (@ `azure_identity-1.25.3/azure/identity/_internal/aad_client_base.py`) -> Impact: **39.2** | LOC: 68
- `__init__` **(Many-Argument Workhorses)** (@ `azure_identity-1.25.3/azure/identity/aio/_credentials/default.py`) -> Impact: **38.0** | LOC: 136

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `azure_identity-1.25.3/tests` | 70 | 14838.04 | 24.68% | 0.0% |
| `azure_identity-1.25.3/azure/identity/_credentials` | 28 | 2831.56 | 40.3% | 3.19% |
| `azure_identity-1.25.3/azure/identity/_internal` | 18 | 2543.5 | 43.48% | 0.0% |
| `azure_identity-1.25.3/azure/identity/aio/_credentials` | 23 | 2057.92 | 44.93% | 0.0% |
| `azure_identity-1.25.3/azure/identity/aio/_internal` | 6 | 434.16 | 34.57% | 0.0% |
| `azure_identity-1.25.3/samples` | 6 | 344.72 | 31.57% | 22.96% |
| `azure_identity-1.25.3/azure/identity` | 8 | 281.14 | 18.03% | 0.0% |
| `azure_identity-1.25.3/tests/integration/azure-kubernetes-service` | 1 | 117.58 | 37.32% | 0.0% |
| `azure_identity-1.25.3/tests/perfstress_tests` | 4 | 101.06 | 0.0% | 0.0% |
| `azure_identity-1.25.3/tests/integration/azure-web-apps` | 1 | 90.98 | 49.69% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `azure_identity-1.25.3/samples/credential_creation_code_snippets.py` -> **100.0%** Exposure
- `azure_identity-1.25.3/azure/identity/_credentials/shared_cache.py` -> **89.375%** Exposure
- `azure_identity-1.25.3/samples/custom_credentials.py` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `azure_identity-1.25.3/azure/identity/_constants.py` -> **100.0%** Exposure
- `azure_identity-1.25.3/azure/identity/_credentials/authorization_code.py` -> **100.0%** Exposure
- `azure_identity-1.25.3/azure/identity/_credentials/azd_cli.py` -> **100.0%** Exposure
- `azure_identity-1.25.3/azure/identity/_credentials/azure_cli.py` -> **100.0%** Exposure
- `azure_identity-1.25.3/azure/identity/_credentials/azure_ml.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `azure_identity-1.25.3/tests/test_managed_identity_async.py` -> **38** Orphaned Functions | **4** Duplicates
- `azure_identity-1.25.3/tests/test_shared_cache_credential_async.py` -> **35** Orphaned Functions | **3** Duplicates
- `azure_identity-1.25.3/samples/credential_creation_code_snippets.py` -> **31** Orphaned Functions | **2** Duplicates
- `azure_identity-1.25.3/tests/test_interactive_credential.py` -> **16** Orphaned Functions | **10** Duplicates
- `azure_identity-1.25.3/tests/test_cli_credential_async.py` -> **25** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `azure_identity-1.25.3/tests/test_environment_credential_async.py` -> **99.9089%** Exposure
- `azure_identity-1.25.3/tests/test_auth_code.py` -> **99.4496%** Exposure
- `azure_identity-1.25.3/tests/test_auth_code_async.py` -> **99.2415%** Exposure
- `azure_identity-1.25.3/azure/identity/_credentials/certificate.py` -> **99.1439%** Exposure
- `azure_identity-1.25.3/tests/test_certificate_credential.py` -> **99.1181%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1111` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `azure_identity-1.25.3/tests/test_managed_identity_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.172)
- **Top Global Matches:** file_cluster_15: 8.172, file_cluster_12: 8.28, file_cluster_11: 8.437
- **Magnitude:** 1186.46 | **LOC:** 1520 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.8%), Complexity Load (formerly Cognitive Load) (42.3%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_token_exchange` **(Many-Argument Workhorses)** (Impact: 7.1)
  * `test_azure_arc_tenant_id` **(Defensive Guards)** (Impact: 6.2)
  * `test_token_exchange_tenant_id` **(Many-Argument Workhorses)** (Impact: 6.1)
  * `test_azure_ml_tenant_id` **(I/O & Config Routines)** (Impact: 5.4)
    * *Intent:* """Azure ML: MSI_ENDPOINT, MSI_SECRET set (like App Service 2017-09-01 but with a different response...
  * `test_app_service_2019_08_01_tenant_id` **(Defensive Guards)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 103 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 639
* *State Mutation (weighted view):* 320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 309`, `args: 52`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 274`, `duplicate_logic: 4`, `unreferenced_by_name: 38`
* *Architecture:* `io: 25`, `api: 46`, `concurrency: 124`, `import: 16`
* *Defense:* `safety: 107`, `doc: 20`, `test: 179`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.imds, azure.identity._internal, azure.identity._internal.user_agent, azure.identity.aio, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_shared_cache_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.896)
- **Top Global Matches:** file_cluster_15: 7.896, file_cluster_13: 8.279, file_cluster_16: 9.053
- **Magnitude:** 1080.0 | **LOC:** 882 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (29.1%)
- **Documentation Coverage:** 30.5344% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 9.3)
  * `test_empty_cache` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* """the credential should raise CredentialUnavailableError when the cache is empty"""
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 6.3)
  * `test_claims_skips_cached_access_token` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* """When claims are provided, the credential should skip cached access tokens and request a new one""...
  * `test_authority_aliases` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* """the credential should use a refresh token valid for any known alias of its authority"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 89 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 569
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 237`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 255`, `duplicate_logic: 3`, `unreferenced_by_name: 35`
* *Architecture:* `io: 19`, `api: 41`, `concurrency: 124`, `import: 16`
* *Defense:* `safety: 69`, `doc: 27`, `test: 142`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` azure.core.exceptions, azure.core.pipeline.policies, azure.identity, azure.identity._constants, azure.identity._internal, azure.identity._internal.shared_token_cache, azure.identity._internal.user_agent, azure.identity.aio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_shared_cache_credential.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.156)
- **Top Global Matches:** file_cluster_15: 7.156, file_cluster_13: 8.064, file_cluster_16: 8.36
- **Magnitude:** 775.66 | **LOC:** 1231 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 2.424; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (71.9%), Guard Balance (formerly Safety Score) (56.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (27.6%)
- **Documentation Coverage:** 40.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_account_event` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `test_multitenant_authentication_auth_record` **(Defensive Guards)** (Impact: 11.4)
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 9.4)
  * `test_empty_cache` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* """the credential should raise CredentialUnavailableError when the cache is empty"""
  * `send` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 251`, `args: 59`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `state_mutation: 366`, `duplicate_logic: 4`
* *Architecture:* `io: 23`, `api: 58`, `import: 12`
* *Defense:* `safety: 104`, `doc: 31`, `test: 155`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.424
  * `Choke Point (Betweenness):` 0.000266 | `Ripple Effect (Closeness):` 0.015789
  * `Imports (Out-Degree: 10):` azure.core.exceptions, azure.core.pipeline.policies, azure.identity, azure.identity._constants, azure.identity._internal, azure.identity._internal.shared_token_cache, azure.identity._internal.user_agent, helpers...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `azure_identity-1.25.3/tests/test_powershell_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.555)
- **Top Global Matches:** file_cluster_15: 7.555, file_cluster_13: 8.555, file_cluster_12: 8.822
- **Magnitude:** 634.9 | **LOC:** 466 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (55.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 31.7073% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fake_exec` **(Defensive Guards)** (Impact: 18.2)
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 17.4)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 13.0)
  * `fake_exec` **(Defensive Guards)** (Impact: 12.9)
  * `test_get_token` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* """The credential should parse Azure PowerShell's output to an AccessToken"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 232
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 165`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 110`, `unreferenced_by_name: 24`
* *Architecture:* `io: 3`, `api: 28`, `concurrency: 57`, `import: 18`
* *Defense:* `safety: 36`, `doc: 19`, `test: 101`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` asyncio, azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.azure_powershell, azure.identity.aio, base64, credscan_ignore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_cli_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.129)
- **Top Global Matches:** file_cluster_15: 8.129, file_cluster_11: 8.739, file_cluster_13: 9.01
- **Magnitude:** 608.2 | **LOC:** 464 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 22.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 14.8)
  * `fake_exec` **(Defensive Guards)** (Impact: 12.8)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 11.4)
  * `fake_exec` **(Defensive Guards)** (Impact: 11.1)
  * `test_empty_claims_does_not_raise_error` **(Defensive Guards)** (Impact: 6.0)
    * *Intent:* """The credential should not raise error when claims parameter is empty or None"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 46 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 294
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 173`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 85`, `unreferenced_by_name: 25`
* *Architecture:* `io: 1`, `api: 30`, `concurrency: 64`, `import: 16`
* *Defense:* `safety: 27`, `doc: 23`, `test: 114`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` asyncio, azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.azure_cli, azure.identity.aio, datetime, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_client_secret_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.968)
- **Top Global Matches:** file_cluster_15: 7.968, file_cluster_13: 8.144, file_cluster_11: 8.874
- **Magnitude:** 573.78 | **LOC:** 425 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Credential Material (formerly Secrets Risk) (91.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.9%)
- **Documentation Coverage:** 65.5738% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 9.0)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 8.8)
  * `send` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `send` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `test_request_url` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* """the credential should accept an authority, with or without scheme, as an argument or environment ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 317
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 143`, `args: 19`, `func_start: 19`
* *Risk/State:* `state_mutation: 94`, `unreferenced_by_name: 15`
* *Architecture:* `io: 6`, `api: 19`, `concurrency: 57`, `import: 14`
* *Defense:* `safety: 57`, `doc: 6`, `test: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` azure.core.credentials, azure.core.pipeline.policies, azure.identity, azure.identity._constants, azure.identity._internal.user_agent, azure.identity.aio, helpers, helpers_async...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_azd_cli_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.186)
- **Top Global Matches:** file_cluster_15: 8.186, file_cluster_11: 8.597, file_cluster_12: 8.983
- **Magnitude:** 569.18 | **LOC:** 450 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 32.5581% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 14.8)
  * `fake_exec` **(Defensive Guards)** (Impact: 12.8)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 11.4)
  * `fake_exec` **(Defensive Guards)** (Impact: 11.1)
  * `test_empty_claims_does_not_raise_error` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* """The credential should not raise error when claims parameter is empty or None"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 40 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 259
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 171`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 87`, `unreferenced_by_name: 21`
* *Architecture:* `io: 1`, `api: 30`, `concurrency: 59`, `import: 15`
* *Defense:* `safety: 27`, `doc: 20`, `test: 106`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` asyncio, azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.azd_cli, azure.identity.aio, datetime, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/azure/identity/_internal/aad_client_base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.519)
- **Top Global Matches:** file_cluster_5: 7.519, file_cluster_12: 9.971, file_cluster_7: 10.394
- **Magnitude:** 559.6 | **LOC:** 453 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **17**; blast radius 17.005; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_process_response` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 22.3)
  * `get_cached_access_token` **(Type Conversions)** (Impact: 19.6)
    * *Intent:* # Do not return a cached token if claims are provided. if kwargs.get("claims"): return None tenant =...
  * `_get_on_behalf_of_request` **(Stateful Encapsulated Methods)** (Impact: 18.8)
  * `_get_refresh_token_on_behalf_of_request` **(Stateful Encapsulated Methods)** (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 97`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 105`
* *Architecture:* `api: 19`, `import: 19`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.005
  * `Choke Point (Betweenness):` 0.001565 | `Ripple Effect (Closeness):` 0.290646
  * `Imports (Out-Degree: 3):` .._persistent_cache, .aadclient_certificate, .utils, abc, azure.core.credentials, azure.core.exceptions, azure.core.pipeline, azure.core.pipeline.policies...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `azure_identity-1.25.3/tests/test_certificate_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.889)
- **Top Global Matches:** file_cluster_15: 7.889, file_cluster_13: 8.087, file_cluster_11: 8.477
- **Magnitude:** 553.48 | **LOC:** 455 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.1%), Complexity Load (formerly Cognitive Load) (36.9%)
- **Documentation Coverage:** 58.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 12.1)
  * `test_multitenant_authentication_backcompat` **(Defensive Guards)** (Impact: 11.8)
  * `test_request_body` **(Defensive Guards)** (Impact: 8.6)
  * `test_token_cache_persistent` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* """the credential should optionally use a persistent cache, and default to an in memory cache"""
  * `test_request_url` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* """the credential should accept an authority, with or without scheme, as an argument or environment ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 45 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 279
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 157`, `args: 22`, `func_start: 22`
* *Risk/State:* `state_mutation: 83`, `unreferenced_by_name: 17`
* *Architecture:* `io: 9`, `api: 22`, `concurrency: 54`, `import: 12`
* *Defense:* `safety: 58`, `doc: 9`, `test: 80`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` azure.core.pipeline.policies, azure.identity, azure.identity._constants, azure.identity._internal.user_agent, azure.identity.aio, helpers, helpers_async, msal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_certificate_credential.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.405)
- **Top Global Matches:** file_cluster_15: 7.405, file_cluster_13: 8.124, file_cluster_11: 8.268
- **Magnitude:** 476.66 | **LOC:** 633 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **17**; blast radius 3.424; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (99.1%), Connectivity (formerly Api Exposure) (70.1%), Guard Balance (formerly Safety Score) (52.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 46.5753% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_jwt_ps256` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* """Validate the request meets Microsoft Entra ID's expectations for a client credential grant using ...
  * `validate_jwt` **(Defensive Guards)** (Impact: 24.2)
    * *Intent:* """Validate the request meets Microsoft Entra ID's expectations for a client credential grant using ...
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 14.2)
  * `test_multitenant_authentication_backcompat` **(Defensive Guards)** (Impact: 14.0)
  * `test_token_cache_persistent` **(Defensive Guards)** (Impact: 8.1)
    * *Intent:* """the credential should use a persistent cache if cache_persistence_options are configured"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 175`, `args: 27`, `func_start: 25`
* *Risk/State:* `state_mutation: 132`, `duplicate_logic: 2`
* *Architecture:* `io: 18`, `api: 25`, `import: 18`
* *Defense:* `safety: 86`, `doc: 14`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.424
  * `Choke Point (Betweenness):` 0.002723 | `Ripple Effect (Closeness):` 0.031579
  * `Imports (Out-Degree: 7):` azure.core.pipeline.policies, azure.identity, azure.identity._constants, azure.identity._credentials.certificate, azure.identity._enums, azure.identity._internal.user_agent, cryptography, cryptography.hazmat.backends...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `azure_identity-1.25.3/tests/test_imds_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.346)
- **Top Global Matches:** file_cluster_12: 7.346, file_cluster_15: 8.809, file_cluster_11: 9.446
- **Magnitude:** 455.14 | **LOC:** 401 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.0%)
- **Documentation Coverage:** 73.2143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_imds_retry_policy` **(Defensive Guards)** (Impact: 12.0)
  * `test_cache` **(Defensive Guards)** (Impact: 4.8)
  * `test_imds_credential_uses_custom_retry_policy` **(Defensive Guards)** (Impact: 4.5)
  * `test_system_assigned_tenant_id` **(Defensive Guards)** (Impact: 4.4)
  * `test_user_assigned_tenant_id` **(Defensive Guards)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 232
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 116`, `args: 24`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 84`, `unreferenced_by_name: 18`
* *Architecture:* `io: 5`, `api: 21`, `concurrency: 42`, `import: 19`
* *Defense:* `safety: 36`, `doc: 5`, `test: 63`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` azure.core.exceptions, azure.core.pipeline, azure.core.pipeline.policies, azure.core.rest, azure.identity, azure.identity._constants, azure.identity._credentials.imds, azure.identity._internal.user_agent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_managed_identity.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.575)
- **Top Global Matches:** file_cluster_15: 7.575, file_cluster_11: 7.657, file_cluster_13: 8.031
- **Magnitude:** 449.92 | **LOC:** 1216 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 2.142; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (58.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.1%), Complexity Load (formerly Cognitive Load) (28.2%)
- **Documentation Coverage:** 60.9524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_token_exchange` **(Many-Argument Workhorses)** (Impact: 7.1)
  * `test_token_exchange_tenant_id` **(Many-Argument Workhorses)** (Impact: 6.0)
  * `test_azure_ml_tenant_id` **(I/O & Config Routines)** (Impact: 5.2)
  * `test_app_service_2019_08_01_tenant_id` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* """App Service 2019-08-01: IDENTITY_ENDPOINT, IDENTITY_HEADER set"""
  * `test_claims_propagated` **(Defensive Guards)** (Impact: 5.0)
    * *Intent:* """Test that claims passed are forwarded to MSAL's acquire_token_for_client."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 217`, `args: 38`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 221`, `duplicate_logic: 4`
* *Architecture:* `io: 18`, `api: 37`, `import: 14`
* *Defense:* `safety: 96`, `doc: 16`, `test: 116`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005263
  * `Imports (Out-Degree: 7):` azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.imds, azure.identity._credentials.managed_identity, azure.identity._internal, azure.identity._internal.user_agent, helpers...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `azure_identity-1.25.3/tests/test_obo_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.808)
- **Top Global Matches:** file_cluster_11: 7.808, file_cluster_15: 7.856, file_cluster_13: 8.532
- **Magnitude:** 443.58 | **LOC:** 378 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.8%), Complexity Load (formerly Cognitive Load) (36.6%)
- **Documentation Coverage:** 63.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 9.5)
  * `test_refresh_token` **(Defensive Guards)** (Impact: 8.8)
  * `send` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `send` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `load_settings` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 209
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 128`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`, `unreferenced_by_name: 15`
* *Architecture:* `io: 8`, `api: 23`, `concurrency: 44`, `import: 17`
* *Defense:* `safety: 39`, `doc: 8`, `test: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` azure.core.pipeline.policies, azure.identity, azure.identity._constants, azure.identity._internal.aad_client_base, azure.identity._internal.user_agent, azure.identity.aio, devtools_testutils, devtools_testutils.aio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_azd_cli_credential.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.296)
- **Top Global Matches:** file_cluster_15: 7.296, file_cluster_13: 7.988, file_cluster_11: 8.771
- **Magnitude:** 390.6 | **LOC:** 600 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 2.214; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (68.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.4%), Complexity Load (formerly Cognitive Load) (24.4%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 14.8)
  * `fake_check_output` **(Defensive Guards)** (Impact: 12.8)
  * `fake_check_output` **(Defensive Guards)** (Impact: 12.8)
  * `test_multitenant_authentication_class` **(Defensive Guards)** (Impact: 11.4)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 179`, `args: 44`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `state_mutation: 110`, `duplicate_logic: 2`
* *Architecture:* `api: 45`, `import: 11`
* *Defense:* `safety: 51`, `doc: 48`, `test: 116`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.214
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005263
  * `Imports (Out-Degree: 4):` azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.azd_cli, datetime, helpers, json, pytest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `azure_identity-1.25.3/tests/test_auth_code_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.018)
- **Top Global Matches:** file_cluster_15: 7.018, file_cluster_11: 7.759, file_cluster_13: 8.445
- **Magnitude:** 351.48 | **LOC:** 267 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Credential Material (formerly Secrets Risk) (99.2%), Guard Balance (formerly Safety Score) (56.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 10.6)
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 9.2)
  * `send` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `send` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `test_auth_code_credential` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 175
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 80`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 62`, `unreferenced_by_name: 9`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 30`, `import: 11`
* *Defense:* `safety: 26`, `doc: 1`, `test: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` azure.core.exceptions, azure.core.pipeline.policies, azure.identity._constants, azure.identity._internal.user_agent, azure.identity.aio, helpers, helpers_async, msal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/azure/identity/_internal/shared_token_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.301)
- **Top Global Matches:** file_cluster_5: 8.301, file_cluster_7: 11.549, file_cluster_12: 11.702
- **Magnitude:** 342.26 | **LOC:** 292 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 3.276; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 88.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_account` **(Stateful Encapsulated Methods)** (Impact: 30.8)
  * `_get_cached_access_token` **(Stateful Encapsulated Methods)** (Impact: 19.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 18.3)
  * `_initialize_cache` **(Stateful Encapsulated Methods)** (Impact: 16.8)
    * *Intent:* # If no cache options were provided, the default cache will be used. This credential accepts the # u...
  * `_filtered_accounts` **(Stateful Encapsulated Methods)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 62`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 65`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.276
  * `Choke Point (Betweenness):` 0.000151 | `Ripple Effect (Closeness):` 0.157389
  * `Imports (Out-Degree: 6):` ..CredentialUnavailableError, .._constants, .._internal, .._persistent_cache, abc, azure.core.credentials, msal, platform...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `azure_identity-1.25.3/tests/test_cli_credential.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.459)
- **Top Global Matches:** file_cluster_15: 7.459, file_cluster_13: 8.537, file_cluster_11: 8.749
- **Magnitude:** 323.22 | **LOC:** 461 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 2.214; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (63.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%), Complexity Load (formerly Cognitive Load) (22.9%)
- **Documentation Coverage:** 28.0899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 14.8)
  * `fake_check_output` **(Defensive Guards)** (Impact: 12.8)
  * `fake_check_output` **(Defensive Guards)** (Impact: 12.8)
  * `test_multitenant_authentication_class` **(Defensive Guards)** (Impact: 11.4)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 141`, `args: 29`, `func_start: 29`
* *Risk/State:* `state_mutation: 78`, `duplicate_logic: 2`
* *Architecture:* `api: 29`, `import: 12`
* *Defense:* `safety: 31`, `doc: 21`, `test: 107`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.214
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005263
  * `Imports (Out-Degree: 4):` azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.azure_cli, datetime, helpers, itertools, json...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `azure_identity-1.25.3/tests/test_default_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.447)
- **Top Global Matches:** file_cluster_10: 8.447, file_cluster_13: 8.565, file_cluster_11: 8.771
- **Magnitude:** 317.64 | **LOC:** 427 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.8%), Complexity Load (formerly Cognitive Load) (35.7%)
- **Documentation Coverage:** 58.6957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_authority` **(Type Conversions)** (Impact: 11.2)
    * *Intent:* """the credential should accept authority configuration by keyword argument or environment"""
  * `test_initialization` **(Defensive Guards)** (Impact: 7.8)
  * `assert_credentials_not_present` **(Defensive Guards)** (Impact: 5.8)
  * `test_exclude_options` **(Defensive Guards)** (Impact: 5.7)
  * `get_credential_for_shared_cache_test` **(Callbacks & Closures)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 128
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 146`, `args: 22`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `api: 18`, `concurrency: 28`, `import: 14`
* *Defense:* `safety: 32`, `doc: 8`, `test: 80`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` azure.core.credentials, azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity.aio, azure.identity.aio._credentials.default, helpers, helpers_async...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_client_secret_credential.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.128)
- **Top Global Matches:** file_cluster_15: 7.128, file_cluster_13: 7.778, file_cluster_10: 8.208
- **Magnitude:** 314.68 | **LOC:** 456 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (90.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.6%), Complexity Load (formerly Cognitive Load) (30.7%)
- **Documentation Coverage:** 53.9683% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 10.5)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 10.1)
  * `send` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `send` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* # ensure the `claims` and `tenant_id` keywords from credential's `get_token` method don't make it to...
  * `test_regional_authority` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* """the credential should configure MSAL with a regional authority specified via kwarg or environment...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 131`, `args: 22`, `func_start: 20`
* *Risk/State:* `state_mutation: 103`, `duplicate_logic: 2`, `unreferenced_by_name: 16`
* *Architecture:* `io: 5`, `api: 20`, `import: 12`
* *Defense:* `safety: 63`, `doc: 9`, `test: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` azure.core.pipeline.policies, azure.identity, azure.identity._constants, azure.identity._enums, azure.identity._internal.user_agent, helpers, itertools, msal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_aad_client_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.859)
- **Top Global Matches:** file_cluster_15: 7.859, file_cluster_13: 8.989, file_cluster_11: 8.996
- **Magnitude:** 314.4 | **LOC:** 327 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (43.5%), Guard Balance (formerly Safety Score) (41.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_retries_token_requests` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* """The client should retry token requests"""
  * `test_error_reporting` **(Defensive Guards)** (Impact: 4.3)
  * `test_multitenant_cache` **(I/O & Config Routines)** (Impact: 4.2)
  * `test_request_url` **(Defensive Guards)** (Impact: 4.1)
  * `test_exceptions_do_not_expose_secrets` **(Defensive Guards)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 147
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 124`, `args: 18`, `func_start: 18`
* *Risk/State:* `state_mutation: 83`, `duplicate_logic: 2`, `unreferenced_by_name: 10`
* *Architecture:* `io: 1`, `api: 18`, `concurrency: 37`, `import: 12`
* *Defense:* `safety: 46`, `doc: 3`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` azure.core.exceptions, azure.identity._constants, azure.identity._internal, azure.identity.aio._internal.aad_client, functools, helpers, helpers_async, msal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_get_token_mixin_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.018)
- **Top Global Matches:** file_cluster_15: 9.018, file_cluster_13: 9.12, file_cluster_11: 9.773
- **Magnitude:** 297.38 | **LOC:** 223 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.9%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 21.7391% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_retry_delay` **(Type Conversions)** (Impact: 3.5)
    * *Intent:* """A credential should wait between requests when trying to refresh a token"""
  * `test_token_acquisition_failure` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* """When the credential has no token cached, every get_token call should prompt a token request"""
  * `test_expired_token_propagates_error` **(Type Conversions)** (Impact: 3.3)
    * *Intent:* """When a cached token is expired (required), request failures should propagate, not be swallowed.""...
  * `test_tenant_id` **(Defensive Guards)** (Impact: 3.2)
  * `_acquire_token_silently` **(Encapsulated Accessors)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 168
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 67`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`, `unreferenced_by_name: 17`
* *Architecture:* `api: 16`, `concurrency: 33`, `import: 7`
* *Defense:* `safety: 15`, `doc: 12`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` azure.core.credentials, azure.identity._constants, azure.identity.aio._internal.get_token_mixin, helpers, pytest, time, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_default.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.054)
- **Top Global Matches:** file_cluster_15: 8.054, file_cluster_11: 8.29, file_cluster_13: 8.325
- **Magnitude:** 288.26 | **LOC:** 584 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.8%), Complexity Load (formerly Cognitive Load) (22.1%), Connectivity (formerly Api Exposure) (10.6%)
- **Documentation Coverage:** 53.7313% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_authority` **(Type Conversions)** (Impact: 11.1)
    * *Intent:* """the credential should accept authority configuration by keyword argument or environment"""
  * `test_exclude_options` **(Defensive Guards)** (Impact: 9.8)
  * `test_initialization` **(Defensive Guards)** (Impact: 7.8)
  * `assert_credentials_not_present` **(Defensive Guards)** (Impact: 5.8)
  * `get_credential_for_shared_cache_test` **(Many-Argument Workhorses)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 189`, `args: 31`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 104`, `unreferenced_by_name: 23`
* *Architecture:* `io: 3`, `api: 28`, `import: 19`
* *Defense:* `safety: 54`, `doc: 14`, `test: 90`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` azure.core.credentials, azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._credentials.azd_cli, azure.identity._credentials.azure_cli, azure.identity._credentials.broker, azure.identity._credentials.default...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_chained_token_credential_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.444)
- **Top Global Matches:** file_cluster_10: 7.444, file_cluster_15: 8.934, file_cluster_13: 9.225
- **Magnitude:** 270.28 | **LOC:** 307 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.8%), Guard Balance (formerly Safety Score) (36.6%)
- **Documentation Coverage:** 77.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_chain_attempts_all_credentials` **(Callbacks & Closures)** (Impact: 4.2)
  * `test_context_manager` **(Defensive Guards)** (Impact: 3.5)
  * `test_managed_identity_imds_probe` **(I/O & Config Routines)** (Impact: 3.5)
  * `test_close` **(Defensive Guards)** (Impact: 3.4)
  * `test_chain_raises_for_unexpected_error` **(Callbacks & Closures)** (Impact: 3.0)
    * *Intent:* """the chain should not continue after an unexpected error (i.e. anything but CredentialUnavailableE...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 149
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 72`, `args: 34`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `planned_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 11`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 39`, `import: 11`
* *Defense:* `safety: 17`, `doc: 4`, `test: 98`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` azure.core.credentials, azure.core.exceptions, azure.identity, azure.identity._credentials.imds, azure.identity._internal.user_agent, azure.identity.aio, helpers, helpers_async...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/test_interactive_credential.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.286)
- **Top Global Matches:** file_cluster_12: 7.286, file_cluster_15: 8.495, file_cluster_16: 8.495
- **Magnitude:** 257.96 | **LOC:** 468 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.974; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.9%), Complexity Load (formerly Cognitive Load) (26.2%), Connectivity (formerly Api Exposure) (9.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multitenant_authentication` **(Defensive Guards)** (Impact: 9.7)
  * `__init__` **(Encapsulated Accessors)** (Impact: 7.5)
  * `test_multitenant_authentication_not_allowed` **(Defensive Guards)** (Impact: 6.4)
  * `request_token` **(Compute Cores)** (Impact: 5.8)
  * `test_token_cache_persistent` **(Defensive Guards)** (Impact: 5.3)
    * *Intent:* """the credential should default to an in memory cache, and optionally use a persistent cache"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 139`, `args: 37`, `func_start: 35`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 78`, `duplicate_logic: 10`, `unreferenced_by_name: 16`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 49`, `doc: 15`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` azure.core.exceptions, azure.identity, azure.identity._constants, azure.identity._internal, helpers, msal, pytest, unittest.mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `azure_identity-1.25.3/tests/helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.747)
- **Top Global Matches:** file_cluster_4: 6.747, file_cluster_12: 9.203, file_cluster_15: 9.824
- **Magnitude:** 249.72 | **LOC:** 220 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **6**; blast radius 24.283; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (94.2%), Guard Balance (formerly Safety Score) (74.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_matches` **(Compute Cores)** (Impact: 35.1)
  * `build_aad_response` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `mock_response` **(Callbacks & Closures)** (Impact: 8.6)
  * `id_token_claims` **(Type Conversions)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 43`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 46`
* *Architecture:* `io: 7`, `api: 16`, `import: 6`
* *Defense:* `safety: 7`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.283
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.27406
  * `Imports (Out-Degree: 0):` azure.core.credentials, base64, json, time, unittest, urllib.parse
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `azure_identity-1.25.3/tests/test_default_async.py` (PYTHON) | Magnitude: 317.64 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 242, structural_boundaries: 146, core_var_decl: 100, design_snake_case: 99
- `azure_identity-1.25.3/tests/test_browser_credential.py` (PYTHON) | Magnitude: 113.28 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 71, test: 56, core_var_decl: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `azure_identity-1.25.3/tests/test_obo_async.py` (PYTHON) | Magnitude: 443.58 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 248, structural_boundaries: 128, core_var_decl: 102, design_snake_case: 102
- `azure_identity-1.25.3/tests/integration/test_azure_functions.py` (PYTHON) | Magnitude: 17.78 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 13, test: 10, core_var_decl: 9
- `azure_identity-1.25.3/tests/integration/test_azure_web_apps.py` (PYTHON) | Magnitude: 23.78 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 13, test: 10, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `azure_identity-1.25.3/tests/test_environment_credential_async.py` (PYTHON) | Magnitude: 140.3 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 82, core_var_decl: 45, design_snake_case: 44
- `azure_identity-1.25.3/azure/identity/_credentials/browser.py` (PYTHON) | Magnitude: 117.98 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 29, structural_boundaries: 28, core_var_decl: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `azure_identity-1.25.3/tests/test_azure_arc.py` (PYTHON) | Magnitude: 9.08 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 7, import: 5, test: 4
- `azure_identity-1.25.3/tests/managed-identity-live/test_cloud_shell.py` (PYTHON) | Magnitude: 8.4 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, core_var_decl: 6, design_snake_case: 6
- `azure_identity-1.25.3/tests/test_app_service.py` (PYTHON) | Magnitude: 45.74 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 30, test: 19, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `azure_identity-1.25.3/tests/test_device_code_credential.py` (PYTHON) | Magnitude: 167.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 298, core_var_decl: 141, design_snake_case: 141, state_mutation: 81
- `azure_identity-1.25.3/tests/test_username_password_credential.py` (PYTHON) | Magnitude: 106.94 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, core_var_decl: 76, design_snake_case: 76, state_mutation: 47
- `azure_identity-1.25.3/tests/test_auth_record.py` (PYTHON) | Magnitude: 18.46 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, safety: 8, state_mutation: 6
- `azure_identity-1.25.3/tests/test_managed_identity.py` (PYTHON) | Magnitude: 449.92 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 965, core_var_decl: 372, design_snake_case: 369, state_mutation: 221
- `azure_identity-1.25.3/tests/test_get_token_mixin_async.py` (PYTHON) | Magnitude: 297.38 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 67, core_var_decl: 59, design_snake_case: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `azure_identity-1.25.3/azure/identity/_credentials/__init__.py` (PYTHON) | Magnitude: 17.82 | Delta: **0.167** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 20, import: 19, api: 1
- `azure_identity-1.25.3/azure/identity/aio/_credentials/__init__.py` (PYTHON) | Magnitude: 17.68 | Delta: **0.193** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 32, import: 16, indent_spaces: 16, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `azure_identity-1.25.3/tests/test_initialization.py` (PYTHON) | Magnitude: 7.3 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 73, indent_spaces: 56, structural_boundaries: 44, test: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `azure_identity-1.25.3/azure/identity/_credentials/azure_arc.py` (PYTHON) | Magnitude: 66.8 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 41, branch: 15, core_var_decl: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `azure_identity-1.25.3/azure/identity/aio/_credentials/workload_identity.py` (PYTHON) | Magnitude: 52.34 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 14, state_mutation: 10, core_var_decl: 10
- `azure_identity-1.25.3/azure/identity/_credentials/on_behalf_of.py` (PYTHON) | Magnitude: 124.64 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 31, branch: 25, core_var_decl: 23

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `azure_identity-1.25.3/azure/identity/_credentials/managed_identity.py` -> **Severity: 2.912** (Bridge: 0.0291 * Flux: 100.0%)
- `azure_identity-1.25.3/azure/identity/__init__.py` -> **Severity: 2.701** (Bridge: 0.0984 * Flux: 27.4596%)
- `azure_identity-1.25.3/azure/identity/_internal/__init__.py` -> **Severity: 2.626** (Bridge: 0.0265 * Flux: 99.1837%)
- `azure_identity-1.25.3/azure/identity/_credentials/__init__.py` -> **Severity: 1.408** (Bridge: 0.0838 * Flux: 16.7982%)
- `azure_identity-1.25.3/azure/identity/aio/_credentials/managed_identity.py` -> **Severity: 1.361** (Bridge: 0.0136 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `azure_identity-1.25.3/azure/identity/_constants.py` -> **Severity: 35.165** (Embedded: 0.4718 * Error Risk: 74.5411%)
- `azure_identity-1.25.3/azure/identity/_internal/aad_client_base.py` -> **Severity: 24.989** (Embedded: 0.2906 * Error Risk: 85.9764%)
- `azure_identity-1.25.3/azure/identity/_internal/utils.py` -> **Severity: 23.357** (Embedded: 0.3592 * Error Risk: 65.0245%)
- `azure_identity-1.25.3/azure/identity/_persistent_cache.py` -> **Severity: 23.341** (Embedded: 0.3348 * Error Risk: 69.7158%)
- `azure_identity-1.25.3/azure/identity/_internal/aad_client.py` -> **Severity: 22.583** (Embedded: 0.2823 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `azure_identity-1.25.3/azure/identity/_constants.py` -> **Severity: 7388.0** (Blast Radius: 73.88 * Doc Risk: 100.0%)
- `azure_identity-1.25.3/tests/helpers.py` -> **Severity: 1942.64** (Blast Radius: 24.283 * Doc Risk: 80.0%)
- `azure_identity-1.25.3/azure/identity/_internal/utils.py` -> **Severity: 1805.876** (Blast Radius: 43.341 * Doc Risk: 41.6667%)
- `azure_identity-1.25.3/azure/identity/_persistent_cache.py` -> **Severity: 1763.4** (Blast Radius: 17.634 * Doc Risk: 100.0%)
- `azure_identity-1.25.3/azure/identity/_internal/aad_client_base.py` -> **Severity: 1700.5** (Blast Radius: 17.005 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6286 call pairs -- scoped 37.8%, unique 0.0%, ambiguous 3.5%, external 58.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 6286 | 37.8% | 0.0% | 3.5% | 58.7% |

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
