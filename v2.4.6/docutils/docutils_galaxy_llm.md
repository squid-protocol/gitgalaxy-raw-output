# ARCHITECTURAL_BRIEF: docutils
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/docutils` |
| **Timestamp** | `2026-08-03T21:20:28.280055+00:00` |
| **Scan Duration** | `1.1s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 145 malicious artifacts.

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
| Total Artifacts | 263 |
| Analyzed Artifacts (Scanned) | 205 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 58 |
| Total LOC | 33314 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6071 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2979 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5978 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 143 | 30366 | 69.8% |
| PLAINTEXT | 36 | 0 | 17.6% |
| CSS | 24 | 2418 | 11.7% |
| JAVASCRIPT | 1 | 513 | 0.5% |
| MAKEFILE | 1 | 17 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.871`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 110 | 53.7% |
| file_cluster_13 | 49 | 23.9% |
| file_cluster_16 | 9 | 4.4% |
| file_cluster_11 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 36 | 17.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 58*

**Composition by Extension & Reason:**
- `.el`: 24x Excluded (Unsupported Extension: '.el')
- `.rst`: 15x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 4x Unsupported Format (.undeterminable)
- `.tex`: 4x Excluded (Unsupported Extension: '.tex')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 365 LOC), 1x Excluded (Machine-Generated Source Code Signature: 192 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.sty`: 1x Excluded (Unsupported Extension: '.sty')
- `.odt`: 1x Excluded (Explicitly Denied Extension: '.odt')
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 26 LOC)
- `.css`: 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 93.0 | 9.5 | 5.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 19.9 | 4.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.1 | 2.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 15.6 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.4 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 94.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 41.6 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 27.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 1.2 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `docutils-0.22.4/docutils/utils/_roman_numerals.py` (Hits: 26)
- `docutils-0.22.4/docutils/writers/s5_html/__init__.py` (Hits: 22)
- `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.py** (`docutils-0.22.4/docutils/core.py`) — 13 inbound connections
2. **nodes.py** (`docutils-0.22.4/docutils/nodes.py`) — 9 inbound connections
3. **io.py** (`docutils-0.22.4/docutils/io.py`) — 6 inbound connections
4. **_typing.py** (`docutils-0.22.4/docutils/utils/_typing.py`) — 5 inbound connections
5. **math.css** (`docutils-0.22.4/docutils/writers/html5_polyglot/math.css`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`docutils-0.22.4/docutils/writers/odf_odt/__init__.py`) — 27 outbound dependencies
2. **nodes.py** (`docutils-0.22.4/docutils/nodes.py`) — 18 outbound dependencies
3. **buildhtml.py** (`docutils-0.22.4/tools/buildhtml.py`) — 17 outbound dependencies
4. **__init__.py** (`docutils-0.22.4/docutils/utils/__init__.py`) — 16 outbound dependencies
5. **_html_base.py** (`docutils-0.22.4/docutils/writers/_html_base.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `docutils-0.22.4/docutils/writers/odf_odt/__init__.py`) -> Impact: **3454.2** | LOC: 1915
- `checkskip` (@ `docutils-0.22.4/docutils/utils/math/math2html.py`) -> Impact: **2710.7** | LOC: 1351
- `process` (@ `docutils-0.22.4/docutils/frontend.py`) -> Impact: **1785.0** | LOC: 511
- `get_state` (@ `docutils-0.22.4/docutils/statemachine.py`) -> Impact: **1602.8** | LOC: 775
  * *Intent:* """Offset of `self.input_lines` from the beginning of the file."""
