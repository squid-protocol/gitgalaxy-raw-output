# ARCHITECTURAL_BRIEF: kivy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/kivy` |
| **Timestamp** | `2026-08-07T04:00:28.448678+00:00` |
| **Scan Duration** | `3.2s` |
| **Git Branch** | `master` |
| **Git Commit** | `dc32205ac51ba5452eb904b2fd78cdafffd64ccd` |
| **Git Remote** | `https://github.com/kivy/kivy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 547 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1207 |
| Analyzed Artifacts (Scanned) | 602 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 605 |
| Total LOC | 78157 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 49.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4311 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2003 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9141 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 45 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 528 | 74497 | 87.7% |
| XML | 18 | 6 | 3.0% |
| PLAINTEXT | 16 | 0 | 2.7% |
| OBJECTIVE-C | 12 | 1982 | 2.0% |
| JSON | 11 | 842 | 1.8% |
| MARKDOWN | 9 | 0 | 1.5% |
| SHELL | 4 | 520 | 0.7% |
| MAKEFILE | 2 | 249 | 0.3% |
| GLSL | 1 | 29 | 0.2% |
| YAML | 1 | 32 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.378`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 287 | 47.7% |
| file_cluster_8 | 253 | 42.0% |
| file_cluster_0 | 16 | 2.7% |
| file_cluster_4 | 6 | 1.0% |
| file_cluster_7 | 5 | 0.8% |
| file_cluster_9 | 3 | 0.5% |
| file_cluster_12 | 2 | 0.3% |
| file_cluster_1 | 1 | 0.2% |
| file_cluster_11 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 4.2% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 605*

