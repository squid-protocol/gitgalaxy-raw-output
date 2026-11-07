# ARCHITECTURAL_BRIEF: beautifulsoup4
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
- **Scope:** 42 analyzed artifact(s), 10513 LOC.
- **Load-bearing artifact:** `beautifulsoup4-4.14.3/bs4/element.py` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `beautifulsoup4-4.14.3/bs4/__init__.py` -- pulls in 16 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `beautifulsoup4-4.14.3/bs4/element.py` at magnitude 2130.78 (structural weight, not risk).
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
| Total Artifacts | 73 |
| Analyzed Artifacts (Scanned) | 42 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 31 |
| Total LOC | 10513 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2065 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3686 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 26.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8385 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 35 | 10294 | 83.3% |
| PLAINTEXT | 3 | 0 | 7.1% |
| MAKEFILE | 3 | 219 | 7.1% |
| MARKDOWN | 1 | 0 | 2.4% |

## 4.1 SOURCE ENCODINGS
All 42 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 36%, Generic / Templated Code Files 24%, Data / Markup / Trivial 10%, Declarative / Non-Code 7%, Large Core Modules 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 38 | 90.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 9.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 31*

**Composition by Extension & Reason:**
- `.testcase`: 16x Excluded (Unsupported Extension: '.testcase')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.rst`: 4x Excluded (Unsupported Extension: '.rst')
- `.jpg`: 3x Excluded (Explicitly Denied Extension: '.jpg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 256 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 66.2 | 21.0 | 18.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 82.8 | 49.3 | 49.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.5 | 8.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 86.1 | 23.9 | 11.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 90.0 | 5.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.5 | 91.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 247 | 25 | 13 | `beautifulsoup4-4.14.3/bs4/tests/test_filter.py` |
| cleanup | 5 | 4 | 0 | `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` |
| guards | 1310 | 32 | 74 | `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` |
| danger | 286 | 26 | 15 | `beautifulsoup4-4.14.3/bs4/element.py` |
| concurrency | 89 | 11 | 3 | `beautifulsoup4-4.14.3/bs4/element.py` |
| connectivity | 991 | 36 | 61 | `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` |
| io | 25 | 12 | 2 | `beautifulsoup4-4.14.3/bs4/__init__.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 1 | 0 | `beautifulsoup4-4.14.3/bs4/diagnose.py` |
| serialization | 9 | 5 | 1 | `beautifulsoup4-4.14.3/bs4/tests/__init__.py` |
| regex | 37 | 6 | 2 | `beautifulsoup4-4.14.3/bs4/dammit.py` |
| events | 0 | 0 | 0 | - |
| tests | 614 | 20 | 47 | `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` |
| docs | 443 | 31 | 25 | `beautifulsoup4-4.14.3/bs4/element.py` |
| debt | 155 | 20 | 5 | `beautifulsoup4-4.14.3/doc.es/Makefile` |
| mutation | 4079 | 38 | 227 | `beautifulsoup4-4.14.3/bs4/element.py` |
| dead_code | 498 | 25 | 38 | `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` |
| credential | 1 | 1 | 0 | `beautifulsoup4-4.14.3/bs4/tests/__init__.py` |
| threat | 17 | 4 | 0 | `beautifulsoup4-4.14.3/bs4/tests/test_dammit.py` |
| ml_ai | 1 | 1 | 0 | `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.3875**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `beautifulsoup4-4.14.3/bs4/__init__.py` (Hits: 5)
- `beautifulsoup4-4.14.3/bs4/tests/test_fuzz.py` (Hits: 3)
- `beautifulsoup4-4.14.3/doc.es/Makefile` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **element.py** (`beautifulsoup4-4.14.3/bs4/element.py`) — 21 inbound connections
2. **__init__.py** (`beautifulsoup4-4.14.3/bs4/__init__.py`) — 20 inbound connections
3. **_typing.py** (`beautifulsoup4-4.14.3/bs4/_typing.py`) — 13 inbound connections
4. **__init__.py** (`beautifulsoup4-4.14.3/bs4/builder/__init__.py`) — 13 inbound connections
5. **__init__.py** (`beautifulsoup4-4.14.3/bs4/tests/__init__.py`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`beautifulsoup4-4.14.3/bs4/__init__.py`) — 16 outbound dependencies
2. **__init__.py** (`beautifulsoup4-4.14.3/bs4/builder/__init__.py`) — 15 outbound dependencies
3. **diagnose.py** (`beautifulsoup4-4.14.3/bs4/diagnose.py`) — 15 outbound dependencies
4. **__init__.py** (`beautifulsoup4-4.14.3/bs4/tests/__init__.py`) — 14 outbound dependencies
5. **test_soup.py** (`beautifulsoup4-4.14.3/bs4/tests/test_soup.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/__init__.py`) -> Impact: **200.7** | LOC: 283
- `__init__` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/element.py`) -> Impact: **124.8** | LOC: 120
- `_find_all` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/element.py`) -> Impact: **72.2** | LOC: 65
- `decode` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/element.py`) -> Impact: **56.8** | LOC: 108
- `_insert` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/element.py`) -> Impact: **50.3** | LOC: 86
- `decode` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/__init__.py`) -> Impact: **48.6** | LOC: 72
- `linkage_validator` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/tests/__init__.py`) -> Impact: **48.5** | LOC: 130
- `__init__` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/filter.py`) -> Impact: **42.2** | LOC: 60
- `_format_tag` **(Many-Argument Workhorses)** (@ `beautifulsoup4-4.14.3/bs4/element.py`) -> Impact: **38.8** | LOC: 61
- `matches_tag` **(Compute Cores)** (@ `beautifulsoup4-4.14.3/bs4/filter.py`) -> Impact: **38.5** | LOC: 77
  * *Intent:* """Do the rules of this `SoupStrainer` trigger a match against the given `Tag`? If the `SoupStrainer` has any `TagNameMatchRule`, at least one must ma...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `beautifulsoup4-4.14.3/bs4` | 11 | 4673.08 | 24.08% | 11.39% |
| `beautifulsoup4-4.14.3/bs4/tests` | 17 | 3191.32 | 16.16% | 0.0% |
| `beautifulsoup4-4.14.3/bs4/builder` | 4 | 1285.46 | 50.7% | 29.19% |
| `beautifulsoup4-4.14.3` | 4 | 101.42 | 0.0% | 0.0% |
| `beautifulsoup4-4.14.3/scripts` | 1 | 80.52 | 46.99% | 27.19% |
| `beautifulsoup4-4.14.3/doc.es` | 2 | 56.1 | 1.75% | 0.0% |
| `beautifulsoup4-4.14.3/doc` | 2 | 31.78 | 0.0% | 18.88% |
| `beautifulsoup4-4.14.3/doc.ru` | 1 | 27.8 | 3.5% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `beautifulsoup4-4.14.3/bs4/diagnose.py` -> **99.4956%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **46.955%** Exposure
- `beautifulsoup4-4.14.3/doc/Makefile` -> **37.7541%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` -> **32.6904%** Exposure
- `beautifulsoup4-4.14.3/scripts/demonstrate_parser_differences.py` -> **27.1931%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_html5lib.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/diagnose.py` -> **100.0%** Exposure
- `beautifulsoup4-4.14.3/bs4/element.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` -> **125** Orphaned Functions | **0** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_css.py` -> **61** Orphaned Functions | **0** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/__init__.py` -> **55** Orphaned Functions | **0** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` -> **41** Orphaned Functions | **0** Duplicates
- `beautifulsoup4-4.14.3/bs4/tests/test_dammit.py` -> **38** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `227` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `beautifulsoup4-4.14.3/bs4/element.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.297)
- **Top Global Matches:** file_cluster_5: 7.297, file_cluster_12: 9.651, file_cluster_0: 9.936
- **Magnitude:** 2130.78 | **LOC:** 3212 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **13**; blast radius 191.836; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (86.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%)
- **Documentation Coverage:** 55.4007% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 124.8)
  * `_find_all` **(Many-Argument Workhorses)** (Impact: 72.2)
  * `decode` **(Many-Argument Workhorses)** (Impact: 56.8)
  * `_insert` **(Many-Argument Workhorses)** (Impact: 50.3)
  * `_format_tag` **(Many-Argument Workhorses)** (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 262 instances
* *State Mutation (weighted view):* 832
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 312`, `structural_boundaries: 365`, `args: 150`, `func_start: 150`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 308`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 139`, `import: 17`
* *Defense:* `safety: 51`, `doc: 127`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 191.836
  * `Choke Point (Betweenness):` 0.069004 | `Ripple Effect (Closeness):` 0.554384
  * `Imports (Out-Degree: 9):` __future__, bs4, bs4._deprecation, bs4._typing, bs4._warnings, bs4.builder, bs4.css, bs4.filter...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.524)
- **Top Global Matches:** file_cluster_4: 9.524, file_cluster_5: 10.67, file_cluster_12: 11.751
- **Magnitude:** 918.98 | **LOC:** 1175 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **16**; blast radius 75.465; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 200.7)
  * `decode` **(Many-Argument Workhorses)** (Impact: 48.6)
  * `_markup_resembles_filename` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* """Error-handling method to issue a warning if incoming markup resembles a filename. :param markup: ...
  * `handle_starttag` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `endData` **(Compute Cores)** (Impact: 21.1)
    * *Intent:* """Method called by the TreeBuilder when the end of a data segment occurs. :param containerClass: Th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 406
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 115`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 156`, `planned_debt: 2`
* *Architecture:* `io: 5`, `api: 22`, `import: 17`
* *Defense:* `safety: 25`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 75.465
  * `Choke Point (Betweenness):` 0.060925 | `Ripple Effect (Closeness):` 0.525954
  * `Imports (Out-Degree: 11):` ._deprecation, .builder, .builder._htmlparser, .css, .dammit, .element, .filter, .formatter...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_tree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.366)
- **Top Global Matches:** file_cluster_15: 7.366, file_cluster_12: 8.465, file_cluster_10: 8.819
- **Magnitude:** 734.44 | **LOC:** 1460 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (32.6%), Complexity Load (formerly Cognitive Load) (22.3%), Connectivity (formerly Api Exposure) (13.9%)
- **Documentation Coverage:** 95.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_find_all_by_class` **(Compute Cores)** (Impact: 8.0)
  * `test_parent_generator` **(Defensive Guards)** (Impact: 6.0)
  * `test_self_and_parent_generator` **(Defensive Guards)** (Impact: 6.0)
  * `test_find_all_by_attribute_dict` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* # You can pass in a dictionary as the argument 'attrs'. This # lets you search for attributes like '...
  * `test_next_generators` **(Defensive Guards)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 448`, `args: 146`, `func_start: 140`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 267`, `planned_debt: 2`, `unreferenced_by_name: 125`
* *Architecture:* `api: 157`, `import: 8`
* *Defense:* `safety: 244`, `doc: 32`, `test: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .SoupTest, bs4, bs4.builder, bs4.element, bs4.filter, pytest, re, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/dammit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.765)
- **Top Global Matches:** file_cluster_4: 8.765, file_cluster_12: 9.387, file_cluster_5: 9.443
- **Magnitude:** 696.2 | **LOC:** 1517 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 48.832; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%), Complexity Load (formerly Cognitive Load) (51.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `detwingle` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `_populate_class_variables` **(Compute Cores)** (Impact: 36.2)
    * *Intent:* """Initialize variables used by this class to manage the plethora of HTML5 named entities. This func...
  * `find_declared_encoding` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `_sub_ms_char` **(Stateful Encapsulated Methods)** (Impact: 24.2)
    * *Intent:* """Changes a MS smart quote character to an XML or HTML entity, or an ASCII character. TODO: Since t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 103`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 125`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 14`
* *Defense:* `safety: 14`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.832
  * `Choke Point (Betweenness):` 0.000305 | `Ripple Effect (Closeness):` 0.387023
  * `Imports (Out-Degree: 1):` bs4._typing, cchardet, chardet, charset_normalizer, codecs, collections, html.entities, logging...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/filter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.493)
- **Top Global Matches:** file_cluster_5: 9.493, file_cluster_4: 10.317, file_cluster_12: 11.309
- **Magnitude:** 532.74 | **LOC:** 765 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **8**; blast radius 43.956; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.9%), Connectivity (formerly Api Exposure) (62.8%)
- **Documentation Coverage:** 43.3962% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 42.2)
  * `matches_tag` **(Compute Cores)** (Impact: 38.5)
    * *Intent:* """Do the rules of this `SoupStrainer` trigger a match against the given `Tag`? If the `SoupStrainer...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* # TODO-TYPING: All MatchRule objects also have an attribute # ``function``, but the type of the func...
  * `allow_tag_creation` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `_make_match_rules` **(Many-Argument Workhorses)** (Impact: 28.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 123`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 53`, `dead_code: 2`
* *Architecture:* `api: 28`, `import: 8`
* *Defense:* `safety: 17`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.956
  * `Choke Point (Betweenness):` 0.002713 | `Ripple Effect (Closeness):` 0.4022
  * `Imports (Out-Degree: 3):` __future__, bs4._deprecation, bs4._typing, bs4.element, collections, re, typing, warnings
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.932)
- **Top Global Matches:** file_cluster_12: 7.932, file_cluster_15: 8.487, file_cluster_0: 9.013
- **Magnitude:** 509.58 | **LOC:** 1349 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **14**; blast radius 31.804; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.1%), Complexity Load (formerly Cognitive Load) (18.7%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 77.4436% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `linkage_validator` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `assert_soup` **(Defensive Guards)** (Impact: 9.2)
  * `test_python_specific_encodings_not_used_in_charset` **(Defensive Guards)** (Impact: 6.9)
    * *Intent:* # You can encode an HTML document using a Python-specific # encoding, but that encoding won't be men...
  * `assertConnectedness` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* """Ensure that next_element and previous_element are properly set for all descendants of the given e...
  * `test_python_specific_encodings_not_used_in_xml_declaration` **(Defensive Guards)** (Impact: 5.3)
    * *Intent:* # You can encode an XML document using a Python-specific # encoding, but that encoding won't be ment...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 250`, `args: 75`, `func_start: 75`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 159`, `fragile_debt: 3`, `unreferenced_by_name: 55`
* *Architecture:* `io: 1`, `api: 78`, `import: 15`
* *Defense:* `safety: 130`, `doc: 48`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.804
  * `Choke Point (Betweenness):` 0.015589 | `Ripple Effect (Closeness):` 0.292683
  * `Imports (Out-Degree: 6):` bs4, bs4._typing, bs4.builder, bs4.builder._htmlparser, bs4.element, bs4.filter, copy, importlib...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/builder/_html5lib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.193)
- **Top Global Matches:** file_cluster_5: 7.193, file_cluster_12: 8.999, file_cluster_0: 9.081
- **Magnitude:** 438.5 | **LOC:** 612 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 13.329; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.6%), Connectivity (formerly Api Exposure) (70.6%), Complexity Load (formerly Cognitive Load) (66.2%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendChild` **(Many-Argument Workhorses)** (Impact: 30.3)
  * `reparentChildren` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* """Move all of this tag's children into another tag."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 16.3)
  * `feed` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* # These methods are defined by Beautiful Soup. """Run some incoming markup through some parsing proc...
  * `__setitem__` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* # If this attribute is a multi-valued attribute for this element, # turn its value into a list. list...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 107`, `args: 37`, `func_start: 37`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 83`, `planned_debt: 4`
