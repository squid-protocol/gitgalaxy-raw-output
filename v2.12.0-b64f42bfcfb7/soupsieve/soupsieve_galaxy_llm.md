# ARCHITECTURAL_BRIEF: soupsieve
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
- **Scope:** 109 analyzed artifact(s), 6078 LOC.
- **Load-bearing artifact:** `soupsieve-2.8.3/tests/util.py` -- 84 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `soupsieve-2.8.3/soupsieve/__init__.py` -- pulls in 8 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `soupsieve-2.8.3/soupsieve/css_match.py` at magnitude 2527.46 (structural weight, not risk).
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
| Total Artifacts | 114 |
| Analyzed Artifacts (Scanned) | 109 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 6078 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 95.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2961 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.661 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4942 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 101 | 6078 | 92.7% |
| PLAINTEXT | 6 | 0 | 5.5% |
| MARKDOWN | 2 | 0 | 1.8% |

## 4.1 SOURCE ENCODINGS
All 109 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 45%, Large Core Modules 28%, Data / Markup / Trivial 17%, Compute Cores Files 4%, Generic / Templated Code Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 101 | 92.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 7.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 46.6 | 3.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.8 | 42.7 | 47.9 | 47.9 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.6 | 1.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.6 | 7.1 | 7.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 77.8 | 1.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 77 | 8 | 0 | `soupsieve-2.8.3/soupsieve/css_match.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 118 | 9 | 0 | `soupsieve-2.8.3/soupsieve/css_match.py` |
| danger | 120 | 10 | 0 | `soupsieve-2.8.3/soupsieve/css_parser.py` |
| concurrency | 33 | 5 | 0 | `soupsieve-2.8.3/soupsieve/css_match.py` |
| connectivity | 653 | 94 | 12 | `soupsieve-2.8.3/soupsieve/css_match.py` |
| io | 12 | 4 | 0 | `soupsieve-2.8.3/soupsieve/css_parser.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 1 | 1 | 0 | `soupsieve-2.8.3/tests/test_api.py` |
| regex | 44 | 5 | 0 | `soupsieve-2.8.3/soupsieve/css_parser.py` |
| events | 0 | 0 | 0 | - |
| tests | 498 | 86 | 9 | `soupsieve-2.8.3/tests/test_api.py` |
| docs | 1000 | 101 | 16 | `soupsieve-2.8.3/soupsieve/css_match.py` |
| debt | 28 | 4 | 0 | `soupsieve-2.8.3/soupsieve/css_parser.py` |
| mutation | 2661 | 91 | 45 | `soupsieve-2.8.3/soupsieve/css_match.py` |
| dead_code | 394 | 86 | 8 | `soupsieve-2.8.3/tests/test_api.py` |
| credential | 2 | 1 | 0 | `soupsieve-2.8.3/soupsieve/css_parser.py` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `soupsieve-2.8.3/soupsieve/css_parser.py` (Hits: 6)
- `soupsieve-2.8.3/tests/test_level4/test_open.py` (Hits: 4)
- `soupsieve-2.8.3/hatch_build.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.py** (`soupsieve-2.8.3/tests/util.py`) — 84 inbound connections
2. **__init__.py** (`soupsieve-2.8.3/soupsieve/__init__.py`) — 22 inbound connections
3. **css_match.py** (`soupsieve-2.8.3/soupsieve/css_match.py`) — 4 inbound connections
4. **css_types.py** (`soupsieve-2.8.3/soupsieve/css_types.py`) — 3 inbound connections
5. **util.py** (`soupsieve-2.8.3/soupsieve/util.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`soupsieve-2.8.3/soupsieve/__init__.py`) — 8 outbound dependencies
2. **css_match.py** (`soupsieve-2.8.3/soupsieve/css_match.py`) — 8 outbound dependencies
3. **css_parser.py** (`soupsieve-2.8.3/soupsieve/css_parser.py`) — 8 outbound dependencies
4. **test_api.py** (`soupsieve-2.8.3/tests/test_api.py`) — 6 outbound dependencies
5. **util.py** (`soupsieve-2.8.3/tests/util.py`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse_selectors` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_parser.py`) -> Impact: **127.6** | LOC: 182
- `match_lang` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **114.2** | LOC: 85
  * *Intent:* """Match languages."""