- `substitution_def` (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **1461.9** | LOC: 382
- `parsebit` (@ `docutils-0.22.4/docutils/utils/math/math2html.py`) -> Impact: **1358.8** | LOC: 503
- `endtag` (@ `docutils-0.22.4/docutils/nodes.py`) -> Impact: **1107.7** | LOC: 1179
- `no_match` (@ `docutils-0.22.4/docutils/parsers/rst/states.py`) -> Impact: **1055.0** | LOC: 661
- `run` (@ `docutils-0.22.4/docutils/parsers/rst/directives/tables.py`) -> Impact: **916.4** | LOC: 383
- `apply` (@ `docutils-0.22.4/docutils/transforms/references.py`) -> Impact: **873.1** | LOC: 245

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__new__` (@ `docutils-0.22.4/docutils/__init__.py`) -> **O(2^N) [Recursive]**
- `process` (@ `docutils-0.22.4/docutils/frontend.py`) -> **O(2^N) [Recursive]**
- `validate_encoding_error_handler` (@ `docutils-0.22.4/docutils/frontend.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `docutils-0.22.4/docutils/io.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """The source of input data."""
- `write` (@ `docutils-0.22.4/docutils/io.py`) -> **O(2^N) [Recursive]**
- `encode` (@ `docutils-0.22.4/docutils/io.py`) -> **O(2^N) [Recursive]**
- `open` (@ `docutils-0.22.4/docutils/io.py`) -> **O(2^N) [Recursive]**
- `walk` (@ `docutils-0.22.4/docutils/nodes.py`) -> **O(2^N) [Recursive]**
- `pformat` (@ `docutils-0.22.4/docutils/nodes.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Body Elements # ============= # General # ------- # # Miscellaneous Body Elements and related Body Subelements (Part) class paragraph(General, TextE...
- `shortrepr` (@ `docutils-0.22.4/docutils/nodes.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `docutils-0.22.4/docutils/writers/odf_odt/__init__.py`) -> DB Complexity: **167**
- `checkskip` (@ `docutils-0.22.4/docutils/utils/math/math2html.py`) -> DB Complexity: **97**
- `find_theme` (@ `docutils-0.22.4/docutils/writers/s5_html/__init__.py`) -> DB Complexity: **93**
- `get_state` (@ `docutils-0.22.4/docutils/statemachine.py`) -> DB Complexity: **68**
  * *Intent:* """Offset of `self.input_lines` from the beginning of the file."""
- `visit_option_argument` (@ `docutils-0.22.4/docutils/writers/manpage.py`) -> DB Complexity: **51**
- `endtag` (@ `docutils-0.22.4/docutils/nodes.py`) -> DB Complexity: **42**
- `parsebit` (@ `docutils-0.22.4/docutils/utils/math/math2html.py`) -> DB Complexity: **41**
- `visit_citation` (@ `docutils-0.22.4/docutils/writers/manpage.py`) -> DB Complexity: **40**
- `process` (@ `docutils-0.22.4/docutils/frontend.py`) -> DB Complexity: **38**
- `extract_options` (@ `docutils-0.22.4/docutils/utils/__init__.py`) -> DB Complexity: **38**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `docutils-0.22.4/docutils` | 8 | 10864.92 | 17.42% | 28.34% |
| `docutils-0.22.4/docutils/parsers/rst` | 4 | 7075.56 | 18.94% | 21.16% |
| `docutils-0.22.4/docutils/utils/math` | 8 | 7040.98 | 15.62% | 26.28% |
| `docutils-0.22.4/docutils/writers/odf_odt` | 3 | 5429.82 | 16.09% | 36.54% |
| `docutils-0.22.4/docutils/parsers/rst/directives` | 9 | 4416.4 | 11.21% | 34.99% |
| `docutils-0.22.4/docutils/transforms` | 8 | 3874.92 | 22.01% | 79.2% |
| `docutils-0.22.4/docutils/writers/html5_polyglot` | 8 | 3183.25 | 10.65% | 20.43% |
| `docutils-0.22.4/docutils/utils` | 7 | 2160.65 | 17.04% | 28.18% |
| `docutils-0.22.4/docutils/writers` | 5 | 1733.44 | 15.45% | 81.65% |
| `docutils-0.22.4/docutils/writers/html4css1` | 3 | 1578.19 | 26.28% | 32.93% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docutils-0.22.4/docutils/parsers/rst/languages/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/transforms/components.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/null.py` -> **99.9999%** Exposure
- `docutils-0.22.4/docutils/writers/null.py` -> **99.9999%** Exposure
- `docutils-0.22.4/docutils/io.py` -> **99.9987%** Exposure
### Highest State Flux (Mutation/Volatility)
- `docutils-0.22.4/docutils/utils/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/code_analyzer.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/math/latex2mathml.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/math/math2html.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/utils/math/mathml_elements.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `docutils-0.22.4/docutils/utils/math/math2html.py` -> **8** Orphaned Functions | **41** Duplicates
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` -> **25** Orphaned Functions | **2** Duplicates
- `docutils-0.22.4/docutils/writers/manpage.py` -> **23** Orphaned Functions | **0** Duplicates
- `docutils-0.22.4/docutils/io.py` -> **0** Orphaned Functions | **13** Duplicates
- `docutils-0.22.4/docutils/parsers/rst/states.py` -> **1** Orphaned Functions | **12** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`docutils-0.22.4/docutils/core.py`** -> AI Confidence: **99.31%**
2. **`docutils-0.22.4/docutils/frontend.py`** -> AI Confidence: **99.31%**
3. **`docutils-0.22.4/docutils/io.py`** -> AI Confidence: **99.31%**
4. **`docutils-0.22.4/docutils/parsers/recommonmark_wrapper.py`** -> AI Confidence: **99.31%**
5. **`docutils-0.22.4/docutils/parsers/rst/directives/images.py`** -> AI Confidence: **99.31%**
6. **`docutils-0.22.4/docutils/parsers/rst/directives/misc.py`** -> AI Confidence: **99.31%**
7. **`docutils-0.22.4/docutils/parsers/rst/directives/tables.py`** -> AI Confidence: **99.31%**
8. **`docutils-0.22.4/docutils/parsers/rst/states.py`** -> AI Confidence: **99.31%**
9. **`docutils-0.22.4/docutils/utils/smartquotes.py`** -> AI Confidence: **99.31%**
10. **`docutils-0.22.4/docutils/writers/latex2e/__init__.py`** -> AI Confidence: **99.31%**
11. **`docutils-0.22.4/docutils/writers/odf_odt/prepstyles.py`** -> AI Confidence: **99.31%**
12. **`docutils-0.22.4/docutils/writers/s5_html/__init__.py`** -> AI Confidence: **99.31%**
13. **`docutils-0.22.4/docutils/utils/__init__.py`** -> AI Confidence: **99.24%**
14. **`docutils-0.22.4/docutils/writers/odf_odt/__init__.py`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `docutils-0.22.4/docutils/utils/math/mathalphabet2unichar.py` -> **0.0008%** Exposure
- `docutils-0.22.4/docutils/utils/math/tex2unichar.py` -> **0.0003%** Exposure
- `docutils-0.22.4/docutils/utils/punctuation_chars.py` -> **0.0003%** Exposure
### Exploit Generation Surface
- `docutils-0.22.4/docutils/__init__.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/core.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/examples.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/frontend.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/io.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `docutils-0.22.4/docutils/nodes.py` -> **1.1522%** Exposure
### Algorithmic DoS Exposure
- `docutils-0.22.4/docutils/core.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/frontend.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/io.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/nodes.py` -> **100.0%** Exposure
- `docutils-0.22.4/docutils/parsers/recommonmark_wrapper.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `456` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON) -> Cumulative Risk: **879.59**
- **Archetype:** `file_cluster_11` (Distance: 13.693 IQR)
- **Magnitude:** 1576.2 | **LOC:** 965 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `visit_entry` (Impact: 296.0), `visit_footnote_reference` (Impact: 223.0), `should_be_compact_paragraph` (Impact: 98.4)

### 2. `docutils-0.22.4/docutils/writers/manpage.py` (PYTHON) -> Cumulative Risk: **865.48**
- **Archetype:** `file_cluster_16` (Distance: 13.221 IQR)
- **Magnitude:** 1520.64 | **LOC:** 1354 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `comment_begin` (Impact: 507.4), `visit_option_argument` (Impact: 176.0), `visit_citation` (Impact: 112.4)

### 3. `docutils-0.22.4/docutils/transforms/__init__.py` (PYTHON) -> Cumulative Risk: **831.71**
- **Archetype:** `file_cluster_16` (Distance: 12.71 IQR)
- **Magnitude:** 120.4 | **LOC:** 197 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9987%)
- **Heaviest Functions:** `get_priority_string` (Impact: 25.6), `apply_transforms` (Impact: 13.8), `add_transform` (Impact: 9.4)

