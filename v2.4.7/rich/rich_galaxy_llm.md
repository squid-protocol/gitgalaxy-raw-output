# ARCHITECTURAL_BRIEF: rich
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/rich` |
| **Timestamp** | `2026-08-07T04:01:55.819432+00:00` |
| **Scan Duration** | `1.25s` |
| **Git Branch** | `master` |
| **Git Commit** | `fc41075a3206d2a5fd846c6f41c4d2becab814fa` |
| **Git Remote** | `https://github.com/Textualize/rich.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 178 malicious artifacts.

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
| Total Artifacts | 553 |
| Analyzed Artifacts (Scanned) | 399 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 154 |
| Total LOC | 25134 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 72.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3082 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2224 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4482 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 179 | 834 | 44.9% |
| PYTHON | 176 | 24256 | 44.1% |
| MARKDOWN | 39 | 0 | 9.8% |
| MAKEFILE | 1 | 15 | 0.3% |
| YAML | 1 | 4 | 0.3% |
| XML | 1 | 1 | 0.3% |
| BATCH | 1 | 24 | 0.3% |
| PLAINTEXT | 1 | 0 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.667`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 80 | 20.1% |
| file_cluster_13 | 73 | 18.3% |
| file_cluster_16 | 24 | 6.0% |
| file_cluster_0 | 3 | 0.8% |
| file_cluster_7 | 1 | 0.3% |
| file_cluster_2 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 177 | 44.4% |
| Static: Literature & Documentation | 40 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 154*

**Composition by Extension & Reason:**
- `.rst`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 481 LOC), 1x Excluded (Saturation: Line 94 exceeds 500 chars)
- `.png`: 16x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2386 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.gif`: 5x Excluded (Explicitly Denied Extension: '.gif')
- `.svg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.ini')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ai`: 1x Excluded (Explicitly Denied Extension: '.ai')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 79.1 | 5.4 | 0.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 98.3 | 14.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 14.7 | 2.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 20.9 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.2 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 45.4 | 20.0 | 0.0 |
| Instability Exposure | 0.0 | 6.1 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_win32_console.py` (Hits: 28)
- `tests/test_console.py` (Hits: 27)
- `rich/console.py` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **console.py** (`rich/console.py`) — 108 inbound connections
2. **text.py** (`rich/text.py`) — 54 inbound connections
3. **style.py** (`rich/style.py`) — 44 inbound connections
4. **segment.py** (`rich/segment.py`) — 29 inbound connections
5. **measure.py** (`rich/measure.py`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **console.py** (`rich/console.py`) — 53 outbound dependencies
2. **progress.py** (`rich/progress.py`) — 31 outbound dependencies
3. **syntax.py** (`rich/syntax.py`) — 27 outbound dependencies
4. **live.py** (`rich/live.py`) — 26 outbound dependencies
5. **pretty.py** (`rich/pretty.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `rich/console.py`) -> Impact: **573.5** | LOC: 570
- `__init__` (@ `rich/progress.py`) -> Impact: **277.9** | LOC: 881
- `_traverse` (@ `rich/pretty.py`) -> Impact: **162.7** | LOC: 254
- `create` (@ `rich/markdown.py`) -> Impact: **137.6** | LOC: 352
- `__init__` (@ `rich/logging.py`) -> Impact: **115.4** | LOC: 161
- `_make_ansi_codes` (@ `rich/style.py`) -> Impact: **103.9** | LOC: 242
- `escape` (@ `rich/markup.py`) -> Impact: **95.8** | LOC: 183
- `__str__` (@ `rich/style.py`) -> Impact: **85.4** | LOC: 46
- `_render` (@ `rich/_inspect.py`) -> Impact: **63.6** | LOC: 94
- `decode_line` (@ `rich/ansi.py`) -> Impact: **53.4** | LOC: 98

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `rich` | 75 | 7471.8 | 16.74% | 19.31% |
| `tests` | 56 | 2751.9 | 3.71% | 0.0% |
| `examples` | 36 | 728.58 | 8.96% | 0.0% |
| `__monolith__` | 30 | 248.88 | 1.32% | 0.0% |
| `benchmarks/results/darrenburns-2022-mbp` | 177 | 190.68 | 0.03% | 0.0% |
| `benchmarks` | 3 | 180.1 | 6.38% | 33.33% |
| `rich/_unicode_data` | 2 | 46.6 | 6.19% | 0.0% |
| `benchmarks/results` | 1 | 25.3 | 0.0% | 0.0% |
| `questions` | 11 | 11.0 | 0.0% | 0.0% |
| `imgs` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `rich/containers.py` -> **100.0%** Exposure
- `rich/markdown.py` -> **99.9999%** Exposure
- `rich/prompt.py` -> **99.9986%** Exposure
- `rich/_windows.py` -> **99.9871%** Exposure
- `benchmarks/benchmarks.py` -> **99.9792%** Exposure
### Highest State Flux (Mutation/Volatility)
- `rich/rule.py` -> **100.0%** Exposure
- `rich/spinner.py` -> **99.9999%** Exposure
- `rich/_log_render.py` -> **99.9998%** Exposure
- `rich/theme.py` -> **99.998%** Exposure
- `rich/status.py` -> **99.9957%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_text.py` -> **66** Orphaned Functions | **0** Duplicates
- `tests/test_console.py` -> **41** Orphaned Functions | **9** Duplicates
- `rich/markdown.py` -> **0** Orphaned Functions | **38** Duplicates
- `tests/test_pretty.py` -> **24** Orphaned Functions | **13** Duplicates
- `tests/test_progress.py` -> **34** Orphaned Functions | **3** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`examples/table_movie.py`** -> AI Confidence: **99.39%**
2. **`rich/_inspect.py`** -> AI Confidence: **99.31%**
3. **`rich/_log_render.py`** -> AI Confidence: **99.31%**
4. **`rich/align.py`** -> AI Confidence: **99.31%**
5. **`rich/ansi.py`** -> AI Confidence: **99.31%**
6. **`rich/columns.py`** -> AI Confidence: **99.31%**
7. **`rich/console.py`** -> AI Confidence: **99.31%**
8. **`rich/live.py`** -> AI Confidence: **99.31%**
9. **`rich/markup.py`** -> AI Confidence: **99.31%**
10. **`rich/pretty.py`** -> AI Confidence: **99.31%**
11. **`rich/progress_bar.py`** -> AI Confidence: **99.31%**
12. **`rich/segment.py`** -> AI Confidence: **99.31%**
13. **`rich/style.py`** -> AI Confidence: **99.31%**
14. **`rich/syntax.py`** -> AI Confidence: **99.31%**
15. **`rich/table.py`** -> AI Confidence: **99.31%**
16. **`rich/text.py`** -> AI Confidence: **99.31%**
17. **`rich/traceback.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `794` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rich/markdown.py` (PYTHON) -> Cumulative Risk: **569.09**
- **Archetype:** `file_cluster_13` (Distance: 11.437 IQR)
- **Magnitude:** 377.22 | **LOC:** 794 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Documentation (99.3527%), State Flux (92.0925%)
- **Heaviest Functions:** `create` (Impact: 137.6), `create` (Impact: 12.8), `render_bullet` (Impact: 8.6)

### 2. `benchmarks/benchmarks.py` (PYTHON) -> Cumulative Risk: **549.5**
- **Archetype:** `file_cluster_8` (Distance: 9.781 IQR)
- **Magnitude:** 168.58 | **LOC:** 219 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9998%), Tech Debt (99.9792%), Verification (80.0%)
- **Heaviest Functions:** `time_wrapping_unicode_heavy_warm_cache` (Impact: 3.6), `setup` (Impact: 3.0), `_print_table` (Impact: 2.9)

### 3. `rich/text.py` (PYTHON) -> Cumulative Risk: **539.01**
- **Archetype:** `file_cluster_16` (Distance: 11.536 IQR)
- **Magnitude:** 566.94 | **LOC:** 1364 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (94.2518%), State Flux (93.1368%), Verification (80.0%)
- **Heaviest Functions:** `divide` (Impact: 34.8), `render` (Impact: 28.6), `expand_tabs` (Impact: 20.9)

### 4. `rich/prompt.py` (PYTHON) -> Cumulative Risk: **533.2**
- **Archetype:** `file_cluster_16` (Distance: 11.521 IQR)
- **Magnitude:** 125.86 | **LOC:** 401 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9986%), State Flux (96.3755%), Verification (80.0%)
- **Heaviest Functions:** `__call__` (Impact: 14.2), `make_prompt` (Impact: 11.6), `process_response` (Impact: 11.4)

### 5. `rich/console.py` (PYTHON) -> Cumulative Risk: **529.3**
- **Archetype:** `file_cluster_16` (Distance: 12.406 IQR)
- **Magnitude:** 1028.32 | **LOC:** 2685 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (93.7856%), Tech Debt (92.7955%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 573.5), `_is_jupyter` (Impact: 13.1), `__enter__` (Impact: 5.4)

### 6. `rich/progress.py` (PYTHON) -> Cumulative Risk: **520.68**
- **Archetype:** `file_cluster_16` (Distance: 11.531 IQR)
- **Magnitude:** 631.7 | **LOC:** 1717 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (93.4353%), State Flux (85.4872%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 277.9), `__call__` (Impact: 11.2), `render` (Impact: 9.4)

### 7. `rich/live.py` (PYTHON) -> Cumulative Risk: **518.71**
- **Archetype:** `file_cluster_13` (Distance: 12.125 IQR)
- **Magnitude:** 251.82 | **LOC:** 405 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9819%), Verification (80.0%), Safety Score (75.6958%)
- **Heaviest Functions:** `stop` (Impact: 36.5), `refresh` (Impact: 29.4), `start` (Impact: 15.4)

### 8. `rich/_log_render.py` (PYTHON) -> Cumulative Risk: **516.93**
- **Archetype:** `file_cluster_13` (Distance: 10.914 IQR)
- **Magnitude:** 84.72 | **LOC:** 95 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Safety Score (84.4627%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 50.1)

### 9. `rich/align.py` (PYTHON) -> Cumulative Risk: **512.83**
- **Archetype:** `file_cluster_13` (Distance: 10.0 IQR)
- **Magnitude:** 96.76 | **LOC:** 321 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9663%), State Flux (92.3696%), Verification (80.0%)
- **Heaviest Functions:** `generate_segments` (Impact: 29.6), `blank_lines` (Impact: 6.2), `blank_lines` (Impact: 4.2)

### 10. `rich/theme.py` (PYTHON) -> Cumulative Risk: **499.61**
- **Archetype:** `file_cluster_13` (Distance: 12.416 IQR)
- **Magnitude:** 50.46 | **LOC:** 116 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.998%), Tech Debt (99.9073%), Documentation (77.2683%)
- **Heaviest Functions:** `push_theme` (Impact: 6.5), `config` (Impact: 3.8), `pop_theme` (Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rich/console.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.406 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.411 IQR)
- **Top Global Matches:** file_cluster_16: 12.406, file_cluster_13: 12.464, file_cluster_0: 12.751
- **Magnitude:** 1028.32 | **LOC:** 2685 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.3537%), Tech Debt (92.7955%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 573.5)
  * `_is_jupyter` (Impact: 13.1)
  * `__enter__` (Impact: 5.4)
  * `stringify` (Impact: 4.2)
  * `get` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 355`, `args: 116`, `func_start: 116`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 213`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 22`, `api: 98`, `concurrency: 14`, `import: 54`
