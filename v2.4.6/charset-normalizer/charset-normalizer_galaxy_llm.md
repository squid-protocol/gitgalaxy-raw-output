# ARCHITECTURAL_BRIEF: charset-normalizer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/charset-normalizer` |
| **Timestamp** | `2026-08-03T21:19:55.217885+00:00` |
| **Scan Duration** | `0.29s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 30 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 59 |
| Analyzed Artifacts (Scanned) | 52 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 5770 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2286 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.163 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 30 | 5770 | 57.7% |
| PLAINTEXT | 19 | 0 | 36.5% |
| MARKDOWN | 3 | 0 | 5.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.34`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 19 | 36.5% |
| file_cluster_13 | 7 | 13.5% |
| file_cluster_16 | 4 | 7.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 42.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 99 exceeds 500 chars)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 264 LOC)
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 356 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 1.5 | 53.8 | 10.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 67.0 | 8.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.5 | 0.3 | 0.0 |
| API Exposure | 0.0 | 8.8 | 3.2 | 2.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 83.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.7 | 9.3 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 34.9 | 2.1 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 30.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py` (Hits: 14)
- `charset_normalizer-3.4.7/noxfile.py` (Hits: 10)
- `charset_normalizer-3.4.7/tests/test_cli.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **constant.py** (`charset_normalizer-3.4.7/src/charset_normalizer/constant.py`) — 8 inbound connections
2. **utils.py** (`charset_normalizer-3.4.7/src/charset_normalizer/utils.py`) — 8 inbound connections
3. **api.py** (`charset_normalizer-3.4.7/src/charset_normalizer/api.py`) — 6 inbound connections
4. **models.py** (`charset_normalizer-3.4.7/src/charset_normalizer/models.py`) — 5 inbound connections
5. **md.py** (`charset_normalizer-3.4.7/src/charset_normalizer/md.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__main__.py** (`charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py`) — 12 outbound dependencies
2. **utils.py** (`charset_normalizer-3.4.7/src/charset_normalizer/utils.py`) — 12 outbound dependencies
3. **cd.py** (`charset_normalizer-3.4.7/src/charset_normalizer/cd.py`) — 10 outbound dependencies
4. **api.py** (`charset_normalizer-3.4.7/src/charset_normalizer/api.py`) — 9 outbound dependencies
5. **__init__.py** (`charset_normalizer-3.4.7/src/charset_normalizer/__init__.py`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `cli_detect` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py`) -> Impact: **577.5** | LOC: 265
- `feed_info` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> Impact: **165.8** | LOC: 75
- `set_logging_handler` (@ `charset_normalizer-3.4.7/src/charset_normalizer/utils.py`) -> Impact: **143.3** | LOC: 67
- `alpha_unicode_split` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cd.py`) -> Impact: **111.5** | LOC: 69
- `append` (@ `charset_normalizer-3.4.7/src/charset_normalizer/models.py`) -> Impact: **104.8** | LOC: 17
  * *Intent:* """ if isinstance(item, int): return self._results[item] if isinstance(item, str): item = iana_name(item, False) for result in self._results: if item ...
- `feed_info` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> Impact: **104.2** | LOC: 45
- `update` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> Impact: **87.7** | LOC: 108
- `encoding_unicode_range` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cd.py`) -> Impact: **55.8** | LOC: 36
  * *Intent:* """ Return associated unicode ranges in a single byte code page. """
