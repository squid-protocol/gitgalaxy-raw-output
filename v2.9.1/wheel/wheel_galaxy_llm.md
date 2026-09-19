# ARCHITECTURAL_BRIEF: wheel
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
- **Scope:** 26 analyzed artifact(s), 2357 LOC.
- **Load-bearing artifact:** `wheel-0.46.3/src/wheel/wheelfile.py` -- 10 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `wheel-0.46.3/src/wheel/_bdist_wheel.py` -- pulls in 25 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `wheel-0.46.3/src/wheel/_bdist_wheel.py` at magnitude 512.2 (structural weight, not risk).
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
| Total Artifacts | 31 |
| Analyzed Artifacts (Scanned) | 26 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 2357 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3923 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.278 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3514 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 24 | 2357 | 92.3% |
| PLAINTEXT | 2 | 0 | 7.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 19%, Large Core Modules (2) 19%, Generic / Templated Code Files 12%, Large Core Modules (3) 12%, Many-Argument Workhorses Files 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 24 | 92.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 7.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 39 LOC)
- `.whl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 69.1 | 23.6 | 18.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.4 | 61.5 | 70.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 62.2 | 3.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.1 | 1.1 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 59.2 | 18.8 | 8.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.1 | 8.4 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.7 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.4 | 89.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 38 | 12 | 3 | `wheel-0.46.3/src/wheel/_bdist_wheel.py` |
| cleanup | 1 | 1 | 0 | `wheel-0.46.3/src/wheel/wheelfile.py` |
| guards | 123 | 16 | 12 | `wheel-0.46.3/tests/commands/test_tags.py` |
| danger | 42 | 11 | 4 | `wheel-0.46.3/src/wheel/wheelfile.py` |
| concurrency | 30 | 5 | 1 | `wheel-0.46.3/src/wheel/_metadata.py` |
| connectivity | 127 | 20 | 13 | `wheel-0.46.3/src/wheel/_bdist_wheel.py` |
| io | 103 | 18 | 7 | `wheel-0.46.3/src/wheel/_bdist_wheel.py` |
| crypto | 1 | 1 | 0 | `wheel-0.46.3/src/wheel/wheelfile.py` |
| ipc | 6 | 3 | 0 | `wheel-0.46.3/tests/test_sdist.py` |
| time | 1 | 1 | 0 | `wheel-0.46.3/src/wheel/wheelfile.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 12 | 5 | 1 | `wheel-0.46.3/src/wheel/_commands/convert.py` |
| events | 0 | 0 | 0 | - |
| tests | 111 | 9 | 9 | `wheel-0.46.3/tests/test_wheelfile.py` |
| docs | 58 | 13 | 7 | `wheel-0.46.3/src/wheel/macosx_libfile.py` |
| debt | 22 | 7 | 2 | `wheel-0.46.3/tests/test_wheelfile.py` |
| mutation | 1057 | 23 | 93 | `wheel-0.46.3/src/wheel/_bdist_wheel.py` |
| dead_code | 38 | 11 | 3 | `wheel-0.46.3/tests/test_wheelfile.py` |
| credential | 6 | 1 | 0 | `wheel-0.46.3/tests/test_wheelfile.py` |
| threat | 7 | 2 | 0 | `wheel-0.46.3/src/wheel/_bdist_wheel.py` |
| ml_ai | 3 | 1 | 0 | `wheel-0.46.3/tests/test_metadata.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.575**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` (Hits: 39)
- `wheel-0.46.3/src/wheel/wheelfile.py` (Hits: 13)
- `wheel-0.46.3/src/wheel/_commands/pack.py` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wheelfile.py** (`wheel-0.46.3/src/wheel/wheelfile.py`) — 10 inbound connections
2. **_metadata.py** (`wheel-0.46.3/src/wheel/_metadata.py`) — 4 inbound connections
3. **util.py** (`wheel-0.46.3/tests/commands/util.py`) — 4 inbound connections
4. **convert.py** (`wheel-0.46.3/src/wheel/_commands/convert.py`) — 2 inbound connections
5. **tags.py** (`wheel-0.46.3/src/wheel/_commands/tags.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_bdist_wheel.py** (`wheel-0.46.3/src/wheel/_bdist_wheel.py`) — 25 outbound dependencies
2. **convert.py** (`wheel-0.46.3/src/wheel/_commands/convert.py`) — 17 outbound dependencies
3. **wheelfile.py** (`wheel-0.46.3/src/wheel/wheelfile.py`) — 13 outbound dependencies
4. **_metadata.py** (`wheel-0.46.3/src/wheel/_metadata.py`) — 11 outbound dependencies
5. **test_convert.py** (`wheel-0.46.3/tests/commands/test_convert.py`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `tags` **(Many-Argument Workhorses)** (@ `wheel-0.46.3/src/wheel/_commands/tags.py`) -> Impact: **56.0** | LOC: 115
- `calculate_macosx_platform_tag` **(Many-Argument Workhorses)** (@ `wheel-0.46.3/src/wheel/macosx_libfile.py`) -> Impact: **50.8** | LOC: 80
  * *Intent:* """ Calculate proper macosx platform tag basing on files which are included to wheel Example platform tag `macosx-10.14-x86_64` """
- `__init__` **(Compute Cores)** (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> Impact: **39.6** | LOC: 29
- `test_pack` **(Many-Argument Workhorses)** (@ `wheel-0.46.3/tests/commands/test_pack.py`) -> Impact: **32.6** | LOC: 64
- `pack` **(Many-Argument Workhorses)** (@ `wheel-0.46.3/src/wheel/_commands/pack.py`) -> Impact: **30.9** | LOC: 59
  * *Intent:* """Repack a previously unpacked wheel directory into a new wheel file. The .dist-info/WHEEL file must contain one or more tags so that the target whee...
- `open` **(Stateful Encapsulated Methods)** (@ `wheel-0.46.3/src/wheel/wheelfile.py`) -> Impact: **30.7** | LOC: 33
- `get_tag` **(Compute Cores)** (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> Impact: **28.3** | LOC: 57
  * *Intent:* # bdist sets self.plat_name if unset, we should only use it for purepy # wheels if the user supplied it. if self.plat_name_supplied: plat_name = cast(...
- `egg2dist` **(Many-Argument Workhorses)** (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> Impact: **25.5** | LOC: 70
  * *Intent:* """Convert an .egg-info directory into a .dist-info directory"""
- `license_paths` **(Compute Cores)** (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> Impact: **24.8** | LOC: 43
- `convert` **(Many-Argument Workhorses)** (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> Impact: **24.6** | LOC: 51

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `wheel-0.46.3/src/wheel` | 9 | 1250.56 | 23.45% | 8.45% |
| `wheel-0.46.3/src/wheel/_commands` | 5 | 626.74 | 43.15% | 0.0% |
| `wheel-0.46.3/tests/commands` | 6 | 404.72 | 17.03% | 0.0% |
| `wheel-0.46.3/tests` | 4 | 136.14 | 9.08% | 0.0% |
| `wheel-0.46.3` | 1 | 1.0 | 0.0% | 0.0% |
| `wheel-0.46.3/tests/testdata` | 1 | 0.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `wheel-0.46.3/src/wheel/_setuptools_logging.py` -> **62.2459%** Exposure
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **13.7842%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_commands/pack.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_commands/tags.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_metadata.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wheel-0.46.3/tests/test_wheelfile.py` -> **11** Orphaned Functions | **0** Duplicates
- `wheel-0.46.3/tests/commands/test_tags.py` -> **10** Orphaned Functions | **0** Duplicates
- `wheel-0.46.3/tests/commands/test_convert.py` -> **6** Orphaned Functions | **0** Duplicates
- `wheel-0.46.3/tests/commands/test_unpack.py` -> **3** Orphaned Functions | **0** Duplicates
- `wheel-0.46.3/tests/test_metadata.py` -> **2** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `154` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `wheel-0.46.3/src/wheel/_bdist_wheel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 512.2 | **LOC:** 617 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 61.282; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Complexity Load (formerly Cognitive Load) (61.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 67.4419% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_tag` **(Compute Cores)** (Impact: 28.3)
    * *Intent:* # bdist sets self.plat_name if unset, we should only use it for purepy # wheels if the user supplied...
  * `egg2dist` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* """Convert an .egg-info directory into a .dist-info directory"""
  * `license_paths` **(Compute Cores)** (Impact: 24.8)
  * `run` **(I/O & Config Routines)** (Impact: 22.8)
  * `get_abi_tag` **(I/O & Config Routines)** (Impact: 21.9)
    * *Intent:* """Return the ABI tag based on SOABI (if available) or emulate SOABI (PyPy2)."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 102`, `args: 22`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 116`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 39`, `api: 20`, `import: 30`
* *Defense:* `safety: 10`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 61.282
  * `Choke Point (Betweenness):` 0.01 | `Ripple Effect (Closeness):` 0.053333
  * `Imports (Out-Degree: 3):` , ._metadata, .macosx_libfile, .wheelfile, __future__, collections.abc, email.generator, email.message...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/_commands/convert.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 340.86 | **LOC:** 338 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 34.621; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Compute Cores)** (Impact: 39.6)
  * `convert` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `__init__` **(Compute Cores)** (Impact: 18.1)
  * `convert_pkg_info` **(Compute Cores)** (Impact: 17.0)
  * `generate_contents` **(Compute Cores)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 67`, `args: 12`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 62`
* *Architecture:* `io: 3`, `api: 13`, `import: 17`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.621
  * `Choke Point (Betweenness):` 0.005 | `Ripple Effect (Closeness):` 0.08
  * `Imports (Out-Degree: 3):` .., .._metadata, ..wheelfile, __future__, abc, collections, collections.abc, email.message...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/macosx_libfile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 302.22 | **LOC:** 487 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 41.185; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (51.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calculate_macosx_platform_tag` **(Many-Argument Workhorses)** (Impact: 50.8)
    * *Intent:* """ Calculate proper macosx platform tag basing on files which are included to wheel Example platfor...
  * `extract_macosx_min_system_version` **(Defensive Guards)** (Impact: 22.6)
  * `read_mach_header` **(Compute Cores)** (Impact: 18.0)
  * `get_base_class_and_magic_number` **(Compute Cores)** (Impact: 13.4)
  * `swap32` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 48`, `args: 7`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 72`, `dead_code: 1`
* *Architecture:* `io: 7`, `api: 15`, `import: 7`
* *Defense:* `safety: 6`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 41.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 0):` __future__, ctypes, io, os, sys, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/wheelfile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 234.34 | **LOC:** 242 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **13**; blast radius 181.704; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.2%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Stateful Encapsulated Methods)** (Impact: 30.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `write_files` **(Compute Cores)** (Impact: 16.6)
  * `writestr` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `close` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* # Write RECORD if self.fp is not None and self.mode == "w" and self._file_hashes: data = StringIO() ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 42`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 42`
* *Architecture:* `io: 13`, `api: 12`, `import: 13`
* *Defense:* `safety: 8`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 181.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.384
  * `Imports (Out-Degree: 0):` __future__, _typeshed, base64, csv, hashlib, io, logging, os.path...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/commands/test_convert.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 161.02 | **LOC:** 292 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (19.2%), Connectivity (formerly Api Exposure) (9.3%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bdist_wininst_path` **(Many-Argument Workhorses)** (Impact: 14.2)
    * *Intent:* # As bdist_wininst is no longer present in Python, and carrying .exe files in the # tarball is risky...
  * `test_convert_egg_directory` **(Defensive Guards)** (Impact: 9.6)
  * `expected_wheel_filename` **(Generic / Templated Code)** (Impact: 9.0)
  * `test_convert_bdist_wininst` **(Defensive Guards)** (Impact: 8.3)
  * `test_convert_egg_file` **(Defensive Guards)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 77`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 29`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`, `api: 13`, `import: 12`
* *Defense:* `safety: 21`, `doc: 7`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, _pytest.fixtures, commands.util, email.message, pathlib, pytest, textwrap, wheel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_metadata.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 141.82 | **LOC:** 185 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 91.493; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.4%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_requirements` **(Compute Cores)** (Impact: 14.2)
  * `pkginfo_to_metadata` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* """ Convert .egg-info directory with PKG-INFO to the Metadata 2.1 format """
  * `split_sections` **(Generic / Templated Code)** (Impact: 12.6)
  * `requires_to_requires_dist` **(Generic / Templated Code)** (Impact: 7.7)
    * *Intent:* """Return the version specifier for a requirement in PEP 345/566 fashion."""
  * `convert_requirements` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* """Yield Requires-Dist: strings for parsed requirements strings."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 43`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 23`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 8`, `import: 11`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 91.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.196923
  * `Imports (Out-Degree: 0):` __future__, collections.abc, email.message, email.parser, functools, itertools, os.path, packaging.requirements...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/_commands/tags.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 131.46 | **LOC:** 141 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 37.681; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.9%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tags` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `_compute_tags` **(Stateful Encapsulated Methods)** (Impact: 7.5)
    * *Intent:* """Add or replace tags. Supports dot-separated tags"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 27`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 29`
