# ARCHITECTURAL_BRIEF: coverage
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
| Total Artifacts | 312 |
| Analyzed Artifacts (Scanned) | 218 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 94 |
| Total LOC | 27085 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4411 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5292 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7329 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 118 | 17381 | 54.1% |
| HTML | 67 | 8171 | 30.7% |
| PLAINTEXT | 13 | 0 | 6.0% |
| M4 | 8 | 61 | 3.7% |
| CSS | 4 | 465 | 1.8% |
| MAKEFILE | 2 | 248 | 0.9% |
| SHELL | 2 | 50 | 0.9% |
| JAVASCRIPT | 2 | 708 | 0.9% |
| XML | 1 | 0 | 0.5% |
| BINARY_THREAT | 1 | 1 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 204 | 93.6% |
| Unknown | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 6.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 94*

**Composition by Extension & Reason:**
- `.rst`: 41x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 13x Excluded (Unsupported Extension: 'no_extension'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.pip`: 9x Excluded (Unsupported Extension: '.pip')
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.html`: 1x Excluded (Saturation: Line 88 exceeds 500 chars), 1x Packed Payload Guard (Impossible Density: 4.43 hits/line), 1x Packed Payload Guard (Impossible Density: 4.44 hits/line)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.xml`: 1x Excluded (Machine-Generated Source Code Signature: 23 LOC), 1x Excluded (Machine-Generated Source Code Signature: 25 LOC)
- `.tok`: 2x Excluded (Unsupported Extension: '.tok')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 261 LOC)
- `.dtd`: 1x Excluded (Unsupported Extension: '.dtd')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.6 | 7.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 30.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 95.1 | 1.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 96.3 | 8.6 | 10.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.2 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 70.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.8 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 26.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 222 | 45 | 3 | `coverage-7.13.5/tests/test_api.py` |
| cleanup | 32 | 3 | 0 | `coverage-7.13.5/Makefile` |
| guards | 1725 | 67 | 25 | `coverage-7.13.5/tests/test_report.py` |
| danger | 376 | 62 | 5 | `coverage-7.13.5/tests/test_json.py` |
| concurrency | 121 | 83 | 1 | `coverage-7.13.5/tests/test_concurrency.py` |
| connectivity | 2794 | 139 | 23 | `coverage-7.13.5/tests/test_arcs.py` |
| io | 2268 | 131 | 31 | `coverage-7.13.5/tests/gold/html/omit_1/main_py.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 28 | 9 | 0 | `coverage-7.13.5/tests/test_concurrency.py` |
| time | 15 | 7 | 0 | `coverage-7.13.5/tests/test_concurrency.py` |
| serialization | 17 | 6 | 0 | `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` |
| regex | 65 | 25 | 1 | `coverage-7.13.5/tests/test_process.py` |
| events | 88 | 70 | 1 | `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` |
| tests | 1722 | 48 | 23 | `coverage-7.13.5/tests/test_data.py` |
| docs | 1522 | 145 | 15 | `coverage-7.13.5/tests/test_arcs.py` |
| debt | 271 | 58 | 4 | `coverage-7.13.5/igor.py` |
| mutation | 10607 | 161 | 103 | `coverage-7.13.5/tests/test_data.py` |
| dead_code | 1203 | 54 | 14 | `coverage-7.13.5/tests/test_arcs.py` |
| credential | 2 | 2 | 0 | `coverage-7.13.5/Makefile` |
| threat | 25 | 14 | 0 | `coverage-7.13.5/tests/helpers.py` |
| ml_ai | 12 | 7 | 0 | `coverage-7.13.5/tests/test_oddball.py` |
| ui | 371 | 73 | 6 | `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `coverage-7.13.5/tests/gold/html/omit_1/main_py.html` (Hits: 41)
- `coverage-7.13.5/tests/gold/html/omit_2/main_py.html` (Hits: 41)
- `coverage-7.13.5/tests/gold/html/omit_3/main_py.html` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **coverage_html_cb_bcae5fc4.js** (`coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js`) — 45 inbound connections
2. **coveragetest.py** (`coverage-7.13.5/tests/coveragetest.py`) — 40 inbound connections
3. **coverage.css** (`coverage-7.13.5/doc/_static/coverage.css`) — 40 inbound connections
4. **pytest.in** (`coverage-7.13.5/requirements/pytest.in`) — 36 inbound connections
5. **helpers.py** (`coverage-7.13.5/tests/helpers.py`) — 27 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_process.py** (`coverage-7.13.5/tests/test_process.py`) — 42 outbound dependencies
2. **test_report.py** (`coverage-7.13.5/tests/test_report.py`) — 38 outbound dependencies
3. **test_html.py** (`coverage-7.13.5/tests/test_html.py`) — 35 outbound dependencies
4. **test_api.py** (`coverage-7.13.5/tests/test_api.py`) — 32 outbound dependencies
5. **test_concurrency.py** (`coverage-7.13.5/tests/test_concurrency.py`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `one_file` (@ `coverage-7.13.5/lab/parser.py`) -> Impact: **51.4** | LOC: 67
  * *Intent:* """Process just one file."""
- `_make_summary` (@ `coverage-7.13.5/tests/test_json.py`) -> Impact: **48.5** | LOC: 65
- `check_coverage` (@ `coverage-7.13.5/tests/coveragetest.py`) -> Impact: **40.8** | LOC: 86
- `should_skip` (@ `coverage-7.13.5/igor.py`) -> Impact: **34.7** | LOC: 35
  * *Intent:* """Is there a reason to skip these tests? Return empty string to run tests, or a message about why we are skipping the tests. """
- `assert_warnings` (@ `coverage-7.13.5/tests/coveragetest.py`) -> Impact: **32.2** | LOC: 62
- `test_if_else` (@ `coverage-7.13.5/tests/test_templite.py`) -> Impact: **31.2** | LOC: 31
- `compare` (@ `coverage-7.13.5/tests/goldtest.py`) -> Impact: **30.9** | LOC: 80
- `arc_ascii_art` (@ `coverage-7.13.5/lab/parser.py`) -> Impact: **29.6** | LOC: 38
  * *Intent:* """Draw arcs as ascii art. Returns a dictionary mapping line numbers to ascii strings to draw for that line. """
- `wire_up_filter` (@ `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js`) -> Impact: **29.6** | LOC: 132
  * *Intent:* // Create the events for the filter box.
- `show_code` (@ `coverage-7.13.5/lab/show_pyc.py`) -> Impact: **28.8** | LOC: 55
  * *Intent:* # fmt: on

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `coverage-7.13.5/tests` | 55 | 9557.6 | 11.28% | 0.0% |
| `coverage-7.13.5/lab` | 17 | 1107.92 | 33.03% | 10.4% |
| `coverage-7.13.5` | 10 | 1080.4 | 5.65% | 6.83% |
| `coverage-7.13.5/tests/gold/html/support` | 2 | 512.15 | 48.1% | 0.0% |
| `coverage-7.13.5/ci` | 5 | 253.16 | 26.96% | 0.0% |
| `coverage-7.13.5/tests/js` | 2 | 111.34 | 3.49% | 0.0% |
| `coverage-7.13.5/requirements` | 7 | 92.44 | 0.0% | 0.0% |
| `coverage-7.13.5/doc` | 4 | 75.3 | 6.62% | 21.26% |
| `coverage-7.13.5/tests/modules/pkg1` | 6 | 75.28 | 0.0% | 0.0% |
| `coverage-7.13.5/tests/modules/pkg1/sub` | 4 | 47.16 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `coverage-7.13.5/lab/hack_pyc.py` -> **95.1142%** Exposure
- `coverage-7.13.5/doc/cog_helpers.py` -> **85.0342%** Exposure
- `coverage-7.13.5/lab/extract_code.py` -> **81.7574%** Exposure
- `coverage-7.13.5/igor.py` -> **68.2881%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `coverage-7.13.5/ci/comment_on_fixes.py` -> **100.0%** Exposure
- `coverage-7.13.5/ci/update_rtfd.py` -> **100.0%** Exposure
- `coverage-7.13.5/igor.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/goals.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/hack_pyc.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `coverage-7.13.5/tests/test_arcs.py` -> **112** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_data.py` -> **80** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_api.py` -> **79** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_coverage.py` -> **71** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_process.py` -> **70** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1049` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `coverage-7.13.5/lab/show_pyc.py` (PYTHON) -> Cumulative Risk: **594.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 152.56 | **LOC:** 218 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (91.5898%)
- **Heaviest Functions:** `show_code` (Impact: 28.8), `lnotab_interpreted` (Impact: 9.4), `show_hex` (Impact: 8.4)

### 2. `coverage-7.13.5/lab/hack_pyc.py` (PYTHON) -> Cumulative Risk: **581.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 96.58 | **LOC:** 99 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2608%), Tech Debt (95.1142%)
- **Heaviest Functions:** `hack_line_numbers` (Impact: 15.5), `read` (Impact: 3.8), `write` (Impact: 3.8)

### 3. `coverage-7.13.5/igor.py` (PYTHON) -> Cumulative Risk: **544.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 392.74 | **LOC:** 555 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.7502%), Verification (80.0%)
- **Heaviest Functions:** `should_skip` (Impact: 34.7), `run_tests_with_coverage` (Impact: 13.3), `main` (Impact: 11.2)

### 4. `coverage-7.13.5/lab/warn_executed.py` (PYTHON) -> Cumulative Risk: **535.44**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 169.48 | **LOC:** 214 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6882%), Verification (80.0%)
- **Heaviest Functions:** `find_not_partial_lines` (Impact: 28.5), `analyze_warnings` (Impact: 14.4), `find_executed_excluded_lines` (Impact: 7.8)

### 5. `coverage-7.13.5/lab/goals.py` (PYTHON) -> Cumulative Risk: **522.97**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 88.84 | **LOC:** 101 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.2963%)
- **Heaviest Functions:** `main` (Impact: 27.9), `select_files` (Impact: 5.4), `total_for_files` (Impact: 4.2)

### 6. `coverage-7.13.5/lab/select_contexts.py` (PYTHON) -> Cumulative Risk: **513.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 50.94 | **LOC:** 67 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.5578%)
- **Heaviest Functions:** `main` (Impact: 25.0)

### 7. `coverage-7.13.5/lab/run_sysmon.py` (PYTHON) -> Cumulative Risk: **501.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 72.8 | **LOC:** 120 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9959%), Safety Score (94.5628%), Documentation (91.6667%)
- **Heaviest Functions:** `show_off_off` (Impact: 4.8), `bytes_to_lines` (Impact: 4.6), `show_off` (Impact: 4.2)

### 8. `coverage-7.13.5/lab/parser.py` (PYTHON) -> Cumulative Risk: **479.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 283.74 | **LOC:** 221 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2203%), Verification (80.0%)
- **Heaviest Functions:** `one_file` (Impact: 51.4), `arc_ascii_art` (Impact: 29.6), `main` (Impact: 16.9)

### 9. `coverage-7.13.5/lab/run_trace.py` (PYTHON) -> Cumulative Risk: **478.56**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 25.76 | **LOC:** 45 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9665%), Safety Score (94.329%)
- **Heaviest Functions:** `trace` (Impact: 11.2)

### 10. `coverage-7.13.5/doc/cog_helpers.py` (PYTHON) -> Cumulative Risk: **462.76**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 44.58 | **LOC:** 107 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9972%), Safety Score (85.3463%), Tech Debt (85.0342%)
- **Heaviest Functions:** `show_configs` (Impact: 12.2), `_read_config` (Impact: 8.1), `show_help` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `coverage-7.13.5/tests/test_data.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 679.28 | **LOC:** 1130 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.9813%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_data_files` (Impact: 14.9)
    * *Intent:* """Make a number data files. `spec` is a string dictating the data for each file. Same characters in...
  * `test_update_conflicting_file_tracers` (Impact: 7.9)
  * `test_update_file_tracer_vs_no_file_tracer` (Impact: 7.8)
  * `test_thread_stress` (Impact: 6.6)
  * `test_meta_data` (Impact: 5.2)
    * *Intent:* # TODO: do we care about this? # The metadata written to the data file shouldn't interfere with # ha...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *Amplified Sql Injection:* 2 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 225`, `args: 89`, `func_start: 88`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 221`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 80`
* *Architecture:* `io: 8`, `api: 93`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 66`, `doc: 14`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, collections.abc, coverage.data, coverage.exceptions, coverage.files, coverage.types, gc, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 590.82 | **LOC:** 1661 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clean_files` (Impact: 10.5)
    * *Intent:* """Remove names matching `pats` from `files`, a list of file names."""
  * `test_combining_bad_data` (Impact: 7.0)
    * *Intent:* # If you try to combine a bad data file, then you will get a warning, # and the file will remain. se...
  * `test_moving_stuff` (Impact: 5.1)
    * *Intent:* # When using absolute file names, moving the source around results in # "No source for code" errors ...
  * `test_switch_context_unstarted` (Impact: 4.8)
    * *Intent:* # Coverage must be started to switch context msg = "Cannot switch context, coverage is not started" ...
  * `test_combine_no_usable_files` (Impact: 4.4)
    * *Intent:* # https://github.com/coveragepy/coveragepy/issues/629 self.make_b_or_c_py() self.make_data_file(".co...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 339`, `args: 99`, `func_start: 99`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 161`, `unreferenced_by_name: 79`
* *Architecture:* `io: 40`, `api: 113`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 114`, `doc: 70`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, b, collections.abc, colorsys, coverage, coverage.data, coverage.exceptions, coverage.files...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_html.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 560.54 | **LOC:** 1573 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.338%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_valid_hrefs` (Impact: 11.5)
    * *Intent:* """Assert that the hrefs in htmlcov/*.html are valid. Doesn't check external links (those with a pro...
  * `test_dynamic_contexts` (Impact: 9.4)
  * `test_dynamic_contexts_relative_files` (Impact: 9.3)
  * `handle_starttag` (Impact: 8.7)
  * `assert_htmlcov_files_exist` (Impact: 8.0)
    * *Intent:* """Assert that all the expected htmlcov files exist."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 312`, `args: 83`, `func_start: 83`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 4`, `state_mutation: 146`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 63`
* *Architecture:* `io: 34`, `api: 91`, `import: 25`
* *Defense:* `safety: 64`, `doc: 67`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` __future__, collections, coverage, coverage.exceptions, coverage.files, coverage.html, coverage.report_core, coverage.types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_concurrency.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 512.26 | **LOC:** 865 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_thread_safe_save_data` (Impact: 18.4)
    * *Intent:* # Non-regression test for: https://github.com/coveragepy/coveragepy/issues/581 # Create some Python ...
  * `cant_trace_msg` (Impact: 16.7)
    * *Intent:* """What might coverage.py say about a concurrency setting and imported module?"""
  * `try_some_code` (Impact: 12.1)
  * `measurable_line` (Impact: 7.7)
    * *Intent:* """Is this a line of code coverage will measure? Not blank, not a comment, and not "else" """
  * `test_multiprocessing_simple` (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 141`, `args: 38`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 107`, `unreferenced_by_name: 29`
* *Architecture:* `io: 8`, `api: 42`, `concurrency: 17`, `import: 25`
* *Defense:* `safety: 42`, `doc: 40`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, collections.abc, coverage, coverage.data, coverage.exceptions, coverage.files, coverage.misc, coverage.sqldata...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 505.46 | **LOC:** 736 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.6238%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wire_up_filter` (Impact: 29.6)
    * *Intent:* // Create the events for the filter box.
  * `sortColumn` (Impact: 19.6)
  * `select_line_or_chunk` (Impact: 13.2)
    * *Intent:* // Select line number lineno, or if it is in a colored chunk, select the // entire chunk
  * `getCellValue` (Impact: 11.0)
    * *Intent:* // Helpers for table sorting
  * `wire_up_sorting` (Impact: 10.8)
    * *Intent:* // Set up the click-to-sort columns.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 86 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 81`, `args: 55`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 115`
* *Architecture:* `io: 12`, `concurrency: 1`
* *Defense:* `safety: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 117.744
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.204545
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/a1_coverage.pth` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 496.7 | **LOC:** 1772 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.8804%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pth_and_source_work_together` (Impact: 13.5)
  * `fullname` (Impact: 6.0)
    * *Intent:* """What is the full module name for `modname` for this test?"""
  * `assert_pydoc_ok` (Impact: 4.5)
    * *Intent:* """Check that pydoc of `name` finds the docstring from `thing`."""
  * `test_aliases_used_in_messages` (Impact: 3.7)
  * `test_warns_if_never_run` (Impact: 3.6)
    * *Intent:* # Note: the name of the function can't have "warning" in it, or the # absolute path of the file will...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 307`, `args: 78`, `func_start: 78`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 151`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 70`
* *Architecture:* `io: 38`, `api: 90`, `import: 24`
* *Defense:* `safety: 149`, `doc: 85`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __future__, coverage, coverage.cmdline, coverage.data, coverage.files, coverage.sqldata, covmod1, covmodzip1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/igor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 392.74 | **LOC:** 555 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2125%), Tech Debt (68.2881%)
**Top Internal Functions/Classes:**
  * `should_skip` (Impact: 34.7)
    * *Intent:* """Is there a reason to skip these tests? Return empty string to run tests, or a message about why w...
  * `run_tests_with_coverage` (Impact: 13.3)
    * *Intent:* """Run tests, but with coverage."""
  * `main` (Impact: 11.2)
    * *Intent:* """Main command-line execution for igor. Verbs are taken from the command line, and extra words take...
  * `message` (Impact: 10.8)
    * *Intent:* """All messages come through here, keep the data we want."""
  * `do_test_with_core` (Impact: 9.5)
    * *Intent:* """Run tests with a particular core."""
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 87`, `args: 25`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 99`, `unreferenced_by_name: 11`
* *Architecture:* `io: 37`, `api: 24`, `import: 22`
* *Defense:* `safety: 8`, `doc: 28`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` coverage, coverage.html, coverage.version, datetime, glob, inspect, itertools, of...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_cmdline.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 389.2 | **LOC:** 1664 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3718%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mock_command_line` (Impact: 13.5)
  * `command_line` (Impact: 11.2)
    * *Intent:* """Stub for command_line, the arg determines what it will do."""
  * `cmd_executes` (Impact: 11.1)
  * `cmd_help` (Impact: 8.3)
  * `test_fail_under` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 13
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 204`, `args: 73`, `func_start: 71`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 3`, `state_mutation: 72`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 53`
* *Architecture:* `io: 5`, `api: 79`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 70`, `doc: 119`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, ast, collections.abc, coverage, coverage.cmdline, coverage.config, coverage.control, coverage.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_report.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 382.94 | **LOC:** 1298 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.312%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_rigged_file` (Impact: 5.1)
    * *Intent:* """Create a file that will have specific results. `stmts` and `miss` are ints, the number of stateme...
  * `get_summary_text` (Impact: 4.4)
    * *Intent:* """Get text output from the SummaryReporter. The arguments are tuples: (name, value) for Coverage.se...
  * `test_dotpy_not_python_ignored` (Impact: 4.2)
    * *Intent:* # We run a Python file, and when reporting, we can't parse it as Python, # but we've said to ignore ...
  * `test_test_data` (Impact: 4.0)
    * *Intent:* # We use our own test files as test data. Check that our assumptions # about them are still valid. W...
  * `test_dotpy_not_python` (Impact: 3.4)
    * *Intent:* # We run a .py file, and when reporting, we can't parse it as Python. # We should get an error messa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 277`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 134`, `fragile_debt: 3`, `unreferenced_by_name: 55`
* *Architecture:* `io: 4`, `api: 66`, `import: 22`
* *Defense:* `safety: 154`, `doc: 52`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __future__, a, also_not_run, coverage, coverage.control, coverage.data, coverage.exceptions, coverage.files...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/coveragetest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 370.88 | **LOC:** 527 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.049%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_coverage` (Impact: 40.8)
  * `assert_warnings` (Impact: 32.2)
  * `make_data_file` (Impact: 16.9)
  * `run_command_status` (Impact: 11.0)
    * *Intent:* """Run the command-line `cmd` in a subprocess, and print its output. Use this when you need to test ...
  * `get_report` (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 109`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 70`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 12`, `api: 31`, `import: 24`
* *Defense:* `safety: 26`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.182
  * `Choke Point (Betweenness):` 0.001494 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 3):` __future__, a, as, collections, collections.abc, contextlib, coverage, coverage.cmdline...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/tests/test_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 360.22 | **LOC:** 1142 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.4116%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_config_settings_are_correct` (Impact: 9.3)
    * *Intent:* """Check that `cov` has all the settings from LOTSA_SETTINGS."""
  * `test_tweak_error_checking` (Impact: 7.6)
    * *Intent:* # Trying to set an unknown config value raises an error. cov = coverage.Coverage() with pytest.raise...
  * `test_tweak_plugin_options` (Impact: 4.9)
    * *Intent:* # Plugin options have a more flexible syntax. cov = coverage.Coverage() cov.set_option("run:plugins"...
  * `test_toml_parse_errors` (Impact: 4.7)
    * *Intent:* # Im-parsable values raise ConfigError, with details. self.make_file(filename, bad_config) with pyte...
  * `test_core_option` (Impact: 4.7)
    * *Intent:* # Test that the core option can be set in the configuration file. self.del_environ("COVERAGE_CORE") ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 251`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 80`, `unreferenced_by_name: 56`
* *Architecture:* `io: 8`, `api: 66`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 128`, `doc: 56`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, coverage, coverage.config, coverage.exceptions, coverage.tomlconfig, coverage.types, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_plugins.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 351.16 | **LOC:** 1334 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.8838%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_bad_plugin` (Impact: 26.3)
  * `run_all_functions` (Impact: 6.6)
    * *Intent:* """Run all functions in `suite_name` under coverage."""
  * `get_plugin_options` (Impact: 5.5)
    * *Intent:* """Just return the options for `plugin` if this is the right module."""
  * `test_exception_if_plugins_on_pytracer` (Impact: 5.1)
  * `test_plugin2_with_xml_report` (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 197`, `args: 55`, `func_start: 55`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 88`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 41`
* *Architecture:* `io: 5`, `api: 64`, `import: 20`
* *Defense:* `safety: 75`, `doc: 59`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, another, collections.abc, coverage, coverage.data, coverage.exceptions, coverage.misc, coverage.plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_arcs.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 350.32 | **LOC:** 2425 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.7389%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pathologically_long_code_object` (Impact: 4.7)
    * *Intent:* # https://github.com/coveragepy/coveragepy/issues/359 # Long code objects sometimes cause problems. ...
  * `test_exception_group` (Impact: 4.6)
    * *Intent:* # PyPy3.11 traces this incorrectly: https://github.com/pypy/pypy/issues/5354 if env.PYPY: missing = ...
  * `test_zero_coverage_while_loop` (Impact: 1.7)
    * *Intent:* # https://github.com/coveragepy/coveragepy/issues/502 self.make_file("main.py", "print('done')") sel...
  * `test_bug_212` (Impact: 1.7)
    * *Intent:* # "except Exception as e" is crucial here. # Bug 212 said that the "if exc" line was incorrectly mar...
  * `test_bug_324` (Impact: 1.7)
    * *Intent:* # This code is tricky: the list() call pulls all the values from gen(), # but each of them is a gene...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 179`, `args: 112`, `func_start: 112`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 22`, `fragile_debt: 1`, `unreferenced_by_name: 112`
* *Architecture:* `io: 1`, `api: 127`, `import: 11`
* *Defense:* `safety: 31`, `doc: 158`, `test: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, asyncio, contextlib, coverage, coverage.data, coverage.files, coverage.python, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 332.88 | **LOC:** 1323 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.3214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_line_endings` (Impact: 4.9)
  * `test_fuzzed_double_parse` (Impact: 4.8)
    * *Intent:* # https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=50381 # The second parse used to raise `Type...
  * `test_os_error` (Impact: 4.5)
  * `test_not_python` (Impact: 3.7)
  * `test_multiline_exclusion_match_all` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 222`, `args: 60`, `func_start: 60`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 115`, `fragile_debt: 1`, `unreferenced_by_name: 58`
* *Architecture:* `io: 1`, `api: 66`, `import: 11`
* *Defense:* `safety: 124`, `doc: 86`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, abc, ast, coverage, coverage.exceptions, coverage.parser, pytest, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_files.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 298.86 | **LOC:** 805 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.7211%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `globs_to_regex_params` (Impact: 11.6)
  * `assert_mapped` (Impact: 7.4)
    * *Intent:* """Assert that `inp` mapped through `aliases` produces `out`. If the aliases are not relative, then ...
  * `test_multiple_patterns` (Impact: 6.8)
    * *Intent:* # also test the debugfn... msgs: list[str] = [] aliases = PathAliases(debugfn=msgs.append, relative=...
  * `test_dot` (Impact: 5.8)
  * `test_globs_to_regex` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 111`, `args: 48`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `unreferenced_by_name: 41`
* *Architecture:* `io: 16`, `api: 52`, `import: 14`
* *Defense:* `safety: 25`, `doc: 13`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, collections.abc, coverage, coverage.exceptions, coverage.files, itertools, os, os.path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_json.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 291.58 | **LOC:** 567 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.1536%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_make_summary` (Impact: 48.5)
  * `_make_file_result` (Impact: 16.6)
  * `test_line_and_branch_coverage` (Impact: 12.7)
  * `test_regions` (Impact: 10.4)
  * `_make_region` (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 33`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 89`, `fragile_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 7`, `import: 9`
* *Defense:* `safety: 1`, `doc: 13`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, coverage, datetime, json, os, pytest, tests.coveragetest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/lab/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 283.74 | **LOC:** 221 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.6354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `one_file` (Impact: 51.4)
    * *Intent:* """Process just one file."""
  * `arc_ascii_art` (Impact: 29.6)
    * *Intent:* """Draw arcs as ascii art. Returns a dictionary mapping line numbers to ascii strings to draw for th...
  * `main` (Impact: 16.9)
    * *Intent:* """A main function for trying the code from the command line."""
  * `disassemble` (Impact: 15.3)
    * *Intent:* """Disassemble code, for ad-hoc experimenting."""
  * `first_all_blanks` (Impact: 7.6)
    * *Intent:* """Find the first position that is all blank in the strings ss."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 48`
* *Architecture:* `io: 1`, `api: 9`, `import: 11`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018182
  * `Imports (Out-Degree: 0):` collections, coverage.parser, coverage.python, dis, glob, optparse, os, re...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/tests/test_debug.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 274.78 | **LOC:** 512 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.8792%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_short_stack_full` (Impact: 8.0)
  * `test_debug_sys_ctracer` (Impact: 4.6)
  * `test_short_stack_frame_ids` (Impact: 4.6)
  * `test_debug_callers` (Impact: 3.6)
  * `test_short_filename` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 167`, `args: 48`, `func_start: 45`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 69`, `fragile_debt: 2`, `unreferenced_by_name: 34`
* *Architecture:* `io: 11`, `api: 50`, `import: 16`
* *Defense:* `safety: 74`, `doc: 18`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, ast, collections.abc, coverage, coverage.debug, coverage.exceptions, io, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_templite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 273.28 | **LOC:** 388 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.0812%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_if_else` (Impact: 31.2)
  * `test_malformed_else` (Impact: 17.3)
  * `test_if` (Impact: 16.9)
  * `test_malformed_for` (Impact: 14.5)
  * `test_malformed_if` (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 80`, `args: 37`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`, `unreferenced_by_name: 29`
* *Architecture:* `api: 37`, `import: 7`
* *Defense:* `safety: 6`, `doc: 9`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, coverage.templite, pytest, re, tests.coveragetest, types, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_xml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 252.34 | **LOC:** 616 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0411%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_tree` (Impact: 12.4)
    * *Intent:* """Make a tree of packages. Makes `width` directories, named d0 .. d{width-1}. Each directory has __...
  * `test_relative_source` (Impact: 9.3)
  * `package_and_class_tags` (Impact: 9.0)
    * *Intent:* """Run an XML report on `cov`, and get the package and class tags."""
  * `unbackslash` (Impact: 8.9)
    * *Intent:* """Find strings in `v`, and replace backslashes with slashes throughout."""
  * `assert_source` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 172`, `args: 39`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 71`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `io: 6`, `api: 44`, `import: 20`
* *Defense:* `safety: 37`, `doc: 25`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` , .subpackage, __future__, collections.abc, coverage, coverage.exceptions, coverage.files, coverage.misc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/helpers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 244.16 | **LOC:** 417 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.5302%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_file` (Impact: 27.7)
  * `re_lines` (Impact: 10.6)
    * *Intent:* """Return a list of lines selected by `pat` in the string `text`. If `match` is false, the selection...
  * `re_lines_text` (Impact: 10.2)
    * *Intent:* """Return the multi-line text of lines selected by `pat`."""
  * `arcz_to_arcs` (Impact: 10.2)
    * *Intent:* """Convert a compact textual representation of arcs to a list of pairs. The text has space-separated...
  * `assert_coverage_warnings` (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 23 instances
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 97`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 3`, `state_mutation: 42`, `dead_code: 1`
* *Architecture:* `io: 23`, `api: 23`, `import: 21`
* *Defense:* `safety: 18`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.926
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.144262
  * `Imports (Out-Degree: 1):` __future__, collections, collections.abc, contextlib, coverage, coverage.debug, coverage.exceptions, coverage.types...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/tests/test_testing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 226.62 | **LOC:** 494 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_same_python_executable` (Impact: 9.9)
    * *Intent:* """Determine if `e1` and `e2` refer to the same Python executable. Either path could include symboli...
  * `test_assert_warnings` (Impact: 9.5)
  * `test_file_count` (Impact: 8.6)
  * `test_re_lines_inverted` (Impact: 6.9)
  * `test_file_exists` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 147`, `args: 34`, `func_start: 34`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `planned_debt: 7`, `unreferenced_by_name: 29`
* *Architecture:* `io: 11`, `api: 40`, `import: 13`
* *Defense:* `safety: 22`, `doc: 15`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, coverage, coverage.exceptions, coverage.files, coverage.types, datetime, os, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_coverage.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 221.14 | **LOC:** 1860 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.4131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_attribute_annotation` (Impact: 4.5)
  * `test_no_data_to_report_on_annotate` (Impact: 3.1)
    * *Intent:* # Reporting with no data produces a nice message and no output # directory. with pytest.raises(NoDat...
  * `test_no_data_to_report_on_html` (Impact: 3.1)
    * *Intent:* # Reporting with no data produces a nice message and no output # directory. with pytest.raises(NoDat...
  * `test_no_data_to_report_on_xml` (Impact: 3.1)
    * *Intent:* # Reporting with no data produces a nice message. with pytest.raises(NoDataError, match="No data to ...
  * `test_failed_coverage` (Impact: 3.0)
    * *Intent:* # If the lines are wrong, the message shows right and wrong. with pytest.raises(AssertionError, matc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 99`, `args: 71`, `func_start: 71`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `unreferenced_by_name: 71`
* *Architecture:* `api: 81`, `import: 6`
* *Defense:* `safety: 1`, `doc: 130`, `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, coverage, coverage.exceptions, pytest, string, sys, tests.coveragetest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_context.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 188.04 | **LOC:** 312 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.7547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_combining_arc_contexts` (Impact: 10.6)
  * `test_combining_line_contexts` (Impact: 6.9)
  * `test_dynamic_alone` (Impact: 3.9)
  * `test_static_and_dynamic` (Impact: 3.9)
  * `get_qualname` (Impact: 3.5)
    * *Intent:* """Helper to return qualname_from_frame for the caller."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 88`, `args: 29`, `func_start: 29`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 40`, `duplicate_logic: 4`, `unreferenced_by_name: 16`
* *Architecture:* `io: 5`, `api: 37`, `import: 13`
* *Defense:* `safety: 16`, `doc: 8`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, coverage, coverage.context, coverage.data, coverage.types, inspect, os.path, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` -> **Severity: 18.861** (Embedded: 0.2045 * Error Risk: 92.2098%)
- `coverage-7.13.5/tests/coveragetest.py` -> **Severity: 16.261** (Embedded: 0.1818 * Error Risk: 89.4346%)
- `coverage-7.13.5/tests/helpers.py` -> **Severity: 13.84** (Embedded: 0.1443 * Error Risk: 95.9388%)
- `coverage-7.13.5/tests/mixins.py` -> **Severity: 6.503** (Embedded: 0.0978 * Error Risk: 66.5013%)
- `coverage-7.13.5/tests/js/tests.js` -> **Severity: 3.291** (Embedded: 0.0636 * Error Risk: 51.7136%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` -> **Severity: 11774.4** (Blast Radius: 117.744 * Doc Risk: 100.0%)
- `coverage-7.13.5/tests/js/tests.js` -> **Severity: 1269.2** (Blast Radius: 12.692 * Doc Risk: 100.0%)
- `coverage-7.13.5/tests/coveragetest.py` -> **Severity: 1060.821** (Blast Radius: 34.182 * Doc Risk: 31.0345%)
- `coverage-7.13.5/tests/helpers.py` -> **Severity: 1047.78** (Blast Radius: 34.926 * Doc Risk: 30.0%)
- `coverage-7.13.5/tests/modules/plugins/another.py` -> **Severity: 374.3** (Blast Radius: 3.743 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
