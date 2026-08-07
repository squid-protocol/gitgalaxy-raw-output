# ARCHITECTURAL_BRIEF: python-simplebench
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/python-simplebench` |
| **Timestamp** | `2026-08-07T05:27:47.849063+00:00` |
| **Scan Duration** | `7.11s` |
| **Git Branch** | `main` |
| **Git Commit** | `f36f50afe458be260d7490a0746168ea70423537` |
| **Git Remote** | `https://github.com/JerilynFranz/python-simplebench.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 283 malicious artifacts.

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
| Total Artifacts | 1704 |
| Analyzed Artifacts (Scanned) | 729 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 975 |
| Total LOC | 139301 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 42.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5136 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0889 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6118 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 43 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 271 | 19948 | 37.2% |
| HTML | 244 | 108998 | 33.5% |
| PLAINTEXT | 176 | 1 | 24.1% |
| CSS | 17 | 8252 | 2.3% |
| JAVASCRIPT | 10 | 955 | 1.4% |
| MARKDOWN | 2 | 0 | 0.3% |
| YAML | 2 | 37 | 0.3% |
| JSON | 2 | 1036 | 0.3% |
| XML | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 20 | 0.1% |
| BATCH | 1 | 52 | 0.1% |
| CSV | 1 | 2 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.75`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 244 | 33.5% |
| file_cluster_13 | 145 | 19.9% |
| file_cluster_8 | 124 | 17.0% |
| file_cluster_16 | 34 | 4.7% |
| file_cluster_17 | 4 | 0.5% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 177 | 24.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 975*

**Composition by Extension & Reason:**
- `.html`: 308x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 217x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 169x Excluded (Unsupported Extension: '.rst'), 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.doctree`: 134x Excluded (Unsupported Extension: '.doctree'), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 258 LOC), 1x Excluded (Machine-Generated Source Code Signature: 320 LOC)
- `.js`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.css`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Static Asset Blob without Intent: 1266 LOC), 2x Excluded (Machine-Generated Source Code Signature: 278 LOC)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 51001 LOC exceeds safe regex boundaries), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.map`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.map'), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inv`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.inv')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 75.0 | 7.5 | 6.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 96.0 | 10.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.6 | 12.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.4 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.9 | 6.8 | 5.3 | 0.0 |
| Concurrency Exposure | 0.0 | 99.1 | 0.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.1 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.7 | 0.5 | 0.5 | 0.5 |
| Volatility Exposure | 0.0 | 100.0 | 21.9 | 31.6 | 31.6 |
| Documentation Exposure | 0.0 | 100.0 | 50.4 | 25.8 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `documentation/html/genindex.html` (Hits: 3505)
- `documentation/html/source/simplebench.html` (Hits: 2804)
- `documentation/html/source/simplebench.stats.html` (Hits: 1162)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **simplebench.enums.html** (`documentation/html/source/simplebench.enums.html`) — 81 inbound connections
2. **simplebench.exceptions.html** (`documentation/html/source/simplebench.exceptions.html`) — 75 inbound connections
3. **simplebench.case.html** (`documentation/html/source/simplebench.case.html`) — 37 inbound connections
4. **simplebench.reporters.reporter.html** (`documentation/html/source/simplebench.reporters.reporter.html`) — 32 inbound connections
5. **argparse.py** (`tests/factories/argparse.py`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **reporter.py** (`src/simplebench/reporters/reporter/reporter.py`) — 27 outbound dependencies
2. **session.py** (`src/simplebench/session.py`) — 22 outbound dependencies
3. **case.py** (`src/simplebench/case.py`) — 21 outbound dependencies
4. **reporter.py** (`src/simplebench/reporters/json/reporter/reporter.py`) — 21 outbound dependencies
5. **_orchestration.py** (`src/simplebench/reporters/reporter/mixins/_orchestration.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `benchmark` (@ `src/simplebench/decorators.py`) -> Impact: **165.7** | LOC: 175
- `render` (@ `src/simplebench/reporters/rich_table/reporter/reporter.py`) -> Impact: **140.8** | LOC: 122
- `dispatch_to_targets` (@ `src/simplebench/reporters/reporter/mixins/_orchestration.py`) -> Impact: **131.5** | LOC: 107
- `report` (@ `src/simplebench/session.py`) -> Impact: **121.0** | LOC: 306
- `render` (@ `src/simplebench/reporters/csv/reporter/reporter.py`) -> Impact: **120.6** | LOC: 109
- `media` (@ `documentation/html/_static/pygments.css`) -> Impact: **96.7** | LOC: 174
  * *Intent:* .highlight .se { color: #79C0FF } /* Literal.String.Escape */ .highlight .sh { color: #79C0FF } /* Literal.String.Heredoc */ .highlight .si { color: #...
- `media` (@ `documentation/html/_static/pygments.css`) -> Impact: **91.3** | LOC: 87
  * *Intent:* body[data-theme="dark"] .highlight .se { color: #ED9D13 } /* Literal.String.Escape */ body[data-theme="dark"] .highlight .sh { color: #ED9D13 } /* Lit...
- `__init__` (@ `src/simplebench/case.py`) -> Impact: **87.8** | LOC: 107
- `report` (@ `src/simplebench/reporters/reporter/reporter.py`) -> Impact: **83.1** | LOC: 81
- `stemWord` (@ `documentation/html/_static/language_data.js`) -> Impact: **82.8** | LOC: 131

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 5 | 5026.34 | 7.19% | 0.0% |
| `src/simplebench` | 15 | 2106.12 | 14.82% | 13.33% |
| `tests` | 13 | 1221.04 | 4.19% | 0.0% |
| `documentation/html/_static` | 16 | 1057.96 | 19.55% | 43.4% |
| `src/simplebench/validators` | 4 | 674.02 | 6.15% | 73.98% |
| `src/simplebench/reporters/reporter` | 6 | 563.98 | 18.92% | 9.21% |
| `tests/factories` | 11 | 511.9 | 4.8% | 0.0% |
| `src/simplebench/reporters/reporter/mixins` | 5 | 445.0 | 8.21% | 3.59% |
| `tests/reporters/reporter/mixins` | 5 | 440.42 | 2.88% | 0.0% |
| `src/simplebench/stats` | 6 | 412.7 | 14.94% | 16.67% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `documentation/html/_downloads/88e7aae14d90ceb1db4850c2e54e5bc2/minimal_parameterized_benchmark.py` -> **100.0%** Exposure
- `documentation/html/_downloads/bd0058ed5532d517f4f50491559904ce/basic_benchmark.py` -> **100.0%** Exposure
- `documentation/tutorials/basic/basic_benchmark.py` -> **100.0%** Exposure
- `documentation/tutorials/parameterized/minimal_parameterized_benchmark.py` -> **100.0%** Exposure
- `src/simplebench/doc_utils.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/simplebench/reporters/csv/reporter/reporter.py` -> **100.0%** Exposure
- `test_plan.py` -> **100.0%** Exposure
- `documentation/html/_sphinx_design_static/design-tabs.js` -> **100.0%** Exposure
- `documentation/html/_static/design-tabs.js` -> **100.0%** Exposure
- `documentation/html/_static/language_data.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_decorators.py` -> **63** Orphaned Functions | **13** Duplicates
- `src/simplebench/stats/stats.py` -> **0** Orphaned Functions | **32** Duplicates
- `tests/test_case.py` -> **14** Orphaned Functions | **9** Duplicates
- `src/simplebench/tasks.py` -> **0** Orphaned Functions | **17** Duplicates
- `tests/factories/reporter/reporter_methods.py` -> **0** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/simplebench/cli.py`** -> AI Confidence: **99.31%**
2. **`src/simplebench/decorators.py`** -> AI Confidence: **99.31%**
3. **`src/simplebench/reporters/csv/reporter/reporter.py`** -> AI Confidence: **99.31%**
4. **`src/simplebench/reporters/reporter/mixins/_argparse.py`** -> AI Confidence: **99.31%**
5. **`src/simplebench/reporters/reporter/mixins/_orchestration.py`** -> AI Confidence: **99.31%**
6. **`src/simplebench/reporters/rich_table/reporter/reporter.py`** -> AI Confidence: **99.31%**
7. **`src/simplebench/runners.py`** -> AI Confidence: **99.31%**
8. **`src/simplebench/tasks.py`** -> AI Confidence: **99.31%**
9. **`tests/reporters/reporter/mixins/test_prioritization.py`** -> AI Confidence: **99.31%**
10. **`tests/reporters/reporter/test_reporter_config.py`** -> AI Confidence: **99.31%**
11. **`tests/test_case.py`** -> AI Confidence: **99.31%**
12. **`src/simplebench/case.py`** -> AI Confidence: **99.24%**
13. **`src/simplebench/reporters/graph/matplotlib/reporter/options/options.py`** -> AI Confidence: **99.24%**
14. **`src/simplebench/reporters/graph/scatterplot/reporter/reporter.py`** -> AI Confidence: **99.24%**
15. **`src/simplebench/session.py`** -> AI Confidence: **99.24%**
16. **`tests/reporters/reporter/test_reporter.py`** -> AI Confidence: **99.24%**
17. **`tests/test_results.py`** -> AI Confidence: **99.24%**
18. **`tests/test_stats.py`** -> AI Confidence: **99.24%**
19. **`src/simplebench/reporters/choices/_base.py`** -> AI Confidence: **99.23%**
20. **`src/simplebench/reporters/choice/choice.py`** -> AI Confidence: **99.18%**
21. **`src/simplebench/reporters/json/reporter/reporter.py`** -> AI Confidence: **99.18%**
22. **`src/simplebench/reporters/reporter/prioritized.py`** -> AI Confidence: **99.18%**
23. **`src/simplebench/timers/info.py`** -> AI Confidence: **99.18%**
24. **`src/simplebench/type_proxies/case_type_proxy.py`** -> AI Confidence: **99.18%**
25. **`tests/factories/reporter/report_log_metadata.py`** -> AI Confidence: **99.18%**
26. **`tests/reporters/reporter/mixins/test_argparse.py`** -> AI Confidence: **99.18%**
27. **`tests/reporters/reporter/mixins/test_targets.py`** -> AI Confidence: **99.18%**
28. **`tests/reporters/validators/test_validate_report_renderer.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1204` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `documentation/html/_static/copybutton.js` (JAVASCRIPT) -> Cumulative Risk: **557.65**
- **Archetype:** `file_cluster_8` (Distance: 11.765 IQR)
- **Magnitude:** 189.46 | **LOC:** 248 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.999%), Safety Score (88.1773%), Verification (80.0%)
- **Heaviest Functions:** `formatCopyText` (Impact: 56.5), `addCopyButtonToCodeCells` (Impact: 35.1), `runWhenDOMLoaded` (Impact: 10.9)

### 2. `documentation/html/_static/language_data.js` (JAVASCRIPT) -> Cumulative Risk: **513.96**
- **Archetype:** `file_cluster_8` (Distance: 11.473 IQR)
- **Magnitude:** 245.08 | **LOC:** 193 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.478%), Verification (80.0%)
- **Heaviest Functions:** `stemWord` (Impact: 82.8), `Stemmer` (Impact: 78.2)

