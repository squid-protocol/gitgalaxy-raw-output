# ARCHITECTURAL_BRIEF: kivy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/kivy` |
| **Timestamp** | `2026-08-03T19:39:07.896700+00:00` |
| **Scan Duration** | `3.23s` |
| **Git Branch** | `master` |
| **Git Commit** | `dc32205ac51ba5452eb904b2fd78cdafffd64ccd` |
| **Git Remote** | `https://github.com/kivy/kivy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 547 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Cognitive Load Exposure | 0.0 | 99.7 | 17.3 | 9.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 18.0 | 7.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.2 | 0.2 | 0.0 |
| API Exposure | 0.0 | 13.1 | 3.8 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 97.1 | 6.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.8 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 63.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 51.1 | 73.7 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `_select_word` (@ `kivy/uix/textinput.py`) -> Impact: **2788.1** | LOC: 1162
- `resolve_font_name` (@ `kivy/core/text/__init__.py`) -> Impact: **1593.0** | LOC: 579
- `_apply_rule` (@ `kivy/lang/builder.py`) -> Impact: **1535.2** | LOC: 331
  * *Intent:* # register all the dynamic classes for name, baseclasses in parser.dynamic_classes.items(): Factory.register(name, baseclasses=baseclasses, filename=f...
- `add_widget` (@ `kivy/uix/widget.py`) -> Impact: **1463.7** | LOC: 474
- `shorten_post` (@ `kivy/core/text/markup.py`) -> Impact: **1439.8** | LOC: 332
- `gl_check_error` (@ `kivy/graphics/cgl_backend/cgl_debug.pyx`) -> Impact: **1404.2** | LOC: 1272
- `__init__` (@ `kivy/core/image/__init__.py`) -> Impact: **1154.2** | LOC: 404
  * *Intent:* ''' if self._textures is None: self.populate() return self._textures @property def nocache(self): '''Indicate if the texture will not be stored in the...
- `_dispatch_result` (@ `kivy/network/urlrequest.py`) -> Impact: **1099.1** | LOC: 400
- `points` (@ `kivy/graphics/vertex_instructions.pyx`) -> Impact: **1024.3** | LOC: 844
- `screenshot` (@ `kivy/core/window/window_sdl3.py`) -> Impact: **967.5** | LOC: 311

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `add_directive_header` (@ `doc/sources/sphinxext/autodoc.py`) -> **O(2^N) [Recursive]**
- `on_touch_down` (@ `examples/canvas/bezier.py`) -> **O(2^N) [Recursive]**
- `on_touch_up` (@ `examples/canvas/tesselate.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `examples/shader/rotated.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `examples/shader/shadertree.py`) -> **O(2^N) [Recursive]**
- `on_touch_down` (@ `examples/widgets/colorpicker.py`) -> **O(2^N) [Recursive]**
- `goto_node` (@ `examples/widgets/compound_selection.py`) -> **O(2^N) [Recursive]**
  * *Intent:* ''' This function is used to go to the node by typing the number of the text of the button. '''
- `keyboard_on_key_down` (@ `examples/widgets/focus_behavior.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `examples/widgets/sequenced_images/main.py`) -> **O(2^N) [Recursive]**
- `display_settings` (@ `examples/widgets/settings.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `_select_word` (@ `kivy/uix/textinput.py`) -> DB Complexity: **82**
- `points` (@ `kivy/graphics/vertex_instructions.pyx`) -> DB Complexity: **81**
- `make_images_[Truncated]` (@ `kivy/tools/image-testsuite/imagemagick-testsuite.sh`) -> DB Complexity: **74**
  * *Intent:* # Creates 1xN and Nx1 test images from the given pattern, in the given # format. Only use alpha != FF if you are actually testing alpha.
- `draw_pattern` (@ `kivy/tools/image-testsuite/imagemagick-testsuite.sh`) -> DB Complexity: **62**
  * *Intent:* # Outputs command line arguments for convert to draw pixels from the # specified pattern in the specified direction. It is always 1 in w or h.
- `__init__` (@ `kivy/core/image/__init__.py`) -> DB Complexity: **57**
  * *Intent:* ''' if self._textures is None: self.populate() return self._textures @property def nocache(self): '''Indicate if the texture will not be stored in the...
- `resolve_font_name` (@ `kivy/core/text/__init__.py`) -> DB Complexity: **53**
- `__init__` (@ `kivy/input/motionevent.py`) -> DB Complexity: **52**
  * *Intent:* ---------------------------
- `__init__` (@ `kivy/uix/textinput.py`) -> DB Complexity: **49**
- `load_kv` (@ `kivy/app.py`) -> DB Complexity: **46**
- `pkgconfig` (@ `setup.py`) -> DB Complexity: **45**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `kivy/core/window` | 8 | 27558.9 | 20.73% | 42.73% |
| `kivy/uix` | 38 | 26568.64 | 23.09% | 40.03% |
| `kivy` | 33 | 13011.58 | 23.01% | 29.14% |
| `kivy/tests` | 75 | 10546.4 | 7.45% | 0.0% |
| `kivy/graphics` | 47 | 8293.26 | 18.81% | 27.91% |
| `kivy/core/text` | 7 | 5899.04 | 28.64% | 60.45% |
| `kivy/modules` | 13 | 4556.84 | 17.2% | 32.49% |
| `kivy/lang` | 3 | 3680.0 | 29.65% | 57.18% |
| `kivy/input/providers` | 13 | 3633.34 | 40.57% | 25.26% |
| `kivy/uix/behaviors` | 11 | 3624.46 | 19.26% | 23.55% |

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
- `kivy/tests/test_provider_registry.py` -> **45** Orphaned Functions | **0** Duplicates
- `kivy/graphics/vertex_instructions.pyx` -> **0** Orphaned Functions | **42** Duplicates
- `kivy/tests/test_vector.py` -> **42** Orphaned Functions | **0** Duplicates
- `kivy/tests/test_properties.py` -> **40** Orphaned Functions | **0** Duplicates

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

### Obfuscation & Evasion Surface
- `kivy/modules/_webdebugger.py` -> **100.0%** Exposure
- `kivy/tests/test_imageloader.py` -> **100.0%** Exposure
### Exploit Generation Surface
- `doc/sources/sphinxext/autodoc.py` -> **100.0%** Exposure
- `doc/sources/sphinxext/preprocess.py` -> **100.0%** Exposure
- `examples/3Drendering/main.py` -> **100.0%** Exposure
- `examples/3Drendering/objloader.py` -> **100.0%** Exposure
- `examples/RST_Editor/main.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `kivy/lang/builder.py` -> **100.0%** Exposure
- `kivy/modules/_webdebugger.py` -> **100.0%** Exposure
- `kivy/storage/dictstore.py` -> **100.0%** Exposure
- `kivy/tests/test_environ_cli.py` -> **100.0%** Exposure
- `kivy/tools/packaging/pyinstaller_hooks/__init__.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `doc/sources/sphinxext/autodoc.py` -> **100.0%** Exposure
- `doc/sources/sphinxext/preprocess.py` -> **100.0%** Exposure
- `examples/3Drendering/main.py` -> **100.0%** Exposure
- `examples/3Drendering/objloader.py` -> **100.0%** Exposure
- `examples/RST_Editor/main.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3073` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `kivy/clock.py` (PYTHON) -> Cumulative Risk: **909.25**
- **Archetype:** `file_cluster_4` (Distance: 12.175 IQR)
- **Magnitude:** 954.32 | **LOC:** 1344 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `async_idle` (Impact: 86.2), `idle` (Impact: 62.5), `_libc_clock_gettime_wrapper` (Impact: 38.2)

### 2. `kivy/base.py` (PYTHON) -> Cumulative Risk: **877.56**
- **Archetype:** `file_cluster_13` (Distance: 12.922 IQR)
- **Magnitude:** 861.2 | **LOC:** 618 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9997%)
- **Heaviest Functions:** `post_dispatch_input` (Impact: 163.9), `mainloop` (Impact: 73.4), `async_mainloop` (Impact: 48.9)

### 3. `kivy/loader.py` (PYTHON) -> Cumulative Risk: **871.04**
- **Archetype:** `file_cluster_13` (Distance: 12.815 IQR)
- **Magnitude:** 539.26 | **LOC:** 576 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_load_urllib` (Impact: 267.9), `_load` (Impact: 31.8), `_set_max_upload_per_frame` (Impact: 10.6)

### 4. `kivy/core/video/video_ffpyplayer.py` (PYTHON) -> Cumulative Risk: **849.1**
- **Archetype:** `file_cluster_13` (Distance: 13.33 IQR)
- **Magnitude:** 520.86 | **LOC:** 450 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_next_frame_run` (Impact: 156.6), `_redraw` (Impact: 87.5), `play` (Impact: 24.5)

### 5. `kivy/core/video/__init__.py` (PYTHON) -> Cumulative Risk: **846.75**
- **Archetype:** `file_cluster_13` (Distance: 12.671 IQR)
- **Magnitude:** 136.62 | **LOC:** 225 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 22.2), `_set_filename` (Impact: 10.8), `__del__` (Impact: 2.7)

### 6. `kivy/modules/console.py` (PYTHON) -> Cumulative Risk: **821.78**
- **Archetype:** `file_cluster_13` (Distance: 12.313 IQR)
- **Magnitude:** 1834.9 | **LOC:** 1054 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `show_property` (Impact: 634.2), `keyboard_shortcut` (Impact: 158.7), `pick` (Impact: 67.8)

### 7. `kivy/core/window/window_sdl3.py` (PYTHON) -> Cumulative Risk: **818.33**
- **Archetype:** `file_cluster_13` (Distance: 11.897 IQR)
- **Magnitude:** 2092.74 | **LOC:** 884 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `screenshot` (Impact: 967.5), `create_window` (Impact: 283.1), `_update_modifiers` (Impact: 86.8)

### 8. `kivy/core/video/video_android.py` (PYTHON) -> Cumulative Risk: **811.77**
- **Archetype:** `file_cluster_13` (Distance: 11.849 IQR)
- **Magnitude:** 318.42 | **LOC:** 247 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `unload` (Impact: 187.3), `load` (Impact: 24.2), `onError` (Impact: 9.1)

### 9. `kivy/input/providers/mactouch.py` (PYTHON) -> Cumulative Risk: **807.65**
- **Archetype:** `file_cluster_13` (Distance: 10.257 IQR)
- **Magnitude:** 130.68 | **LOC:** 221 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__str__` (Impact: 73.1), `__init__` (Impact: 6.2), `depack` (Impact: 5.5)

### 10. `kivy/core/audio_output/audio_ffpyplayer.py` (PYTHON) -> Cumulative Risk: **803.7**
- **Archetype:** `file_cluster_13` (Distance: 12.034 IQR)
- **Magnitude:** 245.14 | **LOC:** 187 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `load` (Impact: 25.0), `play` (Impact: 21.3), `stop` (Impact: 21.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `kivy/core/window/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.506 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.623 IQR)
- **Top Global Matches:** file_cluster_13: 12.506, file_cluster_8: 12.611, file_cluster_7: 12.723
- **Magnitude:** 24080.32 | **LOC:** 2600 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.1633%), Tech Debt (14.7858%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 319`, `args: 144`, `func_start: 138`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 230`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 89`, `import: 36`
* *Defense:* `safety: 5`, `doc: 227`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` kivy.base, kivy.core.gl, kivy.graphics.opengl, ios, kivy.core.window, kivy.logger, kivy.uix.behaviors, kivy.graphics.context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/uix/textinput.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.781 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.507 IQR)
- **Top Global Matches:** file_cluster_8: 12.781, file_cluster_13: 12.887, file_cluster_7: 12.925
- **Magnitude:** 5406.12 | **LOC:** 4018 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (37.9863%), Tech Debt (30.4251%)
**Top Internal Functions/Classes:**
  * `_select_word` (Impact: 2788.1 | O(2^N) | DB: 82)
  * `do_cursor_movement` (Impact: 356.9 | O(N^6) | DB: 1)
    * *Intent:* # handle undo and redo self._set_unredo_bkspc( cursor_index, cursor_index - 1, substring, from_undo,...
  * `insert_text` (Impact: 185.4 | O(N^6) | DB: 1)
  * `_move_cursor_word_right` (Impact: 117.1 | O(N^6))
  * `_move_cursor_word_left` (Impact: 111.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 600`, `structural_boundaries: 358`, `args: 147`, `func_start: 138`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 599`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `io: 1`, `api: 69`, `import: 31`
* *Defense:* `safety: 26`, `doc: 186`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.336
  * `Choke Point (Betweenness):` 0.001807 | `Ripple Effect (Closeness):` 0.144915
  * `Imports (Out-Degree: 12):` kivy.base, textwrap, weakref, kivy.app, kivy.core.window, kivy.uix.behaviors, kivy.graphics.context, kivy.core.clipboard...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `kivy/uix/scrollview.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.553 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.152 IQR)
- **Top Global Matches:** file_cluster_8: 11.553, file_cluster_13: 11.832, file_cluster_7: 11.846
- **Magnitude:** 3899.78 | **LOC:** 3544 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (25.001%), Tech Debt (14.2194%)
**Top Internal Functions/Classes:**
  * `on_touch_move` (Impact: 275.1 | O(2^N) | DB: 4)
  * `_change_touch_mode` (Impact: 264.6 | O(2^N) | DB: 5)
  * `on_touch_up` (Impact: 234.9 | O(2^N) | DB: 3)
    * *Intent:* # } # Purpose: Coordinates touches across multiple levels of nested # ScrollViews # Lifecycle: Built...
  * `scroll_to` (Impact: 190.3 | O(2^N) | DB: 2)
    * *Intent:* # Check if stored touch is stale (completed but not cleaned up) # This happens when a touch complete...
  * `_scroll_initialize` (Impact: 181.9 | O(N^6) | DB: 3)
    * *Intent:* # Need minimum movement to determine direction
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 319`, `args: 86`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 246`, `dead_code: 6`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 41`, `import: 16`
* *Defense:* `safety: 12`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.199
  * `Choke Point (Betweenness):` 0.003773 | `Ripple Effect (Closeness):` 0.145721
  * `Imports (Out-Degree: 8):` kivy.uix.gridlayout, kivy.graphics, kivy.animation, kivy.uix.stencilview, kivy.factory, kivy.uix.scrollview, kivy.effects.dampedscroll, kivy.app...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `kivy/core/text/markup.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.289 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.818 IQR)
