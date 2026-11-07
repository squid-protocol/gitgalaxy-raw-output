# ARCHITECTURAL_BRIEF: tornado
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tornadoweb/tornado.git` |
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
- **Scope:** 174 analyzed artifact(s), 28271 LOC.
- **Load-bearing artifact:** `tornado/__init__.py` -- 61 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tornado/web.py` -- pulls in 32 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tornado/web.py` at magnitude 2595.32 (structural weight, not risk).
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
| Total Artifacts | 319 |
| Analyzed Artifacts (Scanned) | 174 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 145 |
| Total LOC | 28271 |
| Volatility Index | 0.029 |
| % Scanned of codebase = | 54.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2367 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.253 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0904 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 109 | 27106 | 62.6% |
| HTML | 16 | 240 | 9.2% |
| MARKDOWN | 9 | 0 | 5.2% |
| SHELL | 9 | 107 | 5.2% |
| PLAINTEXT | 7 | 0 | 4.0% |
| YAML | 5 | 238 | 2.9% |
| CSS | 4 | 243 | 2.3% |
| JAVASCRIPT | 3 | 156 | 1.7% |
| RUBY | 3 | 22 | 1.7% |
| XML | 2 | 0 | 1.1% |
| JSON | 2 | 51 | 1.1% |
| DOCKERFILE | 1 | 8 | 0.6% |
| POSTGRESQL | 1 | 19 | 0.6% |
| M4 | 1 | 8 | 0.6% |
| C | 1 | 72 | 0.6% |
| CSV | 1 | 1 | 0.6% |

## 4.1 SOURCE ENCODINGS
All 174 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 34%, Parameter Forwarders Files 20%, Generic / Templated Code Files 16%, Declarative / Non-Code 10%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 158 | 90.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 9.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 145*

**Composition by Extension & Reason:**
- `.rst`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 9x Excluded (Unsupported Extension: '.ini')
- `.cfg`: 4x Excluded (Unsupported Extension: '.cfg')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.mo`: 1x Excluded (Unsupported Extension: '.mo')
- `.po`: 1x Excluded (Unsupported Extension: '.po')
- `.bz2`: 1x Excluded (Explicitly Denied Extension: '.bz2')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.crt`: 1x Excluded (Unsupported Extension: '.crt')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 26.4 | 16.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.0 | 46.1 | 54.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 10.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 77.9 | 15.2 | 9.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 26.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.6 | 80.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 451 | 65 | 7 | `tornado/test/web_test.py` |
| cleanup | 265 | 36 | 4 | `tornado/test/iostream_test.py` |
| guards | 1671 | 86 | 26 | `tornado/web.py` |
| danger | 1351 | 102 | 20 | `tornado/web.py` |
| concurrency | 1444 | 76 | 20 | `tornado/test/iostream_test.py` |
| connectivity | 3204 | 114 | 50 | `tornado/test/httpserver_test.py` |
| io | 776 | 76 | 11 | `tornado/test/web_test.py` |
| crypto | 19 | 16 | 0 | `tornado/test/iostream_test.py` |
| ipc | 45 | 13 | 0 | `tornado/process.py` |
| time | 175 | 35 | 4 | `tornado/web.py` |
| serialization | 3 | 2 | 0 | `demos/websocket/static/chat.js` |
| regex | 56 | 21 | 1 | `tornado/httputil.py` |
| events | 408 | 49 | 5 | `tornado/websocket.py` |
| tests | 1127 | 41 | 22 | `tornado/test/httpclient_test.py` |
| docs | 766 | 76 | 14 | `tornado/web.py` |
| debt | 244 | 59 | 5 | `tornado/test/gen_test.py` |
| mutation | 9869 | 124 | 177 | `tornado/web.py` |
| dead_code | 876 | 59 | 16 | `tornado/test/gen_test.py` |
| credential | 2 | 2 | 0 | `tornado/test/escape_test.py` |
| threat | 15 | 4 | 0 | `tornado/test/template_test.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 50 | 13 | 0 | `tornado/test/template_test.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tornado/test/web_test.py` (Hits: 94)
- `tornado/netutil.py` (Hits: 70)
- `tornado/iostream.py` (Hits: 56)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`tornado/__init__.py`) — 61 inbound connections
2. **log.py** (`tornado/log.py`) — 32 inbound connections
3. **web.py** (`tornado/web.py`) — 31 inbound connections
4. **ioloop.py** (`tornado/ioloop.py`) — 30 inbound connections
5. **testing.py** (`tornado/testing.py`) — 28 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **web.py** (`tornado/web.py`) — 32 outbound dependencies
2. **web_test.py** (`tornado/test/web_test.py`) — 30 outbound dependencies
3. **__init__.pyi** (`tornado/__init__.pyi`) — 29 outbound dependencies
4. **httpserver_test.py** (`tornado/test/httpserver_test.py`) — 29 outbound dependencies
5. **simple_httpclient_test.py** (`tornado/test/simple_httpclient_test.py`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_curl_setup_request` **(Many-Argument Workhorses)** (@ `tornado/curl_httpclient.py`) -> Impact: **167.8** | LOC: 221
- `_parse` **(Many-Argument Workhorses)** (@ `tornado/template.py`) -> Impact: **157.5** | LOC: 199
- `run` **(Compute Cores)** (@ `tornado/simple_httpclient.py`) -> Impact: **92.9** | LOC: 160
- `format_date` **(Many-Argument Workhorses)** (@ `tornado/locale.py`) -> Impact: **89.9** | LOC: 105
- `set_cookie` **(Many-Argument Workhorses)** (@ `tornado/web.py`) -> Impact: **73.6** | LOC: 102
- `bind_sockets` **(Many-Argument Workhorses)** (@ `tornado/netutil.py`) -> Impact: **72.7** | LOC: 132
- `write_headers` **(Stateful Encapsulated Methods)** (@ `tornado/http1connection.py`) -> Impact: **64.7** | LOC: 86
- `_read_message` **(Stateful Encapsulated Methods)** (@ `tornado/http1connection.py`) -> Impact: **63.2** | LOC: 121
- `get` **(Many-Argument Workhorses)** (@ `tornado/web.py`) -> Impact: **60.1** | LOC: 82
  * *Intent:* # Set up our path instance variables. self.path = self.parse_url_path(path) del path # make sure we don't refer to path instead of self.path again abs...
- `linkify` **(Many-Argument Workhorses)** (@ `tornado/escape.py`) -> Impact: **56.6** | LOC: 103

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tornado` | 34 | 15126.76 | 44.91% | 17.71% |
| `tornado/test` | 39 | 9631.04 | 22.6% | 0.0% |
| `tornado/platform` | 4 | 599.82 | 37.07% | 2.63% |
| `demos/blog` | 6 | 427.48 | 14.73% | 2.7% |
| `demos/blog/templates` | 8 | 284.36 | 4.9% | 0.0% |
| `maint/test/redbot` | 2 | 205.7 | 19.42% | 0.0% |
| `demos/file_upload` | 2 | 195.5 | 83.22% | 48.53% |
| `maint/benchmark` | 5 | 179.9 | 43.24% | 28.25% |
| `demos/webspider` | 1 | 120.0 | 84.6% | 64.04% |
| `maint/test/websocket` | 6 | 109.92 | 5.82% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `demos/websocket/chatdemo.py` -> **99.9447%** Exposure
- `tornado/locks.py` -> **99.8327%** Exposure
- `.github/workflows/test.yml` -> **99.6558%** Exposure
- `tornado/queues.py` -> **98.1139%** Exposure
- `demos/file_upload/file_receiver.py` -> **97.0688%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `demos/chat/chatdemo.py` -> **100.0%** Exposure
- `demos/file_upload/file_uploader.py` -> **100.0%** Exposure
- `demos/webspider/webspider.py` -> **100.0%** Exposure
- `maint/benchmark/benchmark.py` -> **100.0%** Exposure
- `maint/scripts/custom_fixers/fix_future_imports.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tornado/test/gen_test.py` -> **75** Orphaned Functions | **16** Duplicates
- `tornado/test/httpserver_test.py` -> **73** Orphaned Functions | **6** Duplicates
- `tornado/test/ioloop_test.py` -> **55** Orphaned Functions | **2** Duplicates
- `tornado/test/iostream_test.py` -> **55** Orphaned Functions | **2** Duplicates
- `tornado/test/websocket_test.py` -> **51** Orphaned Functions | **6** Duplicates

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
- **Unknown Dependencies:** `1085` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tornado/web.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.808)
- **Top Global Matches:** file_cluster_5: 6.808, file_cluster_12: 9.783, file_cluster_7: 11.079
- **Magnitude:** 2595.32 | **LOC:** 3804 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **32**; blast radius 19.555; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 58.0556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_cookie` **(Many-Argument Workhorses)** (Impact: 73.6)
  * `get` **(Many-Argument Workhorses)** (Impact: 60.1)
    * *Intent:* # Set up our path instance variables. self.path = self.parse_url_path(path) del path # make sure we ...
  * `render` **(Many-Argument Workhorses)** (Impact: 41.7)
    * *Intent:* """Renders the template with the given arguments as the response. ``render()`` calls ``finish()``, s...
  * `_execute` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `get_content` **(Many-Argument Workhorses)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 304 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 996
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 534`, `args: 199`, `func_start: 196`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 388`, `planned_debt: 8`
* *Architecture:* `io: 27`, `api: 168`, `concurrency: 9`, `import: 36`
* *Defense:* `safety: 103`, `doc: 118`, `test: 1`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.555
  * `Choke Point (Betweenness):` 0.00801 | `Ripple Effect (Closeness):` 0.196443
  * `Imports (Out-Degree: 7):` base64, binascii, collections.abc, datetime, email.utils, functools, gzip, hashlib...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `tornado/websocket.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.319)