**Composition by Extension & Reason:**
- `.png`: 252x Excluded (Explicitly Denied Extension: '.png')
- `.kv`: 82x Excluded (Unsupported Extension: '.kv'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 47x Excluded (Unsupported Extension: '.rst')
- `.jpg`: 44x Excluded (Explicitly Denied Extension: '.jpg')
- `.py`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 191 LOC), 1x Excluded (Machine-Generated Source Code Signature: 202 LOC)
- `.wav`: 18x Excluded (Explicitly Denied Extension: '.wav')
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 15x Excluded (Explicitly Denied Extension: '.gif')
- `.h`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 7x Excluded (Explicitly Denied Extension: '.zip')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ttf`: 6x Excluded (Explicitly Denied Extension: '.ttf')
- `.spec`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pyx`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.2 | 9.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 44.1 | 57.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.1 | 0.2 | 0.0 |
| API Exposure | 0.0 | 13.1 | 3.8 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 97.1 | 6.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 20.0 | 11.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `kivy/tools/image-testsuite/imagemagick-testsuite.sh` (Hits: 40)
- `kivy/__init__.py` (Hits: 30)
- `setup.py` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **app.py** (`kivy/app.py`) — 168 inbound connections
2. **logger.py** (`kivy/logger.py`) — 106 inbound connections
3. **clock.py** (`kivy/clock.py`) — 102 inbound connections
4. **widget.py** (`kivy/uix/widget.py`) — 72 inbound connections
5. **base.py** (`kivy/base.py`) — 56 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`kivy/core/window/__init__.py`) — 32 outbound dependencies
2. **textinput.py** (`kivy/uix/textinput.py`) — 30 outbound dependencies
3. **common.py** (`kivy/tests/common.py`) — 28 outbound dependencies
4. **console.py** (`kivy/modules/console.py`) — 25 outbound dependencies
5. **pep8.py** (`kivy/tools/pep8checker/pep8.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `gl_check_error` (@ `kivy/graphics/cgl_backend/cgl_debug.pyx`) -> Impact: **510.5** | LOC: 1272
- `_select_word` (@ `kivy/uix/textinput.py`) -> Impact: **395.8** | LOC: 1162
- `break_around_binary_operator` (@ `kivy/tools/pep8checker/pep8.py`) -> Impact: **253.5** | LOC: 324
- `resolve_font_name` (@ `kivy/core/text/__init__.py`) -> Impact: **252.4** | LOC: 579
- `dispatch_visit` (@ `kivy/uix/rst.py`) -> Impact: **244.7** | LOC: 530
- `is_binary_operator` (@ `kivy/tools/pep8checker/pep8.py`) -> Impact: **234.5** | LOC: 291
  * *Intent:* # trailing space matches opening space need_space = (prev_end, start != prev_end) elif need_space and start == prev_end: # A needed opening space was ...
- `_apply_rule` (@ `kivy/lang/builder.py`) -> Impact: **233.5** | LOC: 331
  * *Intent:* # register all the dynamic classes for name, baseclasses in parser.dynamic_classes.items(): Factory.register(name, baseclasses=baseclasses, filename=f...
- `add_widget` (@ `kivy/uix/widget.py`) -> Impact: **229.4** | LOC: 474
- `shorten_post` (@ `kivy/core/text/markup.py`) -> Impact: **219.9** | LOC: 332
- `_thread_run` (@ `kivy/input/providers/hidinput.py`) -> Impact: **196.9** | LOC: 369
  * *Intent:* # ensure the key exist key, value = arg if key not in HIDInputMotionEventProvider.options: Logger.error('HIDInput: unknown %s option' % key) continue ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `kivy/core/window` | 8 | 25325.8 | 20.73% | 42.73% |
| `kivy/uix` | 38 | 10721.84 | 23.05% | 40.03% |
| `kivy/tests` | 75 | 6736.8 | 7.65% | 0.0% |
| `kivy` | 33 | 6096.88 | 22.97% | 29.14% |
| `kivy/graphics` | 47 | 4800.46 | 18.81% | 27.91% |
| `kivy/core/text` | 7 | 1936.94 | 28.63% | 62.95% |
| `kivy/input/providers` | 13 | 1870.64 | 40.5% | 25.26% |
| `kivy/modules` | 13 | 1726.94 | 17.2% | 32.49% |
| `kivy/uix/behaviors` | 11 | 1377.66 | 19.78% | 23.55% |
| `kivy/lang` | 3 | 1060.6 | 28.23% | 57.18% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `kivy/animation.py` -> **100.0%** Exposure
- `kivy/core/audio_output/audio_sdl3.pyx` -> **100.0%** Exposure
- `kivy/core/spelling/spelling_osxappkit.py` -> **100.0%** Exposure
- `kivy/core/system_tray/__init__.py` -> **100.0%** Exposure
- `kivy/core/text/text_sdl3.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `kivy/core/video/__init__.py` -> **100.0%** Exposure
- `kivy/core/video/video_android.py` -> **100.0%** Exposure
- `kivy/effects/dampedscroll.py` -> **100.0%** Exposure
- `kivy/effects/kinetic.py` -> **100.0%** Exposure
- `kivy/effects/scroll.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `kivy/graphics/context_instructions.pyx` -> **0** Orphaned Functions | **90** Duplicates
- `kivy/tests/test_properties.py` -> **40** Orphaned Functions | **37** Duplicates
- `kivy/tests/test_provider_registry.py` -> **45** Orphaned Functions | **0** Duplicates
- `kivy/graphics/vertex_instructions.pyx` -> **0** Orphaned Functions | **42** Duplicates
- `kivy/tests/test_vector.py` -> **42** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`kivy/graphics/cgl.pyx`** -> AI Confidence: **99.48%**
2. **`kivy/include/gl_redirect.h`** -> AI Confidence: **99.48%**
3. **`kivy/tools/pep8checker/pep8.py`** -> AI Confidence: **99.39%**
4. **`kivy/core/text/markup.py`** -> AI Confidence: **99.34%**
5. **`doc/sources/conf.py`** -> AI Confidence: **99.31%**
6. **`doc/sources/sphinxext/preprocess.py`** -> AI Confidence: **99.31%**
7. **`examples/miscellaneous/shapecollisions.py`** -> AI Confidence: **99.31%**
8. **`kivy/__init__.py`** -> AI Confidence: **99.31%**
9. **`kivy/_event.pyx`** -> AI Confidence: **99.31%**
10. **`kivy/atlas.py`** -> AI Confidence: **99.31%**
11. **`kivy/base.py`** -> AI Confidence: **99.31%**
12. **`kivy/config.py`** -> AI Confidence: **99.31%**
13. **`kivy/core/__init__.py`** -> AI Confidence: **99.31%**
14. **`kivy/core/text/__init__.py`** -> AI Confidence: **99.31%**
15. **`kivy/core/window/_window_sdl3.pyx`** -> AI Confidence: **99.31%**
16. **`kivy/core/window/window_sdl3.py`** -> AI Confidence: **99.31%**
17. **`kivy/graphics/context.pyx`** -> AI Confidence: **99.31%**
18. **`kivy/graphics/svg.pyx`** -> AI Confidence: **99.31%**
19. **`kivy/graphics/texture.pyx`** -> AI Confidence: **99.31%**
20. **`kivy/input/providers/__init__.py`** -> AI Confidence: **99.31%**
21. **`kivy/input/providers/hidinput.py`** -> AI Confidence: **99.31%**
22. **`kivy/input/providers/linuxwacom.py`** -> AI Confidence: **99.31%**
23. **`kivy/input/providers/mouse.py`** -> AI Confidence: **99.31%**
24. **`kivy/input/providers/mtdev.py`** -> AI Confidence: **99.31%**
25. **`kivy/input/providers/probesysfs.py`** -> AI Confidence: **99.31%**
26. **`kivy/lang/builder.py`** -> AI Confidence: **99.31%**
27. **`kivy/lang/parser.py`** -> AI Confidence: **99.31%**
28. **`kivy/modules/__init__.py`** -> AI Confidence: **99.31%**
29. **`kivy/modules/inspector.py`** -> AI Confidence: **99.31%**
30. **`kivy/modules/joycursor.py`** -> AI Confidence: **99.31%**
31. **`kivy/multistroke.py`** -> AI Confidence: **99.31%**
32. **`kivy/network/urlrequest.py`** -> AI Confidence: **99.31%**
33. **`kivy/properties.pyx`** -> AI Confidence: **99.31%**
34. **`kivy/tools/packaging/pyinstaller_hooks/__init__.py`** -> AI Confidence: **99.31%**
35. **`kivy/uix/actionbar.py`** -> AI Confidence: **99.31%**
36. **`kivy/uix/behaviors/compoundselection.py`** -> AI Confidence: **99.31%**
37. **`kivy/uix/carousel.py`** -> AI Confidence: **99.31%**
38. **`kivy/uix/gesturesurface.py`** -> AI Confidence: **99.31%**
39. **`kivy/uix/label.py`** -> AI Confidence: **99.31%**
40. **`kivy/uix/rst.py`** -> AI Confidence: **99.31%**
41. **`kivy/uix/scrollview.py`** -> AI Confidence: **99.31%**
42. **`kivy/uix/tabbedpanel.py`** -> AI Confidence: **99.31%**
43. **`kivy/uix/textinput.py`** -> AI Confidence: **99.31%**
44. **`kivy/uix/vkeyboard.py`** -> AI Confidence: **99.31%**
45. **`kivy/uix/widget.py`** -> AI Confidence: **99.31%**
46. **`setup.py`** -> AI Confidence: **99.31%**
47. **`kivy/_version.py`** -> AI Confidence: **99.29%**
48. **`kivy/core/camera/camera_avfoundation_implem.mm`** -> AI Confidence: **99.29%**
49. **`kivy/core/image/img_imageio_implem.mm`** -> AI Confidence: **99.29%**
50. **`kivy/graphics/egl_backend/egl_angle_metal_implem.mm`** -> AI Confidence: **99.29%**
51. **`kivy/app.py`** -> AI Confidence: **99.24%**
52. **`kivy/core/image/__init__.py`** -> AI Confidence: **99.24%**
53. **`kivy/core/video/video_ffpyplayer.py`** -> AI Confidence: **99.24%**
54. **`kivy/graphics/instructions.pyx`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3073` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `kivy/clock.py` (PYTHON) -> Cumulative Risk: **687.98**
- **Archetype:** `file_cluster_4` (Distance: 12.177 IQR)
- **Magnitude:** 576.02 | **LOC:** 1344 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.912%)
- **Heaviest Functions:** `async_idle` (Impact: 26.2), `idle` (Impact: 19.2), `_check_ready` (Impact: 12.9)

