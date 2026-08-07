# ARCHITECTURAL_BRIEF: beautifulsoup4
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/beautifulsoup4` |
| **Timestamp** | `2026-08-07T05:21:35.292309+00:00` |
| **Scan Duration** | `0.42s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 35 malicious artifacts.

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
> **Architectural Drift Z-Score:** `4.633`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 17 | 43.6% |
| file_cluster_16 | 12 | 30.8% |
| file_cluster_13 | 5 | 12.8% |
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
| Cognitive Load Exposure | 0.0 | 24.6 | 7.7 | 4.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 85.9 | 30.6 | 5.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.5 | 5.9 | 4.7 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.1 | 27.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 90.0 | 6.4 | 0.0 | 0.0 |
| Specification Exposure | 53.3 | 100.0 | 97.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 89.3 | 11.8 | 0.0 | 0.0 |
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

- `deprecated_argument` (@ `beautifulsoup4-4.14.3/bs4/__init__.py`) -> Impact: **298.9** | LOC: 748
- `quoted_attribute_value` (@ `beautifulsoup4-4.14.3/bs4/dammit.py`) -> Impact: **243.8** | LOC: 961
- `__init__` (@ `beautifulsoup4-4.14.3/bs4/builder/__init__.py`) -> Impact: **60.5** | LOC: 330
- `lxml_trace` (@ `beautifulsoup4-4.14.3/bs4/diagnose.py`) -> Impact: **40.0** | LOC: 159
- `matches_tag` (@ `beautifulsoup4-4.14.3/bs4/filter.py`) -> Impact: **37.9** | LOC: 65
  * *Intent:* # If you pass in 'class_' as part of kwargs, it's # because class is a Python reserved word. If you # pass it in as part of the attrs dict, it's # cal...
- `diagnose` (@ `beautifulsoup4-4.14.3/bs4/diagnose.py`) -> Impact: **34.5** | LOC: 51
- `handle_entityref` (@ `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py`) -> Impact: **33.1** | LOC: 143
- `lookup` (@ `beautifulsoup4-4.14.3/bs4/builder/__init__.py`) -> Impact: **21.0** | LOC: 38
- `excludes_everything` (@ `beautifulsoup4-4.14.3/bs4/filter.py`) -> Impact: **20.0** | LOC: 18
- `test_id_child_selector_nth_of_type` (@ `beautifulsoup4-4.14.3/bs4/tests/test_css.py`) -> Impact: **18.6** | LOC: 129

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `beautifulsoup4-4.14.3/bs4/tests` | 16 | 2075.92 | 2.9% | 0.0% |
| `beautifulsoup4-4.14.3/bs4` | 11 | 1767.86 | 11.76% | 38.63% |
| `beautifulsoup4-4.14.3/bs4/builder` | 3 | 472.96 | 18.36% | 70.11% |
| `beautifulsoup4-4.14.3` | 4 | 101.42 | 0.0% | 0.0% |
| `beautifulsoup4-4.14.3/doc.es` | 2 | 50.4 | 8.38% | 0.0% |
| `beautifulsoup4-4.14.3/doc.ru` | 1 | 34.1 | 4.12% | 0.0% |
| `beautifulsoup4-4.14.3/doc` | 2 | 31.46 | 8.82% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **99.9999%** Exposure
- `beautifulsoup4-4.14.3/bs4/_deprecation.py` -> **99.9998%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **99.9527%** Exposure
- `beautifulsoup4-4.14.3/bs4/formatter.py` -> **96.1368%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **72.6236%** Exposure
### Highest State Flux (Mutation/Volatility)
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **99.0664%** Exposure
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **97.6806%** Exposure
- `beautifulsoup4-4.14.3/bs4/formatter.py` -> **94.5979%** Exposure
- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **93.6499%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **91.705%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` -> **135** Orphaned Functions | **8** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/__init__.py` -> **40** Orphaned Functions | **4** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` -> **33** Orphaned Functions | **4** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_filter.py` -> **29** Orphaned Functions | **4** Duplicates
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `216` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `beautifulsoup4-4.14.3/bs4/filter.py` (PYTHON) -> Cumulative Risk: **535.26**
- **Archetype:** `file_cluster_16` (Distance: 11.945 IQR)
- **Magnitude:** 300.44 | **LOC:** 765 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (97.6806%), Verification (80.0%)
- **Heaviest Functions:** `matches_tag` (Impact: 37.9), `excludes_everything` (Impact: 20.0), `match` (Impact: 14.8)

