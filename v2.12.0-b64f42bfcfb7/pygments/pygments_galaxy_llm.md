# ARCHITECTURAL_BRIEF: pygments
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pygments/pygments.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1469 analyzed artifact(s), 104748 LOC.
- **Load-bearing artifact:** `pygments/token.py` -- 295 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/examplefiles/rust/eval.rs` -- pulls in 37 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/examplefiles/tads3/tads3_example.t` at magnitude 7880.24 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 2708 |
| Analyzed Artifacts (Scanned) | 1469 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1239 |
| Total LOC | 104748 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 54.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3898 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4787 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8602 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 26 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 783 | 2 | 53.3% |
| PYTHON | 378 | 77298 | 25.7% |
| HTML | 141 | 1584 | 9.6% |
| SCALA | 26 | 433 | 1.8% |
| JAVASCRIPT | 10 | 452 | 0.7% |
| PERL | 9 | 2072 | 0.6% |
| MAKEFILE | 7 | 1785 | 0.5% |
| RUBY | 7 | 2191 | 0.5% |
| CPP | 6 | 1700 | 0.4% |
| LUA | 6 | 448 | 0.4% |
| SHELL | 5 | 1184 | 0.3% |
| SCHEME | 5 | 1670 | 0.3% |
| C | 5 | 3596 | 0.3% |
| HASKELL | 5 | 1129 | 0.3% |
| JAVA | 5 | 482 | 0.3% |
| YAML | 4 | 352 | 0.3% |
| CSS | 4 | 122 | 0.3% |
| ASSEMBLY | 4 | 249 | 0.3% |
| GROOVY | 4 | 95 | 0.3% |
| JSON | 3 | 58 | 0.2% |
| ADA | 3 | 230 | 0.2% |
| FORTRAN | 3 | 588 | 0.2% |
| GLSL | 3 | 94 | 0.2% |
| PHP | 3 | 294 | 0.2% |
| BATCH | 2 | 347 | 0.1% |
| M4 | 2 | 11 | 0.1% |
| CSHARP | 2 | 249 | 0.1% |
| EASYTRIEVE | 2 | 32 | 0.1% |
| REXX | 2 | 66 | 0.1% |
| GO | 2 | 25 | 0.1% |
| MATLAB | 2 | 22 | 0.1% |
| POWERSHELL | 2 | 97 | 0.1% |
| SQLITE | 2 | 59 | 0.1% |
| TYPESCRIPT | 2 | 38 | 0.1% |
| DOCKERFILE | 1 | 9 | 0.1% |
| COBOL | 1 | 2071 | 0.1% |
| BLP | 1 | 28 | 0.1% |
| CRYSTAL | 1 | 1771 | 0.1% |
| CSD | 1 | 15 | 0.1% |
| DART | 1 | 17 | 0.1% |
| ELIXIR | 1 | 164 | 0.1% |
| FSHARP | 1 | 508 | 0.1% |
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

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1465 |
| unknown | unknown | 2 |
| utf-8 | bom | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 66%, Declarative / Non-Code 16%, Compute Cores Files 5%, Large Core Modules (3) 3%, Parameter Forwarders Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 684 | 46.6% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 782 | 53.2% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1239*