- **Top Global Matches:** file_cluster_5: 6.319, file_cluster_12: 9.607, file_cluster_7: 10.778
- **Magnitude:** 1187.76 | **LOC:** 1721 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **25**; blast radius 3.754; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.0%)
- **Documentation Coverage:** 70.1754% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_receive_frame` **(Stateful Encapsulated Methods)** (Impact: 36.6)
    * *Intent:* # Read the frame header. data = await self._read_bytes(2) header, mask_payloadlen = struct.unpack("B...
  * `_write_frame` **(Stateful Encapsulated Methods)** (Impact: 31.0)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 26.3)
  * `close` **(Stateful Encapsulated Methods)** (Impact: 25.6)
    * *Intent:* """Closes the WebSocket connection."""
  * `_handle_message` **(Stateful Encapsulated Methods)** (Impact: 24.5)
    * *Intent:* """Execute on_message, returning its Future if it is a coroutine."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 118 instances
* *Concurrency (weighted view):* 143
* *State Mutation (weighted view):* 416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 271`, `args: 104`, `func_start: 100`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 180`, `planned_debt: 8`, `duplicate_logic: 8`
* *Architecture:* `io: 6`, `api: 75`, `concurrency: 38`, `import: 26`
* *Defense:* `safety: 44`, `doc: 42`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.754
  * `Choke Point (Betweenness):` 0.000749 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 11):` abc, asyncio, base64, collections.abc, functools, hashlib, logging, os...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tornado/auth.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.367)
