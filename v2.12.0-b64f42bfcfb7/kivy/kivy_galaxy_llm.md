# ARCHITECTURAL_BRIEF: kivy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kivy/kivy.git` |
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
- **Scope:** 665 analyzed artifact(s), 86568 LOC.
- **Load-bearing artifact:** `kivy/app.py` -- 158 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `doc/autobuild.py` -- pulls in 45 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `kivy/uix/textinput.py` at magnitude 3691.72 (structural weight, not risk).
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
| Total Artifacts | 1207 |
| Analyzed Artifacts (Scanned) | 665 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 542 |
| Total LOC | 86568 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 55.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.357 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1615 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2159 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 48 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 570 | 81680 | 85.7% |
| XML | 18 | 6 | 2.7% |
| PLAINTEXT | 16 | 0 | 2.4% |
| YAML | 15 | 1092 | 2.3% |
| MARKDOWN | 12 | 0 | 1.8% |
| JSON | 11 | 842 | 1.7% |
| CPP | 11 | 1331 | 1.7% |
| OBJECTIVE-C | 5 | 818 | 0.8% |
| SHELL | 4 | 521 | 0.6% |
| MAKEFILE | 2 | 249 | 0.3% |
| GLSL | 1 | 29 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 665 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 32%, Data / Markup / Trivial 18%, Large Core Modules (3) 18%, Declarative / Non-Code 7%, Encapsulated Accessors Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 633 | 95.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 29 | 4.4% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 542*

