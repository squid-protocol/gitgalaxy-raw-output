# ARCHITECTURAL_BRIEF: fonttools
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
- **Scope:** 580 analyzed artifact(s), 136406 LOC.
- **Load-bearing artifact:** `fonttools-4.62.1/Lib/fontTools/ttLib/ttFont.py` -- 148 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `fonttools-4.62.1/Lib/fontTools/ttLib/tables/__init__.py` -- pulls in 83 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `fonttools-4.62.1/Lib/fontTools/subset/__init__.py` at magnitude 5022.56 (structural weight, not risk).
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
| Total Artifacts | 2101 |
| Analyzed Artifacts (Scanned) | 580 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1521 |
| Total LOC | 136406 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 27.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4524 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2192 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 23.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9697 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 52 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 532 | 136368 | 91.7% |
| PLAINTEXT | 37 | 0 | 6.4% |
| MARKDOWN | 4 | 0 | 0.7% |
| XML | 4 | 0 | 0.7% |
| MAKEFILE | 1 | 10 | 0.2% |
| BATCH | 1 | 27 | 0.2% |
| JSON | 1 | 1 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 580 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 21%, Data / Markup / Trivial 20%, Large Core Modules (3) 17%, Large Core Modules (2) 16%, Many-Argument Workhorses Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 538 | 92.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 41 | 7.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1521*

**Composition by Extension & Reason:**
- `.ttx`: 414x Excluded (Unsupported Extension: '.ttx')
- `.otf`: 214x Excluded (Explicitly Denied Extension: '.otf')
- `.rst`: 210x Excluded (Unsupported Extension: '.rst')
- `.gdef`: 153x Excluded (Unsupported Extension: '.GDEF')
- `.fea`: 151x Excluded (Unsupported Extension: '.fea')
- `.gsub`: 108x Excluded (Unsupported Extension: '.GSUB')
- `.gpos`: 102x Excluded (Unsupported Extension: '.GPOS')
- `.designspace`: 67x Excluded (Unsupported Extension: '.designspace')
- `.cmap`: 21x Excluded (Unsupported Extension: '.cmap')
- `.ttf`: 16x Excluded (Explicitly Denied Extension: '.ttf')
- `.glif`: 9x Excluded (Unsupported Extension: '.glif')
- `.bin`: 6x Excluded (Unsupported Extension: '.bin')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 192 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 5234 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3640 LOC)
- `.pdf`: 4x Excluded (Explicitly Denied Extension: '.pdf')
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 32.5 | 28.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.8 | 60.3 | 60.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 26.0 | 15.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 16.9 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 50.2 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.9 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.0 | 98.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2655 | 265 | 10 | `fonttools-4.62.1/Lib/fontTools/ufoLib/__init__.py` |
| cleanup | 75 | 30 | 0 | `fonttools-4.62.1/Tests/ttLib/woff2_test.py` |
| guards | 6624 | 372 | 27 | `fonttools-4.62.1/Tests/colorLib/builder_test.py` |
| danger | 3837 | 412 | 14 | `fonttools-4.62.1/Lib/fontTools/ufoLib/glifLib.py` |
| concurrency | 161 | 47 | 0 | `fonttools-4.62.1/Lib/fontTools/cffLib/specializer.py` |
| connectivity | 8407 | 484 | 31 | `fonttools-4.62.1/Lib/fontTools/ttLib/tables/otConverters.py` |
| io | 1325 | 258 | 6 | `fonttools-4.62.1/Tests/designspaceLib/designspace_test.py` |
| crypto | 3 | 3 | 0 | `fonttools-4.62.1/Lib/fontTools/pens/hashPointPen.py` |
| ipc | 20 | 7 | 0 | `fonttools-4.62.1/Lib/fontTools/diff/__init__.py` |
| time | 18 | 7 | 0 | `fonttools-4.62.1/Tests/misc/loggingTools_test.py` |
| serialization | 2 | 2 | 0 | `fonttools-4.62.1/Lib/fontTools/misc/textTools.py` |
| regex | 91 | 38 | 0 | `fonttools-4.62.1/Lib/fontTools/misc/psLib.py` |
| events | 66 | 17 | 0 | `fonttools-4.62.1/Lib/fontTools/misc/psCharStrings.py` |
| tests | 3532 | 177 | 16 | `fonttools-4.62.1/Tests/feaLib/parser_test.py` |
| docs | 2377 | 322 | 9 | `fonttools-4.62.1/Tests/ufoLib/GLIF2_test.py` |
| debt | 706 | 151 | 3 | `fonttools-4.62.1/Lib/fontTools/misc/psCharStrings.py` |
| mutation | 62031 | 465 | 270 | `fonttools-4.62.1/Tests/ufoLib/UFO2_test.py` |
| dead_code | 2557 | 205 | 10 | `fonttools-4.62.1/Tests/feaLib/parser_test.py` |
| credential | 0 | 0 | 0 | - |
| threat | 83 | 19 | 0 | `fonttools-4.62.1/Tests/ttLib/tables/C_O_L_R_test.py` |
| ml_ai | 10 | 6 | 0 | `fonttools-4.62.1/Lib/fontTools/varLib/plot.py` |
| ui | 15 | 5 | 0 | `fonttools-4.62.1/Tests/pens/pointInsidePen_test.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `fonttools-4.62.1/Tests/designspaceLib/designspace_test.py` (Hits: 88)
- `fonttools-4.62.1/Tests/ufoLib/UFOConversion_test.py` (Hits: 81)
- `fonttools-4.62.1/Tests/varLib/varLib_test.py` (Hits: 79)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ttFont.py** (`fonttools-4.62.1/Lib/fontTools/ttLib/ttFont.py`) — 148 inbound connections
2. **__init__.py** (`fonttools-4.62.1/Lib/fontTools/ttLib/__init__.py`) — 146 inbound connections
3. **textTools.py** (`fonttools-4.62.1/Lib/fontTools/misc/textTools.py`) — 123 inbound connections
4. **__init__.py** (`fonttools-4.62.1/Lib/fontTools/__init__.py`) — 79 inbound connections
5. **__init__.py** (`fonttools-4.62.1/Lib/fontTools/misc/__init__.py`) — 64 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`fonttools-4.62.1/Lib/fontTools/ttLib/tables/__init__.py`) — 83 outbound dependencies
2. **__init__.py** (`fonttools-4.62.1/Lib/fontTools/varLib/__init__.py`) — 38 outbound dependencies
3. **__init__.py** (`fonttools-4.62.1/Lib/fontTools/varLib/instancer/__init__.py`) — 29 outbound dependencies
4. **__init__.py** (`fonttools-4.62.1/Lib/fontTools/subset/__init__.py`) — 28 outbound dependencies
5. **otTables.py** (`fonttools-4.62.1/Lib/fontTools/ttLib/tables/otTables.py`) — 28 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_gen` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/varLib/interpolatable.py`) -> Impact: **301.4** | LOC: 456
- `main` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/varLib/interpolatable.py`) -> Impact: **215.0** | LOC: 594
  * *Intent:* """Test for interpolatability issues between fonts"""
