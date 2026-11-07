# ARCHITECTURAL_BRIEF: pytudes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/norvig/pytudes.git` |
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
- **Scope:** 47 analyzed artifact(s), 7447 LOC.
- **Load-bearing artifact:** `py/lis.py` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ipynb/evs.html` -- pulls in 33 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ipynb/usecs.txt` at magnitude 973.94 (structural weight, not risk).
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
| Total Artifacts | 205 |
| Analyzed Artifacts (Scanned) | 47 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 158 |
| Total LOC | 7447 |
| Volatility Index | 0.043 |
| % Scanned of codebase = | 22.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1837 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6413 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 20 | 2602 | 42.6% |
| PLAINTEXT | 11 | 2 | 23.4% |
| CSV | 6 | 1581 | 12.8% |
| MARKDOWN | 4 | 0 | 8.5% |
| YAML | 2 | 70 | 4.3% |
| HTML | 2 | 2491 | 4.3% |
| JAVA | 2 | 701 | 4.3% |

## 4.1 SOURCE ENCODINGS
All 47 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 53%, Large Core Modules (3) 21%, Compute Cores Files 13%, Generic / Templated Code Files 4%, Parameter Forwarders Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 32 | 68.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 27.7% |
| Static: Minified & Vendor Opaque Mass | 2 | 4.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 158*

