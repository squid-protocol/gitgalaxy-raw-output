# ARCHITECTURAL_BRIEF: httpx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/httpx` |
| **Timestamp** | `2026-08-07T05:23:14.674792+00:00` |
| **Scan Duration** | `0.38s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 58 malicious artifacts.

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
| Total Artifacts | 70 |
| Analyzed Artifacts (Scanned) | 61 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 11963 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2411 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2534 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0233 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 58 | 11963 | 95.1% |
| MARKDOWN | 3 | 0 | 4.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.469`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 29 | 47.5% |
| file_cluster_13 | 14 | 23.0% |
| file_cluster_16 | 6 | 9.8% |
| file_cluster_4 | 5 | 8.2% |
| file_cluster_0 | 4 | 6.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 4.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.json`: 1x Excluded (Massive Static Asset Blob: 9747 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 1.4 | 73.2 | 15.1 | 5.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.5 | 23.6 | 4.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.8 | 6.2 | 7.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 29.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 6.7 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.8 | 19.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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

- `_parse_header_links` (@ `httpx-0.28.1/httpx/_models.py`) -> Impact: **518.1** | LOC: 1083
- `_send_single_request` (@ `httpx-0.28.1/httpx/_client.py`) -> Impact: **117.3** | LOC: 648
- `urlparse` (@ `httpx-0.28.1/httpx/_urlparse.py`) -> Impact: **96.7** | LOC: 133
- `get_lexer_for_response` (@ `httpx-0.28.1/httpx/_main.py`) -> Impact: **92.4** | LOC: 168
- `test_response_set_explicit_encoding` (@ `httpx-0.28.1/tests/models/test_responses.py`) -> Impact: **88.2** | LOC: 586
  * *Intent:* """ headers = {"Content-Type": "image/png"} response = httpx.Response( 200, content=b"xyz", headers=headers, ) assert response.text == "xyz" assert re...
- `__repr__` (@ `httpx-0.28.1/httpx/_urls.py`) -> Impact: **77.2** | LOC: 193
  * *Intent:* """ return self._uri_reference.host.encode("ascii") @property def port(self) -> int | None: """
- `test_query_requiring_percent_encoding` (@ `httpx-0.28.1/tests/models/test_url.py`) -> Impact: **76.9** | LOC: 221
- `encode_host` (@ `httpx-0.28.1/httpx/_urlparse.py`) -> Impact: **74.2** | LOC: 123
  * *Intent:* # The parsed ASCII bytestrings are our canonical form. # All properties of the URL are derived from these. return ParseResult( parsed_scheme, parsed_u...
- `unquote` (@ `httpx-0.28.1/httpx/_utils.py`) -> Impact: **63.5** | LOC: 110
- `redirects` (@ `httpx-0.28.1/tests/client/test_redirects.py`) -> Impact: **57.3** | LOC: 106

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `httpx-0.28.1/httpx` | 17 | 3215.82 | 24.52% | 34.53% |
| `httpx-0.28.1/tests/client` | 11 | 1581.56 | 10.88% | 0.0% |
| `httpx-0.28.1/tests` | 17 | 1161.18 | 9.69% | 0.0% |
| `httpx-0.28.1/tests/models` | 8 | 852.76 | 6.05% | 0.0% |
| `httpx-0.28.1/httpx/_transports` | 5 | 299.7 | 25.81% | 56.93% |
| `httpx-0.28.1` | 3 | 26.58 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `httpx-0.28.1/httpx/_auth.py` -> **100.0%** Exposure
- `httpx-0.28.1/httpx/_decoders.py` -> **100.0%** Exposure
- `httpx-0.28.1/httpx/_exceptions.py` -> **100.0%** Exposure
- `httpx-0.28.1/httpx/_content.py` -> **99.9986%** Exposure
- `httpx-0.28.1/httpx/_config.py` -> **99.9844%** Exposure
### Highest State Flux (Mutation/Volatility)
- `httpx-0.28.1/httpx/_config.py` -> **99.9999%** Exposure
- `httpx-0.28.1/httpx/_decoders.py` -> **99.9872%** Exposure
- `httpx-0.28.1/httpx/_models.py` -> **99.9135%** Exposure
- `httpx-0.28.1/httpx/_utils.py` -> **99.6029%** Exposure
- `httpx-0.28.1/httpx/_multipart.py` -> **98.883%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `httpx-0.28.1/tests/client/test_auth.py` -> **36** Orphaned Functions | **9** Duplicates
- `httpx-0.28.1/tests/client/test_client.py` -> **33** Orphaned Functions | **12** Duplicates
- `httpx-0.28.1/tests/models/test_url.py` -> **39** Orphaned Functions | **0** Duplicates
- `httpx-0.28.1/tests/client/test_async_client.py` -> **25** Orphaned Functions | **13** Duplicates
- `httpx-0.28.1/httpx/_decoders.py` -> **0** Orphaned Functions | **31** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`httpx-0.28.1/httpx/_config.py`** -> AI Confidence: **99.31%**
2. **`httpx-0.28.1/httpx/_main.py`** -> AI Confidence: **99.31%**
3. **`httpx-0.28.1/httpx/_models.py`** -> AI Confidence: **99.31%**
4. **`httpx-0.28.1/httpx/_utils.py`** -> AI Confidence: **99.31%**
5. **`httpx-0.28.1/httpx/__version__.py`** -> AI Confidence: **99.29%**
6. **`httpx-0.28.1/httpx/_multipart.py`** -> AI Confidence: **99.23%**
7. **`httpx-0.28.1/httpx/_urlparse.py`** -> AI Confidence: **99.22%**
8. **`httpx-0.28.1/httpx/_transports/asgi.py`** -> AI Confidence: **99.18%**
9. **`httpx-0.28.1/httpx/_auth.py`** -> AI Confidence: **99.16%**
10. **`httpx-0.28.1/httpx/_client.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `250` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `httpx-0.28.1/httpx/_transports/asgi.py` (PYTHON) -> Cumulative Risk: **637.74**
- **Archetype:** `file_cluster_13` (Distance: 11.263 IQR)
- **Magnitude:** 89.92 | **LOC:** 188 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9976%), State Flux (92.7411%), Tech Debt (90.3904%)
- **Heaviest Functions:** `send` (Impact: 9.5), `receive` (Impact: 6.7), `is_running_trio` (Impact: 5.8)

