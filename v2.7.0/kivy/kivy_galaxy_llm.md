# ARCHITECTURAL_BRIEF: kivy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kivy/kivy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1207 |
| Analyzed Artifacts (Scanned) | 655 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 552 |
| Total LOC | 85503 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 54.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4211 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1871 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8977 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 46 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 568 | 81381 | 86.7% |
| XML | 18 | 6 | 2.7% |
| CPP | 18 | 1607 | 2.7% |
| PLAINTEXT | 17 | 0 | 2.6% |
| JSON | 11 | 842 | 1.7% |
| MARKDOWN | 9 | 0 | 1.4% |
| OBJECTIVE-C | 6 | 836 | 0.9% |
| SHELL | 4 | 521 | 0.6% |
| MAKEFILE | 2 | 249 | 0.3% |
| GLSL | 1 | 29 | 0.2% |
| YAML | 1 | 32 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 626 | 95.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 26 | 4.0% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 552*

**Composition by Extension & Reason:**
- `.png`: 252x Excluded (Explicitly Denied Extension: '.png')
- `.kv`: 90x Excluded (Unsupported Extension: '.kv')
- `.rst`: 47x Excluded (Unsupported Extension: '.rst')
- `.jpg`: 44x Excluded (Explicitly Denied Extension: '.jpg')
- `.wav`: 18x Excluded (Explicitly Denied Extension: '.wav')
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 15x Excluded (Explicitly Denied Extension: '.gif')
- `.c`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 7x Excluded (Explicitly Denied Extension: '.zip')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ttf`: 6x Excluded (Explicitly Denied Extension: '.ttf')
- `.spec`: 5x Excluded (Unsupported Extension: '.spec')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 191 LOC), 1x Excluded (Machine-Generated Source Code Signature: 202 LOC)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.1 | 29.2 | 29.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 70.1 | 83.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.1 | 8.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 85.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.8 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 67.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1623 | 229 | 6 | `kivy/core/camera/camera_avfoundation_implem.mm` |
| cleanup | 80 | 40 | 0 | `kivy/core/camera/camera_avfoundation_implem.mm` |
| guards | 4504 | 329 | 21 | `kivy/uix/textinput.py` |
| danger | 2375 | 337 | 10 | `kivy/graphics/cgl_backend/cgl_mock.pyx` |
| concurrency | 489 | 77 | 1 | `kivy/tools/pep8checker/pep8.py` |
| connectivity | 6307 | 518 | 25 | `kivy/graphics/opengl.pyx` |
| io | 710 | 154 | 3 | `kivy/tools/image-testsuite/imagemagick-testsuite.sh` |
| crypto | 2 | 2 | 0 | `kivy/loader.py` |
| ipc | 65 | 17 | 0 | `kivy/tests/pyinstaller/test_pyinstaller.py` |
| time | 20 | 13 | 0 | `kivy/core/camera/camera_avfoundation_implem.mm` |
| serialization | 3 | 3 | 0 | `kivy/gesture.py` |
| regex | 64 | 17 | 0 | `kivy/tools/pep8checker/pep8.py` |
| events | 753 | 72 | 1 | `kivy/_event.pyx` |
| tests | 1357 | 92 | 4 | `kivy/tests/test_properties.py` |
| docs | 3789 | 431 | 18 | `kivy/graphics/opengl.pyx` |
| debt | 967 | 188 | 4 | `setup.py` |
| mutation | 40257 | 527 | 171 | `kivy/uix/textinput.py` |
| dead_code | 2188 | 360 | 7 | `kivy/lib/sdl3.pxi` |
| credential | 96 | 6 | 0 | `examples/gestures/my_gestures.py` |
| threat | 1394 | 153 | 3 | `kivy/include/common_subset.h` |
| ml_ai | 27 | 11 | 0 | `kivy/tools/generate-icons.py` |
| ui | 126 | 32 | 0 | `kivy/tests/test_graphics.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0417**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `kivy/tools/image-testsuite/imagemagick-testsuite.sh` (Hits: 42)
- `kivy/tools/pep8checker/pep8.py` (Hits: 39)
- `setup.py` (Hits: 25)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **app.py** (`kivy/app.py`) — 171 inbound connections
2. **logger.py** (`kivy/logger.py`) — 107 inbound connections
3. **clock.py** (`kivy/clock.py`) — 103 inbound connections
4. **widget.py** (`kivy/uix/widget.py`) — 77 inbound connections
5. **base.py** (`kivy/base.py`) — 59 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **autobuild.py** (`doc/autobuild.py`) — 45 outbound dependencies
2. **__init__.py** (`kivy/core/window/__init__.py`) — 32 outbound dependencies
3. **textinput.py** (`kivy/uix/textinput.py`) — 30 outbound dependencies
4. **common.py** (`kivy/tests/common.py`) — 28 outbound dependencies
5. **console.py** (`kivy/modules/console.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `layout_text` (@ `kivy/core/text/text_layout.pyx`) -> Impact: **313.2** | LOC: 324
- `continued_indentation` (@ `kivy/tools/pep8checker/pep8.py`) -> Impact: **241.8** | LOC: 197
- `shorten_post` (@ `kivy/core/text/markup.py`) -> Impact: **222.1** | LOC: 376
  * *Intent:* ''' Shortens the text to a single line according to the label options. This function operates on a text that has already been laid out because for mar...
- `layout_text_unrestricted` (@ `kivy/core/text/text_layout.pyx`) -> Impact: **196.0** | LOC: 103
- `_thread_run` (@ `kivy/input/providers/hidinput.py`) -> Impact: **181.8** | LOC: 346
- `dispatch_visit` (@ `kivy/uix/rst.py`) -> Impact: **160.6** | LOC: 372
- `layout_hint_with_bounds` (@ `kivy/uix/layout.py`) -> Impact: **157.9** | LOC: 216
- `_pre_render` (@ `kivy/core/text/markup.py`) -> Impact: **148.3** | LOC: 307
  * *Intent:* # split markup, words, and lines # result: list of word with position and width/height # during the first pass, we don't care about h/valign self._cac...
- `upload_uniform` (@ `kivy/graphics/shader.pyx`) -> Impact: **143.8** | LOC: 237
  * *Intent:* '''Pass a uniform variable to the shader. '''
- `log_cgl_funcs` (@ `kivy/graphics/cgl.pyx`) -> Impact: **142.9** | LOC: 259

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `kivy/uix` | 50 | 21188.92 | 37.29% | 20.14% |
| `kivy/graphics` | 47 | 12238.06 | 27.83% | 43.79% |
| `kivy` | 33 | 10911.2 | 37.99% | 9.34% |
| `kivy/tests` | 83 | 10555.6 | 18.27% | 0.0% |
| `kivy/core/text` | 9 | 4575.14 | 57.41% | 33.09% |
| `kivy/core/window` | 8 | 3719.22 | 43.95% | 65.96% |
| `kivy/input/providers` | 13 | 3438.2 | 69.03% | 14.67% |
| `kivy/modules` | 13 | 2529.64 | 37.78% | 10.95% |
| `kivy/uix/behaviors` | 11 | 2069.46 | 37.55% | 5.46% |
| `examples/widgets` | 43 | 1962.57 | 18.7% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `kivy/core/spelling/spelling_osxappkit.py` -> **100.0%** Exposure
- `kivy/core/window/window_info.pxd` -> **100.0%** Exposure
- `kivy/core/window/window_info.pyx` -> **100.0%** Exposure
- `kivy/graphics/context_instructions.pxd` -> **100.0%** Exposure
- `kivy/graphics/egl_backend/egl_angle.pxd` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3238` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `kivy/core/window/window_sdl3.py` (PYTHON) -> Cumulative Risk: **741.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 791.54 | **LOC:** 884 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5322%), Documentation (98.6842%)
- **Heaviest Functions:** `mainloop` (Impact: 101.9), `create_window` (Impact: 42.3), `_update_modifiers` (Impact: 35.8)