- `__call__` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py`) -> Impact: **52.8** | LOC: 17
- `_character_flags` (@ `charset_normalizer-3.4.7/src/charset_normalizer/utils.py`) -> Impact: **49.6** | LOC: 33
  * *Intent:* """Compute all name-based classification flags with a single unicodedata.name() call."""

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `append` (@ `charset_normalizer-3.4.7/src/charset_normalizer/models.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ if isinstance(item, int): return self._results[item] if isinstance(item, str): item = iana_name(item, False) for result in self._results: if item ...
- `coverage` (@ `charset_normalizer-3.4.7/noxfile.py`) -> **O(2^N) [Recursive]**
- `performance` (@ `charset_normalizer-3.4.7/noxfile.py`) -> **O(2^N) [Recursive]**
- `docs` (@ `charset_normalizer-3.4.7/noxfile.py`) -> **O(2^N) [Recursive]**
- `cli_detect` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py`) -> **O(N^6)**
- `output` (@ `charset_normalizer-3.4.7/src/charset_normalizer/models.py`) -> **O(N^6)**
- `set_logging_handler` (@ `charset_normalizer-3.4.7/src/charset_normalizer/utils.py`) -> **O(N^6)**
- `alpha_unicode_split` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cd.py`) -> **O(N^5)**
- `encoding_unicode_range` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cd.py`) -> **O(N^5)**
  * *Intent:* """ Return associated unicode ranges in a single byte code page. """
- `feed_info` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> **O(N^5)**

### Highest Data Gravity (Database Complexity)
- `update` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> DB Complexity: **77**
- `cli_detect` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py`) -> DB Complexity: **25**
- `downstream_niquests` (@ `charset_normalizer-3.4.7/noxfile.py`) -> DB Complexity: **21**
- `feed_info` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> DB Complexity: **19**
- `__call__` (@ `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py`) -> DB Complexity: **18**
- `reset` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> DB Complexity: **13**
- `feed_info` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> DB Complexity: **12**
- `reset` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> DB Complexity: **9**
- `feed_info` (@ `charset_normalizer-3.4.7/src/charset_normalizer/md.py`) -> DB Complexity: **6**
- `test_multiple_file_normalize` (@ `charset_normalizer-3.4.7/tests/test_cli.py`) -> DB Complexity: **6**
  * *Intent:* """Ensure --normalize with multiple files writes each output to the correct path and sets unicode_path on the corresponding result entry (not always o...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `charset_normalizer-3.4.7/src/charset_normalizer` | 10 | 2538.08 | 17.18% | 18.13% |
| `charset_normalizer-3.4.7/src/charset_normalizer/cli` | 2 | 727.88 | 11.54% | 0.0% |
| `charset_normalizer-3.4.7/tests` | 14 | 558.34 | 4.25% | 0.0% |
| `charset_normalizer-3.4.7` | 5 | 144.88 | 5.81% | 13.86% |
| `charset_normalizer-3.4.7/data` | 19 | 22.5 | 0.0% | 0.0% |
| `charset_normalizer-3.4.7/_mypyc_hook` | 2 | 19.16 | 16.61% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/noxfile.py` -> **69.2802%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **67.1031%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/utils.py` -> **14.2065%** Exposure
### Highest State Flux (Mutation/Volatility)
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/_mypyc_hook/backend.py` -> **99.8653%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **98.6697%** Exposure
- `charset_normalizer-3.4.7/setup.py` -> **88.1396%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/api.py` -> **74.0595%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **0** Orphaned Functions | **40** Duplicates
- `charset_normalizer-3.4.7/tests/test_cli.py` -> **15** Orphaned Functions | **0** Duplicates
- `charset_normalizer-3.4.7/tests/test_base_detection.py` -> **12** Orphaned Functions | **0** Duplicates
- `charset_normalizer-3.4.7/noxfile.py` -> **5** Orphaned Functions | **0** Duplicates
- `charset_normalizer-3.4.7/tests/test_detect_legacy.py` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`charset_normalizer-3.4.7/src/charset_normalizer/api.py`** -> AI Confidence: **99.39%**
2. **`charset_normalizer-3.4.7/src/charset_normalizer/cd.py`** -> AI Confidence: **99.31%**
3. **`charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py`** -> AI Confidence: **99.31%**
4. **`charset_normalizer-3.4.7/src/charset_normalizer/md.py`** -> AI Confidence: **99.31%**
5. **`charset_normalizer-3.4.7/src/charset_normalizer/utils.py`** -> AI Confidence: **99.24%**
6. **`charset_normalizer-3.4.7/src/charset_normalizer/models.py`** -> AI Confidence: **99.15%**
7. **`charset_normalizer-3.4.7/noxfile.py`** -> AI Confidence: **99.13%**
8. **`charset_normalizer-3.4.7/setup.py`** -> AI Confidence: **99.13%**
9. **`charset_normalizer-3.4.7/src/charset_normalizer/constant.py`** -> AI Confidence: **99.13%**
10. **`charset_normalizer-3.4.7/src/charset_normalizer/legacy.py`** -> AI Confidence: **99.13%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `charset_normalizer-3.4.7/tests/test_base_detection.py` -> **0.0099%** Exposure
- `charset_normalizer-3.4.7/tests/test_edge_case.py` -> **0.0006%** Exposure
### Exploit Generation Surface
- `charset_normalizer-3.4.7/noxfile.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `charset_normalizer-3.4.7/noxfile.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **100.0%** Exposure
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `130` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `charset_normalizer-3.4.7/src/charset_normalizer/models.py` (PYTHON) -> Cumulative Risk: **855.87**
- **Archetype:** `file_cluster_16` (Distance: 11.596 IQR)
- **Magnitude:** 495.98 | **LOC:** 370 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `append` (Impact: 104.8), `output` (Impact: 31.6), `language` (Impact: 31.5)

### 2. `charset_normalizer-3.4.7/src/charset_normalizer/md.py` (PYTHON) -> Cumulative Risk: **827.63**
- **Archetype:** `file_cluster_16` (Distance: 12.577 IQR)
- **Magnitude:** 1053.56 | **LOC:** 937 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `feed_info` (Impact: 165.8), `feed_info` (Impact: 104.2), `update` (Impact: 87.7)

### 3. `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` (PYTHON) -> Cumulative Risk: **664.01**
- **Archetype:** `file_cluster_16` (Distance: 10.146 IQR)
- **Magnitude:** 357.6 | **LOC:** 455 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (97.4113%)
- **Heaviest Functions:** `alpha_unicode_split` (Impact: 111.5), `encoding_unicode_range` (Impact: 55.8), `mb_encoding_languages` (Impact: 27.8)

### 4. `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py` (PYTHON) -> Cumulative Risk: **597.18**
- **Archetype:** `file_cluster_8` (Distance: 9.613 IQR)
- **Magnitude:** 713.76 | **LOC:** 363 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (82.6591%)
- **Heaviest Functions:** `cli_detect` (Impact: 577.5), `__call__` (Impact: 52.8), `query_yes_no` (Impact: 31.9)

### 5. `charset_normalizer-3.4.7/src/charset_normalizer/utils.py` (PYTHON) -> Cumulative Risk: **560.84**
- **Archetype:** `file_cluster_16` (Distance: 9.362 IQR)
- **Magnitude:** 440.3 | **LOC:** 423 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9991%), Documentation (99.989%)
- **Heaviest Functions:** `set_logging_handler` (Impact: 143.3), `_character_flags` (Impact: 49.6), `identify_sig_or_bom` (Impact: 31.4)

### 6. `charset_normalizer-3.4.7/noxfile.py` (PYTHON) -> Cumulative Risk: **525.38**
- **Archetype:** `file_cluster_8` (Distance: 8.213 IQR)
- **Magnitude:** 114.62 | **LOC:** 233 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `downstream_niquests` (Impact: 24.1), `coverage` (Impact: 19.2), `git_clone` (Impact: 14.6)

### 7. `charset_normalizer-3.4.7/_mypyc_hook/backend.py` (PYTHON) -> Cumulative Risk: **398.25**
- **Archetype:** `file_cluster_13` (Distance: 11.246 IQR)
- **Magnitude:** 8.64 | **LOC:** 38 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8653%), Safety Score (67.037%), Documentation (50.5416%)
- **Heaviest Functions:** `get_requires_for_build_wheel` (Impact: 1.1)

### 8. `charset_normalizer-3.4.7/tests/test_cli.py` (PYTHON) -> Cumulative Risk: **364.62**
- **Archetype:** `file_cluster_8` (Distance: 9.551 IQR)
- **Magnitude:** 169.68 | **LOC:** 190 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_multiple_file_normalize` (Impact: 48.8), `test_multiple_file_normalize_with_altern` (Impact: 37.8), `test_single_file_normalize` (Impact: 7.5)

### 9. `charset_normalizer-3.4.7/tests/test_thread_safety.py` (PYTHON) -> Cumulative Risk: **356.65**
- **Archetype:** `file_cluster_13` (Distance: 9.642 IQR)
- **Magnitude:** 77.76 | **LOC:** 55 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9756%), Algorithmic Dos (95.2574%), Stability (50.0%)
- **Heaviest Functions:** `test_concurrent_detection` (Impact: 37.2), `_detect` (Impact: 27.6), `test_concurrent_detection_repeated` (Impact: 7.2)

### 10. `charset_normalizer-3.4.7/tests/test_detect_legacy.py` (PYTHON) -> Cumulative Risk: **355.1**
- **Archetype:** `file_cluster_8` (Distance: 8.138 IQR)
- **Magnitude:** 64.66 | **LOC:** 61 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9948%), Logic Bomb (88.8385%), Stability (50.0%)
- **Heaviest Functions:** `test_small_payload_confidence_altered` (Impact: 14.7), `test_detect_dict_keys` (Impact: 14.4), `test_detect_dict_value_type` (Impact: 14.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `charset_normalizer-3.4.7/src/charset_normalizer/md.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.577 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.334 IQR)
- **Top Global Matches:** file_cluster_16: 12.577, file_cluster_8: 12.579, file_cluster_13: 12.643
- **Magnitude:** 1053.56 | **LOC:** 937 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (53.7735%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `feed_info` (Impact: 165.8 | O(N^5) | DB: 19)
  * `feed_info` (Impact: 104.2 | O(N^5) | DB: 12)
  * `update` (Impact: 87.7 | O(N^4) | DB: 77)
  * `feed_info` (Impact: 35.8 | O(N^4) | DB: 1)
  * `feed_info` (Impact: 35.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 111`, `args: 44`, `func_start: 44`, `class_start: 11`
* *Risk/State:* `state_mutation: 334`, `planned_debt: 1`, `duplicate_logic: 40`
* *Architecture:* `io: 1`, `api: 46`, `import: 8`
* *Defense:* `safety: 2`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.024
  * `Choke Point (Betweenness):` 0.001176 | `Ripple Effect (Closeness):` 0.144075
  * `Imports (Out-Degree: 2):` logging, sys, typing, functools, .constant, __future__, .utils, typing_extensions
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.613 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.992 IQR)
- **Top Global Matches:** file_cluster_8: 9.613, file_cluster_13: 9.747, file_cluster_7: 10.104
- **Magnitude:** 713.76 | **LOC:** 363 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (18.0714%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cli_detect` (Impact: 577.5 | O(N^6) | DB: 25)
  * `__call__` (Impact: 52.8 | O(N^4) | DB: 18)
  * `query_yes_no` (Impact: 31.9 | O(N^3))
    * *Intent:* """Ask a yes/no question via input() and return the answer as a bool."""
  * `__repr__` (Impact: 17.7 | O(N^3))
  * `__init__` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 49`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`
* *Architecture:* `io: 14`, `api: 6`, `import: 12`
* *Defense:* `safety: 5`, `doc: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` charset_normalizer.models, charset_normalizer.version, platform, charset_normalizer.md, sys, typing, unicodedata, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/src/charset_normalizer/models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.596 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.327 IQR)
- **Top Global Matches:** file_cluster_16: 11.596, file_cluster_0: 11.761, file_cluster_13: 11.786
- **Magnitude:** 495.98 | **LOC:** 370 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (44.8384%), Tech Debt (67.1031%)
**Top Internal Functions/Classes:**
  * `append` (Impact: 104.8 | O(2^N) | DB: 2)
    * *Intent:* """ if isinstance(item, int): return self._results[item] if isinstance(item, str): item = iana_name(...
  * `output` (Impact: 31.6 | O(N^6) | DB: 2)
  * `language` (Impact: 31.5 | O(N^4))
  * `__lt__` (Impact: 31.3 | O(N^4))
    * *Intent:* """ Implemented to make sorted available upon CharsetMatches items. """
  * `__str__` (Impact: 26.7 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 98`, `args: 36`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 41`, `duplicate_logic: 3`
* *Architecture:* `api: 41`, `import: 8`
* *Defense:* `safety: 7`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.945
  * `Choke Point (Betweenness):` 0.001667 | `Ripple Effect (Closeness):` 0.131808
  * `Imports (Out-Degree: 3):` charset_normalizer.cd, typing, .constant, json, encodings.aliases, re, __future__, .utils
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `charset_normalizer-3.4.7/src/charset_normalizer/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.362 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.844 IQR)
- **Top Global Matches:** file_cluster_16: 9.362, file_cluster_13: 9.503, file_cluster_8: 9.566
- **Magnitude:** 440.3 | **LOC:** 423 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.5864%), Tech Debt (14.2065%)
**Top Internal Functions/Classes:**
  * `set_logging_handler` (Impact: 143.3 | O(N^6))
  * `_character_flags` (Impact: 49.6 | O(N^3))
    * *Intent:* """Compute all name-based classification flags with a single unicodedata.name() call."""
  * `identify_sig_or_bom` (Impact: 31.4 | O(N^4))
  * `cp_similarity` (Impact: 18.2 | O(N^3))
  * `iana_name` (Impact: 18.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 96`, `args: 29`, `func_start: 29`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 53`, `import: 15`
* *Defense:* `safety: 5`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 86.655
  * `Choke Point (Betweenness):` 0.000882 | `Ripple Effect (Closeness):` 0.200784
  * `Imports (Out-Degree: 1):` logging, _multibytecodec, bisect, importlib, functools, unicodedata, typing, re...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.146 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.501 IQR)
- **Top Global Matches:** file_cluster_16: 10.146, file_cluster_8: 10.276, file_cluster_13: 10.278
- **Magnitude:** 357.6 | **LOC:** 455 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.648%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `alpha_unicode_split` (Impact: 111.5 | O(N^5) | DB: 2)
  * `encoding_unicode_range` (Impact: 55.8 | O(N^5))
    * *Intent:* """ Return associated unicode ranges in a single byte code page. """
  * `mb_encoding_languages` (Impact: 27.8 | O(N^2))
  * `merge_coherence_ratios` (Impact: 26.2 | O(N^4) | DB: 1)
  * `filter_alt_coherence_matches` (Impact: 25.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 66`, `args: 14`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 25`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `doc: 22`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.054
  * `Choke Point (Betweenness):` 0.001961 | `Ripple Effect (Closeness):` 0.118627
  * `Imports (Out-Degree: 4):` .models, functools, collections, importlib, typing, .constant, .md, codecs...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `charset_normalizer-3.4.7/tests/test_cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.551 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.012 IQR)
- **Top Global Matches:** file_cluster_8: 9.551, file_cluster_13: 9.936, file_cluster_7: 10.129
- **Magnitude:** 169.68 | **LOC:** 190 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (3.6992%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multiple_file_normalize` (Impact: 48.8 | O(N^5) | DB: 6)
    * *Intent:* """Ensure --normalize with multiple files writes each output to the correct path and sets unicode_pa...
  * `test_multiple_file_normalize_with_altern` (Impact: 37.8 | O(N^5))
  * `test_single_file_normalize` (Impact: 7.5 | O(N^3))
  * `test_non_existent_file` (Impact: 7.2 | O(N^3))
  * `test_version_output_success` (Impact: 7.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 33`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `orphaned_logic: 15`
* *Architecture:* `io: 3`, `api: 16`, `import: 6`
* *Defense:* `safety: 10`, `doc: 4`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` charset_normalizer.cli, unittest, unittest.mock, os, os.path, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/noxfile.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.213 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.756 IQR)
- **Top Global Matches:** file_cluster_8: 8.213, file_cluster_16: 8.548, file_cluster_0: 8.666
- **Magnitude:** 114.62 | **LOC:** 233 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (6.0658%), Tech Debt (69.2802%)
**Top Internal Functions/Classes:**
  * `downstream_niquests` (Impact: 24.1 | O(N^2) | DB: 21)
  * `coverage` (Impact: 19.2 | O(2^N))
  * `git_clone` (Impact: 14.6 | O(N^3) | DB: 3)
    * *Intent:* """We either clone the target repository or if already exist simply reset the state and pull. """
  * `performance` (Impact: 12.7 | O(2^N))
  * `docs` (Impact: 12.4 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 19`, `args: 12`, `func_start: 12`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `io: 10`, `api: 12`, `import: 6`
* *Defense:* `doc: 4`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, nox, shutil, charset_normalizer, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/src/charset_normalizer/api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.972 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.859 IQR)
- **Top Global Matches:** file_cluster_8: 9.972, file_cluster_16: 10.641, file_cluster_7: 10.647
- **Magnitude:** 90.42 | **LOC:** 989 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.4784%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_fp` (Impact: 1.6 | O(N^1))
  * `from_path` (Impact: 1.6 | O(N^1))
  * `is_binary` (Impact: 1.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 57`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 65`
* *Architecture:* `io: 1`, `api: 5`, `import: 9`
* *Defense:* `safety: 15`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 53.587
  * `Choke Point (Betweenness):` 0.009902 | `Ripple Effect (Closeness):` 0.120098
  * `Imports (Out-Degree: 5):` logging, .models, os, typing, .constant, .md, __future__, .cd...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `charset_normalizer-3.4.7/tests/test_thread_safety.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.642 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.883 IQR)