* *Defense:* `safety: 51`, `doc: 236`, `test: 4`, `sync_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 104.767
  * `Choke Point (Betweenness):` 0.035788 | `Ripple Effect (Closeness):` 0.287036
  * `Imports (Out-Degree: 33):` .style, rich._windows_renderer, abc, getpass, inspect, .status, rich.json, .traceback...
  * `Imported By (In-Degree: 108):` (Excluded from Brief to save tokens)

### `rich/progress.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.531 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.316 IQR)
- **Top Global Matches:** file_cluster_16: 11.531, file_cluster_13: 11.719, file_cluster_8: 11.968
- **Magnitude:** 631.7 | **LOC:** 1717 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (19.6703%), Tech Debt (93.4353%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 277.9)
  * `__call__` (Impact: 11.2)
  * `render` (Impact: 9.4)
  * `run` (Impact: 7.6)
  * `render` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 265`, `args: 97`, `func_start: 96`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 114`, `duplicate_logic: 23`
* *Architecture:* `io: 8`, `api: 92`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 9`, `doc: 162`, `test: 1`, `sync_locks: 6`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.139
  * `Choke Point (Betweenness):` 0.001645 | `Ripple Effect (Closeness):` 0.020101
  * `Imports (Out-Degree: 11):` .style, abc, operator, .table, typing_extensions, time, .highlighter, .syntax...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `rich/text.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.536 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.288 IQR)