- **Top Global Matches:** file_cluster_5: 8.367, file_cluster_7: 11.02, file_cluster_12: 11.389
- **Magnitude:** 922.12 | **LOC:** 1233 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **14**; blast radius 3.826; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (88.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 78.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_on_authentication_verified` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `twitter_request` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `authorize_redirect` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `_oauth_request_token_url` **(Stateful Encapsulated Methods)** (Impact: 16.9)
  * `get_authenticated_user` **(Many-Argument Workhorses)** (Impact: 16.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 131 instances
* *Concurrency (weighted view):* 121
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 113`, `args: 31`, `func_start: 31`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 188`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 23`, `concurrency: 26`, `import: 14`
* *Defense:* `safety: 5`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.826
  * `Choke Point (Betweenness):` 0.000123 | `Ripple Effect (Closeness):` 0.023121
  * `Imports (Out-Degree: 4):` base64, binascii, collections.abc, hashlib, hmac, time, tornado, tornado.httputil...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tornado/iostream.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.757)
- **Top Global Matches:** file_cluster_5: 6.757, file_cluster_12: 8.569, file_cluster_0: 10.582
- **Magnitude:** 901.9 | **LOC:** 1609 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **19**; blast radius 9.12; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.0%), Guard Balance (formerly Safety Score) (66.9%), Complexity Load (formerly Cognitive Load) (37.3%)
- **Documentation Coverage:** 61.2613% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_handle_events` **(Stateful Encapsulated Methods)** (Impact: 32.6)
  * `start_tls` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `close` **(Stateful Encapsulated Methods)** (Impact: 23.1)
  * `_read_to_buffer_loop` **(Stateful Encapsulated Methods)** (Impact: 17.6)
    * *Intent:* # This method is called from _handle_read and _try_inline_read. if self._read_bytes is not None: tar...
  * `_signal_closed` **(Stateful Encapsulated Methods)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 104 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 374
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 235`, `args: 78`, `func_start: 71`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 166`, `planned_debt: 5`
* *Architecture:* `io: 56`, `api: 47`, `concurrency: 3`, `import: 21`
* *Defense:* `safety: 75`, `doc: 40`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.12
  * `Choke Point (Betweenness):` 0.001181 | `Ripple Effect (Closeness):` 0.162324
  * `Imports (Out-Degree: 6):` asyncio, collections, collections.abc, doctest, errno, io, numbers, os...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `tornado/http1connection.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.599)
- **Top Global Matches:** file_cluster_4: 8.599, file_cluster_5: 9.459, file_cluster_12: 9.621
- **Magnitude:** 890.14 | **LOC:** 887 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 5.195; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 58.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_headers` **(Stateful Encapsulated Methods)** (Impact: 64.7)
  * `_read_message` **(Stateful Encapsulated Methods)** (Impact: 63.2)
  * `_read_body` **(Many-Argument Workhorses)** (Impact: 31.7)
  * `_read_chunked_body` **(Stateful Encapsulated Methods)** (Impact: 17.2)
    * *Intent:* # TODO: "chunk extensions" http://tools.ietf.org/html/rfc2616#section-3.6.1 total_size = 0 while Tru...
  * `data_received` **(Compute Cores)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 104 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 340
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 145`, `args: 40`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 132`, `planned_debt: 5`
* *Architecture:* `api: 23`, `concurrency: 32`, `import: 11`
* *Defense:* `safety: 31`, `doc: 23`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.195
  * `Choke Point (Betweenness):` 0.001434 | `Ripple Effect (Closeness):` 0.118701
  * `Imports (Out-Degree: 6):` asyncio, collections.abc, logging, re, tornado, tornado.concurrent, tornado.escape, tornado.log...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tornado/httputil.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.777)
- **Top Global Matches:** file_cluster_5: 6.777, file_cluster_12: 9.205, file_cluster_7: 10.919
- **Magnitude:** 863.64 | **LOC:** 1373 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **21**; blast radius 8.665; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%)
- **Documentation Coverage:** 54.4554% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_body_arguments` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `parse_multipart_form_data` **(Many-Argument Workhorses)** (Impact: 42.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `parse_line` **(Many-Argument Workhorses)** (Impact: 22.5)
  * `add` **(Stateful Encapsulated Methods)** (Impact: 18.8)
    * *Intent:* # new public methods """Adds a new value for the given key."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 173`, `args: 55`, `func_start: 55`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 146`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 54`, `concurrency: 1`, `import: 23`
* *Defense:* `safety: 25`, `doc: 51`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.665
  * `Choke Point (Betweenness):` 0.000272 | `Ripple Effect (Closeness):` 0.115928
  * `Imports (Out-Degree: 2):` __future__, asyncio, calendar, collections.abc, copy, dataclasses, datetime, doctest...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `tornado/test/web_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.923)
- **Top Global Matches:** file_cluster_12: 5.923, file_cluster_15: 7.75, file_cluster_7: 9.317
- **Magnitude:** 853.5 | **LOC:** 3441 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.8%), Guard Balance (formerly Safety Score) (59.3%), Complexity Load (formerly Cognitive Load) (18.8%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_handlers` **(Defensive Guards)** (Impact: 26.0)
  * `get` **(Compute Cores)** (Impact: 23.7)
    * *Intent:* # Type checks: web.py interfaces convert argument values to # unicode strings (by default, but see a...
  * `get` **(Defensive Guards)** (Impact: 22.4)
    * *Intent:* # Control characters and semicolons raise errors in cookie names and attributes # (but not values, w...
  * `test_cookie_tampering_future_timestamp` **(Compute Cores)** (Impact: 11.8)
  * `decode_argument` **(Compute Cores)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 380`, `args: 135`, `func_start: 134`, `class_start: 86`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 266`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 38`
* *Architecture:* `io: 94`, `api: 190`, `import: 32`
* *Defense:* `safety: 20`, `doc: 5`, `test: 60`, `sync_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` binascii, contextlib, copy, datetime, email.utils, gzip, http, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/template.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.419)
- **Top Global Matches:** file_cluster_5: 7.419, file_cluster_12: 9.38, file_cluster_0: 9.881
- **Magnitude:** 811.42 | **LOC:** 1043 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 4.686; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.7%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 90.566% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse` **(Many-Argument Workhorses)** (Impact: 157.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 54.6)
    * *Intent:* # note that the constructor's signature is not extracted with # autodoc because _UNSET looks like ga...
  * `__getitem__` **(Defensive Guards)** (Impact: 12.9)
  * `resolve_path` **(Compute Cores)** (Impact: 12.7)
  * `resolve_path` **(Generic / Templated Code)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 83 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 188`, `args: 71`, `func_start: 69`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 1`, `state_mutation: 152`, `fragile_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 9`, `api: 44`, `concurrency: 2`, `import: 13`
* *Defense:* `safety: 19`, `doc: 13`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.686
  * `Choke Point (Betweenness):` 0.00017 | `Ripple Effect (Closeness):` 0.028902
  * `Imports (Out-Degree: 3):` collections.abc, datetime, io, linecache, missing, os.path, posixpath, re...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tornado/test/iostream_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.316)