### 2. `kivy/input/providers/linuxwacom.py` (PYTHON) -> Cumulative Risk: **721.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 457.56 | **LOC:** 397 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6175%), State Flux (95.0%)
- **Heaviest Functions:** `_thread_run` (Impact: 85.0), `__init__` (Impact: 20.6), `process` (Impact: 14.1)

### 3. `kivy/core/video/video_ffpyplayer.py` (PYTHON) -> Cumulative Risk: **717.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 330.46 | **LOC:** 450 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.2736%)
- **Heaviest Functions:** `_next_frame_run` (Impact: 44.9), `_redraw` (Impact: 25.2), `play` (Impact: 9.9)

### 4. `kivy/clock.py` (PYTHON) -> Cumulative Risk: **714.28**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 865.82 | **LOC:** 1344 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.3086%)
- **Heaviest Functions:** `async_idle` (Impact: 19.2), `idle` (Impact: 16.0), `_check_ready` (Impact: 12.9)

### 5. `kivy/input/providers/mtdev.py` (PYTHON) -> Cumulative Risk: **709.95**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 379.56 | **LOC:** 381 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (98.7354%), State Flux (95.0%)
- **Heaviest Functions:** `_thread_run` (Impact: 69.9), `__init__` (Impact: 22.6), `depack` (Impact: 14.8)