* *Architecture:* `api: 40`, `import: 12`
* *Defense:* `safety: 21`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.329
  * `Choke Point (Betweenness):` 0.000203 | `Ripple Effect (Closeness):` 0.280989
  * `Imports (Out-Degree: 4):` bs4, bs4._typing, bs4.builder, bs4.element, html5lib, html5lib.constants, html5lib.treebuilders, typing...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/builder/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.354)
- **Top Global Matches:** file_cluster_5: 5.354, file_cluster_12: 8.995, file_cluster_7: 10.172
- **Magnitude:** 349.0 | **LOC:** 849 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **15**; blast radius 57.973; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.8%), Connectivity (formerly Api Exposure) (63.7%)
- **Documentation Coverage:** 51.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `lookup` **(Compute Cores)** (Impact: 21.3)
    * *Intent:* """Look up a TreeBuilder subclass with the desired features. :param features: A list of features to ...
  * `_replace_cdata_list_attribute_values` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `warn_if_markup_looks_like_xml` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `set_up_substitutions` **(Many-Argument Workhorses)** (Impact: 13.0)
    * *Intent:* """Replace the declared encoding in a <meta> tag with a placeholder, to be substituted when the tag ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 100`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 57`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 34`, `import: 17`
* *Defense:* `safety: 10`, `doc: 22`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 57.973
  * `Choke Point (Betweenness):` 0.052693 | `Ripple Effect (Closeness):` 0.445917
  * `Imports (Out-Degree: 9):` ._html5lib, ._htmlparser, ._lxml, __future__, bs4, bs4._typing, bs4._warnings, bs4.element...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_filter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.718)
- **Top Global Matches:** file_cluster_12: 7.718, file_cluster_0: 8.01, file_cluster_15: 8.114
- **Magnitude:** 321.02 | **LOC:** 702 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (34.8%), Complexity Load (formerly Cognitive Load) (23.9%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 97.5904% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_match` **(Defensive Guards)** (Impact: 10.9)
  * `allow_tag_creation` **(Generic / Templated Code)** (Impact: 9.5)
  * `tag_matches` **(Generic / Templated Code)** (Impact: 8.8)
  * `test_allow_tag_creation` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* # By default, ElementFilter.allow_tag_creation allows everything. filter = ElementFilter() f = filte...
  * `test_default_behavior` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* # An unconfigured ElementFilter matches absolutely everything. selector = ElementFilter() assert not...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 220`, `args: 50`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `unreferenced_by_name: 31`