### 2. `beautifulsoup4-4.14.3/bs4/diagnose.py` (PYTHON) -> Cumulative Risk: **514.16**
- **Archetype:** `file_cluster_13` (Distance: 11.719 IQR)
- **Magnitude:** 138.34 | **LOC:** 269 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (88.4052%), Verification (80.0%), Tech Debt (68.8564%)
- **Heaviest Functions:** `lxml_trace` (Impact: 40.0), `diagnose` (Impact: 34.5), `handle_pi` (Impact: 18.5)

### 3. `beautifulsoup4-4.14.3/bs4/builder/__init__.py` (PYTHON) -> Cumulative Risk: **503.17**
- **Archetype:** `file_cluster_16` (Distance: 11.14 IQR)
- **Magnitude:** 204.1 | **LOC:** 849 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (91.705%), Verification (80.0%), Tech Debt (72.6236%)
- **Heaviest Functions:** `__init__` (Impact: 60.5), `lookup` (Impact: 21.0), `register_treebuilders_from` (Impact: 6.6)

### 4. `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` (PYTHON) -> Cumulative Risk: **455.76**
- **Archetype:** `file_cluster_16` (Distance: 12.055 IQR)
- **Magnitude:** 154.66 | **LOC:** 502 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9527%), State Flux (99.0664%), Stability (50.0%)
- **Heaviest Functions:** `end` (Impact: 13.2), `feed` (Impact: 11.6), `_register_namespaces` (Impact: 7.6)

### 5. `beautifulsoup4-4.14.3/bs4/formatter.py` (PYTHON) -> Cumulative Risk: **434.73**
- **Archetype:** `file_cluster_16` (Distance: 10.486 IQR)
- **Magnitude:** 46.6 | **LOC:** 277 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.1368%), State Flux (94.5979%), Safety Score (60.9033%)
- **Heaviest Functions:** `substitute` (Impact: 9.5), `attribute_value` (Impact: 1.9), `__init__` (Impact: 1.4)

### 6. `beautifulsoup4-4.14.3/bs4/_deprecation.py` (PYTHON) -> Cumulative Risk: **434.24**
- **Archetype:** `file_cluster_16` (Distance: 9.121 IQR)
- **Magnitude:** 27.12 | **LOC:** 81 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), Documentation (89.2589%), Safety Score (85.9379%)
- **Heaviest Functions:** `_deprecated_alias` (Impact: 3.2), `deprecate` (Impact: 2.6), `_deprecated` (Impact: 2.5)

### 7. `beautifulsoup4-4.14.3/bs4/__init__.py` (PYTHON) -> Cumulative Risk: **423.78**
- **Archetype:** `file_cluster_16` (Distance: 11.576 IQR)
- **Magnitude:** 419.24 | **LOC:** 1175 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (93.6499%), Verification (80.0%), Safety Score (62.6721%)
- **Heaviest Functions:** `deprecated_argument` (Impact: 298.9), `__init__` (Impact: 1.5)

### 8. `beautifulsoup4-4.14.3/bs4/dammit.py` (PYTHON) -> Cumulative Risk: **422.8**
- **Archetype:** `file_cluster_16` (Distance: 11.185 IQR)
- **Magnitude:** 376.4 | **LOC:** 1517 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (85.7261%), Verification (80.0%), Safety Score (58.7888%)
- **Heaviest Functions:** `quoted_attribute_value` (Impact: 243.8), `_chardet_dammit` (Impact: 6.3), `_substitute_html_entity` (Impact: 3.9)

### 9. `beautifulsoup4-4.14.3/doc.es/conf.py` (PYTHON) -> Cumulative Risk: **391.9**
- **Archetype:** `file_cluster_13` (Distance: 20.539 IQR)
- **Magnitude:** 16.3 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Dead Code (89.9557%), Safety Score (65.5399%), State Flux (59.548%)