**Composition by Extension & Reason:**
- `.png`: 252x Excluded (Explicitly Denied Extension: '.png')
- `.kv`: 90x Excluded (Unsupported Extension: '.kv')
- `.rst`: 47x Excluded (Unsupported Extension: '.rst')
- `.jpg`: 44x Excluded (Explicitly Denied Extension: '.jpg')
- `.wav`: 18x Excluded (Explicitly Denied Extension: '.wav')
- `.gif`: 15x Excluded (Explicitly Denied Extension: '.gif')
- `.c`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 7x Excluded (Explicitly Denied Extension: '.zip')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ttf`: 6x Excluded (Explicitly Denied Extension: '.ttf')
- `.spec`: 5x Excluded (Unsupported Extension: '.spec')
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.4 | 28.5 | 28.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.7 | 55.6 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.9 | 8.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 84.7 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.6 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 95.8 | 6.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 68.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1307 | 220 | 5 | `kivy/core/camera/camera_avfoundation_implem.mm` |
| cleanup | 80 | 40 | 0 | `kivy/core/camera/camera_avfoundation_implem.mm` |
| guards | 4529 | 331 | 21 | `kivy/uix/textinput.py` |
| danger | 2376 | 334 | 10 | `kivy/graphics/cgl_backend/cgl_mock.pyx` |
| concurrency | 498 | 83 | 1 | `kivy/tools/pep8checker/pep8.py` |
| connectivity | 6332 | 526 | 25 | `kivy/graphics/opengl.pyx` |
| io | 723 | 159 | 3 | `kivy/tools/image-testsuite/imagemagick-testsuite.sh` |
| crypto | 2 | 2 | 0 | `kivy/loader.py` |
| ipc | 65 | 17 | 0 | `kivy/tests/pyinstaller/test_pyinstaller.py` |
| time | 20 | 13 | 0 | `kivy/core/camera/camera_avfoundation_implem.mm` |
| serialization | 3 | 3 | 0 | `kivy/gesture.py` |
| regex | 64 | 17 | 0 | `kivy/tools/pep8checker/pep8.py` |
| events | 765 | 78 | 2 | `kivy/_event.pyx` |
| tests | 1358 | 93 | 4 | `kivy/tests/test_properties.py` |
| docs | 3840 | 442 | 18 | `kivy/graphics/opengl.pyx` |
| debt | 1002 | 195 | 4 | `setup.py` |
| mutation | 40462 | 537 | 171 | `kivy/uix/textinput.py` |
| dead_code | 1925 | 309 | 7 | `kivy/lib/sdl3.pxi` |
| credential | 96 | 6 | 0 | `examples/gestures/my_gestures.py` |
| threat | 36 | 14 | 0 | `kivy/tests/test_imageloader.py` |
| ml_ai | 10 | 6 | 0 | `kivy/core/camera/camera_opencv.py` |
| ui | 126 | 32 | 0 | `kivy/tests/test_graphics.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `kivy/tools/image-testsuite/imagemagick-testsuite.sh` (Hits: 42)
- `kivy/tools/pep8checker/pep8.py` (Hits: 39)
- `setup.py` (Hits: 25)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **app.py** (`kivy/app.py`) — 158 inbound connections
2. **builder.py** (`kivy/lang/builder.py`) — 113 inbound connections
3. **logger.py** (`kivy/logger.py`) — 108 inbound connections
4. **clock.py** (`kivy/clock.py`) — 104 inbound connections
5. **__init__.py** (`kivy/lang/__init__.py`) — 102 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **autobuild.py** (`doc/autobuild.py`) — 45 outbound dependencies
2. **__init__.py** (`kivy/core/window/__init__.py`) — 31 outbound dependencies
3. **textinput.py** (`kivy/uix/textinput.py`) — 29 outbound dependencies
4. **common.py** (`kivy/tests/common.py`) — 28 outbound dependencies
5. **settings.py** (`kivy/uix/settings.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `layout_text` **(Many-Argument Workhorses)** (@ `kivy/core/text/text_layout.pyx`) -> Impact: **313.2** | LOC: 324
- `continued_indentation` **(Many-Argument Workhorses)** (@ `kivy/tools/pep8checker/pep8.py`) -> Impact: **241.8** | LOC: 197
- `shorten_post` **(Many-Argument Workhorses)** (@ `kivy/core/text/markup.py`) -> Impact: **222.1** | LOC: 376
  * *Intent:* ''' Shortens the text to a single line according to the label options. This function operates on a text that has already been laid out because for mar...
- `layout_text_unrestricted` **(Many-Argument Workhorses)** (@ `kivy/core/text/text_layout.pyx`) -> Impact: **196.0** | LOC: 103
- `_thread_run` **(Many-Argument Workhorses)** (@ `kivy/input/providers/hidinput.py`) -> Impact: **181.8** | LOC: 346
- `dispatch_visit` **(Many-Argument Workhorses)** (@ `kivy/uix/rst.py`) -> Impact: **160.6** | LOC: 372
- `layout_hint_with_bounds` **(Many-Argument Workhorses)** (@ `kivy/uix/layout.py`) -> Impact: **157.9** | LOC: 216
- `_pre_render` **(Stateful Encapsulated Methods)** (@ `kivy/core/text/markup.py`) -> Impact: **148.3** | LOC: 307
  * *Intent:* # split markup, words, and lines # result: list of word with position and width/height # during the first pass, we don't care about h/valign self._cac...
- `upload_uniform` **(Many-Argument Workhorses)** (@ `kivy/graphics/shader.pyx`) -> Impact: **143.8** | LOC: 237
  * *Intent:* '''Pass a uniform variable to the shader. '''
- `log_cgl_funcs` **(I/O & Config Routines)** (@ `kivy/graphics/cgl.pyx`) -> Impact: **142.9** | LOC: 259

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `kivy/uix` | 50 | 21189.42 | 37.29% | 18.88% |
| `kivy/graphics` | 47 | 12238.06 | 27.83% | 41.48% |
| `kivy` | 34 | 11028.64 | 38.2% | 7.55% |
| `kivy/tests` | 83 | 10619.9 | 18.26% | 0.0% |
| `kivy/core/text` | 9 | 4575.14 | 57.41% | 32.04% |
| `kivy/core/window` | 8 | 3719.22 | 43.95% | 64.55% |
| `kivy/input/providers` | 13 | 3438.2 | 69.03% | 11.33% |
| `kivy/modules` | 13 | 2529.64 | 37.78% | 8.75% |
| `kivy/uix/behaviors` | 11 | 2069.46 | 37.55% | 2.87% |
| `examples/widgets` | 43 | 1962.57 | 18.7% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/test_ubuntu_python.yml` -> **100.0%** Exposure
- `kivy/core/spelling/spelling_osxappkit.py` -> **100.0%** Exposure
- `kivy/core/window/window_info.pxd` -> **100.0%** Exposure
- `kivy/core/window/window_info.pyx` -> **100.0%** Exposure
- `kivy/graphics/context_instructions.pxd` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doc/autobuild.py` -> **100.0%** Exposure
- `doc/sources/conf.py` -> **100.0%** Exposure
- `doc/sources/sphinxext/preprocess.py` -> **100.0%** Exposure
- `examples/settings/main.py` -> **100.0%** Exposure
- `kivy/__init__.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `kivy/lib/sdl3.pxi` -> **277** Orphaned Functions | **14** Duplicates
- `kivy/tests/test_properties.py` -> **40** Orphaned Functions | **27** Duplicates
- `kivy/tests/test_provider_registry.py` -> **45** Orphaned Functions | **0** Duplicates
- `kivy/tests/test_utils.py` -> **43** Orphaned Functions | **0** Duplicates
- `kivy/tests/test_vector.py` -> **42** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3104` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `kivy/uix/textinput.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.482)
- **Top Global Matches:** file_cluster_4: 5.482, file_cluster_16: 10.069, file_cluster_12: 10.125
- **Magnitude:** 3691.72 | **LOC:** 4018 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **29**; blast radius 0.829; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.3%)
- **Documentation Coverage:** 72.4138% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_cursor_movement` **(Many-Argument Workhorses)** (Impact: 106.5)
    * *Intent:* '''Move the cursor relative to its current position. Action can be one of : - cursor_left: move the ...
  * `keyboard_on_key_down` **(Stateful Encapsulated Methods)** (Impact: 64.9)
  * `_draw_line` **(Many-Argument Workhorses)** (Impact: 63.0)
  * `_show_cut_copy_paste` **(Many-Argument Workhorses)** (Impact: 57.7)
  * `insert_text` **(Many-Argument Workhorses)** (Impact: 55.5)
    * *Intent:* '''Insert new text at the current cursor position. Override this function in order to pre-process te...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 574 instances
* *State Mutation (weighted view):* 2003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 362`, `args: 147`, `func_start: 138`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 855`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 70`, `import: 31`
* *Defense:* `safety: 25`, `doc: 93`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.829
  * `Choke Point (Betweenness):` 0.004205 | `Ripple Effect (Closeness):` 0.118074
  * `Imports (Out-Degree: 21):` itertools, kivy.animation, kivy.app, kivy.base, kivy.cache, kivy.clock, kivy.config, kivy.core.clipboard...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `kivy/uix/scrollview.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.008)
- **Top Global Matches:** file_cluster_4: 6.008, file_cluster_6: 7.162, file_cluster_16: 13.314
- **Magnitude:** 2358.28 | **LOC:** 3544 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **16**; blast radius 0.807; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.6%)
- **Documentation Coverage:** 89.6552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_scroll_initialize` **(Stateful Encapsulated Methods)** (Impact: 56.3)
    * *Intent:* # This is the first phase of the scroll gesture, call from on_touch_down # it is used to determine i...
  * `on_touch_down` **(Many-Argument Workhorses)** (Impact: 48.1)
    * *Intent:* # -------------------------------------------------- # - in_bar_x: bool - Touch started on horizonta...
  * `_change_touch_mode` **(Stateful Encapsulated Methods)** (Impact: 48.1)
    * *Intent:* # SCROLL TIMEOUT HANDLER - GESTURE DETECTION TIMEOUT # =============================================...
  * `on_touch_move` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* # SCROLLVIEW TOUCH HANDLING WITH ARBITRARY DEPTH HIERARCHY # =======================================...
  * `_check_nested_delegation` **(Many-Argument Workhorses)** (Impact: 44.8)
    * *Intent:* # Check if this ScrollView should delegate to its parent in hierarchy. # # Uses the hierarchy to fin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 321`, `args: 86`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 438`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 16`
