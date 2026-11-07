# ARCHITECTURAL_BRIEF: aiohttp
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
- **Scope:** 200 analyzed artifact(s), 75561 LOC.
- **Load-bearing artifact:** `aiohttp-3.13.5/aiohttp/__init__.py` -- 94 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `aiohttp-3.13.5/tests/test_client_functional.py` -- pulls in 36 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `aiohttp-3.13.5/tests/test_client_functional.py` at magnitude 10429.76 (structural weight, not risk).
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
| Total Artifacts | 232 |
| Analyzed Artifacts (Scanned) | 200 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 32 |
| Total LOC | 75561 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3218 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2452 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 22.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6917 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 172 | 65221 | 86.0% |
| M4 | 13 | 74 | 6.5% |
| PLAINTEXT | 5 | 1 | 2.5% |
| JSON | 3 | 676 | 1.5% |
| C | 2 | 9332 | 1.0% |
| SHELL | 2 | 5 | 1.0% |
| MAKEFILE | 1 | 147 | 0.5% |
| HTML | 1 | 94 | 0.5% |
| DOCKERFILE | 1 | 11 | 0.5% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 199 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 35%, Large Core Modules (2) 18%, Data / Markup / Trivial 14%, Large Core Modules (3) 7%, Declarative / Non-Code 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 195 | 97.5% |
| Unknown | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 32*

**Composition by Extension & Reason:**
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Machine-Generated Source Code Signature: 53 LOC), 1x Excluded (Machine-Generated Source Code Signature: 315 LOC)
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 31398 LOC), 1x Excluded (Machine-Generated Source Code Signature: 10589 LOC), 1x Excluded (Machine-Generated Source Code Signature: 8687 LOC)
- `no_extension`: 1x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.unknown_mime_type'), 1x Excluded (Unsupported Extension: '.dockerignore')
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.crt`: 1x Excluded (Unsupported Extension: '.crt')
- `.csr`: 1x Excluded (Unsupported Extension: '.csr')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.aiohttp`: 1x Excluded (Unsupported Extension: '.aiohttp')
- `.autobahn`: 1x Excluded (Unsupported Extension: '.autobahn')
- `.zero_bytes`: 1x Excluded (Unsupported Extension: '.zero_bytes')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 37.2 | 42.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.6 | 49.5 | 54.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 4.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.7 | 11.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 62.5 | 100.0 | 100.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.7 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.5 | 95.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 753 | 106 | 11 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| cleanup | 948 | 68 | 9 | `aiohttp-3.13.5/tests/test_connector.py` |
| guards | 9007 | 145 | 126 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| danger | 3452 | 130 | 31 | `aiohttp-3.13.5/aiohttp/_find_header.c` |
| concurrency | 10754 | 129 | 122 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| connectivity | 6088 | 165 | 81 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| io | 2372 | 144 | 30 | `aiohttp-3.13.5/tests/test_connector.py` |
| crypto | 40 | 28 | 1 | `aiohttp-3.13.5/aiohttp/client_reqrep.py` |
| ipc | 21 | 8 | 0 | `aiohttp-3.13.5/tests/test_run_app.py` |
| time | 69 | 15 | 0 | `aiohttp-3.13.5/tests/test_cookiejar.py` |
| serialization | 15 | 5 | 0 | `aiohttp-3.13.5/tests/test_client_exceptions.py` |
| regex | 60 | 19 | 0 | `aiohttp-3.13.5/aiohttp/web_urldispatcher.py` |
| events | 1781 | 63 | 20 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| tests | 7285 | 82 | 105 | `aiohttp-3.13.5/tests/test_connector.py` |
| docs | 1341 | 126 | 19 | `aiohttp-3.13.5/tests/test_cookie_helpers.py` |
| debt | 740 | 83 | 10 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| mutation | 30148 | 171 | 422 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| dead_code | 3033 | 87 | 46 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| credential | 62 | 8 | 0 | `aiohttp-3.13.5/examples/token_refresh_middleware.py` |
| threat | 35 | 8 | 0 | `aiohttp-3.13.5/tests/test_multipart.py` |
| ml_ai | 49 | 1 | 0 | `aiohttp-3.13.5/aiohttp/_find_header.c` |
| ui | 12 | 3 | 0 | `aiohttp-3.13.5/examples/websocket.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5357**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `aiohttp-3.13.5/tests/test_connector.py` (Hits: 341)
- `aiohttp-3.13.5/tests/test_client_functional.py` (Hits: 203)
- `aiohttp-3.13.5/tests/test_multipart.py` (Hits: 132)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`aiohttp-3.13.5/aiohttp/__init__.py`) — 94 inbound connections
2. **client.py** (`aiohttp-3.13.5/aiohttp/client.py`) — 53 inbound connections
3. **helpers.py** (`aiohttp-3.13.5/aiohttp/helpers.py`) — 45 inbound connections
4. **abc.py** (`aiohttp-3.13.5/aiohttp/abc.py`) — 31 inbound connections
5. **multipart.py** (`aiohttp-3.13.5/aiohttp/multipart.py`) — 28 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_client_functional.py** (`aiohttp-3.13.5/tests/test_client_functional.py`) — 36 outbound dependencies
2. **client_reqrep.py** (`aiohttp-3.13.5/aiohttp/client_reqrep.py`) — 33 outbound dependencies
3. **helpers.py** (`aiohttp-3.13.5/aiohttp/helpers.py`) — 33 outbound dependencies
4. **client.py** (`aiohttp-3.13.5/aiohttp/client.py`) — 30 outbound dependencies
5. **test_utils.py** (`aiohttp-3.13.5/aiohttp/test_utils.py`) — 30 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `find_header` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/_find_header.c`) -> Impact: **6511.5** | LOC: 9853
- `_request` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/client.py`) -> Impact: **588.4** | LOC: 456
- `__init__` **(Stateful Encapsulated Methods)** (@ `aiohttp-3.13.5/aiohttp/client.py`) -> Impact: **217.9** | LOC: 159
- `_ws_connect` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/client.py`) -> Impact: **157.8** | LOC: 216
- `feed_data` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/http_parser.py`) -> Impact: **135.4** | LOC: 218
- `__init__` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/client_reqrep.py`) -> Impact: **108.9** | LOC: 78
  * *Intent:* # N.B. # Adding __del__ method with self._writer closing doesn't make sense # because _writer is instance method, thus it keeps a reference to self. #...
