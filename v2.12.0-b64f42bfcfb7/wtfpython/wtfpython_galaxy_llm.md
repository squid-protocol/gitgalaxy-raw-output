# ARCHITECTURAL_BRIEF: wtfpython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/satwikkansal/wtfpython.git` |
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
- **Scope:** 30 analyzed artifact(s), 436 LOC.
- **Load-bearing artifact:** `translations/ru-russian/CONTRIBUTING.md` -- 4 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `irrelevant/obsolete/initial.md` -- pulls in 4 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `irrelevant/notebook_generator.py` at magnitude 356.8 (structural weight, not risk).
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
| Total Artifacts | 44 |
| Analyzed Artifacts (Scanned) | 30 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 14 |
| Total LOC | 436 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.155 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 1.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2857 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 17 | 0 | 56.7% |
| PYTHON | 8 | 408 | 26.7% |
| YAML | 2 | 28 | 6.7% |
| XML | 2 | 0 | 6.7% |
| PLAINTEXT | 1 | 0 | 3.3% |

## 4.1 SOURCE ENCODINGS
All 30 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 80%, Declarative / Non-Code 10%, Generic / Templated Code Files 3%, Interface Declarations Files 3%, Large Core Modules (3) 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12 | 40.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 18 | 60.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 14*

**Composition by Extension & Reason:**
- `.svg`: 4x Excluded (Machine-Generated Source Code Signature: 4 LOC), 2x Excluded (Machine-Generated Source Code Signature: 5 LOC)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ipynb`: 1x Excluded (Unsupported Extension: '.ipynb')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 47.4 | 15.1 | 4.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.6 | 38.8 | 48.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 8.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 23.3 | 3.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 2.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 50.9 | 59.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.6 | 11.8 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1 | 1 | 0 | `irrelevant/obsolete/parse_readme.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 15 | 4 | 1 | `irrelevant/obsolete/parse_readme.py` |
| danger | 28 | 4 | 2 | `irrelevant/notebook_generator.py` |
| concurrency | 1 | 1 | 0 | `.github/workflows/pr.yml` |
| connectivity | 11 | 4 | 1 | `irrelevant/notebook_generator.py` |
| io | 13 | 5 | 2 | `irrelevant/notebook_generator.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `irrelevant/obsolete/generate_contributions.py` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 14 | 3 | 0 | `irrelevant/notebook_generator.py` |
| debt | 19 | 5 | 2 | `snippets/2_tricky_strings.py` |
| mutation | 289 | 7 | 12 | `irrelevant/notebook_generator.py` |
| dead_code | 1 | 1 | 0 | `noxfile.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `irrelevant/notebook_generator.py` (Hits: 4)
- `irrelevant/obsolete/generate_contributions.py` (Hits: 3)
- `irrelevant/obsolete/parse_readme.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`translations/ru-russian/CONTRIBUTING.md`) — 4 inbound connections
2. **mixed_tabs_and_spaces.py** (`mixed_tabs_and_spaces.py`) — 4 inbound connections
3. **CONTRIBUTORS.md** (`translations/ru-russian/CONTRIBUTORS.md`) — 2 inbound connections
4. **bug.md** (`.github/ISSUE_TEMPLATE/bug.md`) — 0 inbound connections
5. **new_snippet.md** (`.github/ISSUE_TEMPLATE/new_snippet.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **initial.md** (`irrelevant/obsolete/initial.md`) — 4 outbound dependencies
2. **notebook_generator.py** (`irrelevant/notebook_generator.py`) — 3 outbound dependencies
3. **generate_contributions.py** (`irrelevant/obsolete/generate_contributions.py`) — 3 outbound dependencies
4. **noxfile.py** (`noxfile.py`) — 3 outbound dependencies
5. **common.md** (`.github/PULL_REQUEST_TEMPLATE/common.md`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse_example_parts` **(Many-Argument Workhorses)** (@ `irrelevant/notebook_generator.py`) -> Impact: **57.1** | LOC: 103
  * *Intent:* """ Parse the given lines and return a dictionary with two keys: build_up, which contains all the text before an H4 (explanation) is encountered, and ...
- `convert_to_cells` **(Many-Argument Workhorses)** (@ `irrelevant/notebook_generator.py`) -> Impact: **16.2** | LOC: 81
  * *Intent:* """ Converts a list of dictionaries containing markdown and code cells into a Jupyter notebook. :param cell_contents: A list of dictionaries, each dic...
- `convert_to_notebook` **(Many-Argument Workhorses)** (@ `irrelevant/notebook_generator.py`) -> Impact: **9.6** | LOC: 32
  * *Intent:* """ Convert a JSON file containing the examples to a Jupyter Notebook. """
- `inspect_and_sanitize_code_lines` **(Compute Cores)** (@ `irrelevant/notebook_generator.py`) -> Impact: **6.6** | LOC: 18
  * *Intent:* """ Remove lines from the beginning of a code block that are not statements. :param lines: A list of strings, each representing a line in the code blo...
- `remove_from_beginning` **(Compute Cores)** (@ `irrelevant/notebook_generator.py`) -> Impact: **5.4** | LOC: 5
- `is_interactive_statement` **(Compute Cores)** (@ `irrelevant/notebook_generator.py`) -> Impact: **4.5** | LOC: 5
- `square` **(Parameter Forwarders)** (@ `mixed_tabs_and_spaces.py`) -> Impact: **3.1** | LOC: 5
- `generate_code_block` **(Parameter Forwarders)** (@ `irrelevant/notebook_generator.py`) -> Impact: **2.5** | LOC: 16
  * *Intent:* """ Generates a code block that executes the given statements. :param statements: The list of statements to execute. :type statements: list(str) """
- `generate_markdown_block` **(Parameter Forwarders)** (@ `irrelevant/notebook_generator.py`) -> Impact: **2.0** | LOC: 12
  * *Intent:* """ Generates a markdown block from a list of lines. """
- `tests` **(Generic / Templated Code)** (@ `noxfile.py`) -> Impact: **1.5** | LOC: 2

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `irrelevant` | 3 | 373.2 | 26.42% | 7.28% |
| `irrelevant/obsolete` | 3 | 217.74 | 28.17% | 10.37% |
| `__monolith__` | 8 | 103.46 | 2.16% | 4.72% |
| `translations/fa-farsi` | 1 | 84.6 | 0.0% | 0.0% |
| `translations/ru-russian` | 4 | 83.02 | 0.0% | 0.0% |
| `snippets` | 2 | 31.76 | 0.0% | 50.0% |
| `images` | 2 | 21.04 | 0.0% | 0.0% |
| `.github/workflows` | 1 | 3.9 | 0.0% | 0.0% |
| `.github/ISSUE_TEMPLATE` | 3 | 3.0 | 0.0% | 0.0% |
| `.github/PULL_REQUEST_TEMPLATE` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `snippets/2_tricky_strings.py` -> **100.0%** Exposure
- `noxfile.py` -> **37.7541%** Exposure
- `irrelevant/obsolete/generate_contributions.py` -> **31.123%** Exposure
- `irrelevant/notebook_generator.py` -> **21.8315%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `irrelevant/notebook_generator.py` -> **100.0%** Exposure
- `irrelevant/obsolete/generate_contributions.py` -> **100.0%** Exposure
- `irrelevant/obsolete/parse_readme.py` -> **100.0%** Exposure
- `irrelevant/insert_ids.py` -> **99.9665%** Exposure
- `snippets/2_tricky_strings.py` -> **91.6827%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `noxfile.py` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `24` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `irrelevant/notebook_generator.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.118)
- **Top Global Matches:** file_cluster_4: 11.118, file_cluster_6: 11.124, file_cluster_12: 14.507
- **Magnitude:** 356.8 | **LOC:** 398 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 23.5083% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_example_parts` **(Many-Argument Workhorses)** (Impact: 57.1)
    * *Intent:* """ Parse the given lines and return a dictionary with two keys: build_up, which contains all the te...
  * `convert_to_cells` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* """ Converts a list of dictionaries containing markdown and code cells into a Jupyter notebook. :par...
  * `convert_to_notebook` **(Many-Argument Workhorses)** (Impact: 9.6)
    * *Intent:* """ Convert a JSON file containing the examples to a Jupyter Notebook. """
  * `inspect_and_sanitize_code_lines` **(Compute Cores)** (Impact: 6.6)
    * *Intent:* """ Remove lines from the beginning of a code block that are not statements. :param lines: A list of...
  * `remove_from_beginning` **(Compute Cores)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 31`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 90`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 8`, `import: 3`
