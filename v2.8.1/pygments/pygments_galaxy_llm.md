# ARCHITECTURAL_BRIEF: pygments
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pygments/pygments.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 2709 |
| Analyzed Artifacts (Scanned) | 1452 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1257 |
| Total LOC | 101930 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 53.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3636 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5054 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5975 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 781 | 2 | 53.8% |
| PYTHON | 377 | 77559 | 26.0% |
| HTML | 140 | 1322 | 9.6% |
| SCALA | 26 | 433 | 1.8% |
| JAVASCRIPT | 10 | 452 | 0.7% |
| PERL | 9 | 2072 | 0.6% |
| MAKEFILE | 7 | 1785 | 0.5% |
| RUBY | 7 | 2189 | 0.5% |
| LUA | 6 | 448 | 0.4% |
| SHELL | 5 | 1184 | 0.3% |
| C | 5 | 3596 | 0.3% |
| CPP | 5 | 1690 | 0.3% |
| HASKELL | 5 | 1129 | 0.3% |
| JAVA | 5 | 482 | 0.3% |
| CSS | 4 | 122 | 0.3% |
| ASSEMBLY | 4 | 249 | 0.3% |
| GROOVY | 4 | 95 | 0.3% |
| SCHEME | 4 | 1596 | 0.3% |
| JSON | 3 | 58 | 0.2% |
| ADA | 3 | 230 | 0.2% |
| FORTRAN | 3 | 588 | 0.2% |
| PHP | 3 | 294 | 0.2% |
| BATCH | 2 | 347 | 0.1% |
| YAML | 2 | 240 | 0.1% |
| M4 | 2 | 11 | 0.1% |
| CSHARP | 2 | 249 | 0.1% |
| GLSL | 2 | 27 | 0.1% |
| GO | 2 | 25 | 0.1% |
| MATLAB | 2 | 22 | 0.1% |
| POWERSHELL | 2 | 97 | 0.1% |
| SQLITE | 2 | 59 | 0.1% |
| TYPESCRIPT | 2 | 38 | 0.1% |
| DOCKERFILE | 1 | 9 | 0.1% |
| BLP | 1 | 28 | 0.1% |
| COBOL | 1 | 2075 | 0.1% |
| DART | 1 | 17 | 0.1% |
| JCL | 1 | 26 | 0.1% |
| KOTLIN | 1 | 40 | 0.1% |
| MARKDOWN | 1 | 0 | 0.1% |
| NIX | 1 | 65 | 0.1% |
| OBJECTIVE-C | 1 | 113 | 0.1% |
| APEX | 1 | 10 | 0.1% |
| PROTO | 1 | 21 | 0.1% |
| RUST | 1 | 487 | 0.1% |
| SOLIDITY | 1 | 88 | 0.1% |
| SWIFT | 1 | 39 | 0.1% |
| XML | 1 | 0 | 0.1% |
| ZIG | 1 | 222 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.22; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 67%, Declarative / Non-Code 16%, Interface Declarations Files 4%, Large Core Modules 4%, Compute Cores Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 669 | 46.1% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 780 | 53.7% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1257*