**Composition by Extension & Reason:**
- `.output`: 662x Excluded (Unsupported Extension: '.output'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 30x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.dylan-console')
- `.rst`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.rst')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 24 LOC), 1x Excluded (Machine-Generated Source Code Signature: 996 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1645 LOC)
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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.9 | 2.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.8 | 38.1 | 52.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.9 | 8.4 | 4.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 34.4 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.2 | 0.8 | 1.6 | 1.6 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 54.0 | 8.3 | 13.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 482 | 94 | 0 | `tests/examplefiles/cpp/example.cpp` |
| cleanup | 99 | 29 | 0 | `tests/examplefiles/make/Makefile` |
| guards | 1993 | 222 | 2 | `tests/examplefiles/cpp/functions.cpp` |
| danger | 1527 | 230 | 2 | `tests/examplefiles/fish/example.fish` |
| concurrency | 767 | 128 | 0 | `pygments/lexers/webmisc.py` |
| connectivity | 2532 | 419 | 4 | `pygments/lexers/templates.py` |
| io | 1361 | 188 | 2 | `tests/examplefiles/tcsh/test.tcsh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 43 | 13 | 0 | `tests/examplefiles/cobol/example.cob` |
| time | 61 | 20 | 0 | `tests/examplefiles/rb/pleac.in.rb` |
| serialization | 40 | 5 | 0 | `tests/examplefiles/cobol/example.cob` |
| regex | 484 | 96 | 0 | `tests/examplefiles/tcsh/test.tcsh` |
| events | 165 | 50 | 0 | `pygments/lexers/lisp.py` |
| tests | 486 | 46 | 0 | `tests/test_tnt.py` |
| docs | 2040 | 393 | 3 | `tests/examplefiles/scheme/boot-9.scm` |
| debt | 983 | 139 | 0 | `tests/examplefiles/cr/test.cr` |
| mutation | 26728 | 622 | 36 | `tests/examplefiles/c/ceval.c` |
| dead_code | 853 | 172 | 1 | `tests/examplefiles/cpp/example.cpp` |
| credential | 6 | 6 | 0 | `pygments/lexers/apl.py` |
| threat | 27 | 9 | 0 | `tests/examplefiles/php/test.php` |
| ml_ai | 106 | 19 | 0 | `tests/examplefiles/rb/pleac.in.rb` |
| ui | 96 | 25 | 0 | `tests/examplefiles/html/example.xhtml` |

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

1. **token.py** (`pygments/token.py`) — 295 inbound connections
2. **lexer.py** (`pygments/lexer.py`) — 233 inbound connections
3. **style.py** (`pygments/style.py`) — 52 inbound connections
4. **util.py** (`pygments/util.py`) — 47 inbound connections
5. **__init__.py** (`pygments/lexers/__init__.py`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **eval.rs** (`tests/examplefiles/rust/eval.rs`) — 37 outbound dependencies
2. **other.py** (`pygments/lexers/other.py`) — 23 outbound dependencies
3. **compiled.py** (`pygments/lexers/compiled.py`) — 21 outbound dependencies
4. **AcidStateAdvanced.hs** (`tests/examplefiles/haskell/AcidStateAdvanced.hs`) — 21 outbound dependencies
5. **cmdline.py** (`pygments/cmdline.py`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `PyEval_EvalFrameEx` **(Many-Argument Workhorses)** (@ `tests/examplefiles/c/ceval.c`) -> Impact: **871.9** | LOC: 2092
- `ASBeautifier::beautify` **(Many-Argument Workhorses)** (@ `tests/examplefiles/cpp/example.cpp`) -> Impact: **600.8** | LOC: 1155
  * *Intent:* /** * beautify a line of source code. * every line of source code in a source code file should be sent * one after the other to the beautify method. *...
- `psb_zbaseprc_aply` **(Many-Argument Workhorses)** (@ `tests/examplefiles/fortran/zmlrpc.f90`) -> Impact: **380.4** | LOC: 651
- `make-hash-table` **(Compute Cores)** (@ `tests/examplefiles/scheme/boot-9.scm`) -> Impact: **273.3** | LOC: 1195
  * *Intent:* ;;; {Trivial Functions}
- `get_tokens_unprocessed` **(Many-Argument Workhorses)** (@ `pygments/lexers/pascal.py`) -> Impact: **224.2** | LOC: 223
- `main_inner` **(Many-Argument Workhorses)** (@ `pygments/cmdline.py`) -> Impact: **170.8** | LOC: 333
- `inspect` **(Compute Cores)** (@ `tests/examplefiles/rb/example.rb`) -> Impact: **161.4** | LOC: 767
  * *Intent:* # Returns a string containing a human-readable representation of the # set. ("#<Set: {element1, element2, ...}>")
- `factorize` **(Compute Cores)** (@ `tests/examplefiles/rb/pleac.in.rb`) -> Impact: **127.8** | LOC: 577
  * *Intent:* # dunno if an equivalent to Lingua::EN::Inflect exists... # @@PLEAC@@_2.19 #----------------------------- #!/usr/bin/ruby # bigfact - calculating prim...
- `next_token` **(Compute Cores)** (@ `tests/examplefiles/rb/example.rb`) -> Impact: **124.5** | LOC: 111
- `AHCON` **(Many-Argument Workhorses)** (@ `tests/examplefiles/fortranfixed/ahcon.f`) -> Impact: **119.8** | LOC: 340

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pygments/lexers` | 242 | 21654.48 | 15.0% | 6.67% |
| `tests/examplefiles/tads3` | 1 | 7880.24 | 7.99% | 0.0% |
| `tests/examplefiles/asc` | 1 | 5000.0 | 0.0% | 0.0% |
| `tests/examplefiles/sml` | 1 | 5000.0 | 0.0% | 0.0% |
| `tests/examplefiles/c` | 4 | 3482.42 | 20.85% | 0.0% |
| `pygments` | 15 | 2916.96 | 36.42% | 3.3% |
| `pygments/formatters` | 12 | 2544.52 | 48.49% | 26.24% |
| `tests` | 33 | 2421.84 | 13.89% | 0.0% |
| `tests/examplefiles/rb` | 7 | 2391.42 | 18.8% | 0.0% |
| `tests/examplefiles/lhs` | 2 | 1945.92 | 3.66% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `external/moin-parser.py` -> **99.9983%** Exposure
- `.github/workflows/build.yaml` -> **99.9976%** Exposure
- `pygments/lexers/inferno.py` -> **99.8338%** Exposure
- `external/autopygmentize` -> **98.7568%** Exposure
- `scripts/check_sources.py` -> **87.1217%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doc/_static/demo-worker.js` -> **100.0%** Exposure
- `doc/_static/demo.js` -> **100.0%** Exposure
- `doc/conf.py` -> **100.0%** Exposure
- `external/moin-parser.py` -> **100.0%** Exposure
- `pygments/cmdline.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/examplefiles/c/example.c` -> **51** Orphaned Functions | **0** Duplicates
- `tests/examplefiles/cr/test.cr` -> **8** Orphaned Functions | **41** Duplicates
- `tests/examplefiles/cobol/example.cob` -> **45** Orphaned Functions | **2** Duplicates
- `tests/examplefiles/cpp/example.cpp` -> **36** Orphaned Functions | **0** Duplicates
- `tests/examplefiles/rb/pleac.in.rb` -> **28** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1463` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/examplefiles/tads3/tads3_example.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.451)
- **Top Global Matches:** file_cluster_2: 4.451, file_cluster_13: 4.983, file_cluster_17: 6.104
- **Magnitude:** 7880.24 | **LOC:** 1249 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 75`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 5`, `import: 7`
* *Defense:* `safety: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` big, doubt, handles, it, the, this, water
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/asc/id_ecdsa` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/sml/intsyn.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/c/ceval.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.71)
- **Top Global Matches:** file_cluster_4: 6.71, file_cluster_15: 8.503, file_cluster_16: 9.021
- **Magnitude:** 2330.14 | **LOC:** 2605 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.1%), Complexity Load (formerly Cognitive Load) (49.0%), Connectivity (formerly Api Exposure) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyEval_EvalFrameEx` **(Many-Argument Workhorses)** (Impact: 871.9)
  * `Py_MakePendingCalls` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `dump_tsc` **(Many-Argument Workhorses)** (Impact: 6.7)
    * *Intent:* #endif
  * `Py_AddPendingCall` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `_Py_CheckRecursiveCall` **(Compute Cores)** (Impact: 5.3)
    * *Intent:* Without USE_STACKCHECK, there is no need for this. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 429 instances
