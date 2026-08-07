# ARCHITECTURAL_BRIEF: sse-starlette
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/sse-starlette` |
| **Timestamp** | `2026-08-07T05:26:48.526592+00:00` |
| **Scan Duration** | `0.11s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 11 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 20 |
| Analyzed Artifacts (Scanned) | 14 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 1259 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.281 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1828 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0222 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 11 | 1259 | 78.6% |
| PLAINTEXT | 2 | 0 | 14.3% |
| MARKDOWN | 1 | 0 | 7.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.451`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_4 | 4 | 28.6% |
| file_cluster_8 | 3 | 21.4% |
| file_cluster_13 | 2 | 14.3% |
| file_cluster_16 | 1 | 7.1% |
| file_cluster_0 | 1 | 7.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 21.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 3.0 | 49.5 | 19.2 | 23.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 76.4 | 24.2 | 18.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 99.4 | 12.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.8 | 5.0 | 4.2 | 1.9 |
| Concurrency Exposure | 0.0 | 100.0 | 54.5 | 99.9 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 2.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 49.1 | 7.9 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sse_starlette-3.3.4/tests/anyio_compat.py` (Hits: 1)
- `sse_starlette-3.3.4/AUTHORS` (Hits: 0)
- `sse_starlette-3.3.4/MANIFEST.in` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sse.py** (`sse_starlette-3.3.4/sse_starlette/sse.py`) — 6 inbound connections
2. **event.py** (`sse_starlette-3.3.4/sse_starlette/event.py`) — 3 inbound connections
3. **anyio_compat.py** (`sse_starlette-3.3.4/tests/anyio_compat.py`) — 2 inbound connections
4. **AUTHORS** (`sse_starlette-3.3.4/AUTHORS`) — 0 inbound connections
5. **MANIFEST.in** (`sse_starlette-3.3.4/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sse.py** (`sse_starlette-3.3.4/sse_starlette/sse.py`) — 15 outbound dependencies
2. **test_sse.py** (`sse_starlette-3.3.4/tests/test_sse.py`) — 11 outbound dependencies
3. **test_multi_loop.py** (`sse_starlette-3.3.4/tests/test_multi_loop.py`) — 6 outbound dependencies
4. **test_issue132.py** (`sse_starlette-3.3.4/tests/test_issue132.py`) — 5 outbound dependencies
5. **event.py** (`sse_starlette-3.3.4/sse_starlette/event.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_same_thread_shares_state` (@ `sse_starlette-3.3.4/tests/test_multi_loop.py`) -> Impact: **55.3** | LOC: 240
- `test_single_watcher_per_thread` (@ `sse_starlette-3.3.4/tests/test_issue152.py`) -> Impact: **48.5** | LOC: 171
  * *Intent:* # Watcher polls every 0.5s, so we need >0.5s for it to detect shutdown.
- `_stream_response` (@ `sse_starlette-3.3.4/sse_starlette/sse.py`) -> Impact: **44.9** | LOC: 101
  * *Intent:* # "The no-store response directive indicates that any caches of any kind (private or shared) # should not store this response." # -- https://developer...
- `test_shutdownGracePeriod_whenGeneratorEx` (@ `sse_starlette-3.3.4/tests/test_issue167.py`) -> Impact: **25.1** | LOC: 63
- `_shutdown_watcher` (@ `sse_starlette-3.3.4/sse_starlette/sse.py`) -> Impact: **19.4** | LOC: 27
- `encode` (@ `sse_starlette-3.3.4/sse_starlette/event.py`) -> Impact: **17.0** | LOC: 28
- `test_noShutdownEvent_whenShutdownDetecte` (@ `sse_starlette-3.3.4/tests/test_issue167.py`) -> Impact: **14.2** | LOC: 43
  * *Intent:* # If force-cancel worked, run_response should have finished # and we should be able to cancel the outer group cleanly
- `app` (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **13.6** | LOC: 32
- `stream_numbers` (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **12.8** | LOC: 15
  * *Intent:* # Arrange async def app(scope, receive, send): # Create bounded memory channel for producer-consumer communication send_chan, recv_chan = anyio.create...
- `test_send_whenTimeoutOccurs_thenRaisesSe` (@ `sse_starlette-3.3.4/tests/test_sse.py`) -> Impact: **11.4** | LOC: 28
  * *Intent:* # https://www.python-httpx.org/async/#streaming-responses tg.start_soon(httpx_client.get, "/endless") finally: assert scope.cancel_called is True asse...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sse_starlette-3.3.4/tests` | 8 | 989.68 | 16.37% | 0.0% |
| `sse_starlette-3.3.4/sse_starlette` | 3 | 307.12 | 26.73% | 46.64% |
| `sse_starlette-3.3.4` | 3 | 10.88 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `sse_starlette-3.3.4/sse_starlette/event.py` -> **99.417%** Exposure
- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **40.5014%** Exposure
### Highest State Flux (Mutation/Volatility)
- `sse_starlette-3.3.4/sse_starlette/event.py` -> **99.9556%** Exposure
- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **99.6189%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sse_starlette-3.3.4/tests/test_issue167.py` -> **6** Orphaned Functions | **20** Duplicates
- `sse_starlette-3.3.4/tests/test_sse.py` -> **13** Orphaned Functions | **8** Duplicates
- `sse_starlette-3.3.4/tests/test_issue132.py` -> **9** Orphaned Functions | **2** Duplicates
- `sse_starlette-3.3.4/tests/test_event.py` -> **6** Orphaned Functions | **0** Duplicates
- `sse_starlette-3.3.4/sse_starlette/event.py` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`sse_starlette-3.3.4/sse_starlette/sse.py`** -> AI Confidence: **99.24%**
2. **`sse_starlette-3.3.4/tests/test_sse.py`** -> AI Confidence: **99.18%**
3. **`sse_starlette-3.3.4/sse_starlette/event.py`** -> AI Confidence: **99.06%**
4. **`sse_starlette-3.3.4/tests/anyio_compat.py`** -> AI Confidence: **98.96%**
5. **`sse_starlette-3.3.4/tests/test_issue132.py`** -> AI Confidence: **98.96%**
6. **`sse_starlette-3.3.4/tests/test_multi_loop.py`** -> AI Confidence: **98.96%**
7. **`sse_starlette-3.3.4/tests/test_issue167.py`** -> AI Confidence: **98.88%**
8. **`sse_starlette-3.3.4/tests/test_issue152.py`** -> AI Confidence: **98.86%**
9. **`sse_starlette-3.3.4/sse_starlette/__init__.py`** -> AI Confidence: **98.84%**
10. **`sse_starlette-3.3.4/tests/__init__.py`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `57` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `sse_starlette-3.3.4/sse_starlette/sse.py` (PYTHON) -> Cumulative Risk: **596.84**
- **Archetype:** `file_cluster_13` (Distance: 12.448 IQR)
- **Magnitude:** 242.6 | **LOC:** 438 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9995%), State Flux (99.6189%), Verification (80.0%)
- **Heaviest Functions:** `_stream_response` (Impact: 44.9), `_shutdown_watcher` (Impact: 19.4), `__call__` (Impact: 10.2)

### 2. `sse_starlette-3.3.4/sse_starlette/event.py` (PYTHON) -> Cumulative Risk: **504.88**
- **Archetype:** `file_cluster_16` (Distance: 11.332 IQR)
- **Magnitude:** 51.44 | **LOC:** 97 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9556%), Tech Debt (99.417%), Safety Score (76.4087%)
- **Heaviest Functions:** `encode` (Impact: 17.0), `ensure_bytes` (Impact: 7.4), `__init__` (Impact: 1.4)

### 3. `sse_starlette-3.3.4/tests/test_issue167.py` (PYTHON) -> Cumulative Risk: **317.16**
- **Archetype:** `file_cluster_4` (Distance: 11.215 IQR)
- **Magnitude:** 279.7 | **LOC:** 286 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Safety Score (30.7623%)
- **Heaviest Functions:** `test_shutdownGracePeriod_whenGeneratorEx` (Impact: 25.1), `test_noShutdownEvent_whenShutdownDetecte` (Impact: 14.2), `mock_send` (Impact: 10.7)

### 4. `sse_starlette-3.3.4/tests/test_sse.py` (PYTHON) -> Cumulative Risk: **302.09**
- **Archetype:** `file_cluster_4` (Distance: 10.871 IQR)
- **Magnitude:** 227.44 | **LOC:** 335 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), Stability (50.0%), Cognitive Load (27.0735%)
- **Heaviest Functions:** `app` (Impact: 13.6), `stream_numbers` (Impact: 12.8), `test_send_whenTimeoutOccurs_thenRaisesSe` (Impact: 11.4)

### 5. `sse_starlette-3.3.4/tests/test_multi_loop.py` (PYTHON) -> Cumulative Risk: **300.56**
- **Archetype:** `file_cluster_4` (Distance: 12.436 IQR)
- **Magnitude:** 231.8 | **LOC:** 280 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Cognitive Load (24.9925%)
- **Heaviest Functions:** `test_same_thread_shares_state` (Impact: 55.3), `get_state` (Impact: 2.1)

### 6. `sse_starlette-3.3.4/tests/test_issue152.py` (PYTHON) -> Cumulative Risk: **295.3**
- **Archetype:** `file_cluster_4` (Distance: 11.739 IQR)
- **Magnitude:** 113.98 | **LOC:** 212 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Cognitive Load (23.7741%)
- **Heaviest Functions:** `test_single_watcher_per_thread` (Impact: 48.5), `tracking_watcher` (Impact: 2.2)

### 7. `sse_starlette-3.3.4/tests/test_issue132.py` (PYTHON) -> Cumulative Risk: **276.91**
- **Archetype:** `file_cluster_8` (Distance: 11.494 IQR)
- **Magnitude:** 89.42 | **LOC:** 171 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9164%), Stability (50.0%), Cognitive Load (11.9795%)
- **Heaviest Functions:** `test_detects_uvicorn_server_should_exit` (Impact: 9.3), `test_fallback_when_no_uvicorn_server` (Impact: 9.1), `test_detects_appstatus_should_exit` (Impact: 7.0)

### 8. `sse_starlette-3.3.4/tests/anyio_compat.py` (PYTHON) -> Cumulative Risk: **225.63**
- **Archetype:** `file_cluster_0` (Distance: 15.052 IQR)
- **Magnitude:** 11.48 | **LOC:** 33 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (37.7541%), Dead Code (23.1475%)
- **Heaviest Functions:** `collapse_excgroups` (Impact: 9.1)

### 9. `sse_starlette-3.3.4/tests/test_event.py` (PYTHON) -> Cumulative Risk: **160.91**
- **Archetype:** `file_cluster_8` (Distance: 9.015 IQR)
- **Magnitude:** 25.34 | **LOC:** 132 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Api Exposure (7.9582%), Cognitive Load (2.9558%)
- **Heaviest Functions:** `test_server_sent_event` (Impact: 5.5), `test_retry_is_int` (Impact: 3.8), `test_multiline_data` (Impact: 2.2)

### 10. `sse_starlette-3.3.4/sse_starlette/__init__.py` (PYTHON) -> Cumulative Risk: **105.31**
- **Archetype:** `file_cluster_13` (Distance: 6.381 IQR)
- **Magnitude:** 13.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (26.6667%), Documentation (21.1038%), Cognitive Load (5.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sse_starlette-3.3.4/tests/test_issue167.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.215 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.667 IQR)
- **Top Global Matches:** file_cluster_4: 11.215, file_cluster_0: 11.915, file_cluster_13: 11.938
- **Magnitude:** 279.7 | **LOC:** 286 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.6231%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_shutdownGracePeriod_whenGeneratorEx` (Impact: 25.1)
  * `test_noShutdownEvent_whenShutdownDetecte` (Impact: 14.2)
    * *Intent:* # If force-cancel worked, run_response should have finished # and we should be able to cancel the ou...
  * `mock_send` (Impact: 10.7)
  * `test_shutdownEvent_whenShutdownDetected_` (Impact: 10.1)
  * `gen` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 92`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `duplicate_logic: 20`, `orphaned_logic: 6`
* *Architecture:* `api: 27`, `concurrency: 95`, `import: 4`
* *Defense:* `safety: 19`, `doc: 16`, `test: 23`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` anyio, tests.anyio_compat, sse_starlette.sse, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/sse_starlette/sse.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.448 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.59 IQR)
- **Top Global Matches:** file_cluster_13: 12.448, file_cluster_4: 12.517, file_cluster_16: 12.612
- **Magnitude:** 242.6 | **LOC:** 438 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5238%), Tech Debt (40.5014%)
**Top Internal Functions/Classes:**
  * `_stream_response` (Impact: 44.9)
    * *Intent:* # "The no-store response directive indicates that any caches of any kind (private or shared) # shoul...
  * `_shutdown_watcher` (Impact: 19.4)
  * `__call__` (Impact: 10.2)
  * `_get_uvicorn_server` (Impact: 7.5)
  * `_ensure_watcher_started_on_this_loop` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 79`, `args: 21`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `concurrency: 56`, `import: 15`
* *Defense:* `safety: 18`, `doc: 30`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 200.615
  * `Choke Point (Betweenness):` 0.032051 | `Ripple Effect (Closeness):` 0.461538
  * `Imports (Out-Degree: 1):` asyncio, sse_starlette.event, dataclasses, threading, uvicorn.main, starlette.concurrency, starlette.responses, logging...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `sse_starlette-3.3.4/tests/test_multi_loop.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.436 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.498 IQR)