- `parse_pseudo_class` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_parser.py`) -> Impact: **110.9** | LOC: 101
- `match_nth` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **103.0** | LOC: 100
  * *Intent:* """Match `nth` elements."""
- `match_selectors` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **92.2** | LOC: 83
  * *Intent:* """Check if element matches one of the selectors."""
- `parse_attribute_selector` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_parser.py`) -> Impact: **77.2** | LOC: 69
  * *Intent:* """Create attribute selector from the returned regex match."""
- `parse_value` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **70.7** | LOC: 53
  * *Intent:* """Parse the input value."""
- `match_dir` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **66.9** | LOC: 58
  * *Intent:* """Check directionality."""
- `parse_pseudo_nth` **(Many-Argument Workhorses)** (@ `soupsieve-2.8.3/soupsieve/css_parser.py`) -> Impact: **66.9** | LOC: 64
- `match_indeterminate` **(Compute Cores)** (@ `soupsieve-2.8.3/soupsieve/css_match.py`) -> Impact: **56.7** | LOC: 61
  * *Intent:* """Match default."""

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `soupsieve-2.8.3/soupsieve` | 7 | 4660.5 | 37.24% | 13.94% |
| `soupsieve-2.8.3/tests/test_level4` | 37 | 638.6 | 0.88% | 0.0% |
| `soupsieve-2.8.3/tests` | 6 | 477.72 | 7.09% | 0.0% |
| `soupsieve-2.8.3/tests/test_level3` | 20 | 424.32 | 1.12% | 0.0% |
| `soupsieve-2.8.3/tests/test_extra` | 5 | 207.78 | 3.3% | 0.0% |
| `soupsieve-2.8.3/tests/test_level2` | 9 | 191.66 | 0.32% | 0.0% |
| `soupsieve-2.8.3/tests/test_level1` | 14 | 133.88 | 0.0% | 0.0% |
| `soupsieve-2.8.3/tests/test_nesting_1` | 2 | 61.58 | 7.72% | 0.0% |
| `soupsieve-2.8.3` | 3 | 14.94 | 0.0% | 12.58% |
| `soupsieve-2.8.3/requirements` | 6 | 6.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `soupsieve-2.8.3/soupsieve/css_types.py` -> **97.5834%** Exposure
- `soupsieve-2.8.3/hatch_build.py` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `soupsieve-2.8.3/soupsieve/__meta__.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/css_parser.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/pretty.py` -> **100.0%** Exposure
- `soupsieve-2.8.3/soupsieve/util.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `soupsieve-2.8.3/tests/test_api.py` -> **45** Orphaned Functions | **0** Duplicates
- `soupsieve-2.8.3/tests/test_level2/test_attribute.py` -> **30** Orphaned Functions | **0** Duplicates
- `soupsieve-2.8.3/tests/test_extra/test_soup_contains.py` -> **20** Orphaned Functions | **0** Duplicates
- `soupsieve-2.8.3/tests/test_level4/test_lang.py` -> **20** Orphaned Functions | **0** Duplicates
- `soupsieve-2.8.3/tests/test_level3/test_namespace.py` -> **14** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `80` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `soupsieve-2.8.3/soupsieve/css_match.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.837)
- **Top Global Matches:** file_cluster_6: 8.837, file_cluster_4: 13.237, file_cluster_8: 15.562
- **Magnitude:** 2527.46 | **LOC:** 1655 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 47.392; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.4%)
- **Documentation Coverage:** 7.8212% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match_lang` **(Many-Argument Workhorses)** (Impact: 114.2)
    * *Intent:* """Match languages."""
  * `match_nth` **(Many-Argument Workhorses)** (Impact: 103.0)
    * *Intent:* """Match `nth` elements."""
  * `match_selectors` **(Many-Argument Workhorses)** (Impact: 92.2)
    * *Intent:* """Check if element matches one of the selectors."""
  * `parse_value` **(Many-Argument Workhorses)** (Impact: 70.7)
    * *Intent:* """Parse the input value."""
  * `match_dir` **(Many-Argument Workhorses)** (Impact: 66.9)
    * *Intent:* """Check directionality."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 317 instances
* *State Mutation (weighted view):* 991
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 604`, `structural_boundaries: 308`, `args: 90`, `func_start: 90`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 357`
* *Architecture:* `api: 89`, `import: 8`
* *Defense:* `safety: 32`, `doc: 96`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 47.392
  * `Choke Point (Betweenness):` 0.00026 | `Ripple Effect (Closeness):` 0.300787
  * `Imports (Out-Degree: 2):` .css_types, .util, __future__, bs4, datetime, re, typing, unicodedata
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/soupsieve/css_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.938)
- **Top Global Matches:** file_cluster_6: 6.938, file_cluster_4: 12.803, file_cluster_8: 13.628
- **Magnitude:** 1494.74 | **LOC:** 1319 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 35.594; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 24.5614% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_selectors` **(Many-Argument Workhorses)** (Impact: 127.6)
  * `parse_pseudo_class` **(Many-Argument Workhorses)** (Impact: 110.9)
  * `parse_attribute_selector` **(Many-Argument Workhorses)** (Impact: 77.2)
    * *Intent:* """Create attribute selector from the returned regex match."""
  * `parse_pseudo_nth` **(Many-Argument Workhorses)** (Impact: 66.9)
  * `parse_combinator` **(Many-Argument Workhorses)** (Impact: 37.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 223 instances
* *State Mutation (weighted view):* 779
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 120`, `args: 32`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 333`
* *Architecture:* `io: 6`, `api: 28`, `import: 9`
* *Defense:* `safety: 3`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.292656
  * `Imports (Out-Degree: 3):` .css_match, .css_types, .util, __future__, functools, re, typing, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/tests/test_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.9)