* *Defense:* `safety: 11`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.807
  * `Choke Point (Betweenness):` 0.004208 | `Ripple Effect (Closeness):` 0.119061
  * `Imports (Out-Degree: 15):` enum, functools, kivy.animation, kivy.app, kivy.clock, kivy.config, kivy.effects.dampedscroll, kivy.factory...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `kivy/graphics/vertex_instructions_line.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.699)
- **Top Global Matches:** file_cluster_4: 5.699, file_cluster_6: 9.083, file_cluster_16: 11.959
- **Magnitude:** 1776.24 | **LOC:** 1785 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.395; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%)
- **Documentation Coverage:** 96.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_extended` **(Many-Argument Workhorses)** (Impact: 92.1)
  * `build_smooth` **(I/O & Config Routines)** (Impact: 56.9)
    * *Intent:* # FIXME: Some artifacts can be observed, depending on the line width, # overdraw_width and radius. T...
  * `build_legacy` **(I/O & Config Routines)** (Impact: 34.4)
  * `prebuild_rounded_rectangle` **(Stateful Encapsulated Methods)** (Impact: 32.5)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 347 instances
* *State Mutation (weighted view):* 1249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 93`, `args: 57`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 555`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 9`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` itertools, kivy.cache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/graphics/vertex_instructions.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.602)
- **Top Global Matches:** file_cluster_12: 6.602, file_cluster_16: 7.599, file_cluster_15: 7.67
- **Magnitude:** 1757.88 | **LOC:** 2301 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.873; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 70.0565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_triangle_strip` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `build` **(I/O & Config Routines)** (Impact: 30.0)
  * `build` **(I/O & Config Routines)** (Impact: 27.8)
  * `build` **(I/O & Config Routines)** (Impact: 24.4)
  * `build` **(I/O & Config Routines)** (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 275 instances
* *State Mutation (weighted view):* 1066
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 164`, `args: 119`, `func_start: 119`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 516`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 29`
* *Architecture:* `api: 60`, `import: 3`
* *Defense:* `safety: 12`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.873
  * `Choke Point (Betweenness):` 0.000248 | `Ripple Effect (Closeness):` 0.003765
  * `Imports (Out-Degree: 5):` kivy.logger, kivy.utils, os
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/graphics/svg.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.566)
- **Top Global Matches:** file_cluster_4: 5.566, file_cluster_15: 8.819, file_cluster_12: 9.002
- **Magnitude:** 1563.9 | **LOC:** 1279 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.842; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 82.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_element` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `parse_path` **(Many-Argument Workhorses)** (Impact: 60.8)
    * *Intent:* # In the SVG specs, initial movetos are absolute, even if # specified as 'm'. This is the default be...
  * `parse_color` **(Type Conversions)** (Impact: 39.0)
  * `arc_to` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 294 instances
* *State Mutation (weighted view):* 1020
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 94`, `args: 51`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 432`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 21`, `import: 11`
* *Defense:* `safety: 10`, `doc: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.842
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.003012
  * `Imports (Out-Degree: 6):` array, gzip, kivy.core.window, kivy.logger, kivy.properties, kivy.utils, math, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/properties.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.214)
- **Top Global Matches:** file_cluster_12: 7.214, file_cluster_15: 8.17, file_cluster_16: 9.315
- **Magnitude:** 1481.54 | **LOC:** 2249 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.792; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (81.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%)
- **Documentation Coverage:** 81.1828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert` **(Many-Argument Workhorses)** (Impact: 66.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `set` **(Many-Argument Workhorses)** (Impact: 34.3)
    * *Intent:* # Takes the a python object of the type used by this property # (see :attr:`val_type`), and saves it...
  * `convert` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `_parse_str` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* ''' Takes a ConfigParser's string (or any value supplied by the user), and converts it to the python...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 163 instances
* *State Mutation (weighted view):* 588
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 229`, `args: 139`, `func_start: 139`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 262`, `planned_debt: 2`
* *Architecture:* `api: 38`, `import: 8`
* *Defense:* `safety: 36`, `doc: 37`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.792
  * `Choke Point (Betweenness):` 0.000237 | `Ripple Effect (Closeness):` 0.003012
  * `Imports (Out-Degree: 5):` functools, kivy._metrics, kivy.clock, kivy.config, kivy.logger, kivy.utils, kivy.weakmethod, weakref
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/core/window/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.025)
- **Top Global Matches:** file_cluster_12: 7.025, file_cluster_7: 8.879, file_cluster_5: 9.348
- **Magnitude:** 1392.84 | **LOC:** 2600 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **57** in-repo importer(s); it depends on **31**; blast radius 6.222; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.8%)
- **Documentation Coverage:** 44.3478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_childsize` **(Compute Cores)** (Impact: 54.6)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 46.0)
  * `request_keyboard` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `on_keyboard` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `on_motion` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* '''Event called when a motion event is received. :Parameters: `etype`: str One of "begin", "update" ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 175 instances
* *State Mutation (weighted view):* 627
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 320`, `args: 144`, `func_start: 138`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 277`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 92`, `import: 36`
* *Defense:* `safety: 5`, `doc: 111`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.222
  * `Choke Point (Betweenness):` 0.022406 | `Ripple Effect (Closeness):` 0.237888
  * `Imports (Out-Degree: 24):` android, collections, ios, kivy.animation, kivy.base, kivy.cache, kivy.clock, kivy.config...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `kivy/core/text/markup.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.064)
