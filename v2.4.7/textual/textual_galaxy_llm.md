# ARCHITECTURAL_BRIEF: textual
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/textual` |
| **Timestamp** | `2026-08-07T04:04:13.002539+00:00` |
| **Scan Duration** | `3.66s` |
| **Git Branch** | `main` |
| **Git Commit** | `04b03c8db64266a6a7811cc161bae9986e53b1a1` |
| **Git Remote** | `https://github.com/Textualize/textual.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 687 malicious artifacts.

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
> **Architectural Drift Z-Score:** `4.975`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 362 | 50.7% |
| file_cluster_8 | 156 | 21.8% |
| file_cluster_4 | 86 | 12.0% |
| file_cluster_16 | 78 | 10.9% |
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
| Cognitive Load Exposure | 0.0 | 99.6 | 13.4 | 7.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 90.8 | 22.6 | 0.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.2 | 5.3 | 4.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 32.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 16.7 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 12.8 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
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

- `get_child_by_type` (@ `src/textual/widget.py`) -> Impact: **886.8** | LOC: 2597
- `check_identifiers` (@ `src/textual/dom.py`) -> Impact: **433.1** | LOC: 1388
  * *Intent:* """Validate identifier and raise an error if it fails. Args: description: Description of where identifier is used for error message. *names: Identifie...
- `process_transition` (@ `src/textual/css/_styles_builder.py`) -> Impact: **250.2** | LOC: 443
- `test_app_resize_order` (@ `tests/snapshot_tests/test_snapshots.py`) -> Impact: **149.3** | LOC: 977
- `_render_line` (@ `src/textual/widgets/_text_area.py`) -> Impact: **135.9** | LOC: 223
- `go` (@ `src/textual/widgets/_markdown.py`) -> Impact: **134.8** | LOC: 582
- `hex6` (@ `src/textual/color.py`) -> Impact: **126.5** | LOC: 313
  * *Intent:* """This color encoded in Rich's Color class. Returns: A color object as used by Rich. """