- **Top Global Matches:** file_cluster_13: 12.289, file_cluster_17: 12.324, file_cluster_8: 12.36
- **Magnitude:** 2495.36 | **LOC:** 961 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (52.9791%), Tech Debt (9.8918%)
**Top Internal Functions/Classes:**
  * `shorten_post` (Impact: 1439.8 | O(2^N) | DB: 36)
  * `_pre_render` (Impact: 591.3 | O(N^6) | DB: 13)
  * `render_lines` (Impact: 216.1 | O(N^6) | DB: 2)
    * *Intent:* # now keep adding spaces to already split words until done
  * `get_markup_label_class` (Impact: 22.8 | O(N^3) | DB: 5)
  * `render` (Impact: 10.8 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 92`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 150`, `dead_code: 9`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 6`, `doc: 26`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.539
  * `Choke Point (Betweenness):` 0.0009 | `Ripple Effect (Closeness):` 0.166687
  * `Imports (Out-Degree: 2):` kivy.core.text, kivy.parser, kivy.core.text.text_layout, kivy.logger, kivy.properties, copy, functools, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/lang/builder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.858 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.323 IQR)
- **Top Global Matches:** file_cluster_13: 12.858, file_cluster_17: 13.035, file_cluster_0: 13.089
- **Magnitude:** 2457.32 | **LOC:** 1024 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (35.1378%), Tech Debt (10.3521%)
**Top Internal Functions/Classes:**
  * `_apply_rule` (Impact: 1535.2 | O(2^N) | DB: 24)
    * *Intent:* # register all the dynamic classes for name, baseclasses in parser.dynamic_classes.items(): Factory....
  * `update_intermediates` (Impact: 254.8 | O(2^N))
  * `load_file` (Impact: 184.6 | O(N^6) | DB: 10)
  * `create_handler` (Impact: 181.7 | O(N^6) | DB: 4)
    * *Intent:* # bind all attrs, except last to update_intermediates for val in keys[s:-1]: # if we need to dynamic...
  * `apply_rules` (Impact: 102.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 125`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 79`, `dead_code: 8`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 25`, `import: 17`
* *Defense:* `safety: 46`, `doc: 41`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.13
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.021742
  * `Imports (Out-Degree: 6):` os.path, kivy.factory, kivy.utils, os, kivy, atexit, kivy.lang.parser, kivy.logger...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `kivy/core/text/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.342 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.698 IQR)
- **Top Global Matches:** file_cluster_0: 12.342, file_cluster_13: 12.359, file_cluster_11: 12.588
- **Magnitude:** 2183.86 | **LOC:** 1241 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (38.3768%), Tech Debt (18.1685%)
**Top Internal Functions/Classes:**
  * `resolve_font_name` (Impact: 1593.0 | O(2^N) | DB: 53)
  * `__init__` (Impact: 359.4 | O(N^5) | DB: 7)
  * `register` (Impact: 52.5 | O(N^5) | DB: 2)
  * `get_provider_class` (Impact: 18.2 | O(N^4))
  * `_migrate_deprecated_padding_xy` (Impact: 10.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 133`, `args: 43`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 88`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 14`, `api: 36`, `import: 16`
* *Defense:* `safety: 6`, `doc: 56`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` kivy.utils, kivy.graphics.texture, kivy.core.text, os, kivy.uix.label, kivy, ast, kivy.core.text.text_layout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/window/window_sdl3.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.897 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.498 IQR)
- **Top Global Matches:** file_cluster_13: 11.897, file_cluster_8: 11.995, file_cluster_0: 12.237
- **Magnitude:** 2092.74 | **LOC:** 884 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (63.1884%), Tech Debt (72.9769%)
**Top Internal Functions/Classes:**
  * `screenshot` (Impact: 967.5 | O(2^N) | DB: 21)
  * `create_window` (Impact: 283.1 | O(2^N) | DB: 15)
  * `_update_modifiers` (Impact: 86.8 | O(N^4) | DB: 1)
  * `_event_filter` (Impact: 86.2 | O(N^6) | DB: 3)
  * `update` (Impact: 84.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 140`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 139`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 30`, `import: 21`
* *Defense:* `safety: 13`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` kivy.core.window._window_sdl3, kivy.base, os.path, kivy.utils, kivy.graphics.opengl, kivy.input.motionevent, kivy, kivy.app...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/core/image/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.252 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.951 IQR)
- **Top Global Matches:** file_cluster_0: 13.252, file_cluster_13: 13.27, file_cluster_11: 13.522
- **Magnitude:** 2017.6 | **LOC:** 1306 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (48.8188%), Tech Debt (41.1651%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1154.2 | O(2^N) | DB: 57)
    * *Intent:* ''' if self._textures is None: self.populate() return self._textures @property def nocache(self): ''...
  * `populate` (Impact: 512.7 | O(2^N) | DB: 13)
  * `iterate_mipmaps` (Impact: 13.4 | O(N^4))
  * `__init__` (Impact: 12.6 | O(N^3) | DB: 9)
    * *Intent:* ------------------
  * `__init__` (Impact: 8.9 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 166`, `args: 58`, `func_start: 58`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 200`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 52`, `import: 18`
* *Defense:* `safety: 20`, `doc: 98`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` base64, kivy.logger, zipfile, kivy.clock, kivy.setupconfig, kivy.uix.image, re, kivy.graphics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/uix/widget.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.772 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.096 IQR)
- **Top Global Matches:** file_cluster_13: 11.772, file_cluster_7: 11.915, file_cluster_8: 12.019
- **Magnitude:** 2011.82 | **LOC:** 1625 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (30.919%), Tech Debt (22.9892%)
**Top Internal Functions/Classes:**
  * `add_widget` (Impact: 1463.7 | O(2^N) | DB: 18)
  * `on_motion` (Impact: 181.1 | O(2^N))
  * `__init__` (Impact: 88.5 | O(2^N) | DB: 4)
  * `on_touch_down` (Impact: 43.7 | O(2^N))
  * `on_touch_move` (Impact: 35.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 130`, `args: 47`, `func_start: 47`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 61`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 45`, `import: 13`
* *Defense:* `safety: 8`, `doc: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.675
  * `Choke Point (Betweenness):` 0.008934 | `Ripple Effect (Closeness):` 0.294511
  * `Imports (Out-Degree: 7):` kivy.eventmanager, kivy.graphics, kivy.base, itertools, kivy.event, kivy.factory, kivy.core.image, kivy.graphics.transformation...
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `kivy/graphics/vertex_instructions.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.999 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.426 IQR)
- **Top Global Matches:** file_cluster_0: 11.999, file_cluster_8: 12.036, file_cluster_7: 12.18
- **Magnitude:** 1902.78 | **LOC:** 2301 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (40.2078%), Tech Debt (99.9951%)
**Top Internal Functions/Classes:**
  * `points` (Impact: 1024.3 | O(2^N) | DB: 81)
  * `__init__` (Impact: 78.8 | O(2^N) | DB: 7)
  * `__init__` (Impact: 56.0 | O(2^N) | DB: 6)
  * `points` (Impact: 42.1 | O(2^N) | DB: 1)
  * `indices` (Impact: 26.4 | O(2^N) | DB: 2)
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
- **Top Global Matches:** file_cluster_13: 12.313, file_cluster_8: 12.55, file_cluster_0: 12.625
- **Magnitude:** 1834.9 | **LOC:** 1054 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (35.1582%), Tech Debt (99.9533%)
**Top Internal Functions/Classes:**
  * `show_property` (Impact: 634.2 | O(2^N))
  * `keyboard_shortcut` (Impact: 158.7 | O(N^6) | DB: 8)
  * `pick` (Impact: 67.8 | O(2^N))
  * `on_touch_down` (Impact: 61.2 | O(2^N) | DB: 1)
  * `highlight_at` (Impact: 56.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 177`, `args: 67`, `func_start: 67`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 115`, `dead_code: 1`, `duplicate_logic: 24`
* *Architecture:* `api: 80`, `import: 24`
* *Defense:* `safety: 35`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` kivy.uix.gridlayout, weakref, kivy.uix.modalview, kivy.logger, kivy.clock, kivy.uix.image, kivy.graphics, kivy.uix.widget...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/modules/inspector.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.982 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.452 IQR)
- **Top Global Matches:** file_cluster_8: 11.982, file_cluster_13: 12.0, file_cluster_0: 12.304
- **Magnitude:** 1564.02 | **LOC:** 756 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (38.8452%), Tech Debt (35.0851%)
**Top Internal Functions/Classes:**
  * `show_property` (Impact: 634.1 | O(2^N))
  * `pick` (Impact: 67.7 | O(2^N))
  * `show_widget_info` (Impact: 64.3 | O(N^5) | DB: 2)
  * `on_activated` (Impact: 55.3 | O(N^5) | DB: 3)
  * `on_touch_down` (Impact: 52.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 98`, `args: 33`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 70`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `safety: 39`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` kivy.modules, itertools, kivy.animation, kivy.factory, weakref, kivy.app, kivy.graphics.transformation, kivy.core.window...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/multistroke.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.395 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.717 IQR)
