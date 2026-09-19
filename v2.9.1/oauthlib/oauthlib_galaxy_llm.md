# ARCHITECTURAL_BRIEF: oauthlib
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 154 analyzed artifact(s), 11522 LOC.
- **Load-bearing artifact:** `oauthlib-3.3.1/oauthlib/common.py` -- 47 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/signature.py` -- pulls in 11 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/signature.py` at magnitude 403.36 (structural weight, not risk).
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
| Total Artifacts | 159 |
| Analyzed Artifacts (Scanned) | 154 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 11522 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5624 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3449 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4033 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 153 | 11522 | 99.4% |
| PLAINTEXT | 1 | 0 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.878`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.88; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 42%, Data / Markup / Trivial 21%, Many-Argument Workhorses Files 20%, Large Core Modules (3) 5%, Declarative / Non-Code 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 153 | 99.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.2 | 18.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 58.5 | 71.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 98.1 | 23.7 | 10.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 27.1 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 70.8 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.8 | 66.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 92 | 29 | 2 | `oauthlib-3.3.1/oauthlib/common.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 251 | 50 | 5 | `oauthlib-3.3.1/oauthlib/common.py` |
| danger | 320 | 57 | 7 | `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py` |
| concurrency | 1 | 1 | 0 | `oauthlib-3.3.1/setup.py` |
| connectivity | 1180 | 119 | 17 | `oauthlib-3.3.1/tests/oauth1/rfc5849/endpoints/test_base.py` |
| io | 6 | 5 | 0 | `oauthlib-3.3.1/setup.py` |
| crypto | 8 | 6 | 0 | `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/signature.py` |
| ipc | 1 | 1 | 0 | `oauthlib-3.3.1/setup.py` |
| time | 25 | 16 | 1 | `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_base.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 5 | 2 | 0 | `oauthlib-3.3.1/oauthlib/uri_validate.py` |
| events | 60 | 12 | 0 | `oauthlib-3.3.1/oauthlib/openid/connect/core/grant_types/dispatchers.py` |
| tests | 1073 | 58 | 19 | `oauthlib-3.3.1/tests/oauth2/rfc6749/test_server.py` |
| docs | 497 | 105 | 8 | `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/request_validator.py` |
| debt | 78 | 29 | 1 | `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/request_validator.py` |
| mutation | 5814 | 119 | 104 | `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_base.py` |
| dead_code | 422 | 57 | 8 | `oauthlib-3.3.1/tests/oauth1/rfc5849/endpoints/test_base.py` |
| credential | 23 | 10 | 0 | `oauthlib-3.3.1/tests/oauth1/rfc5849/test_signatures.py` |
| threat | 99 | 26 | 3 | `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/request_validator.py` |
| ml_ai | 7 | 5 | 0 | `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_service_application.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `oauthlib-3.3.1/setup.py` (Hits: 2)
- `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/__init__.py` (Hits: 1)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/clients/service_application.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **common.py** (`oauthlib-3.3.1/oauthlib/common.py`) — 47 inbound connections
2. **tokens.py** (`oauthlib-3.3.1/oauthlib/oauth2/rfc6749/tokens.py`) — 17 inbound connections
3. **errors.py** (`oauthlib-3.3.1/oauthlib/oauth2/rfc6749/errors.py`) — 10 inbound connections
4. **token.py** (`oauthlib-3.3.1/oauthlib/oauth2/rfc6749/endpoints/token.py`) — 5 inbound connections
5. **utils.py** (`oauthlib-3.3.1/oauthlib/oauth2/rfc6749/utils.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **signature.py** (`oauthlib-3.3.1/oauthlib/oauth1/rfc5849/signature.py`) — 11 outbound dependencies
2. **common.py** (`oauthlib-3.3.1/oauthlib/common.py`) — 10 outbound dependencies
3. **__init__.py** (`oauthlib-3.3.1/oauthlib/oauth2/__init__.py`) — 10 outbound dependencies
4. **authorization_code.py** (`oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py`) — 10 outbound dependencies
5. **test_server.py** (`oauthlib-3.3.1/tests/oauth2/rfc6749/test_server.py`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `prepare_mac_header` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/tokens.py`) -> Impact: **77.9** | LOC: 104
- `sign` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/__init__.py`) -> Impact: **60.7** | LOC: 103
  * *Intent:* """Sign a request Signs an HTTP request with the specified parts. Returns a 3-tuple of the signed request's URI, headers, and body. Note that http_met...
- `prepare_request_body` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/clients/service_application.py`) -> Impact: **60.4** | LOC: 126
- `validate_token_request` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py`) -> Impact: **52.2** | LOC: 109
  * *Intent:* """ :param request: OAuthlib request. :type request: oauthlib.common.Request """
- `validate_metadata` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/endpoints/metadata.py`) -> Impact: **46.5** | LOC: 24
- `collect_parameters` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/signature.py`) -> Impact: **38.5** | LOC: 85
- `validate_authorization_request` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py`) -> Impact: **35.2** | LOC: 115
  * *Intent:* """Check the authorization request for normal and fatal errors. A normal error could be a missing response_type parameter or the client attempting to ...
- `openid_authorization_validator` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/openid/connect/core/grant_types/base.py`) -> Impact: **35.1** | LOC: 182
  * *Intent:* """Perform OpenID Connect specific authorization request validation. nonce OPTIONAL. String value used to associate a Client session with an ID Token,...