### 4. `docutils-0.22.4/docutils/io.py` (PYTHON) -> Cumulative Risk: **819.13**
- **Archetype:** `file_cluster_13` (Distance: 13.235 IQR)
- **Magnitude:** 879.0 | **LOC:** 717 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9987%)
- **Heaviest Functions:** `__repr__` (Impact: 346.2), `write` (Impact: 147.2), `write` (Impact: 62.0)

### 5. `docutils-0.22.4/docutils/utils/math/math2html.py` (PYTHON) -> Cumulative Risk: **800.23**
- **Archetype:** `file_cluster_8` (Distance: 11.595 IQR)
- **Magnitude:** 5820.78 | **LOC:** 3167 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `checkskip` (Impact: 2710.7), `parsebit` (Impact: 1358.8), `readoption` (Impact: 53.9)

### 6. `docutils-0.22.4/docutils/transforms/parts.py` (PYTHON) -> Cumulative Risk: **796.53**
- **Archetype:** `file_cluster_13` (Distance: 12.326 IQR)
- **Magnitude:** 404.04 | **LOC:** 176 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9994%)
- **Heaviest Functions:** `build_contents` (Impact: 169.6), `update_section_numbers` (Impact: 85.0), `apply` (Impact: 53.2)

### 7. `docutils-0.22.4/docutils/utils/__init__.py` (PYTHON) -> Cumulative Risk: **784.2**
- **Archetype:** `file_cluster_13` (Distance: 12.642 IQR)
- **Magnitude:** 1203.04 | **LOC:** 851 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `extract_options` (Impact: 716.1), `system_message` (Impact: 293.9), `__init__` (Impact: 21.4)