### 10. `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` (PYTHON) -> Cumulative Risk: **384.17**
- **Archetype:** `file_cluster_16` (Distance: 11.153 IQR)
- **Magnitude:** 114.2 | **LOC:** 463 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (89.7011%), Safety Score (70.0833%), Stability (50.0%)
- **Heaviest Functions:** `handle_entityref` (Impact: 33.1), `handle_charref` (Impact: 9.6), `handle_endtag` (Impact: 8.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.056 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.89 IQR)
- **Top Global Matches:** file_cluster_8: 13.056, file_cluster_0: 13.321, file_cluster_13: 13.346
- **Magnitude:** 608.0 | **LOC:** 1460 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0248%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_replace_with_errors` (Impact: 7.6)
  * `test_suspicious_syntax_warning` (Impact: 7.6)
  * `test_insert_after_raises_exception_if_af` (Impact: 7.4)
  * `test_insert_before_raises_notimplemented` (Impact: 7.4)
    * *Intent:* # Can't insert an element after itself. b = soup.b with pytest.raises(ValueError): b.insert_after(b)...
  * `test_parent_generator` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 446`, `args: 152`, `func_start: 146`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 57`, `planned_debt: 2`, `duplicate_logic: 8`, `orphaned_logic: 135`
* *Architecture:* `api: 163`, `import: 8`
* *Defense:* `safety: 262`, `doc: 66`, `test: 411`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4.element, warnings, bs4.filter, bs4.builder, bs4, pytest, , re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.576 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.82 IQR)
- **Top Global Matches:** file_cluster_16: 11.576, file_cluster_13: 11.695, file_cluster_8: 11.772
- **Magnitude:** 419.24 | **LOC:** 1175 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5537%), Tech Debt (9.2521%)
**Top Internal Functions/Classes:**
  * `deprecated_argument` (Impact: 298.9)
  * `__init__` (Impact: 1.5)
    * *Intent:* #: want, look for one with these features. DEFAULT_BUILDER_FEATURES: Sequence[str] = ["html", "fast"...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 114`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 86`, `planned_debt: 2`
* *Architecture:* `io: 5`, `api: 19`, `import: 17`
* *Defense:* `safety: 25`, `doc: 88`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .builder._htmlparser, warnings, ._deprecation, .builder, bs4._typing, .element, collections, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/element.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.098 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.771 IQR)
- **Top Global Matches:** file_cluster_16: 12.098, file_cluster_0: 12.392, file_cluster_13: 12.495
- **Magnitude:** 388.44 | **LOC:** 3212 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.7963%), Tech Debt (41.7055%)
**Top Internal Functions/Classes:**
  * `__setitem__` (Impact: 15.4)
  * `__setitem__` (Impact: 9.0)
    * *Intent:* """ if eventual_encoding in PYTHON_SPECIFIC_ENCODINGS: return "" return eventual_encoding class Attr...
  * `__getattr__` (Impact: 4.3)
  * `substitute_encoding` (Impact: 3.8)
  * `__init__` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 362`, `args: 150`, `func_start: 150`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 183`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 129`, `import: 17`
* *Defense:* `safety: 54`, `doc: 397`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 232.515
  * `Choke Point (Betweenness):` 0.078592 | `Ripple Effect (Closeness):` 0.464035
  * `Imports (Out-Degree: 6):` warnings, bs4.filter, bs4._typing, bs4.builder, __future__, bs4._deprecation, typing, bs4...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/dammit.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.185 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.547 IQR)
- **Top Global Matches:** file_cluster_16: 11.185, file_cluster_13: 11.276, file_cluster_8: 11.305
- **Magnitude:** 376.4 | **LOC:** 1517 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.6857%), Tech Debt (8.9628%)
**Top Internal Functions/Classes:**
  * `quoted_attribute_value` (Impact: 243.8)
  * `_chardet_dammit` (Impact: 6.3)
  * `_substitute_html_entity` (Impact: 3.9)
    * *Intent:* #: A map of Unicode strings to the corresponding named XML entities. #: #: :meta hide-value:
  * `_escape_unrecognized_entity_name` (Impact: 3.7)
    * *Intent:* #: A regular expression matching an angle bracket or an ampersand. #:
  * `_substitute_xml_entity` (Impact: 2.2)
    * *Intent:* #: A regular expression matching an angle bracket or an ampersand that #: is not part of an XML or H...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 102`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 84`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 16`, `import: 14`
* *Defense:* `safety: 17`, `doc: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.512
  * `Choke Point (Betweenness):` 0.004979 | `Ripple Effect (Closeness):` 0.257797
  * `Imports (Out-Degree: 1):` logging, html.entities, codecs, bs4._typing, warnings, types, collections, chardet...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/filter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.945 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.793 IQR)
- **Top Global Matches:** file_cluster_16: 11.945, file_cluster_13: 12.056, file_cluster_0: 12.106
- **Magnitude:** 300.44 | **LOC:** 765 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.6174%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `matches_tag` (Impact: 37.9)
    * *Intent:* # If you pass in 'class_' as part of kwargs, it's # because class is a Python reserved word. If you ...
  * `excludes_everything` (Impact: 20.0)
  * `match` (Impact: 14.8)
    * *Intent:* # attrs = " ".join( # [f"{k}={v}" for k, v in sorted(tag.attrs.items())] # print(f"Testing <{tag.nam...
  * `_base_match` (Impact: 13.5)
  * `filter` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 123`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 59`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 31`, `import: 8`
