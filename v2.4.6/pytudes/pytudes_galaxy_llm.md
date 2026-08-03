# ARCHITECTURAL_BRIEF: pytudes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/pytudes` |
| **Timestamp** | `2026-08-03T19:40:20.741110+00:00` |
| **Scan Duration** | `1.32s` |
| **Git Branch** | `main` |
| **Git Commit** | `2e8234232da3e6d0ffeccaea081810862b3e6f99` |
| **Git Remote** | `https://github.com/norvig/pytudes.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 21 malicious artifacts.

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
| Total Artifacts | 205 |
| Analyzed Artifacts (Scanned) | 41 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 164 |
| Total LOC | 5035 |
| Volatility Index | 0.049 |
| % Scanned of codebase = | 20.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 19 | 2502 | 46.3% |
| PLAINTEXT | 10 | 2 | 24.4% |
| CSV | 5 | 945 | 12.2% |
| MARKDOWN | 4 | 0 | 9.8% |
| JAVA | 2 | 316 | 4.9% |
| HTML | 1 | 1270 | 2.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.395`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 22 | 53.7% |
| file_cluster_13 | 2 | 4.9% |
| file_cluster_17 | 2 | 4.9% |
| file_cluster_16 | 1 | 2.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 29.3% |
| Static: Minified & Vendor Opaque Mass | 2 | 4.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 164*