- **Top Global Matches:** file_cluster_15: 5.9, file_cluster_11: 7.492, file_cluster_2: 7.927
- **Magnitude:** 272.44 | **LOC:** 646 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (20.3%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_match` **(I/O & Config Routines)** (Impact: 5.4)
    * *Intent:* """Test matching."""
  * `test_select_limit` **(I/O & Config Routines)** (Impact: 4.1)
    * *Intent:* """Test select limit."""
  * `test_iselect` **(I/O & Config Routines)** (Impact: 4.1)
    * *Intent:* """Test select iterator."""
  * `test_select` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* """Test select."""
  * `test_select_order` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* """Test select order."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 91`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 66`, `unreferenced_by_name: 45`
* *Architecture:* `api: 48`, `import: 6`
* *Defense:* `doc: 64`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .util, copy, pickle, pytest, random, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/css_types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.638)
- **Top Global Matches:** file_cluster_5: 6.638, file_cluster_7: 10.838, file_cluster_12: 11.23
- **Magnitude:** 185.24 | **LOC:** 408 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 65.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Debt Markers (formerly Tech Debt) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.5%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_validate` **(Stateful Encapsulated Methods)** (Impact: 12.5)
    * *Intent:* """Validate arguments."""
  * `_validate` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* """Validate arguments."""
  * `_validate` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* """Validate arguments."""
  * `__init__` **(Type Conversions)** (Impact: 7.4)
  * `__eq__` **(Defensive Guards)** (Impact: 7.3)
    * *Intent:* """Equal."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 75`, `args: 35`, `func_start: 35`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 27`, `duplicate_logic: 6`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 12`, `doc: 47`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 65.82
  * `Choke Point (Betweenness):` 0.007615 | `Ripple Effect (Closeness):` 0.303829
  * `Imports (Out-Degree: 1):` .pretty, __future__, copyreg, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/soupsieve/__meta__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.461)
- **Top Global Matches:** file_cluster_8: 8.461, file_cluster_6: 13.944, file_cluster_4: 22.023
- **Magnitude:** 155.38 | **LOC:** 198 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 38.165; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__new__` **(Many-Argument Workhorses)** (Impact: 50.0)
  * `parse_version` **(Type Conversions)** (Impact: 25.7)
    * *Intent:* """Parse version into a comparable Version tuple."""
  * `_get_canonical` **(Stateful Encapsulated Methods)** (Impact: 9.3)
    * *Intent:* """Get the canonical output string."""
  * `_is_pre` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* """Is prerelease."""
  * `_is_dev` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* """Is development."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 25`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.298227
  * `Imports (Out-Degree: 0):` __future__, collections, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/soupsieve/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.626)
