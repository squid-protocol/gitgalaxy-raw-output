# ARCHITECTURAL_BRIEF: httpx
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
- **Scope:** 62 analyzed artifact(s), 12189 LOC.
- **Load-bearing artifact:** `httpx-0.28.1/httpx/_models.py` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `httpx-0.28.1/httpx/_client.py` -- pulls in 23 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `httpx-0.28.1/httpx/_models.py` at magnitude 1244.06 (structural weight, not risk).
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
| Total Artifacts | 70 |
| Analyzed Artifacts (Scanned) | 62 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 12189 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2651 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1983 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0542 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 59 | 12189 | 95.2% |
| MARKDOWN | 3 | 0 | 4.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.702`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.70; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 45%, Generic / Templated Code Files 23%, Data / Markup / Trivial 13%, Large Core Modules (3) 8%, Many-Argument Workhorses Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 59 | 95.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 4.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.json`: 1x Excluded (Massive Static Asset Blob: 9747 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 90.9 | 29.6 | 28.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.1 | 50.1 | 54.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.1 | 4.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 80.9 | 24.1 | 11.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 34.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.7 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 79.0 | 95.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 299 | 36 | 15 | `httpx-0.28.1/tests/models/test_url.py` |
| cleanup | 23 | 8 | 1 | `httpx-0.28.1/httpx/_client.py` |
| guards | 1776 | 48 | 78 | `httpx-0.28.1/tests/models/test_url.py` |
| danger | 316 | 40 | 13 | `httpx-0.28.1/httpx/_models.py` |
| concurrency | 795 | 30 | 56 | `httpx-0.28.1/tests/client/test_auth.py` |
| connectivity | 1087 | 54 | 43 | `httpx-0.28.1/tests/models/test_responses.py` |
| io | 1221 | 46 | 49 | `httpx-0.28.1/tests/client/test_auth.py` |
| crypto | 9 | 7 | 1 | `httpx-0.28.1/httpx/_auth.py` |
| ipc | 0 | 0 | 0 | - |
| time | 9 | 5 | 0 | `httpx-0.28.1/httpx/_client.py` |
| serialization | 8 | 2 | 0 | `httpx-0.28.1/tests/models/test_requests.py` |
| regex | 19 | 5 | 0 | `httpx-0.28.1/httpx/_urlparse.py` |
| events | 102 | 12 | 3 | `httpx-0.28.1/tests/conftest.py` |
| tests | 892 | 35 | 39 | `httpx-0.28.1/tests/models/test_responses.py` |
| docs | 300 | 39 | 12 | `httpx-0.28.1/httpx/_models.py` |
| debt | 63 | 15 | 3 | `httpx-0.28.1/httpx/_main.py` |
| mutation | 6007 | 54 | 208 | `httpx-0.28.1/httpx/_client.py` |
| dead_code | 553 | 32 | 27 | `httpx-0.28.1/tests/models/test_responses.py` |
| credential | 5 | 3 | 0 | `httpx-0.28.1/tests/models/test_cookies.py` |
| threat | 77 | 15 | 2 | `httpx-0.28.1/httpx/_models.py` |
| ml_ai | 40 | 6 | 0 | `httpx-0.28.1/tests/models/test_url.py` |
| ui | 3 | 1 | 0 | `httpx-0.28.1/httpx/_multipart.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.1389**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `httpx-0.28.1/tests/client/test_auth.py` (Hits: 130)
- `httpx-0.28.1/tests/client/test_redirects.py` (Hits: 127)
- `httpx-0.28.1/tests/models/test_responses.py` (Hits: 111)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_models.py** (`httpx-0.28.1/httpx/_models.py`) — 12 inbound connections
2. **_types.py** (`httpx-0.28.1/httpx/_types.py`) — 12 inbound connections
3. **_exceptions.py** (`httpx-0.28.1/httpx/_exceptions.py`) — 9 inbound connections
4. **_urls.py** (`httpx-0.28.1/httpx/_urls.py`) — 8 inbound connections
5. **_utils.py** (`httpx-0.28.1/httpx/_utils.py`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_client.py** (`httpx-0.28.1/httpx/_client.py`) — 23 outbound dependencies
2. **_main.py** (`httpx-0.28.1/httpx/_main.py`) — 18 outbound dependencies
3. **_models.py** (`httpx-0.28.1/httpx/_models.py`) — 18 outbound dependencies
4. **__init__.py** (`httpx-0.28.1/httpx/__init__.py`) — 14 outbound dependencies
5. **default.py** (`httpx-0.28.1/httpx/_transports/default.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `urlparse` **(Many-Argument Workhorses)** (@ `httpx-0.28.1/httpx/_urlparse.py`) -> Impact: **96.7** | LOC: 133
  * *Intent:* # Initial basic checks on allowable URLs. # --------------------------------------- # Hard limit the maximum allowable URL length. if len(url) > MAX_U...
- `__init__` **(Defensive Guards)** (@ `httpx-0.28.1/httpx/_config.py`) -> Impact: **60.5** | LOC: 45
- `main` **(Many-Argument Workhorses)** (@ `httpx-0.28.1/httpx/_main.py`) -> Impact: **53.7** | LOC: 55
- `__init__` **(Many-Argument Workhorses)** (@ `httpx-0.28.1/httpx/_models.py`) -> Impact: **42.5** | LOC: 57
- `redirects` **(Compute Cores)** (@ `httpx-0.28.1/tests/client/test_redirects.py`) -> Impact: **42.1** | LOC: 106
- `__init__` **(Stateful Encapsulated Methods)** (@ `httpx-0.28.1/httpx/_urls.py`) -> Impact: **41.9** | LOC: 37
- `__init__` **(Many-Argument Workhorses)** (@ `httpx-0.28.1/httpx/_client.py`) -> Impact: **40.6** | LOC: 78
- `__init__` **(Many-Argument Workhorses)** (@ `httpx-0.28.1/httpx/_client.py`) -> Impact: **40.6** | LOC: 78
- `__init__` **(Stateful Encapsulated Methods)** (@ `httpx-0.28.1/httpx/_urls.py`) -> Impact: **34.4** | LOC: 48
- `__init__` **(Many-Argument Workhorses)** (@ `httpx-0.28.1/httpx/_transports/default.py`) -> Impact: **32.8** | LOC: 80

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `httpx-0.28.1/httpx` | 17 | 5390.32 | 42.67% | 16.27% |
| `httpx-0.28.1/tests/client` | 11 | 2531.76 | 27.37% | 0.0% |
| `httpx-0.28.1/tests` | 18 | 2398.9 | 18.66% | 0.0% |
| `httpx-0.28.1/tests/models` | 8 | 1462.36 | 22.6% | 0.0% |
| `httpx-0.28.1/httpx/_transports` | 5 | 517.5 | 40.08% | 0.0% |
| `httpx-0.28.1` | 3 | 26.58 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `httpx-0.28.1/httpx/_exceptions.py` -> **98.1139%** Exposure
- `httpx-0.28.1/httpx/_auth.py` -> **92.0768%** Exposure
- `httpx-0.28.1/httpx/_decoders.py` -> **44.3425%** Exposure
- `httpx-0.28.1/httpx/_urls.py` -> **42.1295%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `httpx-0.28.1/httpx/_auth.py` -> **100.0%** Exposure
- `httpx-0.28.1/httpx/_config.py` -> **100.0%** Exposure
- `httpx-0.28.1/httpx/_content.py` -> **100.0%** Exposure
- `httpx-0.28.1/httpx/_decoders.py` -> **100.0%** Exposure
- `httpx-0.28.1/httpx/_models.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `httpx-0.28.1/tests/models/test_responses.py` -> **71** Orphaned Functions | **4** Duplicates
- `httpx-0.28.1/tests/models/test_url.py` -> **69** Orphaned Functions | **0** Duplicates
- `httpx-0.28.1/tests/client/test_auth.py` -> **37** Orphaned Functions | **0** Duplicates
- `httpx-0.28.1/tests/client/test_client.py` -> **33** Orphaned Functions | **2** Duplicates
- `httpx-0.28.1/tests/test_content.py` -> **27** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `265` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `httpx-0.28.1/httpx/_models.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1244.06 | **LOC:** 1278 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **18**; blast radius 138.931; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 52.795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `delete` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `get` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `aiter_bytes` **(Defensive Guards)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 142 instances
* *Concurrency (weighted view):* 94
* *State Mutation (weighted view):* 457
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 233`, `args: 95`, `func_start: 95`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 173`
* *Architecture:* `api: 67`, `concurrency: 19`, `import: 18`
* *Defense:* `safety: 56`, `doc: 51`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 138.931
  * `Choke Point (Betweenness):` 0.033971 | `Ripple Effect (Closeness):` 0.233365
  * `Imports (Out-Degree: 8):` ._content, ._decoders, ._exceptions, ._multipart, ._status_codes, ._types, ._urls, ._utils...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_client.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1153.58 | **LOC:** 2020 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **23**; blast radius 8.342; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (78.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 77.3438% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `build_request` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `_send_handling_redirects` **(Stateful Encapsulated Methods)** (Impact: 19.7)
  * `_send_handling_redirects` **(Stateful Encapsulated Methods)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 162
* *State Mutation (weighted view):* 332
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 257`, `args: 81`, `func_start: 81`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 154`
* *Architecture:* `io: 8`, `api: 55`, `concurrency: 52`, `import: 24`
* *Defense:* `safety: 38`, `doc: 49`, `test: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.342
  * `Choke Point (Betweenness):` 0.004244 | `Ripple Effect (Closeness):` 0.04918
  * `Imports (Out-Degree: 12):` .__version__, ._auth, ._config, ._decoders, ._exceptions, ._models, ._status_codes, ._transports.base...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/client/test_auth.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 848.9 | **LOC:** 773 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 5.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.7%), Guard Balance (formerly Safety Score) (33.8%)
- **Documentation Coverage:** 78.4946% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `challenge_send` **(Compute Cores)** (Impact: 10.0)
  * `test_digest_auth` **(Defensive Guards)** (Impact: 7.5)
  * `__call__` **(Generic / Templated Code)** (Impact: 5.4)
  * `test_digest_auth_no_specified_qop` **(Defensive Guards)** (Impact: 4.4)
  * `auth_flow` **(Generic / Templated Code)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 78 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 477
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 277`, `args: 49`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 173`, `unreferenced_by_name: 37`
* *Architecture:* `io: 130`, `api: 48`, `concurrency: 87`, `import: 11`
* *Defense:* `safety: 102`, `doc: 15`, `test: 74`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..common, anyio, hashlib, httpx, netrc, os, pytest, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/models/test_responses.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 764.36 | **LOC:** 1038 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.7%), Guard Balance (formerly Safety Score) (16.5%)
- **Documentation Coverage:** 89.6774% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_raise_for_status` **(Defensive Guards)** (Impact: 7.8)
  * `test_aiter_raw_with_chunksize` **(Defensive Guards)** (Impact: 4.8)
  * `test_aiter_bytes_with_chunk_size` **(Defensive Guards)** (Impact: 4.6)
  * `test_aiter_text_with_chunk_size` **(Defensive Guards)** (Impact: 4.6)
  * `test_cannot_read_after_stream_consumed` **(I/O & Config Routines)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 40 instances
* *Amplified Cascading Flux:* 49 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 243
* *State Mutation (weighted view):* 279
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 293`, `args: 78`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 181`, `duplicate_logic: 4`, `unreferenced_by_name: 71`
* *Architecture:* `io: 111`, `api: 78`, `concurrency: 43`, `import: 6`
* *Defense:* `safety: 172`, `doc: 8`, `test: 115`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chardet, httpx, json, pickle, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/client/test_async_client.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 581.14 | **LOC:** 376 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (48.1%), Guard Balance (formerly Safety Score) (14.8%)
- **Documentation Coverage:** 97.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_raise_for_status` **(Defensive Guards)** (Impact: 6.3)
  * `test_context_managed_transport_and_mount` **(Interface Declarations)** (Impact: 2.9)
  * `test_cancellation_during_stream` **(Interface Declarations)** (Impact: 2.9)
    * *Intent:* """ If any BaseException is raised during streaming the response, then the stream should be closed. ...
  * `test_context_managed_transport` **(Interface Declarations)** (Impact: 2.5)
  * `response_with_cancel_during_stream` **(Generic / Templated Code)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 65 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 414
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 194`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 46`, `unreferenced_by_name: 25`
* *Architecture:* `io: 49`, `api: 37`, `concurrency: 89`, `import: 5`
* *Defense:* `safety: 45`, `doc: 1`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, datetime, httpx, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/test_content.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 495.98 | **LOC:** 519 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (50.0%), Connectivity (formerly Api Exposure) (10.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_aiterator_content` **(Defensive Guards)** (Impact: 5.7)
  * `test_multipart_multiple_files_single_input_content` **(I/O & Config Routines)** (Impact: 4.4)
  * `test_bytes_content` **(Defensive Guards)** (Impact: 4.2)
  * `test_multipart_data_and_files_content` **(Defensive Guards)** (Impact: 4.2)
  * `test_multipart_files_content` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 233
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 155`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `duplicate_logic: 4`, `unreferenced_by_name: 27`
* *Architecture:* `io: 36`, `api: 30`, `concurrency: 43`, `import: 4`
* *Defense:* `safety: 150`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httpx, io, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/test_asgi.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 481.04 | **LOC:** 225 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (61.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.8%)
- **Documentation Coverage:** 95.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_body` **(Parameter Forwarders)** (Impact: 5.1)
  * `echo_body` **(Parameter Forwarders)** (Impact: 4.5)
  * `echo_headers` **(Type Conversions)** (Impact: 4.5)
  * `test_asgi_disconnect_after_response_complete` **(Interface Declarations)** (Impact: 3.6)
  * `hello_world` **(Type Conversions)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 55 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 338
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 122`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 12`
* *Architecture:* `io: 30`, `api: 20`, `concurrency: 63`, `import: 3`
* *Defense:* `safety: 19`, `doc: 1`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httpx, json, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_urlparse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 424.5 | **LOC:** 528 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 35.049; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.7%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlparse` **(Many-Argument Workhorses)** (Impact: 96.7)
    * *Intent:* # Initial basic checks on allowable URLs. # --------------------------------------- # Hard limit the...
  * `validate_path` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* """ Path validation rules that depend on if the URL contains a scheme or authority component. See ht...
  * `normalize_path` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* """ Drop "." and ".." segments from a URL path. For example: normalize_path("/path/./to/somewhere/.....
  * `quote` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* """ Use percent-encoding to quote a string, omitting existing '%xx' escape sequences. See: https://w...
  * `__str__` **(Compute Cores)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 48`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 69`
* *Architecture:* `api: 13`, `import: 6`
* *Defense:* `safety: 11`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.049
  * `Choke Point (Betweenness):` 0.003461 | `Ripple Effect (Closeness):` 0.141686
  * `Imports (Out-Degree: 1):` ._exceptions, __future__, idna, ipaddress, re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/client/test_redirects.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 365.88 | **LOC:** 448 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Guard Balance (formerly Safety Score) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.3%)
- **Documentation Coverage:** 90.625% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `redirects` **(Compute Cores)** (Impact: 42.1)
  * `cookie_sessions` **(Compute Cores)** (Impact: 10.0)
  * `test_redirect_cookie_behavior` **(Defensive Guards)** (Impact: 2.5)
  * `handle_request` **(Type Conversions)** (Impact: 1.9)
  * `test_next_request` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 158`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 113`, `unreferenced_by_name: 29`
* *Architecture:* `io: 127`, `api: 33`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 78`, `doc: 3`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httpx, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_urls.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 358.04 | **LOC:** 642 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **9**; blast radius 86.914; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.5%)
- **Documentation Coverage:** 37.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 41.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 34.4)
  * `__repr__` **(Compute Cores)** (Impact: 23.9)
  * `raw_path` **(Generic / Templated Code)** (Impact: 5.0)
    * *Intent:* """ The complete URL path and query string as raw bytes. Used as the target when constructing HTTP r...
  * `multi_items` **(Generic / Templated Code)** (Impact: 4.9)
    * *Intent:* """ Return all items in the query params. Allow duplicate keys to occur. Usage: q = httpx.QueryParam...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 121`, `args: 50`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 44`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 43`, `import: 10`
* *Defense:* `safety: 13`, `doc: 30`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 86.914
  * `Choke Point (Betweenness):` 0.006211 | `Ripple Effect (Closeness):` 0.193523
  * `Imports (Out-Degree: 3):` ._types, ._urlparse, ._utils, __future__, collections, idna, typing, urllib.parse...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 353.42 | **LOC:** 288 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 10.425; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (82.2%), Connectivity (formerly Api Exposure) (63.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `app` **(Defensive Guards)** (Impact: 18.9)
  * `watch_restarts` **(Defensive Guards)** (Impact: 4.9)
  * `echo_body` **(Generic / Templated Code)** (Impact: 4.8)
  * `echo_binary` **(Generic / Templated Code)** (Impact: 4.8)
  * `clean_environ` **(I/O & Config Routines)** (Impact: 4.7)
    * *Intent:* """Keeps os.environ clean for every test without having to mock os.environ"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 175
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 112`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`
* *Architecture:* `io: 3`, `api: 23`, `concurrency: 55`, `import: 14`
* *Defense:* `safety: 5`, `doc: 1`, `test: 15`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.425
  * `Choke Point (Betweenness):` 0.000273 | `Ripple Effect (Closeness):` 0.016393
  * `Imports (Out-Degree: 1):` asyncio, cryptography.hazmat.backends, cryptography.hazmat.primitives.serialization, httpx, json, os, pytest, tests.concurrency...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 334.88 | **LOC:** 507 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 6.034; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Complexity Load (formerly Cognitive Load) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 53.7)
  * `trace` **(Many-Argument Workhorses)** (Impact: 29.9)
  * `format_certificate` **(Defensive Guards)** (Impact: 14.9)
  * `format_request_headers` **(Compute Cores)** (Impact: 12.7)
  * `print_help` **(I/O & Config Routines)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 81`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 57`
* *Architecture:* `io: 3`, `api: 14`, `import: 18`
* *Defense:* `safety: 10`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016393
  * `Imports (Out-Degree: 4):` ._client, ._exceptions, ._models, ._status_codes, __future__, click, functools, httpcore...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 302.74 | **LOC:** 249 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 31.789; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Complexity Load (formerly Cognitive Load) (70.5%), Connectivity (formerly Api Exposure) (54.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 60.5)
  * `create_ssl_context` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `__repr__` **(Type Conversions)** (Impact: 10.3)
    * *Intent:* # The authentication is represented with the password component masked. auth = (self.auth[0], "*****...
  * `__eq__` **(Defensive Guards)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 46`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 54`
* *Architecture:* `io: 2`, `api: 8`, `import: 10`
* *Defense:* `safety: 19`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.789
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.155577
  * `Imports (Out-Degree: 3):` ._models, ._types, ._urls, __future__, certifi, os, ssl, typing...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_decoders.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 298.44 | **LOC:** 394 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 20.987; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.5%), Connectivity (formerly Api Exposure) (60.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 98.1132% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Compute Cores)** (Impact: 16.7)
  * `decode` **(Compute Cores)** (Impact: 16.7)
  * `decode` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* # See https://docs.python.org/3/library/stdtypes.html#str.splitlines NEWLINE_CHARS = "\n\r\x0b\x0c\x...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 7.9)
  * `decode` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 104`, `args: 31`, `func_start: 31`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 53`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 33`, `import: 9`