- **Top Global Matches:** file_cluster_4: 12.436, file_cluster_13: 12.999, file_cluster_0: 13.12
- **Magnitude:** 231.8 | **LOC:** 280 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9925%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_same_thread_shares_state` (Impact: 55.3)
  * `get_state` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 62`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 13`, `orphaned_logic: 1`
* *Architecture:* `api: 18`, `concurrency: 140`, `import: 6`
* *Defense:* `safety: 31`, `doc: 24`, `test: 27`, `sync_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` asyncio, unittest.mock, pytest, threading, typing, sse_starlette.sse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/test_sse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.871 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.506 IQR)
- **Top Global Matches:** file_cluster_4: 10.871, file_cluster_13: 11.05, file_cluster_0: 11.156
- **Magnitude:** 227.44 | **LOC:** 335 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.0735%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `app` (Impact: 13.6)
  * `stream_numbers` (Impact: 12.8)
    * *Intent:* # Arrange async def app(scope, receive, send): # Create bounded memory channel for producer-consumer...
  * `test_send_whenTimeoutOccurs_thenRaisesSe` (Impact: 11.4)
    * *Intent:* # https://www.python-httpx.org/async/#streaming-responses tg.start_soon(httpx_client.get, "/endless"...
  * `app` (Impact: 10.8)
    * *Intent:* # Arrange
  * `test_ping_whenConcurrentWithEvents_thenR` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 103`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `duplicate_logic: 8`, `orphaned_logic: 13`