### 2. `httpx-0.28.1/httpx/_content.py` (PYTHON) -> Cumulative Risk: **623.37**
- **Archetype:** `file_cluster_13` (Distance: 11.167 IQR)
- **Magnitude:** 100.36 | **LOC:** 241 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9986%), Concurrency (93.8172%), State Flux (90.4115%)
- **Heaviest Functions:** `__aiter__` (Impact: 14.8), `__iter__` (Impact: 12.9), `encode_text` (Impact: 2.7)

### 3. `httpx-0.28.1/httpx/_models.py` (PYTHON) -> Cumulative Risk: **596.11**
- **Archetype:** `file_cluster_16` (Distance: 13.332 IQR)
- **Magnitude:** 904.96 | **LOC:** 1278 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9135%), Concurrency (99.2627%), Verification (80.0%)
- **Heaviest Functions:** `_parse_header_links` (Impact: 518.1), `_normalize_header_value` (Impact: 9.1), `_normalize_header_key` (Impact: 7.1)

### 4. `httpx-0.28.1/httpx/_transports/default.py` (PYTHON) -> Cumulative Risk: **555.43**
- **Archetype:** `file_cluster_13` (Distance: 10.04 IQR)
- **Magnitude:** 108.48 | **LOC:** 407 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.6592%), Verification (80.0%), Concurrency (70.5133%)
- **Heaviest Functions:** `map_httpcore_exceptions` (Impact: 15.0), `__aiter__` (Impact: 6.2), `__iter__` (Impact: 5.4)

### 5. `httpx-0.28.1/httpx/_config.py` (PYTHON) -> Cumulative Risk: **530.41**
- **Archetype:** `file_cluster_13` (Distance: 12.632 IQR)
- **Magnitude:** 137.54 | **LOC:** 249 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9844%), Safety Score (71.1377%)
- **Heaviest Functions:** `__repr__` (Impact: 12.6), `__eq__` (Impact: 9.1), `__eq__` (Impact: 7.3)

### 6. `httpx-0.28.1/httpx/_decoders.py` (PYTHON) -> Cumulative Risk: **525.71**
- **Archetype:** `file_cluster_16` (Distance: 13.029 IQR)
- **Magnitude:** 259.24 | **LOC:** 394 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9872%), Documentation (84.0612%)
- **Heaviest Functions:** `decode` (Impact: 16.7), `decode` (Impact: 16.7), `decode` (Impact: 15.7)

### 7. `httpx-0.28.1/httpx/_client.py` (PYTHON) -> Cumulative Risk: **480.32**
- **Archetype:** `file_cluster_8` (Distance: 11.302 IQR)
- **Magnitude:** 599.38 | **LOC:** 2020 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (93.4394%), Tech Debt (73.5288%), State Flux (69.3436%)
- **Heaviest Functions:** `_send_single_request` (Impact: 117.3), `_redirect_url` (Impact: 15.3), `_redirect_method` (Impact: 15.0)

### 8. `httpx-0.28.1/httpx/_urls.py` (PYTHON) -> Cumulative Risk: **472.51**
- **Archetype:** `file_cluster_16` (Distance: 12.279 IQR)
- **Magnitude:** 247.14 | **LOC:** 642 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (84.3994%), Verification (80.0%), Safety Score (67.6984%)
- **Heaviest Functions:** `__repr__` (Impact: 77.2), `__init__` (Impact: 34.4), `raw_path` (Impact: 5.5)

