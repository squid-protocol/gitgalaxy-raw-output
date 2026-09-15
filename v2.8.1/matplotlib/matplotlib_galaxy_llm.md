# ARCHITECTURAL_BRIEF: matplotlib
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 1405 |
| Analyzed Artifacts (Scanned) | 968 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 437 |
| Total LOC | 85364 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.9% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.547 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4202 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7772 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 41 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 605 | 24131 | 62.5% |
| CPP | 210 | 56491 | 21.7% |
| XML | 80 | 0 | 8.3% |
| PLAINTEXT | 43 | 0 | 4.4% |
| JSON | 8 | 2399 | 0.8% |
| HTML | 8 | 119 | 0.8% |
| MARKDOWN | 5 | 0 | 0.5% |
| YAML | 3 | 343 | 0.3% |
| MAKEFILE | 1 | 31 | 0.1% |
| CSS | 1 | 149 | 0.1% |
| BATCH | 1 | 55 | 0.1% |
| OBJECTIVE-C | 1 | 1617 | 0.1% |
| C | 1 | 16 | 0.1% |
| SHELL | 1 | 13 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.67; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 37%, Data / Markup / Trivial 18%, Interface Declarations Files 15%, Large Core Modules 12%, Parameter Forwarders Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 920 | 95.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 48 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 437*

**Composition by Extension & Reason:**
- `.rst`: 336x Excluded (Unsupported Extension: '.rst')
- `.png`: 53x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 90 LOC), 1x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `.build`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1412 LOC), 1x Excluded (Static Asset Blob without Intent: 1296 LOC)
- `.pdf`: 2x Excluded (Explicitly Denied Extension: '.pdf')
- `.cpp`: 1x Excluded (Embedded Hex Payload: 59106 hex tokens in 10427 LOC), 1x Excluded (Embedded Hex Payload: 4528 hex tokens in 676 LOC)
- `.wrap`: 2x Excluded (Unsupported Extension: '.wrap')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bib`: 1x Excluded (Unsupported Extension: '.bib')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 21.1 | 7.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 67.0 | 75.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 26.7 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 80.6 | 0.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 48.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 41.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8065 | 359 | 12 | `matplotlib-3.10.8/src/ft2font_wrapper.cpp` |
| cleanup | 164 | 49 | 0 | `matplotlib-3.10.8/src/_macosx.m` |
| guards | 4166 | 244 | 12 | `matplotlib-3.10.8/src/tri/_tri.cpp` |
| danger | 517 | 147 | 2 | `matplotlib-3.10.8/src/_macosx.m` |
| concurrency | 20 | 12 | 0 | `matplotlib-3.10.8/tools/boilerplate.py` |
| connectivity | 1886 | 385 | 5 | `matplotlib-3.10.8/src/_macosx.m` |
| io | 164 | 49 | 0 | `matplotlib-3.10.8/tools/gh_api.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 19 | 11 | 0 | `matplotlib-3.10.8/doc/conf.py` |
| time | 45 | 16 | 0 | `matplotlib-3.10.8/src/_macosx.m` |
| serialization | 2 | 2 | 0 | `matplotlib-3.10.8/tools/check_typehints.py` |
| regex | 15 | 8 | 0 | `matplotlib-3.10.8/doc/sphinxext/math_symbol_table.py` |
| events | 35 | 16 | 0 | `matplotlib-3.10.8/galleries/examples/user_interfaces/embedding_webagg_sgskip.py` |
| tests | 96 | 36 | 0 | `matplotlib-3.10.8/galleries/examples/showcase/pan_zoom_overlap.py` |
| docs | 971 | 610 | 2 | `matplotlib-3.10.8/galleries/examples/statistics/confidence_ellipse.py` |
| debt | 882 | 122 | 1 | `matplotlib-3.10.8/extern/agg24-svn/include/agg_pixfmt_rgba.h` |
| mutation | 34083 | 809 | 81 | `matplotlib-3.10.8/extern/agg24-svn/include/agg_blur.h` |
| dead_code | 1102 | 208 | 2 | `matplotlib-3.10.8/src/tri/_tri.cpp` |
| credential | 7 | 1 | 0 | `matplotlib-3.10.8/doc/_static/quiver_sizes.svg` |
| threat | 282 | 190 | 1 | `matplotlib-3.10.8/galleries/examples/units/basic_units.py` |
| ml_ai | 1513 | 583 | 4 | `matplotlib-3.10.8/galleries/examples/misc/custom_projection.py` |
| ui | 21 | 7 | 0 | `matplotlib-3.10.8/src/_macosx.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `matplotlib-3.10.8/tools/gh_api.py` (Hits: 20)
- `matplotlib-3.10.8/tools/visualize_tests.py` (Hits: 11)
- `matplotlib-3.10.8/doc/conf.py` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pyplot.py** (`matplotlib-3.10.8/galleries/tutorials/pyplot.py`) — 550 inbound connections
2. **agg_basics.h** (`matplotlib-3.10.8/extern/agg24-svn/include/agg_basics.h`) — 102 inbound connections
3. **agg_array.h** (`matplotlib-3.10.8/extern/agg24-svn/include/agg_array.h`) — 29 inbound connections
4. **colors.py** (`matplotlib-3.10.8/galleries/users_explain/colors/colors.py`) — 23 inbound connections
5. **agg_color_rgba.h** (`matplotlib-3.10.8/extern/agg24-svn/include/agg_color_rgba.h`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_backend_agg.h** (`matplotlib-3.10.8/src/_backend_agg.h`) — 33 outbound dependencies
2. **conf.py** (`matplotlib-3.10.8/doc/conf.py`) — 27 outbound dependencies
3. **embedding_webagg_sgskip.py** (`matplotlib-3.10.8/galleries/examples/user_interfaces/embedding_webagg_sgskip.py`) — 16 outbound dependencies
4. **agg_platform_support.cpp** (`matplotlib-3.10.8/extern/agg24-svn/src/platform/BeOS/agg_platform_support.cpp`) — 16 outbound dependencies
5. **agg_platform_support.cpp** (`matplotlib-3.10.8/extern/agg24-svn/src/platform/AmigaOS/agg_platform_support.cpp`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `platform_specific::put_image` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/platform/X11/agg_platform_support.cpp`) -> Impact: **449.5** | LOC: 221
  * *Intent:* //------------------------------------------------------------------------