* *Defense:* `safety: 23`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.149706
  * `Imports (Out-Degree: 1):` ._exceptions, __future__, brotli, brotlicffi, codecs, io, typing, zlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/models/test_url.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 286.62 | **LOC:** 864 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.6%), Complexity Load (formerly Cognitive Load) (10.3%), Dead Code Surface (formerly Dead Code) (5.2%)
- **Documentation Coverage:** 79.7101% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_url_join` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* # Tests for `URL.join()`. """ Some basic URL joining tests. """
  * `test_relative_url_join` **(Defensive Guards)** (Impact: 9.3)
  * `test_url_join_rfc3986` **(Defensive Guards)** (Impact: 3.7)
    * *Intent:* """ URL joining tests, as-per reference examples in RFC 3986. https://tools.ietf.org/html/rfc3986#se...
  * `test_url_set` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* """ Ensure that `httpx.URL` instances can be used in sets. """
  * `test_idna_url` **(Defensive Guards)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 300`, `args: 69`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 78`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 69`
* *Architecture:* `io: 98`, `api: 70`, `import: 2`
* *Defense:* `safety: 184`, `doc: 14`, `test: 96`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httpx, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_auth.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 277.64 | **LOC:** 349 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 29.711; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Debt Markers (formerly Tech Debt) (92.1%), Concurrency Surface (formerly Concurrency) (91.6%)
- **Documentation Coverage:** 92.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `auth_flow` **(Stateful Encapsulated Methods)** (Impact: 15.4)
  * `_parse_challenge` **(Stateful Encapsulated Methods)** (Impact: 14.9)
  * `_build_auth_header` **(Stateful Encapsulated Methods)** (Impact: 14.3)
  * `_get_header_value` **(Stateful Encapsulated Methods)** (Impact: 9.5)
  * `_resolve_qop` **(Stateful Encapsulated Methods)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 64`, `args: 19`, `func_start: 19`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 61`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 3`, `import: 13`
* *Defense:* `safety: 7`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.711
  * `Choke Point (Betweenness):` 0.000601 | `Ripple Effect (Closeness):` 0.149706
  * `Imports (Out-Degree: 3):` ._exceptions, ._models, ._utils, __future__, base64, hashlib, netrc, os...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_multipart.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 256.14 | **LOC:** 301 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 24.815; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.8%), Complexity Load (formerly Cognitive Load) (54.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 89.1892% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `__init__` **(Defensive Guards)** (Impact: 16.7)
  * `_iter_fields` **(Stateful Encapsulated Methods)** (Impact: 16.6)
  * `get_multipart_boundary_from_content_type` **(Compute Cores)** (Impact: 9.1)
  * `render_headers` **(Stateful Encapsulated Methods)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 65`, `args: 21`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 40`
* *Architecture:* `io: 2`, `api: 18`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 16`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.815
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.152585
  * `Imports (Out-Degree: 2):` ._types, ._utils, __future__, io, mimetypes, os, pathlib, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/client/test_client.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 227.4 | **LOC:** 463 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (26.4%), Guard Balance (formerly Safety Score) (15.5%), Concurrency Surface (formerly Concurrency) (14.6%)