- **Top Global Matches:** file_cluster_16: 11.536, file_cluster_13: 11.702, file_cluster_8: 11.852
- **Magnitude:** 566.94 | **LOC:** 1364 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (24.3982%), Tech Debt (94.2518%)
**Top Internal Functions/Classes:**
  * `divide` (Impact: 34.8)
  * `render` (Impact: 28.6)
  * `expand_tabs` (Impact: 20.9)
  * `join` (Impact: 15.5)
  * `__getitem__` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 179`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 109`, `planned_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `api: 74`, `import: 22`
* *Defense:* `safety: 16`, `doc: 112`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.177
  * `Choke Point (Betweenness):` 0.007499 | `Ripple Effect (Closeness):` 0.214977
  * `Imports (Out-Degree: 15):` rich.text, .style, operator, ._pick, ._loop, functools, .align, .emoji...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `rich/pretty.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.508 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.224 IQR)
- **Top Global Matches:** file_cluster_16: 10.508, file_cluster_13: 10.522, file_cluster_8: 10.661
- **Magnitude:** 391.62 | **LOC:** 1017 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.0881%), Tech Debt (38.3079%)
**Top Internal Functions/Classes:**
  * `_traverse` (Impact: 162.7)
  * `iter_tokens` (Impact: 21.9)
  * `iter_rich_args` (Impact: 16.8)
  * `expand` (Impact: 15.5)
  * `to_repr` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 154`, `args: 44`, `func_start: 34`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 18`, `duplicate_logic: 6`