* *Defense:* `safety: 2`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json, os, pprint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `irrelevant/obsolete/parse_readme.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.139)
- **Top Global Matches:** file_cluster_7: 4.139, file_cluster_12: 7.724, file_cluster_5: 8.837
- **Magnitude:** 125.78 | **LOC:** 152 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Complexity Load (formerly Cognitive Load) (37.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 39`
* *Architecture:* `io: 3`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `translations/fa-farsi/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 84.6 | **LOC:** 4230 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 27.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CONTRIBUTING.md, mixed_tabs_and_spaces.py
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 83.6 | **LOC:** 4180 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 27.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CONTRIBUTING.md, mixed_tabs_and_spaces.py
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `translations/ru-russian/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 79.32 | **LOC:** 3966 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 27.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CONTRIBUTING.md, mixed_tabs_and_spaces.py
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `irrelevant/obsolete/initial.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 47.3 | **LOC:** 2365 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 27.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CONTRIBUTING.md, after_board_initialized.png, after_row_initialized.png, mixed_tabs_and_spaces.py
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `irrelevant/obsolete/generate_contributions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.371)
- **Top Global Matches:** file_cluster_7: 5.371, file_cluster_12: 7.928, file_cluster_5: 9.33
- **Magnitude:** 44.66 | **LOC:** 54 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.9%), Complexity Load (formerly Cognitive Load) (46.9%), Debt Markers (formerly Tech Debt) (31.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pprint, re, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `snippets/2_tricky_strings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.252)
- **Top Global Matches:** file_cluster_2: 6.252, file_cluster_17: 7.252, file_cluster_13: 7.741
- **Magnitude:** 21.24 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (45.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 6`, `fragile_debt: 8`
* *Architecture:* None
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `irrelevant/insert_ids.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.619)
- **Top Global Matches:** file_cluster_7: 6.619, file_cluster_14: 7.692, file_cluster_12: 10.226
- **Magnitude:** 15.4 | **LOC:** 25 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (31.9%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 94.033% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_random_id_comment` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `images/logo.svg` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `images/logo_dark_theme.svg` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `snippets/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mixed_tabs_and_spaces.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.048)
- **Top Global Matches:** file_cluster_15: 6.048, file_cluster_2: 6.918, file_cluster_11: 7.329
- **Magnitude:** 7.22 | **LOC:** 8 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 73.882; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (50.0%), Connectivity (formerly Api Exposure) (23.3%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `square` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 73.882
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.137931
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `noxfile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.811)
- **Top Global Matches:** file_cluster_0: 5.811, file_cluster_13: 8.631, file_cluster_2: 9.856
- **Magnitude:** 6.66 | **LOC:** 14 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.9%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (9.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tests` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nox, nox.sessions, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/pr.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.792)
- **Top Global Matches:** file_cluster_2: 5.792, file_cluster_17: 7.039, file_cluster_11: 7.389
- **Magnitude:** 3.9 | **LOC:** 29 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (28.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Write git diff to temp file` **(I/O & Config Routines)** (Impact: 1.3)
  * `Output diff` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `concurrency: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` markdownlint-cli2-action@v17, checkout@v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code-of-conduct.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.5 | **LOC:** 75 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `translations/ru-russian/code-of-conduct.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.42 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CONTRIBUTING.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.32 | **LOC:** 66 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 27.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CONTRIBUTORS.md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `translations/ru-russian/CONTRIBUTING.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.28 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 73.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 73.882
  * `Choke Point (Betweenness):` 0.004926 | `Ripple Effect (Closeness):` 0.137931
  * `Imports (Out-Degree: 1):` CONTRIBUTORS.md
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `.travis.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.145)
- **Top Global Matches:** file_cluster_2: 6.145, file_cluster_17: 7.782, file_cluster_13: 7.892
- **Magnitude:** 1.16 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `script` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/ISSUE_TEMPLATE/bug.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` issues
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/ISSUE_TEMPLATE/new_snippet.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` issues
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/ISSUE_TEMPLATE/translation.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` issues
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/PULL_REQUEST_TEMPLATE/common.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CONTRIBUTING.md, CONTRIBUTORS.md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/PULL_REQUEST_TEMPLATE/new_snippet.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 27.364; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CONTRIBUTING.md, CONTRIBUTORS.md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `irrelevant/notebook_generator.py` (PYTHON) | Magnitude: 356.8 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 226, state_mutation: 90, core_var_decl: 69, design_snake_case: 67

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `mixed_tabs_and_spaces.py` -> **Severity: 7.192** (Embedded: 0.1379 * Error Risk: 52.1415%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `mixed_tabs_and_spaces.py` -> **Severity: 3694.1** (Blast Radius: 73.882 * Doc Risk: 50.0%)
- `irrelevant/insert_ids.py` -> **Severity: 2573.119** (Blast Radius: 27.364 * Doc Risk: 94.033%)
- `noxfile.py` -> **Severity: 1368.2** (Blast Radius: 27.364 * Doc Risk: 50.0%)
- `irrelevant/notebook_generator.py` -> **Severity: 643.281** (Blast Radius: 27.364 * Doc Risk: 23.5083%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 77 call pairs -- scoped 14.3%, unique 0.0%, ambiguous 0.0%, external 85.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 77 | 14.3% | 0.0% | 0.0% | 85.7% |

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