### 6. `doc/sources/sphinxext/preprocess.py` (PYTHON) -> Cumulative Risk: **690.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 179.4 | **LOC:** 126 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.5684%)
- **Heaviest Functions:** `callback_docstring` (Impact: 63.2), `is_cython_extension` (Impact: 22.3), `callback_signature` (Impact: 6.4)

### 7. `kivy/core/audio_output/audio_ffpyplayer.py` (PYTHON) -> Cumulative Risk: **683.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 136.44 | **LOC:** 187 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.5174%)
- **Heaviest Functions:** `_player_callback` (Impact: 8.5), `load` (Impact: 6.5), `_do_eos` (Impact: 5.4)

### 8. `kivy/modules/console.py` (PYTHON) -> Cumulative Risk: **677.28**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 978.5 | **LOC:** 1054 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8487%), Documentation (83.3333%)
- **Heaviest Functions:** `show_property` (Impact: 94.5), `keyboard_shortcut` (Impact: 46.9), `on_widget` (Impact: 17.4)

### 9. `kivy/core/text/_text_pango.pyx` (PYTHON) -> Cumulative Risk: **674.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 755.0 | **LOC:** 982 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.121%)
- **Heaviest Functions:** `_render_layout` (Impact: 78.0), `_set_cc_options` (Impact: 46.8), `_ft2_scan_fontfile_to_fontfamily_cache` (Impact: 30.0)