### 8. `docutils-0.22.4/docutils/utils/math/mathml_elements.py` (PYTHON) -> Cumulative Risk: **769.83**
- **Archetype:** `file_cluster_13` (Distance: 13.288 IQR)
- **Magnitude:** 525.32 | **LOC:** 483 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__setitem__` (Impact: 98.6), `append` (Impact: 44.0), `__init__` (Impact: 42.3)

### 9. `docutils-0.22.4/docutils/readers/__init__.py` (PYTHON) -> Cumulative Risk: **765.94**
- **Archetype:** `file_cluster_13` (Distance: 12.205 IQR)
- **Magnitude:** 116.94 | **LOC:** 136 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9994%)
- **Heaviest Functions:** `__init__` (Impact: 29.3), `read` (Impact: 18.3), `get_reader_class` (Impact: 12.6)

### 10. `docutils-0.22.4/docutils/parsers/rst/tableparser.py` (PYTHON) -> Cumulative Risk: **752.13**
- **Archetype:** `file_cluster_8` (Distance: 11.577 IQR)
- **Magnitude:** 738.94 | **LOC:** 544 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.8085%)
- **Heaviest Functions:** `init_row` (Impact: 227.3), `structure_from_cells` (Impact: 132.9), `find_head_body_sep` (Impact: 100.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `docutils-0.22.4/docutils/utils/math/math2html.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.595 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.624 IQR)
- **Top Global Matches:** file_cluster_8: 11.595, file_cluster_16: 11.768, file_cluster_11: 11.98
- **Magnitude:** 5820.78 | **LOC:** 3167 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 97
- **Risk Profile:** Cognitive Load (47.3889%), Tech Debt (98.7933%)
**Top Internal Functions/Classes:**
  * `checkskip` (Impact: 2710.7 | O(2^N) | DB: 97)
  * `parsebit` (Impact: 1358.8 | O(2^N) | DB: 41)
  * `readoption` (Impact: 53.9 | O(N^3) | DB: 1)
  * `gethtml` (Impact: 35.2 | O(2^N))
  * `finished` (Impact: 35.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `structural_boundaries: 975`, `args: 297`, `func_start: 293`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 384`, `planned_debt: 9`, `duplicate_logic: 41`, `orphaned_logic: 8`
* *Architecture:* `io: 11`, `api: 337`, `import: 5`
* *Defense:* `safety: 20`, `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pathlib, unicodedata, sys, __future__, docutils.utils.math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/states.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.805 IQR)
- **Top Global Matches:** file_cluster_8: 11.923, file_cluster_7: 12.137, file_cluster_13: 12.178
- **Magnitude:** 5507.46 | **LOC:** 3267 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (19.9324%), Tech Debt (41.4323%)
**Top Internal Functions/Classes:**
  * `substitution_def` (Impact: 1461.9 | O(2^N) | DB: 6)
  * `no_match` (Impact: 1055.0 | O(N^6) | DB: 25)
  * `footnote` (Impact: 588.4 | O(2^N) | DB: 4)
  * `footnote_reference` (Impact: 578.0 | O(2^N))
  * `implicit_inline` (Impact: 140.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 665`, `structural_boundaries: 430`, `args: 141`, `func_start: 141`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 200`, `dead_code: 4`, `planned_debt: 4`, `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 162`, `import: 18`
* *Defense:* `safety: 75`, `doc: 252`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` docutils, re, types, docutils.nodes, __future__, docutils.utils, warnings, docutils.parsers.rst...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.917 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.709 IQR)
- **Top Global Matches:** file_cluster_8: 11.917, file_cluster_16: 11.991, file_cluster_13: 12.138
- **Magnitude:** 5107.8 | **LOC:** 3462 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 167
- **Risk Profile:** Cognitive Load (28.322%), Tech Debt (12.6206%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 3454.2 | O(2^N) | DB: 167)
  * `visit_title` (Impact: 128.6 | O(2^N) | DB: 2)
    * *Intent:* # # I don't know how to implement targets in ODF. # How do we create a target in oowriter? A cross-r...
  * `visit_reference` (Impact: 74.1 | O(N^6) | DB: 1)
  * `get_table_style` (Impact: 56.4 | O(N^6))
  * `visit_raw` (Impact: 49.5 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 491`, `args: 276`, `func_start: 276`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 345`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 3`
* *Architecture:* `io: 21`, `api: 329`, `import: 26`
* *Defense:* `safety: 36`, `doc: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` configparser, time, __future__, zipfile, pygments.lexers, warnings, tempfile, urllib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/html5_polyglot/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.212 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.555 IQR)
- **Top Global Matches:** file_cluster_16: 12.212, file_cluster_8: 12.326, file_cluster_13: 12.385
- **Magnitude:** 3175.15 | **LOC:** 399 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (56.9858%), Tech Debt (10.6381%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 63`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 101`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 37`, `import: 4`
* *Defense:* `safety: 11`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathlib, __future__, docutils.writers, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/nodes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.885 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.8 IQR)
- **Top Global Matches:** file_cluster_16: 12.885, file_cluster_13: 13.116, file_cluster_11: 13.212
- **Magnitude:** 2958.2 | **LOC:** 3342 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (16.4685%), Tech Debt (69.0378%)
**Top Internal Functions/Classes:**
  * `endtag` (Impact: 1107.7 | O(N^6) | DB: 42)
  * `walk` (Impact: 481.5 | O(2^N))
  * `pformat` (Impact: 159.4 | O(2^N) | DB: 5)
    * *Intent:* # Body Elements # ============= # General # ------- # # Miscellaneous Body Elements and related Body...
  * `unknown_departure` (Impact: 148.1 | O(N^4) | DB: 8)
    * *Intent:* """Describtion of a command-line option."""
  * `shortrepr` (Impact: 86.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 543`, `args: 170`, `func_start: 170`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 131`, `dead_code: 5`, `planned_debt: 9`, `duplicate_logic: 12`
* *Architecture:* `io: 5`, `api: 282`, `import: 18`
* *Defense:* `safety: 108`, `doc: 428`, `test: 6`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 86.685
  * `Choke Point (Betweenness):` 0.001509 | `Ripple Effect (Closeness):` 0.079812
  * `Imports (Out-Degree: 2):` in, dependency, docutils.utils._typing, xml.dom, unicodedata, sys, collections.abc, re...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/frontend.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.728 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.528 IQR)
- **Top Global Matches:** file_cluster_16: 11.728, file_cluster_8: 11.806, file_cluster_13: 11.817
- **Magnitude:** 2926.28 | **LOC:** 1179 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (21.7102%), Tech Debt (22.1598%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 1785.0 | O(2^N) | DB: 38)
  * `validate_encoding_error_handler` (Impact: 319.6 | O(2^N))
  * `validate_threshold` (Impact: 248.5 | O(N^6) | DB: 4)
  * `make_paths_absolute` (Impact: 86.7 | O(N^6) | DB: 6)
  * `validate_encoding` (Impact: 64.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 148`, `args: 40`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 57`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 16`, `api: 46`, `import: 16`
* *Defense:* `safety: 47`, `doc: 80`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.842
  * `Choke Point (Betweenness):` 0.000676 | `Ripple Effect (Closeness):` 0.065134
  * `Imports (Out-Degree: 1):` pathlib, sys, configparser, os.path, docutils.io, collections.abc, docutils, codecs...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/statemachine.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.988 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.628 IQR)