* *Defense:* `safety: 17`, `doc: 72`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.977
  * `Choke Point (Betweenness):` 0.003556 | `Ripple Effect (Closeness):` 0.309357
  * `Imports (Out-Degree: 3):` bs4.element, warnings, bs4._typing, __future__, collections, bs4._deprecation, typing, re
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.136 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.797 IQR)
- **Top Global Matches:** file_cluster_8: 12.136, file_cluster_13: 12.394, file_cluster_7: 12.469
- **Magnitude:** 295.18 | **LOC:** 1349 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.6836%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_angle_brackets_in_attribute_values_` (Impact: 15.7)
    * *Intent:* """Inline elements can be nested indefinitely."""
  * `test_html5_style_meta_tag_reflects_curre` (Impact: 11.6)
    * *Intent:* # Encode it to UTF-8. result = soup.encode("utf-8") # What do we expect the result to look like? Wel...
  * `test_formatter_processes_script_tag_for_` (Impact: 8.5)
  * `test_python_specific_encodings_not_used_` (Impact: 6.3)
    * *Intent:* # You can encode an HTML document using a Python-specific # encoding, but that encoding won't be men...
  * `test_real_xhtml_document` (Impact: 6.2)
    * *Intent:* """Generate and parse a document with the given doctype."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 320`, `args: 109`, `func_start: 109`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`, `dead_code: 2`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 40`
* *Architecture:* `io: 1`, `api: 113`, `import: 15`
* *Defense:* `safety: 166`, `doc: 98`, `test: 250`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bs4.element, importlib, warnings, copy, bs4.filter, bs4.builder, bs4._typing, bs4.builder._htmlparser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_filter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.854 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.977 IQR)
- **Top Global Matches:** file_cluster_8: 11.854, file_cluster_0: 12.023, file_cluster_13: 12.146
- **Magnitude:** 222.52 | **LOC:** 702 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_match` (Impact: 13.1)
  * `test_allow_tag_creation` (Impact: 9.1)
    * *Intent:* # By default, ElementFilter.allow_tag_creation allows everything. filter = ElementFilter() f = filte...
  * `test_default_behavior` (Impact: 7.7)
    * *Intent:* # An unconfigured ElementFilter matches absolutely everything. selector = ElementFilter() assert not...
  * `test_empty_match_not_allowed` (Impact: 7.2)
  * `test_full_match_not_allowed` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 213`, `args: 50`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 29`
* *Architecture:* `api: 46`, `import: 8`
* *Defense:* `safety: 120`, `doc: 4`, `test: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bs4.element, warnings, bs4.filter, bs4._typing, typing, pytest, , re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/builder/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.14 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.43 IQR)
- **Top Global Matches:** file_cluster_16: 11.14, file_cluster_13: 11.309, file_cluster_8: 11.526
- **Magnitude:** 204.1 | **LOC:** 849 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.234%), Tech Debt (72.6236%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 60.5)
  * `lookup` (Impact: 21.0)
  * `register_treebuilders_from` (Impact: 6.6)
    * *Intent:* # TODO: This cast will fail in the (very unlikely) scenario # that the programmer who instantiates t...
  * `register` (Impact: 3.8)
  * `can_be_empty_element` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 100`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 48`, `planned_debt: 3`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 37`, `import: 17`
* *Defense:* `safety: 11`, `doc: 67`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bs4.element, warnings, bs4._typing, __future__, types, collections, typing, bs4...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.75 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_8: 11.75, file_cluster_13: 11.827, file_cluster_0: 11.878
- **Magnitude:** 201.8 | **LOC:** 603 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0487%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_custom_builder_class` (Impact: 8.4)
    * *Intent:* # it'll be instantiated with the appropriate keyword arguments. class Mock(object): def __init__(sel...
  * `test_cdata_list_attributes` (Impact: 6.7)
    * *Intent:* # HTML standard says that some attributes, like 'class' have # space-separated lists as values. mark...
  * `test_parser_markup_rejection` (Impact: 6.2)
    * *Intent:* # explanatory ParserRejectedMarkup exception is raised. class Mock(TreeBuilder): def feed(self, *arg...
  * `test_ascii_in_unicode_out` (Impact: 6.2)
    * *Intent:* # ASCII input is converted to Unicode. The original_encoding # attribute is set to 'utf-8', a supers...
  * `test_invalid_markup_type` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 194`, `args: 50`, `func_start: 49`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 11`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 33`
* *Architecture:* `io: 1`, `api: 61`, `import: 13`
* *Defense:* `safety: 86`, `doc: 6`, `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bs4.element, logging, bs4.filter, warnings, bs4.builder, typing, bs4, pickle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.055 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.843 IQR)
- **Top Global Matches:** file_cluster_16: 12.055, file_cluster_13: 12.114, file_cluster_8: 12.407
- **Magnitude:** 154.66 | **LOC:** 502 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.8095%), Tech Debt (99.9527%)
**Top Internal Functions/Classes:**
  * `end` (Impact: 13.2)
    * *Intent:* # Also treat the namespace mapping as a set of attributes on the # tag, so we can recreate it later.
  * `feed` (Impact: 11.6)
    * *Intent:* # We were given Unicode. Maybe lxml can parse Unicode on # this system? # https://bugs.launchpad.net...
  * `_register_namespaces` (Impact: 7.6)
    * *Intent:* # Beyond this point, self.soup is set, so we can assume (and # assert) it's not None whenever necess...
  * `_getNsTag` (Impact: 5.5)
    * *Intent:* **kwargs: Any, # TODO: Issue a warning if parser is present but not a # callable, since that means t...
  * `parser_for` (Impact: 4.0)
    * *Intent:* # This is 'if key' and not 'if key is not None' because we # don't track un-prefixed namespaces. Sou...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 80`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 50`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 23`, `import: 12`