* *Architecture:* `io: 3`, `api: 27`, `import: 31`
* *Defense:* `safety: 40`, `doc: 48`, `test: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.234
  * `Choke Point (Betweenness):` 0.001421 | `Ripple Effect (Closeness):` 0.16574
  * `Imports (Out-Degree: 9):` rich, .abc, inspect, ._pick, reprlib, ._loop, .highlighter, dataclasses...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `rich/markdown.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.437 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.924 IQR)
- **Top Global Matches:** file_cluster_13: 11.437, file_cluster_16: 11.541, file_cluster_0: 11.779
- **Magnitude:** 377.22 | **LOC:** 794 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.3373%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 137.6)
  * `create` (Impact: 12.8)
  * `render_bullet` (Impact: 8.6)
  * `on_child_close` (Impact: 8.4)
  * `create` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 159`, `args: 57`, `func_start: 57`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 67`, `duplicate_logic: 38`
* *Architecture:* `io: 2`, `api: 51`, `import: 23`
* *Defense:* `safety: 17`, `doc: 58`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.102
  * `Choke Point (Betweenness):` 0.001016 | `Ripple Effect (Closeness):` 0.11342
  * `Imports (Out-Degree: 11):` .style, markdown_it.token, ._loop, rich.table, .syntax, dataclasses, , pydoc...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rich/style.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.709 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.075 IQR)
- **Top Global Matches:** file_cluster_16: 10.709, file_cluster_13: 11.023, file_cluster_0: 11.066
- **Magnitude:** 332.06 | **LOC:** 793 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.1135%), Tech Debt (17.7747%)
**Top Internal Functions/Classes:**
  * `_make_ansi_codes` (Impact: 103.9)
  * `__str__` (Impact: 85.4)
  * `on` (Impact: 8.3)
  * `copy` (Impact: 7.8)
  * `update_link` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 112`, `args: 38`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 43`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 35`, `import: 10`
* *Defense:* `safety: 9`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.843
  * `Choke Point (Betweenness):` 0.001097 | `Ripple Effect (Closeness):` 0.209712
  * `Imports (Out-Degree: 2):` sys, .color, pickle, operator, , typing, .repr, .terminal_theme...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `tests/test_text.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.252 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.968 IQR)
- **Top Global Matches:** file_cluster_8: 12.252, file_cluster_0: 12.66, file_cluster_13: 12.661
- **Magnitude:** 322.92 | **LOC:** 1130 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.6068%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_render` (Impact: 21.1)
  * `test_append_tokens` (Impact: 7.9)
  * `test_soft_wrap` (Impact: 6.6)
    * *Intent:* """Regression text for https://github.com/Textualize/rich/issues/3479"""
  * `test_append` (Impact: 5.8)
  * `test_highlight_regex` (Impact: 5.0)
    * *Intent:* # As a string text = Text("peek-a-boo") count = text.highlight_regex(r"NEVER_MATCH", "red") assert c...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 345`, `args: 92`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`, `orphaned_logic: 66`
* *Architecture:* `api: 92`, `import: 8`
* *Defense:* `safety: 235`, `doc: 32`, `test: 334`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pytest, rich.text, re, typing, rich.style, io, rich.console, rich.measure
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_console.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.741 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.803 IQR)
- **Top Global Matches:** file_cluster_8: 10.741, file_cluster_13: 10.741, file_cluster_16: 10.819
- **Magnitude:** 272.58 | **LOC:** 1130 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.6017%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print` (Impact: 43.5)
  * `test_console_options_update` (Impact: 9.8)
  * `print` (Impact: 5.6)
  * `test_get_style_error` (Impact: 5.5)
  * `test_capture` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 179`, `args: 55`, `func_start: 71`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 17`, `duplicate_logic: 9`, `orphaned_logic: 41`
