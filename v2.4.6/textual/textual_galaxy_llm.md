# ARCHITECTURAL_BRIEF: textual
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/textual` |
| **Timestamp** | `2026-08-03T19:43:08.173200+00:00` |
| **Scan Duration** | `3.81s` |
| **Git Branch** | `main` |
| **Git Commit** | `04b03c8db64266a6a7811cc161bae9986e53b1a1` |
| **Git Remote** | `https://github.com/Textualize/textual.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 687 malicious artifacts.

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
| Total Artifacts | 2116 |
| Analyzed Artifacts (Scanned) | 714 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1402 |
| Total LOC | 78913 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 33.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4388 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3592 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6913 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 56 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 670 | 77195 | 93.8% |
| MARKDOWN | 23 | 0 | 3.2% |
| SCHEME | 15 | 1454 | 2.1% |
| XML | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 83 | 0.1% |
| YAML | 1 | 4 | 0.1% |
| PLAINTEXT | 1 | 0 | 0.1% |
| TYPESCRIPT | 1 | 177 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.966`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 361 | 50.6% |
| file_cluster_8 | 156 | 21.8% |
| file_cluster_4 | 86 | 12.0% |
| file_cluster_16 | 79 | 11.1% |
| file_cluster_2 | 3 | 0.4% |
| file_cluster_7 | 2 | 0.3% |
| file_cluster_0 | 2 | 0.3% |
| file_cluster_17 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 24 | 3.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1402*

**Composition by Extension & Reason:**
- `.svg`: 528x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 317x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1270 LOC)
- `.md`: 298x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3621 LOC)
- `.tcss`: 146x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Unsupported Extension: '.tcss')
- `.png`: 35x Excluded (Explicitly Denied Extension: '.png')
- `.gif`: 26x Excluded (Explicitly Denied Extension: '.gif')
- `.yml`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mov`: 3x Excluded (Explicitly Denied Extension: '.mov')
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.monopic`: 2x Excluded (Unsupported Extension: '.monopic')
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')
- `.mp4`: 1x Excluded (Explicitly Denied Extension: '.mp4')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.6 | 13.3 | 7.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 7.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.2 | 5.3 | 4.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 35.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 16.7 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 12.9 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 56.3 | 74.1 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 35.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/textual/drivers/linux_driver.py` (Hits: 11)
- `src/textual/_import_app.py` (Hits: 10)
- `src/textual/app.py` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **app.py** (`src/textual/app.py`) — 374 inbound connections
2. **widgets.py** (`src/textual/demo/widgets.py`) — 316 inbound connections
3. **containers.py** (`src/textual/containers.py`) — 102 inbound connections
4. **widget.py** (`src/textual/widget.py`) — 99 inbound connections
5. **geometry.py** (`src/textual/geometry.py`) — 80 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **app.py** (`src/textual/app.py`) — 89 outbound dependencies
2. **widget.py** (`src/textual/widget.py`) — 57 outbound dependencies
3. **__init__.py** (`src/textual/widgets/__init__.py`) — 45 outbound dependencies
4. **dom.py** (`src/textual/dom.py`) — 44 outbound dependencies
5. **screen.py** (`src/textual/screen.py`) — 42 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_child_by_type` (@ `src/textual/widget.py`) -> Impact: **2779.0** | LOC: 2597
- `check_identifiers` (@ `src/textual/dom.py`) -> Impact: **2615.5** | LOC: 1388
  * *Intent:* """Validate identifier and raise an error if it fails. Args: description: Description of where identifier is used for error message. *names: Identifie...
- `process_transition` (@ `src/textual/css/_styles_builder.py`) -> Impact: **820.1** | LOC: 443
- `__set__` (@ `src/textual/css/_style_properties.py`) -> Impact: **669.5** | LOC: 230
- `get_content_tab` (@ `src/textual/widgets/_tabbed_content.py`) -> Impact: **652.1** | LOC: 432
- `_forward_event` (@ `src/textual/screen.py`) -> Impact: **491.1** | LOC: 122
- `update` (@ `src/textual/widgets/_select.py`) -> Impact: **478.4** | LOC: 353
- `write_binary_encoded` (@ `src/textual/drivers/web_driver.py`) -> Impact: **460.6** | LOC: 252
- `_render_line` (@ `src/textual/widgets/_text_area.py`) -> Impact: **447.6** | LOC: 223
- `shebang_python` (@ `src/textual/_import_app.py`) -> Impact: **438.7** | LOC: 94
  * *Intent:* """Does the given file look like it's run with Python? Args: candidate: The candidate file to check. Returns: ``True`` if it looks to #! python, ``Fal...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `shebang_python` (@ `src/textual/_import_app.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Does the given file look like it's run with Python? Args: candidate: The candidate file to check. Returns: ``True`` if it looks to #! python, ``Fal...