- `get_content_tab` (@ `src/textual/widgets/_tabbed_content.py`) -> Impact: **111.7** | LOC: 432
- `_compose` (@ `src/textual/widget.py`) -> Impact: **110.5** | LOC: 210
- `__set__` (@ `src/textual/css/_style_properties.py`) -> Impact: **105.5** | LOC: 230

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/textual` | 121 | 14338.36 | 21.35% | 26.58% |
| `tests` | 130 | 10995.52 | 12.6% | 0.0% |
| `src/textual/widgets` | 59 | 8645.97 | 17.07% | 34.47% |
| `src/textual/css` | 20 | 2333.74 | 17.05% | 18.82% |
| `tests/snapshot_tests` | 3 | 2037.12 | 3.95% | 0.0% |
| `tests/snapshot_tests/snapshot_apps` | 147 | 1573.56 | 4.86% | 0.0% |
| `tests/text_area` | 12 | 1452.04 | 21.48% | 0.0% |
| `examples` | 19 | 1114.93 | 15.55% | 0.0% |
| `src/textual/drivers` | 12 | 817.82 | 17.47% | 14.24% |
| `tests/css` | 15 | 808.86 | 6.47% | 0.0% |

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
- `tests/snapshot_tests/test_snapshots.py` -> **232** Orphaned Functions | **112** Duplicates
- `tests/test_reactive.py` -> **51** Orphaned Functions | **40** Duplicates
- `tests/test_geometry.py` -> **87** Orphaned Functions | **0** Duplicates
- `tests/test_data_table.py` -> **67** Orphaned Functions | **0** Duplicates
- `tests/test_tabbed_content.py` -> **25** Orphaned Functions | **30** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3789` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/textual/widgets/_markdown.py` (PYTHON) -> Cumulative Risk: **613.06**
- **Archetype:** `file_cluster_4` (Distance: 13.4 IQR)
- **Magnitude:** 1041.32 | **LOC:** 1669 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.7737%), Tech Debt (98.3048%)
- **Heaviest Functions:** `go` (Impact: 134.8), `_parse_markdown` (Impact: 57.8), `append` (Impact: 34.3)

### 2. `src/textual/demo/game.py` (PYTHON) -> Cumulative Risk: **611.9**
- **Archetype:** `file_cluster_13` (Distance: 11.602 IQR)
- **Magnitude:** 213.72 | **LOC:** 590 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.0268%), Tech Debt (94.4089%), Concurrency (87.6259%)
- **Heaviest Functions:** `get_tile` (Impact: 49.4), `compose` (Impact: 7.9), `watch_dimensions` (Impact: 7.2)

### 3. `src/textual/command.py` (PYTHON) -> Cumulative Risk: **609.93**
- **Archetype:** `file_cluster_13` (Distance: 13.074 IQR)
- **Magnitude:** 507.22 | **LOC:** 1277 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9974%), Concurrency (99.9081%), State Flux (98.7293%)
- **Heaviest Functions:** `_watch__list_visible` (Impact: 95.7), `_provider_classes` (Impact: 16.9), `_search` (Impact: 10.9)

### 4. `src/textual/dom.py` (PYTHON) -> Cumulative Risk: **602.5**
- **Archetype:** `file_cluster_13` (Distance: 12.919 IQR)
- **Magnitude:** 1060.86 | **LOC:** 1917 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 95.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.8884%), State Flux (83.884%), Verification (80.0%)
- **Heaviest Functions:** `check_identifiers` (Impact: 433.1), `rich_style` (Impact: 22.4), `css_identifier_styled` (Impact: 16.2)

### 5. `src/textual/widgets/_list_view.py` (PYTHON) -> Cumulative Risk: **597.41**
- **Archetype:** `file_cluster_13` (Distance: 12.359 IQR)
- **Magnitude:** 245.4 | **LOC:** 397 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.8534%), Tech Debt (98.7158%), Concurrency (96.6731%)
- **Heaviest Functions:** `remove_items` (Impact: 20.5), `watch_index` (Impact: 19.5), `pop` (Impact: 18.7)

### 6. `src/textual/widgets/_header.py` (PYTHON) -> Cumulative Risk: **580.85**
- **Archetype:** `file_cluster_13` (Distance: 12.097 IQR)
- **Magnitude:** 91.88 | **LOC:** 229 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5411%), Concurrency (97.1754%), Tech Debt (96.614%)
- **Heaviest Functions:** `compose` (Impact: 5.6), `screen_sub_title` (Impact: 5.6), `screen_title` (Impact: 5.5)

### 7. `src/textual/message_pump.py` (PYTHON) -> Cumulative Risk: **577.79**
- **Archetype:** `file_cluster_4` (Distance: 13.217 IQR)
- **Magnitude:** 598.28 | **LOC:** 921 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (97.0801%), Verification (80.0%)
- **Heaviest Functions:** `_process_messages_loop` (Impact: 37.0), `post_message` (Impact: 27.0), `_close_messages` (Impact: 20.2)

### 8. `src/textual/worker.py` (PYTHON) -> Cumulative Risk: **569.27**
- **Archetype:** `file_cluster_4` (Distance: 13.378 IQR)
- **Magnitude:** 311.8 | **LOC:** 456 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9933%), State Flux (99.9889%)
- **Heaviest Functions:** `wait` (Impact: 19.3), `_run_threaded` (Impact: 16.1), `_run_async` (Impact: 12.7)

### 9. `src/textual/driver.py` (PYTHON) -> Cumulative Risk: **569.11**
- **Archetype:** `file_cluster_13` (Distance: 11.915 IQR)
- **Magnitude:** 135.16 | **LOC:** 302 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (94.3037%), Concurrency (83.1226%)
- **Heaviest Functions:** `process_message` (Impact: 26.9), `save_file_thread` (Impact: 15.3), `no_automatic_restart` (Impact: 5.6)

### 10. `src/textual/widgets/_tree.py` (PYTHON) -> Cumulative Risk: **567.71**
- **Archetype:** `file_cluster_16` (Distance: 12.28 IQR)
- **Magnitude:** 782.0 | **LOC:** 1601 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (95.4759%), State Flux (91.1765%), Documentation (80.6367%)
- **Heaviest Functions:** `_render_line` (Impact: 79.4), `_build` (Impact: 23.1), `add_json` (Impact: 19.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/snapshot_tests/test_snapshots.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.526 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.617 IQR)
- **Top Global Matches:** file_cluster_16: 13.526, file_cluster_7: 13.651, file_cluster_13: 13.703
- **Magnitude:** 2010.96 | **LOC:** 4874 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 92.0%
- **Risk Profile:** Cognitive Load (5.3494%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_app_resize_order` (Impact: 149.3)
  * `test_richlog_shrink` (Impact: 19.7)
    * *Intent:* # Perform the write in compose - it'll be deferred until the size is known
  * `test_input_selection` (Impact: 11.2)
    * *Intent:* """When the input is smaller than its content, the start of the content should be visible, not the e...
  * `test_radio_set_is_scrollable` (Impact: 11.2)
  * `test_background_tint` (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 1214`, `args: 572`, `func_start: 571`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 26`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 112`, `orphaned_logic: 232`
* *Architecture:* `io: 5`, `api: 705`, `concurrency: 173`, `import: 26`
* *Defense:* `safety: 343`, `doc: 532`, `test: 698`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` textual.command, textual.color, asyncio, textual.screen, textual.content, textual._on, textual.binding, textual.pilot...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widget.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.554 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.233 IQR)
- **Top Global Matches:** file_cluster_16: 13.554, file_cluster_13: 13.651, file_cluster_0: 13.742
- **Magnitude:** 1783.5 | **LOC:** 4955 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 96.5%
- **Risk Profile:** Cognitive Load (33.4529%), Tech Debt (19.0199%)
**Top Internal Functions/Classes:**
  * `get_child_by_type` (Impact: 886.8)
  * `_compose` (Impact: 110.5)
  * `_check_refresh` (Impact: 27.7)
  * `_on_click` (Impact: 14.3)
  * `check_message_enabled` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 622`, `structural_boundaries: 715`, `args: 288`, `func_start: 269`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 285`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 205`, `concurrency: 82`, `import: 63`
* *Defense:* `safety: 102`, `doc: 530`, `test: 11`, `sync_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.701
  * `Choke Point (Betweenness):` 0.030929 | `Ripple Effect (Closeness):` 0.374686
  * `Imports (Out-Degree: 40):` textual.strip, textual.color, textual.css.query, textual.layout, fractions, textual.dom, textual.visual, asyncio...
  * `Imported By (In-Degree: 99):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_data_table.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.342 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.028 IQR)
- **Top Global Matches:** file_cluster_16: 12.342, file_cluster_13: 12.498, file_cluster_7: 12.572
- **Magnitude:** 1099.5 | **LOC:** 2865 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (15.4629%), Tech Debt (98.0586%)
**Top Internal Functions/Classes:**
  * `_update_dimensions` (Impact: 38.0)
  * `_compute_row_renderables` (Impact: 23.0)
    * *Intent:* # Update pre-existing rows to account for the new column.
  * `_on_click` (Impact: 22.5)
    * *Intent:* """Auxiliary method to compute styles used to render a given cell. Args: is_header_cell: Is this a c...
  * `_render_line` (Impact: 17.0)
  * `action_page_down` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 322`, `args: 133`, `func_start: 133`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 242`, `planned_debt: 2`, `duplicate_logic: 28`