- `draw_glyph` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/varLib/interpolatablePlot.py`) -> Impact: **214.7** | LOC: 273
- `instantiateCFF2` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/varLib/instancer/__init__.py`) -> Impact: **206.3** | LOC: 263
- `instantiateVariableFont` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/varLib/mutator.py`) -> Impact: **201.5** | LOC: 273
  * *Intent:* """Generate a static instance from a variable TTFont and a dictionary defining the desired location along the variable font's axes. The location value...
- `specializeCommands` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/cffLib/specializer.py`) -> Impact: **186.5** | LOC: 300
- `_extractSubSpace` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/designspaceLib/split.py`) -> Impact: **140.3** | LOC: 214
- `_read` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/tfmLib.py`) -> Impact: **134.4** | LOC: 263
- `_readGlyphFromTreeFormat2` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/ufoLib/glifLib.py`) -> Impact: **115.5** | LOC: 105
- `add_problem` **(Many-Argument Workhorses)** (@ `fonttools-4.62.1/Lib/fontTools/varLib/interpolatablePlot.py`) -> Impact: **112.4** | LOC: 337

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `fonttools-4.62.1/Lib/fontTools/ttLib/tables` | 96 | 25396.08 | 35.87% | 7.33% |
| `fonttools-4.62.1/Lib/fontTools/varLib` | 23 | 12710.32 | 58.62% | 11.58% |
| `fonttools-4.62.1/Lib/fontTools/misc` | 36 | 8195.12 | 39.74% | 6.68% |
| `fonttools-4.62.1/Lib/fontTools/feaLib` | 10 | 7766.44 | 34.32% | 16.87% |
| `fonttools-4.62.1/Lib/fontTools/cffLib` | 6 | 5888.18 | 75.15% | 16.58% |
| `fonttools-4.62.1/Lib/fontTools/ttLib` | 13 | 5742.48 | 43.17% | 6.3% |
| `fonttools-4.62.1/Lib/fontTools/subset` | 5 | 5572.6 | 49.98% | 8.25% |
| `fonttools-4.62.1/Tests/ttLib/tables` | 47 | 5134.48 | 16.43% | 0.0% |
| `fonttools-4.62.1/Lib/fontTools/ufoLib` | 11 | 5008.66 | 36.1% | 15.56% |
| `fonttools-4.62.1/Lib/fontTools/pens` | 29 | 4020.36 | 41.46% | 29.54% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `fonttools-4.62.1/Lib/fontTools/misc/psCharStrings.py` -> **99.9994%** Exposure
- `fonttools-4.62.1/Lib/fontTools/pens/qtPen.py` -> **99.9925%** Exposure
- `fonttools-4.62.1/Lib/fontTools/pens/wxPen.py` -> **99.9925%** Exposure
- `fonttools-4.62.1/Snippets/print-json.py` -> **99.9666%** Exposure
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/L_T_S_H_.py` -> **99.8499%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `fonttools-4.62.1/Lib/fontTools/afmLib.py` -> **100.0%** Exposure
- `fonttools-4.62.1/Lib/fontTools/cffLib/CFF2ToCFF.py` -> **100.0%** Exposure
- `fonttools-4.62.1/Lib/fontTools/cffLib/CFFToCFF2.py` -> **100.0%** Exposure
- `fonttools-4.62.1/Lib/fontTools/cffLib/__init__.py` -> **100.0%** Exposure
- `fonttools-4.62.1/Lib/fontTools/cffLib/specializer.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `fonttools-4.62.1/Tests/feaLib/parser_test.py` -> **209** Orphaned Functions | **0** Duplicates
- `fonttools-4.62.1/Tests/ttLib/woff2_test.py` -> **95** Orphaned Functions | **2** Duplicates
- `fonttools-4.62.1/Tests/ufoLib/GLIF2_test.py` -> **94** Orphaned Functions | **0** Duplicates
- `fonttools-4.62.1/Tests/subset/subset_test.py` -> **87** Orphaned Functions | **0** Duplicates
- `fonttools-4.62.1/Tests/ttx/ttx_test.py` -> **87** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2906` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `fonttools-4.62.1/Lib/fontTools/subset/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.95)
- **Top Global Matches:** file_cluster_4: 6.95, file_cluster_6: 8.679, file_cluster_12: 13.297
- **Magnitude:** 5022.56 | **LOC:** 4097 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 1.309; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.9%)
- **Documentation Coverage:** 88.2793% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `closure_glyphs` **(Many-Argument Workhorses)** (Impact: 97.5)
  * `subset_glyphs` **(Many-Argument Workhorses)** (Impact: 80.6)
  * `_closure_glyphs` **(Many-Argument Workhorses)** (Impact: 74.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `parse_opts` **(Many-Argument Workhorses)** (Impact: 69.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 771 instances
* *State Mutation (weighted view):* 2413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1034`, `structural_boundaries: 523`, `args: 198`, `func_start: 179`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 871`, `dead_code: 3`, `planned_debt: 26`, `fragile_debt: 7`, `duplicate_logic: 4`
* *Architecture:* `io: 11`, `api: 172`, `import: 30`
* *Defense:* `safety: 57`, `doc: 24`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.309
  * `Choke Point (Betweenness):` 0.000657 | `Ripple Effect (Closeness):` 0.003454
  * `Imports (Out-Degree: 24):` __future__, array, collections, fontTools, fontTools.colorLib.builder, fontTools.colorLib.unbuilder, fontTools.misc.cliTools, fontTools.misc.loggingTools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/cffLib/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.432)
- **Top Global Matches:** file_cluster_12: 6.432, file_cluster_15: 8.127, file_cluster_4: 8.528
- **Magnitude:** 3615.8 | **LOC:** 3695 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **14**; blast radius 2.125; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.8%)
- **Documentation Coverage:** 93.2161% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromXML` **(Many-Argument Workhorses)** (Impact: 64.6)
    * *Intent:* """Reads data from the XML element into the ``CFFFontSet`` object."""
  * `compile` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* """Write the object back into binary representation onto the given file. ``file`` should be a file h...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `getChildren` **(Defensive Guards)** (Impact: 37.4)
  * `_read` **(Many-Argument Workhorses)** (Impact: 36.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 614 instances
* *State Mutation (weighted view):* 1972
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 496`, `args: 216`, `func_start: 216`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 744`, `fragile_debt: 2`, `duplicate_logic: 22`
* *Architecture:* `api: 219`, `import: 18`
* *Defense:* `safety: 108`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.125
  * `Choke Point (Betweenness):` 0.006958 | `Ripple Effect (Closeness):` 0.066266
  * `Imports (Out-Degree: 12):` .CFF2ToCFF, .CFFToCFF2, .transforms, array, fontTools.misc, fontTools.misc.arrayTools, fontTools.misc.textTools, fontTools.ttLib...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/tables/otTables.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.832)
- **Top Global Matches:** file_cluster_12: 6.832, file_cluster_7: 9.272, file_cluster_5: 9.388
- **Magnitude:** 3542.26 | **LOC:** 2704 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **28**; blast radius 6.072; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (88.1%), Guard Balance (formerly Safety Score) (88.0%), Complexity Load (formerly Cognitive Load) (85.6%)
- **Documentation Coverage:** 97.2789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decompile` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `splitPairPos` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `fromXML` **(Many-Argument Workhorses)** (Impact: 35.9)
  * `fromXML` **(Many-Argument Workhorses)** (Impact: 33.4)
  * `toXML` **(Many-Argument Workhorses)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 603 instances
* *State Mutation (weighted view):* 2047
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 404`, `args: 152`, `func_start: 135`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 81`, `high_risk_execution: 1`, `state_mutation: 841`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 3`
* *Architecture:* `api: 148`, `import: 30`
* *Defense:* `safety: 74`, `doc: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.072
  * `Choke Point (Betweenness):` 0.01268 | `Ripple Effect (Closeness):` 0.1612
  * `Imports (Out-Degree: 17):` .otBase, .otConverters, .otData, array, collections, copy, enum, fontTools.feaLib.lookupDebugInfo...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/designspaceLib/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.432)
- **Top Global Matches:** file_cluster_4: 7.432, file_cluster_12: 8.802, file_cluster_5: 9.79
- **Magnitude:** 3271.78 | **LOC:** 3347 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **16**; blast radius 7.123; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.6%), Connectivity (formerly Api Exposure) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 48.0315% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_readSingleInstanceElement` **(Many-Argument Workhorses)** (Impact: 79.3)
  * `write` **(Many-Argument Workhorses)** (Impact: 61.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 60.3)
  * `_addInstance` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `_addSource` **(Many-Argument Workhorses)** (Impact: 41.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 539 instances
* *State Mutation (weighted view):* 1758
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 511`, `structural_boundaries: 306`, `args: 136`, `func_start: 136`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 680`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `io: 13`, `api: 122`, `import: 19`
* *Defense:* `safety: 29`, `doc: 176`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.123
  * `Choke Point (Betweenness):` 0.000233 | `Ripple Effect (Closeness):` 0.154128
  * `Imports (Out-Degree: 4):` __future__, argparse, collections, copy, fontTools.misc, fontTools.misc.loggingTools, fontTools.misc.textTools, fontTools.varLib.models...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/otlLib/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.11)
- **Top Global Matches:** file_cluster_12: 7.11, file_cluster_7: 8.815, file_cluster_5: 9.04
- **Magnitude:** 3165.14 | **LOC:** 3482 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **17**; blast radius 1.83; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.3%), Connectivity (formerly Api Exposure) (82.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 68.4685% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `promote_lookup_type` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* # https://github.com/fonttools/fonttools/issues/612 # A multiple substitution may have a single dest...
  * `buildLookup` **(Many-Argument Workhorses)** (Impact: 40.2)
    * *Intent:* """Turns a collection of rules into a lookup. A Lookup (as defined in the `OpenType Spec <https://do...
  * `buildFormat2Subtable` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `_buildMathGlyphInfo` **(Many-Argument Workhorses)** (Impact: 34.6)
  * `buildSinglePos` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* """Builds a list of single adjustment (GPOS1) subtables. This builds a list of SinglePos subtables f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 521 instances
* *State Mutation (weighted view):* 1730
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 412`, `args: 177`, `func_start: 171`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 88`, `state_mutation: 688`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 156`, `import: 17`
* *Defense:* `safety: 49`, `doc: 71`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.83
  * `Choke Point (Betweenness):` 0.004185 | `Ripple Effect (Closeness):` 0.086259
  * `Imports (Out-Degree: 11):` __future__, collections, copy, fontTools, fontTools.feaLib.ast, fontTools.misc.fixedTools, fontTools.misc.loggingTools, fontTools.misc.roundTools...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/tables/_g_l_y_f.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.12)