### 3. `src/simplebench/stats/stats.py` (PYTHON) -> Cumulative Risk: **508.34**
- **Archetype:** `file_cluster_16` (Distance: 11.598 IQR)
- **Magnitude:** 253.72 | **LOC:** 614 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (83.0203%), Verification (80.0%)
- **Heaviest Functions:** `__eq__` (Impact: 26.2), `__eq__` (Impact: 26.2), `from_dict` (Impact: 11.5)

### 4. `src/simplebench/reporters/csv/reporter/reporter.py` (PYTHON) -> Cumulative Risk: **493.78**
- **Archetype:** `file_cluster_13` (Distance: 12.675 IQR)
- **Magnitude:** 213.78 | **LOC:** 213 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.0091%), Verification (80.0%)
- **Heaviest Functions:** `render` (Impact: 120.6), `__init__` (Impact: 3.8)

### 5. `documentation/html/_static/searchtools.js` (JAVASCRIPT) -> Cumulative Risk: **489.81**
- **Archetype:** `file_cluster_17` (Distance: 12.161 IQR)
- **Magnitude:** 370.38 | **LOC:** 633 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5749%), Verification (80.0%), Safety Score (65.7578%)
- **Heaviest Functions:** `performTermsSearch` (Impact: 46.7), `_performSearch` (Impact: 46.3), `performObjectSearch` (Impact: 27.6)