* *Architecture:* `io: 27`, `api: 55`, `import: 24`
* *Defense:* `safety: 61`, `doc: 16`, `test: 195`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` pytest, rich, rich.color, rich.text, rich.control, rich.measure, rich.style, rich._null_file...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/syntax.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.846 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.861 IQR)
- **Top Global Matches:** file_cluster_13: 10.846, file_cluster_16: 10.908, file_cluster_8: 11.028
- **Magnitude:** 269.02 | **LOC:** 986 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.6847%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `guess_lexer` (Impact: 19.4)
  * `tokens_to_spans` (Impact: 18.5)
  * `_apply_stylized_ranges` (Impact: 16.9)
  * `_get_line_numbers_color` (Impact: 11.1)
  * `_process_code` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 132`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 69`, `duplicate_logic: 9`
* *Architecture:* `io: 5`, `api: 25`, `import: 28`
* *Defense:* `safety: 20`, `doc: 56`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.731
  * `Choke Point (Betweenness):` 0.001307 | `Ripple Effect (Closeness):` 0.136285
  * `Imports (Out-Degree: 12):` pygments.lexer, .style, pygments.styles, abc, pygments.util, ._loop, pathlib, pygments.lexers...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `tests/test_progress.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.75 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.035 IQR)
- **Top Global Matches:** file_cluster_8: 11.75, file_cluster_13: 11.86, file_cluster_16: 12.024
- **Magnitude:** 267.84 | **LOC:** 691 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_wrap_file_task_total` (Impact: 13.3)
  * `test_progress_track` (Impact: 12.4)
  * `test_wrap_file` (Impact: 11.2)
  * `test_progress_max_refresh` (Impact: 10.6)
  * `test_open` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 167`, `args: 57`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 27`, `duplicate_logic: 3`, `orphaned_logic: 34`
* *Architecture:* `io: 12`, `api: 44`, `import: 13`
* *Defense:* `safety: 89`, `doc: 4`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` pytest, rich.progress_bar, tempfile, rich.text, os, .render, rich.progress, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/live.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.125 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.977 IQR)
- **Top Global Matches:** file_cluster_13: 12.125, file_cluster_16: 12.567, file_cluster_11: 12.614
- **Magnitude:** 251.82 | **LOC:** 405 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.6856%), Tech Debt (72.8766%)
**Top Internal Functions/Classes:**
  * `stop` (Impact: 36.5)
  * `refresh` (Impact: 29.4)
  * `start` (Impact: 15.4)
  * `renderable` (Impact: 12.7)
    * *Intent:* """Disable redirecting of stdout / stderr."""
  * `_enable_redirect_io` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 86`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 82`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 10`, `api: 15`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 11`, `doc: 26`, `test: 1`, `sync_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.086
  * `Choke Point (Betweenness):` 0.002524 | `Ripple Effect (Closeness):` 0.167907
  * `Imports (Out-Degree: 10):` .table, typing_extensions, .live_render, ipywidgets, time, .align, .syntax, .panel...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `examples/downloader.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.513 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.643 IQR)
- **Top Global Matches:** file_cluster_13: 9.513, file_cluster_8: 9.898, file_cluster_4: 10.198
- **Magnitude:** 241.64 | **LOC:** 82 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.9933%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 21`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 5`, `api: 3`, `concurrency: 3`, `import: 9`
* *Defense:* `doc: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` urllib.request, sys, signal, threading, typing, rich.progress, os.path, concurrent.futures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/traceback.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.51 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.79 IQR)
- **Top Global Matches:** file_cluster_13: 10.51, file_cluster_16: 10.657, file_cluster_0: 10.768
- **Magnitude:** 233.3 | **LOC:** 925 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.006%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_render_stack` (Impact: 48.0)
  * `render_stack` (Impact: 41.6)
  * `ipy_excepthook_closure` (Impact: 18.2)
  * `from_exception` (Impact: 5.5)
  * `__init__` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 109`, `args: 21`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 51`, `dead_code: 2`
* *Architecture:* `io: 15`, `api: 21`, `import: 28`
* *Defense:* `safety: 24`, `doc: 18`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.451
  * `Choke Point (Betweenness):` 0.001417 | `Ripple Effect (Closeness):` 0.163109
  * `Imports (Out-Degree: 9):` rich, .style, inspect, traceback, pygments.util, ._loop, .highlighter, pygments.lexers...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/test_pretty.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.417 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.087 IQR)
- **Top Global Matches:** file_cluster_0: 11.417, file_cluster_16: 11.456, file_cluster_8: 11.544
- **Magnitude:** 215.42 | **LOC:** 760 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.2485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ansi_in_pretty_repr` (Impact: 25.2)
  * `__repr__` (Impact: 9.0)
  * `test_dataclass_no_attribute` (Impact: 4.4)
    * *Intent:* """ Test that can use None as key to have tuple positional values and with a default. """
  * `test_ipy_display_hook__special_repr_rais` (Impact: 2.7)
    * *Intent:* # should be repr as-is
  * `test_pretty_namedtuple` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 234`, `args: 77`, `func_start: 77`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 7`, `duplicate_logic: 13`, `orphaned_logic: 24`