* *Defense:* `safety: 29`, `doc: 25`, `test: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.788
  * `Choke Point (Betweenness):` 0.009602 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 4):` bs4.element, bs4._typing, lxml, bs4.builder, __future__, bs4.dammit, typing, io...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_css.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.802 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.672 IQR)
- **Top Global Matches:** file_cluster_8: 10.802, file_cluster_13: 11.344, file_cluster_7: 11.377
- **Magnitude:** 153.26 | **LOC:** 537 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0429%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_id_child_selector_nth_of_type` (Impact: 18.6)
  * `test_multi_class_support` (Impact: 6.3)
  * `test_items_in_id` (Impact: 5.7)
  * `test_unsupported_pseudoclass` (Impact: 5.5)
  * `test_class_one` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 148`, `args: 63`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 64`, `import: 7`
* *Defense:* `safety: 55`, `doc: 6`, `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, bs4, typing, pytest, , soupsieve, packaging.version
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/diagnose.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.719 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.039 IQR)
- **Top Global Matches:** file_cluster_13: 11.719, file_cluster_16: 11.966, file_cluster_8: 12.173
- **Magnitude:** 138.34 | **LOC:** 269 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.3156%), Tech Debt (68.8564%)
**Top Internal Functions/Classes:**
  * `lxml_trace` (Impact: 40.0)
  * `diagnose` (Impact: 34.5)
  * `handle_pi` (Impact: 18.5)
  * `handle_data` (Impact: 2.0)
  * `handle_entityref` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 51`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `orphaned_logic: 5`
* *Architecture:* `io: 1`, `api: 18`, `import: 19`
* *Defense:* `safety: 11`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bs4._typing, lxml, bs4.builder, random, traceback, bs4, io, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_dammit.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.227 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_8: 11.227, file_cluster_0: 11.573, file_cluster_13: 11.694
- **Magnitude:** 136.62 | **LOC:** 513 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.2367%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_last_ditch_entity_replacement` (Impact: 6.9)
    * *Intent:* # completely incompatible with UTF-8 (ie. encoded with some other # encoding). # # Since there is no...
  * `test_known_definite_versus_user_encoding` (Impact: 6.7)
    * *Intent:* # The known_definite_encodings are used before sniffing the # byte-order mark; the user_encodings ar...
  * `test_deprecated_override_encodings` (Impact: 6.3)
    * *Intent:* # override_encodings is a deprecated alias for # known_definite_encodings. hebrew = b"\xed\xe5\xec\x...
  * `test_html5_entity` (Impact: 4.7)
    * *Intent:* # A few spot checks of our ability to recognize # special character sequences and convert them # to ...
  * `test_detwingle` (Impact: 4.6)
    * *Intent:* # Here's a UTF8 document. utf8 = ("\N{SNOWMAN}" * 3).encode("utf8") # Here's a Windows-1252 document...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 124`, `args: 39`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 29`