- `feed_data` **(Stateful Encapsulated Methods)** (@ `aiohttp-3.13.5/aiohttp/http_parser.py`) -> Impact: **94.6** | LOC: 148
- `__init__` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/web_response.py`) -> Impact: **92.7** | LOC: 64
- `_handle_frame` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py`) -> Impact: **90.3** | LOC: 140
- `_handle_frame` **(Many-Argument Workhorses)** (@ `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py`) -> Impact: **90.3** | LOC: 140

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `aiohttp-3.13.5/tests` | 76 | 73590.96 | 30.88% | 0.0% |
| `aiohttp-3.13.5/aiohttp` | 55 | 30531.6 | 53.91% | 12.2% |
| `aiohttp-3.13.5/examples` | 26 | 7574.66 | 38.88% | 0.0% |
| `aiohttp-3.13.5/aiohttp/_websocket` | 10 | 1597.84 | 34.71% | 6.21% |
| `aiohttp-3.13.5/requirements` | 14 | 183.82 | 0.99% | 0.0% |
| `aiohttp-3.13.5/tests/isolated` | 2 | 157.06 | 45.0% | 0.0% |
| `aiohttp-3.13.5` | 5 | 131.92 | 20.02% | 11.1% |
| `aiohttp-3.13.5/tests/autobahn/client` | 2 | 91.28 | 25.0% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn/server` | 2 | 91.2 | 25.0% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn` | 1 | 78.36 | 21.84% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `aiohttp-3.13.5/aiohttp/payload_streamer.py` -> **99.9447%** Exposure
- `aiohttp-3.13.5/aiohttp/client_exceptions.py` -> **97.4129%** Exposure
- `aiohttp-3.13.5/aiohttp/streams.py` -> **90.5292%** Exposure
- `aiohttp-3.13.5/aiohttp/payload.py` -> **83.5118%** Exposure
- `aiohttp-3.13.5/aiohttp/web_urldispatcher.py` -> **73.4834%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `aiohttp-3.13.5/aiohttp/_http_parser.pyx` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/helpers.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/models.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **240** Orphaned Functions | **121** Duplicates
- `aiohttp-3.13.5/tests/test_connector.py` -> **177** Orphaned Functions | **19** Duplicates
- `aiohttp-3.13.5/tests/test_client_request.py` -> **172** Orphaned Functions | **8** Duplicates
- `aiohttp-3.13.5/tests/test_http_parser.py` -> **167** Orphaned Functions | **0** Duplicates
- `aiohttp-3.13.5/tests/test_web_response.py` -> **145** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `aiohttp-3.13.5/examples/token_refresh_middleware.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/examples/fake_server.py` -> **99.9954%** Exposure
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **5.9472%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1340` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `aiohttp-3.13.5/tests/test_client_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.83)
- **Top Global Matches:** file_cluster_0: 9.83, file_cluster_12: 10.41, file_cluster_5: 10.739
- **Magnitude:** 10429.76 | **LOC:** 5805 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.4%), Complexity Load (formerly Cognitive Load) (43.3%)
- **Documentation Coverage:** 94.7907% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_amazon_like_cookie_scenario` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* """Test real-world cookie scenario similar to Amazon."""
  * `test_ssl_client_shutdown_timeout` **(Many-Argument Workhorses)** (Impact: 12.0)
  * `test_drop_auth_on_redirect_to_other_host` **(Defensive Guards)** (Impact: 11.6)
  * `test_file_upload_307_302_redirect_chain` **(Defensive Guards)** (Impact: 11.6)
  * `test_file_upload_301_302_redirect_non_post` **(Defensive Guards)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1124 instances
* *Amplified Cascading Flux:* 150 instances
* *Concurrency (weighted view):* 7091
* *State Mutation (weighted view):* 1396
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 2558`, `args: 538`, `func_start: 538`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 1096`, `duplicate_logic: 121`, `unreferenced_by_name: 240`
* *Architecture:* `io: 203`, `api: 545`, `concurrency: 1471`, `import: 37`
* *Defense:* `safety: 597`, `doc: 55`, `test: 361`, `sync_locks: 1`, `cleanup: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` aiohttp, aiohttp.abc, aiohttp.client_exceptions, aiohttp.client_reqrep, aiohttp.compression_utils, aiohttp.connector, aiohttp.http_exceptions, aiohttp.http_writer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/_find_header.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 7.916)
- **Top Global Matches:** file_cluster_1: 7.916, file_cluster_3: 48.594, file_cluster_8: 70.34
- **Magnitude:** 6705.94 | **LOC:** 9871 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_header` **(Many-Argument Workhorses)** (Impact: 6511.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3474`, `structural_boundaries: 1739`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _find_header.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_connector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.166)
- **Top Global Matches:** file_cluster_0: 9.166, file_cluster_12: 9.784, file_cluster_15: 10.43
- **Magnitude:** 5773.8 | **LOC:** 4537 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 94.7686% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_connect_reuse_proxy_headers` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `test_tcp_connector_multiple_hosts_errors` **(Defensive Guards)** (Impact: 27.8)
  * `create_connection` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `test_tcp_connector_multiple_hosts_one_timeout` **(Defensive Guards)** (Impact: 15.9)
  * `test_multiple_dns_resolution_requests_first_fails_second_successful` **(Defensive Guards)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 529 instances
* *Amplified Cascading Flux:* 112 instances
* *Concurrency (weighted view):* 3405
* *State Mutation (weighted view):* 1178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 1280`, `args: 262`, `func_start: 252`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 954`, `planned_debt: 1`, `duplicate_logic: 19`, `unreferenced_by_name: 177`
* *Architecture:* `io: 341`, `api: 240`, `concurrency: 760`, `import: 30`
* *Defense:* `safety: 418`, `doc: 40`, `test: 543`, `sync_locks: 4`, `cleanup: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` aiohttp, aiohttp.client, aiohttp.client_proto, aiohttp.client_reqrep, aiohttp.connector, aiohttp.pytest_plugin, aiohttp.resolver, aiohttp.test_utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.808)
- **Top Global Matches:** file_cluster_0: 8.808, file_cluster_12: 9.401, file_cluster_15: 9.947
- **Magnitude:** 5004.3 | **LOC:** 2383 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.1%)
- **Documentation Coverage:** 99.1247% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_subapp_middleware_context` **(Defensive Guards)** (Impact: 8.7)
  * `test_request_tracing` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `resolve` **(Many-Argument Workhorses)** (Impact: 7.5)
  * `test_files_upload_with_same_key` **(Defensive Guards)** (Impact: 7.3)
  * `handler` **(Defensive Guards)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 563 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 3510
* *State Mutation (weighted view):* 692
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 1190`, `args: 229`, `func_start: 229`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 600`, `fragile_debt: 4`, `duplicate_logic: 42`, `unreferenced_by_name: 105`
* *Architecture:* `io: 66`, `api: 229`, `concurrency: 695`, `import: 21`
* *Defense:* `safety: 288`, `doc: 3`, `test: 149`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` aiohttp, aiohttp.compression_utils, aiohttp.hdrs, aiohttp.pytest_plugin, aiohttp.typedefs, aiohttp.web_protocol, asyncio, brotli...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/examples/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_ws_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.477)
- **Top Global Matches:** file_cluster_0: 8.477, file_cluster_15: 9.921, file_cluster_12: 10.455
- **Magnitude:** 3817.28 | **LOC:** 1279 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (53.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.8%)
- **Documentation Coverage:** 97.8495% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_heartbeat_no_pong_after_receive_many_messages` **(Defensive Guards)** (Impact: 7.4)
  * `test_heartbeat_no_pong_after_send_many_messages` **(Defensive Guards)** (Impact: 7.4)
  * `test_closed_async_for` **(Defensive Guards)** (Impact: 5.9)
  * `test_ws_client_async_for` **(Defensive Guards)** (Impact: 5.4)
  * `handler` **(Defensive Guards)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 509 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 3077
* *State Mutation (weighted view):* 383
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 718`, `args: 94`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 295`, `duplicate_logic: 21`, `unreferenced_by_name: 46`
* *Architecture:* `io: 47`, `api: 94`, `concurrency: 532`, `import: 13`
* *Defense:* `safety: 126`, `doc: 8`, `test: 71`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` aiohttp, aiohttp._websocket.reader, aiohttp.client_ws, aiohttp.http, aiohttp.pytest_plugin, async_timeout, asyncio, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_websocket_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.908)
- **Top Global Matches:** file_cluster_12: 8.908, file_cluster_5: 9.102, file_cluster_0: 9.628
- **Magnitude:** 3696.54 | **LOC:** 1397 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 97.8261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_websocket_shutdown` **(Defensive Guards)** (Impact: 7.0)
    * *Intent:* """Test that the client websocket gets the close message when the server is shutting down."""
  * `test_closed_async_for` **(Defensive Guards)** (Impact: 6.9)
  * `test_server_ws_async_for` **(Defensive Guards)** (Impact: 6.7)
  * `test_heartbeat_no_pong_send_many_messages` **(Defensive Guards)** (Impact: 6.5)
  * `test_heartbeat_no_pong_receive_many_messages` **(Defensive Guards)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 483 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 2935
* *State Mutation (weighted view):* 378
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 752`, `args: 92`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 324`, `duplicate_logic: 4`, `unreferenced_by_name: 45`
* *Architecture:* `io: 30`, `api: 92`, `concurrency: 520`, `import: 11`
* *Defense:* `safety: 160`, `doc: 12`, `test: 50`, `sync_locks: 4`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` aiohttp, aiohttp.http, aiohttp.pytest_plugin, asyncio, contextlib, pytest, sys, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_streams.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.637)
- **Top Global Matches:** file_cluster_0: 8.637, file_cluster_11: 10.687, file_cluster_15: 10.906
- **Magnitude:** 2780.48 | **LOC:** 1726 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.5%), Guard Balance (formerly Safety Score) (38.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_unread_data` **(Defensive Guards)** (Impact: 21.5)
  * `get_memory_usage` **(Defensive Guards)** (Impact: 9.6)
  * `test_readchunk_with_unread` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* # Test that stream.unread does not break controlled chunk receiving. stream = self._make_one() # Sen...
  * `test_stream_reader_small_limit_resumes_reading` **(Defensive Guards)** (Impact: 5.8)
  * `test_read_eof_unread_data_no_warning` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* # Read bytes. stream = self._make_one() stream.feed_eof() with mock.patch("aiohttp.streams.internal_...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 304 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 1900
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 610`, `args: 137`, `func_start: 137`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 316`, `duplicate_logic: 2`, `unreferenced_by_name: 96`
* *Architecture:* `io: 4`, `api: 138`, `concurrency: 380`, `import: 11`
* *Defense:* `safety: 247`, `doc: 6`, `test: 187`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` abc, aiohttp, aiohttp.http_exceptions, asyncio, collections, gc, itertools, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_http_writer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.927)
- **Top Global Matches:** file_cluster_0: 7.927, file_cluster_12: 9.559, file_cluster_15: 9.805
- **Magnitude:** 2480.08 | **LOC:** 1654 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.9%), Complexity Load (formerly Cognitive Load) (39.6%)
- **Documentation Coverage:** 97.561% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_write_large_payload_deflate_compression_data_in_eof_writelines_all_zlib` **(Defensive Guards)** (Impact: 15.7)
  * `test_write_large_payload_deflate_compression_data_in_eof_all_zlib` **(Defensive Guards)** (Impact: 11.5)
  * `test_write_large_payload_deflate_compression_data_in_eof` **(Defensive Guards)** (Impact: 11.2)
  * `test_write_large_payload_deflate_compression_chunked_data_in_eof` **(Type Conversions)** (Impact: 11.2)
  * `test_write_large_payload_deflate_compression_chunked_data_in_eof_all_zlib` **(Type Conversions)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 260 instances
* *Amplified Cascading Flux:* 79 instances
* *Concurrency (weighted view):* 1625
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 435`, `args: 82`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 249`, `unreferenced_by_name: 72`
* *Architecture:* `io: 7`, `api: 82`, `concurrency: 325`, `import: 11`
* *Defense:* `safety: 172`, `doc: 24`, `test: 148`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` aiohttp, aiohttp.base_protocol, aiohttp.compression_utils, aiohttp.http_writer, array, asyncio, multidict, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_request.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.227)
- **Top Global Matches:** file_cluster_0: 8.227, file_cluster_12: 10.504, file_cluster_5: 10.814
- **Magnitude:** 2306.1 | **LOC:** 2283 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (36.8%), Guard Balance (formerly Safety Score) (35.7%)
- **Documentation Coverage:** 92.02% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_write_bytes_with_iterable_content_length_limit` **(Defensive Guards)** (Impact: 10.3)
  * `test_warn_stacklevel_points_to_user_code` **(Defensive Guards)** (Impact: 6.0)
  * `test_warn_stacklevel_update_body_from_data` **(Defensive Guards)** (Impact: 5.8)
  * `test_no_warn_for_consumed_payload_via_body_setter` **(Defensive Guards)** (Impact: 5.6)
  * `test_no_warn_for_autoclose_payload_via_body_setter` **(Defensive Guards)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 192 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 1259
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 759`, `args: 202`, `func_start: 202`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 308`, `duplicate_logic: 8`, `unreferenced_by_name: 172`
* *Architecture:* `io: 46`, `api: 200`, `concurrency: 299`, `import: 21`
* *Defense:* `safety: 296`, `doc: 42`, `test: 261`, `immutability_locks: 1`, `cleanup: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` aiohttp, aiohttp.abc, aiohttp.client_exceptions, aiohttp.client_reqrep, aiohttp.compression_utils, aiohttp.http, asyncio, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_multipart.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.648)
- **Top Global Matches:** file_cluster_0: 7.648, file_cluster_15: 9.693, file_cluster_12: 9.814
- **Magnitude:** 2206.8 | **LOC:** 1864 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (48.7%), Guard Balance (formerly Safety Score) (46.0%)
- **Documentation Coverage:** 98.5915% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_read_boundary_across_chunks` **(Defensive Guards)** (Impact: 12.8)
  * `readline` **(Generic / Templated Code)** (Impact: 9.1)
  * `test_async_for_reader` **(I/O & Config Routines)** (Impact: 9.0)
  * `check` **(Defensive Guards)** (Impact: 8.9)
  * `test_read_chunk_by_length_doesnt_breaks_reader` **(Defensive Guards)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 192 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 1204