### 2. `kivy/core/camera/camera_avfoundation_implem.mm` (OBJECTIVE-C) -> Cumulative Risk: **644.15**
- **Archetype:** `file_cluster_8` (Distance: 13.789 IQR)
- **Magnitude:** 446.4 | **LOC:** 677 | **CtrlFlow:** 97.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.9943%), Tech Debt (89.9913%)
- **Heaviest Functions:** `updateImage` (Impact: 24.8), `captureOutput` (Impact: 11.6), `init` (Impact: 3.1)

### 3. `kivy/modules/console.py` (PYTHON) -> Cumulative Risk: **640.73**
- **Archetype:** `file_cluster_13` (Distance: 12.313 IQR)
- **Magnitude:** 670.7 | **LOC:** 1054 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9533%), State Flux (99.5727%)
- **Heaviest Functions:** `show_property` (Impact: 94.5), `keyboard_shortcut` (Impact: 46.9), `on_widget` (Impact: 17.4)

### 4. `kivy/core/audio_output/audio_ffpyplayer.py` (PYTHON) -> Cumulative Risk: **634.39**
- **Archetype:** `file_cluster_13` (Distance: 11.976 IQR)
- **Magnitude:** 131.34 | **LOC:** 187 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (85.2582%), Documentation (84.1124%)
- **Heaviest Functions:** `_player_callback` (Impact: 8.5), `load` (Impact: 7.7), `play` (Impact: 5.7)

### 5. `kivy/core/video/video_android.py` (PYTHON) -> Cumulative Risk: **633.84**
- **Archetype:** `file_cluster_13` (Distance: 11.849 IQR)
- **Magnitude:** 147.92 | **LOC:** 247 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (86.4328%), Tech Debt (82.3067%)
- **Heaviest Functions:** `unload` (Impact: 41.8), `load` (Impact: 11.2), `onError` (Impact: 4.7)

### 6. `kivy/base.py` (PYTHON) -> Cumulative Risk: **631.94**
- **Archetype:** `file_cluster_13` (Distance: 12.922 IQR)
- **Magnitude:** 423.4 | **LOC:** 618 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9944%), Tech Debt (95.4282%), Concurrency (86.0223%)
- **Heaviest Functions:** `post_dispatch_input` (Impact: 48.9), `_runTouchApp_prepare` (Impact: 21.2), `async_idle` (Impact: 19.9)

### 7. `kivy/core/window/window_sdl3.py` (PYTHON) -> Cumulative Risk: **631.14**
- **Archetype:** `file_cluster_13` (Distance: 11.897 IQR)
- **Magnitude:** 596.54 | **LOC:** 884 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7021%), Verification (80.0%), Churn (75.11%)
- **Heaviest Functions:** `screenshot` (Impact: 151.6), `create_window` (Impact: 44.0), `_update_modifiers` (Impact: 35.8)

### 8. `kivy/core/video/video_ffpyplayer.py` (PYTHON) -> Cumulative Risk: **621.14**
- **Archetype:** `file_cluster_13` (Distance: 13.329 IQR)
- **Magnitude:** 280.46 | **LOC:** 450 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (98.7484%), Safety Score (83.9154%)
- **Heaviest Functions:** `_next_frame_run` (Impact: 48.4), `_redraw` (Impact: 26.9), `play` (Impact: 11.5)

### 9. `kivy/loader.py` (PYTHON) -> Cumulative Risk: **612.42**
- **Archetype:** `file_cluster_13` (Distance: 12.815 IQR)
- **Magnitude:** 285.66 | **LOC:** 576 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9912%), Verification (80.0%), Safety Score (73.6958%)
- **Heaviest Functions:** `_load_urllib` (Impact: 82.8), `_load` (Impact: 13.6), `_set_max_upload_per_frame` (Impact: 5.4)

### 10. `kivy/core/text/_text_pango.pyx` (PYTHON) -> Cumulative Risk: **592.15**
- **Archetype:** `file_cluster_8` (Distance: 10.361 IQR)
- **Magnitude:** 387.8 | **LOC:** 982 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (95.6225%), State Flux (95.1454%), Documentation (91.6833%)
- **Heaviest Functions:** `render_as_bytes` (Impact: 16.9), `render` (Impact: 13.7), `kpango_font_context_add_font` (Impact: 13.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `kivy/core/window/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.506 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.623 IQR)
- **Top Global Matches:** file_cluster_13: 12.506, file_cluster_8: 12.611, file_cluster_7: 12.723
- **Magnitude:** 24080.32 | **LOC:** 2600 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (21.1633%), Tech Debt (14.7858%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 319`, `args: 144`, `func_start: 138`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 230`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 89`, `import: 36`
* *Defense:* `safety: 5`, `doc: 227`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` android, kivy.cache, os.path, kivy.core.image, kivy.clock, kivy.context, kivy.graphics.transformation, kivy.uix.behaviors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/uix/textinput.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.779 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.507 IQR)
- **Top Global Matches:** file_cluster_8: 12.779, file_cluster_13: 12.886, file_cluster_7: 12.924
- **Magnitude:** 1759.82 | **LOC:** 4018 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.0078%), Tech Debt (30.4251%)
**Top Internal Functions/Classes:**
  * `_select_word` (Impact: 395.8)
  * `do_cursor_movement` (Impact: 105.3)
    * *Intent:* # handle undo and redo self._set_unredo_bkspc( cursor_index, cursor_index - 1, substring, from_undo,...
  * `insert_text` (Impact: 55.4)
  * `_move_cursor_word_right` (Impact: 34.8)
  * `_move_cursor_word_left` (Impact: 33.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 600`, `structural_boundaries: 358`, `args: 147`, `func_start: 138`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 599`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `io: 1`, `api: 69`, `import: 31`
* *Defense:* `safety: 26`, `doc: 186`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.336
  * `Choke Point (Betweenness):` 0.001807 | `Ripple Effect (Closeness):` 0.144915
  * `Imports (Out-Degree: 12):` kivy.cache, kivy.clock, kivy.core.text, kivy.uix.behaviors, kivy.graphics.texture, kivy.uix.image, kivy.graphics.context, kivy.graphics...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `kivy/uix/scrollview.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.553 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.152 IQR)