- **Top Global Matches:** file_cluster_6: 6.064, file_cluster_4: 11.446, file_cluster_8: 14.375
- **Magnitude:** 1309.26 | **LOC:** 961 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 1.266; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.8%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 37.037% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shorten_post` **(Many-Argument Workhorses)** (Impact: 222.1)
    * *Intent:* ''' Shortens the text to a single line according to the label options. This function operates on a t...
  * `_pre_render` **(Stateful Encapsulated Methods)** (Impact: 148.3)
    * *Intent:* # split markup, words, and lines # result: list of word with position and width/height # during the ...
  * `render_lines` **(Many-Argument Workhorses)** (Impact: 64.0)
  * `n_restricted` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* ''' Similar to the function `n`, except it only returns the first occurrence and it's not an iterato...
  * `p_restricted` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* ''' Similar to `n_restricted`, except it returns the first occurrence starting from the right, like ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 740
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 92`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 286`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 6`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.266
  * `Choke Point (Betweenness):` 0.000916 | `Ripple Effect (Closeness):` 0.130269
  * `Imports (Out-Degree: 3):` copy, functools, kivy.core.text, kivy.core.text.text_layout, kivy.logger, kivy.parser, kivy.properties, re
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `kivy/multistroke.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.542)
- **Top Global Matches:** file_cluster_12: 7.542, file_cluster_4: 9.161, file_cluster_7: 9.657
- **Magnitude:** 1214.06 | **LOC:** 1475 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.584; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.9%)
- **Documentation Coverage:** 55.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter` **(Many-Argument Workhorses)** (Impact: 67.1)
    * *Intent:* ''':meth:`filter` returns a subset of objects in :attr:`self.db`, according to given criteria. This ...
  * `recognize` **(Many-Argument Workhorses)** (Impact: 54.7)
    * *Intent:* '''Search for gestures matching `strokes`. Returns a :class:`ProgressTracker` instance. This method ...
  * `_recognize_tick` **(Stateful Encapsulated Methods)** (Impact: 23.5)
    * *Intent:* # This callback is scheduled once per frame until completed
  * `match_candidate` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* '''Match a given candidate against this MultistrokeGesture object. Will test against all templates a...
  * `_add_result` **(Stateful Encapsulated Methods)** (Impact: 20.8)
    * *Intent:* # Add a result; used internally by the recognize() function if tpl <= len(res): n = gesture.template...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 205 instances
* *State Mutation (weighted view):* 661
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 158`, `args: 58`, `func_start: 56`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 251`, `fragile_debt: 5`
* *Architecture:* `io: 2`, `api: 50`, `import: 12`
* *Defense:* `safety: 10`, `doc: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.584
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.004518
  * `Imports (Out-Degree: 4):` base64, collections, io, kivy.clock, kivy.event, kivy.properties, kivy.vector, math...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.133)
- **Top Global Matches:** file_cluster_4: 7.133, file_cluster_6: 10.3, file_cluster_12: 11.769
- **Magnitude:** 1165.12 | **LOC:** 1527 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.395; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.8%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 45.122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `determine_gl_flags` **(I/O & Config Routines)** (Impact: 30.3)
  * `determine_sdl3` **(I/O & Config Routines)** (Impact: 26.6)
  * `build_extensions` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* # build files config_h_fn = ('include', 'config.h') config_pxi_fn = ('include', 'config.pxi') config...
  * `get_extensions_from_sources` **(Compute Cores)** (Impact: 15.3)
  * `determine_angle_flags` **(I/O & Config Routines)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 278 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 906
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 122`, `args: 22`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 3`, `state_mutation: 350`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 25`, `api: 22`, `import: 27`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Cython, collections, copy, kivy, kivy.tools.packaging.cython_cfg, kivy.tools.packaging.factory, kivy.tools.packaging.osx.build, kivy.tools.packaging.win32.build...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/window/_window_sdl3.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.209)
- **Top Global Matches:** file_cluster_4: 5.209, file_cluster_15: 8.867, file_cluster_16: 8.946
- **Magnitude:** 1108.68 | **LOC:** 1150 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.395; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.8%)
- **Documentation Coverage:** 98.1982% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup_window` **(Many-Argument Workhorses)** (Impact: 130.6)
  * `poll` **(Compute Cores)** (Impact: 93.6)
  * `show_keyboard` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `custom_titlebar_handler_callback` **(Compute Cores)** (Impact: 42.1)
  * `set_system_cursor` **(Compute Cores)** (Impact: 25.9)
    * *Intent:* # prevent the compiler to not be happy because of # an uninitialized value (return False in Cython i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 473
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 220`, `args: 64`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 183`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 45`, `import: 8`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` android, ctypes, kivy, kivy.app, kivy.config, kivy.logger, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/text/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.527)
- **Top Global Matches:** file_cluster_4: 7.527, file_cluster_6: 11.108, file_cluster_12: 11.222
- **Magnitude:** 1074.24 | **LOC:** 1241 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **16**; blast radius 2.726; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.9%)
- **Documentation Coverage:** 40.5405% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 110.9)
  * `shorten` **(Many-Argument Workhorses)** (Impact: 82.2)
    * *Intent:* ''' Shortens the text to fit into a single line by the width specified by :attr:`text_size` [0]. If ...
  * `render_lines` **(Many-Argument Workhorses)** (Impact: 62.1)
  * `render` **(Stateful Encapsulated Methods)** (Impact: 44.5)
    * *Intent:* '''Return a tuple (width, height) to create the image with the user constraints. (width, height) inc...
  * `resolve_font_name` **(Compute Cores)** (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 568
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 135`, `args: 43`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 1`, `state_mutation: 210`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 10`, `api: 33`, `import: 16`
* *Defense:* `safety: 5`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.726
  * `Choke Point (Betweenness):` 0.001425 | `Ripple Effect (Closeness):` 0.135064
  * `Imports (Out-Degree: 7):` ast, copy, functools, kivy, kivy.config, kivy.core, kivy.core.text.text_layout, kivy.core.text.text_pango...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `kivy/uix/rst.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.631)
- **Top Global Matches:** file_cluster_4: 7.631, file_cluster_12: 9.105, file_cluster_7: 11.145
- **Magnitude:** 1030.9 | **LOC:** 1489 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 0.73; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 84.3137% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch_visit` **(Many-Argument Workhorses)** (Impact: 160.6)
  * `dispatch_departure` **(Many-Argument Workhorses)** (Impact: 80.0)
  * `brute_refs` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* # get foot/cit refs manually because the output from # docutils' parser doesn't contain any of these...
  * `get_refs` **(Compute Cores)** (Impact: 26.0)
    * *Intent:* # get foot/cit refs manually because the output from # docutils' parser doesn't contain any of these...
  * `goto` **(Many-Argument Workhorses)** (Impact: 13.3)
    * *Intent:* '''Scroll to the reference. If it's not found, nothing will be done. For this text:: .. _myref: This...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 575
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 150`, `args: 30`, `func_start: 29`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 247`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 54`, `import: 22`
* *Defense:* `safety: 24`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.73
  * `Choke Point (Betweenness):` 0.000269 | `Ripple Effect (Closeness):` 0.003012
  * `Imports (Out-Degree: 16):` docutils, docutils.parsers, docutils.parsers.rst, docutils.parsers.rst.roles, kivy.animation, kivy.base, kivy.clock, kivy.lang...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/_event.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.821)
- **Top Global Matches:** file_cluster_12: 7.821, file_cluster_4: 7.906, file_cluster_15: 9.71
- **Magnitude:** 1019.04 | **LOC:** 1343 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **5**; blast radius 8.226; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%), Complexity Load (formerly Cognitive Load) (48.5%)
- **Documentation Coverage:** 41.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_dispatch` **(Many-Argument Workhorses)** (Impact: 117.8)
  * `dispatch` **(Many-Argument Workhorses)** (Impact: 73.5)
  * `__cinit__` **(Stateful Encapsulated Methods)** (Impact: 33.2)
  * `create_property` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* '''Create a new property at runtime. .. versionadded:: 1.0.9 .. versionchanged:: 1.8.0 `value` param...
  * `funbind` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* '''Similar to unbind, except we only remove the first match, and we don't deref the observers before...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 353
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 130`, `args: 51`, `func_start: 51`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 135`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 17`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.226
  * `Choke Point (Betweenness):` 0.000982 | `Ripple Effect (Closeness):` 0.263812
  * `Imports (Out-Degree: 2):` collections, functools, kivy.utils, kivy.weakmethod, kivy.weakproxy
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `kivy/modules/console.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.885)
- **Top Global Matches:** file_cluster_12: 6.885, file_cluster_7: 9.374, file_cluster_4: 9.587
- **Magnitude:** 978.5 | **LOC:** 1054 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.403; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.8%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `show_property` **(Many-Argument Workhorses)** (Impact: 94.5)
    * *Intent:* # normal call: (tree node, focus, ) # nested call: (widget, prop value, prop key, index in dict/list...
  * `keyboard_shortcut` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `on_widget` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `highlight_at` **(Defensive Guards)** (Impact: 16.9)
    * *Intent:* """Select a widget from a x/y window coordinate. This is mostly used internally when Select mode is ...
  * `_update_widget_tree_node` **(Stateful Encapsulated Methods)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 178`, `args: 67`, `func_start: 67`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 181`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 75`, `import: 24`
* *Defense:* `safety: 29`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.403
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.001506
  * `Imports (Out-Degree: 18):` functools, itertools, kivy, kivy.clock, kivy.graphics, kivy.graphics.context_instructions, kivy.graphics.texture, kivy.graphics.transformation...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/lang/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.957)
- **Top Global Matches:** file_cluster_4: 8.957, file_cluster_12: 11.68, file_cluster_6: 12.219
- **Magnitude:** 943.82 | **LOC:** 1024 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **113** in-repo importer(s); it depends on **17**; blast radius 16.923; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.4%)
- **Documentation Coverage:** 54.386% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_apply_rule` **(Many-Argument Workhorses)** (Impact: 119.9)
  * `create_handler` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `update_intermediates` **(Many-Argument Workhorses)** (Impact: 43.5)
    * *Intent:* ''' Function that is called when an intermediate property is updated and `rebind` of that property i...
  * `apply` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `apply_rules` **(Many-Argument Workhorses)** (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 132 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 431
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 132`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 5`, `state_mutation: 167`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 24`, `import: 17`
* *Defense:* `safety: 32`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.923
  * `Choke Point (Betweenness):` 0.009188 | `Ripple Effect (Closeness):` 0.260118
  * `Imports (Out-Degree: 8):` atexit, copy, functools, html, kivy, kivy._event, kivy.cache, kivy.context...
  * `Imported By (In-Degree: 113):` (Excluded from Brief to save tokens)

### `kivy/core/text/text_layout.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.565)
- **Top Global Matches:** file_cluster_8: 7.565, file_cluster_6: 9.358, file_cluster_4: 17.764
- **Magnitude:** 929.44 | **LOC:** 594 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.9%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `layout_text` **(Many-Argument Workhorses)** (Impact: 313.2)
  * `layout_text_unrestricted` **(Many-Argument Workhorses)** (Impact: 196.0)
  * `add_line` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `final_strip` **(Compute Cores)** (Impact: 8.7)
    * *Intent:* ''' Ensures that the line does not end with trailing spaces. Given the line, it'll start from the la...
  * `__cinit__` **(Many-Argument Workhorses)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 124`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 3`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/image/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.887)
- **Top Global Matches:** file_cluster_12: 6.887, file_cluster_4: 7.99, file_cluster_16: 8.552
- **Magnitude:** 929.42 | **LOC:** 1306 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **17**; blast radius 7.002; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.8%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save` **(Many-Argument Workhorses)** (Impact: 42.3)
    * *Intent:* '''Save image texture to file. The filename should have the '.png' extension because the texture dat...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 36.9)
    * *Intent:* # this event should be fired on animation of sequenced img's self.register_event_type('on_texture') ...
  * `_load_single` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `_set_filename` **(Stateful Encapsulated Methods)** (Impact: 24.9)
  * `read_pixel` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* '''For a given local x/y position, return the pixel color at that position. .. warning:: This functi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 148 instances
* *State Mutation (weighted view):* 487
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 169`, `args: 58`, `func_start: 58`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 191`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 49`, `import: 18`
* *Defense:* `safety: 16`, `doc: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.002
  * `Choke Point (Betweenness):` 0.00597 | `Ripple Effect (Closeness):` 0.216998
  * `Imports (Out-Degree: 9):` base64, filetype, io, kivy.atlas, kivy.cache, kivy.clock, kivy.core, kivy.event...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `kivy/lang/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.801)
- **Top Global Matches:** file_cluster_4: 7.801, file_cluster_6: 8.622, file_cluster_12: 13.572
- **Magnitude:** 885.7 | **LOC:** 828 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **19**; blast radius 7.053; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 86.2069% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_level` **(Many-Argument Workhorses)** (Impact: 119.7)
    * *Intent:* '''Parse the current level (level * spaces) indentation. '''
  * `get_names_from_expression` **(Defensive Guards)** (Impact: 41.6)
    * *Intent:* """ Look for all the symbols used in an ast node. """
  * `execute_directives` **(Defensive Guards)** (Impact: 39.6)
  * `precompile` **(Compute Cores)** (Impact: 25.2)
  * `_build_rule` **(Stateful Encapsulated Methods)** (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 133 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 458
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 120`, `args: 34`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 7`, `state_mutation: 192`
* *Architecture:* `io: 3`, `api: 25`, `import: 20`
* *Defense:* `safety: 22`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.053
  * `Choke Point (Betweenness):` 0.013123 | `Ripple Effect (Closeness):` 0.182908
  * `Imports (Out-Degree: 8):` ast, collections, functools, importlib, kivy, kivy.app, kivy.cache, kivy.lang.builder...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `kivy/graphics/texture.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.226)
- **Top Global Matches:** file_cluster_16: 7.226, file_cluster_15: 7.343, file_cluster_4: 7.538
- **Magnitude:** 883.22 | **LOC:** 1401 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.73; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (47.3%)
- **Documentation Coverage:** 41.4141% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blit_buffer` **(Many-Argument Workhorses)** (Impact: 126.8)
  * `_texture_create` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `reload` **(Stateful Encapsulated Methods)** (Impact: 25.2)
  * `texture_create_from_data` **(Compute Cores)** (Impact: 21.0)
    * *Intent:* '''Create a texture from an ImageData class. '''
  * `texture_create` **(Many-Argument Workhorses)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 135`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 166`, `fragile_debt: 2`
* *Architecture:* `api: 35`, `import: 10`
* *Defense:* `safety: 9`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.73
  * `Choke Point (Betweenness):` 0.000234 | `Ripple Effect (Closeness):` 0.001506
  * `Imports (Out-Degree: 6):` kivy.core.image, kivy.graphics, kivy.graphics.fbo, kivy.loader, kivy.utils, kivy.weakmethod, os
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/graphics/opengl.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.995)
- **Top Global Matches:** file_cluster_15: 4.995, file_cluster_11: 6.781, file_cluster_12: 7.341
- **Magnitude:** 876.6 | **LOC:** 1557 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.395; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.1%)
- **Documentation Coverage:** 4.9296% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `glVertexAttribPointer` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* '''See: `glVertexAttribPointer() on Kronos website <http://www.khronos.org/opengles/sdk/docs/man/xht...
  * `glReadPixels` **(Many-Argument Workhorses)** (Impact: 12.2)
  * `glDrawElements` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* '''See: `glDrawElements() on Kronos website <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDr...
  * `glGetFramebufferAttachmentParameteriv` **(Compute Cores)** (Impact: 6.7)
    * *Intent:* '''See: `glGetFramebufferAttachmentParameteriv() on Kronos website <http://www.khronos.org/opengles/...
  * `glGetBufferParameteriv` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* '''See: `glGetBufferParameteriv() on Kronos website <http://www.khronos.org/opengles/sdk/docs/man/xh...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 203`, `args: 143`, `func_start: 143`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 319`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 141`, `import: 1`
* *Defense:* `safety: 8`, `doc: 143`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` kivy.logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/clock.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.355)
- **Top Global Matches:** file_cluster_12: 6.355, file_cluster_16: 7.511, file_cluster_15: 8.323
- **Magnitude:** 865.82 | **LOC:** 1344 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **104** in-repo importer(s); it depends on **16**; blast radius 19.291; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 58.4158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `async_idle` **(Stateful Encapsulated Methods)** (Impact: 19.2)
  * `idle` **(Stateful Encapsulated Methods)** (Impact: 16.0)
  * `_check_ready` **(Stateful Encapsulated Methods)** (Impact: 12.9)
  * `triggered` **(Many-Argument Workhorses)** (Impact: 11.1)
    * *Intent:* """Decorator that schedules the execution of a function after a specified timeout using :meth:`CyClo...
  * `on_schedule` **(Type Conversions)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 149
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 155`, `args: 59`, `func_start: 59`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 188`, `duplicate_logic: 2`
* *Architecture:* `api: 49`, `concurrency: 29`, `import: 19`
* *Defense:* `safety: 3`, `doc: 27`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.291
  * `Choke Point (Betweenness):` 0.019553 | `Ripple Effect (Closeness):` 0.285578
  * `Imports (Out-Degree: 4):` asyncio, ctypes, ctypes.util, functools, kivy._clock, kivy._clock., kivy.base, kivy.config...
  * `Imported By (In-Degree: 104):` (Excluded from Brief to save tokens)

### `kivy/input/providers/hidinput.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.279)
- **Top Global Matches:** file_cluster_6: 8.279, file_cluster_8: 9.267, file_cluster_4: 16.376
- **Magnitude:** 840.52 | **LOC:** 779 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.436; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_thread_run` **(Many-Argument Workhorses)** (Impact: 181.8)
  * `process_as_mouse_or_keyboard` **(Many-Argument Workhorses)** (Impact: 103.5)
  * `process_as_multitouch` **(Many-Argument Workhorses)** (Impact: 41.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 27.0)
  * `process` **(Defensive Guards)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 95 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 62`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 178`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 13`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.436
  * `Choke Point (Betweenness):` 0.000204 | `Ripple Effect (Closeness):` 0.117047
  * `Imports (Out-Degree: 6):` collections, fcntl, kivy.core.window, kivy.input.factory, kivy.input.motionevent, kivy.input.provider, kivy.input.shape, kivy.logger...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/uix/filechooser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.366)
