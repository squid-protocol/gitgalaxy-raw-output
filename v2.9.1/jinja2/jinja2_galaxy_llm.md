# ARCHITECTURAL_BRIEF: jinja2
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
- **Scope:** 54 analyzed artifact(s), 13946 LOC.
- **Load-bearing artifact:** `jinja2-3.1.6/requirements/typing.in` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `jinja2-3.1.6/src/jinja2/environment.py` -- pulls in 25 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `jinja2-3.1.6/src/jinja2/compiler.py` at magnitude 1747.9 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 54 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 13946 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2768 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1808 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 29.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.459 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 46 | 13930 | 85.2% |
| M4 | 3 | 9 | 5.6% |
| PLAINTEXT | 2 | 0 | 3.7% |
| HTML | 2 | 7 | 3.7% |
| MARKDOWN | 1 | 0 | 1.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.911`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.91; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 35%, Generic / Templated Code Files 30%, Data / Markup / Trivial 22%, Declarative / Non-Code 2%, Encapsulated Accessors Files 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 51 | 94.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 152 LOC), 1x Excluded (Machine-Generated Source Code Signature: 29 LOC)
- `.py`: 1x Excluded (Saturation: Line 5 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1207 LOC), 1x Packed Payload Guard (Impossible Density: 3.21 hits/line)
- `no_extension`: 2x Unsupported Format (.undeterminable)
- `.in`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.7 | 26.9 | 27.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 55.0 | 45.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 77.6 | 26.9 | 12.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 17.8 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.8 | 84.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 290 | 36 | 13 | `jinja2-3.1.6/tests/test_core_tags.py` |
| cleanup | 7 | 4 | 0 | `jinja2-3.1.6/src/jinja2/compiler.py` |
| guards | 1513 | 41 | 75 | `jinja2-3.1.6/tests/test_filters.py` |
| danger | 691 | 35 | 45 | `jinja2-3.1.6/src/jinja2/filters.py` |
| concurrency | 238 | 13 | 19 | `jinja2-3.1.6/src/jinja2/filters.py` |
| connectivity | 1503 | 45 | 76 | `jinja2-3.1.6/tests/test_lexnparse.py` |
| io | 99 | 10 | 3 | `jinja2-3.1.6/src/jinja2/loaders.py` |
| crypto | 2 | 2 | 0 | `jinja2-3.1.6/src/jinja2/bccache.py` |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 1 | 0 | `jinja2-3.1.6/tests/test_loader.py` |
| serialization | 7 | 5 | 0 | `jinja2-3.1.6/src/jinja2/bccache.py` |
| regex | 26 | 7 | 1 | `jinja2-3.1.6/src/jinja2/lexer.py` |
| events | 4 | 2 | 0 | `jinja2-3.1.6/src/jinja2/runtime.py` |
| tests | 913 | 25 | 60 | `jinja2-3.1.6/tests/test_lexnparse.py` |
| docs | 636 | 37 | 38 | `jinja2-3.1.6/src/jinja2/environment.py` |
| debt | 39 | 12 | 3 | `jinja2-3.1.6/tests/test_async.py` |
| mutation | 5729 | 45 | 285 | `jinja2-3.1.6/src/jinja2/parser.py` |
| dead_code | 704 | 35 | 45 | `jinja2-3.1.6/tests/test_lexnparse.py` |
| credential | 0 | 0 | 0 | - |
| threat | 107 | 20 | 6 | `jinja2-3.1.6/src/jinja2/runtime.py` |
| ml_ai | 13 | 2 | 0 | `jinja2-3.1.6/tests/test_utils.py` |
| ui | 867 | 26 | 69 | `jinja2-3.1.6/tests/test_filters.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.7842**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jinja2-3.1.6/src/jinja2/loaders.py` (Hits: 47)
- `jinja2-3.1.6/src/jinja2/bccache.py` (Hits: 19)
- `jinja2-3.1.6/tests/test_loader.py` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **typing.in** (`jinja2-3.1.6/requirements/typing.in`) — 21 inbound connections
2. **exceptions.py** (`jinja2-3.1.6/src/jinja2/exceptions.py`) — 19 inbound connections
3. **environment.py** (`jinja2-3.1.6/src/jinja2/environment.py`) — 18 inbound connections
4. **runtime.py** (`jinja2-3.1.6/src/jinja2/runtime.py`) — 15 inbound connections
5. **utils.py** (`jinja2-3.1.6/src/jinja2/utils.py`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **environment.py** (`jinja2-3.1.6/src/jinja2/environment.py`) — 25 outbound dependencies
2. **utils.py** (`jinja2-3.1.6/src/jinja2/utils.py`) — 20 outbound dependencies
3. **compiler.py** (`jinja2-3.1.6/src/jinja2/compiler.py`) — 19 outbound dependencies
4. **loaders.py** (`jinja2-3.1.6/src/jinja2/loaders.py`) — 18 outbound dependencies
5. **filters.py** (`jinja2-3.1.6/src/jinja2/filters.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `tokeniter` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/lexer.py`) -> Impact: **134.9** | LOC: 200
- `urlize` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/utils.py`) -> Impact: **108.9** | LOC: 121
- `visit_For` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **90.9** | LOC: 138
- `parse` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/ext.py`) -> Impact: **58.0** | LOC: 121
  * *Intent:* """Parse a translatable tag."""
- `visit_Template` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **56.0** | LOC: 121
  * *Intent:* # -- Statement Visitors
- `visit_Output` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **53.9** | LOC: 78
  * *Intent:* # If an extends is active, don't render outside a block. if frame.require_output_check: # A top-level extends is known to exist at compile time. if se...
- `_filter_test_common` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/environment.py`) -> Impact: **50.6** | LOC: 53
- `test_error_messages` **(Compute Cores)** (@ `jinja2-3.1.6/tests/test_lexnparse.py`) -> Impact: **50.2** | LOC: 35
- `signature` **(Many-Argument Workhorses)** (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **45.3** | LOC: 56
- `do_filesizeformat` **(Compute Cores)** (@ `jinja2-3.1.6/src/jinja2/filters.py`) -> Impact: **43.1** | LOC: 31
  * *Intent:* """Format the value like a 'human-readable' file size (i.e. 13 kB, 4.1 MB, 102 Bytes, etc). Per default decimal prefixes are used (Mega, Giga, etc.), ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `jinja2-3.1.6/src/jinja2` | 22 | 9559.32 | 41.32% | 7.53% |
| `jinja2-3.1.6/tests` | 23 | 5415.68 | 20.11% | 0.0% |
| `jinja2-3.1.6/requirements` | 3 | 34.68 | 0.0% | 0.0% |
| `jinja2-3.1.6/tests/res/templates` | 3 | 24.64 | 0.85% | 0.0% |
| `jinja2-3.1.6/tests/res` | 1 | 10.52 | 0.0% | 0.0% |
| `jinja2-3.1.6` | 2 | 2.16 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `jinja2-3.1.6/src/jinja2/meta.py` -> **99.9797%** Exposure
- `jinja2-3.1.6/src/jinja2/compiler.py` -> **15.1684%** Exposure
- `jinja2-3.1.6/src/jinja2/bccache.py` -> **11.6493%** Exposure
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **10.9602%** Exposure
- `jinja2-3.1.6/src/jinja2/loaders.py` -> **9.6612%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `jinja2-3.1.6/src/jinja2/debug.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/ext.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/idtracking.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/lexer.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jinja2-3.1.6/tests/test_filters.py` -> **100** Orphaned Functions | **0** Duplicates
- `jinja2-3.1.6/tests/test_lexnparse.py` -> **98** Orphaned Functions | **0** Duplicates
- `jinja2-3.1.6/tests/test_async.py` -> **58** Orphaned Functions | **11** Duplicates
- `jinja2-3.1.6/tests/test_core_tags.py` -> **58** Orphaned Functions | **0** Duplicates
- `jinja2-3.1.6/tests/test_regression.py` -> **53** Orphaned Functions | **3** Duplicates

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
- **Unknown Dependencies:** `274` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `jinja2-3.1.6/src/jinja2/compiler.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1747.9 | **LOC:** 1999 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **19**; blast radius 19.322; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.2%)
- **Documentation Coverage:** 69.4323% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_For` **(Many-Argument Workhorses)** (Impact: 90.9)
  * `visit_Template` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* # -- Statement Visitors
  * `visit_Output` **(Many-Argument Workhorses)** (Impact: 53.9)
    * *Intent:* # If an extends is active, don't render outside a block. if frame.require_output_check: # A top-leve...
  * `signature` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `pop_assign_tracking` **(Compute Cores)** (Impact: 38.5)
    * *Intent:* """Pops the topmost level for assignment tracking and updates the context variables if necessary. ""...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 156 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 264`, `args: 118`, `func_start: 118`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 215`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 110`, `concurrency: 14`, `import: 24`
* *Defense:* `safety: 37`, `doc: 50`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.322
  * `Choke Point (Betweenness):` 0.039687 | `Ripple Effect (Closeness):` 0.282353
  * `Imports (Out-Degree: 8):` , .environment, .exceptions, .idtracking, .nodes, .optimizer, .runtime, .utils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1244.84 | **LOC:** 1050 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 14.732; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.4%)
- **Documentation Coverage:** 84.4828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_fail_ut_eof` **(Many-Argument Workhorses)** (Impact: 33.3)
  * `parse_tuple` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `subparse` **(Defensive Guards)** (Impact: 26.6)
  * `parse_primary` **(Compute Cores)** (Impact: 26.3)
    * *Intent:* """Parse a name or literal value. If ``with_namespace`` is enabled, also parse namespace attr refs, ...
  * `parse_test` **(Compute Cores)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 225`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 256`, `dead_code: 1`
* *Architecture:* `api: 57`, `import: 9`
* *Defense:* `safety: 9`, `doc: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.732
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.269663
  * `Imports (Out-Degree: 4):` , .environment, .exceptions, .lexer, typing, typing_extensions
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/filters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1105.84 | **LOC:** 1874 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 12.395; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Concurrency Surface (formerly Concurrency) (94.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 75.1479% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_filesizeformat` **(Compute Cores)** (Impact: 43.1)
    * *Intent:* """Format the value like a 'human-readable' file size (i.e. 13 kB, 4.1 MB, 102 Bytes, etc). Per defa...
  * `do_urlize` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `do_indent` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `sync_do_join` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `do_xmlattr` **(Many-Argument Workhorses)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 259`, `args: 94`, `func_start: 85`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 111`, `state_mutation: 120`, `dead_code: 2`
* *Architecture:* `api: 83`, `concurrency: 24`, `import: 31`
* *Defense:* `safety: 50`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.395
  * `Choke Point (Betweenness):` 0.015898 | `Ripple Effect (Closeness):` 0.198347
  * `Imports (Out-Degree: 7):` .async_utils, .environment, .exceptions, .nodes, .runtime, .sandbox, .utils, collections...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/environment.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 975.4 | **LOC:** 1673 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **25**; blast radius 86.462; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.4%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 70.4225% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_filter_test_common` **(Many-Argument Workhorses)** (Impact: 50.6)
  * `overlay` **(Many-Argument Workhorses)** (Impact: 42.7)
  * `compile_templates` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `dump` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `_load_template` **(Stateful Encapsulated Methods)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 85
* *State Mutation (weighted view):* 311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 303`, `args: 75`, `func_start: 73`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 2`, `state_mutation: 149`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 6`, `api: 62`, `concurrency: 20`, `import: 61`
* *Defense:* `safety: 52`, `doc: 56`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 86.462
  * `Choke Point (Betweenness):` 0.151468 | `Ripple Effect (Closeness):` 0.428571
  * `Imports (Out-Degree: 12):` , .bccache, .compiler, .debug, .defaults, .exceptions, .ext, .lexer...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_lexnparse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 855.38 | **LOC:** 1031 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.4%), Complexity Load (formerly Cognitive Load) (21.6%), Connectivity (formerly Api Exposure) (13.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_error_messages` **(Compute Cores)** (Impact: 50.2)
  * `test_tuple_expr` **(Defensive Guards)** (Impact: 9.3)
  * `test_grouping` **(Defensive Guards)** (Impact: 8.9)
  * `test_function_calls` **(Compute Cores)** (Impact: 8.1)
  * `test_lineno_with_strip` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 279`, `args: 110`, `func_start: 109`, `class_start: 7`
* *Risk/State:* `state_mutation: 195`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 98`
* *Architecture:* `api: 115`, `import: 13`
* *Defense:* `safety: 125`, `doc: 44`, `test: 121`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jinja2, jinja2.lexer, pprint, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/runtime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 787.24 | **LOC:** 1063 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **13**; blast radius 88.834; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 62.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* # This requires a bit of explanation, In the past we used to # decide largely based on compile-time ...
  * `new_context` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `call` **(Many-Argument Workhorses)** (Impact: 22.4)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 14.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 79
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 253`, `args: 82`, `func_start: 82`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 136`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 19`, `import: 25`
* *Defense:* `safety: 20`, `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 88.834
  * `Choke Point (Betweenness):` 0.042307 | `Ripple Effect (Closeness):` 0.40678
  * `Imports (Out-Degree: 5):` .async_utils, .environment, .exceptions, .nodes, .utils, collections, functools, itertools...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_async.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 659.02 | **LOC:** 735 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.7%), Complexity Load (formerly Cognitive Load) (33.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_scoped_loop_var` **(Defensive Guards)** (Impact: 9.2)
  * `test_recursive_loop_filter` **(Defensive Guards)** (Impact: 6.4)
  * `test_nonrecursive_loop_filter` **(Defensive Guards)** (Impact: 6.3)
  * `test_recursive_depth0` **(Type Conversions)** (Impact: 5.9)
  * `test_recursive_depth` **(Type Conversions)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 140
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 257`, `args: 86`, `func_start: 82`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 118`, `fragile_debt: 1`, `duplicate_logic: 11`, `unreferenced_by_name: 58`
* *Architecture:* `api: 80`, `concurrency: 35`, `import: 12`
* *Defense:* `safety: 84`, `doc: 17`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` asyncio, bar, baz, context, jinja2, jinja2.async_utils, jinja2.exceptions, jinja2.nativetypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 648.06 | **LOC:** 871 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 14.856; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.3%)
- **Documentation Coverage:** 88.6076% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* """Parse a translatable tag."""
  * `_make_node` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `_parse_block` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `_install_callables` **(Stateful Encapsulated Methods)** (Impact: 14.4)
  * `_install_null` **(Stateful Encapsulated Methods)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 140`, `args: 43`, `func_start: 43`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 127`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 31`, `import: 19`
* *Defense:* `safety: 13`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.856
  * `Choke Point (Betweenness):` 0.003086 | `Ripple Effect (Closeness):` 0.269663
  * `Imports (Out-Degree: 7):` , .environment, .exceptions, .lexer, .parser, .runtime, .utils, gettext...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_filters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 626.78 | **LOC:** 884 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (23.0%), Complexity Load (formerly Cognitive Load) (18.0%), Connectivity (formerly Api Exposure) (13.6%)
- **Documentation Coverage:** 99.0338% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_filter_undefined_in_condexpr` **(Defensive Guards)** (Impact: 12.6)
  * `test_filter_undefined_in_elif` **(Defensive Guards)** (Impact: 9.1)
  * `test_filter_undefined_in_nested_if` **(Defensive Guards)** (Impact: 9.1)
  * `test_filter_undefined_in_else` **(Defensive Guards)** (Impact: 7.3)
  * `test_filter_undefined_in_if` **(Defensive Guards)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 276`, `args: 111`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `state_mutation: 200`, `unreferenced_by_name: 100`
* *Architecture:* `api: 105`, `import: 10`
* *Defense:* `safety: 131`, `doc: 38`, `test: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections, jinja2, jinja2.exceptions, markupsafe, pprint, pytest, random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/lexer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 584.84 | **LOC:** 869 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **10**; blast radius 38.803; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.6%)
- **Documentation Coverage:** 44.8276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tokeniter` **(Many-Argument Workhorses)** (Impact: 134.9)
  * `wrap` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 11.4)
    * *Intent:* # shortcuts e = re.escape def c(x: str) -> t.Pattern[str]: return re.compile(x, re.M | re.S) # lexin...
  * `compile_rules` **(I/O & Config Routines)** (Impact: 7.6)
    * *Intent:* """Compiles all the rules from the environment into a list of rules."""
  * `expect` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* """Expect a given token type and return it. This accepts the same argument as :meth:`jinja2.lexer.To...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 115`, `args: 34`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 145`, `dead_code: 4`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 8`, `doc: 28`, `test: 1`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 38.803
  * `Choke Point (Betweenness):` 0.009842 | `Ripple Effect (Closeness):` 0.311688
  * `Imports (Out-Degree: 4):` ._identifier, .environment, .exceptions, .utils, ast, collections, re, sys...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/utils.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 549.44 | **LOC:** 767 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **20**; blast radius 77.818; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.7%)
- **Documentation Coverage:** 41.4141% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlize` **(Many-Argument Workhorses)** (Impact: 108.9)
  * `generate_lorem_ipsum` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `select_autoescape` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `url_quote` **(Defensive Guards)** (Impact: 13.1)
    * *Intent:* """Quote a string for use in a URL using the given charset. :param obj: String or bytes to quote. Ot...
  * `import_string` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* """Imports an object based on a string. This is useful if you want to use import paths as endpoints ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 159`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 86`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 46`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 15`, `doc: 38`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 77.818
  * `Choke Point (Betweenness):` 0.040677 | `Ripple Effect (Closeness):` 0.4
  * `Imports (Out-Degree: 5):` .constants, .environment, .lexer, .runtime, collections, enum, jinja2, json...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/loaders.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 450.96 | **LOC:** 694 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **18**; blast radius 21.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Connectivity (formerly Api Exposure) (58.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 32.2)
  * `get_source` **(Defensive Guards)** (Impact: 15.7)
  * `load` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `list_templates` **(Compute Cores)** (Impact: 12.8)
  * `split_template_path` **(Generic / Templated Code)** (Impact: 12.1)
    * *Intent:* """Split a path into segments and perform a sanity check. If it detects '..' in the path it will rai...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 215
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 118`, `args: 34`, `func_start: 32`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 83`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 47`, `api: 31`, `import: 16`
* *Defense:* `safety: 27`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.603
  * `Choke Point (Betweenness):` 0.006639 | `Ripple Effect (Closeness):` 0.27907
  * `Imports (Out-Degree: 4):` .environment, .exceptions, .utils, collections, does, hashlib, importlib, importlib.util...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_core_tags.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 440.3 | **LOC:** 604 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.804; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (19.4%), Guard Balance (formerly Safety Score) (18.9%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_context_vars` **(Defensive Guards)** (Impact: 17.4)
  * `test_elif_deep` **(Defensive Guards)** (Impact: 10.7)
  * `test_scoped_loop_var` **(Defensive Guards)** (Impact: 9.2)
  * `test_complete` **(Defensive Guards)** (Impact: 8.9)
  * `test_namespace_loop` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 173`, `args: 65`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 78`, `fragile_debt: 6`, `unreferenced_by_name: 58`
