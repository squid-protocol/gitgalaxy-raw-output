# ARCHITECTURAL_BRIEF: requests
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
- **Scope:** 50 analyzed artifact(s), 6981 LOC.
- **Load-bearing artifact:** `requests-2.33.1/src/requests/cookies.py` -- 8 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `requests-2.33.1/tests/test_requests.py` -- pulls in 30 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `requests-2.33.1/tests/test_requests.py` at magnitude 1891.36 (structural weight, not risk).
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
| Total Artifacts | 66 |
| Analyzed Artifacts (Scanned) | 50 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 6981 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 75.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.283 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1167 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3563 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 34 | 6907 | 68.0% |
| MAKEFILE | 8 | 74 | 16.0% |
| MARKDOWN | 5 | 0 | 10.0% |
| PLAINTEXT | 3 | 0 | 6.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `2.795`
> **Composition Archetype:** `Small Flat Repo (2)` (z +2.79; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Large Core Modules (2) 22%, Parameter Forwarders Files 14%, Declarative / Non-Code 12%, Large Core Modules (3) 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 42 | 84.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 16.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `.cnf`: 6x Excluded (Unsupported Extension: '.cnf')
- `.srl`: 3x Excluded (Unsupported Extension: '.srl')
- `.csr`: 3x Excluded (Unsupported Extension: '.csr')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.6 | 18.7 | 10.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.1 | 46.8 | 50.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 90.9 | 20.8 | 9.1 | 7.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.8 | 77.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 143 | 16 | 7 | `requests-2.33.1/tests/test_requests.py` |
| cleanup | 26 | 14 | 1 | `requests-2.33.1/tests/test_testserver.py` |
| guards | 900 | 27 | 33 | `requests-2.33.1/tests/test_requests.py` |
| danger | 170 | 15 | 11 | `requests-2.33.1/src/requests/adapters.py` |
| concurrency | 71 | 11 | 6 | `requests-2.33.1/tests/test_lowlevel.py` |
| connectivity | 710 | 35 | 30 | `requests-2.33.1/tests/test_requests.py` |
| io | 484 | 23 | 10 | `requests-2.33.1/tests/test_requests.py` |
| crypto | 8 | 6 | 1 | `requests-2.33.1/src/requests/__init__.py` |
| ipc | 0 | 0 | 0 | - |
| time | 10 | 4 | 0 | `requests-2.33.1/src/requests/cookies.py` |
| serialization | 7 | 1 | 0 | `requests-2.33.1/tests/test_requests.py` |
| regex | 12 | 4 | 0 | `requests-2.33.1/src/requests/utils.py` |
| events | 63 | 7 | 2 | `requests-2.33.1/tests/test_requests.py` |
| tests | 544 | 13 | 12 | `requests-2.33.1/tests/test_requests.py` |
| docs | 302 | 25 | 25 | `requests-2.33.1/src/requests/utils.py` |
| debt | 43 | 9 | 1 | `requests-2.33.1/tests/test_requests.py` |
| mutation | 3326 | 32 | 193 | `requests-2.33.1/tests/test_requests.py` |
| dead_code | 348 | 17 | 4 | `requests-2.33.1/tests/test_requests.py` |
| credential | 0 | 0 | 0 | - |
| threat | 65 | 15 | 4 | `requests-2.33.1/src/requests/models.py` |
| ml_ai | 41 | 4 | 0 | `requests-2.33.1/tests/test_utils.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.946**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `requests-2.33.1/tests/test_requests.py` (Hits: 333)
- `requests-2.33.1/src/requests/utils.py` (Hits: 27)
- `requests-2.33.1/tests/test_testserver.py` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cookies.py** (`requests-2.33.1/src/requests/cookies.py`) — 8 inbound connections
2. **structures.py** (`requests-2.33.1/src/requests/structures.py`) — 8 inbound connections
3. **exceptions.py** (`requests-2.33.1/src/requests/exceptions.py`) — 7 inbound connections
4. **_internal_utils.py** (`requests-2.33.1/src/requests/_internal_utils.py`) — 6 inbound connections
5. **server.py** (`requests-2.33.1/tests/testserver/server.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_requests.py** (`requests-2.33.1/tests/test_requests.py`) — 30 outbound dependencies
2. **utils.py** (`requests-2.33.1/src/requests/utils.py`) — 22 outbound dependencies
3. **models.py** (`requests-2.33.1/src/requests/models.py`) — 20 outbound dependencies
4. **adapters.py** (`requests-2.33.1/src/requests/adapters.py`) — 18 outbound dependencies
5. **__init__.py** (`requests-2.33.1/src/requests/__init__.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolve_redirects` **(Many-Argument Workhorses)** (@ `requests-2.33.1/src/requests/sessions.py`) -> Impact: **59.2** | LOC: 122
- `build_digest_header` **(Many-Argument Workhorses)** (@ `requests-2.33.1/src/requests/auth.py`) -> Impact: **57.5** | LOC: 109
  * *Intent:* """ :rtype: str """
- `_encode_files` **(Defensive Guards)** (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **48.4** | LOC: 67
  * *Intent:* """Build the body for a multipart/form-data request. Will successfully encode files when passed as a dict or a list of tuples. Order is retained if da...
- `send` **(Many-Argument Workhorses)** (@ `requests-2.33.1/src/requests/adapters.py`) -> Impact: **47.8** | LOC: 107
- `prepare_body` **(Many-Argument Workhorses)** (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **46.3** | LOC: 77
  * *Intent:* """Prepares the given HTTP body data."""
- `cert_verify` **(Many-Argument Workhorses)** (@ `requests-2.33.1/src/requests/adapters.py`) -> Impact: **44.4** | LOC: 55
  * *Intent:* """Verify a SSL certificate. This method should not be called from user code, and is only exposed for use when subclassing the :class:`HTTPAdapter <re...
- `__init__` **(Many-Argument Workhorses)** (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **43.2** | LOC: 33
- `prepare_url` **(Many-Argument Workhorses)** (@ `requests-2.33.1/src/requests/models.py`) -> Impact: **37.6** | LOC: 73
  * *Intent:* """Prepares the given HTTP URL."""
- `should_bypass_proxies` **(Compute Cores)** (@ `requests-2.33.1/src/requests/utils.py`) -> Impact: **34.1** | LOC: 59
  * *Intent:* """ Returns whether we should bypass proxies or not. :rtype: bool """
- `super_len` **(Defensive Guards)** (@ `requests-2.33.1/src/requests/utils.py`) -> Impact: **27.5** | LOC: 69

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `requests-2.33.1/src/requests` | 18 | 3942.26 | 34.97% | 14.49% |
| `requests-2.33.1/tests` | 13 | 2729.62 | 8.25% | 0.0% |
| `requests-2.33.1/tests/testserver` | 2 | 167.46 | 21.85% | 0.0% |
| `requests-2.33.1` | 6 | 58.74 | 0.64% | 0.0% |
| `requests-2.33.1/tests/certs/expired/server` | 1 | 8.72 | 0.0% | 0.0% |
| `requests-2.33.1/tests/certs/mtls/client` | 1 | 8.72 | 0.0% | 0.0% |
| `requests-2.33.1/tests/certs/valid/server` | 1 | 8.72 | 0.0% | 0.0% |
| `requests-2.33.1/tests/certs/expired` | 2 | 8.58 | 0.0% | 0.0% |
| `requests-2.33.1/tests/certs/expired/ca` | 1 | 6.48 | 0.0% | 0.0% |
| `requests-2.33.1/tests/certs/mtls/client/ca` | 1 | 6.48 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `requests-2.33.1/src/requests/auth.py` -> **99.9792%** Exposure
- `requests-2.33.1/src/requests/help.py` -> **93.0993%** Exposure
- `requests-2.33.1/src/requests/hooks.py` -> **37.7541%** Exposure
- `requests-2.33.1/src/requests/utils.py` -> **20.3328%** Exposure
- `requests-2.33.1/src/requests/adapters.py` -> **9.6551%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `requests-2.33.1/src/requests/__version__.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/adapters.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/auth.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/compat.py` -> **100.0%** Exposure
- `requests-2.33.1/src/requests/help.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `requests-2.33.1/tests/test_requests.py` -> **238** Orphaned Functions | **11** Duplicates
- `requests-2.33.1/tests/test_utils.py` -> **57** Orphaned Functions | **8** Duplicates
- `requests-2.33.1/tests/test_lowlevel.py` -> **13** Orphaned Functions | **0** Duplicates
- `requests-2.33.1/tests/test_testserver.py` -> **11** Orphaned Functions | **0** Duplicates
- `requests-2.33.1/tests/test_structures.py` -> **6** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `179` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `requests-2.33.1/tests/test_requests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1891.36 | **LOC:** 3045 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 13.787; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.6%), Guard Balance (formerly Safety Score) (31.6%), Concurrency Surface (formerly Concurrency) (20.2%)
- **Documentation Coverage:** 88.0819% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_https_warnings` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* """warnings are emitted with requests.get"""
  * `test_POSTBIN_SEEKED_OBJECT_WITH_NO_ITER` **(Defensive Guards)** (Impact: 12.4)
  * `test_custom_redirect_mixin` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* """Tests a custom mixin to overwrite ``get_redirect_target``. Ensures a subclassed ``requests.Sessio...
  * `seek` **(Compute Cores)** (Impact: 8.3)
  * `get_redirect_target` **(Compute Cores)** (Impact: 7.4)
    * *Intent:* # default behavior if resp.is_redirect: return resp.headers["location"] # edge case - check to see i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 77 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 873
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 927`, `args: 276`, `func_start: 274`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 7`, `state_mutation: 719`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 11`, `unreferenced_by_name: 238`
* *Architecture:* `io: 333`, `api: 273`, `concurrency: 5`, `import: 32`
* *Defense:* `safety: 449`, `doc: 35`, `test: 331`, `sync_locks: 4`, `immutability_locks: 12`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` , .compat, .testserver.server, .utils, collections, contextlib, io, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/models.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 895.7 | **LOC:** 1042 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **20**; blast radius 22.205; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.8%)
- **Documentation Coverage:** 33.7209% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_encode_files` **(Defensive Guards)** (Impact: 48.4)
    * *Intent:* """Build the body for a multipart/form-data request. Will successfully encode files when passed as a...
  * `prepare_body` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* """Prepares the given HTTP body data."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `prepare_url` **(Many-Argument Workhorses)** (Impact: 37.6)
    * *Intent:* """Prepares the given HTTP URL."""
  * `iter_content` **(Defensive Guards)** (Impact: 26.9)
    * *Intent:* """Iterates over the response data. When stream=True is set on the request, this avoids reading the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 126 instances
* *State Mutation (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 139`, `args: 44`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 162`, `dead_code: 1`
* *Architecture:* `api: 39`, `import: 20`
* *Defense:* `safety: 60`, `doc: 35`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.205
  * `Choke Point (Betweenness):` 0.003295 | `Ripple Effect (Closeness):` 0.085034
  * `Imports (Out-Degree: 7):` ._internal_utils, .auth, .compat, .cookies, .exceptions, .hooks, .status_codes, .structures...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 754.46 | **LOC:** 1084 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 16.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Connectivity (formerly Api Exposure) (67.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 10.4651% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `should_bypass_proxies` **(Compute Cores)** (Impact: 34.1)
    * *Intent:* """ Returns whether we should bypass proxies or not. :rtype: bool """
  * `super_len` **(Defensive Guards)** (Impact: 27.5)
  * `get_netrc_auth` **(Defensive Guards)** (Impact: 22.9)
    * *Intent:* """Returns the Requests tuple auth for a given url from netrc."""
  * `_validate_header_part` **(Stateful Encapsulated Methods)** (Impact: 20.9)
  * `guess_json_utf` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """ :rtype: str """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 172`, `args: 43`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 131`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* `io: 27`, `api: 41`, `import: 23`
* *Defense:* `safety: 51`, `doc: 40`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.717
  * `Choke Point (Betweenness):` 0.00085 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 5):` , .__version__, ._internal_utils, .compat, .cookies, .exceptions, .structures, codecs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/sessions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 592.26 | **LOC:** 835 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 16.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.2%)
- **Documentation Coverage:** 51.7241% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_redirects` **(Many-Argument Workhorses)** (Impact: 59.2)
  * `send` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* """Send a given PreparedRequest. :rtype: requests.Response """
  * `merge_environment_settings` **(Many-Argument Workhorses)** (Impact: 25.3)
    * *Intent:* """ Check the environment and merge it with some settings. :rtype: dict """
  * `should_strip_auth` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* """Decide whether Authorization header should be removed when redirecting"""
  * `request` **(Many-Argument Workhorses)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 92`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 106`
* *Architecture:* `io: 1`, `api: 30`, `import: 16`
* *Defense:* `safety: 9`, `doc: 25`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.633
  * `Choke Point (Betweenness):` 0.001736 | `Ripple Effect (Closeness):` 0.040816
  * `Imports (Out-Degree: 9):` ._internal_utils, .adapters, .auth, .compat, .cookies, .exceptions, .hooks, .models...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/adapters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 485.08 | **LOC:** 698 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 28.248; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 41.4634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `cert_verify` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* """Verify a SSL certificate. This method should not be called from user code, and is only exposed fo...
  * `_urllib3_request_context` **(Stateful Encapsulated Methods)** (Impact: 21.9)
  * `get_connection` **(Many-Argument Workhorses)** (Impact: 16.0)
    * *Intent:* """DEPRECATED: Users should move to `get_connection_with_tls_context` for all subclasses of HTTPAdap...
  * `get_connection_with_tls_context` **(Many-Argument Workhorses)** (Impact: 14.6)
    * *Intent:* """Returns a urllib3 connection for the given request and TLS settings. This should not be called fr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 86`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 92`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 19`, `import: 22`
* *Defense:* `safety: 26`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.248
  * `Choke Point (Betweenness):` 0.003401 | `Ripple Effect (Closeness):` 0.065306
  * `Imports (Out-Degree: 5):` .auth, .compat, .cookies, .exceptions, .models, .structures, .utils, os.path...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/cookies.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 423.94 | **LOC:** 562 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **7**; blast radius 61.066; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (89.7%), Guard Balance (formerly Safety Score) (86.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 35.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_find_no_duplicates` **(Stateful Encapsulated Methods)** (Impact: 21.5)
    * *Intent:* """Both ``__get_item__`` and ``get`` call this function: it's never used elsewhere in Requests. :par...
  * `remove_cookie_by_name` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* """Unsets a cookie by name, by default over all domains and paths. Wraps CookieJar.clear(), is O(n)....
  * `_find` **(Stateful Encapsulated Methods)** (Impact: 16.6)
    * *Intent:* """Requests uses this method internally to get cookie values. If there are conflicting cookies, _fin...
  * `cookiejar_from_dict` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* """Returns a CookieJar from a key/value dictionary. :param cookie_dict: Dict of key/values to insert...
  * `get_dict` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* """Takes as an argument an optional domain and path and returns a plain old Python dict of name-valu...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 113`, `args: 49`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 50`, `dead_code: 1`
* *Architecture:* `api: 50`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 18`, `doc: 36`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 61.066
  * `Choke Point (Betweenness):` 0.001665 | `Ripple Effect (Closeness):` 0.183673
  * `Imports (Out-Degree: 1):` ._internal_utils, .compat, calendar, copy, dummy_threading, threading, time
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_utils.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 360.62 | **LOC:** 991 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 13.787; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (21.6%), Connectivity (formerly Api Exposure) (13.2%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_should_bypass_proxies_win_registry` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* """Tests for function should_bypass_proxies to check if proxy can be bypassed or not with Windows re...
  * `test_iter_slices` **(Defensive Guards)** (Impact: 9.0)
  * `QueryValueEx` **(Compute Cores)** (Impact: 7.3)
  * `QueryValueEx` **(Compute Cores)** (Impact: 7.3)
  * `QueryValueEx` **(Compute Cores)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 264`, `args: 78`, `func_start: 78`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 47`, `fragile_debt: 1`, `duplicate_logic: 8`, `unreferenced_by_name: 57`
* *Architecture:* `io: 24`, `api: 94`, `import: 18`
* *Defense:* `safety: 73`, `doc: 19`, `test: 114`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .compat, collections, copy, filecmp, io, os, pytest, requests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/auth.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 313.6 | **LOC:** 315 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 22.891; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_digest_header` **(Many-Argument Workhorses)** (Impact: 57.5)
    * *Intent:* """ :rtype: str """
  * `_basic_auth_str` **(Stateful Encapsulated Methods)** (Impact: 14.2)
    * *Intent:* """Returns a Basic Auth string."""
  * `handle_401` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* """ Takes the given response and tries digest-auth, if needed. :rtype: requests.Response """
  * `__call__` **(Defensive Guards)** (Impact: 4.4)
    * *Intent:* # Initialize per-thread state, if needed self.init_per_thread_state() # If we have a saved nonce, sk...
  * `handle_redirect` **(Parameter Forwarders)** (Impact: 4.2)
    * *Intent:* """Reset num_401_calls counter on redirects."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 58`, `args: 20`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 73`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 11`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.891
  * `Choke Point (Betweenness):` 0.00039 | `Ripple Effect (Closeness):` 0.091837
  * `Imports (Out-Degree: 2):` ._internal_utils, .compat, .cookies, .utils, base64, hashlib, os, re...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_lowlevel.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 249.98 | **LOC:** 429 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 13.787; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.9%), Complexity Load (formerly Cognitive Load) (30.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_digestauth_401_count_reset_on_redirect` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* """Ensure we correctly reset num_401_calls after a successful digest auth, followed by a 302 redirec...
  * `test_digestauth_401_only_sent_once` **(I/O & Config Routines)** (Impact: 3.2)
    * *Intent:* """Ensure we correctly respond to a 401 challenge once, and then stop responding if challenged again...
  * `test_fragment_update_on_redirect` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* """Verify we only append previous fragment if one doesn't exist on new location. If a new fragment i...
  * `test_fragment_not_sent_with_request` **(Defensive Guards)** (Impact: 3.0)
    * *Intent:* """Verify that the fragment portion of a URI isn't sent to the server."""
  * `test_digestauth_only_on_4xx` **(Defensive Guards)** (Impact: 2.8)
    * *Intent:* """Ensure we only send digestauth on 4xx challenges. See https://github.com/psf/requests/issues/3772...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 113`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 91`, `unreferenced_by_name: 13`
* *Architecture:* `io: 23`, `api: 22`, `concurrency: 13`, `import: 6`
* *Defense:* `safety: 44`, `doc: 11`, `test: 19`, `sync_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .utils, pytest, requests, requests.compat, tests.testserver.server, threading
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/tests/testserver/server.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 156.94 | **LOC:** 177 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 50.115; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (90.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (43.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__exit__` **(Type Conversions)** (Impact: 9.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `consume_socket_content` **(Compute Cores)** (Impact: 7.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 6.3)
  * `_handle_requests` **(Stateful Encapsulated Methods)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 35`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 28`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 9`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 6`, `doc: 1`, `sync_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.102041
  * `Imports (Out-Degree: 0):` select, socket, ssl, threading
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/help.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 89.36 | **LOC:** 132 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 25.506; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Debt Markers (formerly Tech Debt) (93.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `info` **(I/O & Config Routines)** (Impact: 8.8)
    * *Intent:* """Generate information for a bug report."""
  * `_implementation` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* """Return a dict with the Python implementation and version. Provide both the name and the version o...
  * `main` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* """Pretty-print the bug information as JSON."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 20`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 27`, `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 2`, `import: 12`
* *Defense:* `safety: 8`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.506
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 0):` , OpenSSL, chardet, charset_normalizer, cryptography, idna, json, platform...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_testserver.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 80.84 | **LOC:** 166 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 13.787; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (77.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.7%), Complexity Load (formerly Cognitive Load) (20.7%)
- **Documentation Coverage:** 8.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multiple_requests` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* """multiple requests can be served"""
  * `test_request_recovery` **(Defensive Guards)** (Impact: 2.5)
    * *Intent:* """can check the requests content"""
  * `test_basic` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* """messages are sent and received properly"""
  * `test_basic_waiting_server` **(Type Conversions)** (Impact: 2.1)
    * *Intent:* """the server waits for the block_server event to be set before closing"""
  * `test_request_recovery_with_bigger_timeout` **(Defensive Guards)** (Impact: 2.1)
    * *Intent:* """a biggest timeout can be specified"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 59`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `io: 24`, `api: 13`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 15`, `doc: 11`, `test: 17`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, requests, socket, tests.testserver.server, threading, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/structures.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 58.1 | **LOC:** 100 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **2**; blast radius 56.863; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Connectivity (formerly Api Exposure) (68.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__eq__` **(Type Conversions)** (Impact: 5.5)
  * `__init__` **(Encapsulated Accessors)** (Impact: 4.2)
  * `lower_items` **(Parameter Forwarders)** (Impact: 3.0)
    * *Intent:* """Like iteritems(), but with all lowercase keys."""
  * `__iter__` **(Parameter Forwarders)** (Impact: 2.9)
  * `__setitem__` **(Parameter Forwarders)** (Impact: 2.2)
    * *Intent:* # Use the lowercased key for lookups, but store the actual # key alongside the value. self._store[ke...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 32`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 56.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.170068
  * `Imports (Out-Degree: 0):` .compat, collections
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 57.58 | **LOC:** 153 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 47.161; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (90.9%), Guard Balance (formerly Safety Score) (77.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* """Initialize RequestException with `request` and `response` objects."""
  * `__init__` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* """ Construct the JSONDecodeError instance first with all args. Then use it's args to construct the ...
  * `__reduce__` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* """ The __reduce__ method called when pickling the object must be the one from the JSONDecodeError (...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 35`, `args: 3`, `func_start: 3`, `class_start: 25`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 26`, `import: 2`
* *Defense:* `safety: 1`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.150278
  * `Imports (Out-Degree: 0):` .compat, urllib3.exceptions
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/test_structures.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 44.08 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 13.787; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.4%), Guard Balance (formerly Safety Score) (10.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_instance_equality` **(Defensive Guards)** (Impact: 2.1)
  * `test_getitem` **(Defensive Guards)** (Impact: 2.1)
  * `test_get` **(Defensive Guards)** (Impact: 2.1)
  * `test_delitem` **(Defensive Guards)** (Impact: 1.9)
  * `test_getitem` **(Defensive Guards)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 29`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 14`, `import: 2`
* *Defense:* `safety: 11`, `doc: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, requests.structures
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 41.02 | **LOC:** 2051 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/__version__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 39.2 | **LOC:** 15 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 18.303; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.7%), Complexity Load (formerly Cognitive Load) (52.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045918
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 39.16 | **LOC:** 184 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 13.787; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (30.2%), Complexity Load (formerly Cognitive Load) (22.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_compatibility` **(Type Conversions)** (Impact: 15.7)
  * `_check_cryptography` **(Stateful Encapsulated Methods)** (Impact: 3.4)
    * *Intent:* # cryptography < 1.3.4 try: cryptography_version = list(map(int, cryptography_version.split("."))) e...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 44`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `safety: 16`, `doc: 1`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` , .__version__, .api, .exceptions, .models, .sessions, .status_codes, chardet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/hooks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 36.38 | **LOC:** 35 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 18.889; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.9%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch_hook` **(Defensive Guards)** (Impact: 14.0)
    * *Intent:* # TODO: response is the only one """Dispatches a hook dictionary on a given piece of data."""
  * `default_hooks` **(Interface Declarations)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 2`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.889
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.073469
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/tests/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 35.64 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 13.787; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (54.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (8.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nosan_server` **(I/O & Config Routines)** (Impact: 2.6)
    * *Intent:* # delay importing until the fixture in order to make it possible # to deselect the test via command-...
  * `prepare_url` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* # Issue #1483: Make sure the URL always has a trailing slash httpbin_url = value.url.rstrip("/") + "...
  * `inner` **(Parameter Forwarders)** (Impact: 1.5)
  * `httpbin` **(Parameter Forwarders)** (Impact: 1.5)
  * `httpbin_secure` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 5`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BaseHTTPServer, SimpleHTTPServer, http.server, pytest, requests.compat, ssl, threading, trustme
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/compat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 32.7 | **LOC:** 107 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 26.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_resolve_char_detection` **(Stateful Encapsulated Methods)** (Impact: 3.5)
    * *Intent:* # ------------------- # Character Detection # ------------------- """Find supported character detect...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 30`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`
* *Architecture:* `io: 1`, `import: 15`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.678
  * `Choke Point (Betweenness):` 0.001701 | `Ripple Effect (Closeness):` 0.061224
  * `Imports (Out-Degree: 1):` collections, collections.abc, compatibility, http, http.cookies, importlib, io, json...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/packages.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 31.3 | **LOC:** 24 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 13.787; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.7%), Complexity Load (formerly Cognitive Load) (64.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 10`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 13.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .compat, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `requests-2.33.1/src/requests/api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 30.32 | **LOC:** 158 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 15.461; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.4%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 4.3)
    * *Intent:* """Constructs and sends a :class:`Request <Request>`. :param method: method for the new :class:`Requ...
  * `post` **(Parameter Forwarders)** (Impact: 2.9)
  * `get` **(Parameter Forwarders)** (Impact: 2.6)
  * `put` **(Parameter Forwarders)** (Impact: 2.6)
  * `patch` **(Parameter Forwarders)** (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `args: 8`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 9`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.461
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 0):` , requests
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/status_codes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 27.74 | **LOC:** 129 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 19.391; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.1%), Guard Balance (formerly Safety Score) (70.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (20.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init` **(Stateful Encapsulated Methods)** (Impact: 8.8)
  * `doc` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.391
  * `Choke Point (Betweenness):` 0.000142 | `Ripple Effect (Closeness):` 0.073469
  * `Imports (Out-Degree: 1):` .structures, requests
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `requests-2.33.1/src/requests/_internal_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 23.3 | **LOC:** 52 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 85.123; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (15.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_native_string` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* """Given a string object, regardless of type, returns a representation of that string in the native ...
  * `unicode_is_ascii` **(Defensive Guards)** (Impact: 2.1)
    * *Intent:* """Determine if unicode string only contains ASCII characters. :param str u_string: unicode string t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 5`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 85.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.149956
  * `Imports (Out-Degree: 0):` .compat, re
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `requests-2.33.1/src/requests/adapters.py` -> **Severity: 0.34** (Bridge: 0.0034 * Flux: 100.0%)
- `requests-2.33.1/src/requests/models.py` -> **Severity: 0.33** (Bridge: 0.0033 * Flux: 100.0%)
- `requests-2.33.1/src/requests/sessions.py` -> **Severity: 0.174** (Bridge: 0.0017 * Flux: 100.0%)
- `requests-2.33.1/src/requests/compat.py` -> **Severity: 0.17** (Bridge: 0.0017 * Flux: 100.0%)
- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 0.166** (Bridge: 0.0017 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 15.896** (Embedded: 0.1837 * Error Risk: 86.5476%)
- `requests-2.33.1/src/requests/structures.py` -> **Severity: 14.054** (Embedded: 0.1701 * Error Risk: 82.6353%)
- `requests-2.33.1/src/requests/exceptions.py` -> **Severity: 11.595** (Embedded: 0.1503 * Error Risk: 77.156%)
- `requests-2.33.1/src/requests/_internal_utils.py` -> **Severity: 9.504** (Embedded: 0.15 * Error Risk: 63.3804%)
- `requests-2.33.1/tests/testserver/server.py` -> **Severity: 9.262** (Embedded: 0.102 * Error Risk: 90.7656%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `requests-2.33.1/src/requests/structures.py` -> **Severity: 5212.444** (Blast Radius: 56.863 * Doc Risk: 91.6667%)
- `requests-2.33.1/tests/testserver/server.py` -> **Severity: 5011.5** (Blast Radius: 50.115 * Doc Risk: 100.0%)
- `requests-2.33.1/src/requests/cookies.py` -> **Severity: 2180.929** (Blast Radius: 61.066 * Doc Risk: 35.7143%)
- `requests-2.33.1/src/requests/status_codes.py` -> **Severity: 1939.1** (Blast Radius: 19.391 * Doc Risk: 100.0%)
- `requests-2.33.1/src/requests/auth.py` -> **Severity: 1831.28** (Blast Radius: 22.891 * Doc Risk: 80.0%)

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
