# ARCHITECTURAL_BRIEF: pygments
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/pygments` |
| **Timestamp** | `2026-08-03T19:39:44.945454+00:00` |
| **Scan Duration** | `5.04s` |
| **Git Branch** | `master` |
| **Git Commit** | `a763de564943ea67ae5914dd615e9e50830e83d1` |
| **Git Remote** | `https://github.com/pygments/pygments.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 485 malicious artifacts.

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
| Total Artifacts | 2709 |
| Analyzed Artifacts (Scanned) | 1414 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1295 |
| Total LOC | 95142 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 52.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.364 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5072 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2694 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 769 | 2 | 54.4% |
| PYTHON | 372 | 74734 | 26.3% |
| HTML | 138 | 1197 | 9.8% |
| SCALA | 26 | 433 | 1.8% |
| JAVASCRIPT | 10 | 453 | 0.7% |
| PERL | 9 | 1947 | 0.6% |
| MAKEFILE | 7 | 1782 | 0.5% |
| LUA | 6 | 371 | 0.4% |
| RUBY | 6 | 1947 | 0.4% |
| C | 5 | 2749 | 0.4% |
| CPP | 5 | 1457 | 0.4% |
| HASKELL | 5 | 1130 | 0.4% |
| SHELL | 4 | 478 | 0.3% |
| ASSEMBLY | 4 | 249 | 0.3% |
| SCHEME | 4 | 1582 | 0.3% |
| CSS | 3 | 85 | 0.2% |
| JSON | 3 | 58 | 0.2% |
| FORTRAN | 3 | 567 | 0.2% |
| JAVA | 3 | 32 | 0.2% |
| BATCH | 2 | 350 | 0.1% |
| YAML | 2 | 238 | 0.1% |
| M4 | 2 | 11 | 0.1% |
| GLSL | 2 | 27 | 0.1% |
| GO | 2 | 25 | 0.1% |
| GROOVY | 2 | 4 | 0.1% |
| PHP | 2 | 9 | 0.1% |
| SQLITE | 2 | 59 | 0.1% |
| TYPESCRIPT | 2 | 38 | 0.1% |
| DOCKERFILE | 1 | 9 | 0.1% |
| COBOL | 1 | 2075 | 0.1% |
| CSHARP | 1 | 5 | 0.1% |
| JCL | 1 | 31 | 0.1% |
| KOTLIN | 1 | 40 | 0.1% |
| MATLAB | 1 | 19 | 0.1% |
| MARKDOWN | 1 | 0 | 0.1% |
| NIX | 1 | 65 | 0.1% |
| OBJECTIVE-C | 1 | 113 | 0.1% |
| APEX | 1 | 10 | 0.1% |
| POWERSHELL | 1 | 31 | 0.1% |
| PROTO | 1 | 21 | 0.1% |
| RUST | 1 | 487 | 0.1% |
| ZIG | 1 | 222 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.828`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 425 | 30.1% |
| file_cluster_0 | 135 | 9.5% |
| file_cluster_13 | 62 | 4.4% |
| file_cluster_9 | 6 | 0.4% |
| file_cluster_17 | 4 | 0.3% |
| file_cluster_16 | 4 | 0.3% |
| Unknown | 2 | 0.1% |
| file_cluster_2 | 2 | 0.1% |
| file_cluster_7 | 2 | 0.1% |
| file_cluster_4 | 1 | 0.1% |
| file_cluster_11 | 1 | 0.1% |
| file_cluster_12 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 768 | 54.3% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1295*

**Composition by Extension & Reason:**
- `.output`: 541x Excluded (Unsupported Extension: '.output'), 122x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 28x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.rst`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.rst')
- `.py`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 297 LOC), 1x Excluded (Machine-Generated Source Code Signature: 24 LOC)
- `.txt`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2718 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2201 LOC)
- `.graphql`: 14x Excluded (Unsupported Extension: '.graphql')
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.conf`: 7x Excluded (Unsupported Extension: '.conf')
- `.pytb`: 7x Excluded (Unsupported Extension: '.pytb')
- `.dtd`: 3x Excluded (Unsupported Extension: '.dtd'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mcschema`: 4x Excluded (Unsupported Extension: '.mcschema')
- `.sed`: 4x Excluded (Unsupported Extension: '.sed')
- `.srcinfo`: 4x Excluded (Unsupported Extension: '.SRCINFO')
- `.ul4`: 4x Excluded (Unsupported Extension: '.ul4')
- `.toc`: 4x Excluded (Unsupported Extension: '.toc')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 92.6 | 8.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 9.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.9 | 1.9 | 0.0 |
| API Exposure | 0.0 | 19.6 | 2.5 | 2.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 79.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.1 | 0.9 | 1.6 | 1.6 |
| Volatility Exposure | 0.0 | 52.5 | 8.5 | 13.1 | 13.1 |
| Documentation Exposure | 0.0 | 100.0 | 25.6 | 14.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 17.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 93.4 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/examplefiles/html/example.xhtml` (Hits: 99)
- `pygments/cmdline.py` (Hits: 48)
- `tests/examplefiles/fish/example.fish` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **token.py** (`pygments/token.py`) — 292 inbound connections
2. **lexer.py** (`pygments/lexer.py`) — 226 inbound connections
3. **style.py** (`pygments/style.py`) — 52 inbound connections
4. **util.py** (`pygments/util.py`) — 48 inbound connections
5. **formatter.py** (`pygments/formatter.py`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **eval.rs** (`tests/examplefiles/rust/eval.rs`) — 37 outbound dependencies
2. **other.py** (`pygments/lexers/other.py`) — 23 outbound dependencies
3. **compiled.py** (`pygments/lexers/compiled.py`) — 21 outbound dependencies
4. **AcidStateAdvanced.hs** (`tests/examplefiles/haskell/AcidStateAdvanced.hs`) — 21 outbound dependencies
5. **perl_perl5db.pl** (`tests/examplefiles/perl/perl_perl5db.pl`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Py_MakePendingCalls` (@ `tests/examplefiles/c/ceval.c`) -> Impact: **4862.2** | LOC: 1417
- `ASBeautifier::beautify` (@ `tests/examplefiles/cpp/example.cpp`) -> Impact: **4289.7** | LOC: 1253
- `psb_zbaseprc_aply` (@ `tests/examplefiles/fortran/zmlrpc.f90`) -> Impact: **2811.8** | LOC: 579
- `CodeRay_[Truncated]` (@ `tests/examplefiles/rb/example.rb`) -> Impact: **2735.7** | LOC: 1851
- `eval` (@ `tests/examplefiles/perl/perl_perl5db.pl`) -> Impact: **1560.7** | LOC: 950
  * *Intent:* ############################################## Begin lexical danger zone # 'my' variables used here could leak into (that is, be visible in) # the con...
