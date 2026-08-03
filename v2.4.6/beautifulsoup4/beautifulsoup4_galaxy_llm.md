# ARCHITECTURAL_BRIEF: beautifulsoup4
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/beautifulsoup4` |
| **Timestamp** | `2026-08-03T21:19:37.840603+00:00` |
| **Scan Duration** | `0.47s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 35 malicious artifacts.

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
| Total Artifacts | 72 |
| Analyzed Artifacts (Scanned) | 39 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 33 |
| Total LOC | 10025 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 54.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2197 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3134 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 15.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0969 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 32 | 9807 | 82.1% |
| PLAINTEXT | 3 | 0 | 7.7% |
| MAKEFILE | 3 | 218 | 7.7% |
| MARKDOWN | 1 | 0 | 2.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.548`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 17 | 43.6% |
| file_cluster_16 | 11 | 28.2% |
| file_cluster_13 | 6 | 15.4% |
| file_cluster_0 | 1 | 2.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 10.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 33*

**Composition by Extension & Reason:**
- `.testcase`: 16x Excluded (Unsupported Extension: '.testcase')
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 4x Excluded (Unsupported Extension: '.rst')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 256 LOC)
- `.jpg`: 3x Excluded (Explicitly Denied Extension: '.jpg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 24.6 | 7.7 | 4.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 14.4 | 0.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.5 | 5.9 | 4.7 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.1 | 27.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 90.0 | 6.4 | 0.0 | 0.0 |
| Specification Exposure | 53.3 | 100.0 | 97.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.0 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 68.1 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 59.3 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `beautifulsoup4-4.14.3/bs4/__init__.py` (Hits: 5)
- `beautifulsoup4-4.14.3/bs4/tests/test_fuzz.py` (Hits: 3)
- `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **element.py** (`beautifulsoup4-4.14.3/bs4/element.py`) — 17 inbound connections
2. **_typing.py** (`beautifulsoup4-4.14.3/bs4/_typing.py`) — 12 inbound connections
3. **filter.py** (`beautifulsoup4-4.14.3/bs4/filter.py`) — 8 inbound connections
4. **exceptions.py** (`beautifulsoup4-4.14.3/bs4/exceptions.py`) — 6 inbound connections
5. **dammit.py** (`beautifulsoup4-4.14.3/bs4/dammit.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`beautifulsoup4-4.14.3/bs4/__init__.py`) — 17 outbound dependencies
2. **diagnose.py** (`beautifulsoup4-4.14.3/bs4/diagnose.py`) — 15 outbound dependencies
3. **element.py** (`beautifulsoup4-4.14.3/bs4/element.py`) — 14 outbound dependencies
4. **__init__.py** (`beautifulsoup4-4.14.3/bs4/tests/__init__.py`) — 14 outbound dependencies
5. **__init__.py** (`beautifulsoup4-4.14.3/bs4/builder/__init__.py`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `deprecated_argument` (@ `beautifulsoup4-4.14.3/bs4/__init__.py`) -> Impact: **1868.2** | LOC: 748
- `quoted_attribute_value` (@ `beautifulsoup4-4.14.3/bs4/dammit.py`) -> Impact: **1418.1** | LOC: 961
- `matches_tag` (@ `beautifulsoup4-4.14.3/bs4/filter.py`) -> Impact: **245.7** | LOC: 65
  * *Intent:* # If you pass in 'class_' as part of kwargs, it's # because class is a Python reserved word. If you # pass it in as part of the attrs dict, it's # cal...
- `__init__` (@ `beautifulsoup4-4.14.3/bs4/builder/__init__.py`) -> Impact: **236.5** | LOC: 330
- `diagnose` (@ `beautifulsoup4-4.14.3/bs4/diagnose.py`) -> Impact: **82.5** | LOC: 51
- `handle_entityref` (@ `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py`) -> Impact: **72.1** | LOC: 143
- `lxml_trace` (@ `beautifulsoup4-4.14.3/bs4/diagnose.py`) -> Impact: **72.0** | LOC: 159
- `__setitem__` (@ `beautifulsoup4-4.14.3/bs4/element.py`) -> Impact: **71.5** | LOC: 29
- `feed` (@ `beautifulsoup4-4.14.3/bs4/builder/_lxml.py`) -> Impact: **63.6** | LOC: 25
  * *Intent:* # We were given Unicode. Maybe lxml can parse Unicode on # this system? # https://bugs.launchpad.net/lxml/+bug/1948551. # We can remove it once the up...
- `lookup` (@ `beautifulsoup4-4.14.3/bs4/builder/__init__.py`) -> Impact: **59.1** | LOC: 38

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `deprecated_argument` (@ `beautifulsoup4-4.14.3/bs4/__init__.py`) -> **O(2^N) [Recursive]**
- `quoted_attribute_value` (@ `beautifulsoup4-4.14.3/bs4/dammit.py`) -> **O(2^N) [Recursive]**
- `matches_tag` (@ `beautifulsoup4-4.14.3/bs4/filter.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # If you pass in 'class_' as part of kwargs, it's # because class is a Python reserved word. If you # pass it in as part of the attrs dict, it's # cal...
- `feed` (@ `beautifulsoup4-4.14.3/bs4/builder/_lxml.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # We were given Unicode. Maybe lxml can parse Unicode on # this system? # https://bugs.launchpad.net/lxml/+bug/1948551. # We can remove it once the up...
- `__init__` (@ `beautifulsoup4-4.14.3/bs4/builder/__init__.py`) -> **O(2^N) [Recursive]**
- `escape` (@ `beautifulsoup4-4.14.3/bs4/css.py`) -> **O(2^N) [Recursive]**
- `__setitem__` (@ `beautifulsoup4-4.14.3/bs4/element.py`) -> **O(2^N) [Recursive]**
- `handle_endtag` (@ `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Unlike other parsers, html.parser doesn't send separate end tag # handle_startendtag, but only if the original markup looked like # <tag/>.) # # So ...
- `feed` (@ `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py`) -> **O(2^N) [Recursive]**
- `feed` (@ `beautifulsoup4-4.14.3/bs4/builder/_lxml.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `deprecated_argument` (@ `beautifulsoup4-4.14.3/bs4/__init__.py`) -> DB Complexity: **45**
- `quoted_attribute_value` (@ `beautifulsoup4-4.14.3/bs4/dammit.py`) -> DB Complexity: **30**
- `test_formatter_custom` (@ `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py`) -> DB Complexity: **10**
- `__markup` (@ `beautifulsoup4-4.14.3/bs4/tests/test_fuzz.py`) -> DB Complexity: **9**
- `test_custom_builder_class` (@ `beautifulsoup4-4.14.3/bs4/tests/test_soup.py`) -> DB Complexity: **9**
  * *Intent:* # it'll be instantiated with the appropriate keyword arguments. class Mock(object): def __init__(self, **kwargs): self.called_with = kwargs self.is_xm...
- `test_smooth` (@ `beautifulsoup4-4.14.3/bs4/tests/test_tree.py`) -> DB Complexity: **8**
- `lxml_trace` (@ `beautifulsoup4-4.14.3/bs4/diagnose.py`) -> DB Complexity: **7**
- `handle_entityref` (@ `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py`) -> DB Complexity: **5**
- `__init__` (@ `beautifulsoup4-4.14.3/bs4/builder/__init__.py`) -> DB Complexity: **4**
- `register_treebuilders_from` (@ `beautifulsoup4-4.14.3/bs4/builder/__init__.py`) -> DB Complexity: **4**
  * *Intent:* # TODO: This cast will fail in the (very unlikely) scenario # that the programmer who instantiates the TreeBuilder # specifies meta['content'] or meta...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `beautifulsoup4-4.14.3/bs4` | 11 | 5119.46 | 11.76% | 24.8% |
| `beautifulsoup4-4.14.3/bs4/tests` | 16 | 2862.92 | 2.86% | 0.0% |
| `beautifulsoup4-4.14.3/bs4/builder` | 3 | 924.76 | 18.36% | 70.11% |
| `beautifulsoup4-4.14.3` | 4 | 101.42 | 0.0% | 0.0% |
| `beautifulsoup4-4.14.3/doc.es` | 2 | 65.4 | 8.87% | 0.0% |
| `beautifulsoup4-4.14.3/doc.ru` | 1 | 49.1 | 5.1% | 0.0% |
| `beautifulsoup4-4.14.3/doc` | 2 | 31.46 | 8.82% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **99.9999%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **99.9527%** Exposure
- `beautifulsoup4-4.14.3/bs4/formatter.py` -> **96.1368%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **72.6236%** Exposure
- `beautifulsoup4-4.14.3/bs4/element.py` -> **41.7055%** Exposure
### Highest State Flux (Mutation/Volatility)
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **99.0664%** Exposure
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **97.6806%** Exposure
- `beautifulsoup4-4.14.3/bs4/formatter.py` -> **94.5979%** Exposure
- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **93.6499%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **91.705%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` -> **135** Orphaned Functions | **8** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/__init__.py` -> **40** Orphaned Functions | **4** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_filter.py` -> **29** Orphaned Functions | **4** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` -> **30** Orphaned Functions | **0** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_dammit.py` -> **29** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`beautifulsoup4-4.14.3/bs4/__init__.py`** -> AI Confidence: **99.31%**
2. **`beautifulsoup4-4.14.3/bs4/dammit.py`** -> AI Confidence: **99.31%**
3. **`beautifulsoup4-4.14.3/bs4/filter.py`** -> AI Confidence: **99.31%**
4. **`beautifulsoup4-4.14.3/bs4/element.py`** -> AI Confidence: **99.24%**
5. **`beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py`** -> AI Confidence: **99.23%**
6. **`beautifulsoup4-4.14.3/bs4/builder/__init__.py`** -> AI Confidence: **99.16%**
7. **`beautifulsoup4-4.14.3/bs4/builder/_lxml.py`** -> AI Confidence: **99.16%**
8. **`beautifulsoup4-4.14.3/bs4/diagnose.py`** -> AI Confidence: **99.16%**
9. **`beautifulsoup4-4.14.3/bs4/tests/__init__.py`** -> AI Confidence: **99.08%**
10. **`beautifulsoup4-4.14.3/bs4/tests/test_htmlparser.py`** -> AI Confidence: **99.08%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `beautifulsoup4-4.14.3/bs4/tests/test_dammit.py` -> **0.0053%** Exposure
- `beautifulsoup4-4.14.3/bs4/tests/test_htmlparser.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/dammit.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/dammit.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `216` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `beautifulsoup4-4.14.3/bs4/filter.py` (PYTHON) -> Cumulative Risk: **805.41**
- **Archetype:** `file_cluster_16` (Distance: 11.945 IQR)
- **Magnitude:** 696.24 | **LOC:** 765 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `matches_tag` (Impact: 245.7), `excludes_everything` (Impact: 48.5), `filter` (Impact: 37.1)

### 2. `beautifulsoup4-4.14.3/bs4/builder/__init__.py` (PYTHON) -> Cumulative Risk: **733.56**
- **Archetype:** `file_cluster_16` (Distance: 11.14 IQR)
- **Magnitude:** 437.8 | **LOC:** 849 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (91.705%)
- **Heaviest Functions:** `__init__` (Impact: 236.5), `lookup` (Impact: 59.1), `register_treebuilders_from` (Impact: 12.6)

### 3. `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` (PYTHON) -> Cumulative Risk: **698.01**
- **Archetype:** `file_cluster_16` (Distance: 12.058 IQR)
- **Magnitude:** 283.16 | **LOC:** 502 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9527%)
- **Heaviest Functions:** `feed` (Impact: 63.6), `end` (Impact: 37.5), `_register_namespaces` (Impact: 20.7)

### 4. `beautifulsoup4-4.14.3/bs4/diagnose.py` (PYTHON) -> Cumulative Risk: **654.79**
- **Archetype:** `file_cluster_13` (Distance: 11.672 IQR)
- **Magnitude:** 193.84 | **LOC:** 269 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (97.4289%)
- **Heaviest Functions:** `diagnose` (Impact: 82.5), `lxml_trace` (Impact: 72.0)

### 5. `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` (PYTHON) -> Cumulative Risk: **626.96**
- **Archetype:** `file_cluster_16` (Distance: 11.153 IQR)
- **Magnitude:** 203.8 | **LOC:** 463 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (89.7011%)
- **Heaviest Functions:** `handle_entityref` (Impact: 72.1), `handle_endtag` (Impact: 32.6), `handle_charref` (Impact: 18.3)

### 6. `beautifulsoup4-4.14.3/bs4/__init__.py` (PYTHON) -> Cumulative Risk: **608.45**
- **Archetype:** `file_cluster_16` (Distance: 11.576 IQR)
- **Magnitude:** 1989.04 | **LOC:** 1175 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (93.6499%)
- **Heaviest Functions:** `deprecated_argument` (Impact: 1868.2), `__init__` (Impact: 2.0)

### 7. `beautifulsoup4-4.14.3/bs4/dammit.py` (PYTHON) -> Cumulative Risk: **572.18**
- **Archetype:** `file_cluster_16` (Distance: 11.185 IQR)
- **Magnitude:** 1561.4 | **LOC:** 1517 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (85.7261%)
- **Heaviest Functions:** `quoted_attribute_value` (Impact: 1418.1), `_chardet_dammit` (Impact: 9.3), `_substitute_html_entity` (Impact: 7.3)

### 8. `beautifulsoup4-4.14.3/bs4/element.py` (PYTHON) -> Cumulative Risk: **513.4**
- **Archetype:** `file_cluster_16` (Distance: 12.098 IQR)
- **Magnitude:** 481.64 | **LOC:** 3212 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (87.5046%), Verification (80.0%)
- **Heaviest Functions:** `__setitem__` (Impact: 71.5), `__setitem__` (Impact: 33.0), `substitute_encoding` (Impact: 7.2)

### 9. `beautifulsoup4-4.14.3/bs4/css.py` (PYTHON) -> Cumulative Risk: **443.46**
- **Archetype:** `file_cluster_16` (Distance: 9.75 IQR)
- **Magnitude:** 67.98 | **LOC:** 340 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9905%), Verification (80.0%), Safety Score (72.6357%)
- **Heaviest Functions:** `escape` (Impact: 17.7), `__init__` (Impact: 15.4), `select` (Impact: 3.4)

### 10. `beautifulsoup4-4.14.3/bs4/_deprecation.py` (PYTHON) -> Cumulative Risk: **438.96**
- **Archetype:** `file_cluster_16` (Distance: 9.118 IQR)
- **Magnitude:** 24.82 | **LOC:** 81 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9998%), Algorithmic Dos (99.7582%), Safety Score (80.0%)
- **Heaviest Functions:** `_deprecated_alias` (Impact: 5.2), `_deprecated` (Impact: 5.1), `alias` (Impact: 4.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `beautifulsoup4-4.14.3/bs4/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.576 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.82 IQR)
- **Top Global Matches:** file_cluster_16: 11.576, file_cluster_13: 11.695, file_cluster_8: 11.772
- **Magnitude:** 1989.04 | **LOC:** 1175 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (14.5537%), Tech Debt (9.2521%)
**Top Internal Functions/Classes:**
  * `deprecated_argument` (Impact: 1868.2 | O(2^N) | DB: 45)
  * `__init__` (Impact: 2.0 | O(N^2))
    * *Intent:* #: want, look for one with these features. DEFAULT_BUILDER_FEATURES: Sequence[str] = ["html", "fast"...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 114`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 86`, `planned_debt: 2`
* *Architecture:* `io: 5`, `api: 19`, `import: 17`
* *Defense:* `safety: 25`, `doc: 88`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` bs4._typing, .builder._htmlparser, .css, ._deprecation, .dammit, .formatter, bs4, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/dammit.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.185 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.547 IQR)
- **Top Global Matches:** file_cluster_16: 11.185, file_cluster_13: 11.276, file_cluster_8: 11.305
- **Magnitude:** 1561.4 | **LOC:** 1517 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (20.6857%), Tech Debt (8.9628%)
**Top Internal Functions/Classes:**
  * `quoted_attribute_value` (Impact: 1418.1 | O(2^N) | DB: 30)
  * `_chardet_dammit` (Impact: 9.3 | O(N^2))
  * `_substitute_html_entity` (Impact: 7.3 | O(N^3))
    * *Intent:* #: A map of Unicode strings to the corresponding named XML entities. #: #: :meta hide-value:
  * `_escape_unrecognized_entity_name` (Impact: 7.2 | O(N^3))
    * *Intent:* #: A regular expression matching an angle bracket or an ampersand. #:
  * `_substitute_xml_entity` (Impact: 3.0 | O(N^2))
    * *Intent:* #: A regular expression matching an angle bracket or an ampersand that #: is not part of an XML or H...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 102`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 84`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 16`, `import: 14`
* *Defense:* `safety: 17`, `doc: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.512
  * `Choke Point (Betweenness):` 0.004979 | `Ripple Effect (Closeness):` 0.257797
  * `Imports (Out-Degree: 1):` bs4._typing, chardet, html.entities, types, typing_extensions, charset_normalizer, warnings, collections...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.056 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.89 IQR)
- **Top Global Matches:** file_cluster_8: 13.056, file_cluster_0: 13.321, file_cluster_13: 13.346
- **Magnitude:** 834.7 | **LOC:** 1460 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (3.0229%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_suspicious_syntax_warning` (Impact: 18.0 | O(N^4))
  * `test_replace_with_errors` (Impact: 14.6 | O(N^3))
  * `test_insert_after_raises_exception_if_af` (Impact: 14.4 | O(N^3))
  * `test_insert_before_raises_notimplemented` (Impact: 14.4 | O(N^3))
    * *Intent:* # Can't insert an element after itself. b = soup.b with pytest.raises(ValueError): b.insert_after(b)...
  * `test_parent_generator` (Impact: 14.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 446`, `args: 152`, `func_start: 146`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 57`, `planned_debt: 2`, `duplicate_logic: 8`, `orphaned_logic: 135`
* *Architecture:* `api: 163`, `import: 8`
* *Defense:* `safety: 262`, `doc: 66`, `test: 411`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4.element, bs4.builder, pytest, bs4.filter, warnings, re, , bs4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/filter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.945 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.793 IQR)
- **Top Global Matches:** file_cluster_16: 11.945, file_cluster_13: 12.056, file_cluster_0: 12.106
- **Magnitude:** 696.24 | **LOC:** 765 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (24.6174%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `matches_tag` (Impact: 245.7 | O(2^N))
    * *Intent:* # If you pass in 'class_' as part of kwargs, it's # because class is a Python reserved word. If you ...
  * `excludes_everything` (Impact: 48.5 | O(N^4))
  * `filter` (Impact: 37.1 | O(N^5))
  * `_base_match` (Impact: 31.7 | O(N^4) | DB: 1)
  * `match` (Impact: 28.8 | O(N^3))
    * *Intent:* # attrs = " ".join( # [f"{k}={v}" for k, v in sorted(tag.attrs.items())] # print(f"Testing <{tag.nam...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 123`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 59`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 31`, `import: 8`
* *Defense:* `safety: 17`, `doc: 72`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.977
  * `Choke Point (Betweenness):` 0.003556 | `Ripple Effect (Closeness):` 0.309357
  * `Imports (Out-Degree: 3):` bs4._deprecation, bs4.element, bs4._typing, __future__, warnings, collections, re, typing
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/element.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.098 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.771 IQR)
- **Top Global Matches:** file_cluster_16: 12.098, file_cluster_0: 12.392, file_cluster_13: 12.495
- **Magnitude:** 481.64 | **LOC:** 3212 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.7963%), Tech Debt (41.7055%)
**Top Internal Functions/Classes:**
  * `__setitem__` (Impact: 71.5 | O(2^N))
  * `__setitem__` (Impact: 33.0 | O(2^N))
    * *Intent:* """ if eventual_encoding in PYTHON_SPECIFIC_ENCODINGS: return "" return eventual_encoding class Attr...
  * `substitute_encoding` (Impact: 7.2 | O(N^3))
  * `__getattr__` (Impact: 6.3 | O(N^2))
  * `__new__` (Impact: 5.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 362`, `args: 150`, `func_start: 150`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 183`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 129`, `import: 17`
* *Defense:* `safety: 54`, `doc: 397`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 232.515
  * `Choke Point (Betweenness):` 0.078592 | `Ripple Effect (Closeness):` 0.464035
  * `Imports (Out-Degree: 6):` bs4._deprecation, bs4._typing, typing_extensions, __future__, bs4.builder, bs4.filter, bs4.formatter, SoupStrainer...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/builder/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.14 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.43 IQR)
- **Top Global Matches:** file_cluster_16: 11.14, file_cluster_13: 11.309, file_cluster_8: 11.526
- **Magnitude:** 437.8 | **LOC:** 849 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.234%), Tech Debt (72.6236%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 236.5 | O(2^N) | DB: 4)
  * `lookup` (Impact: 59.1 | O(N^5) | DB: 1)
  * `register_treebuilders_from` (Impact: 12.6 | O(N^3) | DB: 4)
    * *Intent:* # TODO: This cast will fail in the (very unlikely) scenario # that the programmer who instantiates t...
  * `register` (Impact: 7.2 | O(N^3) | DB: 2)
  * `can_be_empty_element` (Impact: 7.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 100`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 48`, `planned_debt: 3`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 37`, `import: 17`
* *Defense:* `safety: 11`, `doc: 67`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bs4._typing, bs4.element, types, __future__, warnings, collections, bs4._warnings, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.135 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.797 IQR)
- **Top Global Matches:** file_cluster_8: 12.135, file_cluster_13: 12.393, file_cluster_7: 12.468
- **Magnitude:** 395.68 | **LOC:** 1349 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (1.6823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_html5_style_meta_tag_reflects_curre` (Impact: 25.4 | O(N^5) | DB: 3)
    * *Intent:* # Encode it to UTF-8. result = soup.encode("utf-8") # What do we expect the result to look like? Wel...
  * `test_real_xhtml_document` (Impact: 19.2 | O(N^6))
    * *Intent:* """Generate and parse a document with the given doctype."""
  * `test_angle_brackets_in_attribute_values_` (Impact: 17.5 | O(N^3))
    * *Intent:* """Inline elements can be nested indefinitely."""
  * `test_python_specific_encodings_not_used_` (Impact: 14.1 | O(N^4))
    * *Intent:* # You can encode an HTML document using a Python-specific # encoding, but that encoding won't be men...
  * `assertConnectedness` (Impact: 13.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 320`, `args: 109`, `func_start: 109`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`, `dead_code: 2`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 40`
* *Architecture:* `io: 1`, `api: 113`, `import: 15`
* *Defense:* `safety: 166`, `doc: 98`, `test: 250`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bs4._typing, bs4.element, pytest, pickle, bs4.filter, importlib, bs4.builder, soupsieve...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_filter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.856 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.977 IQR)
- **Top Global Matches:** file_cluster_8: 11.856, file_cluster_0: 12.025, file_cluster_13: 12.147
- **Magnitude:** 327.62 | **LOC:** 702 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.0778%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_match` (Impact: 25.2 | O(N^3))
  * `test_allow_tag_creation` (Impact: 23.0 | O(N^5))
    * *Intent:* # By default, ElementFilter.allow_tag_creation allows everything. filter = ElementFilter() f = filte...
  * `test_empty_match_not_allowed` (Impact: 14.2 | O(N^3))
  * `test_full_match_not_allowed` (Impact: 14.2 | O(N^3))
  * `test_parse_only_combining_tag_and_string` (Impact: 14.1 | O(N^4))
    * *Intent:* # If you pass parse_only a SoupStrainer that contains both tag # restrictions and string restriction...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 213`, `args: 50`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 29`
* *Architecture:* `api: 46`, `import: 8`
* *Defense:* `safety: 120`, `doc: 4`, `test: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bs4._typing, bs4.element, pytest, bs4.filter, warnings, re, typing, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.058 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.843 IQR)
- **Top Global Matches:** file_cluster_16: 12.058, file_cluster_13: 12.117, file_cluster_8: 12.41
- **Magnitude:** 283.16 | **LOC:** 502 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (22.8095%), Tech Debt (99.9527%)
**Top Internal Functions/Classes:**
  * `feed` (Impact: 63.6 | O(2^N) | DB: 1)
    * *Intent:* # We were given Unicode. Maybe lxml can parse Unicode on # this system? # https://bugs.launchpad.net...
  * `end` (Impact: 37.5 | O(N^5) | DB: 2)
    * *Intent:* # Also treat the namespace mapping as a set of attributes on the # tag, so we can recreate it later.
  * `_register_namespaces` (Impact: 20.7 | O(N^4))
    * *Intent:* # Beyond this point, self.soup is set, so we can assume (and # assert) it's not None whenever necess...
  * `feed` (Impact: 14.4 | O(2^N) | DB: 1)
  * `_getNsTag` (Impact: 10.7 | O(N^3))
    * *Intent:* **kwargs: Any, # TODO: Issue a warning if parser is present but not a # callable, since that means t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 80`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 50`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 23`, `import: 12`
* *Defense:* `safety: 29`, `doc: 25`, `test: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.788
  * `Choke Point (Betweenness):` 0.009602 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 4):` bs4._typing, bs4.element, bs4.dammit, typing_extensions, __future__, bs4.builder, io, lxml...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.735 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.361 IQR)
- **Top Global Matches:** file_cluster_8: 11.735, file_cluster_13: 11.821, file_cluster_0: 11.875
- **Magnitude:** 274.0 | **LOC:** 603 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (3.3926%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_custom_builder_class` (Impact: 18.8 | O(N^5) | DB: 9)
    * *Intent:* # it'll be instantiated with the appropriate keyword arguments. class Mock(object): def __init__(sel...
  * `test_cdata_list_attributes` (Impact: 17.1 | O(N^5))
    * *Intent:* # HTML standard says that some attributes, like 'class' have # space-separated lists as values. mark...
  * `test_parser_markup_rejection` (Impact: 14.0 | O(N^4))
    * *Intent:* # explanatory ParserRejectedMarkup exception is raised. class Mock(TreeBuilder): def feed(self, *arg...
  * `test_ascii_in_unicode_out` (Impact: 14.0 | O(N^4))
    * *Intent:* # ASCII input is converted to Unicode. The original_encoding # attribute is set to 'utf-8', a supers...
  * `test_invalid_markup_type` (Impact: 10.7 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 194`, `args: 50`, `func_start: 49`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 11`, `fragile_debt: 1`, `orphaned_logic: 30`
* *Architecture:* `io: 1`, `api: 61`, `import: 13`
* *Defense:* `safety: 86`, `doc: 6`, `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bs4.element, pytest, pickle, bs4.builder, bs4.filter, warnings, logging, bs4._warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_css.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.802 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.672 IQR)
- **Top Global Matches:** file_cluster_8: 10.802, file_cluster_13: 11.344, file_cluster_7: 11.377
- **Magnitude:** 212.66 | **LOC:** 537 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.0429%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_id_child_selector_nth_of_type` (Impact: 30.7 | O(N^3))
  * `test_multi_class_support` (Impact: 11.5 | O(N^3))
  * `test_items_in_id` (Impact: 10.9 | O(N^3))
  * `test_unsupported_pseudoclass` (Impact: 10.7 | O(N^3))
  * `test_one_id` (Impact: 7.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 148`, `args: 63`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 64`, `import: 7`
* *Defense:* `safety: 55`, `doc: 6`, `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, pytest, packaging.version, soupsieve, typing, , bs4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.153 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.473 IQR)
- **Top Global Matches:** file_cluster_16: 11.153, file_cluster_13: 11.185, file_cluster_8: 11.579
- **Magnitude:** 203.8 | **LOC:** 463 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (15.0456%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `handle_entityref` (Impact: 72.1 | O(N^4) | DB: 5)
  * `handle_endtag` (Impact: 32.6 | O(2^N) | DB: 1)
    * *Intent:* # Unlike other parsers, html.parser doesn't send separate end tag # handle_startendtag, but only if ...
  * `handle_charref` (Impact: 18.3 | O(N^3))
  * `feed` (Impact: 17.4 | O(2^N))
  * `handle_data` (Impact: 5.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 43`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 25`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 20`, `import: 10`
* *Defense:* `safety: 6`, `doc: 52`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.623
  * `Choke Point (Betweenness):` 0.010313 | `Ripple Effect (Closeness):` 0.105263
  * `Imports (Out-Degree: 4):` bs4._typing, bs4.element, bs4.dammit, html.parser, __future__, bs4.builder, typing, bs4.exceptions...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/diagnose.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.672 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.039 IQR)
- **Top Global Matches:** file_cluster_13: 11.672, file_cluster_16: 11.917, file_cluster_8: 12.127
- **Magnitude:** 193.84 | **LOC:** 269 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (10.3156%), Tech Debt (16.7731%)
**Top Internal Functions/Classes:**
  * `diagnose` (Impact: 82.5 | O(N^4) | DB: 2)
  * `lxml_trace` (Impact: 72.0 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 51`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 18`, `import: 19`
* *Defense:* `safety: 11`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bs4._typing, html.parser, tempfile, bs4.builder, traceback, time, html5lib, pstats...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_dammit.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.227 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_8: 11.227, file_cluster_0: 11.573, file_cluster_13: 11.694
- **Magnitude:** 192.82 | **LOC:** 513 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (2.2353%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_last_ditch_entity_replacement` (Impact: 14.7 | O(N^4))
    * *Intent:* # completely incompatible with UTF-8 (ie. encoded with some other # encoding). # # Since there is no...
  * `test_deprecated_override_encodings` (Impact: 14.1 | O(N^4))
    * *Intent:* # override_encodings is a deprecated alias for # known_definite_encodings. hebrew = b"\xed\xe5\xec\x...
  * `test_known_definite_versus_user_encoding` (Impact: 11.9 | O(N^3))
    * *Intent:* # The known_definite_encodings are used before sniffing the # byte-order mark; the user_encodings ar...
  * `test_html5_entity` (Impact: 8.2 | O(N^3))
    * *Intent:* # A few spot checks of our ability to recognize # special character sequences and convert them # to ...
  * `test_detwingle` (Impact: 8.1 | O(N^3))
    * *Intent:* # Here's a UTF8 document. utf8 = ("\N{SNOWMAN}" * 3).encode("utf8") # Here's a Windows-1252 document...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 124`, `args: 39`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 29`
* *Architecture:* `api: 43`, `import: 6`
* *Defense:* `safety: 74`, `doc: 10`, `test: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bs4.dammit, pytest, warnings, logging, bs4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.009 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.701 IQR)
- **Top Global Matches:** file_cluster_8: 12.009, file_cluster_13: 12.157, file_cluster_7: 12.437
- **Magnitude:** 104.28 | **LOC:** 438 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (1.5956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_encoding_substitutes_unrecognized_c` (Impact: 22.4 | O(N^3) | DB: 3)
  * `test_formatter_custom` (Impact: 20.8 | O(N^3) | DB: 10)
  * `test_unicode_string_can_be_encoded` (Impact: 2.8 | O(N^2))
  * `test_tag_containing_unicode_string_can_b` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 139`, `args: 42`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `state_mutation: 7`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 43`, `import: 9`
* *Defense:* `safety: 74`, `doc: 16`, `test: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4.element, pytest, pickle, bs4.filter, warnings, , sys, copy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_builder_registry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.922 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.704 IQR)
- **Top Global Matches:** file_cluster_13: 11.922, file_cluster_8: 12.063, file_cluster_7: 12.478
- **Magnitude:** 99.32 | **LOC:** 140 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (2.8843%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lookup_by_markup_type` (Impact: 22.2 | O(N^4))
  * `test_beautifulsoup_constructor_does_look` (Impact: 11.1 | O(N^3))
    * *Intent:* # specifying a parser, but we'll ignore it. # You can pass in a string. BeautifulSoup("", features="...
  * `test_named_library` (Impact: 10.8 | O(N^3))
  * `test_combination` (Impact: 10.7 | O(N^3))
  * `builder_for_features` (Impact: 3.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 58`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 23`, `doc: 6`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4.builder._html5lib, bs4.builder, pytest, warnings, bs4.builder._lxml, typing, bs4.builder._htmlparser, ...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_tag.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.906 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.01 IQR)
- **Top Global Matches:** file_cluster_8: 12.906, file_cluster_13: 13.154, file_cluster_16: 13.199
- **Magnitude:** 76.52 | **LOC:** 242 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (1.5134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_deprecated_member_access` (Impact: 10.8 | O(N^3))
  * `test__should_pretty_print` (Impact: 3.5 | O(N^2))
  * `test_len` (Impact: 3.3 | O(N^2))
  * `test_tag_with_multiple_children_has_no_s` (Impact: 3.2 | O(N^2) | DB: 1)
    * *Intent:* # A Tag with no children has no .stirng.
  * `test_lack_of_string` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 101`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 57`, `doc: 14`, `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, , bs4.element
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_formatter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.846 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.589 IQR)
- **Top Global Matches:** file_cluster_8: 10.846, file_cluster_0: 11.007, file_cluster_13: 11.054
- **Magnitude:** 70.5 | **LOC:** 171 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.7929%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_empty_attributes_are_booleans` (Impact: 22.2 | O(N^5))
    * *Intent:* # Test the behavior of empty_attributes_are_booleans as well # as which Formatters have it enabled. ...
  * `test_sort_attributes` (Impact: 19.1 | O(N^6) | DB: 1)
    * *Intent:* # Test the ability to override Formatter.attributes() to, # e.g., disable the normal sorting of attr...
  * `test_default_attributes` (Impact: 3.5 | O(N^2))
    * *Intent:* # Test the default behavior of Formatter.attributes(). formatter = Formatter() tag = Tag(name="tag")...
  * `test_indent` (Impact: 3.5 | O(N^2))
    * *Intent:* # Pretty-print a tree with a Formatter set to # indent in a certain way and verify the results. soup...
  * `test_indent_subclasses` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 43`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 24`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, , bs4.element, bs4.formatter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/css.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.75 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.766 IQR)
- **Top Global Matches:** file_cluster_16: 9.75, file_cluster_13: 9.952, file_cluster_8: 10.146
- **Magnitude:** 67.98 | **LOC:** 340 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.5059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `escape` (Impact: 17.7 | O(2^N))
  * `__init__` (Impact: 15.4 | O(N^4) | DB: 2)
  * `select` (Impact: 3.4 | O(2^N))
    * *Intent:* # Import here to avoid circular import
  * `match` (Impact: 3.3 | O(N^2))
  * `_rs` (Impact: 2.9 | O(N^2))
    * *Intent:* """Escape a CSS identifier. This is a simple wrapper around `soupsieve.escape() <https://facelessuse...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 40`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 2`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 3`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272962
  * `Imports (Out-Degree: 2):` bs4._typing, bs4.element, types, __future__, soupsieve, warnings, typing, bs4
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_element.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.179 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.914 IQR)
- **Top Global Matches:** file_cluster_8: 12.179, file_cluster_13: 12.591, file_cluster_7: 12.671
- **Magnitude:** 62.62 | **LOC:** 179 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.4886%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_getattr_exception` (Impact: 7.4 | O(N^3))
  * `test_content_meta_attribute_value` (Impact: 5.3 | O(N^2))
    * *Intent:* # no encoding will be mentioned in the output HTML. assert "" == value.substitute_encoding("palmos")...
  * `test_equality` (Impact: 3.4 | O(N^2))
    * *Intent:* # __getitem__ is delegated to the result sequence.
  * `test_attributes_are_equivalent_if_prefix` (Impact: 3.3 | O(N^2))
  * `test_charset_meta_attribute_value` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 66`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `orphaned_logic: 12`
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `safety: 42`, `doc: 6`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, bs4.filter, bs4.element
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_htmlparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.387 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.249 IQR)
- **Top Global Matches:** file_cluster_13: 11.387, file_cluster_8: 11.438, file_cluster_7: 11.916
- **Magnitude:** 62.36 | **LOC:** 165 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (2.7602%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_empty_element` (Impact: 18.0 | O(N^4) | DB: 1)
  * `test_feed_raises_correct_exception_on_re` (Impact: 9.3 | O(N^4))
    * *Intent:* # Mock BeautifulSoupHTMLParser so it raises an AssertionError and verify that this is # turned into ...
  * `test_surrogate_in_character_reference` (Impact: 3.0 | O(N^2))
  * `test_builder_is_pickled` (Impact: 2.9 | O(N^2) | DB: 2)
    * *Intent:* """Unlike most tree builders, HTMLParserTreeBuilder can be pickled and will be restored after pickli...
  * `test_namespaced_system_doctype` (Impact: 2.7 | O(N^2))
    * *Intent:* # html.parser can't handle namespaced doctypes, so skip this one. pass def test_namespaced_public_do...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 53`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 16`, `import: 7`
* *Defense:* `safety: 21`, `doc: 4`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, pickle, typing, bs4.builder._htmlparser, bs4.exceptions, , bs4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/formatter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.486 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.388 IQR)
- **Top Global Matches:** file_cluster_16: 10.486, file_cluster_13: 10.743, file_cluster_8: 10.8
- **Magnitude:** 58.6 | **LOC:** 277 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.4326%), Tech Debt (96.1368%)
**Top Internal Functions/Classes:**
  * `substitute` (Impact: 18.1 | O(N^3))
  * `attribute_value` (Impact: 2.8 | O(N^2))
  * `__init__` (Impact: 1.9 | O(N^2))
  * `__init__` (Impact: 1.9 | O(N^2))
  * `__init__` (Impact: 1.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 31`, `args: 7`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `duplicate_logic: 3`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 3`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 46.737
  * `Choke Point (Betweenness):` 0.010313 | `Ripple Effect (Closeness):` 0.278421
  * `Imports (Out-Degree: 3):` bs4._typing, bs4.dammit, typing_extensions, __future__, typing, .element
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_navigablestring.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.601 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.871 IQR)
- **Top Global Matches:** file_cluster_8: 12.601, file_cluster_13: 12.793, file_cluster_17: 12.969
- **Magnitude:** 52.54 | **LOC:** 156 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.1894%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_string_detects_attribute_access_att` (Impact: 7.5 | O(N^3))
  * `test_string_has_immutable_name_property` (Impact: 7.2 | O(N^3))
    * *Intent:* # string.name is defined as None and can't be modified string = self.soup("s").string assert None is...
  * `test_text_acquisition_methods` (Impact: 4.2 | O(N^2))
    * *Intent:* # These methods are intended for use against Tag, but they # work on NavigableString as well, s = Na...
  * `test_cdata_is_never_formatted` (Impact: 4.2 | O(N^3) | DB: 2)
    * *Intent:* """Text inside a CData object is passed into the formatter. But the return value is ignored. """
  * `test_cdata` (Impact: 3.0 | O(N^2) | DB: 1)
    * *Intent:* # None of the current builders turn CDATA sections into CData # objects, but you can create them man...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 57`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 8`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 43`, `doc: 2`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, , bs4.element
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/CHANGELOG` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 49.32 | **LOC:** 2466 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/NEWS.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 49.32 | **LOC:** 2466 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `beautifulsoup4-4.14.3/bs4/tests/test_lxml.py` (PYTHON) | Magnitude: 19.32 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 57, test: 41, safety: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `beautifulsoup4-4.14.3/bs4/exceptions.py` (PYTHON) | Magnitude: 19.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 6, indent_spaces: 5, class_start: 3
- `beautifulsoup4-4.14.3/bs4/tests/test_htmlparser.py` (PYTHON) | Magnitude: 62.36 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 53, test: 34, safety: 21
- `beautifulsoup4-4.14.3/doc.es/conf.py` (PYTHON) | Magnitude: 16.3 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 3, structural_boundaries: 2, io: 2, import: 2
- `beautifulsoup4-4.14.3/doc/conf.py` (PYTHON) | Magnitude: 16.3 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 3, structural_boundaries: 2, io: 2, import: 2
- `beautifulsoup4-4.14.3/bs4/tests/test_builder_registry.py` (PYTHON) | Magnitude: 99.32 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 58, test: 36, safety: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` (PYTHON) | Magnitude: 203.8 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 207, doc: 52, structural_boundaries: 43, branch: 36
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` (PYTHON) | Magnitude: 283.16 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 80, encapsulation: 60, state_mutation: 50
- `beautifulsoup4-4.14.3/bs4/dammit.py` (PYTHON) | Magnitude: 1561.4 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 795, sec_reflection_metaprogramming: 457, branch: 139, structural_boundaries: 102
- `beautifulsoup4-4.14.3/bs4/filter.py` (PYTHON) | Magnitude: 696.24 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 375, branch: 136, structural_boundaries: 123, encapsulation: 84
- `beautifulsoup4-4.14.3/bs4/__init__.py` (PYTHON) | Magnitude: 1989.04 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 656, branch: 161, structural_boundaries: 114, doc: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `beautifulsoup4-4.14.3/bs4/tests/test_fuzz.py` (PYTHON) | Magnitude: 44.9 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 20, test: 14, safety: 9
- `beautifulsoup4-4.14.3/bs4/_warnings.py` (PYTHON) | Magnitude: 20.3 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 24, indent_spaces: 10, structural_boundaries: 5, class_start: 5
- `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` (PYTHON) | Magnitude: 274.0 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 398, structural_boundaries: 194, test: 126, safety: 86
- `beautifulsoup4-4.14.3/bs4/tests/test_builder.py` (PYTHON) | Magnitude: 33.08 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, test: 9, branch: 4
- `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py` (PYTHON) | Magnitude: 104.28 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 139, test: 112, safety: 74

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 6.877** (Bridge: 0.0786 * Flux: 87.5046%)
- `beautifulsoup4-4.14.3/bs4/formatter.py` -> **Severity: 0.976** (Bridge: 0.0103 * Flux: 94.5979%)
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **Severity: 0.951** (Bridge: 0.0096 * Flux: 99.0664%)
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` -> **Severity: 0.925** (Bridge: 0.0103 * Flux: 89.7011%)
- `beautifulsoup4-4.14.3/bs4/dammit.py` -> **Severity: 0.427** (Bridge: 0.005 * Flux: 85.7261%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `beautifulsoup4-4.14.3/bs4/_deprecation.py` -> **Severity: 23.32** (Embedded: 0.2915 * Error Risk: 80.0%)
- `beautifulsoup4-4.14.3/bs4/css.py` -> **Severity: 19.827** (Embedded: 0.273 * Error Risk: 72.6357%)
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **Severity: 14.41** (Embedded: 0.3094 * Error Risk: 46.5816%)
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` -> **Severity: 6.667** (Embedded: 0.1053 * Error Risk: 63.3333%)
- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 3.854** (Embedded: 0.464 * Error Risk: 8.3045%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `beautifulsoup4-4.14.3/bs4/_deprecation.py` -> **Severity: 6013.088** (Blast Radius: 60.131 * Doc Risk: 99.9998%)
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **Severity: 5962.752** (Blast Radius: 60.977 * Doc Risk: 97.7869%)
- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 2771.649** (Blast Radius: 232.515 * Doc Risk: 11.9203%)
- `beautifulsoup4-4.14.3/bs4/_typing.py` -> **Severity: 1764.192** (Blast Radius: 147.999 * Doc Risk: 11.9203%)
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **Severity: 1507.448** (Blast Radius: 20.788 * Doc Risk: 72.5153%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