- `platform_specific::load_pmap` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/platform/win32/agg_platform_support.cpp`) -> Impact: **387.4** | LOC: 267
  * *Intent:* //------------------------------------------------------------------------
- `markers` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_markers.h`) -> Impact: **213.4** | LOC: 26
  * *Intent:* //--------------------------------------------------------------------
- `window_proc` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/platform/win32/agg_platform_support.cpp`) -> Impact: **212.5** | LOC: 360
  * *Intent:* //------------------------------------------------------------------------
- `handle_idcmp` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/platform/AmigaOS/agg_platform_support.cpp`) -> Impact: **204.2** | LOC: 204
  * *Intent:* //------------------------------------------------------------------------
- `markers` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_markers.h`) -> Impact: **199.7** | LOC: 26
  * *Intent:* //--------------------------------------------------------------------
- `markers` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_markers.h`) -> Impact: **193.0** | LOC: 38
  * *Intent:* //--------------------------------------------------------------------
- `markers` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_markers.h`) -> Impact: **185.0** | LOC: 26
  * *Intent:* //--------------------------------------------------------------------
- `platform_support::load_img` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/platform/X11/agg_platform_support.cpp`) -> Impact: **168.7** | LOC: 221
  * *Intent:* //------------------------------------------------------------------------
- `curve4_div::recursive_bezier` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/agg_curves.cpp`) -> Impact: **165.5** | LOC: 210
  * *Intent:* //------------------------------------------------------------------------

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `matplotlib-3.10.8/extern/agg24-svn/include` | 127 | 28568.7 | 41.94% | 33.35% |
| `matplotlib-3.10.8/src` | 26 | 6442.62 | 34.98% | 22.69% |
| `matplotlib-3.10.8/extern/agg24-svn/src` | 27 | 3255.0 | 56.38% | 69.0% |
| `matplotlib-3.10.8/extern/agg24-svn/src/ctrl` | 9 | 2750.42 | 81.31% | 93.07% |
| `matplotlib-3.10.8/extern/agg24-svn/src/platform/win32` | 2 | 1870.32 | 85.75% | 72.91% |
| `matplotlib-3.10.8/src/tri` | 3 | 1710.4 | 35.23% | 50.25% |
| `matplotlib-3.10.8/extern/agg24-svn/src/platform/X11` | 1 | 1509.86 | 100.0% | 48.6% |
| `matplotlib-3.10.8/galleries/examples/text_labels_and_annotations` | 47 | 1381.58 | 11.66% | 0.0% |
| `matplotlib-3.10.8/galleries/examples/images_contours_and_fields` | 48 | 1330.86 | 9.28% | 0.0% |
| `matplotlib-3.10.8/galleries/examples/misc` | 31 | 1305.92 | 20.44% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_curves.h` -> **100.0%** Exposure
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_rasterizer_sl_clip.h` -> **100.0%** Exposure
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_rendering_buffer.h` -> **100.0%** Exposure
- `matplotlib-3.10.8/extern/agg24-svn/include/ctrl/agg_bezier_ctrl.h` -> **100.0%** Exposure
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_color_gray.h` -> **99.9997%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `matplotlib-3.10.8/ci/schemas/vendor_schemas.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/doc/conf.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/doc/sphinxext/github.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/doc/sphinxext/math_symbol_table.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/doc/sphinxext/missing_references.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `matplotlib-3.10.8/src/tri/_tri.cpp` -> **100** Orphaned Functions | **0** Duplicates
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_pixfmt_rgba.h` -> **0** Orphaned Functions | **70** Duplicates
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_pixfmt_rgb_packed.h` -> **18** Orphaned Functions | **42** Duplicates
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_color_rgba.h` -> **0** Orphaned Functions | **58** Duplicates
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_curves.h` -> **0** Orphaned Functions | **57** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2507` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `matplotlib-3.10.8/extern/agg24-svn/include/agg_array.h` (CPP) -> Cumulative Risk: **766.68**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.74)
- **Magnitude:** 648.98 | **LOC:** 1120 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.999%), State Flux (99.998%)
- **Heaviest Functions:** `quick_sort` (Compute Cores, Impact: 46.7), `binary_search_pos` (Many-Argument Workhorses, Impact: 15.2), `deserialize` (Many-Argument Workhorses, Impact: 13.4)

### 2. `matplotlib-3.10.8/extern/agg24-svn/include/agg_color_rgba.h` (CPP) -> Cumulative Risk: **753.02**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.28)
- **Magnitude:** 876.8 | **LOC:** 1354 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.9994%)
- **Heaviest Functions:** `rgba::from_wavelength` (Compute Cores, Impact: 38.5), `add` (Compute Cores, Impact: 17.1), `add` (Compute Cores, Impact: 17.1)

### 3. `matplotlib-3.10.8/extern/agg24-svn/include/agg_basics.h` (CPP) -> Cumulative Risk: **745.12**
- **Archetype:** `file_cluster_13` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.73)
- **Magnitude:** 249.74 | **LOC:** 561 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.7365%)
- **Heaviest Functions:** `intersect_rectangles` (Compute Cores, Impact: 9.5), `unite_rectangles` (Compute Cores, Impact: 9.2), `clip` (Compute Cores, Impact: 8.9)

### 4. `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_scanline.h` (CPP) -> Cumulative Risk: **732.48**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.14)
- **Magnitude:** 639.34 | **LOC:** 853 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (91.9602%)
- **Heaviest Functions:** `render_scanlines_compound` (Many-Argument Workhorses, Impact: 104.5), `render_scanlines_compound_layered` (Many-Argument Workhorses, Impact: 82.6), `render_scanlines_aa_solid` (Many-Argument Workhorses, Impact: 20.3)

### 5. `matplotlib-3.10.8/extern/agg24-svn/src/platform/sdl/agg_platform_support.cpp` (CPP) -> Cumulative Risk: **730.22**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.59)
- **Magnitude:** 591.66 | **LOC:** 709 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `platform_specific::platform_specific` (Many-Argument Workhorses, Impact: 65.7), `platform_support::run` (Compute Cores, Impact: 64.0), `platform_support::init` (Many-Argument Workhorses, Impact: 21.6)

### 6. `matplotlib-3.10.8/extern/agg24-svn/src/ctrl/agg_cbox_ctrl.cpp` (CPP) -> Cumulative Risk: **726.72**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.05)
- **Magnitude:** 200.18 | **LOC:** 215 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.5485%)
- **Heaviest Functions:** `cbox_ctrl_impl::vertex` (Compute Cores, Impact: 33.3), `cbox_ctrl_impl::rewind` (Compute Cores, Impact: 15.9), `cbox_ctrl_impl::on_mouse_button_down` (Compute Cores, Impact: 9.2)

### 7. `matplotlib-3.10.8/extern/agg24-svn/src/ctrl/agg_gamma_ctrl.cpp` (CPP) -> Cumulative Risk: **723.36**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.74)
- **Magnitude:** 452.94 | **LOC:** 434 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `gamma_ctrl_impl::vertex` (Compute Cores, Impact: 53.1), `gamma_ctrl_impl::rewind` (Compute Cores, Impact: 36.0), `gamma_ctrl_impl::on_arrow_keys` (Many-Argument Workhorses, Impact: 28.1)

### 8. `matplotlib-3.10.8/extern/agg24-svn/include/agg_scanline_storage_aa.h` (CPP) -> Cumulative Risk: **720.11**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.11)
- **Magnitude:** 415.82 | **LOC:** 816 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9891%), Tech Debt (98.8799%)
- **Heaviest Functions:** `sweep_scanline` (Compute Cores, Impact: 14.6), `sweep_scanline` (Compute Cores, Impact: 14.4), `render` (Compute Cores, Impact: 13.0)

### 9. `matplotlib-3.10.8/extern/agg24-svn/src/ctrl/agg_rbox_ctrl.cpp` (CPP) -> Cumulative Risk: **719.93**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.66)
- **Magnitude:** 288.26 | **LOC:** 326 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `rbox_ctrl_impl::vertex` (Compute Cores, Impact: 56.3), `rbox_ctrl_impl::rewind` (Compute Cores, Impact: 23.5), `rbox_ctrl_impl::on_arrow_keys` (Many-Argument Workhorses, Impact: 19.2)

### 10. `matplotlib-3.10.8/extern/agg24-svn/include/agg_image_accessors.h` (CPP) -> Cumulative Risk: **719.78**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.06)
- **Magnitude:** 305.3 | **LOC:** 482 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Tech Debt (99.5601%)
- **Heaviest Functions:** `span` (Type Conversions, Impact: 10.6), `span` (Type Conversions, Impact: 10.6), `pixel` (I/O & Config Routines, Impact: 5.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_markers.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2202.2 | **LOC:** 707 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1639%), Tech Debt (9.5531%)
**Top Internal Functions/Classes:**
  * `markers` **(Compute Cores)** (Impact: 213.4)
    * *Intent:* //--------------------------------------------------------------------
  * `markers` **(Compute Cores)** (Impact: 199.7)
    * *Intent:* //--------------------------------------------------------------------
  * `markers` **(Compute Cores)** (Impact: 193.0)
    * *Intent:* //--------------------------------------------------------------------
  * `markers` **(Compute Cores)** (Impact: 185.0)
    * *Intent:* //--------------------------------------------------------------------
  * `marker` **(Compute Cores)** (Impact: 86.2)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 359 instances
* *State Mutation (weighted view):* 1077
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 46`, `args: 97`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 359`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` agg_basics.h, agg_renderer_primitives.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_blur.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1704.06 | **LOC:** 1504 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.5695%), Tech Debt (9.8726%)
**Top Internal Functions/Classes:**
  * `stack_blur_rgba32` **(Many-Argument Workhorses)** (Impact: 60.4)
    * *Intent:* //=======================================================stack_blur_rgba32
  * `stack_blur_rgb24` **(Many-Argument Workhorses)** (Impact: 58.5)
    * *Intent:* //========================================================stack_blur_rgb24
  * `stack_blur_gray8` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* //========================================================stack_blur_gray8
  * `blur_x` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* //--------------------------------------------------------------------
  * `blur` **(Compute Cores)** (Impact: 26.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 360 instances
* *State Mutation (weighted view):* 1315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 210`, `args: 36`, `func_start: 49`, `class_start: 10`
* *Risk/State:* `state_mutation: 595`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` agg_array.h, agg_pixfmt_base.h, agg_pixfmt_transposer.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_outline_aa.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1688.34 | **LOC:** 1838 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.8541%), Tech Debt (63.6418%)
**Top Internal Functions/Classes:**
  * `line_interpolator_aa3` **(Many-Argument Workhorses)** (Impact: 69.8)
    * *Intent:* //---------------------------------------------------------------------
  * `line_interpolator_aa1` **(Many-Argument Workhorses)** (Impact: 59.8)
    * *Intent:* //---------------------------------------------------------------------
  * `line3` **(Many-Argument Workhorses)** (Impact: 32.1)
    * *Intent:* //-------------------------------------------------------------------------
  * `pie_hline` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* //-------------------------------------------------------------------------
  * `line1` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* //-------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 312 instances