### 6. `src/simplebench/reporters/rich_table/reporter/reporter.py` (PYTHON) -> Cumulative Risk: **484.17**
- **Archetype:** `file_cluster_13` (Distance: 11.437 IQR)
- **Magnitude:** 192.22 | **LOC:** 226 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9974%), Safety Score (83.485%), Verification (80.0%)
- **Heaviest Functions:** `render` (Impact: 140.8), `__init__` (Impact: 3.8)

### 7. `src/simplebench/session.py` (PYTHON) -> Cumulative Risk: **473.19**
- **Archetype:** `file_cluster_13` (Distance: 13.346 IQR)
- **Magnitude:** 312.12 | **LOC:** 607 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7644%), Churn (88.56%), Verification (80.0%)
- **Heaviest Functions:** `report` (Impact: 121.0), `__init__` (Impact: 32.2), `run` (Impact: 22.6)

### 8. `src/simplebench/case.py` (PYTHON) -> Cumulative Risk: **469.75**
- **Archetype:** `file_cluster_16` (Distance: 12.282 IQR)
- **Magnitude:** 366.62 | **LOC:** 1016 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (94.64%), Verification (80.0%), State Flux (78.5495%)
- **Heaviest Functions:** `__init__` (Impact: 87.8), `run` (Impact: 35.1), `validate_action_signature` (Impact: 31.3)

### 9. `src/simplebench/tasks.py` (PYTHON) -> Cumulative Risk: **461.06**
- **Archetype:** `file_cluster_16` (Distance: 12.829 IQR)
- **Magnitude:** 323.7 | **LOC:** 534 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9994%), State Flux (98.7433%), Verification (80.0%)
- **Heaviest Functions:** `update` (Impact: 39.8), `__init__` (Impact: 25.4), `__init__` (Impact: 21.2)