* *State Mutation (weighted view):* 452
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 721`, `args: 145`, `func_start: 145`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 376`, `fragile_debt: 10`, `duplicate_logic: 2`, `unreferenced_by_name: 113`
* *Architecture:* `io: 132`, `api: 148`, `concurrency: 244`, `import: 17`
* *Defense:* `safety: 210`, `doc: 4`, `test: 176`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` aiohttp, aiohttp.abc, aiohttp.compression_utils, aiohttp.hdrs, aiohttp.helpers, aiohttp.multipart, aiohttp.streams, asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_middleware.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.112)
- **Top Global Matches:** file_cluster_0: 8.112, file_cluster_5: 9.188, file_cluster_12: 9.649
- **Magnitude:** 1892.02 | **LOC:** 1272 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (53.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (26.3%)
- **Documentation Coverage:** 82.0809% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_client_middleware_multi_step_auth` **(Defensive Guards)** (Impact: 26.8)
    * *Intent:* """Test middleware with multi-step authentication flow."""
  * `test_client_middleware_challenge_auth` **(Defensive Guards)** (Impact: 20.3)
    * *Intent:* """Test authentication middleware with challenge/response pattern like digest auth."""
  * `multi_step_auth_middleware` **(Defensive Guards)** (Impact: 19.3)
  * `challenge_auth_middleware` **(Compute Cores)** (Impact: 16.9)
  * `test_client_middleware_conditional_retry` **(Defensive Guards)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 169 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 1080
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 547`, `args: 87`, `func_start: 87`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 215`, `duplicate_logic: 13`, `unreferenced_by_name: 27`
* *Architecture:* `io: 10`, `api: 84`, `concurrency: 235`, `import: 11`
* *Defense:* `safety: 121`, `doc: 41`, `test: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` aiohttp, aiohttp.abc, aiohttp.client_middlewares, aiohttp.client_proto, aiohttp.pytest_plugin, aiohttp.resolver, aiohttp.tracing, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_sendfile_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.258)
- **Top Global Matches:** file_cluster_5: 8.258, file_cluster_12: 9.023, file_cluster_7: 10.156
- **Magnitude:** 1867.16 | **LOC:** 1153 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.1%)
- **Documentation Coverage:** 97.6744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sender` **(Defensive Guards)** (Impact: 9.7)
  * `test_static_file_range` **(Defensive Guards)** (Impact: 8.1)
  * `test_static_file_huge_cancel` **(Defensive Guards)** (Impact: 7.2)
  * `test_static_file_huge` **(Defensive Guards)** (Impact: 7.0)
  * `maker` **(Defensive Guards)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 209 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 1329
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 481`, `args: 64`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 220`, `duplicate_logic: 10`, `unreferenced_by_name: 42`
* *Architecture:* `io: 47`, `api: 64`, `concurrency: 284`, `import: 15`
* *Defense:* `safety: 148`, `doc: 5`, `test: 69`, `cleanup: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` aiohttp, aiohttp.compression_utils, aiohttp.pytest_plugin, asyncio, brotli, brotlicffi, bz2, gzip...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/client.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.898)
- **Top Global Matches:** file_cluster_5: 7.898, file_cluster_12: 10.247, file_cluster_0: 11.091
- **Magnitude:** 1758.2 | **LOC:** 1647 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **53** in-repo importer(s); it depends on **30**; blast radius 22.32; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 64.6018% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_request` **(Many-Argument Workhorses)** (Impact: 588.4)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 217.9)
  * `_ws_connect` **(Many-Argument Workhorses)** (Impact: 157.8)
  * `_prepare_headers` **(Stateful Encapsulated Methods)** (Impact: 11.1)
    * *Intent:* """Add default headers and transform it to CIMultiDict"""
  * `request` **(Many-Argument Workhorses)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 125 instances
