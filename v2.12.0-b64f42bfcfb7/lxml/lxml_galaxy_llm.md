# ARCHITECTURAL_BRIEF: lxml
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 341 analyzed artifact(s), 69237 LOC.
- **Load-bearing artifact:** `lxml-6.0.2/src/lxml/__init__.py` -- 33 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lxml-6.0.2/src/lxml/tests/test_etree.py` -- pulls in 20 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lxml-6.0.2/src/lxml/tests/test_etree.py` at magnitude 3697.28 (structural weight, not risk).
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
| Total Artifacts | 456 |
| Analyzed Artifacts (Scanned) | 341 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 115 |
| Total LOC | 69237 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6757 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2663 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.635 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 145 | 44205 | 42.5% |
| XML | 73 | 0 | 21.4% |
| PLAINTEXT | 62 | 0 | 18.2% |
| HTML | 32 | 20810 | 9.4% |
| CSS | 9 | 1346 | 2.6% |
| JAVASCRIPT | 8 | 1636 | 2.3% |
| C | 7 | 1001 | 2.1% |
| MAKEFILE | 3 | 162 | 0.9% |
| SCHEME | 1 | 8 | 0.3% |
| SHELL | 1 | 69 | 0.3% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 340 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 54%, Large Core Modules (3) 13%, Parameter Forwarders Files 11%, State Mutators Files 5%, Declarative / Non-Code 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 279 | 81.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 62 | 18.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 115*