- **Top Global Matches:** file_cluster_4: 5.12, file_cluster_12: 10.07, file_cluster_6: 10.748
- **Magnitude:** 2860.64 | **LOC:** 2303 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **26**; blast radius 3.901; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.1%)
- **Documentation Coverage:** 58.8235% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Many-Argument Workhorses)** (Impact: 65.5)
    * *Intent:* """Draws the glyph using the supplied pen object. Arguments: pen: An object conforming to the pen pr...
  * `trim` **(Many-Argument Workhorses)** (Impact: 53.1)
    * *Intent:* """Remove padding and, if requested, hinting, from a glyph. This works on both expanded and compacte...
  * `fromXML` **(Many-Argument Workhorses)** (Impact: 51.2)
  * `dropImpliedOnCurvePoints` **(Compute Cores)** (Impact: 47.7)
    * *Intent:* """Drop impliable on-curve points from the (simple) glyph or glyphs. In TrueType glyf outlines, on-c...
  * `compileDeltasForSpeed` **(Many-Argument Workhorses)** (Impact: 44.8)
    * *Intent:* # uses widest representation needed, for all deltas. compressedFlags = bytearray() compressedXs = by...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 505 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1609
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 317`, `args: 103`, `func_start: 101`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 599`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 5`, `api: 73`, `import: 28`
* *Defense:* `safety: 76`, `doc: 49`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.901
  * `Choke Point (Betweenness):` 0.004507 | `Ripple Effect (Closeness):` 0.198508
  * `Imports (Out-Degree: 13):` .DefaultTable, .ttProgram, array, collections, doctest, enum, fontTools, fontTools.misc...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/feaLib/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.7)
- **Top Global Matches:** file_cluster_4: 5.7, file_cluster_12: 10.692, file_cluster_15: 10.852
- **Magnitude:** 2836.1 | **LOC:** 2396 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.93; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.2%), Connectivity (formerly Api Exposure) (78.9%)
- **Documentation Coverage:** 93.1373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_block_` **(Many-Argument Workhorses)** (Impact: 93.8)
  * `parse_substitute_` **(Compute Cores)** (Impact: 85.9)
  * `parse_glyphclass_` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* # Parses a glyph class, either named or anonymous, or (if # ``bool(accept_glyphname)``) a glyph name...
  * `parse_glyph_pattern_` **(Many-Argument Workhorses)** (Impact: 53.1)
    * *Intent:* # Parses a glyph pattern, including lookups and context, e.g.:: # # a b # a b c' d e # a b c' lookup...
  * `make_glyph_range_` **(Many-Argument Workhorses)** (Impact: 49.2)
    * *Intent:* """(location, "a.sc", "d.sc") --> ["a.sc", "b.sc", "c.sc", "d.sc"]"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 458 instances