* *Concurrency (weighted view):* 145
* *State Mutation (weighted view):* 413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 236`, `args: 63`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 163`
* *Architecture:* `io: 7`, `api: 50`, `concurrency: 50`, `import: 30`
* *Defense:* `safety: 37`, `doc: 33`, `test: 2`, `immutability_locks: 6`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.32
  * `Choke Point (Betweenness):` 0.031722 | `Ripple Effect (Closeness):` 0.336914
  * `Imports (Out-Degree: 15):` ._websocket.reader, .abc, .client_exceptions, .client_middlewares, .client_reqrep, .client_ws, .connector, .cookiejar...
  * `Imported By (In-Degree: 53):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/aiohttp/connector.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.239)
- **Top Global Matches:** file_cluster_5: 8.239, file_cluster_12: 9.768, file_cluster_0: 10.24
- **Magnitude:** 1720.58 | **LOC:** 1855 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **27**; blast radius 9.36; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.0%)
- **Documentation Coverage:** 67.2269% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_start_tls_connection` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 47.2)
  * `_resolve_host` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `_close` **(Stateful Encapsulated Methods)** (Impact: 41.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 36.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 53 instances
* *Amplified Cascading Flux:* 152 instances
* *Concurrency (weighted view):* 384
* *State Mutation (weighted view):* 519
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 322`, `args: 79`, `func_start: 79`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 215`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 29`, `api: 42`, `concurrency: 119`, `import: 30`
* *Defense:* `safety: 67`, `doc: 42`, `test: 1`, `immutability_locks: 6`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.36
  * `Choke Point (Betweenness):` 0.006691 | `Ripple Effect (Closeness):` 0.298717
  * `Imports (Out-Degree: 10):` .abc, .client, .client_exceptions, .client_proto, .client_reqrep, .hdrs, .helpers, .log...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_web_response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.767)
- **Top Global Matches:** file_cluster_0: 7.767, file_cluster_12: 10.603, file_cluster_13: 10.665
- **Magnitude:** 1702.52 | **LOC:** 1608 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.0%), Guard Balance (formerly Safety Score) (35.8%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_request` **(Many-Argument Workhorses)** (Impact: 11.5)
  * `test_payload_body_get_text` **(Generic / Templated Code)** (Impact: 5.5)
  * `test_multiline_reason` **(Generic / Templated Code)** (Impact: 5.3)
  * `_strip_server` **(Encapsulated Accessors)** (Impact: 3.7)
  * `test_last_modified_invalid_type` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 138 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 843
* *State Mutation (weighted view):* 396
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 588`, `args: 163`, `func_start: 163`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 350`, `duplicate_logic: 4`, `unreferenced_by_name: 145`
* *Architecture:* `io: 10`, `api: 163`, `concurrency: 153`, `import: 21`
* *Defense:* `safety: 256`, `doc: 9`, `test: 233`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` aiohttp, aiohttp.abc, aiohttp.helpers, aiohttp.http_writer, aiohttp.multipart, aiohttp.payload, aiohttp.test_utils, aiohttp.web...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/client_reqrep.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.361)
- **Top Global Matches:** file_cluster_4: 9.361, file_cluster_5: 9.598, file_cluster_0: 10.161
- **Magnitude:** 1596.58 | **LOC:** 1537 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **33**; blast radius 21.41; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 72.3404% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 108.9)
    * *Intent:* # N.B. # Adding __del__ method with self._writer closing doesn't make sense # because _writer is ins...
  * `send` **(Many-Argument Workhorses)** (Impact: 51.7)
    * *Intent:* # Specify request target: # - CONNECT request must send authority form URI # - not CONNECT proxy mus...
  * `_merge_ssl_params` **(Many-Argument Workhorses)** (Impact: 40.7)
  * `update_body_from_data` **(Stateful Encapsulated Methods)** (Impact: 34.0)
    * *Intent:* """Update request body from data."""
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 31.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 181 instances
* *Concurrency (weighted view):* 223
* *State Mutation (weighted view):* 571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 258`, `args: 81`, `func_start: 79`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 209`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 6`, `api: 64`, `concurrency: 58`, `import: 34`
* *Defense:* `safety: 44`, `doc: 25`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.41
  * `Choke Point (Betweenness):` 0.014402 | `Ripple Effect (Closeness):` 0.301345
  * `Imports (Out-Degree: 15):` ._cookie_helpers, .abc, .client, .client_exceptions, .compression_utils, .connector, .formdata, .hdrs...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_payload.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.697)