- **Top Global Matches:** file_cluster_8: 11.395, file_cluster_13: 11.474, file_cluster_7: 11.602
- **Magnitude:** 1480.06 | **LOC:** 1475 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (17.5852%), Tech Debt (99.9291%)
**Top Internal Functions/Classes:**
  * `filter` (Impact: 210.3 | O(N^6) | DB: 1)
  * `recognize` (Impact: 170.6 | O(N^6))
    * *Intent:* # Min priority 50, max 100 gdb.filter(priority=[50, 100]) When this option is used, :attr:`Recognize...
  * `import_gesture` (Impact: 67.7 | O(2^N) | DB: 4)
  * `resample` (Impact: 64.3 | O(2^N))
  * `_heap_permute` (Impact: 63.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 154`, `args: 58`, `func_start: 56`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 94`, `fragile_debt: 5`, `duplicate_logic: 13`
* *Architecture:* `io: 2`, `api: 58`, `import: 12`
* *Defense:* `safety: 11`, `doc: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.686
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004992
  * `Imports (Out-Degree: 3):` base64, kivy.multistroke, kivy.event, zlib, kivy.vector, pickle, io, collections...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/network/urlrequest.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.138 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.325 IQR)
- **Top Global Matches:** file_cluster_13: 12.138, file_cluster_0: 12.368, file_cluster_8: 12.457
- **Magnitude:** 1459.96 | **LOC:** 794 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (37.3073%), Tech Debt (15.2032%)
**Top Internal Functions/Classes:**
  * `_dispatch_result` (Impact: 1099.1 | O(2^N) | DB: 22)
  * `_fetch_url` (Impact: 105.6 | O(N^6) | DB: 3)
  * `run` (Impact: 58.5 | O(N^4) | DB: 1)
  * `decode_result` (Impact: 30.9 | O(N^5))
  * `__init__` (Impact: 1.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 103`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 125`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 29`, `concurrency: 1`, `import: 17`
* *Defense:* `safety: 18`, `doc: 24`, `test: 1`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.95
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003328
  * `Imports (Out-Degree: 5):` ssl, requests, base64, kivy.utils, time, certifi, os, json...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/graphics/cgl_backend/cgl_debug.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.159 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.257 IQR)