### 10. `kivy/core/video/video_android.py` (PYTHON) -> Cumulative Risk: **667.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 187.32 | **LOC:** 247 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.7724%)
- **Heaviest Functions:** `load` (Impact: 8.2), `_do_eos` (Impact: 6.2), `play` (Impact: 6.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `kivy/uix/textinput.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3691.72 | **LOC:** 4018 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (44.7364%), Tech Debt (8.996%)
**Top Internal Functions/Classes:**
  * `do_cursor_movement` (Impact: 106.5)
    * *Intent:* '''Move the cursor relative to its current position. Action can be one of : - cursor_left: move the ...
  * `keyboard_on_key_down` (Impact: 64.9)
  * `_draw_line` (Impact: 63.0)
  * `_show_cut_copy_paste` (Impact: 57.7)
  * `insert_text` (Impact: 55.5)
    * *Intent:* '''Insert new text at the current cursor position. Override this function in order to pre-process te...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 574 instances
* *State Mutation (weighted view):* 2003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 362`, `args: 147`, `func_start: 138`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 855`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 70`, `import: 31`
* *Defense:* `safety: 25`, `doc: 93`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.002042 | `Ripple Effect (Closeness):` 0.139597
  * `Imports (Out-Degree: 13):` itertools, kivy.animation, kivy.app, kivy.base, kivy.cache, kivy.clock, kivy.config, kivy.core.clipboard...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `kivy/uix/scrollview.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2358.28 | **LOC:** 3544 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (60.5653%), Tech Debt (8.5792%)
**Top Internal Functions/Classes:**
  * `_scroll_initialize` (Impact: 56.3)
    * *Intent:* # This is the first phase of the scroll gesture, call from on_touch_down # it is used to determine i...
  * `on_touch_down` (Impact: 48.1)
    * *Intent:* # -------------------------------------------------- # - in_bar_x: bool - Touch started on horizonta...
  * `_change_touch_mode` (Impact: 48.1)
    * *Intent:* # SCROLL TIMEOUT HANDLER - GESTURE DETECTION TIMEOUT # =============================================...
  * `on_touch_move` (Impact: 46.5)
    * *Intent:* # SCROLLVIEW TOUCH HANDLING WITH ARBITRARY DEPTH HIERARCHY # =======================================...
  * `_check_nested_delegation` (Impact: 44.8)
    * *Intent:* # Check if this ScrollView should delegate to its parent in hierarchy. # # Uses the hierarchy to fin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 321`, `args: 86`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 438`, `dead_code: 6`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 16`
* *Defense:* `safety: 11`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.976
  * `Choke Point (Betweenness):` 0.004348 | `Ripple Effect (Closeness):` 0.140303
  * `Imports (Out-Degree: 9):` enum, functools, kivy.animation, kivy.app, kivy.clock, kivy.config, kivy.core.window, kivy.effects.dampedscroll...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `kivy/graphics/vertex_instructions_line.pxi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1776.24 | **LOC:** 1785 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2688%), Tech Debt (8.8547%)
**Top Internal Functions/Classes:**
  * `build_extended` (Impact: 92.1)
  * `build_smooth` (Impact: 56.9)
    * *Intent:* # FIXME: Some artifacts can be observed, depending on the line width, # overdraw_width and radius. T...
  * `build_legacy` (Impact: 34.4)
  * `prebuild_rounded_rectangle` (Impact: 32.5)
  * `__init__` (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 347 instances
* *State Mutation (weighted view):* 1249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 93`, `args: 57`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 555`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 9`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` itertools, kivy.cache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/graphics/vertex_instructions.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1757.88 | **LOC:** 2301 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.3718%), Tech Debt (99.7993%)
**Top Internal Functions/Classes:**
  * `add_triangle_strip` (Impact: 31.6)
  * `build` (Impact: 30.0)
  * `build` (Impact: 27.8)
  * `build` (Impact: 24.4)
  * `build` (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 275 instances
* *State Mutation (weighted view):* 1066
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 164`, `args: 119`, `func_start: 119`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 516`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 29`
* *Architecture:* `api: 60`, `import: 3`
* *Defense:* `safety: 12`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` kivy.logger, kivy.utils, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/graphics/svg.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1563.9 | **LOC:** 1279 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.6365%), Tech Debt (17.8429%)
**Top Internal Functions/Classes:**
  * `parse_element` (Impact: 67.7)
  * `parse_path` (Impact: 60.8)
    * *Intent:* # In the SVG specs, initial movetos are absolute, even if # specified as 'm'. This is the default be...
  * `parse_color` (Impact: 39.0)
  * `arc_to` (Impact: 29.1)
  * `__init__` (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 294 instances
* *State Mutation (weighted view):* 1020
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 94`, `args: 51`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 432`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 21`, `import: 11`
* *Defense:* `safety: 10`, `doc: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` array, gzip, kivy.core.window, kivy.graphics.svg, kivy.logger, kivy.properties, kivy.utils, math...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/properties.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1481.54 | **LOC:** 2249 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.0879%), Tech Debt (8.6425%)
**Top Internal Functions/Classes:**
  * `convert` (Impact: 66.3)
  * `__init__` (Impact: 38.4)
  * `set` (Impact: 34.3)
    * *Intent:* # Takes the a python object of the type used by this property # (see :attr:`val_type`), and saves it...
  * `convert` (Impact: 26.1)
  * `_parse_str` (Impact: 24.0)
    * *Intent:* ''' Takes a ConfigParser's string (or any value supplied by the user), and converts it to the python...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 163 instances
* *State Mutation (weighted view):* 588
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 229`, `args: 139`, `func_start: 139`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 262`, `dead_code: 4`, `planned_debt: 2`
* *Architecture:* `api: 38`, `import: 8`
* *Defense:* `safety: 36`, `doc: 37`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` functools, kivy._metrics, kivy.clock, kivy.config, kivy.logger, kivy.utils, kivy.weakmethod, weakref
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/window/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1392.84 | **LOC:** 2600 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.1281%), Tech Debt (34.7796%)
**Top Internal Functions/Classes:**
  * `update_childsize` (Impact: 54.6)
  * `__init__` (Impact: 46.0)
  * `request_keyboard` (Impact: 38.0)
  * `on_keyboard` (Impact: 25.2)
  * `on_motion` (Impact: 21.9)
    * *Intent:* '''Event called when a motion event is received. :Parameters: `etype`: str One of "begin", "update" ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 175 instances