- `validate_token_request` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types/refresh_token.py`) -> Impact: **34.4** | LOC: 65
  * *Intent:* """ :param request: OAuthlib request. :type request: oauthlib.common.Request """
- `_check_signature` **(Many-Argument Workhorses)** (@ `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/endpoints/base.py`) -> Impact: **33.1** | LOC: 62
  * *Intent:* # ---- RSA Signature verification ---- if request.signature_method in {SIGNATURE_RSA_SHA1, SIGNATURE_RSA_SHA256, SIGNATURE_RSA_SHA512}: # RSA-based si...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `oauthlib-3.3.1/oauthlib/oauth2/rfc6749` | 6 | 1146.74 | 26.27% | 26.3% |
| `oauthlib-3.3.1/oauthlib/oauth1/rfc5849` | 6 | 1017.64 | 35.23% | 17.53% |
| `oauthlib-3.3.1/tests/oauth2/rfc6749/endpoints` | 12 | 832.36 | 36.74% | 0.0% |
| `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types` | 7 | 682.66 | 30.68% | 4.95% |
| `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/clients` | 7 | 631.88 | 20.77% | 1.69% |
| `oauthlib-3.3.1/tests/oauth2/rfc6749/grant_types` | 6 | 576.14 | 28.97% | 0.0% |
| `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/endpoints` | 8 | 521.26 | 29.25% | 17.28% |
| `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/endpoints` | 9 | 521.0 | 31.5% | 11.11% |
| `oauthlib-3.3.1/tests/oauth1/rfc5849/endpoints` | 7 | 476.06 | 9.45% | 0.0% |
| `oauthlib-3.3.1/tests/oauth2/rfc6749` | 6 | 463.92 | 12.24% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/request_validator.py` -> **100.0%** Exposure
- `oauthlib-3.3.1/oauthlib/openid/connect/core/grant_types/dispatchers.py` -> **100.0%** Exposure
- `oauthlib-3.3.1/oauthlib/openid/connect/core/request_validator.py` -> **99.9925%** Exposure
- `oauthlib-3.3.1/oauthlib/uri_validate.py` -> **78.1356%** Exposure
- `oauthlib-3.3.1/setup.py` -> **76.9183%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `oauthlib-3.3.1/oauthlib/common.py` -> **100.0%** Exposure
- `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/__init__.py` -> **100.0%** Exposure
- `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/endpoints/authorization.py` -> **100.0%** Exposure
- `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/endpoints/base.py` -> **100.0%** Exposure
- `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/endpoints/request_token.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `oauthlib-3.3.1/tests/oauth1/rfc5849/endpoints/test_base.py` -> **40** Orphaned Functions | **0** Duplicates
- `oauthlib-3.3.1/tests/test_common.py` -> **32** Orphaned Functions | **0** Duplicates
- `oauthlib-3.3.1/tests/oauth1/rfc5849/test_client.py` -> **25** Orphaned Functions | **0** Duplicates
- `oauthlib-3.3.1/tests/oauth2/rfc6749/endpoints/test_error_responses.py` -> **23** Orphaned Functions | **0** Duplicates
- `oauthlib-3.3.1/tests/oauth2/rfc6749/grant_types/test_resource_owner_password.py` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_backend_application.py` -> **100.0%** Exposure
- `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_legacy_application.py` -> **99.9954%** Exposure
- `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_service_application.py` -> **99.9913%** Exposure
- `oauthlib-3.3.1/tests/oauth1/rfc5849/test_signatures.py` -> **99.9595%** Exposure
- `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_web_application.py` -> **99.5195%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `499` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/signature.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 403.36 | **LOC:** 853 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 6.985; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 68.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `collect_parameters` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `base_string_uri` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* """ Calculates the _base string URI_. The *base string URI* is one of the components that make up th...
  * `_verify_hmac` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `verify_plaintext` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* """Verify a PLAINTEXT signature. Per `section 3.4`_ of the spec. .. _`section 3.4`: https://tools.ie...
  * `_sign_hmac` **(Many-Argument Workhorses)** (Impact: 9.9)
    * *Intent:* # ==== Common functions for HMAC-based signature methods =========
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 76`, `args: 29`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 73`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 10`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.985
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 1):` , binascii, contextlib, hashlib, hmac, ipaddress, jwt.algorithms, logging...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/tokens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 370.58 | **LOC:** 351 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **8**; blast radius 35.703; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.1%)
- **Documentation Coverage:** 51.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_mac_header` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `create_token` **(Many-Argument Workhorses)** (Impact: 24.3)
    * *Intent:* """ Create a BearerToken, by default without refresh token. :param request: OAuthlib request. :type ...
  * `__init__` **(Encapsulated Accessors)** (Impact: 10.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.2)
  * `get_token_from_header` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* """ Helper function to extract a token from the request header. :param request: OAuthlib request. :t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 59`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 59`, `planned_debt: 3`
* *Architecture:* `api: 24`, `import: 8`
* *Defense:* `safety: 1`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.703
  * `Choke Point (Betweenness):` 0.000265 | `Ripple Effect (Closeness):` 0.115294
  * `Imports (Out-Degree: 1):` , binascii, hashlib, hmac, oauthlib, oauthlib.common, urllib.parse, warnings
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/clients/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 369.86 | **LOC:** 598 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.3%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_token` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `prepare_authorization_request` **(Many-Argument Workhorses)** (Impact: 17.7)
  * `populate_token_attributes` **(Stateful Encapsulated Methods)** (Impact: 16.8)
    * *Intent:* """Add attributes from a token exchange response to self."""
  * `prepare_token_request` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `_add_bearer_token` **(Stateful Encapsulated Methods)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 48`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 9`