- **Top Global Matches:** file_cluster_8: 9.159, file_cluster_7: 9.827, file_cluster_1: 10.081
- **Magnitude:** 1437.86 | **LOC:** 1425 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (11.9707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gl_check_error` (Impact: 1404.2 | O(2^N))
  * `init_backend_debug` (Impact: 4.2 | O(N^1) | DB: 1)
  * `gl_debug_print` (Impact: 3.6 | O(N^1))
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

### `kivy/uix/carousel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.058 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.715 IQR)
- **Top Global Matches:** file_cluster_13: 12.058, file_cluster_8: 12.089, file_cluster_7: 12.227
- **Magnitude:** 1311.68 | **LOC:** 696 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (29.5969%), Tech Debt (11.7439%)
**Top Internal Functions/Classes:**
  * `on_touch_move` (Impact: 256.6 | O(2^N) | DB: 2)
  * `_position_visible_slides` (Impact: 245.4 | O(N^6))
  * `on__offset` (Impact: 126.4 | O(N^5) | DB: 2)
  * `on_touch_up` (Impact: 104.9 | O(2^N) | DB: 1)
  * `_insert_visible_slides` (Impact: 81.7 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 82`, `args: 32`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `state_mutation: 88`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `import: 8`
* *Defense:* `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003328
  * `Imports (Out-Degree: 5):` kivy.uix.carousel, kivy.animation, kivy.uix.stencilview, kivy.factory, kivy.app, kivy.clock, kivy.properties, kivy.uix.image...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.103 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.378 IQR)