* *State Mutation (weighted view):* 1446
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 567`, `structural_boundaries: 345`, `args: 104`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 530`
* *Architecture:* `io: 2`, `api: 103`, `import: 10`
* *Defense:* `safety: 47`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.93
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.016391
  * `Imports (Out-Degree: 7):` fontTools.feaLib.ast, fontTools.feaLib.error, fontTools.feaLib.lexer, fontTools.feaLib.variableScalar, fontTools.misc.encodingTools, fontTools.misc.loggingTools, fontTools.misc.textTools, logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/feaLib/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.406)
- **Top Global Matches:** file_cluster_4: 8.406, file_cluster_12: 8.928, file_cluster_7: 10.953
- **Magnitude:** 2509.32 | **LOC:** 1839 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **26**; blast radius 1.532; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (88.3%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.0213% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 63.0)
  * `build_feature_aalt_` **(Compute Cores)** (Impact: 39.3)
  * `build_OS_2` **(Compute Cores)** (Impact: 38.1)
  * `makeTable` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `makeOpenTypeValueRecord` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* """ast.ValueRecord --> otBase.ValueRecord"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 371 instances
* *State Mutation (weighted view):* 1252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 252`, `args: 94`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 510`, `dead_code: 1`
* *Architecture:* `api: 92`, `import: 26`
* *Defense:* `safety: 29`, `doc: 10`, `sync_locks: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.532
  * `Choke Point (Betweenness):` 0.002053 | `Ripple Effect (Closeness):` 0.023028
  * `Imports (Out-Degree: 21):` __future__, collections, copy, fontTools.feaLib.ast, fontTools.feaLib.error, fontTools.feaLib.lookupDebugInfo, fontTools.feaLib.parser, fontTools.feaLib.variableScalar...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/tables/otConverters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.973)
- **Top Global Matches:** file_cluster_12: 5.973, file_cluster_15: 8.335, file_cluster_16: 9.092
- **Magnitude:** 2375.42 | **LOC:** 2071 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **15**; blast radius 1.673; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.0%), Connectivity (formerly Api Exposure) (89.7%), Guard Balance (formerly Safety Score) (77.0%)
- **Documentation Coverage:** 96.1003% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildConverters` **(Many-Argument Workhorses)** (Impact: 42.9)
    * *Intent:* """Given a table spec from otData.py, build a converter object for each field of the table. This is ...
  * `write` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `xmlRead` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `write` **(Many-Argument Workhorses)** (Impact: 31.8)
  * `read` **(Many-Argument Workhorses)** (Impact: 25.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 983
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 445`, `args: 196`, `func_start: 185`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 2`, `state_mutation: 443`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 222`, `import: 16`
* *Defense:* `safety: 42`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.673
  * `Choke Point (Betweenness):` 0.000811 | `Ripple Effect (Closeness):` 0.123528
  * `Imports (Out-Degree: 9):` .otBase, .otTables, fontTools.misc.fixedTools, fontTools.misc.lazyTools, fontTools.misc.roundTools, fontTools.misc.textTools, fontTools.ttLib, fontTools.ttLib.tables.TupleVariation...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/varLib/merger.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.597)
- **Top Global Matches:** file_cluster_4: 7.597, file_cluster_6: 9.892, file_cluster_12: 12.707
- **Magnitude:** 2357.12 | **LOC:** 1718 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **20**; blast radius 1.162; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Complexity Load (formerly Cognitive Load) (84.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.6879% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge` **(Many-Argument Workhorses)** (Impact: 70.9)
  * `_MarkBasePosFormat1_merge` **(Many-Argument Workhorses)** (Impact: 67.9)
  * `_PairPosFormat2_align_matrices` **(Many-Argument Workhorses)** (Impact: 53.0)
  * `merge` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `_merge_GlyphOrders` **(Stateful Encapsulated Methods)** (Impact: 42.0)
    * *Intent:* """Takes font and list of glyph lists (must be sorted by glyph id), and returns two things: - Combin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 396 instances
* *State Mutation (weighted view):* 1233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 409`, `structural_boundaries: 227`, `args: 71`, `func_start: 69`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 441`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 53`, `import: 21`
* *Defense:* `safety: 57`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.162
  * `Choke Point (Betweenness):` 0.020327 | `Ripple Effect (Closeness):` 0.096446
  * `Imports (Out-Degree: 17):` .errors, copy, enum, fontTools.colorLib.builder, fontTools.misc, fontTools.misc.roundTools, fontTools.misc.treeTools, fontTools.otlLib.builder...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/varLib/instancer/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.792)
- **Top Global Matches:** file_cluster_4: 6.792, file_cluster_12: 10.498, file_cluster_5: 11.802
- **Magnitude:** 2057.76 | **LOC:** 2050 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **29**; blast radius 2.654; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.4%)
- **Documentation Coverage:** 81.0811% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `instantiateCFF2` **(Many-Argument Workhorses)** (Impact: 206.3)
  * `instantiateVariableFont` **(Many-Argument Workhorses)** (Impact: 82.8)
  * `_instantiateVHVAR` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* # TODO(anthrotype) Add support for HVAR/VVAR in CFF2
  * `parseArgs` **(Compute Cores)** (Impact: 37.4)
    * *Intent:* """Parse argv. Returns: 3-tuple (infile, axisLimits, options) axisLimits is either a Dict[str, Optio...
  * `normalize` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* """Return a new NormalizedAxisLimits with normalized -1..0..+1 values. If usingAvar is True, the ava...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 953
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 275`, `args: 68`, `func_start: 67`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 355`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 57`, `import: 33`
* *Defense:* `safety: 39`, `doc: 22`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.654
  * `Choke Point (Betweenness):` 0.001717 | `Ripple Effect (Closeness):` 0.008636
  * `Imports (Out-Degree: 23):` .featureVars, argparse, collections, contextlib, copy, dataclasses, enum, fontTools...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ufoLib/glifLib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.52)
- **Top Global Matches:** file_cluster_5: 9.52, file_cluster_4: 11.123, file_cluster_12: 11.389
- **Magnitude:** 2015.38 | **LOC:** 2124 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **19**; blast radius 3.12; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%), Complexity Load (formerly Cognitive Load) (63.1%)
- **Documentation Coverage:** 77.305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_readGlyphFromTreeFormat2` **(Many-Argument Workhorses)** (Impact: 115.5)
  * `_validateAndMassagePointStructures` **(Many-Argument Workhorses)** (Impact: 103.5)
    * *Intent:* # all formats
  * `addPoint` **(Many-Argument Workhorses)** (Impact: 82.1)
  * `_readGlyphFromTreeFormat1` **(Many-Argument Workhorses)** (Impact: 61.9)
  * `_writeGlyphToBytes` **(Many-Argument Workhorses)** (Impact: 53.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 245 instances
* *State Mutation (weighted view):* 782
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 221`, `args: 81`, `func_start: 81`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 292`
* *Architecture:* `io: 1`, `api: 47`, `import: 25`
* *Defense:* `safety: 78`, `doc: 31`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.12
  * `Choke Point (Betweenness):` 0.001019 | `Ripple Effect (Closeness):` 0.020113
  * `Imports (Out-Degree: 11):` __future__, collections, collections.abc, doctest, fontTools.annotations, fontTools.misc, fontTools.misc.filesystem, fontTools.misc.filesystem._base...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/tables/_c_m_a_p.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.992)
- **Top Global Matches:** file_cluster_4: 7.992, file_cluster_12: 9.19, file_cluster_7: 11.153
- **Magnitude:** 1927.02 | **LOC:** 1598 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 2.903; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `decompile` **(Many-Argument Workhorses)** (Impact: 49.9)
    * *Intent:* # we usually get here indirectly from the subtable __getattr__ function, in which case both args mus...
  * `splitRange` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* # uint16 endCode[segCount] # Ending character code for each segment, last = 0xFFFF. # uint16 reserve...
  * `compile` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `decompile` **(Many-Argument Workhorses)** (Impact: 31.3)
    * *Intent:* # we usually get here indirectly from the subtable __getattr__ function, in which case both args mus...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 343 instances
* *State Mutation (weighted view):* 1157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 172`, `args: 62`, `func_start: 61`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 471`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 9`, `api: 62`, `import: 9`
* *Defense:* `safety: 63`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.903
  * `Choke Point (Betweenness):` 0.002216 | `Ripple Effect (Closeness):` 0.188623
  * `Imports (Out-Degree: 6):` .DefaultTable, array, fontTools.misc.encodingTools, fontTools.misc.textTools, fontTools.ttLib, fontTools.unicode, logging, struct...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/feaLib/ast.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.255)
- **Top Global Matches:** file_cluster_12: 6.255, file_cluster_15: 6.309, file_cluster_16: 8.543
- **Magnitude:** 1866.18 | **LOC:** 2144 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 1.411; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (94.3%), Debt Markers (formerly Tech Debt) (71.7%), Guard Balance (formerly Safety Score) (70.9%)
- **Documentation Coverage:** 69.9115% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asFea` **(Compute Cores)** (Impact: 29.9)
  * `build` **(Defensive Guards)** (Impact: 25.8)
    * *Intent:* """Calls the builder object's ``add_multiple_subst`` callback."""
  * `asFea` **(Compute Cores)** (Impact: 23.7)
  * `asFea` **(Compute Cores)** (Impact: 23.6)
  * `asFea` **(Compute Cores)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 671
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 393`, `args: 203`, `func_start: 202`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 311`, `planned_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 205`, `import: 7`
* *Defense:* `safety: 24`, `doc: 117`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.411
  * `Choke Point (Betweenness):` 0.002877 | `Ripple Effect (Closeness):` 0.074726
  * `Imports (Out-Degree: 5):` collections, fontTools.feaLib.error, fontTools.feaLib.location, fontTools.misc.encodingTools, fontTools.misc.textTools, itertools, weakref
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/mtiLib/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.534)
- **Top Global Matches:** file_cluster_12: 7.534, file_cluster_4: 9.503, file_cluster_7: 9.614
- **Magnitude:** 1820.4 | **LOC:** 1401 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 1.343; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 97.861% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `parsePair` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `parseContext` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `parseGSUBGPOS` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `parseMarkToSomething` **(Many-Argument Workhorses)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 325 instances
* *State Mutation (weighted view):* 1078
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 285`, `args: 103`, `func_start: 78`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 1`, `state_mutation: 428`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 81`, `import: 17`
* *Defense:* `safety: 73`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.343
  * `Choke Point (Betweenness):` 0.000765 | `Ripple Effect (Closeness):` 0.003454
  * `Imports (Out-Degree: 13):` argparse, contextlib, fontTools, fontTools.feaLib.lookupDebugInfo, fontTools.misc, fontTools.misc.testTools, fontTools.otlLib, fontTools.ttLib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/woff2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.557)
- **Top Global Matches:** file_cluster_4: 4.557, file_cluster_6: 9.813, file_cluster_16: 10.737
- **Magnitude:** 1811.76 | **LOC:** 1681 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 1.366; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* """Data class that holds the WOFF2 header major/minor version, any metadata or private data (as byte...
  * `reconstruct` **(Many-Argument Workhorses)** (Impact: 43.6)
  * `main` **(Stateful Encapsulated Methods)** (Impact: 37.9)
    * *Intent:* """Compress and decompress WOFF2 fonts"""
  * `transform` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `_encodeTriplets` **(Many-Argument Workhorses)** (Impact: 35.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 315 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1046
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 182`, `args: 69`, `func_start: 69`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 416`
* *Architecture:* `io: 10`, `api: 37`, `import: 17`
* *Defense:* `safety: 35`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.366
  * `Choke Point (Betweenness):` 0.002263 | `Ripple Effect (Closeness):` 0.133179
  * `Imports (Out-Degree: 11):` argparse, array, brotli, brotlicffi, collections, fontTools, fontTools.misc, fontTools.misc.arrayTools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/misc/psCharStrings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.978)
- **Top Global Matches:** file_cluster_12: 5.978, file_cluster_15: 7.977, file_cluster_7: 9.206
- **Magnitude:** 1786.42 | **LOC:** 1512 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **6**; blast radius 2.66; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (83.1%)
- **Documentation Coverage:** 95.3623% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Defensive Guards)** (Impact: 28.1)
  * `encodeFloat` **(Compute Cores)** (Impact: 28.0)
    * *Intent:* # For CFF only, used in cffLib if f == 0.0: # 0.0 == +0.0 == -0.0 return realZeroBytes # Note: 14 de...
  * `toXML` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `execute` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `encodeInt` **(Many-Argument Workhorses)** (Impact: 23.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 254 instances
* *Api Near Db Sink:* 8 instances
* *State Mutation (weighted view):* 919
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 285`, `args: 175`, `func_start: 174`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 411`, `dead_code: 6`, `fragile_debt: 6`, `duplicate_logic: 42`
* *Architecture:* `api: 175`, `import: 9`
* *Defense:* `safety: 32`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.66
  * `Choke Point (Betweenness):` 0.001041 | `Ripple Effect (Closeness):` 0.067166
  * `Imports (Out-Degree: 4):` fontTools.encodings.StandardEncoding, fontTools.misc.fixedTools, fontTools.misc.textTools, fontTools.pens.boundsPen, logging, struct
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ufoLib/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.882)
- **Top Global Matches:** file_cluster_5: 9.882, file_cluster_4: 10.551, file_cluster_12: 11.346
- **Magnitude:** 1751.9 | **LOC:** 2576 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **19**; blast radius 2.819; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 49.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 95.0)
  * `getGlyphSet` **(Many-Argument Workhorses)** (Impact: 51.3)
  * `renameGlyphSet` **(Many-Argument Workhorses)** (Impact: 40.7)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 37.7)
    * *Intent:* # Only call __fspath__ if path is not already a str or FS object if not isinstance(path, (str, fs.ba...
  * `writeKerning` **(Many-Argument Workhorses)** (Impact: 36.8)
    * *Intent:* # kerning.plist
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 746
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 350`, `structural_boundaries: 386`, `args: 76`, `func_start: 76`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 284`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 24`, `api: 56`, `import: 30`
* *Defense:* `safety: 88`, `doc: 57`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.819
  * `Choke Point (Betweenness):` 0.000473 | `Ripple Effect (Closeness):` 0.019484
  * `Imports (Out-Degree: 9):` __future__, collections, copy, doctest, enum, fontTools.annotations, fontTools.misc, fontTools.misc.filesystem._base...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/varLib/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.067)