- **Top Global Matches:** file_cluster_15: 7.316, file_cluster_12: 7.581, file_cluster_13: 8.156
- **Magnitude:** 768.32 | **LOC:** 1420 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.7%), Guard Balance (formerly Safety Score) (53.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.7%), Complexity Load (formerly Cognitive Load) (40.8%)
- **Documentation Coverage:** 96.9072% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_many_mixed_reads` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* # Stress buffer handling when going back and forth between # read_bytes() (using an internal buffer)...
  * `check_append_all_then_skip_all` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `to_bytes` **(Defensive Guards)** (Impact: 7.3)
  * `test_future_write` **(Defensive Guards)** (Impact: 7.1)
    * *Intent:* """ Test that write() Futures are never orphaned. """
  * `test_large_read_until` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* # Performance test: read_until used to have a quadratic component # so a read_until of 4MB would tak...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 250`, `args: 105`, `func_start: 104`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 187`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 55`
* *Architecture:* `io: 51`, `api: 107`, `concurrency: 25`, `import: 26`
* *Defense:* `safety: 74`, `doc: 4`, `test: 58`, `sync_locks: 11`, `cleanup: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` asyncio, errno, hashlib, logging, os, platform, random, socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/test/httpserver_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.638)
- **Top Global Matches:** file_cluster_15: 6.638, file_cluster_12: 7.411, file_cluster_10: 7.792
- **Magnitude:** 760.24 | **LOC:** 1508 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.8%), Guard Balance (formerly Safety Score) (54.8%), Concurrency Surface (formerly Concurrency) (17.0%), Complexity Load (formerly Cognitive Load) (15.0%)
- **Documentation Coverage:** 98.7302% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_invalid_methods` **(Compute Cores)** (Impact: 7.2)
    * *Intent:* # RFC 9110 distinguishes between syntactically invalid methods and those that are # valid but unknow...
  * `test_post_encodings` **(Compute Cores)** (Impact: 6.5)
  * `get_app` **(Type Conversions)** (Impact: 5.5)
  * `get_app` **(Parameter Forwarders)** (Impact: 5.2)
  * `check_type` **(Parameter Forwarders)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 325`, `args: 172`, `func_start: 158`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 147`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 73`