* *State Mutation (weighted view):* 1326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 245`, `args: 119`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 468`, `fragile_debt: 17`, `unreferenced_by_name: 15`
* *Architecture:* `api: 23`, `import: 9`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Python.h, code.h, ctype.h, errno.h, eval.h, frameobject.h, opcode.h, pythread.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/lhs/DancingSudoku.lhs` (HASKELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.89)
- **Top Global Matches:** file_cluster_7: 4.89, file_cluster_14: 6.149, file_cluster_5: 8.849
- **Magnitude:** 1863.12 | **LOC:** 412 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (4.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 141`, `args: 35`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 50`, `high_risk_execution: 3`, `state_mutation: 11`
* *Architecture:* `io: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/cpp/example.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.174)
- **Top Global Matches:** file_cluster_15: 7.174, file_cluster_4: 8.597, file_cluster_16: 8.952
- **Magnitude:** 1731.38 | **LOC:** 2364 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (34.4%), Dead Code Surface (formerly Dead Code) (10.3%), Connectivity (formerly Api Exposure) (1.1%)
- **Documentation Coverage:** 30.9524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ASBeautifier::beautify` **(Many-Argument Workhorses)** (Impact: 600.8)
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
* *Structure:* `branch: 442`, `structural_boundaries: 94`, `args: 44`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 446`, `dead_code: 22`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 36`
* *Architecture:* `api: 2`, `import: 27`
* *Defense:* `doc: 44`, `immutability_locks: 74`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ASBeautifier.h, ASFormatter.h, ASResource.h, ASSourceIterator.h, algorithm, ansigenerator.h, cctype, charcodes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/rb/example.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.112)
- **Top Global Matches:** file_cluster_4: 7.112, file_cluster_12: 11.163, file_cluster_15: 11.606
- **Magnitude:** 1190.5 | **LOC:** 1853 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.5%), Complexity Load (formerly Cognitive Load) (46.1%), Concurrency Surface (formerly Concurrency) (16.4%), Dead Code Surface (formerly Dead Code) (8.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect` **(Compute Cores)** (Impact: 161.4)
    * *Intent:* # Returns a string containing a human-readable representation of the # set. ("#<Set: {element1, elem...
  * `next_token` **(Compute Cores)** (Impact: 124.5)
  * `getReasonPhrase` **(Compute Cores)** (Impact: 65.2)
    * *Intent:* # {{{ if status == 100 "Continue" elsif status == 101 "Switching Protocols" elsif status == 200 "OK"...
  * `initialize` **(Many-Argument Workhorses)** (Impact: 52.7)
    * *Intent:* # Sets a cookie. Please see below for details of the attributes. # {{{ # HTTP headers (Cookies are a...
  * `getHttpHeader` **(I/O & Config Routines)** (Impact: 20.4)
    * *Intent:* # Returns a HTTP header (type String) with all cookies. Rweb does this for # you. # {{{ if defined?(...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 164 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 538
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 439`, `structural_boundaries: 222`, `args: 51`, `func_start: 90`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 210`, `dead_code: 13`, `planned_debt: 1`, `unreferenced_by_name: 21`
* *Architecture:* `io: 4`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 6`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Enumerable, TSort, rbtree, set, strscan, tsort
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/c/example.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.708)
- **Top Global Matches:** file_cluster_16: 5.708, file_cluster_12: 7.123, file_cluster_15: 7.145
- **Magnitude:** 1128.16 | **LOC:** 2081 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.5%), Complexity Load (formerly Cognitive Load) (30.4%), Dead Code Surface (formerly Dead Code) (4.9%), Connectivity (formerly Api Exposure) (3.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rb_ary_splice` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `rb_ary_initialize` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* * a[1]['cat'] = 'Felix' * a * * # here multiple copies are created * a = Array.new(2) { Hash.new } *...
  * `rb_ary_join` **(Compute Cores)** (Impact: 30.0)
  * `rb_get_values_at` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `rb_ary_aref` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* * a[2] + a[0] + a[1] #=> "cab" * a[6] #=> nil * a[1, 2] #=> [ "b", "c" ] * a[1..3] #=> [ "b", "c", "...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 465
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 159`, `args: 60`, `func_start: 89`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 175`, `dead_code: 1`, `unreferenced_by_name: 51`
* *Architecture:* `api: 43`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` codegen.h, node.h, ruby.h, st.h, stdarg.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/rb/pleac.in.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.672)
- **Top Global Matches:** file_cluster_4: 7.672, file_cluster_15: 11.058, file_cluster_10: 11.695
- **Magnitude:** 1109.56 | **LOC:** 1224 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.3%), Complexity Load (formerly Cognitive Load) (45.3%), Dead Code Surface (formerly Dead Code) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `factorize` **(Compute Cores)** (Impact: 127.8)
    * *Intent:* # dunno if an equivalent to Lingua::EN::Inflect exists... # @@PLEAC@@_2.19 #------------------------...
  * `printfactorhash` **(Many-Argument Workhorses)** (Impact: 47.5)
    * *Intent:* # For chaining comparisons, you may use Numeric#nonzero?, which # returns num if num is not zero, ni...
  * `from_roman` **(I/O & Config Routines)** (Impact: 34.2)
  * `what_about_that_array` **(I/O & Config Routines)** (Impact: 33.1)
  * `pop2` **(I/O & Config Routines)** (Impact: 32.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 144 instances
* *State Mutation (weighted view):* 563
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 52`, `args: 31`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 11`, `state_mutation: 275`, `dead_code: 1`, `unreferenced_by_name: 28`
* *Architecture:* `io: 6`, `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Soundex, complex.rb, matrix.rb, mersenne_twister, online, rational.rb, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/examplefiles/cr/test.cr` (CRYSTAL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.414)
- **Top Global Matches:** file_cluster_15: 7.414, file_cluster_11: 7.547, file_cluster_10: 7.808
- **Magnitude:** 1017.02 | **LOC:** 2552 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.5%), Complexity Load (formerly Cognitive Load) (43.2%), Concurrency Surface (formerly Concurrency) (24.0%), Dead Code Surface (formerly Dead Code) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `paint` **(Compute Cores)** (Impact: 6.1)
  * `paint` **(Compute Cores)** (Impact: 6.1)
  * `define_method` **(Compute Cores)** (Impact: 5.6)
  * `fresh_vars_sample` **(Compute Cores)** (Impact: 4.8)
  * `elem_type` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 108 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 391`, `args: 107`, `func_start: 165`, `class_start: 113`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 243`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 41`, `unreferenced_by_name: 8`