- **Documentation Coverage:** 97.8261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_raise_for_status` **(Defensive Guards)** (Impact: 6.3)
  * `test_stream_iterator` **(Defensive Guards)** (Impact: 3.3)
  * `test_raw_iterator` **(Defensive Guards)** (Impact: 3.3)
  * `echo_raw_headers` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_context_managed_transport_and_mount` **(Interface Declarations)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 203`, `args: 49`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 74`, `duplicate_logic: 2`, `unreferenced_by_name: 33`
* *Architecture:* `io: 62`, `api: 45`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 76`, `doc: 1`, `test: 45`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, chardet, datetime, httpx, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_content.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 227.26 | **LOC:** 241 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 20.795; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Complexity Load (formerly Cognitive Load) (81.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_request` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `encode_content` **(Defensive Guards)** (Impact: 18.3)
  * `encode_response` **(Generic / Templated Code)** (Impact: 12.2)
  * `__iter__` **(Stateful Encapsulated Methods)** (Impact: 10.6)
  * `__aiter__` **(Stateful Encapsulated Methods)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 63`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 45`, `dead_code: 1`
* *Architecture:* `api: 13`, `concurrency: 6`, `import: 10`
* *Defense:* `safety: 9`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.795
  * `Choke Point (Betweenness):` 0.000191 | `Ripple Effect (Closeness):` 0.149706
  * `Imports (Out-Degree: 4):` ._exceptions, ._multipart, ._types, ._utils, __future__, inspect, json, typing...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/test_decoders.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 204.98 | **LOC:** 356 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.9%), Guard Balance (formerly Safety Score) (44.3%)