- **Top Global Matches:** file_cluster_5: 7.626, file_cluster_7: 10.323, file_cluster_14: 11.296
- **Magnitude:** 142.16 | **LOC:** 118 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 65.82; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Connectivity (formerly Api Exposure) (57.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_pattern_context` **(Compute Cores)** (Impact: 19.3)
    * *Intent:* """Get the pattern context."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.4)
    * *Intent:* """Initialize."""
  * `lower` **(Generic / Templated Code)** (Impact: 6.1)
    * *Intent:* """Lower."""
  * `deprecated` **(Encapsulated Accessors)** (Impact: 2.8)
    * *Intent:* """ Raise a `DeprecationWarning` when wrapped function/method is called. Usage: @deprecated("This me...
  * `_deprecated_func` **(Encapsulated Accessors)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 21`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 33`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.82
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.303829
  * `Imports (Out-Degree: 0):` __future__, functools, re, typing, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/tests/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.107)
- **Top Global Matches:** file_cluster_12: 6.107, file_cluster_15: 7.91, file_cluster_7: 8.898
- **Magnitude:** 138.7 | **LOC:** 160 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **84** in-repo importer(s); it depends on **6**; blast radius 191.138; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (69.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_selector` **(Many-Argument Workhorses)** (Impact: 12.3)
    * *Intent:* """Assert selector."""
  * `available_parsers` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* """ Filter a list of parsers, down to the available ones. If there are none, report the test as skip...
  * `get_parsers` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* """Get parsers."""
  * `skip_if` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* """Skip conditional wrapper."""
  * `skip_no_lxml` **(Parameter Forwarders)** (Impact: 4.7)
    * *Intent:* """Decorator that skips lxml is not available."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 32`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 24`
* *Architecture:* `api: 14`, `import: 7`
* *Defense:* `safety: 4`, `doc: 16`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 191.138
  * `Choke Point (Betweenness):` 0.038162 | `Ripple Effect (Closeness):` 0.777778
  * `Imports (Out-Degree: 1):` bs4, bs4.builder, pytest, soupsieve, textwrap, unittest
  * `Imported By (In-Degree: 84):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/tests/test_level2/test_attribute.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.997)
- **Top Global Matches:** file_cluster_15: 5.997, file_cluster_2: 7.085, file_cluster_11: 7.138
- **Magnitude:** 113.4 | **LOC:** 420 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.1%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_attribute_type_xhtml` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* """Type is treated as case insensitive in XHTML."""
  * `test_attribute_type_html` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* """Type is treated as case insensitive in HTML."""
  * `test_attribute_type_xml` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* """Type is treated as case sensitive in XML."""
  * `test_multi_attribute` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* """Test multiple attribute."""
  * `test_attribute_start_dash` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* """Test attribute whose dash separated value starts with the specified value."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `unreferenced_by_name: 30`
* *Architecture:* `api: 31`, `import: 3`
* *Defense:* `doc: 40`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, bs4, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_extra/test_soup_contains.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.841)
- **Top Global Matches:** file_cluster_15: 4.841, file_cluster_11: 6.968, file_cluster_2: 7.013
- **Magnitude:** 100.66 | **LOC:** 318 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.5%), Connectivity (formerly Api Exposure) (10.7%), Complexity Load (formerly Cognitive Load) (5.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_contains_iframe` **(I/O & Config Routines)** (Impact: 5.9)
    * *Intent:* """Test contains with `iframe`."""
  * `test_contains_warn` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* """Test old alias raises a warning."""
  * `test_contains_cdata_lxml_html` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* """Test contains CDATA in `lxml` HTML parser."""
  * `test_contains_iframe_xml` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test contains with `iframe` which shouldn't matter in XML."""
  * `test_contains_escapes` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* """Test contains with escape characters."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 34`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 20`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `doc: 31`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, bs4, lxml, soupsieve, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level3/test_root.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.163)
- **Top Global Matches:** file_cluster_15: 5.163, file_cluster_11: 7.447, file_cluster_13: 7.458
- **Magnitude:** 95.82 | **LOC:** 189 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (16.0%), Connectivity (formerly Api Exposure) (9.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_no_iframe` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """Test that we don't count `iframe` as root."""
  * `test_iframe` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* """ Test that we only count `iframe` as root since the scoped element is the root. Not all the parse...
  * `test_root_iframe` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* """Test root."""
  * `test_root_whitespace` **(Compute Cores)** (Impact: 3.4)
    * *Intent:* """Test when there is root and white space."""
  * `test_root_preprocess` **(Compute Cores)** (Impact: 3.4)
    * *Intent:* """Test when there is root and pre-processing statement."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 19`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `unreferenced_by_name: 11`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `doc: 21`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, bs4, pytest, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/pretty.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 10.185)
- **Top Global Matches:** file_cluster_9: 10.185, file_cluster_12: 12.643, file_cluster_7: 13.434
- **Magnitude:** 86.28 | **LOC:** 149 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 58.976; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pretty` **(Compute Cores)** (Impact: 18.9)
    * *Intent:* """Make the object output string pretty."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.976
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.22567
  * `Imports (Out-Degree: 0):` __future__, re, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/tests/test_level4/test_lang.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.902)
- **Top Global Matches:** file_cluster_15: 5.902, file_cluster_2: 6.639, file_cluster_11: 6.946
- **Magnitude:** 78.54 | **LOC:** 404 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.0%), Connectivity (formerly Api Exposure) (10.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_language_list` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test language list."""
  * `test_xml_style_language` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test XML style language."""
  * `test_language_in_xhtml` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test language in XHTML."""
  * `test_language_in_xhtml_without_html_style_lang` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Test language in XHTML. HTML namespace elements must use HTML style language. """
  * `test_language_in_header` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* """Test that we can find language in header."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 23`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 20`
* *Architecture:* `api: 21`, `import: 1`
* *Defense:* `doc: 32`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/soupsieve/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.328)
- **Top Global Matches:** file_cluster_5: 6.328, file_cluster_7: 10.371, file_cluster_12: 10.768
- **Magnitude:** 69.24 | **LOC:** 169 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **8**; blast radius 191.622; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (76.0%), Guard Balance (formerly Safety Score) (69.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (48.8%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `match` **(Generic / Templated Code)** (Impact: 8.5)
  * `select` **(Generic / Templated Code)** (Impact: 3.5)
  * `iselect` **(Generic / Templated Code)** (Impact: 3.5)
  * `closest` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 36`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 2`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 191.622
  * `Choke Point (Betweenness):` 0.0437 | `Ripple Effect (Closeness):` 0.452015
  * `Imports (Out-Degree: 5):` .__meta__, .css_match, .css_parser, .css_types, .util, __future__, bs4, typing
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `soupsieve-2.8.3/tests/test_level3/test_namespace.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.34)
- **Top Global Matches:** file_cluster_15: 5.34, file_cluster_2: 6.88, file_cluster_11: 7.187
- **Magnitude:** 63.86 | **LOC:** 328 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.9%), Connectivity (formerly Api Exposure) (9.8%), Complexity Load (formerly Cognitive Load) (1.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap_xlink` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* """Wrap with `xlink`."""
  * `test_namespace_inherit` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test for a tag namespace inheritance."""
  * `test_namespace_with_default` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* """Test for a tag with a default namespace."""
  * `test_namespace_case` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* """Test that namespaces are always case sensitive."""
  * `test_namespace_no_default` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* """ Test for a tag with without specifying a default namespace. Because we employ level 4 selectors ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 19`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 14`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `doc: 21`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_dir.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.068)
- **Top Global Matches:** file_cluster_15: 5.068, file_cluster_2: 6.993, file_cluster_11: 7.02
- **Magnitude:** 57.68 | **LOC:** 216 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.4%), Connectivity (formerly Api Exposure) (9.5%), Complexity Load (formerly Cognitive Load) (5.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_iframe` **(I/O & Config Routines)** (Impact: 6.0)
    * *Intent:* """Test direction in `iframe`."""
  * `test_dir_on_input_root` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* """Test input direction when input is the root."""
  * `test_xml_in_html` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test cases for when we have XML in HTML."""
  * `test_dir_auto_root` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* """Test that the root is assumed left to right if auto used."""
  * `test_dir_bidi_detect` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* """Test bidirectional detection."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 11`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `doc: 18`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, bs4, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_scope.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.734)
- **Top Global Matches:** file_cluster_15: 6.734, file_cluster_16: 7.879, file_cluster_2: 7.937
- **Magnitude:** 51.06 | **LOC:** 81 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (15.4%), Connectivity (formerly Api Exposure) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_scope_is_select_target` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* """Test that scope is the element which scope is called on."""
  * `test_scope_cannot_select_target` **(Compute Cores)** (Impact: 3.3)
    * *Intent:* """Test that scope, the element which scope is called on, cannot be selected."""
  * `test_scope_is_root` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* """Test scope is the root when the a specific element is not the target of the select call."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_nesting_1/test_amp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.734)
- **Top Global Matches:** file_cluster_15: 6.734, file_cluster_16: 7.879, file_cluster_2: 7.937
- **Magnitude:** 51.06 | **LOC:** 81 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (15.4%), Connectivity (formerly Api Exposure) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_amp_is_select_target` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* """Test that ampersand is the element which scope is called on."""
  * `test_amp_cannot_select_target` **(Compute Cores)** (Impact: 3.3)
    * *Intent:* """Test that ampersand, the element which scope is called on, cannot be selected."""
  * `test_amp_is_root` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* """Test ampersand is the root when the a specific element is not the target of the select call."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level3/test_nth_child.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.49)
- **Top Global Matches:** file_cluster_15: 5.49, file_cluster_2: 5.876, file_cluster_11: 6.593
- **Magnitude:** 44.28 | **LOC:** 247 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.5%), Complexity Load (formerly Cognitive Load) (4.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_nth_child_no_parent` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* """Test `nth` child with no parent."""
  * `test_nth_child` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test `nth` child."""
  * `test_nth_child_odd` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test `nth` child odd."""
  * `test_nth_child_even` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test `nth` child even."""
  * `test_nth_child_complex` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test `nth` child complex."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `doc: 14`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_extra/test_custom.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.633)
- **Top Global Matches:** file_cluster_15: 5.633, file_cluster_2: 6.541, file_cluster_11: 6.783
- **Magnitude:** 40.84 | **LOC:** 144 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.5%), Connectivity (formerly Api Exposure) (10.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_custom_selectors` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test custom selectors."""
  * `test_custom_dependency` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* """Test custom selector dependency on other custom selectors."""
  * `test_custom_dependency_out_of_order` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* """Test custom selector out of order dependency."""
  * `test_custom_escapes` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """Test custom selectors with escapes."""
  * `test_custom_selectors_exotic` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* """Test custom selectors."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 10`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 13`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_extra/test_soup_contains_own.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.915)
- **Top Global Matches:** file_cluster_15: 4.915, file_cluster_13: 6.971, file_cluster_11: 6.996
- **Magnitude:** 40.52 | **LOC:** 113 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.3%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_contains_own_cdata_lxml_html` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* """Test contains CDATA in `lxml` HTML."""
  * `test_contains_own_cdata_html5` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """Test contains CDATA in HTML5."""
  * `test_contains_own_cdata_py_html` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """Test contains CDATA in Python HTML parser."""
  * `test_contains_own_cdata_xml` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """Test contains-own CDATA in XML."""
  * `test_contains_own_with_broken_text` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """Test contains-own to see how it matches a broken text."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `doc: 15`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..util, lxml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_has.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.625)
- **Top Global Matches:** file_cluster_15: 5.625, file_cluster_2: 6.716, file_cluster_11: 6.772
- **Magnitude:** 38.96 | **LOC:** 163 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.2%), Connectivity (formerly Api Exposure) (10.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_has_mixed` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* """Test has mixed."""
  * `test_has_nested_pseudo` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* """Test has with nested pseudo."""
  * `test_has_descendant` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* """Test has descendant."""
  * `test_has_next_sibling` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* """Test has next sibling."""
  * `test_has_subsequent_sibling` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* """Test has subsequent sibling."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 17`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `doc: 16`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_in_range.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.831)