* *Architecture:* `io: 1`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` server
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/lexers/templates.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.211)
- **Top Global Matches:** file_cluster_15: 5.211, file_cluster_16: 7.665, file_cluster_2: 7.757
- **Magnitude:** 1012.04 | **LOC:** 2356 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.732; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (68.9%), Guard Balance (formerly Safety Score) (68.1%), Debt Markers (formerly Tech Debt) (63.0%)
- **Documentation Coverage:** 96.875% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.00068
  * `Imports (Out-Degree: 13):` pygments.lexer, pygments.lexers.css, pygments.lexers.data, pygments.lexers.html, pygments.lexers.javascript, pygments.lexers.jvm, pygments.lexers.perl, pygments.lexers.php...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/examplefiles/cobol/example.cob` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.449)
- **Top Global Matches:** file_cluster_11: 7.449, file_cluster_15: 8.187, file_cluster_2: 8.337
- **Magnitude:** 980.62 | **LOC:** 2621 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (37.4%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `202-Show-And-Change-Switches` **(I/O & Config Routines)** (Impact: 45.9)
  * `032-Process` **(I/O & Config Routines)** (Impact: 33.5)
  * `232-Build-Command` **(I/O & Config Routines)** (Impact: 19.1)
    * *Intent:* ***************************************************************** ** Run the compiled program ** ***...
  * `213-Run-Compiler` **(I/O & Config Routines)** (Impact: 15.6)
  * `030-Scan-Compressed-Src` **(I/O & Config Routines)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 645
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 139`, `args: 16`, `func_start: 64`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 245`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 45`
* *Architecture:* `io: 9`, `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FileStat-Msgs, screenio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/lexer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.802)
- **Top Global Matches:** file_cluster_6: 8.802, file_cluster_4: 10.001, file_cluster_12: 15.25
- **Magnitude:** 967.72 | **LOC:** 964 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **233** in-repo importer(s); it depends on **9**; blast radius 50.329; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Connectivity (formerly Api Exposure) (80.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 55.2632% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 53.2)
    * *Intent:* """ Split ``text`` into (tokentype, text) pairs. If ``context`` is given, use this lexer context ins...
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* """ Split ``text`` into (tokentype, text) pairs. ``stack`` is the initial stack (default: ``['root']...
  * `using` **(Compute Cores)** (Impact: 37.1)
    * *Intent:* """ Callback that processes the match with a different lexer. The keyword arguments are forwarded to...
  * `callback` **(Compute Cores)** (Impact: 37.0)
  * `_preprocess_lexer_input` **(Stateful Encapsulated Methods)** (Impact: 31.7)
    * *Intent:* """Apply preprocessing such as decoding the input, removing BOM and normalizing newlines."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 166`, `args: 45`, `func_start: 43`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 170`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 39`, `import: 9`
* *Defense:* `safety: 45`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.329
  * `Choke Point (Betweenness):` 0.000565 | `Ripple Effect (Closeness):` 0.160719
  * `Imports (Out-Degree: 5):` chardet, pygments.filter, pygments.filters, pygments.regexopt, pygments.token, pygments.util, re, sys...
  * `Imported By (In-Degree: 233):` (Excluded from Brief to save tokens)

### `pygments/lexers/webmisc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.736)
- **Top Global Matches:** file_cluster_9: 6.736, file_cluster_15: 7.535, file_cluster_16: 8.218
- **Magnitude:** 781.9 | **LOC:** 1007 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.607; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (66.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 153`
* *Architecture:* `api: 34`, `import: 7`
* *Defense:* `safety: 3`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.607
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001224
  * `Imports (Out-Degree: 6):` pygments.lexer, pygments.lexers.css, pygments.lexers.html, pygments.lexers.javascript, pygments.lexers.ruby, pygments.token, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/data.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.351)
- **Top Global Matches:** file_cluster_4: 9.351, file_cluster_9: 9.638, file_cluster_12: 10.854
- **Magnitude:** 730.36 | **LOC:** 764 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 0.88; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.4%)
- **Documentation Coverage:** 55.0% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.88
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004573
  * `Imports (Out-Degree: 2):` pygments.lexer, pygments.token
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/examplefiles/fortran/zmlrpc.f90` (FORTRAN | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.581)
- **Top Global Matches:** file_cluster_8: 6.581, file_cluster_6: 17.447, file_cluster_3: 19.688
- **Magnitude:** 653.3 | **LOC:** 799 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.513; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (37.4%), Concurrency Surface (formerly Concurrency) (15.9%), Connectivity (formerly Api Exposure) (4.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 93`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 3`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 23`, `immutability_locks: 7`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` psb_const_mod, psb_descriptor_type, psb_error_mod, psb_penv_mod, psb_prec_type, psb_psblas_mod, psb_serial_mod
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pygments/cmdline.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.577)
- **Top Global Matches:** file_cluster_6: 9.577, file_cluster_8: 11.599, file_cluster_4: 16.695
- **Magnitude:** 636.18 | **LOC:** 669 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 1.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%), Complexity Load (formerly Cognitive Load) (73.2%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main_inner` **(Many-Argument Workhorses)** (Impact: 170.8)
  * `main` **(Compute Cores)** (Impact: 56.5)
    * *Intent:* """ Main command line entry point. """
  * `_print_list` **(Stateful Encapsulated Methods)** (Impact: 23.7)
  * `_print_list_as_json` **(Stateful Encapsulated Methods)** (Impact: 14.9)
  * `_parse_options` **(Stateful Encapsulated Methods)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 126`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 112`, `fragile_debt: 2`
* *Architecture:* `io: 45`, `api: 5`, `import: 18`
* *Defense:* `safety: 39`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.059
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.001361
  * `Imports (Out-Degree: 11):` and, argparse, colorama.initialise, json, os, pygments, pygments.filters, pygments.formatters...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pygments/lexers/lisp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.67)
- **Top Global Matches:** file_cluster_4: 7.67, file_cluster_9: 10.931, file_cluster_16: 11.624
- **Magnitude:** 629.92 | **LOC:** 3153 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 0.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.3%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_process_declaration` **(Stateful Encapsulated Methods)** (Impact: 53.9)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 18.6)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 16.7)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* # Recognizing builtins.
  * `_process_declarations` **(Stateful Encapsulated Methods)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 84 instances
