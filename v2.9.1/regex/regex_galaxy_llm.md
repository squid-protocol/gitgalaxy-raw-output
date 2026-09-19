# ARCHITECTURAL_BRIEF: regex
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 11 analyzed artifact(s), 27817 LOC.
- **Load-bearing artifact:** `regex-2026.4.4/regex/_main.py` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `regex-2026.4.4/tools/build_regex_unicode.py` -- pulls in 10 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `regex-2026.4.4/src/_regex.c` at magnitude 13992.7 (structural weight, not risk).
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
| Total Artifacts | 16 |
| Analyzed Artifacts (Scanned) | 11 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 27817 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 6 | 8275 | 54.5% |
| C | 3 | 19542 | 27.3% |
| PLAINTEXT | 2 | 0 | 18.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 27%, Declarative / Non-Code 27%, Large Core Modules (3) 18%, Encapsulated Accessors Files 9%, Many-Argument Workhorses Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9 | 81.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 18.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.c`: 1x Excluded (Monolithic Amalgamation: 31587 LOC exceeds safe regex boundaries)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.0 | 37.0 | 13.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 67.1 | 79.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 93.5 | 14.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.5 | 26.2 | 11.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 27.8 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 57.3 | 99.2 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 5.2 | 1.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.4 | 90.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7538 | 6 | 255 | `regex-2026.4.4/src/_regex.c` |
| cleanup | 0 | 0 | 0 | - |
| guards | 774 | 5 | 190 | `regex-2026.4.4/src/_regex.c` |
| danger | 671 | 7 | 151 | `regex-2026.4.4/src/_regex.c` |
| concurrency | 5 | 2 | 2 | `regex-2026.4.4/tools/build_regex_unicode.py` |
| connectivity | 672 | 7 | 119 | `regex-2026.4.4/regex/_regex_core.py` |
| io | 27 | 4 | 7 | `regex-2026.4.4/regex/tests/test_regex.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 1 | 1 | 0 | `regex-2026.4.4/regex/tests/test_regex.py` |
| regex | 1 | 1 | 0 | `regex-2026.4.4/tools/build_regex_unicode.py` |
| events | 0 | 0 | 0 | - |
| tests | 106 | 1 | 0 | `regex-2026.4.4/regex/tests/test_regex.py` |
| docs | 107 | 4 | 18 | `regex-2026.4.4/regex/tests/test_regex.py` |
| debt | 182 | 5 | 66 | `regex-2026.4.4/regex/_regex_core.py` |
| mutation | 10442 | 7 | 1878 | `regex-2026.4.4/src/_regex.c` |
| dead_code | 114 | 4 | 6 | `regex-2026.4.4/regex/tests/test_regex.py` |
| credential | 3 | 1 | 0 | `regex-2026.4.4/regex/tests/test_regex.py` |
| threat | 345 | 2 | 23 | `regex-2026.4.4/src/_regex.c` |
| ml_ai | 13 | 1 | 0 | `regex-2026.4.4/src/_regex.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `regex-2026.4.4/regex/tests/test_regex.py` (Hits: 16)
- `regex-2026.4.4/tools/build_regex_unicode.py` (Hits: 7)
- `regex-2026.4.4/regex/_regex_core.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_main.py** (`regex-2026.4.4/regex/_main.py`) — 1 inbound connections
2. **_regex_core.py** (`regex-2026.4.4/regex/_regex_core.py`) — 1 inbound connections
3. **_regex.h** (`regex-2026.4.4/src/_regex.h`) — 1 inbound connections
4. **_regex_unicode.h** (`regex-2026.4.4/src/_regex_unicode.h`) — 1 inbound connections
5. **LICENSE.txt** (`regex-2026.4.4/LICENSE.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **build_regex_unicode.py** (`regex-2026.4.4/tools/build_regex_unicode.py`) — 10 outbound dependencies
2. **test_regex.py** (`regex-2026.4.4/regex/tests/test_regex.py`) — 8 outbound dependencies
3. **_regex_core.py** (`regex-2026.4.4/regex/_regex_core.py`) — 7 outbound dependencies
4. **_regex.c** (`regex-2026.4.4/src/_regex.c`) — 7 outbound dependencies
5. **_main.py** (`regex-2026.4.4/regex/_main.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `unicode_at_default_boundary` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/src/_regex.c`) -> Impact: **142.6** | LOC: 219
  * *Intent:* /* Checks whether a position is on a default word boundary. * * The rules are defined here: * https://www.unicode.org/reports/tr29/#Default_Word_Bound...
- `_compile` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/regex/_main.py`) -> Impact: **116.5** | LOC: 224
- `test_properties` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> Impact: **111.0** | LOC: 183
- `re_compile` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/src/_regex.c`) -> Impact: **95.9** | LOC: 256
  * *Intent:* /* Compiles regular expression code to a PatternObject. * * The regular expression code is provided as a list and is then compiled to * 'nodes'. Vario...
- `test_hg_bugs` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/regex/tests/test_regex.py`) -> Impact: **87.3** | LOC: 616
  * *Intent:* # Hg issue 28: regex.compile("(?>b)") causes "TypeError: 'Character' # object is not subscriptable" self.assertEqual(bool(regex.compile("(?>b)", flags...