**Composition by Extension & Reason:**
- `.output`: 663x Excluded (Unsupported Extension: '.output')
- `no_extension`: 30x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.dylan-console')
- `.rst`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.rst')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 297 LOC), 1x Excluded (Machine-Generated Source Code Signature: 24 LOC), 1x Excluded (Machine-Generated Source Code Signature: 996 LOC)
- `.graphql`: 14x Excluded (Unsupported Extension: '.graphql')
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.conf`: 7x Excluded (Unsupported Extension: '.conf')
- `.pytb`: 7x Excluded (Unsupported Extension: '.pytb')
- `.dtd`: 4x Excluded (Unsupported Extension: '.dtd')
- `.mcschema`: 4x Excluded (Unsupported Extension: '.mcschema')
- `.sed`: 4x Excluded (Unsupported Extension: '.sed')
- `.srcinfo`: 4x Excluded (Unsupported Extension: '.SRCINFO')
- `.ul4`: 4x Excluded (Unsupported Extension: '.ul4')
- `.toc`: 4x Excluded (Unsupported Extension: '.toc')
- `.ent`: 3x Excluded (Unsupported Extension: '.ent')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.0 | 2.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 47.7 | 63.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.3 | 8.5 | 4.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 75.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.2 | 0.9 | 1.6 | 1.6 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 54.0 | 8.5 | 13.4 | 13.4 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 34.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 93.4 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1445 | 99 | 0 | `tests/examplefiles/cpp/example.cpp` |
| cleanup | 85 | 25 | 0 | `tests/examplefiles/make/Makefile` |
| guards | 1965 | 217 | 2 | `tests/examplefiles/cpp/functions.cpp` |
| danger | 1476 | 224 | 2 | `tests/examplefiles/fish/example.fish` |
| concurrency | 759 | 125 | 0 | `pygments/lexers/webmisc.py` |
| connectivity | 2525 | 413 | 4 | `pygments/lexers/templates.py` |
| io | 1349 | 180 | 2 | `tests/examplefiles/tcsh/test.tcsh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 52 | 11 | 0 | `tests/examplefiles/cobol/example.cob` |
| time | 59 | 18 | 0 | `tests/examplefiles/rb/pleac.in.rb` |
| serialization | 77 | 5 | 0 | `tests/examplefiles/cobol/example.cob` |
| regex | 485 | 94 | 0 | `tests/examplefiles/tcsh/test.tcsh` |
| events | 163 | 48 | 0 | `pygments/lexers/lisp.py` |
| tests | 486 | 46 | 0 | `tests/test_tnt.py` |
| docs | 2032 | 390 | 3 | `tests/examplefiles/scheme/boot-9.scm` |
| debt | 879 | 132 | 0 | `tests/examplefiles/rb/pleac.in.rb` |
| mutation | 25726 | 612 | 36 | `tests/examplefiles/c/ceval.c` |
| dead_code | 1268 | 194 | 1 | `pygments/styles/monokai.py` |
| credential | 12 | 7 | 0 | `tests/examplefiles/cobol/example.cob` |
| threat | 862 | 118 | 0 | `tests/examplefiles/c/ceval.c` |
| ml_ai | 117 | 28 | 0 | `tests/examplefiles/rb/pleac.in.rb` |
| ui | 95 | 24 | 0 | `tests/examplefiles/html/example.xhtml` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/examplefiles/tcsh/test.tcsh` (Hits: 262)
- `tests/examplefiles/html/example.xhtml` (Hits: 99)
- `tests/examplefiles/fish/example.fish` (Hits: 46)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **token.py** (`pygments/token.py`) — 294 inbound connections
2. **lexer.py** (`pygments/lexer.py`) — 227 inbound connections
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

- `PyEval_EvalFrameEx` **(Many-Argument Workhorses)** (@ `tests/examplefiles/c/ceval.c`) -> Impact: **901.3** | LOC: 2092
- `ASBeautifier::beautify` **(Compute Cores)** (@ `tests/examplefiles/cpp/example.cpp`) -> Impact: **605.1** | LOC: 1155
  * *Intent:* /** * beautify a line of source code. * every line of source code in a source code file should be sent * one after the other to the beautify method. *...
- `psb_zbaseprc_aply` **(Many-Argument Workhorses)** (@ `tests/examplefiles/fortran/zmlrpc.f90`) -> Impact: **380.4** | LOC: 651
- `make-hash-table` **(Compute Cores)** (@ `tests/examplefiles/scheme/boot-9.scm`) -> Impact: **273.3** | LOC: 1195
  * *Intent:* ;;; {Trivial Functions}
- `get_tokens_unprocessed` **(Compute Cores)** (@ `pygments/lexers/pascal.py`) -> Impact: **224.2** | LOC: 223
- `main_inner` **(Many-Argument Workhorses)** (@ `pygments/cmdline.py`) -> Impact: **170.8** | LOC: 333
- `inspect` **(Compute Cores)** (@ `tests/examplefiles/rb/example.rb`) -> Impact: **161.4** | LOC: 767
  * *Intent:* # Returns a string containing a human-readable representation of the # set. ("#<Set: {element1, element2, ...}>")
- `AHCON` **(Many-Argument Workhorses)** (@ `tests/examplefiles/fortranfixed/ahcon.f`) -> Impact: **119.8** | LOC: 339
- `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (@ `tests/examplefiles/tcsh/test.tcsh`) -> Impact: **119.1** | LOC: 788
  * *Intent:* # for traditional completion of zcat command # traditional_nm_complete # for traditional completion of nm command # traditilnal_tex_complete # for tra...