**Composition by Extension & Reason:**
- `.ipynb`: 106x Excluded (Unsupported Extension: '.ipynb')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 128458 LOC), 1x Excluded (Monolithic Amalgamation: 333334 LOC exceeds the 150000 LOC backstop), 1x Excluded (Monolithic Amalgamation: 286359 LOC exceeds the 150000 LOC backstop)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.tsv`: 2x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Massive Static Asset Blob: 8655 LOC), 1x Excluded (Massive Static Asset Blob: 42173 LOC)
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.class`: 3x Excluded (Explicitly Denied Extension: '.class')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.md`: 1x Excluded (Lexical Monotony: High structural repetition detected in 49079 LOC)
- `.csv`: 1x Excluded (Massive Static Asset Blob: 6454 LOC)
- `.svg`: 1x Excluded (Static Asset Blob without Intent: 1904 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.2 | 38.7 | 43.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.7 | 49.0 | 62.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 90.4 | 4.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 43.5 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 69.8 | 31.9 | 26.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 24.2 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 69.2 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.8 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 86.7 | 5.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.3 | 72.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 89 | 18 | 7 | `py/ibol.py` |
| cleanup | 7 | 5 | 0 | `py/lettercount.py` |
| guards | 220 | 22 | 17 | `ipynb/Sudoku.java` |
| danger | 139 | 19 | 12 | `py/lispy.py` |
| concurrency | 25 | 5 | 0 | `py/Sudoku.java` |
| connectivity | 433 | 24 | 22 | `ipynb/evs.html` |
| io | 187 | 17 | 4 | `ipynb/evs.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 3 | 1 | 0 | `ipynb/evs.html` |
| serialization | 0 | 0 | 0 | - |
| regex | 19 | 12 | 1 | `py/py2html.py` |
| events | 37 | 2 | 0 | `ipynb/evs.html` |
| tests | 3 | 1 | 0 | `ipynb/Sudoku.java` |
| docs | 149 | 22 | 10 | `ipynb/Sudoku.java` |
| debt | 115 | 22 | 7 | `py/ibol.py` |
| mutation | 1903 | 23 | 82 | `ipynb/evs.html` |
| dead_code | 12 | 4 | 0 | `py/ngrams.py` |
| credential | 7 | 2 | 0 | `ipynb/evs.html` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 38 | 1 | 0 | `ipynb/evs.html` |
| ui | 33 | 1 | 0 | `ipynb/evs.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ipynb/evs.html` (Hits: 136)
- `py/lispy.py` (Hits: 11)
- `py/docex.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lis.py** (`py/lis.py`) — 2 inbound connections
2. **lispy.py** (`py/lispy.py`) — 2 inbound connections
3. **pal3.py** (`py/pal3.py`) — 2 inbound connections
4. **SET.py** (`py/SET.py`) — 1 inbound connections
5. **beal.py** (`py/beal.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **evs.html** (`ipynb/evs.html`) — 33 outbound dependencies
2. **README.md** (`README.md`) — 18 outbound dependencies
3. **ngrams.py** (`py/ngrams.py`) — 10 outbound dependencies
4. **Sudoku.java** (`ipynb/Sudoku.java`) — 6 outbound dependencies
5. **Sudoku.java** (`py/Sudoku.java`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `expand` **(Compute Cores)** (@ `py/lispy.py`) -> Impact: **49.3** | LOC: 51
  * *Intent:* ################ expand
- `copyblock` **(Many-Argument Workhorses)** (@ `py/yaptu.py`) -> Impact: **44.4** | LOC: 48
- `editsR` **(Compute Cores)** (@ `py/ngrams.py`) -> Impact: **39.3** | LOC: 25
- `eval` **(Compute Cores)** (@ `py/lispy.py`) -> Impact: **31.2** | LOC: 36
  * *Intent:* ################ eval (tail recursive)
- `main` **(Compute Cores)** (@ `py/Sudoku.java`) -> Impact: **31.0** | LOC: 26
  * *Intent:* /** Parse command line args and solve puzzles in files. **/
- `edits` **(Compute Cores)** (@ `py/ngrams.py`) -> Impact: **31.0** | LOC: 31
- `creport` **(Compute Cores)** (@ `py/ibol.py`) -> Impact: **29.9** | LOC: 43
- `main` **(Compute Cores)** (@ `ipynb/Sudoku.java`) -> Impact: **28.1** | LOC: 25
  * *Intent:* /** Parse command line args and solve puzzles in files. **/
- `test` **(I/O & Config Routines)** (@ `py/testaccum.py`) -> Impact: **25.9** | LOC: 37
- `eliminate` **(Compute Cores)** (@ `py/sudoku.py`) -> Impact: **25.1** | LOC: 23
  * *Intent:* """Eliminate d from values[s]; propagate when values or places <= 2. Return values, except return False if a contradiction is detected."""

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `py` | 23 | 3909.96 | 49.57% | 6.0% |
| `ipynb` | 16 | 1794.98 | 5.9% | 1.14% |
| `data` | 1 | 40.4 | 0.0% | 0.0% |
| `__monolith__` | 3 | 7.6 | 0.0% | 0.0% |
| `.github/workflows` | 1 | 6.02 | 4.42% | 0.0% |
| `txt` | 2 | 2.0 | 0.0% | 0.0% |
| `data/ngrams` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `py/ngrams.py` -> **90.351%** Exposure
- `py/parse.py` -> **37.7541%** Exposure
- `py/Sudoku.java` -> **9.8621%** Exposure
- `ipynb/Sudoku.java` -> **9.826%** Exposure
- `ipynb/evs.html` -> **8.4932%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ipynb/portman.py` -> **100.0%** Exposure
- `py/SET.py` -> **100.0%** Exposure
- `py/beal.py` -> **100.0%** Exposure
- `py/docex.py` -> **100.0%** Exposure
- `py/lettercount.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `py/ngrams.py` -> **9** Orphaned Functions | **0** Duplicates
- `ipynb/Sudoku.java` -> **1** Orphaned Functions | **0** Duplicates
- `py/Sudoku.java` -> **1** Orphaned Functions | **0** Duplicates
- `py/parse.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `48` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `144` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ipynb/usecs.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 973.94 | **LOC:** 48697 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/lettercount.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.166)
- **Top Global Matches:** file_cluster_15: 6.166, file_cluster_12: 7.607, file_cluster_11: 8.352
- **Magnitude:** 406.04 | **LOC:** 445 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%), Connectivity (formerly Api Exposure) (67.9%)
- **Documentation Coverage:** 86.4865% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stats` **(Compute Cores)** (Impact: 16.3)
  * `columns` **(Compute Cores)** (Impact: 15.9)
  * `getcount` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* """The count for letter sequence s (one or two letters) starting at position i of words of length le...
  * `makecsv` **(Compute Cores)** (Impact: 13.3)
  * `substr` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* """Return the substr of word of given length starting/ending at pos; or None."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 87`, `args: 40`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`
* *Architecture:* `io: 4`, `api: 37`, `import: 6`
* *Defense:* `safety: 1`, `doc: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` __future__, collections, glob, itertools, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/lispy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.874)
- **Top Global Matches:** file_cluster_4: 8.874, file_cluster_12: 11.12, file_cluster_6: 12.788
- **Magnitude:** 369.5 | **LOC:** 317 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 30.145; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (74.9%), Connectivity (formerly Api Exposure) (69.8%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expand` **(Compute Cores)** (Impact: 49.3)
    * *Intent:* ################ expand
  * `eval` **(Compute Cores)** (Impact: 31.2)
    * *Intent:* ################ eval (tail recursive)
  * `read` **(Compute Cores)** (Impact: 16.4)
  * `read_ahead` **(Compute Cores)** (Impact: 13.3)
  * `repl` **(Defensive Guards)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 32 instances
* *High Risk Execution (weighted view):* 11
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 100`, `args: 44`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 13`, `state_mutation: 41`
* *Architecture:* `io: 11`, `api: 26`, `import: 2`
* *Defense:* `safety: 11`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.145
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 0):` cmath, io, math, operator, re, sys
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `py/pal2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.491)
- **Top Global Matches:** file_cluster_12: 6.491, file_cluster_7: 8.416, file_cluster_5: 9.653
- **Magnitude:** 334.54 | **LOC:** 269 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%), Connectivity (formerly Api Exposure) (64.5%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_k_startingwith` **(Stateful Encapsulated Methods)** (Impact: 20.9)
  * `search` **(Compute Cores)** (Impact: 19.8)
  * `consider_candidates` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* """Push a new state with a set of candidate words onto stack."""
  * `report` **(Defensive Guards)** (Impact: 9.2)
  * `reversible_words` **(Compute Cores)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 76`, `args: 27`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 57`
* *Architecture:* `io: 4`, `api: 26`, `import: 2`
* *Defense:* `safety: 23`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` __future__, bisect, random, re, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/ngrams.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.412)
- **Top Global Matches:** file_cluster_4: 7.412, file_cluster_12: 8.059, file_cluster_15: 9.014
- **Magnitude:** 326.6 | **LOC:** 261 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 20.147; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (90.4%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.1831% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `editsR` **(Compute Cores)** (Impact: 39.3)
  * `edits` **(Compute Cores)** (Impact: 31.0)
  * `neighboring_msgs` **(Compute Cores)** (Impact: 13.4)
  * `hillclimb` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `__init__` **(Type Conversions)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 92`, `args: 39`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 35`, `unreferenced_by_name: 9`
* *Architecture:* `api: 35`, `import: 5`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections, doctest, glob, heapq, math, operator, random...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/Sudoku.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.655)
- **Top Global Matches:** file_cluster_12: 7.655, file_cluster_4: 8.953, file_cluster_7: 9.602
- **Magnitude:** 317.66 | **LOC:** 482 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 20.147; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (34.4%)
- **Documentation Coverage:** 8.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 31.0)
    * *Intent:* /** Parse command line args and solve puzzles in files. **/
  * `naked_pairs` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* /** Look for two squares in a unit with the same two possible values, and no other values. ** For ex...
  * `search` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* //////////////////////////////// Search algorithm //////////////////////////////// /** Search for a ...
  * `dual_consistent` **(Compute Cores)** (Impact: 12.8)
    * *Intent:* /** After we eliminate d from possibilities for grid[s], check each unit of s ** and make sure there...
  * `solveList` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* /** Solve a list of puzzles in a single thread. ** repeat -R<number> times; print each puzzle's stat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 84`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 35`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 7`, `import: 2`
* *Defense:* `safety: 3`, `doc: 22`, `sync_locks: 2`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.*, java.lang.Integer.*, java.lang.StringBuilder, java.util.*, java.util.concurrent.CountDownLatch, java.util.stream.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ipynb/Sudoku.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.562)
- **Top Global Matches:** file_cluster_12: 7.562, file_cluster_4: 8.666, file_cluster_7: 9.68
- **Magnitude:** 306.66 | **LOC:** 488 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 20.147; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.2%), Complexity Load (formerly Cognitive Load) (30.7%)
- **Documentation Coverage:** 4.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* /** Parse command line args and solve puzzles in files. **/
  * `naked_pairs` **(Compute Cores)** (Impact: 18.5)
    * *Intent:* /** Look for two squares in a unit with the same two possible values, and no other values. ** For ex...
  * `search` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* //////////////////////////////// Search algorithm //////////////////////////////// /** Search for a ...
  * `verify` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* /** Verify that grid is a solution to the puzzle. **/
  * `dual_consistent` **(Compute Cores)** (Impact: 12.8)
    * *Intent:* /** After we eliminate d from possibilities for grid[s], check each unit of s ** and make sure there...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 84`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 34`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 9`, `doc: 22`, `test: 3`, `sync_locks: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.*, java.lang.Integer.*, java.lang.StringBuilder, java.util.*, java.util.concurrent.CountDownLatch, java.util.stream.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/ibol.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.52)
- **Top Global Matches:** file_cluster_4: 8.52, file_cluster_12: 8.986, file_cluster_15: 9.738
- **Magnitude:** 256.38 | **LOC:** 195 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.9%), Connectivity (formerly Api Exposure) (67.6%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `creport` **(Compute Cores)** (Impact: 29.9)
  * `closure` **(Compute Cores)** (Impact: 12.6)
  * `near` **(Compute Cores)** (Impact: 11.4)
  * `pct_near_another` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* #table(lambda cl: sum(nspecies(c) > 1 for c in cl))
  * `compare` **(Compute Cores)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 56`, `args: 23`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`
* *Architecture:* `io: 2`, `api: 22`, `import: 3`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` __future__, collections, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/pal3.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.837)
- **Top Global Matches:** file_cluster_12: 6.837, file_cluster_15: 7.968, file_cluster_5: 9.387
- **Magnitude:** 254.8 | **LOC:** 171 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 39.136; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%), Connectivity (formerly Api Exposure) (65.1%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check` **(Compute Cores)** (Impact: 16.0)
  * `__init__` **(Compute Cores)** (Impact: 10.7)
  * `search` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* """Depth-first search for palindromes. From the current state, find all applicable actions. Do the f...
  * `do` **(Compute Cores)** (Impact: 9.3)
  * `is_palindrome` **(Compute Cores)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 58`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`
* *Architecture:* `io: 1`, `api: 18`, `import: 2`
* *Defense:* `safety: 20`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 0):` collections, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `py/pal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.188)
- **Top Global Matches:** file_cluster_12: 6.188, file_cluster_15: 7.126, file_cluster_16: 9.196
- **Magnitude:** 244.16 | **LOC:** 156 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 21.154; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.5%)
- **Documentation Coverage:** 78.3784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Compute Cores)** (Impact: 11.5)
  * `search` **(Compute Cores)** (Impact: 10.9)
  * `extend` **(Compute Cores)** (Impact: 10.8)
  * `backtrack` **(Compute Cores)** (Impact: 9.2)
  * `__init__` **(Compute Cores)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 53`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 40`
* *Architecture:* `io: 3`, `api: 19`, `import: 2`
* *Defense:* `safety: 1`, `doc: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 1):` __future__, bisect, os, random, re, string
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/docex.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.715)
- **Top Global Matches:** file_cluster_12: 7.715, file_cluster_9: 9.997, file_cluster_7: 10.043
- **Magnitude:** 215.24 | **LOC:** 238 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%), Connectivity (formerly Api Exposure) (54.9%)
- **Documentation Coverage:** 48.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_docstring` **(Defensive Guards)** (Impact: 20.4)
  * `run_string` **(Defensive Guards)** (Impact: 18.4)
    * *Intent:* """Run a test string, printing inputs and results."""
  * `evaluate` **(Compute Cores)** (Impact: 14.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `main` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* """Run Docex. args should be a list of python filenames. If the first arg is a non-python filename, ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 26`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 5`, `state_mutation: 29`
* *Architecture:* `io: 5`, `api: 13`, `import: 4`
* *Defense:* `safety: 11`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` __future__, glob, re, sys, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ipynb/evs.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 8.737)
- **Top Global Matches:** file_cluster_13: 8.737, file_cluster_12: 8.74, file_cluster_10: 9.371
- **Magnitude:** 197.82 | **LOC:** 1284 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 20.147; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (21.6%), Mutation Surface (formerly State Flux) (19.8%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `itemblur` **(Callbacks & Closures)** (Impact: 1.9)
  * `itemfocus` **(Callbacks & Closures)** (Impact: 1.9)
  * `loadChartbeat` **(Interface Declarations)** (Impact: 1.4)
  * `style` **(State Mutators)** (Impact: 1.1)
  * `gtag` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 407`, `args: 210`, `func_start: 33`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 17`, `fragile_debt: 1`
* *Architecture:* `io: 136`, `api: 118`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 7`, `doc: 10`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` morningconsult.com, s.w.org, apple-touch-icon.png, favicon-16x16.png, favicon-32x32.png, favicon.ico, manifest.json, safari-pinned-tab.svg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ipynb/portman.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.876)
- **Top Global Matches:** file_cluster_5: 7.876, file_cluster_0: 8.791, file_cluster_12: 9.509
- **Magnitude:** 186.38 | **LOC:** 139 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 20.147; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%), Complexity Load (formerly Cognitive Load) (42.0%)
- **Documentation Coverage:** 3.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_bridges` **(Compute Cores)** (Impact: 19.0)
    * *Intent:* """A table of bridges[pre][suf] == (excess, (overlap, word)), e.g. bridges['ar']['c'] == (0, (2, 'ar...
  * `try_bridge` **(Many-Argument Workhorses)** (Impact: 10.9)
    * *Intent:* """Store a new bridge if it has less excess than the previous bridges[pre][suf]."""
  * `natalie` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* """Return a portmantout path containing all words in W."""
  * `bridging_steps` **(Generic / Templated Code)** (Impact: 9.0)
    * *Intent:* """The steps from the shortest bridge that bridges from a suffix of prev_word to a prefix of an unus...
  * `used` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* """Remove word from `W.unused` and, for each prefix, from `W.startswith[pre]`."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 37`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`
* *Architecture:* `io: 2`, `api: 17`, `import: 2`
* *Defense:* `safety: 3`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/sudoku.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.568)
- **Top Global Matches:** file_cluster_15: 7.568, file_cluster_9: 9.292, file_cluster_16: 9.491
- **Magnitude:** 182.54 | **LOC:** 162 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.4%), Connectivity (formerly Api Exposure) (59.0%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eliminate` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* """Eliminate d from values[s]; propagate when values or places <= 2. Return values, except return Fa...
  * `search` **(Defensive Guards)** (Impact: 13.3)
  * `display` **(Compute Cores)** (Impact: 10.3)
    * *Intent:* ################ Display as 2-D grid ################
  * `grid_values` **(Defensive Guards)** (Impact: 10.2)
  * `assign` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* ################ Constraint Propagation ################ """Eliminate all the other values (except d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 44`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `io: 3`, `api: 13`, `import: 1`
* *Defense:* `safety: 8`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/yaptu.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.127)
- **Top Global Matches:** file_cluster_6: 8.127, file_cluster_4: 10.041, file_cluster_12: 16.178
- **Magnitude:** 167.64 | **LOC:** 172 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyblock` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `preproc` **(Compute Cores)** (Impact: 15.2)
  * `repl` **(Defensive Guards)** (Impact: 14.5)
  * `execute` **(Defensive Guards)** (Impact: 3.9)
  * `copyfile` **(Parameter Forwarders)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 19`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 9`, `state_mutation: 31`
* *Architecture:* `io: 4`, `api: 8`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` __future__, os, os.path, re, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/beal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_12: 7.049, file_cluster_7: 8.331, file_cluster_5: 9.894
- **Magnitude:** 151.1 | **LOC:** 160 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.5%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 68.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `beal_modp` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* ############################################################################## """See if any A ** x ...
  * `exponents_upto` **(Compute Cores)** (Impact: 11.7)
  * `make_Apowers_modp` **(Compute Cores)** (Impact: 10.2)
  * `beal` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* """See if any A ** x + B ** y equals some C ** z, with gcd(A, B) == 1. Consider any 1 <= A,B <= max_...
  * `make_Apowers` **(Compute Cores)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 60`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 24`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` __future__, collections, fractions, itertools, math
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/py2html.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.172)
- **Top Global Matches:** file_cluster_12: 6.172, file_cluster_15: 8.188, file_cluster_7: 8.638
- **Magnitude:** 136.68 | **LOC:** 116 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.2%), Connectivity (formerly Api Exposure) (59.4%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert_files` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `num_cmp` **(Type Conversions)** (Impact: 5.5)
  * `num` **(Type Conversions)** (Impact: 4.4)
  * `modulelink` **(Parameter Forwarders)** (Impact: 3.7)
    * *Intent:* """Hyperlink to a module, either locally or on python.org"""
  * `find1` **(Parameter Forwarders)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 35`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`
* *Architecture:* `io: 5`, `api: 11`, `import: 2`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` glob, os, re, string, sys, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/SET.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.539)
- **Top Global Matches:** file_cluster_15: 6.539, file_cluster_10: 8.37, file_cluster_16: 8.822
- **Magnitude:** 117.78 | **LOC:** 135 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (62.1%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tally_game_play` **(Compute Cores)** (Impact: 10.6)
  * `show` **(Type Conversions)** (Impact: 9.2)
  * `tally_initial_layout_no_prior_sets` **(Type Conversions)** (Impact: 7.5)
    * *Intent:* """Simulate N initial deals for each size, keeping tallies for Sets and NoSets, but only when there ...
  * `is_set` **(Compute Cores)** (Impact: 7.4)
  * `tally_initial_layout` **(Type Conversions)** (Impact: 7.4)
    * *Intent:* #### Three experiments
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 35`, `args: 12`, `func_start: 11`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` collections, itertools, random
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/lis.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.6)
- **Top Global Matches:** file_cluster_12: 7.6, file_cluster_7: 9.9, file_cluster_15: 10.293
- **Magnitude:** 105.34 | **LOC:** 133 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 30.145; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eval` **(Defensive Guards)** (Impact: 21.9)
    * *Intent:* ################ eval
  * `read_from_tokens` **(Compute Cores)** (Impact: 10.6)
  * `repl` **(Compute Cores)** (Impact: 4.5)
    * *Intent:* ################ Interaction: A REPL
  * `lispstr` **(Defensive Guards)** (Impact: 4.5)
  * `standard_env` **(Callbacks & Closures)** (Impact: 2.5)
    * *Intent:* ################ Global Environment
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 37`, `args: 22`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 9`, `state_mutation: 19`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.145
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 0):` collections, math, operator
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `py/spell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.125)
- **Top Global Matches:** file_cluster_15: 6.125, file_cluster_16: 8.663, file_cluster_11: 8.756
- **Magnitude:** 95.28 | **LOC:** 107 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.2%), Connectivity (formerly Api Exposure) (56.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `edits1` **(Compute Cores)** (Impact: 16.0)
  * `spelltest` **(Compute Cores)** (Impact: 7.8)
  * `candidates` **(Compute Cores)** (Impact: 7.2)
  * `Testset` **(Compute Cores)** (Impact: 5.9)
  * `known` **(Type Conversions)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 43`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 3`, `api: 9`, `import: 3`
* *Defense:* `safety: 17`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` collections, re, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/pytudes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.719)
- **Top Global Matches:** file_cluster_0: 6.719, file_cluster_15: 7.874, file_cluster_12: 8.294
- **Magnitude:** 85.18 | **LOC:** 280 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.7%), Guard Balance (formerly Safety Score) (56.7%), Connectivity (formerly Api Exposure) (51.8%)
- **Documentation Coverage:** 8.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_newest` **(Generic / Templated Code)** (Impact: 8.3)
    * *Intent:* """Mutate `notebooks['New']` to have a collection of newest notebooks."""
  * `show` **(Compute Cores)** (Impact: 5.2)
  * `format_notebook` **(Parameter Forwarders)** (Impact: 5.1)
    * *Intent:* """Make a markdown table entry for a jupyter/ipython notebook."""
  * `format_python` **(Generic / Templated Code)** (Impact: 4.2)
    * *Intent:* """Make a markdown table entry for a .py file."""
  * `check` **(Interface Declarations)** (Impact: 3.5)
    * *Intent:* """Check that the listing of *.ipynb files matches the README.md file"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 57`, `args: 13`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `io: 1`, `api: 12`, `import: 2`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` re, urllib.request
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/parse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.42)
- **Top Global Matches:** file_cluster_15: 6.42, file_cluster_16: 7.629, file_cluster_2: 7.766
- **Magnitude:** 58.04 | **LOC:** 54 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 20.147; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.8%), Guard Balance (formerly Safety Score) (63.2%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Compute Cores)** (Impact: 16.4)
  * `match` **(Compute Cores)** (Impact: 8.9)
  * `mklist` **(Compute Cores)** (Impact: 4.4)
  * `category` **(Compute Cores)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/testaccum.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.588)
- **Top Global Matches:** file_cluster_6: 9.588, file_cluster_8: 14.148, file_cluster_4: 14.911
- **Magnitude:** 49.56 | **LOC:** 75 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 21.154; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Complexity Load (formerly Cognitive Load) (65.0%), Guard Balance (formerly Safety Score) (56.2%), Connectivity (formerly Api Exposure) (36.4%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(I/O & Config Routines)** (Impact: 25.9)
  * `test1` **(Defensive Guards)** (Impact: 5.5)
  * `expand_accumulations` **(Callbacks & Closures)** (Impact: 1.9)
    * *Intent:* """Replace any accumulation displays in program_text with calls to accumulation. Used to simulate a ...
  * `def` **(Callbacks & Closures)** (Impact: 1.6)
  * `f` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 16`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 5`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` __future__, accum, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `data/latlong.htm` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.729)
- **Top Global Matches:** file_cluster_2: 2.729, file_cluster_17: 5.002, file_cluster_15: 6.333
- **Magnitude:** 40.4 | **LOC:** 1381 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.8%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 40`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/lispytest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.626)
- **Top Global Matches:** file_cluster_9: 9.626, file_cluster_12: 12.584, file_cluster_7: 14.045
- **Magnitude:** 31.96 | **LOC:** 123 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 21.154; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Guard Balance (formerly Safety Score) (56.1%), Connectivity (formerly Api Exposure) (16.4%), Complexity Load (formerly Cognitive Load) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Defensive Guards)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 4`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 2):` __future__, lis, lispy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ipynb/evs.html` (HTML) | Magnitude: 197.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 867, core_var_decl: 576, design_snake_case: 572, decorators: 482

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `py/Sudoku.java` -> **Visali Alagappan** (100.0% isolated ownership) | Magnitude: 317.66
- `py/pytudes.py` -> **Peter Norvig** (100.0% isolated ownership) | Magnitude: 85.18

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `py/lispy.py` -> **Severity: 3.465** (Embedded: 0.0435 * Error Risk: 79.6918%)
- `py/pal3.py` -> **Severity: 3.423** (Embedded: 0.0435 * Error Risk: 78.7243%)
- `py/lis.py` -> **Severity: 3.238** (Embedded: 0.0435 * Error Risk: 74.4762%)
- `py/pal.py` -> **Severity: 1.819** (Embedded: 0.0217 * Error Risk: 83.6658%)
- `py/yaptu.py` -> **Severity: 1.815** (Embedded: 0.0217 * Error Risk: 83.4992%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `py/pal3.py` -> **Severity: 3683.386** (Blast Radius: 39.136 * Doc Risk: 94.1176%)
- `py/lis.py` -> **Severity: 3014.5** (Blast Radius: 30.145 * Doc Risk: 100.0%)
- `py/lispy.py` -> **Severity: 2888.895** (Blast Radius: 30.145 * Doc Risk: 95.8333%)
- `py/lispytest.py` -> **Severity: 2115.4** (Blast Radius: 21.154 * Doc Risk: 100.0%)
- `py/spell.py` -> **Severity: 2115.4** (Blast Radius: 21.154 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1279 call pairs -- scoped 33.4%, unique 0.0%, ambiguous 2.7%, external 63.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 1128 | 32.8% | 0.0% | 3.1% | 64.1% |
| java | 143 | 39.9% | 0.0% | 0.0% | 60.1% |
| html | 8 | 0.0% | 0.0% | 0.0% | 100.0% |

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