* *Architecture:* `api: 136`, `concurrency: 2`, `import: 30`
* *Defense:* `safety: 23`, `doc: 352`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.797
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004488
  * `Imports (Out-Degree: 16):` textual.strip, textual.color, itertools, textual.geometry, typing_extensions, textual.message, textual.renderables.styled, textual._two_way_dict...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_text_area.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.218 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.83 IQR)
- **Top Global Matches:** file_cluster_16: 12.218, file_cluster_13: 12.349, file_cluster_8: 12.424
- **Magnitude:** 1081.22 | **LOC:** 2656 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (22.8914%), Tech Debt (30.2704%)
**Top Internal Functions/Classes:**
  * `_render_line` (Impact: 135.9)
  * `_set_document` (Impact: 40.9)
    * *Intent:* # Record the location of a matching closing/opening bracket.
  * `render_line` (Impact: 32.3)
  * `_redo_batch` (Impact: 21.0)
  * `_undo_batch` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 320`, `args: 133`, `func_start: 133`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 142`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 150`, `concurrency: 18`, `import: 37`
* *Defense:* `safety: 21`, `doc: 328`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.735
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.012823
  * `Imports (Out-Degree: 22):` textual._cells, textual.strip, textual.color, textual.document._wrapped_document, textual.document._document, textual.geometry, collections, typing_extensions...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/textual/screen.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.29 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.514 IQR)
- **Top Global Matches:** file_cluster_16: 13.29, file_cluster_13: 13.306, file_cluster_8: 13.52
- **Magnitude:** 1072.38 | **LOC:** 2234 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 97.5%
- **Risk Profile:** Cognitive Load (35.7644%), Tech Debt (17.5922%)
**Top Internal Functions/Classes:**
  * `_forward_event` (Impact: 75.4)
  * `_refresh_layout` (Impact: 48.1)
  * `_handle_mouse_move` (Impact: 33.6)
  * `focus_chain` (Impact: 27.0)
  * `_binding_chain` (Impact: 24.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 309`, `args: 98`, `func_start: 98`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 200`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 82`, `concurrency: 45`, `import: 44`
* *Defense:* `safety: 57`, `doc: 248`, `test: 2`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.598
  * `Choke Point (Betweenness):` 0.012456 | `Ripple Effect (Closeness):` 0.352663
  * `Imports (Out-Degree: 32):` textual._compositor, textual.command, textual.css.query, textual.layout, textual.dom, asyncio, textual._context, textual.keys...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `src/textual/dom.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.919 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.843 IQR)
- **Top Global Matches:** file_cluster_13: 12.919, file_cluster_16: 12.942, file_cluster_0: 13.049
- **Magnitude:** 1060.86 | **LOC:** 1917 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 95.2%
- **Risk Profile:** Cognitive Load (33.4206%), Tech Debt (96.8884%)
**Top Internal Functions/Classes:**
  * `check_identifiers` (Impact: 433.1)
    * *Intent:* """Validate identifier and raise an error if it fails. Args: description: Description of where ident...
  * `rich_style` (Impact: 22.4)
  * `css_identifier_styled` (Impact: 16.2)
  * `screen` (Impact: 14.7)
  * `css_tree` (Impact: 13.0)
    * *Intent:* """The ID of this node, or None if the node has no ID."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 363`, `args: 112`, `func_start: 112`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 106`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 15`