- **Top Global Matches:** file_cluster_8: 11.553, file_cluster_13: 11.832, file_cluster_7: 11.846
- **Magnitude:** 1500.98 | **LOC:** 3544 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.001%), Tech Debt (14.2194%)
**Top Internal Functions/Classes:**
  * `_scroll_initialize` (Impact: 56.3)
    * *Intent:* # Need minimum movement to determine direction
  * `on_touch_down` (Impact: 48.1)
  * `_change_touch_mode` (Impact: 48.1)
  * `on_touch_move` (Impact: 46.5)
  * `_check_nested_delegation` (Impact: 44.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 319`, `args: 86`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 246`, `dead_code: 6`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 41`, `import: 16`
* *Defense:* `safety: 12`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.199
  * `Choke Point (Betweenness):` 0.003773 | `Ripple Effect (Closeness):` 0.145721
  * `Imports (Out-Degree: 8):` kivy.uix.button, kivy.uix.stencilview, kivy.factory, math, kivy.uix.scrollview, kivy.clock, kivy.graphics, kivy.effects.dampedscroll...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `kivy/core/text/markup.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.267 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.797 IQR)
- **Top Global Matches:** file_cluster_13: 12.267, file_cluster_17: 12.301, file_cluster_8: 12.339
- **Magnitude:** 749.86 | **LOC:** 961 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (52.8992%), Tech Debt (27.4116%)
**Top Internal Functions/Classes:**
  * `shorten_post` (Impact: 219.9)
  * `_pre_render` (Impact: 179.9)
  * `render_lines` (Impact: 64.0)
    * *Intent:* # now keep adding spaces to already split words until done
  * `n_restricted` (Impact: 21.6)
  * `p_restricted` (Impact: 21.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 92`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 148`, `dead_code: 9`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 6`, `doc: 26`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.539
  * `Choke Point (Betweenness):` 0.0009 | `Ripple Effect (Closeness):` 0.166687
  * `Imports (Out-Degree: 2):` kivy.core.text.markup, kivy.parser, kivy.core.text.text_layout, kivy.core.text, re, functools, kivy.properties, kivy.logger...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/graphics/vertex_instructions.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.999 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.426 IQR)
- **Top Global Matches:** file_cluster_0: 11.999, file_cluster_8: 12.036, file_cluster_7: 12.18
- **Magnitude:** 738.88 | **LOC:** 2301 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.2078%), Tech Debt (99.9951%)
**Top Internal Functions/Classes:**
  * `points` (Impact: 182.5)
  * `__init__` (Impact: 16.4)
  * `__init__` (Impact: 14.4)
  * `points` (Impact: 10.9)
  * `add_point` (Impact: 8.2)
    * *Intent:* # if user updated the list, but didn't do self.indices = ... then # we'd not know about it, so ensur...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 164`, `args: 73`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 320`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 42`
* *Architecture:* `api: 58`, `import: 3`
* *Defense:* `safety: 13`, `doc: 104`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` kivy.logger, os, kivy.utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/modules/console.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.313 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.877 IQR)
- **Top Global Matches:** file_cluster_13: 12.313, file_cluster_8: 12.549, file_cluster_0: 12.625
- **Magnitude:** 670.7 | **LOC:** 1054 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (35.131%), Tech Debt (99.9533%)
**Top Internal Functions/Classes:**
  * `show_property` (Impact: 94.5)
  * `keyboard_shortcut` (Impact: 46.9)
  * `on_widget` (Impact: 17.4)
  * `highlight_at` (Impact: 16.9)
  * `_update_widget_tree_node` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 177`, `args: 67`, `func_start: 67`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 115`, `dead_code: 1`, `duplicate_logic: 24`
* *Architecture:* `api: 80`, `import: 24`
* *Defense:* `safety: 35`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` kivy, kivy.uix.relativelayout, kivy.graphics.transformation, kivy.clock, kivy.uix.label, kivy.graphics.texture, kivy.uix.gridlayout, kivy.uix.image...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/multistroke.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.394 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.717 IQR)
- **Top Global Matches:** file_cluster_8: 11.394, file_cluster_13: 11.473, file_cluster_7: 11.601
- **Magnitude:** 665.66 | **LOC:** 1475 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.5852%), Tech Debt (99.9291%)
**Top Internal Functions/Classes:**
  * `filter` (Impact: 63.0)
  * `recognize` (Impact: 51.6)
    * *Intent:* # Min priority 50, max 100 gdb.filter(priority=[50, 100]) When this option is used, :attr:`Recognize...
  * `_recognize_tick` (Impact: 28.3)
  * `_add_result` (Impact: 20.8)
  * `match_candidate` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 154`, `args: 58`, `func_start: 56`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 94`, `fragile_debt: 5`, `duplicate_logic: 13`