* *State Mutation (weighted view):* 1019
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 168`, `args: 41`, `func_start: 115`, `class_start: 12`
* *Risk/State:* `state_mutation: 395`, `duplicate_logic: 18`
* *Architecture:* `api: 23`, `import: 8`
* *Defense:* `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.984
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.001034
  * `Imports (Out-Degree: 8):` agg_array.h, agg_clip_liang_barsky.h, agg_dda_line.h, agg_ellipse_bresenham.h, agg_gamma_functions.h, agg_line_aa_basics.h, agg_math.h, agg_renderer_base.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/src/tri/_tri.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1668.68 | **LOC:** 2072 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.1935%), Tech Debt (97.4681%)
**Top Internal Functions/Classes:**
  * `TrapezoidMapTriFinder::add_edge_to_tree` **(Compute Cores)** (Impact: 85.7)
  * `TrapezoidMapTriFinder::Node::search` **(Compute Cores)** (Impact: 59.1)
  * `TriContourGenerator::follow_boundary` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `Triangulation::Triangulation` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `TriContourGenerator::follow_interior` **(Many-Argument Workhorses)** (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 160`, `args: 102`, `func_start: 116`
* *Risk/State:* `state_mutation: 219`, `unreferenced_by_name: 100`
* *Architecture:* `import: 5`
* *Defense:* `safety: 88`, `immutability_locks: 155`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mplutils.h, _tri.h, algorithm, random, set
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/src/platform/X11/agg_platform_support.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1509.86 | **LOC:** 1602 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (48.5981%)
**Top Internal Functions/Classes:**
  * `platform_specific::put_image` **(Compute Cores)** (Impact: 449.5)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::load_img` **(Compute Cores)** (Impact: 168.7)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::save_img` **(Compute Cores)** (Impact: 130.8)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::init` **(Many-Argument Workhorses)** (Impact: 110.8)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::run` **(Compute Cores)** (Impact: 95.0)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 106 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 395
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 50`, `args: 19`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 183`, `dead_code: 9`, `unreferenced_by_name: 30`
* *Architecture:* `io: 6`, `api: 1`, `import: 15`
* *Defense:* `immutability_locks: 14`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Xatom.h, Xlib.h, Xutil.h, keysym.h, agg_basics.h, agg_pixfmt_gray.h, agg_pixfmt_rgb.h, agg_pixfmt_rgba.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_pixfmt_rgba.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1500.38 | **LOC:** 2802 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.7655%), Tech Debt (99.5135%)
**Top Internal Functions/Classes:**
  * `blend_hline` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_vline` **(Many-Argument Workhorses)** (Impact: 33.7)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_color_hspan` **(Many-Argument Workhorses)** (Impact: 31.0)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_color_vspan` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_from` **(Many-Argument Workhorses)** (Impact: 27.7)
    * *Intent:* //-------------------------------------------------------------------- // Blend from another RGBA su...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 147 instances
* *State Mutation (weighted view):* 567
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 830`, `args: 92`, `func_start: 165`, `class_start: 50`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 273`, `dead_code: 5`, `duplicate_logic: 70`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.348
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.00698
  * `Imports (Out-Degree: 2):` agg_pixfmt_base.h, agg_rendering_buffer.h, math.h, string.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/src/platform/win32/agg_platform_support.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1436.42 | **LOC:** 1656 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (61.3509%)
**Top Internal Functions/Classes:**
  * `platform_specific::load_pmap` **(Many-Argument Workhorses)** (Impact: 387.4)
    * *Intent:* //------------------------------------------------------------------------
  * `window_proc` **(Many-Argument Workhorses)** (Impact: 212.5)
    * *Intent:* //------------------------------------------------------------------------
  * `convert_pmap` **(Many-Argument Workhorses)** (Impact: 134.6)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_specific::platform_specific` **(Many-Argument Workhorses)** (Impact: 93.3)
    * *Intent:* //------------------------------------------------------------------------
  * `tokenizer::next_token` **(I/O & Config Routines)** (Impact: 40.4)
    * *Intent:* //-----------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 456`, `structural_boundaries: 63`, `args: 52`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 174`, `dead_code: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` agg_pixfmt_gray.h, agg_pixfmt_rgb.h, agg_pixfmt_rgba.h, agg_platform_support.h, agg_win32_bmp.h, string.h, agg_color_conv.h, agg_color_conv_rgb16.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/src/_macosx.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1119.94 | **LOC:** 1915 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.8524%), Tech Debt (8.2623%)
**Top Internal Functions/Classes:**
  * `convertKeyEvent` **(Compute Cores)** (Impact: 83.4)
  * `FigureCanvas_set_cursor` **(Compute Cores)** (Impact: 23.7)
  * `flagsChanged` **(Compute Cores)** (Impact: 21.0)
    * *Intent:* // flagsChanged gets called whenever a modifier key is pressed OR released // so we need to handle b...
  * `FigureCanvas_init` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `Timer__timer_start` **(Compute Cores)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 108 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 392
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 162`, `args: 130`, `func_start: 141`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 11`, `state_mutation: 176`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 54`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 2`, `immutability_locks: 30`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ApplicationServices.h, Cocoa.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_scanline_boolean_algebra.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1042.74 | **LOC:** 1568 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.4676%), Tech Debt (19.8395%)
**Top Internal Functions/Classes:**
  * `sbool_unite_shapes` **(Many-Argument Workhorses)** (Impact: 81.3)
    * *Intent:* //----------------------------------------------------sbool_unite_shapes // Unite the scanline shape...
  * `sbool_unite_scanlines` **(Many-Argument Workhorses)** (Impact: 77.1)
    * *Intent:* //-------------------------------------------------sbool_unite_scanlines // Unite two scanlines, "sl...
  * `sbool_combine_shapes_aa` **(Many-Argument Workhorses)** (Impact: 46.4)
    * *Intent:* //-----------------------------------------------sbool_combine_shapes_aa
  * `sbool_intersect_shapes` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* //------------------------------------------------sbool_intersect_shapes // Intersect the scanline s...
  * `sbool_combine_shapes_bin` **(C Struct Operations)** (Impact: 40.7)
    * *Intent:* //----------------------------------------------sbool_combine_shapes_bin
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 260`, `args: 20`, `func_start: 30`, `class_start: 104`
* *Risk/State:* `state_mutation: 159`, `unreferenced_by_name: 11`
* *Architecture:* `import: 3`
* *Defense:* `immutability_locks: 38`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` agg_basics.h, math.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/src/_path.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1024.68 | **LOC:** 1249 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.4347%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `point_in_path_impl` **(Many-Argument Workhorses)** (Impact: 72.5)
    * *Intent:* // Related work by Samosky is in: // // Samosky, Joseph, "SectionView: A system for interactively sp...
  * `segments_intersect` **(Many-Argument Workhorses)** (Impact: 62.2)
  * `clip_path_to_rect` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `point_in_path_collection` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `__convert_to_string` **(Many-Argument Workhorses)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 433
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 190`, `args: 51`, `func_start: 44`, `class_start: 8`
* *Risk/State:* `state_mutation: 167`, `dead_code: 4`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.623
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.001034
  * `Imports (Out-Degree: 7):` _backend_agg_basic_types.h, agg_conv_contour.h, agg_conv_curve.h, agg_conv_stroke.h, agg_conv_transform.h, agg_trans_affine.h, algorithm, cmath...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_span_image_filter_rgba.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 950.28 | **LOC:** 891 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.8753%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate` **(Many-Argument Workhorses)** (Impact: 83.6)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 42.4)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 42.4)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 149 instances