- **Top Global Matches:** file_cluster_16: 13.988, file_cluster_13: 13.989, file_cluster_8: 14.014
- **Magnitude:** 2660.52 | **LOC:** 1535 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (43.1015%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_state` (Impact: 1602.8 | O(2^N) | DB: 68)
    * *Intent:* """Offset of `self.input_lines` from the beginning of the file."""
  * `run` (Impact: 355.6 | O(2^N) | DB: 24)
  * `get_indented` (Impact: 196.5 | O(N^6))
  * `get_2D_block` (Impact: 53.9 | O(N^4))
    * *Intent:* """ (indented, line_offset, blank_finish ) = self.state_machine.get_known_indented(match.end()) sm =...
  * `get_text_block` (Impact: 35.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 217`, `args: 92`, `func_start: 92`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 206`
* *Architecture:* `io: 10`, `api: 89`, `import: 5`
* *Defense:* `safety: 60`, `doc: 196`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009804
  * `Imports (Out-Degree: 0):` unicodedata, sys, statemachine, docutils, re, __future__
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/transforms/references.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.603 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.078 IQR)
- **Top Global Matches:** file_cluster_8: 11.603, file_cluster_16: 11.856, file_cluster_13: 11.907
- **Magnitude:** 1698.96 | **LOC:** 991 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (14.5498%), Tech Debt (67.5645%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 873.1 | O(2^N) | DB: 2)
  * `symbolize_footnotes` (Impact: 527.9 | O(N^6) | DB: 13)
  * `apply` (Impact: 85.8 | O(N^5) | DB: 5)
  * `number_footnote_references` (Impact: 62.4 | O(N^6))
  * `number_footnotes` (Impact: 42.8 | O(N^5) | DB: 3)
    * *Intent:* """ Given:: <paragraph> <reference refname="direct-external"> direct external <target ids="id1" name...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 102`, `args: 26`, `func_start: 26`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 56`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 57`, `doc: 38`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docutils.transforms, __future__, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.693 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.706 IQR)
- **Top Global Matches:** file_cluster_11: 13.693, file_cluster_16: 13.716, file_cluster_13: 13.772
- **Magnitude:** 1576.2 | **LOC:** 965 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (78.8475%), Tech Debt (98.7845%)
**Top Internal Functions/Classes:**
  * `visit_entry` (Impact: 296.0 | O(2^N) | DB: 30)
    * *Intent:* # use table for docinfo def visit_docinfo(self, node) -> None: self.context.append(len(self.body)) s...
  * `visit_footnote_reference` (Impact: 223.0 | O(N^6) | DB: 14)
  * `should_be_compact_paragraph` (Impact: 98.4 | O(N^6))
    * *Intent:* # add newline after wrapper tags, don't use <code> for code def visit_literal_block(self, node) -> N...
  * `visit_label` (Impact: 88.5 | O(N^6) | DB: 22)
  * `visit_table` (Impact: 70.0 | O(N^6) | DB: 15)
    * *Intent:* # <sup> not allowed in <pre> in HTML 4 def visit_superscript(self, node) -> None: if isinstance(node...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 157`, `args: 95`, `func_start: 95`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 386`, `dead_code: 3`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 25`
* *Architecture:* `io: 14`, `api: 97`, `import: 6`
* *Defense:* `safety: 36`, `doc: 12`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` docutils.writers, os.path, docutils, docutils.writers._html_base, re, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/manpage.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.221 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.705 IQR)
- **Top Global Matches:** file_cluster_16: 13.221, file_cluster_11: 13.454, file_cluster_13: 13.541
- **Magnitude:** 1520.64 | **LOC:** 1354 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (53.7986%), Tech Debt (96.1648%)
**Top Internal Functions/Classes:**
  * `comment_begin` (Impact: 507.4 | O(2^N) | DB: 20)
  * `visit_option_argument` (Impact: 176.0 | O(N^4) | DB: 51)
  * `visit_citation` (Impact: 112.4 | O(N^6) | DB: 40)
  * `visit_option` (Impact: 22.2 | O(N^4) | DB: 4)
  * `visit_docinfo_item` (Impact: 12.3 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 295`, `args: 203`, `func_start: 203`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 388`, `dead_code: 6`, `planned_debt: 6`, `fragile_debt: 4`, `orphaned_logic: 23`
* *Architecture:* `api: 196`, `import: 5`
* *Defense:* `safety: 14`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` re, docutils.utils._roman_numerals, __future__, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/directives/misc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.793 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.352 IQR)
- **Top Global Matches:** file_cluster_8: 10.793, file_cluster_13: 10.908, file_cluster_7: 11.154
- **Magnitude:** 1476.42 | **LOC:** 691 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (9.2175%), Tech Debt (84.4437%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 728.2 | O(2^N) | DB: 8)
    * *Intent:* # ignored except for 'literal' or 'code': 'number-lines': directives.value_or((None,), int), 'class'...
  * `run` (Impact: 432.7 | O(2^N) | DB: 3)
  * `run` (Impact: 173.0 | O(2^N) | DB: 1)
  * `run` (Impact: 45.8 | O(2^N))
  * `run` (Impact: 19.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 104`, `args: 19`, `func_start: 19`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 31`, `import: 12`
* *Defense:* `safety: 32`, `doc: 30`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.677
  * `Choke Point (Betweenness):` 0.000978 | `Ripple Effect (Closeness):` 0.015609
  * `Imports (Out-Degree: 2):` pathlib, docutils, re, urllib.request, time, docutils.parsers.rst.directives.body, __future__, docutils.transforms...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/utils/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.642 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.073 IQR)