* *State Mutation (weighted view):* 627
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 320`, `args: 144`, `func_start: 138`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 277`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 92`, `import: 36`
* *Defense:* `safety: 5`, `doc: 111`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` android, collections, ios, kivy.animation, kivy.base, kivy.cache, kivy.clock, kivy.config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/text/markup.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1309.26 | **LOC:** 961 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (80.0591%), Tech Debt (9.8918%)
**Top Internal Functions/Classes:**
  * `shorten_post` (Impact: 222.1)
    * *Intent:* ''' Shortens the text to a single line according to the label options. This function operates on a t...
  * `_pre_render` (Impact: 148.3)
    * *Intent:* # split markup, words, and lines # result: list of word with position and width/height # during the ...
  * `render_lines` (Impact: 64.0)
  * `n_restricted` (Impact: 22.1)
    * *Intent:* ''' Similar to the function `n`, except it only returns the first occurrence and it's not an iterato...
  * `p_restricted` (Impact: 21.6)
    * *Intent:* ''' Similar to `n_restricted`, except it returns the first occurrence starting from the right, like ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 740
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 92`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 286`, `dead_code: 9`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 6`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.047
  * `Choke Point (Betweenness):` 0.000873 | `Ripple Effect (Closeness):` 0.16119
  * `Imports (Out-Degree: 2):` copy, functools, kivy.core.text, kivy.core.text.markup, kivy.core.text.text_layout, kivy.logger, kivy.parser, kivy.properties...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `kivy/multistroke.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1214.06 | **LOC:** 1475 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.7438%), Tech Debt (22.866%)
**Top Internal Functions/Classes:**
  * `filter` (Impact: 67.1)
    * *Intent:* ''':meth:`filter` returns a subset of objects in :attr:`self.db`, according to given criteria. This ...
  * `recognize` (Impact: 54.7)
    * *Intent:* '''Search for gestures matching `strokes`. Returns a :class:`ProgressTracker` instance. This method ...
  * `_recognize_tick` (Impact: 23.5)
    * *Intent:* # This callback is scheduled once per frame until completed
  * `match_candidate` (Impact: 21.3)
    * *Intent:* '''Match a given candidate against this MultistrokeGesture object. Will test against all templates a...
  * `_add_result` (Impact: 20.8)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.603
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.004587
  * `Imports (Out-Degree: 3):` base64, collections, io, kivy.clock, kivy.event, kivy.multistroke, kivy.properties, kivy.vector...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1165.12 | **LOC:** 1527 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (46.9512%), Tech Debt (17.4879%)
**Top Internal Functions/Classes:**
  * `determine_gl_flags` (Impact: 30.3)
  * `determine_sdl3` (Impact: 26.6)
  * `build_extensions` (Impact: 18.0)
    * *Intent:* # build files config_h_fn = ('include', 'config.h') config_pxi_fn = ('include', 'config.pxi') config...
  * `get_extensions_from_sources` (Impact: 15.3)
  * `determine_angle_flags` (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 278 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 906
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 122`, `args: 22`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 3`, `state_mutation: 350`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 25`, `api: 22`, `import: 27`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Cython, collections, copy, kivy, kivy.tools.packaging.cython_cfg, kivy.tools.packaging.factory, kivy.tools.packaging.osx.build, kivy.tools.packaging.win32.build...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/window/_window_sdl3.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1108.68 | **LOC:** 1150 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.367%), Tech Debt (8.4329%)
**Top Internal Functions/Classes:**
  * `setup_window` (Impact: 130.6)
  * `poll` (Impact: 93.6)
  * `show_keyboard` (Impact: 46.9)
  * `custom_titlebar_handler_callback` (Impact: 42.1)
  * `set_system_cursor` (Impact: 25.9)
    * *Intent:* # prevent the compiler to not be happy because of # an uninitialized value (return False in Cython i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 473
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 220`, `args: 64`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 183`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 45`, `import: 8`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001529
  * `Imports (Out-Degree: 3):` android, ctypes, kivy, kivy.app, kivy.config, kivy.logger, os
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/core/text/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1074.24 | **LOC:** 1241 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.9066%), Tech Debt (18.1931%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 110.9)
  * `shorten` (Impact: 82.2)
    * *Intent:* ''' Shortens the text to fit into a single line by the width specified by :attr:`text_size` [0]. If ...
  * `render_lines` (Impact: 62.1)
  * `render` (Impact: 44.5)
    * *Intent:* '''Return a tuple (width, height) to create the image with the user constraints. (width, height) inc...
  * `resolve_font_name` (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 179 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 568
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 135`, `args: 43`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 1`, `state_mutation: 210`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 10`, `api: 33`, `import: 16`
* *Defense:* `safety: 5`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ast, copy, functools, kivy, kivy.config, kivy.core, kivy.core.text, kivy.core.text.text_layout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/uix/rst.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1030.9 | **LOC:** 1489 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.0189%), Tech Debt (8.6341%)
**Top Internal Functions/Classes:**
  * `dispatch_visit` (Impact: 160.6)
  * `dispatch_departure` (Impact: 80.0)
  * `brute_refs` (Impact: 26.6)
    * *Intent:* # get foot/cit refs manually because the output from # docutils' parser doesn't contain any of these...
  * `get_refs` (Impact: 26.0)
    * *Intent:* # get foot/cit refs manually because the output from # docutils' parser doesn't contain any of these...
  * `goto` (Impact: 13.3)
    * *Intent:* '''Scroll to the reference. If it's not found, nothing will be done. For this text:: .. _myref: This...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 575
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 150`, `args: 30`, `func_start: 29`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 247`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 54`, `import: 22`
* *Defense:* `safety: 24`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.721
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003058
  * `Imports (Out-Degree: 12):` docutils, docutils.parsers, docutils.parsers.rst, docutils.parsers.rst.roles, functools, kivy.animation, kivy.base, kivy.clock...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/_event.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1019.04 | **LOC:** 1343 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.5296%), Tech Debt (13.0264%)