* *Architecture:* `api: 129`, `concurrency: 3`, `import: 56`
* *Defense:* `safety: 52`, `doc: 212`, `test: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.325
  * `Choke Point (Betweenness):` 0.016845 | `Ripple Effect (Closeness):` 0.352951
  * `Imports (Out-Degree: 28):` rich.tree, inspect, textual.css.constants, rich.highlighter, textual.color, textual.css.query, rich.columns, textual._context...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_markdown.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.4 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.475 IQR)
- **Top Global Matches:** file_cluster_4: 13.4, file_cluster_16: 13.523, file_cluster_13: 13.557
- **Magnitude:** 1041.32 | **LOC:** 1669 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (49.9206%), Tech Debt (98.3048%)
**Top Internal Functions/Classes:**
  * `go` (Impact: 134.8)
  * `_parse_markdown` (Impact: 57.8)
  * `append` (Impact: 34.3)
  * `await_append` (Impact: 34.3)
  * `update` (Impact: 27.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 275`, `args: 93`, `func_start: 93`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 177`, `duplicate_logic: 22`
* *Architecture:* `io: 1`, `api: 105`, `concurrency: 271`, `import: 29`
* *Defense:* `safety: 30`, `doc: 246`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.276
  * `Choke Point (Betweenness):` 0.000518 | `Ripple Effect (Closeness):` 0.008415
  * `Imports (Out-Degree: 17):` textual.widgets._label, textual.css.query, textual.layout, urllib.parse, asyncio, textual._slug, typing_extensions, textual.content...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tests/test_data_table.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.439 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.941 IQR)
- **Top Global Matches:** file_cluster_4: 12.439, file_cluster_8: 12.543, file_cluster_13: 12.874
- **Magnitude:** 848.14 | **LOC:** 1492 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.5323%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scrolling_cursor_into_view` (Impact: 52.8)
  * `test_datatable_message_emission` (Impact: 9.2)
  * `test_column_cursor_highlight_events` (Impact: 7.8)
  * `test_row_cursor_highlight_events` (Impact: 7.7)
  * `test_add_rows` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 456`, `args: 91`, `func_start: 91`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`, `orphaned_logic: 67`
* *Architecture:* `api: 92`, `concurrency: 298`, `import: 12`
* *Defense:* `safety: 245`, `doc: 46`, `test: 345`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` textual.actions, rich.panel, textual.message, textual._wait, textual.coordinate, rich.text, pytest, textual.widgets...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/app.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.36 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.474 IQR)
- **Top Global Matches:** file_cluster_13: 12.36, file_cluster_16: 12.453, file_cluster_8: 12.46
- **Magnitude:** 815.4 | **LOC:** 4986 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 93.0%
- **Risk Profile:** Cognitive Load (11.5681%), Tech Debt (29.4314%)
**Top Internal Functions/Classes:**
  * `get_driver_class` (Impact: 63.6)
    * *Intent:* """The widget that is focused on the currently active screen, or `None`. Focused widgets receive key...
  * `_print` (Impact: 24.9)
    * *Intent:* """Get the inline height (height when in inline mode). Returns: Height in lines. """
  * `get_system_commands` (Impact: 21.3)
  * `__init_subclass__` (Impact: 18.9)
    * *Intent:* """The original stderr stream (before redirection etc)."""
  * `_on_css_change` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 422`, `args: 113`, `func_start: 105`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 117`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 10`
* *Architecture:* `io: 10`, `api: 121`, `concurrency: 85`, `import: 98`
* *Defense:* `safety: 48`, `doc: 624`, `test: 4`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 74.901
  * `Choke Point (Betweenness):` 0.088167 | `Ripple Effect (Closeness):` 0.503511
  * `Imports (Out-Degree: 51):` textual._compositor, textual.visual, textual._context, gc, textual.await_complete, base64, textual.binding, textual.signal...
  * `Imported By (In-Degree: 374):` (Excluded from Brief to save tokens)

### `tests/test_tabbed_content.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.163 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.742 IQR)
- **Top Global Matches:** file_cluster_4: 12.163, file_cluster_16: 12.501, file_cluster_8: 12.551
- **Magnitude:** 803.68 | **LOC:** 917 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.2478%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tabbed_content_add_after_pane` (Impact: 49.0)
  * `test_tabbed_content_initial` (Impact: 46.9)
  * `test_disabling_nested_tabs` (Impact: 36.6)
  * `test_tabbed_content_switch_via_ui` (Impact: 29.1)
    * *Intent:* """Check tab navigation via the user interface."""
  * `test_disabling_via_tabbed_content` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 396`, `args: 98`, `func_start: 98`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `duplicate_logic: 30`, `orphaned_logic: 25`