- **Top Global Matches:** file_cluster_13: 9.642, file_cluster_16: 9.655, file_cluster_8: 9.677
- **Magnitude:** 77.76 | **LOC:** 55 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.9794%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_concurrent_detection` (Impact: 37.2 | O(N^5))
    * *Intent:* """Three files detected concurrently must each return the correct encoding and language, proving no ...
  * `_detect` (Impact: 27.6 | O(N^2))
  * `test_concurrent_detection_repeated` (Impact: 7.2 | O(N^3))
    * *Intent:* """Run the same three-file detection five times to surface any intermittent race conditions."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 2`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, __future__, charset_normalizer.api, concurrent.futures
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/tests/test_base_detection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.92 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.747 IQR)
- **Top Global Matches:** file_cluster_8: 10.92, file_cluster_0: 11.247, file_cluster_13: 11.388
- **Magnitude:** 69.9 | **LOC:** 213 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.2391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_empty_but_with_bom_or_sig` (Impact: 11.0 | O(N^2))
  * `test_md_triggered_but_with_bom_or_sig` (Impact: 8.4 | O(N^2))
  * `test_content_with_bom_or_sig` (Impact: 8.2 | O(N^2))
  * `test_mb_cutting_chk` (Impact: 5.9 | O(N^2))
    * *Intent:* # on chunks extraction. payload = ( b"\xbf\xaa\xbb\xe7\xc0\xfb \xbf\xb9\xbc\xf6 " b" \xbf\xac\xb1\xb...
  * `test_bool_matches` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 60`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 36`, `doc: 6`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` charset_normalizer.models, pytest, __future__, charset_normalizer.api
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/tests/test_detect_legacy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.138 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.784 IQR)
- **Top Global Matches:** file_cluster_8: 8.138, file_cluster_13: 8.376, file_cluster_7: 8.618
- **Magnitude:** 64.66 | **LOC:** 61 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.1807%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_small_payload_confidence_altered` (Impact: 14.7 | O(N^3))
  * `test_detect_dict_keys` (Impact: 14.4 | O(N^3))
  * `test_detect_dict_value_type` (Impact: 14.4 | O(N^3))
  * `test_detect_dict_value` (Impact: 7.2 | O(N^3))
  * `test_utf8_sig_not_striped` (Impact: 7.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 11`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` charset_normalizer.legacy, __future__, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/src/charset_normalizer/constant.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.439 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.428 IQR)
- **Top Global Matches:** file_cluster_8: 8.439, file_cluster_7: 9.414, file_cluster_1: 9.575
- **Magnitude:** 56.1 | **LOC:** 2051 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.9542%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 11`, `args: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 5`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 158.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.226891
  * `Imports (Out-Degree: 0):` re, encodings.aliases, codecs, __future__, time
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `charset_normalizer-3.4.7/tests/test_logging.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.369 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.547 IQR)
- **Top Global Matches:** file_cluster_13: 11.369, file_cluster_8: 11.547, file_cluster_0: 12.058
- **Magnitude:** 46.28 | **LOC:** 54 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.4542%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_explain_false_handler_set_behavior` (Impact: 27.4 | O(N^4))
  * `test_explain_true_behavior` (Impact: 7.2 | O(N^3))
  * `setup_method` (Impact: 2.8 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 24`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 9`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` logging, pytest, charset_normalizer.constant, charset_normalizer.utils, __future__, charset_normalizer.api
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/tests/test_large_payload.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.326 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.845 IQR)
- **Top Global Matches:** file_cluster_8: 11.326, file_cluster_13: 11.509, file_cluster_7: 12.07
- **Magnitude:** 39.66 | **LOC:** 56 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.5981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_misleading_large_sequence` (Impact: 18.8 | O(N^2))
  * `test_large_payload_u8_sig_basic_entry` (Impact: 8.5 | O(N^2))
  * `test_large_payload_ascii_basic_entry` (Impact: 8.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 26`, `args: 3`, `func_start: 3`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 15`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` charset_normalizer.constant, pytest, __future__, charset_normalizer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/tests/test_coherence_detection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.565 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.296 IQR)
- **Top Global Matches:** file_cluster_8: 7.565, file_cluster_13: 8.478, file_cluster_0: 8.495
- **Magnitude:** 26.94 | **LOC:** 109 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_infer_language_from_cp` (Impact: 17.9 | O(N^3))
  * `test_target_features` (Impact: 2.2 | O(N^1))
  * `test_filter_alt_coherence_matches` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 4`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, __future__, charset_normalizer.cd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.239 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.758 IQR)
- **Top Global Matches:** file_cluster_13: 9.239, file_cluster_8: 9.422, file_cluster_17: 10.159
- **Magnitude:** 18.56 | **LOC:** 38 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.0057%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 8`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mypyc.build, sys, os, __future__, setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/src/charset_normalizer/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.202 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.245 IQR)
- **Top Global Matches:** file_cluster_13: 7.202, file_cluster_8: 7.231, file_cluster_7: 7.836
- **Magnitude:** 16.4 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.4569%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` logging, .models, .version, charset_normalizer, .legacy, __future__, .api, .utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/tests/test_edge_case.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.461 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.542 IQR)
- **Top Global Matches:** file_cluster_13: 11.461, file_cluster_8: 11.518, file_cluster_0: 11.846
- **Magnitude:** 14.64 | **LOC:** 60 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.9687%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_issue_gh509` (Impact: 3.8 | O(N^2))
  * `test_issue_gh520` (Impact: 3.1 | O(N^2))
    * *Intent:* """Verify that minorities does not strip basic latin characters!"""
  * `test_unicode_edge_case` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 18`, `args: 4`, `func_start: 4`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 8`, `doc: 6`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, __future__, charset_normalizer, platform
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/src/charset_normalizer/cli/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.134 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.805 IQR)
- **Top Global Matches:** file_cluster_8: 6.134, file_cluster_13: 6.271, file_cluster_7: 7.274
- **Magnitude:** 14.12 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, .__main__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/tests/test_preemptive_detection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.057 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.243 IQR)
- **Top Global Matches:** file_cluster_8: 7.057, file_cluster_13: 7.816, file_cluster_7: 7.926
- **Magnitude:** 12.34 | **LOC:** 93 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.2499%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_preemptive_mark_replacement` (Impact: 8.8 | O(N^2))
    * *Intent:* """ When generating (to Unicode converted) bytes, we want to change any potential declarative charse...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 2`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, __future__, charset_normalizer.utils, charset_normalizer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/src/charset_normalizer/__main__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.684 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.415 IQR)