- **Top Global Matches:** file_cluster_0: 7.697, file_cluster_5: 9.169, file_cluster_12: 9.785
- **Magnitude:** 1593.88 | **LOC:** 1356 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.1%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 41.704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_textio_payload_reads_in_chunks` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* """Test TextIOPayload reads data in chunks of READ_SIZE, not all at once."""
  * `test_iobase_payload_reads_in_chunks` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* """Test IOBasePayload reads data in chunks of READ_SIZE, not all at once."""
  * `mock_read` **(Generic / Templated Code)** (Impact: 7.7)
  * `mock_read` **(Generic / Templated Code)** (Impact: 7.7)
  * `test_iobase_payload_large_content_length` **(Generic / Templated Code)** (Impact: 5.5)
    * *Intent:* """Test IOBasePayload with very large content_length doesn't read all at once."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 140 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 878
* *State Mutation (weighted view):* 339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 456`, `args: 117`, `func_start: 115`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 293`, `fragile_debt: 2`, `duplicate_logic: 20`, `unreferenced_by_name: 66`
* *Architecture:* `io: 7`, `api: 118`, `concurrency: 178`, `import: 14`
* *Defense:* `safety: 182`, `doc: 74`, `test: 81`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` aiohttp, aiohttp.abc, aiohttp.payload, array, asyncio, collections.abc, io, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/multipart.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.867)
- **Top Global Matches:** file_cluster_5: 6.867, file_cluster_12: 9.103, file_cluster_0: 9.669
- **Magnitude:** 1591.96 | **LOC:** 1214 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **23**; blast radius 12.979; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (54.8%)
- **Documentation Coverage:** 61.8321% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_content_disposition` **(Compute Cores)** (Impact: 41.8)
  * `read_chunk` **(Stateful Encapsulated Methods)** (Impact: 28.1)
    * *Intent:* """Reads body part content chunk of the specified size. size: chunk size """
  * `content_disposition_filename` **(Compute Cores)** (Impact: 25.8)
  * `_read_chunk_from_stream` **(Stateful Encapsulated Methods)** (Impact: 24.7)
    * *Intent:* # Reads content chunk of body part with unknown length. # The Content-Length header for body part is...
  * `append_payload` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* """Adds a new body part to multipart writer."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 73 instances
* *Amplified Cascading Flux:* 167 instances
* *Concurrency (weighted view):* 455
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 309`, `args: 79`, `func_start: 79`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 200`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 61`, `concurrency: 90`, `import: 25`
* *Defense:* `safety: 22`, `doc: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.979
  * `Choke Point (Betweenness):` 0.007422 | `Ripple Effect (Closeness):` 0.348335
  * `Imports (Out-Degree: 11):` .abc, .client_reqrep, .compression_utils, .hdrs, .helpers, .http, .http_exceptions, .log...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_http_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.165)
- **Top Global Matches:** file_cluster_5: 7.165, file_cluster_12: 8.652, file_cluster_0: 9.537
- **Magnitude:** 1556.96 | **LOC:** 2232 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.3%), Guard Balance (formerly Safety Score) (33.5%)
- **Documentation Coverage:** 97.7077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_max_headers` **(Compute Cores)** (Impact: 12.8)
  * `test_max_trailer_size` **(Defensive Guards)** (Impact: 11.5)
  * `test_max_header_field_size` **(Generic / Templated Code)** (Impact: 9.1)
  * `test_max_header_value_size` **(Generic / Templated Code)** (Impact: 9.1)
  * `test_max_header_value_size_continuation` **(Generic / Templated Code)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 471
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 704`, `args: 175`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 306`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 167`
* *Architecture:* `io: 43`, `api: 176`, `concurrency: 86`, `import: 20`
* *Defense:* `safety: 412`, `doc: 18`, `test: 302`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` aiohttp, aiohttp.base_protocol, aiohttp.http_parser, asyncio, backports.zstd, brotli, brotlicffi, compression.zstd...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_urldispatch.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.585)
- **Top Global Matches:** file_cluster_0: 9.585, file_cluster_12: 11.097, file_cluster_5: 11.098
- **Magnitude:** 1466.62 | **LOC:** 1386 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.1%), Guard Balance (formerly Safety Score) (37.9%)
- **Documentation Coverage:** 96.0784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_set_options_route` **(Defensive Guards)** (Impact: 7.8)
  * `test_match_domain` **(Defensive Guards)** (Impact: 6.3)
  * `test_add_static_path_checks` **(Generic / Templated Code)** (Impact: 5.5)
    * *Intent:* """Test that static paths must exist and be directories."""
  * `test_routes_view_contains` **(Defensive Guards)** (Impact: 3.7)
  * `test_register_uncommon_http_methods` **(Generic / Templated Code)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 106 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 647
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 498`, `args: 153`, `func_start: 153`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 325`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 137`
* *Architecture:* `io: 63`, `api: 153`, `concurrency: 117`, `import: 14`
* *Defense:* `safety: 224`, `doc: 6`, `test: 183`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` aiohttp, aiohttp.test_utils, aiohttp.web, aiohttp.web_urldispatcher, collections.abc, pathlib, platform, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_urldispatcher.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.273)
- **Top Global Matches:** file_cluster_0: 8.273, file_cluster_12: 9.265, file_cluster_5: 9.285
- **Magnitude:** 1454.42 | **LOC:** 1053 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.5%), Complexity Load (formerly Cognitive Load) (40.6%)
- **Documentation Coverage:** 89.0625% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_static_directory_with_mock_permission_error` **(Defensive Guards)** (Impact: 8.4)
  * `test_access_root_of_static_handler_xss` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `test_access_root_of_static_handler` **(Many-Argument Workhorses)** (Impact: 7.6)
  * `test_access_to_the_file_with_spaces` **(Many-Argument Workhorses)** (Impact: 6.2)
  * `test_static_file_with_mock_permission_error` **(Defensive Guards)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 161 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 1001
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 365`, `args: 61`, `func_start: 61`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 171`, `duplicate_logic: 14`, `unreferenced_by_name: 35`
* *Architecture:* `io: 60`, `api: 66`, `concurrency: 196`, `import: 13`
* *Defense:* `safety: 98`, `doc: 14`, `test: 65`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` aiohttp, aiohttp.pytest_plugin, aiohttp.web_urldispatcher, asyncio, functools, os, pathlib, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_session.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.778)
- **Top Global Matches:** file_cluster_5: 7.778, file_cluster_12: 9.072, file_cluster_7: 11.09
- **Magnitude:** 1433.2 | **LOC:** 1414 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.9%), Guard Balance (formerly Safety Score) (43.1%)
- **Documentation Coverage:** 92.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_request_tracing_url_params` **(Defensive Guards)** (Impact: 17.0)
  * `test_ws_connect_unix_socket_allowed_protocols` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `test_ssl_shutdown_timeout_passed_to_connector_pre_311` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* """Test that both deprecation and runtime warnings are issued on Python < 3.11."""
  * `test_ws_connect_allowed_protocols` **(Many-Argument Workhorses)** (Impact: 7.6)
  * `test_ssl_shutdown_timeout_passed_to_connector` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* # Test default value (no warning expected) async with ClientSession() as session: assert isinstance(...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 124 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 802