**Top Internal Functions/Classes:**
  * `_dispatch` (Impact: 117.8)
  * `dispatch` (Impact: 73.5)
  * `__cinit__` (Impact: 33.2)
  * `create_property` (Impact: 32.8)
    * *Intent:* '''Create a new property at runtime. .. versionadded:: 1.0.9 .. versionchanged:: 1.8.0 `value` param...
  * `funbind` (Impact: 30.0)
    * *Intent:* '''Similar to unbind, except we only remove the first match, and we don't deref the observers before...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 353
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 130`, `args: 51`, `func_start: 51`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 135`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 17`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` collections, functools, kivy.app, kivy.uix.boxlayout, kivy.uix.button, kivy.utils, kivy.weakmethod, kivy.weakproxy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/modules/console.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 978.5 | **LOC:** 1054 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (65.7892%), Tech Debt (32.4034%)
**Top Internal Functions/Classes:**
  * `show_property` (Impact: 94.5)
    * *Intent:* # normal call: (tree node, focus, ) # nested call: (widget, prop value, prop key, index in dict/list...
  * `keyboard_shortcut` (Impact: 46.9)
  * `on_widget` (Impact: 17.4)
  * `highlight_at` (Impact: 16.9)
    * *Intent:* """Select a widget from a x/y window coordinate. This is mostly used internally when Select mode is ...
  * `_update_widget_tree_node` (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 178`, `args: 67`, `func_start: 67`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 181`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 75`, `import: 24`
* *Defense:* `safety: 29`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002039
  * `Imports (Out-Degree: 14):` functools, itertools, kivy, kivy.clock, kivy.graphics, kivy.graphics.context_instructions, kivy.graphics.texture, kivy.graphics.transformation...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/lang/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 943.82 | **LOC:** 1024 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.3512%), Tech Debt (10.3521%)
**Top Internal Functions/Classes:**
  * `_apply_rule` (Impact: 119.9)
  * `create_handler` (Impact: 51.6)
  * `update_intermediates` (Impact: 43.5)
    * *Intent:* ''' Function that is called when an intermediate property is updated and `rebind` of that property i...
  * `apply` (Impact: 29.2)
  * `apply_rules` (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 132 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 431
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 132`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 5`, `state_mutation: 167`, `dead_code: 8`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 24`, `import: 17`
* *Defense:* `safety: 32`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.979
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.020237
  * `Imports (Out-Degree: 6):` atexit, copy, functools, html, kivy, kivy._event, kivy.cache, kivy.context...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `kivy/core/text/text_layout.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 929.44 | **LOC:** 594 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9198%), Tech Debt (13.7318%)
**Top Internal Functions/Classes:**
  * `layout_text` (Impact: 313.2)
  * `layout_text_unrestricted` (Impact: 196.0)
  * `add_line` (Impact: 26.9)
  * `final_strip` (Impact: 8.7)
    * *Intent:* ''' Ensures that the line does not end with trailing spaces. Given the line, it'll start from the la...
  * `__cinit__` (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 124`, `dead_code: 10`, `fragile_debt: 1`
* *Architecture:* `api: 3`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` kivy.core.text, kivy.core.text.text_layout
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/image/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 929.42 | **LOC:** 1306 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (48.8293%), Tech Debt (27.0925%)
**Top Internal Functions/Classes:**
  * `save` (Impact: 42.3)
    * *Intent:* '''Save image texture to file. The filename should have the '.png' extension because the texture dat...
  * `__init__` (Impact: 36.9)
    * *Intent:* # this event should be fired on animation of sequenced img's self.register_event_type('on_texture') ...
  * `_load_single` (Impact: 31.5)
  * `_set_filename` (Impact: 24.9)
  * `read_pixel` (Impact: 24.4)
    * *Intent:* '''For a given local x/y position, return the pixel color at that position. .. warning:: This functi...
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 148 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 487
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 169`, `args: 58`, `func_start: 58`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 191`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 49`, `import: 18`
* *Defense:* `safety: 16`, `doc: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` base64, filetype, io, kivy, kivy.atlas, kivy.cache, kivy.clock, kivy.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/lang/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 885.7 | **LOC:** 828 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (75.1707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_level` (Impact: 119.7)
    * *Intent:* '''Parse the current level (level * spaces) indentation. '''
  * `get_names_from_expression` (Impact: 41.6)
    * *Intent:* """ Look for all the symbols used in an ast node. """
  * `execute_directives` (Impact: 39.6)
  * `precompile` (Impact: 25.2)
  * `_build_rule` (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 133 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 458
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 120`, `args: 34`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 7`, `state_mutation: 192`, `dead_code: 5`
* *Architecture:* `io: 3`, `api: 25`, `import: 20`
* *Defense:* `safety: 22`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012287
  * `Imports (Out-Degree: 7):` ast, collections, functools, importlib, kivy, kivy.app, kivy.cache, kivy.lang.builder...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/graphics/texture.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 883.22 | **LOC:** 1401 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.2995%), Tech Debt (11.5684%)
**Top Internal Functions/Classes:**
  * `blit_buffer` (Impact: 126.8)
  * `_texture_create` (Impact: 47.8)
  * `reload` (Impact: 25.2)
  * `texture_create_from_data` (Impact: 21.0)
    * *Intent:* '''Create a texture from an ImageData class. '''
  * `texture_create` (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 135`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 166`, `dead_code: 9`, `fragile_debt: 2`
* *Architecture:* `api: 35`, `import: 10`
* *Defense:* `safety: 9`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` array, kivy.core.image, kivy.core.window, kivy.graphics, kivy.graphics.fbo, kivy.loader, kivy.utils, kivy.weakmethod...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/graphics/opengl.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 876.6 | **LOC:** 1557 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4815%), Tech Debt (9.4449%)
**Top Internal Functions/Classes:**
  * `glVertexAttribPointer` (Impact: 13.9)
    * *Intent:* '''See: `glVertexAttribPointer() on Kronos website <http://www.khronos.org/opengles/sdk/docs/man/xht...
  * `glReadPixels` (Impact: 12.2)
  * `glDrawElements` (Impact: 11.8)
    * *Intent:* '''See: `glDrawElements() on Kronos website <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDr...
  * `glGetFramebufferAttachmentParameteriv` (Impact: 6.7)
    * *Intent:* '''See: `glGetFramebufferAttachmentParameteriv() on Kronos website <http://www.khronos.org/opengles/...
  * `glGetBufferParameteriv` (Impact: 5.8)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.803
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 1):` kivy.logger
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `kivy/clock.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 865.82 | **LOC:** 1344 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.9628%), Tech Debt (19.4085%)
**Top Internal Functions/Classes:**
  * `async_idle` (Impact: 19.2)
  * `idle` (Impact: 16.0)
  * `_check_ready` (Impact: 12.9)
  * `triggered` (Impact: 11.1)
    * *Intent:* """Decorator that schedules the execution of a function after a specified timeout using :meth:`CyClo...
  * `on_schedule` (Impact: 11.0)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.956
  * `Choke Point (Betweenness):` 0.006546 | `Ripple Effect (Closeness):` 0.274362
  * `Imports (Out-Degree: 5):` asyncio, ctypes, ctypes.util, functools, kivy._clock, kivy._clock., kivy.base, kivy.clock...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `kivy/input/providers/hidinput.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 840.52 | **LOC:** 779 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.3692%), Tech Debt (11.0659%)