* *Architecture:* `io: 35`, `api: 197`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 10`, `doc: 11`, `test: 76`, `sync_locks: 4`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` contextlib, datetime, gzip, io, logging, os, shutil, socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/test/gen_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.471)
- **Top Global Matches:** file_cluster_12: 7.471, file_cluster_11: 9.608, file_cluster_13: 9.613
- **Magnitude:** 726.7 | **LOC:** 1112 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 83.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.5%), Guard Balance (formerly Safety Score) (54.4%), Complexity Load (formerly Cognitive Load) (42.8%)
- **Documentation Coverage:** 99.2453% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_already_done` **(Compute Cores)** (Impact: 18.1)
  * `test_iterator_async_await` **(Defensive Guards)** (Impact: 13.1)
    * *Intent:* # Recreate the previous test with py35 syntax. It's a little clunky # because of the way the previou...
  * `finish_coroutines` **(Compute Cores)** (Impact: 10.6)
  * `test_iterator` **(Defensive Guards)** (Impact: 9.7)
  * `f` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 117
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 242`, `args: 154`, `func_start: 149`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 112`, `duplicate_logic: 16`, `unreferenced_by_name: 75`
* *Architecture:* `io: 1`, `api: 130`, `concurrency: 37`, `import: 18`
* *Defense:* `safety: 21`, `doc: 1`, `test: 74`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` asyncio, concurrent, contextvars, datetime, gc, platform, sys, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/simple_httpclient.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.871)
- **Top Global Matches:** file_cluster_5: 8.871, file_cluster_12: 8.939, file_cluster_4: 9.17
- **Magnitude:** 588.54 | **LOC:** 697 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **23**; blast radius 4.907; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (88.7%), Complexity Load (formerly Cognitive Load) (87.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 92.9)
  * `_get_ssl_options` **(Stateful Encapsulated Methods)** (Impact: 18.7)
  * `_handle_exception` **(Stateful Encapsulated Methods)** (Impact: 17.4)
  * `finish` **(Defensive Guards)** (Impact: 15.9)
  * `initialize` **(Many-Argument Workhorses)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 77 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 258
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 114`, `args: 31`, `func_start: 29`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 104`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 11`, `concurrency: 9`, `import: 23`
* *Defense:* `safety: 23`, `doc: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.907
  * `Choke Point (Betweenness):` 0.002275 | `Ripple Effect (Closeness):` 0.088133
  * `Imports (Out-Degree: 9):` base64, collections, collections.abc, copy, functools, io, re, socket...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `tornado/test/simple_httpclient_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.263)
- **Top Global Matches:** file_cluster_12: 6.263, file_cluster_15: 6.983, file_cluster_10: 8.086
- **Magnitude:** 553.06 | **LOC:** 886 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (87.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.8%), Guard Balance (formerly Safety Score) (56.7%), Complexity Load (formerly Cognitive Load) (30.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `respond_204` **(Compute Cores)** (Impact: 8.1)
  * `test_connection_refused` **(Type Conversions)** (Impact: 6.6)
  * `test_connection_limit` **(Callbacks & Closures)** (Impact: 5.7)
  * `test_streaming_follow_redirects` **(Generic / Templated Code)** (Impact: 5.2)
    * *Intent:* # When following redirects, header and streaming callbacks # should only be called for the final res...
  * `test_streaming_callback_coroutine` **(Stateful Encapsulated Methods)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 270`, `args: 116`, `func_start: 108`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 78`, `planned_debt: 1`, `duplicate_logic: 10`, `unreferenced_by_name: 45`
* *Architecture:* `io: 8`, `api: 139`, `concurrency: 20`, `import: 29`
* *Defense:* `safety: 3`, `test: 46`, `sync_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` asyncio, collections, contextlib, errno, logging, os, re, socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/test/httpclient_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.342)
- **Top Global Matches:** file_cluster_12: 6.342, file_cluster_15: 7.269, file_cluster_11: 8.711
- **Magnitude:** 535.62 | **LOC:** 951 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 2.652; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (77.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.5%), Guard Balance (formerly Safety Score) (56.8%), Concurrency Surface (formerly Concurrency) (33.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_method_after_redirect` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* # Legacy redirect codes (301, 302) convert POST requests to GET. for status in [301, 302, 303]: url ...
  * `test_header_callback` **(Compute Cores)** (Impact: 7.2)
  * `test_body_sanity_checks` **(Type Conversions)** (Impact: 7.2)
    * *Intent:* # These methods require a body. for method in ("POST", "PUT", "PATCH"): with self.assertRaises(Value...
  * `test_bind_source_ip` **(Type Conversions)** (Impact: 6.3)
  * `header_callback` **(Compute Cores)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 195`, `args: 91`, `func_start: 90`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 117`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 113`, `concurrency: 3`, `import: 24`
* *Defense:* `safety: 13`, `doc: 2`, `test: 78`, `sync_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.652
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00578
  * `Imports (Out-Degree: 12):` base64, binascii, contextlib, copy, datetime, gzip, io, subprocess...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tornado/test/websocket_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.301)
- **Top Global Matches:** file_cluster_12: 6.301, file_cluster_15: 6.558, file_cluster_13: 7.655
- **Magnitude:** 534.36 | **LOC:** 990 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.3%), Complexity Load (formerly Cognitive Load) (17.8%), Concurrency Surface (formerly Concurrency) (17.1%)
- **Documentation Coverage:** 99.0566% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_inner` **(Stateful Encapsulated Methods)** (Impact: 5.6)
  * `select_subprotocol` **(Compute Cores)** (Impact: 5.5)
  * `test_check_origin_invalid_subdomains` **(Compute Cores)** (Impact: 5.3)
  * `install_hook` **(Stateful Encapsulated Methods)** (Impact: 5.2)
    * *Intent:* """Optionally suppress the client's "pong" response."""
  * `wrapper` **(Encapsulated Accessors)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 247`, `args: 107`, `func_start: 106`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 112`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 51`