**Composition by Extension & Reason:**
- `.data`: 43x Excluded (Unsupported Extension: '.data')
- `.html`: 2x Packed Payload Guard (Impossible Density: 5.35 hits/line), 1x Excluded (Lexical Monotony: High structural repetition detected in 4280 LOC), 1x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 24599 LOC), 1x Excluded (Machine-Generated Source Code Signature: 14345 LOC), 1x Excluded (Monolithic Amalgamation: 308003 LOC exceeds the 150000 LOC backstop)
- `.js`: 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rng`: 4x Excluded (Unsupported Extension: '.rng')
- `.css`: 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 10 LOC)
- `.asc`: 2x Excluded (Unsupported Extension: '.asc')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.dtd`: 2x Excluded (Unsupported Extension: '.dtd')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.inv`: 1x Excluded (Unsupported Extension: '.inv')
- `.mgp`: 1x Excluded (Unsupported Extension: '.mgp')
- `.htc`: 1x Excluded (Unsupported Extension: '.htc')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.0 | 20.2 | 4.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.0 | 37.1 | 49.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 97.6 | 11.2 | 2.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 36.2 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.6 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 658 | 75 | 3 | `lxml-6.0.2/src/lxml/tests/test_etree.py` |
| cleanup | 160 | 28 | 0 | `lxml-6.0.2/doc/html/apidoc/lxml.html` |
| guards | 2365 | 132 | 24 | `lxml-6.0.2/src/lxml/etree.pyx` |
| danger | 1283 | 112 | 11 | `lxml-6.0.2/src/lxml/etree.pyx` |
| concurrency | 185 | 25 | 0 | `lxml-6.0.2/src/lxml/html/_difflib.py` |
| connectivity | 4291 | 149 | 31 | `lxml-6.0.2/src/lxml/tests/test_etree.py` |
| io | 16502 | 91 | 17 | `lxml-6.0.2/doc/html/apidoc/genindex.html` |
| crypto | 3 | 3 | 0 | `lxml-6.0.2/buildlibxml.py` |
| ipc | 24 | 7 | 0 | `lxml-6.0.2/doc/mkhtml.py` |
| time | 12 | 7 | 0 | `lxml-6.0.2/benchmark/benchbase.py` |
| serialization | 3 | 1 | 0 | `lxml-6.0.2/src/lxml/tests/test_objectify.py` |
| regex | 164 | 54 | 2 | `lxml-6.0.2/doc/html/apidoc/_static/language_data.js` |
| events | 271 | 47 | 2 | `lxml-6.0.2/src/lxml/tests/test_sax.py` |
| tests | 1728 | 41 | 5 | `lxml-6.0.2/src/lxml/tests/test_etree.py` |
| docs | 1321 | 140 | 8 | `lxml-6.0.2/src/lxml/etree.pyx` |
| debt | 448 | 88 | 4 | `lxml-6.0.2/src/lxml/tests/test_etree.py` |
| mutation | 37668 | 175 | 244 | `lxml-6.0.2/doc/html/apidoc/genindex.html` |
| dead_code | 2295 | 111 | 14 | `lxml-6.0.2/src/lxml/tests/test_etree.py` |
| credential | 5 | 3 | 0 | `lxml-6.0.2/src/lxml/tests/selftest.py` |
| threat | 7 | 4 | 0 | `lxml-6.0.2/doc/html/elementsoup.html` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 340 | 40 | 2 | `lxml-6.0.2/doc/html/apidoc/lxml.sax.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lxml-6.0.2/doc/html/apidoc/genindex.html` (Hits: 7196)
- `lxml-6.0.2/doc/html/apidoc/lxml.html` (Hits: 6820)
- `lxml-6.0.2/doc/html/FAQ.html` (Hits: 277)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`lxml-6.0.2/src/lxml/__init__.py`) — 33 inbound connections
2. **genindex.html** (`lxml-6.0.2/doc/html/apidoc/genindex.html`) — 31 inbound connections
3. **search.html** (`lxml-6.0.2/doc/html/apidoc/search.html`) — 31 inbound connections
4. **common_imports.py** (`lxml-6.0.2/src/lxml/tests/common_imports.py`) — 28 inbound connections
5. **style.css** (`lxml-6.0.2/doc/html/style.css`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_etree.py** (`lxml-6.0.2/src/lxml/tests/test_etree.py`) — 20 outbound dependencies
2. **buildlibxml.py** (`lxml-6.0.2/buildlibxml.py`) — 17 outbound dependencies
3. **common_imports.py** (`lxml-6.0.2/src/lxml/tests/common_imports.py`) — 16 outbound dependencies
4. **test_elementtree.py** (`lxml-6.0.2/src/lxml/tests/test_elementtree.py`) — 16 outbound dependencies
5. **test_html5parser.py** (`lxml-6.0.2/src/lxml/html/tests/test_html5parser.py`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_annotate_element` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/src/lxml/objectify.pyx`) -> Impact: **158.6** | LOC: 120
- `ext_modules` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/setupinfo.py`) -> Impact: **136.5** | LOC: 136
- `DataElement` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/src/lxml/objectify.pyx`) -> Impact: **129.6** | LOC: 104
- `_mdiff` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/src/lxml/html/_difflib.py`) -> Impact: **111.4** | LOC: 268
- `_replaceSlice` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/src/lxml/apihelpers.pxi`) -> Impact: **110.1** | LOC: 138
- `build_libs` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/buildlibxml.py`) -> Impact: **103.8** | LOC: 116
- `index` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/src/lxml/etree.pyx`) -> Impact: **93.7** | LOC: 86
  * *Intent:* """index(self, child, start=None, stop=None) Find the position of the child within the parent. This method is not part of the original ElementTree API...
- `_checkNumber` **(Compute Cores)** (@ `lxml-6.0.2/src/lxml/objectify.pyx`) -> Impact: **88.6** | LOC: 74
- `main` **(Compute Cores)** (@ `lxml-6.0.2/test.py`) -> Impact: **86.1** | LOC: 166
  * *Intent:* """Main program."""
- `tostring` **(Many-Argument Workhorses)** (@ `lxml-6.0.2/src/lxml/etree.pyx`) -> Impact: **84.8** | LOC: 110

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lxml-6.0.2/src/lxml` | 47 | 21285.62 | 43.48% | 54.5% |
| `lxml-6.0.2/src/lxml/tests` | 44 | 15605.6 | 18.14% | 0.0% |
| `lxml-6.0.2/src/lxml/html` | 15 | 5437.68 | 38.69% | 23.55% |
| `lxml-6.0.2` | 15 | 2969.2 | 23.99% | 11.52% |
| `lxml-6.0.2/benchmark` | 6 | 1806.64 | 54.07% | 56.29% |
| `lxml-6.0.2/src/lxml/includes` | 19 | 1574.12 | 3.41% | 67.19% |
| `lxml-6.0.2/doc` | 32 | 1039.14 | 9.16% | 1.72% |
| `lxml-6.0.2/doc/html/apidoc/_static` | 8 | 1004.38 | 33.0% | 17.37% |
| `lxml-6.0.2/src/lxml/html/tests` | 19 | 716.72 | 18.65% | 0.0% |
| `lxml-6.0.2/doc/s5/ep2008` | 3 | 687.28 | 12.03% | 33.27% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lxml-6.0.2/benchmark/bench_etree.py` -> **100.0%** Exposure
- `lxml-6.0.2/src/lxml/includes/etreepublic.pxd` -> **100.0%** Exposure
- `lxml-6.0.2/src/lxml/includes/xmlschema.pxd` -> **100.0%** Exposure
- `lxml-6.0.2/src/lxml/includes/xslt.pxd` -> **100.0%** Exposure
- `lxml-6.0.2/src/lxml/public-api.pxi` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lxml-6.0.2/benchmark/bench_objectify.py` -> **100.0%** Exposure
- `lxml-6.0.2/benchmark/benchbase.py` -> **100.0%** Exposure
- `lxml-6.0.2/benchmark/run_benchmarks.py` -> **100.0%** Exposure
- `lxml-6.0.2/buildlibxml.py` -> **100.0%** Exposure
- `lxml-6.0.2/doc/mkhtml.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lxml-6.0.2/src/lxml/tests/test_etree.py` -> **359** Orphaned Functions | **37** Duplicates
- `lxml-6.0.2/src/lxml/tests/test_elementtree.py` -> **282** Orphaned Functions | **30** Duplicates
- `lxml-6.0.2/src/lxml/tests/test_objectify.py` -> **206** Orphaned Functions | **0** Duplicates
- `lxml-6.0.2/src/lxml/tests/test_xslt.py` -> **98** Orphaned Functions | **6** Duplicates
- `lxml-6.0.2/src/lxml/tests/test_htmlparser.py` -> **55** Orphaned Functions | **21** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `655` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lxml-6.0.2/src/lxml/tests/test_etree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.3)
- **Top Global Matches:** file_cluster_15: 8.3, file_cluster_12: 8.438, file_cluster_0: 9.504
- **Magnitude:** 3697.28 | **LOC:** 5867 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 1.759; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (38.6%), Connectivity (formerly Api Exposure) (13.9%)
- **Documentation Coverage:** 99.5386% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_parse_error_logging` **(Defensive Guards)** (Impact: 16.6)
  * `_test_python_error_logging` **(Stateful Encapsulated Methods)** (Impact: 14.1)
    * *Intent:* """This can't really be tested as long as there isn't a way to reset the logging setup ... """
  * `test_very_large_sourceline_iterparse` **(Defensive Guards)** (Impact: 11.8)
  * `test_attrib_order` **(Defensive Guards)** (Impact: 11.7)
  * `test_html_prefix_nsmap` **(Compute Cores)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 2014
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 636`, `args: 426`, `func_start: 425`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 1672`, `dead_code: 3`, `fragile_debt: 7`, `duplicate_logic: 37`, `unreferenced_by_name: 359`
* *Architecture:* `io: 15`, `api: 453`, `import: 24`
* *Defense:* `safety: 55`, `doc: 37`, `test: 368`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .common_imports, .selftest, .selftest2, collections, collections.abc, contextlib, copy, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/src/lxml/tests/test_elementtree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.836)
- **Top Global Matches:** file_cluster_12: 10.836, file_cluster_15: 11.221, file_cluster_16: 11.948
- **Magnitude:** 3515.62 | **LOC:** 5021 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.759; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (40.2%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 99.3481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_xml_c14n2` **(Compute Cores)** (Impact: 51.8)
    * *Intent:* # # basic method=c14n tests from the c14n 2.0 specification. uses # test files under xmltestdata/c14...
  * `test_interface` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* # Test element tree interface. def check_string(string): len(string) for char in string: self.assert...
  * `_canonicalize` **(Stateful Encapsulated Methods)** (Impact: 12.7)
  * `_canonicalize` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `assertEncodingDeclaration` **(Defensive Guards)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 204 instances
