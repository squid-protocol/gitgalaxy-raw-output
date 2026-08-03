# ARCHITECTURAL_BRIEF: soupsieve
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/soupsieve` |
| **Timestamp** | `2026-08-03T21:25:26.983713+00:00` |
| **Scan Duration** | `0.43s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 100 malicious artifacts.

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
| Total Artifacts | 114 |
| Analyzed Artifacts (Scanned) | 106 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 6050 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4444 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 100 | 6050 | 94.3% |
| PLAINTEXT | 4 | 0 | 3.8% |
| MARKDOWN | 2 | 0 | 1.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.432`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 90 | 84.9% |
| file_cluster_13 | 6 | 5.7% |
| file_cluster_16 | 4 | 3.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 5.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 38.5 | 4.2 | 1.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 3.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.2 | 7.0 | 7.3 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.1 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 67.1 | 87.7 | 87.7 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 33.2 | 0.1 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `soupsieve-2.8.3/soupsieve/css_parser.py` (Hits: 6)
- `soupsieve-2.8.3/tests/test_level4/test_open.py` (Hits: 4)
- `soupsieve-2.8.3/tests/test_bs4_cases.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__meta__.py** (`soupsieve-2.8.3/soupsieve/__meta__.py`) — 2 inbound connections
2. **pretty.py** (`soupsieve-2.8.3/soupsieve/pretty.py`) — 1 inbound connections
3. **LICENSE.md** (`soupsieve-2.8.3/LICENSE.md`) — 0 inbound connections
4. **README.md** (`soupsieve-2.8.3/README.md`) — 0 inbound connections
5. **lint.txt** (`soupsieve-2.8.3/requirements/lint.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **css_match.py** (`soupsieve-2.8.3/soupsieve/css_match.py`) — 7 outbound dependencies
2. **css_parser.py** (`soupsieve-2.8.3/soupsieve/css_parser.py`) — 7 outbound dependencies
3. **__init__.py** (`soupsieve-2.8.3/soupsieve/__init__.py`) — 6 outbound dependencies
4. **test_api.py** (`soupsieve-2.8.3/tests/test_api.py`) — 6 outbound dependencies
5. **util.py** (`soupsieve-2.8.3/tests/util.py`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `match_dir` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **450.9** | LOC: 59
- `match_lang` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **434.7** | LOC: 86
- `match_nth` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **388.5** | LOC: 101
  * *Intent:* # If a < 0, our count is working backwards, so floor the index by increasing the count. # Find the count that yields the lowest, in bound value and us...
- `match_selectors` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **268.2** | LOC: 84
- `parse_value` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **206.7** | LOC: 54
- `match_indeterminate` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **191.1** | LOC: 63
- `match_range` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **169.7** | LOC: 33
  * *Intent:* """ Match placeholder shown according to HTML spec. - text area should be checked if they have content. A single newline does not count as content. ""...
- `find_bidi` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **136.9** | LOC: 37
- `match_default` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **129.3** | LOC: 40
- `match_contains` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **126.6** | LOC: 28
  * *Intent:* # Can't do nested forms (haven't figured out why we never hit this)

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `match_dir` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> **O(2^N) [Recursive]**
- `find_bidi` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> **O(2^N) [Recursive]**
- `normalize_value` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> **O(2^N) [Recursive]**
- `closest` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> **O(2^N) [Recursive]**
- `deprecated` (@ `soupsieve-2.8.3/soupsieve/util.py`) -> **O(2^N) [Recursive]**
- `filter` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `soupsieve-2.8.3/soupsieve/css_types.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Get item."""
- `__init__` (@ `soupsieve-2.8.3/soupsieve/util.py`) -> **O(2^N) [Recursive]**
- `match` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> **O(2^N) [Recursive]**
- `closest` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_targted_open` (@ `soupsieve-2.8.3/tests/test_level4/test_open.py`) -> DB Complexity: **6**
- `match_selectors` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> DB Complexity: **4**
- `get_pattern_context` (@ `soupsieve-2.8.3/soupsieve/util.py`) -> DB Complexity: **4**
- `__init__` (@ `soupsieve-2.8.3/soupsieve/util.py`) -> DB Complexity: **4**
- `test_open` (@ `soupsieve-2.8.3/tests/test_level4/test_open.py`) -> DB Complexity: **3**
- `test_not_open` (@ `soupsieve-2.8.3/tests/test_level4/test_open.py`) -> DB Complexity: **3**
- `match_lang` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> DB Complexity: **2**
- `normalize_value` (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> DB Complexity: **2**
- `__init__` (@ `soupsieve-2.8.3/soupsieve/css_types.py`) -> DB Complexity: **2**
- `test_copy_pickle` (@ `soupsieve-2.8.3/tests/test_api.py`) -> DB Complexity: **2**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `soupsieve-2.8.3/soupsieve` | 7 | 5166.21 | 25.0% | 22.66% |
| `soupsieve-2.8.3/tests/test_level4` | 37 | 810.9 | 2.15% | 0.0% |
| `soupsieve-2.8.3/tests` | 6 | 512.62 | 3.52% | 0.0% |
| `soupsieve-2.8.3/tests/test_level3` | 20 | 484.72 | 2.49% | 0.0% |
| `soupsieve-2.8.3/tests/test_extra` | 5 | 270.78 | 2.03% | 0.0% |
| `soupsieve-2.8.3/tests/test_level2` | 9 | 245.36 | 3.16% | 0.0% |
| `soupsieve-2.8.3/tests/test_level1` | 14 | 162.58 | 3.37% | 0.0% |
| `soupsieve-2.8.3/tests/test_nesting_1` | 2 | 56.08 | 3.79% | 0.0% |
| `soupsieve-2.8.3/requirements` | 4 | 4.0 | 0.0% | 0.0% |
| `soupsieve-2.8.3` | 2 | 2.78 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `soupsieve-2.8.3/soupsieve/css_types.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **58.6499%** Exposure
### Highest State Flux (Mutation/Volatility)
- `soupsieve-2.8.3/soupsieve/util.py` -> **99.9996%** Exposure
- `soupsieve-2.8.3/soupsieve/pretty.py` -> **99.995%** Exposure
- `soupsieve-2.8.3/soupsieve/css_parser.py` -> **99.8836%** Exposure
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **51.7704%** Exposure
- `soupsieve-2.8.3/soupsieve/css_types.py` -> **40.6326%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `soupsieve-2.8.3/soupsieve/css_types.py` -> **2** Orphaned Functions | **28** Duplicates
- `soupsieve-2.8.3/tests/test_level2/test_attribute.py` -> **30** Orphaned Functions | **0** Duplicates
- `soupsieve-2.8.3/tests/test_extra/test_soup_contains.py` -> **18** Orphaned Functions | **2** Duplicates
- `soupsieve-2.8.3/tests/test_level4/test_lang.py` -> **20** Orphaned Functions | **0** Duplicates
- `soupsieve-2.8.3/tests/test_api.py` -> **19** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`soupsieve-2.8.3/soupsieve/css_match.py`** -> AI Confidence: **99.31%**
2. **`soupsieve-2.8.3/soupsieve/css_parser.py`** -> AI Confidence: **99.31%**
3. **`soupsieve-2.8.3/soupsieve/__meta__.py`** -> AI Confidence: **99.09%**
4. **`soupsieve-2.8.3/soupsieve/pretty.py`** -> AI Confidence: **99.06%**
5. **`soupsieve-2.8.3/soupsieve/util.py`** -> AI Confidence: **99.03%**
6. **`soupsieve-2.8.3/tests/util.py`** -> AI Confidence: **99.03%**
7. **`soupsieve-2.8.3/soupsieve/__init__.py`** -> AI Confidence: **98.96%**
8. **`soupsieve-2.8.3/tests/test_level4/test_scope.py`** -> AI Confidence: **98.96%**
9. **`soupsieve-2.8.3/tests/test_nesting_1/test_amp.py`** -> AI Confidence: **98.96%**
10. **`soupsieve-2.8.3/tests/test_api.py`** -> AI Confidence: **98.93%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/css_parser.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/util.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/tests/test_api.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/tests/test_extra/test_custom.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/util.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/tests/test_api.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/tests/test_extra/test_soup_contains.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/tests/test_level2/test_attribute.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `78` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `soupsieve-2.8.3/soupsieve/css_types.py` (PYTHON) -> Cumulative Risk: **749.55**
- **Archetype:** `file_cluster_16` (Distance: 11.533 IQR)
- **Magnitude:** 275.24 | **LOC:** 408 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Logic Bomb (99.9995%), Algorithmic Dos (99.9965%)
- **Heaviest Functions:** `_validate` (Impact: 39.6), `_validate` (Impact: 27.3), `_validate` (Impact: 27.3)

### 2. `soupsieve-2.8.3/soupsieve/util.py` (PYTHON) -> Cumulative Risk: **748.91**
- **Archetype:** `file_cluster_16` (Distance: 11.807 IQR)
- **Magnitude:** 124.36 | **LOC:** 118 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `get_pattern_context` (Impact: 36.6), `__init__` (Impact: 27.5), `lower` (Impact: 12.4)

### 3. `soupsieve-2.8.3/soupsieve/css_match.py` (PYTHON) -> Cumulative Risk: **695.02**
- **Archetype:** `file_cluster_16` (Distance: 11.624 IQR)
- **Magnitude:** 4157.26 | **LOC:** 1655 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9633%)
- **Heaviest Functions:** `match_dir` (Impact: 450.9), `match_lang` (Impact: 434.7), `match_nth` (Impact: 388.5)

### 4. `soupsieve-2.8.3/soupsieve/__meta__.py` (PYTHON) -> Cumulative Risk: **413.64**
- **Archetype:** `file_cluster_8` (Distance: 9.978 IQR)
- **Magnitude:** 96.18 | **LOC:** 198 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.999%), Algorithmic Dos (83.8157%), Stability (50.0%)
- **Heaviest Functions:** `parse_version` (Impact: 52.7), `_get_canonical` (Impact: 21.6), `_is_pre` (Impact: 2.8)

### 5. `soupsieve-2.8.3/soupsieve/css_parser.py` (PYTHON) -> Cumulative Risk: **410.13**
- **Archetype:** `file_cluster_8` (Distance: 11.814 IQR)
- **Magnitude:** 254.44 | **LOC:** 1319 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.8836%), Stability (50.0%)
- **Heaviest Functions:** `process_selectors` (Impact: 3.2)

### 6. `soupsieve-2.8.3/tests/util.py` (PYTHON) -> Cumulative Risk: **370.8**
- **Archetype:** `file_cluster_13` (Distance: 11.055 IQR)
- **Magnitude:** 150.4 | **LOC:** 160 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `assert_selector` (Impact: 29.3), `available_parsers` (Impact: 28.5), `get_parsers` (Impact: 21.6)

### 7. `soupsieve-2.8.3/tests/test_api.py` (PYTHON) -> Cumulative Risk: **365.14**
- **Archetype:** `file_cluster_8` (Distance: 10.702 IQR)
- **Magnitude:** 256.74 | **LOC:** 646 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_copy_pickle` (Impact: 125.9), `test_match` (Impact: 8.3), `test_filter_tag` (Impact: 6.9)

### 8. `soupsieve-2.8.3/tests/test_level2/test_attribute.py` (PYTHON) -> Cumulative Risk: **364.71**
- **Archetype:** `file_cluster_8` (Distance: 9.758 IQR)
- **Magnitude:** 148.5 | **LOC:** 420 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_nested_sequences` (Impact: 7.4), `test_attribute_type_html` (Impact: 4.1), `test_attribute_type_xml` (Impact: 4.1)

### 9. `soupsieve-2.8.3/tests/test_extra/test_soup_contains.py` (PYTHON) -> Cumulative Risk: **362.25**
- **Archetype:** `file_cluster_8` (Distance: 9.497 IQR)
- **Magnitude:** 139.06 | **LOC:** 318 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_contains_warn` (Impact: 22.0), `test_contains_iframe` (Impact: 11.7), `test_contains_cdata_lxml_html` (Impact: 11.2)

### 10. `soupsieve-2.8.3/tests/test_level3/test_root.py` (PYTHON) -> Cumulative Risk: **362.02**
- **Archetype:** `file_cluster_8` (Distance: 10.429 IQR)
- **Magnitude:** 85.02 | **LOC:** 189 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9996%), Stability (50.0%)
- **Heaviest Functions:** `test_no_iframe` (Impact: 18.2), `test_root_iframe` (Impact: 10.9), `test_iframe` (Impact: 8.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `soupsieve-2.8.3/soupsieve/css_match.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.624 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.183 IQR)
- **Top Global Matches:** file_cluster_16: 11.624, file_cluster_0: 11.8, file_cluster_8: 11.83
- **Magnitude:** 4157.26 | **LOC:** 1655 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (38.5036%), Tech Debt (58.6499%)
**Top Internal Functions/Classes:**
  * `match_dir` (Impact: 450.9 | O(2^N))
  * `match_lang` (Impact: 434.7 | O(N^6) | DB: 2)
  * `match_nth` (Impact: 388.5 | O(N^6))
    * *Intent:* # If a < 0, our count is working backwards, so floor the index by increasing the count. # Find the c...
  * `match_selectors` (Impact: 268.2 | O(N^5) | DB: 4)
  * `parse_value` (Impact: 206.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 603`, `structural_boundaries: 308`, `args: 90`, `func_start: 90`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 66`, `duplicate_logic: 11`, `orphaned_logic: 4`
* *Architecture:* `api: 88`, `import: 8`
* *Defense:* `safety: 35`, `doc: 192`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, bs4, unicodedata, datetime, re, , typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/css_types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.533 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.346 IQR)
- **Top Global Matches:** file_cluster_16: 11.533, file_cluster_13: 12.047, file_cluster_7: 12.098
- **Magnitude:** 275.24 | **LOC:** 408 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (18.2685%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_validate` (Impact: 39.6 | O(N^4))
  * `_validate` (Impact: 27.3 | O(N^3))
  * `_validate` (Impact: 27.3 | O(N^3))
  * `__eq__` (Impact: 14.3 | O(N^3))
  * `__ne__` (Impact: 14.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 75`, `args: 35`, `func_start: 35`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 12`, `duplicate_logic: 28`, `orphaned_logic: 2`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `safety: 18`, `doc: 94`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .pretty, typing, __future__, copyreg
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.702 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.731 IQR)
- **Top Global Matches:** file_cluster_8: 10.702, file_cluster_7: 10.814, file_cluster_1: 11.045
- **Magnitude:** 256.74 | **LOC:** 646 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (2.7879%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_copy_pickle` (Impact: 125.9 | O(N^4) | DB: 2)
  * `test_match` (Impact: 8.3 | O(N^2))
  * `test_filter_tag` (Impact: 6.9 | O(N^2))
  * `test_select_limit` (Impact: 5.8 | O(N^2))
  * `test_iselect` (Impact: 5.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 68`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 19`
* *Architecture:* `api: 48`, `import: 6`
* *Defense:* `doc: 128`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, , copy, random, pytest, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/css_parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.814 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.728 IQR)
- **Top Global Matches:** file_cluster_8: 11.814, file_cluster_16: 11.963, file_cluster_7: 12.031
- **Magnitude:** 254.44 | **LOC:** 1319 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.9589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process_selectors` (Impact: 3.2 | O(N^2))
    * *Intent:* ''' ).process_selectors(flags=FLG_PSEUDO | FLG_HTML) # CSS pattern for `:default` (must compile CSS_...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 120`, `args: 32`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 206`
* *Architecture:* `io: 6`, `api: 27`, `import: 9`
* *Defense:* `safety: 3`, `doc: 106`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, functools, re, , warnings, typing, .util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/pretty.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.186 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.386 IQR)
- **Top Global Matches:** file_cluster_8: 10.186, file_cluster_13: 10.389, file_cluster_7: 10.66
- **Magnitude:** 227.59 | **LOC:** 149 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (27.7445%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009524
  * `Imports (Out-Degree: 0):` soupsieve, typing, re, __future__
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/tests/util.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.055 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.873 IQR)
- **Top Global Matches:** file_cluster_13: 11.055, file_cluster_8: 11.298, file_cluster_7: 11.36
- **Magnitude:** 150.4 | **LOC:** 160 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.3282%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_selector` (Impact: 29.3 | O(N^4) | DB: 1)
  * `available_parsers` (Impact: 28.5 | O(N^3))
  * `get_parsers` (Impact: 21.6 | O(N^3))
  * `skip_no_lxml` (Impact: 11.0 | O(N^3))
  * `assert_raises` (Impact: 10.1 | O(N^3))
    * *Intent:* """Assert raises."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 31`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `api: 21`, `import: 7`
* *Defense:* `safety: 4`, `doc: 32`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` textwrap, bs4, soupsieve, bs4.builder, pytest, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level2/test_attribute.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.758 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.83 IQR)
- **Top Global Matches:** file_cluster_8: 9.758, file_cluster_7: 9.999, file_cluster_1: 10.193
- **Magnitude:** 148.5 | **LOC:** 420 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.2931%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_nested_sequences` (Impact: 7.4 | O(N^3))
  * `test_attribute_type_html` (Impact: 4.1 | O(N^3))
  * `test_attribute_type_xml` (Impact: 4.1 | O(N^3))
    * *Intent:* """ Test invalid tag. Tag must come first. """
  * `test_attribute_type_xhtml` (Impact: 4.1 | O(N^3))
  * `test_attribute` (Impact: 4.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 46`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 30`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `doc: 80`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, .., bs4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_extra/test_soup_contains.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.497 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.342 IQR)
- **Top Global Matches:** file_cluster_8: 9.497, file_cluster_7: 9.762, file_cluster_1: 9.976
- **Magnitude:** 139.06 | **LOC:** 318 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.5265%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_contains_warn` (Impact: 22.0 | O(N^5))
  * `test_contains_iframe` (Impact: 11.7 | O(N^3))
  * `test_contains_cdata_lxml_html` (Impact: 11.2 | O(N^3))
  * `test_contains_iframe_xml` (Impact: 4.8 | O(N^3))
  * `test_contains_escapes` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 33`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `duplicate_logic: 2`, `orphaned_logic: 18`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `doc: 62`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bs4, soupsieve, lxml, warnings, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/util.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.807 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.639 IQR)