* *Architecture:* `io: 11`, `api: 146`, `concurrency: 7`, `import: 24`
* *Defense:* `safety: 12`, `doc: 3`, `test: 50`, `sync_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` asyncio, contextlib, datetime, functools, socket, tornado, tornado.concurrent, tornado.httpclient...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/test/ioloop_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.186)
- **Top Global Matches:** file_cluster_12: 7.186, file_cluster_10: 8.832, file_cluster_15: 9.011
- **Magnitude:** 523.46 | **LOC:** 808 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.8%), Guard Balance (formerly Safety Score) (54.3%), Complexity Load (formerly Cognitive Load) (40.2%)
- **Documentation Coverage:** 92.5134% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_remove_handler_from_handler` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* # Create two sockets with simultaneous read events. client, server = socket.socketpair() try: client...
  * `handle_read` **(Compute Cores)** (Impact: 5.5)
  * `test_init_close_race` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* # Regression test for #2367 # # Skipped on windows because of what looks like a bug in the # proacto...
  * `simulate_calls` **(Many-Argument Workhorses)** (Impact: 4.8)
    * *Intent:* """Simulate a series of calls to the PeriodicCallback. Pass a list of call durations in seconds (neg...
  * `test_add_callback_while_closing` **(Callbacks & Closures)** (Impact: 3.7)
    * *Intent:* # add_callback should not fail if it races with another thread # closing the IOLoop. The callbacks a...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 188`, `args: 118`, `func_start: 98`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 87`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 55`
* *Architecture:* `io: 9`, `api: 99`, `concurrency: 30`, `import: 22`
* *Defense:* `safety: 12`, `doc: 7`, `test: 67`, `sync_locks: 7`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` asyncio, collections.abc, concurrent, concurrent.futures, contextlib, datetime, functools, socket...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/locale.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.987)
- **Top Global Matches:** file_cluster_4: 8.987, file_cluster_6: 11.42, file_cluster_5: 12.073
- **Magnitude:** 494.58 | **LOC:** 589 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 3.309; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.1%)
- **Documentation Coverage:** 51.3514% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format_date` **(Many-Argument Workhorses)** (Impact: 89.9)
  * `load_translations` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* """Loads translations from CSV files in a directory. Translations are strings with optional Python-s...
  * `pgettext` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `get_closest` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* """Returns the closest match for the given locale code."""
  * `translate` **(Many-Argument Workhorses)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 89`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 88`
* *Architecture:* `io: 9`, `api: 20`, `import: 13`
* *Defense:* `safety: 6`, `doc: 17`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.309
  * `Choke Point (Betweenness):` 0.000153 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 3):` __future__, codecs, collections.abc, csv, datetime, gettext, glob, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tornado/platform/asyncio.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.581)
- **Top Global Matches:** file_cluster_5: 6.581, file_cluster_12: 10.318, file_cluster_7: 10.559
- **Magnitude:** 481.98 | **LOC:** 749 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **16**; blast radius 10.229; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.7%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 95.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_handler` **(Compute Cores)** (Impact: 18.9)
  * `_run_select` **(Stateful Encapsulated Methods)** (Impact: 16.0)
  * `initialize` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `__getattr__` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* # The event loop policy system is deprecated in Python 3.14; simply accessing # the name asyncio.Def...
  * `add_handler` **(Generic / Templated Code)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 123
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 126`, `args: 49`, `func_start: 48`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 52`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 40`, `concurrency: 33`, `import: 17`
* *Defense:* `safety: 37`, `doc: 8`, `sync_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.229
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.180875
  * `Imports (Out-Degree: 2):` asyncio, atexit, collections.abc, concurrent.futures, contextvars, errno, functools, select...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tornado/options.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.748)
- **Top Global Matches:** file_cluster_5: 6.748, file_cluster_7: 10.338, file_cluster_12: 10.377
- **Magnitude:** 456.72 | **LOC:** 734 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **11**; blast radius 34.641; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.5%)
- **Documentation Coverage:** 68.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `define` **(Many-Argument Workhorses)** (Impact: 48.8)
  * `parse_config_file` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* """Parses and loads the config file at the given path. The config file contains Python code that wil...
  * `print_help` **(Compute Cores)** (Impact: 24.0)
    * *Intent:* """Prints all the command line options to stderr (or another file)."""
  * `parse_command_line` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `set` **(Stateful Encapsulated Methods)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 120`, `args: 38`, `func_start: 37`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 1`, `state_mutation: 68`
* *Architecture:* `io: 6`, `api: 26`, `import: 11`
* *Defense:* `safety: 12`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.641
  * `Choke Point (Betweenness):` 0.001484 | `Ripple Effect (Closeness):` 0.257796
  * `Imports (Out-Degree: 3):` collections.abc, datetime, numbers, os, re, sys, textwrap, tornado.escape...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `tornado/httpclient.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.74)
- **Top Global Matches:** file_cluster_5: 5.74, file_cluster_12: 8.774, file_cluster_0: 10.109
- **Magnitude:** 455.3 | **LOC:** 789 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 71.4%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **15**; blast radius 8.909; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.6%), Complexity Load (formerly Cognitive Load) (49.0%)
- **Documentation Coverage:** 89.6552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 33.3)
  * `fetch` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `__new__` **(Compute Cores)** (Impact: 12.8)
  * `close` **(Stateful Encapsulated Methods)** (Impact: 8.3)
    * *Intent:* """Destroys this HTTP client, freeing any file descriptors used. This method is **not needed in norm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 90`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 93`, `planned_debt: 1`
* *Architecture:* `api: 26`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 6`, `doc: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.909
  * `Choke Point (Betweenness):` 0.003456 | `Ripple Effect (Closeness):` 0.131427
  * `Imports (Out-Degree: 7):` collections.abc, datetime, functools, io, ssl, time, tornado, tornado.concurrent...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `tornado/curl_httpclient.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.878)