### 9. `httpx-0.28.1/httpx/_transports/wsgi.py` (PYTHON) -> Cumulative Risk: **456.85**
- **Archetype:** `file_cluster_13` (Distance: 9.492 IQR)
- **Magnitude:** 54.38 | **LOC:** 150 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.614%), State Flux (75.4777%), Documentation (59.1226%)
- **Heaviest Functions:** `handle_request` (Impact: 18.5), `_skip_leading_empty_chunks` (Impact: 6.3), `__iter__` (Impact: 3.6)

### 10. `httpx-0.28.1/httpx/_utils.py` (PYTHON) -> Cumulative Risk: **444.78**
- **Archetype:** `file_cluster_13` (Distance: 12.143 IQR)
- **Magnitude:** 158.96 | **LOC:** 243 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6029%), Documentation (92.3575%), Safety Score (64.9009%)
- **Heaviest Functions:** `unquote` (Impact: 63.5), `get_environment_proxies` (Impact: 26.6), `primitive_value_to_str` (Impact: 8.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `httpx-0.28.1/httpx/_models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.332 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.219 IQR)
- **Top Global Matches:** file_cluster_16: 13.332, file_cluster_13: 13.39, file_cluster_4: 13.43
- **Magnitude:** 904.96 | **LOC:** 1278 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.765%), Tech Debt (13.5262%)
**Top Internal Functions/Classes:**
  * `_parse_header_links` (Impact: 518.1)
  * `_normalize_header_value` (Impact: 9.1)
  * `_normalize_header_key` (Impact: 7.1)
  * `_is_known_encoding` (Impact: 4.4)
    * *Intent:* """ Return `True` if `encoding` is a known codec. """
  * `info` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 222`, `args: 95`, `func_start: 95`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 199`, `duplicate_logic: 2`
* *Architecture:* `api: 64`, `concurrency: 74`, `import: 18`
* *Defense:* `safety: 56`, `doc: 104`, `test: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 141.663
  * `Choke Point (Betweenness):` 0.035122 | `Ripple Effect (Closeness):` 0.237255
  * `Imports (Out-Degree: 8):` http.cookiejar, email.message, datetime, json, codecs, urllib.request, re, ._exceptions...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_client.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.302 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.921 IQR)
- **Top Global Matches:** file_cluster_8: 11.302, file_cluster_16: 11.311, file_cluster_13: 11.392
- **Magnitude:** 599.38 | **LOC:** 2020 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.2127%), Tech Debt (73.5288%)
**Top Internal Functions/Classes:**
  * `_send_single_request` (Impact: 117.3)
  * `_redirect_url` (Impact: 15.3)
  * `_redirect_method` (Impact: 15.0)
  * `_redirect_headers` (Impact: 12.4)
  * `_build_auth` (Impact: 10.9)
    * *Intent:* # To merge URLs we always append to the base URL. To get this # behaviour correct we always ensure t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 253`, `args: 81`, `func_start: 81`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 111`, `duplicate_logic: 20`