- `escape_tex` (@ `pygments/formatters/latex.py`) -> Impact: **938.5** | LOC: 341
- `get_tokens_unprocessed` (@ `pygments/lexer.py`) -> Impact: **774.0** | LOC: 140
- `get_tokens_unprocessed` (@ `pygments/lexers/pascal.py`) -> Impact: **756.8** | LOC: 223
- `main_inner` (@ `pygments/cmdline.py`) -> Impact: **683.5** | LOC: 333
- `__new__` (@ `pygments/style.py`) -> Impact: **678.8** | LOC: 114

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `format` (@ `pygments/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ from io import StringIO, BytesIO __version__ = '2.20.0' __docformat__ = 'restructuredtext' __all__ = ['lex', 'format', 'highlight']
- `lex` (@ `pygments/__init__.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pygments/cmdline.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pygments/filters/__init__.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pygments/filters/__init__.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pygments/filters/__init__.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pygments/filters/__init__.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pygments/formatters/img.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pygments/formatters/irc.py`) -> **O(2^N) [Recursive]**
- `escape_tex` (@ `pygments/formatters/latex.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `ASBeautifier::beautify` (@ `tests/examplefiles/cpp/example.cpp`) -> DB Complexity: **529**
- `Py_MakePendingCalls` (@ `tests/examplefiles/c/ceval.c`) -> DB Complexity: **362**
- `codegenInit` (@ `tests/examplefiles/c/example.c`) -> DB Complexity: **150**
- `eval` (@ `tests/examplefiles/perl/perl_perl5db.pl`) -> DB Complexity: **149**
  * *Intent:* ############################################## Begin lexical danger zone # 'my' variables used here could leak into (that is, be visible in) # the con...
- `psb_zbaseprc_aply` (@ `tests/examplefiles/fortran/zmlrpc.f90`) -> DB Complexity: **128**
- `CodeRay_[Truncated]` (@ `tests/examplefiles/rb/example.rb`) -> DB Complexity: **117**
- `main_inner` (@ `pygments/cmdline.py`) -> DB Complexity: **99**
- `232-Build-Command` (@ `tests/examplefiles/cobol/example.cob`) -> DB Complexity: **86**
- `ASBeautifier::initStatic` (@ `tests/examplefiles/cpp/example.cpp`) -> DB Complexity: **78**
- `codegenEnterFunction` (@ `tests/examplefiles/c/example.c`) -> DB Complexity: **58**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pygments/lexers` | 241 | 46392.55 | 5.15% | 10.42% |
| `tests/examplefiles/scheme` | 2 | 17371.94 | 4.14% | 0.0% |
| `tests/examplefiles/c` | 4 | 7778.18 | 23.32% | 0.0% |
| `tests/examplefiles/cpp` | 5 | 6254.94 | 17.11% | 0.0% |
| `pygments` | 15 | 5553.86 | 20.98% | 15.38% |
| `tests/examplefiles/asc` | 1 | 5000.0 | 0.0% | 0.0% |
| `tests/examplefiles/sml` | 1 | 5000.0 | 0.0% | 0.0% |
| `pygments/formatters` | 12 | 4696.2 | 24.68% | 18.24% |
| `tests/examplefiles/lhs` | 2 | 3926.2 | 12.9% | 0.0% |
| `tests/examplefiles/rb` | 6 | 3902.64 | 10.21% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pygments/filter.py` -> **100.0%** Exposure
- `pygments/lexers/robotframework.py` -> **100.0%** Exposure
- `external/moin-parser.py` -> **99.9998%** Exposure
- `external/autopygmentize` -> **99.9995%** Exposure
- `pygments/formatters/other.py` -> **99.9988%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pygments/formatter.py` -> **100.0%** Exposure
- `pygments/formatters/rtf.py` -> **100.0%** Exposure
- `pygments/scanner.py` -> **100.0%** Exposure
- `external/autopygmentize` -> **100.0%** Exposure
- `pygments/console.py` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/examplefiles/cobol/example.cob` -> **50** Orphaned Functions | **4** Duplicates
- `pygments/lexers/templates.py` -> **0** Orphaned Functions | **51** Duplicates
- `tests/examplefiles/c/example.c` -> **45** Orphaned Functions | **0** Duplicates
- `pygments/lexers/robotframework.py` -> **0** Orphaned Functions | **29** Duplicates
- `tests/examplefiles/cpp/functions.cpp` -> **1** Orphaned Functions | **26** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tests/examplefiles/c/ceval.c`** -> AI Confidence: **99.48%**
2. **`tests/examplefiles/cpp/example.cpp`** -> AI Confidence: **99.48%**
3. **`tests/examplefiles/fortran/zmlrpc.f90`** -> AI Confidence: **99.48%**
4. **`pygments/lexers/webmisc.py`** -> AI Confidence: **99.39%**
5. **`tests/examplefiles/rb/pleac.in.rb`** -> AI Confidence: **99.39%**
6. **`pygments/lexers/pascal.py`** -> AI Confidence: **99.34%**
7. **`tests/examplefiles/zig/example.zig`** -> AI Confidence: **99.34%**
8. **`tests/examplefiles/make/firefox.mak`** -> AI Confidence: **99.32%**
9. **`pygments/lexers/rebol.py`** -> AI Confidence: **99.32%**
10. **`doc/pyodide/Dockerfile`** -> AI Confidence: **99.32%**
11. **`pygments/cmdline.py`** -> AI Confidence: **99.31%**
12. **`pygments/formatters/img.py`** -> AI Confidence: **99.31%**
13. **`pygments/lexer.py`** -> AI Confidence: **99.31%**
14. **`pygments/lexers/__init__.py`** -> AI Confidence: **99.31%**
15. **`pygments/lexers/_php_builtins.py`** -> AI Confidence: **99.31%**
16. **`pygments/lexers/csound.py`** -> AI Confidence: **99.31%**
17. **`pygments/lexers/markup.py`** -> AI Confidence: **99.31%**
18. **`pygments/sphinxext.py`** -> AI Confidence: **99.31%**
19. **`scripts/debug_lexer.py`** -> AI Confidence: **99.31%**
20. **`tests/examplefiles/c/example.c`** -> AI Confidence: **99.31%**
21. **`tests/examplefiles/rb/example.rb`** -> AI Confidence: **99.31%**
22. **`tests/examplefiles/javascript+mozpreproc/demo.js.in`** -> AI Confidence: **99.29%**
23. **`pygments/lexers/_vbscript_builtins.py`** -> AI Confidence: **99.29%**
24. **`pygments/lexers/modula2.py`** -> AI Confidence: **99.29%**
25. **`tests/examplefiles/devicetree/example.dts`** -> AI Confidence: **99.29%**
26. **`tests/examplefiles/html+php/html+php_faulty.phtml`** -> AI Confidence: **99.29%**
27. **`tests/examplefiles/php/ints.php`** -> AI Confidence: **99.29%**
28. **`tests/examplefiles/kotlin/example.kt`** -> AI Confidence: **99.29%**
29. **`tests/examplefiles/racket/example.rkt`** -> AI Confidence: **99.29%**
30. **`tests/examplefiles/scheme/r6rs-comments.scm`** -> AI Confidence: **99.29%**
31. **`tests/examplefiles/rb/hash_syntax.rb`** -> AI Confidence: **99.29%**
32. **`tests/examplefiles/scala/for-comprehension.scala`** -> AI Confidence: **99.29%**
33. **`tests/examplefiles/scala/inline.scala`** -> AI Confidence: **99.29%**
34. **`tests/examplefiles/scala/pattern-matching.scala`** -> AI Confidence: **99.29%**
35. **`pygments/formatters/__init__.py`** -> AI Confidence: **99.23%**
36. **`pygments/lexers/html.py`** -> AI Confidence: **99.23%**
37. **`pygments/lexers/mime.py`** -> AI Confidence: **99.23%**
38. **`tests/examplefiles/js/evil_regex.js`** -> AI Confidence: **99.17%**
39. **`pygments/lexers/_ada_builtins.py`** -> AI Confidence: **99.17%**
40. **`pygments/lexers/_qlik_builtins.py`** -> AI Confidence: **99.17%**
41. **`pygments/lexers/ruby.py`** -> AI Confidence: **99.17%**
42. **`tests/examplefiles/c/labels.c`** -> AI Confidence: **99.17%**
43. **`tests/examplefiles/rb/condensed_ruby.rb`** -> AI Confidence: **99.17%**
44. **`tests/examplefiles/scala/match-types.scala`** -> AI Confidence: **99.17%**
45. **`pygments/lexers/templates.py`** -> AI Confidence: **99.16%**
46. **`tests/test_basic_api.py`** -> AI Confidence: **99.16%**
47. **`tests/examplefiles/rust/eval.rs`** -> AI Confidence: **99.16%**
48. **`tests/test_html_formatter_linenos_elements.py`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `pygments/lexers/perl.py` -> **100.0%** Exposure
- `pygments/lexers/prolog.py` -> **0.7274%** Exposure
- `tests/test_irc_formatter.py` -> **0.0051%** Exposure
- `tests/test_util.py` -> **0.0002%** Exposure
### Exploit Generation Surface
- `doc/_static/demo-worker.js` -> **100.0%** Exposure
- `pygments/cmdline.py` -> **100.0%** Exposure
- `pygments/filters/__init__.py` -> **100.0%** Exposure
- `pygments/formatters/__init__.py` -> **100.0%** Exposure
- `pygments/formatters/bbcode.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `pygments/formatters/__init__.py` -> **100.0%** Exposure
- `pygments/lexers/__init__.py` -> **100.0%** Exposure
- `pygments/lexers/comal.py` -> **100.0%** Exposure
- `pygments/lexers/shell.py` -> **100.0%** Exposure
- `tests/test_html_formatter.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `tests/examplefiles/cpp/example.cpp` -> **9.9935%** Exposure
- `tests/examplefiles/c/ceval.c` -> **0.0017%** Exposure
### Hardcoded Payload Artifacts
- `tests/examplefiles/cobol/example.cob` -> **93.3829%** Exposure
### Algorithmic DoS Exposure
- `external/moin-parser.py` -> **100.0%** Exposure
- `pygments/cmdline.py` -> **100.0%** Exposure
- `pygments/console.py` -> **100.0%** Exposure
- `pygments/filters/__init__.py` -> **100.0%** Exposure
- `pygments/formatter.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1425` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pygments/lexer.py` (PYTHON) -> Cumulative Risk: **804.85**
- **Archetype:** `file_cluster_13` (Distance: 12.633 IQR)
- **Magnitude:** 2105.42 | **LOC:** 964 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `get_tokens_unprocessed` (Impact: 774.0), `_process_new_state` (Impact: 348.3), `_preprocess_lexer_input` (Impact: 111.5)

### 2. `external/moin-parser.py` (PYTHON) -> Cumulative Risk: **788.13**
- **Archetype:** `file_cluster_13` (Distance: 12.362 IQR)
- **Magnitude:** 0.07 | **LOC:** 113 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9998%)
- **Heaviest Functions:** `__init__` (Impact: 40.4), `wrap` (Impact: 8.2), `format` (Impact: 2.9)