- **Top Global Matches:** file_cluster_4: 8.878, file_cluster_5: 8.979, file_cluster_12: 9.291
- **Magnitude:** 446.0 | **LOC:** 594 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 3.309; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.6%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_curl_setup_request` **(Many-Argument Workhorses)** (Impact: 167.8)
  * `_handle_socket` **(Stateful Encapsulated Methods)** (Impact: 13.6)
    * *Intent:* """Called by libcurl when it wants to change the file descriptors it cares about. """
  * `_handle_events` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* """Called by IOLoop when there is activity on one of our file descriptors. """
  * `_curl_debug` **(Stateful Encapsulated Methods)** (Impact: 10.6)
  * `_process_queue` **(Stateful Encapsulated Methods)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 65`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 55`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 9`, `concurrency: 3`, `import: 15`
* *Defense:* `safety: 20`, `doc: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.309
  * `Choke Point (Betweenness):` 0.000185 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 6):` collections, collections.abc, functools, inspect, io, logging, pycurl, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tornado/gen.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.131)
- **Top Global Matches:** file_cluster_5: 7.131, file_cluster_7: 10.825, file_cluster_12: 11.174
- **Magnitude:** 430.1 | **LOC:** 888 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **16**; blast radius 14.669; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.0%), Connectivity (formerly Api Exposure) (53.4%)
- **Documentation Coverage:** 75.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multi_future` **(Defensive Guards)** (Impact: 34.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 18.9)
  * `run` **(Defensive Guards)** (Impact: 17.0)
    * *Intent:* """Starts or resumes the generator, running until it reaches a yield point that is not ready. """
  * `with_timeout` **(Many-Argument Workhorses)** (Impact: 13.9)
  * `callback` **(Defensive Guards)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 133`, `args: 40`, `func_start: 35`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 76`
* *Architecture:* `io: 5`, `api: 35`, `concurrency: 3`, `import: 18`
* *Defense:* `safety: 29`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.669
  * `Choke Point (Betweenness):` 0.000374 | `Ripple Effect (Closeness):` 0.166596
  * `Imports (Out-Degree: 4):` asyncio, builtins, collections, collections.abc, concurrent.futures, contextvars, datetime, functools...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `tornado/test/locks_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.165)
- **Top Global Matches:** file_cluster_12: 7.165, file_cluster_7: 8.785, file_cluster_5: 9.25
- **Magnitude:** 429.12 | **LOC:** 535 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.519; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.8%), Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (47.3%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `record_done` **(Parameter Forwarders)** (Impact: 6.5)
    * *Intent:* """Record the resolution of a Future returned by Condition.wait."""
  * `test_garbage_collection` **(I/O & Config Routines)** (Impact: 5.4)
    * *Intent:* # Test that timed-out waiters are occasionally cleaned from the queue. sem = locks.Semaphore(value=0...
  * `test_context_manager_contended` **(Annotated & Test Methods)** (Impact: 5.1)
  * `test_acquire_fifo` **(Annotated & Test Methods)** (Impact: 5.0)
  * `test_nested_notify` **(Callbacks & Closures)** (Impact: 4.9)
    * *Intent:* # Ensure no notifications lost, even if notify() is reentered by a # waiter calling notify(). c = lo...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 149
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 93`, `args: 49`, `func_start: 48`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 74`, `unreferenced_by_name: 29`
* *Architecture:* `api: 50`, `concurrency: 34`, `import: 6`
* *Defense:* `doc: 2`, `test: 42`, `sync_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.519
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` asyncio, datetime, tornado, tornado.gen, tornado.testing, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/testing.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.611)
- **Top Global Matches:** file_cluster_5: 5.611, file_cluster_12: 9.375, file_cluster_7: 10.324
- **Magnitude:** 415.6 | **LOC:** 864 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **24**; blast radius 19.342; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (80.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.0%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 71.6049% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__exit__` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `wait` **(Stateful Encapsulated Methods)** (Impact: 20.7)
  * `main` **(Compute Cores)** (Impact: 20.1)
    * *Intent:* """A simple test runner. This test runner is essentially equivalent to `unittest.main` from the stan...
  * `filter` **(Compute Cores)** (Impact: 14.9)
  * `wrap` **(Stateful Encapsulated Methods)** (Impact: 13.8)
    * *Intent:* # Stack up several decorators to allow us to access the generator # object itself. In the innermost ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 133`, `args: 42`, `func_start: 40`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 60`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 11`, `api: 39`, `concurrency: 7`, `import: 25`
* *Defense:* `safety: 14`, `doc: 21`, `test: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.342
  * `Choke Point (Betweenness):` 0.009982 | `Ripple Effect (Closeness):` 0.16338
  * `Imports (Out-Degree: 10):` asyncio, collections.abc, functools, inspect, logging, os, re, signal...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `tornado/ioloop.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.202)
- **Top Global Matches:** file_cluster_5: 7.202, file_cluster_7: 11.271, file_cluster_12: 11.415
- **Magnitude:** 415.02 | **LOC:** 979 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **22**; blast radius 43.708; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 55.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_sync` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* """Starts the `IOLoop`, runs the given function, and stops the loop. The function must return either...
  * `add_timeout` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 9.7)
  * `configure` **(Defensive Guards)** (Impact: 8.4)
  * `_update_next` **(Stateful Encapsulated Methods)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 136`, `args: 59`, `func_start: 55`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 40`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 48`, `concurrency: 13`, `import: 25`