* *Architecture:* `io: 8`, `api: 52`, `concurrency: 82`, `import: 24`
* *Defense:* `safety: 44`, `doc: 98`, `test: 4`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.506
  * `Choke Point (Betweenness):` 0.004388 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 12):` ._models, ._status_codes, ._types, __future__, ssl, .__version__, warnings, contextlib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/client/test_async_client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.612 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.341 IQR)
- **Top Global Matches:** file_cluster_4: 11.612, file_cluster_0: 11.949, file_cluster_13: 12.421
- **Magnitude:** 385.64 | **LOC:** 376 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_raise_for_status` (Impact: 12.7)
  * `test_client_closed_state_using_implicit_` (Impact: 8.9)
  * `test_access_content_stream_response` (Impact: 8.4)
  * `test_cancellation_during_stream` (Impact: 7.3)
    * *Intent:* """ If any BaseException is raised during streaming the response, then the stream should be closed. ...
  * `test_stream_response` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 160`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 10`, `duplicate_logic: 13`, `orphaned_logic: 25`
* *Architecture:* `io: 49`, `api: 37`, `concurrency: 164`, `import: 5`
* *Defense:* `safety: 45`, `doc: 2`, `test: 107`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, typing, pytest, httpx, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/client/test_auth.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.23 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.66 IQR)
- **Top Global Matches:** file_cluster_4: 12.23, file_cluster_0: 12.24, file_cluster_13: 12.519
- **Magnitude:** 364.6 | **LOC:** 773 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9891%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_auth_invalid_type` (Impact: 10.8)
  * `challenge_send` (Impact: 10.0)
  * `test_digest_auth_no_specified_qop` (Impact: 9.4)
  * `test_basic_auth_with_stream` (Impact: 6.8)
  * `test_digest_auth_unavailable_streaming_b` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 234`, `args: 49`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 16`, `duplicate_logic: 9`, `orphaned_logic: 36`
* *Architecture:* `io: 130`, `api: 48`, `concurrency: 92`, `import: 11`
* *Defense:* `safety: 102`, `doc: 30`, `test: 174`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, anyio, urllib.request, sys, threading, typing, pytest, netrc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/models/test_responses.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.832 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.062 IQR)
- **Top Global Matches:** file_cluster_0: 11.832, file_cluster_8: 11.936, file_cluster_4: 11.961
- **Magnitude:** 286.66 | **LOC:** 1038 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.7249%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_response_set_explicit_encoding` (Impact: 88.2)
    * *Intent:* """ headers = {"Content-Type": "image/png"} response = httpx.Response( 200, content=b"xyz", headers=...
  * `test_raise_for_status` (Impact: 20.1)
  * `test_response_content_type_encoding` (Impact: 3.6)
    * *Intent:* """ Use the charset encoding in the Content-Type header if possible. """
  * `test_response_text` (Impact: 2.8)
  * `test_response` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 271`, `args: 78`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `orphaned_logic: 14`
* *Architecture:* `io: 111`, `api: 78`, `concurrency: 48`, `import: 6`
* *Defense:* `safety: 172`, `doc: 16`, `test: 287`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chardet, json, typing, pytest, httpx, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/models/test_url.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.627 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.023 IQR)
- **Top Global Matches:** file_cluster_8: 12.627, file_cluster_0: 12.787, file_cluster_7: 12.989
- **Magnitude:** 266.92 | **LOC:** 864 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.2493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_query_requiring_percent_encoding` (Impact: 76.9)
  * `test_url_copywith_urlencoded_path` (Impact: 7.5)
  * `test_complete_url` (Impact: 7.1)
  * `test_url_percent_escape_host` (Impact: 5.6)
  * `test_param_with_percent_encoded` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 272`, `args: 69`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 39`
* *Architecture:* `io: 98`, `api: 70`, `import: 2`
* *Defense:* `safety: 184`, `doc: 28`, `test: 280`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, httpx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_decoders.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.029 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.073 IQR)
- **Top Global Matches:** file_cluster_16: 13.029, file_cluster_13: 13.064, file_cluster_8: 13.33
- **Magnitude:** 259.24 | **LOC:** 394 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.5735%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `decode` (Impact: 16.7)
  * `decode` (Impact: 16.7)
  * `decode` (Impact: 15.7)
  * `__init__` (Impact: 9.5)
  * `flush` (Impact: 7.6)
    * *Intent:* # The 'brotlicffi' package. self._decompress = self.decompressor.decompress # pragma: no cover else:...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 104`, `args: 31`, `func_start: 31`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 68`, `duplicate_logic: 31`
* *Architecture:* `io: 4`, `api: 33`, `import: 9`
* *Defense:* `safety: 23`, `doc: 24`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.152201
  * `Imports (Out-Degree: 1):` zlib, codecs, ._exceptions, typing, zstandard, io, brotli, __future__...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_urls.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.279 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.781 IQR)
- **Top Global Matches:** file_cluster_16: 12.279, file_cluster_13: 12.437, file_cluster_0: 12.483
- **Magnitude:** 247.14 | **LOC:** 642 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.6211%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 77.2)
    * *Intent:* """ return self._uri_reference.host.encode("ascii") @property def port(self) -> int | None: """
  * `__init__` (Impact: 34.4)
  * `raw_path` (Impact: 5.5)
  * `host` (Impact: 3.9)
  * `is_absolute_url` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 121`, `args: 50`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 26`
* *Architecture:* `io: 1`, `api: 42`, `import: 10`
* *Defense:* `safety: 13`, `doc: 60`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 88.623
  * `Choke Point (Betweenness):` 0.006422 | `Ripple Effect (Closeness):` 0.196748
  * `Imports (Out-Degree: 3):` warnings, ._urlparse, collections, typing, ._types, idna, urllib.parse, ._utils...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/test_content.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.386 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.794 IQR)
- **Top Global Matches:** file_cluster_0: 12.386, file_cluster_4: 12.391, file_cluster_17: 12.471
- **Magnitude:** 243.08 | **LOC:** 519 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.35%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_aiterator_content` (Impact: 13.7)
  * `test_allow_nan_false` (Impact: 9.3)
  * `test_bytes_content` (Impact: 9.2)
  * `test_response_aiterator_content` (Impact: 8.8)
  * `test_iterator_content` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 143`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `duplicate_logic: 4`, `orphaned_logic: 27`