* *State Mutation (weighted view):* 237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 523`, `args: 116`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 211`, `duplicate_logic: 2`, `unreferenced_by_name: 69`
* *Architecture:* `io: 45`, `api: 107`, `concurrency: 182`, `import: 27`
* *Defense:* `safety: 166`, `doc: 9`, `test: 176`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` aiohttp, aiohttp.client, aiohttp.client_proto, aiohttp.client_reqrep, aiohttp.connector, aiohttp.helpers, aiohttp.http, aiohttp.pytest_plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_proxy_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.594)
- **Top Global Matches:** file_cluster_12: 8.594, file_cluster_0: 8.676, file_cluster_15: 9.392
- **Magnitude:** 1236.98 | **LOC:** 943 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 1.531; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.3%), Guard Balance (formerly Safety Score) (41.1%)
- **Documentation Coverage:** 98.0392% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_https_proxy_unsupported_tls_in_tls` **(Many-Argument Workhorses)** (Impact: 11.2)
    * *Intent:* # Filter out the warning from # https://github.com/abhinavsingh/proxy.py/blob/30574fd0414005dfa8792a...
  * `xtest_proxy_https_multi_conn_limit` **(Defensive Guards)** (Impact: 10.3)
  * `proxy_test_server` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* # Handle all proxy requests and imitate remote server response. _patch_ssl_transport(monkeypatch) de...
  * `secure_proxy_url` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* """Return the URL of an instance of a running secure proxy. This fixture also spawns that instance a...
  * `web_server_endpoint_url` **(Many-Argument Workhorses)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 122 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 788
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 378`, `args: 52`, `func_start: 52`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 162`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 33`
* *Architecture:* `io: 97`, `api: 49`, `concurrency: 178`, `import: 20`
* *Defense:* `safety: 136`, `doc: 5`, `test: 77`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` aiohttp, aiohttp.client_exceptions, aiohttp.helpers, aiohttp.pytest_plugin, aiohttp.test_utils, asyncio, contextlib, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/web_urldispatcher.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.692)
- **Top Global Matches:** file_cluster_5: 6.692, file_cluster_0: 9.474, file_cluster_12: 9.766
- **Magnitude:** 1190.58 | **LOC:** 1310 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **28**; blast radius 9.133; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (73.5%), Complexity Load (formerly Cognitive Load) (68.4%)
- **Documentation Coverage:** 80.9524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 39.4)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 29.6)
  * `resolve` **(Compute Cores)** (Impact: 21.1)
  * `register_resource` **(Defensive Guards)** (Impact: 21.0)
  * `add_resource` **(Compute Cores)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 99 instances
* *Concurrency (weighted view):* 130
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 399`, `args: 153`, `func_start: 153`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 169`, `planned_debt: 5`, `duplicate_logic: 8`
* *Architecture:* `io: 10`, `api: 116`, `concurrency: 30`, `import: 29`
* *Defense:* `safety: 46`, `doc: 30`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.133
  * `Choke Point (Betweenness):` 0.002785 | `Ripple Effect (Closeness):` 0.233543
  * `Imports (Out-Degree: 11):` .abc, .hdrs, .helpers, .http, .typedefs, .web_app, .web_exceptions, .web_fileresponse...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `aiohttp-3.13.5/examples/fake_server.py` (PYTHON) | Magnitude: 113.28 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 46, concurrency: 21, state_mutation: 20
- `aiohttp-3.13.5/examples/web_rewrite_headers_middleware.py` (PYTHON) | Magnitude: 29.98 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, listeners: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `aiohttp-3.13.5/tests/autobahn/server/server.py` (PYTHON) | Magnitude: 75.92 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 19, state_mutation: 9, branch: 8
- `aiohttp-3.13.5/tests/test_proxy_functional.py` (PYTHON) | Magnitude: 1236.98 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 571, structural_boundaries: 378, core_var_decl: 179, concurrency: 178

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `aiohttp-3.13.5/examples/digest_auth_qop_auth.py` (PYTHON) | Magnitude: 45.18 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, state_mutation: 8, debug_prints: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `aiohttp-3.13.5/aiohttp/cookiejar.py` (PYTHON) | Magnitude: 553.76 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 333, state_mutation: 111, structural_boundaries: 104, branch: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `aiohttp-3.13.5/tests/test_benchmarks_client.py` (PYTHON) | Magnitude: 1166.64 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 359, structural_boundaries: 176, concurrency: 130, core_var_decl: 95

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `aiohttp-3.13.5/aiohttp/client.py` -> **Severity: 3.172** (Bridge: 0.0317 * Flux: 99.9962%)
- `aiohttp-3.13.5/aiohttp/__init__.py` -> **Severity: 1.806** (Bridge: 0.0588 * Flux: 30.7316%)
- `aiohttp-3.13.5/aiohttp/web.py` -> **Severity: 1.748** (Bridge: 0.0195 * Flux: 89.5878%)
- `aiohttp-3.13.5/aiohttp/abc.py` -> **Severity: 1.668** (Bridge: 0.0168 * Flux: 99.5645%)
- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 1.598** (Bridge: 0.016 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `aiohttp-3.13.5/aiohttp/helpers.py` -> **Severity: 31.385** (Embedded: 0.4226 * Error Risk: 74.2645%)
- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 30.025** (Embedded: 0.3618 * Error Risk: 82.9829%)
- `aiohttp-3.13.5/aiohttp/streams.py` -> **Severity: 27.473** (Embedded: 0.371 * Error Risk: 74.0568%)
- `aiohttp-3.13.5/aiohttp/multipart.py` -> **Severity: 27.067** (Embedded: 0.3483 * Error Risk: 77.7035%)
- `aiohttp-3.13.5/aiohttp/payload.py` -> **Severity: 24.998** (Embedded: 0.3369 * Error Risk: 74.1957%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 5094.4** (Blast Radius: 50.944 * Doc Risk: 100.0%)
- `aiohttp-3.13.5/aiohttp/web.py` -> **Severity: 4765.9** (Blast Radius: 47.659 * Doc Risk: 100.0%)
- `aiohttp-3.13.5/aiohttp/__init__.py` -> **Severity: 4553.6** (Blast Radius: 45.536 * Doc Risk: 100.0%)
- `aiohttp-3.13.5/aiohttp/helpers.py` -> **Severity: 3017.801** (Blast Radius: 44.899 * Doc Risk: 67.2131%)
- `aiohttp-3.13.5/aiohttp/web_response.py` -> **Severity: 2520.805** (Blast Radius: 26.187 * Doc Risk: 96.2617%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 151 literal sites + 2 sites through wrappers = 153
- **`panics_and_aborts`:** 2170 literal sites + 32 sites through wrappers = 2202

- `stopper` (function, panics_and_aborts, primitive): 27 call sites in 1 files -- `aiohttp-3.13.5/tests/test_run_app.py`
- `shutdown` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `aiohttp-3.13.5/tests/test_web_runner.py`
- `dns_response_error` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `aiohttp-3.13.5/tests/test_connector.py`
- `fail` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `aiohttp-3.13.5/tests/test_run_app.py`
- `fetch` (function, debug_prints, primitive): 1 call sites in 1 files -- `aiohttp-3.13.5/examples/client_auth.py`
- `fetch` (function, debug_prints, primitive): 1 call sites in 1 files -- `aiohttp-3.13.5/examples/client_json.py`
- `test_subprocess_co` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `aiohttp-3.13.5/tests/test_loop.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 22199 call pairs -- scoped 38.9%, unique 0.0%, ambiguous 16.4%, external 44.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 22169 | 38.9% | 0.0% | 16.4% | 44.7% |
| html | 14 | 35.7% | 0.0% | 0.0% | 64.3% |
| makefile | 12 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 3 | 0.0% | 0.0% | 0.0% | 100.0% |
| c | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
