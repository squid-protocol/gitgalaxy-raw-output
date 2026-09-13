# ARCHITECTURAL_BRIEF: aiohttp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 232 |
| Analyzed Artifacts (Scanned) | 193 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 39 |
| Total LOC | 74340 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.364 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1476 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6378 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 168 | 64033 | 87.0% |
| M4 | 9 | 40 | 4.7% |
| PLAINTEXT | 6 | 2 | 3.1% |
| JSON | 3 | 676 | 1.6% |
| C | 2 | 9332 | 1.0% |
| SHELL | 2 | 5 | 1.0% |
| MAKEFILE | 1 | 147 | 0.5% |
| HTML | 1 | 94 | 0.5% |
| DOCKERFILE | 1 | 11 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 187 | 96.9% |
| Unknown | 2 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 39*

**Composition by Extension & Reason:**
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Machine-Generated Source Code Signature: 53 LOC)
- `.c`: 1x Excluded (Monolithic Amalgamation: 31398 LOC exceeds safe regex boundaries), 1x Excluded (Machine-Generated Source Code Signature: 10589 LOC), 1x Excluded (Machine-Generated Source Code Signature: 8687 LOC)
- `.in`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Packed Payload Guard (Impossible Density: 3.02 hits/line), 1x Packed Payload Guard (Impossible Density: 3.76 hits/line)
- `no_extension`: 1x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.unknown_mime_type'), 1x Excluded (Unsupported Extension: '.dockerignore')
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 38.1 | 43.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 58.8 | 67.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.3 | 11.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 64.2 | 100.0 | 100.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 21.7 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 85.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 72.9 | 95.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 752 | 106 | 12 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| cleanup | 873 | 66 | 8 | `aiohttp-3.13.5/tests/test_connector.py` |
| guards | 8874 | 142 | 139 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| danger | 3443 | 127 | 36 | `aiohttp-3.13.5/aiohttp/_find_header.c` |
| concurrency | 10150 | 127 | 122 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| connectivity | 5927 | 162 | 81 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| io | 2312 | 140 | 30 | `aiohttp-3.13.5/tests/test_connector.py` |
| crypto | 40 | 28 | 1 | `aiohttp-3.13.5/aiohttp/client_reqrep.py` |
| ipc | 44 | 17 | 0 | `aiohttp-3.13.5/tests/test_run_app.py` |
| time | 69 | 15 | 0 | `aiohttp-3.13.5/tests/test_cookiejar.py` |
| serialization | 15 | 5 | 0 | `aiohttp-3.13.5/tests/test_client_exceptions.py` |
| regex | 60 | 19 | 0 | `aiohttp-3.13.5/aiohttp/web_urldispatcher.py` |
| events | 1681 | 61 | 20 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| tests | 7197 | 80 | 127 | `aiohttp-3.13.5/tests/test_connector.py` |
| docs | 1322 | 122 | 23 | `aiohttp-3.13.5/tests/test_cookie_helpers.py` |
| debt | 709 | 81 | 10 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| mutation | 29423 | 167 | 422 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| dead_code | 3021 | 97 | 53 | `aiohttp-3.13.5/tests/test_client_functional.py` |
| credential | 11 | 7 | 0 | `aiohttp-3.13.5/tests/test_urldispatch.py` |
| threat | 1594 | 72 | 8 | `aiohttp-3.13.5/aiohttp/_find_header.c` |
| ml_ai | 81 | 13 | 0 | `aiohttp-3.13.5/aiohttp/_find_header.c` |
| ui | 12 | 3 | 0 | `aiohttp-3.13.5/examples/websocket.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5714**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `aiohttp-3.13.5/tests/test_connector.py` (Hits: 341)
- `aiohttp-3.13.5/tests/test_client_functional.py` (Hits: 203)
- `aiohttp-3.13.5/tests/test_multipart.py` (Hits: 132)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **abc.py** (`aiohttp-3.13.5/aiohttp/abc.py`) — 39 inbound connections
2. **multidict.in** (`aiohttp-3.13.5/requirements/multidict.in`) — 39 inbound connections
3. **typedefs.py** (`aiohttp-3.13.5/aiohttp/typedefs.py`) — 28 inbound connections
4. **http.py** (`aiohttp-3.13.5/aiohttp/http.py`) — 25 inbound connections
5. **pytest_plugin.py** (`aiohttp-3.13.5/aiohttp/pytest_plugin.py`) — 21 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_client_functional.py** (`aiohttp-3.13.5/tests/test_client_functional.py`) — 36 outbound dependencies
2. **helpers.py** (`aiohttp-3.13.5/aiohttp/helpers.py`) — 33 outbound dependencies
3. **client_reqrep.py** (`aiohttp-3.13.5/aiohttp/client_reqrep.py`) — 31 outbound dependencies
4. **client.py** (`aiohttp-3.13.5/aiohttp/client.py`) — 30 outbound dependencies
5. **test_utils.py** (`aiohttp-3.13.5/aiohttp/test_utils.py`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `find_header` (@ `aiohttp-3.13.5/aiohttp/_find_header.c`) -> Impact: **1669.6** | LOC: 2492
- `_request` (@ `aiohttp-3.13.5/aiohttp/client.py`) -> Impact: **588.4** | LOC: 456
- `__init__` (@ `aiohttp-3.13.5/aiohttp/client.py`) -> Impact: **217.9** | LOC: 159
- `_ws_connect` (@ `aiohttp-3.13.5/aiohttp/client.py`) -> Impact: **157.8** | LOC: 216
- `feed_data` (@ `aiohttp-3.13.5/aiohttp/http_parser.py`) -> Impact: **135.4** | LOC: 218
- `__init__` (@ `aiohttp-3.13.5/aiohttp/client_reqrep.py`) -> Impact: **108.9** | LOC: 78
  * *Intent:* # N.B. # Adding __del__ method with self._writer closing doesn't make sense # because _writer is instance method, thus it keeps a reference to self. #...
- `feed_data` (@ `aiohttp-3.13.5/aiohttp/http_parser.py`) -> Impact: **94.6** | LOC: 148
- `__init__` (@ `aiohttp-3.13.5/aiohttp/web_response.py`) -> Impact: **92.7** | LOC: 64
- `_handle_frame` (@ `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py`) -> Impact: **90.3** | LOC: 140
- `_handle_frame` (@ `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py`) -> Impact: **90.3** | LOC: 140

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `aiohttp-3.13.5/tests` | 74 | 69298.7 | 30.72% | 0.0% |
| `aiohttp-3.13.5/aiohttp` | 55 | 25697.7 | 53.91% | 12.75% |
| `aiohttp-3.13.5/examples` | 27 | 12570.66 | 37.44% | 0.0% |
| `aiohttp-3.13.5/aiohttp/_websocket` | 10 | 1597.84 | 34.71% | 8.64% |
| `aiohttp-3.13.5/tests/isolated` | 2 | 157.06 | 45.0% | 0.0% |
| `aiohttp-3.13.5` | 5 | 131.92 | 20.02% | 13.5% |
| `aiohttp-3.13.5/requirements` | 9 | 107.8 | 0.0% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn/client` | 2 | 91.28 | 25.0% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn/server` | 2 | 91.2 | 25.0% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn` | 1 | 78.36 | 21.84% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `aiohttp-3.13.5/aiohttp/payload_streamer.py` -> **99.9797%** Exposure
- `aiohttp-3.13.5/aiohttp/client_exceptions.py` -> **98.0549%** Exposure
- `aiohttp-3.13.5/aiohttp/streams.py` -> **91.6628%** Exposure
- `aiohttp-3.13.5/aiohttp/payload.py` -> **85.2622%** Exposure
- `aiohttp-3.13.5/aiohttp/web_urldispatcher.py` -> **74.9791%** Exposure
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
- `aiohttp-3.13.5/examples/fake_server.py` -> **99.9954%** Exposure
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **11.4686%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1326` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `aiohttp-3.13.5/aiohttp/client_exceptions.py` (PYTHON) -> Cumulative Risk: **801.26**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 252.84 | **LOC:** 433 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (98.0549%)
- **Heaviest Functions:** `__init__` (Impact: 21.4), `__init__` (Impact: 6.8), `__init__` (Impact: 6.5)

### 2. `aiohttp-3.13.5/aiohttp/web_runner.py` (PYTHON) -> Cumulative Risk: **774.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 474.18 | **LOC:** 400 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9991%), Documentation (96.5517%)
- **Heaviest Functions:** `__init__` (Impact: 17.0), `__init__` (Impact: 13.8), `__init__` (Impact: 8.2)

### 3. `aiohttp-3.13.5/aiohttp/web_response.py` (PYTHON) -> Cumulative Risk: **770.03**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1006.24 | **LOC:** 857 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9949%), Documentation (96.2617%)
- **Heaviest Functions:** `__init__` (Impact: 92.7), `set_cookie` (Impact: 45.9), `_prepare_headers` (Impact: 38.6)

### 4. `aiohttp-3.13.5/aiohttp/streams.py` (PYTHON) -> Cumulative Risk: **762.13**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 861.92 | **LOC:** 763 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (96.0453%)
- **Heaviest Functions:** `readuntil` (Impact: 27.9), `read` (Impact: 22.8), `_read_nowait_chunk` (Impact: 20.8)

### 5. `aiohttp-3.13.5/aiohttp/client_reqrep.py` (PYTHON) -> Cumulative Risk: **752.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1596.58 | **LOC:** 1537 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Safety Score (94.6706%)
- **Heaviest Functions:** `__init__` (Impact: 108.9), `send` (Impact: 51.7), `_merge_ssl_params` (Impact: 40.7)

### 6. `aiohttp-3.13.5/aiohttp/web_app.py` (PYTHON) -> Cumulative Risk: **751.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 543.04 | **LOC:** 621 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.9984%), Safety Score (93.5508%)
- **Heaviest Functions:** `_handle` (Impact: 24.7), `__init__` (Impact: 17.8), `_set_loop` (Impact: 11.2)

### 7. `aiohttp-3.13.5/aiohttp/client_proto.py` (PYTHON) -> Cumulative Risk: **747.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 302.42 | **LOC:** 362 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (97.0639%), Documentation (95.122%)
- **Heaviest Functions:** `data_received` (Impact: 38.1), `connection_lost` (Impact: 26.2), `should_close` (Impact: 11.8)

### 8. `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` (PYTHON) -> Cumulative Risk: **745.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 539.62 | **LOC:** 479 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.6205%), Safety Score (98.4341%)
- **Heaviest Functions:** `_handle_frame` (Impact: 90.3), `_feed_data` (Impact: 77.0), `_read_from_buffer` (Impact: 7.6)

### 9. `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` (PYTHON) -> Cumulative Risk: **745.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 539.62 | **LOC:** 479 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.6205%), Safety Score (98.4341%)
- **Heaviest Functions:** `_handle_frame` (Impact: 90.3), `_feed_data` (Impact: 77.0), `_read_from_buffer` (Impact: 7.6)

### 10. `aiohttp-3.13.5/aiohttp/web_middlewares.py` (PYTHON) -> Cumulative Risk: **745.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 177.04 | **LOC:** 122 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `normalize_path_middleware` (Impact: 41.5), `impl` (Impact: 27.4), `_check_request_resolves` (Impact: 4.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `aiohttp-3.13.5/tests/test_client_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10429.76 | **LOC:** 5805 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.3462%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_amazon_like_cookie_scenario` (Impact: 18.5)
    * *Intent:* """Test real-world cookie scenario similar to Amazon."""
  * `test_ssl_client_shutdown_timeout` (Impact: 12.0)
  * `test_drop_auth_on_redirect_to_other_host` (Impact: 11.6)
  * `test_file_upload_307_302_redirect_chain` (Impact: 11.6)
  * `test_file_upload_301_302_redirect_non_post` (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1124 instances
* *Amplified Cascading Flux:* 150 instances
* *Concurrency (weighted view):* 7091
* *State Mutation (weighted view):* 1396
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 2558`, `args: 538`, `func_start: 538`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 1096`, `dead_code: 3`, `duplicate_logic: 121`, `unreferenced_by_name: 240`
* *Architecture:* `io: 203`, `api: 545`, `concurrency: 1471`, `import: 37`
* *Defense:* `safety: 597`, `doc: 55`, `test: 361`, `sync_locks: 1`, `cleanup: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` aiohttp, aiohttp.abc, aiohttp.client_exceptions, aiohttp.client_reqrep, aiohttp.compression_utils, aiohttp.connector, aiohttp.http_exceptions, aiohttp.http_writer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_connector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5773.8 | **LOC:** 4537 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.0299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_connect_reuse_proxy_headers` (Impact: 32.8)
  * `test_tcp_connector_multiple_hosts_errors` (Impact: 27.8)
  * `create_connection` (Impact: 24.6)
  * `test_tcp_connector_multiple_hosts_one_timeout` (Impact: 15.9)
  * `test_multiple_dns_resolution_requests_first_fails_second_successful` (Impact: 12.4)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` aiohttp, aiohttp.client, aiohttp.client_proto, aiohttp.client_reqrep, aiohttp.connector, aiohttp.pytest_plugin, aiohttp.resolver, aiohttp.test_utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5004.3 | **LOC:** 2383 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_subapp_middleware_context` (Impact: 8.7)
  * `test_request_tracing` (Impact: 7.7)
  * `resolve` (Impact: 7.5)
  * `test_files_upload_with_same_key` (Impact: 7.3)
  * `handler` (Impact: 6.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` aiohttp, aiohttp.compression_utils, aiohttp.hdrs, aiohttp.pytest_plugin, aiohttp.typedefs, aiohttp.web_protocol, asyncio, brotli...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/examples/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/examples/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_websocket_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3696.54 | **LOC:** 1397 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.9516%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_websocket_shutdown` (Impact: 7.0)
    * *Intent:* """Test that the client websocket gets the close message when the server is shutting down."""
  * `test_closed_async_for` (Impact: 6.9)
  * `test_server_ws_async_for` (Impact: 6.7)
  * `test_heartbeat_no_pong_send_many_messages` (Impact: 6.5)
  * `test_heartbeat_no_pong_receive_many_messages` (Impact: 6.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` aiohttp, aiohttp.http, aiohttp.pytest_plugin, asyncio, contextlib, pytest, sys, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_streams.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2780.48 | **LOC:** 1726 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.5083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unread_data` (Impact: 21.5)
  * `get_memory_usage` (Impact: 9.6)
  * `test_readchunk_with_unread` (Impact: 9.3)
    * *Intent:* # Test that stream.unread does not break controlled chunk receiving. stream = self._make_one() # Sen...
  * `test_stream_reader_small_limit_resumes_reading` (Impact: 5.8)
  * `test_read_eof_unread_data_no_warning` (Impact: 5.2)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` abc, aiohttp, aiohttp.http_exceptions, asyncio, collections, gc, itertools, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_http_writer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2480.08 | **LOC:** 1654 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.5561%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_write_large_payload_deflate_compression_data_in_eof_writelines_all_zlib` (Impact: 15.7)
  * `test_write_large_payload_deflate_compression_data_in_eof_all_zlib` (Impact: 11.5)
  * `test_write_large_payload_deflate_compression_data_in_eof` (Impact: 11.2)
  * `test_write_large_payload_deflate_compression_chunked_data_in_eof` (Impact: 11.2)
  * `test_write_large_payload_deflate_compression_chunked_data_in_eof_all_zlib` (Impact: 11.2)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` aiohttp, aiohttp.base_protocol, aiohttp.compression_utils, aiohttp.http_writer, array, asyncio, multidict, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_request.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2306.1 | **LOC:** 2283 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.7507%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_write_bytes_with_iterable_content_length_limit` (Impact: 10.3)
  * `test_warn_stacklevel_points_to_user_code` (Impact: 6.0)
  * `test_warn_stacklevel_update_body_from_data` (Impact: 5.8)
  * `test_no_warn_for_consumed_payload_via_body_setter` (Impact: 5.6)
  * `test_no_warn_for_autoclose_payload_via_body_setter` (Impact: 5.3)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` aiohttp, aiohttp.abc, aiohttp.client_exceptions, aiohttp.client_reqrep, aiohttp.compression_utils, aiohttp.http, asyncio, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_multipart.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2206.8 | **LOC:** 1864 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.722%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_read_boundary_across_chunks` (Impact: 12.8)
  * `readline` (Impact: 9.1)
  * `test_async_for_reader` (Impact: 9.0)
  * `check` (Impact: 8.9)
  * `test_read_chunk_by_length_doesnt_breaks_reader` (Impact: 7.2)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` aiohttp, aiohttp.abc, aiohttp.compression_utils, aiohttp.hdrs, aiohttp.helpers, aiohttp.multipart, aiohttp.streams, asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_middleware.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1892.02 | **LOC:** 1272 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.3279%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_client_middleware_multi_step_auth` (Impact: 26.8)
    * *Intent:* """Test middleware with multi-step authentication flow."""
  * `test_client_middleware_challenge_auth` (Impact: 20.3)
    * *Intent:* """Test authentication middleware with challenge/response pattern like digest auth."""
  * `multi_step_auth_middleware` (Impact: 19.3)
  * `challenge_auth_middleware` (Impact: 16.9)
  * `test_client_middleware_conditional_retry` (Impact: 15.9)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` aiohttp, aiohttp.abc, aiohttp.client_middlewares, aiohttp.client_proto, aiohttp.pytest_plugin, aiohttp.resolver, aiohttp.tracing, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/_find_header.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1872.04 | **LOC:** 9871 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5483%), Tech Debt (7.6994%)
**Top Internal Functions/Classes:**
  * `find_header` (Impact: 1669.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3476`, `structural_boundaries: 1739`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _find_header.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_sendfile_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1867.16 | **LOC:** 1153 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.0862%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sender` (Impact: 9.7)
  * `test_static_file_range` (Impact: 8.1)
  * `test_static_file_huge_cancel` (Impact: 7.2)
  * `test_static_file_huge` (Impact: 7.0)
  * `maker` (Impact: 5.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` aiohttp, aiohttp.compression_utils, aiohttp.pytest_plugin, asyncio, brotli, brotlicffi, bz2, gzip...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/client.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1758.2 | **LOC:** 1647 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.3625%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_request` (Impact: 588.4)
  * `__init__` (Impact: 217.9)
  * `_ws_connect` (Impact: 157.8)
  * `_prepare_headers` (Impact: 11.1)
    * *Intent:* """Add default headers and transform it to CIMultiDict"""
  * `request` (Impact: 8.4)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.698
  * `Choke Point (Betweenness):` 0.006787 | `Ripple Effect (Closeness):` 0.077005
  * `Imports (Out-Degree: 12):` , ._websocket.reader, .abc, .client_exceptions, .client_middlewares, .client_reqrep, .client_ws, .connector...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/aiohttp/connector.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1720.58 | **LOC:** 1855 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.7552%), Tech Debt (14.1634%)
**Top Internal Functions/Classes:**
  * `_start_tls_connection` (Impact: 50.8)
  * `__init__` (Impact: 47.2)
  * `_resolve_host` (Impact: 42.5)
  * `_close` (Impact: 41.2)
  * `__init__` (Impact: 36.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 53 instances
* *Amplified Cascading Flux:* 152 instances
* *Concurrency (weighted view):* 384
* *State Mutation (weighted view):* 519
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 322`, `args: 79`, `func_start: 79`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 215`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 29`, `api: 42`, `concurrency: 119`, `import: 30`
* *Defense:* `safety: 67`, `doc: 42`, `test: 1`, `immutability_locks: 6`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.989
  * `Choke Point (Betweenness):` 0.007583 | `Ripple Effect (Closeness):` 0.163477
  * `Imports (Out-Degree: 8):` , .abc, .client, .client_exceptions, .client_proto, .client_reqrep, .helpers, .log...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_web_response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1702.52 | **LOC:** 1608 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.0387%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_request` (Impact: 11.5)
  * `test_payload_body_get_text` (Impact: 5.5)
  * `test_multiline_reason` (Impact: 5.3)
  * `_strip_server` (Impact: 3.7)
  * `test_last_modified_invalid_type` (Impact: 3.2)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` aiohttp, aiohttp.abc, aiohttp.helpers, aiohttp.http_writer, aiohttp.multipart, aiohttp.payload, aiohttp.test_utils, aiohttp.web...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/client_reqrep.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1596.58 | **LOC:** 1537 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1911%), Tech Debt (31.8151%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 108.9)
    * *Intent:* # N.B. # Adding __del__ method with self._writer closing doesn't make sense # because _writer is ins...
  * `send` (Impact: 51.7)
    * *Intent:* # Specify request target: # - CONNECT request must send authority form URI # - not CONNECT proxy mus...
  * `_merge_ssl_params` (Impact: 40.7)
  * `update_body_from_data` (Impact: 34.0)
    * *Intent:* """Update request body from data."""
  * `__init__` (Impact: 31.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 181 instances
* *Concurrency (weighted view):* 223
* *State Mutation (weighted view):* 571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 258`, `args: 81`, `func_start: 79`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 209`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 6`, `api: 64`, `concurrency: 58`, `import: 34`
* *Defense:* `safety: 44`, `doc: 25`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.652
  * `Choke Point (Betweenness):` 0.025234 | `Ripple Effect (Closeness):` 0.218494
  * `Imports (Out-Degree: 11):` , ._cookie_helpers, .abc, .client, .client_exceptions, .compression_utils, .connector, .formdata...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_payload.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1593.88 | **LOC:** 1356 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_textio_payload_reads_in_chunks` (Impact: 8.1)
    * *Intent:* """Test TextIOPayload reads data in chunks of READ_SIZE, not all at once."""
  * `test_iobase_payload_reads_in_chunks` (Impact: 8.0)
    * *Intent:* """Test IOBasePayload reads data in chunks of READ_SIZE, not all at once."""
  * `mock_read` (Impact: 7.7)
  * `mock_read` (Impact: 7.7)
  * `test_iobase_payload_large_content_length` (Impact: 5.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` aiohttp, aiohttp.abc, aiohttp.payload, array, asyncio, collections.abc, io, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/multipart.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1591.96 | **LOC:** 1214 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.7745%), Tech Debt (21.6987%)
**Top Internal Functions/Classes:**
  * `parse_content_disposition` (Impact: 41.8)
  * `read_chunk` (Impact: 28.1)
    * *Intent:* """Reads body part content chunk of the specified size. size: chunk size """
  * `content_disposition_filename` (Impact: 25.8)
  * `_read_chunk_from_stream` (Impact: 24.7)
    * *Intent:* # Reads content chunk of body part with unknown length. # The Content-Length header for body part is...
  * `append_payload` (Impact: 22.6)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.193
  * `Choke Point (Betweenness):` 0.00973 | `Ripple Effect (Closeness):` 0.169157
  * `Imports (Out-Degree: 10):` .abc, .client_reqrep, .compression_utils, .hdrs, .helpers, .http, .http_exceptions, .log...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_http_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1556.96 | **LOC:** 2232 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.2793%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_max_headers` (Impact: 12.8)
  * `test_max_trailer_size` (Impact: 11.5)
  * `test_max_header_field_size` (Impact: 9.1)
  * `test_max_header_value_size` (Impact: 9.1)
  * `test_max_header_value_size_continuation` (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 471
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 704`, `args: 175`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 306`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 167`
* *Architecture:* `io: 43`, `api: 176`, `concurrency: 86`, `import: 20`
* *Defense:* `safety: 412`, `doc: 18`, `test: 302`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` aiohttp, aiohttp.base_protocol, aiohttp.http_parser, asyncio, backports.zstd, brotli, brotlicffi, compression.zstd...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_urldispatch.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1466.62 | **LOC:** 1386 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.0615%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_set_options_route` (Impact: 7.8)
  * `test_match_domain` (Impact: 6.3)
  * `test_add_static_path_checks` (Impact: 5.5)
    * *Intent:* """Test that static paths must exist and be directories."""
  * `test_routes_view_contains` (Impact: 3.7)
  * `test_register_uncommon_http_methods` (Impact: 3.6)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` aiohttp, aiohttp.test_utils, aiohttp.web, aiohttp.web_urldispatcher, collections.abc, pathlib, platform, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_urldispatcher.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1454.42 | **LOC:** 1053 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_static_directory_with_mock_permission_error` (Impact: 8.4)
  * `test_access_root_of_static_handler_xss` (Impact: 7.7)
  * `test_access_root_of_static_handler` (Impact: 7.6)
  * `test_access_to_the_file_with_spaces` (Impact: 6.2)
  * `test_static_file_with_mock_permission_error` (Impact: 5.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` aiohttp, aiohttp.pytest_plugin, aiohttp.web_urldispatcher, asyncio, functools, os, pathlib, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_session.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1433.2 | **LOC:** 1414 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.8903%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_request_tracing_url_params` (Impact: 17.0)
  * `test_ws_connect_unix_socket_allowed_protocols` (Impact: 7.9)
  * `test_ssl_shutdown_timeout_passed_to_connector_pre_311` (Impact: 7.8)
    * *Intent:* """Test that both deprecation and runtime warnings are issued on Python < 3.11."""
  * `test_ws_connect_allowed_protocols` (Impact: 7.6)
  * `test_ssl_shutdown_timeout_passed_to_connector` (Impact: 6.9)
    * *Intent:* # Test default value (no warning expected) async with ClientSession() as session: assert isinstance(...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 124 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 802
* *State Mutation (weighted view):* 237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 523`, `args: 116`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 211`, `dead_code: 5`, `duplicate_logic: 2`, `unreferenced_by_name: 69`
* *Architecture:* `io: 45`, `api: 107`, `concurrency: 182`, `import: 27`
* *Defense:* `safety: 166`, `doc: 9`, `test: 176`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` aiohttp, aiohttp.client, aiohttp.client_proto, aiohttp.client_reqrep, aiohttp.connector, aiohttp.helpers, aiohttp.http, aiohttp.pytest_plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_proxy_functional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1236.98 | **LOC:** 943 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.2908%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_https_proxy_unsupported_tls_in_tls` (Impact: 11.2)
    * *Intent:* # Filter out the warning from # https://github.com/abhinavsingh/proxy.py/blob/30574fd0414005dfa8792a...
  * `xtest_proxy_https_multi_conn_limit` (Impact: 10.3)
  * `proxy_test_server` (Impact: 10.2)
    * *Intent:* # Handle all proxy requests and imitate remote server response. _patch_ssl_transport(monkeypatch) de...
  * `secure_proxy_url` (Impact: 8.5)
    * *Intent:* """Return the URL of an instance of a running secure proxy. This fixture also spawns that instance a...
  * `web_server_endpoint_url` (Impact: 8.0)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` aiohttp, aiohttp.client_exceptions, aiohttp.helpers, aiohttp.pytest_plugin, aiohttp.test_utils, asyncio, contextlib, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/web_urldispatcher.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1190.58 | **LOC:** 1310 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.3742%), Tech Debt (74.9791%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 39.4)
  * `__init__` (Impact: 29.6)
  * `resolve` (Impact: 21.1)
  * `register_resource` (Impact: 21.0)
  * `add_resource` (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 99 instances
* *Concurrency (weighted view):* 130
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 399`, `args: 153`, `func_start: 153`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 169`, `dead_code: 2`, `planned_debt: 5`, `duplicate_logic: 8`
* *Architecture:* `io: 10`, `api: 116`, `concurrency: 30`, `import: 29`
* *Defense:* `safety: 46`, `doc: 30`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.956
  * `Choke Point (Betweenness):` 0.007938 | `Ripple Effect (Closeness):` 0.189361
  * `Imports (Out-Degree: 9):` , .abc, .helpers, .http, .typedefs, .web_app, .web_exceptions, .web_fileresponse...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `aiohttp-3.13.5/aiohttp/client_reqrep.py` -> **Severity: 2.523** (Bridge: 0.0252 * Flux: 100.0%)
- `aiohttp-3.13.5/aiohttp/web.py` -> **Severity: 2.41** (Bridge: 0.0269 * Flux: 89.5878%)
- `aiohttp-3.13.5/aiohttp/abc.py` -> **Severity: 2.129** (Bridge: 0.0214 * Flux: 99.5645%)
- `aiohttp-3.13.5/aiohttp/web_request.py` -> **Severity: 2.045** (Bridge: 0.0204 * Flux: 100.0%)
- `aiohttp-3.13.5/aiohttp/test_utils.py` -> **Severity: 1.99** (Bridge: 0.0199 * Flux: 99.9998%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 29.453** (Embedded: 0.2964 * Error Risk: 99.3725%)
- `aiohttp-3.13.5/aiohttp/streams.py` -> **Severity: 24.801** (Embedded: 0.2582 * Error Risk: 96.0453%)
- `aiohttp-3.13.5/aiohttp/abc.py` -> **Severity: 23.273** (Embedded: 0.3071 * Error Risk: 75.7882%)
- `aiohttp-3.13.5/aiohttp/_cookie_helpers.py` -> **Severity: 22.497** (Embedded: 0.2269 * Error Risk: 99.1532%)
- `aiohttp-3.13.5/aiohttp/http_parser.py` -> **Severity: 22.078** (Embedded: 0.2257 * Error Risk: 97.8094%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 5904.4** (Blast Radius: 59.044 * Doc Risk: 100.0%)
- `aiohttp-3.13.5/aiohttp/web.py` -> **Severity: 3526.3** (Blast Radius: 35.263 * Doc Risk: 100.0%)
- `aiohttp-3.13.5/aiohttp/web_response.py` -> **Severity: 2650.373** (Blast Radius: 27.533 * Doc Risk: 96.2617%)
- `aiohttp-3.13.5/aiohttp/client_exceptions.py` -> **Severity: 1831.4** (Blast Radius: 18.314 * Doc Risk: 100.0%)
- `aiohttp-3.13.5/aiohttp/base_protocol.py` -> **Severity: 1802.97** (Blast Radius: 20.033 * Doc Risk: 90.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