* *Architecture:* `api: 69`, `import: 6`
* *Defense:* `safety: 88`, `doc: 29`, `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jinja2, pytest, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 430.98 | **LOC:** 740 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.5%), Complexity Load (formerly Cognitive Load) (27.7%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `interpolate` **(Compute Cores)** (Impact: 18.4)
  * `filter_stream` **(Compute Cores)** (Impact: 7.2)
  * `parse` **(Type Conversions)** (Impact: 5.9)
  * `test_basic_scope_behavior` **(Type Conversions)** (Impact: 5.7)
    * *Intent:* # This is what the old with statement compiled down to class ScopeExt(Extension): tags = {"scope"} d...
  * `npgettext` **(Parameter Forwarders)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 207`, `args: 68`, `func_start: 65`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 135`, `unreferenced_by_name: 45`
* *Architecture:* `api: 76`, `import: 17`
* *Defense:* `safety: 72`, `doc: 14`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io, jinja2, jinja2.exceptions, jinja2.ext, jinja2.lexer, pytest, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_regression.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 392.9 | **LOC:** 768 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (29.2%), Complexity Load (formerly Cognitive Load) (17.9%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_double_caller_no_default` **(Defensive Guards)** (Impact: 13.1)
  * `test_empty_if_condition_fails` **(Compute Cores)** (Impact: 9.0)
  * `test_call_with_args` **(Many-Argument Workhorses)** (Impact: 8.9)
  * `test_variable_reuse` **(Defensive Guards)** (Impact: 7.4)
  * `test_nested_for_else` **(Defensive Guards)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 172`, `args: 62`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `dead_code: 4`, `duplicate_logic: 3`, `unreferenced_by_name: 53`
* *Architecture:* `api: 62`, `import: 13`
* *Defense:* `safety: 68`, `doc: 29`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jinja2, jinja2.filters, jinja2.runtime, jinja2.utils, markupsafe, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/idtracking.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 353.78 | **LOC:** 319 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 14.412; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.6%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_For` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `visit_Name` **(Generic / Templated Code)** (Impact: 11.7)
  * `branch_update` **(Defensive Guards)** (Impact: 11.5)
  * `__init__` **(Generic / Templated Code)** (Impact: 8.7)
  * `visit_FromImport` **(Defensive Guards)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 71`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 50`