### 10. `src/simplebench/reporters/choice/choice.py` (PYTHON) -> Cumulative Risk: **436.07**
- **Archetype:** `file_cluster_13` (Distance: 13.484 IQR)
- **Magnitude:** 137.44 | **LOC:** 348 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Verification (80.0%), Safety Score (73.8794%)
- **Heaviest Functions:** `__eq__` (Impact: 28.8), `deferred_reporter_import` (Impact: 3.9), `__init__` (Impact: 3.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/validators/misc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.332 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.972 IQR)
- **Top Global Matches:** file_cluster_8: 11.332, file_cluster_16: 11.338, file_cluster_7: 11.504
- **Magnitude:** 462.24 | **LOC:** 1100 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9043%), Tech Debt (96.6814%)
**Top Internal Functions/Classes:**
  * `validate_string` (Impact: 47.2)
  * `validate_dirpath` (Impact: 46.1)
  * `validate_sequence_of_type` (Impact: 33.1)
  * `validate_filename` (Impact: 31.8)
    * *Intent:* # Type: list[str]
  * `validate_sequence_of_str` (Impact: 28.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 152`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 1`, `duplicate_logic: 13`
* *Architecture:* `io: 1`, `api: 30`, `import: 6`
* *Defense:* `safety: 41`, `doc: 200`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` re, typing, simplebench.type_proxies.lazy_type_proxy, simplebench.exceptions, pathlib, simplebench.validators.exceptions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `documentation/html/_static/searchtools.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.161 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.169 IQR)
- **Top Global Matches:** file_cluster_17: 12.161, file_cluster_8: 12.584, file_cluster_11: 12.674
- **Magnitude:** 370.38 | **LOC:** 633 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.4951%), Tech Debt (51.9689%)
**Top Internal Functions/Classes:**
  * `performTermsSearch` (Impact: 46.7)
  * `_performSearch` (Impact: 46.3)
  * `performObjectSearch` (Impact: 27.6)
  * `objectSearchCallback` (Impact: 26.8)
    * *Intent:* // maybe skip this "word" // stopwords array is from language_data.js
  * `_displayItem` (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 69`, `args: 41`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 2`
* *Defense:* `safety: 23`, `doc: 6`, `immutability_locks: 71`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/case.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.282 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.156 IQR)
- **Top Global Matches:** file_cluster_16: 12.282, file_cluster_13: 12.346, file_cluster_0: 12.464
- **Magnitude:** 366.62 | **LOC:** 1016 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.9214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 87.8)
  * `run` (Impact: 35.1)
    * *Intent:* # All checks passed
  * `validate_action_signature` (Impact: 31.3)
  * `validate_kwargs_variations` (Impact: 15.9)
  * `validate_options` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 127`, `args: 31`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 39`
* *Architecture:* `io: 1`, `api: 31`, `import: 20`
* *Defense:* `safety: 20`, `doc: 125`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` copy, .protocols, .reporters.protocols, simplebench, .runners, .enums, .validators, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_decorators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.27 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.465 IQR)
- **Top Global Matches:** file_cluster_0: 12.27, file_cluster_16: 12.331, file_cluster_8: 12.401
- **Magnitude:** 335.62 | **LOC:** 708 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (1.7546%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_run_decorated_case` (Impact: 14.3)
  * `test_decorator_use_field_for_n_valid` (Impact: 10.4)
  * `test_benchmark_decorator_registers_case` (Impact: 8.5)
  * `test_decorator_with_no_parameters` (Impact: 5.1)
  * `test_decorator_with_empty_parameters` (Impact: 5.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 241`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `duplicate_logic: 13`, `orphaned_logic: 63`
* *Architecture:* `api: 78`, `import: 7`
* *Defense:* `safety: 74`, `doc: 100`, `test: 145`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, simplebench.defaults, simplebench.session, pytest, simplebench.decorators, simplebench.exceptions, simplebench.enums
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/tasks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.829 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.269 IQR)
- **Top Global Matches:** file_cluster_16: 12.829, file_cluster_13: 12.936, file_cluster_8: 13.115
- **Magnitude:** 323.7 | **LOC:** 534 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.5892%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 39.8)
  * `__init__` (Impact: 25.4)
  * `__init__` (Impact: 21.2)
  * `__init__` (Impact: 13.9)
  * `update` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 76`, `args: 29`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 49`, `duplicate_logic: 17`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 15`, `doc: 158`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, typing, rich.console, .exceptions.tasks, rich.progress, .session, .exceptions, .enums
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/session.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.346 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.299 IQR)
- **Top Global Matches:** file_cluster_13: 13.346, file_cluster_16: 13.438, file_cluster_0: 13.522
- **Magnitude:** 312.12 | **LOC:** 607 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.4834%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `report` (Impact: 121.0)
  * `__init__` (Impact: 32.2)
  * `run` (Impact: 22.6)
  * `parse_args` (Impact: 14.9)
    * *Intent:* """Whether the reporter flags have been added to the ArgumentParser."""
  * `add_reporter_flags` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 113`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`
