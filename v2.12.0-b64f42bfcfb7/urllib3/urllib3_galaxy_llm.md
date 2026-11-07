# ARCHITECTURAL_BRIEF: urllib3
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
- **Scope:** 84 analyzed artifact(s), 22715 LOC.
- **Load-bearing artifact:** `urllib3-2.6.3/src/urllib3/exceptions.py` -- 38 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` -- pulls in 36 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` at magnitude 1701.24 (structural weight, not risk).
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
| Total Artifacts | 94 |
| Analyzed Artifacts (Scanned) | 84 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 22715 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2596 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1393 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 25.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2816 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 80 | 22376 | 95.2% |
| PLAINTEXT | 1 | 0 | 1.2% |
| MARKDOWN | 1 | 0 | 1.2% |
| JAVASCRIPT | 1 | 92 | 1.2% |
| HTML | 1 | 247 | 1.2% |

## 4.1 SOURCE ENCODINGS
All 84 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 38%, Large Core Modules (2) 33%, Data / Markup / Trivial 10%, Large Core Modules (3) 8%, Many-Argument Workhorses Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 82 | 97.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.pem`: 2x Excluded (Unsupported Extension: '.pem')
- `.crt`: 1x Excluded (Unsupported Extension: '.crt')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 32.7 | 27.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 50.7 | 52.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.6 | 5.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 97.3 | 30.6 | 25.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.8 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 72.4 | 87.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 332 | 45 | 10 | `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` |
| cleanup | 208 | 27 | 6 | `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` |
| guards | 2640 | 69 | 89 | `urllib3-2.6.3/test/test_response.py` |
| danger | 550 | 60 | 21 | `urllib3-2.6.3/src/urllib3/response.py` |
| concurrency | 395 | 32 | 13 | `urllib3-2.6.3/dummyserver/app.py` |
| connectivity | 1767 | 76 | 53 | `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` |
| io | 619 | 48 | 18 | `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` |
| crypto | 41 | 24 | 1 | `urllib3-2.6.3/src/urllib3/contrib/pyopenssl.py` |
| ipc | 12 | 12 | 1 | `urllib3-2.6.3/dummyserver/testcase.py` |
| time | 29 | 11 | 1 | `urllib3-2.6.3/dummyserver/app.py` |
| serialization | 2 | 2 | 0 | `urllib3-2.6.3/test/test_exceptions.py` |
| regex | 18 | 6 | 0 | `urllib3-2.6.3/src/urllib3/util/url.py` |
| events | 172 | 17 | 4 | `urllib3-2.6.3/test/contrib/test_socks.py` |
| tests | 1952 | 36 | 69 | `urllib3-2.6.3/test/test_response.py` |
| docs | 430 | 58 | 13 | `urllib3-2.6.3/src/urllib3/exceptions.py` |
| debt | 101 | 28 | 3 | `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` |
| mutation | 9767 | 76 | 293 | `urllib3-2.6.3/test/test_response.py` |
| dead_code | 494 | 27 | 25 | `urllib3-2.6.3/test/with_dummyserver/test_connectionpool.py` |
| credential | 2 | 1 | 0 | `urllib3-2.6.3/src/urllib3/util/url.py` |
| threat | 17 | 3 | 0 | `urllib3-2.6.3/test/with_dummyserver/test_chunked_transfer.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 1 | 1 | 0 | `urllib3-2.6.3/test/contrib/emscripten/templates/pyodide-console.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.775**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` (Hits: 147)
- `urllib3-2.6.3/test/contrib/test_socks.py` (Hits: 57)
- `urllib3-2.6.3/test/test_util.py` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **exceptions.py** (`urllib3-2.6.3/src/urllib3/exceptions.py`) — 38 inbound connections
2. **connectionpool.py** (`urllib3-2.6.3/src/urllib3/connectionpool.py`) — 23 inbound connections
3. **response.py** (`urllib3-2.6.3/src/urllib3/response.py`) — 22 inbound connections
4. **connection.py** (`urllib3-2.6.3/src/urllib3/connection.py`) — 21 inbound connections
5. **__init__.py** (`urllib3-2.6.3/src/urllib3/util/__init__.py`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_socketlevel.py** (`urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py`) — 36 outbound dependencies
2. **test_https.py** (`urllib3-2.6.3/test/with_dummyserver/test_https.py`) — 29 outbound dependencies
3. **connection.py** (`urllib3-2.6.3/src/urllib3/connection.py`) — 28 outbound dependencies
4. **test_util.py** (`urllib3-2.6.3/test/test_util.py`) — 28 outbound dependencies
5. **test_connectionpool.py** (`urllib3-2.6.3/test/with_dummyserver/test_connectionpool.py`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `urlopen` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connectionpool.py`) -> Impact: **142.1** | LOC: 369
- `_ssl_wrap_socket_and_match_hostname` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> Impact: **109.2** | LOC: 123
- `increment` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/retry.py`) -> Impact: **81.2** | LOC: 96
- `create_urllib3_context` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/ssl_.py`) -> Impact: **78.2** | LOC: 150
- `request` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> Impact: **74.4** | LOC: 96
  * *Intent:* # `request` method's signature intentionally violates LSP. # urllib3's API is different from `http.client.HTTPConnection` and the subclassing is only ...
- `match_hostname` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py`) -> Impact: **55.2** | LOC: 65
- `ssl_wrap_socket` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/util/ssl_.py`) -> Impact: **52.2** | LOC: 72
- `read` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/response.py`) -> Impact: **51.7** | LOC: 95
- `_make_request` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/connectionpool.py`) -> Impact: **46.4** | LOC: 180
- `read1` **(Many-Argument Workhorses)** (@ `urllib3-2.6.3/src/urllib3/response.py`) -> Impact: **45.5** | LOC: 69

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `urllib3-2.6.3/test` | 22 | 4169.56 | 15.6% | 0.0% |
| `urllib3-2.6.3/src/urllib3` | 12 | 4051.9 | 39.55% | 14.98% |
| `urllib3-2.6.3/test/with_dummyserver` | 9 | 3972.14 | 15.6% | 0.0% |
| `urllib3-2.6.3/src/urllib3/util` | 13 | 2049.74 | 39.83% | 7.02% |
| `urllib3-2.6.3/dummyserver` | 6 | 1529.68 | 68.29% | 7.4% |
| `urllib3-2.6.3/src/urllib3/http2` | 3 | 414.16 | 57.4% | 12.03% |
| `urllib3-2.6.3/src/urllib3/contrib/emscripten` | 6 | 9.9 | 56.58% | 16.26% |
| `urllib3-2.6.3/test/contrib/emscripten` | 3 | 8.05 | 14.85% | 0.0% |
| `urllib3-2.6.3/test/contrib` | 4 | 5.65 | 7.33% | 0.0% |
| `urllib3-2.6.3/src/urllib3/contrib` | 3 | 4.37 | 36.71% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py` -> **97.5834%** Exposure
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **96.0443%** Exposure
- `urllib3-2.6.3/src/urllib3/util/response.py` -> **62.2459%** Exposure
- `urllib3-2.6.3/src/urllib3/response.py` -> **37.8992%** Exposure
- `urllib3-2.6.3/dummyserver/testcase.py` -> **33.0066%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `urllib3-2.6.3/dummyserver/app.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/hypercornserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/socketserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/_collections.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/connection.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `urllib3-2.6.3/test/with_dummyserver/test_connectionpool.py` -> **86** Orphaned Functions | **0** Duplicates
- `urllib3-2.6.3/test/test_collections.py` -> **50** Orphaned Functions | **0** Duplicates
- `urllib3-2.6.3/test/contrib/emscripten/test_emscripten.py` -> **41** Orphaned Functions | **3** Duplicates
- `urllib3-2.6.3/test/with_dummyserver/test_proxy_poolmanager.py` -> **43** Orphaned Functions | **0** Duplicates
- `urllib3-2.6.3/test/with_dummyserver/test_poolmanager.py` -> **40** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `721` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.421)
- **Top Global Matches:** file_cluster_0: 8.421, file_cluster_12: 8.449, file_cluster_5: 8.601
- **Magnitude:** 1701.24 | **LOC:** 2762 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **36**; blast radius 3.965; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.8%), Guard Balance (formerly Safety Score) (56.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (23.5%)
- **Documentation Coverage:** 93.871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `original_ssl_wrap_socket` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `test_chunked_specified` **(Defensive Guards)** (Impact: 25.6)
  * `test_chunked_not_specified` **(Defensive Guards)** (Impact: 25.6)
  * `_test_broken_header_parsing` **(Stateful Encapsulated Methods)** (Impact: 15.4)
  * `test_multipart_assert_header_parsing_no_defects` **(Defensive Guards)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 164 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 691
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 636`, `args: 162`, `func_start: 160`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 363`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 22`
* *Architecture:* `io: 147`, `api: 170`, `concurrency: 7`, `import: 38`
* *Defense:* `safety: 174`, `doc: 13`, `test: 140`, `sync_locks: 34`, `cleanup: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.965
  * `Choke Point (Betweenness):` 0.001842 | `Ripple Effect (Closeness):` 0.012048
  * `Imports (Out-Degree: 16):` ..LogRecorder, __future__, _typeshed, collections, contextlib, dummyserver.socketserver, dummyserver.testcase, errno...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/test_response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.094)
- **Top Global Matches:** file_cluster_0: 7.094, file_cluster_12: 9.389, file_cluster_5: 9.672
- **Magnitude:** 1313.68 | **LOC:** 1996 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 3.677; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (70.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.1%), Complexity Load (formerly Cognitive Load) (41.0%)
- **Documentation Coverage:** 98.8848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pop_current_chunk` **(Defensive Guards)** (Impact: 21.4)
  * `test_memory_usage_decode_with_max_length` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* # We set the 10 MB limit to ensure that the whole decompressed data # is not stored unnecessarily. #...
  * `test_io_not_closed_until_all_data_is_read` **(Defensive Guards)** (Impact: 13.7)
  * `test_deflate_streaming_tell_intermediate_point` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* # Ensure that ``tell()`` returns the correct number of bytes when # part-way through streaming compr...
  * `test_read_chunked_with_all_data_already_in_decompressor` **(Many-Argument Workhorses)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 690
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 554`, `args: 140`, `func_start: 135`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 466`, `dead_code: 2`
* *Architecture:* `io: 17`, `api: 136`, `import: 21`
* *Defense:* `safety: 283`, `doc: 6`, `test: 208`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.677
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.012048
  * `Imports (Out-Degree: 5):` __future__, backports, base64, compression, contextlib, gzip, http.client, io...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.025)
