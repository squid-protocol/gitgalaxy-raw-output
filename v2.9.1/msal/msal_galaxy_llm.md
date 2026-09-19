# ARCHITECTURAL_BRIEF: msal
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
- **Scope:** 49 analyzed artifact(s), 9038 LOC.
- **Load-bearing artifact:** `msal-1.35.1/msal/oauth2cli/authcode.py` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `msal-1.35.1/msal/application.py` -- pulls in 39 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `msal-1.35.1/msal/application.py` at magnitude 1630.7 (structural weight, not risk).
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
| Total Artifacts | 52 |
| Analyzed Artifacts (Scanned) | 49 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 9038 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4818 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1788 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7938 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 48 | 9038 | 98.0% |
| MARKDOWN | 1 | 0 | 2.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.603`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.60; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 37%, Large Core Modules (3) 18%, Encapsulated Accessors Files 14%, Data / Markup / Trivial 8%, Many-Argument Workhorses Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 48 | 98.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 42 exceeds 500 chars)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 71.8 | 23.9 | 19.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.7 | 68.9 | 70.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 47.6 | 2.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 61.1 | 17.9 | 12.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 50.0 | 2.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.2 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 75.5 | 92.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 5.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 186 | 29 | 9 | `msal-1.35.1/msal/application.py` |
| cleanup | 10 | 6 | 1 | `msal-1.35.1/tests/test_authority.py` |
| guards | 462 | 35 | 30 | `msal-1.35.1/msal/application.py` |
| danger | 199 | 35 | 11 | `msal-1.35.1/msal/application.py` |
| concurrency | 19 | 6 | 2 | `msal-1.35.1/msal/token_cache.py` |
| connectivity | 638 | 44 | 24 | `msal-1.35.1/tests/test_application.py` |
| io | 140 | 21 | 9 | `msal-1.35.1/msal/application.py` |
| crypto | 6 | 6 | 1 | `msal-1.35.1/msal/application.py` |
| ipc | 3 | 1 | 0 | `msal-1.35.1/msal/oauth2cli/authcode.py` |
| time | 39 | 16 | 3 | `msal-1.35.1/msal/oauth2cli/oauth2.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 4 | 4 | 0 | `msal-1.35.1/msal/application.py` |
| events | 151 | 22 | 8 | `msal-1.35.1/tests/test_authcode.py` |
| tests | 583 | 24 | 24 | `msal-1.35.1/tests/test_application.py` |
| docs | 361 | 33 | 13 | `msal-1.35.1/msal/application.py` |
| debt | 71 | 15 | 4 | `msal-1.35.1/msal/__main__.py` |
| mutation | 4351 | 45 | 160 | `msal-1.35.1/msal/application.py` |
| dead_code | 209 | 21 | 12 | `msal-1.35.1/tests/test_authority.py` |
| credential | 11 | 6 | 1 | `msal-1.35.1/msal/application.py` |
| threat | 29 | 12 | 2 | `msal-1.35.1/tests/test_e2e.py` |
| ml_ai | 8 | 4 | 0 | `msal-1.35.1/tests/test_ccs.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `msal-1.35.1/msal/application.py` (Hits: 19)
- `msal-1.35.1/tests/test_mi.py` (Hits: 19)
- `msal-1.35.1/tests/test_e2e.py` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **authcode.py** (`msal-1.35.1/msal/oauth2cli/authcode.py`) — 7 inbound connections
2. **oidc.py** (`msal-1.35.1/msal/oauth2cli/oidc.py`) — 7 inbound connections
3. **application.py** (`msal-1.35.1/msal/application.py`) — 5 inbound connections
4. **token_cache.py** (`msal-1.35.1/msal/token_cache.py`) — 5 inbound connections
5. **mex.py** (`msal-1.35.1/msal/mex.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **application.py** (`msal-1.35.1/msal/application.py`) — 39 outbound dependencies
2. **authcode.py** (`msal-1.35.1/msal/oauth2cli/authcode.py`) — 21 outbound dependencies
3. **test_e2e.py** (`msal-1.35.1/tests/test_e2e.py`) — 20 outbound dependencies
4. **managed_identity.py** (`msal-1.35.1/msal/managed_identity.py`) — 16 outbound dependencies
5. **oauth2.py** (`msal-1.35.1/msal/oauth2cli/oauth2.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/application.py`) -> Impact: **124.3** | LOC: 422
- `_acquire_token_silent_from_cache_and_possibly_refresh_it` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/application.py`) -> Impact: **111.7** | LOC: 112
- `_acquire_token_interactive_via_broker` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/application.py`) -> Impact: **98.2** | LOC: 89
- `acquire_token_interactive` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/application.py`) -> Impact: **83.0** | LOC: 189
- `_build_client` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/application.py`) -> Impact: **73.2** | LOC: 122
- `_signin_interactively` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/broker.py`) -> Impact: **61.6** | LOC: 54
- `_get_auth_response` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/oauth2cli/authcode.py`) -> Impact: **56.4** | LOC: 67
- `__init__` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/oauth2cli/oauth2.py`) -> Impact: **52.5** | LOC: 112
- `search` **(Many-Argument Workhorses)** (@ `msal-1.35.1/msal/token_cache.py`) -> Impact: **48.8** | LOC: 46
  * *Intent:* """Returns a generator of matching entries. It is O(1) for AT hits, and O(n) for other types. Note that it holds a lock during the entire search. """
- `_initialize_entra_authority` **(Stateful Encapsulated Methods)** (@ `msal-1.35.1/msal/authority.py`) -> Impact: **47.0** | LOC: 46

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `msal-1.35.1/msal` | 18 | 3963.28 | 39.54% | 6.28% |
| `msal-1.35.1/tests` | 23 | 2950.82 | 11.11% | 0.0% |
| `msal-1.35.1/msal/oauth2cli` | 6 | 1369.32 | 30.28% | 3.72% |
| `msal-1.35.1` | 2 | 14.04 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `msal-1.35.1/msal/throttled_http_client.py` -> **47.598%** Exposure
- `msal-1.35.1/msal/__main__.py` -> **21.0561%** Exposure
- `msal-1.35.1/msal/managed_identity.py` -> **12.4362%** Exposure
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **11.4829%** Exposure
- `msal-1.35.1/msal/authority.py` -> **11.4512%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `msal-1.35.1/msal/authority.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/cloudshell.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/individual_cache.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/oauth2cli/assertion.py` -> **100.0%** Exposure
- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `msal-1.35.1/tests/test_authority.py` -> **51** Orphaned Functions | **6** Duplicates
- `msal-1.35.1/tests/test_application.py` -> **49** Orphaned Functions | **6** Duplicates
- `msal-1.35.1/tests/test_mi.py` -> **25** Orphaned Functions | **2** Duplicates
- `msal-1.35.1/tests/test_e2e_manual.py` -> **13** Orphaned Functions | **2** Duplicates
- `msal-1.35.1/tests/test_client.py` -> **12** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `msal-1.35.1/tests/test_optional_thumbprint.py` -> **99.9295%** Exposure
- `msal-1.35.1/msal/application.py` -> **75.9921%** Exposure
- `msal-1.35.1/tests/test_application.py` -> **67.0021%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `295` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `msal-1.35.1/msal/application.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1630.7 | **LOC:** 2556 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **39**; blast radius 30.586; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.4%), Test Surface (formerly Verification) (80.0%), Credential Material (formerly Secrets Risk) (76.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 124.3)
  * `_acquire_token_silent_from_cache_and_possibly_refresh_it` **(Many-Argument Workhorses)** (Impact: 111.7)
  * `_acquire_token_interactive_via_broker` **(Many-Argument Workhorses)** (Impact: 98.2)
  * `acquire_token_interactive` **(Many-Argument Workhorses)** (Impact: 83.0)
  * `_build_client` **(Many-Argument Workhorses)** (Impact: 73.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 554
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 234`, `args: 67`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 242`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 19`, `api: 24`, `concurrency: 1`, `import: 39`
* *Defense:* `safety: 36`, `doc: 120`, `test: 1`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.586
  * `Choke Point (Betweenness):` 0.03354 | `Ripple Effect (Closeness):` 0.104167
  * `Imports (Out-Degree: 14):` , .authority, .broker, .cloudshell, .mex, .oauth2cli, .oauth2cli.authcode, .oauth2cli.oidc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_e2e.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 809.42 | **LOC:** 1496 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 14.308; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.1%), Connectivity (formerly Api Exposure) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (20.2%)
- **Documentation Coverage:** 62.9371% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_test_acquire_token_obo` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `assertCacheWorksForUser` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `_test_username_password` **(Many-Argument Workhorses)** (Impact: 23.0)
  * `_get_hint` **(Stateful Encapsulated Methods)** (Impact: 22.9)
  * `_build_app` **(Many-Argument Workhorses)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 186`, `args: 85`, `func_start: 82`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 189`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 18`, `api: 76`, `import: 26`
* *Defense:* `safety: 15`, `doc: 43`, `test: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.308
  * `Choke Point (Betweenness):` 0.00133 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 2):` base64, dotenv, json, logging, mock, msal, msal.oauth2cli, msal.oauth2cli.authcode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_application.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 623.48 | **LOC:** 929 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 7.734; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.7%), Credential Material (formerly Secrets Risk) (67.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (26.0%)
- **Documentation Coverage:** 96.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_maintaining_offline_state_and_sending_them` **(Compute Cores)** (Impact: 15.6)
  * `test_acquire_token_for_client` **(Compute Cores)** (Impact: 7.1)
  * `mock_post` **(Parameter Forwarders)** (Impact: 7.0)
  * `mock_post` **(Compute Cores)** (Impact: 7.0)
  * `mock_post` **(Compute Cores)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 168`, `args: 95`, `func_start: 91`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 157`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 49`
* *Architecture:* `io: 4`, `api: 108`, `import: 11`
* *Defense:* `doc: 13`, `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` json, logging, msal, msal.application, msal.telemetry, sys, tests, tests.http_client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/oauth2cli/oauth2.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 617.24 | **LOC:** 879 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 181.253; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 52.5)
  * `_obtain_token` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `obtain_token_by_auth_code_flow` **(Many-Argument Workhorses)** (Impact: 35.9)
  * `_obtain_token` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `obtain_token_by_refresh_token` **(Many-Argument Workhorses)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 97`, `args: 30`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 110`, `planned_debt: 3`
* *Architecture:* `io: 4`, `api: 19`, `import: 16`
* *Defense:* `safety: 20`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 181.253
  * `Choke Point (Betweenness):` 0.002881 | `Ripple Effect (Closeness):` 0.179067
  * `Imports (Out-Degree: 1):` .authcode, base64, functools, hashlib, json, logging, random, requests...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/managed_identity.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 386.72 | **LOC:** 689 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 10.864; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 92.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acquire_token_for_client` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `_obtain_token` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `__init__` **(Compute Cores)** (Impact: 25.3)
  * `_obtain_token_on_arc` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* # https://learn.microsoft.com/en-us/azure/azure-arc/servers/managed-identity-authentication logger.d...
  * `_obtain_token_on_service_fabric` **(Many-Argument Workhorses)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 86`, `args: 20`, `func_start: 19`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 65`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 15`, `api: 12`, `import: 13`
* *Defense:* `safety: 16`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.864
  * `Choke Point (Betweenness):` 0.002438 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 4):` .cloudshell, .individual_cache, .throttled_http_client, .token_cache, collections, hashlib, json, logging...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_authority.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 383.32 | **LOC:** 704 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.734; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (12.4%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_wellknown_host_and_tenant` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* # This test makes real HTTP calls to authority endpoints. # It is intentionally network-based to val...
  * `test_new_sovereign_hosts_should_build_authority_endpoints` **(Many-Argument Workhorses)** (Impact: 5.1)
  * `test_turning_off_instance_discovery_should_work_for_all_kinds_of_clouds` **(Parameter Forwarders)** (Impact: 5.0)
  * `test_known_authority_should_use_same_host_and_skip_instance_discovery` **(Many-Argument Workhorses)** (Impact: 4.8)
  * `test_memorize` **(Defensive Guards)** (Impact: 3.8)
    * *Intent:* # We use a real authority so the constructor can finish tenant discovery authority = "https://login....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 116`, `args: 64`, `func_start: 64`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 128`, `duplicate_logic: 6`, `unreferenced_by_name: 51`
* *Architecture:* `io: 2`, `api: 69`, `import: 8`
* *Defense:* `safety: 5`, `doc: 32`, `test: 117`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock, msal, msal.authority, os, tests, tests.http_client, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/token_cache.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 365.78 | **LOC:** 446 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 34.518; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 82.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search` **(Many-Argument Workhorses)** (Impact: 48.8)
    * *Intent:* """Returns a generator of matching entries. It is O(1) for AT hits, and O(n) for other types. Note t...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 29.6)
  * `__add` **(Stateful Encapsulated Methods)** (Impact: 25.5)
    * *Intent:* # event typically contains: client_id, scope, token_endpoint, # response, params, data, grant_type e...
  * `_is_matching` **(Stateful Encapsulated Methods)** (Impact: 20.5)
  * `__parse_account` **(Stateful Encapsulated Methods)** (Impact: 10.6)
    * *Intent:* """Return client_info and home_account_id"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 70`, `args: 28`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 58`, `planned_debt: 1`
* *Architecture:* `api: 21`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 9`, `doc: 8`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.518
  * `Choke Point (Betweenness):` 0.010047 | `Ripple Effect (Closeness):` 0.148284
  * `Imports (Out-Degree: 3):` .authority, .oauth2cli.oauth2, .oauth2cli.oidc, atexit, json, logging, msal, os...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/authcode.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 365.1 | **LOC:** 440 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **21**; blast radius 191.506; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.8%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_auth_response` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `get_auth_response` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* """Wait and return the auth response. Raise RuntimeError when timeout. :param str auth_uri: If provi...
  * `_browse` **(Defensive Guards)** (Impact: 19.3)
    * *Intent:* """Browse uri with named browser. Default browser is customizable by $BROWSER"""
  * `_process_auth_response` **(Stateful Encapsulated Methods)** (Impact: 18.2)
    * *Intent:* # NOTE: Don't do self.server.shutdown() here. It'll halt the server. """Process the auth response fr...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 15.7)
    * *Intent:* # This class has (rather than is) an _AuthCodeHttpServer, so it does not leak API """Create a Receiv...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 89`, `args: 22`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 55`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 12`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 14`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 191.506
  * `Choke Point (Betweenness):` 0.003694 | `Ripple Effect (Closeness):` 0.197917
  * `Imports (Out-Degree: 1):` .oauth2, BaseHTTPServer, argparse, cgi, collections, html, http.server, json...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/authority.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 294.3 | **LOC:** 306 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 27.555; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.1%)