- **Top Global Matches:** file_cluster_8: 10.103, file_cluster_13: 10.487, file_cluster_7: 10.63
- **Magnitude:** 1219.72 | **LOC:** 1527 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (9.7796%), Tech Debt (15.7373%)
**Top Internal Functions/Classes:**
  * `pkgconfig` (Impact: 621.3 | O(2^N) | DB: 45)
  * `determine_sdl3` (Impact: 118.9 | O(N^5) | DB: 11)
  * `determine_gl_flags` (Impact: 116.9 | O(N^4))
  * `determine_base_flags` (Impact: 54.0 | O(N^5) | DB: 6)
  * `determine_angle_flags` (Impact: 44.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 115`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 2`, `state_mutation: 54`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 30`, `api: 22`, `import: 27`
* *Defense:* `safety: 7`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` textwrap, subprocess, logging, setuptools.command.build_ext, setuptools, kivy_deps.sdl3_dev, tempfile, kivy.tools.packaging.factory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/lang/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.03 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.812 IQR)
- **Top Global Matches:** file_cluster_13: 12.03, file_cluster_17: 12.378, file_cluster_0: 12.379
- **Magnitude:** 1209.08 | **LOC:** 828 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (48.8209%), Tech Debt (61.1985%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 543.5 | O(N^6) | DB: 25)
  * `get_names_from_expression` (Impact: 194.0 | O(2^N) | DB: 2)
    * *Intent:* """ Look for all the symbols used in an ast node. """
  * `_build_rule` (Impact: 124.5 | O(N^6) | DB: 3)
  * `precompile` (Impact: 49.1 | O(2^N))
  * `__init__` (Impact: 31.0 | O(2^N) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 120`, `args: 34`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 6`, `state_mutation: 105`, `dead_code: 5`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 24`, `import: 22`
* *Defense:* `safety: 26`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.403
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.013045
  * `Imports (Out-Degree: 7):` package, kivy.app, kivy.logger, kivy.lang.builder, re, importlib, os, traceback...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/uix/rst.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.258 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.51 IQR)
- **Top Global Matches:** file_cluster_13: 12.258, file_cluster_8: 12.452, file_cluster_0: 12.658
- **Magnitude:** 1195.9 | **LOC:** 1489 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (39.827%), Tech Debt (92.1636%)
**Top Internal Functions/Classes:**
  * `dispatch_visit` (Impact: 681.2 | O(N^5) | DB: 38)
  * `brute_refs` (Impact: 87.2 | O(N^6) | DB: 1)
  * `goto` (Impact: 26.9 | O(N^4) | DB: 1)
  * `dispatch_visit` (Impact: 26.8 | O(N^4) | DB: 3)
  * `_load_from_text` (Impact: 14.8 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 149`, `args: 30`, `func_start: 29`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 174`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 4`, `api: 57`, `import: 22`
* *Defense:* `safety: 25`, `doc: 40`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003328
  * `Imports (Out-Degree: 10):` kivy.uix.gridlayout, kivy.base, kivy.logger, kivy.clock, parse_color, kivy.uix.image, os, kivy.uix.videoplayer...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kivy/config.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.276 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.849 IQR)