* *State Mutation (weighted view):* 655
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 127`, `func_start: 23`, `class_start: 7`
* *Risk/State:* `state_mutation: 357`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.609
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.003232
  * `Imports (Out-Degree: 3):` agg_basics.h, agg_color_rgba.h, agg_span_image_filter.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_outline_image.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 920.1 | **LOC:** 1037 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7519%), Tech Debt (25.0197%)
**Top Internal Functions/Classes:**
  * `line_interpolator_image` **(Many-Argument Workhorses)** (Impact: 101.5)
    * *Intent:* //---------------------------------------------------------------------
  * `line3` **(Many-Argument Workhorses)** (Impact: 32.3)
    * *Intent:* //-------------------------------------------------------------------------
  * `step_hor` **(I/O & Config Routines)** (Impact: 19.1)
    * *Intent:* //---------------------------------------------------------------------
  * `step_ver` **(I/O & Config Routines)** (Impact: 19.1)
    * *Intent:* //---------------------------------------------------------------------
  * `pixel` **(Compute Cores)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 165 instances
* *State Mutation (weighted view):* 565
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 109`, `args: 21`, `func_start: 70`, `class_start: 6`
* *Risk/State:* `state_mutation: 235`, `unreferenced_by_name: 11`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `immutability_locks: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` agg_array.h, agg_clip_liang_barsky.h, agg_dda_line.h, agg_line_aa_basics.h, agg_math.h, agg_rendering_buffer.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_color_rgba.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 876.8 | **LOC:** 1354 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1452%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `rgba::from_wavelength` **(Compute Cores)** (Impact: 38.5)
    * *Intent:* //------------------------------------------------------------------------
  * `add` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* //--------------------------------------------------------------------
  * `add` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* //--------------------------------------------------------------------
  * `add` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* //--------------------------------------------------------------------
  * `premultiply` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 206`, `args: 40`, `func_start: 141`, `class_start: 12`
* *Risk/State:* `state_mutation: 216`, `duplicate_logic: 58`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `immutability_locks: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.047
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.027554
  * `Imports (Out-Degree: 2):` agg_basics.h, agg_gamma_lut.h, math.h
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_span_image_filter_rgb.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 844.42 | **LOC:** 862 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.7168%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate` **(Many-Argument Workhorses)** (Impact: 83.4)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 37.7)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 37.7)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 567
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 127`, `func_start: 23`, `class_start: 7`
* *Risk/State:* `state_mutation: 307`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` agg_basics.h, agg_color_rgba.h, agg_span_image_filter.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_base.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 806.24 | **LOC:** 732 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.9321%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blend_from_color` **(Many-Argument Workhorses)** (Impact: 30.0)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_from_lut` **(Many-Argument Workhorses)** (Impact: 30.0)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_from` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* //--------------------------------------------------------------------
  * `clip_rect_area` **(Many-Argument Workhorses)** (Impact: 26.7)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_color_hspan` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 103`, `args: 23`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 139`, `dead_code: 1`
* *Architecture:* `api: 28`, `import: 2`
* *Defense:* `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.652
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.012887
  * `Imports (Out-Degree: 2):` agg_basics.h, agg_rendering_buffer.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/src/path_converters.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 747.8 | **LOC:** 1169 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.1517%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `vertex` **(Compute Cores)** (Impact: 82.5)
  * `vertex` **(Many-Argument Workhorses)** (Impact: 79.6)
  * `vertex` **(Compute Cores)** (Impact: 59.2)
  * `should_snap` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `draw_clipped_line` **(Many-Argument Workhorses)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 340
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 91`, `args: 25`, `func_start: 33`, `class_start: 9`
* *Risk/State:* `state_mutation: 142`, `dead_code: 6`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `doc: 4`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.765
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.004137
  * `Imports (Out-Degree: 3):` agg_clip_liang_barsky.h, agg_conv_segmentator.h, cmath, cstdint, limits, mplutils.h, pybind11.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/src/platform/AmigaOS/agg_platform_support.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 672.8 | **LOC:** 978 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.7688%), Tech Debt (81.5737%)
**Top Internal Functions/Classes:**
  * `handle_idcmp` **(Many-Argument Workhorses)** (Impact: 204.2)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_specific::load_img` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_specific::platform_specific` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::init` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_specific::handle_input` **(I/O & Config Routines)** (Impact: 12.7)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 57`, `args: 50`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 77`, `dead_code: 1`, `unreferenced_by_name: 32`
* *Architecture:* `api: 2`, `import: 15`
* *Defense:* `sync_locks: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` requester.h, window.h, cstring, pictureclass.h, agg_platform_support.h, Picasso96API.h, datatypes.h, dos.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_pixfmt_rgb.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 660.18 | **LOC:** 995 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.7864%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blend_from` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* //-------------------------------------------------------------------- // Blend from an RGBA surface...
  * `blend_color_hspan` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_color_vspan` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_from_lut` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* //-------------------------------------------------------------------- // Blend from color table, us...
  * `blend_hline` **(Many-Argument Workhorses)** (Impact: 23.5)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 248`, `args: 36`, `func_start: 71`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 89`