* *Architecture:* `io: 21`, `api: 85`, `import: 14`
* *Defense:* `safety: 88`, `doc: 22`, `test: 140`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sys, pytest, rich.text, attr, rich.pretty, dataclasses, typing, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/color.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.369 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.104 IQR)
- **Top Global Matches:** file_cluster_13: 10.369, file_cluster_8: 10.412, file_cluster_16: 10.565
- **Magnitude:** 207.56 | **LOC:** 622 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.5625%), Tech Debt (20.0306%)
**Top Internal Functions/Classes:**
  * `downgrade` (Impact: 42.7)
  * `get_ansi_codes` (Impact: 36.0)
  * `parse` (Impact: 30.3)
  * `from_ansi` (Impact: 5.6)
  * `system` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 124`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `state_mutation: 25`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 30`, `import: 17`
* *Defense:* `safety: 15`, `doc: 46`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.734
  * `Choke Point (Betweenness):` 0.002658 | `Ripple Effect (Closeness):` 0.17476
  * `Imports (Out-Degree: 6):` sys, .color_triplet, re, .style, enum, ._palettes, .console, .table...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `rich/segment.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.832 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.57 IQR)
- **Top Global Matches:** file_cluster_16: 9.832, file_cluster_13: 10.072, file_cluster_7: 10.174
- **Magnitude:** 196.4 | **LOC:** 784 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.6434%), Tech Debt (41.7012%)
**Top Internal Functions/Classes:**
  * `_split_cells` (Impact: 21.8)
  * `split_lines` (Impact: 16.6)
  * `strip_links` (Impact: 12.6)
    * *Intent:* """ _height = height or len(lines) blank = ( [cls(" " * width + "\n", style)] if new_lines else [cls...
  * `simplify` (Impact: 11.3)
  * `remove_color` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 94`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 13`, `duplicate_logic: 4`
* *Architecture:* `api: 42`, `import: 13`
* *Defense:* `safety: 3`, `doc: 56`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.133
  * `Choke Point (Betweenness):` 0.003089 | `Ripple Effect (Closeness):` 0.188203
  * `Imports (Out-Degree: 6):` rich.syntax, rich.text, .style, enum, operator, .console, itertools, logging...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `tests/test_traceback.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.078 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.667 IQR)
- **Top Global Matches:** file_cluster_8: 12.078, file_cluster_0: 12.245, file_cluster_13: 12.258
- **Magnitude:** 174.58 | **LOC:** 400 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_handler` (Impact: 16.3)
  * `test_nested_exception` (Impact: 8.2)
  * `test_caused_exception` (Impact: 8.2)
  * `test_traceback_console_theme_applies` (Impact: 7.2)
    * *Intent:* """ Ensure that themes supplied via Console init work on Tracebacks. Regression test for https://git...
  * `test_recursive_exception` (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 99`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `duplicate_logic: 10`, `orphaned_logic: 21`
* *Architecture:* `io: 9`, `api: 35`, `import: 8`
* *Defense:* `safety: 88`, `doc: 12`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sys, pytest, re, rich.theme, rich.traceback, typing, io, rich.console
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/_inspect.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.993 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.483 IQR)
- **Top Global Matches:** file_cluster_13: 11.993, file_cluster_16: 12.173, file_cluster_12: 12.36
- **Magnitude:** 170.84 | **LOC:** 273 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (48.2909%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_render` (Impact: 63.6)
  * `_get_signature` (Impact: 22.1)
  * `_make_title` (Impact: 9.2)
  * `_get_formatted_doc` (Impact: 5.7)
  * `safe_getattr` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 58`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 16`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.805
  * `Choke Point (Betweenness):` 0.000263 | `Ripple Effect (Closeness):` 0.005025
  * `Imports (Out-Degree: 6):` .pretty, .control, .highlighter, .console, .panel, .table, inspect, .text...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `benchmarks/benchmarks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.781 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.563 IQR)
- **Top Global Matches:** file_cluster_8: 9.781, file_cluster_13: 9.904, file_cluster_7: 10.436
- **Magnitude:** 168.58 | **LOC:** 219 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.1453%), Tech Debt (99.9792%)
**Top Internal Functions/Classes:**
  * `time_wrapping_unicode_heavy_warm_cache` (Impact: 3.6)
  * `setup` (Impact: 3.0)
  * `_print_table` (Impact: 2.9)
  * `setup` (Impact: 2.1)
  * `setup` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 72`, `args: 43`, `func_start: 43`, `class_start: 9`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 7`