* *Architecture:* `io: 2`, `api: 58`, `import: 12`
* *Defense:* `safety: 11`, `doc: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.686
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004992
  * `Imports (Out-Degree: 3):` base64, kivy.multistroke, pickle, io, kivy.vector, math, kivy.clock, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/uix/rst.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.258 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.51 IQR)
- **Top Global Matches:** file_cluster_13: 12.258, file_cluster_8: 12.452, file_cluster_0: 12.658
- **Magnitude:** 629.3 | **LOC:** 1489 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.6441%), Tech Debt (92.1636%)
**Top Internal Functions/Classes:**
  * `dispatch_visit` (Impact: 244.7)
  * `brute_refs` (Impact: 26.6)
  * `get_refs` (Impact: 26.0)
  * `goto` (Impact: 11.9)
  * `dispatch_visit` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 149`, `args: 30`, `func_start: 29`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 174`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 4`, `api: 57`, `import: 22`
* *Defense:* `safety: 25`, `doc: 40`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003328
  * `Imports (Out-Degree: 10):` os.path, kivy.clock, kivy.uix.label, kivy.uix.gridlayout, kivy.uix.image, docutils.parsers.rst, kivy.uix.anchorlayout, kivy.uix.scrollview...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/include/common_subset.h` (OBJECTIVE-C | Tier 4 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.737 IQR)
- **Top Global Matches:** file_cluster_8: 8.737, file_cluster_7: 9.684, file_cluster_1: 9.824
- **Magnitude:** 611.35 | **LOC:** 498 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2612%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 17`, `args: 142`, `func_start: 142`
* *Risk/State:* `safety_bypasses: 10`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001664
  * `Imports (Out-Degree: 1):` gl2platform.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/core/window/window_sdl3.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.897 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.498 IQR)
- **Top Global Matches:** file_cluster_13: 11.897, file_cluster_8: 11.995, file_cluster_0: 12.237
- **Magnitude:** 596.54 | **LOC:** 884 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (63.1884%), Tech Debt (72.9769%)
**Top Internal Functions/Classes:**
  * `screenshot` (Impact: 151.6)
  * `create_window` (Impact: 44.0)
  * `_update_modifiers` (Impact: 35.8)
  * `_event_filter` (Impact: 26.2)
  * `_do_resize` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 140`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 139`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 30`, `import: 21`
* *Defense:* `safety: 13`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` android, kivy.core.window._window_sdl3, kivy.input.provider, os.path, kivy, kivy.clock, kivy.resources, kivy.utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/lang/builder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.858 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.323 IQR)
- **Top Global Matches:** file_cluster_13: 12.858, file_cluster_17: 13.035, file_cluster_0: 13.089
- **Magnitude:** 585.62 | **LOC:** 1024 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.1531%), Tech Debt (10.3521%)
**Top Internal Functions/Classes:**
  * `_apply_rule` (Impact: 233.5)
    * *Intent:* # register all the dynamic classes for name, baseclasses in parser.dynamic_classes.items(): Factory....
  * `load_file` (Impact: 56.0)
  * `create_handler` (Impact: 54.5)
    * *Intent:* # bind all attrs, except last to update_intermediates for val in keys[s:-1]: # if we need to dynamic...
  * `update_intermediates` (Impact: 44.8)
  * `apply_rules` (Impact: 42.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 125`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 79`, `dead_code: 8`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 25`, `import: 17`
* *Defense:* `safety: 46`, `doc: 41`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.13
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.021742
  * `Imports (Out-Degree: 6):` kivy.cache, os.path, kivy.lang.parser, kivy, os, copy, kivy.utils, kivy.context...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `kivy/core/image/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.252 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.951 IQR)