* *Architecture:* `api: 35`, `import: 3`
* *Defense:* `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.002068
  * `Imports (Out-Degree: 2):` agg_pixfmt_base.h, agg_rendering_buffer.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/src/platform/mac/agg_platform_support.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 658.22 | **LOC:** 1053 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.8732%), Tech Debt (87.1665%)
**Top Internal Functions/Classes:**
  * `platform_specific::load_pmap` **(Compute Cores)** (Impact: 163.3)
    * *Intent:* //------------------------------------------------------------------------
  * `DoKeyDown` **(Many-Argument Workhorses)** (Impact: 47.8)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_specific::save_pmap` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_specific::platform_specific` **(Many-Argument Workhorses)** (Impact: 31.0)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_specific::display_pmap` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 74`, `args: 64`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 80`, `dead_code: 1`, `unreferenced_by_name: 32`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carbon.h, console.h, agg_platform_support.h, agg_mac_pmap.h, string.h, unistd.h, agg_color_conv_rgb8.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_array.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 648.98 | **LOC:** 1120 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1844%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `quick_sort` **(Compute Cores)** (Impact: 46.7)
    * *Intent:* //--------------------------------------------------------------quick_sort
  * `binary_search_pos` **(Many-Argument Workhorses)** (Impact: 15.2)
    * *Intent:* //------------------------------------------------------binary_search_pos
  * `deserialize` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `allocate` **(Compute Cores)** (Impact: 10.1)
  * `remove_duplicates` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* //------------------------------------------------------remove_duplicates // Remove duplicates from ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 256`, `args: 127`, `func_start: 111`, `class_start: 9`