- `get_tokens_unprocessed` **(Many-Argument Workhorses)** (@ `pygments/lexers/data.py`) -> Impact: **112.0** | LOC: 230
  * *Intent:* """Parse JSON data."""

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pygments/lexers` | 242 | 21744.44 | 15.01% | 8.75% |
| `tests/examplefiles/tads3` | 1 | 7880.24 | 7.99% | 0.0% |
| `tests/examplefiles/asc` | 1 | 5000.0 | 0.0% | 0.0% |
| `tests/examplefiles/sml` | 1 | 5000.0 | 0.0% | 0.0% |
| `tests/examplefiles/c` | 4 | 3543.82 | 20.92% | 0.0% |
| `pygments` | 15 | 2916.96 | 36.42% | 3.84% |
| `pygments/formatters` | 12 | 2544.52 | 48.49% | 32.06% |
| `tests` | 33 | 2419.14 | 13.89% | 0.0% |
| `tests/examplefiles/rb` | 7 | 2316.18 | 20.68% | 0.0% |
| `tests/examplefiles/lhs` | 2 | 1945.92 | 3.66% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `external/moin-parser.py` -> **99.9996%** Exposure
- `pygments/lexers/inferno.py` -> **99.9533%** Exposure
- `external/autopygmentize` -> **99.5095%** Exposure
- `external/markdown-processor.py` -> **92.4142%** Exposure
- `pygments/formatters/pangomarkup.py` -> **92.4142%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doc/_static/demo-worker.js` -> **100.0%** Exposure
- `doc/_static/demo.js` -> **100.0%** Exposure
- `external/moin-parser.py` -> **100.0%** Exposure
- `pygments/cmdline.py` -> **100.0%** Exposure
- `pygments/console.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/examplefiles/cobol/example.cob` -> **49** Orphaned Functions | **5** Duplicates
- `tests/examplefiles/c/example.c` -> **51** Orphaned Functions | **0** Duplicates
- `tests/examplefiles/cpp/example.cpp` -> **36** Orphaned Functions | **0** Duplicates
- `tests/examplefiles/rb/pleac.in.rb` -> **28** Orphaned Functions | **0** Duplicates
- `tests/test_rtf_formatter.py` -> **26** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/examplefiles/cobol/example.cob` -> **93.3829%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1477` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `doc/_static/demo-worker.js` (JAVASCRIPT) -> Cumulative Risk: **657.04**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +2.79)
- **Magnitude:** 114.08 | **LOC:** 76 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `onmessage` (Compute Cores, Impact: 24.3), `loadPyodideAndPygments` (Interface Declarations, Impact: 2.5)

### 2. `pygments/lexers/haskell.py` (PYTHON) -> Cumulative Risk: **635.14**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z -0.15)
- **Magnitude:** 259.98 | **LOC:** 868 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9889%), Safety Score (84.6208%)
- **Heaviest Functions:** `get_tokens_unprocessed` (Compute Cores, Impact: 36.8), `get_tokens_unprocessed` (Compute Cores, Impact: 9.1), `__init__` (Parameter Forwarders, Impact: 2.1)

### 3. `pygments/style.py` (PYTHON) -> Cumulative Risk: **632.19**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.72)
- **Magnitude:** 236.06 | **LOC:** 204 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.7699%)
- **Heaviest Functions:** `__new__` (Many-Argument Workhorses, Impact: 74.8), `style_for_token` (Compute Cores, Impact: 20.5), `colorformat` (Defensive Guards, Impact: 12.0)

### 4. `pygments/lexers/pascal.py` (PYTHON) -> Cumulative Risk: **629.77**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.88)
- **Magnitude:** 576.08 | **LOC:** 645 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.5732%)
- **Heaviest Functions:** `get_tokens_unprocessed` (Compute Cores, Impact: 224.2), `__init__` (Compute Cores, Impact: 13.1), `__init__` (Parameter Forwarders, Impact: 1.9)

### 5. `pygments/lexers/mime.py` (PYTHON) -> Cumulative Risk: **626.34**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.01)
- **Magnitude:** 237.02 | **LOC:** 211 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.3587%)
- **Heaviest Functions:** `get_content_type_subtokens` (Compute Cores, Impact: 30.0), `get_body_tokens` (Compute Cores, Impact: 24.9), `get_header_tokens` (Compute Cores, Impact: 23.2)

### 6. `doc/_static/demo.js` (JAVASCRIPT) -> Cumulative Risk: **624.47**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.34)
- **Magnitude:** 191.1 | **LOC:** 201 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9998%)
- **Heaviest Functions:** `onmessage` (Compute Cores, Impact: 18.9), `highlight` (Compute Cores, Impact: 13.1), `updateCopyLink` (I/O & Config Routines, Impact: 5.0)