- **Top Global Matches:** file_cluster_0: 13.252, file_cluster_13: 13.27, file_cluster_11: 13.522
- **Magnitude:** 580.4 | **LOC:** 1306 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (48.8188%), Tech Debt (41.1651%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 182.2)
    * *Intent:* ''' if self._textures is None: self.populate() return self._textures @property def nocache(self): ''...
  * `populate` (Impact: 86.7)
  * `__init__` (Impact: 6.6)
    * *Intent:* ------------------
  * `iterate_mipmaps` (Impact: 5.6)
  * `__init__` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 166`, `args: 58`, `func_start: 58`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 200`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 52`, `import: 18`
* *Defense:* `safety: 20`, `doc: 98`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` kivy.cache, kivy, kivy.core.image, kivy.clock, kivy.graphics.texture, kivy.uix.image, kivy.graphics, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/clock.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.177 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.026 IQR)
- **Top Global Matches:** file_cluster_4: 12.177, file_cluster_13: 12.308, file_cluster_8: 12.423
- **Magnitude:** 576.02 | **LOC:** 1344 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.5424%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `async_idle` (Impact: 26.2)
  * `idle` (Impact: 19.2)
    * *Intent:* # on mobile platforms, just use time.sleep def _usleep(microseconds, obj=None): time.sleep(microseco...
  * `_check_ready` (Impact: 12.9)
  * `_libc_clock_gettime_wrapper` (Impact: 12.2)
    * *Intent:* # Because no reference is kept to the instance returned from Foo(), # the object will be collected b...
  * `async_idle` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 154`, `args: 59`, `func_start: 59`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 119`, `duplicate_logic: 33`
* *Architecture:* `api: 60`, `concurrency: 119`, `import: 20`
* *Defense:* `safety: 4`, `doc: 72`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.121
  * `Choke Point (Betweenness):` 0.00339 | `Ripple Effect (Closeness):` 0.280337
  * `Imports (Out-Degree: 5):` kivy._clock, kivy._clock., ctypes, asyncio, time, kivy.clock, os, kivy.context...
  * `Imported By (In-Degree: 102):` (Excluded from Brief to save tokens)

### `kivy/graphics/vertex_instructions_line.pxi` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.573 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.62 IQR)
- **Top Global Matches:** file_cluster_8: 11.573, file_cluster_7: 11.955, file_cluster_1: 12.206
- **Magnitude:** 564.64 | **LOC:** 1785 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.9553%), Tech Debt (99.9958%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 29.4)
  * `__set__` (Impact: 11.0)
  * `__set__` (Impact: 9.2)
  * `__set__` (Impact: 7.4)
  * `__set__` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 93`, `args: 41`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 363`, `fragile_debt: 1`, `duplicate_logic: 39`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 11`, `doc: 42`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` kivy.cache, itertools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/graphics/opengl.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.931 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.269 IQR)
- **Top Global Matches:** file_cluster_8: 9.931, file_cluster_7: 10.123, file_cluster_1: 10.407
- **Magnitude:** 557.2 | **LOC:** 1557 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0534%), Tech Debt (9.4449%)
**Top Internal Functions/Classes:**
  * `glReadPixels` (Impact: 17.3)
  * `glVertexAttribPointer` (Impact: 13.8)
    * *Intent:* ''' cgl.glTexParameteri(target, pname, param) def glTexParameteriv(GLenum target, GLenum pname):#, G...
  * `glDrawElements` (Impact: 11.7)
    * *Intent:* '''See: `glDeleteShader() on Kronos website <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDe...
  * `glGetBooleanv` (Impact: 6.5)
  * `glGetFloatv` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 203`, `args: 141`, `func_start: 141`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 162`, `import: 1`
* *Defense:* `safety: 8`, `doc: 286`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.86
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.009983
  * `Imports (Out-Degree: 1):` kivy.logger
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `kivy/core/text/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.342 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.698 IQR)
- **Top Global Matches:** file_cluster_0: 12.342, file_cluster_13: 12.359, file_cluster_11: 12.588
- **Magnitude:** 550.66 | **LOC:** 1241 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (38.3768%), Tech Debt (18.1685%)
**Top Internal Functions/Classes:**
  * `resolve_font_name` (Impact: 252.4)
  * `__init__` (Impact: 122.8)
  * `register` (Impact: 18.2)
  * `get_provider_class` (Impact: 7.8)
  * `_migrate_deprecated_padding_xy` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 133`, `args: 43`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 88`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 14`, `api: 36`, `import: 16`
* *Defense:* `safety: 6`, `doc: 56`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` sys, kivy, kivy.core.text.text_layout, os, kivy.utils, kivy.resources, kivy.core.text, kivy.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/input/providers/hidinput.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.531 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.63 IQR)
- **Top Global Matches:** file_cluster_8: 10.531, file_cluster_13: 10.853, file_cluster_7: 11.051
- **Magnitude:** 544.6 | **LOC:** 779 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.1928%), Tech Debt (11.0727%)
**Top Internal Functions/Classes:**
  * `_thread_run` (Impact: 196.9)
    * *Intent:* # ensure the key exist key, value = arg if key not in HIDInputMotionEventProvider.options: Logger.er...
  * `process_as_mouse_or_keyboard` (Impact: 103.5)
  * `process_as_multitouch` (Impact: 41.3)
  * `process` (Impact: 27.8)
  * `assign_rel_coord` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 62`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 95`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 13`, `concurrency: 7`, `import: 12`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001664
  * `Imports (Out-Degree: 5):` kivy.input.factory, kivy.input.provider, os, threading, kivy.input.motionevent, kivy.input.shape, struct, fcntl...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/graphics/cgl_backend/cgl_debug.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.159 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.257 IQR)
- **Top Global Matches:** file_cluster_8: 9.159, file_cluster_7: 9.827, file_cluster_1: 10.081
- **Magnitude:** 544.16 | **LOC:** 1425 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gl_check_error` (Impact: 510.5)
  * `init_backend_debug` (Impact: 4.2)
  * `gl_debug_print` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 82`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `dead_code: 11`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001664
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `kivy/graphics/context_instructions.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.716 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.202 IQR)
- **Top Global Matches:** file_cluster_0: 12.716, file_cluster_13: 13.027, file_cluster_8: 13.08
- **Magnitude:** 517.8 | **LOC:** 948 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.2105%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 23.2)
  * `__init__` (Impact: 19.3)
  * `__init__` (Impact: 13.2)
  * `__init__` (Impact: 11.0)
  * `source` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 178`, `args: 99`, `func_start: 92`
* *Risk/State:* `state_mutation: 183`, `fragile_debt: 1`, `duplicate_logic: 90`
* *Architecture:* `io: 1`, `api: 53`, `import: 6`
* *Defense:* `safety: 4`, `doc: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` kivy.cache, os.path, kivy, kivy.core.image, kivy.resources, kivy.logger, kivy.graphics
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/animation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.945 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.657 IQR)
- **Top Global Matches:** file_cluster_0: 11.945, file_cluster_12: 12.17, file_cluster_13: 12.216
- **Magnitude:** 502.4 | **LOC:** 831 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.369%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_calculate` (Impact: 25.6)
  * `cancel_all` (Impact: 23.7)
  * `_update` (Impact: 21.0)
  * `stop_all` (Impact: 10.9)
  * `_out_bounce_internal` (Impact: 9.3)
    * *Intent:* ''' return progress * progress * progress * progress * progress @staticmethod def out_quint(progress...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 167`, `args: 76`, `func_start: 76`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 73`, `planned_debt: 1`, `duplicate_logic: 24`
* *Architecture:* `api: 102`, `import: 5`
* *Defense:* `safety: 10`, `doc: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.123
  * `Choke Point (Betweenness):` 9.8e-05 | `Ripple Effect (Closeness):` 0.154526
  * `Imports (Out-Degree: 3):` kivy.weakproxy, math, kivy.clock, kivy.event, collections
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `kivy/modules/inspector.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.982 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.452 IQR)
- **Top Global Matches:** file_cluster_8: 11.982, file_cluster_13: 12.0, file_cluster_0: 12.304
- **Magnitude:** 493.22 | **LOC:** 756 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.8452%), Tech Debt (35.0851%)
**Top Internal Functions/Classes:**
  * `show_property` (Impact: 94.4)
  * `show_widget_info` (Impact: 22.7)
  * `on_activated` (Impact: 19.3)
  * `keyboard_shortcut` (Impact: 18.6)
  * `highlight_at` (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 98`, `args: 33`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 70`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `safety: 39`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` kivy.uix.button, kivy.lang, kivy.factory, kivy.weakproxy, kivy.properties, kivy.graphics.transformation, kivy.clock, kivy.animation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/uix/filechooser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.053 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.563 IQR)
- **Top Global Matches:** file_cluster_13: 12.053, file_cluster_8: 12.374, file_cluster_7: 12.409
- **Magnitude:** 492.18 | **LOC:** 1114 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.7043%), Tech Debt (99.7544%)
**Top Internal Functions/Classes:**
  * `is_hidden` (Impact: 121.0)
  * `_generate_file_entries` (Impact: 32.5)
  * `_create_files_entries` (Impact: 19.7)
  * `_add_files` (Impact: 18.0)
  * `update_view` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 175`, `args: 71`, `func_start: 67`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 82`, `dead_code: 2`, `fragile_debt: 3`, `duplicate_logic: 10`
* *Architecture:* `io: 4`, `api: 63`, `import: 21`
* *Defense:* `safety: 19`, `doc: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.946
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.142842
  * `Imports (Out-Degree: 5):` fnmatch, os.path, kivy.uix.relativelayout, kivy.clock, kivy.core.text, win32file, pprint, kivy.factory...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/uix/carousel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.057 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.715 IQR)