* *Architecture:* `io: 6`, `api: 1`, `import: 7`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.681
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.09
  * `Imports (Out-Degree: 1):` ..wheelfile, __future__, collections.abc, email.parser, email.policy, itertools, os
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/test_wheelfile.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 98.84 | **LOC:** 205 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.4%), Complexity Load (formerly Cognitive Load) (16.5%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_timestamp` **(Defensive Guards)** (Impact: 7.0)
  * `test_attributes` **(Defensive Guards)** (Impact: 6.2)
    * *Intent:* # With the change from ZipFile.write() to .writestr(), we need to manually # set member attributes. ...
  * `test_testzip_bad_hash` **(Generic / Templated Code)** (Impact: 4.8)
  * `test_testzip_missing_hash` **(Generic / Templated Code)** (Impact: 4.6)
  * `test_weak_hash_algorithm` **(Generic / Templated Code)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 71`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 17`, `unreferenced_by_name: 11`
* *Architecture:* `io: 2`, `api: 12`, `import: 8`
* *Defense:* `safety: 13`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pathlib, pytest, stat, sys, wheel.wheelfile, zipfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/test_tags.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 97.6 | **LOC:** 233 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (30.3%), Guard Balance (formerly Safety Score) (29.4%), Connectivity (formerly Api Exposure) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_permission_bits` **(Defensive Guards)** (Impact: 6.7)
  * `test_plat_tags` **(Defensive Guards)** (Impact: 3.4)
  * `test_multi_tags` **(Defensive Guards)** (Impact: 2.8)
  * `test_python_tags` **(Defensive Guards)** (Impact: 2.5)
  * `test_abi_tags` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 73`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 45`, `unreferenced_by_name: 10`
* *Architecture:* `io: 1`, `api: 11`, `import: 8`
* *Defense:* `safety: 35`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .util, __future__, pathlib, pytest, shutil, subprocess, wheel.wheelfile, zipfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/test_pack.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 89.1 | **LOC:** 93 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (32.1%), Connectivity (formerly Api Exposure) (3.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pack` **(Many-Argument Workhorses)** (Impact: 32.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 24`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 9`
* *Defense:* `safety: 4`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .util, __future__, email.message, email.parser, email.policy, os, pytest, zipfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_commands/pack.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 74.1 | **LOC:** 85 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 27.872; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pack` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* """Repack a previously unpacked wheel directory into a new wheel file. The .dist-info/WHEEL file mus...
  * `compute_tagline` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* """Compute a tagline from a list of tags. :param tags: A list of tags :return: A tagline """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 22`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 8`, `api: 2`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.872
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.04
  * `Imports (Out-Degree: 1):` ..wheelfile, __future__, email.generator, email.parser, email.policy, os.path, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/_commands/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 64.46 | **LOC:** 154 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (75.1%), Connectivity (formerly Api Exposure) (53.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parser` **(I/O & Config Routines)** (Impact: 7.2)
  * `parse_build_tag` **(Generic / Templated Code)** (Impact: 6.0)
  * `tags_f` **(Generic / Templated Code)** (Impact: 5.1)
  * `main` **(Defensive Guards)** (Impact: 3.6)
  * `unpack_f` **(Generic / Templated Code)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 34`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 3`, `api: 8`, `import: 11`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .., ..wheelfile, .convert, .pack, .tags, .unpack, __future__, argparse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/util.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 26.2 | **LOC:** 44 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 71.069; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (23.3%), Complexity Load (formerly Cognitive Load) (20.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_command` **(Defensive Guards)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 21`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 71.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.16
  * `Imports (Out-Degree: 0):` __future__, io, os, pytest, subprocess, sys, unittest.mock, wheel._commands
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/test_sdist.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 20.64 | **LOC:** 52 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 23.822; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (14.2%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_compare_sdists` **(Type Conversions)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 6`
* *Defense:* `safety: 1`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathlib, pytest, subprocess, sys, tarfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/test_unpack.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 20.28 | **LOC:** 80 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (36.1%), Connectivity (formerly Api Exposure) (6.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_unpack` **(Defensive Guards)** (Impact: 2.6)
  * `test_chmod_outside_unpack_tree` **(Defensive Guards)** (Impact: 2.3)
  * `test_unpack_executable_bit` **(Defensive Guards)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 29`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 8`
* *Defense:* `safety: 7`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .util, __future__, pathlib, platform, pytest, stat, wheel.wheelfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_commands/unpack.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 15.86 | **LOC:** 31 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 27.872; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (76.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unpack` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* """Unpack a wheel. Wheel content will be unpacked to {dest}/{name}-{ver}, where {name} is the packag...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.872
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.04
  * `Imports (Out-Degree: 1):` ..wheelfile, __future__, pathlib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/bdist_wheel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.32 | **LOC:** 27 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 44.071; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`
* *Risk/State:* None
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.071
  * `Choke Point (Betweenness):` 0.006667 | `Ripple Effect (Closeness):` 0.04
  * `Imports (Out-Degree: 1):` ._bdist_wheel, setuptools.command.bdist_wheel, typing, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/metadata.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.3 | **LOC:** 18 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 26`
* *Risk/State:* None
* *Architecture:* `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ._metadata, it, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/test_metadata.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 13.48 | **LOC:** 97 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.7%), Connectivity (formerly Api Exposure) (4.8%), Complexity Load (formerly Cognitive Load) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pkginfo_to_metadata` **(I/O & Config Routines)** (Impact: 4.3)
  * `test_metadata_deprecated` **(Defensive Guards)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 3`, `doc: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pathlib, pytest, wheel, wheel._metadata
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 12.04 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 23.822; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/__main__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 9.74 | **LOC:** 26 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 23.822; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (82.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (10.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._commands, __future__, os.path, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_setuptools_logging.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 7.58 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.822; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.2%), Debt Markers (formerly Tech Debt) (62.2%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configure` **(I/O & Config Routines)** (Impact: 1.8)
    * *Intent:* """ Configure logging to emit warning and above to stderr and everything else to stdout. This behavi...
  * `_not_warning` **(Encapsulated Accessors)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, logging, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/test_bdist_wheel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3.18 | **LOC:** 7 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 23.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Complexity Load (formerly Cognitive Load) (2.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_import_bdist_wheel` **(Generic / Templated Code)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, wheel.bdist_wheel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/testdata/eggnames.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.76 | **LOC:** 88 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
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

- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **Severity: 1.0** (Bridge: 0.01 * Flux: 100.0%)
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **Severity: 0.5** (Bridge: 0.005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wheel-0.46.3/src/wheel/wheelfile.py` -> **Severity: 36.888** (Embedded: 0.384 * Error Risk: 96.0616%)
- `wheel-0.46.3/src/wheel/_metadata.py` -> **Severity: 19.228** (Embedded: 0.1969 * Error Risk: 97.6427%)
- `wheel-0.46.3/tests/commands/util.py` -> **Severity: 10.64** (Embedded: 0.16 * Error Risk: 66.5013%)
- `wheel-0.46.3/src/wheel/_commands/tags.py` -> **Severity: 8.706** (Embedded: 0.09 * Error Risk: 96.7278%)
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **Severity: 7.87** (Embedded: 0.08 * Error Risk: 98.3735%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wheel-0.46.3/src/wheel/wheelfile.py` -> **Severity: 14345.058** (Blast Radius: 181.704 * Doc Risk: 78.9474%)
- `wheel-0.46.3/tests/commands/util.py` -> **Severity: 7106.9** (Blast Radius: 71.069 * Doc Risk: 100.0%)
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **Severity: 4132.975** (Blast Radius: 61.282 * Doc Risk: 67.4419%)
- `wheel-0.46.3/src/wheel/_metadata.py` -> **Severity: 4066.351** (Blast Radius: 91.493 * Doc Risk: 44.4444%)
- `wheel-0.46.3/src/wheel/macosx_libfile.py` -> **Severity: 3530.143** (Blast Radius: 41.185 * Doc Risk: 85.7143%)

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