- **Top Global Matches:** file_cluster_12: 5.366, file_cluster_7: 8.572, file_cluster_16: 8.7
- **Magnitude:** 795.88 | **LOC:** 1114 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 0.743; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%), Debt Markers (formerly Tech Debt) (54.8%)
- **Documentation Coverage:** 84.2105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_generate_file_entries` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* # Generator that will create all the files entries. # the generator is used via _update_files() and ...
  * `entry_touched` **(Compute Cores)** (Impact: 29.4)
    * *Intent:* '''(internal) This method must be called by the template when an entry is touched by the user. '''
  * `_apply_filters` **(Stateful Encapsulated Methods)** (Impact: 21.4)
  * `entry_released` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* '''(internal) This method must be called by the template when an entry is touched by the user. .. ve...
  * `_create_files_entries` **(Stateful Encapsulated Methods)** (Impact: 18.0)
    * *Intent:* # create maximum entries during 50ms max, or 10 minimum (slow system) # (on a "fast system" (core i7...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 176`, `args: 71`, `func_start: 67`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 149`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 60`, `import: 21`
* *Defense:* `safety: 19`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.743
  * `Choke Point (Betweenness):` 0.00141 | `Ripple Effect (Closeness):` 0.117047
  * `Imports (Out-Degree: 12):` collections.abc, fnmatch, kivy.app, kivy.clock, kivy.core.text, kivy.factory, kivy.lang, kivy.logger...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/core/window/window_sdl3.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.102)