* *Architecture:* `api: 46`, `import: 8`
* *Defense:* `safety: 120`, `doc: 2`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .SoupTest, bs4._typing, bs4.element, bs4.filter, pytest, re, typing, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_soup.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.313)
- **Top Global Matches:** file_cluster_12: 6.313, file_cluster_5: 8.819, file_cluster_7: 8.936
- **Magnitude:** 276.5 | **LOC:** 603 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.1%), Complexity Load (formerly Cognitive Load) (18.9%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_assert_warning` **(Stateful Encapsulated Methods)** (Impact: 6.4)
    * *Intent:* # Note that some of the tests in this class create BeautifulSoup # objects directly rather than usin...
  * `test_custom_builder_class` **(Defensive Guards)** (Impact: 4.6)
    * *Intent:* # Verify that you can pass in a custom Builder class and # it'll be instantiated with the appropriat...
  * `test_alternate_string_containers` **(Defensive Guards)** (Impact: 4.4)
    * *Intent:* # Test the ability to customize the string containers for # different types of tags. class PString(N...
  * `test_cdata_list_attributes` **(Defensive Guards)** (Impact: 4.3)
    * *Intent:* # Most attribute values are represented as scalars, but the # HTML standard says that some attribute...
  * `test_replacement_classes` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* # Test the ability to pass in replacements for element classes # which will be used when building th...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 212`, `args: 50`, `func_start: 49`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 87`, `fragile_debt: 1`, `unreferenced_by_name: 41`
* *Architecture:* `io: 1`, `api: 61`, `import: 13`
* *Defense:* `safety: 86`, `doc: 3`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .LXML_PRESENT, .SoupTest, .default_builder, bs4, bs4._warnings, bs4.builder, bs4.element, bs4.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_css.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.393)
- **Top Global Matches:** file_cluster_15: 6.393, file_cluster_12: 7.346, file_cluster_11: 8.029
- **Magnitude:** 276.06 | **LOC:** 537 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.6%), Complexity Load (formerly Cognitive Load) (16.3%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_css_selects` **(Defensive Guards)** (Impact: 5.1)
  * `test_match` **(Defensive Guards)** (Impact: 4.5)
  * `test_select_one_returns_none_if_no_match` **(Defensive Guards)** (Impact: 4.4)
  * `assert_css_select_multiple` **(Generic / Templated Code)** (Impact: 3.6)
  * `test_select_duplicate_elements` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* # When markup contains duplicate elements, a multiple select # will find all of them. markup = '<div...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 160`, `args: 63`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 40`, `unreferenced_by_name: 61`
* *Architecture:* `api: 64`, `import: 7`
* *Defense:* `safety: 55`, `doc: 3`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .SOUP_SIEVE_PRESENT, .SoupTest, bs4, packaging.version, pytest, soupsieve, types, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/builder/_lxml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.983)
- **Top Global Matches:** file_cluster_5: 5.983, file_cluster_12: 9.062, file_cluster_0: 10.446
- **Magnitude:** 254.56 | **LOC:** 502 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 14.179; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.1%), Complexity Load (formerly Cognitive Load) (62.5%), Connectivity (formerly Api Exposure) (50.0%)
- **Documentation Coverage:** 71.0526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `end` **(Defensive Guards)** (Impact: 13.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 11.0)
  * `feed` **(Defensive Guards)** (Impact: 9.9)
  * `_prefix_for_namespace` **(Stateful Encapsulated Methods)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 80`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 45`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 20`, `import: 12`
* *Defense:* `safety: 27`, `doc: 8`, `test: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.179
  * `Choke Point (Betweenness):` 0.002287 | `Ripple Effect (Closeness):` 0.288904
  * `Imports (Out-Degree: 6):` __future__, bs4, bs4._typing, bs4.builder, bs4.dammit, bs4.element, bs4.exceptions, io...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.379)