- **Top Global Matches:** file_cluster_8: 5.684, file_cluster_13: 5.782, file_cluster_7: 7.104
- **Magnitude:** 12.08 | **LOC:** 7 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, .cli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/src/charset_normalizer/version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.624 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.375 IQR)
- **Top Global Matches:** file_cluster_8: 8.624, file_cluster_13: 8.659, file_cluster_7: 8.898
- **Magnitude:** 11.56 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.553
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `charset_normalizer-3.4.7/_mypyc_hook/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `charset_normalizer-3.4.7/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 9.7 | **LOC:** 485 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `charset_normalizer-3.4.7/tests/test_thread_safety.py` (PYTHON) | Magnitude: 77.76 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 16, branch: 15, encapsulation: 6
- `charset_normalizer-3.4.7/src/charset_normalizer/__init__.py` (PYTHON) | Magnitude: 16.4 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 10, import: 7, encapsulation: 4
- `charset_normalizer-3.4.7/tests/test_edge_case.py` (PYTHON) | Magnitude: 14.64 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, sec_reflection_metaprogramming: 17, test: 14
- `charset_normalizer-3.4.7/tests/test_logging.py` (PYTHON) | Magnitude: 46.28 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 24, test: 13, safety: 9
- `charset_normalizer-3.4.7/setup.py` (PYTHON) | Magnitude: 18.56 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, branch: 8, structural_boundaries: 8, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` (PYTHON) | Magnitude: 1053.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 670, state_mutation: 334, encapsulation: 303, branch: 156
- `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` (PYTHON) | Magnitude: 357.6 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 265, branch: 97, structural_boundaries: 66, generics: 35
- `charset_normalizer-3.4.7/src/charset_normalizer/utils.py` (PYTHON) | Magnitude: 440.3 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 96, branch: 70, api: 53
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` (PYTHON) | Magnitude: 495.98 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 98, encapsulation: 80, branch: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `charset_normalizer-3.4.7/src/charset_normalizer/version.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 3, structural_boundaries: 2, doc: 2, import: 1
- `charset_normalizer-3.4.7/src/charset_normalizer/__main__.py` (PYTHON) | Magnitude: 12.08 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, encapsulation: 3, import: 2, branch: 1
- `charset_normalizer-3.4.7/src/charset_normalizer/legacy.py` (PYTHON) | Magnitude: 4.08 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, branch: 22, structural_boundaries: 17, import: 6
- `charset_normalizer-3.4.7/src/charset_normalizer/cli/__main__.py` (PYTHON) | Magnitude: 713.76 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 287, branch: 80, structural_boundaries: 49, encapsulation: 29
- `charset_normalizer-3.4.7/src/charset_normalizer/cli/__init__.py` (PYTHON) | Magnitude: 14.12 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, encapsulation: 3, import: 2, indent_spaces: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `charset_normalizer-3.4.7/src/charset_normalizer/api.py` -> **Severity: 0.733** (Bridge: 0.0099 * Flux: 74.0595%)
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **Severity: 0.164** (Bridge: 0.0017 * Flux: 98.6697%)
- `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` -> **Severity: 0.14** (Bridge: 0.002 * Flux: 71.2271%)
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **Severity: 0.118** (Bridge: 0.0012 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **Severity: 6.157** (Embedded: 0.1441 * Error Risk: 42.7331%)
- `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` -> **Severity: 5.368** (Embedded: 0.1186 * Error Risk: 45.2542%)
- `charset_normalizer-3.4.7/src/charset_normalizer/legacy.py` -> **Severity: 1.977** (Embedded: 0.0392 * Error Risk: 50.4082%)
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **Severity: 1.447** (Embedded: 0.1318 * Error Risk: 10.9814%)
- `charset_normalizer-3.4.7/src/charset_normalizer/constant.py` -> **Severity: 1.091** (Embedded: 0.2269 * Error Risk: 4.81%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `charset_normalizer-3.4.7/src/charset_normalizer/utils.py` -> **Severity: 8664.547** (Blast Radius: 86.655 * Doc Risk: 99.989%)
- `charset_normalizer-3.4.7/src/charset_normalizer/md.py` -> **Severity: 4386.503** (Blast Radius: 44.024 * Doc Risk: 99.6389%)
- `charset_normalizer-3.4.7/src/charset_normalizer/cd.py` -> **Severity: 4193.946** (Blast Radius: 43.054 * Doc Risk: 97.4113%)
- `charset_normalizer-3.4.7/src/charset_normalizer/models.py` -> **Severity: 4094.488** (Blast Radius: 40.945 * Doc Risk: 99.9997%)
- `charset_normalizer-3.4.7/src/charset_normalizer/constant.py` -> **Severity: 1887.699** (Blast Radius: 158.36 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