* *Architecture:* `io: 36`, `api: 30`, `concurrency: 53`, `import: 4`
* *Defense:* `safety: 150`, `test: 162`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, httpx, io, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_urlparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.586 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.411 IQR)
- **Top Global Matches:** file_cluster_8: 10.586, file_cluster_13: 10.788, file_cluster_16: 10.899
- **Magnitude:** 241.3 | **LOC:** 528 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.5388%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `urlparse` (Impact: 96.7)
  * `encode_host` (Impact: 74.2)
    * *Intent:* # The parsed ASCII bytestrings are our canonical form. # All properties of the URL are derived from ...
  * `quote` (Impact: 15.0)
  * `percent_encoded` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 28`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 11`, `doc: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.739
  * `Choke Point (Betweenness):` 0.003578 | `Ripple Effect (Closeness):` 0.144048
  * `Imports (Out-Degree: 1):` re, ._exceptions, typing, idna, ipaddress, __future__
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/client/test_client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.114 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.461 IQR)
- **Top Global Matches:** file_cluster_8: 12.114, file_cluster_13: 12.145, file_cluster_0: 12.199
- **Magnitude:** 238.0 | **LOC:** 463 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9394%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_raise_for_status` (Impact: 11.0)
  * `test_client_closed_state_using_implicit_` (Impact: 7.9)
  * `test_stream_iterator` (Impact: 7.4)
  * `test_raw_iterator` (Impact: 7.4)
  * `test_cannot_stream_async_request` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 170`, `args: 49`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 12`, `duplicate_logic: 12`, `orphaned_logic: 33`
* *Architecture:* `io: 62`, `api: 45`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 76`, `doc: 2`, `test: 121`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chardet, datetime, typing, pytest, httpx, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/client/test_redirects.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.59 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.273 IQR)
- **Top Global Matches:** file_cluster_8: 11.59, file_cluster_0: 11.837, file_cluster_13: 11.981
- **Magnitude:** 205.48 | **LOC:** 448 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `redirects` (Impact: 57.3)
  * `cookie_sessions` (Impact: 13.6)
  * `test_async_too_many_redirects` (Impact: 6.3)
  * `test_async_invalid_redirect` (Impact: 6.3)
  * `test_async_next_request` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 147`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 29`
* *Architecture:* `io: 127`, `api: 33`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 78`, `doc: 6`, `test: 116`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, httpx, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/test_asgi.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.976 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.966 IQR)
- **Top Global Matches:** file_cluster_4: 10.976, file_cluster_0: 11.316, file_cluster_8: 11.49
- **Magnitude:** 187.54 | **LOC:** 225 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.275%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_asgi_disconnect_after_response_comp` (Impact: 7.6)
  * `test_asgi_exc` (Impact: 6.2)
  * `test_asgi_exc_after_response` (Impact: 6.2)
  * `read_body` (Impact: 5.1)
  * `test_asgi_headers` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 108`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 12`
* *Architecture:* `io: 30`, `api: 20`, `concurrency: 78`, `import: 3`
* *Defense:* `safety: 19`, `doc: 2`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, httpx, json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.143 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.487 IQR)
- **Top Global Matches:** file_cluster_13: 12.143, file_cluster_16: 12.312, file_cluster_11: 12.58
- **Magnitude:** 158.96 | **LOC:** 243 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.4981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unquote` (Impact: 63.5)
  * `get_environment_proxies` (Impact: 26.6)
  * `primitive_value_to_str` (Impact: 8.5)
    * *Intent:* """ Coerce a primitive data type into a string value. Note that we prefer JSON-style 'true'/'false' ...
  * `to_bytes` (Impact: 5.3)
  * `to_str` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 54`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 24`
* *Architecture:* `io: 2`, `api: 18`, `import: 9`
* *Defense:* `safety: 12`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 75.236
  * `Choke Point (Betweenness):` 0.004237 | `Ripple Effect (Closeness):` 0.187597
  * `Imports (Out-Degree: 2):` os, urllib.request, re, typing, ._types, ipaddress, ._urls, __future__
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_main.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.677 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.092 IQR)
- **Top Global Matches:** file_cluster_8: 9.677, file_cluster_13: 9.779, file_cluster_0: 9.854
- **Magnitude:** 157.58 | **LOC:** 507 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1489%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_lexer_for_response` (Impact: 92.4)
  * `print_help` (Impact: 17.6)
  * `main` (Impact: 1.9)
  * `validate_json` (Impact: 1.2)
  * `validate_auth` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 78`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 18`
* *Architecture:* `io: 3`, `api: 15`, `import: 18`
* *Defense:* `safety: 10`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016667
  * `Imports (Out-Degree: 4):` ._models, rich.table, functools, json, pygments.util, ._status_codes, rich.markup, ._exceptions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_multipart.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.644 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.875 IQR)
- **Top Global Matches:** file_cluster_13: 11.644, file_cluster_16: 11.845, file_cluster_17: 11.992
- **Magnitude:** 147.44 | **LOC:** 301 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.9925%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render_headers` (Impact: 49.1)
  * `__init__` (Impact: 16.7)
    * *Intent:* """ A single form field item, within a multipart form field. """
  * `get_content_length` (Impact: 6.0)
  * `__aiter__` (Impact: 4.2)
  * `iter_chunks` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 65`, `args: 21`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 35`
* *Architecture:* `io: 2`, `api: 19`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 17`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.155128
  * `Imports (Out-Degree: 2):` os, mimetypes, pathlib, re, typing, ._types, io, ._utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/client/test_event_hooks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.857 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.785 IQR)
- **Top Global Matches:** file_cluster_4: 9.857, file_cluster_8: 10.19, file_cluster_0: 10.443
- **Magnitude:** 144.6 | **LOC:** 229 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.3273%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_async_event_hooks_raising_exception` (Impact: 6.7)
  * `test_async_event_hooks_with_redirect` (Impact: 6.7)
  * `app` (Impact: 6.4)
  * `test_event_hooks_with_redirect` (Impact: 6.1)
    * *Intent:* """ A redirect request should trigger additional 'request' and 'response' event hooks. """
  * `test_event_hooks_raising_exception` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 39`, `args: 17`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 8`, `duplicate_logic: 10`, `orphaned_logic: 6`
* *Architecture:* `io: 32`, `api: 17`, `concurrency: 54`, `import: 2`
* *Defense:* `safety: 10`, `doc: 4`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, httpx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_config.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.632 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.028 IQR)
- **Top Global Matches:** file_cluster_13: 12.632, file_cluster_16: 12.953, file_cluster_11: 12.962
- **Magnitude:** 137.54 | **LOC:** 249 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.3174%), Tech Debt (99.9844%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 12.6)
  * `__eq__` (Impact: 9.1)
  * `__eq__` (Impact: 7.3)
    * *Intent:* **Parameters:**
  * `raw_auth` (Impact: 5.5)
  * `__repr__` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 45`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 76`, `duplicate_logic: 8`
* *Architecture:* `io: 6`, `api: 10`, `import: 10`
* *Defense:* `safety: 19`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 32.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.15817
  * `Imports (Out-Degree: 3):` os, ._models, warnings, typing, ._types, ._urls, __future__, ssl...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/models/test_requests.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.061 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.377 IQR)
- **Top Global Matches:** file_cluster_0: 12.061, file_cluster_13: 12.115, file_cluster_4: 12.157
- **Magnitude:** 120.56 | **LOC:** 242 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.5862%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_request_async_streaming_content_pic` (Impact: 6.8)
  * `test_request_generator_content_picklable` (Impact: 5.9)
  * `test_aread_and_stream_data` (Impact: 4.5)
    * *Intent:* # Ensure a request may still be streamed if it has been read. # Needed for cases such as authenticat...
  * `test_cannot_access_streaming_content_wit` (Impact: 3.9)
    * *Intent:* # Ensure that streaming requests def streaming_body() -> typing.Iterator[bytes]: # pragma: no cover ...
  * `test_ignore_transfer_encoding_header_if_` (Impact: 2.4)
    * *Intent:* """ `Transfer-Encoding` should be ignored if `Content-Length` has been set explicitly. See https://g...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 82`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 8`, `orphaned_logic: 23`