### 7. `pygments/lexers/webmisc.py` (PYTHON) -> Cumulative Risk: **619.15**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.18)
- **Magnitude:** 781.9 | **LOC:** 1007 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (93.8308%)
- **Heaviest Functions:** `popstate_kindtest_callback` (Compute Cores, Impact: 30.7), `popstate_callback` (Compute Cores, Impact: 18.8), `pushstate_operator_order_callback` (Compute Cores, Impact: 18.4)

### 8. `pygments/formatters/terminal256.py` (PYTHON) -> Cumulative Risk: **607.03**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.16)
- **Magnitude:** 391.32 | **LOC:** 339 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.8687%)
- **Heaviest Functions:** `format_unencoded` (Many-Argument Workhorses, Impact: 25.9), `_setup_styles` (Compute Cores, Impact: 18.0), `color_string` (Compute Cores, Impact: 16.8)

### 9. `pygments/formatters/groff.py` (PYTHON) -> Cumulative Risk: **606.84**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.73)
- **Magnitude:** 176.52 | **LOC:** 171 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.1362%)
- **Heaviest Functions:** `format_unencoded` (Many-Argument Workhorses, Impact: 27.6), `_make_styles` (Compute Cores, Impact: 18.0), `_wrap_line` (Compute Cores, Impact: 14.9)