- **Top Global Matches:** file_cluster_16: 11.807, file_cluster_13: 11.809, file_cluster_8: 12.22
- **Magnitude:** 124.36 | **LOC:** 118 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (34.8771%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_pattern_context` (Impact: 36.6 | O(N^3) | DB: 4)
  * `__init__` (Impact: 27.5 | O(2^N) | DB: 4)
  * `lower` (Impact: 12.4 | O(N^2) | DB: 1)
  * `deprecated` (Impact: 9.4 | O(2^N))
  * `warn_deprecated` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 21`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 27`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, functools, re, warnings, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_lang.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.299 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.424 IQR)
- **Top Global Matches:** file_cluster_8: 9.299, file_cluster_7: 9.583, file_cluster_1: 9.761
- **Magnitude:** 105.24 | **LOC:** 404 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_language_list` (Impact: 4.2 | O(N^3))
  * `test_xml_style_language` (Impact: 4.2 | O(N^3))
    * *Intent:* """Test undetermined language."""
  * `test_language_in_xhtml_without_html_styl` (Impact: 4.2 | O(N^3))
  * `test_language_und` (Impact: 4.1 | O(N^3))
  * `test_language_empty_string` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 23`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 20`
* *Architecture:* `api: 21`, `import: 1`
* *Defense:* `doc: 64`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/__meta__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.978 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.524 IQR)
- **Top Global Matches:** file_cluster_8: 9.978, file_cluster_16: 10.107, file_cluster_13: 10.244
- **Magnitude:** 96.18 | **LOC:** 198 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (26.9381%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_version` (Impact: 52.7 | O(N^2))
  * `_get_canonical` (Impact: 21.6 | O(N^3) | DB: 1)
    * *Intent:* # Ensure valid development or development/pre release elif release < "alpha": if release > ".dev" an...
  * `_is_pre` (Impact: 2.8 | O(N^2))
  * `_is_dev` (Impact: 2.8 | O(N^2))
    * *Intent:* # Ensure all parts are positive integers. for value in (major, minor, micro, pre, post): if not (isi...
  * `_is_post` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 23`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 2`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019048
  * `Imports (Out-Degree: 0):` collections, re, __future__
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/tests/test_level3/test_root.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.429 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.013 IQR)
- **Top Global Matches:** file_cluster_8: 10.429, file_cluster_7: 10.568, file_cluster_13: 10.716
- **Magnitude:** 85.02 | **LOC:** 189 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.2456%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_no_iframe` (Impact: 18.2 | O(N^3))
    * *Intent:* # Root in HTML is `<html>` self.assert_selector( self.MARKUP, ":root", ["root"], flags=util.HTML ) d...
  * `test_root_iframe` (Impact: 10.9 | O(N^3))
  * `test_iframe` (Impact: 8.3 | O(N^2))
  * `test_root_whitespace` (Impact: 5.7 | O(N^2))
  * `test_root_preprocess` (Impact: 5.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 19`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 11`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `doc: 42`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, .., bs4, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level3/test_namespace.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.378 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.852 IQR)
- **Top Global Matches:** file_cluster_8: 8.378, file_cluster_7: 8.785, file_cluster_1: 8.989
- **Magnitude:** 82.76 | **LOC:** 328 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.3295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wrap_xlink` (Impact: 9.3 | O(N^2))
  * `test_attribute_namespace` (Impact: 7.2 | O(N^3))
  * `test_namespace_inherit` (Impact: 5.9 | O(N^4))
  * `test_namespace_with_default` (Impact: 5.7 | O(N^4))
  * `test_namespace_case` (Impact: 5.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 19`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 10`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `doc: 42`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_dir.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.284 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.395 IQR)
- **Top Global Matches:** file_cluster_8: 9.284, file_cluster_7: 9.58, file_cluster_1: 9.783
- **Magnitude:** 73.68 | **LOC:** 216 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.5895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_iframe` (Impact: 11.4 | O(N^3))
  * `test_dir_on_input_root` (Impact: 10.9 | O(N^3))
    * *Intent:* """Test that the root is assumed left to right if auto used."""
  * `test_xml_in_html` (Impact: 4.8 | O(N^3))
  * `test_dir_bidi_detect` (Impact: 4.3 | O(N^3))
  * `test_dir_auto_root` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 11`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `doc: 36`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, .., bs4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_versions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.725 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.77 IQR)
- **Top Global Matches:** file_cluster_8: 11.725, file_cluster_7: 12.08, file_cluster_13: 12.131
- **Magnitude:** 64.54 | **LOC:** 94 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9801%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_asserts` (Impact: 46.4 | O(N^3))
  * `test_version_parsing` (Impact: 5.2 | O(N^3))
  * `test_version_output` (Impact: 3.3 | O(N^2))
  * `test_version_comparison` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 34`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 26`, `doc: 12`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, soupsieve.__meta__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_has.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.651 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.022 IQR)