- **Top Global Matches:** file_cluster_4: 8.025, file_cluster_0: 9.709, file_cluster_16: 10.566
- **Magnitude:** 1266.04 | **LOC:** 1481 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **24**; blast radius 65.811; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (76.0%), Guard Balance (formerly Safety Score) (69.8%), Connectivity (formerly Api Exposure) (54.1%)
- **Documentation Coverage:** 89.2617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `read1` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `read_chunked` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `_fp_read` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `_raw_read` **(Many-Argument Workhorses)** (Impact: 34.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 270`, `args: 82`, `func_start: 82`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 183`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 73`, `import: 27`
* *Defense:* `safety: 45`, `doc: 20`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 65.811
  * `Choke Point (Betweenness):` 0.024741 | `Ripple Effect (Closeness):` 0.407182
  * `Imports (Out-Degree: 8):` ._base_connection, ._collections, .connection, .connectionpool, .exceptions, .util, .util.response, .util.retry...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/app.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.157)
- **Top Global Matches:** file_cluster_0: 7.157, file_cluster_10: 9.932, file_cluster_13: 10.045
- **Magnitude:** 827.14 | **LOC:** 484 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 7.98; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (90.5%), Complexity Load (formerly Cognitive Load) (86.0%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pyodide_upload` **(Compute Cores)** (Impact: 10.0)
  * `encodingrequest` **(I/O & Config Routines)** (Impact: 7.0)
  * `upload` **(Type Conversions)** (Impact: 6.4)
  * `_get_pyodide_template` **(Stateful Encapsulated Methods)** (Impact: 5.6)
    * *Intent:* # serve code to run pyodide in a webworker, or html template # these are included in pytest_pyodide,...
  * `successful_retry` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* """First return an error and then success It's not currently very flexible as the number of retries ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 62 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 404
* *State Mutation (weighted view):* 232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 188`, `args: 42`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 96`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 76`, `concurrency: 94`, `import: 15`
* *Defense:* `safety: 4`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.106356
  * `Imports (Out-Degree: 0):` __future__, collections, collections.abc, contextlib, datetime, email.utils, gzip, io...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/connection.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.363)
- **Top Global Matches:** file_cluster_4: 7.363, file_cluster_6: 10.539, file_cluster_12: 12.409
- **Magnitude:** 780.7 | **LOC:** 1100 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **28**; blast radius 55.2; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (70.5%), Guard Balance (formerly Safety Score) (68.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_ssl_wrap_socket_and_match_hostname` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `request` **(Many-Argument Workhorses)** (Impact: 74.4)
    * *Intent:* # `request` method's signature intentionally violates LSP. # urllib3's API is different from `http.c...
  * `connect` **(I/O & Config Routines)** (Impact: 33.7)
    * *Intent:* # Today we don't need to be doing this step before the /actual/ socket # connection, however in the ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `set_cert` **(Many-Argument Workhorses)** (Impact: 25.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 140`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 143`, `planned_debt: 4`
* *Architecture:* `io: 27`, `api: 24`, `concurrency: 3`, `import: 37`
* *Defense:* `safety: 21`, `doc: 17`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 55.2
  * `Choke Point (Betweenness):` 0.059154 | `Ripple Effect (Closeness):` 0.39196
  * `Imports (Out-Degree: 18):` ._base_connection, ._collections, ._version, .exceptions, .http2, .response, .util, .util.request...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/with_dummyserver/test_connectionpool.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.519)
- **Top Global Matches:** file_cluster_0: 6.519, file_cluster_15: 9.326, file_cluster_13: 9.364
- **Magnitude:** 636.8 | **LOC:** 1477 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.9%), Complexity Load (formerly Cognitive Load) (18.5%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 79.3103% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_headers_not_modified_by_request` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `test_http2_test_error` **(Defensive Guards)** (Impact: 7.4)
  * `test_source_address_error` **(Generic / Templated Code)** (Impact: 6.7)
  * `test_skip_header_non_supported` **(Type Conversions)** (Impact: 6.7)
  * `test_user_agent_header_not_sent_twice` **(Defensive Guards)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 533`, `args: 87`, `func_start: 87`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 234`, `planned_debt: 3`, `unreferenced_by_name: 86`
* *Architecture:* `io: 18`, `api: 96`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 172`, `doc: 21`, `test: 140`, `sync_locks: 7`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` ..INVALID_SOURCE_ADDRESSES, ..TARPIT_HOST, ..VALID_SOURCE_ADDRESSES, ..port_helpers, __future__, dummyserver.socketserver, dummyserver.testcase, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/connectionpool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.127)
- **Top Global Matches:** file_cluster_5: 8.127, file_cluster_12: 8.606, file_cluster_4: 9.37
- **Magnitude:** 614.58 | **LOC:** 1179 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **26**; blast radius 61.869; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlopen` **(Many-Argument Workhorses)** (Impact: 142.1)
  * `_make_request` **(Many-Argument Workhorses)** (Impact: 46.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `is_same_host` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* """ Check if the given ``url`` is a member of the same host as this connection pool. """
  * `_get_conn` **(Stateful Encapsulated Methods)** (Impact: 14.0)
    * *Intent:* """ Get a connection. Will return a pooled connection if one is available. If no connections are ava...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 130`, `args: 27`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 100`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 12`, `import: 30`
* *Defense:* `safety: 32`, `doc: 21`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 61.869
  * `Choke Point (Betweenness):` 0.04871 | `Ripple Effect (Closeness):` 0.399426
  * `Imports (Out-Degree: 14):` ._base_connection, ._collections, ._request_methods, .connection, .exceptions, .response, .util.connection, .util.proxy...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/with_dummyserver/test_https.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.644)
- **Top Global Matches:** file_cluster_0: 7.644, file_cluster_12: 7.899, file_cluster_5: 8.421
- **Magnitude:** 608.38 | **LOC:** 1353 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 3.965; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (67.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.5%), Concurrency Surface (formerly Concurrency) (17.0%)
- **Documentation Coverage:** 90.0709% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ssl_version` **(Compute Cores)** (Impact: 16.3)
  * `test_hostname_checks_common_name_respected` **(Defensive Guards)** (Impact: 15.9)
  * `test_sslkeylogfile` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `test_ssl_version_is_deprecated` **(Defensive Guards)** (Impact: 9.7)
  * `test_ssl_version_with_protocol_tls_or_client_not_deprecated` **(Type Conversions)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 477`, `args: 71`, `func_start: 71`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 124`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 77`, `concurrency: 1`, `import: 31`
* *Defense:* `safety: 131`, `doc: 10`, `test: 132`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.965
  * `Choke Point (Betweenness):` 0.002099 | `Ripple Effect (Closeness):` 0.012048
  * `Imports (Out-Degree: 16):` __future__, concurrent.futures, contextlib, datetime, dummyserver.socketserver, dummyserver.testcase, os.path, pathlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/with_dummyserver/test_proxy_poolmanager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.29)
- **Top Global Matches:** file_cluster_0: 6.29, file_cluster_13: 8.769, file_cluster_15: 9.076
- **Magnitude:** 444.3 | **LOC:** 891 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.4%), Complexity Load (formerly Cognitive Load) (27.5%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 95.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_proxy_https_target_tls_error` **(Defensive Guards)** (Impact: 11.0)
  * `test_https_proxy_hostname_verification` **(Defensive Guards)** (Impact: 10.1)
  * `test_https_proxy_no_san` **(Defensive Guards)** (Impact: 9.1)
  * `test_proxy_pooling` **(Defensive Guards)** (Impact: 8.0)
  * `test_https_proxy_assert_fingerprint_md5_non_matching` **(Generic / Templated Code)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 341`, `args: 48`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 144`, `unreferenced_by_name: 43`
* *Architecture:* `io: 8`, `api: 49`, `import: 27`
* *Defense:* `safety: 143`, `doc: 2`, `test: 76`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` ..TARPIT_HOST, ..requires_network, __future__, binascii, contextlib, dummyserver.socketserver, dummyserver.testcase, hashlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/poolmanager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.048)
- **Top Global Matches:** file_cluster_5: 8.048, file_cluster_12: 10.252, file_cluster_4: 10.909
- **Magnitude:** 420.1 | **LOC:** 652 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **20**; blast radius 6.397; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (43.3%)
- **Documentation Coverage:** 89.6552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlopen` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `_default_key_normalizer` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `_new_pool` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `connection_from_host` **(Many-Argument Workhorses)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 84`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 87`, `dead_code: 1`
* *Architecture:* `api: 15`, `import: 20`
* *Defense:* `safety: 7`, `doc: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.397
  * `Choke Point (Betweenness):` 0.004551 | `Ripple Effect (Closeness):` 0.14498
  * `Imports (Out-Degree: 11):` ._collections, ._request_methods, .connection, .connectionpool, .exceptions, .response, .util.connection, .util.proxy...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/retry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.998)
- **Top Global Matches:** file_cluster_4: 6.998, file_cluster_0: 10.143, file_cluster_16: 10.184
- **Magnitude:** 382.84 | **LOC:** 550 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **14**; blast radius 49.841; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%), Connectivity (formerly Api Exposure) (51.4%)
- **Documentation Coverage:** 60.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `increment` **(Many-Argument Workhorses)** (Impact: 81.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 28.5)
  * `is_retry` **(Many-Argument Workhorses)** (Impact: 16.7)
  * `from_int` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `parse_retry_after` **(Compute Cores)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 69`, `args: 17`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 63`
* *Architecture:* `api: 14`, `import: 14`
* *Defense:* `safety: 4`, `doc: 11`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 49.841
  * `Choke Point (Betweenness):` 0.005985 | `Ripple Effect (Closeness):` 0.384768
  * `Imports (Out-Degree: 4):` ..connectionpool, ..exceptions, ..response, .util, __future__, email, itertools, logging...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/_collections.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.125)
- **Top Global Matches:** file_cluster_5: 7.125, file_cluster_0: 8.823, file_cluster_12: 9.401
- **Magnitude:** 372.22 | **LOC:** 488 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **6**; blast radius 25.004; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.6%), Connectivity (formerly Api Exposure) (56.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 84.127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extend` **(Defensive Guards)** (Impact: 29.6)
    * *Intent:* """Generic import function for any type of header-like object. Adapted version of MutableMapping.upd...
  * `add` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* """Adds a (name, value) pair, doesn't overwrite the value if it already exists. If this is called wi...
  * `ensure_can_construct_http_header_dict` **(Defensive Guards)** (Impact: 10.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 10.5)
  * `__setitem__` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 110`, `args: 42`, `func_start: 42`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 63`
* *Architecture:* `api: 26`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 28`, `doc: 9`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.004
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.334562
  * `Imports (Out-Degree: 0):` __future__, collections, enum, threading, typing, typing_extensions
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/ssl_.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.956)
- **Top Global Matches:** file_cluster_4: 6.956, file_cluster_6: 11.222, file_cluster_12: 11.708
- **Magnitude:** 358.6 | **LOC:** 528 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **13**; blast radius 33.088; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.4%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 48.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_urllib3_context` **(Many-Argument Workhorses)** (Impact: 78.2)
  * `ssl_wrap_socket` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `assert_fingerprint` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* """ Checks if given fingerprint matches the supplied certificate. :param cert: Certificate as bytes ...
  * `_is_bpo_43522_fixed` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `_ssl_wrap_socket_impl` **(Stateful Encapsulated Methods)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`
* *Architecture:* `io: 16`, `api: 8`, `import: 17`
* *Defense:* `safety: 12`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.088
  * `Choke Point (Betweenness):` 0.008433 | `Ripple Effect (Closeness):` 0.325114
  * `Imports (Out-Degree: 3):` ..exceptions, .ssltransport, .url, __future__, binascii, hashlib, hmac, os...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/test_util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.183)
- **Top Global Matches:** file_cluster_0: 6.183, file_cluster_13: 8.754, file_cluster_15: 9.623
- **Magnitude:** 356.96 | **LOC:** 1127 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 3.965; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.5%), Complexity Load (formerly Cognitive Load) (7.9%)
- **Documentation Coverage:** 95.9732% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_url_vulnerabilities` **(Defensive Guards)** (Impact: 6.4)
  * `test_create_connection_with_invalid_idna_labels` **(Generic / Templated Code)** (Impact: 5.5)
  * `test_scheme_host_port` **(Defensive Guards)** (Impact: 4.5)
  * `test_invalid_timeouts` **(Generic / Templated Code)** (Impact: 4.2)
  * `test_is_has_never_check_common_name_reliable` **(Many-Argument Workhorses)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 262`, `args: 74`, `func_start: 74`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 84`
* *Architecture:* `io: 43`, `api: 80`, `import: 28`
* *Defense:* `safety: 62`, `doc: 7`, `test: 159`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.965
  * `Choke Point (Betweenness):` 0.001753 | `Ripple Effect (Closeness):` 0.012048
  * `Imports (Out-Degree: 14):` .clear_warnings, __future__, http, io, itertools, logging, pytest, socket...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/url.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.494)
- **Top Global Matches:** file_cluster_4: 8.494, file_cluster_6: 9.428, file_cluster_16: 14.455
- **Magnitude:** 352.26 | **LOC:** 470 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **6**; blast radius 37.251; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (60.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_url` **(Compute Cores)** (Impact: 41.9)
    * *Intent:* """ Given a url, return a parsed :class:`.Url` namedtuple. Best-effort is performed to parse incompl...
  * `_normalize_host` **(Stateful Encapsulated Methods)** (Impact: 29.1)
  * `_encode_invalid_chars` **(Stateful Encapsulated Methods)** (Impact: 17.3)
  * `_remove_path_dot_segments` **(Stateful Encapsulated Methods)** (Impact: 14.1)
    * *Intent:* # See http://tools.ietf.org/html/rfc3986#section-5.2.4 for pseudo-code segments = path.split("/") # ...
  * `url` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* """ Convert self into a url This function should more or less round-trip with :func:`.parse_url`. Th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 55`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `safety: 5`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.251
  * `Choke Point (Betweenness):` 0.005478 | `Ripple Effect (Closeness):` 0.367893
  * `Imports (Out-Degree: 2):` ..exceptions, .util, __future__, idna, re, typing
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/http2/connection.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.366)
- **Top Global Matches:** file_cluster_5: 6.366, file_cluster_12: 8.828, file_cluster_7: 10.267
- **Magnitude:** 306.84 | **LOC:** 357 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 8.638; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.3%), Guard Balance (formerly Safety Score) (70.8%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `send` **(Defensive Guards)** (Impact: 28.2)
    * *Intent:* """Send data to the server. `data` can be: `str`, `bytes`, an iterable, or file-like objects that su...
  * `putrequest` **(Stateful Encapsulated Methods)** (Impact: 19.4)
  * `getresponse` **(Defensive Guards)** (Impact: 17.6)
  * `putheader` **(Defensive Guards)** (Impact: 16.6)
    * *Intent:* # TODO SKIPPABLE_HEADERS from urllib3 are ignored. header = header.encode() if isinstance(header, st...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 73`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 48`, `planned_debt: 5`
* *Architecture:* `api: 16`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 13`, `doc: 6`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.638
  * `Choke Point (Betweenness):` 0.000392 | `Ripple Effect (Closeness):` 0.260495
  * `Imports (Out-Degree: 5):` .._base_connection, .._collections, ..connection, ..exceptions, ..response, __future__, h2.config, h2.connection...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/test_collections.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.076)
- **Top Global Matches:** file_cluster_0: 8.076, file_cluster_5: 9.169, file_cluster_12: 9.914
- **Magnitude:** 305.26 | **LOC:** 473 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.4%), Guard Balance (formerly Safety Score) (28.9%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 98.0583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_union_with_unsupported_type` **(Generic / Templated Code)** (Impact: 5.4)
  * `test_maxsize` **(Defensive Guards)** (Impact: 5.0)
  * `test_expire` **(Type Conversions)** (Impact: 4.9)
  * `test_access_ordering` **(Type Conversions)** (Impact: 4.9)
  * `test_extend_with_wrong_number_of_args_is_typeerror` **(Generic / Templated Code)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 211`, `args: 53`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 79`, `unreferenced_by_name: 50`
* *Architecture:* `api: 53`, `import: 5`
* *Defense:* `safety: 117`, `doc: 1`, `test: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pytest, typing, urllib3._collections
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/test/test_ssltransport.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.794)
- **Top Global Matches:** file_cluster_0: 6.794, file_cluster_13: 9.617, file_cluster_12: 9.785
- **Magnitude:** 288.8 | **LOC:** 574 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (27.4%), Complexity Load (formerly Cognitive Load) (22.4%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_read_write_loop` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `start_dummy_server` **(Generic / Templated Code)** (Impact: 9.2)
  * `test_ssl_object_attributes` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* """Ensures common ssl attributes are exposed"""
  * `sample_request` **(Generic / Templated Code)** (Impact: 4.6)
  * `sample_response` **(Generic / Templated Code)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 153`, `args: 40`, `func_start: 40`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 81`, `duplicate_logic: 2`, `unreferenced_by_name: 18`
* *Architecture:* `io: 31`, `api: 42`, `concurrency: 2`, `import: 13`
* *Defense:* `safety: 29`, `doc: 16`, `test: 47`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, dummyserver.socketserver, dummyserver.testcase, platform, pytest, select, socket, ssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/dummyserver/testcase.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.61)
- **Top Global Matches:** file_cluster_5: 6.61, file_cluster_12: 8.434, file_cluster_0: 9.666
- **Magnitude:** 286.78 | **LOC:** 354 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **14**; blast radius 7.612; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (83.1%), Connectivity (formerly Api Exposure) (72.9%)
- **Documentation Coverage:** 86.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start_response_handler` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `assert_header_received` **(Defensive Guards)** (Impact: 14.3)
  * `socket_handler` **(Defensive Guards)** (Impact: 12.6)
  * `consume_socket` **(Defensive Guards)** (Impact: 10.9)
  * `consume_request` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* """ Consume a socket until after the HTTP request is sent. """
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 74`, `args: 19`, `func_start: 19`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 50`, `duplicate_logic: 2`
* *Architecture:* `io: 15`, `api: 24`, `concurrency: 13`, `import: 14`
* *Defense:* `safety: 8`, `doc: 4`, `test: 4`, `sync_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.612
  * `Choke Point (Betweenness):` 0.009601 | `Ripple Effect (Closeness):` 0.133457
  * `Imports (Out-Degree: 7):` __future__, contextlib, dummyserver.app, dummyserver.asgi_proxy, dummyserver.hypercornserver, dummyserver.socketserver, pytest, socket...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/with_dummyserver/test_poolmanager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.114)