* *Architecture:* `api: 138`, `concurrency: 175`, `import: 6`
* *Defense:* `safety: 143`, `doc: 18`, `test: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` textual.reactive, pytest, textual.widgets, textual.app, __future__, textual.widgets._tabbed_content
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_tree.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.28 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.516 IQR)
- **Top Global Matches:** file_cluster_16: 12.28, file_cluster_13: 12.506, file_cluster_0: 12.584
- **Magnitude:** 782.0 | **LOC:** 1601 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.1651%), Tech Debt (95.4759%)
**Top Internal Functions/Classes:**
  * `_render_line` (Impact: 79.4)
  * `_build` (Impact: 23.1)
  * `add_json` (Impact: 19.8)
  * `watch_cursor_line` (Impact: 19.4)
  * `action_toggle_expand_all` (Impact: 18.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 233`, `args: 111`, `func_start: 111`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 105`, `duplicate_logic: 20`
* *Architecture:* `api: 122`, `concurrency: 10`, `import: 19`
* *Defense:* `safety: 33`, `doc: 228`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.328
  * `Choke Point (Betweenness):` 0.001628 | `Ripple Effect (Closeness):` 0.191325
  * `Imports (Out-Degree: 11):` textual.strip, rich.highlighter, textual.geometry, typing_extensions, textual.message, textual.scroll_view, textual.binding, rich.repr...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/textual/content.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.821 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_16: 11.821, file_cluster_13: 11.901, file_cluster_8: 12.015
- **Magnitude:** 734.04 | **LOC:** 1834 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 92.0%
- **Risk Profile:** Cognitive Load (13.7512%), Tech Debt (41.9645%)
**Top Internal Functions/Classes:**
  * `to_strip` (Impact: 34.6)
  * `join` (Impact: 32.0)
  * `_divide_spans` (Impact: 28.5)
  * `__getitem__` (Impact: 24.7)
  * `expand_tabs` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 268`, `args: 75`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 101`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 81`, `import: 27`
* *Defense:* `safety: 38`, `doc: 132`, `test: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.153
  * `Choke Point (Betweenness):` 0.00772 | `Ripple Effect (Closeness):` 0.35123
  * `Imports (Out-Degree: 12):` rich._wrap, textual._cells, textual.strip, textual.color, textual.visual, textual._context, textual.css.types, typing_extensions...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `tests/test_reactive.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.162 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.439 IQR)
- **Top Global Matches:** file_cluster_4: 13.162, file_cluster_16: 13.362, file_cluster_13: 13.569
- **Magnitude:** 679.98 | **LOC:** 843 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.4994%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_public_and_private_validate_order` (Impact: 9.0)
  * `test_reactive_inheritance` (Impact: 8.2)
  * `test_watch_compute` (Impact: 7.7)
  * `test_compute` (Impact: 7.5)
  * `test_watch_async_init_false` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 289`, `args: 99`, `func_start: 98`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 49`, `duplicate_logic: 40`, `orphaned_logic: 51`
* *Architecture:* `api: 131`, `concurrency: 183`, `import: 8`
* *Defense:* `safety: 95`, `doc: 48`, `test: 129`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` textual.reactive, textual.message, textual.message_pump, pytest, textual.app, asyncio, __future__, textual.widget
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/css/_styles_builder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.65 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.139 IQR)
- **Top Global Matches:** file_cluster_16: 10.65, file_cluster_8: 10.712, file_cluster_13: 11.01
- **Magnitude:** 661.68 | **LOC:** 1317 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.1258%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process_transition` (Impact: 250.2)
  * `process_color` (Impact: 30.2)
  * `_parse_border` (Impact: 25.9)
  * `process_keyline` (Impact: 23.9)
  * `add_declaration` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 162`, `args: 79`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 25`
* *Architecture:* `api: 91`, `import: 22`
* *Defense:* `safety: 46`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.978
  * `Choke Point (Betweenness):` 0.002857 | `Ripple Effect (Closeness):` 0.207998
  * `Imports (Out-Degree: 19):` textual._cells, textual.css.constants, textual.css.transition, textual.color, textual.css.types, textual.css._help_text, textual.geometry, textual.layouts.factory...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/textual/message_pump.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.217 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.16 IQR)
- **Top Global Matches:** file_cluster_4: 13.217, file_cluster_13: 13.238, file_cluster_16: 13.349
- **Magnitude:** 598.28 | **LOC:** 921 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.7418%), Tech Debt (17.6272%)
**Top Internal Functions/Classes:**
  * `_process_messages_loop` (Impact: 37.0)
  * `post_message` (Impact: 27.0)
  * `_close_messages` (Impact: 20.2)
    * *Intent:* *,
  * `_dispatch_message` (Impact: 18.9)
  * `_on_message` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 233`, `args: 54`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 83`, `duplicate_logic: 2`
* *Architecture:* `api: 43`, `concurrency: 151`, `import: 31`
* *Defense:* `safety: 63`, `doc: 96`, `test: 3`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.595
  * `Choke Point (Betweenness):` 0.00431 | `Ripple Effect (Closeness):` 0.280892
  * `Imports (Out-Degree: 16):` asyncio, textual._context, textual.constants, textual._time, textual.timer, typing_extensions, textual.message, textual.css.model...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/test_widget.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.43 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.982 IQR)