- **Top Global Matches:** file_cluster_8: 9.651, file_cluster_7: 9.928, file_cluster_1: 10.106
- **Magnitude:** 58.56 | **LOC:** 163 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_has_mixed` (Impact: 4.3 | O(N^3))
  * `test_has_nested_pseudo` (Impact: 4.3 | O(N^3))
  * `test_has_descendant` (Impact: 4.0 | O(N^3))
  * `test_has_next_sibling` (Impact: 4.0 | O(N^3))
  * `test_has_subsequent_sibling` (Impact: 4.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 17`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 12`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `doc: 32`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_is.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.376 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.632 IQR)
- **Top Global Matches:** file_cluster_8: 9.376, file_cluster_7: 9.675, file_cluster_1: 9.856
- **Magnitude:** 54.98 | **LOC:** 132 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multiple_is` (Impact: 4.5 | O(N^3))
    * *Intent:* # Each pseudo class is evaluated separately
  * `test_nested_is` (Impact: 4.3 | O(N^3))
  * `test_is_with_other_pseudo` (Impact: 4.1 | O(N^3))
    * *Intent:* # So this will not match self.assert_selector( self.MARKUP, ":is(span):not(span)", [], flags=util.HT...
  * `test_is` (Impact: 4.0 | O(N^3))
    * *Intent:* """ def test_is(self): """Test multiple selectors with "is"."""
  * `test_is_multi_comma` (Impact: 4.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 11`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `doc: 28`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_extra/test_custom.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.847 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.402 IQR)
- **Top Global Matches:** file_cluster_8: 8.847, file_cluster_7: 9.211, file_cluster_1: 9.391
- **Magnitude:** 51.24 | **LOC:** 144 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_custom_selectors` (Impact: 5.1 | O(N^3))
  * `test_custom_dependency` (Impact: 4.3 | O(N^3))
  * `test_custom_dependency_out_of_order` (Impact: 4.3 | O(N^3))
    * *Intent:* """Test custom selector out of order dependency."""
  * `test_custom_escapes` (Impact: 4.2 | O(N^3))
  * `test_custom_selectors_exotic` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 10`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 26`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_scope.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.093 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.499 IQR)
- **Top Global Matches:** file_cluster_8: 9.093, file_cluster_7: 9.388, file_cluster_13: 9.578
- **Magnitude:** 45.56 | **LOC:** 81 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.5899%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scope_is_select_target` (Impact: 27.2 | O(N^4))
  * `test_scope_cannot_select_target` (Impact: 9.2 | O(N^4))
  * `test_scope_is_root` (Impact: 4.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `doc: 12`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_nesting_1/test_amp.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.093 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.499 IQR)
- **Top Global Matches:** file_cluster_8: 9.093, file_cluster_7: 9.388, file_cluster_13: 9.578
- **Magnitude:** 45.56 | **LOC:** 81 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.5899%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_amp_is_select_target` (Impact: 27.2 | O(N^4))
  * `test_amp_cannot_select_target` (Impact: 9.2 | O(N^4))
  * `test_amp_is_root` (Impact: 4.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `doc: 12`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_extra/test_soup_contains_own.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.686 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.677 IQR)
- **Top Global Matches:** file_cluster_8: 9.686, file_cluster_7: 9.873, file_cluster_1: 10.084
- **Magnitude:** 44.82 | **LOC:** 113 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.6882%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_contains_own_cdata_lxml_html` (Impact: 11.2 | O(N^3))
  * `test_contains_own_cdata_html5` (Impact: 4.1 | O(N^3))
  * `test_contains_own_cdata_py_html` (Impact: 4.1 | O(N^3))
  * `test_contains_own_cdata_xml` (Impact: 4.1 | O(N^3))
  * `test_contains_own_with_broken_text` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 7`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `doc: 30`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lxml, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level3/test_nth_child.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.129 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.935 IQR)
- **Top Global Matches:** file_cluster_8: 8.129, file_cluster_7: 8.564, file_cluster_1: 8.761
- **Magnitude:** 43.18 | **LOC:** 247 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.4006%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_nth_child_no_parent` (Impact: 11.1 | O(N^3))
  * `test_nth_child_complex` (Impact: 5.5 | O(N^3))
  * `test_nth_child` (Impact: 5.2 | O(N^3))
  * `test_nth_child_odd` (Impact: 4.5 | O(N^3))
  * `test_nth_child_even` (Impact: 4.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 6`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `doc: 28`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` soupsieve, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level3/test_attribute.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.578 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.905 IQR)
- **Top Global Matches:** file_cluster_8: 9.578, file_cluster_7: 9.855, file_cluster_1: 10.033
- **Magnitude:** 42.3 | **LOC:** 113 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_attribute_contains` (Impact: 4.1 | O(N^3))
  * `test_attribute_begins` (Impact: 4.0 | O(N^3))
  * `test_attribute_end` (Impact: 4.0 | O(N^3))
  * `test_attribute_contains_with_newlines` (Impact: 4.0 | O(N^3))
  * `test_attribute_starts_with_newlines` (Impact: 4.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 8`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `doc: 24`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_in_range.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.592 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.471 IQR)
- **Top Global Matches:** file_cluster_8: 9.592, file_cluster_7: 9.826, file_cluster_1: 10.003
- **Magnitude:** 37.86 | **LOC:** 238 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_in_range_number` (Impact: 4.1 | O(N^3))
  * `test_in_range_range` (Impact: 4.1 | O(N^3))
    * *Intent:* <!-- These should not match -->
  * `test_in_range_month` (Impact: 4.1 | O(N^3))
  * `test_in_range_week` (Impact: 4.1 | O(N^3))
  * `test_in_range_date` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 7`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 32`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_out_of_range.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.592 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.471 IQR)
- **Top Global Matches:** file_cluster_8: 9.592, file_cluster_7: 9.826, file_cluster_1: 10.003
- **Magnitude:** 37.86 | **LOC:** 238 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_out_of_range_number` (Impact: 4.1 | O(N^3))
  * `test_out_of_range_range` (Impact: 4.1 | O(N^3))
    * *Intent:* <!-- These should match -->
  * `test_out_of_range_month` (Impact: 4.1 | O(N^3))
  * `test_out_of_range_week` (Impact: 4.1 | O(N^3))
  * `test_out_of_range_date` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 7`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 32`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `soupsieve-2.8.3/tests/test_bs4_cases.py` (PYTHON) | Magnitude: 25.14 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 33, test: 26, doc: 22
- `soupsieve-2.8.3/tests/test_quirks.py` (PYTHON) | Magnitude: 5.28 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 6, indent_spaces: 6, api: 2
- `soupsieve-2.8.3/tests/test_level1/test_at_rule.py` (PYTHON) | Magnitude: 4.88 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, api: 2, test: 2
- `soupsieve-2.8.3/tests/test_level1/test_pseudo_element.py` (PYTHON) | Magnitude: 4.88 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, api: 2, test: 2
- `soupsieve-2.8.3/tests/util.py` (PYTHON) | Magnitude: 150.4 | Delta: **0.243 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 70, doc: 32, structural_boundaries: 31, api: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `soupsieve-2.8.3/soupsieve/util.py` (PYTHON) | Magnitude: 124.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, state_mutation: 27, structural_boundaries: 21, branch: 14
- `soupsieve-2.8.3/soupsieve/css_match.py` (PYTHON) | Magnitude: 4157.26 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1078, branch: 603, structural_boundaries: 308, doc: 192
- `soupsieve-2.8.3/soupsieve/__init__.py` (PYTHON) | Magnitude: 31.14 | Delta: **0.417 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 36, generics: 25, doc: 20
- `soupsieve-2.8.3/soupsieve/css_types.py` (PYTHON) | Magnitude: 275.24 | Delta: **0.514 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 203, encapsulation: 101, doc: 94, structural_boundaries: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `soupsieve-2.8.3/tests/test_level1/test_list.py` (PYTHON) | Magnitude: 16.52 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 14, indent_spaces: 12, structural_boundaries: 9, api: 5
- `soupsieve-2.8.3/tests/test_api.py` (PYTHON) | Magnitude: 256.74 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 238, doc: 128, structural_boundaries: 68, test: 52
- `soupsieve-2.8.3/tests/test_level3/test_subsequent_sibling.py` (PYTHON) | Magnitude: 4.98 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 8, indent_spaces: 6, structural_boundaries: 4, api: 2
- `soupsieve-2.8.3/tests/test_level1/test_descendant.py` (PYTHON) | Magnitude: 4.98 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 8, indent_spaces: 6, structural_boundaries: 4, api: 2
- `soupsieve-2.8.3/tests/test_level2/test_first_child.py` (PYTHON) | Magnitude: 4.98 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 8, indent_spaces: 6, structural_boundaries: 4, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `soupsieve-2.8.3/soupsieve/pretty.py` -> **Severity: 0.493** (Embedded: 0.0095 * Error Risk: 51.7391%)
- `soupsieve-2.8.3/soupsieve/__meta__.py` -> **Severity: 0.091** (Embedded: 0.019 * Error Risk: 4.7884%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `soupsieve-2.8.3/soupsieve/util.py` -> **Severity: 920.976** (Blast Radius: 9.212 * Doc Risk: 99.9757%)
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **Severity: 920.862** (Blast Radius: 9.212 * Doc Risk: 99.9633%)
- `soupsieve-2.8.3/soupsieve/css_types.py` -> **Severity: 773.867** (Blast Radius: 9.212 * Doc Risk: 84.0064%)
- `soupsieve-2.8.3/soupsieve/__init__.py` -> **Severity: 509.746** (Blast Radius: 9.212 * Doc Risk: 55.335%)
- `soupsieve-2.8.3/soupsieve/__meta__.py` -> **Severity: 465.452** (Blast Radius: 24.874 * Doc Risk: 18.7124%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