- **Top Global Matches:** file_cluster_5: 6.379, file_cluster_12: 9.534, file_cluster_7: 9.948
- **Magnitude:** 243.4 | **LOC:** 463 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 25.154; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.8%), Connectivity (formerly Api Exposure) (59.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 35.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_starttag` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `prepare_markup` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.6)
  * `handle_charref` **(Type Conversions)** (Impact: 9.8)
    * *Intent:* """Handle a numeric character reference by converting it to the corresponding Unicode character and ...
  * `handle_endtag` **(Many-Argument Workhorses)** (Impact: 8.8)
    * *Intent:* """Handle a closing tag, e.g. '</tag>' :param tag: A tag name. :param check_already_closed: True if ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 43`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 42`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 16`, `import: 10`
* *Defense:* `safety: 6`, `doc: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.154
  * `Choke Point (Betweenness):` 0.002937 | `Ripple Effect (Closeness):` 0.347664
  * `Imports (Out-Degree: 6):` __future__, bs4, bs4._typing, bs4.builder, bs4.dammit, bs4.element, bs4.exceptions, html.parser...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_dammit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.653)
- **Top Global Matches:** file_cluster_15: 6.653, file_cluster_13: 7.321, file_cluster_11: 7.637
- **Magnitude:** 211.12 | **LOC:** 513 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.3%), Complexity Load (formerly Cognitive Load) (17.9%), Connectivity (formerly Api Exposure) (12.1%)
- **Documentation Coverage:** 94.8718% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_known_definite_versus_user_encodings` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* # The known_definite_encodings are used before sniffing the # byte-order mark; the user_encodings ar...
  * `test_html5_entity` **(Defensive Guards)** (Impact: 4.1)
  * `test_deprecated_override_encodings` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* # override_encodings is a deprecated alias for # known_definite_encodings. hebrew = b"\xed\xe5\xec\x...
  * `test_detwingle_ignores_multibyte_characters` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* # Each of these characters has a UTF-8 representation ending # in \x93. \x93 is a smart quote if int...
  * `test_find_declared_encoding` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* # Test our ability to find a declared encoding inside an # XML or HTML document. # # Even if the doc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 126`, `args: 39`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `state_mutation: 66`, `unreferenced_by_name: 38`
* *Architecture:* `api: 43`, `import: 6`
* *Defense:* `safety: 74`, `doc: 5`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4, bs4.dammit, logging, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/diagnose.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.66)
- **Top Global Matches:** file_cluster_5: 6.66, file_cluster_12: 8.535, file_cluster_0: 9.481
- **Magnitude:** 185.94 | **LOC:** 269 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.1%)
- **Documentation Coverage:** 54.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diagnose` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* """Diagnostic suite for isolating common problems. :param data: Some markup that needs to be explain...
  * `lxml_trace` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* """Print out the lxml events that occur during parsing. This lets you see how lxml parses a document...
  * `rdoc` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* """Randomly generate an invalid HTML document. :meta private: """
  * `rword` **(Generic / Templated Code)** (Impact: 6.3)
    * *Intent:* """Generate a random word-like string. :meta private: """
  * `benchmark_parsers` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* """Very basic head-to-head performance benchmark."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 53`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 39`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `api: 18`, `import: 19`
* *Defense:* `safety: 9`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bs4, bs4._typing, bs4.builder, cProfile, html.parser, html5lib, io, lxml...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_pageelement.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.838)
- **Top Global Matches:** file_cluster_15: 6.838, file_cluster_10: 7.546, file_cluster_11: 7.959
- **Magnitude:** 162.26 | **LOC:** 438 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.7%), Complexity Load (formerly Cognitive Load) (28.5%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_deprecated_renderContents` **(Defensive Guards)** (Impact: 4.8)
  * `test_formatter_is_run_on_attribute_values` **(Defensive Guards)** (Impact: 2.2)
  * `test_encode_deeply_nested_document` **(Defensive Guards)** (Impact: 1.9)
    * *Intent:* # This test verifies that encoding a string doesn't involve # any recursive function calls. If it di...
  * `test_formatter_html` **(Defensive Guards)** (Impact: 1.9)
  * `test_formatter_html5` **(Defensive Guards)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 124`, `args: 31`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 82`, `unreferenced_by_name: 17`