- **Top Global Matches:** file_cluster_13: 12.642, file_cluster_16: 12.735, file_cluster_11: 12.971
- **Magnitude:** 1203.04 | **LOC:** 851 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (33.4491%), Tech Debt (45.6506%)
**Top Internal Functions/Classes:**
  * `extract_options` (Impact: 716.1 | O(N^6) | DB: 38)
  * `system_message` (Impact: 293.9 | O(2^N) | DB: 1)
  * `__init__` (Impact: 21.4 | O(N^3) | DB: 5)
  * `__init__` (Impact: 11.4 | O(2^N) | DB: 1)
  * `extract_extension_options` (Impact: 8.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 127`, `args: 39`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 59`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 10`, `api: 51`, `import: 18`
* *Defense:* `safety: 23`, `doc: 92`, `test: 2`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` docutils.utils._typing, pathlib, unicodedata, sys, os.path, itertools, collections.abc, docutils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/directives/tables.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.858 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.521 IQR)
- **Top Global Matches:** file_cluster_8: 10.858, file_cluster_13: 10.948, file_cluster_17: 11.228
- **Magnitude:** 1127.9 | **LOC:** 524 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (18.7%), Tech Debt (19.1363%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 916.4 | O(2^N) | DB: 17)
  * `check_table_dimensions` (Impact: 90.2 | O(N^5))
  * `extend_short_rows_with_empty_cells` (Impact: 24.2 | O(N^5) | DB: 1)
  * `make_title` (Impact: 18.8 | O(N^6))
  * `align` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 78`, `args: 18`, `func_start: 18`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 46`, `planned_debt: 8`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 16`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` docutils.parsers.rst.directives.misc, docutils.io, docutils, urllib.request, __future__, docutils.utils, warnings, docutils.parsers.rst...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.145 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.743 IQR)