* *State Mutation (weighted view):* 1953
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 562`, `args: 397`, `func_start: 395`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 1545`, `fragile_debt: 6`, `duplicate_logic: 30`, `unreferenced_by_name: 282`
* *Architecture:* `io: 34`, `api: 399`, `import: 17`
* *Defense:* `safety: 35`, `doc: 13`, `test: 328`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .common_imports, array, contextlib, copy, functools, io, itertools, operator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/src/lxml/etree.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.567)
- **Top Global Matches:** file_cluster_12: 7.567, file_cluster_15: 8.311, file_cluster_16: 8.698
- **Magnitude:** 2829.38 | **LOC:** 3854 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **13**; blast radius 10.043; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.2%), Connectivity (formerly Api Exposure) (60.4%)
- **Documentation Coverage:** 54.6419% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `index` **(Many-Argument Workhorses)** (Impact: 93.7)
    * *Intent:* """index(self, child, start=None, stop=None) Find the position of the child within the parent. This ...
  * `tostring` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `write` **(Many-Argument Workhorses)** (Impact: 81.5)
  * `getelementpath` **(Compute Cores)** (Impact: 36.1)
    * *Intent:* """getelementpath(self, element) Returns a structural, absolute ElementPath expression to find the e...
  * `_storeTags` **(Many-Argument Workhorses)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 360 instances
* *State Mutation (weighted view):* 1133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 513`, `structural_boundaries: 605`, `args: 244`, `func_start: 244`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 413`, `dead_code: 3`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `io: 5`, `api: 130`, `import: 18`
* *Defense:* `safety: 52`, `doc: 128`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.043
  * `Choke Point (Betweenness):` 0.000124 | `Ripple Effect (Closeness):` 0.025431
  * `Imports (Out-Degree: 2):` abc, collections, collections.abc, functools, io, itertools, lxml, lxml.cssselect...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/serializer.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.946)
- **Top Global Matches:** file_cluster_4: 5.946, file_cluster_6: 10.327, file_cluster_12: 11.107
- **Magnitude:** 2313.12 | **LOC:** 1850 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.507; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (97.9%), Complexity Load (formerly Cognitive Load) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 87.6106% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_start` **(Many-Argument Workhorses)** (Impact: 79.3)
  * `_writeDtdToBuffer` **(Many-Argument Workhorses)** (Impact: 72.1)
  * `_writeNodeToBuffer` **(Many-Argument Workhorses)** (Impact: 69.3)
  * `_tostring` **(Many-Argument Workhorses)** (Impact: 60.4)
  * `write` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* """write(self, *args, with_tail=True, pretty_print=False, method=None) Write subtrees or strings int...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 285 instances
* *Concurrency (weighted view):* 106
* *State Mutation (weighted view):* 908
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 196`, `args: 92`, `func_start: 91`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 338`, `unreferenced_by_name: 6`
* *Architecture:* `io: 5`, `api: 22`, `concurrency: 21`, `import: 5`
* *Defense:* `safety: 39`, `doc: 12`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.507
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002732
  * `Imports (Out-Degree: 0):` codecs, contextlib, gzip, io
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/objectify.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.09)
- **Top Global Matches:** file_cluster_4: 7.09, file_cluster_12: 7.36, file_cluster_15: 7.895
- **Magnitude:** 2241.82 | **LOC:** 2150 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.008; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.6%), Guard Balance (formerly Safety Score) (78.9%)
- **Documentation Coverage:** 77.6119% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_annotate_element` **(Many-Argument Workhorses)** (Impact: 158.6)
  * `DataElement` **(Many-Argument Workhorses)** (Impact: 129.6)
  * `_checkNumber` **(Compute Cores)** (Impact: 88.6)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 51.4)
  * `_setSlice` **(Many-Argument Workhorses)** (Impact: 45.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 974
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 375`, `args: 161`, `func_start: 161`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 360`, `duplicate_logic: 3`, `unreferenced_by_name: 47`
* *Architecture:* `api: 31`, `import: 4`
* *Defense:* `safety: 37`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002732
  * `Imports (Out-Degree: 2):` copyreg, lxml, math, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/html/__init__.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.831)