- **Documentation Coverage:** 92.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_text_decoder_with_autodetect` **(Defensive Guards)** (Impact: 6.2)
  * `iterator` **(Generic / Templated Code)** (Impact: 2.2)
  * `test_zstd_multiframe` **(I/O & Config Routines)** (Impact: 2.0)
    * *Intent:* # test inspired by urllib3 test suite data = ( # Zstandard frame zstd.compress(b"foo") # skippable f...
  * `test_multi_with_identity` **(I/O & Config Routines)** (Impact: 2.0)
  * `test_streaming_text_decoder` **(Generic / Templated Code)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 77`, `args: 27`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 77`, `unreferenced_by_name: 23`
* *Architecture:* `io: 39`, `api: 27`, `concurrency: 10`, `import: 8`
* *Defense:* `safety: 32`, `doc: 2`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, chardet, httpx, io, pytest, typing, zlib, zstandard
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_transports/default.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 201.78 | **LOC:** 407 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 7.423; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Concurrency Surface (formerly Concurrency) (86.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `map_httpcore_exceptions` **(Defensive Guards)** (Impact: 8.2)
  * `handle_request` **(Defensive Guards)** (Impact: 3.2)
  * `handle_async_request` **(Defensive Guards)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 81`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `io: 7`, `api: 18`, `concurrency: 12`, `import: 19`