- `unicode_at_grapheme_boundary` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/src/_regex.c`) -> Impact: **87.1** | LOC: 148
  * *Intent:* /* Checks whether a position is on a grapheme boundary. * * The rules are defined here: * https://www.unicode.org/reports/tr29/#Grapheme_Cluster_Bound...
- `parse_escape` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/regex/_regex_core.py`) -> Impact: **66.1** | LOC: 82
- `parse_sequence` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/regex/_regex_core.py`) -> Impact: **64.9** | LOC: 85
- `pattern_findall` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/src/_regex.c`) -> Impact: **64.4** | LOC: 128
  * *Intent:* /* PatternObject's 'findall' method. */
- `lookup_property` **(Many-Argument Workhorses)** (@ `regex-2026.4.4/regex/_regex_core.py`) -> Impact: **64.3** | LOC: 69

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `regex-2026.4.4/src` | 3 | 14152.04 | 33.36% | 2.55% |
| `regex-2026.4.4/regex` | 3 | 6054.5 | 48.54% | 35.6% |
| `regex-2026.4.4/regex/tests` | 1 | 1563.76 | 12.01% | 0.0% |
| `regex-2026.4.4` | 3 | 59.38 | 4.33% | 0.0% |
| `regex-2026.4.4/tools` | 1 | 1.81 | 62.43% | 12.04% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `regex-2026.4.4/regex/_regex_core.py` -> **93.4745%** Exposure
- `regex-2026.4.4/regex/_main.py` -> **13.319%** Exposure
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **12.0429%** Exposure
- `regex-2026.4.4/src/_regex.c` -> **7.6413%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `regex-2026.4.4/regex/_main.py` -> **100.0%** Exposure
- `regex-2026.4.4/regex/_regex_core.py` -> **100.0%** Exposure
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **100.0%** Exposure
- `regex-2026.4.4/src/_regex.c` -> **100.0%** Exposure
- `regex-2026.4.4/setup.py` -> **99.1837%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `regex-2026.4.4/regex/tests/test_regex.py` -> **101** Orphaned Functions | **0** Duplicates
- `regex-2026.4.4/regex/_regex_core.py` -> **0** Orphaned Functions | **68** Duplicates
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **5** Orphaned Functions | **0** Duplicates
- `regex-2026.4.4/src/_regex.c` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `42` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `regex-2026.4.4/src/_regex.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 13992.7 | **LOC:** 26651 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 63.111; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Complexity Load (formerly Cognitive Load) (96.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unicode_at_default_boundary` **(Many-Argument Workhorses)** (Impact: 142.6)
    * *Intent:* /* Checks whether a position is on a default word boundary. * * The rules are defined here: * https:...
  * `re_compile` **(Many-Argument Workhorses)** (Impact: 95.9)
    * *Intent:* /* Compiles regular expression code to a PatternObject. * * The regular expression code is provided ...
  * `unicode_at_grapheme_boundary` **(Many-Argument Workhorses)** (Impact: 87.1)
    * *Intent:* /* Checks whether a position is on a grapheme boundary. * * The rules are defined here: * https://ww...
  * `pattern_findall` **(Many-Argument Workhorses)** (Impact: 64.4)
    * *Intent:* /* PatternObject's 'findall' method. */
  * `fold_case` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* /* Folds the case of a string. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3867 instances
* *State Mutation (weighted view):* 12182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5371`, `structural_boundaries: 2981`, `args: 1157`, `func_start: 129`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 370`, `state_mutation: 4448`, `unreferenced_by_name: 1`
* *Architecture:* `api: 48`, `import: 7`
* *Defense:* `safety: 349`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Python.h, _regex.h, ctype.h, pyport.h, pythread.h, structmember.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/regex/_regex_core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 5455.16 | **LOC:** 4677 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 162.354; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Debt Markers (formerly Tech Debt) (93.5%), Complexity Load (formerly Cognitive Load) (92.1%)
- **Documentation Coverage:** 98.8746% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_escape` **(Many-Argument Workhorses)** (Impact: 66.1)
  * `parse_sequence` **(Many-Argument Workhorses)** (Impact: 64.9)
  * `lookup_property` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `_compile_replacement` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `parse_paren` **(Many-Argument Workhorses)** (Impact: 37.5)
    * *Intent:* """Parses a parenthesised subpattern or a flag. Returns FLAGS if it's an inline flag. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 750 instances
* *State Mutation (weighted view):* 2581
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 889`, `structural_boundaries: 915`, `args: 355`, `func_start: 353`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 1081`, `dead_code: 5`, `duplicate_logic: 68`
* *Architecture:* `io: 3`, `api: 322`, `import: 6`
* *Defense:* `safety: 110`, `doc: 6`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 162.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` collections, enum, is, random, regex, string, unicodedata
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/regex/tests/test_regex.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1563.76 | **LOC:** 4541 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 63.111; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (12.0%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_properties` **(Many-Argument Workhorses)** (Impact: 111.0)
  * `test_hg_bugs` **(Many-Argument Workhorses)** (Impact: 87.3)
    * *Intent:* # Hg issue 28: regex.compile("(?>b)") causes "TypeError: 'Character' # object is not subscriptable" ...
  * `test_repeat_minmax` **(Compute Cores)** (Impact: 45.6)
  * `test_partial` **(Compute Cores)** (Impact: 40.8)
  * `test_branch_reset` **(Compute Cores)** (Impact: 36.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 348
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 167`, `args: 166`, `func_start: 111`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 164`, `dead_code: 1`, `fragile_debt: 66`, `unreferenced_by_name: 101`
* *Architecture:* `io: 16`, `api: 113`, `import: 8`
* *Defense:* `safety: 6`, `doc: 69`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` array, copy, pickle, regex, string, sys, unittest, weakref
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/regex/_main.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 585.78 | **LOC:** 757 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 116.756; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.5%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_compile` **(Many-Argument Workhorses)** (Impact: 116.5)
  * `escape` **(Many-Argument Workhorses)** (Impact: 35.8)
    * *Intent:* """Escape a string for use as a literal in a pattern. If special_only is True, escape only special c...
  * `_compile_replacement_helper` **(Stateful Encapsulated Methods)** (Impact: 26.8)
  * `match` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* # -------------------------------------------------------------------- # Public interface.
  * `prefixmatch` **(Many-Argument Workhorses)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 92`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 118`, `fragile_debt: 1`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 22`, `doc: 14`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 116.756
  * `Choke Point (Betweenness):` 0.011111 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` copyreg, locale, regex, regex._regex_core, threading
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/src/_regex_unicode.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 140.0 | **LOC:** 319 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 162.354; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (94.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 106`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 119`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 162.354
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/changelog.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 30.96 | **LOC:** 1548 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 24.24 | **LOC:** 17 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 63.111; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (79.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os.path, setuptools, sysconfig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/src/_regex.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 19.34 | **LOC:** 236 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 116.756; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 116.756
  * `Choke Point (Betweenness):` 0.011111 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` _regex_unicode.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `regex-2026.4.4/regex/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 13.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 63.111; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` regex._main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 4.18 | **LOC:** 209 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `regex-2026.4.4/tools/build_regex_unicode.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1.81 | **LOC:** 1786 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 63.111; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (62.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_code` **(Many-Argument Workhorses)** (Impact: 62.0)
  * `write_summary` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `generate_all_cases` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `generate_script_extensions_lookup` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `generate_full_case_folding` **(Many-Argument Workhorses)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 364 instances
* *State Mutation (weighted view):* 1157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 162`, `args: 59`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 429`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 7`, `api: 47`, `import: 10`
* *Defense:* `safety: 12`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 63.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` codecs, contextlib, io, itertools, os, os.path, re, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `regex-2026.4.4/regex/_main.py` -> **Severity: 1.111** (Bridge: 0.0111 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `regex-2026.4.4/regex/_regex_core.py` -> **Severity: 13.209** (Embedded: 0.1333 * Error Risk: 99.0655%)
- `regex-2026.4.4/regex/_main.py` -> **Severity: 9.944** (Embedded: 0.1 * Error Risk: 99.4357%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `regex-2026.4.4/regex/_regex_core.py` -> **Severity: 16052.687** (Blast Radius: 162.354 * Doc Risk: 98.8746%)
- `regex-2026.4.4/regex/_main.py` -> **Severity: 10614.183** (Blast Radius: 116.756 * Doc Risk: 90.9091%)
- `regex-2026.4.4/regex/tests/test_regex.py` -> **Severity: 6311.1** (Blast Radius: 63.111 * Doc Risk: 100.0%)
- `regex-2026.4.4/tools/build_regex_unicode.py` -> **Severity: 6311.1** (Blast Radius: 63.111 * Doc Risk: 100.0%)
- `regex-2026.4.4/src/_regex.c` -> **Severity: 6311.1** (Blast Radius: 63.111 * Doc Risk: 100.0%)

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