- **Top Global Matches:** file_cluster_0: 7.114, file_cluster_12: 8.65, file_cluster_5: 9.278
- **Magnitude:** 278.86 | **LOC:** 811 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.1%), Complexity Load (formerly Cognitive Load) (14.7%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 97.5904% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_top_level_request_with_body_and_json` **(Generic / Templated Code)** (Impact: 8.7)
  * `test_request_with_json` **(Defensive Guards)** (Impact: 5.9)
  * `test_redirect_cross_host_set_removed_headers` **(Defensive Guards)** (Impact: 4.2)
  * `test_too_many_redirects` **(Defensive Guards)** (Impact: 3.8)
  * `test_top_level_request_with_invalid_body` **(Generic / Templated Code)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 257`, `args: 42`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 103`, `unreferenced_by_name: 40`
* *Architecture:* `api: 44`, `import: 13`
* *Defense:* `safety: 114`, `doc: 3`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` __future__, dummyserver.socketserver, dummyserver.testcase, gzip, pytest, test, typing, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/test/test_poolmanager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.923)
- **Top Global Matches:** file_cluster_0: 6.923, file_cluster_12: 8.555, file_cluster_5: 8.923
- **Magnitude:** 276.76 | **LOC:** 499 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.5%), Complexity Load (formerly Cognitive Load) (20.0%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 35.4839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_https_pool_key_fields` **(Defensive Guards)** (Impact: 11.7)
    * *Intent:* """Assert the HTTPSPoolKey fields are honored when selecting a pool."""
  * `test_http_pool_key_fields` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* """Assert the HTTPPoolKey fields are honored when selecting a pool."""
  * `test_pools_keyed_with_from_host` **(Defensive Guards)** (Impact: 8.2)
    * *Intent:* """Assert pools are still keyed correctly with connection_from_host."""
  * `test_deprecated_no_scheme` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* # Don't actually make a network connection, just verify the DeprecationWarning connection_from_host....
  * `test_many_urls` **(Defensive Guards)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 138`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 107`, `unreferenced_by_name: 31`
* *Architecture:* `io: 5`, `api: 32`, `import: 13`
* *Defense:* `safety: 84`, `doc: 22`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` __future__, gc, pytest, socket, test, unittest, unittest.mock, urllib3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/test/test_retry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.673)
- **Top Global Matches:** file_cluster_0: 6.673, file_cluster_13: 9.439, file_cluster_15: 9.442
- **Magnitude:** 260.68 | **LOC:** 441 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.4%), Complexity Load (formerly Cognitive Load) (26.6%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 58.6207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_respect_retry_after_header_sleep` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `test_error_message` **(Defensive Guards)** (Impact: 8.5)
  * `test_backoff` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* """Backoff is computed correctly"""
  * `test_string` **(Type Conversions)** (Impact: 3.5)
    * *Intent:* """Retry string representation looks the way we expect"""
  * `test_status_counter` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 144`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 118`, `unreferenced_by_name: 29`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 76`, `doc: 12`, `test: 55`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, datetime, pytest, test, unittest, urllib3.exceptions, urllib3.response, urllib3.util.retry
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/util/ssltransport.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.112)
- **Top Global Matches:** file_cluster_5: 7.112, file_cluster_0: 8.702, file_cluster_12: 9.451
- **Magnitude:** 257.06 | **LOC:** 272 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 17.015; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%), Guard Balance (formerly Safety Score) (69.0%)
- **Documentation Coverage:** 96.2264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makefile` **(Many-Argument Workhorses)** (Impact: 42.2)
  * `_ssl_io_loop` **(Stateful Encapsulated Methods)** (Impact: 26.4)
  * `_wrap_ssl_read` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `recv_into` **(Generic / Templated Code)** (Impact: 7.3)
  * `sendall` **(Type Conversions)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 68`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`, `planned_debt: 1`
* *Architecture:* `io: 16`, `api: 25`, `import: 8`
* *Defense:* `safety: 7`, `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.015
  * `Choke Point (Betweenness):` 0.000492 | `Ripple Effect (Closeness):` 0.29535
  * `Imports (Out-Degree: 2):` ..exceptions, .ssl_, __future__, io, socket, ssl, typing, typing_extensions
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/test/with_dummyserver/test_chunked_transfer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.992)
- **Top Global Matches:** file_cluster_0: 5.992, file_cluster_15: 9.399, file_cluster_12: 9.407
- **Magnitude:** 233.74 | **LOC:** 334 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.3%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_test_body` **(Stateful Encapsulated Methods)** (Impact: 15.7)
  * `test_chunks` **(Defensive Guards)** (Impact: 11.1)
  * `test_preserve_chunked_on_redirect` **(Defensive Guards)** (Impact: 10.1)
  * `test_preserve_chunked_on_broken_connection` **(Defensive Guards)** (Impact: 10.0)
  * `socket_handler` **(Compute Cores)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 93`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `unreferenced_by_name: 20`