* *Defense:* `safety: 19`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.423
  * `Choke Point (Betweenness):` 0.001726 | `Ripple Effect (Closeness):` 0.05123
  * `Imports (Out-Degree: 6):` .._config, .._exceptions, .._models, .._types, .._urls, .base, __future__, contextlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 190.46 | **LOC:** 243 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 73.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Connectivity (formerly Api Exposure) (73.0%), Complexity Load (formerly Cognitive Load) (50.1%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Compute Cores)** (Impact: 22.2)
  * `get_environment_proxies` **(I/O & Config Routines)** (Impact: 16.4)
    * *Intent:* """Gets proxy information from the environment"""
  * `matches` **(Compute Cores)** (Impact: 16.2)
  * `primitive_value_to_str` **(Type Conversions)** (Impact: 6.3)
    * *Intent:* """ Coerce a primitive data type into a string value. Note that we prefer JSON-style 'true'/'false' ...
  * `to_bytes` **(Defensive Guards)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 54`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 27`
* *Architecture:* `io: 2`, `api: 16`, `import: 9`
* *Defense:* `safety: 8`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 73.784
  * `Choke Point (Betweenness):` 0.004098 | `Ripple Effect (Closeness):` 0.184522
  * `Imports (Out-Degree: 2):` ._types, ._urls, __future__, ipaddress, os, re, typing, urllib.request
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/test_multipart.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 189.34 | **LOC:** 470 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.3%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 92.1569% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multipart_invalid_key` **(Type Conversions)** (Impact: 3.5)
  * `test_multipart_encode` **(Type Conversions)** (Impact: 3.5)
  * `test_multipart_invalid_value` **(Type Conversions)** (Impact: 3.2)
  * `test_multipart` **(Defensive Guards)** (Impact: 3.0)
  * `test_multipart_encode_non_seekable_filelike` **(Generic / Templated Code)** (Impact: 3.0)
    * *Intent:* """ Test that special readable but non-seekable filelike objects are supported. In this case uploads...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 93`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 99`, `unreferenced_by_name: 23`