* *High Risk Execution (weighted view):* 26
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 301`, `args: 21`, `func_start: 14`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 27`, `state_mutation: 219`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 26`, `api: 20`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 15`, `doc: 26`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.808
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.002226
  * `Imports (Out-Degree: 4):` pygments.lexer, pygments.lexers._cl_builtins, pygments.lexers._scheme_builtins, pygments.lexers.python, pygments.token, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pygments/lexers/robotframework.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.35)
- **Top Global Matches:** file_cluster_16: 5.35, file_cluster_12: 7.057, file_cluster_15: 7.236
- **Magnitude:** 628.9 | **LOC:** 552 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.533; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (68.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_tokenize` **(Stateful Encapsulated Methods)** (Impact: 22.8)
  * `_tokenize` **(Stateful Encapsulated Methods)** (Impact: 16.7)
  * `_tokenize` **(Stateful Encapsulated Methods)** (Impact: 13.7)
  * `_variable_state` **(Stateful Encapsulated Methods)** (Impact: 12.5)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.533
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00068
  * `Imports (Out-Degree: 2):` pygments.lexer, pygments.token, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/pascal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.39)
- **Top Global Matches:** file_cluster_8: 8.39, file_cluster_6: 10.242, file_cluster_4: 18.316
- **Magnitude:** 576.08 | **LOC:** 645 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.534; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 224.2)
  * `__init__` **(Type Conversions)** (Impact: 13.1)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.9)
  * `get_tokens_unprocessed` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 125`, `fragile_debt: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.534
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00068
  * `Imports (Out-Degree: 5):` pygments.lexer, pygments.lexers.modula2, pygments.scanner, pygments.token, pygments.util, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/markup.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.828)
- **Top Global Matches:** file_cluster_4: 5.828, file_cluster_6: 9.011, file_cluster_12: 12.289
- **Magnitude:** 562.98 | **LOC:** 1660 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.681; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Connectivity (formerly Api Exposure) (43.8%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_handle_sourcecode` **(Stateful Encapsulated Methods)** (Impact: 48.7)
  * `_handle_codeblock` **(Stateful Encapsulated Methods)** (Impact: 39.4)
  * `_handle_codeblock` **(Stateful Encapsulated Methods)** (Impact: 27.4)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.681
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.001531
  * `Imports (Out-Degree: 9):` pygments.lexer, pygments.lexers, pygments.lexers.css, pygments.lexers.data, pygments.lexers.html, pygments.lexers.javascript, pygments.lexers.lilypond, pygments.token...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pygments/formatters/img.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.553)