- **Top Global Matches:** file_cluster_8: 11.145, file_cluster_13: 11.229, file_cluster_16: 11.24
- **Magnitude:** 964.06 | **LOC:** 856 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (9.0435%), Tech Debt (9.1888%)
**Top Internal Functions/Classes:**
  * `debugging_dumps` (Impact: 154.6 | O(N^6) | DB: 9)
  * `report_SystemMessage` (Impact: 114.7 | O(N^6) | DB: 3)
  * `publish` (Impact: 106.9 | O(N^6) | DB: 7)
  * `publish_programmatically` (Impact: 105.1 | O(N^6))
    * *Intent:* """ Set up & run a `Publisher` for programmatic use. Return a document tree. Parameters: see `publis...
  * `set_destination` (Impact: 79.8 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 77`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 35`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 39`, `import: 11`
* *Defense:* `safety: 18`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.934
  * `Choke Point (Betweenness):` 0.001183 | `Ripple Effect (Closeness):` 0.063725
  * `Imports (Out-Degree: 2):` locale, sys, docutils, docutils.readers, docutils.nodes, os, __future__, docutils.frontend...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/io.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.235 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.971 IQR)
- **Top Global Matches:** file_cluster_13: 13.235, file_cluster_16: 13.396, file_cluster_11: 13.457
- **Magnitude:** 879.0 | **LOC:** 717 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (32.7976%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 346.2 | O(2^N) | DB: 7)
    * *Intent:* """The source of input data."""
  * `write` (Impact: 147.2 | O(2^N) | DB: 9)
  * `write` (Impact: 62.0 | O(2^N) | DB: 6)
  * `encode` (Impact: 61.2 | O(2^N))
  * `open` (Impact: 49.1 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 98`, `args: 30`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 70`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 13`
* *Architecture:* `io: 18`, `api: 35`, `import: 11`
* *Defense:* `safety: 46`, `doc: 100`, `test: 2`, `immutability_locks: 9`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.548
  * `Choke Point (Betweenness):` 0.000241 | `Ripple Effect (Closeness):` 0.05296
  * `Imports (Out-Degree: 1):` locale, sys, docutils, re, docutils.nodes, os, __future__, warnings...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/transforms/peps.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.862 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.189 IQR)
- **Top Global Matches:** file_cluster_13: 11.862, file_cluster_8: 12.06, file_cluster_16: 12.143
- **Magnitude:** 809.18 | **LOC:** 316 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (23.12%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 739.8 | O(2^N) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 40`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 47`
* *Architecture:* `io: 1`, `api: 18`, `import: 8`
* *Defense:* `safety: 13`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docutils, re, docutils.transforms, time, os, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/directives/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.354 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.828 IQR)
- **Top Global Matches:** file_cluster_13: 12.354, file_cluster_16: 12.395, file_cluster_8: 12.511
- **Magnitude:** 772.62 | **LOC:** 481 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (14.0991%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `directive` (Impact: 513.2 | O(2^N) | DB: 8)
  * `single_char_or_unicode` (Impact: 99.5 | O(2^N))
  * `encoding` (Impact: 71.4 | O(2^N))
  * `positive_int_list` (Impact: 12.4 | O(N^2))
  * `value_or` (Impact: 10.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 83`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `safety: 26`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections.abc, docutils, re, docutils.parsers.rst.languages, __future__, docutils.utils, importlib, docutils.parsers.rst...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/parsers/rst/roles.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.815 IQR)
- **Top Global Matches:** file_cluster_13: 11.707, file_cluster_8: 11.754, file_cluster_16: 11.976
- **Magnitude:** 770.26 | **LOC:** 451 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (16.7661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `role` (Impact: 655.7 | O(2^N) | DB: 16)
  * `set_classes` (Impact: 35.1 | O(2^N))
  * `normalized_role_options` (Impact: 17.6 | O(2^N))
  * `normalize_options` (Impact: 8.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 72`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 32`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 18`, `doc: 28`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.656
  * `Choke Point (Betweenness):` 0.00058 | `Ripple Effect (Closeness):` 0.024714
  * `Imports (Out-Degree: 1):` docutils, docutils.parsers.rst.languages, __future__, docutils.utils.code_analyzer, warnings, docutils.parsers.rst
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/tableparser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.577 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.577, file_cluster_13: 11.636, file_cluster_7: 11.786
- **Magnitude:** 738.94 | **LOC:** 544 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (18.7966%), Tech Debt (43.1932%)
**Top Internal Functions/Classes:**
  * `init_row` (Impact: 227.3 | O(2^N) | DB: 7)
  * `structure_from_cells` (Impact: 132.9 | O(N^6) | DB: 11)
  * `find_head_body_sep` (Impact: 100.4 | O(N^6) | DB: 15)
  * `scan_left` (Impact: 37.6 | O(N^4))
  * `scan_down` (Impact: 34.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 63`, `args: 21`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 53`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 24`, `import: 5`
* *Defense:* `safety: 7`, `doc: 46`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, docutils, re, docutils.utils, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/s5_html/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.065 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.406 IQR)
- **Top Global Matches:** file_cluster_13: 12.065, file_cluster_8: 12.314, file_cluster_11: 12.461
- **Magnitude:** 730.2 | **LOC:** 355 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (34.4987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `find_theme` (Impact: 609.2 | O(2^N) | DB: 93)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 41`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 104`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 12`, `import: 8`
* *Defense:* `safety: 3`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathlib, docutils.writers, sys, docutils, re, os, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.17 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.539 IQR)
- **Top Global Matches:** file_cluster_8: 12.17, file_cluster_2: 12.338, file_cluster_17: 12.373
- **Magnitude:** 724.66 | **LOC:** 559 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (93.006%), Tech Debt (16.4818%)
**Top Internal Functions/Classes:**
  * `keys` (Impact: 82.8 | O(N^1))
    * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
  * `getIncrementals` (Impact: 50.2 | O(2^N) | DB: 5)
  * `go` (Impact: 35.0 | O(N^1) | DB: 7)
  * `slideLabel` (Impact: 24.1 | O(N^1) | DB: 9)
  * `clicker` (Impact: 23.3 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 118`, `args: 30`, `func_start: 75`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 2`, `state_mutation: 238`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/transforms/frontmatter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.97 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.945 IQR)
- **Top Global Matches:** file_cluster_13: 11.97, file_cluster_8: 12.004, file_cluster_17: 12.13
- **Magnitude:** 538.3 | **LOC:** 549 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (15.1974%), Tech Debt (68.2505%)
**Top Internal Functions/Classes:**
  * `extract_bibliographic` (Impact: 261.3 | O(N^6) | DB: 8)
  * `authors_from_one_paragraph` (Impact: 42.4 | O(N^5))
  * `set_metadata` (Impact: 30.8 | O(N^6))
  * `authors_from_bullet_list` (Impact: 26.5 | O(N^4) | DB: 1)
  * `promote_title` (Impact: 25.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 53`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 18`, `import: 4`
* *Defense:* `safety: 28`, `doc: 22`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, docutils.transforms, __future__, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docutils-0.22.4/docutils/utils/math/mathml_elements.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.288 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.932 IQR)
- **Top Global Matches:** file_cluster_13: 13.288, file_cluster_16: 13.327, file_cluster_8: 13.432
- **Magnitude:** 525.32 | **LOC:** 483 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (24.463%), Tech Debt (99.956%)
**Top Internal Functions/Classes:**
  * `__setitem__` (Impact: 98.6 | O(2^N) | DB: 1)
  * `append` (Impact: 44.0 | O(2^N) | DB: 1)
  * `__init__` (Impact: 42.3 | O(2^N) | DB: 1)
    * *Intent:* # Group sub-expressions in a horizontal row # # <menclose>, <mtd>, <mscarry>, and <math> treat their...
  * `close` (Impact: 35.3 | O(2^N))
    * *Intent:* # Token elements # ~~~~~~~~~~~~~~ """Arbitrary text with no notational meaning."""
  * `transfer_attributes` (Impact: 30.8 | O(N^6))
    * *Intent:* # MathML element classes # ---------------------- class math(MathRow): """Top-level MathML element, ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 74`, `args: 20`, `func_start: 20`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `duplicate_logic: 7`
* *Architecture:* `api: 47`, `import: 3`
* *Defense:* `safety: 11`, `doc: 92`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004902
  * `Imports (Out-Degree: 0):` mathml_elements, numbers, xml.etree.ElementTree, __future__
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/parsers/rst/directives/body.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.434 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.181 IQR)
- **Top Global Matches:** file_cluster_8: 10.434, file_cluster_13: 10.481, file_cluster_7: 10.776
- **Magnitude:** 496.02 | **LOC:** 330 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (8.9859%), Tech Debt (11.3295%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 450.5 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 57`, `args: 10`, `func_start: 10`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 17`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 24`, `import: 5`
* *Defense:* `safety: 10`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.19
  * `Choke Point (Betweenness):` 0.000411 | `Ripple Effect (Closeness):` 0.014122
  * `Imports (Out-Degree: 2):` docutils.parsers.rst, docutils.utils.code_analyzer, docutils.parsers.rst.roles, docutils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `docutils-0.22.4/docutils/transforms/parts.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.326 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.931 IQR)
- **Top Global Matches:** file_cluster_13: 12.326, file_cluster_8: 12.521, file_cluster_11: 12.62
- **Magnitude:** 404.04 | **LOC:** 176 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (37.537%), Tech Debt (99.9881%)
**Top Internal Functions/Classes:**
  * `build_contents` (Impact: 169.6 | O(2^N) | DB: 7)
  * `update_section_numbers` (Impact: 85.0 | O(2^N) | DB: 1)
  * `apply` (Impact: 53.2 | O(N^5) | DB: 4)
    * *Intent:* """ This transform generates a table of contents from the entire document tree or from a single bran...
  * `apply` (Impact: 18.1 | O(N^4) | DB: 9)
    * *Intent:* """ default_priority = 710 """Should be applied before `Contents`."""
  * `visit_image` (Impact: 7.1 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 25`, `args: 10`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 42`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 13`, `import: 4`