- **Documentation Coverage:** 76.4706% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_initialize_entra_authority` **(Stateful Encapsulated Methods)** (Impact: 47.0)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 39.9)
  * `has_valid_issuer` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* """ Returns True if the issuer from OIDC discovery is valid for this authority. An issuer is valid i...
  * `canonicalize` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* # Returns (url_parsed_result, hostname_in_lowercase, tenant) authority = urlparse(authority_or_auth_...
  * `user_realm_discovery` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* # It will typically return a dict containing "ver", "account_type", # "federation_protocol", "cloud_...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 43`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 52`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.140833
  * `Imports (Out-Degree: 0):` json, logging, urllib.parse, urlparse
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/__main__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 264.44 | **LOC:** 348 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 7.734; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%), Complexity Load (formerly Cognitive Load) (51.0%)
- **Documentation Coverage:** 42.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_acquire_token_interactive` **(Stateful Encapsulated Methods)** (Impact: 41.9)
    * *Intent:* """acquire_token_interactive() - User will be prompted if app opts to do select_account."""
  * `_main` **(I/O & Config Routines)** (Impact: 37.4)
  * `_select_options` **(Stateful Encapsulated Methods)** (Impact: 20.6)
  * `_acquire_token_silent` **(Stateful Encapsulated Methods)** (Impact: 7.7)
    * *Intent:* """acquire_token_silent() - with an account already signed into MSAL Python."""
  * `_acquire_ssh_cert_silently` **(Stateful Encapsulated Methods)** (Impact: 6.4)
    * *Intent:* """Acquire an SSH Cert silently- This typically only works with Azure CLI"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 50`, `args: 24`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 43`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 1`, `import: 2`
* *Defense:* `safety: 29`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` atexit, base64, dotenv, getpass, json, logging, msal, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/broker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 254.84 | **LOC:** 292 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 16.041; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.0%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_signin_interactively` **(Many-Argument Workhorses)** (Impact: 61.6)
  * `_convert_result` **(Stateful Encapsulated Methods)** (Impact: 29.6)
  * `_acquire_token_silently` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `_signin_silently` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `_signout_silently` **(Stateful Encapsulated Methods)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 39`, `args: 18`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`
* *Architecture:* `io: 3`, `api: 7`, `import: 7`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.041
  * `Choke Point (Betweenness):` 0.000443 | `Ripple Effect (Closeness):` 0.085069
  * `Imports (Out-Degree: 1):` .sku, json, logging, pymsalruntime, sys, time, uuid
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/oidc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 239.7 | **LOC:** 339 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 50.63; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.1%)
- **Documentation Coverage:** 41.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode_id_token` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* """Decodes and validates an id_token and returns its claims as a dictionary. ID token claims would a...
  * `obtain_token_by_auth_code_flow` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* """Validate the auth_response being redirected back, and then obtain tokens, including ID token whic...
  * `obtain_token_by_browser` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `initiate_auth_code_flow` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `obtain_token_by_authorization_code` **(Many-Argument Workhorses)** (Impact: 12.3)
    * *Intent:* """Get a token via authorization code. a.k.a. Authorization Code Grant. Return value and all other p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 46`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`