* *Architecture:* `api: 43`, `import: 6`
* *Defense:* `safety: 74`, `doc: 10`, `test: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` logging, warnings, bs4.dammit, bs4, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.153 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.473 IQR)
- **Top Global Matches:** file_cluster_16: 11.153, file_cluster_13: 11.185, file_cluster_8: 11.579
- **Magnitude:** 114.2 | **LOC:** 463 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.0456%), Tech Debt (37.7541%)
**Top Internal Functions/Classes:**
  * `handle_entityref` (Impact: 33.1)
  * `handle_charref` (Impact: 9.6)
  * `handle_endtag` (Impact: 8.6)
    * *Intent:* # Unlike other parsers, html.parser doesn't send separate end tag # handle_startendtag, but only if ...
  * `feed` (Impact: 5.4)
  * `error` (Impact: 2.5)
    * *Intent:* # Keep a list of empty-element tags that were encountered # without an explicit closing tag. If we e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 43`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 25`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 20`, `import: 10`
* *Defense:* `safety: 6`, `doc: 52`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.623
  * `Choke Point (Betweenness):` 0.010313 | `Ripple Effect (Closeness):` 0.105263
  * `Imports (Out-Degree: 4):` bs4.element, bs4._typing, bs4.builder, bs4.dammit, __future__, typing, bs4, bs4.exceptions...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.009 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.701 IQR)
- **Top Global Matches:** file_cluster_8: 12.009, file_cluster_13: 12.157, file_cluster_7: 12.437
- **Magnitude:** 90.28 | **LOC:** 438 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.5956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_formatter_custom` (Impact: 17.3)
  * `test_encoding_substitutes_unrecognized_c` (Impact: 13.7)
  * `test_unicode_string_can_be_encoded` (Impact: 1.9)
  * `test_tag_containing_unicode_string_can_b` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 139`, `args: 42`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `state_mutation: 7`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 43`, `import: 9`
* *Defense:* `safety: 74`, `doc: 16`, `test: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4.element, copy, warnings, bs4.filter, bs4, pickle, sys, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_builder_registry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.922 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.704 IQR)
- **Top Global Matches:** file_cluster_13: 11.922, file_cluster_8: 12.063, file_cluster_7: 12.478
- **Magnitude:** 61.82 | **LOC:** 140 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8843%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lookup_by_markup_type` (Impact: 9.2)
  * `test_beautifulsoup_constructor_does_look` (Impact: 5.9)
    * *Intent:* # specifying a parser, but we'll ignore it. # You can pass in a string. BeautifulSoup("", features="...
  * `test_named_library` (Impact: 5.6)
  * `test_combination` (Impact: 5.5)
  * `test_lookup_gets_most_recent_builder_sup` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 58`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 23`, `doc: 6`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` warnings, bs4.builder._lxml, bs4.builder, bs4.builder._htmlparser, typing, bs4, pytest, ...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_tag.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.906 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.01 IQR)
- **Top Global Matches:** file_cluster_8: 12.906, file_cluster_13: 13.154, file_cluster_16: 13.199
- **Magnitude:** 60.92 | **LOC:** 242 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.5134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_deprecated_member_access` (Impact: 5.6)
  * `test__should_pretty_print` (Impact: 2.6)
  * `test_len` (Impact: 2.4)
  * `test_tag_with_multiple_children_has_no_s` (Impact: 2.4)
    * *Intent:* # A Tag with no children has no .stirng.
  * `test_member_access_invokes_find` (Impact: 2.1)
    * *Intent:* """Accessing a Python member .foo invokes find('foo')"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 101`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 57`, `doc: 14`, `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bs4.element, warnings, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_element.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.179 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.914 IQR)