* *Architecture:* `api: 38`, `import: 4`
* *Defense:* `safety: 2`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.412
  * `Choke Point (Betweenness):` 0.000699 | `Ripple Effect (Closeness):` 0.217404
  * `Imports (Out-Degree: 2):` , .visitor, typing, typing_extensions
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 304.54 | **LOC:** 436 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.9%), Guard Balance (formerly Safety Score) (15.9%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 97.8022% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_Const` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* # This method is pure nonsense, but works fine for testing... if node.value == "foo": self.write(rep...
  * `test_autoescape_autoselect` **(Defensive Guards)** (Impact: 6.0)
  * `test_find_undeclared_variables` **(Defensive Guards)** (Impact: 6.0)
  * `test_finalize` **(Defensive Guards)** (Impact: 5.9)
  * `test_custom_code_generator` **(Defensive Guards)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 209`, `args: 47`, `func_start: 44`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 80`, `unreferenced_by_name: 37`
* *Architecture:* `io: 1`, `api: 54`, `import: 25`
* *Defense:* `safety: 87`, `doc: 1`, `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` a, b, jinja2, jinja2.compiler, jinja2.runtime, jinja2.sandbox, jinja2.utils, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_loader.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 282.86 | **LOC:** 437 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (36.9%), Guard Balance (formerly Safety Score) (28.3%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 95.7447% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile_down` **(Compute Cores)** (Impact: 6.5)
  * `teardown_method` **(Compute Cores)** (Impact: 6.1)
  * `find_spec` **(Parameter Forwarders)** (Impact: 5.0)
  * `test_pep_451_import_hook` **(Defensive Guards)** (Impact: 3.5)
  * `test_error_includes_paths` **(Type Conversions)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 151`, `args: 49`, `func_start: 48`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 98`, `unreferenced_by_name: 37`
* *Architecture:* `io: 14`, `api: 51`, `import: 17`
* *Defense:* `safety: 63`, `doc: 2`, `test: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` gc, importlib.abc, importlib.machinery, importlib.util, jinja2, jinja2.exceptions, jinja2.loaders, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_async_filters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 256.82 | **LOC:** 322 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (35.7%), Complexity Load (formerly Cognitive Load) (32.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_custom_async_iteratable_filter` **(Type Conversions)** (Impact: 7.0)
  * `customfilter` **(Type Conversions)** (Impact: 4.6)
  * `test_groupby_case` **(Defensive Guards)** (Impact: 4.5)
  * `closing` **(Defensive Guards)** (Impact: 3.2)
  * `make_aiter` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 103`, `args: 57`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 43`, `unreferenced_by_name: 25`
* *Architecture:* `api: 40`, `concurrency: 17`, `import: 8`
* *Defense:* `safety: 27`, `doc: 8`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` asyncio, collections, contextlib, jinja2, jinja2.async_utils, markupsafe, pytest, trio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/sandbox.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 208.32 | **LOC:** 437 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 12.647; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (63.0%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_internal_attribute` **(Defensive Guards)** (Impact: 31.2)
    * *Intent:* """Test if the attribute given is an internal python attribute. For example this function returns `T...
  * `wrap_str_format` **(Defensive Guards)** (Impact: 17.7)
    * *Intent:* """If the given value is a ``str.format`` or ``str.format_map`` method, return a new function than h...
  * `getitem` **(Defensive Guards)** (Impact: 13.2)
  * `get_field` **(Generic / Templated Code)** (Impact: 9.5)
  * `getattr` **(Defensive Guards)** (Impact: 8.9)
    * *Intent:* """Subscribe an object from sandboxed code and prefer the attribute. The attribute passed *must* be ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 90`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 26`
* *Architecture:* `api: 20`, `import: 14`
* *Defense:* `safety: 21`, `doc: 16`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.647
  * `Choke Point (Betweenness):` 0.006435 | `Ripple Effect (Closeness):` 0.164384
  * `Imports (Out-Degree: 4):` .environment, .exceptions, .runtime, _string, collections, functools, jinja2.sandbox, markupsafe...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/bccache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 188.12 | **LOC:** 409 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 16.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Connectivity (formerly Api Exposure) (58.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 56.5217% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_default_cache_dir` **(Stateful Encapsulated Methods)** (Impact: 17.9)
  * `dump_bytecode` **(Type Conversions)** (Impact: 7.5)
  * `load_bytecode` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* """Loads bytecode from a file or file like object."""
  * `load_bytecode` **(Defensive Guards)** (Impact: 5.6)
  * `get_cache_key` **(Generic / Templated Code)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 70`, `args: 26`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 35`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 19`, `api: 24`, `import: 15`
* *Defense:* `safety: 16`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.784
  * `Choke Point (Betweenness):` 0.005125 | `Ripple Effect (Closeness):` 0.272727
  * `Imports (Out-Degree: 2):` .environment, errno, fnmatch, hashlib, io, marshal, os, pickle...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_inheritance.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 182.6 | **LOC:** 411 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.804; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.4%), Complexity Load (formerly Cognitive Load) (11.8%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_invalid_required` **(Defensive Guards)** (Impact: 12.0)
  * `test_duplicate_required_or_scoped` **(Type Conversions)** (Impact: 9.7)
  * `test_required_with_scope` **(Type Conversions)** (Impact: 6.3)
  * `test_multi_inheritance` **(Defensive Guards)** (Impact: 6.1)
  * `test_level3_required` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 83`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `state_mutation: 44`, `unreferenced_by_name: 22`
* *Architecture:* `api: 25`, `import: 5`
* *Defense:* `safety: 25`, `doc: 14`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foo, jinja2, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/debug.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 159.02 | **LOC:** 192 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 15.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.4%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fake_traceback` **(Many-Argument Workhorses)** (Impact: 21.5)
  * `rewrite_traceback_stack` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """Rewrite the current exception to replace any tracebacks from within compiled template code with t...
  * `get_template_locals` **(Defensive Guards)** (Impact: 16.2)
    * *Intent:* """Based on the runtime locals, get the context that would be available at that point in the templat...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 24`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 33`
* *Architecture:* `io: 3`, `api: 3`, `import: 8`
* *Defense:* `safety: 4`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.82
  * `Choke Point (Betweenness):` 0.000815 | `Ripple Effect (Closeness):` 0.272727
  * `Imports (Out-Degree: 4):` .exceptions, .runtime, .utils, sys, types, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_compile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 148.72 | **LOC:** 109 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (32.0%), Connectivity (formerly Api Exposure) (8.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_top_level_set_vars_unpacking_deterministic` **(Defensive Guards)** (Impact: 6.8)
  * `test_loop_set_vars_unpacking_deterministic` **(Defensive Guards)** (Impact: 6.5)
  * `test_filters_deterministic` **(Defensive Guards)** (Impact: 6.2)
  * `test_block_set_vars_unpacking_deterministic` **(Defensive Guards)** (Impact: 5.0)
  * `test_import_as_with_context_deterministic` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 27`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 40`, `unreferenced_by_name: 6`
* *Architecture:* `io: 5`, `api: 6`, `import: 6`
* *Defense:* `safety: 6`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jinja2, jinja2.environment, jinja2.loaders, m, os, pytest, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_security.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 141.58 | **LOC:** 203 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 6.804; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.2%), Complexity Load (formerly Cognitive Load) (33.9%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_restricted` **(Compute Cores)** (Impact: 5.8)
  * `test_binary_operator_intercepting` **(Defensive Guards)** (Impact: 4.1)
  * `test_unary_operator_intercepting` **(Defensive Guards)** (Impact: 4.1)
  * `test_unsafe` **(Defensive Guards)** (Impact: 2.7)
  * `test_template_data` **(Defensive Guards)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 82`, `args: 27`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `state_mutation: 44`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 21`, `doc: 2`, `test: 32`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jinja2, jinja2.exceptions, jinja2.nodes, jinja2.sandbox, markupsafe, pytest
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

- `jinja2-3.1.6/src/jinja2/environment.py` -> **Severity: 15.147** (Bridge: 0.1515 * Flux: 99.9984%)
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 4.231** (Bridge: 0.0423 * Flux: 100.0%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 4.068** (Bridge: 0.0407 * Flux: 100.0%)
- `jinja2-3.1.6/src/jinja2/compiler.py` -> **Severity: 3.969** (Bridge: 0.0397 * Flux: 99.9995%)
- `jinja2-3.1.6/src/jinja2/defaults.py` -> **Severity: 2.271** (Bridge: 0.0227 * Flux: 99.9994%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 40.616** (Embedded: 0.4211 * Error Risk: 96.463%)
- `jinja2-3.1.6/src/jinja2/environment.py` -> **Severity: 40.527** (Embedded: 0.4286 * Error Risk: 94.5621%)
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 40.012** (Embedded: 0.4068 * Error Risk: 98.3624%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 39.702** (Embedded: 0.4 * Error Risk: 99.2543%)
- `jinja2-3.1.6/src/jinja2/lexer.py` -> **Severity: 28.978** (Embedded: 0.3117 * Error Risk: 92.9717%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 7831.4** (Blast Radius: 78.314 * Doc Risk: 100.0%)
- `jinja2-3.1.6/src/jinja2/environment.py` -> **Severity: 6088.87** (Blast Radius: 86.462 * Doc Risk: 70.4225%)
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 5516.307** (Blast Radius: 88.834 * Doc Risk: 62.0968%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 3222.762** (Blast Radius: 77.818 * Doc Risk: 41.4141%)
- `jinja2-3.1.6/src/jinja2/async_utils.py` -> **Severity: 3112.2** (Blast Radius: 31.122 * Doc Risk: 100.0%)

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