- **Top Global Matches:** file_cluster_12: 6.553, file_cluster_16: 7.491, file_cluster_15: 8.855
- **Magnitude:** 538.56 | **LOC:** 687 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.568; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%), Complexity Load (formerly Cognitive Load) (35.8%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `_create_mac` **(Stateful Encapsulated Methods)** (Impact: 21.2)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.568
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00068
  * `Imports (Out-Degree: 2):` PIL, _winreg, os, pygments.formatter, pygments.util, subprocess, sys, winreg
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pygments/lexers/shell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.485)
- **Top Global Matches:** file_cluster_6: 6.485, file_cluster_8: 12.054, file_cluster_4: 13.538
- **Magnitude:** 537.9 | **LOC:** 903 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.812; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (50.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_make_begin_state` **(Many-Argument Workhorses)** (Impact: 93.4)
  * `get_tokens_unprocessed` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `_make_label_state` **(Stateful Encapsulated Methods)** (Impact: 23.2)
  * `_make_follow_state` **(Stateful Encapsulated Methods)** (Impact: 19.9)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 62`, `args: 10`, `func_start: 10`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 8`, `state_mutation: 161`
* *Architecture:* `io: 2`, `api: 17`, `import: 4`
* *Defense:* `safety: 3`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.812
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002177
  * `Imports (Out-Degree: 3):` hide, pygments.lexer, pygments.token, pygments.util, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pygments/lexers/scripting.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.589)
- **Top Global Matches:** file_cluster_4: 5.589, file_cluster_15: 9.19, file_cluster_16: 9.286
- **Magnitude:** 503.76 | **LOC:** 1639 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 0.65; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.7%), Connectivity (formerly Api Exposure) (45.0%)
- **Documentation Coverage:** 68.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyse_text` **(Compute Cores)** (Impact: 49.3)
    * *Intent:* """ Perform a structural analysis for basic Easytrieve constructs. """
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 19.0)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 11.0)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 7.9)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.65
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002041
  * `Imports (Out-Degree: 4):` pygments.lexer, pygments.lexers._lua_builtins, pygments.lexers._luau_builtins, pygments.token, pygments.util, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pygments/lexers/sql.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.943)