- **Top Global Matches:** file_cluster_8: 8.067, file_cluster_3: 18.195, file_cluster_6: 19.183
- **Magnitude:** 1745.14 | **LOC:** 1583 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **38**; blast radius 2.202; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 106.1)
  * `load_designspace` **(Many-Argument Workhorses)** (Impact: 96.4)
    * *Intent:* # TODO: remove this and always assume 'designspace' is a DesignSpaceDocument, # never a file path, a...
  * `_add_avar` **(Many-Argument Workhorses)** (Impact: 94.1)
    * *Intent:* """ Add 'avar' table to font. axes is an ordered dictionary of AxisDescriptor objects. """
  * `_merge_TTHinting` **(Many-Argument Workhorses)** (Impact: 51.4)
    * *Intent:* # TODO: Modify gasp table to deactivate gridfitting for all ranges?
  * `main` **(Compute Cores)** (Impact: 48.4)
    * *Intent:* """Build variable fonts from a designspace file and masters"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 882
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 177`, `args: 34`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 2`, `state_mutation: 326`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 3`
* *Architecture:* `io: 13`, `api: 12`, `import: 38`
* *Defense:* `safety: 28`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.202
  * `Choke Point (Betweenness):` 0.018299 | `Ripple Effect (Closeness):` 0.083666
  * `Imports (Out-Degree: 31):` ..otlLib.builder, .cff, .errors, argparse, collections, copy, doctest, fontTools...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/tables/otBase.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.841)
- **Top Global Matches:** file_cluster_12: 6.841, file_cluster_4: 9.318, file_cluster_7: 9.389
- **Magnitude:** 1689.16 | **LOC:** 1459 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **12**; blast radius 18.876; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.8058% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `_gatherGraphForHarfbuzz` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `_gatherTables` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* # Convert table references in self.items tree to a flat # list of tables in depth-first traversal or...
  * `compile` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* """Compiles the table into binary. Called automatically on save."""
  * `decompile` **(Stateful Encapsulated Methods)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 230 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 776
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 320`, `args: 128`, `func_start: 128`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 4`, `state_mutation: 316`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 117`, `import: 18`
* *Defense:* `safety: 76`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.876
  * `Choke Point (Betweenness):` 0.013389 | `Ripple Effect (Closeness):` 0.16962
  * `Imports (Out-Degree: 4):` .DefaultTable, .otTables, array, enum, fontTools.config, fontTools.misc.textTools, functools, logging...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/ttFont.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.498)
- **Top Global Matches:** file_cluster_5: 7.498, file_cluster_0: 8.911, file_cluster_12: 9.912
- **Magnitude:** 1513.2 | **LOC:** 1682 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **148** in-repo importer(s); it depends on **28**; blast radius 33.868; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (85.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 82.9609% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 103.6)
  * `_saveXML` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `getGlyphSet` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `save` **(Many-Argument Workhorses)** (Impact: 30.8)
  * `_tableToXML` **(Stateful Encapsulated Methods)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 382`, `args: 224`, `func_start: 224`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 178`, `fragile_debt: 2`
* *Architecture:* `io: 13`, `api: 132`, `import: 37`
* *Defense:* `safety: 38`, `doc: 42`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.868
  * `Choke Point (Betweenness):` 0.100468 | `Ripple Effect (Closeness):` 0.289543
  * `Imports (Out-Degree: 20):` .macUtils, .reorderGlyphs, .tables, .tables.DefaultTable, __future__, collections.abc, fontTools, fontTools.config...
  * `Imported By (In-Degree: 148):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/voltLib/voltToFea.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.761)
- **Top Global Matches:** file_cluster_6: 8.761, file_cluster_4: 13.848, file_cluster_8: 14.899
- **Magnitude:** 1310.9 | **LOC:** 912 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 1.328; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.0%)
- **Documentation Coverage:** 90.3226% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_gposLookup` **(Many-Argument Workhorses)** (Impact: 84.6)
  * `_buildFeatureFile` **(Many-Argument Workhorses)** (Impact: 71.9)
  * `_gsubLookup` **(Many-Argument Workhorses)** (Impact: 56.7)
  * `_lookupDefinition` **(Many-Argument Workhorses)** (Impact: 54.9)
  * `_collectStatements` **(Defensive Guards)** (Impact: 44.2)
    * *Intent:* # Collect glyph difinitions first, as we need them to map VOLT glyph names to font glyph name. for s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 232 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 732
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 108`, `args: 29`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 1`, `state_mutation: 268`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 5`, `import: 12`
* *Defense:* `safety: 57`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.328
  * `Choke Point (Betweenness):` 0.000568 | `Ripple Effect (Closeness):` 0.003454
  * `Imports (Out-Degree: 7):` argparse, fontTools, fontTools.feaLib, fontTools.ttLib, fontTools.voltLib, fontTools.voltLib.parser, graphlib, io...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/varLib/interpolatable.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.094)
- **Top Global Matches:** file_cluster_6: 7.094, file_cluster_8: 12.696, file_cluster_4: 13.461
- **Magnitude:** 1218.74 | **LOC:** 1210 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 0.881; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%)
- **Documentation Coverage:** 76.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_gen` **(Many-Argument Workhorses)** (Impact: 301.4)
  * `main` **(Many-Argument Workhorses)** (Impact: 215.0)
    * *Intent:* """Test for interpolatability issues between fonts"""
  * `_populate` **(Defensive Guards)** (Impact: 11.4)
  * `grand_parent` **(Compute Cores)** (Impact: 9.1)
  * `draw` **(Compute Cores)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 191 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 147`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 239`
* *Architecture:* `io: 10`, `api: 9`, `import: 31`
* *Defense:* `safety: 22`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.881
  * `Choke Point (Betweenness):` 0.000122 | `Ripple Effect (Closeness):` 0.001727
  * `Imports (Out-Degree: 18):` .interpolatableHelpers, .interpolatablePlot, .interpolatableTestContourOrder, .interpolatableTestStartingPoint, argparse, base64, collections, fontTools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Lib/fontTools/ttLib/tables/TupleVariation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.85)
- **Top Global Matches:** file_cluster_12: 7.85, file_cluster_9: 8.716, file_cluster_7: 10.179
- **Magnitude:** 1210.48 | **LOC:** 887 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **9**; blast radius 2.093; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 82.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decompileTupleVariation_` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `compileTupleVariationStore` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `encodeDeltaRunAsWords_` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `decompilePoints_` **(Many-Argument Workhorses)** (Impact: 29.3)
    * *Intent:* """(numPoints, data, offset, tableTag) --> ([point1, point2, ...], newOffset)"""
  * `compileDeltaValues_` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* """[value1, value2, value3, ...] --> bytearray Emits a sequence of runs. Each run starts with a byte...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 660
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 123`, `args: 36`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 242`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 36`, `import: 10`
* *Defense:* `safety: 11`, `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.093
  * `Choke Point (Betweenness):` 0.000146 | `Ripple Effect (Closeness):` 0.131361
  * `Imports (Out-Degree: 3):` array, collections, fontTools.misc.fixedTools, fontTools.misc.textTools, fontTools.varLib.iup, logging, struct, sys...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `fonttools-4.62.1/Tests/ttLib/woff2_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.624)
- **Top Global Matches:** file_cluster_15: 6.624, file_cluster_12: 7.585, file_cluster_11: 8.887
- **Magnitude:** 1158.02 | **LOC:** 1535 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.686; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.7%), Connectivity (formerly Api Exposure) (13.5%)
- **Documentation Coverage:** 98.4252% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalise_table` **(Defensive Guards)** (Impact: 19.6)
    * *Intent:* """Return normalised table data. Keep 'font' instance unmodified."""
  * `fontfile` **(I/O & Config Routines)** (Impact: 10.7)
  * `normalise_font` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* """Return normalised font data. Keep 'font' instance unmodified."""
  * `test_checksums` **(Compute Cores)** (Impact: 8.0)
  * `test_normaliseGlyfAndLoca` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 117 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 283`, `args: 129`, `func_start: 127`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 394`, `duplicate_logic: 2`, `unreferenced_by_name: 95`