- **Top Global Matches:** file_cluster_13: 12.057, file_cluster_8: 12.089, file_cluster_7: 12.226
- **Magnitude:** 490.68 | **LOC:** 696 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.5969%), Tech Debt (11.7439%)
**Top Internal Functions/Classes:**
  * `_position_visible_slides` (Impact: 72.2)
  * `on__offset` (Impact: 43.2)
  * `_insert_visible_slides` (Impact: 41.7)
  * `on_touch_move` (Impact: 38.4)
  * `_start_animation` (Impact: 32.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 82`, `args: 32`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `state_mutation: 88`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `import: 8`
* *Defense:* `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003328
  * `Imports (Out-Degree: 5):` kivy.uix.stencilview, kivy.uix.relativelayout, kivy.clock, kivy.animation, functools, kivy.uix.carousel, kivy.uix.image, kivy.properties...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/lang/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.03 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.812 IQR)
- **Top Global Matches:** file_cluster_13: 12.03, file_cluster_17: 12.378, file_cluster_0: 12.379
- **Magnitude:** 461.38 | **LOC:** 828 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.5286%), Tech Debt (61.1985%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 166.8)
  * `get_names_from_expression` (Impact: 41.6)
    * *Intent:* """ Look for all the symbols used in an ast node. """
  * `_build_rule` (Impact: 37.9)
  * `precompile` (Impact: 12.8)
  * `__repr__` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 120`, `args: 34`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 6`, `state_mutation: 105`, `dead_code: 5`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 24`, `import: 22`
* *Defense:* `safety: 26`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.403
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.013045
  * `Imports (Out-Degree: 7):` kivy.cache, kivy, importlib, types, traceback, collections, syntax, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/tests/test_properties.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.9 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.924 IQR)
- **Top Global Matches:** file_cluster_13: 10.9, file_cluster_8: 10.987, file_cluster_0: 11.062
- **Magnitude:** 451.28 | **LOC:** 1340 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.8893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_reference` (Impact: 14.7)
  * `test_reference_child_update` (Impact: 13.6)
  * `test_color_property` (Impact: 11.2)
  * `test_bounded_numeric_property_error_hand` (Impact: 10.1)
  * `test_stringcheck` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 336`, `args: 84`, `func_start: 83`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 39`, `dead_code: 1`, `duplicate_logic: 37`, `orphaned_logic: 40`