- **Top Global Matches:** file_cluster_13: 11.276, file_cluster_8: 11.376, file_cluster_0: 11.421
- **Magnitude:** 1147.18 | **LOC:** 1037 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (13.1158%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 865.4 | O(2^N) | DB: 5)
  * `read` (Impact: 105.5 | O(2^N) | DB: 1)
  * `_do_callbacks` (Impact: 33.9 | O(N^4))
  * `set` (Impact: 18.4 | O(2^N))
  * `getdefault` (Impact: 13.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 70`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 17`, `dead_code: 3`
* *Architecture:* `io: 2`, `api: 19`, `import: 9`
* *Defense:* `safety: 19`, `doc: 36`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 110.398
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.320642
  * `Imports (Out-Degree: 2):` os.path, kivy.utils, weakref, os, kivy, collections, kivy.logger, kivy.config...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `kivy/uix/filechooser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.047 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.561 IQR)
- **Top Global Matches:** file_cluster_13: 12.047, file_cluster_8: 12.368, file_cluster_7: 12.404
- **Magnitude:** 1118.88 | **LOC:** 1114 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (27.5881%), Tech Debt (99.7544%)
**Top Internal Functions/Classes:**
  * `is_hidden` (Impact: 380.8 | O(N^6) | DB: 14)
  * `_generate_file_entries` (Impact: 92.5 | O(N^5) | DB: 4)
  * `set_view_mode` (Impact: 53.9 | O(2^N) | DB: 3)
  * `_create_files_entries` (Impact: 45.7 | O(N^4) | DB: 4)
  * `_add_files` (Impact: 42.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 175`, `args: 69`, `func_start: 67`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 82`, `dead_code: 2`, `fragile_debt: 3`, `duplicate_logic: 10`
* *Architecture:* `io: 4`, `api: 63`, `import: 21`
* *Defense:* `safety: 19`, `doc: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.946
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.142842
  * `Imports (Out-Degree: 5):` textwrap, weakref, kivy.app, kivy.logger, kivy.clock, kivy.core.text, os, pprint...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `kivy/app.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.7 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.944 IQR)
- **Top Global Matches:** file_cluster_13: 12.7, file_cluster_0: 12.997, file_cluster_11: 13.199
- **Magnitude:** 1105.56 | **LOC:** 1361 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (37.4908%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_kv` (Impact: 965.9 | O(2^N) | DB: 46)
  * `on_title` (Impact: 8.2 | O(N^3))
  * `on_icon` (Impact: 8.2 | O(N^3))
  * `build` (Impact: 7.2 | O(N^3))
  * `__init__` (Impact: 6.3 | O(2^N) | DB: 9)
    * *Intent:* -------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 121`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 66`, `dead_code: 3`
* *Architecture:* `io: 10`, `api: 35`, `concurrency: 2`, `import: 21`
* *Defense:* `safety: 12`, `doc: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.21
  * `Choke Point (Betweenness):` 0.023527 | `Ripple Effect (Closeness):` 0.271622
  * `Imports (Out-Degree: 9):` kivy.base, cProfile, kivy.app, kivy.core.window, kivy.logger, kivy.setupconfig, os, kivy.uix.settings...
  * `Imported By (In-Degree: 168):` (Excluded from Brief to save tokens)

### `kivy/graphics/opengl.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.931 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.269 IQR)
- **Top Global Matches:** file_cluster_8: 9.931, file_cluster_7: 10.123, file_cluster_1: 10.407
- **Magnitude:** 1045.7 | **LOC:** 1557 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.0534%), Tech Debt (9.4449%)
**Top Internal Functions/Classes:**
  * `glReadPixels` (Impact: 80.8 | O(2^N))
  * `glVertexAttribPointer` (Impact: 40.2 | O(2^N))
    * *Intent:* ''' cgl.glTexParameteri(target, pname, param) def glTexParameteriv(GLenum target, GLenum pname):#, G...
  * `glDrawElements` (Impact: 34.1 | O(2^N))
    * *Intent:* '''See: `glDeleteShader() on Kronos website <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDe...
  * `glCompressedTexSubImage2D` (Impact: 22.5 | O(2^N))
    * *Intent:* # >_< #def glClearDepthf(GLclampf depth): # '''See: `glClearDepthf() on Kronos website # <http://www...
  * `glTexImage2D` (Impact: 22.5 | O(2^N))
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