* *Architecture:* `io: 19`, `api: 142`, `import: 21`
* *Defense:* `safety: 67`, `doc: 3`, `test: 138`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.686
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` brotli, brotlicffi, collections, copy, fontTools, fontTools.misc, fontTools.misc.textTools, fontTools.pens.recordingPen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `fonttools-4.62.1/Tests/ttLib/tables/C_O_L_R_test.py` (PYTHON) | Magnitude: 147.9 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 578, core_var_decl: 228, design_snake_case: 179, structural_boundaries: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `fonttools-4.62.1/Tests/misc/configTools_test.py` (PYTHON) | Magnitude: 22.48 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 28, safety: 15, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/__init__.py` (PYTHON) | Magnitude: 8.1 | Delta: **0.231** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 164, indent_spaces: 83, import: 82, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `fonttools-4.62.1/Tests/ttLib/tables/_t_r_a_k_test.py` (PYTHON) | Magnitude: 154.92 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 274, core_var_decl: 124, design_snake_case: 71, state_mutation: 56
- `fonttools-4.62.1/Tests/misc/visitor_test.py` (PYTHON) | Magnitude: 48.68 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 27, state_mutation: 18, args: 11
- `fonttools-4.62.1/Lib/fontTools/feaLib/ast.py` (PYTHON) | Magnitude: 1866.18 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1361, structural_boundaries: 393, state_mutation: 311, core_var_decl: 295
- `fonttools-4.62.1/Tests/feaLib/variableScalar_test.py` (PYTHON) | Magnitude: 62.3 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 105, core_var_decl: 40, design_snake_case: 40, structural_boundaries: 39
- `fonttools-4.62.1/Tests/ttLib/tables/TupleVariation_test.py` (PYTHON) | Magnitude: 392.84 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 842, core_var_decl: 207, design_snake_case: 143, state_mutation: 118

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `fonttools-4.62.1/Tests/ttLib/reorderGlyphs_test.py` (PYTHON) | Magnitude: 43.06 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 57, state_mutation: 27, core_var_decl: 26, design_snake_case: 25
- `fonttools-4.62.1/Lib/fontTools/ttLib/ttVisitor.py` (PYTHON) | Magnitude: 25.0 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, branch: 4, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `fonttools-4.62.1/Tests/feaLib/error_test.py` (PYTHON) | Magnitude: 8.46 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, test: 6, import: 4
- `fonttools-4.62.1/Tests/ttLib/tables/V_A_R_C_test.py` (PYTHON) | Magnitude: 58.52 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 67, core_var_decl: 30, design_snake_case: 28, state_mutation: 26
- `fonttools-4.62.1/Tests/misc/plistlib_test.py` (PYTHON) | Magnitude: 317.36 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 168, core_var_decl: 138, design_snake_case: 114
- `fonttools-4.62.1/Lib/fontTools/merge/__init__.py` (PYTHON) | Magnitude: 190.64 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 139, structural_boundaries: 44, branch: 37, core_var_decl: 37
- `fonttools-4.62.1/Tests/misc/textTools_test.py` (PYTHON) | Magnitude: 2.44 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 8, safety: 5, indent_spaces: 5, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `fonttools-4.62.1/Tests/ttLib/tables/ttProgram_test.py` (PYTHON) | Magnitude: 42.84 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 32, state_mutation: 24, core_var_decl: 23
- `fonttools-4.62.1/Tests/pens/roundingPen_test.py` (PYTHON) | Magnitude: 24.64 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 18, state_mutation: 9, core_var_decl: 9
- `fonttools-4.62.1/Tests/varLib/builder_test.py` (PYTHON) | Magnitude: 37.8 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 34, safety: 13, core_var_decl: 12
- `fonttools-4.62.1/Tests/misc/timeTools_test.py` (PYTHON) | Magnitude: 10.94 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 16, safety: 10, test: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/_l_t_a_g.py` (PYTHON) | Magnitude: 82.02 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 47, state_mutation: 19, structural_boundaries: 16, core_var_decl: 15
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/L_T_S_H_.py` (PYTHON) | Magnitude: 64.1 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 15, state_mutation: 12, core_var_decl: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `fonttools-4.62.1/Lib/fontTools/ttLib/ttFont.py` -> **Severity: 10.047** (Bridge: 0.1005 * Flux: 99.9999%)
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/DefaultTable.py` -> **Severity: 3.519** (Bridge: 0.0352 * Flux: 99.9665%)
- `fonttools-4.62.1/Lib/fontTools/colorLib/builder.py` -> **Severity: 2.403** (Bridge: 0.024 * Flux: 100.0%)
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/C_O_L_R_.py` -> **Severity: 2.355** (Bridge: 0.0236 * Flux: 100.0%)
- `fonttools-4.62.1/Lib/fontTools/varLib/merger.py` -> **Severity: 2.033** (Bridge: 0.0203 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `fonttools-4.62.1/Lib/fontTools/misc/textTools.py` -> **Severity: 25.598** (Embedded: 0.3457 * Error Risk: 74.0444%)
- `fonttools-4.62.1/Lib/fontTools/misc/loggingTools.py` -> **Severity: 25.269** (Embedded: 0.2884 * Error Risk: 87.6273%)
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/DefaultTable.py` -> **Severity: 19.945** (Embedded: 0.2493 * Error Risk: 80.0%)
- `fonttools-4.62.1/Lib/fontTools/ttLib/ttFont.py` -> **Severity: 19.822** (Embedded: 0.2895 * Error Risk: 68.4593%)
- `fonttools-4.62.1/Lib/fontTools/misc/xmlWriter.py` -> **Severity: 17.476** (Embedded: 0.2202 * Error Risk: 79.3584%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `fonttools-4.62.1/Lib/fontTools/misc/textTools.py` -> **Severity: 4330.304** (Blast Radius: 54.478 * Doc Risk: 79.4872%)
- `fonttools-4.62.1/Lib/fontTools/ttLib/ttFont.py` -> **Severity: 2809.72** (Blast Radius: 33.868 * Doc Risk: 82.9609%)
- `fonttools-4.62.1/Lib/fontTools/ttLib/__init__.py` -> **Severity: 2781.3** (Blast Radius: 27.813 * Doc Risk: 100.0%)
- `fonttools-4.62.1/Lib/fontTools/misc/loggingTools.py` -> **Severity: 2636.957** (Blast Radius: 45.205 * Doc Risk: 58.3333%)
- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/DefaultTable.py` -> **Severity: 2306.0** (Blast Radius: 23.06 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 240 literal sites + 5 sites through wrappers = 245
- **`panics_and_aborts`:** 1362 literal sites + 17 sites through wrappers = 1379

- `_raise_serialization_error` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `fonttools-4.62.1/Lib/fontTools/misc/etree.py`
- `raise_exception` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `fonttools-4.62.1/Tests/ttx/ttx_test.py`
- `_make_element` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `fonttools-4.62.1/Lib/fontTools/misc/plistlib/__init__.py`
- `dump` (function, debug_prints, primitive): 2 call sites in 1 files -- `fonttools-4.62.1/Tests/ttLib/tables/C_O_L_R_test.py`
- `usage` (function, debug_prints, primitive): 2 call sites in 1 files -- `fonttools-4.62.1/MetaTools/roundTrip.py`
- `usage` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `fonttools-4.62.1/MetaTools/roundTrip.py`
- `_raise_incompatible_point` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `fonttools-4.62.1/Lib/fontTools/qu2cu/qu2cu.py`
- `dump` (function, debug_prints, primitive): 1 call sites in 1 files -- `fonttools-4.62.1/Tests/ttLib/tables/S_V_G__test.py`
- `getFormatSwitchingBaseTableClass` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `fonttools-4.62.1/Lib/fontTools/ttLib/tables/otBase.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 31528 call pairs -- scoped 40.5%, unique 0.0%, ambiguous 18.8%, external 40.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 31528 | 40.5% | 0.0% | 18.8% | 40.7% |

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