**Top Internal Functions/Classes:**
  * `_thread_run` (Impact: 181.8)
  * `process_as_mouse_or_keyboard` (Impact: 103.5)
  * `process_as_multitouch` (Impact: 41.3)
  * `__init__` (Impact: 27.0)
  * `process` (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 95 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 62`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 178`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 13`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.415
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001529
  * `Imports (Out-Degree: 5):` collections, fcntl, kivy.core.window, kivy.input.factory, kivy.input.motionevent, kivy.input.provider, kivy.input.shape, kivy.logger...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/uix/filechooser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 795.88 | **LOC:** 1114 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.976%), Tech Debt (58.3106%)
**Top Internal Functions/Classes:**
  * `_generate_file_entries` (Impact: 30.5)
    * *Intent:* # Generator that will create all the files entries. # the generator is used via _update_files() and ...
  * `entry_touched` (Impact: 29.4)
    * *Intent:* '''(internal) This method must be called by the template when an entry is touched by the user. '''
  * `_apply_filters` (Impact: 21.4)
  * `entry_released` (Impact: 20.9)
    * *Intent:* '''(internal) This method must be called by the template when an entry is touched by the user. .. ve...
  * `_create_files_entries` (Impact: 18.0)
    * *Intent:* # create maximum entries during 50ms max, or 10 minimum (slow system) # (on a "fast system" (core i7...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 176`, `args: 71`, `func_start: 67`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 149`, `dead_code: 2`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 60`, `import: 21`
* *Defense:* `safety: 19`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.829
  * `Choke Point (Betweenness):` 0.001248 | `Ripple Effect (Closeness):` 0.137606
  * `Imports (Out-Degree: 7):` collections.abc, fnmatch, kivy.app, kivy.clock, kivy.core.text, kivy.factory, kivy.lang, kivy.logger...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/core/window/window_sdl3.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 791.54 | **LOC:** 884 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (90.5812%), Tech Debt (99.5322%)
**Top Internal Functions/Classes:**
  * `mainloop` (Impact: 101.9)
    * *Intent:* # for android/iOS, we don't want to have any event nor executing our # main loop while the pause is ...
  * `create_window` (Impact: 42.3)
  * `_update_modifiers` (Impact: 35.8)
  * `_event_filter` (Impact: 26.2)
  * `do_pause` (Impact: 15.7)
    * *Intent:* # should go to app pause mode (desktop style) from kivy.app import App from kivy.base import stopTou...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 140`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 181`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 29`
* *Architecture:* `io: 2`, `api: 30`, `import: 21`
* *Defense:* `safety: 11`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` android, collections, kivy, kivy.app, kivy.base, kivy.clock, kivy.config, kivy.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `kivy/core/window/window_sdl3.py` -> Churn: **61.31%** | Cog Load: 90.5812% | Debt: 99.5322%
- `kivy/__init__.py` -> Churn: **57.45%** | Cog Load: 64.0472% | Debt: 11.4235%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `kivy/uix/scrollview.py` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 2358.28
- `kivy/core/window/_window_sdl3.pyx` -> **Kristian Sloth Lauszus** (100.0% isolated ownership) | Magnitude: 1108.68
- `kivy/core/text/__init__.py` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 1074.24
- `kivy/uix/rst.py` -> **haosenwang1018** (100.0% isolated ownership) | Magnitude: 1030.9
- `kivy/_event.pyx` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 1019.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `kivy/app.py` -> **Severity: 2.622** (Bridge: 0.0262 * Flux: 100.0%)
- `kivy/uix/settings.py` -> **Severity: 2.012** (Bridge: 0.0201 * Flux: 100.0%)
- `kivy/uix/widget.py` -> **Severity: 1.108** (Bridge: 0.0111 * Flux: 100.0%)
- `kivy/clock.py` -> **Severity: 0.655** (Bridge: 0.0065 * Flux: 100.0%)
- `kivy/uix/slider.py` -> **Severity: 0.596** (Bridge: 0.006 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `kivy/logger.py` -> **Severity: 33.632** (Embedded: 0.3462 * Error Risk: 97.1454%)
- `kivy/uix/widget.py` -> **Severity: 28.027** (Embedded: 0.2886 * Error Risk: 97.1011%)
- `kivy/clock.py` -> **Severity: 27.247** (Embedded: 0.2744 * Error Risk: 99.3086%)
- `kivy/base.py` -> **Severity: 27.208** (Embedded: 0.281 * Error Risk: 96.8404%)
- `kivy/utils.py` -> **Severity: 26.804** (Embedded: 0.3085 * Error Risk: 86.8802%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `kivy/logger.py` -> **Severity: 17468.493** (Blast Radius: 209.622 * Doc Risk: 83.3333%)
- `kivy/utils.py` -> **Severity: 5831.176** (Blast Radius: 150.383 * Doc Risk: 38.7755%)
- `kivy/config.py` -> **Severity: 1982.966** (Blast Radius: 104.814 * Doc Risk: 18.9189%)
- `kivy/clock.py` -> **Severity: 1516.241** (Blast Radius: 25.956 * Doc Risk: 58.4158%)
- `kivy/uix/label.py` -> **Severity: 1386.164** (Blast Radius: 16.942 * Doc Risk: 81.8182%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