* *Architecture:* `io: 1`, `api: 30`, `import: 21`
* *Defense:* `safety: 20`, `doc: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` datetime, simplebench, simplebench.case, simplebench.reporters.choice, simplebench.reporters.reporter, simplebench.exceptions, simplebench.reporters.reporter_manager, simplebench.reporters.protocols...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/reporter/reporter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.776 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.409 IQR)
- **Top Global Matches:** file_cluster_13: 11.776, file_cluster_16: 11.916, file_cluster_11: 12.018
- **Magnitude:** 276.7 | **LOC:** 647 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.4191%), Tech Debt (40.0538%)
**Top Internal Functions/Classes:**
  * `report` (Impact: 83.1)
  * `_validate_subclass_config` (Impact: 32.0)
    * *Intent:* """Deferred import of core types to avoid circular imports during initialization. This imports :clas...
  * `set_default_options` (Impact: 18.1)
  * `run_report` (Impact: 13.6)
  * `get_base_unit_for_section` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 120`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`, `planned_debt: 12`
* *Architecture:* `io: 3`, `api: 31`, `import: 25`
* *Defense:* `safety: 15`, `doc: 123`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` runtime, simplebench.results, simplebench.reporters.reporter.options, simplebench.defaults, simplebench.case, simplebench.exceptions, simplebench.reporters.reporter.mixins, rich.text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_case.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.133 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.423 IQR)
- **Top Global Matches:** file_cluster_8: 10.133, file_cluster_16: 10.383, file_cluster_7: 10.408
- **Magnitude:** 261.78 | **LOC:** 1140 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.7506%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_run` (Impact: 14.9)
  * `postrun_benchmark_case` (Impact: 9.6)
  * `benchcase_with_size_and_factor` (Impact: 7.4)
  * `broken_benchcase_missing_bench` (Impact: 6.8)
  * `broken_callback_extra_param` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 137`, `args: 57`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 1`, `duplicate_logic: 9`, `orphaned_logic: 14`
* *Architecture:* `api: 50`, `import: 18`
* *Defense:* `safety: 10`, `doc: 138`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` simplebench.results, .testspec, simplebench.reporters.validators.exceptions, simplebench.reporters.reporter.options, simplebench.iteration, simplebench.case, functools, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/graph/matplotlib/reporter/options/options.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.34 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.5 IQR)
- **Top Global Matches:** file_cluster_16: 12.34, file_cluster_0: 12.481, file_cluster_13: 12.533
- **Magnitude:** 256.1 | **LOC:** 638 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 46.3)
  * `set_default_y_starts_at_zero` (Impact: 7.3)
  * `set_default_x_labels_rotation` (Impact: 7.3)
    * *Intent:* """ return cls._HARDCODED_IMAGE_TYPE _DEFAULT_WIDTH: int | None = None """:meta private:"""
  * `set_default_style` (Impact: 7.3)
  * `set_default_theme` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 82`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 50`, `import: 8`