- **Top Global Matches:** file_cluster_4: 12.43, file_cluster_13: 12.734, file_cluster_16: 12.987
- **Magnitude:** 543.38 | **LOC:** 769 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (32.1009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parent` (Impact: 61.6)
  * `test_sort_children` (Impact: 25.6)
  * `test_get_common_ancestor` (Impact: 19.4)
  * `compose` (Impact: 9.1)
  * `test_of_type` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 284`, `args: 75`, `func_start: 75`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`, `duplicate_logic: 16`, `orphaned_logic: 19`
* *Architecture:* `api: 98`, `concurrency: 177`, `import: 20`
* *Defense:* `safety: 98`, `doc: 22`, `test: 155`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` textual._node_list, textual.content, textual.message, textual.containers, textual.css.query, pytest, textual.widgets, textual.screen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/command.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.074 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.474 IQR)
- **Top Global Matches:** file_cluster_13: 13.074, file_cluster_16: 13.218, file_cluster_4: 13.296
- **Magnitude:** 507.22 | **LOC:** 1277 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.5536%), Tech Debt (99.9974%)
**Top Internal Functions/Classes:**
  * `_watch__list_visible` (Impact: 95.7)
  * `_provider_classes` (Impact: 16.9)
  * `_search` (Impact: 10.9)
  * `search` (Impact: 10.9)
  * `compose` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 198`, `args: 63`, `func_start: 63`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 101`, `planned_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `api: 44`, `concurrency: 68`, `import: 35`
* *Defense:* `safety: 38`, `doc: 204`, `test: 6`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.168
  * `Choke Point (Betweenness):` 0.007497 | `Ripple Effect (Closeness):` 0.3126
  * `Imports (Out-Degree: 17):` inspect, rich.traceback, textual.visual, asyncio, textual.timer, textual.screen, typing_extensions, textual.content...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/textual/geometry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.166 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.345 IQR)
- **Top Global Matches:** file_cluster_16: 11.166, file_cluster_0: 11.438, file_cluster_7: 11.635
- **Magnitude:** 458.98 | **LOC:** 1488 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.255%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `unpack` (Impact: 47.2)
    * *Intent:* """ # Unrolled because this method is used a lot x1, y1, w1, h1 = self cx1, cy1, w2, h2 = region x2 ...
  * `intersection` (Impact: 30.3)
  * `clamp` (Impact: 14.8)
  * `overlaps` (Impact: 14.3)
  * `clamped` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 238`, `args: 96`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 114`, `import: 9`
* *Defense:* `safety: 20`, `doc: 206`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.397675
  * `Imports (Out-Degree: 0):` typing_extensions, typing, functools, os, textual_speedups, __future__, textual.geometry, rich.repr...
  * `Imported By (In-Degree: 80):` (Excluded from Brief to save tokens)

### `src/textual/strip.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.265 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.682 IQR)
- **Top Global Matches:** file_cluster_16: 11.265, file_cluster_13: 11.318, file_cluster_0: 11.594
- **Magnitude:** 447.74 | **LOC:** 818 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.8244%), Tech Debt (19.5417%)
**Top Internal Functions/Classes:**
  * `crop` (Impact: 36.5)
    * *Intent:* """Simplify the segments (join segments with same style). Returns: New strip. """
  * `join` (Impact: 25.1)
  * `render_ansi` (Impact: 23.6)
  * `text_align` (Impact: 21.6)
  * `adjust_cell_length` (Impact: 20.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 135`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 67`, `duplicate_logic: 2`
* *Architecture:* `api: 51`, `import: 15`
* *Defense:* `safety: 5`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.578
  * `Choke Point (Betweenness):` 0.001016 | `Ripple Effect (Closeness):` 0.273599
  * `Imports (Out-Degree: 6):` textual._segment_tools, typing, functools, rich.color, textual.cache, textual.color, textual.filter, rich.measure...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `examples/dictionary.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.44 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.79 IQR)
- **Top Global Matches:** file_cluster_4: 13.44, file_cluster_13: 13.664, file_cluster_0: 14.08
- **Magnitude:** 443.85 | **LOC:** 76 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.8339%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 21`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 6`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` textual.containers, textual.widgets, textual.app, __future__, httpx, textual
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/css/_style_properties.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.974 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.499 IQR)
- **Top Global Matches:** file_cluster_16: 11.974, file_cluster_13: 12.112, file_cluster_8: 12.22
- **Magnitude:** 434.74 | **LOC:** 1259 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.4783%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__set__` (Impact: 105.5)
  * `__set__` (Impact: 32.4)
  * `__set__` (Impact: 17.4)
  * `__set__` (Impact: 17.1)
  * `__set__` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 219`, `args: 73`, `func_start: 73`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 49`, `duplicate_logic: 52`
* *Architecture:* `api: 32`, `import: 26`
* *Defense:* `safety: 48`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.9
  * `Choke Point (Betweenness):` 0.002768 | `Ripple Effect (Closeness):` 0.210635
  * `Imports (Out-Degree: 18):` textual._cells, textual.css.constants, textual.css.transition, textual.color, textual.layout, textual.dom, textual.css.types, textual.css._help_text...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_screens.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.368 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.186 IQR)
- **Top Global Matches:** file_cluster_4: 12.368, file_cluster_13: 12.707, file_cluster_0: 12.954
- **Magnitude:** 427.14 | **LOC:** 626 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.9426%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_screens` (Impact: 16.4)
  * `test_disallow_screen_instances` (Impact: 11.4)
  * `test_auto_focus_on_screen_if_app_auto_fo` (Impact: 10.3)
    * *Intent:* """Setting app.AUTO_FOCUS = `None` means it is not taken into consideration."""
  * `test_push_screen_wait_for_dismiss` (Impact: 7.8)
  * `test_installed_screens` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 238`, `args: 47`, `func_start: 47`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 19`, `duplicate_logic: 23`, `orphaned_logic: 18`