- **Top Global Matches:** file_cluster_8: 12.179, file_cluster_13: 12.591, file_cluster_7: 12.671
- **Magnitude:** 49.72 | **LOC:** 179 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.4886%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_content_meta_attribute_value` (Impact: 4.4)
    * *Intent:* # no encoding will be mentioned in the output HTML. assert "" == value.substitute_encoding("palmos")...
  * `test_getattr_exception` (Impact: 3.9)
  * `test_attributes_are_equivalent_if_prefix` (Impact: 2.5)
  * `test_equality` (Impact: 2.5)
    * *Intent:* # __getitem__ is delegated to the result sequence.
  * `test_charset_meta_attribute_value` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 66`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `orphaned_logic: 12`
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `safety: 42`, `doc: 6`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, bs4.element, bs4.filter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/CHANGELOG` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 49.32 | **LOC:** 2466 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `beautifulsoup4-4.14.3/bs4/tests/test_htmlparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.387 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.249 IQR)
- **Top Global Matches:** file_cluster_13: 11.387, file_cluster_8: 11.438, file_cluster_7: 11.916
- **Magnitude:** 47.06 | **LOC:** 165 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.7764%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_empty_element` (Impact: 10.2)
  * `test_feed_raises_correct_exception_on_re` (Impact: 4.1)
    * *Intent:* # Mock BeautifulSoupHTMLParser so it raises an AssertionError and verify that this is # turned into ...
  * `test_builder_is_pickled` (Impact: 2.1)
    * *Intent:* """Unlike most tree builders, HTMLParserTreeBuilder can be pickled and will be restored after pickli...
  * `test_surrogate_in_character_reference` (Impact: 2.1)
  * `test_namespaced_system_doctype` (Impact: 1.9)
    * *Intent:* # html.parser can't handle namespaced doctypes, so skip this one. pass def test_namespaced_public_do...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 53`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 16`, `import: 7`
* *Defense:* `safety: 21`, `doc: 4`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4.builder._htmlparser, bs4, typing, pickle, pytest, , bs4.exceptions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/formatter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.486 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.388 IQR)
- **Top Global Matches:** file_cluster_16: 10.486, file_cluster_13: 10.743, file_cluster_8: 10.8
- **Magnitude:** 46.6 | **LOC:** 277 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4326%), Tech Debt (96.1368%)
**Top Internal Functions/Classes:**
  * `substitute` (Impact: 9.5)
  * `attribute_value` (Impact: 1.9)
  * `__init__` (Impact: 1.4)
  * `__init__` (Impact: 1.4)
  * `__init__` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 31`, `args: 7`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `duplicate_logic: 3`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 3`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 46.737
  * `Choke Point (Betweenness):` 0.010313 | `Ripple Effect (Closeness):` 0.278421
  * `Imports (Out-Degree: 3):` bs4._typing, bs4.dammit, __future__, .element, typing, typing_extensions
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_formatter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.845 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.589 IQR)
- **Top Global Matches:** file_cluster_8: 10.845, file_cluster_0: 11.005, file_cluster_13: 11.052
- **Magnitude:** 45.4 | **LOC:** 171 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7929%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_empty_attributes_are_booleans` (Impact: 8.3)
    * *Intent:* # Test the behavior of empty_attributes_are_booleans as well # as which Formatters have it enabled. ...
  * `test_sort_attributes` (Impact: 6.1)
    * *Intent:* # Test the ability to override Formatter.attributes() to, # e.g., disable the normal sorting of attr...
  * `attributes` (Impact: 5.5)
  * `test_default_attributes` (Impact: 2.6)
    * *Intent:* # Test the default behavior of Formatter.attributes(). formatter = Formatter() tag = Tag(name="tag")...
  * `test_indent` (Impact: 2.5)
    * *Intent:* # Pretty-print a tree with a Formatter set to # indent in a certain way and verify the results. soup...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 43`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 24`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, bs4.formatter, bs4.element, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_navigablestring.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.601 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.871 IQR)
- **Top Global Matches:** file_cluster_8: 12.601, file_cluster_13: 12.793, file_cluster_17: 12.969
- **Magnitude:** 41.64 | **LOC:** 156 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2203%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_string_detects_attribute_access_att` (Impact: 4.0)
  * `test_string_has_immutable_name_property` (Impact: 3.8)
    * *Intent:* # string.name is defined as None and can't be modified string = self.soup("s").string assert None is...
  * `test_text_acquisition_methods` (Impact: 3.3)
    * *Intent:* # These methods are intended for use against Tag, but they # work on NavigableString as well, s = Na...
  * `test_cdata_is_never_formatted` (Impact: 2.5)
    * *Intent:* """Text inside a CData object is passed into the formatter. But the return value is ignored. """
  * `test_cdata` (Impact: 2.2)
    * *Intent:* # None of the current builders turn CDATA sections into CData # objects, but you can create them man...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 57`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 8`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 43`, `doc: 2`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, bs4.element, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/css.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.75 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.766 IQR)