* *Architecture:* `api: 32`, `concurrency: 46`, `import: 12`
* *Defense:* `safety: 22`, `doc: 2`, `test: 49`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` asyncio, pytest, math, logging, starlette.background, anyio, anyio.lowlevel, sse_starlette.sse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/test_issue152.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.739 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.911 IQR)
- **Top Global Matches:** file_cluster_4: 11.739, file_cluster_13: 11.86, file_cluster_0: 12.214
- **Magnitude:** 113.98 | **LOC:** 212 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.7741%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_single_watcher_per_thread` (Impact: 48.5)
    * *Intent:* # Watcher polls every 0.5s, so we need >0.5s for it to detect shutdown.
  * `tracking_watcher` (Impact: 2.2)
    * *Intent:* """ Issue #152 regression: Only one watcher should be started per thread. In real ASGI apps: - Each ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 47`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 9`, `concurrency: 45`, `import: 13`
* *Defense:* `safety: 17`, `doc: 16`, `test: 18`, `sync_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` anyio, asyncio, sse_starlette.sse, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/test_issue132.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.494 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.309 IQR)
- **Top Global Matches:** file_cluster_8: 11.494, file_cluster_13: 11.554, file_cluster_4: 11.64
- **Magnitude:** 89.42 | **LOC:** 171 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9795%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_detects_uvicorn_server_should_exit` (Impact: 9.3)
  * `test_fallback_when_no_uvicorn_server` (Impact: 9.1)
    * *Intent:* # Wait for event to be signaled (with timeout) with anyio.fail_after(2): await event.wait() # AppSta...
  * `test_detects_appstatus_should_exit` (Impact: 7.0)
  * `test_returns_server_when_handler_is_boun` (Impact: 4.1)
  * `test_returns_none_when_self_lacks_should` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 44`, `args: 13`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `duplicate_logic: 2`, `orphaned_logic: 9`
* *Architecture:* `api: 14`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 9`, `doc: 24`, `test: 32`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest.mock, pytest, anyio, signal, sse_starlette.sse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/sse_starlette/event.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.332 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.914 IQR)
- **Top Global Matches:** file_cluster_16: 11.332, file_cluster_13: 11.36, file_cluster_8: 11.608
- **Magnitude:** 51.44 | **LOC:** 97 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.6561%), Tech Debt (99.417%)
**Top Internal Functions/Classes:**
  * `encode` (Impact: 17.0)
  * `ensure_bytes` (Impact: 7.4)
  * `__init__` (Impact: 1.4)
  * `__init__` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 18`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 265.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.378698
  * `Imports (Out-Degree: 0):` io, re, json, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sse_starlette-3.3.4/tests/test_event.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.015 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.437 IQR)
- **Top Global Matches:** file_cluster_8: 9.015, file_cluster_0: 9.58, file_cluster_13: 9.865
- **Magnitude:** 25.34 | **LOC:** 132 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_server_sent_event` (Impact: 5.5)
  * `test_retry_is_int` (Impact: 3.8)
  * `test_multiline_data` (Impact: 2.2)
  * `test_custom_sep` (Impact: 1.9)
  * `test_json_server_sent_event` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 18`, `args: 6`, `func_start: 6`
* *Risk/State:* `orphaned_logic: 6`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 9`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sse_starlette.event, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/sse_starlette/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.381 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.094 IQR)
- **Top Global Matches:** file_cluster_13: 6.381, file_cluster_8: 6.568, file_cluster_7: 7.62
- **Magnitude:** 13.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sse_starlette.event, sse_starlette.sse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/tests/anyio_compat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.052 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.606 IQR)
- **Top Global Matches:** file_cluster_0: 15.052, file_cluster_13: 15.106, file_cluster_11: 15.465
- **Magnitude:** 11.48 | **LOC:** 33 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.576%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `collapse_excgroups` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 76.919
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.153846
  * `Imports (Out-Degree: 0):` typing, contextlib, exceptiongroup, sys
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `sse_starlette-3.3.4/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 8.88 | **LOC:** 444 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/AUTHORS` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sse_starlette-3.3.4/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `sse_starlette-3.3.4/tests/anyio_compat.py` (PYTHON) | Magnitude: 11.48 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, branch: 6, safety: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `sse_starlette-3.3.4/sse_starlette/sse.py` (PYTHON) | Magnitude: 242.6 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 228, structural_boundaries: 79, concurrency: 56, branch: 55
- `sse_starlette-3.3.4/sse_starlette/__init__.py` (PYTHON) | Magnitude: 13.08 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, encapsulation: 2, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `sse_starlette-3.3.4/sse_starlette/event.py` (PYTHON) | Magnitude: 51.44 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, state_mutation: 18, structural_boundaries: 16, branch: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `sse_starlette-3.3.4/tests/test_issue152.py` (PYTHON) | Magnitude: 113.98 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 47, concurrency: 45, encapsulation: 26
- `sse_starlette-3.3.4/tests/test_sse.py` (PYTHON) | Magnitude: 227.44 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 103, test: 49, concurrency: 46
- `sse_starlette-3.3.4/tests/test_multi_loop.py` (PYTHON) | Magnitude: 231.8 | Delta: **0.563 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 161, concurrency: 140, structural_boundaries: 62, safety: 31
- `sse_starlette-3.3.4/tests/test_issue167.py` (PYTHON) | Magnitude: 279.7 | Delta: **0.7 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 188, concurrency: 95, structural_boundaries: 92, branch: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `sse_starlette-3.3.4/tests/test_issue132.py` (PYTHON) | Magnitude: 89.42 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 44, test: 32, doc: 24
- `sse_starlette-3.3.4/tests/test_event.py` (PYTHON) | Magnitude: 25.34 | Delta: **0.565 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, test: 21, structural_boundaries: 18, explicit_casts: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **Severity: 3.193** (Bridge: 0.0321 * Flux: 99.6189%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `sse_starlette-3.3.4/sse_starlette/event.py` -> **Severity: 28.936** (Embedded: 0.3787 * Error Risk: 76.4087%)
- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **Severity: 27.186** (Embedded: 0.4615 * Error Risk: 58.904%)
- `sse_starlette-3.3.4/tests/anyio_compat.py` -> **Severity: 5.808** (Embedded: 0.1538 * Error Risk: 37.7541%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sse_starlette-3.3.4/sse_starlette/event.py` -> **Severity: 13021.753** (Blast Radius: 265.11 * Doc Risk: 49.1183%)
- `sse_starlette-3.3.4/sse_starlette/sse.py` -> **Severity: 3240.715** (Blast Radius: 200.615 * Doc Risk: 16.1539%)
- `sse_starlette-3.3.4/sse_starlette/__init__.py` -> **Severity: 877.454** (Blast Radius: 41.578 * Doc Risk: 21.1038%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