* *Defense:* `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` base64, hashlib, oauthlib.common, oauthlib.oauth2.rfc6749, oauthlib.oauth2.rfc6749.errors, oauthlib.oauth2.rfc6749.parameters, oauthlib.oauth2.rfc6749.utils, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/oauthlib/common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 364.74 | **LOC:** 434 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **10**; blast radius 211.683; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (98.1%), Guard Balance (formerly Safety Score) (94.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 60.6557% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `to_unicode` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* """Convert a number of different types of objects to unicode."""
  * `extract_params` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* """Extract parameters and return them as a list of 2-tuples. Will successfully extract parameters fr...
  * `encode_params_utf8` **(Defensive Guards)** (Impact: 9.0)
    * *Intent:* """Ensures that all parameters in a list of 2-element tuples are encoded to bytestrings using UTF-8 ...
  * `decode_params_utf8` **(Defensive Guards)** (Impact: 9.0)
    * *Intent:* """Ensures that all parameters in a list of 2-element tuples are decoded to unicode using UTF-8. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 90`, `args: 31`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 64`
* *Architecture:* `api: 31`, `import: 12`
* *Defense:* `safety: 26`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 211.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.357298
  * `Imports (Out-Degree: 0):` , collections, datetime, jwt, logging, random, re, secrets...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/parameters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 339.54 | **LOC:** 529 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 7.667; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (50.4%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_grant_uri` **(Many-Argument Workhorses)** (Impact: 28.6)
  * `prepare_token_request` **(Many-Argument Workhorses)** (Impact: 23.5)
    * *Intent:* """Prepare the access token request. The client makes a request to the token endpoint by adding the ...
  * `parse_implicit_response` **(Many-Argument Workhorses)** (Impact: 23.5)
    * *Intent:* """Parse the implicit token response URI into a dict. If the resource owner grants the access reques...
  * `prepare_token_revocation_request` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `parse_expires` **(Defensive Guards)** (Impact: 18.3)
    * *Intent:* """Parse `expires_in`, `expires_at` fields from params Parse following these rules: - `expires_in` m...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 32`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 60`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 13`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.667
  * `Choke Point (Betweenness):` 0.000193 | `Ripple Effect (Closeness):` 0.020915
  * `Imports (Out-Degree: 2):` .errors, .tokens, .utils, json, oauthlib.common, oauthlib.signals, os, time...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 297.36 | **LOC:** 367 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 53.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sign` **(Many-Argument Workhorses)** (Impact: 60.7)
    * *Intent:* """Sign a request Signs an HTTP request with the specified parts. Returns a 3-tuple of the signed re...
  * `get_oauth_params` **(Compute Cores)** (Impact: 20.8)
    * *Intent:* """Get the basic OAuth parameters to be used in generating a signature. """
  * `_render` **(Stateful Encapsulated Methods)** (Impact: 17.5)
    * *Intent:* """Render a signed request according to signature type Returns a 3-tuple containing the request URI,...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `__repr__` **(Compute Cores)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 27`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 8`, `import: 6`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , base64, hashlib, logging, oauthlib.common, urllib.parse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/tests/oauth2/rfc6749/grant_types/test_authorization_code.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 258.68 | **LOC:** 383 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 5.487; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (86.6%), Connectivity (formerly Api Exposure) (84.6%), Guard Balance (formerly Safety Score) (83.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 97.6744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pkce_default_method` **(Compute Cores)** (Impact: 3.3)
  * `test_pkce_wrong_method` **(Parameter Forwarders)** (Impact: 3.2)
  * `setUp` **(Parameter Forwarders)** (Impact: 2.3)
  * `test_create_token_response_without_refresh_token` **(I/O & Config Routines)** (Impact: 2.3)
  * `test_create_authorization_response` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 60`, `args: 45`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 120`
* *Architecture:* `api: 44`, `import: 7`
* *Defense:* `doc: 1`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.487
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.013072
  * `Imports (Out-Degree: 2):` json, oauthlib.common, oauthlib.oauth2.rfc6749, oauthlib.oauth2.rfc6749.grant_types, oauthlib.oauth2.rfc6749.tokens, tests.unittest, unittest
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/tests/oauth1/rfc5849/endpoints/test_base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 250.72 | **LOC:** 407 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.4%), Complexity Load (formerly Cognitive Load) (66.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_timestamp_and_nonce` **(Compute Cores)** (Impact: 8.7)
  * `validate_verifier` **(Parameter Forwarders)** (Impact: 5.1)
  * `validate_access_token` **(Parameter Forwarders)** (Impact: 4.6)
  * `validate_request_token` **(Parameter Forwarders)** (Impact: 4.6)
  * `test_signature_method_validation` **(Annotated & Test Methods)** (Impact: 4.5)
    * *Intent:* """Ensure valid signature method is used."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 91`, `args: 46`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 81`, `unreferenced_by_name: 40`
* *Architecture:* `api: 52`, `import: 7`
* *Defense:* `doc: 8`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` oauthlib.common, oauthlib.oauth1, oauthlib.oauth1.rfc5849, oauthlib.oauth1.rfc5849.endpoints, re, tests.unittest, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/errors.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 232.84 | **LOC:** 400 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **4**; blast radius 28.316; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Connectivity (formerly Api Exposure) (96.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `headers` **(Compute Cores)** (Impact: 6.5)
  * `twotuples` **(Compute Cores)** (Impact: 6.1)
  * `raise_from_error` **(Compute Cores)** (Impact: 5.7)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 53`, `args: 8`, `func_start: 8`, `class_start: 34`
* *Risk/State:* `state_mutation: 73`
* *Architecture:* `io: 1`, `api: 40`, `import: 4`
* *Defense:* `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.316
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.081448
  * `Imports (Out-Degree: 1):` inspect, json, oauthlib.common, sys
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types/authorization_code.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 212.2 | **LOC:** 548 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 11.637; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 11.7647% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_token_request` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* """ :param request: OAuthlib request. :type request: oauthlib.common.Request """
  * `validate_authorization_request` **(Many-Argument Workhorses)** (Impact: 35.2)
    * *Intent:* """Check the authorization request for normal and fatal errors. A normal error could be a missing re...
  * `create_authorization_response` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* """ The client constructs the request URI by adding the following parameters to the query component ...
  * `create_token_response` **(Many-Argument Workhorses)** (Impact: 7.7)
    * *Intent:* """Validate the authorization code. The client MUST NOT use the authorization code more than once. I...
  * `create_authorization_code` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* """ Generates an authorization grant represented as a dictionary. :param request: OAuthlib request. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 31`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `planned_debt: 2`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 9`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.637
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.026688
  * `Imports (Out-Degree: 1):` .., .base, base64, hashlib, json, logging, oauthlib, oauthlib.common...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/endpoints/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 200.24 | **LOC:** 240 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.8%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_signature` **(Many-Argument Workhorses)** (Impact: 33.1)
    * *Intent:* # ---- RSA Signature verification ---- if request.signature_method in {SIGNATURE_RSA_SHA1, SIGNATURE...
  * `_create_request` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* # Only include body data from x-www-form-urlencoded requests headers = CaseInsensitiveDict(headers o...
  * `_check_mandatory_parameters` **(Many-Argument Workhorses)** (Impact: 20.5)
    * *Intent:* # The server SHOULD return a 400 (Bad Request) status code when # receiving a request with missing p...
  * `_get_signature_type_and_params` **(Stateful Encapsulated Methods)** (Impact: 7.2)
    * *Intent:* """Extracts parameters from query, headers and body. Signature type is set to the source in which pa...
  * `_check_transport_security` **(Encapsulated Accessors)** (Impact: 5.4)
    * *Intent:* # TODO: move into oauthlib.common from oauth2.utils if (self.request_validator.enforce_ssl and not r...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 18`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 42`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., oauthlib.common, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/grant_types/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 199.06 | **LOC:** 266 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 9.714; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.0%)
- **Documentation Coverage:** 48.4848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_authorization_response` **(Many-Argument Workhorses)** (Impact: 23.1)
    * *Intent:* """Place token according to response mode. Base classes can define a default response mode for their...
  * `_handle_redirects` **(Stateful Encapsulated Methods)** (Impact: 13.3)
  * `_create_cors_headers` **(Stateful Encapsulated Methods)** (Impact: 9.5)
    * *Intent:* """If CORS is allowed, create the appropriate headers."""
  * `validate_scopes` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* """ :param request: OAuthlib request. :type request: oauthlib.common.Request """
  * `_setup_custom_validators` **(Stateful Encapsulated Methods)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 46`, `args: 17`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `planned_debt: 2`
* *Architecture:* `api: 16`, `import: 7`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.714
  * `Choke Point (Betweenness):` 0.000172 | `Ripple Effect (Closeness):` 0.008715
  * `Imports (Out-Degree: 2):` ..request_validator, ..utils, itertools, logging, oauthlib.common, oauthlib.oauth2.rfc6749, oauthlib.uri_validate
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/tests/oauth2/rfc6749/endpoints/test_error_responses.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 189.48 | **LOC:** 492 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.2%), Complexity Load (formerly Cognitive Load) (53.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (10.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_invalid_request` **(I/O & Config Routines)** (Impact: 7.5)
  * `test_invalid_request_method` **(Defensive Guards)** (Impact: 7.0)
  * `test_invalid_post_request` **(Defensive Guards)** (Impact: 4.0)
  * `test_server_error` **(I/O & Config Routines)** (Impact: 3.4)
  * `test_unauthorized_client` **(I/O & Config Routines)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 50`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`, `unreferenced_by_name: 23`
* *Architecture:* `api: 26`, `import: 6`
* *Defense:* `safety: 12`, `doc: 1`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` json, oauthlib.common, oauthlib.oauth2, oauthlib.oauth2.rfc6749, tests.unittest, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/oauthlib/oauth1/rfc5849/request_validator.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 167.54 | **LOC:** 850 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 5.38; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.6%), Guard Balance (formerly Safety Score) (51.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 31.3253% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_timestamp_and_nonce` **(Many-Argument Workhorses)** (Impact: 5.3)
  * `validate_realms` **(Many-Argument Workhorses)** (Impact: 4.3)
  * `validate_verifier` **(Many-Argument Workhorses)** (Impact: 4.0)
    * *Intent:* """Validates a verification code. :param client_key: The client/consumer key. :param token: A reques...
  * `validate_request_token` **(Many-Argument Workhorses)** (Impact: 3.9)
    * *Intent:* """Validates that supplied request token is registered and valid. :param client_key: The client/cons...
  * `validate_access_token` **(Many-Argument Workhorses)** (Impact: 3.9)
    * *Intent:* """Validates that supplied access token is registered and valid. :param client_key: The client/consu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 64`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `api: 42`, `import: 1`
* *Defense:* `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.38
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 1):` , oauthlib.common, your_datastore
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/tests/oauth2/rfc6749/test_server.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 161.86 | **LOC:** 392 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (93.5%), Guard Balance (formerly Safety Score) (71.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setUp` **(I/O & Config Routines)** (Impact: 3.9)
  * `setUp` **(Parameter Forwarders)** (Impact: 3.0)
  * `test_authorization_grant` **(I/O & Config Routines)** (Impact: 2.9)
  * `test_authorization_grant` **(I/O & Config Routines)** (Impact: 2.9)
  * `setUp` **(I/O & Config Routines)** (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 48`, `args: 32`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `state_mutation: 80`, `dead_code: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 27`, `import: 10`
* *Defense:* `doc: 2`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` json, oauthlib, oauthlib.oauth2.rfc6749, oauthlib.oauth2.rfc6749.endpoints, oauthlib.oauth2.rfc6749.endpoints.authorization, oauthlib.oauth2.rfc6749.endpoints.resource, oauthlib.oauth2.rfc6749.endpoints.token, oauthlib.oauth2.rfc6749.grant_types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/tests/test_common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 149.6 | **LOC:** 244 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (29.9%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 94.0299% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_generate_token` **(Compute Cores)** (Impact: 3.4)
  * `test_generate_client_id` **(Compute Cores)** (Impact: 3.4)
  * `test_generate_nonce` **(Parameter Forwarders)** (Impact: 3.1)
    * *Intent:* """Ping me (ib-lundgren) when you discover how to test randomness."""
  * `test_urldecode` **(I/O & Config Routines)** (Impact: 2.6)
  * `test_non_unicode_params` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 47`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 44`, `unreferenced_by_name: 32`
* *Architecture:* `api: 37`, `import: 3`
* *Defense:* `safety: 2`, `doc: 2`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` oauthlib, oauthlib.common, tests.unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/oauthlib/openid/connect/core/grant_types/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 149.4 | **LOC:** 331 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 5.38; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.4%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `openid_authorization_validator` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* """Perform OpenID Connect specific authorization request validation. nonce OPTIONAL. String value us...
  * `add_id_token` **(Many-Argument Workhorses)** (Impact: 25.6)
    * *Intent:* """ Construct an initial version of id_token, and let the request_validator sign or encrypt it. The ...
  * `__setattr__` **(Compute Cores)** (Impact: 6.3)
  * `_inflate_claims` **(Stateful Encapsulated Methods)** (Impact: 5.7)
    * *Intent:* # this may be called multiple times in a single request so make sure we only de-serialize the claims...
  * `id_token_hash` **(Many-Argument Workhorses)** (Impact: 3.2)
    * *Intent:* """ Its value is the base64url encoding of the left-most half of the hash of the octets of the ASCII...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.38
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 1):` base64, hashlib, json, logging, oauthlib.oauth2.rfc6749.errors, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/tests/oauth1/rfc5849/test_signatures.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 142.2 | **LOC:** 904 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Guard Balance (formerly Safety Score) (59.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (8.8%)
- **Documentation Coverage:** 17.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_base_string_uri` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* """ Test the ``base_string_uri`` function. """
  * `test_hmac_false_positives` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* """ Test verify_hmac-* functions will correctly detect invalid signatures. """
  * `test_rsa_bad_keys` **(I/O & Config Routines)** (Impact: 6.0)
    * *Intent:* """ Testing RSA sign and verify with bad key values produces errors. This test is useful for coverag...
  * `test_plaintext_false_positives` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* """ Test verify_plaintext function will correctly detect invalid signatures. """
  * `test_signature_base_string` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* # ==== Signature base string calculating function tests ========== """ Test the ``signature_base_str...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 27`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `state_mutation: 52`, `dead_code: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `doc: 21`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jwt, oauthlib.oauth1.rfc5849.signature, tests.unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/tests/oauth2/rfc6749/test_parameters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 140.16 | **LOC:** 332 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.6%), Connectivity (formerly Api Exposure) (9.1%)
- **Documentation Coverage:** 41.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_parse_expires` **(Compute Cores)** (Impact: 21.0)
  * `test_json_token_response` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* """Verify correct parameter parsing and validation for token responses. """
  * `test_url_encoded_token_response` **(Defensive Guards)** (Impact: 4.0)
    * *Intent:* """Verify fallback parameter parsing and validation for token responses. """
  * `test_grant_response` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* """Verify correct parameter parsing and validation for auth code responses."""
  * `record_scope_change` **(Parameter Forwarders)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 32`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 73`, `duplicate_logic: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 13`, `import: 5`
* *Defense:* `safety: 6`, `doc: 7`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` oauthlib, oauthlib.oauth2.rfc6749.errors, oauthlib.oauth2.rfc6749.parameters, tests.unittest, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/tests/oauth2/rfc6749/clients/test_base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 138.94 | **LOC:** 379 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.776; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.5%), Complexity Load (formerly Cognitive Load) (75.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (9.1%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_parse_token_response_expires_at_types` **(Compute Cores)** (Impact: 5.3)
  * `test_add_bearer_token` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test a number of bearer token placements"""
  * `test_add_mac_token` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* # Missing access token client = Client(self.client_id, token_type="MAC") self.assertRaises(ValueErro...
  * `test_revocation_request` **(I/O & Config Routines)** (Impact: 2.9)
  * `test_prepare_refresh_token_request` **(I/O & Config Routines)** (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 31`, `args: 16`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 87`, `dead_code: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 14`, `import: 8`
* *Defense:* `doc: 1`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, json, oauthlib, oauthlib.oauth2, oauthlib.oauth2.rfc6749, oauthlib.oauth2.rfc6749.clients, tests.unittest, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/request_validator.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 133.1 | **LOC:** 681 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 12.654; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 3.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_bearer_token` **(Many-Argument Workhorses)** (Impact: 4.9)
    * *Intent:* """Persist the Bearer token. The Bearer token should at minimum be associated with: - a client and i...
  * `validate_bearer_token` **(Many-Argument Workhorses)** (Impact: 4.8)
    * *Intent:* """Ensure the Bearer token is valid and authorized access to scopes. :param token: A string of rando...
  * `introspect_token` **(Many-Argument Workhorses)** (Impact: 4.7)
    * *Intent:* """Introspect an access or refresh token. Called once the introspect request is validated. This meth...
  * `validate_code` **(Many-Argument Workhorses)** (Impact: 4.5)
    * *Intent:* """Verify that the authorization_code is valid and assigned to the given client. Before returning tr...
  * `save_authorization_code` **(Many-Argument Workhorses)** (Impact: 4.4)
    * *Intent:* """Persist the authorization_code. The code should at minimum be stored with: - the client_id (``cli...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 37`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `dead_code: 2`, `planned_debt: 21`
* *Architecture:* `api: 29`, `import: 1`
* *Defense:* `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.654
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 0):` logging
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/tests/oauth2/rfc6749/grant_types/test_refresh_token.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 131.54 | **LOC:** 228 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 4.846; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.0%), Connectivity (formerly Api Exposure) (64.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_custom_auth_validators_unsupported` **(Parameter Forwarders)** (Impact: 2.1)
  * `test_authentication_required_populate_client_id` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """ Make sure that request.client_id is populated from request.client.client_id if None. """
  * `setUp` **(Parameter Forwarders)** (Impact: 2.0)
  * `test_create_token_response` **(Parameter Forwarders)** (Impact: 2.0)
  * `test_create_token_inherit_scope` **(Parameter Forwarders)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 42`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `api: 21`, `import: 7`
* *Defense:* `doc: 2`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.846
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 2):` json, oauthlib.common, oauthlib.oauth2.rfc6749, oauthlib.oauth2.rfc6749.grant_types, oauthlib.oauth2.rfc6749.tokens, tests.unittest, unittest
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/tests/oauth1/rfc5849/test_client.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 119.92 | **LOC:** 270 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.776; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (68.1%), Guard Balance (formerly Safety Score) (55.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_decoding` **(Compute Cores)** (Impact: 3.3)
  * `test_sign_get_with_body` **(Parameter Forwarders)** (Impact: 3.2)
  * `test_rsa_method` **(I/O & Config Routines)** (Impact: 2.9)
  * `test_case_insensitive_headers` **(Parameter Forwarders)** (Impact: 2.5)
  * `test_register_method` **(Callbacks & Closures)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 42`, `args: 26`, `func_start: 25`, `class_start: 5`
* *Risk/State:* `state_mutation: 34`, `unreferenced_by_name: 25`
* *Architecture:* `api: 30`, `import: 4`
* *Defense:* `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` oauthlib.common, oauthlib.oauth1, oauthlib.oauth1.rfc5849, tests.unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/endpoints/metadata.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 118.98 | **LOC:** 239 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 4.578; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_metadata` **(Many-Argument Workhorses)** (Impact: 46.5)
  * `validate_metadata_server` **(I/O & Config Routines)** (Impact: 13.0)
    * *Intent:* """ Authorization servers can have metadata describing their configuration. The following authorizat...
  * `validate_metadata_authorization` **(Defensive Guards)** (Impact: 11.1)
  * `__init__` **(Defensive Guards)** (Impact: 5.0)
  * `create_metadata_response` **(Parameter Forwarders)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 29`, `args: 9`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `safety: 12`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 3):` .., .authorization, .base, .introspect, .revocation, .token, copy, json...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/clients/service_application.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 109.92 | **LOC:** 190 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 4.418; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_request_body` **(Many-Argument Workhorses)** (Impact: 60.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 13`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `io: 1`, `api: 3`, `import: 5`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.418
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.006536
  * `Imports (Out-Degree: 1):` ..parameters, .base, jwt, oauthlib.common, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `oauthlib-3.3.1/oauthlib/openid/connect/core/endpoints/pre_configured.py` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 95.6487%)
- `oauthlib-3.3.1/oauthlib/openid/connect/core/endpoints/userinfo.py` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.9999%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/errors.py` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 100.0%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/tokens.py` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 100.0%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc8628/endpoints/device_authorization.py` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 99.9982%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `oauthlib-3.3.1/oauthlib/common.py` -> **Severity: 33.848** (Embedded: 0.3573 * Error Risk: 94.7335%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/tokens.py` -> **Severity: 11.473** (Embedded: 0.1153 * Error Risk: 99.5124%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/errors.py` -> **Severity: 8.088** (Embedded: 0.0814 * Error Risk: 99.3039%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/endpoints/token.py` -> **Severity: 2.909** (Embedded: 0.0327 * Error Risk: 89.0067%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/endpoints/base.py` -> **Severity: 2.295** (Embedded: 0.0297 * Error Risk: 77.2644%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `oauthlib-3.3.1/oauthlib/common.py` -> **Severity: 12839.781** (Blast Radius: 211.683 * Doc Risk: 60.6557%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/errors.py` -> **Severity: 2831.6** (Blast Radius: 28.316 * Doc Risk: 100.0%)
- `oauthlib-3.3.1/oauthlib/oauth2/rfc6749/tokens.py` -> **Severity: 1824.82** (Blast Radius: 35.703 * Doc Risk: 51.1111%)
- `oauthlib-3.3.1/oauthlib/uri_validate.py` -> **Severity: 1111.4** (Blast Radius: 11.114 * Doc Risk: 100.0%)
- `oauthlib-3.3.1/oauthlib/openid/connect/core/endpoints/pre_configured.py` -> **Severity: 859.0** (Blast Radius: 8.59 * Doc Risk: 100.0%)

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