* *Defense:* `safety: 28`, `doc: 36`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.708
  * `Choke Point (Betweenness):` 0.007234 | `Ripple Effect (Closeness):` 0.243486
  * `Imports (Out-Degree: 7):` __future__, asyncio, collections.abc, concurrent.futures, datetime, functools, inspect, math...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `demos/websocket/static/chat.js` (JAVASCRIPT) | Magnitude: 27.46 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 13, args: 9, closures: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `maint/benchmark/chunk_benchmark.py` (PYTHON) | Magnitude: 15.72 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 18, core_var_decl: 10, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `demos/file_upload/file_receiver.py` (PYTHON) | Magnitude: 53.02 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 17, api: 8, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tornado/__init__.pyi` (PYTHON) | Magnitude: 15.66 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 3, import: 2, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tornado/curl_httpclient.py` (PYTHON) | Magnitude: 446.0 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 409, branch: 101, core_var_decl: 68, structural_boundaries: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tornado/simple_httpclient.py` (PYTHON) | Magnitude: 588.54 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 517, branch: 126, structural_boundaries: 114, state_mutation: 104

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tornado/autoreload.py` (PYTHON) | Magnitude: 159.66 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 48, core_var_decl: 43, state_mutation: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tornado/log.py` (PYTHON) | Magnitude: 196.9 | Delta: **0.167** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 186, core_var_decl: 60, design_snake_case: 52, branch: 43

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tornado/websocket.py` -> Churn: **78.04%** | Cog Load: 56.8335% | Debt: 76.1743%
- `tornado/curl_httpclient.py` -> Churn: **73.58%** | Cog Load: 74.4171% | Debt: 15.6296%
- `tornado/template.py` -> Churn: **73.58%** | Cog Load: 73.756% | Debt: 79.7146%
- `tornado/httpserver.py` -> Churn: **73.58%** | Cog Load: 71.5533% | Debt: 12.0836%
- `tornado/simple_httpclient.py` -> Churn: **73.58%** | Cog Load: 87.7798% | Debt: 29.8456%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tornado/web.py` -> **Ben Darnell** (83.3% isolated ownership) | Magnitude: 2595.32
- `tornado/http1connection.py` -> **Ben Darnell** (83.3% isolated ownership) | Magnitude: 890.14
- `tornado/template.py` -> **Ben Darnell** (85.7% isolated ownership) | Magnitude: 811.42
- `tornado/test/gen_test.py` -> **Ben Darnell** (83.3% isolated ownership) | Magnitude: 726.7
- `tornado/simple_httpclient.py` -> **Ben Darnell** (85.7% isolated ownership) | Magnitude: 588.54

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tornado/testing.py` -> **Severity: 0.998** (Bridge: 0.01 * Flux: 99.9993%)
- `tornado/web.py` -> **Severity: 0.801** (Bridge: 0.008 * Flux: 100.0%)
- `tornado/ioloop.py` -> **Severity: 0.723** (Bridge: 0.0072 * Flux: 99.9514%)
- `tornado/httpserver.py` -> **Severity: 0.533** (Bridge: 0.0053 * Flux: 99.9999%)
- `tornado/httpclient.py` -> **Severity: 0.346** (Bridge: 0.0035 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tornado/util.py` -> **Severity: 24.437** (Embedded: 0.3021 * Error Risk: 80.898%)
- `tornado/__init__.py` -> **Severity: 21.268** (Embedded: 0.3929 * Error Risk: 54.1334%)
- `tornado/escape.py` -> **Severity: 21.186** (Embedded: 0.2693 * Error Risk: 78.6617%)
- `tornado/log.py` -> **Severity: 21.03** (Embedded: 0.2983 * Error Risk: 70.4977%)
- `tornado/options.py` -> **Severity: 19.868** (Embedded: 0.2578 * Error Risk: 77.0701%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tornado/__init__.py` -> **Severity: 9709.4** (Blast Radius: 97.094 * Doc Risk: 100.0%)
- `tornado/util.py` -> **Severity: 5466.68** (Blast Radius: 98.753 * Doc Risk: 55.3571%)
- `tornado/speedups.pyi` -> **Severity: 4449.6** (Blast Radius: 44.496 * Doc Risk: 100.0%)
- `tornado/log.py` -> **Severity: 4395.172** (Blast Radius: 51.277 * Doc Risk: 85.7143%)
- `tornado/concurrent.py` -> **Severity: 2670.749** (Blast Radius: 29.569 * Doc Risk: 90.3226%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 430 literal sites + 6 sites through wrappers = 436

- `f3` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tornado/test/gen_test.py`
- `tornado_coroutine` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tornado/test/asyncio_test.py`
- `wrapper` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tornado/websocket.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9413 call pairs -- scoped 39.4%, unique 0.0%, ambiguous 14.2%, external 46.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 9319 | 39.8% | 0.0% | 14.3% | 45.9% |
| javascript | 48 | 4.2% | 0.0% | 0.0% | 95.8% |
| ruby | 21 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 20 | 0.0% | 0.0% | 0.0% | 100.0% |
| c | 4 | 0.0% | 0.0% | 0.0% | 100.0% |
| postgresql | 1 | 100.0% | 0.0% | 0.0% | 0.0% |

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