* *Architecture:* `io: 2`, `api: 32`, `import: 9`
* *Defense:* `safety: 60`, `doc: 7`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .SoupTest, bs4, bs4.element, bs4.filter, copy, pickle, pytest, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_tag.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.264)
- **Top Global Matches:** file_cluster_0: 8.264, file_cluster_15: 8.409, file_cluster_11: 9.22
- **Magnitude:** 112.32 | **LOC:** 242 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (21.4%), Complexity Load (formerly Cognitive Load) (14.7%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 79.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_deprecated_member_access` **(Defensive Guards)** (Impact: 3.3)
  * `test_string_methods_inside_special_string_container_tags` **(Defensive Guards)** (Impact: 3.0)
    * *Intent:* # Strings inside tags like <script> are generally ignored by # methods like get_text, because they'r...
  * `test__should_pretty_print` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* # Test the rules about when a tag should be pretty-printed. tag = self.soup("").new_tag("a_tag") # N...
  * `test_len` **(Defensive Guards)** (Impact: 2.1)
    * *Intent:* """The length of a Tag is its number of children."""
  * `test_tag_with_multiple_children_has_no_string` **(Defensive Guards)** (Impact: 2.1)
    * *Intent:* # A Tag with no children has no .string. soup = self.soup("<a>foo<b></b><b></b></b>") assert soup.b....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 102`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 38`, `planned_debt: 1`, `unreferenced_by_name: 24`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 57`, `doc: 7`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .SoupTest, bs4.element, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_html5lib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.503)