* *Risk/State:* `state_mutation: 137`, `dead_code: 2`, `duplicate_logic: 47`
* *Architecture:* `api: 30`, `import: 3`
* *Defense:* `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.266
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.053423
  * `Imports (Out-Degree: 1):` agg_basics.h, stddef.h, string.h
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_scanline.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 639.34 | **LOC:** 853 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.5036%), Tech Debt (89.1606%)
**Top Internal Functions/Classes:**
  * `render_scanlines_compound` **(Many-Argument Workhorses)** (Impact: 104.5)
    * *Intent:* //=============================================render_scanlines_compound
  * `render_scanlines_compound_layered` **(Many-Argument Workhorses)** (Impact: 82.6)
    * *Intent:* //=======================================render_scanlines_compound_layered
  * `render_scanlines_aa_solid` **(Many-Argument Workhorses)** (Impact: 20.3)
    * *Intent:* //===============================================render_scanlines_aa_solid
  * `render_scanlines_bin_solid` **(Many-Argument Workhorses)** (Impact: 17.7)
    * *Intent:* //==============================================render_scanlines_bin_solid
  * `render_scanline_aa` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* //======================================================render_scanline_aa
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 150`, `args: 16`, `func_start: 36`, `class_start: 20`
* *Risk/State:* `state_mutation: 107`, `dead_code: 8`, `duplicate_logic: 12`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `immutability_locks: 21`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.357
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.012249
  * `Imports (Out-Degree: 2):` agg_basics.h, agg_renderer_base.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_span_image_filter_gray.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 612.88 | **LOC:** 732 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate` **(Many-Argument Workhorses)** (Impact: 80.8)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 28.1)
    * *Intent:* //--------------------------------------------------------------------
  * `generate` **(Many-Argument Workhorses)** (Impact: 12.4)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 105 instances
* *State Mutation (weighted view):* 375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 113`, `func_start: 23`, `class_start: 7`
* *Risk/State:* `state_mutation: 165`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.609
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.003232
  * `Imports (Out-Degree: 3):` agg_basics.h, agg_color_gray.h, agg_span_image_filter.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/src/ft2font.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 593.54 | **LOC:** 753 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.2002%), Tech Debt (98.5436%)