- **Top Global Matches:** file_cluster_12: 7.831, file_cluster_15: 8.552, file_cluster_16: 9.224
- **Magnitude:** 1830.08 | **LOC:** 1928 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **14**; blast radius 12.153; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%)
- **Documentation Coverage:** 55.3097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iterlinks` **(Compute Cores)** (Impact: 73.7)
    * *Intent:* """ Yield (element, attribute, link, pos), where attribute may be None (indicating the link is in th...
  * `fromstring` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* """ Parse the html, returning a single element/document. This tries to minimally parse the chunk of ...
  * `fragments_fromstring` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `rewrite_links` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `fragment_fromstring` **(Many-Argument Workhorses)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 242 instances
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 376`, `args: 129`, `func_start: 129`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 270`, `planned_debt: 1`, `fragile_debt: 11`, `duplicate_logic: 6`
* *Architecture:* `io: 3`, `api: 115`, `import: 15`
* *Defense:* `safety: 45`, `doc: 73`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.153
  * `Choke Point (Betweenness):` 0.000495 | `Ripple Effect (Closeness):` 0.030783
  * `Imports (Out-Degree: 5):` ..etree, ._setmixin, .defs, collections.abc, copy, functools, lxml.cssselect, os...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/apihelpers.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.381)
- **Top Global Matches:** file_cluster_4: 8.381, file_cluster_12: 8.413, file_cluster_15: 10.592
- **Magnitude:** 1777.84 | **LOC:** 1802 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%)
- **Documentation Coverage:** 65.9341% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_replaceSlice` **(Many-Argument Workhorses)** (Impact: 110.1)
  * `_makeElement` **(Many-Argument Workhorses)** (Impact: 53.4)
  * `_removeUnusedNamespaceDeclarations` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* """Remove any namespace declarations from a subtree that are not used by any of its elements (or att...
  * `_tagMatches` **(Compute Cores)** (Impact: 36.0)
    * *Intent:* """Tests if the node matches namespace URI and tag name. A node matches if it matches both c_href an...
  * `_mapTagsToQnameMatchArray` **(Many-Argument Workhorses)** (Impact: 28.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 254 instances
* *State Mutation (weighted view):* 775
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 445`, `structural_boundaries: 239`, `args: 91`, `func_start: 91`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 267`, `fragile_debt: 3`, `unreferenced_by_name: 44`
* *Architecture:* None
* *Defense:* `safety: 56`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/src/lxml/parser.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.264)
- **Top Global Matches:** file_cluster_12: 7.264, file_cluster_15: 7.554, file_cluster_16: 7.588
- **Magnitude:** 1661.52 | **LOC:** 2072 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **2**; blast radius 9.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 72.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `feed` **(Many-Argument Workhorses)** (Impact: 72.0)
    * *Intent:* """feed(self, data) Feeds data to the parser. The argument should be an 8-bit string buffer containi...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 69.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 25.8)
  * `copyToBuffer` **(Stateful Encapsulated Methods)** (Impact: 24.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 991
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 192`, `args: 76`, `func_start: 76`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 377`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 4`, `unreferenced_by_name: 11`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `safety: 66`, `doc: 30`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.378
  * `Choke Point (Betweenness):` 0.000165 | `Ripple Effect (Closeness):` 0.039064
  * `Imports (Out-Degree: 1):` types, warnings
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/tests/test_objectify.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.807)
- **Top Global Matches:** file_cluster_15: 6.807, file_cluster_12: 8.167, file_cluster_16: 8.959
- **Magnitude:** 1653.96 | **LOC:** 2758 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.759; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.6%), Connectivity (formerly Api Exposure) (13.5%)
- **Documentation Coverage:** 99.1091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_standard_lookup_fuzz` **(Defensive Guards)** (Impact: 17.7)
  * `test_schema_types_prefixed` **(Defensive Guards)** (Impact: 11.9)
  * `test_schema_types` **(Defensive Guards)** (Impact: 11.8)
  * `test_standard_lookup` **(Defensive Guards)** (Impact: 10.8)
  * `test_getslice_partial` **(Compute Cores)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 111 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 268`, `args: 214`, `func_start: 214`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 569`, `dead_code: 2`, `unreferenced_by_name: 206`
* *Architecture:* `api: 218`, `import: 9`
* *Defense:* `safety: 98`, `doc: 28`, `test: 206`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .common_imports, datetime, lxml, operator, pickle, random, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/src/lxml/html/_difflib.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.409)
- **Top Global Matches:** file_cluster_4: 7.409, file_cluster_6: 7.468, file_cluster_12: 14.168
- **Magnitude:** 1137.76 | **LOC:** 2107 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 2.312; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 55.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mdiff` **(Many-Argument Workhorses)** (Impact: 111.4)
  * `find_longest_match` **(Many-Argument Workhorses)** (Impact: 69.3)
    * *Intent:* """Find longest matching block in a[alo:ahi] and b[blo:bhi]. By default it will find the longest mat...
  * `context_diff` **(Many-Argument Workhorses)** (Impact: 54.8)
    * *Intent:* # See http://www.unix.org/single_unix_specification/
  * `_fancy_replace` **(Many-Argument Workhorses)** (Impact: 49.8)
  * `unified_diff` **(Many-Argument Workhorses)** (Impact: 45.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 142 instances
* *State Mutation (weighted view):* 451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 142`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 167`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* `api: 28`, `import: 5`
* *Defense:* `safety: 20`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.312
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003643
  * `Imports (Out-Degree: 0):` collections, cython, heapq, re, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/tests/test_xslt.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.656)