### 3. `pygments/lexers/robotframework.py` (PYTHON) -> Cumulative Risk: **770.26**
- **Archetype:** `file_cluster_8` (Distance: 11.311 IQR)
- **Magnitude:** 1099.8 | **LOC:** 552 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `tokenize` (Impact: 142.7), `_tokenize` (Impact: 110.8), `_tokenize` (Impact: 80.7)

### 4. `pygments/lexers/__init__.py` (PYTHON) -> Cumulative Risk: **750.38**
- **Archetype:** `file_cluster_13` (Distance: 11.209 IQR)
- **Magnitude:** 421.22 | **LOC:** 363 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `find_lexer_class_for_filename` (Impact: 69.3), `guess_lexer_for_filename` (Impact: 56.8), `guess_lexer` (Impact: 43.1)

### 5. `pygments/formatters/terminal256.py` (PYTHON) -> Cumulative Risk: **741.25**
- **Archetype:** `file_cluster_8` (Distance: 12.03 IQR)
- **Magnitude:** 805.12 | **LOC:** 339 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `escape` (Impact: 530.1), `format_unencoded` (Impact: 92.9), `_setup_styles` (Impact: 61.4)

### 6. `pygments/formatters/other.py` (PYTHON) -> Cumulative Risk: **735.02**
- **Archetype:** `file_cluster_13` (Distance: 11.389 IQR)
- **Magnitude:** 224.18 | **LOC:** 161 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `format` (Impact: 78.8), `__init__` (Impact: 49.3), `__init__` (Impact: 27.9)