* *Architecture:* `api: 76`, `import: 10`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` rich.syntax, rich.color, rich.table, rich.segment, rich.text, rich.pretty, rich.style, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/logging.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.714 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.421 IQR)
- **Top Global Matches:** file_cluster_13: 10.714, file_cluster_8: 10.96, file_cluster_16: 10.981
- **Magnitude:** 155.46 | **LOC:** 298 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.9735%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 115.4)
  * `divide` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 39`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`
* *Architecture:* `io: 1`, `api: 6`, `import: 14`
* *Defense:* `safety: 10`, `doc: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.9
  * `Choke Point (Betweenness):` 0.00038 | `Ripple Effect (Closeness):` 0.124707
  * `Imports (Out-Degree: 5):` pathlib, .highlighter, .console, , logging, .text, datetime, types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/table.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.691 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.294 IQR)
- **Top Global Matches:** file_cluster_16: 10.691, file_cluster_13: 10.839, file_cluster_8: 10.901
- **Magnitude:** 143.96 | **LOC:** 1016 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.6707%), Tech Debt (25.0442%)
**Top Internal Functions/Classes:**
  * `_extra_width` (Impact: 7.4)
  * `get_row_style` (Impact: 6.5)
    * *Intent:* *headers,
  * `__init__` (Impact: 4.6)
  * `expand` (Impact: 3.7)
  * `padding` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 100`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 60`, `duplicate_logic: 4`