- **Top Global Matches:** file_cluster_15: 6.656, file_cluster_12: 7.784, file_cluster_16: 8.449
- **Magnitude:** 1007.68 | **LOC:** 2084 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.759; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (20.5%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execute` **(Defensive Guards)** (Impact: 12.8)
  * `execute` **(Defensive Guards)** (Impact: 12.7)
  * `test_exslt_regexp_match` **(Compute Cores)** (Impact: 11.7)
  * `test_extension_element_apply_templates_remove_blank_text` **(Defensive Guards)** (Impact: 8.7)
  * `test_extension_element_apply_templates` **(Compute Cores)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 453
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 226`, `args: 126`, `func_start: 126`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 401`, `fragile_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 98`
* *Architecture:* `io: 11`, `api: 149`, `import: 9`
* *Defense:* `safety: 40`, `doc: 109`, `test: 101`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .common_imports, contextlib, copy, gzip, io, os.path, tempfile, textwrap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/src/lxml/saxparser.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.803)
- **Top Global Matches:** file_cluster_12: 6.803, file_cluster_7: 9.16, file_cluster_5: 9.564
- **Magnitude:** 991.3 | **LOC:** 876 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 3.005; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.4%)
- **Documentation Coverage:** 77.0492% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_handleSaxTargetStart` **(Many-Argument Workhorses)** (Impact: 76.2)
  * `_handleSaxStart` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `_connectEvents` **(Stateful Encapsulated Methods)** (Impact: 24.6)
    * *Intent:* """Wrap original SAX2 callbacks to collect parse events without parser target. """
  * `_connectTarget` **(Stateful Encapsulated Methods)** (Impact: 21.3)
    * *Intent:* """Wrap original SAX2 callbacks to call into parser target. """
  * `_pushSaxStartEvent` **(Many-Argument Workhorses)** (Impact: 20.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 101`, `args: 54`, `func_start: 54`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 184`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`
* *Defense:* `safety: 33`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.005464
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/extensions.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.846)
- **Top Global Matches:** file_cluster_12: 6.846, file_cluster_7: 9.174, file_cluster_5: 9.693
- **Magnitude:** 910.26 | **LOC:** 831 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 4.0; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.0%), Guard Balance (formerly Safety Score) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.9649% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 47.8)
  * `_unpackNodeSetEntry` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `_unwrapXPathObject` **(Compute Cores)** (Impact: 27.4)
  * `match` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `_buildElementStringResult` **(Many-Argument Workhorses)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 144 instances
* *State Mutation (weighted view):* 457
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 101`, `args: 47`, `func_start: 46`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 169`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 25`
* *Architecture:* `api: 9`
* *Defense:* `safety: 24`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007286
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/html/diff.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.032)
- **Top Global Matches:** file_cluster_12: 6.032, file_cluster_15: 8.293, file_cluster_4: 8.584
- **Magnitude:** 886.92 | **LOC:** 973 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 3.254; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.7%)
- **Documentation Coverage:** 45.7447% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cleanup_delete` **(Compute Cores)** (Impact: 43.6)
    * *Intent:* """ Cleans up any DEL_START/DEL_END markers in the document, replacing them with <del></del>. To do ...
  * `flatten_el` **(Compute Cores)** (Impact: 31.3)
    * *Intent:* """ Takes an lxml element el, and generates all the text chunks for that tag. Each start tag is a ch...
  * `fixup_chunks` **(Defensive Guards)** (Impact: 20.9)
    * *Intent:* """ This function takes a list of chunks and produces a list of tokens. """
  * `mark_unbalanced` **(Compute Cores)** (Impact: 18.1)
  * `_move_el_inside_block` **(Stateful Encapsulated Methods)** (Impact: 17.2)
    * *Intent:* """ helper for _fixup_ins_del_tags; actually takes the <ins> etc tags and moves them inside any bloc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 477
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 167`, `args: 48`, `func_start: 48`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 177`, `fragile_debt: 1`
* *Architecture:* `api: 49`, `import: 15`
* *Defense:* `safety: 14`, `doc: 33`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.254
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.002732
  * `Imports (Out-Degree: 5):` ._difflib, .defs, cython, cython.cimports.lxml.html._difflib, difflib, functools, html, inspect...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/includes/xmlerror.pxd` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.74)