* *Architecture:* `io: 2`, `api: 84`, `concurrency: 149`, `import: 17`
* *Defense:* `safety: 86`, `doc: 24`, `test: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` textual.worker, textual.events, textual.containers, pytest, textual.widgets, textual.screen, asyncio, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_option_list.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.248 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.728 IQR)
- **Top Global Matches:** file_cluster_16: 12.248, file_cluster_13: 12.352, file_cluster_0: 12.616
- **Magnitude:** 409.28 | **LOC:** 1040 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (24.8405%), Tech Debt (82.9997%)
**Top Internal Functions/Classes:**
  * `add_options` (Impact: 54.8)
  * `_update_lines` (Impact: 20.6)
  * `render_line` (Impact: 15.6)
  * `get_content_height` (Impact: 11.9)
  * `_get_option_render` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 170`, `args: 65`, `func_start: 65`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 71`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 71`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 22`, `doc: 154`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.729
  * `Choke Point (Betweenness):` 0.002673 | `Ripple Effect (Closeness):` 0.180231
  * `Imports (Out-Degree: 11):` typing_extensions, typing, textual.reactive, dataclasses, textual._loop, textual.message, textual.cache, textual.strip...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_masked_input.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.509 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.002 IQR)
- **Top Global Matches:** file_cluster_16: 11.509, file_cluster_13: 11.566, file_cluster_8: 11.654
- **Magnitude:** 382.26 | **LOC:** 708 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.9451%), Tech Debt (46.7596%)
**Top Internal Functions/Classes:**
  * `insert_text_at_cursor` (Impact: 30.1)
  * `delete_at_position` (Impact: 16.9)
  * `render_line` (Impact: 15.7)
  * `action_delete_left_word` (Impact: 14.8)
  * `check` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 104`, `args: 36`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 63`, `duplicate_logic: 4`
* *Architecture:* `api: 47`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 4`, `doc: 98`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004208
  * `Imports (Out-Degree: 4):` typing_extensions, typing, textual.reactive, enum, dataclasses, textual.validation, textual.strip, rich.text...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_tabs.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.962 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.624 IQR)
- **Top Global Matches:** file_cluster_13: 12.962, file_cluster_16: 13.038, file_cluster_0: 13.207
- **Magnitude:** 356.48 | **LOC:** 885 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.1003%), Tech Debt (99.5128%)
**Top Internal Functions/Classes:**
  * `get_tab` (Impact: 28.3)
  * `hide` (Impact: 18.9)
  * `do_remove` (Impact: 16.9)
  * `_activate_tab` (Impact: 13.5)
  * `_move_tab` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 159`, `args: 54`, `func_start: 53`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`, `duplicate_logic: 14`
* *Architecture:* `api: 58`, `concurrency: 27`, `import: 21`
* *Defense:* `safety: 43`, `doc: 156`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.000201 | `Ripple Effect (Closeness):` 0.00816
  * `Imports (Out-Degree: 15):` textual.css.query, textual.visual, textual.geometry, textual.content, textual.await_complete, textual.message, textual.binding, textual.widget...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/test_on.py` (PYTHON) | Magnitude: 303.88 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 235, structural_boundaries: 133, api: 78, args: 59