### `kivy/graphics/context_instructions.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.716 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.202 IQR)
- **Top Global Matches:** file_cluster_0: 12.716, file_cluster_13: 13.027, file_cluster_8: 13.08
- **Magnitude:** 1040.0 | **LOC:** 948 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (49.2105%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 155.2 | O(2^N) | DB: 6)
  * `__init__` (Impact: 91.3 | O(2^N) | DB: 9)
  * `__init__` (Impact: 73.3 | O(2^N) | DB: 3)
  * `__init__` (Impact: 61.1 | O(2^N) | DB: 6)
  * `origin` (Impact: 28.1 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 178`, `args: 99`, `func_start: 92`
* *Risk/State:* `state_mutation: 183`, `fragile_debt: 1`, `duplicate_logic: 90`
* *Architecture:* `io: 1`, `api: 53`, `import: 6`
* *Defense:* `safety: 4`, `doc: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` kivy.graphics, os.path, kivy.core.image, kivy, kivy.resources, kivy.logger, kivy.cache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `kivy/animation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.945 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.657 IQR)
- **Top Global Matches:** file_cluster_0: 11.945, file_cluster_12: 12.17, file_cluster_13: 12.216
- **Magnitude:** 1033.1 | **LOC:** 831 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (46.369%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_calculate` (Impact: 148.6 | O(2^N))
  * `cancel_all` (Impact: 80.0 | O(N^6) | DB: 2)
  * `_update` (Impact: 59.1 | O(N^5) | DB: 1)
  * `stop_all` (Impact: 31.7 | O(N^5))
  * `cancel_property` (Impact: 30.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 167`, `args: 76`, `func_start: 76`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 73`, `planned_debt: 1`, `duplicate_logic: 24`
* *Architecture:* `api: 102`, `import: 5`
* *Defense:* `safety: 10`, `doc: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.123
  * `Choke Point (Betweenness):` 9.8e-05 | `Ripple Effect (Closeness):` 0.154526
  * `Imports (Out-Degree: 3):` kivy.event, math, collections, kivy.clock, kivy.weakproxy
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `kivy/graphics/fbo.pyx` (PYTHON) | Magnitude: 196.56 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 243, encapsulation: 83, state_mutation: 80, branch: 58
- `kivy/core/text/__init__.py` (PYTHON) | Magnitude: 2183.86 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 568, branch: 165, structural_boundaries: 133, encapsulation: 99
- `kivy/core/image/__init__.py` (PYTHON) | Magnitude: 2017.6 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 558, state_mutation: 200, encapsulation: 188, structural_boundaries: 166
- `kivy/graphics/vertex_instructions.pyx` (PYTHON) | Magnitude: 1902.78 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1272, state_mutation: 320, encapsulation: 295, branch: 201
- `kivy/graphics/boxshadow.pyx` (PYTHON) | Magnitude: 142.24 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 223, encapsulation: 141, structural_boundaries: 48, state_mutation: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `kivy/event.py` (PYTHON) | Magnitude: 14.12 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 8, events: 3, structural_boundaries: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `kivy/tools/image-testsuite/imagemagick-testsuite.sh` (SHELL) | Magnitude: 0.29 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 93, branch: 59, safety_bypasses: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `kivy/input/factory.py` (PYTHON) | Magnitude: 20.06 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 11, doc: 10, api: 7, structural_boundaries: 6
- `tools/build_macos_dependencies.sh` (SHELL) | Magnitude: 0.06 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 34, reflection_metaprogramming: 27, safety_bypasses: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/async/asyncio_basic.py` (PYTHON) | Magnitude: 37.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, concurrency: 12, doc: 10
- `examples/tutorials/pong/main.py` (PYTHON) | Magnitude: 73.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 22, branch: 11, api: 10
- `kivy/tests/visual_test_label.py` (PYTHON) | Magnitude: 59.38 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 24, branch: 10, import: 9
- `examples/svg/benchmark.py` (PYTHON) | Magnitude: 15.36 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, import: 7, globals: 4
- `kivy/tests/test_clock.py` (PYTHON) | Magnitude: 123.4 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 99, test: 73, safety: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `kivy/tests/async_common.py` (PYTHON) | Magnitude: 765.58 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 363, structural_boundaries: 97, branch: 76, api: 36
- `kivy/clock.py` (PYTHON) | Magnitude: 954.32 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 482, encapsulation: 252, structural_boundaries: 154, concurrency: 129
- `tools/build_linux_dependencies.sh` (SHELL) | Magnitude: 0.06 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, state_mutation: 31, safety_bypasses: 26, reflection_metaprogramming: 11
- `kivy/tests/test_uix_dropdown.py` (PYTHON) | Magnitude: 58.8 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 42, test: 11, safety: 10
- `examples/async/asyncio_advanced.py` (PYTHON) | Magnitude: 90.62 | Delta: **0.325 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, concurrency: 27, structural_boundaries: 15, doc: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `kivy/input/shape.py` (PYTHON) | Magnitude: 10.78 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, indent_spaces: 6, structural_boundaries: 4, encapsulation: 4
- `kivy/eventmanager/__init__.py` (PYTHON) | Magnitude: 28.68 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, indent_spaces: 5, structural_boundaries: 4, api: 4
- `kivy/tools/pep8checker/pep8.py` (PYTHON) | Magnitude: 1.46 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 671, branch: 442, doc: 182, structural_boundaries: 139
- `kivy/uix/treeview.py` (PYTHON) | Magnitude: 554.24 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 218, doc: 71, branch: 59, structural_boundaries: 59
- `kivy/input/provider.py` (PYTHON) | Magnitude: 31.84 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 10, structural_boundaries: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `kivy/core/gl/__init__.py` (PYTHON) | Magnitude: 77.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 22, import: 11, branch: 10
- `kivy/uix/button.py` (PYTHON) | Magnitude: 17.3 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, indent_spaces: 10, structural_boundaries: 7, import: 3
- `kivy/uix/recycleview/datamodel.py` (PYTHON) | Magnitude: 226.94 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, branch: 34, structural_boundaries: 27, encapsulation: 19
- `kivy/effects/dampedscroll.py` (PYTHON) | Magnitude: 225.78 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 46, branch: 27, structural_boundaries: 20
- `kivy/graphics/context.pyx` (PYTHON) | Magnitude: 430.56 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
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
- `kivy/clock.py` -> Churn: **59.53%** | Cog Load: 49.6671% | Debt: 99.9999%
- `kivy/graphics/boxshadow.pyx` -> Churn: **59.53%** | Cog Load: 21.1515% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `kivy/uix/scrollview.py` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 3899.78
- `kivy/lang/builder.py` -> **clayote** (100.0% isolated ownership) | Magnitude: 2457.32
- `kivy/uix/rst.py` -> **haosenwang1018** (100.0% isolated ownership) | Magnitude: 1195.9
- `kivy/config.py` -> **Kristian Sloth Lauszus** (100.0% isolated ownership) | Magnitude: 1147.18
- `kivy/_event.pyx` -> **Elliot Garbus** (100.0% isolated ownership) | Magnitude: 1002.44

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

- `kivy/base.py` -> **Severity: 15.862** (Embedded: 0.2904 * Error Risk: 54.6154%)
- `kivy/app.py` -> **Severity: 13.372** (Embedded: 0.2716 * Error Risk: 49.2308%)
- `kivy/cache.py` -> **Severity: 13.289** (Embedded: 0.1779 * Error Risk: 74.7154%)
- `kivy/context.py` -> **Severity: 11.67** (Embedded: 0.2388 * Error Risk: 48.8679%)
- `kivy/uix/togglebutton.py` -> **Severity: 11.545** (Embedded: 0.1443 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `kivy/utils.py` -> **Severity: 15984.1** (Blast Radius: 159.841 * Doc Risk: 100.0%)
- `kivy/logger.py` -> **Severity: 15542.829** (Blast Radius: 221.393 * Doc Risk: 70.2047%)
- `kivy/config.py` -> **Severity: 11039.8** (Blast Radius: 110.398 * Doc Risk: 100.0%)
- `kivy/clock.py` -> **Severity: 2312.1** (Blast Radius: 23.121 * Doc Risk: 100.0%)
- `kivy/base.py` -> **Severity: 2027.89** (Blast Radius: 20.279 * Doc Risk: 99.9995%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