- **Top Global Matches:** file_cluster_12: 6.503, file_cluster_15: 8.134, file_cluster_13: 8.862
- **Magnitude:** 96.08 | **LOC:** 265 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.9%), Connectivity (formerly Api Exposure) (10.5%), Complexity Load (formerly Cognitive Load) (8.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_correctly_nested_tables` **(I/O & Config Routines)** (Impact: 2.6)
    * *Intent:* """html5lib inserts <tbody> tags where other parsers don't."""
  * `test_reparented_markup_containing_children` **(Defensive Guards)** (Impact: 2.3)
  * `test_soupstrainer` **(Defensive Guards)** (Impact: 2.1)
    * *Intent:* # The html5lib tree builder does not support parse_only. strainer = SoupStrainer("b") markup = "<p>A...
  * `test_xml_declaration_followed_by_doctype` **(Defensive Guards)** (Impact: 2.1)
  * `test_reparented_markup_containing_identical_whitespace_nodes` **(Defensive Guards)** (Impact: 1.9)
    * *Intent:* """Verify that we keep the two whitespace nodes in this document distinct when reparenting the adjac...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 64`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 39`, `fragile_debt: 2`, `unreferenced_by_name: 11`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `safety: 26`, `doc: 12`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .HTML5LIB_PRESENT, .HTML5TreeBuilderSmokeTest, bs4, bs4.builder, bs4.filter, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_element.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.449)
- **Top Global Matches:** file_cluster_15: 7.449, file_cluster_2: 7.738, file_cluster_11: 7.738
- **Magnitude:** 84.02 | **LOC:** 179 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (27.5%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_html_attribute_value_handling` **(Defensive Guards)** (Impact: 2.5)
    * *Intent:* # Verify that attribute values are processed according to the # HTML spec's rules. d = HTMLAttribute...
  * `test_xml_attribute_value_handling` **(Defensive Guards)** (Impact: 2.4)
    * *Intent:* # Verify that attribute values are processed according to the # XML spec's rules. d = XMLAttributeDi...
  * `test_attributes_are_equivalent_if_prefix_and_name_identical` **(Defensive Guards)** (Impact: 2.2)
  * `test_equality` **(Defensive Guards)** (Impact: 2.2)
    * *Intent:* # A ResultSet is equal to a list if its result sequence is equal to that list. l = [1, 2, 3] rs1 = R...
  * `test_charset_meta_attribute_value` **(Defensive Guards)** (Impact: 2.0)
    * *Intent:* # The value of a CharsetMetaAttributeValue is whatever # encoding the string is in. value = CharsetM...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 67`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 14`
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `safety: 42`, `doc: 3`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4.element, bs4.filter, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_htmlparser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.691)
- **Top Global Matches:** file_cluster_12: 6.691, file_cluster_7: 8.002, file_cluster_5: 8.487
- **Magnitude:** 80.56 | **LOC:** 165 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.4%), Complexity Load (formerly Cognitive Load) (22.6%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_on_duplicate_attribute` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* # The html.parser tree builder has a variety of ways of # handling a tag that contains the same attr...
  * `test_html5_attributes` **(Defensive Guards)** (Impact: 4.4)
    * *Intent:* # The html.parser TreeBuilder can convert any entity named in # the HTML5 spec to a sequence of Unic...
  * `accumulate` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* # And you can pass in a callable that does whatever you want.
  * `assert_attribute` **(Defensive Guards)** (Impact: 2.2)
    * *Intent:* # You can also get this behavior explicitly.
  * `test_feed_raises_correct_exception_on_rejected_input` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* # Mock BeautifulSoupHTMLParser so it raises an AssertionError and verify that this is # turned into ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 54`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 25`, `unreferenced_by_name: 11`
* *Architecture:* `api: 16`, `import: 7`
* *Defense:* `safety: 21`, `doc: 2`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .HTMLTreeBuilderSmokeTest, bs4, bs4.builder._htmlparser, bs4.exceptions, pickle, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/scripts/demonstrate_parser_differences.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.944)
- **Top Global Matches:** file_cluster_7: 7.944, file_cluster_12: 8.936, file_cluster_5: 10.202
- **Magnitude:** 80.52 | **LOC:** 128 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_against` **(Defensive Guards)** (Impact: 11.3)
  * `dump` **(Parameter Forwarders)** (Impact: 3.0)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 3`, `import: 5`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bs4, bs4.builder, io, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/css.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.851)
- **Top Global Matches:** file_cluster_5: 6.851, file_cluster_7: 9.795, file_cluster_12: 10.373
- **Magnitude:** 80.28 | **LOC:** 340 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 41.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.9%), Guard Balance (formerly Safety Score) (72.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 85.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match` **(Many-Argument Workhorses)** (Impact: 9.2)
  * `select` **(Many-Argument Workhorses)** (Impact: 7.1)
  * `__init__` **(Generic / Templated Code)** (Impact: 6.5)
  * `_ns` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `iselect` **(Many-Argument Workhorses)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 40`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 6`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 3`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.784
  * `Choke Point (Betweenness):` 0.000762 | `Ripple Effect (Closeness):` 0.394465
  * `Imports (Out-Degree: 3):` __future__, bs4, bs4._typing, bs4.element, soupsieve, types, typing, warnings
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `beautifulsoup4-4.14.3/bs4/tests/test_formatter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.543)
- **Top Global Matches:** file_cluster_15: 6.543, file_cluster_13: 7.074, file_cluster_11: 7.584
- **Magnitude:** 78.8 | **LOC:** 171 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.8%), Complexity Load (formerly Cognitive Load) (18.1%), Connectivity (formerly Api Exposure) (9.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_empty_attributes_are_booleans` **(Defensive Guards)** (Impact: 7.1)
    * *Intent:* # Test the behavior of empty_attributes_are_booleans as well # as which Formatters have it enabled. ...
  * `attributes` **(Compute Cores)** (Impact: 5.5)
  * `test_sort_attributes` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* # Test the ability to override Formatter.attributes() to, # e.g., disable the normal sorting of attr...
  * `test_entity_round_trip` **(Defensive Guards)** (Impact: 2.7)
    * *Intent:* # This is more an explanatory test and a way to avoid regressions than a test of functionality. mark...
  * `test_indent` **(Defensive Guards)** (Impact: 2.5)
    * *Intent:* # Pretty-print a tree with a Formatter set to # indent in a certain way and verify the results. soup...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 47`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 8`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 24`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .SoupTest, bs4.element, bs4.formatter, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/tests/test_navigablestring.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.022)