- `__init_subclass__` (@ `src/textual/app.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """The original stderr stream (before redirection etc)."""
- `join` (@ `src/textual/content.py`) -> **O(2^N) [Recursive]**
- `_spacing_examples` (@ `src/textual/css/_help_text.py`) -> **O(2^N) [Recursive]**
- `__set__` (@ `src/textual/css/_style_properties.py`) -> **O(2^N) [Recursive]**
- `generate` (@ `src/textual/design.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Generate a mapping of color name on to a CSS color. Returns: A mapping of color name on to a CSS-style encoded color """
- `check_identifiers` (@ `src/textual/dom.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Validate identifier and raise an error if it fails. Args: description: Description of where identifier is used for error message. *names: Identifie...
- `write_binary_encoded` (@ `src/textual/drivers/web_driver.py`) -> **O(2^N) [Recursive]**
- `get_offsets` (@ `src/textual/fuzzy.py`) -> **O(2^N) [Recursive]**
- `app` (@ `src/textual/message_pump.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_child_by_type` (@ `src/textual/widget.py`) -> DB Complexity: **52**
- `go` (@ `src/textual/widgets/_markdown.py`) -> DB Complexity: **42**
- `check_identifiers` (@ `src/textual/dom.py`) -> DB Complexity: **40**
  * *Intent:* """Validate identifier and raise an error if it fails. Args: description: Description of where identifier is used for error message. *names: Identifie...
- `shebang_python` (@ `src/textual/_import_app.py`) -> DB Complexity: **29**
  * *Intent:* """Does the given file look like it's run with Python? Args: candidate: The candidate file to check. Returns: ``True`` if it looks to #! python, ``Fal...
- `__rich__` (@ `src/textual/css/tokenizer.py`) -> DB Complexity: **27**
- `update` (@ `src/textual/widgets/_select.py`) -> DB Complexity: **26**
- `get_content_tab` (@ `src/textual/widgets/_tabbed_content.py`) -> DB Complexity: **16**
- `main` (@ `src/textual/demo/_project_stargazer_updater.py`) -> DB Complexity: **15**
- `clear` (@ `src/textual/widgets/_data_table.py`) -> DB Complexity: **15**
- `start_application_mode` (@ `src/textual/drivers/linux_driver.py`) -> DB Complexity: **14**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/textual` | 121 | 28846.56 | 21.27% | 25.3% |
| `src/textual/widgets` | 59 | 15698.97 | 17.05% | 32.72% |
| `tests` | 130 | 13818.42 | 12.46% | 0.0% |
| `src/textual/css` | 20 | 5285.74 | 17.05% | 18.82% |
| `tests/snapshot_tests/snapshot_apps` | 147 | 2429.06 | 4.86% | 0.0% |
| `tests/snapshot_tests` | 3 | 2273.32 | 4.21% | 0.0% |
| `tests/text_area` | 12 | 1816.44 | 21.48% | 0.0% |
| `src/textual/drivers` | 12 | 1790.02 | 16.15% | 14.24% |
| `examples` | 19 | 1516.53 | 15.24% | 0.0% |
| `src/textual/demo` | 11 | 1263.46 | 12.99% | 35.92% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/textual/_time.py` -> **100.0%** Exposure
- `src/textual/_tree_sitter.py` -> **100.0%** Exposure
- `src/textual/cache.py` -> **100.0%** Exposure
- `src/textual/clock.py` -> **100.0%** Exposure
- `src/textual/css/_help_renderables.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/textual/css/scalar_animation.py` -> **100.0%** Exposure
- `src/textual/document/_history.py` -> **100.0%** Exposure
- `src/textual/renderables/bar.py` -> **100.0%** Exposure
- `src/textual/_parser.py` -> **99.9999%** Exposure
- `src/textual/compose.py` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/snapshot_tests/test_snapshots.py` -> **225** Orphaned Functions | **0** Duplicates
- `tests/test_geometry.py` -> **87** Orphaned Functions | **0** Duplicates
- `tests/test_data_table.py` -> **66** Orphaned Functions | **0** Duplicates
- `src/textual/css/_style_properties.py` -> **0** Orphaned Functions | **52** Duplicates
- `tests/test_binding_inheritance.py` -> **12** Orphaned Functions | **30** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/textual/_resolve.py`** -> AI Confidence: **99.39%**
2. **`src/textual/_arrange.py`** -> AI Confidence: **99.31%**
3. **`src/textual/_border.py`** -> AI Confidence: **99.31%**
4. **`src/textual/_import_app.py`** -> AI Confidence: **99.31%**
5. **`src/textual/_segment_tools.py`** -> AI Confidence: **99.31%**
6. **`src/textual/_styles_cache.py`** -> AI Confidence: **99.31%**
7. **`src/textual/_wrap.py`** -> AI Confidence: **99.31%**
8. **`src/textual/_xterm_parser.py`** -> AI Confidence: **99.31%**
9. **`src/textual/content.py`** -> AI Confidence: **99.31%**
10. **`src/textual/css/_styles_builder.py`** -> AI Confidence: **99.31%**
11. **`src/textual/css/parse.py`** -> AI Confidence: **99.31%**
12. **`src/textual/css/styles.py`** -> AI Confidence: **99.31%**
13. **`src/textual/css/stylesheet.py`** -> AI Confidence: **99.31%**
14. **`src/textual/design.py`** -> AI Confidence: **99.31%**
15. **`src/textual/layouts/grid.py`** -> AI Confidence: **99.31%**
16. **`src/textual/layouts/horizontal.py`** -> AI Confidence: **99.31%**
17. **`src/textual/layouts/vertical.py`** -> AI Confidence: **99.31%**
18. **`src/textual/markup.py`** -> AI Confidence: **99.31%**
19. **`src/textual/reactive.py`** -> AI Confidence: **99.31%**
20. **`src/textual/screen.py`** -> AI Confidence: **99.31%**
21. **`src/textual/strip.py`** -> AI Confidence: **99.31%**
22. **`src/textual/style.py`** -> AI Confidence: **99.31%**
23. **`src/textual/walk.py`** -> AI Confidence: **99.31%**
24. **`src/textual/widget.py`** -> AI Confidence: **99.31%**
25. **`src/textual/widgets/_data_table.py`** -> AI Confidence: **99.31%**
26. **`src/textual/widgets/_masked_input.py`** -> AI Confidence: **99.31%**
27. **`src/textual/widgets/_text_area.py`** -> AI Confidence: **99.31%**
28. **`src/textual/demo/_project_data.py`** -> AI Confidence: **99.29%**
29. **`src/textual/demo/data.py`** -> AI Confidence: **99.29%**
30. **`src/textual/_animator.py`** -> AI Confidence: **99.24%**
31. **`src/textual/canvas.py`** -> AI Confidence: **99.24%**
32. **`src/textual/color.py`** -> AI Confidence: **99.24%**
33. **`src/textual/css/_style_properties.py`** -> AI Confidence: **99.24%**
34. **`src/textual/css/query.py`** -> AI Confidence: **99.24%**
35. **`src/textual/css/tokenizer.py`** -> AI Confidence: **99.24%**
36. **`src/textual/fuzzy.py`** -> AI Confidence: **99.24%**
37. **`src/textual/highlight.py`** -> AI Confidence: **99.24%**
38. **`src/textual/message_pump.py`** -> AI Confidence: **99.24%**
39. **`src/textual/renderables/sparkline.py`** -> AI Confidence: **99.24%**
40. **`src/textual/scrollbar.py`** -> AI Confidence: **99.24%**
41. **`src/textual/widgets/_directory_tree.py`** -> AI Confidence: **99.24%**
42. **`src/textual/widgets/_footer.py`** -> AI Confidence: **99.24%**
43. **`src/textual/widgets/_input.py`** -> AI Confidence: **99.24%**
44. **`src/textual/widgets/_list_view.py`** -> AI Confidence: **99.24%**
45. **`src/textual/widgets/_rich_log.py`** -> AI Confidence: **99.24%**
46. **`src/textual/widgets/_tree.py`** -> AI Confidence: **99.24%**
47. **`src/textual/binding.py`** -> AI Confidence: **99.23%**
48. **`src/textual/css/_help_text.py`** -> AI Confidence: **99.23%**
49. **`src/textual/css/tokenize.py`** -> AI Confidence: **99.23%**
50. **`src/textual/document/_wrapped_document.py`** -> AI Confidence: **99.23%**
51. **`src/textual/renderables/background_screen.py`** -> AI Confidence: **99.23%**
52. **`examples/code_browser.py`** -> AI Confidence: **99.18%**
53. **`examples/markdown.py`** -> AI Confidence: **99.18%**
54. **`src/textual/_slug.py`** -> AI Confidence: **99.18%**
55. **`src/textual/css/model.py`** -> AI Confidence: **99.18%**
56. **`src/textual/demo/page.py`** -> AI Confidence: **99.18%**
57. **`src/textual/document/_document.py`** -> AI Confidence: **99.18%**
58. **`src/textual/drivers/win32.py`** -> AI Confidence: **99.18%**
59. **`src/textual/getters.py`** -> AI Confidence: **99.18%**
60. **`src/textual/pilot.py`** -> AI Confidence: **99.18%**
61. **`src/textual/renderables/text_opacity.py`** -> AI Confidence: **99.18%**
62. **`src/textual/scroll_view.py`** -> AI Confidence: **99.18%**
63. **`src/textual/theme.py`** -> AI Confidence: **99.18%**
64. **`src/textual/timer.py`** -> AI Confidence: **99.18%**
65. **`src/textual/worker.py`** -> AI Confidence: **99.18%**
66. **`tests/test_gc.py`** -> AI Confidence: **99.18%**
67. **`src/textual/widgets/_key_panel.py`** -> AI Confidence: **99.18%**
68. **`src/textual/widgets/_selection_list.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tests/test_xterm_parser.py` -> **0.0005%** Exposure
### Exploit Generation Surface
- `examples/calculator.py` -> **100.0%** Exposure
- `examples/five_by_five.py` -> **100.0%** Exposure
- `examples/json_tree.py` -> **100.0%** Exposure
- `examples/merlin.py` -> **100.0%** Exposure
- `examples/theme_sandbox.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/textual/demo/game.py` -> **100.0%** Exposure
- `src/textual/dom.py` -> **100.0%** Exposure
- `tests/input/test_input_key_modification_actions.py` -> **100.0%** Exposure
- `tests/input/test_input_key_movement_actions.py` -> **100.0%** Exposure
- `tests/snapshot_tests/snapshot_apps/auto_grid_default_height.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `examples/calculator.py` -> **100.0%** Exposure
- `examples/code_browser.py` -> **100.0%** Exposure
- `examples/five_by_five.py` -> **100.0%** Exposure
- `examples/json_tree.py` -> **100.0%** Exposure
- `examples/merlin.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3789` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/textual/demo/game.py` (PYTHON) -> Cumulative Risk: **918.83**
- **Archetype:** `file_cluster_13` (Distance: 11.602 IQR)
- **Magnitude:** 389.62 | **LOC:** 590 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `get_tile` (Impact: 174.1), `compose` (Impact: 18.3), `watch_dimensions` (Impact: 14.2)

### 2. `src/textual/lazy.py` (PYTHON) -> Cumulative Risk: **867.78**
- **Archetype:** `file_cluster_4` (Distance: 13.316 IQR)
- **Magnitude:** 116.96 | **LOC:** 142 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_reveal` (Impact: 21.1), `mount_composed_widgets` (Impact: 7.6), `mount_composed_widgets` (Impact: 7.4)

### 3. `src/textual/widgets/_tabs.py` (PYTHON) -> Cumulative Risk: **851.59**
- **Archetype:** `file_cluster_13` (Distance: 12.958 IQR)
- **Magnitude:** 658.28 | **LOC:** 885 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_activate_tab` (Impact: 74.1), `hide` (Impact: 70.9), `get_tab` (Impact: 67.3)

### 4. `src/textual/widgets/_radio_set.py` (PYTHON) -> Cumulative Risk: **850.68**
- **Archetype:** `file_cluster_13` (Distance: 11.522 IQR)
- **Magnitude:** 171.3 | **LOC:** 316 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_on_radio_button_changed` (Impact: 32.4), `_on_mount` (Impact: 31.8), `pressed_index` (Impact: 10.8)

### 5. `src/textual/command.py` (PYTHON) -> Cumulative Risk: **848.96**
- **Archetype:** `file_cluster_13` (Distance: 13.074 IQR)
- **Magnitude:** 894.22 | **LOC:** 1277 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_watch__list_visible` (Impact: 290.5), `_provider_classes` (Impact: 48.1), `_search` (Impact: 31.7)

### 6. `src/textual/message_pump.py` (PYTHON) -> Cumulative Risk: **846.8**
- **Archetype:** `file_cluster_4` (Distance: 13.217 IQR)
- **Magnitude:** 1098.48 | **LOC:** 921 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_process_messages_loop` (Impact: 122.0), `post_message` (Impact: 75.5), `_dispatch_message` (Impact: 62.2)

### 7. `src/textual/worker.py` (PYTHON) -> Cumulative Risk: **846.69**
- **Archetype:** `file_cluster_4` (Distance: 13.378 IQR)
- **Magnitude:** 511.3 | **LOC:** 456 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `wait` (Impact: 109.3), `_run_threaded` (Impact: 37.1), `_run` (Impact: 27.3)

### 8. `src/textual/screen.py` (PYTHON) -> Cumulative Risk: **832.7**
- **Archetype:** `file_cluster_16` (Distance: 13.29 IQR)
- **Magnitude:** 2578.78 | **LOC:** 2234 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 97.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_forward_event` (Impact: 491.1), `_refresh_layout` (Impact: 158.1), `_handle_mouse_move` (Impact: 111.6)

### 9. `src/textual/demo/home.py` (PYTHON) -> Cumulative Risk: **826.49**
- **Archetype:** `file_cluster_4` (Distance: 11.08 IQR)
- **Magnitude:** 124.1 | **LOC:** 264 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `compose` (Impact: 26.6), `get_stars` (Impact: 25.2), `compose` (Impact: 22.3)

### 10. `src/textual/widgets/_list_view.py` (PYTHON) -> Cumulative Risk: **821.78**
- **Archetype:** `file_cluster_13` (Distance: 12.357 IQR)
- **Magnitude:** 523.7 | **LOC:** 397 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `pop` (Impact: 122.6), `remove_items` (Impact: 68.1), `watch_index` (Impact: 55.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/textual/widget.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.553 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.233 IQR)
- **Top Global Matches:** file_cluster_16: 13.553, file_cluster_13: 13.65, file_cluster_0: 13.741
- **Magnitude:** 4105.2 | **LOC:** 4955 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 96.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (33.4798%), Tech Debt (19.0199%)
**Top Internal Functions/Classes:**
  * `get_child_by_type` (Impact: 2779.0 | O(N^6) | DB: 52)
  * `_compose` (Impact: 310.5 | O(N^5) | DB: 10)
  * `_check_refresh` (Impact: 92.6 | O(N^6) | DB: 4)
  * `__await__` (Impact: 61.4 | O(2^N))
  * `check_message_enabled` (Impact: 42.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 622`, `structural_boundaries: 715`, `args: 288`, `func_start: 269`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 285`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 205`, `concurrency: 82`, `import: 63`
* *Defense:* `safety: 102`, `doc: 530`, `test: 11`, `sync_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.701
  * `Choke Point (Betweenness):` 0.030929 | `Ripple Effect (Closeness):` 0.374686
  * `Imports (Out-Degree: 40):` textual._arrange, typing, textual.app, textual.cache, rich.text, textual.strip, textual._animator, textual._debug...
  * `Imported By (In-Degree: 99):` (Excluded from Brief to save tokens)

### `src/textual/dom.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.937 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.865 IQR)
- **Top Global Matches:** file_cluster_13: 12.937, file_cluster_16: 12.952, file_cluster_0: 13.075
- **Magnitude:** 2842.96 | **LOC:** 1917 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 95.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (20.021%), Tech Debt (9.9146%)
**Top Internal Functions/Classes:**
  * `check_identifiers` (Impact: 2615.5 | O(2^N) | DB: 40)
    * *Intent:* """Validate identifier and raise an error if it fails. Args: description: Description of where ident...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 363`, `args: 112`, `func_start: 112`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 108`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 96`, `concurrency: 3`, `import: 56`
* *Defense:* `safety: 52`, `doc: 212`, `test: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.325
  * `Choke Point (Betweenness):` 0.016845 | `Ripple Effect (Closeness):` 0.352951
  * `Imports (Out-Degree: 28):` textual.timer, typing, textual.app, textual.css.types, textual.cache, rich.text, textual.css.tokenize, textual.css.parse...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `src/textual/screen.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.29 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.514 IQR)
- **Top Global Matches:** file_cluster_16: 13.29, file_cluster_13: 13.306, file_cluster_8: 13.52
- **Magnitude:** 2578.78 | **LOC:** 2234 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 97.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (35.8961%), Tech Debt (17.5922%)
**Top Internal Functions/Classes:**
  * `_forward_event` (Impact: 491.1 | O(2^N) | DB: 11)
  * `_refresh_layout` (Impact: 158.1 | O(N^6) | DB: 1)
  * `_handle_mouse_move` (Impact: 111.6 | O(N^6) | DB: 2)
  * `arrange` (Impact: 92.2 | O(2^N) | DB: 1)
    * *Intent:* """Get currently active bindings for this screen. If no widget is focused, then app-level bindings a...
  * `focus_chain` (Impact: 87.7 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 309`, `args: 98`, `func_start: 98`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 200`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 82`, `concurrency: 45`, `import: 44`
* *Defense:* `safety: 57`, `doc: 248`, `test: 2`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.598
  * `Choke Point (Betweenness):` 0.012456 | `Ripple Effect (Closeness):` 0.352663
  * `Imports (Out-Degree: 32):` textual._arrange, textual.timer, typing, textual.app, textual._callback, textual.css.parse, textual._path, textual.selection...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `tests/snapshot_tests/test_snapshots.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.544 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.663 IQR)
- **Top Global Matches:** file_cluster_16: 13.544, file_cluster_7: 13.672, file_cluster_4: 13.733
- **Magnitude:** 2247.16 | **LOC:** 4874 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 92.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (6.122%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_app_resize_order` (Impact: 400.5 | O(N^6) | DB: 5)
  * `test_richlog_shrink` (Impact: 32.7 | O(N^4) | DB: 12)
    * *Intent:* # Perform the write in compose - it'll be deferred until the size is known
  * `test_background_tint` (Impact: 23.0 | O(N^4))
  * `test_fr_and_margin` (Impact: 22.7 | O(N^4))
  * `test_input_selection` (Impact: 21.6 | O(N^5) | DB: 1)
    * *Intent:* """When the input is smaller than its content, the start of the content should be visible, not the e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 1214`, `args: 571`, `func_start: 571`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`, `planned_debt: 2`, `fragile_debt: 4`, `orphaned_logic: 225`
* *Architecture:* `io: 5`, `api: 705`, `concurrency: 193`, `import: 26`
* *Defense:* `safety: 343`, `doc: 532`, `test: 698`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` textual.app, rich.text, textual.binding, textual._on, textual.color, pathlib, textual.theme, textual.content...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_text_area.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.218 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.83 IQR)
- **Top Global Matches:** file_cluster_16: 12.218, file_cluster_13: 12.349, file_cluster_8: 12.423
- **Magnitude:** 2098.62 | **LOC:** 2656 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 88.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (22.8746%), Tech Debt (30.2704%)
**Top Internal Functions/Classes:**
  * `_render_line` (Impact: 447.6 | O(N^6))
  * `_set_document` (Impact: 135.9 | O(N^6) | DB: 5)
    * *Intent:* # Record the location of a matching closing/opening bracket.
  * `render_line` (Impact: 106.0 | O(N^6) | DB: 1)
  * `_redo_batch` (Impact: 49.5 | O(N^4))
  * `_undo_batch` (Impact: 49.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 320`, `args: 133`, `func_start: 133`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 142`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 150`, `concurrency: 18`, `import: 37`
* *Defense:* `safety: 21`, `doc: 328`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.735
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.012823
  * `Imports (Out-Degree: 22):` tree_sitter, typing, textual.cache, textual.document._history, rich.text, textual.strip, textual._cells, textual.binding...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_data_table.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.342 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.028 IQR)
- **Top Global Matches:** file_cluster_16: 12.342, file_cluster_13: 12.499, file_cluster_7: 12.572
- **Magnitude:** 2022.1 | **LOC:** 2865 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (15.4629%), Tech Debt (98.0586%)
**Top Internal Functions/Classes:**
  * `_update_dimensions` (Impact: 120.3 | O(N^6) | DB: 8)
  * `action_page_down` (Impact: 84.3 | O(2^N))
  * `action_page_up` (Impact: 84.3 | O(2^N))
  * `_compute_row_renderables` (Impact: 64.6 | O(N^5))
    * *Intent:* # Update pre-existing rows to account for the new column.
  * `_on_click` (Impact: 53.7 | O(N^4) | DB: 1)
    * *Intent:* """Auxiliary method to compute styles used to render a given cell. Args: is_header_cell: Is this a c...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 322`, `args: 133`, `func_start: 133`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 242`, `planned_debt: 2`, `duplicate_logic: 28`
* *Architecture:* `api: 136`, `concurrency: 2`, `import: 30`
* *Defense:* `safety: 23`, `doc: 352`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.797
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004488
  * `Imports (Out-Degree: 16):` typing, textual.cache, rich.text, textual.strip, itertools, textual.binding, rich.console, rich.segment...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_markdown.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.433 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.485 IQR)