- **Top Global Matches:** file_cluster_2: 5.831, file_cluster_11: 6.674, file_cluster_13: 6.708
- **Magnitude:** 36.46 | **LOC:** 238 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.3%), Connectivity (formerly Api Exposure) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_in_range_number` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range number."""
  * `test_in_range_range` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range range."""
  * `test_in_range_month` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range month."""
  * `test_in_range_week` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range week."""
  * `test_in_range_date` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range date."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 7`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 16`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_out_of_range.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.831)
- **Top Global Matches:** file_cluster_2: 5.831, file_cluster_11: 6.674, file_cluster_13: 6.708
- **Magnitude:** 36.46 | **LOC:** 238 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.3%), Connectivity (formerly Api Exposure) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_out_of_range_number` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range number."""
  * `test_out_of_range_range` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range range."""
  * `test_out_of_range_month` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range month."""
  * `test_out_of_range_week` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range week."""
  * `test_out_of_range_date` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test in range date."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 7`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 16`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_is.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.638)
- **Top Global Matches:** file_cluster_15: 5.638, file_cluster_2: 6.706, file_cluster_11: 6.776
- **Magnitude:** 35.58 | **LOC:** 132 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.1%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multiple_is` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* """Test `:is()` behavior when paired with `:not()`."""
  * `test_nested_is` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* """Test multiple nested selectors."""
  * `test_is_with_other_pseudo` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* """Test `:is()` behavior when paired with `:not()`."""
  * `test_is` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* """Test multiple selectors with "is"."""
  * `test_is_multi_comma` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* """Test multiple selectors but with an empty slot due to multiple commas."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `doc: 14`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..util, soupsieve
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `soupsieve-2.8.3/tests/test_level4/test_default.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.168)
- **Top Global Matches:** file_cluster_2: 6.168, file_cluster_15: 6.546, file_cluster_11: 6.682
- **Magnitude:** 32.48 | **LOC:** 210 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.7%), Connectivity (formerly Api Exposure) (7.3%), Complexity Load (formerly Cognitive Load) (6.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_iframe` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* """Test with `iframe`."""
  * `test_default` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """Test default."""
  * `test_default_cached` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Test that we use the cached "default". For the sake of coverage, we will do this impractical sel...
  * `test_nested_form` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* """ Test nested form. This is technically invalid use of forms, but browsers will generally evaluate...
  * `test_nested_form_fail` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* """ Test that the search for elements will bail after the first nested form. You shouldn't nest form...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 5`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 12`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..util, bs4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `soupsieve-2.8.3/soupsieve/__init__.py` -> **Severity: 2.134** (Bridge: 0.0437 * Flux: 48.8237%)
- `soupsieve-2.8.3/soupsieve/css_types.py` -> **Severity: 0.754** (Bridge: 0.0076 * Flux: 99.029%)
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `soupsieve-2.8.3/tests/util.py` -> **Severity: 54.206** (Embedded: 0.7778 * Error Risk: 69.6931%)
- `soupsieve-2.8.3/soupsieve/__init__.py` -> **Severity: 31.287** (Embedded: 0.452 * Error Risk: 69.2157%)
- `soupsieve-2.8.3/soupsieve/util.py` -> **Severity: 28.183** (Embedded: 0.3038 * Error Risk: 92.761%)
- `soupsieve-2.8.3/soupsieve/css_match.py` -> **Severity: 25.489** (Embedded: 0.3008 * Error Risk: 84.7411%)
- `soupsieve-2.8.3/soupsieve/css_parser.py` -> **Severity: 24.82** (Embedded: 0.2927 * Error Risk: 84.8096%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `soupsieve-2.8.3/soupsieve/__init__.py` -> **Severity: 14903.938** (Blast Radius: 191.622 * Doc Risk: 77.7778%)
- `soupsieve-2.8.3/soupsieve/__meta__.py` -> **Severity: 1272.165** (Blast Radius: 38.165 * Doc Risk: 33.3333%)
- `soupsieve-2.8.3/soupsieve/util.py` -> **Severity: 1097.002** (Blast Radius: 65.82 * Doc Risk: 16.6667%)
- `soupsieve-2.8.3/soupsieve/css_parser.py` -> **Severity: 874.238** (Blast Radius: 35.594 * Doc Risk: 24.5614%)
- `soupsieve-2.8.3/soupsieve/css_types.py` -> **Severity: 822.75** (Blast Radius: 65.82 * Doc Risk: 12.5%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1137 call pairs -- scoped 55.6%, unique 0.0%, ambiguous 4.4%, external 40.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 1137 | 55.6% | 0.0% | 4.4% | 40.0% |

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