**Composition by Extension & Reason:**
- `.ipynb`: 105x Excluded (Unsupported Extension: '.ipynb'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (Monolithic Amalgamation: 128458 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 333334 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 286359 LOC exceeds safe regex boundaries)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.tsv`: 2x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Massive Static Asset Blob: 8655 LOC), 1x Excluded (Monolithic Amalgamation: 42173 LOC exceeds safe regex boundaries)
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.class`: 3x Excluded (Explicitly Denied Extension: '.class')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 1x Excluded (Massive Static Asset Blob: 6454 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.md`: 1x Excluded (Monolithic Amalgamation: 49079 LOC exceeds safe regex boundaries)
- `.svg`: 1x Excluded (Static Asset Blob without Intent: 1904 LOC)
- `.html`: 1x Excluded (Embedded Array/Matrix Payload: 7606 commas in 1284 LOC)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 73.6 | 19.7 | 14.2 | 0.0 |
| Error & Exception Exposure | 0.0 | 64.7 | 14.8 | 5.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 98.8 | 19.2 | 0.0 | 0.0 |
| Testing Exposure | 2.0 | 80.0 | 59.9 | 80.0 | 80.0 |
| API Exposure | 0.0 | 11.9 | 5.7 | 6.4 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.8 | 16.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 6.8 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 86.7 | 100.0 | 99.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.8 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 86.7 | 5.2 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 75.6 | 99.7 | 17.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 74.1 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 70.7 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `py/lispy.py` (Hits: 11)
- `py/docex.py` (Hits: 6)
- `py/py2html.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`README.md`) — 0 inbound connections
2. **README.md** (`data/ngrams/README.md`) — 0 inbound connections
3. **reviews.md** (`txt/reviews.md`) — 0 inbound connections
4. **tools.md** (`txt/tools.md`) — 0 inbound connections
5. **latlong.htm** (`data/latlong.htm`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ngrams.py** (`py/ngrams.py`) — 10 outbound dependencies
2. **Sudoku.java** (`ipynb/Sudoku.java`) — 6 outbound dependencies
3. **Sudoku.java** (`py/Sudoku.java`) — 6 outbound dependencies
4. **docex.py** (`py/docex.py`) — 6 outbound dependencies
5. **lispy.py** (`py/lispy.py`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `showh` (@ `py/ibol.py`) -> Impact: **514.5** | LOC: 106
- `copyblock` (@ `py/yaptu.py`) -> Impact: **481.1** | LOC: 101
- `main` (@ `ipynb/Sudoku.java`) -> Impact: **346.6** | LOC: 25
- `write_dict` (@ `py/lettercount.py`) -> Impact: **310.8** | LOC: 153
- `letters` (@ `py/pal3.py`) -> Impact: **308.6** | LOC: 109
- `expand_accumulations` (@ `py/testaccum.py`) -> Impact: **283.7** | LOC: 63
  * *Intent:* """Replace any accumulation displays in program_text with calls to accumulation. Used to simulate a hypothetical Python interpreter that actually hand...
- `expand` (@ `py/lispy.py`) -> Impact: **236.4** | LOC: 51
- `color` (@ `py/py2html.py`) -> Impact: **173.7** | LOC: 80
- `Pedit` (@ `py/ngrams.py`) -> Impact: **166.5** | LOC: 40
- `tally` (@ `py/SET.py`) -> Impact: **159.2** | LOC: 67

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `showh` (@ `py/ibol.py`) -> **O(2^N) [Recursive]**
- `parse` (@ `py/parse.py`) -> **O(2^N) [Recursive]**
- `color` (@ `py/py2html.py`) -> **O(2^N) [Recursive]**
- `copyblock` (@ `py/yaptu.py`) -> **O(2^N) [Recursive]**
- `unit_tests` (@ `py/spell.py`) -> **O(2^N) [Recursive]**
  * *Intent:* ################ Test Code def unit_tests(): assert correction('speling') == 'spelling' # insert assert correction('korrectud') == 'corrected' # repla...
- `expand_accumulations` (@ `py/testaccum.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Replace any accumulation displays in program_text with calls to accumulation. Used to simulate a hypothetical Python interpreter that actually hand...
- `used` (@ `ipynb/portman.py`) -> **O(2^N) [Recursive]**
- `tally` (@ `py/SET.py`) -> **O(2^N) [Recursive]**
- `run_string` (@ `py/docex.py`) -> **O(2^N) [Recursive]**
- `write_dict` (@ `py/lettercount.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `letters` (@ `py/pal3.py`) -> DB Complexity: **36**
- `add_globals` (@ `py/lispy.py`) -> DB Complexity: **21**
- `atom` (@ `py/lispy.py`) -> DB Complexity: **18**
- `copyblock` (@ `py/yaptu.py`) -> DB Complexity: **18**
- `__init__` (@ `py/docex.py`) -> DB Complexity: **17**
  * *Intent:* '''>>> len('abc') 3 >>> len([]) 0 >>> len(5)) Traceback (most recent call last): ... TypeError: len() of unsized object '''
- `color` (@ `py/py2html.py`) -> DB Complexity: **17**
- `search` (@ `py/pal.py`) -> DB Complexity: **15**
- `solve_all` (@ `py/sudoku.py`) -> DB Complexity: **9**
  * *Intent:* """Attempt to solve a sequence of grids. Report results."""
- `write_dict` (@ `py/lettercount.py`) -> DB Complexity: **7**
- `read_dict` (@ `py/pal.py`) -> DB Complexity: **7**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `py` | 22 | 6671.54 | 22.39% | 21.35% |
| `ipynb` | 13 | 1001.32 | 2.94% | 3.73% |
| `data` | 1 | 40.4 | 0.0% | 0.0% |
| `__monolith__` | 2 | 5.22 | 0.0% | 0.0% |
| `txt` | 2 | 2.0 | 0.0% | 0.0% |
| `data/ngrams` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `py/pal.py` -> **98.7998%** Exposure
- `py/pal2.py` -> **88.5488%** Exposure
- `py/ngrams.py` -> **80.9593%** Exposure
- `py/Sudoku.java` -> **53.2847%** Exposure
- `ipynb/Sudoku.java` -> **48.4761%** Exposure
### Highest State Flux (Mutation/Volatility)
- `py/pal3.py` -> **100.0%** Exposure
- `py/pal.py` -> **99.9999%** Exposure
- `py/pal2.py` -> **99.74%** Exposure
- `py/docex.py` -> **98.0964%** Exposure
- `py/lis.py` -> **97.5904%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `py/ngrams.py` -> **7** Orphaned Functions | **0** Duplicates
- `py/pal2.py` -> **4** Orphaned Functions | **2** Duplicates
- `py/pal.py` -> **3** Orphaned Functions | **2** Duplicates
- `ipynb/Sudoku.java` -> **4** Orphaned Functions | **0** Duplicates
- `py/Sudoku.java` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`ipynb/Sudoku.java`** -> AI Confidence: **99.34%**
2. **`py/Sudoku.java`** -> AI Confidence: **99.34%**
3. **`py/ngrams.py`** -> AI Confidence: **99.24%**
4. **`py/docex.py`** -> AI Confidence: **99.17%**
5. **`py/lispy.py`** -> AI Confidence: **99.13%**
6. **`py/yaptu.py`** -> AI Confidence: **99.13%**
7. **`py/SET.py`** -> AI Confidence: **99.09%**
8. **`py/ibol.py`** -> AI Confidence: **99.09%**
9. **`py/testaccum.py`** -> AI Confidence: **99.09%**
10. **`ipynb/portman.py`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `ipynb/Sudoku.java` -> **100.0%** Exposure
- `py/Sudoku.java` -> **100.0%** Exposure
- `ipynb/portman.py` -> **100.0%** Exposure
- `py/SET.py` -> **100.0%** Exposure
- `py/beal.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `py/lispy.py` -> **100.0%** Exposure
- `py/yaptu.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `ipynb/Sudoku.java` -> **100.0%** Exposure
- `ipynb/portman.py` -> **100.0%** Exposure
- `py/SET.py` -> **100.0%** Exposure
- `py/beal.py` -> **100.0%** Exposure
- `py/docex.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `89` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `py/lispy.py` (PYTHON) -> Cumulative Risk: **810.43**
- **Archetype:** `file_cluster_8` (Distance: 11.331 IQR)
- **Magnitude:** 779.38 | **LOC:** 317 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `expand` (Impact: 236.4), `eval` (Impact: 149.0), `atom` (Impact: 142.2)

### 2. `py/pal.py` (PYTHON) -> Cumulative Risk: **759.19**
- **Archetype:** `file_cluster_8` (Distance: 12.183 IQR)
- **Magnitude:** 270.56 | **LOC:** 156 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `search` (Impact: 67.6), `__init__` (Impact: 26.8), `reverse` (Impact: 21.1)

### 3. `py/pal2.py` (PYTHON) -> Cumulative Risk: **758.12**
- **Archetype:** `file_cluster_17` (Distance: 12.797 IQR)
- **Magnitude:** 405.98 | **LOC:** 269 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9946%)
- **Heaviest Functions:** `_k_startingwith` (Impact: 61.0), `search` (Impact: 48.3), `reversible_words` (Impact: 36.9)

### 4. `py/yaptu.py` (PYTHON) -> Cumulative Risk: **720.08**
- **Archetype:** `file_cluster_8` (Distance: 10.508 IQR)
- **Magnitude:** 501.94 | **LOC:** 172 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `copyblock` (Impact: 481.1)

### 5. `py/lis.py` (PYTHON) -> Cumulative Risk: **672.19**
- **Archetype:** `file_cluster_8` (Distance: 11.735 IQR)
- **Magnitude:** 157.84 | **LOC:** 133 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9781%), Documentation (99.6651%), State Flux (97.5904%)
- **Heaviest Functions:** `atom` (Impact: 64.8), `read_from_tokens` (Impact: 49.2), `standard_env` (Impact: 6.7)

### 6. `py/docex.py` (PYTHON) -> Cumulative Risk: **663.78**
- **Archetype:** `file_cluster_13` (Distance: 12.235 IQR)
- **Magnitude:** 429.5 | **LOC:** 238 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9967%)
- **Heaviest Functions:** `run_string` (Impact: 158.2), `fail` (Impact: 86.0), `run_docstring` (Impact: 50.5)

### 7. `py/pal3.py` (PYTHON) -> Cumulative Risk: **660.17**
- **Archetype:** `file_cluster_17` (Distance: 14.085 IQR)
- **Magnitude:** 441.0 | **LOC:** 171 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `letters` (Impact: 308.6), `__init__` (Impact: 21.1), `test1` (Impact: 2.4)

### 8. `py/ngrams.py` (PYTHON) -> Cumulative Risk: **624.1**
- **Archetype:** `file_cluster_8` (Distance: 9.832 IQR)
- **Magnitude:** 494.7 | **LOC:** 261 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9998%)
- **Heaviest Functions:** `Pedit` (Impact: 166.5), `hillclimb` (Impact: 45.3), `neighboring_msgs` (Impact: 39.6)

### 9. `py/pytudes.py` (PYTHON) -> Cumulative Risk: **602.42**
- **Archetype:** `file_cluster_8` (Distance: 9.544 IQR)
- **Magnitude:** 149.08 | **LOC:** 280 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (93.4707%)
- **Heaviest Functions:** `ipynbs` (Impact: 124.2), `read_url` (Impact: 6.2)

### 10. `ipynb/portman.py` (PYTHON) -> Cumulative Risk: **598.87**
- **Archetype:** `file_cluster_16` (Distance: 11.377 IQR)
- **Magnitude:** 243.28 | **LOC:** 139 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9956%)
- **Heaviest Functions:** `build_bridges` (Impact: 55.0), `used` (Impact: 35.1), `bridging_steps` (Impact: 22.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `py/lispy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.331 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.543 IQR)
- **Top Global Matches:** file_cluster_8: 11.331, file_cluster_13: 11.55, file_cluster_0: 11.64
- **Magnitude:** 779.38 | **LOC:** 317 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (54.324%), Tech Debt (12.7767%)
**Top Internal Functions/Classes:**
  * `expand` (Impact: 236.4 | O(2^N))
  * `eval` (Impact: 149.0 | O(2^N) | DB: 1)
  * `atom` (Impact: 142.2 | O(N^4) | DB: 18)
  * `read` (Impact: 96.1 | O(2^N) | DB: 1)
  * `expand_quasiquote` (Impact: 31.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 95`, `args: 44`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 11`, `state_mutation: 34`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 25`, `import: 2`
* *Defense:* `safety: 12`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, cmath, sys, operator, math, io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/ibol.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.693 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.546 IQR)
- **Top Global Matches:** file_cluster_8: 10.693, file_cluster_17: 10.753, file_cluster_13: 10.991
- **Magnitude:** 686.48 | **LOC:** 195 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (26.5243%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `showh` (Impact: 514.5 | O(2^N))
  * `closure` (Impact: 49.3 | O(2^N))
  * `margin` (Impact: 21.9 | O(N^4))
  * `histo` (Impact: 13.3 | O(N^2))
  * `cluster` (Impact: 12.3 | O(N^3))
    * *Intent:* """Return a list of clusters, each cluster element is within d of another and within dc of every oth...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 56`, `args: 23`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`
* *Architecture:* `io: 2`, `api: 21`, `import: 3`
* *Defense:* `safety: 9`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, __future__, collections
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ipynb/Sudoku.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.195 IQR)
- **Top Global Matches:** file_cluster_8: 9.195, file_cluster_7: 9.686, file_cluster_1: 9.943
- **Magnitude:** 655.58 | **LOC:** 488 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.1784%), Tech Debt (48.4761%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 346.6 | O(N^5))
  * `printStats` (Impact: 56.6 | O(N^6))
  * `rowString` (Impact: 55.0 | O(N^6))
  * `dual_consistent` (Impact: 54.9 | O(N^5))
  * `verify` (Impact: 44.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 30`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 6`, `doc: 13`, `test: 2`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.lang.Integer.*, java.io.*, java.util.concurrent.CountDownLatch, java.lang.StringBuilder, java.util.stream.*, java.util.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/lettercount.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.667 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.802 IQR)
- **Top Global Matches:** file_cluster_8: 9.667, file_cluster_13: 9.912, file_cluster_7: 9.941
- **Magnitude:** 521.14 | **LOC:** 445 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (8.9121%), Tech Debt (29.9631%)
**Top Internal Functions/Classes:**
  * `write_dict` (Impact: 310.8 | O(2^N) | DB: 7)
  * `lettercount` (Impact: 54.2 | O(N^4))
  * `colname` (Impact: 31.8 | O(N^4) | DB: 3)
  * `columns` (Impact: 31.5 | O(N^3))
  * `substr` (Impact: 18.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 87`, `args: 39`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `api: 37`, `import: 6`
* *Defense:* `safety: 1`, `doc: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` glob, __future__, time, collections, itertools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/yaptu.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.508 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.215 IQR)
- **Top Global Matches:** file_cluster_8: 10.508, file_cluster_13: 10.688, file_cluster_7: 10.946
- **Magnitude:** 501.94 | **LOC:** 172 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (32.0368%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `copyblock` (Impact: 481.1 | O(2^N) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 18`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `io: 5`, `api: 7`, `import: 2`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, __future__, sys, os, os.path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/ngrams.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.832 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.276 IQR)
- **Top Global Matches:** file_cluster_8: 9.832, file_cluster_13: 9.924, file_cluster_7: 10.127
- **Magnitude:** 494.7 | **LOC:** 261 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (18.2475%), Tech Debt (80.9593%)
**Top Internal Functions/Classes:**
  * `Pedit` (Impact: 166.5 | O(2^N))
  * `hillclimb` (Impact: 45.3 | O(2^N))
  * `neighboring_msgs` (Impact: 39.6 | O(N^4))
  * `decode_subst` (Impact: 28.4 | O(N^6))
  * `segment2` (Impact: 26.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 85`, `args: 39`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `orphaned_logic: 7`
* *Architecture:* `api: 35`, `import: 5`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` heapq, glob, re, __future__, operator, math, collections, string...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/pal3.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.085 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.719 IQR)
- **Top Global Matches:** file_cluster_17: 14.085, file_cluster_13: 14.165, file_cluster_8: 14.252
- **Magnitude:** 441.0 | **LOC:** 171 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (48.9351%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `letters` (Impact: 308.6 | O(2^N) | DB: 36)
  * `__init__` (Impact: 21.1 | O(N^3) | DB: 2)
  * `test1` (Impact: 2.4 | O(N^1))
    * *Intent:* ################ Unit Tests def test1(): assert prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hel...
  * `test2` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 57`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 87`
* *Architecture:* `io: 1`, `api: 17`, `import: 2`
* *Defense:* `safety: 20`, `doc: 6`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, collections
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/docex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.235 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.777 IQR)
- **Top Global Matches:** file_cluster_13: 12.235, file_cluster_8: 12.509, file_cluster_17: 12.526
- **Magnitude:** 429.5 | **LOC:** 238 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (32.7879%), Tech Debt (34.3407%)
**Top Internal Functions/Classes:**
  * `run_string` (Impact: 158.2 | O(2^N))
  * `fail` (Impact: 86.0 | O(N^5) | DB: 4)
  * `run_docstring` (Impact: 50.5 | O(N^4))
  * `__init__` (Impact: 43.8 | O(N^4) | DB: 17)
    * *Intent:* '''>>> len('abc') 3 >>> len([]) 0 >>> len(5)) Traceback (most recent call last): ... TypeError: len(...
  * `run_module` (Impact: 32.2 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 24`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 11`, `import: 4`
* *Defense:* `safety: 11`, `doc: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, glob, __future__, sys, types, module
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/pal2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.797 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.152 IQR)
- **Top Global Matches:** file_cluster_17: 12.797, file_cluster_13: 12.865, file_cluster_8: 12.881
- **Magnitude:** 405.98 | **LOC:** 269 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (26.7317%), Tech Debt (88.5488%)
**Top Internal Functions/Classes:**
  * `_k_startingwith` (Impact: 61.0 | O(N^5) | DB: 1)
  * `search` (Impact: 48.3 | O(N^4) | DB: 3)
  * `reversible_words` (Impact: 36.9 | O(N^6) | DB: 1)
  * `consider_candidates` (Impact: 27.0 | O(N^4) | DB: 1)
    * *Intent:* """Push a new state with a set of candidate words onto stack."""
  * `report` (Impact: 26.7 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 75`, `args: 27`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 43`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 23`, `import: 2`
* *Defense:* `safety: 25`, `doc: 14`, `test: 21`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, __future__, time, random, bisect
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/sudoku.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.174 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.122 IQR)
- **Top Global Matches:** file_cluster_8: 10.174, file_cluster_17: 10.506, file_cluster_7: 10.637
- **Magnitude:** 352.84 | **LOC:** 162 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (14.1946%), Tech Debt (25.009%)
**Top Internal Functions/Classes:**
  * `eliminate` (Impact: 121.2 | O(2^N))
    * *Intent:* """Eliminate d from values[s]; propagate when values or places <= 2. Return values, except return Fa...
  * `solve_all` (Impact: 56.9 | O(2^N) | DB: 9)
    * *Intent:* """Attempt to solve a sequence of grids. Report results."""
  * `search` (Impact: 52.5 | O(2^N))
  * `display` (Impact: 36.8 | O(N^5))
    * *Intent:* ################ Display as 2-D grid ################
  * `test` (Impact: 18.8 | O(N^6))
    * *Intent:* ################ Unit Tests ################
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 43`, `args: 13`, `func_start: 13`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 13`, `import: 1`
* *Defense:* `safety: 8`, `doc: 8`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/testaccum.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.658 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.334 IQR)
- **Top Global Matches:** file_cluster_8: 8.658, file_cluster_17: 8.846, file_cluster_13: 9.02
- **Magnitude:** 287.86 | **LOC:** 75 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.0114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expand_accumulations` (Impact: 283.7 | O(2^N))
    * *Intent:* """Replace any accumulation displays in program_text with calls to accumulation. Used to simulate a ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 16`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, accum, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/pal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.183 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.783 IQR)
- **Top Global Matches:** file_cluster_8: 12.183, file_cluster_13: 12.225, file_cluster_7: 12.384
- **Magnitude:** 270.56 | **LOC:** 156 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (41.3247%), Tech Debt (98.7998%)
**Top Internal Functions/Classes:**
  * `search` (Impact: 67.6 | O(N^4) | DB: 15)
  * `__init__` (Impact: 26.8 | O(N^3))
  * `reverse` (Impact: 21.1 | O(2^N))
  * `__init__` (Impact: 13.5 | O(N^2))
  * `k_startingwith` (Impact: 12.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 51`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 17`, `import: 2`
* *Defense:* `safety: 1`, `doc: 12`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, __future__, os, string, random, bisect
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/Sudoku.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.613 IQR)
- **Top Global Matches:** file_cluster_8: 8.613, file_cluster_7: 9.09, file_cluster_1: 9.331
- **Magnitude:** 268.54 | **LOC:** 482 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.2372%), Tech Debt (53.2847%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 126.2 | O(N^1))
  * `printStats` (Impact: 32.6 | O(N^3))
  * `isSolution` (Impact: 28.5 | O(N^3))
  * `dual_consistent` (Impact: 18.9 | O(N^1))
  * `solveFile` (Impact: 18.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 28`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 2`
* *Defense:* `doc: 12`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.lang.Integer.*, java.io.*, java.util.concurrent.CountDownLatch, java.lang.StringBuilder, java.util.stream.*, java.util.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ipynb/portman.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.377 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.121 IQR)
- **Top Global Matches:** file_cluster_16: 11.377, file_cluster_13: 11.768, file_cluster_8: 11.853
- **Magnitude:** 243.28 | **LOC:** 139 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (19.0022%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_bridges` (Impact: 55.0 | O(N^5))
    * *Intent:* # Two-word bridges
  * `used` (Impact: 35.1 | O(2^N) | DB: 2)
  * `bridging_steps` (Impact: 22.0 | O(N^4))
  * `natalie` (Impact: 18.0 | O(N^3) | DB: 1)
  * `try_bridge` (Impact: 16.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 37`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 17`, `import: 2`
* *Defense:* `safety: 3`, `doc: 32`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/SET.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.973 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.361 IQR)
- **Top Global Matches:** file_cluster_8: 10.973, file_cluster_13: 11.011, file_cluster_17: 11.142
- **Magnitude:** 221.08 | **LOC:** 135 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.1196%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tally` (Impact: 159.2 | O(2^N) | DB: 1)
  * `is_set` (Impact: 17.7 | O(N^3))
    * *Intent:* #### Cards, dealing cards, and defining the notion of sets. CARDS = [number + color + shade + symbol...
  * `find_set` (Impact: 14.2 | O(N^3))
  * `Tallies` (Impact: 5.3 | O(N^1))
  * `deal` (Impact: 3.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 34`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 7`, `doc: 4`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` itertools, collections, random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/beal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.046 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.197 IQR)
- **Top Global Matches:** file_cluster_13: 12.046, file_cluster_8: 12.101, file_cluster_17: 12.269
- **Magnitude:** 205.8 | **LOC:** 160 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.1579%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `beal_modp` (Impact: 49.8 | O(N^6))
    * *Intent:* ############################################################################## """See if any A ** x ...
  * `beal` (Impact: 31.0 | O(N^6))
    * *Intent:* """See if any A ** x + B ** y equals some C ** z, with gcd(A, B) == 1. Consider any 1 <= A,B <= max_...
  * `exponents_upto` (Impact: 24.6 | O(N^3) | DB: 1)
  * `make_Apowers_modp` (Impact: 20.2 | O(N^3))
  * `make_Apowers` (Impact: 17.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 60`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 24`, `doc: 10`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, math, collections, itertools, fractions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/py2html.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.548 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.492 IQR)
- **Top Global Matches:** file_cluster_8: 10.548, file_cluster_13: 10.695, file_cluster_7: 10.802
- **Magnitude:** 200.06 | **LOC:** 116 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (9.4877%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `color` (Impact: 173.7 | O(2^N) | DB: 17)
  * `cmp` (Impact: 2.7 | O(N^2))
  * `b` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 35`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `io: 6`, `api: 11`, `import: 2`
* *Defense:* `safety: 2`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, glob, sys, os, time, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/lis.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.735 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.944 IQR)
- **Top Global Matches:** file_cluster_8: 11.735, file_cluster_13: 11.798, file_cluster_17: 11.954
- **Magnitude:** 157.84 | **LOC:** 133 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (73.6276%), Tech Debt (45.9203%)
**Top Internal Functions/Classes:**
  * `atom` (Impact: 64.8 | O(N^3))
  * `read_from_tokens` (Impact: 49.2 | O(2^N) | DB: 3)
  * `standard_env` (Impact: 6.7 | O(N^2) | DB: 2)
    * *Intent:* ################ Global Environment
  * `__init__` (Impact: 3.5 | O(N^2) | DB: 1)
  * `__call__` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 36`, `args: 21`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 16`, `orphaned_logic: 2`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, operator, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/spell.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.822 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.825 IQR)
- **Top Global Matches:** file_cluster_8: 10.822, file_cluster_17: 11.122, file_cluster_13: 11.159
- **Magnitude:** 155.08 | **LOC:** 107 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (13.1875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unit_tests` (Impact: 96.5 | O(2^N) | DB: 6)
    * *Intent:* ################ Test Code def unit_tests(): assert correction('speling') == 'spelling' # insert ass...
  * `edits1` (Impact: 19.5 | O(N^1))
  * `candidates` (Impact: 8.8 | O(N^1))
  * `correction` (Impact: 7.1 | O(2^N))
  * `known` (Impact: 5.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 43`, `args: 10`, `func_start: 10`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 9`, `import: 3`
* *Defense:* `safety: 17`, `doc: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, collections, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/pytudes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.544 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.199 IQR)
- **Top Global Matches:** file_cluster_8: 9.544, file_cluster_16: 9.906, file_cluster_7: 9.915
- **Magnitude:** 149.08 | **LOC:** 280 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (11.2294%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ipynbs` (Impact: 124.2 | O(2^N) | DB: 4)
  * `read_url` (Impact: 6.2 | O(N^2))
    * *Intent:* """Reads a file from the specified URL and returns its content as a string."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 36`, `args: 13`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 12`, `import: 2`
* *Defense:* `safety: 1`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` urllib.request, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/parse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.674 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.312 IQR)
- **Top Global Matches:** file_cluster_8: 6.674, file_cluster_7: 7.756, file_cluster_13: 7.931
- **Magnitude:** 138.74 | **LOC:** 54 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.4523%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 110.0 | O(2^N))
  * `match` (Impact: 13.2 | O(N^2))
  * `mklist` (Impact: 5.3 | O(N^1))
  * `category` (Impact: 5.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/latlong.htm` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.679 IQR)
- **Top Global Matches:** file_cluster_8: 4.679, file_cluster_7: 6.416, file_cluster_1: 6.479
- **Magnitude:** 40.4 | **LOC:** 1381 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 40`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ipynb/bikerides.tsv` (CSV | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.454 IQR)
- **Top Global Matches:** file_cluster_8: 4.454, file_cluster_7: 6.254, file_cluster_1: 6.319
- **Magnitude:** 26.36 | **LOC:** 587 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ipynb/bikeplaceshort.csv` (CSV | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 18.3 | **LOC:** 184 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ipynb/bikeplaces.csv` (CSV | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 17.72 | **LOC:** 157 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `py/beal.py` (PYTHON) | Magnitude: 205.8 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 60, branch: 35, safety: 24
- `py/docex.py` (PYTHON) | Magnitude: 429.5 | Delta: **0.274 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 130, branch: 54, structural_boundaries: 24, state_mutation: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ipynb/portman.py` (PYTHON) | Magnitude: 243.28 | Delta: **0.391 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, branch: 39, structural_boundaries: 37, doc: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `py/pal2.py` (PYTHON) | Magnitude: 405.98 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 189, structural_boundaries: 75, branch: 61, state_mutation: 43
- `py/pal3.py` (PYTHON) | Magnitude: 441.0 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 87, structural_boundaries: 57, branch: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `py/SET.py` (PYTHON) | Magnitude: 221.08 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 34, branch: 31, args: 11
- `py/pal.py` (PYTHON) | Magnitude: 270.56 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 51, state_mutation: 51, branch: 41
- `py/ibol.py` (PYTHON) | Magnitude: 686.48 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 129, branch: 69, structural_boundaries: 56, debug_prints: 26
- `py/lis.py` (PYTHON) | Magnitude: 157.84 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 36, branch: 24, args: 21
- `py/ngrams.py` (PYTHON) | Magnitude: 494.7 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 142, structural_boundaries: 85, branch: 64, args: 39

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `py/Sudoku.java` -> **Visali Alagappan** (100.0% isolated ownership) | Magnitude: 268.54
- `py/pytudes.py` -> **Peter Norvig** (100.0% isolated ownership) | Magnitude: 149.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/ngrams.py` -> **Severity: 2438.995** (Blast Radius: 24.39 * Doc Risk: 99.9998%)
- `py/parse.py` -> **Severity: 2438.924** (Blast Radius: 24.39 * Doc Risk: 99.9969%)
- `py/docex.py` -> **Severity: 2438.92** (Blast Radius: 24.39 * Doc Risk: 99.9967%)
- `ipynb/portman.py` -> **Severity: 2438.893** (Blast Radius: 24.39 * Doc Risk: 99.9956%)
- `py/pal2.py` -> **Severity: 2438.868** (Blast Radius: 24.39 * Doc Risk: 99.9946%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