* *Architecture:* `io: 33`, `api: 31`, `concurrency: 9`, `import: 4`
* *Defense:* `safety: 45`, `doc: 2`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, httpx, pickle, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/tests/test_decoders.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.697 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.551 IQR)
- **Top Global Matches:** file_cluster_0: 10.697, file_cluster_4: 10.761, file_cluster_13: 10.796
- **Magnitude:** 120.38 | **LOC:** 356 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.7965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_text_decoder_known_encoding` (Impact: 6.5)
    * *Intent:* # Streaming `.aiter_text` iteratively. # Note that if we streamed the text *without* having read it ...
  * `test_text_decoder_with_autodetect` (Impact: 6.2)
  * `test_decoding_errors` (Impact: 5.6)
  * `iterator` (Impact: 4.2)
  * `test_zstd_decoding_error` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 73`, `args: 27`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `io: 39`, `api: 27`, `concurrency: 20`, `import: 8`
* *Defense:* `safety: 32`, `doc: 4`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chardet, zlib, typing, pytest, httpx, zstandard, io, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_transports/default.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.04 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.345 IQR)
- **Top Global Matches:** file_cluster_13: 10.04, file_cluster_8: 10.182, file_cluster_16: 10.289
- **Magnitude:** 108.48 | **LOC:** 407 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.5883%), Tech Debt (97.6592%)
**Top Internal Functions/Classes:**
  * `map_httpcore_exceptions` (Impact: 15.0)
  * `__aiter__` (Impact: 6.2)
  * `__iter__` (Impact: 5.4)
  * `aclose` (Impact: 4.2)
  * `close` (Impact: 3.6)
    * *Intent:* # We want to map to the most specific exception we can find. # Eg if `exc` is an `httpcore.ReadTimeo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 75`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`, `duplicate_logic: 8`