- **Top Global Matches:** file_cluster_16: 9.75, file_cluster_13: 9.952, file_cluster_8: 10.146
- **Magnitude:** 38.48 | **LOC:** 340 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.5059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 6.5)
  * `escape` (Impact: 3.9)
  * `match` (Impact: 2.3)
  * `_rs` (Impact: 2.1)
    * *Intent:* """Escape a CSS identifier. This is a simple wrapper around `soupsieve.escape() <https://facelessuse...
  * `select` (Impact: 1.4)
    * *Intent:* # Import here to avoid circular import
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 40`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 2`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 3`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272962
  * `Imports (Out-Degree: 2):` bs4.element, bs4._typing, warnings, __future__, types, typing, bs4, soupsieve
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `beautifulsoup4-4.14.3/bs4/tests/test_lxml.py` (PYTHON) | Magnitude: 18.42 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 57, test: 41, safety: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `beautifulsoup4-4.14.3/bs4/exceptions.py` (PYTHON) | Magnitude: 6.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 6, indent_spaces: 5, class_start: 3
- `beautifulsoup4-4.14.3/bs4/tests/test_htmlparser.py` (PYTHON) | Magnitude: 47.06 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 53, test: 34, safety: 21
- `beautifulsoup4-4.14.3/doc.es/conf.py` (PYTHON) | Magnitude: 16.3 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 3, structural_boundaries: 2, io: 2, import: 2
- `beautifulsoup4-4.14.3/doc/conf.py` (PYTHON) | Magnitude: 16.3 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 3, structural_boundaries: 2, io: 2, import: 2
- `beautifulsoup4-4.14.3/bs4/tests/test_builder_registry.py` (PYTHON) | Magnitude: 61.82 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 58, test: 36, safety: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` (PYTHON) | Magnitude: 114.2 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 207, doc: 52, structural_boundaries: 43, branch: 36
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` (PYTHON) | Magnitude: 154.66 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 80, encapsulation: 60, state_mutation: 50
- `beautifulsoup4-4.14.3/bs4/dammit.py` (PYTHON) | Magnitude: 376.4 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 795, sec_reflection_metaprogramming: 457, branch: 139, structural_boundaries: 102
- `beautifulsoup4-4.14.3/bs4/filter.py` (PYTHON) | Magnitude: 300.44 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 375, branch: 136, structural_boundaries: 123, encapsulation: 84
- `beautifulsoup4-4.14.3/bs4/__init__.py` (PYTHON) | Magnitude: 419.24 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 656, branch: 161, structural_boundaries: 114, doc: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `beautifulsoup4-4.14.3/bs4/tests/test_fuzz.py` (PYTHON) | Magnitude: 30.2 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 20, test: 14, safety: 9
- `beautifulsoup4-4.14.3/bs4/_warnings.py` (PYTHON) | Magnitude: 20.3 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 24, indent_spaces: 10, structural_boundaries: 5, class_start: 5
- `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` (PYTHON) | Magnitude: 201.8 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 398, structural_boundaries: 194, test: 126, safety: 86
- `beautifulsoup4-4.14.3/bs4/tests/test_builder.py` (PYTHON) | Magnitude: 13.08 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, test: 9, branch: 4
- `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py` (PYTHON) | Magnitude: 90.28 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_13`
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

- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 26.796** (Embedded: 0.464 * Error Risk: 57.7462%)
- `beautifulsoup4-4.14.3/bs4/_typing.py` -> **Severity: 25.217** (Embedded: 0.4094 * Error Risk: 61.5878%)
- `beautifulsoup4-4.14.3/bs4/_deprecation.py` -> **Severity: 25.051** (Embedded: 0.2915 * Error Risk: 85.9379%)
- `beautifulsoup4-4.14.3/bs4/css.py` -> **Severity: 19.827** (Embedded: 0.273 * Error Risk: 72.6357%)
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **Severity: 19.275** (Embedded: 0.3094 * Error Risk: 62.3064%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `beautifulsoup4-4.14.3/bs4/_deprecation.py` -> **Severity: 5367.227** (Blast Radius: 60.131 * Doc Risk: 89.2589%)
- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 2771.649** (Blast Radius: 232.515 * Doc Risk: 11.9203%)
- `beautifulsoup4-4.14.3/bs4/_typing.py` -> **Severity: 1764.192** (Blast Radius: 147.999 * Doc Risk: 11.9203%)
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **Severity: 726.864** (Blast Radius: 60.977 * Doc Risk: 11.9203%)
- `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` -> **Severity: 651.481** (Blast Radius: 20.788 * Doc Risk: 31.3393%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