### 7. `pygments/scanner.py` (PYTHON) -> Cumulative Risk: **708.85**
- **Archetype:** `file_cluster_13` (Distance: 13.531 IQR)
- **Magnitude:** 103.88 | **LOC:** 105 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `scan` (Impact: 25.0), `check` (Impact: 14.3), `__init__` (Impact: 6.5)

### 8. `pygments/sphinxext.py` (PYTHON) -> Cumulative Risk: **706.97**
- **Archetype:** `file_cluster_13` (Distance: 11.735 IQR)
- **Magnitude:** 320.32 | **LOC:** 248 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `document_lexers` (Impact: 124.4), `document_lexers_overview` (Impact: 75.7), `run` (Impact: 28.6)

### 9. `pygments/formatters/rtf.py` (PYTHON) -> Cumulative Risk: **702.9**
- **Archetype:** `file_cluster_13` (Distance: 12.177 IQR)
- **Magnitude:** 746.32 | **LOC:** 350 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `hex_to_rtf_color` (Impact: 505.1), `__init__` (Impact: 111.1), `_escape_text` (Impact: 27.1)

### 10. `doc/_static/demo.js` (JAVASCRIPT) -> Cumulative Risk: **695.73**
- **Archetype:** `file_cluster_4` (Distance: 10.749 IQR)
- **Magnitude:** 222.0 | **LOC:** 201 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.0462%), Logic Bomb (98.4899%)
- **Heaviest Functions:** `highlight` (Impact: 65.8), `onmessage` (Impact: 43.5), `updateCopyLink` (Impact: 14.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/examplefiles/scheme/boot-9.scm` (SCHEME | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.01 IQR)
- **Top Global Matches:** file_cluster_8: 11.01, file_cluster_7: 11.27, file_cluster_1: 11.479
- **Magnitude:** 17357.78 | **LOC:** 1558 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.2827%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 74`, `args: 118`, `func_start: 118`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 26`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 28`
* *Defense:* `safety: 1`, `doc: 252`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/lexers/webmisc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.841 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.698 IQR)
- **Top Global Matches:** file_cluster_8: 10.841, file_cluster_7: 11.092, file_cluster_13: 11.157
- **Magnitude:** 11377.13 | **LOC:** 1007 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (34.0057%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 64`, `args: 28`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 149`, `dead_code: 1`
* *Architecture:* `api: 34`, `import: 7`
* *Defense:* `safety: 5`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.647
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00127
  * `Imports (Out-Degree: 6):` pygments.lexers.ruby, re, pygments.lexers.javascript, pygments.lexer, pygments.token, pygments.lexers.html, pygments.lexers.css
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/examplefiles/c/ceval.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.842 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.819 IQR)
- **Top Global Matches:** file_cluster_8: 13.842, file_cluster_13: 14.051, file_cluster_11: 14.1
- **Magnitude:** 6212.38 | **LOC:** 2605 | **CtrlFlow:** 91.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 362
- **Risk Profile:** Cognitive Load (49.5216%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Py_MakePendingCalls` (Impact: 4862.2 | O(2^N) | DB: 362)
  * `dump_tsc` (Impact: 6.7 | O(N^1) | DB: 8)
    * *Intent:* #else /* this is for linux/x86 (and probably any other GCC/x86 combo) */
  * `PyEval_AcquireThread` (Impact: 6.6 | O(2^N))
  * `PyEval_ReleaseThread` (Impact: 6.5 | O(2^N))
  * `PyEval_InitThreads` (Impact: 3.3 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 499`, `structural_boundaries: 46`, `args: 11`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1112`, `dead_code: 1`, `fragile_debt: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 179`, `import: 9`
* *Defense:* `safety: 10`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` frameobject.h, errno.h, Python.h, code.h, eval.h, pythread.h, structmember.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/cpp/example.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.331 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.416 IQR)
- **Top Global Matches:** file_cluster_13: 15.331, file_cluster_11: 15.485, file_cluster_8: 15.499
- **Magnitude:** 6060.92 | **LOC:** 2364 | **CtrlFlow:** 83.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 529
- **Risk Profile:** Cognitive Load (29.4508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ASBeautifier::beautify` (Impact: 4289.7 | O(N^6) | DB: 529)
  * `AnsiGenerator::getOpenTag` (Impact: 11.1 | O(N^6) | DB: 3)
    * *Intent:* ***************************************************************************/ /**********************...
  * `AnsiGenerator::AnsiGenerator` (Impact: 7.7 | O(N^2) | DB: 5)
  * `AnsiGenerator::getMatchingOpenTag` (Impact: 4.2 | O(N^1))
  * `ASBeautifier::initStatic` (Impact: 4.0 | O(N^1) | DB: 78)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 84`, `args: 42`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `state_mutation: 1687`, `dead_code: 11`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 18`
* *Architecture:* `api: 2`, `import: 27`
* *Defense:* `doc: 61`, `immutability_locks: 65`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` charcodes.h, compiler_defines.h, ASFormatter.h, ASSourceIterator.h, algorithm, codegenerator.h, vector, ansigenerator.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/asc/id_ecdsa` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/sml/intsyn.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/lhs/Sudoku.lhs` (HASKELL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.779 IQR)
- **Top Global Matches:** file_cluster_8: 9.779, file_cluster_17: 10.391, file_cluster_16: 10.482
- **Magnitude:** 3829.58 | **LOC:** 383 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.4861%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 50`, `args: 36`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 12`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `safety: 18`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Monad, List, Array
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/fortran/zmlrpc.f90` (FORTRAN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.579 IQR)
- **Top Global Matches:** file_cluster_13: 13.579, file_cluster_4: 13.598, file_cluster_17: 13.635
- **Magnitude:** 3174.58 | **LOC:** 799 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 128
- **Risk Profile:** Cognitive Load (48.8173%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `psb_zbaseprc_aply` (Impact: 2811.8 | O(2^N) | DB: 128)
  * `mlprec_wrk_free` (Impact: 32.1 | O(2^N) | DB: 1)
  * `psb_zmlprc_aply` (Impact: 9.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 34`, `args: 18`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 35`, `state_mutation: 298`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 3`, `concurrency: 12`, `import: 10`
* *Defense:* `safety: 20`, `immutability_locks: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` psb_psblas_mod, psb_descriptor_type, psb_penv_mod, psb_serial_mod, psb_error_mod, psb_const_mod, psb_prec_type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/rb/example.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.415 IQR)
- **Top Global Matches:** file_cluster_8: 13.415, file_cluster_11: 13.488, file_cluster_13: 13.619
- **Magnitude:** 3078.32 | **LOC:** 1853 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 117
- **Risk Profile:** Cognitive Load (30.6463%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CodeRay_[Truncated]` (Impact: 2735.7 | O(N^6) | DB: 117)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 207`, `args: 91`, `func_start: 90`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 2`, `state_mutation: 313`, `dead_code: 16`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 6`, `doc: 12`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` set, rweb, strscan, rbtree, TSort, tsort, rwebcookie, Enumerable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/lexers/dotnet.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.826 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.976 IQR)
- **Top Global Matches:** file_cluster_8: 9.826, file_cluster_7: 10.242, file_cluster_13: 10.313
- **Magnitude:** 2383.4 | **LOC:** 874 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9262%), Tech Debt (8.7467%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 85`, `args: 8`, `func_start: 8`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 21`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 13`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 16`, `doc: 29`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000706
  * `Imports (Out-Degree: 4):` pygments.util, re, pygments, pygments.lexer, pygments.token, pygments.lexers.html
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/ruby.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.704 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.42 IQR)
- **Top Global Matches:** file_cluster_8: 8.704, file_cluster_7: 9.069, file_cluster_1: 9.365
- **Magnitude:** 2302.49 | **LOC:** 519 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.8664%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 31`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 13`
* *Architecture:* `io: 1`, `api: 10`, `import: 4`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.166
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.006416
  * `Imports (Out-Degree: 3):` pygments.token, pygments.util, re, pygments.lexer
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pygments/lexers/javascript.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.549 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.81 IQR)
- **Top Global Matches:** file_cluster_8: 9.549, file_cluster_7: 9.941, file_cluster_1: 10.222
- **Magnitude:** 2123.39 | **LOC:** 1592 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.2823%), Tech Debt (8.3474%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 70`, `args: 5`, `func_start: 5`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 28`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 12`, `doc: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006704
  * `Imports (Out-Degree: 3):` pygments.util, pygments.unistring, re, pygments.lexer, pygments.token, pygments.lexers._lasso_builtins
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pygments/lexer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.633 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.582 IQR)
- **Top Global Matches:** file_cluster_13: 12.633, file_cluster_7: 12.805, file_cluster_8: 12.845
- **Magnitude:** 2105.42 | **LOC:** 964 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (41.2508%), Tech Debt (99.9962%)
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` (Impact: 774.0 | O(2^N) | DB: 12)
  * `_process_new_state` (Impact: 348.3 | O(2^N) | DB: 4)
  * `_preprocess_lexer_input` (Impact: 111.5 | O(N^6) | DB: 2)
    * *Intent:* #: A list of short, unique identifiers that can be used to look
  * `bygroups` (Impact: 110.3 | O(N^6))
    * *Intent:* """ text = self._preprocess_lexer_input(text) def streamer(): for _, t, v in self.get_tokens_unproce...
  * `using` (Impact: 88.6 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 165`, `args: 45`, `func_start: 43`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 110`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 16`
* *Architecture:* `io: 1`, `api: 41`, `import: 9`
* *Defense:* `safety: 46`, `doc: 70`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 52.543
  * `Choke Point (Betweenness):` 0.000406 | `Ripple Effect (Closeness):` 0.159809
  * `Imports (Out-Degree: 4):` pygments.util, pygments.regexopt, time, sys, re, chardet, pygments.filter, pygments.filters...
  * `Imported By (In-Degree: 226):` (Excluded from Brief to save tokens)

### `tests/examplefiles/cobol/example.cob` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.931 IQR)
- **Top Global Matches:** file_cluster_8: 12.931, file_cluster_0: 13.294, file_cluster_11: 13.332
- **Magnitude:** 2061.8 | **LOC:** 2621 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 86
- **Risk Profile:** Cognitive Load (44.1501%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `202-Show-And-Change-Switches` (Impact: 197.3 | O(N^6) | DB: 37)
  * `032-Process` (Impact: 151.8 | O(N^6) | DB: 46)
  * `232-Build-Command` (Impact: 79.0 | O(N^5) | DB: 86)
  * `106-Determine-Folder-Path` (Impact: 71.0 | O(N^6) | DB: 20)
  * `213-Run-Compiler` (Impact: 67.5 | O(N^4) | DB: 45)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 150`, `args: 15`, `func_start: 74`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 782`, `dead_code: 2`, `fragile_debt: 6`, `duplicate_logic: 4`, `orphaned_logic: 50`
* *Architecture:* `io: 26`, `api: 30`, `import: 2`
* *Defense:* `safety: 113`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` screenio, FileStat-Msgs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/perl/perl_perl5db.pl` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.93 IQR)
- **Top Global Matches:** file_cluster_0: 12.93, file_cluster_13: 13.044, file_cluster_4: 13.14
- **Magnitude:** 1825.98 | **LOC:** 999 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 149
- **Risk Profile:** Cognitive Load (22.79%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `eval` (Impact: 1560.7 | O(2^N) | DB: 149)
    * *Intent:* ############################################## Begin lexical danger zone # 'my' variables used here ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 60`, `args: 4`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 231`, `dead_code: 2`, `fragile_debt: 7`
* *Architecture:* `io: 22`, `concurrency: 23`, `import: 16`
* *Defense:* `safety: 7`, `doc: 75`, `sync_locks: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Term::ReadLine, IO::Socket, that, routine, threads, guarantees, C...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/c/example.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.546 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.442 IQR)
- **Top Global Matches:** file_cluster_8: 13.546, file_cluster_13: 13.735, file_cluster_7: 13.907
- **Magnitude:** 1508.68 | **LOC:** 2081 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 150
- **Risk Profile:** Cognitive Load (33.7724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convertType` (Impact: 24.7 | O(2^N))
  * `rb_ary_join` (Impact: 20.3 | O(N^1) | DB: 17)
  * `rb_ary_splice` (Impact: 18.2 | O(N^1) | DB: 13)
    * *Intent:* /* * call-seq: * array.push(obj, ... ) -> array * * Append---Pushes the given object(s) on to the en...
  * `codegenAddVariable` (Impact: 16.2 | O(N^1) | DB: 1)
  * `rb_get_values_at` (Impact: 13.6 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 132`, `args: 11`, `func_start: 76`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 828`, `orphaned_logic: 45`
* *Architecture:* `api: 307`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` varargs.h, stdarg.h, util.h, codegen.h, st.h, node.h, stdlib.h, ruby.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/lexers/haskell.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.932 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.559 IQR)
- **Top Global Matches:** file_cluster_8: 9.932, file_cluster_7: 10.335, file_cluster_13: 10.45
- **Magnitude:** 1440.04 | **LOC:** 868 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.8663%), Tech Debt (20.2758%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 63`, `args: 7`, `func_start: 7`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 14`, `import: 5`
* *Defense:* `safety: 2`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000706
  * `Imports (Out-Degree: 3):` X, pygments.lexers.markup, re, pygments, pygments.lexer, pygments.token
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/matlab.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.676 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.243 IQR)
- **Top Global Matches:** file_cluster_8: 8.676, file_cluster_7: 9.538, file_cluster_1: 9.74
- **Magnitude:** 1372.31 | **LOC:** 3308 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.2231%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 43`, `args: 4`, `func_start: 4`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 21`, `dead_code: 2`
* *Architecture:* `io: 9`, `api: 9`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 5`, `doc: 12`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000941
  * `Imports (Out-Degree: 2):` pygments.token, pygments.lexers, re, pygments.lexer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/cmdline.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.67 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.543 IQR)
- **Top Global Matches:** file_cluster_8: 10.67, file_cluster_13: 10.858, file_cluster_17: 11.013
- **Magnitude:** 1229.98 | **LOC:** 669 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 99
- **Risk Profile:** Cognitive Load (18.6989%), Tech Debt (13.5098%)
**Top Internal Functions/Classes:**
  * `main_inner` (Impact: 683.5 | O(N^6) | DB: 99)
  * `main` (Impact: 291.9 | O(N^6) | DB: 39)
  * `_print_list` (Impact: 67.4 | O(N^4) | DB: 2)
  * `__init__` (Impact: 51.8 | O(2^N))
  * `_print_list_as_json` (Impact: 41.1 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 113`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 12`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 48`, `api: 4`, `import: 19`
* *Defense:* `safety: 47`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001411
  * `Imports (Out-Degree: 7):` os, json, pygments.filters, pygments.styles, pygments.formatters.terminal, and, pygments.lexers.special, pygments.formatters...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pygments/lexers/php.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.604 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.0 IQR)
- **Top Global Matches:** file_cluster_8: 9.604, file_cluster_13: 9.92, file_cluster_7: 9.953
- **Magnitude:** 1142.68 | **LOC:** 336 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.5078%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 35`, `args: 5`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 29`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.699
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002205
  * `Imports (Out-Degree: 4):` pygments.util, re, pygments.lexer, pygments.token, pygments.lexers._php_builtins
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pygments/lexers/robotframework.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.311 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.369 IQR)
- **Top Global Matches:** file_cluster_8: 11.311, file_cluster_7: 11.478, file_cluster_13: 11.49
- **Magnitude:** 1099.8 | **LOC:** 552 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (52.6259%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `tokenize` (Impact: 142.7 | O(2^N) | DB: 4)
  * `_tokenize` (Impact: 110.8 | O(2^N) | DB: 5)
  * `_tokenize` (Impact: 80.7 | O(2^N) | DB: 2)
  * `_variable_state` (Impact: 36.5 | O(N^5) | DB: 4)
  * `_tokenize` (Impact: 32.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 149`, `args: 60`, `func_start: 60`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 118`, `duplicate_logic: 29`
* *Architecture:* `api: 37`, `import: 3`
* *Defense:* `safety: 5`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000706
  * `Imports (Out-Degree: 2):` pygments.token, re, pygments.lexer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/formatters/latex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.271 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.843 IQR)
- **Top Global Matches:** file_cluster_13: 11.271, file_cluster_8: 11.435, file_cluster_7: 11.453
- **Magnitude:** 1006.72 | **LOC:** 519 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (23.3263%), Tech Debt (10.7469%)
**Top Internal Functions/Classes:**
  * `escape_tex` (Impact: 938.5 | O(2^N) | DB: 27)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 36`, `args: 13`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 55`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 2`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.923
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001882
  * `Imports (Out-Degree: 4):` pygments.util, io, pygments.lexer, pygments.formatter, pygments.token
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pygments/lexers/csound.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.609 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.606 IQR)
- **Top Global Matches:** file_cluster_8: 7.609, file_cluster_7: 8.211, file_cluster_1: 8.491
- **Magnitude:** 914.9 | **LOC:** 467 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.4066%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 21`, `args: 2`, `func_start: 2`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` re, pygments.lexer, pygments.token, pygments.lexers.python, pygments.lexers.html, pygments.lexers.scripting, pygments.lexers._csound_builtins
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/lexers/pascal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.747 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.14 IQR)
- **Top Global Matches:** file_cluster_8: 10.747, file_cluster_13: 11.06, file_cluster_7: 11.174
- **Magnitude:** 909.08 | **LOC:** 645 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (37.7015%), Tech Debt (67.8982%)
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` (Impact: 756.8 | O(N^6) | DB: 11)
  * `__init__` (Impact: 61.6 | O(2^N) | DB: 10)
  * `__init__` (Impact: 5.3 | O(2^N) | DB: 1)
  * `get_tokens_unprocessed` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 28`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 64`, `dead_code: 5`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 5`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.57
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000706
  * `Imports (Out-Degree: 5):` pygments.util, re, pygments.scanner, pygments.lexer, pygments.token, pygments.lexers.modula2
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/crystal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.468 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.987 IQR)
- **Top Global Matches:** file_cluster_8: 8.468, file_cluster_7: 8.846, file_cluster_1: 9.162
- **Magnitude:** 906.98 | **LOC:** 365 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.4437%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 18`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.57
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000706
  * `Imports (Out-Degree: 2):` pygments.token, re, pygments.lexer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/test_guess.py` (PYTHON) | Magnitude: 153.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 77, test: 67, encapsulation: 42
- `tests/test_func.py` (PYTHON) | Magnitude: 17.86 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 18, structural_boundaries: 16, doc: 10, indent_spaces: 10
- `tests/examplefiles/perl/perl_perl5db.pl` (PERL) | Magnitude: 1825.98 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 273, state_mutation: 231, branch: 215, doc: 75
- `tests/test_html_formatter_linenos_elements.py` (PYTHON) | Magnitude: 203.32 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, state_mutation: 21, structural_boundaries: 14, test: 9
- `tests/test_templates.py` (PYTHON) | Magnitude: 41.04 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 27, test: 27, doc: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `external/autopygmentize` (SHELL) | Magnitude: 0.09 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 36, branch: 20, io: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/examplefiles/scala/inline.scala` (SCALA) | Magnitude: 56.04 | Delta: **0.339 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 7, branch: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/examplefiles/perl/perl_misc.pl` (PERL) | Magnitude: 39.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 23, structural_boundaries: 7, branch: 5
- `tests/test_regexlexer.py` (PYTHON) | Magnitude: 9.62 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 17, test: 13, api: 7
- `tests/test_coffeescript.py` (PYTHON) | Magnitude: 125.16 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, test: 6, branch: 5
- `pygments/lexers/codeql.py` (PYTHON) | Magnitude: 17.92 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 10, branch: 4, import: 3
- `tests/test_latex_formatter.py` (PYTHON) | Magnitude: 43.96 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 28, import: 11, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/examplefiles/scala/extensions.scala` (SCALA) | Magnitude: 6.9 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, generics: 10, reflection_metaprogramming: 10
- `tests/examplefiles/scala/inheritance.scala` (SCALA) | Magnitude: 14.16 | Delta: **0.23 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, class_start: 5, generics: 5, branch: 2
- `tests/examplefiles/scala/declarations.scala` (SCALA) | Magnitude: 58.84 | Delta: **0.334 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 133, indent_spaces: 57, generics: 47, reflection_metaprogramming: 36
- `tests/examplefiles/scala/type-operators.scala` (SCALA) | Magnitude: 18.26 | Delta: **0.562 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 6, bitwise_ops: 4, structural_boundaries: 2, immutability_locks: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/examplefiles/rust/eval.rs` (RUST) | Magnitude: 750.04 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 471, structural_boundaries: 154, safety: 86, branch: 76
- `tests/examplefiles/js/general.js` (JAVASCRIPT) | Magnitude: 32.04 | Delta: **0.235 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, structural_boundaries: 16, branch: 10, indent_spaces: 9
- `tests/examplefiles/haskell/SmallCheck.hs` (HASKELL) | Magnitude: 259.32 | Delta: **0.365 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 153, state_mutation: 115, structural_boundaries: 69, args: 69
- `tests/examplefiles/lua/example.lua` (LUA) | Magnitude: 214.84 | Delta: **0.38 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 65, state_mutation: 58, indent_tabs: 42, structural_boundaries: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/examplefiles/jsx/general.jsx` (JAVASCRIPT) | Magnitude: 13.72 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 18, ui_framework: 10, immutability_locks: 9, structural_boundaries: 7
- `doc/_templates/docssidebar.html` (HTML) | Magnitude: 11.56 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ssr_boundaries: 3, branch: 2, io: 2, ui_framework: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `doc/_static/demo.js` (JAVASCRIPT) | Magnitude: 222.0 | Delta: **0.22 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 123, concurrency: 38, globals: 36, branch: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pygments/lexers/data.py` (PYTHON) | Magnitude: 479.7 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 475, branch: 123, structural_boundaries: 61, state_mutation: 58
- `pygments/filter.py` (PYTHON) | Magnitude: 41.9 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, encapsulation: 12, doc: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/examplefiles/cpp/noexcept.cpp` (CPP) | Magnitude: 16.64 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, args: 7, safety_bypasses: 7, pointers: 7
- `tests/examplefiles/objective-c/objc_example.m` (OBJECTIVE-C) | Magnitude: 61.86 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 55, state_mutation: 24, structural_boundaries: 19, explicit_casts: 15
- `pygments/lexers/wowtoc.py` (PYTHON) | Magnitude: 104.66 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 12, branch: 10, encapsulation: 9
- `tests/examplefiles/cpp/functions.cpp` (CPP) | Magnitude: 155.28 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 110, state_mutation: 92, args: 72, structural_boundaries: 40
- `tests/examplefiles/scala/comments.scala` (SCALA) | Magnitude: 10.52 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pygments/lexers/_csound_builtins.py` (PYTHON) | Magnitude: 13.64 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 14, explicit_casts: 3, dead_code: 1, sec_high_risk_execution: 1
- `pygments/styles/arduino.py` (PYTHON) | Magnitude: 18.46 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 69, dead_code: 64, structural_boundaries: 5, doc: 4
- `pygments/styles/tango.py` (PYTHON) | Magnitude: 18.56 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 74, dead_code: 70, structural_boundaries: 5, doc: 4
- `pygments/styles/monokai.py` (PYTHON) | Magnitude: 18.6 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 76, dead_code: 70, structural_boundaries: 5, doc: 4
- `pygments/styles/paraiso_dark.py` (PYTHON) | Magnitude: 18.84 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 76, dead_code: 70, structural_boundaries: 5, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pygments/lexers/webmisc.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 11377.13
- `pygments/lexers/dotnet.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 2383.4
- `pygments/lexers/ruby.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 2302.49
- `pygments/lexers/javascript.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 2123.39
- `pygments/lexers/matlab.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 1372.31

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pygments/lexer.py` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 99.7728%)
- `pygments/formatter.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pygments/lexer.py` -> **Severity: 8.136** (Embedded: 0.1598 * Error Risk: 50.9125%)
- `pygments/regexopt.py` -> **Severity: 3.961** (Embedded: 0.0849 * Error Risk: 46.6667%)
- `pygments/token.py` -> **Severity: 1.228** (Embedded: 0.2056 * Error Risk: 5.9732%)
- `pygments/formatter.py` -> **Severity: 0.562** (Embedded: 0.0089 * Error Risk: 63.3333%)
- `pygments/util.py` -> **Severity: 0.462** (Embedded: 0.103 * Error Risk: 4.484%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pygments/token.py` -> **Severity: 8918.9** (Blast Radius: 89.189 * Doc Risk: 100.0%)
- `pygments/lexer.py` -> **Severity: 5254.3** (Blast Radius: 52.543 * Doc Risk: 100.0%)
- `pygments/util.py` -> **Severity: 2296.8** (Blast Radius: 22.968 * Doc Risk: 100.0%)
- `pygments/style.py` -> **Severity: 1253.9** (Blast Radius: 12.539 * Doc Risk: 100.0%)
- `pygments/regexopt.py` -> **Severity: 1219.4** (Blast Radius: 12.194 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