- **Top Global Matches:** file_cluster_4: 13.433, file_cluster_16: 13.562, file_cluster_13: 13.595
- **Magnitude:** 1691.42 | **LOC:** 1669 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 77.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (49.9337%), Tech Debt (98.3048%)
**Top Internal Functions/Classes:**
  * `go` (Impact: 398.9 | O(N^6) | DB: 42)
  * `_parse_markdown` (Impact: 192.0 | O(N^6) | DB: 4)
  * `append` (Impact: 112.2 | O(N^6) | DB: 2)
  * `update` (Impact: 87.9 | O(N^6) | DB: 9)
  * `rebuild_table_of_contents` (Impact: 26.8 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 275`, `args: 93`, `func_start: 93`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 177`, `duplicate_logic: 22`
* *Architecture:* `io: 1`, `api: 105`, `concurrency: 276`, `import: 29`
* *Defense:* `safety: 30`, `doc: 246`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.276
  * `Choke Point (Betweenness):` 0.000518 | `Ripple Effect (Closeness):` 0.008415
  * `Imports (Out-Degree: 17):` typing, textual.app, weakref, textual.highlight, rich.text, textual.events, contextlib, pathlib...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/textual/content.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.845 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_16: 11.845, file_cluster_13: 11.924, file_cluster_8: 12.038
- **Magnitude:** 1679.74 | **LOC:** 1834 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 92.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (13.7512%), Tech Debt (41.9645%)
**Top Internal Functions/Classes:**
  * `join` (Impact: 208.7 | O(2^N))
  * `to_strip` (Impact: 112.6 | O(N^6) | DB: 2)
  * `_divide_spans` (Impact: 107.5 | O(N^6) | DB: 3)
  * `__getitem__` (Impact: 81.0 | O(N^6))
  * `markup` (Impact: 70.5 | O(2^N))
    * *Intent:* """ self._text: str = ( _strip_control_codes(text) if strip_control_codes and text else text ) self....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 268`, `args: 75`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 101`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 81`, `import: 27`
* *Defense:* `safety: 38`, `doc: 132`, `test: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.153
  * `Choke Point (Betweenness):` 0.00772 | `Ripple Effect (Closeness):` 0.35123
  * `Imports (Out-Degree: 12):` typing, textual.css.types, textual.cache, rich.text, textual.strip, rich.terminal_theme, textual._cells, textual.selection...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `src/textual/css/_styles_builder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.652 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.139 IQR)
- **Top Global Matches:** file_cluster_16: 10.652, file_cluster_8: 10.714, file_cluster_13: 11.012
- **Magnitude:** 1646.68 | **LOC:** 1317 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (16.1289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process_transition` (Impact: 820.1 | O(N^6) | DB: 4)
  * `process_color` (Impact: 100.2 | O(N^6))
  * `_parse_border` (Impact: 85.9 | O(N^6))
  * `process_keyline` (Impact: 78.9 | O(N^6))
  * `add_declaration` (Impact: 49.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 162`, `args: 79`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 25`
* *Architecture:* `api: 91`, `import: 22`
* *Defense:* `safety: 46`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.978
  * `Choke Point (Betweenness):` 0.002857 | `Ripple Effect (Closeness):` 0.207998
  * `Imports (Out-Degree: 19):` typing, textual.css.types, textual.css.tokenize, textual._cells, textual.css._error_tools, textual.geometry, textual._border, textual.color...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/textual/app.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.365 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.488 IQR)
- **Top Global Matches:** file_cluster_13: 12.365, file_cluster_16: 12.458, file_cluster_8: 12.466
- **Magnitude:** 1498.9 | **LOC:** 4986 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 93.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (11.8562%), Tech Debt (29.4314%)
**Top Internal Functions/Classes:**
  * `get_driver_class` (Impact: 202.1 | O(N^6) | DB: 2)
    * *Intent:* """The widget that is focused on the currently active screen, or `None`. Focused widgets receive key...
  * `__init_subclass__` (Impact: 126.8 | O(2^N))
    * *Intent:* """The original stderr stream (before redirection etc)."""
  * `_print` (Impact: 60.9 | O(N^4))
    * *Intent:* """Get the inline height (height when in inline mode). Returns: Height in lines. """
  * `_on_css_change` (Impact: 57.7 | O(N^6))
  * `get_system_commands` (Impact: 49.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 422`, `args: 112`, `func_start: 105`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 117`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 10`
* *Architecture:* `io: 10`, `api: 121`, `concurrency: 90`, `import: 98`
* *Defense:* `safety: 48`, `doc: 624`, `test: 4`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 74.901
  * `Choke Point (Betweenness):` 0.088167 | `Ripple Effect (Closeness):` 0.503511
  * `Imports (Out-Degree: 51):` typing, weakref, textual.features, textual._files, rich.console, rich.segment, textual.system_commands, textual.content...
  * `Imported By (In-Degree: 374):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_tree.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.28 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.515 IQR)
- **Top Global Matches:** file_cluster_16: 12.28, file_cluster_13: 12.506, file_cluster_0: 12.585
- **Magnitude:** 1435.1 | **LOC:** 1601 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (28.1929%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `_render_line` (Impact: 263.1 | O(N^6) | DB: 5)
  * `add_json` (Impact: 64.8 | O(N^6))
  * `_build` (Impact: 64.7 | O(N^5) | DB: 4)
  * `action_toggle_expand_all` (Impact: 53.1 | O(N^5))
  * `watch_cursor_line` (Impact: 46.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 233`, `args: 111`, `func_start: 111`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 105`, `duplicate_logic: 18`
* *Architecture:* `api: 122`, `concurrency: 10`, `import: 19`
* *Defense:* `safety: 33`, `doc: 228`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.328
  * `Choke Point (Betweenness):` 0.001628 | `Ripple Effect (Closeness):` 0.191325
  * `Imports (Out-Degree: 11):` typing, textual.cache, rich.text, textual.strip, textual.binding, textual.geometry, dataclasses, textual.reactive...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/textual/css/_style_properties.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.974 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.499 IQR)
- **Top Global Matches:** file_cluster_16: 11.974, file_cluster_13: 12.113, file_cluster_8: 12.221
- **Magnitude:** 1286.74 | **LOC:** 1259 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (23.4783%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__set__` (Impact: 669.5 | O(2^N) | DB: 6)
  * `__set__` (Impact: 107.3 | O(N^6))
  * `__set__` (Impact: 57.1 | O(N^6))
  * `__set__` (Impact: 41.4 | O(N^4))
  * `__set__` (Impact: 40.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 219`, `args: 73`, `func_start: 73`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 49`, `duplicate_logic: 52`
* *Architecture:* `api: 32`, `import: 26`
* *Defense:* `safety: 48`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.9
  * `Choke Point (Betweenness):` 0.002768 | `Ripple Effect (Closeness):` 0.210635
  * `Imports (Out-Degree: 18):` typing, textual.css.types, textual._cells, textual.geometry, textual.css._error_tools, textual._border, textual.color, textual.layout...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_tabbed_content.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.272 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.759 IQR)
- **Top Global Matches:** file_cluster_4: 12.272, file_cluster_16: 12.615, file_cluster_8: 12.686
- **Magnitude:** 1214.18 | **LOC:** 917 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.8249%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tabbed_content_initial` (Impact: 126.8 | O(N^5) | DB: 1)
  * `test_disabling_nested_tabs` (Impact: 121.6 | O(N^6))
  * `test_tabbed_content_add_after_pane` (Impact: 109.0 | O(N^4))
  * `test_tabbed_content_switch_via_ui` (Impact: 77.0 | O(N^5))
    * *Intent:* """Check tab navigation via the user interface."""
  * `test_disabling_via_tabbed_content` (Impact: 56.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 396`, `args: 98`, `func_start: 98`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`, `orphaned_logic: 23`
* *Architecture:* `api: 138`, `concurrency: 175`, `import: 6`
* *Defense:* `safety: 143`, `doc: 18`, `test: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pytest, textual.app, textual.widgets._tabbed_content, textual.reactive, __future__, textual.widgets
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_data_table.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.455 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.94 IQR)
- **Top Global Matches:** file_cluster_4: 12.455, file_cluster_8: 12.569, file_cluster_13: 12.892
- **Magnitude:** 1144.74 | **LOC:** 1492 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (22.63%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scrolling_cursor_into_view` (Impact: 109.8 | O(N^4) | DB: 3)
  * `test_column_cursor_highlight_events` (Impact: 13.8 | O(N^3))
  * `test_row_cursor_highlight_events` (Impact: 13.7 | O(N^3))
  * `test_remove_row` (Impact: 12.6 | O(N^3))
  * `test_get_column` (Impact: 12.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 456`, `args: 91`, `func_start: 91`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 23`, `orphaned_logic: 66`
* *Architecture:* `api: 92`, `concurrency: 298`, `import: 12`
* *Defense:* `safety: 245`, `doc: 46`, `test: 345`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` pytest, textual.widgets.data_table, textual.app, textual.coordinate, rich.text, __future__, rich.panel, textual._wait...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/strip.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.266 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.682 IQR)
- **Top Global Matches:** file_cluster_16: 11.266, file_cluster_13: 11.318, file_cluster_0: 11.594
- **Magnitude:** 1112.34 | **LOC:** 818 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (19.8244%), Tech Debt (19.5417%)
**Top Internal Functions/Classes:**
  * `join` (Impact: 122.1 | O(2^N))
  * `crop` (Impact: 121.5 | O(N^6) | DB: 1)
    * *Intent:* """Simplify the segments (join segments with same style). Returns: New strip. """
  * `render_ansi` (Impact: 111.6 | O(2^N) | DB: 6)
  * `render` (Impact: 73.6 | O(2^N) | DB: 1)
  * `text_align` (Impact: 71.7 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 135`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 67`, `duplicate_logic: 2`
* *Architecture:* `api: 51`, `import: 15`
* *Defense:* `safety: 5`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.578
  * `Choke Point (Betweenness):` 0.001016 | `Ripple Effect (Closeness):` 0.273599
  * `Imports (Out-Degree: 6):` textual.color, typing, textual.css.types, rich.cells, textual.filter, textual.cache, rich.color, rich.measure...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/textual/message_pump.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.217 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.16 IQR)
- **Top Global Matches:** file_cluster_4: 13.217, file_cluster_13: 13.238, file_cluster_16: 13.349
- **Magnitude:** 1098.48 | **LOC:** 921 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.7418%), Tech Debt (17.6272%)
**Top Internal Functions/Classes:**
  * `_process_messages_loop` (Impact: 122.0 | O(N^6) | DB: 3)
  * `post_message` (Impact: 75.5 | O(N^5) | DB: 1)
  * `_dispatch_message` (Impact: 62.2 | O(N^6))
  * `_close_messages` (Impact: 58.3 | O(N^5) | DB: 2)
    * *Intent:* *,
  * `_process_messages` (Impact: 57.1 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 233`, `args: 54`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 83`, `duplicate_logic: 2`
* *Architecture:* `api: 43`, `concurrency: 151`, `import: 31`
* *Defense:* `safety: 63`, `doc: 96`, `test: 3`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.595
  * `Choke Point (Betweenness):` 0.00431 | `Ripple Effect (Closeness):` 0.280892
  * `Imports (Out-Degree: 16):` textual.timer, typing, textual.app, weakref, textual._callback, threading, time, textual._on...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/textual/command.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.074 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.474 IQR)
- **Top Global Matches:** file_cluster_13: 13.074, file_cluster_16: 13.219, file_cluster_4: 13.297
- **Magnitude:** 894.22 | **LOC:** 1277 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (45.6762%), Tech Debt (99.9974%)
**Top Internal Functions/Classes:**
  * `_watch__list_visible` (Impact: 290.5 | O(N^6) | DB: 11)
  * `_provider_classes` (Impact: 48.1 | O(N^5))
  * `_search` (Impact: 31.7 | O(N^5))
  * `search` (Impact: 31.7 | O(N^5) | DB: 1)
  * `compose` (Impact: 26.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 198`, `args: 63`, `func_start: 63`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 101`, `planned_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `api: 44`, `concurrency: 68`, `import: 35`
* *Defense:* `safety: 38`, `doc: 204`, `test: 6`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.168
  * `Choke Point (Betweenness):` 0.007497 | `Ripple Effect (Closeness):` 0.3126
  * `Imports (Out-Degree: 17):` abc, typing, textual.timer, textual.app, rich.text, rich.traceback, time, rich.align...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_option_list.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.248 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.728 IQR)
- **Top Global Matches:** file_cluster_16: 12.248, file_cluster_13: 12.352, file_cluster_0: 12.616
- **Magnitude:** 853.98 | **LOC:** 1040 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (24.8405%), Tech Debt (82.9997%)
**Top Internal Functions/Classes:**
  * `add_options` (Impact: 288.6 | O(2^N) | DB: 3)
  * `_update_lines` (Impact: 58.7 | O(N^5) | DB: 2)
  * `render_line` (Impact: 36.3 | O(N^4) | DB: 2)
  * `get_content_height` (Impact: 28.7 | O(N^4))
  * `_get_option_render` (Impact: 26.1 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 170`, `args: 65`, `func_start: 65`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 71`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 71`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 22`, `doc: 154`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.729
  * `Choke Point (Betweenness):` 0.002673 | `Ripple Effect (Closeness):` 0.180231
  * `Imports (Out-Degree: 11):` typing_extensions, typing, dataclasses, textual, textual._loop, textual.cache, textual.css.styles, textual.scroll_view...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tests/test_widget.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.629 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.017 IQR)
- **Top Global Matches:** file_cluster_4: 12.629, file_cluster_13: 12.928, file_cluster_16: 13.181
- **Magnitude:** 836.28 | **LOC:** 769 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (28.7194%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parent` (Impact: 255.6 | O(2^N) | DB: 4)
  * `test_get_common_ancestor` (Impact: 59.4 | O(N^6))
  * `test_sort_children` (Impact: 58.6 | O(N^4))
  * `test_of_type` (Impact: 17.1 | O(N^4))
  * `test_mount_error_bad_widget` (Impact: 12.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 284`, `args: 75`, `func_start: 75`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 37`, `orphaned_logic: 18`
* *Architecture:* `api: 98`, `concurrency: 177`, `import: 20`
* *Defense:* `safety: 98`, `doc: 22`, `test: 155`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` pytest, textual.geometry, textual.widgets, textual.app, textual._node_list, textual, textual.content, textual.css.query...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_tabbed_content.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.662 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.679 IQR)
- **Top Global Matches:** file_cluster_13: 12.662, file_cluster_16: 12.719, file_cluster_0: 12.911
- **Magnitude:** 801.46 | **LOC:** 717 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (37.4676%), Tech Debt (30.5091%)
**Top Internal Functions/Classes:**
  * `get_content_tab` (Impact: 652.1 | O(2^N) | DB: 16)
  * `_on_tab_pane_enabled` (Impact: 13.4 | O(N^4))
  * `sans_prefix` (Impact: 10.8 | O(N^3))
  * `add_prefix` (Impact: 8.0 | O(N^2))
  * `disable_tab` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 121`, `args: 44`, `func_start: 44`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 37`, `duplicate_logic: 2`
* *Architecture:* `api: 39`, `concurrency: 20`, `import: 17`
* *Defense:* `safety: 25`, `doc: 124`, `test: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.187
  * `Choke Point (Betweenness):` 0.004185 | `Ripple Effect (Closeness):` 0.007013
  * `Imports (Out-Degree: 9):` typing_extensions, typing, dataclasses, textual.app, textual, textual.widgets._tabs, textual.content, textual.reactive...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/textual/geometry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.171 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.345 IQR)
- **Top Global Matches:** file_cluster_16: 11.171, file_cluster_0: 11.443, file_cluster_7: 11.64
- **Magnitude:** 773.28 | **LOC:** 1488 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (24.255%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `unpack` (Impact: 142.5 | O(N^6) | DB: 5)
    * *Intent:* """ # Unrolled because this method is used a lot x1, y1, w1, h1 = self cx1, cy1, w2, h2 = region x2 ...
  * `intersection` (Impact: 45.0 | O(N^2))
  * `clamp` (Impact: 28.9 | O(N^3))
  * `overlaps` (Impact: 28.2 | O(N^3))
  * `__contains__` (Impact: 26.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 238`, `args: 96`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 114`, `import: 9`
* *Defense:* `safety: 20`, `doc: 206`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.397675
  * `Imports (Out-Degree: 0):` os, typing_extensions, typing, textual_speedups, functools, __future__, rich.repr, operator...
  * `Imported By (In-Degree: 80):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_masked_input.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.509 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.002 IQR)
- **Top Global Matches:** file_cluster_16: 11.509, file_cluster_13: 11.566, file_cluster_8: 11.654
- **Magnitude:** 753.36 | **LOC:** 708 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (17.9451%), Tech Debt (46.7596%)
**Top Internal Functions/Classes:**
  * `insert_text_at_cursor` (Impact: 99.3 | O(N^6))
  * `delete_at_position` (Impact: 40.3 | O(N^4))
  * `render_line` (Impact: 36.4 | O(N^4))
  * `check` (Impact: 35.5 | O(N^4))
  * `action_delete_left_word` (Impact: 35.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 104`, `args: 36`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 63`, `duplicate_logic: 4`
* *Architecture:* `api: 47`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 4`, `doc: 98`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004208
  * `Imports (Out-Degree: 4):` typing_extensions, typing, dataclasses, re, textual, enum, textual.validation, textual.widgets._input...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/textual/style.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.683 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.75 IQR)
- **Top Global Matches:** file_cluster_16: 9.683, file_cluster_13: 9.723, file_cluster_8: 9.739
- **Magnitude:** 737.8 | **LOC:** 538 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.8941%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `style_definition` (Impact: 208.2 | O(N^6))
  * `__add__` (Impact: 185.3 | O(N^5))
  * `markup_tag` (Impact: 147.0 | O(N^5))
  * `rich_style` (Impact: 32.9 | O(N^3))
  * `rich_style_with_offset` (Impact: 29.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 79`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3`
* *Architecture:* `api: 31`, `import: 13`
* *Defense:* `safety: 10`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.399
  * `Choke Point (Betweenness):` 0.011181 | `Ripple Effect (Closeness):` 0.311248
  * `Imports (Out-Degree: 4):` textual._context, textual.color, dataclasses, typing, textual.markup, textual.css.styles, functools, rich.terminal_theme...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `tests/test_reactive.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.468 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.342 IQR)
- **Top Global Matches:** file_cluster_4: 13.468, file_cluster_16: 13.674, file_cluster_13: 13.871
- **Magnitude:** 726.48 | **LOC:** 843 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (23.1278%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_public_and_private_validate_order` (Impact: 21.0 | O(N^4))
  * `test_watch_async_init_true` (Impact: 16.4 | O(N^4) | DB: 2)
  * `test_watch_compute` (Impact: 13.7 | O(N^3) | DB: 2)
  * `test_compute` (Impact: 13.4 | O(N^3) | DB: 1)
  * `test_watch_async_init_false` (Impact: 13.3 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 289`, `args: 98`, `func_start: 98`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 77`, `duplicate_logic: 2`, `orphaned_logic: 29`
* *Architecture:* `api: 131`, `concurrency: 183`, `import: 8`
* *Defense:* `safety: 95`, `doc: 48`, `test: 129`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pytest, textual.app, textual.reactive, textual.message_pump, __future__, asyncio, textual.widget, textual.message
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_select.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.608 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.681 IQR)
- **Top Global Matches:** file_cluster_13: 12.608, file_cluster_16: 12.633, file_cluster_0: 12.942
- **Magnitude:** 719.6 | **LOC:** 717 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (32.8494%), Tech Debt (28.7861%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 478.4 | O(2^N) | DB: 26)
  * `_find_search_match` (Impact: 35.8 | O(N^4))
  * `_on_key` (Impact: 22.5 | O(N^4))
  * `watch_has_focus` (Impact: 21.2 | O(2^N) | DB: 1)
  * `check_consume_key` (Impact: 12.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 102`, `args: 40`, `func_start: 40`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 74`, `duplicate_logic: 2`
* *Architecture:* `api: 37`, `concurrency: 1`, `import: 17`
* *Defense:* `safety: 13`, `doc: 120`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.384
  * `Choke Point (Betweenness):` 0.000252 | `Ripple Effect (Closeness):` 0.176837
  * `Imports (Out-Degree: 9):` typing_extensions, textual.timer, typing, dataclasses, textual.app, textual, rich.text, textual.reactive...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/test_on.py` (PYTHON) | Magnitude: 297.78 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 235, structural_boundaries: 133, api: 78, args: 59
- `tests/test_xterm_parser.py` (PYTHON) | Magnitude: 131.94 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, test: 106, structural_boundaries: 105, safety: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/textual/_win_sleep.py` (PYTHON) | Magnitude: 83.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 30, doc: 18, concurrency: 13
- `tests/command_palette/test_click_away.py` (PYTHON) | Magnitude: 23.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 11, api: 6, args: 4
- `src/textual/drivers/headless_driver.py` (PYTHON) | Magnitude: 47.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 22, doc: 14, api: 9
- `tests/test_path.py` (PYTHON) | Magnitude: 10.16 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 14, api: 6, class_start: 5
- `tests/notifications/test_notifications.py` (PYTHON) | Magnitude: 39.4 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 33, test: 22, safety: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/snapshot_tests/snapshot_apps/capture_print.py` (PYTHON) | Magnitude: 13.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, api: 5, args: 3
- `src/textual/widgets/_input.py` (PYTHON) | Magnitude: 314.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 604, state_mutation: 183, doc: 176, structural_boundaries: 171
- `tests/test_widget_visibility.py` (PYTHON) | Magnitude: 25.08 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, api: 7, generics: 6
- `src/textual/getters.py` (PYTHON) | Magnitude: 80.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 67, generics: 39, state_mutation: 27
- `tests/test_widget_child_moving.py` (PYTHON) | Magnitude: 223.74 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 60, concurrency: 43, test: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/tree/test_tree_expand_etc.py` (PYTHON) | Magnitude: 160.24 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 42, test: 27, branch: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/animations/test_loading_indicator_animation.py` (PYTHON) | Magnitude: 32.0 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, concurrency: 9, doc: 8
- `tests/css/test_help_text.py` (PYTHON) | Magnitude: 77.06 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 52, test: 48, safety: 32
- `src/textual/widgets/_link.py` (PYTHON) | Magnitude: 153.0 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, bitwise_ops: 16, structural_boundaries: 15, ui_framework: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/css/test_screen_css.py` (PYTHON) | Magnitude: 211.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 109, api: 51, concurrency: 50
- `tests/option_list/test_option_messages.py` (PYTHON) | Magnitude: 115.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 61, safety: 27, concurrency: 27
- `src/textual/_queue.py` (PYTHON) | Magnitude: 73.16 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 23, concurrency: 15, api: 13
- `tests/test_query.py` (PYTHON) | Magnitude: 257.2 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 267, structural_boundaries: 140, test: 108, safety: 82
- `tests/listview/test_inherit_listview.py` (PYTHON) | Magnitude: 66.24 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 29, doc: 14, concurrency: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/test_disabled.py` (PYTHON) | Magnitude: 156.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 33, branch: 20, doc: 20
- `src/textual/demo/widgets.py` (PYTHON) | Magnitude: 443.94 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 362, doc: 100, structural_boundaries: 85, lazy_evaluation: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/animations/test_disabling_animations.py` (PYTHON) | Magnitude: 71.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 36, test: 26, args: 20
- `tests/snapshot_tests/snapshot_apps/rules.py` (PYTHON) | Magnitude: 24.58 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, branch: 5, import: 3
- `tests/test_count_parameters.py` (PYTHON) | Magnitude: 30.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 28, test: 15, safety: 12
- `src/textual/_layout_resolve.py` (PYTHON) | Magnitude: 97.38 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, branch: 20, structural_boundaries: 16, comprehensions: 5
- `src/textual/constants.py` (PYTHON) | Magnitude: 23.22 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 50, indent_spaces: 29, structural_boundaries: 27, immutability_locks: 19

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/textual/widgets/_markdown.py` -> Churn: **56.71%** | Cog Load: 49.9337% | Debt: 98.3048%
- `src/textual/geometry.py` -> Churn: **54.11%** | Cog Load: 24.255% | Debt: 99.999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/textual/widget.py` -> **Will McGugan** (96.5% isolated ownership) | Magnitude: 4105.2
- `src/textual/dom.py` -> **Will McGugan** (95.2% isolated ownership) | Magnitude: 2842.96
- `src/textual/screen.py` -> **Will McGugan** (97.5% isolated ownership) | Magnitude: 2578.78
- `tests/snapshot_tests/test_snapshots.py` -> **Will McGugan** (92.0% isolated ownership) | Magnitude: 2247.16
- `src/textual/widgets/_text_area.py` -> **Will McGugan** (88.9% isolated ownership) | Magnitude: 2098.62

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/textual/app.py` -> **Severity: 3.312** (Bridge: 0.0882 * Flux: 37.563%)
- `src/textual/widget.py` -> **Severity: 2.581** (Bridge: 0.0309 * Flux: 83.4441%)
- `src/textual/dom.py` -> **Severity: 1.43** (Bridge: 0.0168 * Flux: 84.9133%)
- `src/textual/screen.py` -> **Severity: 1.215** (Bridge: 0.0125 * Flux: 97.5565%)
- `src/textual/command.py` -> **Severity: 0.74** (Bridge: 0.0075 * Flux: 98.7293%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/textual/_context.py` -> **Severity: 29.092** (Embedded: 0.3636 * Error Risk: 80.0%)
- `src/textual/_types.py` -> **Severity: 27.985** (Embedded: 0.3498 * Error Risk: 80.0%)
- `src/textual/css/errors.py` -> **Severity: 26.282** (Embedded: 0.3285 * Error Risk: 80.0%)
- `src/textual/_callback.py` -> **Severity: 26.143** (Embedded: 0.3268 * Error Risk: 80.0%)
- `src/textual/actions.py` -> **Severity: 26.134** (Embedded: 0.3267 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/textual/demo/widgets.py` -> **Severity: 4327.2** (Blast Radius: 43.272 * Doc Risk: 100.0%)
- `src/textual/geometry.py` -> **Severity: 3160.2** (Blast Radius: 31.602 * Doc Risk: 100.0%)
- `src/textual/message.py` -> **Severity: 2652.747** (Blast Radius: 29.81 * Doc Risk: 88.9885%)
- `src/textual/app.py` -> **Severity: 1647.567** (Blast Radius: 74.901 * Doc Risk: 21.9966%)
- `src/textual/reactive.py` -> **Severity: 1595.4** (Blast Radius: 15.954 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