* *Architecture:* `api: 16`, `import: 9`
* *Defense:* `safety: 2`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.217742
  * `Imports (Out-Degree: 0):` , base64, hashlib, json, logging, random, string, time...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/individual_cache.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 204.14 | **LOC:** 291 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 21.148; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 45.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 16.5)
  * `__call__` **(Defensive Guards)** (Impact: 13.8)
  * `wrapper` **(Defensive Guards)** (Impact: 13.5)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 12.3)
    * *Intent:* # The code structure below can decorate both function and method. # It is inspired by https://stacko...
  * `_set` **(Stateful Encapsulated Methods)** (Impact: 12.1)
    * *Intent:* # This internal implementation powers both set() and __setitem__(), # so that they don't depend on e...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 45`, `args: 16`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 4`, `doc: 10`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.109601
  * `Imports (Out-Degree: 0):` collections, collections.abc, functools, heapq, threading, time
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_mi.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 169.08 | **LOC:** 480 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 7.734; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.3%), Connectivity (formerly Api Exposure) (11.0%), Complexity Load (formerly Cognitive Load) (6.1%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_test_happy_path` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `test_happy_path` **(Defensive Guards)** (Impact: 4.4)
  * `test_arc_error_should_be_normalized` **(Defensive Guards)** (Impact: 4.2)
  * `_test_happy_path` **(Stateful Encapsulated Methods)** (Impact: 2.5)
  * `_build_app` **(Stateful Encapsulated Methods)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 98`, `args: 36`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 30`, `duplicate_logic: 2`, `unreferenced_by_name: 25`
* *Architecture:* `io: 19`, `api: 41`, `import: 14`
* *Defense:* `safety: 5`, `doc: 3`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hashlib, json, mock, msal, msal.managed_identity, msal.token_cache, os, requests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/tests/test_throttled_http_client.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 151.74 | **LOC:** 259 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 9.925; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (87.1%), Connectivity (formerly Api Exposure) (61.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.3%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_dummy_response` **(Encapsulated Accessors)** (Impact: 4.6)
  * `post` **(Parameter Forwarders)** (Impact: 2.7)
  * `get` **(Parameter Forwarders)** (Impact: 2.5)
  * `_test_RetryAfter_N_seconds_should_keep_entry_for_N_seconds` **(Stateful Encapsulated Methods)** (Impact: 2.5)
  * `test_one_invalid_grant_should_block_a_similar_request` **(Parameter Forwarders)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 68`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 59`
* *Architecture:* `api: 31`, `import: 8`
* *Defense:* `safety: 1`, `doc: 5`, `test: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.925
  * `Choke Point (Betweenness):` 0.000887 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 2):` logging, msal.exceptions, msal.throttled_http_client, pickle, random, tests, tests.http_client, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_client.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 145.34 | **LOC:** 301 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 7.734; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (81.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (33.8%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 92.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_conf` **(I/O & Config Routines)** (Impact: 9.7)
    * *Intent:* """ Example of a configuration file: { "Note": "the OpenID Discovery will be updated by following op...
  * `setUpClass` **(Compute Cores)** (Impact: 7.3)
  * `test_device_flow` **(Defensive Guards)** (Impact: 5.1)
  * `test_auth_code` **(Callbacks & Closures)** (Impact: 2.4)
  * `test_auth_code_flow_error_response` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 45`, `args: 24`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 43`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `io: 9`, `api: 16`, `import: 11`
* *Defense:* `safety: 4`, `doc: 3`, `test: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` json, logging, msal.oauth2cli, msal.oauth2cli.authcode, os, requests, tests, tests.http_client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/throttled_http_client.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 129.58 | **LOC:** 180 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 15.994; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 72.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* """Decorate self.post() and self.get() dynamically"""
  * `parse` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* """Return seconds to throttle"""
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 10.4)
  * `_extract_data` **(Encapsulated Accessors)** (Impact: 6.2)
  * `__init__` **(Encapsulated Accessors)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 39`, `args: 17`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 17`, `planned_debt: 4`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 5`, `doc: 6`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.994
  * `Choke Point (Betweenness):` 0.007092 | `Ripple Effect (Closeness):` 0.1125
  * `Imports (Out-Degree: 3):` .exceptions, .individual_cache, .oauth2cli.http, hashlib, threading
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_token_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 116.7 | **LOC:** 324 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 23.073; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.5%), Connectivity (formerly Api Exposure) (57.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertFoundAccessToken` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `build_response` **(Many-Argument Workhorses)** (Impact: 11.5)
  * `build_id_token` **(Type Conversions)** (Impact: 8.4)
    * *Intent:* # NOTE: These helpers were once implemented as static methods in TokenCacheTestCase. # That would ca...
  * `tearDown` **(Compute Cores)** (Impact: 4.7)
  * `testAddByAad` **(I/O & Config Routines)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 32`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `doc: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.073
  * `Choke Point (Betweenness):` 0.004802 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` ..., base64, json, logging, msal.token_cache, tests, time, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/oauth2cli/assertion.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 113.42 | **LOC:** 138 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 9.925; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_normal_assertion` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.0)
  * `__call__` **(Stateful Encapsulated Methods)** (Impact: 4.7)
  * `create_normal_assertion` **(Many-Argument Workhorses)** (Impact: 3.7)
  * `create_regenerative_assertion` **(Parameter Forwarders)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 24`, `args: 9`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 0):` base64, binascii, jwt, logging, time, uuid
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/cloudshell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 92.86 | **LOC:** 127 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 18.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.9%), Complexity Load (formerly Cognitive Load) (59.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_obtain_token` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `_scope_to_resource` **(Stateful Encapsulated Methods)** (Impact: 12.1)
  * `_is_running_in_cloud_shell` **(Encapsulated Accessors)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 22`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.35
  * `Choke Point (Betweenness):` 0.000665 | `Ripple Effect (Closeness):` 0.1125
  * `Imports (Out-Degree: 1):` .oauth2cli.oidc, base64, json, logging, os, time, urllib.parse, urlparse
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_optional_thumbprint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 91.8 | **LOC:** 216 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.734; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (99.9%), Guard Balance (formerly Safety Score) (68.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (15.6%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_verify_assertion_params` **(Stateful Encapsulated Methods)** (Impact: 14.5)
  * `_setup_mocks` **(Stateful Encapsulated Methods)** (Impact: 7.1)
    * *Intent:* -----END CERTIFICATE-----""" """Helper to setup Authority mock"""
  * `test_pem_with_certificate_only_uses_sha256` **(Many-Argument Workhorses)** (Impact: 3.7)
  * `test_pem_with_adfs_uses_sha1` **(Many-Argument Workhorses)** (Impact: 3.6)
  * `test_pem_with_both_uses_manual_thumbprint_as_sha1` **(Many-Argument Workhorses)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 18`, `args: 9`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 5`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `doc: 11`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` msal.application, unittest, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/msal/mex.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 86.92 | **LOC:** 138 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 37.12; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Complexity Load (formerly Cognitive Load) (57.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_endpoints` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `get_wstrust_username_password_endpoint` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* """Returns {"address": "https://...", "action": "the soapAction value"}"""
  * `_get_policy_ids` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `_get_bindings` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `send_request` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 31`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`
* *Architecture:* `io: 5`, `api: 5`, `import: 5`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130208
  * `Imports (Out-Degree: 0):` logging, urllib.parse, urlparse, xml.etree
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `msal-1.35.1/msal/telemetry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 79.66 | **LOC:** 79 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 11.658; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.7%), Complexity Load (formerly Cognitive Load) (55.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Encapsulated Accessors)** (Impact: 10.9)
  * `update_telemetry` **(Compute Cores)** (Impact: 7.3)
  * `generate_headers` **(Compute Cores)** (Impact: 6.6)
  * `_record_failure` **(Stateful Encapsulated Methods)** (Impact: 3.9)
  * `hit_an_access_token` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 14`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.658
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 0):` logging, uuid
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `msal-1.35.1/tests/test_client_obtain_token_by_browser.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 60.48 | **LOC:** 118 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.734; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (17.5%), Connectivity (formerly Api Exposure) (7.9%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_initiate_auth_code_flow_with_non_form_post_response_mode_should_warn` **(Type Conversions)** (Impact: 5.2)
    * *Intent:* """Test that initiating auth code flow warns for non-form_post response modes"""
  * `get_auth_response` **(Stateful Encapsulated Methods)** (Impact: 4.2)
    * *Intent:* """Override to strip auth_uri, preventing browser launch, and optionally inject scheduled actions.""...
  * `setUp` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* # Mock http_client that returns fake token class MockResponse: def __init__(self): self.status_code ...
  * `test_http_post_should_work_with_obtain_token_by_browser` **(Callbacks & Closures)** (Impact: 2.5)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 33`, `args: 9`, `func_start: 8`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 9`, `import: 7`
* *Defense:* `safety: 3`, `doc: 6`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` json, msal.oauth2cli, msal.oauth2cli.authcode, requests, unittest, urllib.parse, urlparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `msal-1.35.1/tests/test_individual_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 58.78 | **LOC:** 111 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.734; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `foo` **(Parameter Forwarders)** (Impact: 2.5)
  * `test_old_item_can_be_updated_with_new_expiry_time` **(Type Conversions)** (Impact: 2.0)
  * `test_setitem` **(Type Conversions)** (Impact: 1.8)
  * `test_set` **(Type Conversions)** (Impact: 1.8)
  * `test_get_should_not_purge_and_should_return_only_when_the_item_is_still_valid` **(Parameter Forwarders)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 33`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`, `unreferenced_by_name: 12`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.734
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` msal.individual_cache, random, time, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `msal-1.35.1/msal/application.py` -> **Severity: 3.354** (Bridge: 0.0335 * Flux: 99.9999%)
- `msal-1.35.1/msal/token_cache.py` -> **Severity: 1.005** (Bridge: 0.01 * Flux: 99.9999%)
- `msal-1.35.1/msal/throttled_http_client.py` -> **Severity: 0.709** (Bridge: 0.0071 * Flux: 99.9999%)
- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **Severity: 0.369** (Bridge: 0.0037 * Flux: 100.0%)
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **Severity: 0.288** (Bridge: 0.0029 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `msal-1.35.1/msal/oauth2cli/oidc.py` -> **Severity: 20.474** (Embedded: 0.2177 * Error Risk: 94.0303%)
- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **Severity: 18.722** (Embedded: 0.1979 * Error Risk: 94.5964%)
- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **Severity: 16.912** (Embedded: 0.1791 * Error Risk: 94.4447%)
- `msal-1.35.1/msal/token_cache.py` -> **Severity: 13.355** (Embedded: 0.1483 * Error Risk: 90.0666%)
- `msal-1.35.1/msal/authority.py` -> **Severity: 13.217** (Embedded: 0.1408 * Error Risk: 93.8486%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `msal-1.35.1/msal/oauth2cli/oauth2.py` -> **Severity: 14829.794** (Blast Radius: 181.253 * Doc Risk: 81.8182%)
- `msal-1.35.1/msal/oauth2cli/authcode.py` -> **Severity: 13679.005** (Blast Radius: 191.506 * Doc Risk: 71.4286%)
- `msal-1.35.1/msal/mex.py` -> **Severity: 3140.924** (Blast Radius: 37.12 * Doc Risk: 84.6154%)
- `msal-1.35.1/msal/token_cache.py` -> **Severity: 2847.735** (Blast Radius: 34.518 * Doc Risk: 82.5%)
- `msal-1.35.1/tests/test_token_cache.py` -> **Severity: 2307.3** (Blast Radius: 23.073 * Doc Risk: 100.0%)

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