* *Architecture:* `api: 92`, `import: 53`
* *Defense:* `safety: 85`, `doc: 4`, `test: 154`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` kivy.lang, kivy.clock, kivy.uix.label, functools, kivy.event, kivy.uix.togglebutton, unittest, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `kivy/graphics/fbo.pyx` (PYTHON) | Magnitude: 121.96 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 243, encapsulation: 83, state_mutation: 80, branch: 58
- `kivy/core/text/__init__.py` (PYTHON) | Magnitude: 550.66 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 568, branch: 165, structural_boundaries: 133, encapsulation: 99
- `kivy/core/image/__init__.py` (PYTHON) | Magnitude: 580.4 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 558, state_mutation: 200, encapsulation: 188, structural_boundaries: 166
- `kivy/graphics/vertex_instructions.pyx` (PYTHON) | Magnitude: 738.88 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1272, state_mutation: 320, encapsulation: 295, branch: 201
- `kivy/graphics/boxshadow.pyx` (PYTHON) | Magnitude: 100.74 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 223, encapsulation: 141, structural_boundaries: 48, state_mutation: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `kivy/event.py` (PYTHON) | Magnitude: 14.12 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 8, events: 3, structural_boundaries: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `kivy/tools/image-testsuite/imagemagick-testsuite.sh` (SHELL) | Magnitude: 0.22 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 93, branch: 79, safety_bypasses: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `kivy/input/factory.py` (PYTHON) | Magnitude: 14.76 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 11, doc: 10, api: 7, structural_boundaries: 6
- `tools/build_macos_dependencies.sh` (SHELL) | Magnitude: 0.06 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 34, reflection_metaprogramming: 27, safety_bypasses: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/async/asyncio_basic.py` (PYTHON) | Magnitude: 28.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, concurrency: 12, doc: 10
- `examples/tutorials/pong/main.py` (PYTHON) | Magnitude: 48.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 22, branch: 11, api: 10
- `kivy/tests/visual_test_label.py` (PYTHON) | Magnitude: 30.38 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 24, branch: 10, import: 9
- `examples/svg/benchmark.py` (PYTHON) | Magnitude: 15.36 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, import: 7, globals: 4
- `kivy/tests/test_clock.py` (PYTHON) | Magnitude: 125.3 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 99, test: 73, safety: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `kivy/tests/async_common.py` (PYTHON) | Magnitude: 351.08 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 363, structural_boundaries: 97, branch: 76, api: 36
- `kivy/clock.py` (PYTHON) | Magnitude: 576.02 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 482, encapsulation: 252, structural_boundaries: 154, state_mutation: 119
- `kivy/tests/test_uix_dropdown.py` (PYTHON) | Magnitude: 50.2 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 42, test: 11, safety: 10
- `examples/async/asyncio_advanced.py` (PYTHON) | Magnitude: 45.42 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, concurrency: 17, structural_boundaries: 15, doc: 8
- `examples/async/trio_advanced.py` (PYTHON) | Magnitude: 48.72 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, concurrency: 16, structural_boundaries: 15, doc: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `kivy/input/shape.py` (PYTHON) | Magnitude: 7.28 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 4, encapsulation: 4
- `kivy/eventmanager/__init__.py` (PYTHON) | Magnitude: 28.68 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, indent_spaces: 5, structural_boundaries: 4, api: 4
- `kivy/tools/pep8checker/pep8.py` (PYTHON) | Magnitude: 0.74 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 671, branch: 442, doc: 182, structural_boundaries: 139
- `kivy/uix/treeview.py` (PYTHON) | Magnitude: 209.34 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 218, doc: 71, branch: 59, structural_boundaries: 59
- `kivy/input/provider.py` (PYTHON) | Magnitude: 25.14 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 10, structural_boundaries: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `kivy/core/gl/__init__.py` (PYTHON) | Magnitude: 28.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 22, import: 11, branch: 10
- `kivy/uix/button.py` (PYTHON) | Magnitude: 17.3 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, indent_spaces: 10, structural_boundaries: 7, import: 3
- `kivy/uix/recycleview/datamodel.py` (PYTHON) | Magnitude: 111.04 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, branch: 34, structural_boundaries: 27, encapsulation: 19
- `kivy/effects/dampedscroll.py` (PYTHON) | Magnitude: 125.48 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 46, branch: 27, structural_boundaries: 20
- `kivy/graphics/context.pyx` (PYTHON) | Magnitude: 183.26 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 220, state_mutation: 67, branch: 56, structural_boundaries: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `kivy/_version.py` (PYTHON) | Magnitude: 14.68 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 4, branch: 1, dead_code: 1, indent_spaces: 1
- `kivy/core/window/window_attrs.pxi` (PYTHON) | Magnitude: 15.42 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 19, dead_code: 7, encapsulation: 4, structural_boundaries: 3
- `doc/sources/sphinxext/kivy_pygments_theme.py` (PYTHON) | Magnitude: 17.36 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 65, dead_code: 61, structural_boundaries: 5, import: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `kivy/core/window/window_sdl3.py` -> Churn: **75.11%** | Cog Load: 63.1884% | Debt: 72.9769%
- `kivy/clock.py` -> Churn: **59.53%** | Cog Load: 49.5424% | Debt: 99.9999%
- `kivy/graphics/boxshadow.pyx` -> Churn: **59.53%** | Cog Load: 21.1515% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `kivy/uix/scrollview.py` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 1500.98
- `kivy/uix/rst.py` -> **haosenwang1018** (100.0% isolated ownership) | Magnitude: 629.3
- `kivy/lang/builder.py` -> **clayote** (100.0% isolated ownership) | Magnitude: 585.62
- `kivy/input/providers/hidinput.py` -> **haosenwang1018** (100.0% isolated ownership) | Magnitude: 544.6
- `kivy/tests/test_properties.py` -> **Dexer** (100.0% isolated ownership) | Magnitude: 451.28

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `kivy/app.py` -> **Severity: 2.343** (Bridge: 0.0235 * Flux: 99.6052%)
- `kivy/uix/settings.py` -> **Severity: 1.515** (Bridge: 0.0168 * Flux: 90.424%)
- `kivy/uix/widget.py` -> **Severity: 0.866** (Bridge: 0.0089 * Flux: 96.9162%)
- `kivy/uix/label.py` -> **Severity: 0.407** (Bridge: 0.0041 * Flux: 99.0396%)
- `kivy/uix/image.py` -> **Severity: 0.38** (Bridge: 0.0038 * Flux: 99.9985%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `kivy/base.py` -> **Severity: 23.247** (Embedded: 0.2904 * Error Risk: 80.0412%)
- `kivy/clock.py` -> **Severity: 20.799** (Embedded: 0.2803 * Error Risk: 74.1934%)
- `kivy/logger.py` -> **Severity: 20.401** (Embedded: 0.363 * Error Risk: 56.1953%)
- `kivy/app.py` -> **Severity: 18.71** (Embedded: 0.2716 * Error Risk: 68.8814%)
- `kivy/uix/image.py` -> **Severity: 18.049** (Embedded: 0.2238 * Error Risk: 80.6505%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `kivy/utils.py` -> **Severity: 7216.342** (Blast Radius: 159.841 * Doc Risk: 45.147%)
- `kivy/logger.py` -> **Severity: 5075.39** (Blast Radius: 221.393 * Doc Risk: 22.9248%)
- `kivy/config.py` -> **Severity: 1973.96** (Blast Radius: 110.398 * Doc Risk: 17.8804%)
- `kivy/context.py` -> **Severity: 1140.937** (Blast Radius: 11.672 * Doc Risk: 97.7499%)
- `kivy/base.py` -> **Severity: 870.728** (Blast Radius: 20.279 * Doc Risk: 42.9374%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