* *Defense:* `safety: 6`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, docutils.transforms, __future__, docutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `docutils-0.22.4/docutils/writers/html4css1/__init__.py` (PYTHON) | Magnitude: 1576.2 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 675, state_mutation: 386, branch: 164, structural_boundaries: 157

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `docutils-0.22.4/tools/rst2html5.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, safety: 2, doc: 2
- `docutils-0.22.4/docutils/utils/_roman_numerals.py` (PYTHON) | Magnitude: 348.72 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 149, branch: 49, structural_boundaries: 43, encapsulation: 36
- `docutils-0.22.4/docutils/parsers/rst/directives/html.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, doc: 2, import: 2
- `docutils-0.22.4/docutils/transforms/frontmatter.py` (PYTHON) | Magnitude: 538.3 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 236, branch: 77, structural_boundaries: 53, safety: 28
- `docutils-0.22.4/docutils/utils/math/mathml_elements.py` (PYTHON) | Magnitude: 525.32 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 143, doc: 92, structural_boundaries: 74, api: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `docutils-0.22.4/docutils/statemachine.py` (PYTHON) | Magnitude: 2660.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 669, structural_boundaries: 217, state_mutation: 206, doc: 196
- `docutils-0.22.4/docutils/transforms/__init__.py` (PYTHON) | Magnitude: 120.4 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, doc: 44, state_mutation: 27, structural_boundaries: 22
- `docutils-0.22.4/docutils/utils/math/__init__.py` (PYTHON) | Magnitude: 41.46 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, doc: 8, branch: 5
- `docutils-0.22.4/tools/dev/unicode2rstsubs.py` (PYTHON) | Magnitude: 0.32 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 37, branch: 30, doc: 24
- `docutils-0.22.4/docutils/frontend.py` (PYTHON) | Magnitude: 2926.28 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 744, branch: 178, structural_boundaries: 148, doc: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `docutils-0.22.4/docutils/writers/s5_html/themes/default/slides.css` (CSS) | Magnitude: 0.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 3, import: 3
- `docutils-0.22.4/tools/docutils-cli.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, encapsulation: 2, import: 1
- `docutils-0.22.4/docutils/parsers/rst/directives/body.py` (PYTHON) | Magnitude: 496.02 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 206, structural_boundaries: 57, branch: 35, api: 24
- `docutils-0.22.4/docutils/parsers/rst/tableparser.py` (PYTHON) | Magnitude: 738.94 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 281, branch: 74, structural_boundaries: 63, state_mutation: 53
- `docutils-0.22.4/docutils/writers/odf_odt/__init__.py` (PYTHON) | Magnitude: 5107.8 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 2851, structural_boundaries: 491, branch: 412, state_mutation: 345

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `docutils-0.22.4/docutils/utils/code_analyzer.py` -> **Severity: 0.097** (Bridge: 0.001 * Flux: 100.0%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 0.078** (Bridge: 0.0012 * Flux: 65.6756%)
- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 0.075** (Bridge: 0.0015 * Flux: 49.9182%)
- `docutils-0.22.4/docutils/parsers/rst/roles.py` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 96.5578%)
- `docutils-0.22.4/docutils/parsers/rst/directives/images.py` -> **Severity: 0.048** (Bridge: 0.0006 * Flux: 80.6685%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 5.23** (Embedded: 0.0798 * Error Risk: 65.5346%)
- `docutils-0.22.4/docutils/utils/_typing.py` -> **Severity: 5.019** (Embedded: 0.07 * Error Risk: 71.6667%)
- `docutils-0.22.4/docutils/io.py` -> **Severity: 2.591** (Embedded: 0.053 * Error Risk: 48.9189%)
- `docutils-0.22.4/docutils/statemachine.py` -> **Severity: 0.449** (Embedded: 0.0098 * Error Risk: 45.8046%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 0.391** (Embedded: 0.0651 * Error Risk: 6.0087%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `docutils-0.22.4/docutils/nodes.py` -> **Severity: 8389.504** (Blast Radius: 86.685 * Doc Risk: 96.7815%)
- `docutils-0.22.4/docutils/io.py` -> **Severity: 5638.793** (Blast Radius: 58.548 * Doc Risk: 96.3106%)
- `docutils-0.22.4/docutils/frontend.py` -> **Severity: 5576.03** (Blast Radius: 56.842 * Doc Risk: 98.097%)
- `docutils-0.22.4/docutils/utils/_typing.py` -> **Severity: 4304.268** (Blast Radius: 52.361 * Doc Risk: 82.2037%)
- `docutils-0.22.4/docutils/core.py` -> **Severity: 3480.579** (Blast Radius: 34.934 * Doc Risk: 99.633%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