**Top Internal Functions/Classes:**
  * `FT2Font::load_char` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `FT2Font::load_char_with_fallback` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `FT2Font::set_text` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `FT2Image::draw_bitmap` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `FT2Font::get_glyph_name` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 279
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 52`, `args: 48`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 121`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 24`
* *Architecture:* `import: 10`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` algorithm, cstdio, ft2font.h, iterator, mplutils.h, set, sstream, stdexcept...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/src/platform/sdl/agg_platform_support.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 591.66 | **LOC:** 709 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (92.8387%)
**Top Internal Functions/Classes:**
  * `platform_specific::platform_specific` **(Many-Argument Workhorses)** (Impact: 65.7)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::run` **(Compute Cores)** (Impact: 64.0)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::init` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::load_img` **(Compute Cores)** (Impact: 16.8)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::create_img` **(Many-Argument Workhorses)** (Impact: 11.7)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 36`, `args: 19`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 131`, `dead_code: 1`, `unreferenced_by_name: 28`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` SDL.h, SDL_byteorder.h, agg_platform_support.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_pixfmt_rgb_packed.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 583.18 | **LOC:** 1313 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.4483%), Tech Debt (99.9883%)
**Top Internal Functions/Classes:**
  * `blend_from` **(Many-Argument Workhorses)** (Impact: 24.7)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_hline` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_vline` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_from_color` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* //--------------------------------------------------------------------
  * `blend_from_lut` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 267`, `args: 41`, `func_start: 103`, `class_start: 25`
* *Risk/State:* `state_mutation: 85`, `duplicate_logic: 42`, `unreferenced_by_name: 18`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.532
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` agg_basics.h, agg_color_rgba.h, agg_rendering_buffer.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `matplotlib-3.10.8/extern/agg24-svn/include/agg_basics.h` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 96.2713%)
- `matplotlib-3.10.8/src/_backend_agg.h` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 96.196%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_color_rgba.h` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 99.9999%)
- `matplotlib-3.10.8/extern/agg24-svn/include/ctrl/agg_ctrl.h` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 99.8989%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_math_stroke.h` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 99.9955%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `matplotlib-3.10.8/galleries/tutorials/pyplot.py` -> **Severity: 41.865** (Embedded: 0.5688 * Error Risk: 73.6034%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_basics.h` -> **Severity: 9.202** (Embedded: 0.1274 * Error Risk: 72.2221%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_array.h` -> **Severity: 4.867** (Embedded: 0.0534 * Error Risk: 91.1039%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_math.h` -> **Severity: 2.915** (Embedded: 0.0328 * Error Risk: 88.8777%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_color_rgba.h` -> **Severity: 2.556** (Embedded: 0.0276 * Error Risk: 92.7721%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `matplotlib-3.10.8/galleries/tutorials/pyplot.py` -> **Severity: 24556.8** (Blast Radius: 245.568 * Doc Risk: 100.0%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_basics.h` -> **Severity: 7184.8** (Blast Radius: 71.848 * Doc Risk: 100.0%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_array.h` -> **Severity: 1626.6** (Blast Radius: 16.266 * Doc Risk: 100.0%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_math.h` -> **Severity: 672.6** (Blast Radius: 6.726 * Doc Risk: 100.0%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_trans_affine.h` -> **Severity: 581.4** (Blast Radius: 5.814 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