- `tests/test_xterm_parser.py` (PYTHON) | Magnitude: 115.44 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, test: 106, structural_boundaries: 105, safety: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/textual/_win_sleep.py` (PYTHON) | Magnitude: 64.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 30, doc: 18, concurrency: 13
- `tests/command_palette/test_click_away.py` (PYTHON) | Magnitude: 20.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 11, api: 6, args: 4
- `src/textual/drivers/headless_driver.py` (PYTHON) | Magnitude: 30.8 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 22, doc: 14, api: 9
- `tests/test_path.py` (PYTHON) | Magnitude: 10.16 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 14, api: 6, class_start: 5
- `tests/notifications/test_notifications.py` (PYTHON) | Magnitude: 33.4 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 33, test: 22, safety: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/snapshot_tests/snapshot_apps/capture_print.py` (PYTHON) | Magnitude: 10.96 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, api: 5, args: 3
- `tests/test_widget_visibility.py` (PYTHON) | Magnitude: 26.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, api: 7, generics: 6
- `src/textual/widgets/_input.py` (PYTHON) | Magnitude: 297.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 604, state_mutation: 183, doc: 176, structural_boundaries: 171
- `src/textual/getters.py` (PYTHON) | Magnitude: 56.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 67, generics: 39, state_mutation: 27
- `tests/test_widget_child_moving.py` (PYTHON) | Magnitude: 152.94 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 60, concurrency: 43, test: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/tree/test_tree_expand_etc.py` (PYTHON) | Magnitude: 94.14 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 42, test: 27, branch: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/animations/test_loading_indicator_animation.py` (PYTHON) | Magnitude: 26.0 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, concurrency: 9, doc: 8
- `tests/css/test_help_text.py` (PYTHON) | Magnitude: 68.56 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 52, test: 48, safety: 32
- `src/textual/widgets/_link.py` (PYTHON) | Magnitude: 153.0 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, bitwise_ops: 16, structural_boundaries: 15, ui_framework: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/option_list/test_option_messages.py` (PYTHON) | Magnitude: 87.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 61, safety: 27, concurrency: 27
- `src/textual/_queue.py` (PYTHON) | Magnitude: 57.66 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 23, concurrency: 15, api: 13
- `tests/listview/test_inherit_listview.py` (PYTHON) | Magnitude: 48.04 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 29, doc: 14, concurrency: 11
- `src/textual/timer.py` (PYTHON) | Magnitude: 142.74 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, encapsulation: 70, structural_boundaries: 55, concurrency: 43
- `src/textual/message_pump.py` (PYTHON) | Magnitude: 598.28 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 541, encapsulation: 236, structural_boundaries: 233, concurrency: 151

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/test_disabled.py` (PYTHON) | Magnitude: 81.06 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 33, branch: 20, doc: 20
- `src/textual/demo/widgets.py` (PYTHON) | Magnitude: 158.14 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 362, doc: 100, structural_boundaries: 85, lazy_evaluation: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/animations/test_disabling_animations.py` (PYTHON) | Magnitude: 57.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 36, test: 26, args: 20
- `tests/snapshot_tests/snapshot_apps/rules.py` (PYTHON) | Magnitude: 11.58 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, branch: 5, import: 3
- `tests/test_count_parameters.py` (PYTHON) | Magnitude: 25.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 28, test: 15, safety: 12
- `src/textual/_layout_resolve.py` (PYTHON) | Magnitude: 42.78 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, branch: 20, structural_boundaries: 16, comprehensions: 5
- `src/textual/constants.py` (PYTHON) | Magnitude: 18.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 50, indent_spaces: 29, structural_boundaries: 27, immutability_locks: 19

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/textual/dom.py` -> Churn: **60.4%** | Cog Load: 33.4206% | Debt: 96.8884%
- `src/textual/geometry.py` -> Churn: **54.11%** | Cog Load: 24.255% | Debt: 99.999%
- `src/textual/widgets/_markdown.py` -> Churn: **51.21%** | Cog Load: 49.9206% | Debt: 98.3048%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/snapshot_tests/test_snapshots.py` -> **Will McGugan** (92.0% isolated ownership) | Magnitude: 2010.96
- `src/textual/widget.py` -> **Will McGugan** (96.5% isolated ownership) | Magnitude: 1783.5
- `src/textual/widgets/_data_table.py` -> **Will McGugan** (85.7% isolated ownership) | Magnitude: 1099.5
- `src/textual/widgets/_text_area.py` -> **Will McGugan** (88.9% isolated ownership) | Magnitude: 1081.22
- `src/textual/screen.py` -> **Will McGugan** (97.5% isolated ownership) | Magnitude: 1072.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/textual/app.py` -> **Severity: 3.312** (Bridge: 0.0882 * Flux: 37.563%)
- `src/textual/widget.py` -> **Severity: 2.581** (Bridge: 0.0309 * Flux: 83.4441%)
- `src/textual/dom.py` -> **Severity: 1.413** (Bridge: 0.0168 * Flux: 83.884%)
- `src/textual/screen.py` -> **Severity: 1.215** (Bridge: 0.0125 * Flux: 97.5565%)
- `src/textual/command.py` -> **Severity: 0.74** (Bridge: 0.0075 * Flux: 98.7293%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/textual/_types.py` -> **Severity: 31.751** (Embedded: 0.3498 * Error Risk: 90.7682%)
- `src/textual/_context.py` -> **Severity: 29.092** (Embedded: 0.3636 * Error Risk: 80.0%)
- `src/textual/css/errors.py` -> **Severity: 26.497** (Embedded: 0.3285 * Error Risk: 80.6551%)
- `src/textual/message.py` -> **Severity: 26.31** (Embedded: 0.3649 * Error Risk: 72.1075%)
- `src/textual/actions.py` -> **Severity: 26.134** (Embedded: 0.3267 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/textual/message.py` -> **Severity: 2328.236** (Blast Radius: 29.81 * Doc Risk: 78.1025%)
- `src/textual/dom.py` -> **Severity: 2308.064** (Blast Radius: 34.325 * Doc Risk: 67.2415%)
- `src/textual/geometry.py` -> **Severity: 2262.292** (Blast Radius: 31.602 * Doc Risk: 71.587%)
- `src/textual/style.py` -> **Severity: 1539.9** (Blast Radius: 15.399 * Doc Risk: 100.0%)
- `src/textual/demo/widgets.py` -> **Severity: 1528.847** (Blast Radius: 43.272 * Doc Risk: 35.3311%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