* *Defense:* `safety: 4`, `doc: 185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` simplebench.validators, simplebench.reporters.graph.enums.image_type, typing, ...enums.style, ...theme, simplebench.exceptions, simplebench.reporters.graph.options, .exceptions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/stats/stats.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.598 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.321 IQR)
- **Top Global Matches:** file_cluster_16: 11.598, file_cluster_0: 11.821, file_cluster_13: 11.86
- **Magnitude:** 253.72 | **LOC:** 614 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.0547%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__eq__` (Impact: 26.2)
  * `__eq__` (Impact: 26.2)
  * `from_dict` (Impact: 11.5)
  * `from_dict` (Impact: 7.8)
  * `mean` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 102`, `args: 35`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`, `duplicate_logic: 32`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 5`, `doc: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..validators, __future__, typing, ..si_units, math, ..exceptions, .exceptions.stats, statistics
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/runners.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.059 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.587 IQR)
- **Top Global Matches:** file_cluster_13: 11.059, file_cluster_16: 11.12, file_cluster_8: 11.422
- **Magnitude:** 251.96 | **LOC:** 544 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.8692%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `default_runner` (Impact: 77.9)
  * `calibrate_rounds` (Impact: 74.8)
    * *Intent:* # We force a garbage collection before measuring memory usage to reduce noise # from uncollected gar...
  * `_run_timed_iteration` (Impact: 28.9)
    * *Intent:* # The Timeout class acts similarly to a context manager, but here we use it # to wrap the entire ben...
  * `__init__` (Impact: 16.7)
  * `run` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 59`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 9`, `dead_code: 2`
* *Architecture:* `io: 3`, `api: 6`, `import: 19`
* *Defense:* `safety: 8`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tracemalloc, gc, .iteration, .enums, .validators, types, .defaults, .results...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/reporter/mixins/_orchestration.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.381 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.353 IQR)
- **Top Global Matches:** file_cluster_8: 10.381, file_cluster_13: 10.445, file_cluster_7: 10.587
- **Magnitude:** 250.3 | **LOC:** 467 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1708%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dispatch_to_targets` (Impact: 131.5)
  * `render_by_section` (Impact: 55.0)
  * `render_by_case` (Impact: 51.5)
  * `_validate_render_by_args` (Impact: 2.5)
    * *Intent:* """Mixin for orchestration-related functionality for the Reporter class. It provides methods to orch...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 50`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 5`, `import: 19`
* *Defense:* `safety: 7`, `doc: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.196
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001374
  * `Imports (Out-Degree: 15):` runtime, simplebench.case, simplebench.exceptions, rich.text, simplebench.type_proxies, simplebench.reporters.protocols, __future__, simplebench.session...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `documentation/html/_static/language_data.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.473 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.066 IQR)
- **Top Global Matches:** file_cluster_8: 11.473, file_cluster_7: 11.932, file_cluster_13: 12.039
- **Magnitude:** 245.08 | **LOC:** 193 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.0398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stemWord` (Impact: 82.8)
  * `Stemmer` (Impact: 78.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 30`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 79`
* *Architecture:* `api: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/reporters/reporter/mixins/test_prioritization.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.231 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.102 IQR)
- **Top Global Matches:** file_cluster_16: 10.231, file_cluster_8: 10.265, file_cluster_13: 10.456
- **Magnitude:** 227.36 | **LOC:** 663 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.636%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_prioritized_options_testspecs` (Impact: 70.1)
  * `get_prioritized_file_append_and_unique_t` (Impact: 52.7)
  * `get_prioritized_options_helper` (Impact: 9.5)
  * `get_prioritized_file_suffix_testspecs` (Impact: 7.9)
  * `get_prioritized_default_targets_testspec` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 58`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`, `orphaned_logic: 9`
* *Architecture:* `api: 15`, `import: 12`
* *Defense:* `safety: 5`, `doc: 75`, `test: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` dataclasses, simplebench.reporters.reporter.options, ....testspec, simplebench.case, simplebench.reporters.choice.choice_conf, simplebench.reporters.choice.choice, ....factories, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/decorators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.324 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.606 IQR)
- **Top Global Matches:** file_cluster_16: 10.324, file_cluster_13: 10.366, file_cluster_8: 10.463
- **Magnitude:** 226.1 | **LOC:** 373 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.6964%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `benchmark` (Impact: 165.7)
  * `decorator` (Impact: 28.9)
  * `case_action_wrapper` (Impact: 10.9)
  * `get_registered_cases` (Impact: 1.9)
  * `clear_registered_cases` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 6`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .reporters.reporter.options, __future__, typing, .case, simplebench.defaults, .vcs, simplebench, .runners...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/csv/reporter/reporter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.675 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.265 IQR)
- **Top Global Matches:** file_cluster_13: 12.675, file_cluster_16: 13.209, file_cluster_8: 13.293
- **Magnitude:** 213.78 | **LOC:** 213 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.6065%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 120.6)
  * `__init__` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 42`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 84`
* *Architecture:* `api: 3`, `import: 18`
* *Defense:* `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` simplebench.results, io, csv, type, simplebench.reporters.reporter.options, simplebench.defaults, .options, simplebench.reporters.reporter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/choice/choice_conf.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.878 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.802 IQR)
- **Top Global Matches:** file_cluster_13: 12.878, file_cluster_16: 12.92, file_cluster_0: 13.036
- **Magnitude:** 213.56 | **LOC:** 485 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.823%), Tech Debt (12.112%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 73.4)
  * `__eq__` (Impact: 27.0)
    * *Intent:* # Ensure that if one is None and the other is not, we set the None one # to the opposite of the othe...
  * `__hash__` (Impact: 2.7)
  * `flags` (Impact: 1.9)
  * `flag_type` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 51`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 62`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 1`, `doc: 129`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` simplebench.reporters.reporter.options, simplebench.validators, typing, simplebench.reporters.choice.exceptions, collections.abc, simplebench.exceptions, simplebench.enums, simplebench.reporters.protocols
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/factories/_primitives.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.378 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.911 IQR)
- **Top Global Matches:** file_cluster_16: 11.378, file_cluster_0: 12.051, file_cluster_7: 12.082
- **Magnitude:** 212.86 | **LOC:** 821 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.3046%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `description_factory` (Impact: 3.7)
  * `default_output_str` (Impact: 1.9)
  * `default_output` (Impact: 1.9)
  * `default_format` (Impact: 1.9)
    * *Intent:* """Return default output for testing purposes. :return: Text("Default Output") :rtype: Output """
  * `default_format_plain` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 148`, `args: 67`, `func_start: 67`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 84`, `import: 8`
* *Defense:* `doc: 245`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.674
  * `Choke Point (Betweenness):` 8.3e-05 | `Ripple Effect (Closeness):` 0.022684
  * `Imports (Out-Degree: 3):` rich.table, .path, __future__, typing, simplebench.enums, ..cache_factory, pathlib, rich.text
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/rich_table/reporter/reporter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.437 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.989 IQR)
- **Top Global Matches:** file_cluster_13: 11.437, file_cluster_8: 11.918, file_cluster_17: 12.009
- **Magnitude:** 192.22 | **LOC:** 226 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.824%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 140.8)
  * `__init__` (Impact: 3.8)
    * *Intent:* **Defined command-line flags:**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 38`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 42`
* *Architecture:* `api: 3`, `import: 16`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` rich.table, .config, __future__, simplebench.results, typing, simplebench.validators, simplebench.defaults, .options...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `documentation/html/_static/copybutton.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.765 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_8: 11.765, file_cluster_17: 11.86, file_cluster_4: 12.001
- **Magnitude:** 189.46 | **LOC:** 248 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.4615%), Tech Debt (72.7309%)
**Top Internal Functions/Classes:**
  * `formatCopyText` (Impact: 56.5)
  * `addCopyButtonToCodeCells` (Impact: 35.1)
  * `runWhenDOMLoaded` (Impact: 10.9)
  * `clearSelection` (Impact: 7.3)
  * `cb` (Impact: 3.2)
    * *Intent:* /** * Set up copy/paste for code blocks
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 34`, `args: 15`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 60`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `concurrency: 3`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/reporter/protocols.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.656 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.48 IQR)
- **Top Global Matches:** file_cluster_16: 11.656, file_cluster_13: 11.953, file_cluster_7: 12.126
- **Magnitude:** 180.34 | **LOC:** 683 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.0922%), Tech Debt (15.2032%)
**Top Internal Functions/Classes:**
  * `dispatch_to_targets` (Impact: 8.0)
  * `render_by_section` (Impact: 7.2)
  * `render_by_case` (Impact: 7.2)
  * `render` (Impact: 5.1)
  * `get_prioritized_options` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 73`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 76`, `import: 15`
* *Defense:* `doc: 283`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` rich.table, simplebench.reporters.reporter.options, __future__, simplebench.reporters.choices.choices, typing, simplebench.enums, simplebench.case, simplebench.session...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/reporters/test_choices_conf.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.058 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.102 IQR)
- **Top Global Matches:** file_cluster_16: 12.058, file_cluster_13: 12.163, file_cluster_8: 12.179
- **Magnitude:** 176.36 | **LOC:** 391 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.118%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setitem_dunder_method_testspecs` (Impact: 16.2)
  * `choices_conf_add_testspecs` (Impact: 11.8)
  * `choices_conf_extend_testspecs` (Impact: 11.5)
  * `choices_conf_remove_testspecs` (Impact: 5.1)
  * `add_choice_conf_to_empty_choices_with_ke` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 70`, `args: 27`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `orphaned_logic: 10`
* *Architecture:* `api: 24`, `import: 6`
* *Defense:* `safety: 23`, `doc: 34`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..kwargs, ..factories, ..testspec, simplebench.exceptions, pytest, simplebench.reporters.choices
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/results.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.404 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.0 IQR)
- **Top Global Matches:** file_cluster_16: 10.404, file_cluster_8: 10.738, file_cluster_13: 10.815
- **Magnitude:** 174.1 | **LOC:** 670 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.4685%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `results_section` (Impact: 16.7)
  * `_validate_variation_cols` (Impact: 13.6)
  * `_validate_variation_marks` (Impact: 11.8)
  * `__init__` (Impact: 8.8)
  * `_validate_iterations` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 130`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 4`
* *Architecture:* `api: 25`, `import: 10`
* *Defense:* `safety: 13`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, typing, copy, types, .defaults, simplebench.exceptions, .iteration, .stats...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/reporters/validators/test_validate_report_renderer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.89 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.141 IQR)
- **Top Global Matches:** file_cluster_13: 10.89, file_cluster_16: 10.905, file_cluster_8: 10.937
- **Magnitude:** 169.78 | **LOC:** 588 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.1233%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_report` (Impact: 13.6)
  * `invalid_render_with_extra_return_type` (Impact: 7.7)
  * `invalid_render_case_wrong_type` (Impact: 7.6)
  * `invalid_render_case_missing_type_hint` (Impact: 7.6)
    * *Intent:* """An invalid render method for testing purposes. :param case: The benchmark case. :type case: Case ...
  * `invalid_render_extra_parameter` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 118`, `args: 25`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 26`, `import: 19`