- **Top Global Matches:** file_cluster_2: 5.74, file_cluster_15: 7.632, file_cluster_17: 7.686
- **Magnitude:** 838.54 | **LOC:** 861 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xmlSetGenericErrorFunc` **(State Mutators)** (Impact: 1.8)
  * `xmlSetStructuredErrorFunc` **(State Mutators)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 818`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/buildlibxml.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.674)
- **Top Global Matches:** file_cluster_4: 7.674, file_cluster_6: 10.772, file_cluster_12: 11.636
- **Magnitude:** 836.64 | **LOC:** 700 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 2.718; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.0%)
- **Documentation Coverage:** 43.2203% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_libs` **(Many-Argument Workhorses)** (Impact: 103.8)
  * `download_library` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `unpack_tarball` **(Compute Cores)** (Impact: 32.0)
  * `download_and_extract_windows_binaries` **(Compute Cores)** (Impact: 28.7)
  * `find_max_version` **(Compute Cores)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 129 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 424
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 117`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 166`
* *Architecture:* `io: 48`, `api: 28`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 20`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.718
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003643
  * `Imports (Out-Degree: 0):` contextlib, email.message, ftplib, hashlib, json, multiprocessing, os, platform...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/xslt.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.098)
- **Top Global Matches:** file_cluster_12: 7.098, file_cluster_15: 7.714, file_cluster_4: 7.745
- **Magnitude:** 794.72 | **LOC:** 958 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 2.631; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Complexity Load (formerly Cognitive Load) (66.2%)
- **Documentation Coverage:** 65.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Many-Argument Workhorses)** (Impact: 80.6)
    * *Intent:* """__call__(self, _input, profile_run=False, **kw) Execute the XSL transformation on a tree or Eleme...
  * `__getbuffer__` **(Stateful Encapsulated Methods)** (Impact: 25.6)
  * `write_output` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* """write_output(self, file, *, compression=0) Serialise the XSLT output to a file or file-like objec...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 22.2)
  * `_convert_xslt_parameters` **(Many-Argument Workhorses)** (Impact: 22.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 87`, `args: 41`, `func_start: 41`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 172`, `unreferenced_by_name: 13`
* *Architecture:* `api: 9`
* *Defense:* `safety: 18`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.631
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.005464
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/setupinfo.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.268)
- **Top Global Matches:** file_cluster_12: 8.268, file_cluster_4: 8.58, file_cluster_15: 10.635
- **Magnitude:** 793.88 | **LOC:** 563 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 2.257; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Complexity Load (formerly Cognitive Load) (82.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ext_modules` **(Many-Argument Workhorses)** (Impact: 136.5)
  * `find_dependencies` **(Compute Cores)** (Impact: 19.8)
  * `option_value` **(Compute Cores)** (Impact: 18.4)
  * `get_library_versions` **(I/O & Config Routines)** (Impact: 17.1)
  * `cflags` **(Compute Cores)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 139 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 433
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 119`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 3`, `state_mutation: 155`
* *Architecture:* `io: 36`, `api: 25`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.257
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.002732
  * `Imports (Out-Degree: 2):` Cython.Build, Cython.Compiler, Cython.Compiler.Version, buildlibxml, distutils, distutils.core, distutils.errors, io...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/benchmark/benchbase.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.112)
- **Top Global Matches:** file_cluster_12: 7.112, file_cluster_7: 9.345, file_cluster_5: 9.889
- **Magnitude:** 774.22 | **LOC:** 582 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 6.743; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Complexity Load (formerly Cognitive Load) (82.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 89.899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runBench` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `benchmarks` **(Defensive Guards)** (Impact: 26.9)
    * *Intent:* """Returns a list of all benchmarks. A benchmark is a tuple containing a method name and a list of t...
  * `buildSuites` **(Compute Cores)** (Impact: 24.8)
    * *Intent:* ############################################################ # Prepare and run benchmark suites ####...
  * `main` **(Defensive Guards)** (Impact: 18.0)
    * *Intent:* ############################################################ # Main program ########################...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 17.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 118 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 390
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 110`, `args: 47`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 3`, `state_mutation: 154`
* *Architecture:* `io: 9`, `api: 37`, `import: 7`
* *Defense:* `safety: 30`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.743
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.010929
  * `Imports (Out-Degree: 1):` contextlib, copy, functools, gc, itertools, lxml, re, string...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/xmlerror.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.75)
- **Top Global Matches:** file_cluster_12: 6.75, file_cluster_15: 7.448, file_cluster_16: 7.662
- **Magnitude:** 764.28 | **LOC:** 1663 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 2.504; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%)
- **Documentation Coverage:** 56.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_receiveGenericError` **(Many-Argument Workhorses)** (Impact: 64.7)
  * `_setError` **(Stateful Encapsulated Methods)** (Impact: 22.3)
  * `_receiveGeneric` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `_buildParseException` **(Compute Cores)** (Impact: 14.9)
  * `_buildExceptionMessage` **(Compute Cores)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 116`, `args: 68`, `func_start: 68`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 150`, `planned_debt: 1`, `unreferenced_by_name: 22`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `safety: 9`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004918
  * `Imports (Out-Degree: 0):` logging
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.901)
- **Top Global Matches:** file_cluster_12: 7.901, file_cluster_4: 8.263, file_cluster_15: 10.412
- **Magnitude:** 726.98 | **LOC:** 622 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 2.257; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.6%)
- **Documentation Coverage:** 24.0385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 86.1)
    * *Intent:* """Main program."""
  * `get_test_files` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* """Returns a list of test module filenames."""
  * `visit` **(Compute Cores)** (Impact: 20.8)
  * `get_test_cases` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* """Returns a list of test cases from a given list of test modules."""
  * `run` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* """Run the given test case or test suite."""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 119 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 77`, `args: 29`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 149`, `fragile_debt: 4`
* *Architecture:* `io: 29`, `api: 25`, `import: 13`
* *Defense:* `safety: 15`, `doc: 15`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002732
  * `Imports (Out-Degree: 0):` coverage, curses, getopt, logging, os, re, sys, time...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/src/lxml/doctestcompare.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.032)
- **Top Global Matches:** file_cluster_12: 7.032, file_cluster_4: 7.273, file_cluster_15: 8.063
- **Magnitude:** 705.7 | **LOC:** 489 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 3.005; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.6%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare_docs` **(Compute Cores)** (Impact: 35.4)
  * `collect_diff_tag` **(Compute Cores)** (Impact: 31.3)
  * `collect_diff` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `format_doc` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `get_parser` **(Compute Cores)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 109`, `args: 32`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 148`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 33`, `import: 9`
* *Defense:* `safety: 16`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.005
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.005464
  * `Imports (Out-Degree: 1):` cgi, doctest, html, lxml, re, sys
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lxml-6.0.2/doc/s5/ep2008/atom.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.946)
- **Top Global Matches:** file_cluster_12: 5.946, file_cluster_15: 6.909, file_cluster_16: 7.042
- **Magnitude:** 649.42 | **LOC:** 627 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.759; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (80.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 81.7204% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_html__get` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* """ Gives the parsed HTML of element's content. May return an HtmlElement (from lxml.html) or an XHT...
  * `_html__set` **(Stateful Encapsulated Methods)** (Impact: 11.8)
  * `rel_links` **(Compute Cores)** (Impact: 11.0)
    * *Intent:* """ Return all the links with the given ``rel`` attribute. The default relation is ``'alternate'``, ...
  * `__get__` **(Compute Cores)** (Impact: 10.5)
  * `lookup` **(Compute Cores)** (Impact: 10.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 189`, `args: 70`, `func_start: 69`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 156`, `dead_code: 2`, `fragile_debt: 5`, `duplicate_logic: 2`, `unreferenced_by_name: 14`
* *Architecture:* `api: 39`, `import: 10`
* *Defense:* `safety: 9`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cgi, copy, datetime, lxml, lxml.etree, lxml.html, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/doc/s5/lxml-ep2008.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.456)
- **Top Global Matches:** file_cluster_13: 5.456, file_cluster_2: 8.019, file_cluster_11: 8.477
- **Magnitude:** 593.66 | **LOC:** 1359 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.759; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (11.6%), Debt Markers (formerly Tech Debt) (8.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1925`, `args: 82`, `func_start: 2`, `class_start: 178`
* *Risk/State:* `planned_debt: 4`
* *Architecture:* `io: 19`, `api: 64`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` opera.css, outline.css, print.css, slides.css, slides.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lxml-6.0.2/doc/s5/ui/default/slides.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.324)
- **Top Global Matches:** file_cluster_7: 11.324, file_cluster_12: 11.431, file_cluster_4: 11.895
- **Magnitude:** 591.72 | **LOC:** 552 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.058; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keys` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* // 'keys' code adapted from MozPoint (http://mozpoint.mozdev.org/)
  * `go` **(Compute Cores)** (Impact: 28.9)
  * `getIncrementals` **(Compute Cores)** (Impact: 21.5)
  * `clicker` **(Compute Cores)** (Impact: 19.2)
  * `findSlide` **(Compute Cores)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 133`, `args: 30`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 4`, `state_mutation: 94`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002732
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `lxml-6.0.2/src/lxml/html/_html5builder.py` (PYTHON) | Magnitude: 113.66 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 38, structural_boundaries: 20, core_var_decl: 14
- `lxml-6.0.2/doc/s5/ui/default/pretty.css` (CSS) | Magnitude: 0.94 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: class_start: 297, indent_spaces: 13, dead_code: 6, safety_bypasses: 4
- `lxml-6.0.2/src/lxml/tests/test_htmlparser.py` (PYTHON) | Magnitude: 457.22 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 585, state_mutation: 193, core_var_decl: 190, design_snake_case: 173
- `lxml-6.0.2/src/lxml/html/html5parser.py` (PYTHON) | Magnitude: 252.7 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 121, branch: 50, structural_boundaries: 50, core_var_decl: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lxml-6.0.2/src/lxml/html/tests/test_html5parser.py` (PYTHON) | Magnitude: 296.46 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 281, structural_boundaries: 124, core_var_decl: 107, design_snake_case: 96
- `lxml-6.0.2/benchmark/bench_xslt.py` (PYTHON) | Magnitude: 5.7 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, api: 2, import: 2
- `lxml-6.0.2/src/lxml/tests/test_classlookup.py` (PYTHON) | Magnitude: 301.44 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 283, state_mutation: 84, structural_boundaries: 80, core_var_decl: 77
- `lxml-6.0.2/src/lxml/tests/test_etree.py` (PYTHON) | Magnitude: 3697.28 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 4614, core_var_decl: 1675, state_mutation: 1672, design_snake_case: 1363
- `lxml-6.0.2/src/lxml/tests/test_external_document.py` (PYTHON) | Magnitude: 59.58 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 27, structural_boundaries: 19, core_var_decl: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `lxml-6.0.2/src/lxml/includes/etreepublic.pxd` (PYTHON) | Magnitude: 81.68 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 89, args: 45, func_start: 45, unreferenced_by_name: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lxml-6.0.2/src/lxml/apihelpers.pxi` (PYTHON) | Magnitude: 1777.84 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1181, branch: 445, state_mutation: 267, core_var_decl: 263
- `lxml-6.0.2/src/lxml/html/_difflib.py` (PYTHON) | Magnitude: 1137.76 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 710, branch: 227, core_var_decl: 186, design_snake_case: 181

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `lxml-6.0.2/src/lxml/tests/test_builder.py` (PYTHON) | Magnitude: 34.66 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 24, api: 11, test: 11
- `lxml-6.0.2/doc/s5/ui/default/slides.js` (JAVASCRIPT) | Magnitude: 591.72 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 437, branch: 186, structural_boundaries: 133, core_var_decl: 129

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lxml-6.0.2/src/lxml/html/__init__.py` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 100.0%)
- `lxml-6.0.2/src/lxml/parser.pxi` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 100.0%)
- `lxml-6.0.2/src/lxml/etree.pyx` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)
- `lxml-6.0.2/src/lxml/html/diff.py` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)
- `lxml-6.0.2/src/lxml/xslt.pxi` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lxml-6.0.2/src/lxml/__init__.py` -> **Severity: 7.494** (Embedded: 0.1227 * Error Risk: 61.0979%)
- `lxml-6.0.2/src/lxml/tests/common_imports.py` -> **Severity: 4.781** (Embedded: 0.0765 * Error Risk: 62.4966%)
- `lxml-6.0.2/doc/html/apidoc/_static/language_data.js` -> **Severity: 3.911** (Embedded: 0.0444 * Error Risk: 88.0556%)
- `lxml-6.0.2/src/lxml/parser.pxi` -> **Severity: 3.003** (Embedded: 0.0391 * Error Risk: 76.8621%)
- `lxml-6.0.2/doc/html/apidoc/_static/searchtools.js` -> **Severity: 2.685** (Embedded: 0.0444 * Error Risk: 60.4705%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lxml-6.0.2/src/lxml/tests/common_imports.py` -> **Severity: 2201.624** (Blast Radius: 23.155 * Doc Risk: 95.082%)
- `lxml-6.0.2/doc/html/apidoc/_static/searchtools.js` -> **Severity: 1265.733** (Blast Radius: 17.26 * Doc Risk: 73.3333%)
- `lxml-6.0.2/doc/html/apidoc/_static/language_data.js` -> **Severity: 863.0** (Blast Radius: 17.26 * Doc Risk: 50.0%)
- `lxml-6.0.2/src/lxml/cssselect.py` -> **Severity: 859.3** (Blast Radius: 8.593 * Doc Risk: 100.0%)
- `lxml-6.0.2/src/lxml/parser.pxi` -> **Severity: 677.3** (Blast Radius: 9.378 * Doc Risk: 72.2222%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 151 literal sites + 4 sites through wrappers = 155
- **`panics_and_aborts`:** 535 literal sites + 10 sites through wrappers = 545

- `decode` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `lxml-6.0.2/src/lxml/html/_difflib.py`
- `print_deprecated_option` (function, debug_prints, primitive): 3 call sites in 1 files -- `lxml-6.0.2/setupinfo.py`
- `_raise_serialization_error` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `lxml-6.0.2/src/lxml/serializer.pxi`
- `annotate` (function, debug_prints, primitive): 1 call sites in 1 files -- `lxml-6.0.2/src/lxml/html/_diffcommand.py`
- `annotate` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lxml-6.0.2/src/lxml/html/_diffcommand.py`
- `schematron_schema_valid` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lxml-6.0.2/src/lxml/isoschematron/__init__.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 14858 call pairs -- scoped 20.6%, unique 0.0%, ambiguous 25.1%, external 54.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 14150 | 21.1% | 0.0% | 26.3% | 52.6% |
| javascript | 332 | 17.5% | 0.0% | 0.6% | 81.9% |
| html | 288 | 0.0% | 0.0% | 0.0% | 100.0% |
| c | 62 | 3.2% | 0.0% | 0.0% | 96.8% |
| shell | 26 | 23.1% | 0.0% | 0.0% | 76.9% |

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