* *Architecture:* `io: 11`, `api: 28`, `import: 9`
* *Defense:* `safety: 24`, `test: 26`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, dummyserver.testcase, io, pytest, socket, typing, urllib3, urllib3.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/test/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.882)
- **Top Global Matches:** file_cluster_5: 5.882, file_cluster_12: 10.179, file_cluster_7: 10.752
- **Magnitude:** 229.44 | **LOC:** 332 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **24**; blast radius 11.466; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.0%), Connectivity (formerly Api Exposure) (63.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (21.2%)
- **Documentation Coverage:** 85.4839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `requires_network` **(Stateful Encapsulated Methods)** (Impact: 7.3)
    * *Intent:* """Helps you skip tests that require the network"""
  * `stash` **(Type Conversions)** (Impact: 6.0)
  * `wrapper` **(Generic / Templated Code)** (Impact: 5.5)
  * `find_spec` **(Generic / Templated Code)** (Impact: 5.0)
  * `_skip_if_no_route` **(Stateful Encapsulated Methods)** (Impact: 4.9)
    * *Intent:* """Skip test exuction if network is unreachable"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 111`, `args: 35`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 38`, `dead_code: 1`
* *Architecture:* `io: 8`, `api: 29`, `import: 23`
* *Defense:* `safety: 14`, `doc: 8`, `test: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.466
  * `Choke Point (Betweenness):` 0.005047 | `Ripple Effect (Closeness):` 0.185357
  * `Imports (Out-Degree: 3):` __future__, backports, brotli, brotlicffi, collections.abc, compression, errno, functools...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `urllib3-2.6.3/test/with_dummyserver/test_socketlevel.py` (PYTHON) | Magnitude: 1701.24 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 2111, structural_boundaries: 636, core_var_decl: 530, design_snake_case: 517
- `urllib3-2.6.3/test/tz_stub.py` (PYTHON) | Magnitude: 17.74 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, import: 8, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `urllib3-2.6.3/src/urllib3/http2/__init__.py` (PYTHON) | Magnitude: 22.62 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 33, indent_spaces: 28, state_mutation: 12, import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `urllib3-2.6.3/src/urllib3/util/__init__.py` (PYTHON) | Magnitude: 17.78 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, import: 9, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `urllib3-2.6.3/src/urllib3/util/request.py` (PYTHON) | Magnitude: 180.84 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 44, branch: 33, state_mutation: 32

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `urllib3-2.6.3/src/urllib3/connection.py` -> **Severity: 5.915** (Bridge: 0.0592 * Flux: 100.0%)
- `urllib3-2.6.3/src/urllib3/connectionpool.py` -> **Severity: 4.871** (Bridge: 0.0487 * Flux: 99.9995%)
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 4.851** (Bridge: 0.0485 * Flux: 99.9593%)
- `urllib3-2.6.3/src/urllib3/response.py` -> **Severity: 2.474** (Bridge: 0.0247 * Flux: 100.0%)
- `urllib3-2.6.3/src/urllib3/__init__.py` -> **Severity: 1.374** (Bridge: 0.0237 * Flux: 57.8946%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 30.082** (Embedded: 0.5115 * Error Risk: 58.816%)
- `urllib3-2.6.3/src/urllib3/util/retry.py` -> **Severity: 28.466** (Embedded: 0.3848 * Error Risk: 73.982%)
- `urllib3-2.6.3/src/urllib3/response.py` -> **Severity: 28.412** (Embedded: 0.4072 * Error Risk: 69.7768%)
- `urllib3-2.6.3/src/urllib3/util/url.py` -> **Severity: 27.23** (Embedded: 0.3679 * Error Risk: 74.0151%)
- `urllib3-2.6.3/src/urllib3/connection.py` -> **Severity: 26.905** (Embedded: 0.392 * Error Risk: 68.643%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 12895.1** (Blast Radius: 128.951 * Doc Risk: 100.0%)
- `urllib3-2.6.3/src/urllib3/response.py` -> **Severity: 5874.402** (Blast Radius: 65.811 * Doc Risk: 89.2617%)
- `urllib3-2.6.3/src/urllib3/connection.py` -> **Severity: 4293.335** (Blast Radius: 55.2 * Doc Risk: 77.7778%)
- `urllib3-2.6.3/src/urllib3/util/util.py` -> **Severity: 4226.6** (Blast Radius: 42.266 * Doc Risk: 100.0%)
- `urllib3-2.6.3/src/urllib3/connectionpool.py` -> **Severity: 3093.45** (Blast Radius: 61.869 * Doc Risk: 50.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6259 call pairs -- scoped 40.2%, unique 0.0%, ambiguous 11.3%, external 48.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 6202 | 40.4% | 0.0% | 11.4% | 48.2% |
| html | 57 | 12.3% | 0.0% | 0.0% | 87.7% |

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