* *Architecture:* `api: 26`, `import: 18`
* *Defense:* `safety: 7`, `doc: 86`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.342
  * `Choke Point (Betweenness):` 0.002972 | `Ripple Effect (Closeness):` 0.128128
  * `Imports (Out-Degree: 13):` .protocol, .style, .align, .console, dataclasses, , .segment, .text...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `rich/_win32_console.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.753 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.939 IQR)
- **Top Global Matches:** file_cluster_8: 9.753, file_cluster_16: 9.818, file_cluster_7: 9.998
- **Magnitude:** 143.68 | **LOC:** 662 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_styled` (Impact: 25.7)
    * *Intent:* """Set the cursor info - used for adjusting cursor visibility and width Args: std_handle (wintypes.H...
  * `move_cursor_forward` (Impact: 5.8)
  * `move_cursor_backward` (Impact: 5.8)
  * `move_cursor_to` (Impact: 5.5)
  * `GetConsoleMode` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 68`, `args: 29`, `func_start: 29`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`
* *Architecture:* `io: 2`, `api: 36`, `import: 9`
* *Defense:* `safety: 3`, `doc: 62`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.452
  * `Choke Point (Betweenness):` 0.001138 | `Ripple Effect (Closeness):` 0.164151
  * `Imports (Out-Degree: 3):` sys, rich.color, ctypes, typing, rich.style, rich.console, time
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/test_inspect.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.048 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.559 IQR)
- **Top Global Matches:** file_cluster_0: 10.048, file_cluster_8: 10.133, file_cluster_13: 10.289
- **Magnitude:** 132.06 | **LOC:** 517 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.2069%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_inspect_empty_dict` (Impact: 7.9)
  * `test_inspect_text` (Impact: 7.6)
  * `test_inspect_builtin_function_only_pytho` (Impact: 5.9)
  * `test_inspect_swig_edge_case` (Impact: 5.9)
  * `test_qualname_in_slots` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 121`, `args: 51`, `func_start: 29`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1`, `duplicate_logic: 3`, `orphaned_logic: 17`
* *Architecture:* `io: 18`, `api: 34`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 25`, `doc: 14`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sys, pytest, rich, typing, types, io, rich._inspect, rich.console...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/repr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.423 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.902 IQR)
- **Top Global Matches:** file_cluster_16: 10.423, file_cluster_13: 10.651, file_cluster_0: 10.699
- **Magnitude:** 129.84 | **LOC:** 150 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.0411%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `do_replace` (Impact: 48.5)
  * `auto_rich_repr` (Impact: 31.9)
  * `auto_repr` (Impact: 25.2)
  * `auto` (Impact: 2.1)
  * `auto` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 29`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 6`, `duplicate_logic: 3`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 8`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.191
  * `Choke Point (Betweenness):` 0.000373 | `Ripple Effect (Closeness):` 0.1152
  * `Imports (Out-Degree: 1):` typing, functools, inspect, rich.console
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rich/prompt.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.521 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.05 IQR)
- **Top Global Matches:** file_cluster_16: 11.521, file_cluster_0: 11.677, file_cluster_13: 11.69
- **Magnitude:** 125.86 | **LOC:** 401 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.6528%), Tech Debt (99.9986%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 14.2)
  * `make_prompt` (Impact: 11.6)
  * `process_response` (Impact: 11.4)
  * `check_choice` (Impact: 5.5)
  * `render_default` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 53`, `args: 18`, `func_start: 18`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 31`, `dead_code: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 20`, `import: 5`
* *Defense:* `safety: 7`, `doc: 36`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.571
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.002513
  * `Imports (Out-Degree: 2):` rich, .console, , .text, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/test_pretty.py` (PYTHON) | Magnitude: 215.42 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 450, structural_boundaries: 234, test: 140, safety: 88
- `tests/test_repr.py` (PYTHON) | Magnitude: 85.56 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 51, state_mutation: 21, test: 20
- `tests/test_inspect.py` (PYTHON) | Magnitude: 132.06 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 321, structural_boundaries: 121, test: 53, args: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/test_theme.py` (PYTHON) | Magnitude: 21.3 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 23, test: 15, safety: 8
- `rich/theme.py` (PYTHON) | Magnitude: 50.46 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 21, state_mutation: 19, doc: 16
- `tests/test_file_proxy.py` (PYTHON) | Magnitude: 13.36 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 14, test: 10, import: 5
- `examples/recursive_error.py` (PYTHON) | Magnitude: 5.8 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, args: 2, func_start: 2
- `rich/align.py` (PYTHON) | Magnitude: 96.76 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 53, branch: 48, generics: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `rich/__init__.py` (PYTHON) | Magnitude: 21.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 23, encapsulation: 20, doc: 12
- `rich/pretty.py` (PYTHON) | Magnitude: 391.62 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 706, branch: 157, structural_boundaries: 154, encapsulation: 153
- `rich/scope.py` (PYTHON) | Magnitude: 9.68 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 23, generics: 11, import: 9
- `examples/exception.py` (PYTHON) | Magnitude: 10.8 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, doc: 6, branch: 3
- `rich/console.py` (PYTHON) | Magnitude: 1028.32 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1612, structural_boundaries: 355, branch: 351, encapsulation: 324

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/test_markdown.py` (PYTHON) | Magnitude: 25.38 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 25, doc: 20, sec_reflection_metaprogramming: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `rich/errors.py` (PYTHON) | Magnitude: 23.68 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 18, structural_boundaries: 9, class_start: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/test_console.py` (PYTHON) | Magnitude: 272.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 689, test: 195, structural_boundaries: 179, sec_high_risk_execution: 131
- `examples/attrs.py` (PYTHON) | Magnitude: 18.8 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, import: 6, branch: 3
- `tools/make_emoji.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 3, safety: 2
- `tests/test_markup.py` (PYTHON) | Magnitude: 72.66 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 90, test: 87, safety: 60
- `tests/test_live_render.py` (PYTHON) | Magnitude: 15.7 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 23, test: 15, safety: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rich/console.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 1028.32
- `rich/pretty.py` -> **Joel Ostblom** (100.0% isolated ownership) | Magnitude: 391.62
- `rich/markdown.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 377.22
- `rich/style.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 332.06
- `tests/test_text.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 322.92

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rich/console.py` -> **Severity: 3.356** (Bridge: 0.0358 * Flux: 93.7856%)
- `rich/text.py` -> **Severity: 0.698** (Bridge: 0.0075 * Flux: 93.1368%)
- `rich/live.py` -> **Severity: 0.252** (Bridge: 0.0025 * Flux: 99.9819%)
- `rich/table.py` -> **Severity: 0.213** (Bridge: 0.003 * Flux: 71.6782%)
- `rich/align.py` -> **Severity: 0.17** (Bridge: 0.0018 * Flux: 92.3696%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rich/console.py` -> **Severity: 17.309** (Embedded: 0.287 * Error Risk: 60.3034%)
- `rich/jupyter.py` -> **Severity: 14.473** (Embedded: 0.1809 * Error Risk: 80.0%)
- `rich/rule.py` -> **Severity: 13.811** (Embedded: 0.1663 * Error Risk: 83.0581%)
- `rich/_log_render.py` -> **Severity: 13.561** (Embedded: 0.1606 * Error Risk: 84.4627%)
- `rich/protocol.py` -> **Severity: 13.007** (Embedded: 0.1626 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rich/console.py` -> **Severity: 2410.689** (Blast Radius: 104.767 * Doc Risk: 23.01%)
- `rich/style.py` -> **Severity: 2188.124** (Blast Radius: 36.843 * Doc Risk: 59.3905%)
- `rich/text.py` -> **Severity: 2135.07** (Blast Radius: 44.177 * Doc Risk: 48.3299%)
- `rich/segment.py` -> **Severity: 1451.602** (Blast Radius: 26.133 * Doc Risk: 55.5467%)
- `rich/palette.py` -> **Severity: 1292.434** (Blast Radius: 17.591 * Doc Risk: 73.4713%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