- **Top Global Matches:** file_cluster_4: 6.102, file_cluster_16: 8.826, file_cluster_12: 9.299
- **Magnitude:** 791.54 | **LOC:** 884 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.395; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Complexity Load (formerly Cognitive Load) (90.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mainloop` **(Stateful Encapsulated Methods)** (Impact: 101.9)
    * *Intent:* # for android/iOS, we don't want to have any event nor executing our # main loop while the pause is ...
  * `create_window` **(Stateful Encapsulated Methods)** (Impact: 42.3)
  * `_update_modifiers` **(Stateful Encapsulated Methods)** (Impact: 35.8)
  * `_event_filter` **(Stateful Encapsulated Methods)** (Impact: 26.2)
  * `do_pause` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* # should go to app pause mode (desktop style) from kivy.app import App from kivy.base import stopTou...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 140`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 181`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 29`
* *Architecture:* `io: 2`, `api: 30`, `import: 21`
* *Defense:* `safety: 11`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` android, collections, kivy, kivy.app, kivy.base, kivy.clock, kivy.config, kivy.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `kivy/tools/pep8checker/pep8kivy.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 79, branch: 23, structural_boundaries: 19, core_var_decl: 16
- `kivy/tests/test_uix_videoplayer.py` (PYTHON) | Magnitude: 76.04 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 42, test: 21, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `examples/canvas/mesh.py` (PYTHON) | Magnitude: 47.94 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 21, state_mutation: 14, core_var_decl: 10
- `kivy/support.py` (PYTHON) | Magnitude: 137.22 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 66, state_mutation: 23, import: 23
- `kivy/tests/test_audio_provider.py` (PYTHON) | Magnitude: 119.66 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 61, test: 25, core_var_decl: 24
- `kivy/input/postproc/dejitter.py` (PYTHON) | Magnitude: 57.18 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 13, state_mutation: 13, branch: 9
- `kivy/core/system_tray/_system_tray_sdl3.pyx` (PYTHON) | Magnitude: 596.6 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 423, structural_boundaries: 150, branch: 127, state_mutation: 71

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `kivy/core/spelling/spelling_enchant.py` (PYTHON) | Magnitude: 34.84 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, args: 5, func_start: 5
- `kivy/modules/joycursor.py` (PYTHON) | Magnitude: 238.52 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 170, state_mutation: 56, structural_boundaries: 32, core_var_decl: 32
- `kivy/tests/test_urlrequest/test_urlrequest_requests.py` (PYTHON) | Magnitude: 195.46 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 306, core_var_decl: 124, design_snake_case: 124, structural_boundaries: 58
- `examples/demo/showcase/main.py` (PYTHON) | Magnitude: 236.3 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 58, state_mutation: 48, branch: 26
- `kivy/core/audio_output/audio_avplayer.py` (PYTHON) | Magnitude: 70.72 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 26, state_mutation: 16, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `kivy/graphics/scissor_instructions.pyx` (PYTHON) | Magnitude: 114.9 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 43, structural_boundaries: 35, encapsulation: 24
- `kivy/core/audio_output/audio_sdl3.pyx` (PYTHON) | Magnitude: 294.28 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 245, structural_boundaries: 65, branch: 56, state_mutation: 56
- `kivy/core/text/text_pango.py` (PYTHON) | Magnitude: 58.82 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 20, state_mutation: 17, core_var_decl: 14
- `kivy/graphics/texture.pyx` (PYTHON) | Magnitude: 883.22 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 679, core_var_decl: 189, state_mutation: 166, design_snake_case: 155
- `kivy/core/clipboard/clipboard_xsel.py` (PYTHON) | Magnitude: 22.82 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 8, state_mutation: 5, ipc_rpc_bridges: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `kivy/uix/behaviors/__init__.py` (PYTHON) | Magnitude: 17.28 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 20, import: 10, indent_spaces: 3, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `kivy/tests/test_coverage.py` (PYTHON) | Magnitude: 32.7 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 23, state_mutation: 20, safety: 18
- `kivy/tests/test_doc_gallery.py` (PYTHON) | Magnitude: 7.86 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 11, safety: 8, doc: 3
- `kivy/graphics/stencil_instructions.pxd` (PYTHON) | Magnitude: 15.8 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 8, func_start: 8, indent_spaces: 7, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `kivy/tools/packaging/factory.py` (PYTHON) | Magnitude: 0.07 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 31, core_var_decl: 17, design_snake_case: 17
- `examples/widgets/effectwidget.py` (PYTHON) | Magnitude: 69.5 | Delta: **0.191** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 24, state_mutation: 13, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `kivy/input/postproc/doubletap.py` (PYTHON) | Magnitude: 105.48 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 24, structural_boundaries: 23, branch: 20

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/manylinux_wheels.yml` -> Churn: **70.79%** | Cog Load: 14.0804% | Debt: 99.9729%
- `.github/workflows/osx_wheels_app.yml` -> Churn: **70.79%** | Cog Load: 10.8754% | Debt: 98.7417%
- `kivy/core/window/window_sdl3.py` -> Churn: **65.42%** | Cog Load: 90.5812% | Debt: 99.4786%
- `kivy/__init__.py` -> Churn: **61.29%** | Cog Load: 64.0472% | Debt: 9.9859%
- `kivy/modules/console.py` -> Churn: **50.86%** | Cog Load: 65.7892% | Debt: 30.5906%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `kivy/uix/scrollview.py` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 2358.28
- `kivy/core/text/markup.py` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 1309.26
- `kivy/core/text/__init__.py` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 1074.24
- `kivy/uix/rst.py` -> **haosenwang1018** (100.0% isolated ownership) | Magnitude: 1030.9
- `kivy/_event.pyx` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 1019.04

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `kivy/base.py` -> **Severity: 4.263** (Bridge: 0.0426 * Flux: 100.0%)
- `kivy/app.py` -> **Severity: 3.662** (Bridge: 0.0366 * Flux: 100.0%)
- `kivy/core/window/__init__.py` -> **Severity: 2.241** (Bridge: 0.0224 * Flux: 100.0%)
- `kivy/uix/settings.py` -> **Severity: 2.126** (Bridge: 0.0213 * Flux: 100.0%)
- `kivy/clock.py` -> **Severity: 1.955** (Bridge: 0.0196 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `kivy/logger.py` -> **Severity: 28.319** (Embedded: 0.3727 * Error Risk: 75.9788%)
- `kivy/__init__.py` -> **Severity: 24.382** (Embedded: 0.3112 * Error Risk: 78.3531%)
- `kivy/clock.py` -> **Severity: 23.921** (Embedded: 0.2856 * Error Risk: 83.7627%)
- `kivy/utils.py` -> **Severity: 22.02** (Embedded: 0.3401 * Error Risk: 64.7534%)
- `kivy/lang/builder.py` -> **Severity: 21.304** (Embedded: 0.2601 * Error Risk: 81.8998%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `kivy/logger.py` -> **Severity: 13223.911** (Blast Radius: 158.687 * Doc Risk: 83.3333%)
- `kivy/utils.py` -> **Severity: 3724.968** (Blast Radius: 96.065 * Doc Risk: 38.7755%)
- `kivy/config.py` -> **Severity: 1411.331** (Blast Radius: 74.599 * Doc Risk: 18.9189%)
- `kivy/clock.py` -> **Severity: 1126.899** (Blast Radius: 19.291 * Doc Risk: 58.4158%)
- `kivy/context.py` -> **Severity: 1043.392** (Blast Radius: 12.331 * Doc Risk: 84.6154%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 501 literal sites + 2 sites through wrappers = 503
- **`memory_alloc`:** 41 literal sites + 1 sites through wrappers = 42
- **`panics_and_aborts`:** 663 literal sites + 33 sites through wrappers = 696

- `raise_egl_error` (function, panics_and_aborts, primitive): 21 call sites in 1 files -- `kivy/lib/vidcore_lite/egl.pyx`
- `_color_fmt_to_gl` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `kivy/graphics/texture.pyx`
- `_buffer_fmt_to_gl` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `kivy/graphics/texture.pyx`
- `_buffer_type_to_gl_size` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `kivy/graphics/texture.pyx`
- `_stencil_op_to_gl` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `kivy/graphics/stencil_instructions.pyx`
- `run_wrapper` (function, debug_prints, primitive): 2 call sites in 1 files -- `examples/async/asyncio_advanced.py`
- `KivyImageIOProviderSupportedExtensionList` (function, memory_alloc, primitive): 1 call sites in 1 files -- `kivy/core/image/img_imageio_implem.mm`
- `_str_to_gl_texture_min_filter` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `kivy/graphics/texture.pyx`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 20873 call pairs -- scoped 34.3%, unique 0.0%, ambiguous 23.6%, external 42.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 20614 | 34.5% | 0.0% | 23.9% | 41.6% |
| objective-c | 140 | 15.7% | 1.4% | 0.0% | 82.9% |
| shell | 76 | 21.1% | 0.0% | 0.0% | 78.9% |
| cpp | 43 | 2.3% | 0.0% | 0.0% | 97.7% |

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