- **Top Global Matches:** file_cluster_15: 7.022, file_cluster_11: 8.088, file_cluster_13: 8.37
- **Magnitude:** 65.74 | **LOC:** 156 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.9%), Guard Balance (formerly Safety Score) (24.0%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_default_string_containers` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* # In some cases, we use different NavigableString subclasses for # the same text in different tags. ...
  * `test_text_acquisition_methods` **(Defensive Guards)** (Impact: 3.0)
    * *Intent:* # These methods are intended for use against Tag, but they # work on NavigableString as well, s = Na...
  * `test_cdata_is_never_formatted` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* """Text inside a CData object is passed into the formatter. But the return value is ignored. """
  * `test_string_detects_attribute_access_attempt` **(Defensive Guards)** (Impact: 2.0)
  * `test_ruby_strings` **(Defensive Guards)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 60`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 9`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 43`, `doc: 1`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .SoupTest, bs4.element, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `beautifulsoup4-4.14.3/bs4/formatter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.517)
- **Top Global Matches:** file_cluster_12: 7.517, file_cluster_5: 7.993, file_cluster_7: 9.446
- **Magnitude:** 58.54 | **LOC:** 277 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 32.936; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Guard Balance (formerly Safety Score) (60.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `_default` **(Stateful Encapsulated Methods)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 33`, `args: 2`, `func_start: 2`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 25`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 32.936
  * `Choke Point (Betweenness):` 0.000508 | `Ripple Effect (Closeness):` 0.359863
  * `Imports (Out-Degree: 3):` .element, __future__, bs4._typing, bs4.dammit, typing, typing_extensions
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `beautifulsoup4-4.14.3/bs4/tests/test_tag.py` (PYTHON) | Magnitude: 112.32 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 102, safety: 57, state_mutation: 38

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 6.9** (Bridge: 0.069 * Flux: 100.0%)
- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **Severity: 6.093** (Bridge: 0.0609 * Flux: 100.0%)
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **Severity: 5.269** (Bridge: 0.0527 * Flux: 99.9979%)
- `beautifulsoup4-4.14.3/bs4/builder/_htmlparser.py` -> **Severity: 0.294** (Bridge: 0.0029 * Flux: 100.0%)
- `beautifulsoup4-4.14.3/bs4/filter.py` -> **Severity: 0.271** (Bridge: 0.0027 * Flux: 99.9996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **Severity: 40.279** (Embedded: 0.526 * Error Risk: 76.5823%)
- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 40.211** (Embedded: 0.5544 * Error Risk: 72.5326%)
- `beautifulsoup4-4.14.3/bs4/builder/__init__.py` -> **Severity: 30.66** (Embedded: 0.4459 * Error Risk: 68.7582%)
- `beautifulsoup4-4.14.3/bs4/_deprecation.py` -> **Severity: 29.764** (Embedded: 0.3721 * Error Risk: 80.0%)
- `beautifulsoup4-4.14.3/bs4/css.py` -> **Severity: 28.652** (Embedded: 0.3945 * Error Risk: 72.6357%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `beautifulsoup4-4.14.3/bs4/_typing.py` -> **Severity: 12715.0** (Blast Radius: 127.15 * Doc Risk: 100.0%)
- `beautifulsoup4-4.14.3/bs4/element.py` -> **Severity: 10627.849** (Blast Radius: 191.836 * Doc Risk: 55.4007%)
- `beautifulsoup4-4.14.3/bs4/__init__.py` -> **Severity: 3773.25** (Blast Radius: 75.465 * Doc Risk: 50.0%)
- `beautifulsoup4-4.14.3/bs4/css.py` -> **Severity: 3551.64** (Blast Radius: 41.784 * Doc Risk: 85.0%)
- `beautifulsoup4-4.14.3/bs4/_deprecation.py` -> **Severity: 3396.993** (Blast Radius: 43.406 * Doc Risk: 78.2609%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2189 call pairs -- scoped 45.0%, unique 0.0%, ambiguous 17.9%, external 37.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 2189 | 45.0% | 0.0% | 17.9% | 37.2% |

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