* *Architecture:* `io: 35`, `api: 27`, `import: 6`
* *Defense:* `safety: 38`, `doc: 2`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, httpx, io, pytest, tempfile, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_transports/asgi.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 163.32 | **LOC:** 188 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 6.832; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Complexity Load (formerly Cognitive Load) (90.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_async_request` **(Defensive Guards)** (Impact: 23.5)
  * `send` **(Defensive Guards)** (Impact: 9.5)
  * `__init__` **(Generic / Templated Code)** (Impact: 3.0)
  * `is_running_trio` **(Defensive Guards)** (Impact: 2.6)
  * `receive` **(Defensive Guards)** (Impact: 2.6)
    * *Intent:* # ASGI callables.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 46
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 50`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 32`
* *Architecture:* `api: 8`, `concurrency: 11`, `import: 10`
* *Defense:* `safety: 12`, `doc: 1`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.832
  * `Choke Point (Betweenness):` 0.000578 | `Ripple Effect (Closeness):` 0.016393
  * `Imports (Out-Degree: 3):` .._models, .._types, .base, __future__, asyncio, sniffio, trio, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/models/test_requests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 159.36 | **LOC:** 242 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 5.635; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.2%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 96.7213% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_aread_and_stream_data` **(Defensive Guards)** (Impact: 2.5)
    * *Intent:* # Ensure a request may still be streamed if it has been read. # Needed for cases such as authenticat...
  * `test_ignore_transfer_encoding_header_if_content_length_exists` **(Defensive Guards)** (Impact: 1.8)
    * *Intent:* """ `Transfer-Encoding` should be ignored if `Content-Length` has been set explicitly. See https://g...
  * `test_request_async_streaming_content_picklable` **(Annotated & Test Methods)** (Impact: 1.8)
  * `test_request_generator_content_picklable` **(Annotated & Test Methods)** (Impact: 1.8)
  * `test_url` **(Defensive Guards)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 87`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 45`, `duplicate_logic: 6`, `unreferenced_by_name: 23`
* *Architecture:* `io: 33`, `api: 31`, `concurrency: 9`, `import: 4`
* *Defense:* `safety: 45`, `doc: 1`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httpx, pickle, pytest, typing
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

- `httpx-0.28.1/httpx/_models.py` -> **Severity: 3.397** (Bridge: 0.034 * Flux: 100.0%)
- `httpx-0.28.1/httpx/_types.py` -> **Severity: 1.646** (Bridge: 0.0165 * Flux: 99.8309%)
- `httpx-0.28.1/httpx/_exceptions.py` -> **Severity: 0.833** (Bridge: 0.0086 * Flux: 96.7906%)
- `httpx-0.28.1/httpx/_urls.py` -> **Severity: 0.621** (Bridge: 0.0062 * Flux: 99.9997%)
- `httpx-0.28.1/httpx/_client.py` -> **Severity: 0.424** (Bridge: 0.0042 * Flux: 99.8953%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `httpx-0.28.1/httpx/_models.py` -> **Severity: 22.078** (Embedded: 0.2334 * Error Risk: 94.6069%)
- `httpx-0.28.1/httpx/_types.py` -> **Severity: 19.747** (Embedded: 0.2204 * Error Risk: 89.5943%)
- `httpx-0.28.1/httpx/_urls.py` -> **Severity: 18.197** (Embedded: 0.1935 * Error Risk: 94.0327%)
- `httpx-0.28.1/httpx/_utils.py` -> **Severity: 17.855** (Embedded: 0.1845 * Error Risk: 96.7661%)
- `httpx-0.28.1/httpx/_status_codes.py` -> **Severity: 15.57** (Embedded: 0.1606 * Error Risk: 96.9493%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `httpx-0.28.1/httpx/_exceptions.py` -> **Severity: 8418.7** (Blast Radius: 84.187 * Doc Risk: 100.0%)
- `httpx-0.28.1/httpx/_types.py` -> **Severity: 8148.45** (Blast Radius: 108.646 * Doc Risk: 75.0%)
- `httpx-0.28.1/httpx/_models.py` -> **Severity: 7334.862** (Blast Radius: 138.931 * Doc Risk: 52.795%)
- `httpx-0.28.1/httpx/_utils.py` -> **Severity: 5410.824** (Blast Radius: 73.784 * Doc Risk: 73.3333%)
- `httpx-0.28.1/httpx/_urls.py` -> **Severity: 3283.42** (Blast Radius: 86.914 * Doc Risk: 37.7778%)

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