* *Defense:* `doc: 219`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` simplebench.reporters.validators.exceptions, simplebench.reporters.reporter.options, simplebench.case, simplebench.reporters.choice, simplebench.reporters.reporter, ...testspec, pytest, simplebench.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `documentation/html/py-modindex.html` (HTML) | Magnitude: 0.07 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1205, decorators: 447, io: 401, ui_framework: 173
- `tests/test_decorators.py` (PYTHON) | Magnitude: 335.62 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 423, structural_boundaries: 241, test: 145, doc: 100
- `documentation/html/reports/csv_report_field_definitions.html` (HTML) | Magnitude: 0.07 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 252, indent_spaces: 226, decorators: 164, io: 102
- `documentation/html/_modules/index.html` (HTML) | Magnitude: 0.05 | Delta: **0.269 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 227, indent_spaces: 208, structural_boundaries: 140, decorators: 110
- `documentation/html/reports/rich_table_report.html` (HTML) | Magnitude: 0.08 | Delta: **0.3 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 356, decorators: 309, indent_spaces: 244, io: 134

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/reporters/validators/test_validate_report_renderer.py` (PYTHON) | Magnitude: 169.78 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 256, doc: 219, structural_boundaries: 118, branch: 43
- `tests/type_proxies/test_case_type.py` (PYTHON) | Magnitude: 7.2 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 9, doc: 6, test: 5
- `tests/factories/reporter/reporter_methods.py` (PYTHON) | Magnitude: 118.68 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 191, doc: 86, structural_boundaries: 69, branch: 29
- `src/simplebench/type_proxies/__init__.py` (PYTHON) | Magnitude: 16.28 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 8, doc: 4, import: 4
- `tests/factories/session.py` (PYTHON) | Magnitude: 11.34 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 32, structural_boundaries: 22, indent_spaces: 8, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/test_cache_factory.py` (PYTHON) | Magnitude: 122.86 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 55, doc: 36, generics: 28
- `src/simplebench/iteration.py` (PYTHON) | Magnitude: 92.98 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, doc: 50, encapsulation: 47, structural_boundaries: 44
- `tests/cache_factory.py` (PYTHON) | Magnitude: 86.2 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, doc: 42, structural_boundaries: 29, encapsulation: 26
- `tests/factories/path.py` (PYTHON) | Magnitude: 12.08 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 25, structural_boundaries: 17, api: 6, args: 5
- `tests/reporters/reporter/mixins/test_prioritization.py` (PYTHON) | Magnitude: 227.36 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 447, doc: 75, structural_boundaries: 58, branch: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `documentation/html/_static/sphinx_highlight.js` (JAVASCRIPT) | Magnitude: 111.76 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 103, branch: 26, structural_boundaries: 25, immutability_locks: 18
- `documentation/html/_sphinx_design_static/design-tabs.js` (JAVASCRIPT) | Magnitude: 63.42 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, state_mutation: 31, branch: 13, structural_boundaries: 13
- `documentation/html/_static/design-tabs.js` (JAVASCRIPT) | Magnitude: 63.42 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, state_mutation: 31, branch: 13, structural_boundaries: 13
- `documentation/html/_static/searchtools.js` (JAVASCRIPT) | Magnitude: 370.38 | Delta: **0.423 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 333, state_mutation: 103, branch: 80, immutability_locks: 71

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/simplebench/reporters/csv/reporter/options/fields.py` (PYTHON) | Magnitude: 16.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 28, indent_spaces: 12, structural_boundaries: 5, import: 2
- `src/simplebench/reporters/rich_table/reporter/options/fields.py` (PYTHON) | Magnitude: 16.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 28, indent_spaces: 12, structural_boundaries: 5, import: 2
- `src/simplebench/validators/misc.py` (PYTHON) | Magnitude: 462.24 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 514, doc: 200, structural_boundaries: 152, branch: 135
- `src/simplebench/timers/exceptions.py` (PYTHON) | Magnitude: 15.24 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 20, indent_spaces: 8, structural_boundaries: 5, import: 2
- `src/simplebench/stats/__init__.py` (PYTHON) | Magnitude: 16.34 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, import: 5, doc: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `documentation/_static/custom.css` -> Churn: **94.64%** | Cog Load: 5.3338% | Debt: 79.673%
- `src/simplebench/exceptions/__init__.py` -> Churn: **73.25%** | Cog Load: 5.1716% | Debt: 100.0%
- `documentation/tutorials/parameterized/minimal_parameterized_benchmark.py` -> Churn: **63.09%** | Cog Load: 5.0% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/simplebench/case.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 366.62
- `tests/test_decorators.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 335.62
- `src/simplebench/session.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 312.12
- `tests/test_case.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 261.78
- `src/simplebench/stats/stats.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 253.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/cache_factory.py` -> **Severity: 1.594** (Embedded: 0.0262 * Error Risk: 60.7522%)
- `tests/factories/argparse.py` -> **Severity: 1.217** (Embedded: 0.0347 * Error Risk: 35.034%)
- `tests/kwargs/results_kwargs.py` -> **Severity: 0.211** (Embedded: 0.0027 * Error Risk: 76.875%)
- `tests/factories/reporter_options.py` -> **Severity: 0.189** (Embedded: 0.0041 * Error Risk: 45.8358%)
- `tests/kwargs/case_kwargs.py` -> **Severity: 0.166** (Embedded: 0.0027 * Error Risk: 60.303%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/simplebench/timeout/enums.py` -> **Severity: 137.224** (Blast Radius: 15.698 * Doc Risk: 8.7415%)
- `src/simplebench/utils/machine_info.py` -> **Severity: 98.6** (Blast Radius: 0.986 * Doc Risk: 100.0%)
- `src/simplebench/reporters/reporter/prioritized.py` -> **Severity: 92.107** (Blast Radius: 0.986 * Doc Risk: 93.4147%)
- `documentation/Makefile` -> **Severity: 86.898** (Blast Radius: 0.986 * Doc Risk: 88.1321%)
- `src/simplebench/defaults.py` -> **Severity: 67.624** (Blast Radius: 3.782 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