### 10. `pygments/lexers/textfmts.py` (PYTHON) -> Cumulative Risk: **603.31**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.63)
- **Magnitude:** 208.42 | **LOC:** 437 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Safety Score (87.6547%), Documentation (87.5%)
- **Heaviest Functions:** `header_callback` (Compute Cores, Impact: 31.8), `content_callback` (Defensive Guards, Impact: 16.8), `continuous_header_callback` (Compute Cores, Impact: 14.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/examplefiles/tads3/tads3_example.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7880.24 | **LOC:** 1249 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9906%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 75`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `dead_code: 2`
* *Architecture:* `io: 5`, `import: 7`
* *Defense:* `safety: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` big, doubt, handles, it, the, this, water
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/asc/id_ecdsa` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/sml/intsyn.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/c/ceval.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2385.54 | **LOC:** 2605 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.0299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyEval_EvalFrameEx` **(Many-Argument Workhorses)** (Impact: 901.3)
  * `Py_MakePendingCalls` **(I/O & Config Routines)** (Impact: 8.6)
  * `dump_tsc` **(Many-Argument Workhorses)** (Impact: 6.7)
    * *Intent:* #endif
  * `Py_AddPendingCall` **(Compute Cores)** (Impact: 6.5)
  * `_Py_CheckRecursiveCall` **(Compute Cores)** (Impact: 5.3)
    * *Intent:* Without USE_STACKCHECK, there is no need for this. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 442 instances
* *State Mutation (weighted view):* 1352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 487`, `structural_boundaries: 245`, `args: 119`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 468`, `dead_code: 2`, `fragile_debt: 17`, `unreferenced_by_name: 12`
* *Architecture:* `api: 23`, `import: 9`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Python.h, code.h, ctype.h, errno.h, eval.h, frameobject.h, opcode.h, pythread.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/lhs/DancingSudoku.lhs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1863.12 | **LOC:** 412 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1288%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 141`, `args: 35`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 50`, `high_risk_execution: 3`, `state_mutation: 11`
* *Architecture:* `io: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/cpp/example.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1735.68 | **LOC:** 2364 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.4832%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ASBeautifier::beautify` **(Compute Cores)** (Impact: 605.1)
    * *Intent:* /** * beautify a line of source code. * every line of source code in a source code file should be se...
  * `ASBeautifier::findHeader` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* /** * check if a specific line position contains a header, out of several possible headers. * * @ret...
  * `ASBeautifier::getNextProgramCharDistance` **(Compute Cores)** (Impact: 26.1)
    * *Intent:* /** * get distance to the next non-white sspace, non-comment character in the line. * if no such cha...
  * `ASBeautifier::registerInStatementIndent` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* /** * register an in-statement indent. */
  * `ASBeautifier::isLegalNameChar` **(Compute Cores)** (Impact: 10.1)
    * *Intent:* /** * check if a specific character can be used in a legal variable/method/class name * * @return le...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 232 instances
* *State Mutation (weighted view):* 910
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 449`, `structural_boundaries: 94`, `args: 44`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 446`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 36`
* *Architecture:* `api: 2`, `import: 27`
* *Defense:* `doc: 44`, `immutability_locks: 74`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ASBeautifier.h, ASFormatter.h, ASResource.h, ASSourceIterator.h, algorithm, ansigenerator.h, cctype, charcodes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/rb/example.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1165.58 | **LOC:** 1853 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.9437%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `inspect` **(Compute Cores)** (Impact: 161.4)
    * *Intent:* # Returns a string containing a human-readable representation of the # set. ("#<Set: {element1, elem...
  * `next_token` **(Compute Cores)** (Impact: 109.5)
  * `getReasonPhrase` **(Compute Cores)** (Impact: 65.2)
    * *Intent:* # {{{ if status == 100 "Continue" elsif status == 101 "Switching Protocols" elsif status == 200 "OK"...
  * `initialize` **(Compute Cores)** (Impact: 26.5)
    * *Intent:* # Creates a new set containing the elements of the given enumerable # object. # # If a block is give...
  * `getHttpHeader` **(I/O & Config Routines)** (Impact: 16.4)
    * *Intent:* # Returns a HTTP header (type String) with all cookies. Rweb does this for # you. # {{{ if defined?(...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 169 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 548
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 222`, `args: 51`, `func_start: 90`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 210`, `dead_code: 16`, `planned_debt: 1`, `unreferenced_by_name: 21`
* *Architecture:* `io: 4`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 6`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Enumerable, TSort, rbtree, rweb, rwebcookie, set, strscan, tsort
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/c/example.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1134.16 | **LOC:** 2081 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.6544%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rb_ary_splice` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `rb_ary_initialize` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* * a[1]['cat'] = 'Felix' * a * * # here multiple copies are created * a = Array.new(2) { Hash.new } *...
  * `rb_ary_join` **(Compute Cores)** (Impact: 30.0)
  * `rb_get_values_at` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `rb_ary_aref` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* * a[2] + a[0] + a[1] #=> "cab" * a[6] #=> nil * a[1, 2] #=> [ "b", "c" ] * a[1..3] #=> [ "b", "c", "...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 465
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 159`, `args: 60`, `func_start: 89`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 175`, `unreferenced_by_name: 51`
* *Architecture:* `api: 43`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` codegen.h, node.h, ruby.h, st.h, stdarg.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/rb/pleac.in.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1055.86 | **LOC:** 1224 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.1214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `factorize` **(Compute Cores)** (Impact: 92.5)
    * *Intent:* # dunno if an equivalent to Lingua::EN::Inflect exists... # @@PLEAC@@_2.19 #------------------------...
  * `printfactorhash` **(Many-Argument Workhorses)** (Impact: 47.5)
    * *Intent:* # For chaining comparisons, you may use Numeric#nonzero?, which # returns num if num is not zero, ni...
  * `from_roman` **(Compute Cores)** (Impact: 34.2)
  * `what_about_that_array` **(Compute Cores)** (Impact: 33.1)
  * `pop2` **(I/O & Config Routines)** (Impact: 32.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 139 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 553
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 52`, `args: 31`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 11`, `state_mutation: 275`, `dead_code: 4`, `unreferenced_by_name: 28`
* *Architecture:* `io: 6`, `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Soundex, complex.rb, matrix.rb, mersenne_twister, online, rational.rb, the, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/cobol/example.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1022.9 | **LOC:** 2621 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5576%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `202-Show-And-Change-Switches` **(Compute Cores)** (Impact: 45.9)
  * `032-Process` **(I/O & Config Routines)** (Impact: 33.5)
  * `232-Build-Command` **(I/O & Config Routines)** (Impact: 19.1)
    * *Intent:* ***************************************************************** ** Run the compiled program ** ***...
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 16.0)
  * `213-Run-Compiler` **(I/O & Config Routines)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 647
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 198`, `args: 16`, `func_start: 76`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 245`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 49`
* *Architecture:* `io: 18`, `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FileStat-Msgs, screenio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/lexers/templates.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1012.04 | **LOC:** 2356 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.1222%), Tech Debt (64.1422%)
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* """ Since ERB doesn't allow "<%" and other tags inside of ruby blocks we have to use a split approac...
  * `analyse_text` **(Compute Cores)** (Impact: 10.4)
  * `analyse_text` **(Compute Cores)** (Impact: 9.1)
  * `analyse_text` **(Compute Cores)** (Impact: 7.5)
  * `analyse_text` **(Compute Cores)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 239`, `args: 89`, `func_start: 89`, `class_start: 69`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 438`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 109`, `import: 14`
* *Defense:* `safety: 4`, `doc: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.764
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000688
  * `Imports (Out-Degree: 13):` pygments.lexer, pygments.lexers.css, pygments.lexers.data, pygments.lexers.html, pygments.lexers.javascript, pygments.lexers.jvm, pygments.lexers.perl, pygments.lexers.php...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 967.72 | **LOC:** 964 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (41.2553%), Tech Debt (16.1855%)
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 53.2)
    * *Intent:* """ Split ``text`` into (tokentype, text) pairs. If ``context`` is given, use this lexer context ins...
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* """ Split ``text`` into (tokentype, text) pairs. ``stack`` is the initial stack (default: ``['root']...
  * `using` **(Compute Cores)** (Impact: 37.1)
    * *Intent:* """ Callback that processes the match with a different lexer. The keyword arguments are forwarded to...
  * `callback` **(Compute Cores)** (Impact: 37.0)
  * `_preprocess_lexer_input` **(Compute Cores)** (Impact: 31.7)
    * *Intent:* """Apply preprocessing such as decoding the input, removing BOM and normalizing newlines."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 166`, `args: 45`, `func_start: 43`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 170`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 39`, `import: 9`
* *Defense:* `safety: 45`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 51.597
  * `Choke Point (Betweenness):` 0.000333 | `Ripple Effect (Closeness):` 0.156532
  * `Imports (Out-Degree: 4):` chardet, pygments.filter, pygments.filters, pygments.regexopt, pygments.token, pygments.util, re, sys...
  * `Imported By (In-Degree: 227):` (Excluded from Brief to save tokens)

### `pygments/lexers/webmisc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 781.9 | **LOC:** 1007 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.5677%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `popstate_kindtest_callback` **(Compute Cores)** (Impact: 30.7)
  * `popstate_callback` **(Compute Cores)** (Impact: 18.8)
  * `pushstate_operator_order_callback` **(Compute Cores)** (Impact: 18.4)
  * `pushstate_operator_map_callback` **(Compute Cores)** (Impact: 18.4)
  * `pushstate_operator_root_validate` **(Compute Cores)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 67`, `args: 28`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 153`, `dead_code: 1`
* *Architecture:* `api: 34`, `import: 7`
* *Defense:* `safety: 3`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001239
  * `Imports (Out-Degree: 6):` pygments.lexer, pygments.lexers.css, pygments.lexers.html, pygments.lexers.javascript, pygments.lexers.ruby, pygments.token, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/data.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 730.36 | **LOC:** 764 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.6114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 112.0)
    * *Intent:* """Parse JSON data."""
  * `callback` **(Compute Cores)** (Impact: 26.9)
  * `save_indent` **(Compute Cores)** (Impact: 23.6)
    * *Intent:* """Save a possible indentation level."""
  * `callback` **(Compute Cores)** (Impact: 22.6)
  * `callback` **(Compute Cores)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 61`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 133`
* *Architecture:* `api: 26`, `import: 2`
* *Defense:* `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.932
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004626
  * `Imports (Out-Degree: 2):` pygments.lexer, pygments.token
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/examplefiles/fortran/zmlrpc.f90` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 653.3 | **LOC:** 799 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.3667%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `psb_zbaseprc_aply` **(Many-Argument Workhorses)** (Impact: 380.4)
  * `mlprec_wrk_free` **(Defensive Guards)** (Impact: 12.3)
  * `psb_zmlprc_aply` **(Many-Argument Workhorses)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 73 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 39`, `args: 20`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 93`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 3`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 23`, `immutability_locks: 7`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` psb_const_mod, psb_descriptor_type, psb_error_mod, psb_penv_mod, psb_prec_type, psb_psblas_mod, psb_serial_mod
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/cmdline.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 636.18 | **LOC:** 669 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.2363%), Tech Debt (13.5098%)
**Top Internal Functions/Classes:**
  * `main_inner` **(Many-Argument Workhorses)** (Impact: 170.8)
  * `main` **(Compute Cores)** (Impact: 56.5)
    * *Intent:* """ Main command line entry point. """
  * `_print_list` **(Compute Cores)** (Impact: 23.7)
  * `_print_list_as_json` **(Compute Cores)** (Impact: 14.9)
  * `_parse_options` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 126`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 112`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 45`, `api: 5`, `import: 18`
* *Defense:* `safety: 39`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.001376
  * `Imports (Out-Degree: 7):` and, argparse, colorama.initialise, json, os, pygments, pygments.filters, pygments.formatters...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pygments/lexers/lisp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 629.92 | **LOC:** 3153 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.5834%), Tech Debt (9.2973%)
**Top Internal Functions/Classes:**
  * `_process_declaration` **(Compute Cores)** (Impact: 53.9)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 18.6)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 16.7)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* # Recognizing builtins.
  * `_process_declarations` **(Compute Cores)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 84 instances
* *High Risk Execution (weighted view):* 26
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 301`, `args: 21`, `func_start: 14`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 27`, `state_mutation: 219`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 26`, `api: 20`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 15`, `doc: 26`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.847
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.002252
  * `Imports (Out-Degree: 4):` pygments.lexer, pygments.lexers._cl_builtins, pygments.lexers._scheme_builtins, pygments.lexers.python, pygments.token, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pygments/lexers/robotframework.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 628.9 | **LOC:** 552 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.7104%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_tokenize` **(Compute Cores)** (Impact: 22.8)
  * `_tokenize` **(Compute Cores)** (Impact: 16.7)
  * `_tokenize` **(Many-Argument Workhorses)** (Impact: 13.7)
  * `_variable_state` **(Compute Cores)** (Impact: 12.5)
  * `tokenize` **(Compute Cores)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 149`, `args: 60`, `func_start: 60`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 135`
* *Architecture:* `api: 35`, `import: 3`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.557
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000688
  * `Imports (Out-Degree: 2):` pygments.lexer, pygments.token, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/pascal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 576.08 | **LOC:** 645 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.9903%), Tech Debt (10.5365%)
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 224.2)
  * `__init__` **(Compute Cores)** (Impact: 13.1)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.9)
  * `get_tokens_unprocessed` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 125`, `dead_code: 5`, `fragile_debt: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.558
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000688
  * `Imports (Out-Degree: 5):` pygments.lexer, pygments.lexers.modula2, pygments.scanner, pygments.token, pygments.util, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/markup.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 562.98 | **LOC:** 1660 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.7445%), Tech Debt (30.9166%)
**Top Internal Functions/Classes:**
  * `_handle_sourcecode` **(Compute Cores)** (Impact: 48.7)
  * `_handle_codeblock` **(Defensive Guards)** (Impact: 39.4)
  * `_handle_codeblock` **(Defensive Guards)** (Impact: 27.4)
    * *Intent:* """ match args: 1:backticks, 2:lang_name, 3:newline, 4:code, 5:backticks """
  * `handle_score` **(Compute Cores)** (Impact: 25.4)
  * `handle_syntaxhighlight` **(Many-Argument Workhorses)** (Impact: 23.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 97`, `args: 20`, `func_start: 20`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 160`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 24`, `import: 14`
* *Defense:* `safety: 10`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.755
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.001549
  * `Imports (Out-Degree: 8):` pygments.lexer, pygments.lexers, pygments.lexers.css, pygments.lexers.data, pygments.lexers.html, pygments.lexers.javascript, pygments.lexers.lilypond, pygments.token...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pygments/formatters/img.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 538.56 | **LOC:** 687 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.8318%), Tech Debt (9.6018%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `_create_mac` **(Compute Cores)** (Impact: 21.2)
  * `get_font` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* """ Get the font based on bold and italic flags. """
  * `__init__` **(Many-Argument Workhorses)** (Impact: 18.3)
    * *Intent:* """ See the class docstring for explanation of options. """
  * `format` **(Many-Argument Workhorses)** (Impact: 15.8)
    * *Intent:* """ Format ``tokensource``, an iterable of ``(tokentype, tokenstring)`` tuples and write it into ``o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 286
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 93`, `args: 29`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 126`, `planned_debt: 1`
* *Architecture:* `io: 9`, `api: 15`, `import: 8`
* *Defense:* `safety: 21`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.627
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000688
  * `Imports (Out-Degree: 2):` PIL, _winreg, os, pygments.formatter, pygments.util, subprocess, sys, winreg
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/shell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 537.9 | **LOC:** 903 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (50.3666%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_make_begin_state` **(Many-Argument Workhorses)** (Impact: 93.4)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 41.1)
  * `_make_label_state` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `_make_follow_state` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 58 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 62`, `args: 10`, `func_start: 10`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 8`, `state_mutation: 161`
* *Architecture:* `io: 2`, `api: 17`, `import: 4`
* *Defense:* `safety: 3`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.847
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002202
  * `Imports (Out-Degree: 3):` hide, pygments.lexer, pygments.token, pygments.util, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pygments/lexers/scripting.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 503.76 | **LOC:** 1639 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (28.8461%), Tech Debt (9.0097%)
**Top Internal Functions/Classes:**
  * `analyse_text` **(Compute Cores)** (Impact: 49.3)
    * *Intent:* """ Perform a structural analysis for basic Easytrieve constructs. """
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 19.0)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 11.0)
  * `__init__` **(Compute Cores)** (Impact: 7.9)
  * `analyse_text` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """ Check for initial comment and patterns that distinguish Rexx from other C-like languages. """
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 133`, `args: 15`, `func_start: 15`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 196`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 23`, `import: 8`
* *Defense:* `safety: 8`, `doc: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002065
  * `Imports (Out-Degree: 4):` pygments.lexer, pygments.lexers._lua_builtins, pygments.lexers._luau_builtins, pygments.token, pygments.util, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pygments/lexers/sql.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 479.94 | **LOC:** 1112 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (43.9569%), Tech Debt (20.5973%)
**Top Internal Functions/Classes:**
  * `language_callback` **(Compute Cores)** (Impact: 55.4)
    * *Intent:* """Parse the content of a $-string using a lexer The lexer is chosen looking for a nearby LANGUAGE o...
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 37.6)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 23.9)
  * `_get_lexer` **(Defensive Guards)** (Impact: 14.9)
  * `analyse_text` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 272
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 71`, `args: 13`, `func_start: 13`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 148`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 23`, `import: 10`
* *Defense:* `safety: 3`, `doc: 21`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.214
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.003539
  * `Imports (Out-Degree: 2):` collections, pygments.lexer, pygments.lexers, pygments.token, re
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pygments/lexers/modula2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 453.54 | **LOC:** 1580 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.1215%), Tech Debt (8.467%)
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 88.6)
    * *Intent:* # intercept the token stream, modify token attributes and return them
  * `set_dialect` **(Many-Argument Workhorses)** (Impact: 26.7)
    * *Intent:* # Set lexer to a specified dialect # # if __debug__: # print 'entered set_dialect with arg: ', diale...
  * `get_dialect_from_dialect_tag` **(Compute Cores)** (Impact: 16.2)
    * *Intent:* # print ' self.reserved_words: ', self.reserved_words # print ' self.builtins: ', self.builtins # pr...
  * `__init__` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* # M e t h o d s # initialise a lexer instance # # check dialect options # dialects = get_list_opt(op...
  * `analyse_text` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* """It's Pascal-like, but does not use FUNCTION -- uses PROCEDURE instead."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 20`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `dead_code: 8`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `doc: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.631
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000918
  * `Imports (Out-Degree: 3):` pygments.lexer, pygments.token, pygments.util, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pygments/lexers/templates.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 1012.04
- `pygments/lexers/webmisc.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 781.9
- `pygments/cmdline.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 636.18
- `pygments/lexers/lisp.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 629.92
- `pygments/lexers/robotframework.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 628.9

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pygments/lexer.py` -> **Severity: 0.033** (Bridge: 0.0003 * Flux: 100.0%)
- `pygments/lexers/html.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.4357%)
- `pygments/cmdline.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `pygments/formatter.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `pygments/formatters/latex.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pygments/token.py` -> **Severity: 17.904** (Embedded: 0.202 * Error Risk: 88.6135%)
- `pygments/lexer.py` -> **Severity: 15.476** (Embedded: 0.1565 * Error Risk: 98.871%)
- `pygments/util.py` -> **Severity: 9.405** (Embedded: 0.1008 * Error Risk: 93.2787%)
- `pygments/regexopt.py` -> **Severity: 8.182** (Embedded: 0.0831 * Error Risk: 98.4327%)
- `pygments/filter.py` -> **Severity: 5.528** (Embedded: 0.0831 * Error Risk: 66.5013%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pygments/token.py` -> **Severity: 6759.545** (Blast Radius: 88.719 * Doc Risk: 76.1905%)
- `pygments/lexer.py` -> **Severity: 2851.415** (Blast Radius: 51.597 * Doc Risk: 55.2632%)
- `pygments/style.py` -> **Severity: 1226.7** (Blast Radius: 12.267 * Doc Risk: 100.0%)
- `pygments/filter.py` -> **Severity: 678.3** (Blast Radius: 11.628 * Doc Risk: 58.3333%)
- `pygments/util.py` -> **Severity: 536.976** (Blast Radius: 22.553 * Doc Risk: 23.8095%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