* *Architecture:* `io: 7`, `api: 14`, `concurrency: 12`, `import: 19`
* *Defense:* `safety: 20`, `doc: 2`, `test: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.569
  * `Choke Point (Betweenness):` 0.001784 | `Ripple Effect (Closeness):` 0.052083
  * `Imports (Out-Degree: 6):` .._config, socksio, contextlib, .._types, typing, .base, .._urls, httpcore...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/httpx/_content.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.167 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.546 IQR)
- **Top Global Matches:** file_cluster_13: 11.167, file_cluster_16: 11.377, file_cluster_4: 11.404
- **Magnitude:** 100.36 | **LOC:** 241 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.7845%), Tech Debt (99.9986%)
**Top Internal Functions/Classes:**
  * `__aiter__` (Impact: 14.8)
  * `__iter__` (Impact: 12.9)
  * `encode_text` (Impact: 2.7)
  * `encode_json` (Impact: 2.4)
  * `__aiter__` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 63`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 19`, `dead_code: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 15`, `concurrency: 11`, `import: 10`
* *Defense:* `safety: 9`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.204
  * `Choke Point (Betweenness):` 0.000198 | `Ripple Effect (Closeness):` 0.152201
  * `Imports (Out-Degree: 4):` warnings, json, ._exceptions, typing, ._types, urllib.parse, ._utils, __future__...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/test_multipart.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.738 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.582 IQR)
- **Top Global Matches:** file_cluster_8: 9.738, file_cluster_0: 10.032, file_cluster_16: 10.141
- **Magnitude:** 91.14 | **LOC:** 470 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.6172%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multipart_explicit_boundary` (Impact: 15.9)
  * `test_multipart_encode_files_allows_str_c` (Impact: 10.6)
  * `test_multipart_headers_include_content_t` (Impact: 8.6)
    * *Intent:* """ Content-Type from 4th tuple parameter (headers) should override the 3rd parameter (content_type)...
  * `test_multipart_rewinds_files` (Impact: 4.3)
  * `test_multipart_encode_unicode_file_conte` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 85`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 35`, `api: 27`, `import: 6`
* *Defense:* `safety: 38`, `doc: 4`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tempfile, typing, pytest, httpx, io, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpx-0.28.1/httpx/_transports/asgi.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.263 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.936 IQR)
- **Top Global Matches:** file_cluster_13: 11.263, file_cluster_4: 11.273, file_cluster_16: 11.517
- **Magnitude:** 89.92 | **LOC:** 188 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.1667%), Tech Debt (90.3904%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 9.5)
  * `receive` (Impact: 6.7)
  * `is_running_trio` (Impact: 5.8)
  * `create_event` (Impact: 3.9)
  * `__init__` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 50`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 14`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `concurrency: 31`, `import: 10`
* *Defense:* `safety: 13`, `doc: 2`, `test: 6`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.967
  * `Choke Point (Betweenness):` 0.000598 | `Ripple Effect (Closeness):` 0.016667
  * `Imports (Out-Degree: 3):` .._types, typing, .base, trio, __future__, sniffio, asyncio, .._models
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `httpx-0.28.1/tests/test_config.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.236 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.762 IQR)
- **Top Global Matches:** file_cluster_8: 12.236, file_cluster_13: 12.362, file_cluster_0: 12.453
- **Magnitude:** 87.7 | **LOC:** 185 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2064%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_load_ssl_config_verify_non_existing` (Impact: 3.7)
  * `test_load_ssl_config_cert_without_key_ra` (Impact: 3.7)
  * `test_timeout_missing_default` (Impact: 3.6)
  * `test_invalid_proxy_scheme` (Impact: 3.6)
  * `test_load_ssl_with_keylog` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 72`, `args: 27`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 27`
* *Architecture:* `io: 41`, `api: 27`, `import: 6`
* *Defense:* `safety: 38`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathlib, typing, pytest, httpx, ssl, certifi
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `httpx-0.28.1/httpx/__version__.py` (PYTHON) | **Drift Ratio: 1.77x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.799 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.739 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `httpx-0.28.1/tests/test_content.py` (PYTHON) | Magnitude: 243.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 355, test: 162, safety: 150, structural_boundaries: 143
- `httpx-0.28.1/tests/models/test_requests.py` (PYTHON) | Magnitude: 120.56 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 135, structural_boundaries: 82, test: 73, safety: 45
- `httpx-0.28.1/tests/test_decoders.py` (PYTHON) | Magnitude: 120.38 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 73, test: 67, io: 39
- `httpx-0.28.1/tests/models/test_responses.py` (PYTHON) | Magnitude: 286.66 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 653, test: 287, structural_boundaries: 271, safety: 172

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `httpx-0.28.1/httpx/_transports/asgi.py` (PYTHON) | Magnitude: 89.92 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 50, concurrency: 31, encapsulation: 19
- `httpx-0.28.1/httpx/_transports/__init__.py` (PYTHON) | Magnitude: 16.28 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 7, safety_bypasses: 5, import: 5
- `httpx-0.28.1/tests/models/test_whatwg.py` (PYTHON) | Magnitude: 20.34 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, branch: 13, structural_boundaries: 13, test: 9
- `httpx-0.28.1/httpx/_auth.py` (PYTHON) | Magnitude: 82.74 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 64, encapsulation: 53, branch: 37
- `httpx-0.28.1/tests/test_wsgi.py` (PYTHON) | Magnitude: 78.14 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 65, test: 35, io: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `httpx-0.28.1/httpx/_decoders.py` (PYTHON) | Magnitude: 259.24 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, structural_boundaries: 104, state_mutation: 68, branch: 56
- `httpx-0.28.1/httpx/_models.py` (PYTHON) | Magnitude: 904.96 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 819, branch: 239, structural_boundaries: 222, state_mutation: 199
- `httpx-0.28.1/httpx/_urls.py` (PYTHON) | Magnitude: 247.14 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 242, structural_boundaries: 121, encapsulation: 78, branch: 61
- `httpx-0.28.1/httpx/_exceptions.py` (PYTHON) | Magnitude: 73.78 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, doc: 60, structural_boundaries: 51, api: 33
- `httpx-0.28.1/httpx/_transports/base.py` (PYTHON) | Magnitude: 30.64 | Delta: **0.277 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 24, api: 11, generics: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `httpx-0.28.1/tests/client/test_auth.py` (PYTHON) | Magnitude: 364.6 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 437, structural_boundaries: 234, test: 174, io: 130
- `httpx-0.28.1/tests/test_timeouts.py` (PYTHON) | Magnitude: 55.46 | Delta: **0.242 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, io: 18, structural_boundaries: 17, test: 17
- `httpx-0.28.1/tests/client/test_event_hooks.py` (PYTHON) | Magnitude: 144.6 | Delta: **0.333 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, concurrency: 54, structural_boundaries: 39, io: 32
- `httpx-0.28.1/tests/client/test_async_client.py` (PYTHON) | Magnitude: 385.64 | Delta: **0.337 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 204, concurrency: 164, structural_boundaries: 160, test: 107
- `httpx-0.28.1/tests/test_asgi.py` (PYTHON) | Magnitude: 187.54 | Delta: **0.34 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 108, concurrency: 78, test: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `httpx-0.28.1/httpx/_client.py` (PYTHON) | Magnitude: 599.38 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1390, structural_boundaries: 253, encapsulation: 196, branch: 154
- `httpx-0.28.1/httpx/_status_codes.py` (PYTHON) | Magnitude: 38.18 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 24, api: 17, doc: 14
- `httpx-0.28.1/tests/client/test_client.py` (PYTHON) | Magnitude: 238.0 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 274, structural_boundaries: 170, test: 121, safety: 76
- `httpx-0.28.1/tests/test_status_codes.py` (PYTHON) | Magnitude: 17.18 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, test: 13, io: 8, safety: 7
- `httpx-0.28.1/tests/models/test_cookies.py` (PYTHON) | Magnitude: 36.46 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 29, test: 27, safety: 18

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `httpx-0.28.1/httpx/_models.py` -> **Severity: 3.509** (Bridge: 0.0351 * Flux: 99.9135%)
- `httpx-0.28.1/httpx/_urls.py` -> **Severity: 0.542** (Bridge: 0.0064 * Flux: 84.3994%)
- `httpx-0.28.1/httpx/_utils.py` -> **Severity: 0.422** (Bridge: 0.0042 * Flux: 99.6029%)
- `httpx-0.28.1/httpx/_transports/wsgi.py` -> **Severity: 0.322** (Bridge: 0.0043 * Flux: 75.4777%)
- `httpx-0.28.1/httpx/_client.py` -> **Severity: 0.304** (Bridge: 0.0044 * Flux: 69.3436%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `httpx-0.28.1/httpx/_models.py` -> **Severity: 15.615** (Embedded: 0.2373 * Error Risk: 65.8163%)
- `httpx-0.28.1/httpx/_types.py` -> **Severity: 15.452** (Embedded: 0.2241 * Error Risk: 68.9597%)
- `httpx-0.28.1/httpx/_urls.py` -> **Severity: 13.32** (Embedded: 0.1967 * Error Risk: 67.6984%)
- `httpx-0.28.1/httpx/_utils.py` -> **Severity: 12.175** (Embedded: 0.1876 * Error Risk: 64.9009%)
- `httpx-0.28.1/httpx/_config.py` -> **Severity: 11.252** (Embedded: 0.1582 * Error Risk: 71.1377%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `httpx-0.28.1/httpx/_utils.py` -> **Severity: 6948.609** (Blast Radius: 75.236 * Doc Risk: 92.3575%)
- `httpx-0.28.1/httpx/_exceptions.py` -> **Severity: 6038.993** (Blast Radius: 85.842 * Doc Risk: 70.3501%)
- `httpx-0.28.1/httpx/_types.py` -> **Severity: 5841.466** (Blast Radius: 110.783 * Doc Risk: 52.7289%)
- `httpx-0.28.1/httpx/_models.py` -> **Severity: 5053.856** (Blast Radius: 141.663 * Doc Risk: 35.6752%)
- `httpx-0.28.1/httpx/_urls.py` -> **Severity: 3962.99** (Blast Radius: 88.623 * Doc Risk: 44.7174%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