- **Top Global Matches:** file_cluster_6: 5.943, file_cluster_4: 9.156, file_cluster_8: 16.272
- **Magnitude:** 479.94 | **LOC:** 1112 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 1.072; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `language_callback` **(Compute Cores)** (Impact: 55.4)
    * *Intent:* """Parse the content of a $-string using a lexer The lexer is chosen looking for a nearby LANGUAGE o...
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 37.6)
  * `get_tokens_unprocessed` **(Compute Cores)** (Impact: 23.9)
  * `_get_lexer` **(Stateful Encapsulated Methods)** (Impact: 14.9)
  * `analyse_text` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 272
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 71`, `args: 13`, `func_start: 13`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 148`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 23`, `import: 10`
* *Defense:* `safety: 3`, `doc: 21`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.072
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003499
  * `Imports (Out-Degree: 3):` collections, pygments.lexer, pygments.lexers, pygments.token, re
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/examplefiles/jsx/general.jsx` (JAVASCRIPT) | Magnitude: 9.12 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 18, core_var_decl: 11, ui_framework: 10, design_camel_case: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pygments/lexers/compiled.py` (PYTHON) | Magnitude: 17.46 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 42, import: 21, safety_bypasses: 1, api: 1
- `tests/examplefiles/powershell/test.ps1` (POWERSHELL) | Magnitude: 43.54 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 20, decorators: 17, closures: 14
- `tests/examplefiles/haskell/AcidStateAdvanced.hs` (HASKELL) | Magnitude: 22.98 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 44, args: 42, core_var_decl: 31
- `pygments/console.py` (PYTHON) | Magnitude: 62.8 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 21, core_var_decl: 9, design_snake_case: 9
- `pygments/lexers/bqn.py` (PYTHON) | Magnitude: 26.72 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 9, core_var_decl: 9, design_snake_case: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `doc/_themes/pygments14/relations.html` (HTML) | Magnitude: 15.44 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: ssr_boundaries: 12, indent_spaces: 12, structural_boundaries: 6, io: 4
- `tests/examplefiles/cplint/indian_gpadc.pl` (PERL) | Magnitude: 15.82 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 41, bitwise_ops: 22, structural_boundaries: 8, decorators: 7
- `tests/examplefiles/html/example.xhtml` (HTML) | Magnitude: 26.58 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 315, io: 99, core_var_decl: 92, design_snake_case: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pygments/lexers/prql.py` (PYTHON) | Magnitude: 20.7 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 191, core_var_decl: 13, bitwise_ops: 12, design_snake_case: 12
- `pygments/lexers/oberon.py` (PYTHON) | Magnitude: 25.56 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 83, core_var_decl: 12, design_snake_case: 12, state_mutation: 11
- `pygments/lexers/asn1.py` (PYTHON) | Magnitude: 32.62 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 116, core_var_decl: 19, state_mutation: 16, design_snake_case: 12
- `pygments/modeline.py` (PYTHON) | Magnitude: 33.6 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, core_var_decl: 7, design_snake_case: 7
- `tests/test_theorem.py` (PYTHON) | Magnitude: 7.04 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, safety: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pygments/lexers/usd.py` (PYTHON) | Magnitude: 15.06 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 12, core_var_decl: 11, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pygments/lexers/pony.py` (PYTHON) | Magnitude: 26.48 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 12, core_var_decl: 11, design_snake_case: 11
- `doc/_themes/pygments14/layout.html` (HTML) | Magnitude: 92.28 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, ssr_boundaries: 36, io: 25, core_var_decl: 19
- `doc/_templates/styles.html` (HTML) | Magnitude: 61.6 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ssr_boundaries: 18, indent_spaces: 16, args: 11, structural_boundaries: 10
- `tests/test_modeline.py` (PYTHON) | Magnitude: 3.7 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, core_var_decl: 3, design_snake_case: 3
- `pygments/lexers/diff.py` (PYTHON) | Magnitude: 47.38 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 112, state_mutation: 28, core_var_decl: 28, design_snake_case: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/examplefiles/luau/createSignal.luau` (LUA) | Magnitude: 58.34 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 38, structural_boundaries: 32, core_var_decl: 11, branch: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pygments/lexers/templates.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 1012.04
- `pygments/lexers/webmisc.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 781.9
- `pygments/cmdline.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 636.18
- `pygments/lexers/lisp.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 629.92
- `pygments/lexers/robotframework.py` -> **Georg Brandl** (100.0% isolated ownership) | Magnitude: 628.9

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pygments/lexer.py` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 100.0%)
- `pygments/filters/__init__.py` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 95.2431%)
- `pygments/__init__.py` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 91.6827%)
- `pygments/lexers/__init__.py` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)
- `pygments/formatter.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pygments/lexer.py` -> **Severity: 13.082** (Embedded: 0.1607 * Error Risk: 81.3996%)
- `pygments/token.py` -> **Severity: 12.883** (Embedded: 0.1971 * Error Risk: 65.3524%)
- `pygments/util.py` -> **Severity: 7.402** (Embedded: 0.1061 * Error Risk: 69.7699%)
- `pygments/regexopt.py` -> **Severity: 6.713** (Embedded: 0.0858 * Error Risk: 78.245%)
- `pygments/filters/__init__.py` -> **Severity: 4.817** (Embedded: 0.0859 * Error Risk: 56.0653%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pygments/token.py` -> **Severity: 6246.326** (Blast Radius: 81.983 * Doc Risk: 76.1905%)
- `pygments/lexer.py` -> **Severity: 2781.342** (Blast Radius: 50.329 * Doc Risk: 55.2632%)
- `pygments/style.py` -> **Severity: 1118.4** (Blast Radius: 11.184 * Doc Risk: 100.0%)
- `pygments/filters/__init__.py` -> **Severity: 780.463** (Blast Radius: 9.268 * Doc Risk: 84.2105%)
- `pygments/plugin.py` -> **Severity: 655.1** (Blast Radius: 6.551 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `2` files carry mainframe facts -- `15` call sites, `8` dataset bindings, `1001` record items.

### `tests/examplefiles/cobol/example.cob` (COBOL)
- **Calls:** `CALL CHECKSOURCE`, `CALL GETOSTYPE`, `CALL CBL_CHANGE_DIR`, `CALL SYSTEM`, `CALL C$SLEEP`, `CALL CBL_DELETE_FILE`, `CALL LISTING`
- **Datasets:** `BAT-FILE-NAME(declared)`, `COBC-OUTPUT-FILE(INPUT)`, `FILE-NAME(INPUT)`, `EXPANDED-SRC-FILENAME(declared)`, `REPORT-FILENAME(OUTPUT)`, `DISK(OUTPUT)`
- **Record layouts (1001 items):** `RESERVED-WORDS (592)`, `SWITCHES-SCREEN (139)`, `SYNTAX-PARSING-ITEMS (35)`, `FLAGS (27)`, `SWITCHES (21)`, `DETAIL-LINE-X (13)`, `SWITCH-KEYWORD (10)`, `FLAGS (10)`, `TALLY (9)`, `SORT-REC⟵SORT-FILE (9)`, `CONFIG-KEYS (8)`, `SOURCE-CODE-REC⟵SOURCE-CODE (7)` … (+81 more)
- **Data moves:** 251 (ACCEPT 6, ADD 2, MOVE 181, STRING 48, SUBTRACT 1, UNSTRING 13); most-fed items `CMD`, `SWITCH-VALUE`, `CK-S-F1`, `CK-S-F2`, `CK-S-F3`, `CK-S-F4`

### `tests/examplefiles/jcl/example.jcl` (JCL)
- **Calls:** `EXEC PGM IEBGENER`, `EXEC PGM IEFBR14`
- **Datasets:** `SYSUT1→OLDFILE`, `SYSUT2→NEWFILE`
- **Job flow:** `COPY01=IEBGENER` -> `CONT01=IEFBR14` -> `SORT01=IEFBR14` -> `STP4=PROC BILLING`; creates `NEWFILE`

- **Mainframe skeleton completeness:** 51% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: application programs (source or load-module list) (8 gaps).

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 723 literal sites + 4 sites through wrappers = 727

- `println` (function, debug_prints, primitive): 4 call sites in 2 files -- `tests/examplefiles/cr/test.cr`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6965 call pairs -- scoped 29.9%, unique 0.2%, ambiguous 6.8%, external 63.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 4134 | 38.6% | 0.0% | 9.2% | 52.2% |
| ruby | 641 | 10.0% | 0.2% | 12.6% | 77.2% |
| c | 502 | 15.7% | 0.0% | 0.0% | 84.3% |
| haskell | 277 | 36.5% | 5.4% | 0.0% | 58.1% |
| scheme | 276 | 1.1% | 0.0% | 0.0% | 98.9% |
| crystal | 222 | 27.5% | 0.0% | 1.8% | 70.7% |
| shell | 162 | 14.8% | 0.0% | 0.0% | 85.2% |
| java | 133 | 6.0% | 0.0% | 5.3% | 88.7% |
| rust | 109 | 18.3% | 0.0% | 0.0% | 81.7% |
| lua | 88 | 6.8% | 0.0% | 0.0% | 93.2% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
